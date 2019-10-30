package dispatcher

import (
	"context"
	"fmt"
	"time"

	"github.com/containers-ai/alameda/ai-dispatcher/pkg/metrics"
	"github.com/containers-ai/alameda/ai-dispatcher/pkg/queue"
	datahub_v1alpha1 "github.com/containers-ai/api/alameda_api/v1alpha1/datahub"
	datahub_common "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/common"
	datahub_metrics "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/metrics"
	datahub_predictions "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/predictions"
	datahub_resources "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/resources"
	"github.com/golang/protobuf/jsonpb"
	"github.com/golang/protobuf/ptypes/duration"
	"github.com/golang/protobuf/ptypes/timestamp"
	"google.golang.org/grpc"
)

type nodeModelJobSender struct {
	datahubGrpcCn  *grpc.ClientConn
	modelMapper    *ModelMapper
	metricExporter *metrics.Exporter
}

func NewNodeModelJobSender(datahubGrpcCn *grpc.ClientConn, modelMapper *ModelMapper,
	metricExporter *metrics.Exporter) *nodeModelJobSender {
	return &nodeModelJobSender{
		datahubGrpcCn:  datahubGrpcCn,
		modelMapper:    modelMapper,
		metricExporter: metricExporter,
	}
}

func (sender *nodeModelJobSender) sendModelJobs(nodes []*datahub_resources.Node,
	queueSender queue.QueueSender, pdUnit string, granularity int64, predictionStep int64) {

	datahubServiceClnt := datahub_v1alpha1.NewDatahubServiceClient(sender.datahubGrpcCn)
	for _, node := range nodes {
		nodeName := node.GetName()
		lastPredictionMetrics, err := sender.getLastPrediction(datahubServiceClnt, node, granularity)
		if err != nil {
			scope.Infof("Get node %s last prediction failed: %s",
				nodeName, err.Error())
			continue
		}
		if lastPredictionMetrics == nil && err == nil {
			scope.Infof("No prediction found of node %s",
				nodeName)
		}

		sender.sendJobByMetrics(node, queueSender, pdUnit, granularity, predictionStep,
			datahubServiceClnt, lastPredictionMetrics)
	}
}

func (sender *nodeModelJobSender) sendJob(node *datahub_resources.Node, queueSender queue.QueueSender, pdUnit string,
	granularity int64, nodeInfo *modelInfo) {
	nodeName := node.GetName()
	dataGranularity := queue.GetGranularityStr(granularity)
	marshaler := jsonpb.Marshaler{}
	nodeStr, err := marshaler.MarshalToString(node)
	if err != nil {
		scope.Errorf("Encode pb message failed for node %s with granularity seconds %v. %s",
			node.GetName(), granularity, err.Error())
		return
	}
	if len(nodeInfo.ModelMetrics) > 0 && nodeStr != "" {
		jb := queue.NewJobBuilder(pdUnit, granularity, nodeStr)
		jobJSONStr, err := jb.GetJobJSONString()
		if err != nil {
			scope.Errorf(
				"Prepare model job payload failed for node %s with granularity seconds %v. %s",
				nodeName, granularity, err.Error())
			return
		}

		err = queueSender.SendJsonString(modelQueueName, jobJSONStr,
			fmt.Sprintf("%s/%v", nodeName, granularity))
		if err == nil {
			sender.modelMapper.AddModelInfo(pdUnit, dataGranularity, nodeInfo)
		} else {
			scope.Errorf(
				"Send model job payload failed for node %s with granularity seconds %v. %s",
				nodeName, granularity, err.Error())
		}
	}
}

func (sender *nodeModelJobSender) genNodeInfo(nodeName string,
	modelMetrics ...datahub_common.MetricType) *modelInfo {
	nodeInfo := new(modelInfo)
	nodeInfo.Name = nodeName
	nodeInfo.ModelMetrics = modelMetrics
	nodeInfo.SetTimeStamp(time.Now().Unix())
	return nodeInfo
}

func (sender *nodeModelJobSender) getLastPrediction(datahubServiceClnt datahub_v1alpha1.DatahubServiceClient,
	node *datahub_resources.Node, granularity int64) ([]*datahub_predictions.MetricData, error) {
	nodeName := node.GetName()
	nodePredictRes, err := datahubServiceClnt.ListNodePredictions(context.Background(),
		&datahub_predictions.ListNodePredictionsRequest{
			NodeNames:   []string{nodeName},
			Granularity: granularity,
			QueryCondition: &datahub_common.QueryCondition{
				Limit: 1,
				Order: datahub_common.QueryCondition_DESC,
				TimeRange: &datahub_common.TimeRange{
					Step: &duration.Duration{
						Seconds: granularity,
					},
				},
			},
		})
	if err != nil {
		return nil, err
	}
	if len(nodePredictRes.GetNodePredictions()) > 0 {
		lastNodePrediction := nodePredictRes.GetNodePredictions()[0]
		return lastNodePrediction.GetPredictedRawData(), nil
	}
	return nil, nil
}

func (sender *nodeModelJobSender) getQueryMetricStartTime(descNodePredictions []*datahub_predictions.NodePrediction) int64 {
	if len(descNodePredictions) > 0 {
		pdMDs := descNodePredictions[len(descNodePredictions)-1].GetPredictedRawData()
		for _, pdMD := range pdMDs {
			mD := pdMD.GetData()
			if len(mD) > 0 {
				return mD[len(mD)-1].GetTime().GetSeconds()
			}
		}
	}
	return 0
}

