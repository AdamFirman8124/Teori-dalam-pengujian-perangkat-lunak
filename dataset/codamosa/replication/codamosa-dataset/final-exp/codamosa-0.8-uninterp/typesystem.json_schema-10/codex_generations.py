

# Generated at 2022-06-14 14:34:57.200825
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    schema = from_json_schema({"$ref": "#/definitions/test"})
    assert isinstance(schema, Reference)
    assert schema.to == "#/definitions/test"



# Generated at 2022-06-14 14:35:05.718530
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    # Tests for #28
    all_of_data = {
        "allOf": [
            {"type": "string"},
            {
                "oneOf": [
                    {"const": "test"},
                    {"const": "test2"},
                    {"const": "test3"},
                ]
            },
        ]
    }
    all_of = all_of_from_json_schema(data=all_of_data, definitions=SchemaDefinitions())
    assert all_of.validate("test") == "test"



# Generated at 2022-06-14 14:35:09.939292
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema(): # type: ignore
    data = {"if": {"type": "string"}, "then": {"const": "Yes!"}}
    schema = if_then_else_from_json_schema(data, {})
    assert schema({}) == "Yes!"
    assert schema(1) is Undefined
test_if_then_else_from_json_schema()



# Generated at 2022-06-14 14:35:18.675772
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema(
        {
            "type": "object",
            "patternProperties": {"foo.*": {"type": "number"}},
            "additionalProperties": False,
        }
    ) == Object(pattern_properties={"foo.*": Float(allow_infinity=False)})

# Generated at 2022-06-14 14:35:22.202708
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {"not": {"type": "string"}}
    not_schema = not_from_json_schema(data, definitions=None)
    assert not_schema._negated is not None
    assert not_schema._negated.type_ == "string"
    assert not_schema._negated.allow_null == False

# Generated at 2022-06-14 14:35:24.846713
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    test_not = {
        "anyOf": [{"type": "integer"}, {"type": "string"}],
        "default": 1,
    }
    not_test_not = not_from_json_schema(test_not, None)
    assert not ((isinstance(not_test_not, Integer) or isinstance(not_test_not, String)))
    assert not_test_not.default == 1


# Generated at 2022-06-14 14:35:29.823698
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    test_data = {}
    assert isinstance(
        type_from_json_schema(test_data, definitions=SchemaDefinitions()), Any
    )
    assert isinstance(
        type_from_json_schema(test_data, definitions=SchemaDefinitions()), Any
    )



# Generated at 2022-06-14 14:35:38.602397
# Unit test for function get_valid_types
def test_get_valid_types():
    assert {'integer'} == get_valid_types({
        'type': 'integer'
    }).pop(0)
    
    assert {'object', 'integer'} == get_valid_types({
        'type': ['object', 'integer']
    }).pop(0)
    
    assert {'null', 'object', 'integer'} == get_valid_types({
        'type': ['null', 'object', 'integer']
    }).pop(0)

    assert ({'null', 'object', 'integer'}, False) == get_valid_types({
        'type': ['null', 'object', 'integer'],
        'enum': [None],
    })


# Generated at 2022-06-14 14:35:46.995843
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    from . import JsonSchema
    from .types import JsonData

    schema = JsonSchema({
        "if": {
            "type": "integer",
            "multipleOf": 2,
        },
        "then": {
            "type": "string",
            "minLength": 10,
        },
        "else": {
            "type": "integer",
            "maximum": 99,
        },
    })

    assert schema.validate(92)
    assert schema.validate(10) == "value is less than 10"
    assert schema.validate(-2) == "value is less than 10"
    assert schema.validate(11) == "value is not divisible by 2"
    assert schema.validate(100) == "value is more than 99"


# Generated at 2022-06-14 14:35:59.326952
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert isinstance(type_from_json_schema({"type": "string"}, definitions=None), String)
    assert isinstance(
        type_from_json_schema({"type": "integer"}, definitions=None), Integer
    )
    assert isinstance(
        type_from_json_schema({"type": "number"}, definitions=None), Number
    )
    assert isinstance(
        type_from_json_schema({"type": "object"}, definitions=None), Object
    )
    assert isinstance(type_from_json_schema({"type": "array"}, definitions=None), Array)
    assert isinstance(
        type_from_json_schema({"type": "boolean"}, definitions=None), Boolean
    )

    # Null is supported as a primitive value type

# Generated at 2022-06-14 14:36:26.477814
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {'anyOf': [{'minimum': 1}, {'maximum': 10}], 'default': None}
    definitions = None
    assert any_of_from_json_schema(data, definitions).any_of[0].minimum == 1


