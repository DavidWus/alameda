// Code generated by protoc-gen-go. DO NOT EDIT.
// source: alameda_api/v1alpha1/ai_service/ai_service.proto

package containers_ai_alameda_v1alpha1_ai_service

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	empty "github.com/golang/protobuf/ptypes/empty"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

//*
//  Recommendation policy. A policy may be either stable or compact.
type RecommendationPolicy int32

const (
	RecommendationPolicy_STABLE  RecommendationPolicy = 0
	RecommendationPolicy_COMPACT RecommendationPolicy = 1
)

var RecommendationPolicy_name = map[int32]string{
	0: "STABLE",
	1: "COMPACT",
}

var RecommendationPolicy_value = map[string]int32{
	"STABLE":  0,
	"COMPACT": 1,
}

func (x RecommendationPolicy) String() string {
	return proto.EnumName(RecommendationPolicy_name, int32(x))
}

func (RecommendationPolicy) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_facbad1e8d2a4adf, []int{0}
}

/// Types of an object
type Object_Type int32

const (
	Object_POD  Object_Type = 0
	Object_NODE Object_Type = 1
)

var Object_Type_name = map[int32]string{
	0: "POD",
	1: "NODE",
}

var Object_Type_value = map[string]int32{
	"POD":  0,
	"NODE": 1,
}

func (x Object_Type) String() string {
	return proto.EnumName(Object_Type_name, int32(x))
}

func (Object_Type) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_facbad1e8d2a4adf, []int{1, 0}
}

//*
// Represents a Kubernetes pod.
//
type Pod struct {
	NodeName             string   `protobuf:"bytes,1,opt,name=node_name,json=nodeName,proto3" json:"node_name,omitempty"`
	ResourceLink         string   `protobuf:"bytes,2,opt,name=resourceLink,proto3" json:"resourceLink,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Pod) Reset()         { *m = Pod{} }
func (m *Pod) String() string { return proto.CompactTextString(m) }
func (*Pod) ProtoMessage()    {}
func (*Pod) Descriptor() ([]byte, []int) {
	return fileDescriptor_facbad1e8d2a4adf, []int{0}
}

func (m *Pod) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Pod.Unmarshal(m, b)
}
func (m *Pod) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Pod.Marshal(b, m, deterministic)
}
func (m *Pod) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Pod.Merge(m, src)
}
func (m *Pod) XXX_Size() int {
	return xxx_messageInfo_Pod.Size(m)
}
func (m *Pod) XXX_DiscardUnknown() {
	xxx_messageInfo_Pod.DiscardUnknown(m)
}

var xxx_messageInfo_Pod proto.InternalMessageInfo

func (m *Pod) GetNodeName() string {
	if m != nil {
		return m.NodeName
	}
	return ""
}

func (m *Pod) GetResourceLink() string {
	if m != nil {
		return m.ResourceLink
	}
	return ""
}

//*
// Represents a Kubernetes object.
type Object struct {
	Type                 Object_Type          `protobuf:"varint,1,opt,name=type,proto3,enum=containers_ai.alameda.v1alpha1.ai_service.Object_Type" json:"type,omitempty"`
	Policy               RecommendationPolicy `protobuf:"varint,2,opt,name=policy,proto3,enum=containers_ai.alameda.v1alpha1.ai_service.RecommendationPolicy" json:"policy,omitempty"`
	Uid                  string               `protobuf:"bytes,3,opt,name=uid,proto3" json:"uid,omitempty"`
	Namespace            string               `protobuf:"bytes,4,opt,name=namespace,proto3" json:"namespace,omitempty"`
	Name                 string               `protobuf:"bytes,5,opt,name=name,proto3" json:"name,omitempty"`
	Pod                  *Pod                 `protobuf:"bytes,6,opt,name=pod,proto3" json:"pod,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *Object) Reset()         { *m = Object{} }
func (m *Object) String() string { return proto.CompactTextString(m) }
func (*Object) ProtoMessage()    {}
func (*Object) Descriptor() ([]byte, []int) {
	return fileDescriptor_facbad1e8d2a4adf, []int{1}
}

func (m *Object) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Object.Unmarshal(m, b)
}
func (m *Object) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Object.Marshal(b, m, deterministic)
}
func (m *Object) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Object.Merge(m, src)
}
func (m *Object) XXX_Size() int {
	return xxx_messageInfo_Object.Size(m)
}
func (m *Object) XXX_DiscardUnknown() {
	xxx_messageInfo_Object.DiscardUnknown(m)
}

