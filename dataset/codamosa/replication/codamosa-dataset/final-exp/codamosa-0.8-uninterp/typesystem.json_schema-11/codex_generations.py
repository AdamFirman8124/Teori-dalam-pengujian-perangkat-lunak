

# Generated at 2022-06-14 14:35:06.738507
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert not isinstance(
        if_then_else_from_json_schema(
            data = {"if": {"type": "string"}, "then": {"type": "array"}, "else": {"type": "object"}},
            definitions = None,
        ),
        Field,
    )

# Generated at 2022-06-14 14:35:09.800242
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    expected = f = Not(negated=String())
    actual = from_json_schema({"not": {"type": "string"}})
    assert expected == actual


# Generated at 2022-06-14 14:35:16.169777
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    """
    Test OneOf creation
    """
    data = {"oneOf": [{"type": "string"}, {"type": "string"}]}
    test_schema = from_json_schema(data)
    assert isinstance(test_schema, OneOf)
    assert isinstance(test_schema.one_of[0], String)
    assert isinstance(test_schema.one_of[1], String)
    assert test_schema.default is NO_DEFAULT
    assert test_schema.description is None
    assert test_schema.error_messages == {}



# Generated at 2022-06-14 14:35:19.917480
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    one_of = [from_json_schema(item,definitions=definitions) for item in [data["if"],data["then"]] ]
    kwargs = {"one_of": one_of, "default": data.get("default", NO_DEFAULT)}
    return OneOf(**kwargs)


# Generated at 2022-06-14 14:35:30.994787
# Unit test for function to_json_schema
def test_to_json_schema():
    import sys
    import json
    import tempfile
    import io
    import pathlib
    from .tests import test_helpers

    schema_obj = test_helpers.make_schema_example()
    result = to_json_schema(schema_obj)
    assert "definitions" in result, result
    definitions = result["definitions"]
    assert "person" in definitions, definitions
    person_definition = definitions["person"]
    assert person_definition["type"] == "object"
    assert person_definition["required"] == ["name", "age", "times", "height"]
    assert person_definition["properties"]["name"]["enum"] == [
        "Alice",
        "Bob",
        "Carol",
        "Dave",
        "Eve",
        "Frank",
    ]

    example_data

# Generated at 2022-06-14 14:35:40.545228
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True).validate("foo") is None
    assert from_json_schema(False).validate("foo") == "unexpected_value"

    assert from_json_schema({"$ref": "#/definitions/foo"}).validate("foo") is None

    schema = from_json_schema({"type": "string", "minLength": 2})
    assert schema.validate("foo") is None
    assert schema.validate("f") == "min_length"

    schema = from_json_schema({"enum": ["foo", "bar"]})
    assert schema.validate("foo") is None
    assert schema.validate("ble") == "unexpected_value"

    schema = from_json_schema({"const": "foo"})

# Generated at 2022-06-14 14:35:45.033878
# Unit test for function ref_from_json_schema

# Generated at 2022-06-14 14:35:58.052498
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {
        'anyOf': [
            {
                'type': 'array',
                'items':
                {
                    'type': 'string',
                    'minLength': 2,
                    'maxLength': 3
                },
                'minItems': 1
            },
            {
                'type': 'object',
                'properties': {
                    'b': {
                        'type': 'boolean'
                    }
                },
                'minProperties': 1
            }
        ]
    }
    definitions = SchemaDefinitions
    any_of = [from_json_schema(item, definitions=definitions) for item in data["anyOf"]]
    kwargs = {"any_of": any_of, "default": data.get("default", NO_DEFAULT)}
    return Union(**kwargs)



# Generated at 2022-06-14 14:36:01.613104
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {"allOf":[{"type":["string"],"maxLength":4}]}
    result = all_of_from_json_schema(data, definitions=None)
    print(result)



# Generated at 2022-06-14 14:36:11.851673
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    enum_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "test_enum_schema",
        "title": "Test Enum Schema",
        "type": "object",
        "properties": {
            "enum": {
                "$id": "enum",
                "oneOf": [
                    {"type": "integer"},
                    {"type": "number"},
                    {"type": "string"},
                    {"type": "boolean"},
                ],
            }
        },
    }
    enum_field = enum_from_json_schema(enum_schema, None)
    assert enum_field is not None

    enum_field.validate(3.14159)
    enum_field.validate(3)
    enum_field.valid

