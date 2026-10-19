

# Generated at 2022-06-14 14:35:31.988174
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert isinstance(enum_from_json_schema({'enum': ['one', 'two', 'three']}, None), Choice)
    assert isinstance(enum_from_json_schema({'enum': ['test', 'test', 'test']}, None), Choice)
    assert isinstance(enum_from_json_schema({'enum': ['test', 'test', 'test', 'test']}, None), Choice)
    assert isinstance(enum_from_json_schema({'enum': ['one', 'two']}, None), Choice)
    try:
        enum_from_json_schema({'enum': ['one', 'two', 'three', 'three']}, None)
        assert False
    except AssertionError:
        pass



# Generated at 2022-06-14 14:35:36.437778
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    assert one_of_from_json_schema({'oneOf' : [{'type' : 'string'}, {'type' : 'integer'}]}, None) == OneOf(one_of=[String(), Integer()], default=NO_DEFAULT)

# Generated at 2022-06-14 14:35:38.427209
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    assert one_of_from_json_schema({'default':1,
        'oneOf':[
            {'type':'integer'},
            {'type':'number'}
        ]},
        SchemaDefinitions()
    ).validate(1) == 1



# Generated at 2022-06-14 14:35:45.934511
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    schema = {
        "type": "object",
        "properties": {
            "field": {
                "if": {"type": "string", "pattern": "^a"},
                "then": {"type": "string", "pattern": "^b"},
                "else": {"type": "string", "pattern": "^c"},
            }
        },
    }
    field = from_json_schema(schema)

    assert field.validate({"field": "abc"}) == {"field": "abc"}
    assert field.validate({"field": "abd"}) == {"field": "abd"}
    assert field.validate({"field": "adc"}) == {"field": "adc"}
    assert field.validate({"field": "add"}) == {"field": "add"}


# Generated at 2022-06-14 14:35:54.946188
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {"allOf": [{"type": "string"}, {"enum": ["apple", "banana", "orange"]}]}
    assert isinstance(all_of_from_json_schema(data, definitions), AllOf)
    assert all_of_from_json_schema(data, definitions).all_of[0].type == "string"
    assert all_of_from_json_schema(data, definitions).all_of[1].choices == [("apple", "apple"), ("banana", "banana"), ("orange", "orange")]


# Generated at 2022-06-14 14:36:06.632458
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, "boolean", False, None) == Boolean()
    assert from_json_schema_type({}, "boolean", True, None) == Boolean(allow_null=True)
    assert from_json_schema_type({}, "null", True, None) == Const(None)
    assert from_json_schema_type({}, "null", False, None) == NeverMatch()

    schema = {
        "type": "string",
        "minLength": 1,
        "maxLength": 10,
        "format": "uri",
    }
    assert from_json_schema_type(schema, "string", False, None) == String(
        min_length=1, max_length=10, format="uri"
    )


# Generated at 2022-06-14 14:36:10.090240
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    schema = {
        "type": "number",
        "enum": ["1", "2", "3"],
    }
    field = enum_from_json_schema(schema, definitions=None)
    assert field.validate("2") == "2"
    assert field.validate("4") == "4"



# Generated at 2022-06-14 14:36:14.134434
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert (
        enum_from_json_schema(
            {"enum": ["a", "b", "c"]},
            definitions=None
        ) ==
        Choice(choices=[("a", "a"), ("b", "b"), ("c", "c")])
    )



# Generated at 2022-06-14 14:36:25.302631
# Unit test for function to_json_schema
def test_to_json_schema():
    from .json import Json

    def roundtrip(field):
        schema = to_json_schema(field)
        if isinstance(schema, dict):
            schema = Json(schema)
        return from_json_schema(schema)

    # Basic types
    assert roundtrip(String()) == String()
    assert roundtrip(Integer()) == Integer()
    assert roundtrip(Float()) == Float()
    assert roundtrip(Decimal()) == Decimal()
    assert roundtrip(Boolean()) == Boolean()
    assert roundtrip(Any()) == Any()

    # String validators
    assert roundtrip(String(min_length=4, max_length=8)) == String(min_length=4, max_length=8)

# Generated at 2022-06-14 14:36:30.446828
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    def make_ref(reference_string):
        data = {"$ref": reference_string}
        return ref_from_json_schema(data, definitions)
    definitions = SchemaDefinitions()
    definitions["#/definitions/ref"] = Any()
    definitions["https://example.com/definitions/ref"] = Any()
    assert make_ref("#/definitions/ref") == Reference("#/definitions/ref")
    assert make_ref("#/definitions/ref").definitions is definitions
    assert make_ref("https://example.com/definitions/ref") == Reference("https://example.com/definitions/ref")
    assert make_ref("https://example.com/definitions/ref").definitions is definitions



