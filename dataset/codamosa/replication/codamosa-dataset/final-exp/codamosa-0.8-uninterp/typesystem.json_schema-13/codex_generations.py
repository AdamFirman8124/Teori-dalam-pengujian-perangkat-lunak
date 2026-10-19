

# Generated at 2022-06-14 14:35:12.854377
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    test_schema = {
        "type": "object",
        "properties": {
            "id": {
                "$ref": "#/definitions/id"
            }
        },
        "definitions": {
            "id": {
                "title": "ID",
                "type": "integer"
            }
        }
    }
    typesystem_schema = from_json_schema(test_schema)
    assert typesystem_schema.properties["id"] is typesystem_schema.definitions["#/definitions/id"]



# Generated at 2022-06-14 14:35:19.113949
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    field = IfThenElse(
        if_clause=Field(const=0),
        then_clause=Field(const=1),
        else_clause=Field(const=2),
    )
    field_json_schema = field.json()
    # print(json.dumps(field_json_schema, sort_keys=True, indent=2))
    field_from_json_schema = if_then_else_from_json_schema(field_json_schema, {})
    assert field == field_from_json_schema


# Unit tests for function type_from_json_schema

# Generated at 2022-06-14 14:35:22.161047
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {"$ref": "#/definitions/foo"}
    ref = ref_from_json_schema(data, definitions={f"#/definitions/foo": String()})
    assert isinstance(ref, Reference)
    assert ref.to == data["$ref"]


# Generated at 2022-06-14 14:35:29.520280
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    m = if_then_else_from_json_schema({'if': {'type': 'string'}, 'then': {'type': 'boolean'}, 'else': {'type': 'integer'}, 'default': None}, None)
    assert isinstance(m, IfThenElse)
    assert isinstance(m.if_clause, Object)
    assert isinstance(m.then_clause, Boolean)
    assert isinstance(m.else_clause, Integer)
    assert m.default is None

# Generated at 2022-06-14 14:35:31.685442
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema({"allOf": [{"type": "integer"}, {"maximum": 2}]}, None)



# Generated at 2022-06-14 14:35:39.217700
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    field = enum_from_json_schema(data={"enum": ["a", 1, True, {}]})
    assert field.validate("a") is None
    assert field.validate(1) is None
    assert field.validate(True) is None
    assert field.validate({}) is None
    assert not field.validate("b")
    assert not field.validate(False)
    assert not field.validate(None)
    assert not field.validate([])
    assert not field.validate(0)
test_enum_from_json_schema()


# Generated at 2022-06-14 14:35:43.638620
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    schema = Schema(properties={"foo": None})
    assert definitions["#/properties/foo"] is None
    definitions["my_ref"] = schema
    assert definitions["my_ref"] is schema
    field = ref_from_json_schema({"$ref": "my_ref"}, definitions=definitions)
    assert isinstance(field, Reference)
    assert field.to == "my_ref"
    assert field.definitions is definitions



# Generated at 2022-06-14 14:35:51.053701
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    # Given a JSON schema object
    data = {
        "if": {"type": "boolean", "const": True},
        "then": {"type": "number"},
    }

    # When I create a field from the JSON schema object
    field = if_then_else_from_json_schema(data, SchemaDefinitions())

    # Then I should get a IfThenElseField
    assert isinstance(field, IfThenElse)



# Generated at 2022-06-14 14:35:53.744345
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    assert ref_from_json_schema({"$ref": "#/definitions/foo"}) == Reference("#/definitions/foo")

# Generated at 2022-06-14 14:35:55.611150
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {
        "$ref": "#/definitions/my_reference"
    }
    field = ref_from_json_schema(data, definitions={})
    assert field.to == data["$ref"]
    assert field.definitions == {}

# Generated at 2022-06-14 14:36:36.390451
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    field = Field()
    assert field.validate(1) == 1
    assert field.validate(0) == 0
    assert field.validate(-1) == -1
    assert field.validate(1.0) == 1
    assert field.validate(0.0) == 0
    assert field.validate(-1.0) == -1
    assert field.validate('1') == '1'
    assert field.validate('0') == '0'
    assert field.validate('-1') == '-1'
    assert field.validate([]) == []
    assert field.validate({}) == {}