func (sender *nodeModelJobSender) sendJobByMetrics(node *datahub_resources.Node, queueSender queue.QueueSender,
	pdUnit string, granularity int64, predictionStep int64, datahubServiceClnt datahub_v1alpha1.DatahubServiceClient,
	lastPredictionMetrics []*datahub_predictions.MetricData) {
	nodeName := node.GetName()
	dataGranularity := queue.GetGranularityStr(granularity)
	queryCondition := &datahub_common.QueryCondition{
		Order: datahub_common.QueryCondition_DESC,
		TimeRange: &datahub_common.TimeRange{
			StartTime: &timestamp.Timestamp{
				Seconds: time.Now().Unix() - predictionStep*granularity,
			},
			Step: &duration.Duration{
				Seconds: granularity,
			},
		},
	}
	nowSeconds := time.Now().Unix()

	if len(lastPredictionMetrics) == 0 {
		nodeInfo := sender.genNodeInfo(nodeName,
			datahub_common.MetricType_CPU_USAGE_SECONDS_PERCENTAGE,
			datahub_common.MetricType_MEMORY_USAGE_BYTES)
		sender.sendJob(node, queueSender, pdUnit, granularity, nodeInfo)
		scope.Infof("No prediction metrics found of node %s",
			nodeName)
		return
	}

	for _, lastPredictionMetric := range lastPredictionMetrics {
		if len(lastPredictionMetric.GetData()) == 0 {
			nodeInfo := sender.genNodeInfo(nodeName,
				datahub_common.MetricType_CPU_USAGE_SECONDS_PERCENTAGE,
				datahub_common.MetricType_MEMORY_USAGE_BYTES)
			sender.sendJob(node, queueSender, pdUnit, granularity, nodeInfo)
			scope.Infof("No prediction metric %s found of node %s",
				lastPredictionMetric.GetMetricType().String(), nodeName)
			return
		} else {
			lastPrediction := lastPredictionMetric.GetData()[0]
			lastPredictionTime := lastPredictionMetric.GetData()[0].GetTime().GetSeconds()
			if lastPrediction != nil && lastPredictionTime <= nowSeconds {
				scope.Infof("node prediction %s is out of date due to last predict time is %v (current: %v)",
					nodeName, lastPredictionTime, nowSeconds)
			}
			if lastPrediction != nil && lastPredictionTime <= nowSeconds {
				nodeInfo := sender.genNodeInfo(nodeName,
					datahub_common.MetricType_CPU_USAGE_SECONDS_PERCENTAGE,
					datahub_common.MetricType_MEMORY_USAGE_BYTES)
				scope.Infof("send node %s model job due to no predict found or predict is out of date",
					nodeName)
				sender.sendJob(node, queueSender, pdUnit, granularity, nodeInfo)
				return
			}

			nodePredictRes, err := datahubServiceClnt.ListNodePredictions(context.Background(),
				&datahub_predictions.ListNodePredictionsRequest{
					NodeNames:      []string{nodeName},
					ModelId:        lastPrediction.GetModelId(),
					Granularity:    granularity,
					QueryCondition: queryCondition,
				})
			if err != nil {
				scope.Errorf("Get node %s Prediction with granularity %v for sending model job failed: %s",
					nodeName, granularity, err.Error())
				continue
			}
			nodePredictions := nodePredictRes.GetNodePredictions()
			queryStartTime := time.Now().Unix() - predictionStep*granularity
			firstPDTime := sender.getQueryMetricStartTime(nodePredictions)
			if firstPDTime > 0 {
				queryStartTime = firstPDTime
			}
			nodeMetricsRes, err := datahubServiceClnt.ListNodeMetrics(context.Background(),
				&datahub_metrics.ListNodeMetricsRequest{
					QueryCondition: &datahub_common.QueryCondition{
						Order: datahub_common.QueryCondition_DESC,
						TimeRange: &datahub_common.TimeRange{
							StartTime: &timestamp.Timestamp{
								Seconds: queryStartTime,
							},
							Step: &duration.Duration{
								Seconds: granularity,
							},
						},
					},
					NodeNames: []string{nodeName},
				})
			if err != nil {
				scope.Errorf("List nodes %s metric with granularity %v for sending model job failed: %s",
					nodeName, granularity, err.Error())
				continue
			}
			nodeMetrics := nodeMetricsRes.GetNodeMetrics()

			for _, nodeMetric := range nodeMetrics {
				metricData := nodeMetric.GetMetricData()
				for _, metricDatum := range metricData {
					mData := metricDatum.GetData()
					pData := []*datahub_predictions.Sample{}
					nodeInfo := sender.genNodeInfo(nodeName)
					for _, nodePrediction := range nodePredictions {
						predictRawData := nodePrediction.GetPredictedRawData()
						for _, predictRawDatum := range predictRawData {
							if metricDatum.GetMetricType() == predictRawDatum.GetMetricType() {
								pData = append(pData, predictRawDatum.GetData()...)
							}
						}
					}
					metricsNeedToModel, drift := DriftEvaluation(UnitTypeNode, metricDatum.GetMetricType(), granularity, mData, pData, map[string]string{
						"nodeName":          nodeName,
						"targetDisplayName": fmt.Sprintf("node %s", nodeName),
					}, sender.metricExporter)
					if drift {
						scope.Infof("export node %s drift counter with granularity %s",
							nodeName, dataGranularity)
						sender.metricExporter.AddNodeMetricDrift(nodeName, queue.GetGranularityStr(granularity), 1.0)
					}
					nodeInfo.ModelMetrics = append(nodeInfo.ModelMetrics, metricsNeedToModel...)
					isModeling := sender.modelMapper.IsModeling(pdUnit, dataGranularity, nodeInfo)
					if !isModeling || (isModeling && sender.modelMapper.IsModelTimeout(
						pdUnit, dataGranularity, nodeInfo)) {
						sender.sendJob(node, queueSender, pdUnit, granularity, nodeInfo)
					}
				}
			}
		}
	}
}
