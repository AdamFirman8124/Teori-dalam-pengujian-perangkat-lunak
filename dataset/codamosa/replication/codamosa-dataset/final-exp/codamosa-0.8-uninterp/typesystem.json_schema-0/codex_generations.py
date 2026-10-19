

# Generated at 2022-06-14 14:35:07.310109
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    data = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "type": "object",
        "properties": {
            "firstName": {
                "const": "FN1",
                "type": "string",
                "default": "FN1"
            }
        },
        "required": [
            "firstName"
        ]
    }
    field = const_from_json_schema(data, None)
    assert field.validate("FN1") == {"firstName": "FN1"}
    assert field.validate("FN2") == {"firstName": "FN1"}


# Generated at 2022-06-14 14:35:16.007231
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    from . import from_json_schema
    from .utils import to_json  # noqa F401


# Generated at 2022-06-14 14:35:23.754445
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    # Test $ref
    assert (
        from_json_schema({'$ref': '#/definitions/Person'})
        == Reference(to="#/definitions/Person")
    )
    # Test Boolean
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    # Test Null
    assert from_json_schema({'type': 'null'}) == Const(None)
    # Test Boolean
    assert from_json_schema({'type': 'boolean'}) == Boolean()
    # Test Number
    assert from_json_schema({'type': 'number'}) == Float()
    assert from_json_schema({'type': 'integer'}) == Integer()

# Generated at 2022-06-14 14:35:29.872284
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string'
            },
            'age': {
                'type': 'integer'
            }
        }
    }) == Object(properties={
        'name': String(),
        'age': Integer(),
    })



# Generated at 2022-06-14 14:35:39.658999
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    json_schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "if": {"type": "string"},
            "then": {"minLength": 3},
            "default": "default string"
        }
    field = if_then_else_from_json_schema(json_schema, definitions=None)
    assert field.validate(None) == ("default string", None)

    json_schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "if": {"type": "integer"},
            "then": {"minimum": 3},
            "default": 1
        }
    field = if_then_else_from_json_schema(json_schema, definitions=None)

# Generated at 2022-06-14 14:35:45.738126
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    json = {
        "anyOf": [
            {
                "type": "string",
                "maxLength": 100,
                "default": "Hello World!",
            },
            {
                "type": "integer",
                "default": 46
            },
        ],
        "default": "Hello World!",
    }
    obj = any_of_from_json_schema(json, definitions={})
    assert obj.any_of[0].max_length == 100
    assert obj.any_of[0].default == "Hello World!"
    assert obj.any_of[1].default == 46
    assert obj.default == "Hello World!"



# Generated at 2022-06-14 14:35:53.355639
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    # Forwards
    a = const_from_json_schema(data={'const': 'test const'}, definitions={})
    assert a.validate('test const') == None
    assert a.validate('test const2') == False
    # Backwards
    a = to_json_schema(fields={'const': Const(const='test const')}, definitions={})
    assert a == {'const': 'test const'}



# Generated at 2022-06-14 14:36:05.472845
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    # Defaults to None
    schema = {"not": {"type": "string"}}
    field = from_json_schema(schema)
    assert isinstance(field, Not)
    assert field.default == NO_DEFAULT

    # Defaults to NO_DEFAULT
    field = from_json_schema(schema, {"default": None})
    assert isinstance(field, Not)
    assert field.default == NO_DEFAULT
    field = from_json_schema(schema, {"default": NO_DEFAULT})
    assert isinstance(field, Not)
    assert field.default == NO_DEFAULT
    # Defaults to default
    default = 123
    field = from_json_schema(schema, {"default": default})
    assert isinstance(field, Not)
    assert field.default == default
    

# Generated at 2022-06-14 14:36:12.760326
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "if": {
            "type": "integer"
        },
        "then": {
            "type": "integer",
            "minimum": 1
        },
        "else": Any()
    }
    field = if_then_else_from_json_schema(data, None)
    assert isinstance(field, IfThenElse)
    assert field.then_clause
    assert field.else_clause
    assert field.then_clause.validate(1)
    assert not field.else_clause.validate(1)
    assert field.else_clause.validate("a")

# Generated at 2022-06-14 14:36:19.970118
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    schema = {
        "allOf": [
            {"$ref": "#/definitions/item1"},
            {
                "type": "number",
                "minimum": 5,
                "maximum": 10
            }
        ]
    }
    
    definitions = {
        "item1": {
            "type": "string",
            "minLength": 2
        }
    }

    generated = all_of_from_json_schema(schema, definitions)
    expected = AllOf(
        [
            Reference(to="#/definitions/item1"),
            Number(minimum=5, maximum=10)
        ]
    )
    assert generated == expected

