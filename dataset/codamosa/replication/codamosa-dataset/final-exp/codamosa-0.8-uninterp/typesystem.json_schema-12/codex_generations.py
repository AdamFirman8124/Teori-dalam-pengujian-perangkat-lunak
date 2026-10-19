

# Generated at 2022-06-14 14:35:35.777086
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {'allOf': [{'$ref': '#/definitions/Foo'}, {'const': 'foo'}]}
    definitions = SchemaDefinitions()
    definitions['#/definitions/Foo'] = String(max_length=1)
    field = all_of_from_json_schema(data, definitions)
    assert field.validate('foo')



# Generated at 2022-06-14 14:35:41.095288
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type({}, "string", True, None), String)
    assert isinstance(from_json_schema_type({}, "integer", True, None), Integer)
    assert isinstance(from_json_schema_type({}, "number", True, None), Float)
    assert isinstance(from_json_schema_type({}, "boolean", True, None), Boolean)
    assert isinstance(from_json_schema_type({}, "array", True, None), Array)
    assert isinstance(from_json_schema_type({}, "object", True, None), Object)



# Generated at 2022-06-14 14:35:49.948510
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {'if': {'type': 'string'}, 'then': {'type': 'string'}}
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    assert result._JSONSchema__keywords == {
        'ifClause': {'type': 'string', 'default': '<NO DEFAULT>'},
        'thenClause': {'type': 'string', 'default': '<NO DEFAULT>'},
        'elseClause': None,
        'default': '<NO DEFAULT>'
    }, result._JSONSchema__definition



# Generated at 2022-06-14 14:35:57.779014
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    from jsonasobj import as_json

    data = as_json(
        {
            "$schema": "https://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "a": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "string"}
                    }
                }
            },
            "not": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "object",
                        "properties": {
                            "a": {"type": "string"}
                        }
                    }
                },
                "required": ["a"],
            },

        }
    )
    print("Data:", data)


# Generated at 2022-06-14 14:36:03.596404
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert_expected_schema(
        IfThenElse(
            if_clause=Integer(minimum=0),
            then_clause=Integer(minimum=1),
            else_clause=Integer(minimum=2),
        ),
        {
            "if": {"minimum": 0},
            "then": {"minimum": 1},
            "else": {"minimum": 2},
        },
    )



# Generated at 2022-06-14 14:36:06.985522
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    assert not enum_from_json_schema(
        data={"enum": ["one", "two", "three"]}, definitions=SchemaDefinitions()
    ).validates(None)



# Generated at 2022-06-14 14:36:09.551142
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert IfThenElse(
        if_clause=Integer(minimum=2),
        then_clause=Integer(minimum=5),
        else_clause=Integer(minimum=10),
    ).to_json_schema() is not None



# Generated at 2022-06-14 14:36:11.130871
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {
        "oneOf": [{"type": "string", "minLength": 1}, {"type": "number"}],
    }
    one_of = one_of_from_json_schema(data, None)



# Generated at 2022-06-14 14:36:17.370166
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {
        "allOf": [{"type": "number"}, {"maximum": 100}],
        "default": 42,
    }
    field = all_of_from_json_schema(data=data, definitions=SchemaDefinitions())
    assert field.validate(value=42) == (42, None)
    assert field.validate(value=None) == (42, None)
    assert field.validate(value=101) == (101, {"maximum": 100})



# Generated at 2022-06-14 14:36:29.266771
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    # Tests 5.6.7.6
    assert(
        all_of_from_json_schema(
            {
                "$id": "x",
                "allOf": [
                    {"$ref": "y"},
                    {
                        "type": "number",
                        "minimum": 3,
                        "exclusiveMinimum": True,
                    },
                ],
            },
            definitions={
                "y": {
                    "$id": "y",
                    "type": "integer",
                    "maximum": 2,
                },
            },
        ).validate(3) == 3
    )

# Generated at 2022-06-14 14:37:07.225444
# Unit test for function to_json_schema
def test_to_json_schema():
    data = to_json_schema(String(max_length=10))
    assert "maxLength" in data

    data = to_json_schema(Integer(max_value=10))
    assert "maximum" in data

    data = to_json_schema(Float(max_value=10.0))
    assert "maximum" in data

    data = to_json_schema(Decimal(max_value=decimal.Decimal("10.0")))
    assert "maximum" in data

# Generated at 2022-06-14 14:37:18.813721
# Unit test for function from_json_schema_type

