# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alameda_api/v1alpha1/datahub/events/services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alameda_api.v1alpha1.datahub.common import queries_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2
from alameda_api.v1alpha1.datahub.events import events_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_events__pb2
from alameda_api.v1alpha1.datahub.events import types_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_types__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alameda_api/v1alpha1/datahub/events/services.proto',
  package='containersai.alameda.v1alpha1.datahub.events',
  syntax='proto3',
  serialized_options=_b('Z@github.com/containers-ai/api/alameda_api/v1alpha1/datahub/events'),
  serialized_pb=_b('\n2alameda_api/v1alpha1/datahub/events/services.proto\x12,containersai.alameda.v1alpha1.datahub.events\x1a\x31\x61lameda_api/v1alpha1/datahub/common/queries.proto\x1a\x30\x61lameda_api/v1alpha1/datahub/events/events.proto\x1a/alameda_api/v1alpha1/datahub/events/types.proto\x1a\x17google/rpc/status.proto\"\xe7\x02\n\x11ListEventsRequest\x12U\n\x0fquery_condition\x18\x01 \x01(\x0b\x32<.containersai.alameda.v1alpha1.datahub.common.QueryCondition\x12\n\n\x02id\x18\x02 \x03(\t\x12\x12\n\ncluster_id\x18\x03 \x03(\t\x12\x45\n\x04type\x18\x04 \x03(\x0e\x32\x37.containersai.alameda.v1alpha1.datahub.events.EventType\x12K\n\x07version\x18\x05 \x03(\x0e\x32:.containersai.alameda.v1alpha1.datahub.events.EventVersion\x12G\n\x05level\x18\x06 \x03(\x0e\x32\x38.containersai.alameda.v1alpha1.datahub.events.EventLevel\"}\n\x12ListEventsResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x43\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x33.containersai.alameda.v1alpha1.datahub.events.Event\"Z\n\x13\x43reateEventsRequest\x12\x43\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x33.containersai.alameda.v1alpha1.datahub.events.EventBBZ@github.com/containers-ai/api/alameda_api/v1alpha1/datahub/eventsb\x06proto3')
  ,
  dependencies=[alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2.DESCRIPTOR,alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_events__pb2.DESCRIPTOR,alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_types__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_LISTEVENTSREQUEST = _descriptor.Descriptor(
  name='ListEventsRequest',
  full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_condition', full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsRequest.query_condition', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsRequest.cluster_id', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsRequest.type', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsRequest.version', index=4,
      number=5, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsRequest.level', index=5,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=635,
)


_LISTEVENTSRESPONSE = _descriptor.Descriptor(
  name='ListEventsResponse',
  full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='containersai.alameda.v1alpha1.datahub.events.ListEventsResponse.events', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=762,
)


_CREATEEVENTSREQUEST = _descriptor.Descriptor(
  name='CreateEventsRequest',
  full_name='containersai.alameda.v1alpha1.datahub.events.CreateEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='containersai.alameda.v1alpha1.datahub.events.CreateEventsRequest.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=764,
  serialized_end=854,
)

_LISTEVENTSREQUEST.fields_by_name['query_condition'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2._QUERYCONDITION
_LISTEVENTSREQUEST.fields_by_name['type'].enum_type = alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_types__pb2._EVENTTYPE
_LISTEVENTSREQUEST.fields_by_name['version'].enum_type = alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_types__pb2._EVENTVERSION
_LISTEVENTSREQUEST.fields_by_name['level'].enum_type = alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_types__pb2._EVENTLEVEL
_LISTEVENTSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTEVENTSRESPONSE.fields_by_name['events'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_events__pb2._EVENT
_CREATEEVENTSREQUEST.fields_by_name['events'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_events_dot_events__pb2._EVENT
DESCRIPTOR.message_types_by_name['ListEventsRequest'] = _LISTEVENTSREQUEST
DESCRIPTOR.message_types_by_name['ListEventsResponse'] = _LISTEVENTSRESPONSE
DESCRIPTOR.message_types_by_name['CreateEventsRequest'] = _CREATEEVENTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListEventsRequest = _reflection.GeneratedProtocolMessageType('ListEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.events.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.events.ListEventsRequest)
  })
_sym_db.RegisterMessage(ListEventsRequest)

ListEventsResponse = _reflection.GeneratedProtocolMessageType('ListEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSRESPONSE,
  '__module__' : 'alameda_api.v1alpha1.datahub.events.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.events.ListEventsResponse)
  })
_sym_db.RegisterMessage(ListEventsResponse)

CreateEventsRequest = _reflection.GeneratedProtocolMessageType('CreateEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEEVENTSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.events.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.events.CreateEventsRequest)
  })
_sym_db.RegisterMessage(CreateEventsRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)