# Generated at 2022-06-14 14:36:48.458694
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    def _test(data: dict, type_string: str, allow_null: bool, schema: Field):
        assert isinstance(schema, Field)
        assert from_json_schema_type(data, type_string, allow_null, definitions) == schema

    definitions = SchemaDefinitions()

    _test(
        data={
            "type": ["number"],
            "minimum": 0,
            "maximum": 10,
            "exclusiveMinimum": True,
            "exclusiveMaximum": False,
            "multipleOf": 2,
        },
        type_string="number",
        allow_null=False,
        schema=Float(
            minimum=0,
            maximum=10,
            exclusive_minimum=True,
            exclusive_maximum=False,
            multiple_of=2,
        ),
    )

# Generated at 2022-06-14 14:36:51.469837
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    data = {"enum": ["foo"]}
    field = enum_from_json_schema(data=data, definitions=SchemaDefinitions())
    assert issubclass(field.__class__, Choice)



# Generated at 2022-06-14 14:37:00.053417
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    schema = Schema(
        one_of=[
            {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "number"},
                },
            },
            {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"},
                },
            },
        ]
    )
    assert schema({"name": "Gerard", "age": 20}) == {"name": "Gerard", "age": 20}
    assert schema({"name": "Gerard", "age": 20.0}) == {"name": "Gerard", "age": 20}

# Generated at 2022-06-14 14:37:07.172187
# Unit test for function to_json_schema
def test_to_json_schema():
    from . import (
        Array,
        Boolean,
        Choice,
        Const,
        Float,
        Integer,
        Not,
        Object,
        OneOf,
        Optional,
        Reference,
        Required,
        Schema,
        String,
        Union,
        ValidationError,
    )

    class TestSchema(Schema):
        boolean_field = Boolean()
        string_field = String()
        integer_field = Integer()
        enum_field = Choice(choices=[("A", "A"), ("B", "B")], required=False)

        class Meta:
            nullable_fields = ["boolean_field"]

    class NestedSchema(Schema):
        integer_field = Integer()


# Generated at 2022-06-14 14:37:10.672019
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert enum_from_json_schema({
        'enum': [
            'Street',
            'Avenue',
            'Boulevard']
    }, definitions=SchemaDefinitions()).validate('Street')



# Generated at 2022-06-14 14:37:15.146541
# Unit test for function to_json_schema
def test_to_json_schema():
    from . import String

    # Test that to_json_schema is the opposite of from_json_schema
    # (minus the definitions argument, which is tested elsewhere).
    for field in ALL_SCHEMA_FIELDS:
        schema = schema_from_field(field)
        json = to_json_schema(schema)
        if isinstance(field, String):
            assert json["pattern"] == field.pattern
        assert from_json_schema(json) == schema
        json["default"] = None
        assert from_json_schema(json).default == NO_DEFAULT
        assert to_json_schema(schema) == to_json_schema(field)

    # Test that non-JSON Schema formats raise an exception.
    with pytest.raises(AssertionError):
        to_json

# Generated at 2022-06-14 14:37:26.594029
# Unit test for function from_json_schema_type

# Generated at 2022-06-14 14:37:33.035633
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = '''
        {
            "oneOf": [
                {
                    "type": "integer"
                },
                {
                    "type": "string"
                }
            ]
        }
        '''
    definitions = SchemaDefinitions()
    one_of = one_of_from_json_schema(json.loads(data), definitions=definitions)
    assert isinstance(one_of, OneOf)
    assert isinstance(one_of.one_of[0], Integer)
    assert isinstance(one_of.one_of[1], String)


# Generated at 2022-06-14 14:37:40.572169
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    schema = {"enum": ["a", "b", "c"]}
    field = enum_from_json_schema(schema, definitions={})
    assert isinstance(field, Choice)
    assert len(field.choices) == 3
    assert field.choices == [("a", "a"), ("b", "b"), ("c", "c")]



# Generated at 2022-06-14 14:37:44.492080
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    '''
    Test the function enum_from_json_schema
    '''
    assert [{"enum": [1, 2, 3]}] == [enum_from_json_schema({'enum': [1, 2, 3]}, None).to_dict()]



