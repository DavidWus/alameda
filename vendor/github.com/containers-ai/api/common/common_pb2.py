# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import types_pb2 as common_dot_types__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/common.proto',
  package='containersai.common',
  syntax='proto3',
  serialized_options=_b('Z#github.com/containers-ai/api/common'),
  serialized_pb=_b('\n\x13\x63ommon/common.proto\x12\x13\x63ontainersai.common\x1a\x12\x63ommon/types.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xee\x02\n\tTimeRange\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07timeout\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x04step\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12L\n\x12\x61ggregate_function\x18\x05 \x01(\x0e\x32\x30.containersai.common.TimeRange.AggregateFunction\x12.\n\napply_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"/\n\x11\x41ggregateFunction\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03MAX\x10\x01\x12\x07\n\x03\x41VG\x10\x02\"\xe0\x01\n\x0eQueryCondition\x12\x32\n\ntime_range\x18\x01 \x01(\x0b\x32\x1e.containersai.common.TimeRange\x12\x38\n\x05order\x18\x02 \x01(\x0e\x32).containersai.common.QueryCondition.Order\x12\x14\n\x0cwhere_clause\x18\x03 \x01(\t\x12\x0f\n\x07selects\x18\x04 \x03(\t\x12\x0e\n\x06groups\x18\x05 \x03(\t\x12\r\n\x05limit\x18\x06 \x01(\x04\"\x1a\n\x05Order\x12\x07\n\x03\x41SC\x10\x00\x12\x08\n\x04\x44\x45SC\x10\x01\"t\n\x05Query\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x12\n\nexpression\x18\x03 \x01(\t\x12\x36\n\tcondition\x18\x04 \x01(\x0b\x32#.containersai.common.QueryCondition\"?\n\x03Row\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06values\x18\x02 \x03(\t\"/\n\x05Group\x12&\n\x04rows\x18\x01 \x03(\x0b\x32\x18.containersai.common.Row\"\x86\x01\n\x0bReadRawdata\x12)\n\x05query\x18\x01 \x01(\x0b\x32\x1a.containersai.common.Query\x12\x0f\n\x07\x63olumns\x18\x02 \x03(\t\x12*\n\x06groups\x18\x03 \x03(\x0b\x32\x1a.containersai.common.Group\x12\x0f\n\x07rawdata\x18\x04 \x01(\t\"\xd2\x01\n\x0cWriteRawdata\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x03 \x03(\t\x12&\n\x04rows\x18\x04 \x03(\x0b\x32\x18.containersai.common.Row\x12\x35\n\x0c\x63olumn_types\x18\x05 \x03(\x0e\x32\x1f.containersai.common.ColumnType\x12\x31\n\ndata_types\x18\x06 \x03(\x0e\x32\x1d.containersai.common.DataType*;\n\x0c\x44\x61tabaseType\x12\r\n\tUNDEFINED\x10\x00\x12\x0c\n\x08INFLUXDB\x10\x01\x12\x0e\n\nPROMETHEUS\x10\x02\x42%Z#github.com/containers-ai/api/commonb\x06proto3')
  ,
  dependencies=[common_dot_types__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_DATABASETYPE = _descriptor.EnumDescriptor(
  name='DatabaseType',
  full_name='containersai.common.DatabaseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFLUXDB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMETHEUS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1307,
  serialized_end=1366,
)
_sym_db.RegisterEnumDescriptor(_DATABASETYPE)

DatabaseType = enum_type_wrapper.EnumTypeWrapper(_DATABASETYPE)
UNDEFINED = 0
INFLUXDB = 1
PROMETHEUS = 2


_TIMERANGE_AGGREGATEFUNCTION = _descriptor.EnumDescriptor(
  name='AggregateFunction',
  full_name='containersai.common.TimeRange.AggregateFunction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVG', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=449,
  serialized_end=496,
)
_sym_db.RegisterEnumDescriptor(_TIMERANGE_AGGREGATEFUNCTION)

_QUERYCONDITION_ORDER = _descriptor.EnumDescriptor(
  name='Order',
  full_name='containersai.common.QueryCondition.Order',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ASC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESC', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=697,
  serialized_end=723,
)
_sym_db.RegisterEnumDescriptor(_QUERYCONDITION_ORDER)


_TIMERANGE = _descriptor.Descriptor(
  name='TimeRange',
  full_name='containersai.common.TimeRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='containersai.common.TimeRange.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='containersai.common.TimeRange.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='containersai.common.TimeRange.timeout', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='containersai.common.TimeRange.step', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregate_function', full_name='containersai.common.TimeRange.aggregate_function', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apply_time', full_name='containersai.common.TimeRange.apply_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TIMERANGE_AGGREGATEFUNCTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=496,
)


_QUERYCONDITION = _descriptor.Descriptor(
  name='QueryCondition',
  full_name='containersai.common.QueryCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_range', full_name='containersai.common.QueryCondition.time_range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='containersai.common.QueryCondition.order', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='where_clause', full_name='containersai.common.QueryCondition.where_clause', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selects', full_name='containersai.common.QueryCondition.selects', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groups', full_name='containersai.common.QueryCondition.groups', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='containersai.common.QueryCondition.limit', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _QUERYCONDITION_ORDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=499,
  serialized_end=723,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='containersai.common.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='containersai.common.Query.database', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='containersai.common.Query.table', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expression', full_name='containersai.common.Query.expression', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition', full_name='containersai.common.Query.condition', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=725,
  serialized_end=841,
)


_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='containersai.common.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='containersai.common.Row.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='containersai.common.Row.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=843,
  serialized_end=906,
)