# Generated at 2022-06-14 14:36:47.887887
# Unit test for function from_json_schema
def test_from_json_schema():
    assert {
        "#/definitions/foo": Field(description="Foo", type="string"),
        "#/definitions/bar": Field(description="Bar", type="string"),
    } == from_json_schema(
        {
            "$id": "https://example.com/root.json",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "definitions": {
                "foo": {
                    "description": "Foo",
                    "type": "string",
                },
                "bar": {
                    "description": "Bar",
                    "type": "string",
                },
            },
        },
    ).definitions.to_primitive()

    # String
    assert String() == from_json_schema({"type": "string"})

    # N

# Generated at 2022-06-14 14:36:56.999825
# Unit test for function from_json_schema
def test_from_json_schema():
    def test(expected, data):
        assert isinstance(expected, Field)
        result = from_json_schema(data)
        assert expected.hints == result.hints
        assert expected.validate(data)
        if isinstance(expected, Schema):
            assert result in expected.validate(data)
        else:
            assert result == expected
            assert result in expected.validate(data)

    # Boolean
    test(Any(), True)
    test(NeverMatch(), False)
    test(NeverMatch(), {"$ref": "#"})
    test(NeverMatch(), {"not": True})
    test(NeverMatch(), {"not": {"$ref": "#"}})
    test(NeverMatch(), {"allOf": [True, {"$ref": "#"}]})

# Generated at 2022-06-14 14:37:03.347292
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    """
    TODO:
    * Document test cases
    * Add more test cases
    """
    for type_string, data in [
        ("number", {}),
        ("integer", {}),
        ("string", {"minLength":1}),
        ("boolean", {}),
        ("array", {}),
        ("object", {}),
        ("array", {"items": {}}),
    ]:
        field = from_json_schema_type(data, type_string=type_string, allow_null=False, definitions=None)
        assert field is not None
    assert field is not None



# Generated at 2022-06-14 14:37:08.100599
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    data = {"enum": [1,2]}
    definitions = SchemaDefinitions()
    assert(isinstance(enum_from_json_schema(data, definitions), typesystem.fields.Choice))
    assert(enum_from_json_schema(data, definitions).choices == [(1,1), (2,2)])
test_enum_from_json_schema()



# Generated at 2022-06-14 14:37:15.350763
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    data = {"enum": ["one", "two"]}
    field = enum_from_json_schema(data, None)
    assert field.validate("one") == "one"
    assert field.validate("two") == "two"
    assert field.validate("three") is None

    field = enum_from_json_schema(data, None)
    assert field.validate("one") == "one"


# Generated at 2022-06-14 14:37:26.452679
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="number", allow_null=False) == Float()
    assert from_json_schema_type({}, type_string="integer", allow_null=False) == Integer()
    assert from_json_schema_type({}, type_string="string", allow_null=False) == String()
    assert from_json_schema_type({}, type_string="boolean", allow_null=False) == Boolean()
    assert from_json_schema_type({}, type_string="array", allow_null=False) == Array()
    assert from_json_schema_type({}, type_string="object", allow_null=False) == Object()
test_from_json_schema_type()



# Generated at 2022-06-14 14:37:34.456703
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type({"type": "boolean"}, "boolean", False, None), Boolean)
    assert isinstance(from_json_schema_type({"type": "integer"}, "integer", False, None), Integer)
    assert isinstance(from_json_schema_type({"type": "number"}, "number", False, None), Float)
    assert isinstance(from_json_schema_type({"type": "integer"}, "number", False, None), Integer)
    assert isinstance(from_json_schema_type({"type": "string"}, "string", False, None), String)
    assert isinstance(from_json_schema_type({"type": "array"}, "array", False, None), Array)

# Generated at 2022-06-14 14:37:44.134418
# Unit test for function to_json_schema
def test_to_json_schema():
    field = Object(properties={"hello": String(), "there": String()})
    assert to_json_schema(field) == {
        "type": "object",
        "properties": {"hello": {"type": "string"}, "there": {"type": "string"}},
    }

    schema = Schema(properties={"hello": String(), "there": String()})
    assert to_json_schema(schema) == {
        "type": "object",
        "properties": {"hello": {"type": "string"}, "there": {"type": "string"}},
    }