# Generated at 2022-06-14 14:36:44.773156
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": "integer", "maximum": 10, "enum": [1, 3, 5]}) == Integer(
        maximum=10, enum=[1, 3, 5]
    )
    assert from_json_schema(
        {
            "type": "object",
            "required": ["a", "b"],
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "string"},
                "c": {"type": "null"},
            },
        }
    ) == Object(
        properties={
            "a": Integer(),
            "b": String(),
            "c": Any(),
        },
        required=["a", "b"],
    )



# Generated at 2022-06-14 14:36:54.579168
# Unit test for function one_of_from_json_schema

# Generated at 2022-06-14 14:37:00.761910
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    schema = {
    "anyOf": [
        {
            "type": "number"
        },
        {
            "type": "string",
            "enum": ["red", "amber", "green"]
        }
    ]
}
    def validate(data):
        field = any_of_from_json_schema(schema, None)
        return field.validate(data)

    assert validate('red') == True
    assert validate('reds') == False



# Generated at 2022-06-14 14:37:06.765555
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    schemas = {
        "color": {"type": "string"},
        "foreground": {"$ref": f"#/schemas/color"},
        "schema": {"$ref": f"#/schemas/color"},
    }

    definitions = SchemaDefinitions()
    for key, value in schemas.items():
        ref = f"#/schemas/{key}"
        definitions[ref] = from_json_schema(value, definitions=definitions)

    assert ref_from_json_schema({"$ref": f"#/schemas/color"}, definitions=definitions) == definitions[f"#/schemas/color"]



# Generated at 2022-06-14 14:37:08.268555
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(None) == {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": ["null", "object"],
    }



# Generated at 2022-06-14 14:37:18.054192
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    document = {
        "type": "object",
        "properties": {
            "prop": {"$ref": "#/definitions/String"},
        },
        "definitions": {
            "String": {
                "type": "string",
                "format": "date-time",
            },
        },
    }
    typesystem = from_json_schema(document)
    assert isinstance(typesystem, Schema)
    assert isinstance(typesystem.properties["prop"], Reference)
    assert typesystem.properties["prop"].to == "#/definitions/String"
    assert isinstance(definitions["#/definitions/String"], String)



# Generated at 2022-06-14 14:37:29.753807
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem.json_schema import JSONSchema
    from typesystem import types

    schema = JSONSchema("schema.json")
    field = from_json_schema(schema.get_schema(ref="/definitions/Usage"))
    assert isinstance(field, types.Choice)
    assert len(field.fields) == 6
    assert isinstance(field.fields[0], types.Object)
    assert len(field.fields[0].config.properties) == 2
    assert field.fields[0].config.properties["type"].default == "metered"
    assert isinstance(field.fields[1], types.Object)
    assert len(field.fields[1].config.properties) == 2
    assert field.fields[1].config.properties["type"].default == "flat"

# Generated at 2022-06-14 14:37:31.378705
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    assert any_of_from_json_schema({
        "default": None,
        "anyOf": [
            {"const": True},
            {"enum": [False, True]}
        ]
    }).validate(True)



# Generated at 2022-06-14 14:37:42.028679
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "$schema": "http://json-schema.org/draft/2019-09/schema#",
        "$id": "https://example.com/person.schema.json",
        "title": "Person",
        "type": "object",
        "properties": {
            "age": {
                "description": "Age in years which must be equal to or greater than zero.",
                "type": "integer",
                "minimum": 0,
            }
        },
    }

    schema = from_json_schema(data)

    schema({'age': 0})



# Generated at 2022-06-14 14:38:16.188081
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    def test():
        json_schema_data = {
            "oneOf": [
                {"const": "const"},
                {"type": "string", "format": "ipv4", "minLength": 7},
                {"type": "string", "format": "cidr"},
            ]
        }
        one_of = [from_json_schema(item, definitions=definitions) for item in json_schema_data["oneOf"]]
        kwargs = {"one_of": one_of, "default": json_schema_data.get("default", NO_DEFAULT)}
        return OneOf(**kwargs)
    x = test()
    assert x.one_of[0].validate('const') == {'valid': True, 'errors': []}
    assert x.one_of[1].validate

