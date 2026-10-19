

# Generated at 2022-06-14 14:35:22.814381
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({}) == Any()
    assert from_json_schema({'type': 'null'}) == Any()
    assert from_json_schema({'type': 'string'}) == String()
    assert from_json_schema({'type': 'integer'}) == Integer()
    assert from_json_schema({'type': 'any'}) == Any()
    assert from_json_schema({'type': 'number'}) == Number()
    assert from_json_schema({'type': 'boolean'}) == Boolean()
    assert from_json_schema({'type': 'array'}) == Array()
    assert from_json_schema({'type': 'object'}) == Object()


# Generated at 2022-06-14 14:35:27.870763
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    data = {
        "type": "string",
        "minLength": 2,
        "maxLength": 2,
        "pattern": "^(00|11)$",
    }
    field = type_from_json_schema(data, definitions)
    assert field.default == "00"



# Generated at 2022-06-14 14:35:37.976976
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False).is_valid(None) == False

    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "number"}) == Number()
    assert from_json_schema({"type": "integer"}) == Integer()

    assert from_json_schema({"type": "boolean"}) == Boolean()
    assert from_json_schema({"type": "boolean", "default": True}) == Boolean(default=True)

    assert from_json_schema({"type": "array", "items": {"type": "string"}}) == Array(items=String())

# Generated at 2022-06-14 14:35:45.423102
# Unit test for function get_valid_types
def test_get_valid_types():
    assert get_valid_types(data={"type": "number"}) == ({'number'}, False)
    assert get_valid_types(data={"type": "integer"}) == ({'integer'}, False)
    assert get_valid_types(data={"type": "string"}) == ({'string'}, False)
    assert get_valid_types(data={"type": "boolean"}) == ({'boolean'}, False)
    assert get_valid_types(data={"type": "object"}) == ({'object'}, False)
    assert get_valid_types(data={"type": "array"}) == ({'array'}, False)
    assert get_valid_types(data={"type": "null"}) == (set(), True)

# Generated at 2022-06-14 14:35:58.650565
# Unit test for function to_json_schema
def test_to_json_schema():
    from .schema_validator import SchemaValidator, ValidationError

    for nullable in [False, True]:
        field = String(allow_null=nullable, default="default", required=True)
        data = to_json_schema(field)
        validator = SchemaValidator(data)
        assert validator.validate("default")
        assert validator.validate(field.default)
        assert validator.validate(None if nullable else "null")
        assert set(validator.errors) == {[]}


# Generated at 2022-06-14 14:36:05.370462
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(
        from_json_schema_type({"type": "integer"}, "integer", False, None), Integer
    )
    assert isinstance(
        from_json_schema_type({"type": "integer"}, "integer", True, None), Integer
    )
    assert isinstance(
        from_json_schema_type({"type": ["null", "integer"]}, "null", False, None), Integer
    )



# Generated at 2022-06-14 14:36:10.088606
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema({'allOf': [{'type': 'string'}, {'type': 'integer'}]}, definitions=SchemaDefinitions()) == AllOf(all_of=[String(allow_null=False), Integer(allow_null=False)], default=NO_DEFAULT)
test_all_of_from_json_schema()



# Generated at 2022-06-14 14:36:17.116534
# Unit test for function get_valid_types
def test_get_valid_types():
    # Test with no type information
    assert get_valid_types(dict()) == (
        {"null", "boolean", "object", "array", "number", "string"},
        False,
    )
    # Test with only the null type
    assert get_valid_types({"type": "null"}) == (set(), True)
    # Test with a null type and another type
    assert get_valid_types({"type": ["null", "number"]}) == ({"number"}, True)
    # Test with a null type and a number type
    assert get_valid_types({"type": ["null", "integer"]}) == ({"number"}, True)



# Generated at 2022-06-14 14:36:26.915830
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "if": {"type": "integer"},
        "then": {"type": "string"},
        "else": {"type": "boolean"},
    }

    field = from_json_schema(data)
    assert field is not None
    assert field.validate(1) is None
    assert field.validate("a") is None
    assert field.validate(True) is None

    field = from_json_schema(data)
    assert field is not None
    assert field.validate("a") is None
    assert field.validate("a") is None
    assert field.validate("a") is None



# Generated at 2022-06-14 14:36:32.427444
# Unit test for function any_of_from_json_schema

