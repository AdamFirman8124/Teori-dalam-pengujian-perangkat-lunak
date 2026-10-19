

# Generated at 2022-06-14 14:35:40.844929
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    sch = one_of_from_json_schema(
        {
            "allOf": [
                {
                    "$ref": "#/definitions/User",
                },
                {
                    "type": "object",
                    "properties": {
                        "is_active": {"type":"boolean"}
                    }
                }
            ],
            "anyOf": [
                {"type":"string"}
            ],
            "oneOf": [
                {"type": "object", "properties": {}, "additionalProperties": True},
                {"type": "array", "items": {"$ref": "#"}},
            ],
            "default": "tim",
            "definitions": {"User": {"type": "object", "properties": {}}}
        },
        definitions=None
    )
    class ValidationError(Exception):
        pass


# Generated at 2022-06-14 14:35:52.385375
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Float()) == {"type": "number"}
    assert to_json_schema(Decimal()) == {"type": "number"}
    assert to_json_schema(Boolean()) == {"type": "boolean"}
    assert to_json_schema(Array(items=Integer())) == {"type": "array", "items": {"type": "integer"}}
    assert to_json_schema(Array()) == {"type": "array"}
    assert to_json_schema(Integer(default=1)) == {"type": "integer", "default": 1}

# Generated at 2022-06-14 14:35:55.631394
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert enum_from_json_schema({'enum':[1,2,3]}) == Choice([(1,1),(2,2),(3,3)])

# Generated at 2022-06-14 14:36:05.710100
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    # Load test data from JSON
    import json
    from typesystem.base import ValidationError

    test_data = json.loads("""
    {"allOf": [{"type": ["string", "integer"]}, {"minimum": 5}]}
    """)

    # Test with valid input
    input = "abc"
    try:
        check_all_of_from_json_schema(input)
        assert False, "Got to the 'unreachable' code past validation"
    except ValidationError:
        pass

    input = 5
    try:
        check_all_of_from_json_schema(input)
    except ValidationError:
        assert False, "Got to the 'unreachable' code past validation"

    input = {"type": "string", "minimum": 5}

# Generated at 2022-06-14 14:36:14.794809
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = SchemaASDF(Integer())
    assert to_json_schema(schema, {}) == {
        "type": "object",
        "properties": {"asdf": {"type": "integer"}},
        "required": ["asdf"],
    }

    schema = SchemaASDF(Boolean())
    assert to_json_schema(schema, {}) == {
        "type": "object",
        "properties": {"asdf": {"type": "boolean"}},
        "required": ["asdf"],
    }

    schema = SchemaASDF(AllOf(Integer(), Minimum(5)))

# Generated at 2022-06-14 14:36:18.335124
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    ref_field = ref_from_json_schema({"$ref": "#/the_schema"}, definitions={})
    assert isinstance(ref_field, Reference)
    assert ref_field.to == "#/the_schema"
    assert ref_field.definitions is not None



# Generated at 2022-06-14 14:36:23.238544
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    definitions = SchemaDefinitions()
    definitions["#/definitions/foo"] = Any()
    assert isinstance(ref_from_json_schema({"$ref": "#/definitions/foo"}, definitions), Reference)



# Generated at 2022-06-14 14:36:33.828692
# Unit test for function any_of_from_json_schema

# Generated at 2022-06-14 14:36:41.125933
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    def test_for_integer():
        obj = {
            "oneOf": [
                {
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 100,
                },
                {
                    "type": "integer",
                    "minimum": 200,
                    "maximum": 300,
                },
            ]
        }
        obj_schema = one_of_from_json_schema(obj,definitions)
        assert obj_schema.validate(0) is True
        assert obj_schema.validate(100) is True
        assert obj_schema.validate(200) is True
        assert obj_schema.validate(300) is True
        assert obj_schema.validate("Hello world") is False


# Generated at 2022-06-14 14:36:44.914613
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {"allOf": [{"type": "string"}, {"minLength": 3}]}
    all_of = all_of_from_json_schema(data, definitions)
    assert all_of.to_json_schema() == data



# Generated at 2022-06-14 14:37:46.485530
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    from typesystem.typing import get_origin_and_arguments

    schema = {
        "allOf": [
            {"type": "number"},
            {"minimum": 0, "default": 1},
            {"maximum": 100},
        ]
    }