# Generated at 2022-06-14 14:37:56.496620
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    schema = any_of_from_json_schema({
        "anyOf": [
            {
                "type": "string",
                "pattern": "^[A-Za-z]+$"
            },
            {
                "type": "number",
                "minimum": 0,
                "maximum": 100
            }
        ],
        "default": "test"
    }, SchemaDefinitions())
    assert schema.validate("test") == "test"
    assert schema.validate(10) == 10
    assert schema.validate("abc") == "abc"
    assert not schema.validate("10")
    assert not schema.validate(-1)
    assert not schema.validate("a%")
    assert not schema.validate("a-")



# Generated at 2022-06-14 14:38:01.769341
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    assert isinstance(
        ref_from_json_schema({"$ref": "#/definitions/geometry"}), Reference
    )
    assert isinstance(ref_from_json_schema({"$ref": "#/definitions/schema"}), Reference)



# Generated at 2022-06-14 14:38:32.900994
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert isinstance(type_from_json_schema({"type": "string"}, definitions=None), String)
    assert isinstance(type_from_json_schema({"type": "integer"}, definitions=None), Integer)
    assert isinstance(type_from_json_schema({"type": "number"}, definitions=None), Number)
    assert isinstance(type_from_json_schema({"type": "boolean"}, definitions=None), Boolean)
    assert isinstance(type_from_json_schema({"type": "object"}, definitions=None), Object)
    assert isinstance(type_from_json_schema({"type": "array"}, definitions=None), Array)
    assert isinstance(type_from_json_schema({"type": "null"}, definitions=None), Const)

# Generated at 2022-06-14 14:38:41.643333
# Unit test for function to_json_schema
def test_to_json_schema():
    definitions = {
        "a": Any(),
        "b": String(),
        "c": Integer(),
        "d": Const("x"),
        "e": Choice({"y": "y", "z": "z"}),
        "f": Reference("#/definitions/b", definitions={"b": Any()}),
        "g": OneOf([Reference("#/definitions/b", definitions={"b": Any()})]),
    }

# Generated at 2022-06-14 14:38:47.301086
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    case_data = {
        "type": "number",
        "minimum": 10,
    }
    case = from_json_schema_type(case_data, type_string='number', allow_null=False, definitions=definitions)
    assert case.__class__.__name__ == "Float"
    assert case.minimum == 10

    case_data = {
        "type": "integer",
        "minimum": 10,
    }
    case = from_json_schema_type(case_data, type_string='integer', allow_null=False, definitions=definitions)
    assert case.__class__.__name__ == "Integer"
    assert case.minimum == 10


# Generated at 2022-06-14 14:38:58.469365
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({'type': 'string'}) == String()
    assert type_from_json_schema({'type': 'integer'}) == Integer()
    assert type_from_json_schema({'type': 'number'}) == Number()
    assert type_from_json_schema({'type': 'boolean'}) == Boolean()
    assert type_from_json_schema({'type': 'object'}) == Object()
    assert type_from_json_schema({'type': 'array'}) == Array()
    assert type_from_json_schema({'type': 'null'}) == Const(None)

    assert type_from_json_schema({'type': ['string', 'null']}) == Union(any_of=[String(), Const(None)], allow_null=True)



# Generated at 2022-06-14 14:39:10.448842
# Unit test for function to_json_schema
def test_to_json_schema():
    from typing import Any, Dict, Union, Tuple, List, Callable

    # Empty Field
    assert to_json_schema(Field()) == {}

    # Basic Types
    assert to_json_schema(Boolean()) == {"type": "boolean"}
    assert to_json_schema(Boolean(allow_null=True)) == {"type": ["boolean", "null"]}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Integer(allow_null=True)) == {"type": ["integer", "null"]}
    assert to_json_schema(Float()) == {"type": "number"}
    assert to_json_schema(Float(allow_null=True)) == {"type": ["number", "null"]}
    assert to_json_schema