# Generated at 2022-06-14 14:38:21.310401
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {"oneOf": [{"type": "integer"}, {"type": "string"}]}
    '''
    TODO:
    # oneOf tests should raise errors
    data = {"oneOf": [{"type": "string"}]}
    data = {"oneOf": [{"type": "integer"}, {"type": "integer"}]}
    '''
    definitions = SchemaDefinitions()
    obj = one_of_from_json_schema(data, definitions=definitions)
    assert isinstance(obj, OneOf)
    assert obj.default == NO_DEFAULT



# Generated at 2022-06-14 14:38:25.948548
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "enum": [
            "open",
            "closed"
          ]
        }
      ]
    }
    definitions = SchemaDefinitions()
    result = any_of_from_json_schema(data, definitions)
    assert isinstance(result, Union)



# Generated at 2022-06-14 14:38:37.055033
# Unit test for function to_json_schema
def test_to_json_schema():
    data = to_json_schema(Validator.parse_object({"bar": Validator.parse_string()}))
    assert data == {
        "type": "object",
        "properties": {"bar": {"type": "string", "default": NO_DEFAULT}},
        "required": ["bar"],
    }

    data = to_json_schema(
        Validator.parse_object({"bar": Validator.parse_string(format="email")})
    )
    assert data == {
        "type": "object",
        "properties": {"bar": {"type": "string", "format": "email", "default": NO_DEFAULT}},
        "required": ["bar"],
    }

    data = to_json_schema(Validator.parse_array(Validator.parse_string()))
    assert data

# Generated at 2022-06-14 14:38:44.529865
# Unit test for function to_json_schema
def test_to_json_schema():  # noqa: D103
    class MySchema(Schema):
        a = Boolean()
        b = Integer()
        c = Object(
            additional_properties=Boolean(),
            default={"x": True, "y": False},
        )

    schema = MySchema()
    data_as_dict = to_json_schema(schema)

# Generated at 2022-06-14 14:38:49.889074
# Unit test for function any_of_from_json_schema

# Generated at 2022-06-14 14:39:00.016444
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from typesystem import Union, Any, Boolean, Integer, Float, Const

    # Number
    assert from_json_schema_type({"type": "number"}, type_string="number", allow_null=False) == Float()
    assert from_json_schema_type({"type": "number"}, type_string="number", allow_null=True) == Union(
        const=Float(), allow_null=True
    )

    # Integer
    assert from_json_schema_type({"type": "integer"}, type_string="integer", allow_null=False) == Integer()
    assert from_json_schema_type({"type": "integer"}, type_string="integer", allow_null=True) == Union(
        const=Integer(), allow_null=True
    )

    # String
    assert from_json_schema_type

# Generated at 2022-06-14 14:39:12.492998
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    for schema in (
        {"type": "number"},
        {"type": "integer"},
        {"type": "string"},
        {"type": "boolean"},
        {"type": "array"},
        {"type": "object"},
    ):
        field = from_json_schema_type(schema, "number", False, definitions={})
        assert isinstance(field, Number)

        field = from_json_schema_type(schema, "integer", False, definitions={})
        assert isinstance(field, Integer)

        field = from_json_schema_type(schema, "string", False, definitions={})
        assert isinstance(field, String)

        field = from_json_schema_type(schema, "boolean", False, definitions={})
        assert isinstance(field, Boolean)


# Generated at 2022-06-14 14:39:24.140666
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {"oneOf": [
         {
            "$ref": "https://example.com/foo.json#/definitions/pre"
         },
         {
            "required": [ "password" ],
            "$ref": "https://example.com/foo.json#/definitions/user"
         }
    ]}
    field = one_of_from_json_schema(data, definitions)
    assert field.to_primitive() == {
        "oneOf": [
            {"$ref": "https://example.com/foo.json#/definitions/pre"},
            {
                "required": ["password"],
                "$ref": "https://example.com/foo.json#/definitions/user",
            },
        ]
    }

# Generated at 2022-06-14 14:39:29.197938
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    schema = { "anyOf" : [{"type" : "integer"}, {"type" : "number"}]}
    assert isinstance(any_of_from_json_schema(schema), Union)



