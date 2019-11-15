package requests

import (
	DaoMetricTypes "github.com/containers-ai/alameda/datahub/pkg/dao/interfaces/metrics/types"
	FormatEnum "github.com/containers-ai/alameda/datahub/pkg/formatconversion/enumconv"
	FormatTypes "github.com/containers-ai/alameda/datahub/pkg/formatconversion/types"
	"github.com/containers-ai/alameda/datahub/pkg/kubernetes/metadata"
	ApiCommon "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/common"
	ApiMetrics "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/metrics"
	ApiResource "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/resources"
	"github.com/golang/protobuf/ptypes"
	"github.com/golang/protobuf/ptypes/duration"
	"github.com/golang/protobuf/ptypes/timestamp"
	"github.com/pkg/errors"
)

var MetricTypeNameMap = map[ApiCommon.MetricType]FormatEnum.MetricType{
	ApiCommon.MetricType_CPU_USAGE_SECONDS_PERCENTAGE: FormatEnum.MetricTypeCPUUsageSecondsPercentage,
	ApiCommon.MetricType_MEMORY_USAGE_BYTES:           FormatEnum.MetricTypeMemoryUsageBytes,
	ApiCommon.MetricType_POWER_USAGE_WATTS:            FormatEnum.MetricTypePowerUsageWatts,
	ApiCommon.MetricType_TEMPERATURE_CELSIUS:          FormatEnum.MetricTypeTemperatureCelsius,
	ApiCommon.MetricType_DUTY_CYCLE:                   FormatEnum.MetricTypeDutyCycle,
}

type CreateClusterMetricsRequestExtended struct {
	ApiMetrics.CreateClusterMetricsRequest
}

func (r *CreateClusterMetricsRequestExtended) Validate() error {
	for _, m := range r.GetClusterMetrics() {
		if m == nil || m.ObjectMeta == nil || m.ObjectMeta.Name == "" {
			return errors.Errorf(`must provide "Name" in ObjectMeta`)
		}
	}
	return nil
}

func (r *CreateClusterMetricsRequestExtended) ProduceMetrics() DaoMetricTypes.ClusterMetricMap {
	metricMap := DaoMetricTypes.NewClusterMetricMap()

	for _, clusterMetric := range r.GetClusterMetrics() {
		if clusterMetric == nil {
			continue
		}
		m := DaoMetricTypes.NewClusterMetric()
		m.ObjectMeta = NewObjectMeta(clusterMetric.GetObjectMeta())

		for _, data := range clusterMetric.GetMetricData() {
			metricType := MetricTypeNameMap[data.GetMetricType()]
			for _, sample := range data.GetData() {
				timestamp, err := ptypes.Timestamp(sample.GetTime())
				if err != nil {
					scope.Error(" failed: " + err.Error())
				}
				sample := FormatTypes.Sample{
					Timestamp: timestamp,
					Value:     sample.GetNumValue(),
				}
				m.AddSample(metricType, sample)
			}
		}

		metricMap.AddClusterMetric(m)
	}

	return metricMap
}

type CreateNodeMetricsRequestExtended struct {
	ApiMetrics.CreateNodeMetricsRequest
}

func (r *CreateNodeMetricsRequestExtended) Validate() error {
	return nil
}

func (r *CreateNodeMetricsRequestExtended) ProduceMetrics() DaoMetricTypes.NodeMetricMap {
	nodeMetricMap := DaoMetricTypes.NewNodeMetricMap()

	for _, node := range r.GetNodeMetrics() {
		nodeMetric := DaoMetricTypes.NewNodeMetric()
		nodeMetric.ObjectMeta = NewObjectMeta(node.GetObjectMeta())

		for _, data := range node.GetMetricData() {
			metricType := MetricTypeNameMap[data.GetMetricType()]
			for _, sample := range data.GetData() {
				timestamp, err := ptypes.Timestamp(sample.GetTime())
				if err != nil {
					scope.Error(" failed: " + err.Error())
				}
				sample := FormatTypes.Sample{
					Timestamp: timestamp,
					Value:     sample.GetNumValue(),
				}
				nodeMetric.AddSample(metricType, sample)
			}
		}

		nodeMetricMap.AddNodeMetric(nodeMetric)
	}

	return nodeMetricMap
}