# Generated at 2022-06-14 14:37:25.061579
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(from_json_schema_type({}, type_string="number", allow_null=False), Number), ""
    assert isinstance(from_json_schema_type({}, type_string="integer", allow_null=False), Integer), ""
    assert isinstance(from_json_schema_type({}, type_string="string", allow_null=False), String), ""
    assert isinstance(from_json_schema_type({}, type_string="boolean", allow_null=False), Boolean), ""
    assert isinstance(from_json_schema_type({}, type_string="array", allow_null=False), Array), ""
    assert isinstance(from_json_schema_type({}, type_string="object", allow_null=False), Object), ""


# Generated at 2022-06-14 14:37:27.833928
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    # Given
    original = {'not': {'type': 'array'}, 'default': 5}
    # When
    result = not_from_json_schema(data=original, definitions=None)
    # Then
    assert result == Not(negated=Array(allow_null=False), default=5)


# Generated at 2022-06-14 14:37:32.825824
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = {"anyOf":[{"type":"string"},{"type":"integer"}]}
    definitions = SchemaDefinitions()
    result = any_of_from_json_schema(data, definitions)
    assert result.__class__.__name__ == "Union"
    assert result.any_of[0].__class__.__name__ == "String"
    assert result.any_of[1].__class__.__name__ == "Integer"



# Generated at 2022-06-14 14:37:45.482076
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    from typesystem import String

    json_schema = {
        "title": "Title",
        "description": "Description.",
        "default": "Pick me!",
        "anyOf": [
            {
                "type": "string",
                "title": "String",
                "description": "Description.",
                "maxLength": 10,
                "pattern": "[a-z]*",
            },
            {
                "type": "string",
                "title": "String",
                "description": "Description.",
                "maxLength": 10,
                "pattern": "[0-9]*",
            },
        ],
    }

    any_of_from_json_schema(json_schema, definitions=None)
    String(max_length=10, pattern="[a-z]*")

# Generated at 2022-06-14 14:37:58.038891
# Unit test for function to_json_schema
def test_to_json_schema():

    class IntOrNull(Union):
        integer: Integer
        null: Field = field(default=None)

    class Addr(Field):
        line: Field = field(default="")
        zip: Field = field(default="")

    class Dog(Field):
        name: Field = field(default="")
        age: Field = field(default="")
        addr: Field = field(default=None)

    class AdoptsDog(Field):
        name: Field = field(default="")
        addr: Field = field(default=None)
        dog: Field = field(default=None)

    class Person(Field):
        name: Field = field(default="")
        age: field(default="")
        addr: Field = field(default=None)
        adopts_dog: Field = field(default=None)


# Generated at 2022-06-14 14:38:05.567107
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert type_string_to_field.get("number", None) is Float
    assert type_string_to_field.get("integer", None) is Integer
    assert type_string_to_field.get("string", None) is String
    assert type_string_to_field.get("boolean", None) is Boolean
    assert type_string_to_field.get("array", None) is Array
    assert type_string_to_field.get("object", None) is Object


# Generated at 2022-06-14 14:38:14.455818
# Unit test for function to_json_schema
def test_to_json_schema():
    from marshmallow.fields import String, Decimal, Choice
    from marshmallow import ValidationError
    from marshmallow.schema import Schema


# Generated at 2022-06-14 14:38:21.379278
# Unit test for function to_json_schema
def test_to_json_schema():
    # Simple
    json = to_json_schema(String())
    assert json == {"type": "string"}
    json = to_json_schema(Integer())
    assert json == {"type": "integer"}
    json = to_json_schema(Boolean())
    assert json == {"type": "boolean"}
    json = to_json_schema(Any())
    assert json is True
    json = to_json_schema(NeverMatch())
    assert json is False

    # Optional
    json = to_json_schema(String(allow_null=True))
    assert json == {"type": ["string", "null"]}

    # MultipleOf
    json = to_json_schema(Integer(multiple_of=3))
    assert json == {"type": "integer", "multipleOf": 3}

# Generated at 2022-06-14 14:39:00.291310
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert str(from_json_schema_type({}, "number", False, None)) == "Float"
    assert str(from_json_schema_type({}, "integer", False, None)) == "Integer"
    assert str(from_json_schema_type({}, "string", False, None)) == "String"
    assert str(from_json_schema_type({}, "boolean", False, None)) == "Boolean"
    assert str(from_json_schema_type({}, "array", False, None)) == "Array"
    assert str(from_json_schema_type({}, "object", False, None)) == "Object"