# Generated at 2022-06-14 14:37:01.715691
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    # The following code should return a Union(any_of=[Number(), String()])
    schema = "https://schemas.typesystem.dev/tests/union-anyOf-number-string.schema.json"
    validator = typesystem.from_json_schema(schema)
    assert isinstance(validator, Union)
    assert validator.__repr__() == "Union(any_of=[Number(), String()])"


# Generated at 2022-06-14 14:37:06.189374
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {'oneOf': [{'$ref': '#/definitions/user_id'}, {'const': '$current_user'}]}
    definitions = {'user_id': Integer()}
    assert definitions["user_id"] == Generic() and data['oneOf'] == ['#/definitions/user_id', '$current_user']

# Generated at 2022-06-14 14:37:17.598790
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert enum_from_json_schema(data={"enum": [1, 2, 3]}) == Choice(choices=[(1, 1), (2, 2), (3, 3)])
    assert enum_from_json_schema(data={"enum": [1, 2, 3], "default": 1}) == Choice(choices=[(1, 1), (2, 2), (3, 3)], default=1)
    assert enum_from_json_schema(data={"enum": [1, 2, 3], "default": 2}) == Choice(choices=[(1, 1), (2, 2), (3, 3)], default=2)

# Generated at 2022-06-14 14:37:19.058504
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    assert const_from_json_schema(data={"const": "true"}) == Const(const="true")



# Generated at 2022-06-14 14:37:30.964751
# Unit test for function to_json_schema
def test_to_json_schema():
    integers = Integer()
    simple = to_json_schema(integers)
    assert simple == {"type": "integer"}

    integers_with_length_limit = Integer(minimum=0, maximum=255)
    length_limited = to_json_schema(integers_with_length_limit)
    assert length_limited == {
        "type": "integer",
        "minLength": 0,
        "maxLength": 255,
    }

    field_with_null = to_json_schema(Any())
    assert field_with_null == True

    field_with_not_null = to_json_schema(NeverMatch())
    assert field_with_not_null == False

    schema = to_json_schema(Schema(title="example", description="here it is!"))

# Generated at 2022-06-14 14:37:39.353549
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    schema = {'anyOf': [{'type': 'number'}, {'const': 'bar'}]}
    result = any_of_from_json_schema(schema, definitions=None)
    assert result.any_of[0] == Float(minimum=None, maximum=None, multiple_of=None, allow_null=False, default=NO_DEFAULT)
    assert result.any_of[1] == Const('bar')


# Generated at 2022-06-14 14:37:47.870152
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    test_data = {
        "anyOf": [{"type": "integer"}, {"type": "number"}],
        "default": 1.0
    }
    typ = any_of_from_json_schema(test_data, definitions)
    val = typ.validate(1)
    assert val == 1, f"Test_any_of_from_json_schema failed: {val} != 1"
    val = typ.validate(1.0)
    assert val == 1, f"Test_any_of_from_json_schema failed: {val} != 1"
    val = typ.validate(None)
    assert val == 1.0, f"Test_any_of_from_json_schema failed: {val} != 1.0"



# Generated at 2022-06-14 14:37:53.933586
# Unit test for function to_json_schema
def test_to_json_schema():
    # type: () -> None
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False
    assert to_json_schema(String(min_length=1)) == {"type": "string", "minLength": 1}
    assert to_json_schema(Integer(minimum=1)) == {"type": "integer", "minimum": 1}
    assert to_json_schema(Integer(minimum=1, allow_null=True)) == {
        "type": ["integer", "null"],
        "minimum": 1,
    }
    assert to_json_schema(Boolean(allow_null=True)) == {"type": ["boolean", "null"]}

# Generated at 2022-06-14 14:38:02.597828
# Unit test for function one_of_from_json_schema

# Generated at 2022-06-14 14:38:11.551578
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    # Arrange
    schema = {
        "anyOf": [
            {
                "properties" : {
                    "id" :  { "type" : "string" }
                },
                "required" : [ "id" ]
            },
            {
                "properties" : {
                    "id" :  { "type" : "string" },
                    "type" :  { "type" : "string" }
                },
                "required" : [ "id", "type" ]
            }
        ]
    }
    # Act
    schema_field = any_of_from_json_schema(schema,definitions)
    # Assert
    assert isinstance(schema_field,Union)
    assert isinstance(schema_field.any_of[0],Object)

# Generated at 2022-06-14 14:38:41.602577
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    data = {"enum": [0, 1]}
    assert enum_from_json_schema(data, definitions=SchemaDefinitions()) == Choice(
        [
            (0, 0),
            (1, 1),
        ]
    )



