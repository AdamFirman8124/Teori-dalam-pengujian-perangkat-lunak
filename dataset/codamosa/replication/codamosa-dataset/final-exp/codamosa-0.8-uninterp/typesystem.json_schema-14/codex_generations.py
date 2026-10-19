

# Generated at 2022-06-14 14:35:34.444993
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {
        "allOf": [
            {"$ref": "#/definitions/positiveInteger"},
            {"minimum": 1},
        ],
        "definitions": {
            "positiveInteger": {"type": "integer", "minimum": 0}
        }
    }
    field = all_of_from_json_schema(data, definitions)
    assert field.is_valid(1)


# Generated at 2022-06-14 14:35:43.063853
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    from typesystem import from_json_schema
    assert type_from_json_schema({}) == Any()
    assert type_from_json_schema({"type": "string"}, definitions) == String()
    assert type_from_json_schema({"type": "string", "format": "email"}, definitions) == String(
        format="email"
    )
    assert type_from_json_schema(
        {"type": "string", "format": "email", "required": True}, definitions
    ) == String(format="email")
    assert type_from_json_schema({"type": "integer"}, definitions) == Integer()
    assert type_from_json_schema({"type": ["integer", "string"]}, definitions) == Union(
        items=[String(), Integer()]
    )
    assert type_from_

# Generated at 2022-06-14 14:35:45.025683
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({}, SchemaDefinitions()) == Any()
    assert type_from_json_schema({"type": "string"}, SchemaDefinitions()) == String()



# Generated at 2022-06-14 14:35:54.178610
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "type": "string",
        "enum": ["aaaa", "bbbb", "cccc"],
        "default": "aaaa",
    }
    field = from_json_schema(schema)
    assert isinstance(field, Choice)
    assert field.choices == [("aaaa", "aaaa"), ("bbbb", "bbbb"), ("cccc", "cccc")]
    assert field.default == "aaaa"



# Generated at 2022-06-14 14:36:03.762194
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    schema1 = {"type":"number", "minimum":5}
    schema2 = {"type":"number", "maximum":8}
    schema_anyof = {"anyOf": [schema1, schema2]}
    fld_anyof_from_jsonschema = any_of_from_json_schema(schema_anyof, SchemaDefinitions())
    fld_anyof = Union(any_of = [Float(minimum=5), Float(maximum=8)])
    assert fld_anyof.validate(7.5)
    assert fld_anyof_from_jsonschema.validate(7.5)


# Generated at 2022-06-14 14:36:13.210916
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    import json
    source = {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "definitions": {
        "negativeInteger": {
          "type": "integer",
          "minimum": -1
        },
        "positiveInteger": {
          "type": "integer",
          "maximum": 1
        }
      },
      "type": "object",
      "properties": {
        "if": { "$ref": "#/definitions/negativeInteger" },
        "then": { "$ref": "#/definitions/positiveInteger" },
        "else": { "type": "string" }
      },
      "required": [ "if", "then", "else" ]
    }


# Generated at 2022-06-14 14:36:20.882388
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert enum_from_json_schema({"enum": ["foo", "bar"]}) == Choice(choices=[("foo", "foo"), ("bar", "bar")])
    assert enum_from_json_schema({"enum": "foo"}) == Choice(choices=[("foo", "foo")])
    assert enum_from_json_schema({"enum": [3, 9, 27]}, definitions=definitions).validate([3, 9, 27]) is None
    assert enum_from_json_schema({"enum": ["foo", "bar"]}, definitions=definitions).validate("foo") == "foo"
    assert enum_from_json_schema({"enum": ["foo", "bar"]}, definitions=definitions).validate("bar") == "bar"

# Generated at 2022-06-14 14:36:30.130854
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {
      "type": "string",
      "oneOf":[
        {
          "const": "red"
        },
        {
          "const": "green"
        },
        {
          "const": "blue"
        }
      ]
    }
    definitions = SchemaDefinitions()
    schema = any_of_from_json_schema(data,definitions)
    assert schema.one_of[0].to == "red"
    assert schema.one_of[1].to == "green"
    assert schema.one_of[2].to == "blue"