# Generated at 2022-06-14 14:37:50.892301
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = {"not": {}}
    field = not_from_json_schema(schema, {})
    print(field.schema())
    assert field.schema() == {'not': {}}



# Generated at 2022-06-14 14:37:54.873860
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema({"allOf": [{"type": "string", "minLength": 1}, {"type": "string", "maxLength": 3}]})


# Generated at 2022-06-14 14:38:02.064493
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    if_then_else = if_then_else_from_json_schema(
        {
            "if": {"type": "integer"},
            "then": {"type": "string"},
            "else": {"type": "number"},
            "default": "c",
        },
        definitions=None,
    )
    assert isinstance(if_then_else, IfThenElse)
    assert isinstance(if_then_else.if_clause, Integer)
    assert isinstance(if_then_else.then_clause, String)
    assert isinstance(if_then_else.else_clause, Float)


JSONSchema = from_json_schema



# Generated at 2022-06-14 14:38:11.195836
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert enum_from_json_schema({"enum": ["a", "b", "c", None]}, None).deserialize(None) == None
    assert enum_from_json_schema({"enum": ["a", "b", "c", None]}, None).deserialize("a") == "a"
    assert enum_from_json_schema({"enum": ["a", "b", "c", None]}, None).deserialize(0) == "a"
    assert enum_from_json_schema({"enum": ["a", "b", "c", None]}, None).deserialize(2) == "c"
    assert enum_from_json_schema({"enum": ["a", "b", "c", None]}, None).deserialize(3) == None
    assert enum_from_json_

# Generated at 2022-06-14 14:38:15.605760
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    mySchema = from_json_schema({"const":"it works"})
    assert mySchema(None) == None
    assert mySchema("it works") == "it works"
    assert mySchema("bad") == "bad"



# Generated at 2022-06-14 14:38:22.822384
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    """
    Test the function 'if_then_else_from_json_schema'.
    """
    from . import ValidationError
    from .field import NeverMatch

    definitions = SchemaDefinitions()
    if_clause = Boolean(default=False)
    then_clause = Integer(default=2)
    else_clause = String(default='b')
    if_then_else_schema = if_then_else_from_json_schema({'if': if_clause,
                                                         'then': then_clause,
                                                         'else': else_clause},
                                                        definitions=definitions)
    assert isinstance(if_then_else_schema, IfThenElse)
    assert if_then_else_schema.if_clause == if_clause
    assert if_then

# Generated at 2022-06-14 14:38:26.720207
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = {"not": {"type": "integer"}, "default": None}
    field = not_from_json_schema(schema)
    assert field.clean() == None
    assert field.clean(value=1) == 1
    assert field.clean(value='1') == '1'


# Generated at 2022-06-14 14:38:37.603171
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    from typesystem import from_json_schema
    from typesystem.fields import Choice
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "http://example.com/product.schema.json",
        "title": "Product",
        "description": "A product from Acme's catalog",
        "type": "object",
        "properties": {
            'product_id': {
                "type": "string",
                "description": "The unique identifier for a product",
                "enum": ["do_re_mi", "fa_so_la_ti", "fur_elise"]
            }
        },
    }
    field = from_json_schema(schema)

# Generated at 2022-06-14 14:38:42.402546
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {
        'oneOf': [{'const': 1}, {'const': 2}]
    }
    definitions = SchemaDefinitions()
    field = one_of_from_json_schema(data, definitions=definitions)
    assert field.validate(1) == True
    assert field.validate(2) == True
    assert field.validate(3) == False
# End unit test for function one_of_from_json_schema



# Generated at 2022-06-14 14:40:15.729201
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {"anyOf": [{"type": "string"}, {"type": "integer"}]}
    field = any_of_from_json_schema(data)
    assert field.validate("a") == "a"
    assert field.validate(2) == 2
    assert field.validate(2.1) == 2.1

# Generated at 2022-06-14 14:40:17.930331
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = dict(anyOf=[dict(type='string')])
    schema = any_of_from_json_schema(data, definitions)
    assert isinstance(schema, Union)



