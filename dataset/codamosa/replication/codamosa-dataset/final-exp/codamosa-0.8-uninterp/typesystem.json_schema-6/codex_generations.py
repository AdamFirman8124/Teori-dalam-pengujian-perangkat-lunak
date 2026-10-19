

# Generated at 2022-06-14 14:35:30.852484
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    f = const_from_json_schema({"const": 1}, None)
    assert f.validate(1) is None
    assert f.validate(2) is NotImplemented


# Generated at 2022-06-14 14:35:34.396878
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {"$ref": "#/definitions/foo"}
    definitions = {"#/definitions/foo": String()}
    assert ref_from_json_schema(data, definitions=definitions).to_json_schema() == data



# Generated at 2022-06-14 14:35:37.777455
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert isinstance(if_then_else_from_json_schema(
        {'if': {'type': 'string'}, 'then': {'type': 'integer'}},
        SchemaDefinitions()
    ), IfThenElse)
    assert if_then_else_from_json_schema(
        {'if': {'type': 'string'}, 'then': {'type': 'integer'}},
        SchemaDefinitions()
    ).then_clause.field.Fields.type == 'integer'



# Generated at 2022-06-14 14:35:44.019256
# Unit test for function from_json_schema
def test_from_json_schema():
    field = from_json_schema(
        {
            "$ref": "#/definitions/person",
            "definitions": {
                "person": {
                    "type": "object",
                    "properties": {
                        "age": {"type": "integer", "minimum": 0},
                        "name": {"type": "string", "maxLength": 255},
                    },
                }
            },
        }
    )
    assert isinstance(field, Reference)
    assert isinstance(field.schema, Object)
    assert isinstance(field.schema["age"], Integer)
    assert isinstance(field.schema["name"], String)



# Generated at 2022-06-14 14:35:47.285178
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    json_string = '{"$ref": "#/definitions/Person"}'
    from_json_schema(json_string)
    pass



# Generated at 2022-06-14 14:35:59.703384
# Unit test for function get_valid_types
def test_get_valid_types():
    #test1: null, boolean
    data = {"type":"null"}
    assert(get_valid_types(data) == (set(["boolean"]), True))
    #test2: string
    data = {"type":"string"}
    assert(get_valid_types(data) == (set(["string"]), False))
    #test3: integer, string
    data = {"type":["integer", "string"]}
    assert(get_valid_types(data) == (set(["string"]), False))
    #test4: null, integer, number
    data = {"type":["null", "integer", "number"]}
    assert(get_valid_types(data) == (set(["number"]), True))
    #test5: number
    data = {"type":"number"}

# Generated at 2022-06-14 14:36:03.548197
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    with pytest.raises(AssertionError):
        one_of_from_json_schema({}, None)

    assert len(one_of_from_json_schema({"oneOf": []}, None).one_of) == 0



# Generated at 2022-06-14 14:36:13.009904
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({
        "type": "string",
        "minLength": 1,
        "maxLength": 3,
    }) == String(
        min_length=1,
        max_length=3,
        allow_blank=False
    )
    assert type_from_json_schema({
        "type": "string",
        "minLength": 1,
        "maxLength": 3,
        "allow_blank": True,
    }) == String(
        min_length=1,
        max_length=3,
        allow_blank=True
    )
    assert type_from_json_schema({
        "type": "string",
        "allow_blank": True,
    }) == String(allow_blank=True)

# Generated at 2022-06-14 14:36:24.367896
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    data = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "minLength": 1
            },
            "age": {
                "type": "integer",
                "const": {
                    "type": "integer"
                }
            },
            "gender": {
                "type": "string",
                "default": "M",
                "const": "M"
            }
        }
    }
    definitions = SchemaDefinitions()
    assert Const(const="M") == const_from_json_schema(data["properties"]["gender"], definitions)


# Generated at 2022-06-14 14:36:28.180762
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    ref = Reference("abc/def")
    assert ref_from_json_schema({"$ref": "#/definitions/abc/def"}, definitions={ref}) == ref
    assert ref_from_json_schema({"$ref": "abc/def"}, definitions={ref}) == ref



# Generated at 2022-06-14 14:37:12.766943
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    data = dict(anyOf=[{"type": "string"}, {"type":"integer"}], default="foobar")
    definitions = SchemaDefinitions()
    assert any_of_from_json_schema(data, definitions=definitions) == \
        Union(any_of=[String(), Integer()], default='foobar')