# Generated at 2022-06-14 14:36:35.204635
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    # Dict representing valid JSON schema
    data = {
        "type": "object",
        "allOf": [
            {"$ref": "#/definitions/Level"},
            {
                "type": "object",
                "properties": {
                    "defeatThreshold": {
                        "type": ["object", "null"],
                        "properties": {
                            "minThreshold": {"type": "number"},
                            "maxThreshold": {"type": "number"},
                        },
                        "required": ["minThreshold", "maxThreshold"],
                    }
                },
            },
        ],
    }
    # Typesystem field for data

# Generated at 2022-06-14 14:36:39.310172
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    file = open("json_schema_test_files/enum_test.json")
    data = json.load(file)
    choices = [(item, item) for item in data["enum"]]
    kwargs = {"choices": choices, "default": data.get("default", NO_DEFAULT)}
    assert enum_from_json_schema(data, definitions) == Choice(**kwargs)



# Generated at 2022-06-14 14:37:21.439557
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    def test_const_from_json_schema_assert(const, expected):
        actual = const_from_json_schema({"const": const})
        assert actual == expected

    # The four cases correspond to the four primary types,
    # in the order they were specified in the swagger spec.
    test_const_from_json_schema_assert("string", Const("string"))
    test_const_from_json_schema_assert(42, Const(42))
    test_const_from_json_schema_assert(True, Const(True))
    test_const_from_json_schema_assert(None, Const(None))
    test_const_from_json_schema_assert([], Const([]))

# Generated at 2022-06-14 14:37:30.415522
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    json_schema = {"const": 1.0}
    assert const_from_json_schema(json_schema, None).validate(1.0)
    assert not const_from_json_schema(json_schema, None).validate(1)
    assert not const_from_json_schema(json_schema, None).validate(2)
    json_schema = {"const": "foo"}
    assert const_from_json_schema(json_schema, None).validate("foo")
    assert not const_from_json_schema(json_schema, None).validate("bar")


# Generated at 2022-06-14 14:37:36.664565
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema({"allOf": [{"type": "number"}]}, definitions) == Float()
    assert all_of_from_json_schema(
        {"allOf": [{"type": "number"}, {"type": "null"}]}, definitions
    ) == Float(allow_null=True)



# Generated at 2022-06-14 14:37:46.954136
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    schema = {
                "allOf": [
                    {"$ref": "#/definitions/string_schema"},
                    {"$ref": "#/definitions/integer_schema"}
                ]
            }
    definition = {
                    "string_schema": {
                        "type": "string",
                        "minLength": 1
                    },
                    "integer_schema": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 100
                    }

                }
    defs = SchemaDefinitions()
    for key, value in definition.items():
        ref = f"#/definitions/{key}"
        defs[ref] = from_json_schema(value, definitions=defs)

# Generated at 2022-06-14 14:37:55.036452
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "if": {"type": "integer"},
        "then": {"type": "string"},
        "else": {"type": "number"},
    }

    field = if_then_else_from_json_schema(data, definitions=None)
    assert field.if_clause.type == Integer()
    assert field.then_clause.type == String()
    assert field.else_clause.type == Float()



# Generated at 2022-06-14 14:38:01.041507
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    field = const_from_json_schema(data={"const": 10}, definitions=None)
    assert field.validate(10) == 10
    assert field.validate(None) == None
    assert field.validate(20) == False


# Generated at 2022-06-14 14:38:10.288463
# Unit test for function const_from_json_schema
def test_const_from_json_schema():  # pragma: no cover
    const_schema_1 = {
        "const": 9
    }
    const_schema_2 = {
        "const": 9,
        "default": 3
    }
    const_field_1 = const_from_json_schema(const_schema_1, None)
    const_field_2 = const_from_json_schema(const_schema_2, None)
    assert const_field_1(9)
    assert not const_field_1(3)
    assert const_field_1.get_default() == NO_DEFAULT
    assert not const_field_2(9)
    assert const_field_2(3)
    assert const_field_2.get_default() == 3



