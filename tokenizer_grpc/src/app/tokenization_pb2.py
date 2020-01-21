# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tokenization.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="tokenization.proto",
    package="sample",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x12tokenization.proto\x12\x06sample"3\n\x0fTokenizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\npos_filter\x18\x02 \x03(\t""\n\x10TokenizeResponse\x12\x0e\n\x06tokens\x18\x01 \x03(\t"\xca\x01\n\x0bTokenDetail\x12\x0f\n\x07surface\x18\x01 \x01(\t\x12\x0b\n\x03pos\x18\x02 \x01(\t\x12\x14\n\x0cpos_detail_1\x18\x03 \x01(\t\x12\x14\n\x0cpos_detail_2\x18\x04 \x01(\t\x12\x14\n\x0cpos_detail_3\x18\x05 \x01(\t\x12\x0b\n\x03toc\x18\x06 \x01(\t\x12\x13\n\x0b\x63onjugation\x18\x07 \x01(\t\x12\x15\n\roriginal_form\x18\x08 \x01(\t\x12\x0f\n\x07reading\x18\t \x01(\t\x12\x11\n\tpronounce\x18\n \x01(\t"=\n\x16TokenizeDetailResponse\x12#\n\x06tokens\x18\x01 \x03(\x0b\x32\x13.sample.TokenDetail2c\n\x0fTokenizerStream\x12P\n\x15TokenizerStreamServer\x12\x17.sample.TokenizeRequest\x1a\x18.sample.TokenizeResponse"\x00(\x01\x30\x01\x32S\n\tTokenizer\x12\x46\n\x0fTokenizerServer\x12\x17.sample.TokenizeRequest\x1a\x18.sample.TokenizeResponse"\x00\x32u\n\x15TokenizerDetailStream\x12\\\n\x1bTokenizerDetailStreamServer\x12\x17.sample.TokenizeRequest\x1a\x1e.sample.TokenizeDetailResponse"\x00(\x01\x30\x01\x32\x65\n\x0fTokenizerDetail\x12R\n\x15TokenizerDetailServer\x12\x17.sample.TokenizeRequest\x1a\x1e.sample.TokenizeDetailResponse"\x00\x62\x06proto3'
    ),
)


_TOKENIZEREQUEST = _descriptor.Descriptor(
    name="TokenizeRequest",
    full_name="sample.TokenizeRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="text",
            full_name="sample.TokenizeRequest.text",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pos_filter",
            full_name="sample.TokenizeRequest.pos_filter",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=30,
    serialized_end=81,
)


_TOKENIZERESPONSE = _descriptor.Descriptor(
    name="TokenizeResponse",
    full_name="sample.TokenizeResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="tokens",
            full_name="sample.TokenizeResponse.tokens",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=83,
    serialized_end=117,
)


_TOKENDETAIL = _descriptor.Descriptor(
    name="TokenDetail",
    full_name="sample.TokenDetail",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="surface",
            full_name="sample.TokenDetail.surface",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pos",
            full_name="sample.TokenDetail.pos",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pos_detail_1",
            full_name="sample.TokenDetail.pos_detail_1",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pos_detail_2",
            full_name="sample.TokenDetail.pos_detail_2",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pos_detail_3",
            full_name="sample.TokenDetail.pos_detail_3",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="toc",
            full_name="sample.TokenDetail.toc",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="conjugation",
            full_name="sample.TokenDetail.conjugation",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="original_form",
            full_name="sample.TokenDetail.original_form",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="reading",
            full_name="sample.TokenDetail.reading",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pronounce",
            full_name="sample.TokenDetail.pronounce",
            index=9,
            number=10,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=120,
    serialized_end=322,
)


_TOKENIZEDETAILRESPONSE = _descriptor.Descriptor(
    name="TokenizeDetailResponse",
    full_name="sample.TokenizeDetailResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="tokens",
            full_name="sample.TokenizeDetailResponse.tokens",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=324,
    serialized_end=385,
)

_TOKENIZEDETAILRESPONSE.fields_by_name["tokens"].message_type = _TOKENDETAIL
DESCRIPTOR.message_types_by_name["TokenizeRequest"] = _TOKENIZEREQUEST
DESCRIPTOR.message_types_by_name["TokenizeResponse"] = _TOKENIZERESPONSE
DESCRIPTOR.message_types_by_name["TokenDetail"] = _TOKENDETAIL
DESCRIPTOR.message_types_by_name["TokenizeDetailResponse"] = _TOKENIZEDETAILRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenizeRequest = _reflection.GeneratedProtocolMessageType(
    "TokenizeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TOKENIZEREQUEST,
        "__module__": "tokenization_pb2"
        # @@protoc_insertion_point(class_scope:sample.TokenizeRequest)
    },
)
_sym_db.RegisterMessage(TokenizeRequest)

TokenizeResponse = _reflection.GeneratedProtocolMessageType(
    "TokenizeResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TOKENIZERESPONSE,
        "__module__": "tokenization_pb2"
        # @@protoc_insertion_point(class_scope:sample.TokenizeResponse)
    },
)
_sym_db.RegisterMessage(TokenizeResponse)

TokenDetail = _reflection.GeneratedProtocolMessageType(
    "TokenDetail",
    (_message.Message,),
    {
        "DESCRIPTOR": _TOKENDETAIL,
        "__module__": "tokenization_pb2"
        # @@protoc_insertion_point(class_scope:sample.TokenDetail)
    },
)
_sym_db.RegisterMessage(TokenDetail)

TokenizeDetailResponse = _reflection.GeneratedProtocolMessageType(
    "TokenizeDetailResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TOKENIZEDETAILRESPONSE,
        "__module__": "tokenization_pb2"
        # @@protoc_insertion_point(class_scope:sample.TokenizeDetailResponse)
    },
)
_sym_db.RegisterMessage(TokenizeDetailResponse)


_TOKENIZERSTREAM = _descriptor.ServiceDescriptor(
    name="TokenizerStream",
    full_name="sample.TokenizerStream",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=387,
    serialized_end=486,
    methods=[
        _descriptor.MethodDescriptor(
            name="TokenizerStreamServer",
            full_name="sample.TokenizerStream.TokenizerStreamServer",
            index=0,
            containing_service=None,
            input_type=_TOKENIZEREQUEST,
            output_type=_TOKENIZERESPONSE,
            serialized_options=None,
        )
    ],
)
_sym_db.RegisterServiceDescriptor(_TOKENIZERSTREAM)

DESCRIPTOR.services_by_name["TokenizerStream"] = _TOKENIZERSTREAM


_TOKENIZER = _descriptor.ServiceDescriptor(
    name="Tokenizer",
    full_name="sample.Tokenizer",
    file=DESCRIPTOR,
    index=1,
    serialized_options=None,
    serialized_start=488,
    serialized_end=571,
    methods=[
        _descriptor.MethodDescriptor(
            name="TokenizerServer",
            full_name="sample.Tokenizer.TokenizerServer",
            index=0,
            containing_service=None,
            input_type=_TOKENIZEREQUEST,
            output_type=_TOKENIZERESPONSE,
            serialized_options=None,
        )
    ],
)
_sym_db.RegisterServiceDescriptor(_TOKENIZER)

DESCRIPTOR.services_by_name["Tokenizer"] = _TOKENIZER


_TOKENIZERDETAILSTREAM = _descriptor.ServiceDescriptor(
    name="TokenizerDetailStream",
    full_name="sample.TokenizerDetailStream",
    file=DESCRIPTOR,
    index=2,
    serialized_options=None,
    serialized_start=573,
    serialized_end=690,
    methods=[
        _descriptor.MethodDescriptor(
            name="TokenizerDetailStreamServer",
            full_name="sample.TokenizerDetailStream.TokenizerDetailStreamServer",
            index=0,
            containing_service=None,
            input_type=_TOKENIZEREQUEST,
            output_type=_TOKENIZEDETAILRESPONSE,
            serialized_options=None,
        )
    ],
)
_sym_db.RegisterServiceDescriptor(_TOKENIZERDETAILSTREAM)

DESCRIPTOR.services_by_name["TokenizerDetailStream"] = _TOKENIZERDETAILSTREAM


_TOKENIZERDETAIL = _descriptor.ServiceDescriptor(
    name="TokenizerDetail",
    full_name="sample.TokenizerDetail",
    file=DESCRIPTOR,
    index=3,
    serialized_options=None,
    serialized_start=692,
    serialized_end=793,
    methods=[
        _descriptor.MethodDescriptor(
            name="TokenizerDetailServer",
            full_name="sample.TokenizerDetail.TokenizerDetailServer",
            index=0,
            containing_service=None,
            input_type=_TOKENIZEREQUEST,
            output_type=_TOKENIZEDETAILRESPONSE,
            serialized_options=None,
        )
    ],
)
_sym_db.RegisterServiceDescriptor(_TOKENIZERDETAIL)

DESCRIPTOR.services_by_name["TokenizerDetail"] = _TOKENIZERDETAIL

# @@protoc_insertion_point(module_scope)