# Generated at 2022-06-14 14:38:43.285229
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    try:
        ref_from_json_schema({"$ref": "http://google.com"})
    except AssertionError:
        pass
    ref_from_json_schema({"$ref": "#/stuff"})



# Generated at 2022-06-14 14:38:48.333941
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    from copy import copy
    from typesystem.schema import Reference
    schema = {
        "$ref": "#/definitions/foo",
        "definitions": {"foo": {"type": "string"}},
    }
    field = ref_from_json_schema(schema, definitions=SchemaDefinitions())
    assert isinstance(field, Reference)
    assert field.to == "#/definitions/foo"
    assert field.definitions == SchemaDefinitions()
    assert copy(field).validate(None) is True
    assert copy(field).validate("a") is True
    assert copy(field).validate(1) is False


# Generated at 2022-06-14 14:38:53.491613
# Unit test for function from_json_schema
def test_from_json_schema():
    # $ref
    assert from_json_schema({"$ref": "#/definitions/JSONSchema"}) == Reference(
        "JSONSchema", definitions=definitions
    )
    # type: bool
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    # type: string
    assert from_json_schema({"type": "string"}) == String()

# Generated at 2022-06-14 14:38:58.558964
# Unit test for function from_json_schema

# Generated at 2022-06-14 14:39:09.074629
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    try:
        from_json_schema_type(data={}, allow_null=False, type_string="null", definitions=None)
        assert False  # pragma: no cover
    except AssertionError:
        pass

    try:
        from_json_schema_type(data={}, allow_null=True, type_string="null", definitions=None)
        assert False  # pragma: no cover
    except AssertionError:
        pass

    try:
        from_json_schema_type(data={}, allow_null=False, type_string="invalid", definitions=None)
        assert False  # pragma: no cover
    except AssertionError:
        pass


# Generated at 2022-06-14 14:39:21.439448
# Unit test for function to_json_schema
def test_to_json_schema():
    from py_jschema import validate_json
    from py_jschema.examples import load_person_schema

    person = load_person_schema()
    s = to_json_schema(person)
    assert validate_json(s, person)

    # Test with custom types
    import datetime

    class Datetime(Field):
        @classmethod
        def validate(cls, val, path=None):
            if not isinstance(val, datetime.datetime):
                raise ValidationError(f"{path}: Not a datetime: {val!r}")

    data = to_json_schema(Datetime)
    assert data == {"type": ["string", "null"], "format": "date-time"}

# Generated at 2022-06-14 14:39:29.092285
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(
        from_json_schema_type(
            data={"type": "number"},
            type_string="number",
            allow_null=False,
            definitions=SchemaDefinitions(),
        ),
        Float,
    )

    assert isinstance(
        from_json_schema_type(
            data={"type": "integer"},
            type_string="integer",
            allow_null=False,
            definitions=SchemaDefinitions(),
        ),
        Integer,
    )

    assert isinstance(
        from_json_schema_type(
            data={"type": "string"},
            type_string="string",
            allow_null=False,
            definitions=SchemaDefinitions(),
        ),
        String,
    )


# Generated at 2022-06-14 14:39:38.411932
# Unit test for function not_from_json_schema

# Generated at 2022-06-14 14:39:45.811116
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    json_schema = {
        "$ref": "#/definitions/foo",
    }
    definitions = SchemaDefinitions()
    definitions["#/definitions/foo"] = String()
    definition = ref_from_json_schema(json_schema, definitions=definitions)
    assert isinstance(definition, Reference)
    assert definition.to == "#/definitions/foo"



# Generated at 2022-06-14 14:40:21.286014
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    with pytest.raises(AssertionError):
        from_json_schema_type({"type": "foo"}, "foo", False, None)



# Generated at 2022-06-14 14:40:32.217067
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data_1 = {
                'not': {
                    'type': 'string',
                    'not': {
                        'type': 'string'
                    }
                },
                'default': None
            }
    data_2 = {
                'not': {
                    'type': 'string',
                },
                'default': None
            }
    definitions = SchemaDefinitions()
    def_1 = not_from_json_schema(data_1, definitions)
    def_2 = not_from_json_schema(data_2, definitions)
    assert def_1 == Not(negated=Not(negated=String()), default=None)
    assert def_2 == Not(negated=String(), default=None)
    
test_not_from_json_schema()



