

# Generated at 2022-06-14 14:35:51.055972
# Unit test for function to_json_schema
def test_to_json_schema():
    # See https://tools.ietf.org/html/draft-wright-json-schema-validation-01
    from .test_validator import test_field, test_schema

    for cls in test_field:
        data = to_json_schema(cls())
        assert data
    for cls in test_schema:
        data = to_json_schema(cls())
        assert data
    assert True

# Generated at 2022-06-14 14:35:55.581017
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    foo: Field = enum_from_json_schema(data={"enum": ["foo", "bar"], "default": "foo"}, definitions=None)
    assert foo.validate("foo")
    assert foo.validate("bar")
    assert not foo.validate(None)
    assert not foo.validate(42)
    assert foo.default == "foo"

    bar = enum_from_json_schema(data={"enum": ["foo", "bar"], "default": "foo"}, definitions=None)
    assert bar.validate("foo")
    assert bar.validate("bar")
    assert not bar.validate(None)
    assert not bar.validate(42)
    assert bar.default == "foo"



# Generated at 2022-06-14 14:36:03.217927
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    class Defs(SchemaDefinitions):
        pass

    definitions = Defs()
    definitions["#/definitions/foo"] = String()

    data = {
        "$ref": "#/definitions/foo",
    }
    field = ref_from_json_schema(data, definitions=definitions)
    assert field.validate("foo") == "foo"
    assert field.validate("bar") == "bar"
    assert field.validate("quux") == "quux"



# Generated at 2022-06-14 14:36:06.632593
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    with_string = {"type": "string"}
    assert_field(from_json_schema_type(with_string, type_string="string", allow_null=False), String)


# Generated at 2022-06-14 14:36:09.837988
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    any_of_schema = {
        "anyOf": [
            {"type": "number"},
            {"type": "string", "minLength": 3},
        ]
    }
    assert isinstance(any_of_from_json_schema(any_of_schema, None), Union)


# Generated at 2022-06-14 14:36:18.789048
# Unit test for function get_valid_types
def test_get_valid_types():
    assert get_valid_types({}) == ({'null', 'boolean', 'object', 'array', 'number', 'string'}, True)
    assert get_valid_types({'type': 'boolean'}) == ({'boolean'}, False)
    assert get_valid_types({'type': 'string'}) == ({'string'}, False)
    assert get_valid_types({'type': 'null'}) == ({'null'}, True)
    assert get_valid_types({'type': 'null', 'enum': ['foo']}) == ({'null'}, True)
    assert get_valid_types({'type': 'boolean', 'enum': ['foo']}) == ({'boolean'}, False)
    assert get_valid_types({'type': 'number', 'enum': ['foo']}) == ({'number'}, False)

# Generated at 2022-06-14 14:36:23.637711
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    assert any_of_from_json_schema({'anyOf': [{'type': 'integer'}, {'type': 'string'}]}, None) \
        == Union(any_of=[Integer(), String()])



# Generated at 2022-06-14 14:36:27.195459
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    choices = {"a":1, "b": 2}
    data = {"anyOf": choices}
    assert any_of_from_json_schema(data = data, definitions = {}) == Union(choices = choices)



# Generated at 2022-06-14 14:36:30.586671
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    field = enum_from_json_schema({"enum": ["red", "green", "blue"]})
    assert field.validate("red") == "red"
    assert not field.validate("yellow")


# Generated at 2022-06-14 14:36:35.359846
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    result = const_from_json_schema({
        "$ref": "#/definitions/value",
        "const": 8,
        "default": 5,
        "description": "This is a constant value."
    }, definitions=definitions)
    assert result.validate(8)
    assert result.validate(5)
    assert not result.validate(4)



# Generated at 2022-06-14 14:38:26.102943
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    example = {
        "if": {"type": "integer"},
        "then": {"const": 1},
        "else": {"const": 2},
    }
    assert if_then_else_from_json_schema(example, definitions={}) == IfThenElse(
        If(Integer()), Const(1), Const(2)
    )

# Generated at 2022-06-14 14:38:32.401536
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {
        "$ref": "#/definitions/name",
    }
    definitions = SchemaDefinitions()
    definitions["#/definitions/name"] = String()
    field = ref_from_json_schema(data, definitions=definitions)
    assert field.validate("Bob") is None
    assert field.validate("1234") != None
    