# Generated at 2022-06-14 14:38:18.158424
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "definitions": {},
        "properties": {
            "a": {
                "type": "object",
                "properties": {
                    "b": {"type": "number"}
                },
                "required": ["b"]
            }
        },
        "required": ["a"]
    }
    field = from_json_schema(schema)
    # print(field.to_json_schema())


# Generated at 2022-06-14 14:38:23.276807
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    to_test = one_of_from_json_schema({'oneOf': [{'type': 'string'}, {'type': 'integer'}]},definitions=None)
    assert(to_test.validate('test') == 'test')
    assert(to_test.validate(42) == 42)
    assert(to_test.validate(None) == False)
    assert(to_test.validate(True) == False)
    assert(to_test.validate(False) == False)



# Generated at 2022-06-14 14:38:27.003857
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    # Tests for const from json schema
    # Given When Then
    expected = Const(const="foo")
    actual = const_from_json_schema(data={"const": "foo"}, definitions=None)
    assert actual == expected, "Expected and actual values do not match"



# Generated at 2022-06-14 14:38:57.203980
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    try:
        Reference(to="outside_reference", definitions=SchemaDefinitions())
        assert False, "Expected a raised ValueError"
    except ValueError:
        pass



# Generated at 2022-06-14 14:39:01.247177
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    assert (not_from_json_schema({"not": True}) == Not(negated=Const(True)))
    assert (not_from_json_schema({"not": False}) == Not(negated=Const(False)))



# Generated at 2022-06-14 14:39:08.736699
# Unit test for function ref_from_json_schema

# Generated at 2022-06-14 14:39:12.870872
# Unit test for function to_json_schema
def test_to_json_schema():
    data = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer", "minimum": 18},
        },
    }
    field = from_json_schema(data)
    result = to_json_schema(field)
    assert result == data

    class Human(SchemaDefinitions):
        name = String()
        age = Integer(minimum=18)

    result = to_json_schema(Human)
    assert result == data

    class Person(SchemaDefinitions):
        name = String()
        age = Integer(minimum=18)

        def is_adult(self):
            return self.age >= 18
    result = to_json_schema(Person)
    assert result == data

# Generated at 2022-06-14 14:39:24.749281
# Unit test for function to_json_schema
def test_to_json_schema():
    class TestSchema(Schema):
        name = String()
        age = Integer()

    data = to_json_schema(TestSchema)

# Generated at 2022-06-14 14:39:32.130362
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    input_data = {"allOf": [{"$ref": "#/definitions/a"}, {"$ref": "#/definitions/b"}]}
    output_field = all_of_from_json_schema(input_data, definitions)
    expected_output = [{"$ref": "#/definitions/a"}, {"$ref": "#/definitions/b"}]
    assert output_field.all_of == expected_output


# Generated at 2022-06-14 14:39:40.394684
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    definitions = SchemaDefinitions()
    definitions['#/definitions/string_schema'] = String(max_length=3)
    definitions['#/definitions/integer_schema'] = Integer(maximum=5)
    field = from_json_schema(
        {
            "$ref": "#/definitions/string_schema",
        },
        definitions=definitions
    )
    assert isinstance(field, Reference)
    assert field.to == '#/definitions/string_schema'
    assert field.definitions == definitions
    field = from_json_schema(
        {
            "$ref": "#/definitions/integer_schema",
        },
        definitions=definitions
    )
    assert isinstance(field, Reference)
    assert field.to == '#/definitions/integer_schema'

# Generated at 2022-06-14 14:39:43.936287
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    assert not_from_json_schema(data={"not": {"type": "string"}}, definitions=None).__str__() == 'not(<class \'str\'>)'



# Generated at 2022-06-14 14:39:50.272102
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    import pytest

    def _test(data, reference_string):
        ref = ref_from_json_schema(data, definitions=SchemaDefinitions())
        assert ref.to == reference_string

    _test({"$ref": "#/a/b/c"}, "#/a/b/c")
    with pytest.raises(AssertionError):
        _test({"$ref": "a/b/c"}, None)