type CreateNamespaceMetricsRequestExtended struct {
	ApiMetrics.CreateNamespaceMetricsRequest
}

func (r *CreateNamespaceMetricsRequestExtended) Validate() error {
	for _, m := range r.GetNamespaceMetrics() {
		if m == nil || m.ObjectMeta == nil || m.ObjectMeta.Name == "" || m.ObjectMeta.ClusterName == "" {
			return errors.Errorf(`must provide "Name" and "ClusterName" in ObjectMeta`)
		}
	}
	return nil
}

func (r *CreateNamespaceMetricsRequestExtended) ProduceMetrics() DaoMetricTypes.NamespaceMetricMap {
	metricMap := DaoMetricTypes.NewNamespaceMetricMap()

	for _, namespaceMetric := range r.GetNamespaceMetrics() {
		if namespaceMetric == nil {
			continue
		}
		m := DaoMetricTypes.NewNamespaceMetric()
		m.ObjectMeta = NewObjectMeta(namespaceMetric.GetObjectMeta())

		for _, data := range namespaceMetric.GetMetricData() {
			metricType := MetricTypeNameMap[data.GetMetricType()]
			for _, sample := range data.GetData() {
				timestamp, err := ptypes.Timestamp(sample.GetTime())
				if err != nil {
					scope.Error(" failed: " + err.Error())
				}
				sample := FormatTypes.Sample{
					Timestamp: timestamp,
					Value:     sample.GetNumValue(),
				}
				m.AddSample(metricType, sample)
			}
		}

		metricMap.AddNamespaceMetric(m)
	}

	return metricMap
}

type CreateApplicationMetricsRequestExtended struct {
	ApiMetrics.CreateApplicationMetricsRequest
}

func (r *CreateApplicationMetricsRequestExtended) Validate() error {
	for _, m := range r.GetApplicationMetrics() {
		if m == nil || m.ObjectMeta == nil || m.ObjectMeta.Name == "" || m.ObjectMeta.Namespace == "" || m.ObjectMeta.ClusterName == "" {
			return errors.Errorf(`must provide "Name", "Namespace" and "ClusterName" in ObjectMeta`)
		}
	}
	return nil
}

func (r *CreateApplicationMetricsRequestExtended) ProduceMetrics() DaoMetricTypes.AppMetricMap {
	metricMap := DaoMetricTypes.NewAppMetricMap()

	for _, applicationMetric := range r.GetApplicationMetrics() {
		if applicationMetric == nil {
			continue
		}
		m := DaoMetricTypes.NewAppMetric()
		m.ObjectMeta = NewObjectMeta(applicationMetric.GetObjectMeta())

		for _, data := range applicationMetric.GetMetricData() {
			metricType := MetricTypeNameMap[data.GetMetricType()]
			for _, sample := range data.GetData() {
				timestamp, err := ptypes.Timestamp(sample.GetTime())
				if err != nil {
					scope.Error(" failed: " + err.Error())
				}
				sample := FormatTypes.Sample{
					Timestamp: timestamp,
					Value:     sample.GetNumValue(),
				}
				m.AddSample(metricType, sample)
			}
		}

		metricMap.AddAppMetric(m)
	}

	return metricMap
}

type CreateControllerMetricsRequestExtended struct {
	ApiMetrics.CreateControllerMetricsRequest
}