# Generated at 2022-06-14 14:39:12.924543
# Unit test for function to_json_schema

# Generated at 2022-06-14 14:39:24.705131
# Unit test for function from_json_schema
def test_from_json_schema():
    assert Any() == from_json_schema(True)
    assert Any() == from_json_schema({"type": "string"})
    assert Any() == from_json_schema({"type": ["string", "number"]})
    assert Any() == from_json_schema({"enum": ["foo", "bar"]})
    assert Any() == from_json_schema({"$ref": "#/definitions/foo"})
    assert Any() == from_json_schema({"$ref": "#/definitions/foo", "enum": ["foo", "bar"]})

# Generated at 2022-06-14 14:39:36.247042
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem import Schema


# Generated at 2022-06-14 14:39:46.116442
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    for type_string in {"number", "integer", "string", "boolean", "array", "object"}:
        from_json_schema_type({"type": type_string}, type_string, False, None)
    from_json_schema_type({"type": "null"}, "null", True, None)
    from_json_schema_type({"type": {"anyOf": ["null", "string"]}}, "null", True, None)
    from_json_schema_type({"type": {"anyOf": ["null", "string"]}}, "string", False, None)



# Generated at 2022-06-14 14:39:54.544249
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False

    assert to_json_schema(Integer(allow_null=True, minimum=0, maximum=100)) == {
        "type": ["integer", "null"],
        "minimum": 0,
        "maximum": 100
    }

    assert to_json_schema(Float(allow_null=True, minimum=5.5)) == {
        "type": ["number", "null"],
        "minimum": 5.5
    }


# Generated at 2022-06-14 14:40:05.408350
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema({"const": 1}) == Const(1)
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"enum": [1, 2, 3]}) == Choice([1, 2, 3])
    assert from_json_schema({"allOf": [{"type": "string"}, {"enum": [1, 2, 3]}]}) == String(
        choices=[1, 2, 3]
    )
    assert from_json_schema({"not": {"type": "string"}}) == Not(String())

# Generated at 2022-06-14 14:40:15.853942
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String()) == {
        "type": "string",
        "default": "",
        "minLength": 0,
    }

    assert to_json_schema(Integer()) == {
        "type": "integer",
        "default": 0,
        "minimum": -sys.maxsize - 1,
        "exclusiveMinimum": False,
    }

    assert to_json_schema(AllOf([String(), Integer()])) == {
        "allOf": [
            {"type": "string", "default": "", "minLength": 0},
            {"type": "integer", "default": 0, "minimum": -sys.maxsize - 1, "exclusiveMinimum": False},
        ],
        "default": "",
        "minLength": 0,
    }


# Generated at 2022-06-14 14:40:21.934835
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert type_from_json_schema(data={
        "type": "number",
    }, definitions=SchemaDefinitions()) == Float()
    assert type_from_json_schema(data={
        "type": "integer",
    }, definitions=SchemaDefinitions()) == Integer()
    assert type_from_json_schema(data={
        "type": "string",
    }, definitions=SchemaDefinitions()) == String()
    assert type_from_json_schema(data={
        "type": "boolean",
    }, definitions=SchemaDefinitions()) == Boolean()
    assert type_from_json_schema(data={
        "type": "array",
    }, definitions=SchemaDefinitions()) == Array()

# Generated at 2022-06-14 14:40:25.053515
# Unit test for function to_json_schema
def test_to_json_schema():
    field = Integer(maximum=100, default=42)
    definition = {"field": field}
    assert to_json_schema(definition) == {
        "definitions": {
            "field": {
                "maximum": 100,
                "default": 42,
                "type": "integer",
            }
        }
    }

# Generated at 2022-06-14 14:40:51.800569
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert Boolean({}) == from_json_schema_type({}, type_string="boolean", allow_null=False)
    assert Boolean(allow_null=True) == from_json_schema_type(
        {}, type_string="boolean", allow_null=True
    )
    assert String({}) == from_json_schema_type({}, type_string="string", allow_null=False)
    assert String(allow_null=True) == from_json_schema_type(
        {}, type_string="string", allow_null=True
    )
    assert Integer({}) == from_json_schema_type({}, type_string="integer", allow_null=False)