# Generated at 2022-06-14 14:40:43.818119
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    schema = {
        "title": "test_one_of_from_json_schema",
        "type": "object",
        "properties": {
            "test": {
                "type": "string",
                "oneOf": [
                    {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "enum": ["complex"]},
                            "age": {"type": "integer"},
                        },
                        "additionalProperties": False,
                    },
                    {"type": "string", "enum": ["simple"]},
                ],
            }
        },
    }
    typesystem = from_json_schema(schema)

    assert typesystem.validate({"test": "simple"})
    assert typesystem.validate({"test": "complex"}) is False


# Generated at 2022-06-14 14:40:46.805870
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    def test_one_of_from_json_schema():
        schema_data = {
            "oneOf": [
                {"type": "number"},
                {"type": "integer"},
            ],
        }
        schema = one_of_from_json_schema(schema_data, {})
        assert schema.validate(1.0) == True
        assert schema.validate(1) == True
        assert schema.validate("1") == False

    test_one_of_from_json_schema()




# Generated at 2022-06-14 14:40:52.260221
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "http://example.com/product.schema.json",
        "title": "Product",
        "description": "A product from Acme's catalog",
        "type": "object",
        "properties": {
            "productId": {"type": "integer"},
            "productName": {"type": "string"},
            "price": {"type": "number", "exclusiveMinimum": "0.00"},
            "tags": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 1,
                "uniqueItems": True,
            },
        },
        "required": ["productId", "productName", "price"],
    }
    definitions=schema

# Generated at 2022-06-14 14:41:05.286523
# Unit test for function from_json_schema
def test_from_json_schema():
    # Test empty schema
    assert from_json_schema({}) == Any()

    # Test type constraints
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "null"}) == Const(None)
    assert from_json_schema({"type": "number"}) == Number()
    assert from_json_schema({"type": ["null", "number"]}) == Number() | Const(None)
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": "array"}) == Array()
    assert from_json_schema({"type": "object"}) == Object()
    assert from_json_schema({"type": "boolean"}) == Boolean()

    #

# Generated at 2022-06-14 14:41:17.390143
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({}) == Any()
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": ["string", "null"]}) == Union([String(), None])
    assert from_json_schema({"enum": [1, 2, 3]}) == Choice(items=[1, 2, 3])
    assert from_json_schema({"const": 42}) == Const(value=42)
    assert from_json_schema({"maxLength": 10}) == String(max_length=10)
    assert from_json_schema

# Generated at 2022-06-14 14:41:28.715793
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {
        'type': 'object',
        'properties': {
            'foo': {
                'type': 'string'
            }
        }
    }

    parsed = not_from_json_schema(data, definitions=None)
    assert parsed.validate({'foo': 'bar'})

    data2 = {
        'type': 'object',
        'properties': {
            'foo': {
                'type': 'number'
            }
        }
    }

    parsed = not_from_json_schema(data2, definitions=None)
    assert not parsed.validate({'foo': 'bar'})
    assert not parsed.validate({'foo': 1})
    assert parsed.validate({'foo': True})


# Generated at 2022-06-14 14:41:35.526637
# Unit test for function to_json_schema
def test_to_json_schema():
    class Thing(Schema):
        name = String(min_length=1)

    schema = Thing.make_validator()
    assert to_json_schema(schema) == {
        "definitions": {
            "name": {"type": "string"},
            "Thing": {
                "type": "object",
                "required": ["name"],
                "properties": {"name": {"$ref": "#/definitions/name"}},
                "additionalProperties": False,
                "propertyNames": {"$ref": "#/definitions/name"},
            },
        },
    }

    assert to_json_schema(schema.name) == {"type": "string"}



# Generated at 2022-06-14 14:41:40.887544
# Unit test for function from_json_schema
def test_from_json_schema():
    from pprint import pprint

    schema = {
        "definitions": {
            "foo": {
                "type": "string",
                "enum": ["foo", "bar"],
                "minLength": 3,
            },
            "bar": {"type": "null"},
        },
        "$ref": "#/definitions/foo",
    }

    field = from_json_schema(schema)
    field.validate("foo")
    field.validate("bar")
    with pytest.raises(ValidationError):
        field.validate("f")
    with pytest.raises(ValidationError):
        field.validate(None)

    schema = {"if": {"const": 1}, "then": {"const": 1}, "else": {"const": 2}}

# Generated at 2022-06-14 14:42:15.250258
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, "string", False, None) == String()
    assert from_json_schema_type({}, "boolean", False, None) == Boolean()
    assert from_json_schema_type({}, "integer", False, None) == Integer()
    assert from_json_schema_type({}, "number", False, None) == Number()
    assert from_json_schema_type({}, "null", False, None) == Const(None)
    assert from_json_schema_type({}, "object", False, None) == Object()
    assert from_json_schema_type({}, "array", False, None) == Array()

    assert from_json_schema_type({}, "string", True, None) == String(allow_null=True)
    assert from_json_