# Generated at 2022-06-14 14:36:36.588795
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    schema1 = {
        "type": "object",
        "properties": {
            "a": {
                "type": "array",
                "items": {"type": "number"},
                "additionalItems": {"type": "string"},
                "minItems": 1,
                "maxItems": 100,
            }
        },
    }
    field1 = from_json_schema(schema1)
    assert isinstance(field1, Object)
    prop = field1.properties["a"]
    assert isinstance(prop, Array)
    item = prop.items

    assert isinstance(item, Union)
    assert isinstance(item.any_of[0], Float)
    assert isinstance(item.any_of[1], String)

    assert isinstance(field1, Object)

# Generated at 2022-06-14 14:36:47.966562
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": ["string", "boolean"]}) == (String() | Boolean())
    assert from_json_schema({"enum": ["foo", "bar"]}) == Choice(items=["foo", "bar"])
    assert from_json_schema({"type": "array", "items": {"type": "string"}}) == Array(
        items=String()
    )
    assert from_json_schema({"allOf": [{"type": "string"}, {"minLength": 2}]}) == AllOf(
        [String(min_length=2), String()]
    )

# Generated at 2022-06-14 14:36:50.587163
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    assert any_of_from_json_schema(data={"anyOf": [{"type": "integer"}, {"type": "string"}], "default": 5}, definitions = {})


# Generated at 2022-06-14 14:37:01.499416
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = dict(
        type="object",
        properties=dict(
            items=dict(
                type="array",
                items=dict(
                    type="object",
                    properties=dict(
                        value=dict(type="number"),
                        name=dict(type="string"),
                    ),
                    required=["value", "name"],
                ),
            ),
            value=dict(type="number"),
            text=dict(type="string"),
        ),
        required=["items", "value", "text"],
    )

    class Root(Schema):
        items = Array(
            Object(
                name=String(),
                value=Float(),
            ),
        )
        value = Float()
        text = String()

    a = to_json_schema(Root)

# Generated at 2022-06-14 14:37:06.930847
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert enum_from_json_schema({
        "enum": ['a', 'b', 'c', 'd'],
        "default": 'a'
    }, definitions=None).__class__ == Choice
    assert enum_from_json_schema({
        "enum": ['a', 'b', 'c', 'd']
    }, definitions=None).__class__ == Choice
    assert enum_from_json_schema({
        "enum": ['a', 'b', 'c', 'd'],
        "default": 'a'
    }, definitions=None).to_native('a') == 'a'


# Generated at 2022-06-14 14:37:18.505774
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    assert any_of_from_json_schema({
        "anyOf": [
            {
                "type": "boolean",
                "default": False
            },
            {
                "type": "integer",
                "default": 1
            },
            {
                "type": "string",
                "default": "foo"
            }
        ]
    }) == Union(
        any_of=[
            Boolean(allow_null=False, default=False),
            Integer(allow_null=False, default=1),
            String(allow_null=False, default='foo')
        ],
        default=NO_DEFAULT
    )

# Generated at 2022-06-14 14:37:30.286163
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem.serializers import to_python

    # test cases from https://json-schema.org/understanding-json-schema/appendices.html
    schema = {
        "type": "object",
        "properties": {
            "address": {
                "type": "string",
                "pattern": "^\\d{5}$|^\\d{5}-\\d{4}$",
                "description": "5 or 9 digit US ZIP code",
            }
        },
    }

    field = from_json_schema(schema)

    # string
    assert field.validate("foo", "address") == "foo"
    assert to_python(field, "foo", "address") == "foo"

    assert field.validate("", "address") == ""

# Generated at 2022-06-14 14:37:43.205439
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    from typesystem.schemas import Schema
    from typesystem.schemas import SchemaDefinitions
    from typesystem.types import Array

# Generated at 2022-06-14 14:37:55.834041
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    json_schema = {
        "enum": [
            "foo",
            2,
            3.14,
            None,
            True,
            False,
            "xyz",
            "123",
            "0",
        ],
        "type": "number"
    }
    data = from_json_schema(json_schema)

# Generated at 2022-06-14 14:38:40.666968
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(
        True
    ).to_primitive() == {"type": "any"}
    assert from_json_schema(
        False
    ).to_primitive() == {"type": "never"}
    assert from_json_schema(
        {
            "type": "number",
            "minimum": 5,
            "maximum": 10,
            "multipleOf": 2,
            "enum": [8, 10],
            "const": 8,
        }
    ).to_primitive() == {
        "type": "number",
        "minimum": 5,
        "maximum": 10,
        "multipleOf": 2,
        "enum": [8, 10],
        "const": 8,
    }