# Generated at 2022-06-14 14:41:05.050459
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    data = {
        "if": {
            "type": "object",
            "properties": {
                "owner": {"type": "string", "minLength": 10, "maxLength": 20}
            },
            "required": ["owner"],
            "additionalProperties": False,
        },
        "then": {"type": "string", "minLength": 10, "maxLength": 20},
        "else": {"type": "string", "minLength": 10, "maxLength": 30},
    }
    definitions = SchemaDefinitions()
    definitions["#/definitions/JSONSchema"] = JSONSchema
    schema_obj = from_json_schema(data, definitions=definitions)
    assert isinstance(
        schema_obj, Field
    )  # type:ignore # should be ignored in type checking
    assert schema_

# Generated at 2022-06-14 14:41:10.578490
# Unit test for function to_json_schema
def test_to_json_schema():
    inpt = {
        "type": "object",
        "properties": {"base64_data": {"type": "string", "format": "base64"}}
    }
    out = to_json_schema(from_json_schema(inpt))
    assert out == inpt



# Generated at 2022-06-14 14:41:20.535724
# Unit test for function to_json_schema
def test_to_json_schema():
    data_0 = to_json_schema(Any())
    data_1 = to_json_schema(NeverMatch())
    data_2 = to_json_schema(Integer())
    data_3 = to_json_schema(String())
    data_4 = to_json_schema(String(min_length=1))
    data_5 = to_json_schema(String(pattern="\\d+"))
    data_6 = to_json_schema(String(format="ipv4"))
    data_7 = to_json_schema(String(format="ipv4").default())
    data_8 = to_json_schema(Array(String()))
    data_9 = to_json_schema(Array(String().default(), unique_items=True))
    data_10 = to_json_

# Generated at 2022-06-14 14:41:31.261111
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"type": "array"}) == Array()
    assert from_json_schema({"type": "string", "minLength": 2}) == String(min_length=2)
    assert from_json_schema({"type": "string", "enum": ["FOO", "BAR"]}) == String(enum=["FOO", "BAR"])
    assert from_json_schema({"allOf": [{"type": "string"}, {"minLength": 2}]}) == String(min_length=2)
    assert from_json_schema({"anyOf": [{"type": "string"}, {"minLength": 2}]}) == String()

# Generated at 2022-06-14 14:41:38.194628
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from_json_schema_type({}, type_string="string", allow_null=True, definitions=None)
    from_json_schema_type({}, type_string="string", allow_null=False, definitions=None)
    from_json_schema_type(
        {},
        type_string="string",
        allow_null=False,
        definitions=SchemaDefinitions(),
    )



# Generated at 2022-06-14 14:41:48.008272
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    for type_string in ("number", "integer", "string", "boolean", "array", "object"):
        field = from_json_schema_type(
            data={"type": type_string},
            type_string=type_string,
            allow_null=False,
            definitions=SchemaDefinitions(),
        )
        assert isinstance(field, Field)
        field.validate(None)

    with pytest.raises(AssertionError):
        # noinspection PyTypeChecker
        from_json_schema_type(
            data={}, type_string="invalid", allow_null=False, definitions=SchemaDefinitions()
        )



# Generated at 2022-06-14 14:41:54.414880
# Unit test for function to_json_schema
def test_to_json_schema():
    path = './data/config.json'
    with open(path, 'r') as f:
        data = json.load(f)

    obj_schema = from_json_schema(data)
    json_schema = to_json_schema(obj_schema)
    # print(json.dumps(json_schema))


# Generated at 2022-06-14 14:42:02.064179
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Schema(
        fields={
            "name": Field(
                "string",
                max_length=100,
                required=True,
                nullable=False,
                allow_blank=False,
                pattern_regex=re.compile("[A-Za-z0-9]+"),
            )
        }
    )
    target = {
        "definitions": {
            "name": {
                "type": "string",
                "maxLength": 100,
                "required": True,
                "pattern": "[A-Za-z0-9]+",
            }
        }
    }
    assert to_json_schema(schema) == target



# Generated at 2022-06-14 14:42:13.752985
# Unit test for function from_json_schema
def test_from_json_schema():
    schema = {
        "$ref": "#/definitions/Pet",
        "type": "object",
        "enum": [
            {
                "name": "Tiddles",
                "type": "Cat"
            },
            {
                "name": "Fido",
                "type": "Dog"
            }
        ],
        "definitions": {
            "Pet": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "type": {
                        "enum": [
                            "Dog",
                            "Cat"
                        ]
                    }
                }
            }
        }
    }
    result = from_json_schema(schema)

# Generated at 2022-06-14 14:42:39.114870
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(SchemaDefinitions({"a": String(), "b": Integer()})) == {
        "definitions": {
            "a": {"type": "string"},
            "b": {"type": "integer"},
        }
    }


