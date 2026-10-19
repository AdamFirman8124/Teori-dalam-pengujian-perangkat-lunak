

# Generated at 2022-06-14 14:35:23.926392
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert (
        type_from_json_schema(
            {
                "type": "string",
                "minLength": 1,
                "maxLength": 10,
                "pattern": "^[a-zA-Z]+$",
            },
            definitions=SchemaDefinitions(),
        )
        == String(min_length=1, max_length=10, pattern=re.compile(r"^[a-zA-Z]+$"))
    )
    assert (
        type_from_json_schema(
            {"type": "null", "maxLength": "10", "minLength": "1"},
            definitions=SchemaDefinitions(),
        )
        == Const(None)
    )



# Generated at 2022-06-14 14:35:35.280982
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    from typesystem.base import Dict
    from typesystem.composites import AllOf, Boolean
    field = enum_from_json_schema(data={'enum': [1, 2, 3], 'nullable': True}, definitions={})
    assert isinstance(field, AllOf)
    assert len(field.all_of) == 2
    assert isinstance(field.all_of[0], Choice)
    assert len(field.all_of[0].choices) == 3
    assert field.all_of[0].choices == [(1,1), (2,2), (3,3)]
    assert isinstance(field.all_of[1], Boolean)
    assert field.all_of[1].allow_null == True

# Generated at 2022-06-14 14:35:39.813387
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    schema = {
        "allOf": [
            {"$ref": "#/definitions/x"},
            {"$ref": "#/definitions/y"},
        ]
    }
    json_schema = from_json_schema(schema)
    assert isinstance(json_schema, AllOf)
    assert len(json_schema.all_of) == 2



# Generated at 2022-06-14 14:35:46.516451
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    schema = {"allOf": [{"type": "string"}, {"maxLength": 10}]}
    field = all_of_from_json_schema(schema, definitions=SchemaDefinitions())
    field.validate("testing")

    schema = {"allOf": [{"type": "integer"}, {"minimum": 5}]}
    field = all_of_from_json_schema(schema, definitions=SchemaDefinitions())
    field.validate(5)

    schema = {"allOf": [{"type": "integer"}, {"minimum": 5}]}
    field = all_of_from_json_schema(schema, definitions=SchemaDefinitions())
    error_message = "not a valid value (minimum is 5)"
    assert error_message in field.errors(4)



# Generated at 2022-06-14 14:35:55.579098
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert IfThenElse(
        if_clause=Const("Test"),
        then_clause=String(),
        else_clause=Number(),
        default=NO_DEFAULT,
    ) == if_then_else_from_json_schema(
        data={
            "if": {"const": "Test"},
            "then": {"type": "string"},
            "else": {"type": "number"},
            "default": NO_DEFAULT,
        },
        definitions=None,
    )


# Unit tests for function all_of_from_json_schema

# Generated at 2022-06-14 14:36:05.709402
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    # required value
    assert one_of_from_json_schema({
        "oneOf": [
            {"type": "number"},
            {"type": "string"},
        ]
    }).validate(2)
    assert one_of_from_json_schema({
        "oneOf": [
            {"type": "number"},
            {"type": "string"},
        ]
    }).validate('2')
    # optionals
    data = {
        "oneOf": [
            {"type": "number"},
            {"type": "string"},
            {"$ref": "#/definitions/foo"}
        ],
        "definitions": {
            "foo": {
                "type": "integer",
                "default": 12
            }
        }
    }
    assert one_of_from_json_sche

# Generated at 2022-06-14 14:36:14.762506
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    import json
    from typesystem.base import ValidationError
    from typesystem.fields import String
    from typesystem.schemas import SchemaDefinitions

    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "https://example.com/arrays.schema.json",
        "description": "schema for an array of strings",
        "type": "array",
        "items": {"type": "string"},
    }

    definitions = SchemaDefinitions()
    json_schema = from_json_schema(schema, definitions=definitions)

    assert isinstance(json_schema, Array)
    assert isinstance(json_schema.items, String)