# Generated at 2022-06-14 14:38:16.489183
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    test_data = {"oneOf":[{"type":"integer"},{"type":"string"}]}
    test_definitions = SchemaDefinitions()
    test_constraints = one_of_from_json_schema(test_data, test_definitions)
    assert isinstance(test_constraints, OneOf)
    assert isinstance(test_constraints._fields[0], Integer)
    assert isinstance(test_constraints._fields[1], String)
    assert test_constraints._default == NO_DEFAULT
    assert test_constraints._allow_null == False



# Generated at 2022-06-14 14:38:23.950331
# Unit test for function to_json_schema
def test_to_json_schema():
    from squash.validators import from_json_schema
    from squash.validators.fields import Integer
    from squash.validators.schemas import schema_registry

    @schema_registry.register
    class EnumSchema:
        enum_field = enum(a=1, b=2, c=3)

    @schema_registry.register
    class RequiredSchema:
        required_field = integer(required=True)

    @schema_registry.register
    class OptionalSchema:
        optional_field = integer(required=False)

    @schema_registry.register
    class StringSchema:
        string_field = string(
            min_length=3, max_length=10, pattern=r"^\w+$", format="uri"
        )


# Generated at 2022-06-14 14:38:34.894882
# Unit test for function one_of_from_json_schema

# Generated at 2022-06-14 14:38:42.884189
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) is Any()
    assert from_json_schema(False) is NeverMatch()
    # Test typing.Union[str, dict]
    assert from_json_schema({"type": "string"}) is String()
    # Test typing.Union[str, dict] & SchemaDefinitions
    assert from_json_schema({
        "$ref": "#/definitions/Person",
        "definitions": {
            "Person": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"},
                },
            },
        },
    }).is_valid({
        "name": "Frank",
        "age": 17,
    })
    # Test SchemaDefinitions
    definitions = Schema

# Generated at 2022-06-14 14:38:48.240120
# Unit test for function to_json_schema
def test_to_json_schema():
    arg_struct = Struct(
        title="First struct",
        properties={
            "field1": String(title="First String", allow_blank=True),
            "field2": String(title="Second String"),
        },
    )
    arg_struct.validate()
    output = to_json_schema(arg_struct)

# Generated at 2022-06-14 14:38:51.744579
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    s = '{"oneOf":[{"type":"integer"},{"type":"string"}]}'
    assert one_of_from_json_schema(json.loads(s)) == Union([Integer(allow_null=False), String(allow_null=False)])
    s = '{"oneOf":[{"type":"integer"},{"type":"string"},{"type":"null"}]}'
    assert one_of_from_json_schema(json.loads(s)) == Union([Integer(allow_null=True), String(allow_null=True), Const(None, allow_null=True)])


# Generated at 2022-06-14 14:38:55.286937
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {'oneOf': [{'const': 1}, {'const': 2}]}
    definitions = SchemaDefinitions()
    field = one_of_from_json_schema(data, definitions)
    assert isinstance(field, OneOf)
    assert field.one_of[0].const == 1
    assert field.one_of[1].const == 2


# Generated at 2022-06-14 14:39:00.749569
# Unit test for function from_json_schema
def test_from_json_schema():
    schema = Object(
        properties={"name": String(min_length=1), "age": Integer(minimum=0, exclusive_maximum=150)},
        required=["name", "age"],
        additional_properties=Boolean(),
    )
    assert from_json_schema(to_json_schema(schema)["properties"]) == schema



# Generated at 2022-06-14 14:39:03.439548
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    target = one_of_from_json_schema(dict_root, SchemaDefinitions())
    assert isinstance(target, OneOf)



# Generated at 2022-06-14 14:39:12.437991
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    all_of = ["1.1","1.2"]
    one_of = ["1.3"]
    all_of = [1.1,1.2]
    one_of = [1.3]
    assert one_of_from_json_schema(one_of, all_of) == [-1, -1]   
    assert one_of_from_json_schema(one_of, all_of) == "1.3"
    assert one_of_from_json_schema(one_of, all_of) == "1.3"



# Generated at 2022-06-14 14:39:45.817097
# Unit test for function to_json_schema
def test_to_json_schema():

    fields = {
        "name": String(max_length=10),
        "age": Integer(minimum=0, maximum=120),
        "postcode": String(pattern_regex=re.compile(r"[A-Z]{2}1[0-9]{2}")),
    }
    schema = Schema(fields=fields)
    actual = to_json_schema(schema)

