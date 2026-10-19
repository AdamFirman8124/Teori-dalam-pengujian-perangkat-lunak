

# Generated at 2022-06-14 14:35:04.817925
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {"anyOf": [{"type": "string"}, {"type": "integer"}]}
    expected = Union(
        any_of=[
            String(allow_blank=False),
            Integer(minimum=None, maximum=None, multiple_of=None, allow_nan=False),
        ]
    )
    assert any_of_from_json_schema(data, SchemaDefinitions()) == expected



# Generated at 2022-06-14 14:35:13.897235
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    """
    Unit test for function if_then_else_from_json_schema
    """
    test_json_schema = {"if": {"const": "new"}, "then": {"const": True}, "else": {"const": False}}
    assert test_json_schema["if"] == json.loads(json.dumps(if_then_else_from_json_schema(test_json_schema, definitions).then_clause.if_clause.const))
    assert test_json_schema["then"] == json.loads(json.dumps(if_then_else_from_json_schema(test_json_schema, definitions).then_clause.const))

# Generated at 2022-06-14 14:35:21.865706
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    # Test with a value that is not equal to the default
    data = {"not": {"type": "string", "default": "default string"}}
    negated = from_json_schema(data["not"], definitions=None)
    kwargs = {"negated": negated, "default": data.get("default", NO_DEFAULT)}
    field = Not(**kwargs)
    assert not field.validate("not_default")

    # Test with a value that is equal to the default
    data = {"not": {"type": "string", "default": "default string"}}
    negated = from_json_schema(data["not"], definitions=None)
    kwargs = {"negated": negated, "default": data.get("default", NO_DEFAULT)}
    field = Not(**kwargs)
    assert field

# Generated at 2022-06-14 14:35:26.767278
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    schema = '{"$ref": "#/definitions/A"}'
    definitions = SchemaDefinitions()
    definitions["#/definitions/A"] = Field(name="A")
    field = from_json_schema(schema, definitions)
    assert field.name == "A"



# Generated at 2022-06-14 14:35:30.241447
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    test_object = {"const": "test"}
    result = const_from_json_schema(test_object, None)
    assert result != Const, "The const_from_json_schema function is not working as intended"



# Generated at 2022-06-14 14:35:37.097567
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():

    schema = {"enum" : ["dog", "cat", "fish", "rabbit"]}
    assert enum_from_json_schema(schema, definitions) == Choice(choices=[(item,item) for item in schema["enum"]])

    schema = {"enum": ["dog", "cat", "fish", "rabbit"], "default": "cat"}
    assert enum_from_json_schema(schema, definitions) == Choice(choices=[(item,item) for item in schema["enum"]], default="cat")




# Generated at 2022-06-14 14:35:44.357246
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    def test_type(type_, value):
        assert isinstance(type_(value), type_)

    def test_type_fail(type_, value):
        try:
            type_(value)
            raise AssertionError('Should be fail')
        except:
            pass

    type_ = enum_from_json_schema({'enum': ['one', 'two', 'three']}, {})
    test_type(type_, 'one')
    test_type(type_, 'two')
    test_type(type_, 'three')
    test_type_fail(type_, 'four')
    test_type_fail(type_, '')
    test_type_fail(type_, {})



# Generated at 2022-06-14 14:35:50.655591
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    schema = {
        "if": {"type": "string", "pattern": "a*"},
        "then": {"maxLength": 3},
        "else": {"maxLength": 5},
    }

    parsed = if_then_else_from_json_schema(schema, definitions={})
    evaluated = parsed("aaaaa")
    assert evaluated == {"a" * 3}

# Generated at 2022-06-14 14:36:02.915233
# Unit test for function get_valid_types
def test_get_valid_types():
    assert get_valid_types({"type": ""}) == ({}, False)
    assert get_valid_types({"type": None}) == ({}, False)
    assert get_valid_types({"type": "null"}) == ({}, True)
    assert get_valid_types({"type": ["null"]}) == ({}, True)
    assert get_valid_types({"type": "number"}) == ({"number"}, False)
    assert get_valid_types({"type": ["number"]}) == ({"number"}, False)
    assert get_valid_types({"type": "integer"}) == ({"integer"}, False)
    assert get_valid_types({"type": ["integer"]}) == ({"integer"}, False)
    assert get_valid_types({"type": "null", "maximum": 5}) == ({"number"}, False)


# Generated at 2022-06-14 14:36:09.534631
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    import tomlkit
    from .parser import parse_string
    from .printer import print_string

    schema = {
        "if": {"type": "string"},
        "then": {"type": "string"},
        "else": {"type": "number"},
    }
    field = if_then_else_from_json_schema(schema, {})

    schema_toml = print_string(field)
    # Parse into a dictionary and add "$schema", so that it can be re-parsed
    # by tomlkit without getting errors.
    schema_toml_dict = tomlkit.loads(schema_toml)
    schema_toml_dict["$schema"] = ""
    schema_toml = tomlkit.dumps(schema_toml_dict)

    assert field._sche