# Generated at 2022-06-14 14:37:16.844761
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({}) == Any()
    assert from_json_schema({'type': 'object'}) == Object()
    assert from_json_schema({'type': 'string', 'minLength': 2}) == String(min_length=2)

# Generated at 2022-06-14 14:37:20.415814
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    schema = {"enum": ["one", "two"]}

    field = enum_from_json_schema(schema, definitions=SchemaDefinitions())
    assert field.validate("one")
    assert field.validate("two")
    assert not field.validate("three")



# Generated at 2022-06-14 14:37:25.213016
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    schema = {"enum": [0]}
    field = enum_from_json_schema(schema, definitions=SchemaDefinitions())
    assert field.validate(0) is True
    assert field.validate(1) is False


# Generated at 2022-06-14 14:37:33.878575
# Unit test for function to_json_schema
def test_to_json_schema():
    data = {
        "definitions": {
            "string_pattern": {"type": "string", "pattern": "foo"},
            "string_choices": {
                "type": ["string", "null"],
                "enum": ["foo", "baz", "bar"],
            },
        },
        "properties": {
            "name": {"type": "string"},
            "foo": {"$ref": "#/definitions/string_pattern"},
            "bar": {"$ref": "#/definitions/string_choices"},
        },
        "required": ["name", "foo", "bar"],
    }

    class Schema(SchemaDefinitions):
        name = String(required=True)
        foo = Reference(to=String(pattern_regex=re.compile("foo")), required=True)

# Generated at 2022-06-14 14:37:40.228064
# Unit test for function from_json_schema
def test_from_json_schema():
    assert {
        "$ref": "#/definitions/Defined",
    } == to_json_schema(from_json_schema({
        "definitions": {
            "Defined": {"type": "string"},
        },
        "$ref": "#/definitions/Defined",
    }))



# Generated at 2022-06-14 14:37:43.861128
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    assert isinstance(
        one_of_from_json_schema({"oneOf": [{"$ref": "#/definitions/#"}, {"$ref": "#/definitions/string"}]}, definitions),
        (OneOf, TypeError))==True


# Generated at 2022-06-14 14:37:51.684168
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "enum": ["fred", "freddy"],
        "type": "string",
    }
    field = from_json_schema(schema)
    assert isinstance(field, Field)
    assert isinstance(field, Choice)
    assert field.choices == [("fred", "fred"), ("freddy", "freddy")]



# Generated at 2022-06-14 14:38:01.497741
# Unit test for function to_json_schema
def test_to_json_schema():
    def schema_from_json_schema(
        data: dict, _definitions: SchemaDefinitions = None
    ) -> Field:
        definitions = {} if _definitions is None else _definitions
        return from_json_schema(data, definitions=definitions)


# Generated at 2022-06-14 14:38:07.619802
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {"oneOf": [{"type": "string"}, {"type": "integer"}]}
    definitions = SchemaDefinitions()
    field = one_of_from_json_schema(data=data, definitions=definitions)
    assert field.validate("test") is None
    assert field.validate(9) is None
    assert field.validate(1.2) == {"const": "Invalid literal for int() with base 10: '1.2'"}



# Generated at 2022-06-14 14:39:06.119838
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema({"allOf": [{"type": "string"}, {"type": "string"}]}, definitions)


# Generated at 2022-06-14 14:39:18.415832
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert all_of_from_json_schema({"allOf": [{"type": "number"}, {"type": "string"}]}, {}) == AllOf(all_of=[Float(allow_null=False), String(allow_null=False)])
    assert all_of_from_json_schema({"allOf": [{"type": "integer"}, {"type": "string"}]}, {}) == AllOf(all_of=[Integer(allow_null=False), String(allow_null=False)])
    assert all_of_from_json_schema({"allOf": [{"type": "number"}, {"type": "object"}]}, {}) == AllOf(all_of=[Float(allow_null=False), Object(allow_null=False)])

# Generated at 2022-06-14 14:39:27.723406
# Unit test for function from_json_schema
def test_from_json_schema():
    # Boolean
    assert from_json_schema(True).validate(True) is None
    assert from_json_schema(False).validate(True) != None

    # Enum
    assert from_json_schema({"enum": ["a", "b", "c"]}).validate("a") is None
    assert from_json_schema({"enum": ["a", "b", "c"]}).validate("d") != None

    # Const
    assert from_json_schema({"const": 10}).validate(10) is None
    assert from_json_schema({"const": 10}).validate(5) != None

    # Not
    assert from_json_schema({"not": {"type": "string"}}).validate(5) is None
    assert from_json_schema

