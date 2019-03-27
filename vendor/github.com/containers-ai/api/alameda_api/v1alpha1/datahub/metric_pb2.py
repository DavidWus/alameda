# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alameda_api/v1alpha1/datahub/metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from alameda_api.v1alpha1.datahub import metadata_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alameda_api/v1alpha1/datahub/metric.proto',
  package='containers_ai.alameda.v1alpha1.datahub',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)alameda_api/v1alpha1/datahub/metric.proto\x12&containers_ai.alameda.v1alpha1.datahub\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a+alameda_api/v1alpha1/datahub/metadata.proto\"h\n\x0f\x43ontainerMetric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12G\n\x0bmetric_data\x18\x02 \x03(\x0b\x32\x32.containers_ai.alameda.v1alpha1.datahub.MetricData\"\xb0\x01\n\tPodMetric\x12O\n\x0fnamespaced_name\x18\x01 \x01(\x0b\x32\x36.containers_ai.alameda.v1alpha1.datahub.NamespacedName\x12R\n\x11\x63ontainer_metrics\x18\x02 \x03(\x0b\x32\x37.containers_ai.alameda.v1alpha1.datahub.ContainerMetric\"c\n\nNodeMetric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12G\n\x0bmetric_data\x18\x02 \x03(\x0b\x32\x32.containers_ai.alameda.v1alpha1.datahub.MetricData\"s\n\x06Sample\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tnum_value\x18\x03 \x01(\t\"\x9a\x02\n\tTimeRange\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x04step\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12^\n\x11\x61ggregateFunction\x18\x04 \x01(\x0e\x32\x43.containers_ai.alameda.v1alpha1.datahub.TimeRange.AggregateFunction\"&\n\x11\x41ggregateFunction\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03MAX\x10\x01\"\x93\x01\n\nMetricData\x12G\n\x0bmetric_type\x18\x01 \x01(\x0e\x32\x32.containers_ai.alameda.v1alpha1.datahub.MetricType\x12<\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32..containers_ai.alameda.v1alpha1.datahub.Sample*U\n\nMetricType\x12\r\n\tUNDEFINED\x10\x00\x12 \n\x1c\x43PU_USAGE_SECONDS_PERCENTAGE\x10\x01\x12\x16\n\x12MEMORY_USAGE_BYTES\x10\x02\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,alameda__api_dot_v1alpha1_dot_datahub_dot_metadata__pb2.DESCRIPTOR,])

_METRICTYPE = _descriptor.EnumDescriptor(
  name='MetricType',
  full_name='containers_ai.alameda.v1alpha1.datahub.MetricType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CPU_USAGE_SECONDS_PERCENTAGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEMORY_USAGE_BYTES', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1133,
  serialized_end=1218,
)
_sym_db.RegisterEnumDescriptor(_METRICTYPE)

MetricType = enum_type_wrapper.EnumTypeWrapper(_METRICTYPE)
UNDEFINED = 0
CPU_USAGE_SECONDS_PERCENTAGE = 1
MEMORY_USAGE_BYTES = 2


_TIMERANGE_AGGREGATEFUNCTION = _descriptor.EnumDescriptor(
  name='AggregateFunction',
  full_name='containers_ai.alameda.v1alpha1.datahub.TimeRange.AggregateFunction',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=943,
  serialized_end=981,
)
_sym_db.RegisterEnumDescriptor(_TIMERANGE_AGGREGATEFUNCTION)


_CONTAINERMETRIC = _descriptor.Descriptor(
  name='ContainerMetric',
  full_name='containers_ai.alameda.v1alpha1.datahub.ContainerMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerMetric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_data', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerMetric.metric_data', index=1,
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
  serialized_start=195,
  serialized_end=299,
)


_PODMETRIC = _descriptor.Descriptor(
  name='PodMetric',
  full_name='containers_ai.alameda.v1alpha1.datahub.PodMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaced_name', full_name='containers_ai.alameda.v1alpha1.datahub.PodMetric.namespaced_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='container_metrics', full_name='containers_ai.alameda.v1alpha1.datahub.PodMetric.container_metrics', index=1,
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
  serialized_start=302,
  serialized_end=478,
)


_NODEMETRIC = _descriptor.Descriptor(
  name='NodeMetric',
  full_name='containers_ai.alameda.v1alpha1.datahub.NodeMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containers_ai.alameda.v1alpha1.datahub.NodeMetric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_data', full_name='containers_ai.alameda.v1alpha1.datahub.NodeMetric.metric_data', index=1,
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
  serialized_start=480,
  serialized_end=579,
)