# Generated at 2022-06-14 14:37:49.144277
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {"allOf": [{"type": "string"}, {"pattern": "^[A-Z]"}]}
    constraints = all_of_from_json_schema(data, definitions=None)
    assert len(constraints.constraints) == 2
    assert constraints.constraints[0].type == "string"
    assert constraints.constraints[1].type == "regex"
    assert constraints.constraints[1].pattern == "^[A-Z]"



# Generated at 2022-06-14 14:37:59.941324
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "string",
        "minLength": 1,
        "maxLength": 10,
        "format": "email",
        "pattern": "^[0-9][a-z]$",
    }

    field = from_json_schema_type(data=schema, type_string="string", allow_null=False)
    data = "bar@baz.com"
    errors = field.validate(data)
    assert not errors

    data = "foo"
    errors = field.validate(data)
    assert errors

    data = ""
    errors = field.validate(data)
    assert errors

    data = "f23"

# Generated at 2022-06-14 14:38:04.611765
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {"not": {"type": "string"}}

    field = not_from_json_schema(data, definitions=None)
    assert field.validate(123) == "Must not be a string."
    assert field.validate(None) == "Must not be a string."



# Generated at 2022-06-14 14:38:06.785950
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    assert const_from_json_schema({"const": 4}) == Const(const=4, default=NO_DEFAULT)



# Generated at 2022-06-14 14:38:14.236448
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    test_subject_typesystem_field = any_of_from_json_schema({"anyOf": [{"type": "integer"}, {"type": "string"}]}, definitions=definitions)
    test_subject_typesystem_object = typesystem.Object(properties={
        "my_field": test_subject_typesystem_field
    })
    test_subject_invalid = test_subject_typesystem_object({"my_field": 5})
    test_subject_valid = test_subject_typesystem_object({"my_field": "5"})
    assert test_subject_invalid.is_valid()
    assert test_subject_valid.is_valid()



# Generated at 2022-06-14 14:38:24.890761
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({}, definitions=definitions) == Any()
    assert type_from_json_schema({"type": "string"}, definitions=definitions) == String()
    assert type_from_json_schema({"nullable": True}, definitions=definitions) == Const(None)
    assert type_from_json_schema({"nullable": 0}, definitions=definitions) == Any()
    assert type_from_json_schema({"type": ["integer", "number"]}, definitions=definitions) == Union(
        any_of=[Integer(), Float()]
    )
    assert type_from_json_schema({"type": "integer"}, definitions=definitions) == Integer()
    assert type_from_json_schema({"type": "number"}, definitions=definitions) == Float()

# Generated at 2022-06-14 14:38:35.912060
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    json_schema = {'$ref': '#/definitions/JSONSchema'}
    field = from_json_schema(json_schema)
    assert isinstance(field, Reference)
    assert field.schema_definitions is definitions
    assert field.ref == '#/definitions/JSONSchema'
    assert field.definition is None

    json_schema = {'type': 'boolean'}
    field = from_json_schema(json_schema)
    assert isinstance(field, Boolean)

    json_schema = {'type': ['boolean', 'null']}
    field = from_json_schema(json_schema)
    assert isinstance(field, Union)
    assert len(field.any_of) == 1

# Generated at 2022-06-14 14:38:41.321705
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    assert const_from_json_schema(dict(const=1.0), SchemaDefinitions()) == Const(const=1.0)
    assert const_from_json_schema(dict(const=1), SchemaDefinitions()) == Const(const=1)
    assert const_from_json_schema(dict(const="a"), SchemaDefinitions()) == Const(const="a")
    assert const_from_json_schema(dict(const=True), SchemaDefinitions()) == Const(const=True)



# Generated at 2022-06-14 14:38:42.772151
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    original = Any()
    negated_field = not_from_json_schema({"not": {}}, SchemaDefinitions())
    assert negated_field.negated == original



# Generated at 2022-06-14 14:38:47.990665
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    schema = {
        "title": "allOf schema",
        "type": "string",
        "allOf": [
            {"type": "string", "minLength": 3},
            {"type": "string", "maxLength": 10},
        ],
    }
    field = all_of_from_json_schema(schema, definitions=definitions)
    def assert_pass(value):
        assert field.validate(value) == value
    def assert_fail(value, expected_error=None):
        try:
            field.validate(value)
        except Exception as error:
            if expected_error:
                assert isinstance(error, expected_error)
            assert str(error)
        else:
            assert False, f"Expected error for value={value!r}"
    assert_pass('123')
   

