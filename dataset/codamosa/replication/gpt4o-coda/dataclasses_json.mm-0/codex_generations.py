

# Generated at 2024-06-01 17:49:27.415176
# Unit test for function schema
def test_schema():    from dataclasses import dataclass, field

# Generated at 2024-06-01 17:49:33.335815
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class TestClass:
        id: int
        name: str
        timestamp: datetime

    class TestMixin:
        pass

    result = schema(TestClass, TestMixin, infer_missing=True)
    assert 'id' in result
    assert isinstance(result['id'], fields.Int)
    assert 'name' in result
    assert isinstance(result['name'], fields.Str)
    assert 'timestamp' in result
    assert isinstance(result['timestamp'], _TimestampField)

    @dataclass_json
    @dataclass
    class NestedClass:
        nested: TestClass

    result = schema(NestedClass, TestMixin, infer_missing=True)
    assert 'nested' in result
    assert isinstance(result['nested'], fields.Nested)


# Generated at 2024-06-01 17:49:36.024049
# Unit test for method dumps of class SchemaF

# Generated at 2024-06-01 17:49:40.406848
# Unit test for method dump of class SchemaF

# Generated at 2024-06-01 17:49:43.293228
# Unit test for method loads of class SchemaF

# Generated at 2024-06-01 17:49:47.161181
# Unit test for function build_schema
def test_build_schema():    from marshmallow import Schema, fields

# Generated at 2024-06-01 17:49:50.265941
# Unit test for function build_schema
def test_build_schema():    from marshmallow import Schema, fields

# Generated at 2024-06-01 17:49:53.007028
# Unit test for function build_schema

# Generated at 2024-06-01 17:49:56.579065
# Unit test for method loads of class SchemaF

# Generated at 2024-06-01 17:49:59.558829
# Unit test for function build_schema

# Generated at 2024-06-01 17:50:15.964455
# Unit test for method loads of class SchemaF

# Generated at 2024-06-01 17:50:19.288210
# Unit test for method dumps of class SchemaF

# Generated at 2024-06-01 17:50:22.481725
# Unit test for function schema
def test_schema():    from dataclasses import dataclass, field as dc_field

# Generated at 2024-06-01 17:50:26.949024
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from marshmallow import Schema, fields
    from marshmallow_enum import EnumField
    from enum import Enum

    class MyEnum(Enum):
        A = "A"
        B = "B"

    @dataclass
    class NestedDataClass:
        value: int

    @dataclass
    class MyDataClass:
        enum_field: MyEnum
        nested_field: NestedDataClass
        optional_field: typing.Optional[int]
        list_field: typing.List[int]

    class NestedDataClassSchema(Schema):
        value = fields.Int()

    class MyDataClassSchema(Schema):
        enum_field = EnumField(MyEnum, by_value=True)
        nested_field = fields.Nested(NestedDataClassSchema)
        optional_field = fields.Int(allow_none=True)
        list_field = fields.List(fields.Int())

    NestedDataClass.schema = NestedDataClassSchema
    MyDataClass.schema = MyDataClassSchema

# Generated at 2024-06-01 17:50:29.909697
# Unit test for function build_schema

# Generated at 2024-06-01 17:50:38.878499
# Unit test for function build_schema
def test_build_schema():    from marshmallow import Schema, fields

# Generated at 2024-06-01 17:50:41.870284
# Unit test for function build_schema
def test_build_schema():    from dataclasses import dataclass, field as dc_field

# Generated at 2024-06-01 17:50:45.038697
# Unit test for method loads of class SchemaF

# Generated at 2024-06-01 17:50:47.877836
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from marshmallow import Schema, fields
    from marshmallow_enum import EnumField
    from enum import Enum

    class TestEnum(Enum):
        OPTION_A = "option_a"
        OPTION_B = "option_b"

    @dataclass
    class NestedDataClass:
        value: int

    @dataclass
    class TestDataClass:
        enum_field: TestEnum
        nested_field: NestedDataClass
        optional_field: typing.Optional[str]
        list_field: typing.List[int]

    class NestedDataClassSchema(Schema):
        value = fields.Int()

    class TestDataClassSchema(Schema):
        enum_field = EnumField(TestEnum, by_value=True)
        nested_field = fields.Nested(NestedDataClassSchema)
        optional_field = fields.Str(allow_none=True)
        list_field = fields.List(fields.Int())

    NestedDataClass.schema = NestedDataClassSchema

# Generated at 2024-06-01 17:50:50.960864
# Unit test for constructor of class _IsoField

# Generated at 2024-06-01 17:51:16.703711
# Unit test for function build_schema

# Generated at 2024-06-01 17:51:18.997992
# Unit test for method dumps of class SchemaF