# Generated at 2022-06-14 14:38:45.412759
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert (
        String(
            min_length=1, max_length=100, format="date-time", default="2018-01-01T00:00:00Z"
        ).to_json_schema(include_title=False)
        == to_json_schema(
            from_json_schema(
                {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 100,
                    "format": "date-time",
                    "default": "2018-01-01T00:00:00Z",
                }
            )
        )
    )
    assert to_json_schema(from_json_schema({"type": "string"})) == {
        "type": "string",
        "additionalProperties": False,
    }
    assert to_json_

# Generated at 2022-06-14 14:38:57.404435
# Unit test for function from_json_schema
def test_from_json_schema():

    assert isinstance(
        from_json_schema(
            {"$ref": "#/definitions/ReferencedSchema"},
            definitions={
                "#/definitions/ReferencedSchema": String(maximum_length=10),
                "#/definitions/ReferencedSchema2": String(minimum_length=10),
            },
        ),
        String,
    )

    assert isinstance(from_json_schema(True), Any)
    assert isinstance(from_json_schema(False), NeverMatch)

    assert isinstance(from_json_schema({"type": "string"}), String)
    assert isinstance(from_json_schema({"type": "integer"}), Integer)
    assert isinstance(from_json_schema({"type": "number"}), Number)

# Generated at 2022-06-14 14:39:06.884364
# Unit test for function to_json_schema
def test_to_json_schema():
    field = Object(
        properties={"id": Integer(), "name": String(max_length=20, allow_blank=False)}
    )
    expected = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string", "maxLength": 20, "minLength": 1},
        },
        "required": ["id", "name"],
        "type": "object",
    }
    assert to_json_schema(field) == expected



# Generated at 2022-06-14 14:39:19.275276
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    expect(
        if_then_else_from_json_schema(
            {"if": {}, "then": {}}, definitions={}
        ).type_name
    ).to(equal("IfThenElse"))

    expect(
        if_then_else_from_json_schema({"if": {}, "else": {}}, definitions={}).type_name
    ).to(equal("IfThenElse"))

    expect(
        if_then_else_from_json_schema({}, definitions={}).type_name
    ).to(equal("IfThenElse"))


if __name__ == "__main__":
    from prestring.python import Module

    m = Module()

# Generated at 2022-06-14 14:39:28.099158
# Unit test for function to_json_schema
def test_to_json_schema():
    from pydantic.main import Schema

    expected_data = {
        "type": "object",
        "properties": {
            "alpha": {"type": "string"},
            "beta": {"type": "string"},
            "gamma": {"type": "string"},
            "_delta": {"type": "string"},
        },
        "required": ["alpha"],
    }

    class ExampleSchema(Schema):
        alpha: str
        beta: str = None
        gamma: str = None

        class Config:
            extra = "forbid"
            allow_mutation = False

    example_schema = ExampleSchema(alpha="alpha", beta="beta", gamma="gamma")

    actual_data = to_json_schema(example_schema)

    assert expected_data == actual_data


# Generated at 2022-06-14 14:39:35.133711
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    constraints = [
        "if",
        "then",
        "else",
        "const",
        "enum",
        "allOf",
        "anyOf",
        "oneOf",
        "not",
    ]
    for constraint in constraints:
        obj1 = {"if": {"const": True}, "then": {"const": True}, constraint: {}}
        obj2 = {"if": {"const": True}, constraint: {}, "else": {"const": True}}
        obj3 = {constraint: {}, "if": {"const": True}, "else": {"const": True}}

        assert if_then_else_from_json_schema(obj1, definitions=None)
        assert if_then_else_from_json_schema(obj2, definitions=None)
        assert if_then_else_from_json_

# Generated at 2022-06-14 14:39:47.952510
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    data={'items': [{'description': 'String_schema', 'type': 'string'}, {'description': 'Number_schema', 'type': 'number'}], 'type': 'array'}
    type_string = "array"
    allow_null = False
    definitions = SchemaDefinitions()
    result=from_json_schema_type(data, type_string, allow_null, definitions)
    assert(type(result))==type(Array(()))
    assert(result.min_items)==0
    assert(result.max_items)==None
    assert(result.additional_items)==True
    assert(result.items)==None
    assert(result.unique_items)==False
    assert(result.default)== NO_DEFAULT
    assert(result.allow_null)== False