# Generated at 2022-06-14 14:39:56.977294
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(False).is_valid(None) is False



# Generated at 2022-06-14 14:40:06.506126
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "not": {
            "type": "object",
            "properties": {
                "foo": {"type": "string"},
                "bar": {"type": "number", "multipleOf": 3},
            },
        },
    }
    cases = {
        "null": {"": True, "foo": True, "bar": True, None: True},
        "boolean": {True: True},
        "array": {[]: True, [0]: True, [1, 2]: True, [3.14]: True},
        "object": {{"foo": "a"}: True, {"bar": 2}: True},
    }
    field = not_from_json_schema(data, definitions=None)
   

# Generated at 2022-06-14 14:40:11.130467
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    assert not_from_json_schema(
        {"not": {"type": "object", "properties": {"a": {"type": "string"}}}}
    ) == Not(negated=Object(properties={"a": String(allow_blank=True)}), default=NO_DEFAULT)



# Generated at 2022-06-14 14:40:16.125317
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    type_strings = {
        "null",
        "string",
        "integer",
        "number",
        "boolean",
        "object",
        "array",
    }
    for type_string in type_strings:
        assert from_json_schema_type(
            data={}, type_string=type_string, allow_null=False, definitions=None
        ).type == type_string



# Generated at 2022-06-14 14:40:28.543044
# Unit test for function from_json_schema
def test_from_json_schema():
    assert isinstance(from_json_schema(True), Any)
    assert isinstance(from_json_schema(False), NeverMatch)

    data = {"type": "integer"}
    assert isinstance(from_json_schema(data), Integer)

    data = {"type": "string"}
    assert isinstance(from_json_schema(data), String)

    data = {"type": "number"}
    assert isinstance(from_json_schema(data), Number)

    data = {"type": "object"}
    assert isinstance(from_json_schema(data), Object)

    data = {"type": "array"}
    assert isinstance(from_json_schema(data), Array)

    data = {"maximum": 1.0}
    assert isinstance(from_json_schema(data), Number)

   

# Generated at 2022-06-14 14:40:36.898042
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    schema = {
        "type": "object",
        "properties": {
            "a": {"const": "foo"},
            "b": {
                "if": {"required": ["a"]},
                "then": {"const": "bar"},
                "else": {"const": "baz"},
            },
        },
    }
    field = from_json_schema(schema)
    assert field.__validate__({"a": "foo"}) == {"a": "foo", "b": "bar"}
    assert field.__validate__({"a": "foo", "b": "bar"}) == {"a": "foo", "b": "bar"}
    assert field.__validate__({"a": "foo", "b": "baz"}) == {"a": "foo", "b": "baz"}
   

# Generated at 2022-06-14 14:40:48.193097
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem import from_json_schema


# Generated at 2022-06-14 14:41:00.271006
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert JSONSchema.validate(
        json.loads('{"if": {"type": "number"}, "then": {"type": "string"}}')
    )
    assert JSONSchema.validate(
        json.loads('{"if": {"type": "number"}, "else": {"type": "string"}}')
    )
    assert JSONSchema.validate(
        json.loads('{"if": {"type": "number"}, "then": {"type": "string"}, "else": {"type": "string"}}')
    )
    assert not JSONSchema.validate(
        json.loads('{"if": {"type": "number"}, "then": {"type": "string"}, "else": {"type": "number"}}')
    )

# Generated at 2022-06-14 14:41:08.409178
# Unit test for function from_json_schema
def test_from_json_schema():
    assert isinstance(from_json_schema(True), Field)
    assert isinstance(from_json_schema(False), Field)
    assert isinstance(from_json_schema(None), Field)
    assert isinstance(from_json_schema(1), Field)
    assert isinstance(from_json_schema(1.0), Field)
    assert isinstance(from_json_schema("1"), Field)
    assert isinstance(from_json_schema([]), Field)
    assert isinstance(from_json_schema({}), Field)