# Generated at 2022-06-14 14:39:53.961093
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema(
        {"allOf": [{"type": "string"}, {"minLength": 1}]}
    ) == AllOf(all_of=[String(), String(min_length=1)])
    assert all_of_from_json_schema({"allOf": []}) == AllOf(all_of=[])



# Generated at 2022-06-14 14:40:20.730394
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="boolean", allow_null=True) == Boolean(allow_null=True)
    assert from_json_schema_type({}, type_string="boolean", allow_null=False) == Boolean(allow_null=False)
    assert from_json_schema_type({}, type_string="integer", allow_null=True) == Integer(allow_null=True)
    assert from_json_schema_type({}, type_string="integer", allow_null=False) == Integer(allow_null=False)
    assert from_json_schema_type({}, type_string="number", allow_null=True) == Float(allow_null=True)

# Generated at 2022-06-14 14:40:31.782320
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    data = {
        "type": "object",
        "properties": {
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "date_of_birth": {"type": "string", "format": "date"},
            "is_active": {"type": "boolean"},
            "tasks": {
                "type": "array",
                "items": {"type": "string"},
                "uniqueItems": True,
                "minItems": 1,
                "maxItems": 1000,
            },
        },
        "additionalProperties": False,
        "minProperties": 1,
        "maxProperties": 10,
    }
    field = from_json_schema(data)
    assert field["first_name"] == String()

# Generated at 2022-06-14 14:40:37.854729
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    data = {"type": "string", "minLength": 1, "maxLength": 2, "format": "date"}
    field = from_json_schema_type(data, "string", False, None)
    assert isinstance(field, String)
    data = {"type": "string", "format": "date"}
    field = from_json_schema_type(data, "string", False, None)
    assert isinstance(field, String)
    data = {"type": "string", "format": "date", "minLength": 0}
    field = from_json_schema_type(data, "string", False, None)
    assert isinstance(field, String)



# Generated at 2022-06-14 14:40:39.915762
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"type": "string"}) == String()



# Generated at 2022-06-14 14:40:50.415443
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False

    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(String(allow_null=True)) == {"type": ["string", "null"]}
    assert to_json_schema(String(min_length=0)) == {"type": "string", "minLength": 0}
    assert to_json_schema(String(max_length=0)) == {"type": "string", "maxLength": 0}

    assert to_json_schema(Integer()) == {"type": "integer"}

    assert to_json_schema(Float()) == {"type": "number"}

    assert to_json_schema(Decimal()) == {"type": "number"}


# Generated at 2022-06-14 14:41:03.505976
# Unit test for function to_json_schema
def test_to_json_schema():
    definitions: SchemaDefinitions = {
        "fixed_int": Integer(minimum=5, maximum=5),
        "string_in_list": String(choices=[("a", "a"), ("b", "b")]),
    }

    assert to_json_schema(Integer) == {
        "type": "integer",
        "default": NO_DEFAULT,
    }

    assert to_json_schema(Integer(allow_null=True)) == {
        "type": ["integer", "null"],
        "default": NO_DEFAULT,
    }

    assert to_json_schema(Integer(minimum=5)) == {
        "type": "integer",
        "minimum": 5,
        "default": NO_DEFAULT,
    }


# Generated at 2022-06-14 14:41:12.210099
# Unit test for function from_json_schema
def test_from_json_schema():
    data={'$schema': 'http://json-schema.org/draft-07/schema', 'definitions': {'Foo': {'properties': {'foo': {'type': 'string'}}, 'type': 'object'}, 'Bar': {'properties': {'bar': {'$ref': '#/definitions/Foo'}}, 'type': 'object'}, 'Baz': {'properties': {'baz': {'$ref': '#/definitions/Bar'}}, 'type': 'object'}}, 'properties': {'baz': {'$ref': '#/definitions/Baz'}}, 'title': 'Root', 'type': 'object'}
    definitions = SchemaDefinitions()
    definitions["JSONSchema"] = JSONSchema