# Generated at 2022-06-14 14:36:21.661199
# Unit test for function to_json_schema
def test_to_json_schema():
    # As this is the reverse function of from_json_schema and from_json_schema is
    # already tested, we test only a few specific examples here that could fail
    # with types we use in the implementation of to_json_schema.

    # First of all let's check this function is an inverse of itself
    obj = {
        "type": "string",
        "pattern": "^(?!\\s*$).+",
        "minLength": 1,
        "maxLength": 100,
        "description": "required non-blank string",
    }
    field = from_json_schema(obj)
    assert to_json_schema(field) == obj, "inverse function is not inverse"

    # Now let's do some checks that use properties that are only available in
    # python (not available in JSON Schema)

# Generated at 2022-06-14 14:36:27.425594
# Unit test for function get_valid_types
def test_get_valid_types():
    assert get_valid_types({"type": "object"}) == ({"object"}, False)
    assert get_valid_types({"type": ["object", "null"]}) == ({"object"}, True)
    assert get_valid_types({}) == (
        {"boolean", "object", "array", "number", "string"},
        False,
    )



# Generated at 2022-06-14 14:36:32.918601
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    import numpy as np
    field = any_of_from_json_schema({"anyOf": [{"type": "string"}, {"type": "integer"}]} )
    data='string'
    assert field.validate(data) == ('string', None)
    data=5
    assert field.validate(data) == (5, None)
    data=None
    assert field.validate(data) == (None, 'Field may not be null.')
    data='5'
    assert field.validate(data) == ('5', 'Value must be an integer.')
    data=np.nan
    assert field.validate(data) == (np.nan, 'Value must be an integer.')
   

# Generated at 2022-06-14 14:37:05.207359
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    # If clause is not a bool
    with pytest.raises(ValueError):
        if_then_else_from_json_schema({"if": {}, "then": {}, "else": {}}, SchemaDefinitions())
    # If clause is a boolean and then clause is not a bool
    with pytest.raises(ValueError):
        if_then_else_from_json_schema({"if": {"const": True}, "then": {}, "else": {}}, SchemaDefinitions())
    # If clause is a boolean and else clause is not a bool
    with pytest.raises(ValueError):
        if_then_else_from_json_schema({"if": {"const": True}, "then": {}, "else": {}}, SchemaDefinitions())
    # If clause is a boolean, then clause is a boolean

# Generated at 2022-06-14 14:37:13.142719
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    json_schema = {
        "oneOf": [
            {"type": "boolean"},
            {"type": "number"},
            {"type": "object"},
        ],
        "default": True
    }
    typesystem_schema = one_of_from_json_schema(json_schema, definitions=None)
    assert typesystem_schema.schema_obj == {'default': True, 'one_of': [{'type': 'boolean'}, {'type': 'number'}, {'type': 'object'}]}


# Generated at 2022-06-14 14:37:20.758269
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    schema = {
        "type": "object",
        "properties": {
            "a": {"if": {"const": True}, "then": {"const": True}},
            "b": {"if": {"const": True}, "then": {"const": True}, "else": {"const": False}},
            "c": {"if": {"const": False}, "then": {"const": True}, "else": {"const": False}},
        },
    }
    field = from_json_schema(schema)
    assert field.validate(data={"a": True, "b": True, "c": False})



# Generated at 2022-06-14 14:37:25.469730
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    data = {
        "const": 1,
        "default": None
    }
    definitions = SchemaDefinitions()
    field = const_from_json_schema(data, definitions)
    assert isinstance(field, Const)