# Generated at 2022-06-14 14:38:37.435727
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {'oneOf': [{'$ref':'#/definitions/String'}, {'$ref':'#/definitions/URL'}]}
    result = one_of_from_json_schema(data, definitions)
    assert (result.obj_name == 'OneOf')
    # Result should have the same type as from_json_schema
    assert isinstance(result, Schema)



# Generated at 2022-06-14 14:38:44.754749
# Unit test for function if_then_else_from_json_schema

# Generated at 2022-06-14 14:38:47.503871
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    print("\nUnit test for function 'all_of_from_json_schema'")
    field = all_of_from_json_schema({"allOf": [String(), Integer()]}, definitions=None)
    assert isinstance(field, AllOf), "Fail"
    print("Pass")
test_all_of_from_json_schema()


# Generated at 2022-06-14 14:38:51.608767
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    """Test if_then_else_from_json_schema function."""
    schema_json = {
        'if': {'type': 'number'},
        'then': {'type': 'string'},
        'else': {'type': 'integer'}
    }
    expected = IfThenElse(
            if_clause=Number(allow_null=False),
            then_clause=String(allow_null=False),
            else_clause=Integer(allow_null=False)
    )
    actual = if_then_else_from_json_schema(schema_json, SchemaDefinitions())
    assert actual == expected

# Generated at 2022-06-14 14:38:57.963092
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    test_data = {
        "not":{
            "type":"string",
            "enum": ["red", "amber", "green"]
        }
    }
    definitions = SchemaDefinitions()
    actual = not_from_json_schema(test_data, definitions)
    expected = Not(negated = Choice(choices=[("red", "red"), ("amber", "amber"), ("green", "green")]))
    assert actual == expected

# Generated at 2022-06-14 14:39:06.269895
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
  assert IfThenElse(if_clause=Any(),then_clause=Any()) == if_then_else_from_json_schema({
    "if": {},
    "then": {}
  })
  assert IfThenElse(if_clause=Any(),then_clause=Any(),else_clause=Any()) == if_then_else_from_json_schema({
    "if": {},
    "then": {},
    "else": {}
  })

definitions.update(get_referenced_definitions())

# Generated at 2022-06-14 14:39:10.987830
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    from .examples.json_schema import schema_float

    schema = schema_float({"type":"float", "maximum": 5.0})
    for _, field in schema.fields.items():
        if (isinstance(field, Not)):
            assert field.negated.maximum == 5.0




# Generated at 2022-06-14 14:39:23.448860
# Unit test for function from_json_schema
def test_from_json_schema():
    field = from_json_schema(
        {
            "$ref": "#/definitions/foo",
            "enum": [1, "two", 3, "four"],
            "definitions": {
                "foo": {
                    "type": "string",
                    "maxLength": 10,
                    "pattern": "a*",
                    "enum": ["bar"],
                },
                "bar": {"const": "bar"},
            },
        }
    )
    assert field.validate(data="foo")
    assert not field.validate(data="bar")
    assert field.validate(data="aaaaaaaaaa")
    assert not field.validate(data="aaaaaaaaaaa")
    assert field.validate(data="bar")
    assert not field.validate(data="baz")

# Generated at 2022-06-14 14:40:16.165754
# Unit test for function all_of_from_json_schema

# Generated at 2022-06-14 14:40:25.163335
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {'allOf': [
        {
            'const': 1,
            'type': 'integer'
        },
        {
            'const': 2,
            'type': 'integer'
        }
    ]}
    definitions = SchemaDefinitions()
    expected = AllOf(all_of=[Const(const=1), Const(const=2)])
    expected.type_check(2)

    assert from_json_schema(data, definitions=definitions) == expected



# Generated at 2022-06-14 14:40:29.990580
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    expected = [
        data,
        kwargs,
        instance,
        definitions,
        any_of,
        OneOf,
        item,
        from_json_schema
    ]
    schema = {
        "oneOf": [{"type": "string"}, {"maximum": 1}]
    }
    actual = one_of_from_json_schema(schema, definitions)
    assert actual.one_of[0].type == "String"
    assert isinstance(actual.one_of[1], Integer)
    assert actual.one_of[1].maximum == 1