# Generated at 2022-06-14 14:39:22.806944
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({"type": "number"}, type_string="number", allow_null=False) is Float()
    assert from_json_schema_type({"type": "integer"}, type_string="integer", allow_null=False) is Integer()
    assert from_json_schema_type({"type": "string"}, type_string="string", allow_null=False) is String()
    assert from_json_schema_type({"type": "boolean"}, type_string="boolean", allow_null=False) is Boolean()
    assert from_json_schema_type({"type": "array"}, type_string="array", allow_null=False) is Array()
    assert from_json_schema_type({"type": "object"}, type_string="object", allow_null=False) is Object()

# Generated at 2022-06-14 14:39:33.659559
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
 
    data1 = {
        "$ref": "#/definitions/foo",
    }
    data2 = {
        "$ref": "#/definitions/foo",
    }
    definitions = SchemaDefinitions()
    definitions["#/definitions/foo"] = data2
    field = ref_from_json_schema(data1, definitions=definitions)
    assert field.validate({"$ref": "#/definitions/foo"})
    assert not field.validate({"$ref": "#/definitions/bar"})
    assert not field.validate({"$ref": "foo"})



# Generated at 2022-06-14 14:39:38.942511
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {
        "$ref": "#/definitions/Number"
    }
    definitions = SchemaDefinitions()
    definitions["#/definitions/Number"] = Number(minimum=1)

    field = ref_from_json_schema(data=data, definitions=definitions)
    assert field.minimum == 1
    assert field.validate(2) == (2, None)
    assert field.validate(0) == (None, "number must be greater than or equal to 1")



# Generated at 2022-06-14 14:39:51.018253
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    # test_value
    assert (from_json_schema({"const": -10})).to_python(-10) 
    assert (from_json_schema({"const": -10})).to_python("-10")
    assert (from_json_schema({"const": 10})).to_python(10)
    assert (from_json_schema({"const": 20})).to_python("20")
    # test_wrong_value
    assert (from_json_schema({"const": -10})).to_python("-20")
    assert (from_json_schema({"const": 10})).to_python("20")
    assert (from_json_schema({"const": -10})).to_python(10)
    assert (from_json_schema({"const": 10})).to

# Generated at 2022-06-14 14:40:02.974289
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    data_boolean = {'type': 'boolean'}
    assert JSONSchema.validate(data_boolean) == data_boolean
    assert isinstance(type_from_json_schema(data_boolean, definitions=definitions), Boolean)
    assert type_from_json_schema(data_boolean, definitions=definitions).to_json_schema() == data_boolean

    data_number = {'type': 'number'}
    assert JSONSchema.validate(data_number) == data_number
    assert isinstance(type_from_json_schema(data_number, definitions=definitions), Number)
    assert type_from_json_schema(data_number, definitions=definitions).to_json_schema() == data_number


# Generated at 2022-06-14 14:40:32.334049
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Integer(minimum=5, maximum=10)) == {
        "type": "integer",
        "minimum": 5,
        "maximum": 10,
    }

    schema = Schema(
        {"name": String(max_length=20), "age": Integer(minimum=0, maximum=120)}
    )
    expected = {
        "type": "object",
        "properties": {
            "name": {"type": "string", "maxLength": 20},
            "age": {"type": "integer", "minimum": 0, "maximum": 120},
        },
        "required": ["name", "age"],
    }
    assert to_json_schema(schema) == expected


# Generated at 2022-06-14 14:40:35.404241
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True).validate(None) is None
    assert from_json_schema(False).validate(None) is not None



# Generated at 2022-06-14 14:40:45.008257
# Unit test for function from_json_schema_type
def test_from_json_schema_type():

    data = {
        "type": [],
    }
    field = from_json_schema_type(data, type_string="null", allow_null=False, definitions=None)
    assert field.to_native(None) is None

    data = {
        "type": ["number"],
    }
    field = from_json_schema_type(data, type_string="number", allow_null=False, definitions=None)
    assert field.to_native(42) == 42
    assert field.to_native(42.0) == 42.0
    assert field.to_native(None) is None



# Generated at 2022-06-14 14:40:49.040181
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {'$ref': '#/definitions/Foo'}
    definitions = {'#/definitions/Foo': String()}
    field = ref_from_json_schema(data, definitions)
    assert field.validate('hello')
    assert not field.validate(42)