# Generated at 2022-06-14 14:37:33.561601
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {
        "anyOf": [
            {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "number": {"type": "number"},
                },
                "required": ["type", "number"],
            },
            {
                "type": "string",
            },
            {"type": "boolean"},
        ],
    }
    schema = any_of_from_json_schema(data, definitions=SchemaDefinitions())
    assert schema.validate("string") == "string"
    assert schema.validate({"type": "string", "number": 12}) == {"type": "string", "number": 12}
    assert schema.validate(True) is True



# Generated at 2022-06-14 14:37:44.621954
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "if": {
            "const": True,
        },
        "then": {
            "const": True,
        },
        "else": {
            "const": False,
        },
        "default": None,
    }
    assert isinstance(if_then_else_from_json_schema(data, definitions=None), IfThenElse)
    result = if_then_else_from_json_schema(data, definitions=None).schema
    assert result == {
        "if": {"const": True},
        "then": {"const": True},
        "else": {"const": False},
        "default": None,
    }


# Generated at 2022-06-14 14:37:57.274062
# Unit test for function to_json_schema
def test_to_json_schema():
    data = {"a": 1, "b": 2, "c": 3}
    schema1 = Schema(
        a=Integer(minimum=0, maximum=10, exclusive_minimum=True),
        b=Integer(minimum=0, maximum=10, exclusive_maximum=True),
        c=Integer(minimum=0, maximum=10, exclusive_minimum=True, exclusive_maximum=True),
    )
    schema2 = Schema(
        a=Integer(minimum=0, maximum=10, exclusive_minimum=True),
        b=Integer(minimum=0, maximum=10, exclusive_maximum=True),
        c=Integer(minimum=0, maximum=10, exclusive_minimum=True, exclusive_maximum=True),
    )
    assert schema1.validate(data)
    assert schema2.validate(data)
    expected_data

# Generated at 2022-06-14 14:38:08.273601
# Unit test for function to_json_schema
def test_to_json_schema():
    class UserSchema(Schema):
        name = String(max_length=1024)
        age = Integer(minimum=0, maximum=150)
    raw = to_json_schema(UserSchema)
    assert raw == {
        "type": "object",
        "properties": {
            "name": {
                "type": ["string", "null"],
                "maxLength": 1024
            },
            "age": {
                "type": "integer",
                "minimum": 0,
                "maximum": 150
            }
        },
        "required": ["name", "age"]
    }
    raw = to_json_schema(UserSchema(allow_unknown=True))

# Generated at 2022-06-14 14:38:16.368940
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from typesystem.schemas import SchemaDefinitions

    definitions = SchemaDefinitions()

# Generated at 2022-06-14 14:38:21.194523
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data: dict = {
        "if": {"type": "integer", "minimum": 4},
        "then": {"type": "integer", "minimum": 8},
        "else": {"type": "integer", "minimum": 12},
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    assert_schema_is(
        result, Int(minimum=12), {"value": 1}, {"value": 3}, {"value": 2}, {"value": 5}
    )



# Generated at 2022-06-14 14:38:44.752711
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data: dict = {
        "if": {
            "type": "boolean",
        },
        "then": {
            "type": "integer",
        },
        "else": {
            "type": "string",
        },
    }
    field: Field = if_then_else_from_json_schema(data=data, definitions=None)
    assert_valid(field, True)
    assert_valid(field, False)
    assert_valid(field, 1)
    assert_valid(field, "")
    assert_invalid(field, None)
    assert_invalid(field, 1.5)
    assert_invalid(field, [])
    assert_invalid(field, {})


# Generated at 2022-06-14 14:38:50.101235
# Unit test for function not_from_json_schema

# Generated at 2022-06-14 14:39:00.080798
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    json_data = {
        "$id": "https://example.com/person.schema.json",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Person",
        "type": "object",
        "properties": {
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "age": {"description": "Age in years", "type": "integer", "minimum": 0},
        },
    }

    schema = from_json_schema(
        data=json_data
    )  #JSONSchema(additional_properties=False)  # noqa: E501
    assert schema._fields["firstName"].__class__.__name__ == "String"

# Generated at 2022-06-14 14:39:09.945670
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "http://example.com/product.schema.json",
        "title": "Product",
        "description": "A product from Acme's catalog",
        "type": "object",
        "properties": {
            "productId": {
                "description": "The unique identifier for a product",
                "type": "integer"
            },
        },
        "required": ["productId"],
    }
    result = not_from_json_schema(data, definitions)
    
    

