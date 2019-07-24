# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datahub/recommendations/services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2
from datahub.recommendations import recommendations_pb2 as datahub_dot_recommendations_dot_recommendations__pb2
from datahub.resources import types_pb2 as datahub_dot_resources_dot_types__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='datahub/recommendations/services.proto',
  package='containersai.datahub.recommendations',
  syntax='proto3',
  serialized_options=_b('Z4github.com/containers-ai/api/datahub/recommendations'),
  serialized_pb=_b('\n&datahub/recommendations/services.proto\x12$containersai.datahub.recommendations\x1a\x13\x63ommon/common.proto\x1a-datahub/recommendations/recommendations.proto\x1a\x1d\x64\x61tahub/resources/types.proto\x1a\x17google/rpc/status.proto\"\x8c\x01\n\x1f\x43reatePodRecommendationsRequest\x12T\n\x13pod_recommendations\x18\x01 \x03(\x0b\x32\x37.containersai.datahub.recommendations.PodRecommendation\x12\x13\n\x0bgranularity\x18\x02 \x01(\x03\"\x8c\x01\n&CreateControllerRecommendationsRequest\x12\x62\n\x1a\x63ontroller_recommendations\x18\x01 \x03(\x0b\x32>.containersai.datahub.recommendations.ControllerRecommendation\"\xef\x01\n\x1dListPodRecommendationsRequest\x12G\n\x0fnamespaced_name\x18\x01 \x01(\x0b\x32..containersai.datahub.resources.NamespacedName\x12<\n\x0fquery_condition\x18\x02 \x01(\x0b\x32#.containersai.common.QueryCondition\x12\x32\n\x04kind\x18\x03 \x01(\x0e\x32$.containersai.datahub.resources.Kind\x12\x13\n\x0bgranularity\x18\x04 \x01(\x03\"\x9a\x01\n\x1eListPodRecommendationsResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12T\n\x13pod_recommendations\x18\x02 \x03(\x0b\x32\x37.containersai.datahub.recommendations.PodRecommendation\"\xad\x01\n$ListControllerRecommendationsRequest\x12G\n\x0fnamespaced_name\x18\x01 \x01(\x0b\x32..containersai.datahub.resources.NamespacedName\x12<\n\x0fquery_condition\x18\x02 \x01(\x0b\x32#.containersai.common.QueryCondition\"\xaf\x01\n%ListControllerRecommendationsResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x62\n\x1a\x63ontroller_recommendations\x18\x02 \x03(\x0b\x32>.containersai.datahub.recommendations.ControllerRecommendation2\xaf\x06\n\x16RecommendationsService\x12w\n\x18\x43reatePodRecommendations\x12\x45.containersai.datahub.recommendations.CreatePodRecommendationsRequest\x1a\x12.google.rpc.Status\"\x00\x12\x85\x01\n\x1f\x43reateControllerRecommendations\x12L.containersai.datahub.recommendations.CreateControllerRecommendationsRequest\x1a\x12.google.rpc.Status\"\x00\x12\xa5\x01\n\x16ListPodRecommendations\x12\x43.containersai.datahub.recommendations.ListPodRecommendationsRequest\x1a\x44.containersai.datahub.recommendations.ListPodRecommendationsResponse\"\x00\x12\xae\x01\n\x1fListAvailablePodRecommendations\x12\x43.containersai.datahub.recommendations.ListPodRecommendationsRequest\x1a\x44.containersai.datahub.recommendations.ListPodRecommendationsResponse\"\x00\x12\xba\x01\n\x1dListControllerRecommendations\x12J.containersai.datahub.recommendations.ListControllerRecommendationsRequest\x1aK.containersai.datahub.recommendations.ListControllerRecommendationsResponse\"\x00\x42\x36Z4github.com/containers-ai/api/datahub/recommendationsb\x06proto3')
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,datahub_dot_recommendations_dot_recommendations__pb2.DESCRIPTOR,datahub_dot_resources_dot_types__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_CREATEPODRECOMMENDATIONSREQUEST = _descriptor.Descriptor(
  name='CreatePodRecommendationsRequest',
  full_name='containersai.datahub.recommendations.CreatePodRecommendationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pod_recommendations', full_name='containersai.datahub.recommendations.CreatePodRecommendationsRequest.pod_recommendations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granularity', full_name='containersai.datahub.recommendations.CreatePodRecommendationsRequest.granularity', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=205,
  serialized_end=345,
)