# Generated at 2022-06-14 14:42:24.747639
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Boolean()) == {"type": "boolean"}
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Float()) == {"type": "number"}
    assert to_json_schema(Decimal()) == {"type": "number"}
    assert to_json_schema(Array(String())) == {
        "type": "array",
        "items": [{"type": "string"}],
    }
    assert to_json_schema(Object({})) == {"type": "object"}

# Generated at 2022-06-14 14:42:37.552874
# Unit test for function to_json_schema
def test_to_json_schema():
    """Function to_json_schema"""
    arg = Any()
    assert to_json_schema(arg) == True
    arg = NeverMatch()
    assert to_json_schema(arg) == False
    arg = String(min_length=10, max_length=30, pattern_regex="^[a-zA-Z]*$")
    assert to_json_schema(arg) == {
        "type": "string",
        "minLength": 10,
        "maxLength": 30,
        "pattern": "^[a-zA-Z]*$",
    }
    arg = String(min_length=10, max_length=30, pattern_regex="^[a-zA-Z]*$", allow_null=True)

# Generated at 2022-06-14 14:42:49.870701
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert (
        from_json_schema_type(
            {}, "string", allow_null=True, definitions=SchemaDefinitions()
        ).name == "allow_null_string"
    )

    assert (
        from_json_schema_type(
            {"minimum": 5}, "integer", allow_null=True, definitions=SchemaDefinitions()
        ).name == "integer_greater_than_5"
    )

    assert (
        from_json_schema_type(
            {"items": [{"type": "string"}, {"type": "integer"}]},
            "array",
            allow_null=True,
            definitions=SchemaDefinitions(),
        ).name == "array_of_string_or_integer"
    )


# Generated at 2022-06-14 14:43:00.842757
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Array()) == {"type": "array"}
    assert to_json_schema(Object()) == {"type": "object"}
    assert to_json_schema(String(allow_null=True)) == {"type": ["string", "null"]}

    assert to_json_schema(
        Object(properties={"name": String(), "age": Integer()})
    ) == {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
    }

# Generated at 2022-06-14 14:43:11.925147
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Schema(
        **{
            "foo": String(required=True),
            "bar": Object(properties={"baz": Integer(min_value=0, max_value=100)}),
            "bam": Array(
                items=Union(
                    any_of=[Integer(min_value=1), Integer(max_value=42)]
                ),
                min_items=1,
                max_items=5,
            ),
        }
    )

# Generated at 2022-06-14 14:43:19.771298
# Unit test for function to_json_schema
def test_to_json_schema():
    import json  # type: ignore

    field = String(max_length=2)
    json_schema = to_json_schema(field)
    assert json.dumps(
        json_schema,
        sort_keys=True
    ) == '{"maxLength": 2, "type": "string"}'

    field = Float()
    json_schema = to_json_schema(field)
    assert json.dumps(
        json_schema,
        sort_keys=True
    ) == '{"type": "number"}'

    field = Decimal(3, 5)
    json_schema = to_json_schema(field)

# Generated at 2022-06-14 14:43:29.423997
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    assert (from_json_schema({'$ref': '#/definitions/foo'})
            == Reference('#/definitions/foo'))
    assert from_json_schema({'type': 'number'}) == Number()
    assert from_json_schema({'type': ['number', 'integer']}) == Integer()
    assert from_json_schema({'type': ['object', 'integer']}) == Integer()
    assert from_json_schema({'enum': [1]}) == Choice(1)
    assert from_json_schema({'allOf': [{'type': 'number'}, {'const': 1}]}) == Number(1)

# Generated at 2022-06-14 14:43:40.405335
# Unit test for function to_json_schema
def test_to_json_schema():
    assert (
        to_json_schema(Integer.minimum(2))
        == {
            "type": "integer",
            "minimum": 2,
            "default": NO_DEFAULT,
            "exclusiveMinimum": False,
            "uniqueItems": False,
        }
    )
    assert (
        to_json_schema(Integer.range(1, 10))
        == {
            "type": "integer",
            "minimum": 1,
            "maximum": 10,
            "default": NO_DEFAULT,
            "exclusiveMinimum": False,
            "exclusiveMaximum": False,
            "uniqueItems": False,
        }
    )

# Generated at 2022-06-14 14:43:44.444139
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Reference("#/definitions/name")) == {"$ref": "#/definitions/name"}

