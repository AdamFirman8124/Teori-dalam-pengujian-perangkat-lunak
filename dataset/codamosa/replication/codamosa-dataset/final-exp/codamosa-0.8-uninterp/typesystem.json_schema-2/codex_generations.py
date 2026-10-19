

# Generated at 2022-06-14 14:35:17.899938
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {"allOf": [{"type": "string"}, {"enum": ["yes", "no"]}], "default": "yes"}
    field = all_of_from_json_schema(data, definitions=SchemaDefinitions())
    assert field.validate("yes") == "yes"
    assert field.validate("no") == "no"
    assert field.validate("maybe") is None
    assert field.validate(123) is None



# Generated at 2022-06-14 14:35:28.476401
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    data = {'enum': [1, 2, 3], "default": 2}
    field = enum_from_json_schema(data, None)
    assert field.validate(1) == 1
    assert field.validate(2) == 2
    assert field.validate(3) == 3
    assert field.validate(4) == {'enum': [1, 2, 3]}
    assert field.to_python(1) == 1
    assert field.to_python(2) == 2
    assert field.to_python(3) == 3
    assert field.to_python(4) == {'enum': [1, 2, 3]}
    assert field.to_primitive(1) == 1
    assert field.to_primitive(2) == 2
    assert field.to_primitive(3) == 3


# Generated at 2022-06-14 14:35:36.012334
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    from typesystem import fields

    data = {
        "$ref": "#/definitions/foo"
    }
    assert isinstance(ref_from_json_schema(data, definitions={}), fields.Reference)
    assert ref_from_json_schema(data, definitions={}).to == "#/definitions/foo"
    assert ref_from_json_schema(data, definitions={}).definitions == {}
    data = {
        "$ref": "foo"
    }
    assert ref_from_json_schema(data, definitions={}).to == "foo"



# Generated at 2022-06-14 14:35:40.352992
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    not_json_schema = {
        "type":
        "object",
        "properties": {
            "nom_de_famille": {
                "type": "string",
                "minLength": 5,
                "maxLength": 10
            }
        }
    }
    expected_field = Not(
        negated=Object(
            properties={
                "nom_de_famille": String(
                    min_length=5, max_length=10, allow_blank=False)
            },
            additional_properties=True,
            allow_null=True))

    assert (not_from_json_schema(not_json_schema)) == expected_field



# Generated at 2022-06-14 14:35:46.672871
# Unit test for function get_valid_types
def test_get_valid_types():
    assert get_valid_types({"type": "integer"}) == ({"integer"}, False)
    assert get_valid_types({"type": "number"}) == ({"number"}, False)
    assert get_valid_types({"type": "number", "enum": [1, 2, "a"]}) == ({"number"}, False)
    assert get_valid_types({"type": "null"}) == ({"null"}, True)
    assert get_valid_types({"type": ["null", "string"]}) == ({"string"}, True)
    assert get_valid_types({"type": ["null", "integer", "string"]}) == (
        {"integer", "string"},
        True,
    )



# Generated at 2022-06-14 14:35:56.182938
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = {
        "default": True,
        "type": "boolean",
        "not": {
            "type": "boolean",
            "not": {
                "type": "boolean",
                "not": {
                    "type": "boolean",
                    "not": {
                        "type": "boolean",
                        "default": True,
                        "const": True,
                    }
                }
            }
        }
    }
    field = not_from_json_schema(schema, None)
    assert field.validate.__name__ == 'const_validate'


# Generated at 2022-06-14 14:36:07.632393
# Unit test for function any_of_from_json_schema

# Generated at 2022-06-14 14:36:15.719292
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    from typesystem.schemas import SchemaDefinitions
    from typesystem.utils import get_function_arguments  # type: ignore
    for definition in get_function_arguments(ref_from_json_schema):
        assert isinstance(definition, Field)
        assert isinstance(definition, Reference)
        assert definition.to.startswith("#/")

    definitions = SchemaDefinitions()
    definitions["#/definitions/foo"] = Field(name="foo")
    reference = ref_from_json_schema({"$ref": "#/definitions/foo"}, definitions=definitions)

    assert isinstance(reference, Field)
    assert isinstance(reference, Reference)
    assert reference.to == "#/definitions/foo"