# Generated at 2022-06-14 14:39:34.980548
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {"not": {"type": "string", "minLength": 1, "maxLength": 10}}
    assert not_from_json_schema(data, None)._negated.max_length == 10
    data = {"not": {"type": "string", "minLength": 1, "maxLength": 10, "default": "hello"}}
    assert not_from_json_schema(data, None)._negated.max_length == 10
    assert not_from_json_schema(data, None).default == "hello"



# Generated at 2022-06-14 14:39:41.802597
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(False) == NeverMatch()
    assert from_json_schema(True) == Any()
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "array", "items": {"type": "string"}}) == Array(
        items=String()
    )
    assert from_json_schema({"type": "string", "enum": ["red", "green", "blue"]}) == Choice(
        options=["red", "green", "blue"]
    )
    assert from_json_schema({"const": "red"}) == Const("red")
    assert from_json_schema({"allOf": [{"type": "string"}]}) == String()

# Generated at 2022-06-14 14:39:52.423952
# Unit test for function to_json_schema
def test_to_json_schema():
    from .base import Castable


# Generated at 2022-06-14 14:40:04.029671
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {"anyOf":[{"const":1,"default":1},{"const":2},{"number":{"minimum":3}}]}
    definitions = {}
    data = {"not": {"allOf": [{"anyOf":[{"const":1,"default":1},{"const":2},{"number":{"minimum":3}}]}]}}
    result = not_from_json_schema(data, definitions)
    assert result.get_context_value("default") == data.get("default", NO_DEFAULT)
    assert result.get_context_value("negated").default == data["not"]["allOf"][0]["anyOf"][0].get("default", NO_DEFAULT)

# Generated at 2022-06-14 14:40:11.083011
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    import json
    with open("all_of.json") as f:
        data = json.load(f)

        all_of = [from_json_schema(item, definitions=definitions) for item in data["allOf"]]
        kwargs = {"all_of": all_of, "default": data.get("default", NO_DEFAULT)}
        AllOf(**kwargs)

test_all_of_from_json_schema()


# Generated at 2022-06-14 14:40:12.147688
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    pass
    # Not()


# Generated at 2022-06-14 14:40:19.824263
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String) == {"type": "string"}
    assert to_json_schema(Integer) == {"type": "integer"}
    assert to_json_schema(Float) == {"type": "number"}
    assert to_json_schema(Boolean) == {"type": "boolean"}
    assert to_json_schema(Array) == {"type": "array"}
    assert to_json_schema(Object) == {"type": "object"}

    assert to_json_schema(String(allow_null=True)) == {"type": "string"}
    assert to_json_schema(Integer(allow_null=True)) == {"type": "integer"}
    assert to_json_schema(Float(allow_null=True)) == {"type": "number"}
    assert to_json_schema

# Generated at 2022-06-14 14:41:07.227330
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    type_field = from_json_schema_type({"type": "integer"},type_string="integer",allow_null=False,definitions=None)



# Generated at 2022-06-14 14:41:18.873197
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    json_schema_dict = {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/definitions/id"
        }
      },
      "required": ["id"],
      "definitions": {
        "id": {
          "if": {
            "type": "string",
            "maxLength": 255,
            "format": "uuid"
          },
          "then": {
            "const": "uuid"
          },
          "else": {
            "type": "string",
            "maxLength": 100,
            "pattern": "[a-zA-Z0-9_-]+"
          }
        }
      }
    }
    field = from_json_schema(json_schema_dict)

# Generated at 2022-06-14 14:41:25.376369
# Unit test for function from_json_schema_type
def test_from_json_schema_type(): # type: ignore
    assert from_json_schema_type({}, type_string="boolean", allow_null=False).to_json_schema() == {
        "type": "boolean"
    }
    assert from_json_schema_type({}, type_string="boolean", allow_null=True).to_json_schema() == {
        "type": ["boolean", "null"]
    }