# Generated at 2022-06-14 14:40:21.814937
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    json = {"anyOf": [{"type": "number"}]}
    assert any_of_from_json_schema(json, None) == Union(any_of=[Number()])



# Generated at 2022-06-14 14:40:32.539485
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({}, {}) == Any()
    assert type_from_json_schema({"type": "string"}, {}) == String()
    assert type_from_json_schema({"type": "string", "minLength": 1}, {}) == String(min_length=1)
    assert type_from_json_schema({"type": "string", "format": "email"}, {}) == String(format="email")
    assert type_from_json_schema({"type": "integer", "format": "email"}, {}) == String(format="email")
    assert type_from_json_schema({"type": "integer"}, {}) == Integer()
    assert type_from_json_schema({"type": "boolean"}, {}) == Boolean()
    assert type_from_json_schema

# Generated at 2022-06-14 14:40:44.372368
# Unit test for function any_of_from_json_schema

# Generated at 2022-06-14 14:40:48.445995
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {
        "allOf": [
            {"type": "number"},
            {"minimum": 0},
            {"maximum": 100}
        ]
    }
    field = all_of_from_json_schema(data, definitions=SchemaDefinitions())
    assert isinstance(field, AllOf)



# Generated at 2022-06-14 14:40:56.468530
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    all_of = [
        Object(properties={"id": Integer()}),
        Object(properties={"name": String()}),
    ]
    data = {"anyOf": all_of}
    definitions = SchemaDefinitions()
    parents = []
    actual = any_of_from_json_schema(data, definitions)
    expected = Union(
        any_of=[
            Object(properties={"name": String()}),
            Object(properties={"id": Integer()}),
        ]
    )
    assert actual == expected


# Generated at 2022-06-14 14:40:57.276958
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    pass



# Generated at 2022-06-14 14:41:05.344292
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    schema = {
        "anyOf": [
            {
                "type": "string",
                "maxLength": 1,
            },
            {
                "type": ["integer", "number"],
                "minimum": 0,
                "maximum": 20,
            },
        ]
    }
    try:
        field = from_json_schema(schema)
        assert field is not None
    except Exception as e:
        print(e)
        assert False


# Generated at 2022-06-14 14:41:17.019408
# Unit test for function to_json_schema
def test_to_json_schema():
    from zuper_typing import dataclass, ztatic

    @ztatic
    @dataclass
    class Obj:
        x: bool
        y: int
        z: str

    D = {Obj: 1}
    schema = load_schema(D)
    schema_json = to_json_schema(schema)
    schema_json == {
        "definitions": {"Obj": {"properties": {"x": {"type": "boolean"}, "y": {"type": "integer"}, "z": {"type": "string"}}, "required": ["x", "y", "z"], "type": "object"}},
        "properties": {"Obj": {"$ref": "#/definitions/Obj"}},
        "type": "object",
    }



# Generated at 2022-06-14 14:41:55.960944
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Integer(minimum=10)) == {"type": "integer", "minimum": 10}
    assert to_json_schema(Float(exclusiveMaximum=10)) == {
        "type": "number",
        "exclusiveMaximum": 10,
    }
    assert to_json_schema(Decimal(multipleOf="0.1")) == {
        "type": "number",
        "multipleOf": 0.1,
    }
    assert to_json_schema(Boolean()) == {"type": "boolean"}
    assert to_json_schema(Boolean(allow_null=True)) == {"type": ["boolean", "null"]}


# Generated at 2022-06-14 14:42:05.897741
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    """
    Test proper construction of typed field from JSON schema.
    """
    assert type_from_json_schema(
        {
            "type": "null",
        },
        definitions=None,
    ) == Const(None)

    # Union of const fields
    assert type_from_json_schema(
        {
            "type": ["boolean", "null"],
        },
        definitions=None,
    ) == Union(any_of=[Boolean(), Const(None)])

    assert type_from_json_schema(
        {
            "type": ["string", "null"],
        },
        definitions=None,
    ) == Union(any_of=[String(), Const(None)])