# Generated at 2022-06-14 14:39:15.534339
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type({"type": "number"}, type_string="number", allow_null=False, definitions=definitions), Number)
    assert isinstance(from_json_schema_type({"type": "integer"}, type_string="integer", allow_null=False, definitions=definitions), Integer)
    assert isinstance(from_json_schema_type({"type": "string"}, type_string="string", allow_null=False, definitions=definitions), String)
    assert isinstance(from_json_schema_type({"type": "boolean"}, type_string="boolean", allow_null=False, definitions=definitions), Boolean)

# Generated at 2022-06-14 14:39:20.928723
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    negated = String()
    kwargs = {"negated": negated, "default": 1}
    not_ = Not(**kwargs)
    data = {"not": "string"}
    assert (not_from_json_schema(data=data, definitions=None) == not_)
    return 



# Generated at 2022-06-14 14:39:25.438721
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Schema(fields={"foo": String()})
    result = to_json_schema(schema)
    assert result == {
        "type": "object",
        "properties": {"foo": {"type": "string"}},
        "required": ["foo"],
    }

    schema = Schema(fields={"foo": String()}, additional_properties=False)
    result = to_json_schema(schema)
    assert result == {
        "type": "object",
        "properties": {"foo": {"type": "string"}},
        "required": ["foo"],
        "additionalProperties": False,
    }

    schema = Schema(fields={"foo": String()}, null_by_default=True)
    result = to_json_schema(schema)

# Generated at 2022-06-14 14:39:28.168256
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    check_field(
        not_from_json_schema,
        {"type": "number", "not": {"type": "integer"}},
        {1, 1.1, 1.4},
        {1, 1.4},
        {1.1},
    )


# Generated at 2022-06-14 14:39:30.730987
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    from .test.test_json_schema import test_not_from_json_schema as t
    return t()



# Generated at 2022-06-14 14:39:40.062132
# Unit test for function to_json_schema
def test_to_json_schema():
    # type: () -> None
    class Concrete(Schema):
        integer = Integer()
        string = String()
        enumeration = Choice(choices=[("a", "A"), ("b", "B")])
        boolean = Boolean()

        inner_object = Object(properties={"string": String()})
        array = Array(items=Integer())

    validator = Concrete.make_validator()
    result = to_json_schema(validator)

# Generated at 2022-06-14 14:40:21.396480
# Unit test for function if_then_else_from_json_schema

# Generated at 2022-06-14 14:40:32.250779
# Unit test for function to_json_schema

# Generated at 2022-06-14 14:40:43.819378
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    # Given: an if, then, else JSON Schema
    data = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "moo": {
                "if": {"type": "string"},
                "then": {"type": "boolean"},
                "else": {"type": "null"},
            },
        },
    }

    definitions = SchemaDefinitions()
    if_then_else_field = if_then_else_from_json_schema(data, definitions=definitions)

    # Then: expect a field with a mapping function
    assert isinstance(if_then_else_field, Field)
    mapping_function = if_then_else_field.get_mapping_function()

    # And:

# Generated at 2022-06-14 14:40:54.168408
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from typesystem.fields import Boolean, Integer, Float, Object, Array

    assert from_json_schema_type({}, type_string="integer", allow_null=True) == Integer(
        allow_null=True
    )
    assert from_json_schema_type({}, type_string="number", allow_null=True) == Float(
        allow_null=True
    )
    assert from_json_schema_type({}, type_string="boolean", allow_null=True) == Boolean(
        allow_null=True
    )
    assert from_json_schema_type({}, type_string="object", allow_null=True) == Object(
        allow_null=True
    )