_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='containersai.common.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='containersai.common.Group.rows', index=0,
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
  serialized_start=908,
  serialized_end=955,
)


_READRAWDATA = _descriptor.Descriptor(
  name='ReadRawdata',
  full_name='containersai.common.ReadRawdata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='containersai.common.ReadRawdata.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='containersai.common.ReadRawdata.columns', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groups', full_name='containersai.common.ReadRawdata.groups', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rawdata', full_name='containersai.common.ReadRawdata.rawdata', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=958,
  serialized_end=1092,
)


_WRITERAWDATA = _descriptor.Descriptor(
  name='WriteRawdata',
  full_name='containersai.common.WriteRawdata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='containersai.common.WriteRawdata.database', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='containersai.common.WriteRawdata.table', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='containersai.common.WriteRawdata.columns', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rows', full_name='containersai.common.WriteRawdata.rows', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column_types', full_name='containersai.common.WriteRawdata.column_types', index=4,
      number=5, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_types', full_name='containersai.common.WriteRawdata.data_types', index=5,
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
  serialized_start=1095,
  serialized_end=1305,
)

_TIMERANGE.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMERANGE.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMERANGE.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMERANGE.fields_by_name['step'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TIMERANGE.fields_by_name['aggregate_function'].enum_type = _TIMERANGE_AGGREGATEFUNCTION
_TIMERANGE.fields_by_name['apply_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMERANGE_AGGREGATEFUNCTION.containing_type = _TIMERANGE
_QUERYCONDITION.fields_by_name['time_range'].message_type = _TIMERANGE
_QUERYCONDITION.fields_by_name['order'].enum_type = _QUERYCONDITION_ORDER
_QUERYCONDITION_ORDER.containing_type = _QUERYCONDITION
_QUERY.fields_by_name['condition'].message_type = _QUERYCONDITION
_ROW.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GROUP.fields_by_name['rows'].message_type = _ROW
_READRAWDATA.fields_by_name['query'].message_type = _QUERY
_READRAWDATA.fields_by_name['groups'].message_type = _GROUP
_WRITERAWDATA.fields_by_name['rows'].message_type = _ROW
_WRITERAWDATA.fields_by_name['column_types'].enum_type = common_dot_types__pb2._COLUMNTYPE
_WRITERAWDATA.fields_by_name['data_types'].enum_type = common_dot_types__pb2._DATATYPE
DESCRIPTOR.message_types_by_name['TimeRange'] = _TIMERANGE
DESCRIPTOR.message_types_by_name['QueryCondition'] = _QUERYCONDITION
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['Row'] = _ROW
DESCRIPTOR.message_types_by_name['Group'] = _GROUP
DESCRIPTOR.message_types_by_name['ReadRawdata'] = _READRAWDATA
DESCRIPTOR.message_types_by_name['WriteRawdata'] = _WRITERAWDATA
DESCRIPTOR.enum_types_by_name['DatabaseType'] = _DATABASETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeRange = _reflection.GeneratedProtocolMessageType('TimeRange', (_message.Message,), {
  'DESCRIPTOR' : _TIMERANGE,
  '__module__' : 'common.common_pb2'
  # @@protoc_insertion_point(class_scope:containersai.common.TimeRange)
  })
_sym_db.RegisterMessage(TimeRange)

QueryCondition = _reflection.GeneratedProtocolMessageType('QueryCondition', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONDITION,
  '__module__' : 'common.common_pb2'
  # @@protoc_insertion_point(class_scope:containersai.common.QueryCondition)
  })
_sym_db.RegisterMessage(QueryCondition)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'common.common_pb2'
  # @@protoc_insertion_point(class_scope:containersai.common.Query)
  })
_sym_db.RegisterMessage(Query)

Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {
  'DESCRIPTOR' : _ROW,
  '__module__' : 'common.common_pb2'
  # @@protoc_insertion_point(class_scope:containersai.common.Row)
  })
_sym_db.RegisterMessage(Row)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), {
  'DESCRIPTOR' : _GROUP,
  '__module__' : 'common.common_pb2'
  # @@protoc_insertion_point(class_scope:containersai.common.Group)
  })
_sym_db.RegisterMessage(Group)

ReadRawdata = _reflection.GeneratedProtocolMessageType('ReadRawdata', (_message.Message,), {
  'DESCRIPTOR' : _READRAWDATA,
  '__module__' : 'common.common_pb2'
  # @@protoc_insertion_point(class_scope:containersai.common.ReadRawdata)
  })
_sym_db.RegisterMessage(ReadRawdata)

WriteRawdata = _reflection.GeneratedProtocolMessageType('WriteRawdata', (_message.Message,), {
  'DESCRIPTOR' : _WRITERAWDATA,
  '__module__' : 'common.common_pb2'
  # @@protoc_insertion_point(class_scope:containersai.common.WriteRawdata)
  })
_sym_db.RegisterMessage(WriteRawdata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