func (r *CreateControllerMetricsRequestExtended) Validate() error {
	for _, m := range r.GetControllerMetrics() {
		if m == nil || m.ObjectMeta == nil || m.ObjectMeta.Name == "" || m.ObjectMeta.Namespace == "" || m.ObjectMeta.ClusterName == "" {
			return errors.Errorf(`must provide "Name", "Namespace" and "ClusterName" in ObjectMeta`)
		}
	}
	return nil
}

func (r *CreateControllerMetricsRequestExtended) ProduceMetrics() DaoMetricTypes.ControllerMetricMap {
	metricMap := DaoMetricTypes.NewControllerMetricMap()

	for _, controllerMetric := range r.GetControllerMetrics() {
		if controllerMetric == nil {
			continue
		}
		m := DaoMetricTypes.NewControllerMetric()
		m.ObjectMeta.ObjectMeta = NewObjectMeta(controllerMetric.GetObjectMeta())
		m.ObjectMeta.Kind = controllerMetric.Kind.String()
		for _, data := range controllerMetric.GetMetricData() {
			metricType := MetricTypeNameMap[data.GetMetricType()]
			for _, sample := range data.GetData() {
				timestamp, err := ptypes.Timestamp(sample.GetTime())
				if err != nil {
					scope.Error(" failed: " + err.Error())
				}
				sample := FormatTypes.Sample{
					Timestamp: timestamp,
					Value:     sample.GetNumValue(),
				}
				m.AddSample(metricType, sample)
			}
		}

		metricMap.AddControllerMetric(m)
	}

	return metricMap
}

type CreatePodMetricsRequestExtended struct {
	ApiMetrics.CreatePodMetricsRequest
}

func (r *CreatePodMetricsRequestExtended) Validate() error {
	return nil
}

func (r *CreatePodMetricsRequestExtended) ProduceMetrics() DaoMetricTypes.PodMetricMap {
	podMetricMap := DaoMetricTypes.NewPodMetricMap()

	rateRange := int64(5)
	if r.GetRateRange() != 0 {
		rateRange = int64(r.GetRateRange())
	}

	for _, pod := range r.GetPodMetrics() {
		podMetric := DaoMetricTypes.NewPodMetric()
		podMetric.ObjectMeta = NewObjectMeta(pod.GetObjectMeta())
		podMetric.RateRange = rateRange

		for _, container := range pod.GetContainerMetrics() {
			containerMetric := DaoMetricTypes.NewContainerMetric()
			containerMetric.ObjectMeta.Namespace = podMetric.ObjectMeta.Namespace
			containerMetric.ObjectMeta.PodName = podMetric.ObjectMeta.Name
			containerMetric.ObjectMeta.Name = container.GetName()
			containerMetric.RateRange = rateRange

			for _, data := range container.GetMetricData() {
				metricType := MetricTypeNameMap[data.GetMetricType()]
				for _, sample := range data.GetData() {
					timestamp, err := ptypes.Timestamp(sample.GetTime())
					if err != nil {
						scope.Error(" failed: " + err.Error())
					}
					sample := FormatTypes.Sample{
						Timestamp: timestamp,
						Value:     sample.GetNumValue(),
					}
					containerMetric.AddSample(metricType, sample)
				}
			}

			podMetric.ContainerMetricMap.AddContainerMetric(containerMetric)
		}

		podMetricMap.AddPodMetric(podMetric)
	}

	return podMetricMap
}

type ListClusterMetricsRequestExtended struct {
	Request *ApiMetrics.ListClusterMetricsRequest
}

func (r *ListClusterMetricsRequestExtended) Validate() error {
	return nil
}

func (r *ListClusterMetricsRequestExtended) SetDefault() {
	q := normalizeListMetricsRequestQueryCondition(*r.Request.QueryCondition)
	r.Request.QueryCondition = &q
}