# Generated at 2022-06-14 14:42:48.308404
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    schema = {
        "type": "object",
        "details": {"type": "boolean"},
        "address": {"type": "string", "nullable": True},
        "price": {"type": "number", "exclusiveMinimum": 0.0},
    }

    # The Object `properties` argument should accept
    #  a nested dictionary of key/value pairs.

    field = from_json_schema(schema)

    assert isinstance(field, Object)
    assert field.properties["details"].python_type == bool
    assert field.properties["address"].allow_null



# Generated at 2022-06-14 14:42:50.738587
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()



# Generated at 2022-06-14 14:42:58.563195
# Unit test for function to_json_schema
def test_to_json_schema():
    from .serialize import to_json_schema
    from .case import case

    @case({}, {"type": "object"}, doc="Empty object")
    @case(True, {"type": "boolean"}, doc="Boolean field")
    @case(
        {"required": True},
        {"type": "boolean", "default": False, "required": True},
        doc="Boolean field with additional data",
    )
    def test_boolean_field(field: Boolean, output: dict):
        assert to_json_schema(field) == output


# Generated at 2022-06-14 14:43:04.938211
# Unit test for function to_json_schema
def test_to_json_schema():
    validator = (
        Object(
            properties={
                "a": AllOf(
                    all_of=[
                        String(min_length=1, max_length=3),
                        Object(
                            properties={
                                "c": Integer(minimum=0),
                                "d": (
                                    Number(minimum=0, exclusive_minimum=True)
                                    | Number(minimum=5)
                                ),
                            }
                        ),
                    ]
                ),
                "b": (Not(String(min_length=1, max_length=3))),
            }
        )
    )


# Generated at 2022-06-14 14:43:15.422893
# Unit test for function to_json_schema
def test_to_json_schema():
    from .string import PatternString
    from .utils import Number
    from .core import make_schema
    from .object import Property, PatternProperty


# Generated at 2022-06-14 14:43:22.626554
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    # pylint: disable=redefined-outer-name
    from typesystem.schemas import SchemaDefinitions
    from typesystem.types import Array, Boolean, Integer, Object, String

    data = {
        "type": "number",
        "minimum": 1,
        "maximum": 9,
        "exclusiveMinimum": False,
        "exclusiveMaximum": False,
        "multipleOf": 1,
    }
    field = from_json_schema_type(
        data, type_string="number", allow_null=False, definitions=SchemaDefinitions()
    )
    assert field.to_primitive() == {
        "type": "number",
        "minimum": 1,
        "maximum": 9,
        "exclusiveMinimum": False,
        "exclusiveMaximum": False,
        "multipleOf": 1,
    }

# Generated at 2022-06-14 14:43:32.479655
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="string", allow_null=True) == String(
        allow_null=True
    )
    assert from_json_schema_type({}, type_string="string", allow_null=False) == String()
    assert from_json_schema_type({}, type_string="integer", allow_null=True) == Integer(
        allow_null=True
    )
    assert from_json_schema_type({}, type_string="integer", allow_null=False) == Integer()
    assert from_json_schema_type({}, type_string="number", allow_null=True) == Number(
        allow_null=True
    )
    assert from_json_schema_type({}, type_string="number", allow_null=False) == Number()
   

# Generated at 2022-06-14 14:43:43.355174
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Optional(String())) == {
        "type": ["string", "null"]
    }

    assert to_json_schema(Optional(String(default="foo"))) == {
        "type": ["string", "null"],
        "default": "foo",
    }

    assert to_json_schema(
        String(min_length=1, max_length=10, pattern_regex=re.compile("^[a-z]+$"))
    ) == {
        "type": "string",
        "minLength": 1,
        "maxLength": 10,
        "pattern": "^[a-z]+$"
    }


# Generated at 2022-06-14 14:43:50.478420
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert isinstance(type_from_json_schema({}, definitions={}), Any)
    assert isinstance(type_from_json_schema({"type": "null"}, definitions={}), Const)
    assert isinstance(
        type_from_json_schema({"type": "integer"}, definitions={}), Integer
    )
    assert isinstance(
        type_from_json_schema({"type": "number"}, definitions={}), Number
    )
    assert isinstance(
        type_from_json_schema({"type": "boolean"}, definitions={}), Boolean
    )
    assert isinstance(
        type_from_json_schema({"type": "string"}, definitions={}), String
    )