# Generated at 2022-06-14 14:40:58.469938
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    # JSONSchema(not) -> Not()
    schema = {
        "not": {"type": "string"}
    }
    not_field = not_from_json_schema(schema)
    assert isinstance(not_field, Not)
    assert not_field.negated == String()

    schema = {
        "not": {"type": "string"},
        "default": "x"
    }
    not_field = not_from_json_schema(schema)
    assert isinstance(not_field, Not)
    assert not_field.negated == String()
    assert not_field.default == "x"

    # Not() -> String()
    assert String() == Not(Any())
    assert String() == Not(Null())


# Generated at 2022-06-14 14:41:09.436501
# Unit test for function to_json_schema
def test_to_json_schema():
    class MySchema(Schema):
        a = String()

    schema = MySchema()
    schema.a.help_text = "A string"
    schema.a.label = "A string of text"
    schema.a.max_length = 100
    schema.a.min_length = 1
    schema.a.default = "Default string value"
    schema.a.allow_null = True
    schema.a.pattern = r"^\w+$"
    schema.a.pattern_regex = re.compile(r"^\w+$", re.RegexFlag.UNICODE)

    schema.a.enum = [("a", "A"), ("b", "B")]
    schema.a.const = "a"

    schema.a.all_of = [String(), Integer()]
    schema

# Generated at 2022-06-14 14:41:19.789055
# Unit test for function to_json_schema
def test_to_json_schema():
    from pypika.json_schema.schema_definitions import String

    field = String()
    data = to_json_schema(field)
    assert data == {"type": "string"}, data

    field = String()
    data = to_json_schema(field)
    assert data == {"type": "string"}, data

    field = Integer()
    data = to_json_schema(field)
    assert data == {"type": "integer"}, data

    field = Float()
    data = to_json_schema(field)
    assert data == {"type": "number"}, data

    field = String()
    data = to_json_schema(field)
    assert data == {"type": "string"}, data

    field = Array()
    data = to_json_schema(field)

# Generated at 2022-06-14 14:41:30.784165
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Integer()) == {
        "type": ["integer", "null"],
        "minimum": -2147483648,
        "maximum": 2147483647,
        "exclusiveMinimum": False,
        "exclusiveMaximum": False,
    }
    assert to_json_schema(Integer(minimum=-3, maximum=None)) == {
        "type": ["integer", "null"],
        "minimum": -3,
        "maximum": 2147483647,
        "exclusiveMinimum": False,
        "exclusiveMaximum": False,
    }

# Generated at 2022-06-14 14:41:43.284771
# Unit test for function to_json_schema
def test_to_json_schema():
    import json
    import yaml
    from voluptuous_serialize.schema import get_definition_string, HasDefinitions
    import voluptuous as vol

    # Test a few simple scenarios
    schema_a = vol.All([], vol.Length(min=5))
    schema_b = vol.Schema(
        {
            vol.Required("a"): vol.All(
                vol.Coerce(int), vol.Range(min=0), vol.Range(max=10)
            ),
            vol.Required("b"): vol.All(
                vol.Coerce(str), vol.Length(min=5), vol.Length(max=10)
            ),
        }
    )

# Generated at 2022-06-14 14:41:50.738347
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem.fields import Array
    from typesystem.tests.schema_stubs import example_schema
    from typesystem.tests.sample_data import user
    from typesystem.tests.validators import validate_user

    schema = example_schema()
    assert from_json_schema(schema.as_json_schema()) == schema

    # test for 'validate_user'
    assert validate_user(user) is True


# Generated at 2022-06-14 14:42:08.086060
# Unit test for function to_json_schema
def test_to_json_schema():
    arg = Integer()
    assert to_json_schema(arg) == {"type": "integer"}