# Generated at 2022-06-14 14:41:01.592852
# Unit test for function to_json_schema
def test_to_json_schema():
    from validator.validators import (
        Any,
        Array,
        Boolean,
        Choice,
        Const,
        IfThenElse,
        Integer,
        Not,
        OneOf,
        String,
        Union,
    )


# Generated at 2022-06-14 14:41:11.379437
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "if": {
            "properties": {"a": {"const": "a"}},
            "additionalProperties": False,
        },
        "then": {
            "properties": {"b": {"const": "b"}},
            "additionalProperties": False,
        },
        "else": {
            "properties": {"c": {"const": "c"}},
            "additionalProperties": False,
        },
    }
    root = from_json_schema(data)
    assert root({"a": "a", "b": "b"}).get("b") == "b"
    assert root({"a": "a", "c": "c"}).get("b") == "b"
    assert root({"b": "b"}).get("b") == "b"
    assert not root

# Generated at 2022-06-14 14:41:14.663816
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {"$ref": "#/path/to/field"}
    field = ref_from_json_schema(data, definitions={})
    assert field.definition_name == "#/path/to/field"



# Generated at 2022-06-14 14:41:26.786205
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()

    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "number"}) == Number()
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": "boolean"}) == Boolean()
    assert from_json_schema({"type": "object"}) == Object()
    assert from_json_schema({"type": "array"}) == Array()

    assert (
        from_json_schema({"type": ["string", "integer"]}) == Union([String(), Integer()])
    )


# Generated at 2022-06-14 14:41:32.440875
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "phone": {"type": "string", "minLength": 10},
        },
    }

    schema_field = from_json_schema(schema)
    print(schema_field.to_yaml())
test_from_json_schema_type()



# Generated at 2022-06-14 14:41:44.165408
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"const": "foo"}) == Const("foo")

    assert from_json_schema({"const": ""}) == Const("")

    assert from_json_schema({"const": []}) == Const([])

    assert from_json_schema({"const": None}) == Const(None)

    assert from_json_schema({"const": {"foo": "bar"}}) == Const({"foo": "bar"})

    assert from_json_schema({"const": ["a", "b", "c"]}) == Const(["a", "b", "c"])

    assert from_json_schema(
        {
            "properties": {
                "foo": {"type": "string"},
                "bar": {"type": "boolean"},
            }
        }
    ) == Object

# Generated at 2022-06-14 14:42:21.990754
# Unit test for function to_json_schema
def test_to_json_schema():
    import json

    def check_to_from(value):
        field = validator_from_json_schema(to_json_schema(value))
        validate(field, value)
        assert to_json_schema(value) == to_json_schema(field)

    check_to_from(False)
    check_to_from(0)
    check_to_from(None)
    check_to_from(ValueError())

    check_to_from(Integer())
    check_to_from(Integer(minimum=2))
    check_to_from(Integer(maximum=1))
    check_to_from(Integer(exclusive_minimum=True))
    check_to_from(Integer(exclusive_maximum=True))
    check_to_from(Integer(multiple_of=2))

    check_to

# Generated at 2022-06-14 14:42:34.033282
# Unit test for function to_json_schema
def test_to_json_schema():
    class MySchema(Schema):
        pass
    class MySchemaWithDefinitions(Schema):
        pass
    s = MySchema.make_validator()

    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False
    assert to_json_schema(s) == {}

    assert to_json_schema(s.make_field(String)) == {
        "type": "string", "default": NO_DEFAULT}
    assert to_json_schema(s.make_field(String, default="foo")) == {
        "type": "string", "default": "foo"}

# Generated at 2022-06-14 14:42:38.796981
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(AllOf([])) == {"allOf": []}
    assert to_json_schema(Not(Any())) == {"not": True}
    assert to_json_schema(IfThenElse(Any(), Any())) == {
        "if": True,
        "then": True,
    }



# Generated at 2022-06-14 14:42:51.186130
# Unit test for function from_json_schema
def test_from_json_schema():
    import json

    definition_schema = String(pattern=r"^#/definitions/.*")