# Generated at 2022-06-14 14:36:27.336081
# Unit test for function to_json_schema
def test_to_json_schema():
    from .test_objects import TestSchema, TestSchema2
    from .test_examples import StringWithoutDigits

    # A simple example

# Generated at 2022-06-14 14:36:34.212575
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema({
    "allOf": [
      {
        "type": "integer",
        "maximum": 100,
        "default": 1
      },
      {
        "type": "integer",
        "minimum": 10,
        "default": 1
      }
    ],
    "default": 1
  }, definitions=None) == AllOf(all_of=[Integer(maximum=100, default=1), Integer(minimum=10, default=1)], default=1)



# Generated at 2022-06-14 14:37:20.168518
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {
        "oneOf": [
            {
                "type": "integer",
                "default": "1",
                "minimum": 1,
                "maximum": 10
            },
            {
                "type": "string",
                "default": "name",
                "minLength": 3,
                "maxLength": 16,
                "format": "email"
            }
        ]
    }
    definitions = SchemaDefinitions()
    one_of = one_of_from_json_schema(data, definitions=definitions)

# Generated at 2022-06-14 14:37:31.334643
# Unit test for function from_json_schema

# Generated at 2022-06-14 14:37:34.754778
# Unit test for function to_json_schema
def test_to_json_schema():
    from .test_schema import all_fields

    for field, json_data in all_fields.items():
        if isinstance(field, String) and field.allow_blank:
            continue
        result = to_json_schema(field)
        assert json.dumps(result, sort_keys=True) == json.dumps(
            json_data, sort_keys=True
        )



# Generated at 2022-06-14 14:37:46.422052
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String.allow_null()) == {
        "type": "string"
    }

    assert to_json_schema(
        IfThenElse(
            if_clause=String(allow_null=True),
            then_clause=String.allow_null().allow_blank(False),
        )
    ) == {
        "type": ["string", "null"],
        "if": {"type": ["string", "null"]},
        "then": {"type": ["string", "null"], "minLength": 1},
    }


# Generated at 2022-06-14 14:37:57.711154
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    with pytest.raises(AssertionError):
        all_of_from_json_schema(data="oneOf", definitions=definitions)
    assert one_of_from_json_schema(data={"oneOf": "test"}, definitions=definitions) == ["test"]
    # assert one_of_from_json_schema(data={"oneOf": "test_123"}, definitions=definitions) == [
    #     "test_123"
    # ]
    assert one_of_from_json_schema(data=["oneOf"], definitions=definitions) == ["oneOf"]
    assert one_of_from_json_schema(data=[], definitions=definitions) == []


# Generated at 2022-06-14 14:38:03.359406
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    json_schema = {
        "anyOf": [
            {"type": "string", "minLength": 1, "maxLength": 10},
            {"type": "integer", "minimum": 1, "maximum": 100},
        ]
    }
    field = any_of_from_json_schema(json_schema, SchemaDefinitions())



# Generated at 2022-06-14 14:38:10.976801
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    assert any_of_from_json_schema({'anyOf': [{'$ref': '#/definitions/Percent'}, {'$ref': '#/definitions/Amount'}]},
    definitions={'Percent': Integer(minimum=0, maximum=100), 'Amount': Integer(minimum=0)}) ==  \
    Union(any_of=[Reference(to='#/definitions/Percent', definitions={'Percent': Integer(minimum=0, maximum=100), 'Amount': Integer(minimum=0)}),
    Reference(to='#/definitions/Amount', definitions={'Percent': Integer(minimum=0, maximum=100), 'Amount': Integer(minimum=0)})])



# Generated at 2022-06-14 14:38:22.537232
# Unit test for function type_from_json_schema

# Generated at 2022-06-14 14:38:33.322096
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert issubclass(IfThenElse, Field)
    assert issubclass(IfThenElse, HasDefault)
    assert issubclass(IfThenElse, HasDefault)
    assert issubclass(IfThenElse, HasMinimum)
    assert issubclass(IfThenElse, HasMaximum)
    assert issubclass(IfThenElse, HasExclusiveMinimum)
    assert issubclass(IfThenElse, HasExclusiveMaximum)
    assert issubclass(IfThenElse, HasMultipleOf)
    assert issubclass(IfThenElse, HasPattern)
    assert issubclass(IfThenElse, HasFormat)
    assert issubclass(IfThenElse, HasMinLength)
    assert issubclass(IfThenElse, HasMaxLength)
    assert issubclass(IfThenElse, HasMinItems)