func (r *ListClusterMetricsRequestExtended) ProduceRequest() DaoMetricTypes.ListClusterMetricsRequest {
	request := DaoMetricTypes.ListClusterMetricsRequest{}
	request.QueryCondition = QueryConditionExtend{r.Request.GetQueryCondition()}.QueryCondition()
	objectMetas := make([]metadata.ObjectMeta, len(r.Request.GetObjectMeta()))
	for i, objectMeta := range r.Request.GetObjectMeta() {
		copyObjectMeta := objectMeta
		o := NewObjectMeta(copyObjectMeta)
		if o.IsEmpty() {
			objectMetas = nil
			break
		}
		objectMetas[i] = o
	}
	request.ObjectMetas = objectMetas
	return request
}

type ListNodeMetricsRequestExtended struct {
	Request *ApiMetrics.ListNodeMetricsRequest
}

func (r *ListNodeMetricsRequestExtended) Validate() error {
	return nil
}

func (r *ListNodeMetricsRequestExtended) SetDefault() {
	q := normalizeListMetricsRequestQueryCondition(*r.Request.QueryCondition)
	r.Request.QueryCondition = &q
}

func (r *ListNodeMetricsRequestExtended) ProduceRequest() DaoMetricTypes.ListNodeMetricsRequest {
	request := DaoMetricTypes.NewListNodeMetricsRequest()
	request.QueryCondition = QueryConditionExtend{r.Request.GetQueryCondition()}.QueryCondition()
	objectMetas := make([]metadata.ObjectMeta, len(r.Request.GetObjectMeta()))
	for i, objectMeta := range r.Request.GetObjectMeta() {
		copyObjectMeta := objectMeta
		o := NewObjectMeta(copyObjectMeta)
		if o.IsEmpty() {
			objectMetas = nil
			break
		}
		objectMetas[i] = o
	}
	request.ObjectMetas = objectMetas
	return request
}

type ListNamespaceMetricsRequestExtended struct {
	Request *ApiMetrics.ListNamespaceMetricsRequest
}

func (r *ListNamespaceMetricsRequestExtended) Validate() error {
	return nil
}

func (r *ListNamespaceMetricsRequestExtended) SetDefault() {
	q := normalizeListMetricsRequestQueryCondition(*r.Request.QueryCondition)
	r.Request.QueryCondition = &q
}

func (r *ListNamespaceMetricsRequestExtended) ProduceRequest() DaoMetricTypes.ListNamespaceMetricsRequest {
	request := DaoMetricTypes.ListNamespaceMetricsRequest{}
	request.QueryCondition = QueryConditionExtend{r.Request.GetQueryCondition()}.QueryCondition()
	objectMetas := make([]metadata.ObjectMeta, len(r.Request.GetObjectMeta()))
	for i, objectMeta := range r.Request.GetObjectMeta() {
		copyObjectMeta := objectMeta
		o := NewObjectMeta(copyObjectMeta)
		if o.IsEmpty() {
			objectMetas = nil
			break
		}
		objectMetas[i] = o
	}
	request.ObjectMetas = objectMetas
	return request
}

type ListAppMetricsRequestExtended struct {
	Request *ApiMetrics.ListApplicationMetricsRequest
}

func (r *ListAppMetricsRequestExtended) Validate() error {
	return nil
}

func (r *ListAppMetricsRequestExtended) SetDefault() {
	q := normalizeListMetricsRequestQueryCondition(*r.Request.QueryCondition)
	r.Request.QueryCondition = &q
}

func (r *ListAppMetricsRequestExtended) ProduceRequest() DaoMetricTypes.ListAppMetricsRequest {
	request := DaoMetricTypes.ListAppMetricsRequest{}
	request.QueryCondition = QueryConditionExtend{r.Request.GetQueryCondition()}.QueryCondition()
	objectMetas := make([]metadata.ObjectMeta, len(r.Request.GetObjectMeta()))
	for i, objectMeta := range r.Request.GetObjectMeta() {
		copyObjectMeta := objectMeta
		o := NewObjectMeta(copyObjectMeta)
		if o.IsEmpty() {
			objectMetas = nil
			break
		}
		objectMetas[i] = o
	}
	request.ObjectMetas = objectMetas
	return request
}