# Generated at 2022-06-14 14:36:57.898735
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    not_schema = {"not": {"minimum": 10}}
    assert not_from_json_schema(not_schema) == Not(negated=Integer(minimum=10))


# Generated at 2022-06-14 14:37:05.593468
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema(True) == Any()
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": ["integer", "string"]}) == (String() | Integer())
    assert from_json_schema({"enum": [1, 2]}) == Choice(choices=(1, 2))
    assert from_json_schema({"const": [1]}) == Const(value=[1])
    assert from_json_schema({"allOf": [{"const": 1}, {"type": "integer"}]}) == Const(
        value=1
    )

# Generated at 2022-06-14 14:37:11.072019
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {"$ref": "#/definitions/foo"}
    definitions = SchemaDefinitions()
    definitions["#/definitions/foo"] = String()
    field = ref_from_json_schema(data, definitions=definitions)
    assert isinstance(field, Reference)
    assert field.to == "#/definitions/foo"
    assert field.definitions == definitions



# Generated at 2022-06-14 14:37:21.290302
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    schema_json = {
            "$schema": "http://json-schema.org/draft/2019-09/schema",
            "allOf": [
                {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "integer",
                            "minimum": 5
                        }
                    },
                    "required": [
                        "a"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "b": {
                            "type": "string",
                            "minLength": 1
                        }
                    },
                    "required": [
                        "b"
                    ]
                }
            ]
        }

    assert isinstance(all_of_from_json_schema(schema_json, {}), AllOf)
    


# Generated at 2022-06-14 14:37:24.498053
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    assert type(one_of_from_json_schema({}, SchemaDefinitions())) is Field
# End unit test


# Generated at 2022-06-14 14:37:30.922946
# Unit test for function to_json_schema
def test_to_json_schema():
    definition = to_json_schema(
        Union(
            String(min_length=3, max_length=30),
            Integer(minimum=100, maximum=999),
        )
    )

    assert definition == {
        "anyOf": [
            {
                "type": "string",
                "minLength": 3,
                "maxLength": 30,
            },
            {
                "type": "integer",
                "minimum": 100,
                "maximum": 999,
            },
        ]
    }

# Generated at 2022-06-14 14:37:39.095542
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    schema = {
        "type": "object",
        "properties": {
            "not_property": {"not": {"type": "string"}},
        },
    }
    field = from_json_schema(schema)
    assert field.to_primitive() == {
        "type": "object",
        "properties": {
            "not_property": {"not": {"type": "string"}},
        },
    }



# Generated at 2022-06-14 14:37:44.360006
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {"oneOf":[{"type":"number"},{"type":"string"}]}
    definitions = SchemaDefinitions()
    f =one_of_from_json_schema(data, definitions)
    f2 = OneOf(one_of=[Float(allow_null=False),String(allow_null=False)],default=NO_DEFAULT)
    assert f == f2


# Generated at 2022-06-14 14:37:57.090570
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    expected = OneOf(
        one_of=[
            Decimal(
                minimum=1,
                maximum=10,
                exclusive_minimum=False,
                exclusive_maximum=True,
                multiple_of=2,
                default=NO_DEFAULT,
                allow_null=False,
            ),
            Decimal(
                minimum=1,
                maximum=10,
                exclusive_minimum=False,
                exclusive_maximum=True,
                multiple_of=3,
                default=NO_DEFAULT,
                allow_null=False,
            )
        ],
        default=NO_DEFAULT,
    )

# Generated at 2022-06-14 14:38:08.230996
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Integer) == {"type": "integer"}
    assert to_json_schema(Integer(min_value=5)) == {
        "type": "integer",
        "minimum": 5
    }
    assert to_json_schema(Integer(max_value=6)) == {
        "type": "integer",
        "maximum": 6
    }
    assert to_json_schema(Integer(min_value=5, max_value=6)) == {
        "type": "integer",
        "minimum": 5,
        "maximum": 6
    }
    assert to_json_schema(Float) == {"type": "number"}
    assert to_json_schema(Float(min_value=5)) == {
        "type": "number",
        "minimum": 5
    }


# Generated at 2022-06-14 14:39:08.212570
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type({}, type_string="number", allow_null=False), Number)
    assert isinstance(from_json_schema_type({}, type_string="integer", allow_null=False), Integer)
    assert isinstance(from_json_schema_type({}, type_string="string", allow_null=False), String)
    assert isinstance(from_json_schema_type({}, type_string="boolean", allow_null=False), Boolean)
    assert isinstance(from_json_schema_type({}, type_string="array", allow_null=False), Array)
    assert isinstance(
        from_json_schema_type({}, type_string="object", allow_null=False), Object
    )