# Generated at 2022-06-14 14:42:18.995546
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    type(from_json_schema({ "type": "not", "not": { "type": "object" }}))
    type(from_json_schema({ "type": "not", "default": 1, "not": { "type": "object" }}))
    type(from_json_schema({ "type": "not", "default": 1, "not": { "type": "object",  "default": 2 }}))
    type(from_json_schema({ "type": "not", "default": 1, "not": { "type": "object",  "default": 2 }, "default": 3}))
    type(from_json_schema({ "type": "not", "default": 1, "not": { "type": "object",  "default": 2 }, "default": 3 }))


# Generated at 2022-06-14 14:42:30.061216
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Schema(
        name=String(min_length=0, max_length=1024), age=Integer(minimum=0)
    )
    json_schema = to_json_schema(schema)
    assert json_schema == {
        "definitions": {
            "Person": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": ["string", "null"],
                        "minLength": 0,
                        "maxLength": 1024,
                    },
                    "age": {
                        "type": ["integer", "null"],
                        "minimum": 0,
                    },
                },
                "required": ["name", "age",],
            }
        },
        "$ref": "#/definitions/Person",
    }
    schema = Integer(multiple_of=2)

# Generated at 2022-06-14 14:42:40.653276
# Unit test for function from_json_schema
def test_from_json_schema():
    # Example from http://json-schema.org/understanding-json-schema/reference/generic.html
    data = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "$id": "http://example.com/product.schema.json",
        "title": "Product",
        "description": "A product from Acme's catalog",
        "type": "object",
        "properties": {
            "productId": {
                "description": "The unique identifier for a product",
                "type": "integer"
            },
        },
        "required": ["productId"]
    }
    assert from_json_schema(data) == Object(
        properties={"productId": Integer(none_allowed=False)},
        required=["productId"]
    )

# Generated at 2022-06-14 14:42:47.572925
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {
        "not": {
            "type": "string",
            "minLength": 3,
            "maxLength": 8
        },
        "default": "default"
    }
    result = not_from_json_schema(data, {})
    expected = Not(String(min_length=3, max_length=8), 'default')
    assert result == expected





# Generated at 2022-06-14 14:42:53.189251
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = not_from_json_schema(
        {
            "not": {
                "type": [
                    "null",
                    "integer",
                ],
                "minimum": 1,
                "maximum": 100,
            },
        }
    )
    assert schema.validate(0) == (0, None)
    assert schema.validate(1) != (1, None)



# Generated at 2022-06-14 14:42:55.773499
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    assert not_from_json_schema({"not": "string"}, None).validate("object") == True



# Generated at 2022-06-14 14:43:05.952298
# Unit test for function to_json_schema
def test_to_json_schema():
    field = AllOf([Integer(minimum=5), Integer(maximum=10)])
    result = to_json_schema(field)
    assert result == {
        "allOf": [
            {"type": "integer", "minimum": 5},
            {"type": "integer", "maximum": 10},
        ]
    }
    assert to_json_schema(Any()) is True
    assert to_json_schema(NeverMatch()) is False

    class FooSchema(Schema):
        foo = Integer()

    result = to_json_schema(FooSchema)
    assert result == {"definitions": {"FooSchema": {"type": "object", "properties": {}}}}



# Generated at 2022-06-14 14:43:12.663757
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = {"not": {"type": "string"}}
    result = not_from_json_schema(schema)
    assert isinstance(result, Not) is True
    assert isinstance(result.negated, String) is True
    schema = {"not": {"type": "string", "enum": ["a"]}}
    result = not_from_json_schema(schema)
    assert isinstance(result, Not) is True
    assert isinstance(result.negated, Not) is True