_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='containers_ai.alameda.v1alpha1.datahub.Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='containers_ai.alameda.v1alpha1.datahub.Sample.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='containers_ai.alameda.v1alpha1.datahub.Sample.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_value', full_name='containers_ai.alameda.v1alpha1.datahub.Sample.num_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=581,
  serialized_end=696,
)


_TIMERANGE = _descriptor.Descriptor(
  name='TimeRange',
  full_name='containers_ai.alameda.v1alpha1.datahub.TimeRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='containers_ai.alameda.v1alpha1.datahub.TimeRange.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='containers_ai.alameda.v1alpha1.datahub.TimeRange.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='containers_ai.alameda.v1alpha1.datahub.TimeRange.step', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregateFunction', full_name='containers_ai.alameda.v1alpha1.datahub.TimeRange.aggregateFunction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=699,
  serialized_end=981,
)


_METRICDATA = _descriptor.Descriptor(
  name='MetricData',
  full_name='containers_ai.alameda.v1alpha1.datahub.MetricData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_type', full_name='containers_ai.alameda.v1alpha1.datahub.MetricData.metric_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='containers_ai.alameda.v1alpha1.datahub.MetricData.data', index=1,
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
  serialized_start=984,
  serialized_end=1131,
)

_CONTAINERMETRIC.fields_by_name['metric_data'].message_type = _METRICDATA
_PODMETRIC.fields_by_name['namespaced_name'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_metadata__pb2._NAMESPACEDNAME
_PODMETRIC.fields_by_name['container_metrics'].message_type = _CONTAINERMETRIC
_NODEMETRIC.fields_by_name['metric_data'].message_type = _METRICDATA
_SAMPLE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SAMPLE.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMERANGE.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMERANGE.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMERANGE.fields_by_name['step'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TIMERANGE.fields_by_name['aggregateFunction'].enum_type = _TIMERANGE_AGGREGATEFUNCTION
_TIMERANGE_AGGREGATEFUNCTION.containing_type = _TIMERANGE
_METRICDATA.fields_by_name['metric_type'].enum_type = _METRICTYPE
_METRICDATA.fields_by_name['data'].message_type = _SAMPLE
DESCRIPTOR.message_types_by_name['ContainerMetric'] = _CONTAINERMETRIC
DESCRIPTOR.message_types_by_name['PodMetric'] = _PODMETRIC
DESCRIPTOR.message_types_by_name['NodeMetric'] = _NODEMETRIC
DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.message_types_by_name['TimeRange'] = _TIMERANGE
DESCRIPTOR.message_types_by_name['MetricData'] = _METRICDATA
DESCRIPTOR.enum_types_by_name['MetricType'] = _METRICTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerMetric = _reflection.GeneratedProtocolMessageType('ContainerMetric', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERMETRIC,
  __module__ = 'alameda_api.v1alpha1.datahub.metric_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.ContainerMetric)
  ))
_sym_db.RegisterMessage(ContainerMetric)

PodMetric = _reflection.GeneratedProtocolMessageType('PodMetric', (_message.Message,), dict(
  DESCRIPTOR = _PODMETRIC,
  __module__ = 'alameda_api.v1alpha1.datahub.metric_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.PodMetric)
  ))
_sym_db.RegisterMessage(PodMetric)

NodeMetric = _reflection.GeneratedProtocolMessageType('NodeMetric', (_message.Message,), dict(
  DESCRIPTOR = _NODEMETRIC,
  __module__ = 'alameda_api.v1alpha1.datahub.metric_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.NodeMetric)
  ))
_sym_db.RegisterMessage(NodeMetric)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'alameda_api.v1alpha1.datahub.metric_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.Sample)
  ))
_sym_db.RegisterMessage(Sample)

TimeRange = _reflection.GeneratedProtocolMessageType('TimeRange', (_message.Message,), dict(
  DESCRIPTOR = _TIMERANGE,
  __module__ = 'alameda_api.v1alpha1.datahub.metric_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.TimeRange)
  ))
_sym_db.RegisterMessage(TimeRange)

MetricData = _reflection.GeneratedProtocolMessageType('MetricData', (_message.Message,), dict(
  DESCRIPTOR = _METRICDATA,
  __module__ = 'alameda_api.v1alpha1.datahub.metric_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.MetricData)
  ))
_sym_db.RegisterMessage(MetricData)


# @@protoc_insertion_point(module_scope)