# Generated at 2022-06-14 14:39:20.529901
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({}, SchemaDefinitions()) == Any()
    assert type_from_json_schema({"type": "string"}, SchemaDefinitions()) == String()
    assert type_from_json_schema({"type": "object"}, SchemaDefinitions()) == Object()
    assert type_from_json_schema({"type": "integer"}, SchemaDefinitions()) == Integer()
    assert type_from_json_schema({"type": "number"}, SchemaDefinitions()) == Number()
    assert type_from_json_schema({"type": "boolean"}, SchemaDefinitions()) == Boolean()
    assert type_from_json_schema({"type": "null"}, SchemaDefinitions()) == {
        True: Const(None), False: NeverMatch()}
    assert type_from_json_

# Generated at 2022-06-14 14:39:21.684646
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert True  # pragma: no cover



# Generated at 2022-06-14 14:39:29.165882
# Unit test for function from_json_schema
def test_from_json_schema():
    # type: () -> None
    def assert_type(data: dict, expected: Field) -> None:
        # type: (dict, Field) -> None
        actual = from_json_schema(data)
        assert actual == expected

    assert_type(
        {
            "type": "array",
            "items": {"type": "string"},
        },
        Array(items=String()),
    )
    assert_type(
        {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
            "maxItems": 10,
        },
        Array(items=String(), min_items=1, max_items=10,),
    )

# Generated at 2022-06-14 14:39:38.412389
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True).is_valid(1)
    assert from_json_schema(False).is_valid(1)
    assert not from_json_schema(False).is_valid("1")

    assert not from_json_schema({"type": "null"}).is_valid(True)
    assert not from_json_schema({"type": "null"}).is_valid(1)
    assert from_json_schema({"type": "null"}).is_valid(None)

    assert from_json_schema({"type": "integer"}).is_valid(1)
    assert not from_json_schema({"type": "integer"}).is_valid(True)
    assert not from_json_schema({"type": "integer"}).is_valid(1.1)



# Generated at 2022-06-14 14:39:48.614843
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="number").__class__ == Float
    assert from_json_schema_type({}, type_string="integer").__class__ == Integer
    assert from_json_schema_type({}, type_string="string").__class__ == String
    assert from_json_schema_type({}, type_string="boolean").__class__ == Boolean
    assert from_json_schema_type({}, type_string="array").__class__ == Array
    assert from_json_schema_type({}, type_string="object").__class__ == Object




# Generated at 2022-06-14 14:39:50.990096
# Unit test for function to_json_schema
def test_to_json_schema():

    from_json_schema(to_json_schema(String(max_length=5)))



# Generated at 2022-06-14 14:40:02.880673
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "number", "exclusiveMinimum": 1}) == Integer(
        exclusive_minimum=1
    )
    assert from_json_schema({"type": "string", "pattern": "^[A-Z]" + "*"}) == String(pattern="^[A-Z]*")
    assert from_json_schema({"type": "string", "enum": ["A", "B"]}) == Choice(
        choices=["A", "B"]
    )
    assert from_json_schema({"type": ["string", "null"]}) == Union(
        fields=[String(), None]
    )

# Generated at 2022-06-14 14:40:13.995051
# Unit test for function from_json_schema
def test_from_json_schema():
    assert type(from_json_schema(True)) == Any
    assert type(from_json_schema(False)) == NeverMatch

    schema = from_json_schema(
        {
            "allOf": [{"type": "string"}, {"minLength": 1}, {"maxLength": 10}],
        }
    )
    assert type(schema) == AllOf
    assert type(schema.properties[0]) == String
    assert type(schema.properties[1]) == Integer

    schema = from_json_schema(
        {
            "anyOf": [{"type": "string"}, {"type": "number"}],
        }
    )
    assert type(schema) == Choice
    assert type(schema.properties[0]) == String
    assert type(schema.properties[1]) == Number


# Generated at 2022-06-14 14:40:15.826666
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, "number", False, None) == Float(allow_null=False)



# Generated at 2022-06-14 14:41:50.448322
# Unit test for function from_json_schema
def test_from_json_schema():
    # TODO: add tests for all_of, any_of and one_of
    # all_of_from_json_schema()
    # any_of_from_json_schema()
    # one_of_from_json_schema()
    # if_then_else_from_json_schema()
    definitions = SchemaDefinitions()