# Generated at 2022-06-14 14:39:54.380141
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(
        from_json_schema_type(
            {"type": "string"}, type_string="string", allow_null=False, definitions=None
        ),
        String,
    )
    assert isinstance(
        from_json_schema_type(
            {"type": "number"}, type_string="number", allow_null=False, definitions=None
        ),
        Float,
    )
    assert isinstance(
        from_json_schema_type(
            {"type": "number"}, type_string="number", allow_null=False, definitions=None
        ),
        Float,
    )
    assert isinstance(
        from_json_schema_type(
            {"type": "integer"}, type_string="integer", allow_null=False, definitions=None
        ),
        Integer,
    )

# Generated at 2022-06-14 14:40:04.114525
# Unit test for function to_json_schema
def test_to_json_schema():
    s = to_json_schema(Schema(message=String(min_length=2, max_length=3)))
    assert s == {"type": "object", "properties": {"message": {"type": "string", "minLength": 2, "maxLength": 3}}, "required": ["message"]}
    s = to_json_schema(Schema(message=String(min_length=2, max_length=3, default="boom")))
    assert s == {"type": "object", "properties": {"message": {"type": "string", "minLength": 2, "maxLength": 3, "default": "boom"}}, "required": ["message"]}



# Generated at 2022-06-14 14:40:14.922214
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    schema = {
        "type": "object",
        "properties": {
            "answer": {"type": "number"},
            "foo": {"type": "string"},
            "bar": {"type": "array", "items": {"type": "number"}}
        }
    }
    field = from_json_schema(schema)

# Generated at 2022-06-14 14:40:19.382828
# Unit test for function to_json_schema

# Generated at 2022-06-14 14:40:28.994329
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    schema = """
    {
      "type": "object",
      "properties": {
        "age": {
          "type": "integer",
          "minimum": 0,
          "maximum": 150,
          "default": 0
        },
        "name": {
          "type": "string",
          "minLength": 5,
          "maxLength": 50,
          "default": ""
        }
      }
    }
    """
    data = from_json_schema(json.loads(schema))
    assert isinstance(data, Object)
    assert isinstance(data.properties["age"], Integer)
    assert isinstance(data.properties["name"], String)



# Generated at 2022-06-14 14:40:37.303700
# Unit test for function to_json_schema
def test_to_json_schema():
    from .schema_definitions import SchemaDefinitions

    # Case where the schema defines additional references
    schema = SchemaDefinitions(
        MySubSchema=String(min_length=4),
        MySchema=String(min_length=4, max_length=8),
    )
    expected = {
        "definitions": {
            "MySubSchema": {
                "type": "string",
                "minLength": 4,
                "default": NO_DEFAULT,
            },
            "MySchema": {"$ref": "#/definitions/MySubSchema"},
        },
        "type": "string",
        "minLength": 4,
        "maxLength": 8,
        "default": NO_DEFAULT,
    }
    assert to_json_schema(schema) == expected

    #

# Generated at 2022-06-14 14:40:48.529052
# Unit test for function to_json_schema
def test_to_json_schema():
    def assert_json_schema(
        validator: Field,
        expected_json_schema: typing.Union[bool, dict],
        description: str,
    ):
        json_schema = to_json_schema(validator)
        assert json_schema == expected_json_schema, description

    validator = String(allow_blank=False)
    schema = {
        "type": "string",
        "default": NO_DEFAULT,
        "minLength": 1,
        "default": NO_DEFAULT,
    }
    assert_json_schema(validator, schema, "String")

    validator = String(allow_blank=True)
    schema = {"type": "string"}
    assert_json_schema(validator, schema, "String")


# Generated at 2022-06-14 14:41:00.748349
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from typesystem.fields import Any, Integer, String

    c = from_json_schema_type(
        {"type": "number"}, type_string="number", allow_null=True, definitions=None
    )
    assert isinstance(c, Integer)
    assert c.allow_null == True
    assert c.minimum == None
    assert c.maximum == None
    assert c.exclusive_minimum == None
    assert c.exclusive_maximum == None
    assert c.multiple_of == None
    assert c.default == NO_DEFAULT

    c = from_json_schema_type(
        {"type": "integer"},
        type_string="integer",
        allow_null=True,
        definitions=None,
    )
    assert isinstance(c, Integer)
    assert c.allow_null == True

# Generated at 2022-06-14 14:41:03.819897
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type({"type": "integer"}, "integer", False, None), Integer)



# Generated at 2022-06-14 14:42:26.797709
# Unit test for function to_json_schema