# Generated at 2022-06-14 14:41:15.839984
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    config = {'if': {'type': 'integer'}, 'then': {'type': 'integer'}, 'else': {'type': 'string'}}
    myfield = if_then_else_from_json_schema(config, None)
    config_pass = {'if': 1, 'then': 2, 'else': '1'}
    config_fail = {'if': 'a', 'then': 1, 'else': 'b'}
    assert myfield.validate(config_pass) == []
    assert myfield.validate(config_fail) != []

definitions["JSONSchema"] = JSONSchema

if __name__ == "__main__":
    import sys

    with open(sys.argv[1], "r") as f:
        data = json.load(f)


# Generated at 2022-06-14 14:41:44.614588
# Unit test for function to_json_schema
def test_to_json_schema():
    field1 = String()
    field2 = String()
    data = to_json_schema(Object(properties={"field1": field1, "field2": field2}))
    assert data == {"properties": {"field1": {"type": "string"}, "field2": {"type": "string"}}, "type": "object"}



# Generated at 2022-06-14 14:41:56.690360
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem.tests.test_case import ValidationTestCase, TypeSystemTestCase

    class TestCase(ValidationTestCase):
        def test_from_json_schema_works_with_empty_params(self):
            field = from_json_schema({})
            self.assertIsInstance(field, Any)

        def test_from_json_schema_requires_a_json_schema_valid_definition(self):
            with self.assertRaises(ValidationError):
                from_json_schema(None)
            with self.assertRaises(ValidationError):
                from_json_schema(True)
            with self.assertRaises(ValidationError):
                from_json_schema(123)

# Generated at 2022-06-14 14:42:06.574123
# Unit test for function to_json_schema
def test_to_json_schema():
    class Foo(Schema):
        bar: str

    assert to_json_schema(Foo) == {
        "type": "object",
        "properties": {"bar": {"type": "string"}},
        "required": ["bar"],
    }

    class Foo(Schema):
        bar: Union[str, Integer]

    assert to_json_schema(Foo) == {
        "type": "object",
        "properties": {"bar": {"anyOf": [{"type": "string"}, {"type": "integer"}]}},
        "required": ["bar"],
    }

    class Foo(Schema):
        bar: Union[str, Integer, Float]


# Generated at 2022-06-14 14:42:12.762117
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = {
        "oneOf": [{"type": "boolean"}, {"type": "null"}],
        "not": {"type": "integer"},
    }
    f = from_json_schema(schema)
    assert not f.validate(1)
    assert f.validate(True)
    # Test inline the call to OneOf()
    assert not f.validate(None)
    assert not f.validate(None)



# Generated at 2022-06-14 14:42:16.684076
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = {
        "not": {
            "type": "string"
        }
    }
    field = not_from_json_schema(schema,{})
    assert isinstance(field, Not)



# Generated at 2022-06-14 14:42:25.515811
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type(data={}, type_string="string", allow_null=False, definitions=None), String)
    assert isinstance(from_json_schema_type(data={}, type_string="number", allow_null=False, definitions=None), Float)
    assert isinstance(from_json_schema_type(data={}, type_string="integer", allow_null=False, definitions=None), Integer)
    assert isinstance(from_json_schema_type(data={}, type_string="boolean", allow_null=False, definitions=None), Boolean)
    assert isinstance(from_json_schema_type(data={}, type_string="array", allow_null=False, definitions=None), Array)

# Generated at 2022-06-14 14:42:35.096200
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, "number", False, None) is Float
    assert from_json_schema_type({}, "integer", False, None) is Integer
    assert from_json_schema_type({}, "string", False, None) is String
    assert from_json_schema_type({}, "boolean", False, None) is Boolean
    assert from_json_schema_type({}, "array", False, None) is Array
    assert from_json_schema_type({}, "object", False, None) is Object



# Generated at 2022-06-14 14:42:42.925458
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({"type": "number"}, type_string="number", allow_null=False) == Float()
    assert from_json_schema_type({"type": "integer"}, type_string="integer", allow_null=False) == Integer()
    assert from_json_schema_type({"type": "string"}, type_string="string", allow_null=False) == String()
    assert from_json_schema_type({"type": "boolean"}, type_string="boolean", allow_null=False) == Boolean()
    assert from_json_schema_type({"type": "array"}, type_string="array", allow_null=False) == Array()
    assert from_json_schema_type({"type": "object"}, type_string="object", allow_null=False) == Object()