# Generated at 2022-06-14 14:41:19.638629
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {
        "allOf": [
            {"type": "number", "multipleOf": 3},
            {"type": "number", "maximum": 18},
        ]
    }
    all_of = [from_json_schema(item, definitions=definitions) for item in data["allOf"]]
    
    kwargs = {"all_of": all_of, "default": data.get("default", NO_DEFAULT)}
    assert AllOf(**kwargs) == AllOf([Number(multiple_of=3), Number(maximum=18)])

# Generated at 2022-06-14 14:41:25.966076
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {"allOf":[{"type":"string"}, {"minLength": 4}], "default": "harry"}
    field = all_of_from_json_schema(data, definitions)
    assert isinstance(field, AllOf)
    assert len(field.all_of) == 2
    assert field.all_of[0].type == String
    assert field.all_of[1].type == String
    data = {"allOf":[{"type":"string"},
            {"type":"integer"}], "default": "harry"}
    field = all_of_from_json_schema(data, definitions)
    assert isinstance(field, AllOf)
    assert len(field.all_of) == 2
    assert field.all_of[0].type == String
    assert field.all_of[1].type == Integer

# Generated at 2022-06-14 14:41:34.703813
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(String(nullable=True)) == {"type": ["string", "null"]}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Boolean()) == {"type": "boolean"}
    assert to_json_schema(Boolean(nullable=True)) == {"type": ["boolean", "null"]}
    assert to_json_schema(Array(String())) == {
        "type": "array",
        "items": {"type": "string"},
    }

# Generated at 2022-06-14 14:42:14.086089
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Float()) == {"type": "number"}
    assert to_json_schema(Decimal()) == {"type": "number"}
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False
    assert to_json_schema(String(allow_null=True)) == {"type": ["string", "null"]}
    assert to_json_schema(Integer(allow_null=True)) == {"type": ["integer", "null"]}
    assert to_json_schema(Float(allow_null=True)) == {"type": ["number", "null"]}
    assert to_json_

# Generated at 2022-06-14 14:42:24.043586
# Unit test for function to_json_schema
def test_to_json_schema():
    # test that the output works with jsonschema
    import jsonschema

    from . import fields
    from .schema import schema

    def f():
        class Person(Schema):
            first_name = fields.String()
            last_name = fields.String()
            age = fields.Integer()
            secret_password = fields.String(required=False)

        class Address(Schema):
            city = fields.String()
            street = fields.String()

        class HomeAddress(Address):
            door_number = fields.Integer()

        class VacationAddress(Address):
            street_name = fields.String(required=False)

        class User(Schema):
            person = fields.Embedded(Person)
            address = fields.Union(fields.Embedded(HomeAddress), fields.Embedded(VacationAddress))


# Generated at 2022-06-14 14:42:36.709362
# Unit test for function to_json_schema
def test_to_json_schema():
    to_json_schema(Field(default="Foo"))
    to_json_schema(Field(default=""))
    to_json_schema(Field(default=False))
    to_json_schema(Field(default=0))
    to_json_schema(Field(default=0.0))
    to_json_schema(Field(default=Decimal("0")))
    to_json_schema(Field(default=None))
    to_json_schema(Field(default=...))  # type: ignore[operator]
    to_json_schema(Field(default=object()))

    to_json_schema(Integer())
    to_json_schema(Integer(default=0))
    to_json_schema(Integer(default=None))

# Generated at 2022-06-14 14:42:49.133457
# Unit test for function to_json_schema
def test_to_json_schema():
    definitions = {
        "nested": String(max_length=5),
        "nested_array": Array(items=String(max_length=5)),
    }


# Generated at 2022-06-14 14:43:00.077575
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Field()) == {}
    assert to_json_schema(Field(default="default")) == {"default": "default"}
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(String(allow_null=True)) == {"type": ["string", "null"]}
    assert to_json_schema(String(min_length=1)) == {"type": "string", "minLength": 1}
    assert to_json_schema(String(max_length=2)) == {"type": "string", "maxLength": 2}
    assert to_json_schema(String(pattern="[A-Za-z]+")) == {
        "type": "string",
        "pattern": "[A-Za-z]+",
    }