# Generated at 2022-06-14 14:38:37.631699
# Unit test for function one_of_from_json_schema

# Generated at 2022-06-14 14:39:20.927447
# Unit test for function if_then_else_from_json_schema

# Generated at 2022-06-14 14:39:28.816070
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    input_data = {'if': {'type': 'object', 'properties': {'id': {'type': 'integer'}}}, 'then': {'type': 'string'}, 'else': {'type': 'number'}}
    definitions = SchemaDefinitions()
    field = if_then_else_from_json_schema(input_data, definitions=definitions)

    class TestData:
        def __init__(self, data: object, valid: bool) -> None:
            self.data = data
            self.valid = valid

# Generated at 2022-06-14 14:39:36.683820
# Unit test for function if_then_else_from_json_schema

# Generated at 2022-06-14 14:39:45.367224
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    schema = {
        "if": {"type": "integer"},
        "then": {"type": "number"},
    }
    result = if_then_else_from_json_schema(schema, definitions=None)
    assert result.default is NO_DEFAULT
    assert result.if_clause.validate(1) == 1
    assert result.if_clause.validate("foo") == "foo"
    assert result.then_clause.validate("bar") == "bar"


# Generated at 2022-06-14 14:39:54.135543
# Unit test for function if_then_else_from_json_schema

# Generated at 2022-06-14 14:40:03.562971
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    from pillowtop import from_json_schema as pillowtop_from_json_schema

    data = {
        "if": {
            "type": "object",
            "properties": {
                "condition": {"type": "boolean", "const": True}
            },
            "required": ["condition"],
            "default": None
        },
        "then": {
            "type": "string",
            "const": "value"
        },
        "else": {
            "type": "string",
            "const": "other"
        }
    }
    field = pillowtop_from_json_schema(data)

# Generated at 2022-06-14 14:40:14.476487
# Unit test for function to_json_schema
def test_to_json_schema():
    # Simple example
    schema = to_json_schema(
        Schema(
            {
                "a": Integer(0, 50),
                "b": Float(0, 50),
                "c": Decimal(0, 50),
                "d": Boolean(),
                "e": String(min_length=1, pattern_regex=r"^[a-z]+$"),
                "f": Array(items=Integer(0, 50)),
                "g": Array(items=[Integer(0, 50), String()]),
                "h": Object(properties={"i": Integer(), "j": String()}),
                "k": Choice(choices=[("x", "x"), ("y", "y")]),
            }
        )
    )

# Generated at 2022-06-14 14:40:26.723118
# Unit test for function from_json_schema_type

# Generated at 2022-06-14 14:40:35.770740
# Unit test for function to_json_schema
def test_to_json_schema():

    def assert_convert_equals(arg, expected):
        data = to_json_schema(arg)
        assert data == expected

    # type: ignore[call-overload]
    assert_convert_equals(str, {"type": "string"})
    # type: ignore[call-overload]
    assert_convert_equals(Optional[str], {"type": ["string", "null"]})
    assert_convert_equals(String(max_length=10), {"type": "string", "maxLength": 10})

# Generated at 2022-06-14 14:40:41.445238
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "if": {"type": "string"},
        "then": {"minLength": 3},
        "default": "",
    }

    schema = if_then_else_from_json_schema(data, definitions=None)
    assert isinstance(schema, IfThenElse)
    assert schema.default == ""

# Generated at 2022-06-14 14:41:19.594691
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Schema(
        {
            "name": String(min_length=3),
            "age": Integer(minimum=18),
            "address": {
                "street": String(),
                "number": Integer(),
                "city": String(),
            }
        }
    )
    document = {"name": "John", "age": 25, "address": {"street": "Silicon Valley", "number": 12}}
    json_schema_1 = to_json_schema(schema)
    json_schema_2 = schema.to_json_schema()

    assert json_schema_1 == json_schema_2

# Generated at 2022-06-14 14:41:27.882791
# Unit test for function to_json_schema
def test_to_json_schema():
    updated = to_json_schema(
        {"name": Field(String(), max_length=30), "address": Field(String())}
    )
    assert updated == {
        "type": "object",
        "properties": {
            "name": {"type": "string", "maxLength": 30},
            "address": {"type": "string"},
        },
        "required": ["name", "address"],
    }