# Generated at 2024-06-01 17:51:21.632820
# Unit test for function build_schema

# Generated at 2024-06-01 17:51:25.730506
# Unit test for function build_schema

# Generated at 2024-06-01 17:51:28.471565
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField(required=True)
    assert field.required is True

    field = _TimestampField(required=False)
    assert field.required is False

    field = _TimestampField()
    assert field.required is False

    try:
        field._serialize(None, None, None)
    except ValidationError as e:
        assert str(e) == field.default_error_messages["required"]

    try:
        field._deserialize(None, None, None)
    except ValidationError as e:
        assert str(e) == field.default_error_messages["required"]

    timestamp = datetime.now().timestamp()
    dt = datetime.fromtimestamp(timestamp)
    assert field._serialize(dt, None, None) == timestamp
    assert field._deserialize(timestamp, None, None) == dt

# Generated at 2024-06-01 17:51:31.583024
# Unit test for function build_type
def test_build_type():    from dataclasses import dataclass

# Generated at 2024-06-01 17:51:35.146068
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field as dc_field
    from marshmallow import Schema, fields
    from marshmallow.exceptions import ValidationError
    from marshmallow_enum import EnumField
    from datetime import datetime
    from decimal import Decimal
    from uuid import UUID
    from enum import Enum

    class TestEnum(Enum):
        OPTION_A = "A"
        OPTION_B = "B"

    @dataclass
    class NestedDataClass:
        nested_field: int

    @dataclass
    class TestDataClass:
        int_field: int
        str_field: str
        float_field: float
        bool_field: bool
        datetime_field: datetime
        uuid_field: UUID
        decimal_field: Decimal
        enum_field: TestEnum
        nested_dataclass_field: NestedDataClass
        optional_field: typing.Optional[str] = None

    class TestMixin:
        pass


# Generated at 2024-06-01 17:51:38.781699
# Unit test for constructor of class _IsoField

# Generated at 2024-06-01 17:51:42.031994
# Unit test for method load of class SchemaF

# Generated at 2024-06-01 17:51:45.127039
# Unit test for function build_type
def test_build_type():    from dataclasses import dataclass

# Generated at 2024-06-01 17:52:35.425082
# Unit test for method load of class SchemaF

# Generated at 2024-06-01 17:52:39.205018
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField(required=True)
    assert field.required is True

    field = _TimestampField(required=False)
    assert field.required is False

    field = _TimestampField()
    assert field.required is False

    try:
        field._serialize(None, None, None)
    except ValidationError:
        pass
    else:
        assert False, "Expected ValidationError"

    try:
        field._deserialize(None, None, None)
    except ValidationError:
        pass
    else:
        assert False, "Expected ValidationError"

    dt = datetime(2023, 1, 1)
    assert field._serialize(dt, None, None) == dt.timestamp()

    timestamp = 1672531200
    assert field._deserialize(timestamp, None, None) == _timestamp_to_dt_aware(timestamp)

# Generated at 2024-06-01 17:52:41.932889
# Unit test for function build_schema

# Generated at 2024-06-01 17:52:44.306090
# Unit test for method dumps of class SchemaF

# Generated at 2024-06-01 17:52:50.898903
# Unit test for function schema
def test_schema():    from dataclasses import dataclass, field

# Generated at 2024-06-01 17:52:53.178149
# Unit test for method dumps of class SchemaF

# Generated at 2024-06-01 17:52:55.940363
# Unit test for method loads of class SchemaF

# Generated at 2024-06-01 17:53:00.176365
# Unit test for function build_schema
def test_build_schema():    from marshmallow import Schema, fields

# Generated at 2024-06-01 17:53:02.735326
# Unit test for method loads of class SchemaF

# Generated at 2024-06-01 17:53:06.006175
# Unit test for function build_type
def test_build_type():
    from dataclasses import dataclass
    from marshmallow import Schema, fields
    from marshmallow_enum import EnumField
    from enum import Enum

    class TestEnum(Enum):
        OPTION_A = "A"
        OPTION_B = "B"

    @dataclass
    class NestedDataClass:
        value: int

    @dataclass
    class TestDataClass:
        name: str
        age: int
        nested: NestedDataClass
        enum_field: TestEnum

    class NestedDataClassSchema(Schema):
        value = fields.Int()

    class TestDataClassSchema(Schema):
        name = fields.Str()
        age = fields.Int()
        nested = fields.Nested(NestedDataClassSchema)
        enum_field = EnumField(TestEnum, by_value=True)

    NestedDataClass.schema = NestedDataClassSchema
    TestDataClass.schema = TestDataClassSchema


# Generated at 2024-06-01 17:54:40.252874
# Unit test for function build_schema