# Generated at 2022-06-14 14:43:20.176020
# Unit test for function to_json_schema
def test_to_json_schema():
    import json

    class Simple(Schema):
        my_string = String()
        my_int = Integer()

    simple_field = Simple().make_validator()

    class Complex(Schema):
        my_simple = Simple()
        int_1 = Integer()
        int_2 = Integer()

    complex_field = Complex().make_validator()

    class Root(Schema):
        simple = Simple()
        complex = Complex()
        my_default_int = Integer(default=42)

    root = Root().make_validator()


# Generated at 2022-06-14 14:43:38.463831
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert IfThenElse(Const(True), Const(1), Const(2)) == IfThenElse(
        if_clause=Const(True), then_clause=Const(1), else_clause=Const(2)
    )
    assert IfThenElse(Const(False), Const(1), Const(2)) == IfThenElse(
        if_clause=Const(False), then_clause=Const(1), else_clause=Const(2)
    )

    assert IfThenElse(Const(True), Const(1), None) == IfThenElse(
        if_clause=Const(True), then_clause=Const(1)
    )

# Generated at 2022-06-14 14:43:47.571125
# Unit test for function to_json_schema
def test_to_json_schema():
    from . import JSONSchema

    class TestSchema(Schema):
        a = Field()
        b = Field()

    class InnerSchema(Schema):
        c = Field()
        d = Field()

    class InnerInnerSchema(Schema):
        e = Field()

    class TestSchema2(Schema):
        a = Field()
        b = Field()
        c = Field()

        def __schema_validate(self, value):
            return value

    schema = TestSchema(a=String(description="yo"), b=InnerSchema(c=1))
    data = to_json_schema(schema)

    assert JSONSchema().validate(data)

    data = JSONSchema().dict_to_schema(data)
    schema = from_json_schema(data)

# Generated at 2022-06-14 14:43:56.410893
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    data = {
        "type": "number"
    }

    assert isinstance(from_json_schema_type(data, type_string='number', allow_null=False, definitions=None), Field)
    assert not isinstance(from_json_schema_type(data, type_string='number', allow_null=False, definitions=None), Integer)
    assert isinstance(from_json_schema_type(data, type_string='number', allow_null=True, definitions=None), Field)

    assert isinstance(from_json_schema_type(data, type_string='integer', allow_null=False, definitions=None), Field)
    assert isinstance(from_json_schema_type(data, type_string='integer', allow_null=False, definitions=None), Integer)

# Generated at 2022-06-14 14:44:01.366194
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    from . import Field

    class Schema(Field):
        def convert(self, value, **kwargs) -> typing.Any:
            return value

    schema = Schema()

    data = {
        "if": {"properties": {"foo": {"type": "integer"}}},
        "then": {"properties": {"bar": {"type": "integer"}}},
    }
    parsed_schema = if_then_else_from_json_schema(data, definitions=None)
    assert parsed_schema.validate({"foo": 1, "bar": 1}) == {"foo": 1, "bar": 1}
    assert parsed_schema.validate({"foo": 1}) is None
    assert parsed_schema.validate({"foo": "1", "bar": 1}) is None

# Generated at 2022-06-14 14:44:05.833718
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    """
    Unit test to check function if_then_else_from_json_schema
    """
    # default values
    if_clause = Boolean()
    data = {"if": {"type": "boolean"}, "then": None, "else": None}
    field = if_then_else_from_json_schema(data, SchemaDefinitions())
    assert field.if_clause == if_clause
    assert field.then_clause is None
    assert field.else_clause is None
    assert field.default is NO_DEFAULT

    # if clause is empty
    data = {"if": {}, "then": None, "else": None}
    field = if_then_else_from_json_schema(data, SchemaDefinitions())

# Generated at 2022-06-14 14:44:10.919829
# Unit test for function to_json_schema
def test_to_json_schema():
    class TestSchema(Schema):
        field = Integer()

    value = TestSchema.make_validator()
    data = to_json_schema(value)

    expected = {
        "type": "object",
        "properties": {
            "field": {
                "type": ["integer", "null"],
            },
        },
        "required": ["field"],
    }
    assert data == expected

