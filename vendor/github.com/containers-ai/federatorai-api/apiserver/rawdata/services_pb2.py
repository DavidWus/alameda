# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apiserver/rawdata/services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containers_ai.api.common import common_pb2 as containers__ai_dot_api_dot_common_dot_common__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='apiserver/rawdata/services.proto',
  package='containersai.apiserver.rawdata',
  syntax='proto3',
  serialized_options=_b('Z:github.com/containers-ai/federatorai-api/apiserver/rawdata'),
  serialized_pb=_b('\n apiserver/rawdata/services.proto\x12\x1e\x63ontainersai.apiserver.rawdata\x1a%containers-ai/api/common/common.proto\x1a\x17google/rpc/status.proto\"{\n\x12ReadRawdataRequest\x12\x38\n\rdatabase_type\x18\x01 \x01(\x0e\x32!.containersai.common.DatabaseType\x12+\n\x07queries\x18\x02 \x03(\x0b\x32\x1a.containersai.common.Query\"l\n\x13ReadRawdataResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x31\n\x07rawdata\x18\x02 \x03(\x0b\x32 .containersai.common.ReadRawdata\"\x83\x01\n\x13WriteRawdataRequest\x12\x38\n\rdatabase_type\x18\x01 \x01(\x0e\x32!.containersai.common.DatabaseType\x12\x32\n\x07rawdata\x18\x02 \x03(\x0b\x32!.containersai.common.WriteRawdata2\xe5\x01\n\x0eRawdataService\x12x\n\x0bReadRawdata\x12\x32.containersai.apiserver.rawdata.ReadRawdataRequest\x1a\x33.containersai.apiserver.rawdata.ReadRawdataResponse\"\x00\x12Y\n\x0cWriteRawdata\x12\x33.containersai.apiserver.rawdata.WriteRawdataRequest\x1a\x12.google.rpc.Status\"\x00\x42<Z:github.com/containers-ai/federatorai-api/apiserver/rawdatab\x06proto3')
  ,
  dependencies=[containers__ai_dot_api_dot_common_dot_common__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_READRAWDATAREQUEST = _descriptor.Descriptor(
  name='ReadRawdataRequest',
  full_name='containersai.apiserver.rawdata.ReadRawdataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database_type', full_name='containersai.apiserver.rawdata.ReadRawdataRequest.database_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queries', full_name='containersai.apiserver.rawdata.ReadRawdataRequest.queries', index=1,
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
  serialized_start=132,
  serialized_end=255,
)


_READRAWDATARESPONSE = _descriptor.Descriptor(
  name='ReadRawdataResponse',
  full_name='containersai.apiserver.rawdata.ReadRawdataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.apiserver.rawdata.ReadRawdataResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rawdata', full_name='containersai.apiserver.rawdata.ReadRawdataResponse.rawdata', index=1,
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
  serialized_start=257,
  serialized_end=365,
)


_WRITERAWDATAREQUEST = _descriptor.Descriptor(
  name='WriteRawdataRequest',
  full_name='containersai.apiserver.rawdata.WriteRawdataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database_type', full_name='containersai.apiserver.rawdata.WriteRawdataRequest.database_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rawdata', full_name='containersai.apiserver.rawdata.WriteRawdataRequest.rawdata', index=1,
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
  serialized_start=368,
  serialized_end=499,
)

_READRAWDATAREQUEST.fields_by_name['database_type'].enum_type = containers__ai_dot_api_dot_common_dot_common__pb2._DATABASETYPE
_READRAWDATAREQUEST.fields_by_name['queries'].message_type = containers__ai_dot_api_dot_common_dot_common__pb2._QUERY
_READRAWDATARESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_READRAWDATARESPONSE.fields_by_name['rawdata'].message_type = containers__ai_dot_api_dot_common_dot_common__pb2._READRAWDATA
_WRITERAWDATAREQUEST.fields_by_name['database_type'].enum_type = containers__ai_dot_api_dot_common_dot_common__pb2._DATABASETYPE
_WRITERAWDATAREQUEST.fields_by_name['rawdata'].message_type = containers__ai_dot_api_dot_common_dot_common__pb2._WRITERAWDATA
DESCRIPTOR.message_types_by_name['ReadRawdataRequest'] = _READRAWDATAREQUEST
DESCRIPTOR.message_types_by_name['ReadRawdataResponse'] = _READRAWDATARESPONSE
DESCRIPTOR.message_types_by_name['WriteRawdataRequest'] = _WRITERAWDATAREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadRawdataRequest = _reflection.GeneratedProtocolMessageType('ReadRawdataRequest', (_message.Message,), dict(
  DESCRIPTOR = _READRAWDATAREQUEST,
  __module__ = 'apiserver.rawdata.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.apiserver.rawdata.ReadRawdataRequest)
  ))
_sym_db.RegisterMessage(ReadRawdataRequest)

ReadRawdataResponse = _reflection.GeneratedProtocolMessageType('ReadRawdataResponse', (_message.Message,), dict(
  DESCRIPTOR = _READRAWDATARESPONSE,
  __module__ = 'apiserver.rawdata.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.apiserver.rawdata.ReadRawdataResponse)
  ))
_sym_db.RegisterMessage(ReadRawdataResponse)

WriteRawdataRequest = _reflection.GeneratedProtocolMessageType('WriteRawdataRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRITERAWDATAREQUEST,
  __module__ = 'apiserver.rawdata.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.apiserver.rawdata.WriteRawdataRequest)
  ))
_sym_db.RegisterMessage(WriteRawdataRequest)


DESCRIPTOR._options = None

_RAWDATASERVICE = _descriptor.ServiceDescriptor(
  name='RawdataService',
  full_name='containersai.apiserver.rawdata.RawdataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=502,
  serialized_end=731,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReadRawdata',
    full_name='containersai.apiserver.rawdata.RawdataService.ReadRawdata',
    index=0,
    containing_service=None,
    input_type=_READRAWDATAREQUEST,
    output_type=_READRAWDATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteRawdata',
    full_name='containersai.apiserver.rawdata.RawdataService.WriteRawdata',
    index=1,
    containing_service=None,
    input_type=_WRITERAWDATAREQUEST,
    output_type=google_dot_rpc_dot_status__pb2._STATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RAWDATASERVICE)

DESCRIPTOR.services_by_name['RawdataService'] = _RAWDATASERVICE

# @@protoc_insertion_point(module_scope)