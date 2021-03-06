# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lab/lab.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lab/lab.proto',
  package='lab',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rlab/lab.proto\x12\x03lab\"/\n\x10RegNumberRequest\x12\x1b\n\x13registration_number\x18\x01 \x01(\t\"\"\n\x0eLabNameRequest\x12\x10\n\x08lab_name\x18\x01 \x01(\t\"\xa0\x03\n\x03Lab\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\x0e\n\x06region\x18\x04 \x01(\t\x12\x17\n\x0fstreet_address1\x18\x05 \x01(\t\x12\x17\n\x0fstreet_address2\x18\x06 \x01(\t\x12\x0f\n\x07zipcode\x18\x07 \x01(\t\x12\x1b\n\x13registration_number\x18\x08 \x01(\t\x12\r\n\x05\x65mail\x18\t \x01(\t\x12\x14\n\x0cphone_number\x18\n \x01(\t\x12\x18\n\x10proprietary_code\x18\x0b \x01(\t\x12\x14\n\x0ctt_compliant\x18\x0c \x01(\x08\x12\x0c\n\x04\x63ity\x18\r \x01(\t\x12$\n\x1csubmit_test_to_national_repo\x18\x0e \x01(\x08\x12\x13\n\x0bis_approved\x18\x0f \x01(\x08\x12\x0c\n\x04logo\x18\x10 \x01(\t\x12\x0b\n\x03\x62io\x18\x11 \x01(\t\x12\x0f\n\x07website\x18\x12 \x01(\t\x12\x10\n\x08linkedin\x18\x13 \x01(\t\x12\x0f\n\x07twitter\x18\x14 \x01(\t\x12\x11\n\tinstagram\x18\x15 \x01(\t2\x84\x01\n\rLabController\x12?\n\x1aGetLabByRegistrationNumber\x12\x15.lab.RegNumberRequest\x1a\x08.lab.Lab\"\x00\x12\x32\n\x0fGetLabByLabName\x12\x13.lab.LabNameRequest\x1a\x08.lab.Lab\"\x00\x62\x06proto3'
)




_REGNUMBERREQUEST = _descriptor.Descriptor(
  name='RegNumberRequest',
  full_name='lab.RegNumberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration_number', full_name='lab.RegNumberRequest.registration_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=69,
)


_LABNAMEREQUEST = _descriptor.Descriptor(
  name='LabNameRequest',
  full_name='lab.LabNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lab_name', full_name='lab.LabNameRequest.lab_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=71,
  serialized_end=105,
)


_LAB = _descriptor.Descriptor(
  name='Lab',
  full_name='lab.Lab',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='lab.Lab.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='lab.Lab.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='lab.Lab.country', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='lab.Lab.region', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='street_address1', full_name='lab.Lab.street_address1', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='street_address2', full_name='lab.Lab.street_address2', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zipcode', full_name='lab.Lab.zipcode', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registration_number', full_name='lab.Lab.registration_number', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='lab.Lab.email', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='lab.Lab.phone_number', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proprietary_code', full_name='lab.Lab.proprietary_code', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tt_compliant', full_name='lab.Lab.tt_compliant', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='lab.Lab.city', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submit_test_to_national_repo', full_name='lab.Lab.submit_test_to_national_repo', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_approved', full_name='lab.Lab.is_approved', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logo', full_name='lab.Lab.logo', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bio', full_name='lab.Lab.bio', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='website', full_name='lab.Lab.website', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='linkedin', full_name='lab.Lab.linkedin', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='twitter', full_name='lab.Lab.twitter', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instagram', full_name='lab.Lab.instagram', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=108,
  serialized_end=524,
)

DESCRIPTOR.message_types_by_name['RegNumberRequest'] = _REGNUMBERREQUEST
DESCRIPTOR.message_types_by_name['LabNameRequest'] = _LABNAMEREQUEST
DESCRIPTOR.message_types_by_name['Lab'] = _LAB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegNumberRequest = _reflection.GeneratedProtocolMessageType('RegNumberRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGNUMBERREQUEST,
  '__module__' : 'lab.lab_pb2'
  # @@protoc_insertion_point(class_scope:lab.RegNumberRequest)
  })
_sym_db.RegisterMessage(RegNumberRequest)

LabNameRequest = _reflection.GeneratedProtocolMessageType('LabNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _LABNAMEREQUEST,
  '__module__' : 'lab.lab_pb2'
  # @@protoc_insertion_point(class_scope:lab.LabNameRequest)
  })
_sym_db.RegisterMessage(LabNameRequest)

Lab = _reflection.GeneratedProtocolMessageType('Lab', (_message.Message,), {
  'DESCRIPTOR' : _LAB,
  '__module__' : 'lab.lab_pb2'
  # @@protoc_insertion_point(class_scope:lab.Lab)
  })
_sym_db.RegisterMessage(Lab)



_LABCONTROLLER = _descriptor.ServiceDescriptor(
  name='LabController',
  full_name='lab.LabController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=527,
  serialized_end=659,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLabByRegistrationNumber',
    full_name='lab.LabController.GetLabByRegistrationNumber',
    index=0,
    containing_service=None,
    input_type=_REGNUMBERREQUEST,
    output_type=_LAB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLabByLabName',
    full_name='lab.LabController.GetLabByLabName',
    index=1,
    containing_service=None,
    input_type=_LABNAMEREQUEST,
    output_type=_LAB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LABCONTROLLER)

DESCRIPTOR.services_by_name['LabController'] = _LABCONTROLLER

# @@protoc_insertion_point(module_scope)
