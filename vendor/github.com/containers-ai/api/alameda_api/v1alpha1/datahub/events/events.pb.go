// Code generated by protoc-gen-go. DO NOT EDIT.
// source: alameda_api/v1alpha1/datahub/events/events.proto

package events

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
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

type Event struct {
	Time                 *timestamp.Timestamp `protobuf:"bytes,1,opt,name=time,proto3" json:"time,omitempty"`
	Id                   string               `protobuf:"bytes,2,opt,name=id,proto3" json:"id,omitempty"`
	ClusterId            string               `protobuf:"bytes,3,opt,name=cluster_id,json=clusterId,proto3" json:"cluster_id,omitempty"`
	Source               *EventSource         `protobuf:"bytes,4,opt,name=source,proto3" json:"source,omitempty"`
	Type                 EventType            `protobuf:"varint,5,opt,name=type,proto3,enum=containersai.alameda.v1alpha1.datahub.events.EventType" json:"type,omitempty"`
	Version              EventVersion         `protobuf:"varint,6,opt,name=version,proto3,enum=containersai.alameda.v1alpha1.datahub.events.EventVersion" json:"version,omitempty"`
	Level                EventLevel           `protobuf:"varint,7,opt,name=level,proto3,enum=containersai.alameda.v1alpha1.datahub.events.EventLevel" json:"level,omitempty"`
	Subject              *K8SObjectReference  `protobuf:"bytes,8,opt,name=subject,proto3" json:"subject,omitempty"`
	Message              string               `protobuf:"bytes,9,opt,name=message,proto3" json:"message,omitempty"`
	Data                 string               `protobuf:"bytes,10,opt,name=data,proto3" json:"data,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *Event) Reset()         { *m = Event{} }
func (m *Event) String() string { return proto.CompactTextString(m) }
func (*Event) ProtoMessage()    {}
func (*Event) Descriptor() ([]byte, []int) {
	return fileDescriptor_88b342bb6bb4fce1, []int{0}
}

func (m *Event) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Event.Unmarshal(m, b)
}
func (m *Event) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Event.Marshal(b, m, deterministic)
}
func (m *Event) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Event.Merge(m, src)
}
func (m *Event) XXX_Size() int {
	return xxx_messageInfo_Event.Size(m)
}
func (m *Event) XXX_DiscardUnknown() {
	xxx_messageInfo_Event.DiscardUnknown(m)
}

var xxx_messageInfo_Event proto.InternalMessageInfo

func (m *Event) GetTime() *timestamp.Timestamp {
	if m != nil {
		return m.Time
	}
	return nil
}

func (m *Event) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *Event) GetClusterId() string {
	if m != nil {
		return m.ClusterId
	}
	return ""
}

func (m *Event) GetSource() *EventSource {
	if m != nil {
		return m.Source
	}
	return nil
}

func (m *Event) GetType() EventType {
	if m != nil {
		return m.Type
	}
	return EventType_EVENT_TYPE_UNDEFINED
}

func (m *Event) GetVersion() EventVersion {
	if m != nil {
		return m.Version
	}
	return EventVersion_EVENT_VERSION_UNDEFINED
}

func (m *Event) GetLevel() EventLevel {
	if m != nil {
		return m.Level
	}
	return EventLevel_EVENT_LEVEL_UNDEFINED
}

func (m *Event) GetSubject() *K8SObjectReference {
	if m != nil {
		return m.Subject
	}
	return nil
}

func (m *Event) GetMessage() string {
	if m != nil {
		return m.Message
	}
	return ""
}

func (m *Event) GetData() string {
	if m != nil {
		return m.Data
	}
	return ""
}

func init() {
	proto.RegisterType((*Event)(nil), "containersai.alameda.v1alpha1.datahub.events.Event")
}

func init() {
	proto.RegisterFile("alameda_api/v1alpha1/datahub/events/events.proto", fileDescriptor_88b342bb6bb4fce1)
}

var fileDescriptor_88b342bb6bb4fce1 = []byte{
	// 366 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x9c, 0x92, 0x41, 0x4f, 0xc2, 0x30,
	0x14, 0x80, 0x33, 0x1c, 0x4c, 0x6a, 0xc2, 0xa1, 0xa7, 0x86, 0xc4, 0x48, 0x3c, 0x71, 0xd0, 0x56,
	0xf0, 0x20, 0x7a, 0x22, 0x24, 0x1e, 0x0c, 0x46, 0x63, 0x21, 0x1e, 0xb8, 0x90, 0x6e, 0x7b, 0x8c,
	0x9a, 0x6d, 0x5d, 0xd6, 0x6e, 0x09, 0x7f, 0xcc, 0xdf, 0x67, 0xd6, 0x6d, 0xf1, 0x0a, 0x9c, 0xb6,
	0xf7, 0xf6, 0xbe, 0x6f, 0xef, 0xb5, 0x0f, 0x3d, 0x88, 0x58, 0x24, 0x10, 0x8a, 0xad, 0xc8, 0x24,
	0x2b, 0x27, 0x22, 0xce, 0xf6, 0x62, 0xc2, 0x42, 0x61, 0xc4, 0xbe, 0xf0, 0x19, 0x94, 0x90, 0x1a,
	0xdd, 0x3c, 0x68, 0x96, 0x2b, 0xa3, 0xf0, 0x5d, 0xa0, 0x52, 0x23, 0x64, 0x0a, 0xb9, 0x16, 0x92,
	0x36, 0x38, 0x6d, 0x51, 0xda, 0xa0, 0xb4, 0x66, 0x86, 0xec, 0x18, 0xbf, 0x39, 0x64, 0xd0, 0xe8,
	0x87, 0x37, 0x91, 0x52, 0x51, 0x0c, 0xcc, 0x46, 0x7e, 0xb1, 0x63, 0x46, 0x26, 0xa0, 0x8d, 0x48,
	0xb2, 0xba, 0xe0, 0xf6, 0xd7, 0x45, 0xdd, 0xd7, 0x8a, 0xc3, 0x14, 0xb9, 0xd5, 0x47, 0xe2, 0x8c,
	0x9c, 0xf1, 0xd5, 0x74, 0x48, 0x6b, 0x92, 0xb6, 0x24, 0x5d, 0xb7, 0x24, 0xb7, 0x75, 0x78, 0x80,
	0x3a, 0x32, 0x24, 0x9d, 0x91, 0x33, 0xee, 0xf3, 0x8e, 0x0c, 0xf1, 0x35, 0x42, 0x41, 0x5c, 0x68,
	0x03, 0xf9, 0x56, 0x86, 0xe4, 0xc2, 0xe6, 0xfb, 0x4d, 0xe6, 0x2d, 0xc4, 0x5f, 0xa8, 0xa7, 0x55,
	0x91, 0x07, 0x40, 0x5c, 0xfb, 0x83, 0x67, 0x7a, 0xca, 0xe4, 0xd4, 0xf6, 0xb8, 0xb2, 0x02, 0xde,
	0x88, 0xf0, 0x12, 0xb9, 0xd5, 0xac, 0xa4, 0x3b, 0x72, 0xc6, 0x83, 0xe9, 0xd3, 0x19, 0xc2, 0xf5,
	0x21, 0x03, 0x6e, 0x25, 0x78, 0x8d, 0xbc, 0x12, 0x72, 0x2d, 0x55, 0x4a, 0x7a, 0xd6, 0xf7, 0x72,
	0x86, 0xef, 0xbb, 0x36, 0xf0, 0x56, 0x85, 0x3f, 0x50, 0x37, 0x86, 0x12, 0x62, 0xe2, 0x59, 0xe7,
	0xec, 0x0c, 0xe7, 0x7b, 0xc5, 0xf3, 0x5a, 0x83, 0x37, 0xc8, 0xd3, 0x85, 0xff, 0x03, 0x81, 0x21,
	0x97, 0xf6, 0x18, 0xe7, 0xa7, 0x19, 0x97, 0xb3, 0xd5, 0xa7, 0xc5, 0x39, 0xec, 0x20, 0x87, 0x34,
	0x00, 0xde, 0x0a, 0x31, 0x41, 0x5e, 0x02, 0x5a, 0x8b, 0x08, 0x48, 0xdf, 0xde, 0x5e, 0x1b, 0x62,
	0x8c, 0xdc, 0xca, 0x43, 0x90, 0x4d, 0xdb, 0xf7, 0xc5, 0x62, 0x33, 0x8f, 0xa4, 0xa9, 0xd4, 0x81,
	0x4a, 0xd8, 0x7f, 0x13, 0xf7, 0x42, 0xb2, 0x6a, 0x3b, 0x8f, 0xd8, 0x54, 0xbf, 0x67, 0x97, 0xeb,
	0xf1, 0x2f, 0x00, 0x00, 0xff, 0xff, 0x78, 0x3e, 0x64, 0x3f, 0x37, 0x03, 0x00, 0x00,
}