if __name__ == "__main__":  # pragma: no cover
    test_to_json_schema()
    test_from_json_schema()

# Generated at 2022-06-14 14:41:28.910100
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    data = {
        "type": "string"
    }
    assert from_json_schema(data) == String()



# Generated at 2022-06-14 14:41:42.613358
# Unit test for function to_json_schema
def test_to_json_schema():
    field = Integer()

    # Test basic properties
    json = to_json_schema(field)
    assert json == {"type": "integer"}

    # Test with a more complex schema
    field = Integer() + String(allow_blank=False) + String()
    json = to_json_schema(field)
    expected = {
        "allOf": [
            {"type": "integer"},
            {
                "anyOf": [
                    {"type": "string", "minLength": 1},
                    {"type": "null"},
                ]
            },
            {"type": "string"},
        ]
    }
    assert json == expected

    # Test with a schema that uses references
    field = SchemaDefinitions(
        number=Integer(),
        data=Integer() + String(allow_blank=False) + String(),
    )

# Generated at 2022-06-14 14:41:50.897746
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Any()) == True
    assert to_json_schema(String(allow_null=False)) == {"type": "string"}
    assert to_json_schema(String(allow_null=True)) == {"type": ["string", "null"]}
    assert to_json_schema(Object(properties={"a": String()})) == {
        "properties": {"a": {"type": "string"}},
        "type": "object",
    }



# Generated at 2022-06-14 14:42:00.611364
# Unit test for function to_json_schema
def test_to_json_schema():
    from pydantic import BaseModel
    from pydantic.schema import BaseConfig

    class TestModel(BaseModel):
        v: int = Field(..., gt=100, lt=1000)
        d: datetime.datetime = Field(..., gt=datetime.datetime(1970, 1, 1))
        s: typing.Optional[str] = Field(None, min_length=2, max_length=100, pattern=r"\d+")
        r: typing.Optional[float] = Field(None, gt=0, lt=1.0)
        b: typing.Optional[bool] = Field(None)

    data = to_json_schema(TestModel)
    json_str = json.dumps(data, indent=4)
    print(json_str)


# Generated at 2022-06-14 14:42:12.033096
# Unit test for function to_json_schema
def test_to_json_schema():
    from rivr_rest.fields import UUID, URL, Email

    assert to_json_schema(
        Any(description="An anything-goes field")
    ) == {"description": "An anything-goes field"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Integer(name="A name")) == {
        "type": "integer",
        "title": "A name",
    }
    assert to_json_schema(Boolean()) == {"type": "boolean"}
    assert to_json_schema(Boolean(description="A boolean field")) == {
        "description": "A boolean field",
        "type": "boolean",
    }

# Generated at 2022-06-14 14:42:22.528533
# Unit test for function to_json_schema
def test_to_json_schema():
    from pydantic.validators import validator
    from pydantic.schema import make_schema
    from pydantic.main import Model
    from pydantic import BaseSettings

    class DecimalField(BaseModel):
        value: Decimal

    class Settings(BaseSettings):
        decimal_field: DecimalField
        decimal_field_optional: typing.Optional[DecimalField] = None

    schema = make_schema(Settings)
    schema["properties"]["decimal_field"]["type"] = "string"
    schema["properties"]["decimal_field_optional"]["type"] = "string"

    settings = Settings(decimal_field=DecimalField(value=Decimal("12.34")))
    assert settings.decimal_field.value == Decimal("12.34")
    settings = Settings

# Generated at 2022-06-14 14:42:34.627377
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({}, definitions={}) == Any()
    assert (
        type_from_json_schema({'type': "integer"}, definitions={})
        == Integer(allow_null=False)
    )
    assert type_from_json_schema({'type': "boolean"}, definitions={}) == Boolean()
    assert type_from_json_schema({'type': "null"}, definitions={}) == Const(None)
    assert type_from_json_schema({'type': ["null"]}, definitions={}) == Const(None)
    assert type_from_json_schema({'type': ["integer"]}, definitions={}) == Integer()

# Generated at 2022-06-14 14:42:42.741574
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    # Test data.
    TYPES = {"number", "integer", "string", "boolean", "array", "object"}
    JSON_SCHEMA_TYPE_NAMES = list(TYPES) + ["null"]

    # Functions