# Generated at 2022-06-14 14:39:55.352547
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "number"}) == Number()
    assert from_json_schema({"type": "object"}) == Object()
    assert from_json_schema({"type": "array"}) == Array()
    assert from_json_schema({"type": "boolean"}) == Boolean()
    assert from_json_schema({"type": ["null", "integer"]}) == Union([Integer(), NeverMatch()])

# Generated at 2022-06-14 14:40:05.612027
# Unit test for function to_json_schema
def test_to_json_schema():
    # pylint: disable = no-member

    # Test root with definitions
    field = AllOf(
        [
            Reference("foo", definitions={"foo": AllOf([String(), Integer()])}),
            Reference("bar", definitions={"bar": Array(items=String())}),
        ]
    )
    data = to_json_schema(field)
    assert data["allOf"] == [
        {"$ref": "#/definitions/foo"},
        {"$ref": "#/definitions/bar"},
    ]
    assert data["definitions"] == {
        "foo": {"allOf": [{"type": "string"}, {"type": "integer"}]},
        "bar": {"type": "array", "items": {"type": "string"}},
    }

    # Test root without definitions

# Generated at 2022-06-14 14:40:35.863823
# Unit test for function to_json_schema
def test_to_json_schema():
    try:
        to_json_schema(Integer(pattern_regex=re.compile(r"\d+", re.ASCII)))
    except ValueError as e:
        if str(e) != "Cannot convert regular expression with non-standard flags to JSON schema: re.ASCII":
            raise e

    class MySchema(SchemaDefinitions):
        foo = Integer(pattern_regex=re.compile(r"\d+", re.UNICODE))

    data = to_json_schema(MySchema())

# Generated at 2022-06-14 14:40:47.262520
# Unit test for function to_json_schema

# Generated at 2022-06-14 14:40:51.857802
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "array", "items": {"type": "string"}}) == Array(
        items=String()
    )
    assert (
        from_json_schema(
            {
                "type": "object",
                "properties": {
                    "test": {"type": "string"},
                    "test_array": {"type": "array", "items": {"type": "string"}},
                },
            }
        )
        == Object(properties={"test": String(), "test_array": Array(items=String())})
    )



# Generated at 2022-06-14 14:41:05.145059
# Unit test for function to_json_schema
def test_to_json_schema():
    class Person(Schema):
        name = String(min_length=1)
        age = Integer(minimum=1)

    class Book(Schema):
        author = Person
        title = String(min_length=1)
        isbn = Const(const="1234")

    result = to_json_schema(Book)

# Generated at 2022-06-14 14:41:11.876511
# Unit test for function to_json_schema
def test_to_json_schema():
    data = to_json_schema(ExampleOne())
    assert data == {
        "title": "Example One",
        "description": "This is the first example!",
        "type": "null",
        "properties": {"required": {"type": "boolean"}, "string": {"type": ["string", "null"]}},
        "minProperties": 1,
        "required": ["required"]
    }



# Generated at 2022-06-14 14:41:21.348616
# Unit test for function to_json_schema
def test_to_json_schema():
    data = to_json_schema(
        Object(
            properties={
                "a": Integer(),
                "b": Object(
                    properties={
                        "c": Union(
                            any_of=[
                                Integer(),
                                String(min_length=1),
                            ]
                        )
                    }
                ),
            }
        )
    )

# Generated at 2022-06-14 14:41:31.827162
# Unit test for function from_json_schema

# Generated at 2022-06-14 14:41:43.784082
# Unit test for function to_json_schema
def test_to_json_schema():
    """Simple unit test for the to_json_schema function."""

    class MySchema(Schema):
        @validator_command(..., "min")
        @validator_command(..., "max")
        def validate_user_id(cls, value, min, max):
            if min and value < min:
                raise ValidationError(f"Value {value} is less than {min!r}")
            if max and value > max:
                raise ValidationError(f"Value {value} is greater than {max!r}")

        user_id = Integer(min=0, max=1000)

    def test_schema_after_round_trip(schema_class, expected_data):
        schema = schema_class()
        data = to_json_schema(schema)
        assert data == expected

# Generated at 2022-06-14 14:41:56.002854
# Unit test for function to_json_schema
def test_to_json_schema():
    count = 0

# Generated at 2022-06-14 14:42:05.902014
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String()) == {
        "type": "string"
    }

    assert to_json_schema(String(pattern=r"^[A-Za-z]\d$")) == {
        "type": "string",
        "pattern": r"^[A-Za-z]\d$",
    }

    assert to_json_schema(String(format="date-time")) == {
        "type": "string",
        "format": "date-time",
    }

    assert to_json_schema(String(max_length=5)) == {
        "type": "string",
        "maxLength": 5,
    }