type ListControllerMetricsRequestExtended struct {
	Request *ApiMetrics.ListControllerMetricsRequest
}

func (r *ListControllerMetricsRequestExtended) Validate() error {

	var supportedKind = map[ApiResource.Kind]bool{
		ApiResource.Kind_DEPLOYMENT:       true,
		ApiResource.Kind_DEPLOYMENTCONFIG: true,
		ApiResource.Kind_STATEFULSET:      true,
	}
	supported, exist := supportedKind[r.Request.Kind]
	if !exist || !supported {
		return errors.Errorf(`controller kind "%s" not supported`, r.Request.Kind)
	}
	return nil
}

func (r *ListControllerMetricsRequestExtended) SetDefault() {
	q := normalizeListMetricsRequestQueryCondition(*r.Request.QueryCondition)
	r.Request.QueryCondition = &q
}

func (r *ListControllerMetricsRequestExtended) ProduceRequest() DaoMetricTypes.ListControllerMetricsRequest {
	request := DaoMetricTypes.ListControllerMetricsRequest{}
	request.QueryCondition = QueryConditionExtend{r.Request.GetQueryCondition()}.QueryCondition()
	// TODO: Check if kind exists
	request.Kind = r.Request.Kind.String()
	objectMetas := make([]metadata.ObjectMeta, len(r.Request.GetObjectMeta()))
	for i, objectMeta := range r.Request.GetObjectMeta() {
		copyObjectMeta := objectMeta
		o := NewObjectMeta(copyObjectMeta)
		if o.IsEmpty() {
			objectMetas = nil
			break
		}
		objectMetas[i] = o
	}
	request.ObjectMetas = objectMetas
	return request
}

type ListPodMetricsRequestExtended struct {
	Request *ApiMetrics.ListPodMetricsRequest
}

func (r *ListPodMetricsRequestExtended) Validate() error {
	return nil
}

func (r *ListPodMetricsRequestExtended) SetDefault() {
	q := normalizeListMetricsRequestQueryCondition(*r.Request.QueryCondition)
	r.Request.QueryCondition = &q
}

func (r *ListPodMetricsRequestExtended) ProduceRequest() DaoMetricTypes.ListPodMetricsRequest {
	request := DaoMetricTypes.NewListPodMetricsRequest()
	request.QueryCondition = QueryConditionExtend{r.Request.GetQueryCondition()}.QueryCondition()
	request.RateRange = 5
	if r.Request.GetRateRange() != 0 {
		request.RateRange = int64(r.Request.GetRateRange())
	}
	objectMetas := make([]metadata.ObjectMeta, len(r.Request.GetObjectMeta()))
	for i, objectMeta := range r.Request.GetObjectMeta() {
		copyObjectMeta := objectMeta
		o := NewObjectMeta(copyObjectMeta)
		if o.IsEmpty() {
			objectMetas = nil
			break
		}
		objectMetas[i] = o
	}
	request.ObjectMetas = objectMetas
	return request
}

func normalizeListMetricsRequestQueryCondition(q ApiCommon.QueryCondition) ApiCommon.QueryCondition {

	defaultStartTime := timestamp.Timestamp{}
	defaultEndTime := *ptypes.TimestampNow()
	defaultStep := duration.Duration{
		Seconds: 30,
	}

	if q.TimeRange == nil {
		q.TimeRange = &ApiCommon.TimeRange{
			StartTime: &defaultStartTime,
			EndTime:   &defaultEndTime,
			Step:      &defaultStep,
		}
	}
	if q.TimeRange.StartTime == nil {
		q.TimeRange.StartTime = &defaultStartTime
	}
	if q.TimeRange.EndTime == nil {
		q.TimeRange.EndTime = &defaultEndTime
	}
	if q.TimeRange.Step == nil {
		q.TimeRange.Step = &defaultStep
	}

	return q
}