var xxx_messageInfo_Object proto.InternalMessageInfo

func (m *Object) GetType() Object_Type {
	if m != nil {
		return m.Type
	}
	return Object_POD
}

func (m *Object) GetPolicy() RecommendationPolicy {
	if m != nil {
		return m.Policy
	}
	return RecommendationPolicy_STABLE
}

func (m *Object) GetUid() string {
	if m != nil {
		return m.Uid
	}
	return ""
}

func (m *Object) GetNamespace() string {
	if m != nil {
		return m.Namespace
	}
	return ""
}

func (m *Object) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Object) GetPod() *Pod {
	if m != nil {
		return m.Pod
	}
	return nil
}

//*
// Represents a request for creating a list of prediction objects
type PredictionObjectListCreationRequest struct {
	Objects              []*Object `protobuf:"bytes,1,rep,name=objects,proto3" json:"objects,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *PredictionObjectListCreationRequest) Reset()         { *m = PredictionObjectListCreationRequest{} }
func (m *PredictionObjectListCreationRequest) String() string { return proto.CompactTextString(m) }
func (*PredictionObjectListCreationRequest) ProtoMessage()    {}
func (*PredictionObjectListCreationRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_facbad1e8d2a4adf, []int{2}
}

func (m *PredictionObjectListCreationRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_PredictionObjectListCreationRequest.Unmarshal(m, b)
}
func (m *PredictionObjectListCreationRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_PredictionObjectListCreationRequest.Marshal(b, m, deterministic)
}
func (m *PredictionObjectListCreationRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_PredictionObjectListCreationRequest.Merge(m, src)
}
func (m *PredictionObjectListCreationRequest) XXX_Size() int {
	return xxx_messageInfo_PredictionObjectListCreationRequest.Size(m)
}
func (m *PredictionObjectListCreationRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_PredictionObjectListCreationRequest.DiscardUnknown(m)
}

var xxx_messageInfo_PredictionObjectListCreationRequest proto.InternalMessageInfo

func (m *PredictionObjectListCreationRequest) GetObjects() []*Object {
	if m != nil {
		return m.Objects
	}
	return nil
}

//*
// Represents a request for removing a list of prediction objects
type PredictionObjectListDeletionRequest struct {
	Objects              []*Object `protobuf:"bytes,1,rep,name=objects,proto3" json:"objects,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *PredictionObjectListDeletionRequest) Reset()         { *m = PredictionObjectListDeletionRequest{} }
func (m *PredictionObjectListDeletionRequest) String() string { return proto.CompactTextString(m) }
func (*PredictionObjectListDeletionRequest) ProtoMessage()    {}
func (*PredictionObjectListDeletionRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_facbad1e8d2a4adf, []int{3}
}

func (m *PredictionObjectListDeletionRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_PredictionObjectListDeletionRequest.Unmarshal(m, b)
}
func (m *PredictionObjectListDeletionRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_PredictionObjectListDeletionRequest.Marshal(b, m, deterministic)
}
func (m *PredictionObjectListDeletionRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_PredictionObjectListDeletionRequest.Merge(m, src)
}
func (m *PredictionObjectListDeletionRequest) XXX_Size() int {
	return xxx_messageInfo_PredictionObjectListDeletionRequest.Size(m)
}
func (m *PredictionObjectListDeletionRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_PredictionObjectListDeletionRequest.DiscardUnknown(m)
}

var xxx_messageInfo_PredictionObjectListDeletionRequest proto.InternalMessageInfo

func (m *PredictionObjectListDeletionRequest) GetObjects() []*Object {
	if m != nil {
		return m.Objects
	}
	return nil
}

//*
// Represents a reponse of a request
type RequestResponse struct {
	Message              string   `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *RequestResponse) Reset()         { *m = RequestResponse{} }
func (m *RequestResponse) String() string { return proto.CompactTextString(m) }
func (*RequestResponse) ProtoMessage()    {}
func (*RequestResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_facbad1e8d2a4adf, []int{4}
}

func (m *RequestResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_RequestResponse.Unmarshal(m, b)
}
func (m *RequestResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_RequestResponse.Marshal(b, m, deterministic)
}
func (m *RequestResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RequestResponse.Merge(m, src)
}
func (m *RequestResponse) XXX_Size() int {
	return xxx_messageInfo_RequestResponse.Size(m)
}
func (m *RequestResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_RequestResponse.DiscardUnknown(m)
}

var xxx_messageInfo_RequestResponse proto.InternalMessageInfo

func (m *RequestResponse) GetMessage() string {
	if m != nil {
		return m.Message
	}
	return ""
}

func init() {
	proto.RegisterEnum("containers_ai.alameda.v1alpha1.ai_service.RecommendationPolicy", RecommendationPolicy_name, RecommendationPolicy_value)
	proto.RegisterEnum("containers_ai.alameda.v1alpha1.ai_service.Object_Type", Object_Type_name, Object_Type_value)
	proto.RegisterType((*Pod)(nil), "containers_ai.alameda.v1alpha1.ai_service.Pod")
	proto.RegisterType((*Object)(nil), "containers_ai.alameda.v1alpha1.ai_service.Object")
	proto.RegisterType((*PredictionObjectListCreationRequest)(nil), "containers_ai.alameda.v1alpha1.ai_service.PredictionObjectListCreationRequest")
	proto.RegisterType((*PredictionObjectListDeletionRequest)(nil), "containers_ai.alameda.v1alpha1.ai_service.PredictionObjectListDeletionRequest")
	proto.RegisterType((*RequestResponse)(nil), "containers_ai.alameda.v1alpha1.ai_service.RequestResponse")
}

func init() {
	proto.RegisterFile("alameda_api/v1alpha1/ai_service/ai_service.proto", fileDescriptor_facbad1e8d2a4adf)
}

var fileDescriptor_facbad1e8d2a4adf = []byte{
	// 494 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xb4, 0x54, 0xc1, 0x6e, 0xd3, 0x40,
	0x10, 0x8d, 0xe3, 0x90, 0x34, 0x13, 0x54, 0xcc, 0x0a, 0x51, 0x93, 0x72, 0x88, 0xcc, 0x25, 0x80,
	0xb4, 0x26, 0x46, 0xe2, 0xc0, 0x05, 0x42, 0x12, 0x24, 0x20, 0x24, 0x96, 0x1b, 0x89, 0x63, 0xb4,
	0xb1, 0x87, 0xb0, 0x60, 0x7b, 0x17, 0xaf, 0x53, 0x29, 0x67, 0x3e, 0x86, 0x0f, 0xe1, 0xce, 0x37,
	0x21, 0xaf, 0x63, 0x95, 0x56, 0x20, 0xf0, 0xa1, 0xb7, 0xd9, 0x19, 0xcd, 0x9b, 0xf7, 0xde, 0xac,
	0x06, 0x9e, 0xb0, 0x98, 0x25, 0x18, 0xb1, 0x35, 0x93, 0xdc, 0x3d, 0x1f, 0xb1, 0x58, 0x7e, 0x62,
	0x23, 0x97, 0xf1, 0xb5, 0xc2, 0xec, 0x9c, 0x87, 0xf8, 0x5b, 0x48, 0x65, 0x26, 0x72, 0x41, 0x1e,
	0x86, 0x22, 0xcd, 0x19, 0x4f, 0x31, 0x53, 0x6b, 0xc6, 0xe9, 0xa1, 0x9f, 0x56, 0xbd, 0xf4, 0xa2,
	0xa1, 0x7f, 0xba, 0x15, 0x62, 0x1b, 0xa3, 0xab, 0x1b, 0x37, 0xbb, 0x8f, 0x2e, 0x26, 0x32, 0xdf,
	0x97, 0x38, 0xce, 0x6b, 0x30, 0x7d, 0x11, 0x91, 0x53, 0xe8, 0xa6, 0x22, 0xc2, 0x75, 0xca, 0x12,
	0xb4, 0x8d, 0x81, 0x31, 0xec, 0x06, 0x47, 0x45, 0x62, 0xc1, 0x12, 0x24, 0x0e, 0xdc, 0xcc, 0x50,
	0x89, 0x5d, 0x16, 0xe2, 0x9c, 0xa7, 0x5f, 0xec, 0xa6, 0xae, 0x5f, 0xca, 0x39, 0x3f, 0x9b, 0xd0,
	0x5e, 0x6e, 0x3e, 0x63, 0x98, 0x93, 0xb7, 0xd0, 0xca, 0xf7, 0xb2, 0x84, 0x39, 0xf6, 0x9e, 0xd1,
	0xff, 0x66, 0x4a, 0x4b, 0x00, 0xba, 0xda, 0x4b, 0x0c, 0x34, 0x06, 0xf9, 0x00, 0x6d, 0x29, 0x62,
	0x1e, 0xee, 0xf5, 0xd0, 0x63, 0xef, 0x45, 0x0d, 0xb4, 0x00, 0x43, 0x91, 0x24, 0x98, 0x46, 0x2c,
	0xe7, 0x22, 0xf5, 0x35, 0x4c, 0x70, 0x80, 0x23, 0x16, 0x98, 0x3b, 0x1e, 0xd9, 0xa6, 0x96, 0x52,
	0x84, 0xe4, 0x3e, 0x74, 0x0b, 0xf5, 0x4a, 0xb2, 0x10, 0xed, 0x96, 0xce, 0x5f, 0x24, 0x08, 0x81,
	0x96, 0xf6, 0xe6, 0x86, 0x2e, 0xe8, 0x98, 0xbc, 0x04, 0x53, 0x8a, 0xc8, 0x6e, 0x0f, 0x8c, 0x61,
	0xcf, 0xa3, 0x35, 0x98, 0xf9, 0x22, 0x0a, 0x8a, 0x56, 0xe7, 0x1e, 0xb4, 0x0a, 0xb1, 0xa4, 0x03,
	0xa6, 0xbf, 0x9c, 0x5a, 0x0d, 0x72, 0x04, 0xad, 0xc5, 0x72, 0x3a, 0xb3, 0x0c, 0x27, 0x83, 0x07,
	0x7e, 0x86, 0x11, 0x0f, 0x0b, 0xf2, 0xa5, 0x31, 0x73, 0xae, 0xf2, 0x49, 0x86, 0x5a, 0x4e, 0x80,
	0x5f, 0x77, 0xa8, 0x72, 0xf2, 0x0e, 0x3a, 0x42, 0x17, 0x95, 0x6d, 0x0c, 0xcc, 0x61, 0xcf, 0x1b,
	0xd5, 0xf6, 0x3b, 0xa8, 0x10, 0xfe, 0x36, 0x73, 0x8a, 0x31, 0x5e, 0xdb, 0xcc, 0xc7, 0x70, 0xeb,
	0x80, 0x1b, 0xa0, 0x92, 0x22, 0x55, 0x48, 0x6c, 0xe8, 0x24, 0xa8, 0x14, 0xdb, 0x56, 0x5f, 0xb1,
	0x7a, 0x3e, 0x72, 0xe1, 0xce, 0x9f, 0xb6, 0x4a, 0x00, 0xda, 0x67, 0xab, 0xf1, 0xab, 0xf9, 0xcc,
	0x6a, 0x90, 0x1e, 0x74, 0x26, 0xcb, 0xf7, 0xfe, 0x78, 0xb2, 0xb2, 0x0c, 0xef, 0x47, 0x13, 0x6e,
	0x8f, 0x0b, 0x36, 0x69, 0xc4, 0xc6, 0x6f, 0xce, 0x4a, 0x0e, 0xe4, 0xbb, 0x01, 0x27, 0xda, 0x48,
	0xbc, 0x2a, 0x57, 0x91, 0x45, 0x9d, 0x3d, 0xfe, 0x7b, 0x41, 0xfd, 0xe7, 0xb5, 0x7e, 0xec, 0x25,
	0x23, 0x9c, 0x06, 0xf9, 0x66, 0xc0, 0x89, 0xb6, 0xff, 0x1a, 0x98, 0x5e, 0x59, 0x6b, 0xff, 0x2e,
	0x2d, 0x0f, 0x05, 0xad, 0x0e, 0x05, 0x9d, 0x15, 0x87, 0xc2, 0x69, 0x6c, 0xda, 0x3a, 0xf3, 0xf4,
	0x57, 0x00, 0x00, 0x00, 0xff, 0xff, 0x1c, 0xe8, 0xfc, 0xf9, 0xa7, 0x04, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// AlamendaAIServiceClient is the client API for AlamendaAIService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type AlamendaAIServiceClient interface {
	/// Used to create prediction objects
	CreatePredictionObjects(ctx context.Context, in *PredictionObjectListCreationRequest, opts ...grpc.CallOption) (*RequestResponse, error)
	/// Used to remove prediction objects
	DeletePredictionObjects(ctx context.Context, in *PredictionObjectListDeletionRequest, opts ...grpc.CallOption) (*empty.Empty, error)
}

type alamendaAIServiceClient struct {
	cc *grpc.ClientConn
}

func NewAlamendaAIServiceClient(cc *grpc.ClientConn) AlamendaAIServiceClient {
	return &alamendaAIServiceClient{cc}
}

func (c *alamendaAIServiceClient) CreatePredictionObjects(ctx context.Context, in *PredictionObjectListCreationRequest, opts ...grpc.CallOption) (*RequestResponse, error) {
	out := new(RequestResponse)
	err := c.cc.Invoke(ctx, "/containers_ai.alameda.v1alpha1.ai_service.AlamendaAIService/CreatePredictionObjects", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *alamendaAIServiceClient) DeletePredictionObjects(ctx context.Context, in *PredictionObjectListDeletionRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, "/containers_ai.alameda.v1alpha1.ai_service.AlamendaAIService/DeletePredictionObjects", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// AlamendaAIServiceServer is the server API for AlamendaAIService service.
type AlamendaAIServiceServer interface {
	/// Used to create prediction objects
	CreatePredictionObjects(context.Context, *PredictionObjectListCreationRequest) (*RequestResponse, error)
	/// Used to remove prediction objects
	DeletePredictionObjects(context.Context, *PredictionObjectListDeletionRequest) (*empty.Empty, error)
}

// UnimplementedAlamendaAIServiceServer can be embedded to have forward compatible implementations.
type UnimplementedAlamendaAIServiceServer struct {
}

func (*UnimplementedAlamendaAIServiceServer) CreatePredictionObjects(ctx context.Context, req *PredictionObjectListCreationRequest) (*RequestResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreatePredictionObjects not implemented")
}
func (*UnimplementedAlamendaAIServiceServer) DeletePredictionObjects(ctx context.Context, req *PredictionObjectListDeletionRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeletePredictionObjects not implemented")
}

func RegisterAlamendaAIServiceServer(s *grpc.Server, srv AlamendaAIServiceServer) {
	s.RegisterService(&_AlamendaAIService_serviceDesc, srv)
}

func _AlamendaAIService_CreatePredictionObjects_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PredictionObjectListCreationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(AlamendaAIServiceServer).CreatePredictionObjects(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/containers_ai.alameda.v1alpha1.ai_service.AlamendaAIService/CreatePredictionObjects",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(AlamendaAIServiceServer).CreatePredictionObjects(ctx, req.(*PredictionObjectListCreationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _AlamendaAIService_DeletePredictionObjects_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PredictionObjectListDeletionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(AlamendaAIServiceServer).DeletePredictionObjects(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/containers_ai.alameda.v1alpha1.ai_service.AlamendaAIService/DeletePredictionObjects",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(AlamendaAIServiceServer).DeletePredictionObjects(ctx, req.(*PredictionObjectListDeletionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _AlamendaAIService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "containers_ai.alameda.v1alpha1.ai_service.AlamendaAIService",
	HandlerType: (*AlamendaAIServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreatePredictionObjects",
			Handler:    _AlamendaAIService_CreatePredictionObjects_Handler,
		},
		{
			MethodName: "DeletePredictionObjects",
			Handler:    _AlamendaAIService_DeletePredictionObjects_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "alameda_api/v1alpha1/ai_service/ai_service.proto",
}