# Generated at 2022-06-14 14:43:11.097671
# Unit test for function to_json_schema
def test_to_json_schema():
    from .types import get_type

    def check(field: Field, ground_truth: dict) -> None:
        assert to_json_schema(field) == ground_truth
        bytes_ = get_type(field)
        assert to_json_schema(bytes_) == ground_truth
        schema = get_type(field, Schema)
        assert to_json_schema(schema) == ground_truth

    # basic types

    check(allow_null(Integer()), {"type": ["number", "null"]})
    check(
        allow_null(Integer(minimum=1, maximum=100)),
        {"type": ["number", "null"], "minimum": 1, "maximum": 100},
    )
    check(allow_null(Boolean()), {"type": ["boolean", "null"]})

# Generated at 2022-06-14 14:43:16.041844
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {"if": {"enum": [1]}, "then": {"enum": [2]}, "else": {"enum": [3]}}
    assert data["if"] == {"enum": [1]}
    assert data["then"] == {"enum": [2]}
    assert data["else"] == {"enum": [3]}
    result = if_then_else_from_json_schema(data, definitions={})
    assert result.if_clause == {"choices": [(1, 1)]}
    assert result.then_clause == {"choices": [(2, 2)]}
    assert result.else_clause == {"choices": [(3, 3)]}

definitions = SchemaDefinitions()
definitions["JSONSchema"].definitions = definitions


# Generated at 2022-06-14 14:43:23.035115
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    # fmt: off
    # pylint: disable=line-too-long
    if_then_else_constraints = {
        "type": "object",
        "properties": {
            "if": {"$ref": "#/definitions/oneOf" },
            "then": { "$ref": "#/definitions/oneOf" },
            "else": { "$ref": "#/definitions/oneOf" }
        },
        "additionalProperties": False,
        "required": [
            "if",
            "then"
        ]
    }
    # pylint: enable=line-too-long
    # fmt: on


# Generated at 2022-06-14 14:43:32.742680
# Unit test for function to_json_schema
def test_to_json_schema():
    import json
    import jsonschema
    from pydantic_json_schema import Field

    def validate_schema(schema):
        try:
            jsonschema.validate({}, schema)
        except jsonschema.exceptions.ValidationError as exc:
            pytest.fail(
                f"Input schema invalid: {exc}\n{json.dumps(schema, indent=2)}"
            )

    validate_schema(to_json_schema(Field(Any)))
    validate_schema(to_json_schema(Field(NeverMatch)))
    validate_schema(to_json_schema(Field(Named("hello"))))
    validate_schema(to_json_schema(Field(Any, allow_null=True)))

# Generated at 2022-06-14 14:43:43.441715
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Schema(
        {
            "path": String(),
            "owner": {
                "name": String(),
                "age": Integer(),
                "children": Array(String()),
            },
            "shares": Array(
                Choice(
                    choices=[
                        ("READ", "read"),
                        ("WRITE", "write"),
                        ("EXECUTE", "execute"),
                    ]
                )
            ),
        }
    )
    reference_schema = Schema({"email": String().format("email")})
    schema.definitions["email"] = reference_schema

    result = to_json_schema(schema)

# Generated at 2022-06-14 14:44:06.572828
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    for type_str in ("number", "integer", "string", "boolean", "array", "object"):
        assert from_json_schema_type(
            {}, type_string=type_str, allow_null=True, definitions=SchemaDefinitions()
        )



# Generated at 2022-06-14 14:44:13.715353
# Unit test for function from_json_schema
def test_from_json_schema():
    # Simple wrapper around from_json_schema
    def ts_from_js_schema(data: typing.Union[bool, dict], **kwargs):
        return from_json_schema(data, **kwargs)

    assert ts_from_js_schema(True) == Any()
    assert ts_from_js_schema(False) == NeverMatch()

    # Definitions
    assert ts_from_js_schema({"$ref": "#/definitions/foo"}) == Reference("#/definitions/foo")
    assert ts_from_js_schema(True, definitions={"#/definitions/foo": String()}) == Any()