# Generated at 2024-06-01 17:54:43.425438
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field as dc_field
    from marshmallow import Schema, fields
    from marshmallow.exceptions import ValidationError
    from marshmallow_enum import EnumField
    from datetime import datetime
    from decimal import Decimal
    from uuid import UUID
    from enum import Enum
    import typing

    class TestEnum(Enum):
        OPTION_A = "A"
        OPTION_B = "B"

    @dataclass
    class TestDataClass:
        id: int
        name: str
        timestamp: datetime
        uuid: UUID
        amount: Decimal
        enum_field: TestEnum
        optional_field: typing.Optional[str] = None

    class TestDataClassSchema(Schema):
        id = fields.Int(required=True)
        name = fields.Str(required=True)
        timestamp = _TimestampField(required=True)
        uuid = fields.UUID(required=True)
        amount = fields.Decimal(required=True)

# Generated at 2024-06-01 17:54:46.101831
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field as dc_field
    from marshmallow import Schema, fields
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class TestClass:
        id: int
        name: str
        timestamp: datetime = dc_field(default_factory=datetime.now)

    class TestClassSchema(Schema):
        id = fields.Int()
        name = fields.Str()
        timestamp = _TimestampField()

    schema_instance = schema(TestClass, dataclass_json, infer_missing=True)
    expected_schema = {
        'id': fields.Int(),
        'name': fields.Str(),
        'timestamp': _TimestampField()
    }

    assert schema_instance.keys() == expected_schema.keys()
    for key in schema_instance:
        assert isinstance(schema_instance[key], type(expected_schema[key]))

# Generated at 2024-06-01 17:54:49.093254
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class TestClass:
        id: int
        name: str
        timestamp: datetime

    class TestMixin:
        pass

    result = schema(TestClass, TestMixin, infer_missing=True)
    assert 'id' in result
    assert isinstance(result['id'], fields.Int)
    assert 'name' in result
    assert isinstance(result['name'], fields.Str)
    assert 'timestamp' in result
    assert isinstance(result['timestamp'], _TimestampField)

    @dataclass_json
    @dataclass
    class NestedClass:
        nested: TestClass

    result = schema(NestedClass, TestMixin, infer_missing=True)
    assert 'nested' in result
    assert isinstance(result['nested'], fields.Nested)


# Generated at 2024-06-01 17:54:50.117613
# Unit test for constructor of class _TimestampField
def test__TimestampField():
    field = _TimestampField(required=True)
    assert field.required is True

    field = _TimestampField(required=False)
    assert field.required is False

    field = _TimestampField()
    assert field.required is False

# Generated at 2024-06-01 17:54:53.000685
# Unit test for function schema
def test_schema():    from dataclasses import dataclass, field

# Generated at 2024-06-01 17:54:56.015039
# Unit test for constructor of class _IsoField

# Generated at 2024-06-01 17:54:59.529165
# Unit test for function build_schema

# Generated at 2024-06-01 17:55:01.830128
# Unit test for method dump of class SchemaF

# Generated at 2024-06-01 17:55:04.728109
# Unit test for method dumps of class SchemaF

# Generated at 2024-06-01 17:59:02.622009
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass, field as dc_field
    from dataclasses_json import dataclass_json
    from marshmallow import fields

    @dataclass_json
    @dataclass
    class Nested:
        value: int

    @dataclass_json
    @dataclass
    class Example:
        id: int
        name: str
        nested: Nested

    class ExampleSchema(Schema):
        id = fields.Int()
        name = fields.Str()
        nested = fields.Nested(Nested.schema())

    def test_schema():
        example_schema = schema(Example, dataclass_json, infer_missing=False)
        expected_schema = {
            'id': fields.Int(),
            'name': fields.Str(),
            'nested': fields.Nested(Nested.schema())
        }

        assert isinstance(example_schema, dict)
        assert set(example_schema.keys()) == set(expected_schema.keys())

# Generated at 2024-06-01 17:59:07.509552
# Unit test for function build_type
def test_build_type():    from dataclasses import dataclass

# Generated at 2024-06-01 17:59:12.453083
# Unit test for function schema
def test_schema():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json

    @dataclass_json
    @dataclass
    class TestClass:
        id: int
        name: str
        timestamp: datetime

    class TestMixin:
        pass

    result = schema(TestClass, TestMixin, infer_missing=True)
    assert 'id' in result
    assert isinstance(result['id'], fields.Int)
    assert 'name' in result
    assert isinstance(result['name'], fields.Str)
    assert 'timestamp' in result
    assert isinstance(result['timestamp'], _TimestampField)

    @dataclass_json
    @dataclass
    class NestedClass:
        nested: TestClass

    result = schema(NestedClass, TestMixin, infer_missing=True)
    assert 'nested' in result
    assert isinstance(result['nested'], fields.Nested)