# Generated at 2022-06-14 14:43:15.767116
# Unit test for function to_json_schema
def test_to_json_schema():
    from pydantic import BaseModel

    class SubModel(BaseModel):
        field1: str
        field2: int

    class MyModel(BaseModel):
        field1: str
        field2: str = "foobar"
        field3: typing.Optional[int]
        field4: typing.Optional[int] = 12
        field5: int = 12
        field6: bool = True
        field7: bool = False
        field8: typing.List[int]
        field9: typing.List[int] = []
        field10: typing.List[int] = [1, 2, 3, 4, 5]
        field11: typing.List[int] = Field(...)
        field12: typing.List[int] = [1, 2, Field(...)]
        field13: SubModel
        field14: typing

# Generated at 2022-06-14 14:43:24.707250
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(
        {"$ref": "#/definitions/name"}
    ) == Schema(ref="#/definitions/name")
    assert from_json_schema({}) == Any()
    assert from_json_schema({"type": "number"}) == Number()
    assert from_json_schema({"type": "number", "minimum": 1.5}) == Number(minimum=1.5)
    assert from_json_schema({"enum": [1, 2, 3]}) == Choice([1, 2, 3])
    assert from_json_schema({"const": 1}) == Const(1)
    assert from_json_schema({"allOf": [{"type": "string"}]}) == String()

# Generated at 2022-06-14 14:43:33.953615
# Unit test for function to_json_schema
def test_to_json_schema():
    class RootSchema(Schema):
        ref = Reference(to="definition")
        array = Array(of=String())
        object = Object(properties={"key": Integer()})
        choice = Choice(choices=[("A", 1), ("B", 2)])
        const = Const(const=1)
        all_of = AllOf(all_of=[Boolean(), Integer()])
        any_of = Union(any_of=[Boolean(), Integer()])
        one_of = OneOf(one_of=[Boolean(), Integer()])
        not_field = Not(negated=Boolean())

    root = RootSchema()

# Generated at 2022-06-14 14:43:44.280547
# Unit test for function to_json_schema
def test_to_json_schema():
    data = {
        "type": "object",
        "properties": {"a": {"type": "boolean"}, "b": {"type": "string"}},
    }
    assert to_json_schema(from_json_schema(data)) == data
    data = {"type": "string", "pattern": "^[a-z]{2}$", "minLength": 2, "maxLength": 2}
    assert to_json_schema(from_json_schema(data)) == data
    data = {"type": "integer", "minimum": 5, "maximum": 10, "multipleOf": 2}
    assert to_json_schema(from_json_schema(data)) == data


# An extension of the (official) Python "float" type that supports "infinity" and
# "not a number" ("NaN")

# Generated at 2022-06-14 14:43:51.213057
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema(True) == Any()

    # pylint: disable=line-too-long
    assert (
        from_json_schema(
            {
                "type": "string",
                "const": "foo",
            }
        )
        == Const("foo", String(min_length=1))
    )

    assert (
        from_json_schema(
            {
                "type": "string",
                "const": "foo",
                "minLength": 3,
            }
        )
        == Const("foo", String(min_length=3))
    )


# Generated at 2022-06-14 14:44:01.446719
# Unit test for function to_json_schema
def test_to_json_schema():
    f = Field()
    assert to_json_schema(f) is True

    f = Field(default=5)
    assert to_json_schema(f) == {"default": 5}

    f = Field(enum=[1, 2, 3])
    assert to_json_schema(f) == {"enum": [1, 2, 3]}

    f = Field(const=7)
    assert to_json_schema(f) == {"const": 7}

    f = Field(if_then_else=("cond", "then", "else"))
    assert to_json_schema(f) == {"if": "cond", "then": "then", "else": "else"}

    f = Field(if_then_else=("cond", None, "else"))

# Generated at 2022-06-14 14:44:08.056992
# Unit test for function to_json_schema
def test_to_json_schema():
    from json import loads
    from jsonschema import Draft7Validator, validators
    from pprint import pformat

    for testcase in ALL_TESTS:
        field = from_json_schema(testcase.schema)
        schema = to_json_schema(field)
        print(pformat(schema), "\n")
        assert Draft7Validator.check_schema(schema)

    # A simple custom validator class:
    class EnumValidator(validators.Draft7Validator):
        def validate_enum(self, enum, instance, schema):
            if instance not in enum:
                self.fail("{!r} is not a valid choice".format(instance))