_CREATECONTROLLERRECOMMENDATIONSREQUEST = _descriptor.Descriptor(
  name='CreateControllerRecommendationsRequest',
  full_name='containersai.datahub.recommendations.CreateControllerRecommendationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controller_recommendations', full_name='containersai.datahub.recommendations.CreateControllerRecommendationsRequest.controller_recommendations', index=0,
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
  serialized_start=348,
  serialized_end=488,
)


_LISTPODRECOMMENDATIONSREQUEST = _descriptor.Descriptor(
  name='ListPodRecommendationsRequest',
  full_name='containersai.datahub.recommendations.ListPodRecommendationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaced_name', full_name='containersai.datahub.recommendations.ListPodRecommendationsRequest.namespaced_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_condition', full_name='containersai.datahub.recommendations.ListPodRecommendationsRequest.query_condition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='containersai.datahub.recommendations.ListPodRecommendationsRequest.kind', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granularity', full_name='containersai.datahub.recommendations.ListPodRecommendationsRequest.granularity', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=491,
  serialized_end=730,
)


_LISTPODRECOMMENDATIONSRESPONSE = _descriptor.Descriptor(
  name='ListPodRecommendationsResponse',
  full_name='containersai.datahub.recommendations.ListPodRecommendationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.datahub.recommendations.ListPodRecommendationsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pod_recommendations', full_name='containersai.datahub.recommendations.ListPodRecommendationsResponse.pod_recommendations', index=1,
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
  serialized_start=733,
  serialized_end=887,
)


_LISTCONTROLLERRECOMMENDATIONSREQUEST = _descriptor.Descriptor(
  name='ListControllerRecommendationsRequest',
  full_name='containersai.datahub.recommendations.ListControllerRecommendationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaced_name', full_name='containersai.datahub.recommendations.ListControllerRecommendationsRequest.namespaced_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_condition', full_name='containersai.datahub.recommendations.ListControllerRecommendationsRequest.query_condition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=890,
  serialized_end=1063,
)


_LISTCONTROLLERRECOMMENDATIONSRESPONSE = _descriptor.Descriptor(
  name='ListControllerRecommendationsResponse',
  full_name='containersai.datahub.recommendations.ListControllerRecommendationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.datahub.recommendations.ListControllerRecommendationsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controller_recommendations', full_name='containersai.datahub.recommendations.ListControllerRecommendationsResponse.controller_recommendations', index=1,
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
  serialized_start=1066,
  serialized_end=1241,
)

_CREATEPODRECOMMENDATIONSREQUEST.fields_by_name['pod_recommendations'].message_type = datahub_dot_recommendations_dot_recommendations__pb2._PODRECOMMENDATION
_CREATECONTROLLERRECOMMENDATIONSREQUEST.fields_by_name['controller_recommendations'].message_type = datahub_dot_recommendations_dot_recommendations__pb2._CONTROLLERRECOMMENDATION
_LISTPODRECOMMENDATIONSREQUEST.fields_by_name['namespaced_name'].message_type = datahub_dot_resources_dot_types__pb2._NAMESPACEDNAME
_LISTPODRECOMMENDATIONSREQUEST.fields_by_name['query_condition'].message_type = common_dot_common__pb2._QUERYCONDITION
_LISTPODRECOMMENDATIONSREQUEST.fields_by_name['kind'].enum_type = datahub_dot_resources_dot_types__pb2._KIND
_LISTPODRECOMMENDATIONSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTPODRECOMMENDATIONSRESPONSE.fields_by_name['pod_recommendations'].message_type = datahub_dot_recommendations_dot_recommendations__pb2._PODRECOMMENDATION
_LISTCONTROLLERRECOMMENDATIONSREQUEST.fields_by_name['namespaced_name'].message_type = datahub_dot_resources_dot_types__pb2._NAMESPACEDNAME
_LISTCONTROLLERRECOMMENDATIONSREQUEST.fields_by_name['query_condition'].message_type = common_dot_common__pb2._QUERYCONDITION
_LISTCONTROLLERRECOMMENDATIONSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTCONTROLLERRECOMMENDATIONSRESPONSE.fields_by_name['controller_recommendations'].message_type = datahub_dot_recommendations_dot_recommendations__pb2._CONTROLLERRECOMMENDATION
DESCRIPTOR.message_types_by_name['CreatePodRecommendationsRequest'] = _CREATEPODRECOMMENDATIONSREQUEST
DESCRIPTOR.message_types_by_name['CreateControllerRecommendationsRequest'] = _CREATECONTROLLERRECOMMENDATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListPodRecommendationsRequest'] = _LISTPODRECOMMENDATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListPodRecommendationsResponse'] = _LISTPODRECOMMENDATIONSRESPONSE
DESCRIPTOR.message_types_by_name['ListControllerRecommendationsRequest'] = _LISTCONTROLLERRECOMMENDATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListControllerRecommendationsResponse'] = _LISTCONTROLLERRECOMMENDATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreatePodRecommendationsRequest = _reflection.GeneratedProtocolMessageType('CreatePodRecommendationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPODRECOMMENDATIONSREQUEST,
  '__module__' : 'datahub.recommendations.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.datahub.recommendations.CreatePodRecommendationsRequest)
  })