# Generated at 2022-06-14 14:42:46.511777
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    testdata = {'not': {'properties': {'a': {'type': 'integer'}}}}
    # print(not_from_json_schema(testdata))


# Generated at 2022-06-14 14:42:53.099084
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    for type_string, field_class in [
        ("string", String),
        ("integer", Integer),
        ("number", Float),
        ("boolean", Boolean),
        ("array", Array),
        ("object", Object),
    ]:
        schema = {"type": type_string}
        assert isinstance(from_json_schema(schema), field_class)
        assert not isinstance(from_json_schema(schema), Union)



# Generated at 2022-06-14 14:43:38.092729
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False


if typing.TYPE_CHECKING:
    # Unit test for type annotations
    def test_type_annotations():
        String(allow_null=False)
        String(allow_null=True)
        String(allow_null=True, min_length=4)
        String(allow_null=True, max_length=4)
        String(allow_null=True, pattern=r'^\d*\.\d*$')
        String(allow_null=True, format='date')

        Integer(allow_null=False)
        Integer(allow_null=True)
        Integer(allow_null=True, minimum=0)
        Integer(allow_null=True, maximum=10)

# Generated at 2022-06-14 14:43:42.495029
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    import pytest

    with pytest.raises(AssertionError) as e:
        from_json_schema_type(data={}, type_string="", allow_null=False, definitions={})
    assert e.value.args[0] == "Invalid argument type_string=''"



# Generated at 2022-06-14 14:43:45.938025
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "if": {
            "type": "null",
        },
        "then": {
            "type": "string"
        },
        "else": {
            "type": "integer"
        }
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions=definitions)
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Not)
    assert isinstance(result.if_clause.negated, Const)
    assert result.if_clause.negated.const is None



# Generated at 2022-06-14 14:43:52.890468
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type({}, "number", False, None), Float)
    assert isinstance(from_json_schema_type({}, "integer", False, None), Integer)
    assert isinstance(from_json_schema_type({}, "string", False, None), String)
    assert isinstance(from_json_schema_type({}, "boolean", False, None), Boolean)
    assert isinstance(from_json_schema_type({}, "array", False, None), Array)
    assert isinstance(from_json_schema_type({}, "object", False, None), Object)



# Generated at 2022-06-14 14:44:02.396344
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    def assert_type(field, types):
        if isinstance(field, Union):
            field = field.any_of[0]
        assert field.get_type() in types

    assert_type(from_json_schema({"type": "boolean"}), ["boolean"])
    assert_type(from_json_schema({"type": "boolean", "nullable": False}), ["boolean"])
    assert_type(from_json_schema({"type": "boolean", "nullable": True}), ["boolean"])

    assert_type(from_json_schema({"type": "object"}), ["object"])
    assert_type(from_json_schema({"type": "object", "nullable": False}), ["object"])

# Generated at 2022-06-14 14:44:06.953512
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    default_schema = {"default": "default-value"}
    def f(schema):
        return from_json_schema(schema, definitions=None)

    # if then
    schema = {
        "if": {"const": "val"},
        "then": {"const": "val"},
        **default_schema
    }
    assert f(schema).validate("val") == "val"
    assert f(schema).validate("other") == "default-value"

    # if not then
    schema = {
        "if": {"not": {"const": "val"}},
        "then": {"const": "val"},
        **default_schema
    }
    assert f(schema).validate("val") == "default-value"

# Generated at 2022-06-14 14:44:13.860303
# Unit test for function to_json_schema
def test_to_json_schema():
    def test_schemas(schema: Field, expected_json: typing.Union[bool, dict]):
        assert to_json_schema(schema) == expected_json
        # Round-trip the schema through JSON schema and back to a validator.
        result = from_json_schema(expected_json)
        assert result == schema
        # Round-trip the schema through JSON and back to a validator.
        string = json.dumps(expected_json)
        result = from_json_schema(json.loads(string))
        assert result == schema

    # Any
    test_schemas(Any(), True)
    test_schemas(Any(allow_null=True), ["null", True])
    test_schemas(Any(default=123), {"default": 123})

    # NeverMatch
    test