# Generated at 2022-06-14 14:40:37.698059
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    json_schema_object={"$ref":"#/definition/Integer"}
    typesystem_field=ref_from_json_schema(json_schema_object, {})
    # string_representations_of_typesystem_field=str(typesystem_field)
    # assert string_representations_of_typesystem_field==f"Ref(to='')"
    assert str(typesystem_field)== f"Ref(to='#/definition/Integer')"
component_name="ref_from_json_schema"

# Generated at 2022-06-14 14:40:40.616547
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema({"allOf": [{"type": "string"}]}) == String()



# Generated at 2022-06-14 14:40:51.029163
# Unit test for function to_json_schema
def test_to_json_schema():
    class User(SchemaDefinitions):
        name = String(max_length=32)
        address = Object(
            properties={
                "street_address": String(max_length=64),
                "city": String(max_length=64),
            }
        )
        order = Array(
            items=Object(
                properties={
                    "title": String(max_length=64),
                    "quantity": Integer(),
                }
            )
        )
    schema = User()
    data = to_json_schema(schema)
    print("json schema:", data)

# Generated at 2022-06-14 14:41:00.006073
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    data = {
        "anyOf": [
            {"type": "number"},
            {"type": "string"},
            {"type": "boolean"},
            {
                "type": "object",
                "properties": {
                    "key1": {"type": "string"},
                    "key2": {"type": "integer"},
                },
                "additionalProperties": {"type": "number"},
            },
        ]
    }
    expected = Any()
    actual = from_json_schema(data)
    assert actual == expected, actual



# Generated at 2022-06-14 14:41:10.554804
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    schema = {
        "type": "object",
        "properties": {
            "a": {"type": "string", "minLength": 3},
            "b": {"type": "string", "minLength": 1},
        },
        "required": ["a", "b"],
        "allOf": [
            {"properties": {"a": {"minLength": 1}}},
            {"properties": {"b": {"minLength": 3}}},
        ],
    }
    typesystem_field = from_json_schema(schema)

# Generated at 2022-06-14 14:41:20.468704
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    from .test_fixtures.json_schema import TYPE_FIXTURES

    for data in TYPE_FIXTURES:
        schema = from_json_schema(data["json_schema"])

        for field_name in TYPE_FIXTURES[data]:
            field = getattr(schema, field_name, None)
            if field is None:
                continue

            with_valid_value = data["json_schema"].copy()
            with_valid_value[field_name] = field.valid_value
            with_valid_value["type"] = data["type"]

            with_invalid_value = data["json_schema"].copy()
            with_invalid_value[field_name] = field.invalid_value
            with_invalid_value["type"] = data["type"]


# Generated at 2022-06-14 14:41:26.548408
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    assert one_of_from_json_schema(data={'$ref': '#/definitions/person', 'oneOf': [{'$ref': '#/definitions/person'}, {'$ref': '#/definitions/company'}], 'default':{}}, definitions={'#/definitions/person': {'type': 'object', 'properties': {'first_name': {'type': 'string'}, 'last_name': {'type': 'string'}}}}) == OneOf(one_of=[Reference(to='#/definitions/person', definitions={'#/definitions/person': {'type': 'object', 'properties': {'first_name': {'type': 'string'}, 'last_name': {'type': 'string'}}}})], default={})
    assert one_of_from_json_

# Generated at 2022-06-14 14:42:40.072621
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type(data={"type": "number"}, type_string="number", allow_null=False, definitions=None) == Float()
    assert from_json_schema_type(data={"type": "integer"}, type_string="integer", allow_null=False, definitions=None) == Integer()
    assert from_json_schema_type(data={"type": "string"}, type_string="string", allow_null=False, definitions=None) == String()
    assert from_json_schema_type(data={"type": "boolean"}, type_string="boolean", allow_null=False, definitions=None) == Boolean()
    assert from_json_schema_type(data={"type": "array"}, type_string="array", allow_null=False, definitions=None) == Array()