# Generated at 2022-06-14 14:41:34.451496
# Unit test for function to_json_schema
def test_to_json_schema():
    field = AllOf(
        Any(),
        Not(Any()),
        IfThenElse(
            Any(),
            Any(if_clause=Any()),
            Any(if_clause=Any(then_clause=Any()), else_clause=Any()),
        ),
    )
    schema = to_json_schema(field)

    expected = {
        "allOf": [
            True,
            {"not": True},
            {
                "if": True,
                "then": True,
                "else": {
                    "if": True,
                    "then": {"if": True, "then": None},
                    "else": {
                        "if": True,
                        "then": None,
                        "else": True,
                    },
                },
            },
        ]
    }
    assert schema

# Generated at 2022-06-14 14:41:36.581179
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from_json_schema_type(data=None, type_string=None, allow_null=True, definitions=None)
    from_json_schema_type(data=None, type_string=None, allow_null=False, definitions=None)

# Generated at 2022-06-14 14:41:47.361663
# Unit test for function to_json_schema
def test_to_json_schema():
    
    old_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "http://example.com/product.schema.json",
        "title": "Product",
        "type": "object",
        "properties": {
            "productId": {
                "description": "The unique identifier for a product",
                "type": "integer"
            }
        },
        "required": ["productId"]
    }
    
    from_old_schema = from_json_schema(old_schema)
    new_schema = to_json_schema(from_old_schema)
    assert new_schema == old_schema
    
 
# Unit tests for overall parser

# Generated at 2022-06-14 14:41:58.572271
# Unit test for function to_json_schema
def test_to_json_schema():
    class Person(Schema):
        name = String()
        age = Integer()
        is_female = Boolean()

    class Animal(Schema):
        name = String()
        owner = Reference(to=Person)
        num_legs = Integer(minimum=0, maximum=4)
        num_heads = Integer(minimum=0)

    schema = Animal()
    d = to_json_schema(schema)

# Generated at 2022-06-14 14:42:09.616041
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False

    # String
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(String(allow_null=True)) == {"type": ["string", "null"]}
    assert to_json_schema(String(min_length=5)) == {"type": "string", "minLength": 5}
    assert to_json_schema(String(max_length=10)) == {"type": "string", "maxLength": 10}
    assert to_json_schema(String(allow_blank=False)) == {
        "type": "string",
        "minLength": 1,
    }

# Generated at 2022-06-14 14:42:20.355241
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    f = if_then_else_from_json_schema({'if': {
        'const': 1
    }, 'then': {
        'const': 2
    }, 'else': {
        'const': 3
    }}, SchemaDefinitions())
    assert f.default == NO_DEFAULT
    assert f.if_clause.default == NO_DEFAULT
    assert f.if_clause.const == 1
    assert f.then_clause.default == NO_DEFAULT
    assert f.then_clause.const == 2
    assert f.else_clause.default == NO_DEFAULT
    assert f.else_clause.const == 3
    assert f(1) == 2
    assert f(4) == 3
    assert not f.is_empty()

# Generated at 2022-06-14 14:42:27.349158
# Unit test for function to_json_schema
def test_to_json_schema():

    class NameSchema(Schema):
        first = String(min_length=1)
        last = String(min_length=1)

    class PasswordSchema(Schema):
        password = String(format=StringFormat.PASSWORD)
        password_confirm = String(format=StringFormat.PASSWORD)

    class UserSchema(Schema):
        name = NameSchema()
        email = String(format=StringFormat.EMAIL_ADDRESS)
        age = Integer(minimum=13, maximum=120)
        admin = Boolean(default=False)
        status = Choice(choices=[("pending", "pending"), ("active", "active")])
        password = PasswordSchema()

        class Meta:
            with_defaults = False

    class RootSchema(Schema):
        value = UserSchema()

# Generated at 2022-06-14 14:42:57.586173
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(
        from_json_schema_type(
            data={"type": "integer"}, type_string="integer", allow_null=False, definitions=None
        ),
        Integer,
    )
    assert isinstance(
        from_json_schema_type(
            data={"type": "integer", "default": 1},
            type_string="integer",
            allow_null=False,
            definitions=None,
        ),
        Integer,
    )
    assert isinstance(
        from_json_schema_type(
            data={"type": "integer"}, type_string="integer", allow_null=True, definitions=None
        ),
        Integer,
    )


# Generated at 2022-06-14 14:43:07.989787
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    field = type_from_json_schema(
        {
            "type": "string",
            "minLength": 5,
            "maxLength": 10,
            "pattern": "^[0-9]",
            "format": "date-time",
        },
        definitions=None,
    )
    assert field.to_json_schema() == {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "",
        "definitions": {},
        "type": "string",
        "format": "date-time",
        "minLength": 5,
        "maxLength": 10,
        "pattern": "^[0-9]",
    }