# Generated at 2022-06-14 14:42:00.253165
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = String()
    assert to_json_schema(schema) == {"type": "string"}
    assert to_json_schema(schema, {}) == {"type": "string"}
    assert to_json_schema(schema, None) == {"type": "string"}

    schema = String(allow_null=True)
    assert to_json_schema(schema) == {"type": ["string", "null"]}

    schema = String(minimum=2)
    assert to_json_schema(schema) == {"type": "string", "minLength": 2}

    schema = String(maximum=5)
    assert to_json_schema(schema) == {"type": "string", "maxLength": 5}

    schema = String(pattern_regex=re.compile(r"\d+"))

# Generated at 2022-06-14 14:42:11.623775
# Unit test for function from_json_schema
def test_from_json_schema():
    assert isinstance(from_json_schema(False), NeverMatch)
    assert isinstance(from_json_schema(True), Any)
    assert isinstance(from_json_schema({}), Any)
    assert isinstance(from_json_schema({"type": "number"}), Float)

    assert isinstance(from_json_schema({"enum": [1, 2]}), Choice)
    assert isinstance(from_json_schema({"const": "one"}), Const)

    assert isinstance(from_json_schema({"allOf": [{"type": "number"}]}), Float)
    assert isinstance(from_json_schema({"anyOf": [{"type": "number"}]}), Float)

# Generated at 2022-06-14 14:42:22.202719
# Unit test for function to_json_schema
def test_to_json_schema():
    instance = {
        "string": "string",
        "decimal": decimal.Decimal("3.141592653589793238462643383279"),
        "integer": 1,
        "float": 3.141592653589793,
        "boolean": True,
        "array": [1, 2, 3, 4, 5],
        "object": {
            "child": True,
            "child2": "string",
            "child3": {"grandchild": False},
        },
        "choice": "b",
        "const": "a",
        "any_of": "b",
        "one_of": "two",
        "all_of": "asdf",
        "if_then_else": "a",
        "not": "a",
        "ref": "b",
    }


# Generated at 2022-06-14 14:42:34.193326
# Unit test for function to_json_schema
def test_to_json_schema():
    from pprint import pprint
    import json
    from .schema import *

    schema = Schema(
        {
            "list": Array(
                items=Object(
                    properties={"age": Integer(minimum=0, maximum=100)},
                ),
            ),
            "age": Integer(minimum=0, maximum=100),
        }
    )

    result = schema.validate({"age": -10, "list": [{"age": 20}, {"age": 30}]})
    assert len(result) == 2
    assert result[0]["path"] == ["age"]
    assert result[1]["path"] == ["list", 0, "age"]

    schema = Schema({"age": Union(Any(), Integer(minimum=0, maximum=100))})

# Generated at 2022-06-14 14:42:42.526355
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({}) == Any()
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "array"}) == Array()
    assert from_json_schema({"type": "object"}) == Object()
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": "number"}) == Number()
    assert from_json_schema({"type": "boolean"}) == Boolean()
    assert from_json_schema({"type": "null"}) == Const(None)
    assert from_json_schema({"type": "string", "maxLength": 0}) == NeverMatch()

# Generated at 2022-06-14 14:42:52.343258
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert type(from_json_schema({"type": "integer"})) == Integer
    assert type(from_json_schema({"type": "number"})) == Float
    assert type(from_json_schema({"type": "string"})) == String
    assert type(from_json_schema({"type": "boolean"})) == Boolean
    assert type(from_json_schema({"type": "object"})) == Object
    assert type(from_json_schema({"type": "array"})) == Array
    assert type(from_json_schema({"type": ["string", "number"]})) == Union



# Generated at 2022-06-14 14:43:04.017440
# Unit test for function to_json_schema
def test_to_json_schema():
    string_field = String()
    assert to_json_schema(string_field) == {"type": "string"}

    string_field = String(min_length=0, max_length=10)
    assert to_json_schema(string_field) == {
        "type": "string",
        "minLength": 0,
        "maxLength": 10,
    }

    string_field = String(min_length=None, max_length=None)
    assert to_json_schema(string_field) == {"type": "string"}

    string_field = String(pattern_regex=re.compile("^foo*"))
    assert to_json_schema(string_field) == {
        "type": "string",
        "pattern": "^foo*",
    }


# Generated at 2022-06-14 14:43:13.174264
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type({}, "null", False), Const)
    assert isinstance(from_json_schema_type({}, "number", False), Float)
    assert isinstance(from_json_schema_type({}, "integer", False), Integer)
    assert isinstance(from_json_schema_type({}, "string", False), String)
    assert isinstance(from_json_schema_type({}, "boolean", False), Boolean)
    assert isinstance(from_json_schema_type({}, "array", False), Array)
    assert isinstance(from_json_schema_type({}, "object", False), Object)



# Generated at 2022-06-14 14:43:20.539814
# Unit test for function to_json_schema