# Generated at 2022-06-14 14:43:02.570374
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from typesystem.schemas import JSONSchema

    from_json_schema_type.defined = False
    assert not from_json_schema_type.defined

    # type_string == "number"
    xn = {
        "type": "number",
        "minimum": 1,
        "maximum": 2,
    }
    expected = Float(minimum=1, maximum=2, allow_null=False)
    actual = from_json_schema(xn)
    assert actual.validate(1.5) == 1.5
    assert actual.validate(0) == 0
    assert actual.validate(3) == 3
    assert expected == actual

    # type_string == "integer"

# Generated at 2022-06-14 14:43:08.738172
# Unit test for function from_json_schema
def test_from_json_schema():
    assert isinstance(from_json_schema(True), Any)
    assert isinstance(from_json_schema(True, definitions=definitions), Any)
    assert isinstance(from_json_schema(False), NeverMatch)
    assert isinstance(from_json_schema(False, definitions=definitions), NeverMatch)
    assert from_json_schema({"$ref": "#/definitions/string"}) == definitions["#/definitions/string"]

    # Enum
    assert isinstance(from_json_schema({"enum": ["a", "b", "c"]}), Choice)

    # Constraints
    assert isinstance(from_json_schema({"pattern": "(a|b)"}), String)
    assert isinstance(from_json_schema({"exclusiveMaximum": 10}), Number)


# Generated at 2022-06-14 14:43:17.795182
# Unit test for function from_json_schema
def test_from_json_schema():
    """ Unit test for function from_json_schema. """
    assert from_json_schema({}) == Any()

    # Boolean
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()

    # Const
    assert from_json_schema({"const": "a"}).constraints == (
        Const("a"),
    )

    # Enum
    assert from_json_schema({"enum": [1, 2]}).constraints == (
        Choice(choices=[1, 2]),
    )

    # AllOf

# Generated at 2022-06-14 14:43:24.179293
# Unit test for function to_json_schema
def test_to_json_schema():
    # Type: Object
    schema = {"properties": {"a": Integer(minimum=1), "b": String()}}
    json_schema = {
        "type": "object",
        "properties": {
            "a": {
                "type": "integer",
                "minimum": 1,
                "default": NO_DEFAULT,
                "allow_null": False,
            },
            "b": {
                "type": ["string", "null"],
                "default": NO_DEFAULT,
                "allow_null": True,
            },
        },
        "required": ["a", "b"],
        "additionalProperties": False,
    }
    assert to_json_schema(schema) == json_schema
    # Type: Array

# Generated at 2022-06-14 14:43:33.386560
# Unit test for function to_json_schema
def test_to_json_schema():
    from .main import Schema, String, Integer, Boolean
    from .main import Array, Object, Choice, Const, Not, Number
    
    class MySchema(Schema):
        foo = Integer()
        bar = String()

    schema = MySchema()
    schema_schema = Schema.from_field(schema.make_validator())
    assert to_json_schema(schema) == {
        "bar": {
            "default": None,
            "type": "string"
        },
        "foo": {
            "default": None,
            "type": "integer"
        }
    }

# Generated at 2022-06-14 14:43:41.544959
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    schema_data = {
        "oneOf": [
            {"type": "integer"},
            {"type": "string"},
        ]
    }
    field = from_json_schema(schema_data)
    assert isinstance(field, OneOf)
    assert len(field.fields) == 2
    assert isinstance(field.fields[0], Integer)
    assert isinstance(field.fields[1], String)
# End unit test for function from_json_schema



# Generated at 2022-06-14 14:43:59.735051
# Unit test for function to_json_schema
def test_to_json_schema():
    class Model(Schema):
        prop1 = Integer(minimum=1, maximum=10)

    assert to_json_schema(Model) == {
        "type": "object",
        "additionalProperties": False,
        "maxProperties": 1,
        "minProperties": 1,
        "properties": {"prop1": {"type": "integer", "maximum": 10, "minimum": 1}},
        "required": ["prop1"],
    }



# Generated at 2022-06-14 14:44:10.342596
# Unit test for function to_json_schema
def test_to_json_schema():
    # type: () -> None
    class ExampleSchema(SchemaDefinitions):
        uuid_string_field = String(pattern_regex=r"^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$")

    class Example(Schema):
        string_field = String(min_length=1)
        integer_field = Integer(minimum=0, multiple_of=1)
        boolean_field = Boolean()
        uuid_string_field = Reference(to="ExampleSchema.uuid_string_field")