# Generated at 2022-06-14 14:43:17.220900
# Unit test for function to_json_schema

# Generated at 2022-06-14 14:43:23.701225
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    # Test some basic cases
    assert from_json_schema_type({"type": "string"}, type_string="string", allow_null=False) == String()
    assert from_json_schema_type({"type": "integer"}, type_string="integer", allow_null=False) == Integer()
    assert from_json_schema_type({"type": "number"}, type_string="number", allow_null=False) == Float()
    assert from_json_schema_type({"type": "boolean"}, type_string="boolean", allow_null=False) == Boolean()
    assert from_json_schema_type({"type": "array"}, type_string="array", allow_null=False) == Array()

# Generated at 2022-06-14 14:43:33.121383
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    definitions = SchemaDefinitions()

    assert from_json_schema_type({}, type_string="string", allow_null=False, definitions=definitions) == String()
    assert from_json_schema_type({}, type_string="array", allow_null=False, definitions=definitions) == Array()
    assert from_json_schema_type({}, type_string="object", allow_null=False, definitions=definitions) == Object()
    assert from_json_schema_type({}, type_string="number", allow_null=False, definitions=definitions) == Float()
    assert from_json_schema_type({}, type_string="integer", allow_null=False, definitions=definitions) == Integer()

# Generated at 2022-06-14 14:43:43.654150
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Schema(
        name=String(max_length=5),
        age=Integer(min=0, max=200),
        is_human=Boolean(default=False),
        address=String(),
        family_size=Integer(min=1),
        profession=Choice(
            choices=[
                ("doctor", "doctor"),
                ("nurse", "nurse"),
                ("teacher", "teacher"),
            ]
        ),
    )
    as_json = to_json_schema(schema)
    name = as_json["definitions"]["#/properties/name"]
    assert name == {
        "type": "string",
        "maxLength": 5,
    }
    age = as_json["definitions"]["#/properties/age"]

# Generated at 2022-06-14 14:43:52.414572
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert {
        "string": (String, {}),
        "integer": (Integer, {}),
        "number": (Integer, {}),
        "object": (Object, {}),
        "array": (Array, {"unique_items": False}),
        "boolean": (Boolean, {}),
    } == {
        type_string: (from_json_schema_type(dict(type=type_string), type_string).__class__, from_json_schema_type(dict(type=type_string), type_string).json_schema)
        for type_string in ["string", "integer", "number", "object", "array", "boolean"]
    }


# Generated at 2022-06-14 14:43:58.518316
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({}, definitions=SchemaDefinitions()) == Any()
    assert (
        type_from_json_schema({"type": "string"}, definitions=SchemaDefinitions())
        == String()
    )
    assert (
        type_from_json_schema({"type": "string", "nullable": True}, definitions=SchemaDefinitions())
        == String(allow_null=True)
    )
    assert (
        type_from_json_schema({"type": "string", "nullable": True}, definitions=SchemaDefinitions())
        == String(allow_null=True)
    )

# Generated at 2022-06-14 14:44:08.859084
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    """
    Test that function type_from_json_schema can convert JSON schemas of type
    'object' to typesystem.Object, and for all the basic types it can convert
    JSON schemas of type 'number', 'string', 'boolean' to the correct types.
    """
    from typesystem.composites import Not
    from typesystem.fields import Array, Integer, Object, String, Union
    from typesystem.schemas import Reference
    # Test that schemas of type 'object' can be converted to Object
    schema_obj = {"type": "object"}
    assert type(type_from_json_schema(schema_obj)) is Object
    # Test that schemas of type 'string' can be converted to String
    schema_str = {"type": "string"}

# Generated at 2022-06-14 14:44:20.308811
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="number", allow_null=False,\
        definitions={}) == Float(allow_null=False, allow_infinity=True,\
            minimum=None, maximum=None, exclusive_minimum=None,\
            exclusive_maximum=None, multiple_of=None, default=NO_DEFAULT)
    assert from_json_schema_type({}, type_string="integer", allow_null=False,\
        definitions={}) == Integer(allow_null=False, minimum=None,\
            maximum=None, exclusive_minimum=None, exclusive_maximum=None,\
            multiple_of=None, default=NO_DEFAULT)