# Generated at 2022-06-14 14:42:52.207521
# Unit test for function to_json_schema
def test_to_json_schema():
    from . import make_validator

    class NewPerson(Schema):
        name = String()
        age = Integer()
        email = String()
        contact_number = String()


# Generated at 2022-06-14 14:42:55.745004
# Unit test for function to_json_schema
def test_to_json_schema():
    # not implemented yet
    pass


# def to_python_validator(arg) -> typing.Optional[typing.Callable[[Any], Any]]:
#     if isinstance(arg, BaseField):
#         return arg.to_validator()
#     else:
#         return None



# Generated at 2022-06-14 14:43:06.249799
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    class Test:
        def __init__(self, **kwargs) -> None:
            for name, value in kwargs.items():
                setattr(self, name, value)
    data = {
        "type": "string",
        }
    assert type_from_json_schema(data, definitions=definitions) == String()
    data = {
        "type": ["string", "number"],
        }
    assert type_from_json_schema(data, definitions=definitions) == Union(any_of=[String(), Number()])
    data = {
        "type": "null",
        }
    assert type_from_json_schema(data, definitions=definitions) == Const(None)



# Generated at 2022-06-14 14:43:16.037759
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({}, definitions=SchemaDefinitions()) == Any()
    assert type_from_json_schema({}, definitions=SchemaDefinitions()) == Any()
    assert type_from_json_schema({"type": "string"}, definitions=SchemaDefinitions()) == String()
    assert type_from_json_schema({"type": "string"}, definitions=SchemaDefinitions()) == String()
    assert type_from_json_schema({"type": "boolean"}, definitions=SchemaDefinitions()) == Boolean()
    assert type_from_json_schema({"type": "number"}, definitions=SchemaDefinitions()) == Number()
    assert type_from_json_schema({"type": "integer"}, definitions=SchemaDefinitions()) == Integer()

# Generated at 2022-06-14 14:43:23.111980
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = schema_from_json_schema(ExampleSchema, "ExampleSchema")


# Generated at 2022-06-14 14:43:32.796074
# Unit test for function to_json_schema
def test_to_json_schema():
    # pylint: disable=too-many-locals,unused-variable

    schema = Integer(
        allow_null=False,
        minimum=System.now().timestamp,
        maximum=System.now_plus(days=1).timestamp,
        multiple_of=2,
        exclusive_minimum=True,
        exclusive_maximum=False,
        const=1337,
        default=5,
    )
    data = to_json_schema(schema)

# Generated at 2022-06-14 14:43:38.562704
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = {
        "definitions": {
            "john": {
                "type": "object",
                "properties": {
                    "first": {
                        "type": "string",
                        "default": "John",
                        "minLength": 1,
                        "maxLength": 100,
                    },
                    "last": {
                        "type": "string",
                        "default": "Smith",
                        "minLength": 1,
                        "maxLength": 100,
                    },
                },
            }
        },
        "$ref": "#/definitions/john",
    }
    assert to_json_schema(JohnSchema()) == schema



# Generated at 2022-06-14 14:43:47.506672
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    """
    Test 'type_from_json_schema' by supplying it with a JSON schema object
    that has a 'type' property, and asserting that the correct types match.
    """
    field = type_from_json_schema(
        {
            "type": "string",
            "minLength": 2,
            "maxLength": 2,
            "pattern": "^[A-Z]{2}$",
        },
        definitions={},
    )
    assert isinstance(field, String)
    assert field.minimum_length == 2
    assert field.maximum_length == 2
    assert field.pattern == re.compile("^[A-Z]{2}$")

# Generated at 2022-06-14 14:43:55.429190
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Integer(minimum=3)), {"minimum": 3, "type": "integer"}
    assert (
        to_json_schema(
            Integer(
                minimum=3,
                maximum=19,
                min_exclusive=5,
                max_exclusive=17,
                multiple_of=2,
            )
        )
        == {
            "type": "integer",
            "minimum": 3,
            "maximum": 19,
            "exclusiveMinimum": 5,
            "exclusiveMaximum": 17,
            "multipleOf": 2,
        }
    )
    assert to_json_schema(Float(minimum=3.5)), {"minimum": 3.5, "type": "number"}