# Generated at 2022-06-14 14:42:39.344416
# Unit test for function to_json_schema
def test_to_json_schema():
    import enum
    from io import StringIO

    class Color(enum.Enum):
        RED = "red"
        GREEN = "green"
        BLUE = "blue"


# Generated at 2022-06-14 14:42:51.554719
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem.mock import Mock
    from typesystem.schemas import Reference

    assert isinstance(from_json_schema({"type": "boolean"}), Boolean)
    assert isinstance(from_json_schema({"type": "string"}), String)
    assert isinstance(from_json_schema({"type": "integer"}), Integer)
    assert isinstance(from_json_schema({"type": "number"}), Number)
    assert isinstance(from_json_schema({"type": "object"}), Object)
    assert isinstance(from_json_schema({"type": "array"}), Array)
    assert from_json_schema({"type": "array"}).items is Any()
    assert from_json_schema({"type": "null"}) == NeverMatch()

# Generated at 2022-06-14 14:43:03.370069
# Unit test for function to_json_schema
def test_to_json_schema():
    schema_definitions = {
        "person": Object(properties={"name": String(), "age": Integer()}, required=["age"]),
    }
    schema = Object(
        properties={"name": String(), "friends": Array(items=Reference("person"))}
    )
    data = to_json_schema(schema, schema_definitions)

# Generated at 2022-06-14 14:43:04.934356
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"$ref": "test"})



# Generated at 2022-06-14 14:43:15.340238
# Unit test for function from_json_schema

# Generated at 2022-06-14 14:43:19.617288
# Unit test for function to_json_schema
def test_to_json_schema():
    array = Array(
        items=[String(format="uuid"), String(format="date-time"), Integer()]
    )
    assert to_json_schema(array) == {
        "type": "array",
        "items": [
            {"type": "string", "format": "uuid"},
            {"type": "string", "format": "date-time"},
            {"type": "integer"},
        ],
    }  # type: ignore



# Generated at 2022-06-14 14:43:25.046201
# Unit test for function to_json_schema
def test_to_json_schema():
    Schema.from_json_schema(to_json_schema(String)).validate("hello")
    Schema.from_json_schema(to_json_schema(Integer)).validate(123)
    Schema.from_json_schema(to_json_schema(Decimal)).validate(12.3)
    Schema.from_json_schema(to_json_schema(Float)).validate(12.3)
    Schema.from_json_schema(to_json_schema(Boolean)).validate(True)
    Schema.from_json_schema(to_json_schema(Array)).validate([])
    Schema.from_json_schema(to_json_schema(Object)).validate({})

# Generated at 2022-06-14 14:43:36.944816
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    from typesystem.constraints import MaxLength, MinLength
    from typesystem.exceptions import InvalidType
    from typesystem.fields import DateTime

    # type: string
    assert type_from_json_schema({"type": "string"}) == String()

    # type: string, allow_null
    assert type_from_json_schema({"type": ["string", "null"]}) == String(allow_null=True)

    # type: string, allow_null=False, anyOf
    assert type_from_json_schema({"type": ["string", "null"], "allOf": []}) == String(allow_null=True)

    # type: string, minLength, maxLength

# Generated at 2022-06-14 14:43:41.639617
# Unit test for function from_json_schema
def test_from_json_schema():
    schema = {"type": "string", "minLength": 0, "enum": [None]}
    assert from_json_schema(schema)
    assert from_json_schema(True)
    assert from_json_schema(False)
    assert from_json_schema({"$ref": "#"})

# Generated at 2022-06-14 14:43:48.995184
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem.fields import String
    from typesystem.validators import MaxLength
    from typesystem.validators import MinLength

    # From https://github.com/magged/JSONSchema/tree/master/tests/specs/draft-07/optional
    data = {
        "$ref": "#/definitions/foo",
        "definitions": {
            "foo": {
                "type": "string",
                "minLength": 1,
                "maxLength": 10
            }
        }
    }
    field = from_json_schema(data)

    assert isinstance(field, String)
    assert isinstance(field.validators[0], MinLength)
    assert isinstance(field.validators[1], MaxLength)



# Generated at 2022-06-14 14:44:12.137573
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    data = {
        "type": ["number", "string"],
        "format": "date-time",
        "minLength": 1,
        "maximum": 10,
        "default": "test",
    }

    expected = Union(
        any_of=[
            Float(format="date-time", default="test"),
            String(format="date-time", min_length=1, default="test"),
        ]
    )
    actual = from_json_schema_type(data, type_string="number", allow_null=False, definitions={})

    assert actual == expected
    assert actual.to_json_schema() == expected.to_json_schema()