_sym_db.RegisterMessage(CreatePodRecommendationsRequest)

CreateControllerRecommendationsRequest = _reflection.GeneratedProtocolMessageType('CreateControllerRecommendationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONTROLLERRECOMMENDATIONSREQUEST,
  '__module__' : 'datahub.recommendations.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.datahub.recommendations.CreateControllerRecommendationsRequest)
  })
_sym_db.RegisterMessage(CreateControllerRecommendationsRequest)

ListPodRecommendationsRequest = _reflection.GeneratedProtocolMessageType('ListPodRecommendationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPODRECOMMENDATIONSREQUEST,
  '__module__' : 'datahub.recommendations.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.datahub.recommendations.ListPodRecommendationsRequest)
  })
_sym_db.RegisterMessage(ListPodRecommendationsRequest)

ListPodRecommendationsResponse = _reflection.GeneratedProtocolMessageType('ListPodRecommendationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPODRECOMMENDATIONSRESPONSE,
  '__module__' : 'datahub.recommendations.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.datahub.recommendations.ListPodRecommendationsResponse)
  })
_sym_db.RegisterMessage(ListPodRecommendationsResponse)

ListControllerRecommendationsRequest = _reflection.GeneratedProtocolMessageType('ListControllerRecommendationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTROLLERRECOMMENDATIONSREQUEST,
  '__module__' : 'datahub.recommendations.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.datahub.recommendations.ListControllerRecommendationsRequest)
  })
_sym_db.RegisterMessage(ListControllerRecommendationsRequest)

ListControllerRecommendationsResponse = _reflection.GeneratedProtocolMessageType('ListControllerRecommendationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTROLLERRECOMMENDATIONSRESPONSE,
  '__module__' : 'datahub.recommendations.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.datahub.recommendations.ListControllerRecommendationsResponse)
  })
_sym_db.RegisterMessage(ListControllerRecommendationsResponse)


DESCRIPTOR._options = None

_RECOMMENDATIONSSERVICE = _descriptor.ServiceDescriptor(
  name='RecommendationsService',
  full_name='containersai.datahub.recommendations.RecommendationsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1244,
  serialized_end=2059,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreatePodRecommendations',
    full_name='containersai.datahub.recommendations.RecommendationsService.CreatePodRecommendations',
    index=0,
    containing_service=None,
    input_type=_CREATEPODRECOMMENDATIONSREQUEST,
    output_type=google_dot_rpc_dot_status__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateControllerRecommendations',
    full_name='containersai.datahub.recommendations.RecommendationsService.CreateControllerRecommendations',
    index=1,
    containing_service=None,
    input_type=_CREATECONTROLLERRECOMMENDATIONSREQUEST,
    output_type=google_dot_rpc_dot_status__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListPodRecommendations',
    full_name='containersai.datahub.recommendations.RecommendationsService.ListPodRecommendations',
    index=2,
    containing_service=None,
    input_type=_LISTPODRECOMMENDATIONSREQUEST,
    output_type=_LISTPODRECOMMENDATIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListAvailablePodRecommendations',
    full_name='containersai.datahub.recommendations.RecommendationsService.ListAvailablePodRecommendations',
    index=3,
    containing_service=None,
    input_type=_LISTPODRECOMMENDATIONSREQUEST,
    output_type=_LISTPODRECOMMENDATIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListControllerRecommendations',
    full_name='containersai.datahub.recommendations.RecommendationsService.ListControllerRecommendations',
    index=4,
    containing_service=None,
    input_type=_LISTCONTROLLERRECOMMENDATIONSREQUEST,
    output_type=_LISTCONTROLLERRECOMMENDATIONSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDATIONSSERVICE)

DESCRIPTOR.services_by_name['RecommendationsService'] = _RECOMMENDATIONSSERVICE

# @@protoc_insertion_point(module_scope)