# Generated at 2022-06-14 14:39:36.039138
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert isinstance(from_json_schema(data={"type": "integer"}), Integer)
    assert isinstance(from_json_schema(data={"type": "number"}), Number)
    assert isinstance(from_json_schema(data={"type": "boolean"}), Boolean)
    assert isinstance(from_json_schema(data={"type": "null"}), Const)
    assert isinstance(from_json_schema(data={"type": "string"}), String)
    assert isinstance(from_json_schema(data={"type": "array"}), Array)
    assert isinstance(from_json_schema(data={"type": "object"}), Object)
    assert isinstance(from_json_schema(data={"type": "array", "items": {}}), Array)
   

# Generated at 2022-06-14 14:39:48.758020
# Unit test for function to_json_schema
def test_to_json_schema():
    import datetime

    def make_schema():
        class Schema(Validator):
            age = Integer(
                minimum=1, maximum=120, title="Age", description="Age of the person."
            )
            name = String(
                min_length=1,
                max_length=100,
                pattern_regex=re.compile(r"[A-Z][a-z]*"),
                title="Name",
                description="The first and last name of the person.",
            )
            email = String(
                format="email",
                title="Email address",
                description="The persons email address.",
            )
            spouse_age = Integer(
                title="Spouse age",
                description="Age of the persons spouse.",
                default=lambda model: model["age"] + 10,
            )

# Generated at 2022-06-14 14:39:51.145854
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    any_of_from_json_schema(data, definitions=definitions) == Union(**kwargs)



# Generated at 2022-06-14 14:39:53.781494
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    kwargs = {"any_of": [String(), Boolean()], "default": 0}
    return Union(**kwargs)



# Generated at 2022-06-14 14:39:59.030616
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(False).validate(False)
    assert from_json_schema(True).validate(True)
    assert not from_json_schema(False).validate(True)
    assert not from_json_schema(True).validate(False)



# Generated at 2022-06-14 14:40:08.445825
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    definitions = SchemaDefinitions()
    data = {"type": "number"}
    field = from_json_schema(data, definitions=definitions)
    assert isinstance(field, Number)

    data = {"type": "integer"}
    field = from_json_schema(data, definitions=definitions)
    assert isinstance(field, Integer)

    data = {"type": "string"}
    field = from_json_schema(data, definitions=definitions)
    assert isinstance(field, String)

    data = {"type": "boolean"}
    field = from_json_schema(data, definitions=definitions)
    assert isinstance(field, Boolean)

    data = {"type": "array"}
    field = from_json_schema(data, definitions=definitions)
    assert isinstance(field, Array)

# Generated at 2022-06-14 14:40:16.668060
# Unit test for function from_json_schema
def test_from_json_schema():
    print(from_json_schema(False))
    print(from_json_schema(True))
    print(from_json_schema({"enum": [1, 2, 3]}))
    print(from_json_schema({"enum": [1, 2, 3], "type": "integer"}))
    print(from_json_schema({"type": "integer", "minimum": 1, "maximum": 20}))
    print(from_json_schema({"if": {"const": True}, "then": {"const": True}}))
    print(from_json_schema({"if": {"const": False}, "then": {"const": True}}))



# Generated at 2022-06-14 14:40:22.723167
# Unit test for function to_json_schema
def test_to_json_schema():
    import pytest
    from dacite import from_dict
    # Build a validator
    schema = Schema(
        {"name": String(min_length=2), "age": Integer(minimum=18), "registered": Boolean()}
    )
    # Convert to JSON Schema
    json_schema = to_json_schema(schema)
    # Check that result is parsable
    actual_schema = from_dict(
        data=json_schema, data_class=JsonSchema, config=JsonSchema.config
    )
    # Check that result is the same
    assert schema == actual_schema.make_validator()
    assert json_schema == to_json_schema(actual_schema)

    # Converts OK from JSON Schema

# Generated at 2022-06-14 14:40:25.903534
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    assert ref_from_json_schema({"$ref": "#/definitions/my_field"}) == Reference("#/definitions/my_field")