# Generated at 2022-06-14 14:42:16.865432
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({ "type": "string" }) == String()
    assert type_from_json_schema({ "type": "integer" }) == Integer()
    assert type_from_json_schema({ "type": "number" }) == Number()
    assert type_from_json_schema({ "type": "object" }) == Object()
    assert type_from_json_schema({ "type": "array" }) == Array()
    assert type_from_json_schema({ "type": "null" }) == Const(None)
    assert type_from_json_schema({ "type": "boolean" }) == Boolean()
    assert type_from_json_schema({ "type": "string", "nullable": True }) == String(allow_null=True)
    assert type_from_json_sche

# Generated at 2022-06-14 14:42:25.689003
# Unit test for function to_json_schema
def test_to_json_schema():
    data = to_json_schema(Integer(min_value=1, max_value=2))
    assert data == {
        "type": "integer",
        "minimum": 1,
        "maximum": 2,
        "default": NO_DEFAULT,
    }

    data = to_json_schema(
        SchemaDefinitions(
            {
                "name": String(),
                "id": Integer(default=1),
                "person": Object(
                    {
                        "name": Reference("name"),
                        "id": Reference("id"),
                        "name2": Reference("name"),
                    }
                ),
            }
        )
    )

# Generated at 2022-06-14 14:42:30.114944
# Unit test for function from_json_schema
def test_from_json_schema():
    assert isinstance(from_json_schema({"type": "array", "items": {}}), Array)
    assert isinstance(from_json_schema({"type": "array", "items": {"type": "string"}}), Array)



# Generated at 2022-06-14 14:42:40.685715
# Unit test for function from_json_schema
def test_from_json_schema():
    # Booleans
    assert to_json_schema(from_json_schema(True)) == {"type": "boolean"}
    assert to_json_schema(from_json_schema(False)) == {"enum": []}

    # Strings
    assert (
        to_json_schema(from_json_schema({"type": "string"}))
        == {"type": "string"}
    )
    assert to_json_schema(from_json_schema({"minLength": 1})) == {"minLength": 1}
    assert to_json_schema(from_json_schema({"maxLength": 2})) == {"maxLength": 2}

# Generated at 2022-06-14 14:42:52.614066
# Unit test for function from_json_schema

# Generated at 2022-06-14 14:43:04.104388
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    # Boolean
    assert type_from_json_schema({"type": "boolean"}, definitions=definitions) == Boolean()
    # String
    assert type_from_json_schema({"type": "string"}, definitions=definitions) == String()
    # Integer
    assert type_from_json_schema({"type": "integer"}, definitions=definitions) == Integer()
    # Number
    assert type_from_json_schema({"type": "number"}, definitions=definitions) == Number()
    # Array
    assert type_from_json_schema({"type": "array"}, definitions=definitions) == Array(items=Any())
    # Object
    assert type_from_json_schema({"type": "object"}, definitions=definitions) == Object(
        additional_properties=Any()
    )
    # Null

# Generated at 2022-06-14 14:43:09.884739
# Unit test for function to_json_schema
def test_to_json_schema():
    class JsonSchemaModel(Schema):
        a = Integer()

    schema = to_json_schema(JsonSchemaModel)
    assert schema == {
        "definitions": {"JsonSchemaModel": {"properties": {"a": {"type": "integer"}}}},
        "$ref": "#/definitions/JsonSchemaModel",
    }



# Generated at 2022-06-14 14:43:17.116285
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    type_strings = ["number", "integer", "string", "boolean", "array", "object"]
    for type_string in type_strings:
        assert (
            isinstance(
                from_json_schema_type({"type": type_string}, type_string=type_string, allow_null=False, definitions=None),
                Field
            )
            is True
        )
    try:
        from_json_schema_type({"type": "unknown"}, type_string="unknown", allow_null=False, definitions=None)
        assert False, "should throw assertion"
    except AssertionError:
        pass


# Generated at 2022-06-14 14:44:05.710235
# Unit test for function from_json_schema
def test_from_json_schema():
    with open("tests/schemas/json-schemas/index.json") as json_file:
        definitions = SchemaDefinitions()
        for name, value in json.load(json_file)["allOf"][0]["definitions"].items():
            if "definitions" in value:
                value = value["definitions"]
            definitions[f"#/definitions/{name}"] = from_json_schema(value, definitions)

    for name, value in json.load(json_file)["definitions"].items():
        if name != "JSONSchema":
            continue
        schema = from_json_schema(
            value, SchemaDefinitions()
        ).bind(default_error_message_format="{schema_name}")