# Generated at 2022-06-14 14:42:38.803042
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="boolean", allow_null=False,
                                 definitions=SchemaDefinitions()) == Boolean(allow_null=False)
    assert from_json_schema_type({}, type_string="boolean", allow_null=True,
                                 definitions=SchemaDefinitions()) == Boolean(allow_null=True)
    assert from_json_schema_type({}, type_string="integer", allow_null=False,
                                 definitions=SchemaDefinitions()) == Integer(allow_null=False)
    assert from_json_schema_type({}, type_string="integer", allow_null=True,
                                 definitions=SchemaDefinitions()) == Integer(allow_null=True)

# Generated at 2022-06-14 14:42:51.183802
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(String(const="foo")) == {"type": "string", "const": "foo"}
    assert to_json_schema(String(default="bar")) == {
        "type": "string",
        "default": "bar",
    }
    # assert to_json_schema(String(description='desc')) == {'type': 'string', 'description': 'desc'}
    assert to_json_schema(String(allow_blank=True)) == {
        "type": "string",
        "minLength": 0,
    }
    assert to_json_schema(String(allow_blank=False)) == {
        "type": "string",
        "minLength": 1,
    }
    assert to

# Generated at 2022-06-14 14:43:02.606720
# Unit test for function to_json_schema
def test_to_json_schema():
    class SimpleSchema(Schema):
        optional_string: str
        required_string: str
        optional_union: typing.Union[str, int]
        required_union: typing.Union[str, int]
        optional_nullable_union: typing.Union[str, typing.Optional[int]]
        required_nullable_union: typing.Union[str, typing.Optional[int]]
        optional_integer: int
        required_integer: int
        optional_float: float
        required_float: float
        optional_bool: bool
        required_bool: bool
        optional_array: typing.List[str]
        required_array: typing.List[str]
        optional_choice: typing.Optional[str]
        required_choice: str
        optional_const: typing.Optional[bool]
        required_const: bool
       

# Generated at 2022-06-14 14:43:07.232160
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Integer(required=True)
    schema.__validator_schema__ = "integer"
    json_schema = {
        "type": "integer",
        "required": True,
    }
    assert to_json_schema(schema) == json_schema
    schema = String(required=True)
    schema.__validator_schema__ = "string"
    json_schema = {
        "type": "string",
        "required": True,
    }
    assert to_json_schema(schema) == json_schema


# Generated at 2022-06-14 14:43:16.717303
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": "number"}) == Decimal()
    assert from_json_schema({"type": "boolean"}) == Boolean()
    assert from_json_schema({"type": "array"}) == Array(items=Any())
    assert from_json_schema({"type": "object"}) == Object()
    assert from_json_schema({"enum": [1, 2, 3]}) == Choice([1, 2, 3])

# Generated at 2022-06-14 14:43:21.084120
# Unit test for function to_json_schema
def test_to_json_schema():

    @dataclass
    class MySchema:
        __root__: str = String(format="guid")

    json_schema = validate_schema(to_json_schema(MySchema))

    assert json_schema == {
        "type": "object",
        "properties": {"__root__": {"type": "string", "format": "guid"}},
        "required": ["__root__"],
    }

# Generated at 2022-06-14 14:43:26.529004
# Unit test for function to_json_schema

# Generated at 2022-06-14 14:43:38.134347
# Unit test for function to_json_schema
def test_to_json_schema():
    def _test_with_schema(
        schema: Schema,
        expected_result: typing.Union[bool, dict],
        definitions: typing.Optional[SchemaDefinitions] = None,
    ) -> None:
        if not isinstance(schema, Schema):
            schema = schema()
        result = to_json_schema(schema, _definitions=definitions)
        assert result == expected_result, f"Unexpected result."

    def _test_with_field(
        field: Field,
        expected_result: typing.Union[bool, dict],
        definitions: typing.Optional[SchemaDefinitions] = None,
    ) -> None:
        result = to_json_schema(field, _definitions=definitions)
        assert result == expected_result, f"Unexpected result."


# Generated at 2022-06-14 14:43:47.441706
# Unit test for function to_json_schema
def test_to_json_schema():
    from json import loads, JSONDecodeError
    from jsonschema import validate

    assert to_json_schema(Boolean()) == {"type": "boolean"}
    validate(
        {"type": "boolean"},
        loads("""{
            "$schema": "http://json-schema.org/draft-07/schema#",
            "$id": "http://example.com/root.json",
            "type": "object"
        }"""),
    )

    assert to_json_schema(String()) == {"type": "string"}