# Generated at 2022-06-14 14:40:35.286127
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema({}) == Any()
    assert from_json_schema({'$ref': '#/definitions/test'}) == Any()
    assert from_json_schema({'const':1}) == Const(1)
    assert from_json_schema({'type':'array','items':{'$ref':'#/definitions/test'}}) == Any()
    assert from_json_schema({'type':'array','items':{'$ref':'#/definitions/test'},'definitions':{'test':{'type':'number'}}}) == Array()

# Generated at 2022-06-14 14:42:50.841431
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    test_data = {"anyOf": [{}, {}, {}]}
    assert isinstance(any_of_from_json_schema(test_data, definitions), Union) 


# Generated at 2022-06-14 14:42:54.625400
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {'anyOf': [{'const': 'one'}, {'const': 'two'}, {'const': 'three'}]}
    assert any_of_from_json_schema(data, definitions).field_type is Union


# Generated at 2022-06-14 14:43:06.113369
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    schema = {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "number"
        },
        {
          "type": "boolean"
        }
      ]
    }
    result = any_of_from_json_schema(schema, definitions=SchemaDefinitions())
    print(result)

# Generated at 2022-06-14 14:43:15.957877
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Integer(minimum=3, allow_null=False)) == {
        "type": "integer",
        "minimum": 3,
    }
    assert to_json_schema(Integer(minimum=3, allow_null=True)) == {
        "type": ["integer", "null"],
        "minimum": 3,
    }
    assert to_json_schema(String(min_length=3, allow_null=False)) == {
        "type": "string",
        "minLength": 3,
    }
    assert to_json_schema(
        Object(properties={"foo": Integer(minimum=3, allow_null=False)})
    ) == {
        "type": "object",
        "properties": {"foo": {"type": "integer", "minimum": 3}},
    }

# Generated at 2022-06-14 14:43:18.866353
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {"anyOf": [{"type" : "integer"}]}
    definitions = SchemaDefinitions()
    schema = any_of_from_json_schema(data, definitions)
    assert schema is not None
    assert schema is not None


# Generated at 2022-06-14 14:43:24.005660
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {
              "anyOf":[
                {"type":"number"},
                {"type":"integer"}
              ]
            }
    definitions = SchemaDefinitions()
    constraints = any_of_from_json_schema(data, definitions)
    assert(isinstance(constraints, Union))
    assert(len(constraints.any_of) == 2)
    for c in constraints.any_of:
        assert(isinstance(c, (Number, Integer)))
    assert(constraints.allow_null == False)
    assert(constraints.validate(10.0) == True)
    assert(constraints.validate("test") == False)



# Generated at 2022-06-14 14:43:29.925716
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {"anyOf": [{"type": "string"}, {"type": "integer", "minimum": 0}]}
    field = any_of_from_json_schema(data, definitions=definitions)
    assert field.validate("hello") is None
    assert field.validate(5) is None
    assert field.validate(-1) is not None
    assert field.validate(None) is not None



# Generated at 2022-06-14 14:43:37.568440
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    def test_call(**kwargs):
        return Union(**kwargs)

    schema = {
        "anyOf": [
            {
                "$ref": "#/definitions/schema1a",
                "type": "object",
                "default": "default_value1"
            },
            {
                "$ref": "#/definitions/schema1b",
                "type": "object",
                "default": "default_value2"
            }
        ]
    }
    definitions = SchemaDefinitions()
    definitions["#/definitions/schema1a"] = Object()
    definitions["#/definitions/schema1b"] = Object()

    result = any_of_from_json_schema(schema, definitions=definitions)

    assert result.fields == [Object(), Object()]

# Generated at 2022-06-14 14:43:46.730943
# Unit test for function to_json_schema
def test_to_json_schema():
    field = Integer(minimum=0, maximum=10, default=5)
    assert to_json_schema(field) == {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "integer",
        "minimum": 0,
        "maximum": 10,
        "default": 5,
    }
    field = Integer(minimum=0, maximum=10, default=5, allow_null=True)
    assert to_json_schema(field) == {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": ["integer", "null"],
        "minimum": 0,
        "maximum": 10,
        "default": 5,
    }



# Generated at 2022-06-14 14:43:54.826434
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({"type": "string"}, type_string="string", allow_null=False) == String()
    assert from_json_schema_type({"type": "string"}, type_string="string", allow_null=True) == String(allow_null=True)
    assert from_json_schema_type({"type": "boolean"}, type_string="boolean", allow_null=False) == Boolean()
    assert from_json_schema_type({"type": "boolean"}, type_string="boolean", allow_null=True) == Boolean(allow_null=True)
    assert from_json_schema_type({"type": "integer"}, type_string="integer", allow_null=False) == Integer()