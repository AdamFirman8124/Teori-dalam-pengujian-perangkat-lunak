

# Generated at 2022-06-14 14:35:02.972304
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {"$ref": "#/definitions/my_def"}
    reference_string = data["$ref"]
    assert reference_string.startswith("#/"), "Unsupported $ref style in document."
    assert reference_string == "#/definitions/my_def"
test_ref_from_json_schema()



# Generated at 2022-06-14 14:35:07.525066
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    """
    Build a typed field from a JSON schema reference object.
    """
    ref = Reference("#/definitions/foo")
    assert ref_from_json_schema({"$ref": "#/definitions/foo"}, definitions={
        "#/definitions/foo": ref
    }) == ref



# Generated at 2022-06-14 14:35:10.831109
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {"$ref": "#/definitions/name"}
    schema = from_json_schema(data)
    assert isinstance(schema, Reference)
    assert schema.to == "#/definitions/name"

# Generated at 2022-06-14 14:35:21.477677
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    def f(data: dict, definitions: SchemaDefinitions) -> Field:
        return if_then_else_from_json_schema(data, definitions)

    # Test a simple 'if' clause with a boolean literal
    data = {"if": {"const": True}}
    field = f(data, SchemaDefinitions())
    assert field.to_dict() == {"type": "if_then_else"}
    assert field.default == NO_DEFAULT

    # Test an 'if' clause with a boolean literal and 'then' branch
    data = {"if": {"const": True}, "then": {"const": True}}
    field = f(data, SchemaDefinitions())
    assert field.to_dict() == {"type": "if_then_else"}
    assert field.default == NO_DEFAULT

    # Test an 'if' clause

# Generated at 2022-06-14 14:35:32.193888
# Unit test for function if_then_else_from_json_schema

# Generated at 2022-06-14 14:35:39.259007
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert str(if_then_else_from_json_schema(
        {
            'if': {
                'type': 'integer'
            },
            'then': {
                'type': 'string'
            },
            'else': {
                'type': 'boolean'
            }
        },
        definitions= SchemaDefinitions()
    )) == 'IfThenElse(if_clause=Integer(), then_clause=String() if_true, else_clause=Boolean() if_false)'

test_if_then_else_from_json_schema()

# Generated at 2022-06-14 14:35:42.565729
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {
        'oneOf': [{'type': 'integer'}]
    }
    definitions = SchemaDefinitions()
    one_of = [from_json_schema(item, definitions=definitions) for item in data["oneOf"]]
    assert isinstance(one_of, list)
# unit test for function not_from_json_schema

# Generated at 2022-06-14 14:35:48.921620
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    assert type_from_json_schema({"type": "string"}, definitions=definitions) == String()
    obj = Object(properties={"a": String()})
    assert type_from_json_schema({"type": "object"}, definitions=definitions) == obj
    assert (
        type_from_json_schema({"type": "array"}, definitions=definitions)
        == Array(items=Any())
    )
    assert type_from_json_schema({"type": "boolean"}, definitions=definitions) == Boolean()
    assert type_from_json_schema({"type": "integer"}, definitions=definitions) == Integer()
    assert (
        type_from_json_schema({"type": "number"}, definitions=definitions)
        == Number()
    )

# Generated at 2022-06-14 14:36:01.197219
# Unit test for function const_from_json_schema
def test_const_from_json_schema():
    test_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "https://example.com/person.schema.json",
        "title": "Person",
        "type": "object",
        "properties": {
            "firstName": {
                "type": "string",
                "description": "The person's first name.",
                "const": "Pilou"
            },
            "lastName": {
                "type": "string",
                "description": "The person's last name.",
            },
        },
        "required": [
            "firstName",
            "lastName"
        ]
    }

# Generated at 2022-06-14 14:36:11.541114
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    data = {
        "allOf": [
            {
                "type": "object",
                "properties": {
                    "obj_property1": {"type": "string"},
                    "obj_property2": {"type": "number"}
                }
            },
            {
                "type": "object",
                "properties": {
                    "obj_property3": {"type": "string"},
                    "obj_property4": {"type": "number"}
                }
            }
        ]
    }

# Generated at 2022-06-14 14:36:55.079742
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    data = {
        "$ref": "#/definitions/myRef",
        "type": "string",
        "enum": ["bar", "foo"],
        "default": "bar",
    }
    definitions = SchemaDefinitions()
    definitions["#/definitions/myRef"] = String(default="MyRef")
    kwargs = {
        "choices": [("bar", "bar"), ("foo", "foo")],
        "default": "bar"
    }
    assert enum_from_json_schema(data, definitions=definitions) == Choice(**kwargs)



# Generated at 2022-06-14 14:37:00.051469
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {
        "oneOf": [{"type": "string", "enum": ["red", "amber", "green"]}]
    }
    field = one_of_from_json_schema(data, definitions=definitions)
    assert True == isinstance(field, OneOf)
    assert True == isinstance(field._one_of[0], Choice)



# Generated at 2022-06-14 14:37:05.561621
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"},
        ],
        "default": "Default string value"
    }
    definitions = SchemaDefinitions()
    field = one_of_from_json_schema(data, definitions)
    assert isinstance(field, OneOf)
    assert field._default == "Default string value"
    assert len(field.one_of) == 2
    for item in field.one_of:
        assert isinstance(item, (String, Integer, Float))



# Generated at 2022-06-14 14:37:13.658571
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    # Function not_from_json_schema returns a Not object
    assert isinstance(
        not_from_json_schema({'not': {'type': 'string'}}, definitions=SchemaDefinitions()),
        Not
    )

    # Function not_from_json_schema returns a Not object with the correct negated item
    assert isinstance(
        not_from_json_schema(
            {'not': {'type': 'string'}}, definitions=SchemaDefinitions()
        ).negated,
        String
    )



# Generated at 2022-06-14 14:37:17.317132
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
    value = {
        "anyOf": [
            {"type": "string"},
            {"type": "integer"},
        ],
    }
    assert isinstance(any_of_from_json_schema(value, None), Union)



# Generated at 2022-06-14 14:37:24.241413
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    # Indentation of this assertion is one space to support
    # json.tool for pretty printing.
    assert (
'{"title": "Typesystem Example",'
' "type": "object",'
' "required": ["name", "age"],'
' "properties": {'
'  "name": {'
'   "type": "string",'
'   "minLength": 1,'
'   "maxLength": 100'
'  },'
'  "age": {'
'   "type": "integer",'
'   "minimum": 0,'
'   "maximum": 200'
'  }'
' }'
'}'
    ) == json.dumps(to_json_schema(PersonSchema), indent=1, sort_keys=True)



# Generated at 2022-06-14 14:37:33.418558
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False

    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(Float()) == {"type": "number"}
    assert to_json_schema(Boolean()) == {"type": "boolean"}

    assert to_json_schema(String(allow_null=True)) == {"type": ["string", "null"]}
    assert to_json_schema(Integer(allow_null=True)) == {"type": ["integer", "null"]}
    assert to_json_schema(Float(allow_null=True)) == {"type": ["number", "null"]}
    assert to_json

# Generated at 2022-06-14 14:37:45.862091
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="integer", allow_null=False, definitions={}) == Integer(allow_null=False)
    assert from_json_schema_type({}, type_string="integer", allow_null=True, definitions={}) == Integer(allow_null=True)
    assert from_json_schema_type({}, type_string="string", allow_null=True, definitions={}) == String(allow_null=True, allow_blank=True, min_length=None, max_length=None, format=None, pattern=None)
    assert from_json_schema_type({}, type_string="number", allow_null=True, definitions={}) == Float(allow_null=True, minimum=None, maximum=None, exclusive_minimum=None, exclusive_maximum=None, multiple_of=None)

# Generated at 2022-06-14 14:37:58.284627
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "string", "enum": ["a"]}) == Choice(choices=["a"])
    assert from_json_schema({"type": "string", "const": "a"}) == Const("a")
    assert from_json_schema({"$ref": "#/foo"}) == Reference("#/foo")
    assert from_json_schema({"type": "string", "allOf": [{"$ref": "#/foo"}]}) == AllOf([Reference("#/foo"), String()])
    assert from_json_schema({"type": "string", "anyOf": [{"$ref": "#/foo"}]}) == Union([Reference("#/foo"), String()])
    assert from_json

# Generated at 2022-06-14 14:38:04.712401
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    valid_input = {'enum': ["1","2","3"]}
    #valid_output = Choice(choices=[('1','1'),('2','2'),('3','3')])
    valid_output = Choice(choices=[(1,1),(2,2),(3,3)])
    assert enum_from_json_schema(valid_input, definitions=definitions) == valid_output


# Generated at 2022-06-14 14:38:36.500954
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    schema = {
        "type": "object",
        "properties": {
            "string": {"type": "string"},
            "number": {"type": "number"},
            "object": {"type": "object"},
        },
    }
    assert from_json_schema(schema).to_primitive() == {
        "type": "object",
        "properties": {
            "string": {"type": "string"},
            "number": {"type": "number"},
            "object": {"type": "object"},
        },
    }



# Generated at 2022-06-14 14:38:44.114376
# Unit test for function from_json_schema_type

# Generated at 2022-06-14 14:38:49.857878
# Unit test for function from_json_schema
def test_from_json_schema():
    DATA = {
      "type": "object",
      "properties": {
        "price": {
          "type": "number",
          "minimum": 0
        },
        "name": {
          "type": "string",
          "minLength": 1
        }
      }
    }
    field = from_json_schema(DATA)
    assert isinstance(field, Object)
    assert isinstance(field.properties, dict)
    assert isinstance(field.properties["price"], Number)
    assert isinstance(field.properties["name"], String)
    assert field.properties["price"].minimum == 0
    assert field.properties["name"].min_length == 1


# Generated at 2022-06-14 14:38:56.533025
# Unit test for function to_json_schema
def test_to_json_schema():
    class SimpleSchema(Schema):
        foo = Integer(minimum=0, maximum=10)

    data = to_json_schema(SimpleSchema)
    assert data == {
        "definitions": {
            "SimpleSchema": {
                "type": "object",
                "properties": {
                    "foo": {
                        "type": ["integer", "null"],
                        "default": NO_DEFAULT,
                        "minimum": 0,
                        "maximum": 10,
                    }
                },
                "required": ["foo"],
            }
        },
        "$ref": "#/definitions/SimpleSchema",
    }
    data = to_json_schema(SimpleSchema.make_validator())

# Generated at 2022-06-14 14:39:08.645452
# Unit test for function to_json_schema
def test_to_json_schema():
    from py_meta_utils import ModuleAttribute

    from .fields import Field, String, Boolean, Integer, Float, Decimal
    from .fields import Choice, Const
    from .fields import Array, Object
    from .schema import Schema

    class MySchema(Schema):
        item = Field()
        string = String()
        boolean = Boolean()
        integer = Integer()
        float = Float(allow_nan=False)
        decimal = Decimal()
        choice = Choice(choices=[("a", "A"), ("b", "B")])
        const = Const(const="a")
        array = Array(
            min_items=0, max_items=1, items=String(), unique_items=False
        )

# Generated at 2022-06-14 14:39:21.139063
# Unit test for function to_json_schema
def test_to_json_schema():

    class SimpleSchema(Schema):
        integer = Integer()
        string = String(max_length=10, pattern=r"[a-z]+")
        boolean = Boolean()


# Generated at 2022-06-14 14:39:28.920022
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    schema_obj = {'type': 'string'}
    type_strings = ["string"]
    assert from_json_schema_type(schema_obj, type_strings[0], False, {}) == String()
    schema_obj = {'type': 'number'}
    type_strings = ["number"]
    assert from_json_schema_type(schema_obj, type_strings[0], False, {}) == Float()
    schema_obj = {'type': 'integer'}
    type_strings = ["integer"]
    assert from_json_schema_type(schema_obj, type_strings[0], False, {}) == Integer()
    schema_obj = {'type': 'boolean'}
    type_strings = ["boolean"]

# Generated at 2022-06-14 14:39:36.897011
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    json_schema = {
        "if": {
            "properties": {
                "foo": {"type": "string"}
            },
            "required": ["foo"],
        }
    }
    field = if_then_else_from_json_schema(json_schema, {})
    assert field.if_clause.__class__.__name__ == "Object"
    assert field.then_clause is None
    assert field.else_clause is None
    assert field.validate({}) is None
    assert field.validate({"foo": "bar"}) == {"foo": "bar"}
    assert field.validate({"foo": 1}) == {"foo": 1}

# Generated at 2022-06-14 14:39:49.484008
# Unit test for function to_json_schema
def test_to_json_schema():
    from .tests import assert_validate, assert_to_json_schema, assert_from_json_schema
    import pytest

    class Obj:
        a = String(max_length=10)
        b = Array(Integer)

    def obj_schema(_: str) -> Schema:
        return Schema(
            a=String(max_length=10),
            b=Array(Integer()),
            default_validators=[
                Object(required=["a"]),
                Object(min_properties=1),
                Object(max_properties=10),
                Object(required=["s"]),
                Object(max_properties=2),
            ],
        )

    class NestedObj(Schema):
        x = String(max_length=10)
        y = Array(Integer)

    nested_obj = N

# Generated at 2022-06-14 14:40:01.989634
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
  assert from_json_schema_type(data={}, type_string="number", allow_null=False, definitions=None) == Float(allow_null=False)
  assert from_json_schema_type(data={}, type_string="integer", allow_null=False, definitions=None) == Integer(allow_null=False)
  assert from_json_schema_type(data={}, type_string="string", allow_null=False, definitions=None) == String(allow_null=False)
  assert from_json_schema_type(data={}, type_string="boolean", allow_null=False, definitions=None) == Boolean(allow_null=False)
  try:
    from_json_schema_type({}, "array", False, None)
  except AssertionError:
    pass

# Generated at 2022-06-14 14:40:53.709655
# Unit test for function from_json_schema
def test_from_json_schema():
    from pytest import mark
    from typesystem.utils import InvalidValue, MissingValue
    from typesystem.errors import ErrorWrapper


# Generated at 2022-06-14 14:41:01.750549
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, "number", False, None) == Float()
    assert from_json_schema_type({"type": "integer"}, "integer", False, None)
    assert_type(
        from_json_schema_type(
            {}, "integer", False, None  # type: ignore
        ),
        Union,
        any_of=[Integer(), Float()],
    )



# Generated at 2022-06-14 14:41:08.338666
# Unit test for function from_json_schema
def test_from_json_schema():
    data = {
        "type": "object",
        "required": ["bar"],
        "properties": {"foo": {"type": "number"}, "bar": {"type": "number"}},
    }
    field = from_json_schema(data)
    assert isinstance(field, Object)
    assert field.required == {"bar"}
    assert isinstance(field.properties["foo"], Number)
    assert isinstance(field.properties["bar"], Number)



# Generated at 2022-06-14 14:41:15.785202
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    import pytest
    from typesystem.base import ValidationError
    from typesystem.schemas import SchemaDefinitions

    definitions = SchemaDefinitions()
    definitions["test"] = Integer()

# Generated at 2022-06-14 14:41:23.665374
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = Schema(
        {
            "a": String(
                min_length=3, max_length=8, pattern_regex=re.compile(r"^[a-z]+$")
            ),
            "b": Integer(minimum=3, maximum=8, multiple_of=3),
            "c": Choice(choices=[("A", "A"), ("B", "B"), ("C", "C")]),
            "d": Array(items=Integer(minimum=3, maximum=8), min_items=1, max_items=5),
        }
    )
    result = to_json_schema(schema)

# Generated at 2022-06-14 14:41:33.491558
# Unit test for function to_json_schema
def test_to_json_schema():
    source = Array(items=String())
    target = '{"type": "array", "items": {"type": "string"}}'
    assert json.dumps(to_json_schema(source), sort_keys=True) == target

    source = Union(Any())
    target = '{"type": "null"}'
    assert json.dumps(to_json_schema(source), sort_keys=True) == target

    source = Union(Any(), Schema(a=Integer()))
    target = '{"type": ["null", "object"], "properties": {"a": {"type": "integer"}}}'
    assert json.dumps(to_json_schema(source), sort_keys=True) == target

    source = Schema(a=String())

# Generated at 2022-06-14 14:41:45.088255
# Unit test for function to_json_schema
def test_to_json_schema():
    class TestSchema(Schema):
        foo = String()
        bar = Array(items=Integer())

    json_schema = to_json_schema(TestSchema())
    assert isinstance(json_schema, dict)
    assert json_schema == {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "http://example.com/example.json",
        "type": "object",
        "required": ["foo", "bar"],
        "properties": {
            "foo": {"type": "string"},
            "bar": {
                "type": "array",
                "items": {"type": ["integer", "null"]},
                "additionalItems": False,
            },
        },
        "additionalProperties": False,
    }


# Generated at 2022-06-14 14:41:57.187945
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from typesystem import String
    from typesystem.schema import Reference
    definitions = SchemaDefinitions()
    definitions["S"] = String(allow_blank=True)

    schema = from_json_schema(
        data={"type": "object", "properties": {"a": {"type": "string"}}},
        definitions=definitions,
    )
    assert isinstance(schema, Object)
    assert schema.properties["a"] == String(allow_null=False, allow_blank=False)

    schema = from_json_schema(
        data={"$ref": "#/definitions/S"},
        definitions=definitions,
    )
    assert isinstance(schema, Reference)
    assert schema.pointer == "#/definitions/S"


# Generated at 2022-06-14 14:42:07.251429
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="number", allow_null=False, definitions=definitions) == Number()
    assert from_json_schema_type({}, type_string="number", allow_null=True, definitions=definitions) == Number(allow_null=True)
    assert from_json_schema_type({}, type_string="integer", allow_null=False, definitions=definitions) == Integer()
    assert from_json_schema_type({}, type_string="integer", allow_null=True, definitions=definitions) == Integer(allow_null=True)
    assert from_json_schema_type({}, type_string="string", allow_null=False, definitions=definitions) == String()

# Generated at 2022-06-14 14:42:18.231690
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Boolean()) == {"type": "boolean"}
    assert to_json_schema(Integer()) == {"type": "integer"}
    assert to_json_schema(String()) == {"type": "string"}
    assert to_json_schema(GreaterThan(0)) == {"type": "integer", "minimum": 1}
    assert to_json_schema(LessThan(0)) == {"type": "integer", "maximum": -1}
    # Copied from https://json-schema.org/learn/miscellaneous-examples.html

# Generated at 2022-06-14 14:42:41.795374
# Unit test for function to_json_schema
def test_to_json_schema():
    field1 = Reference(
        to="#/definitions/DateString",
        definitions={
            "DateString": String(
                min_length=10, max_length=10, pattern_regex=re.compile("[0-9]{8}")
            )
        },
    )
    field2 = Boolean(default=True)
    field3 = Array(
        items=field1,
        additional_items=True,
        default=[],
    )
    # field4 = field3.get_and_validate("", [])
    field5 = Object(
        properties={
            "optional": String(default="A"),
            "required": String(required=True),
            "nested": Object(
                properties={
                    "field": String(),
                }
            )
        }
    )
    field

# Generated at 2022-06-14 14:42:53.587384
# Unit test for function from_json_schema

# Generated at 2022-06-14 14:43:04.981177
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    from typesystem import from_json_schema

    type_string = "boolean"
    field = from_json_schema_type({}, type_string=type_string)
    assert isinstance(field, Boolean)
    assert field.allow_null

    type_string = "integer"
    field = from_json_schema_type({}, type_string=type_string)
    assert isinstance(field, Integer)
    assert field.allow_null

    type_string = "object"
    field = from_json_schema_type({}, type_string=type_string)
    assert isinstance(field, Object)
    assert field.allow_null

    type_string = "array"
    field = from_json_schema_type({}, type_string=type_string)

# Generated at 2022-06-14 14:43:07.807276
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(String(allow_null=True)) == {
        "type": ["string", "null"]
    }



# Generated at 2022-06-14 14:43:17.079388
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Bool())["type"] == "boolean"
    assert to_json_schema(Any()) is True
    assert to_json_schema(NeverMatch()) is False
    assert (
        to_json_schema(
            Integer(minimum=42, maximum=84, multiple_of=6, default=42)
        )
        == {"type": "integer", "minimum": 42, "maximum": 84, "multipleOf": 6, "default": 42}
    )
    assert (
        to_json_schema(String(min_length=0, max_length=10, allow_blank=True, default=""))
        == {"type": "string", "minLength": 0, "maxLength": 10, "default": ""}
    )

# Generated at 2022-06-14 14:43:22.627439
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    data = {
        "type": "object",
        "properties": {"likes_coffee": {"type": "boolean"}, "has_hair": {"type": "boolean"}},
        "minProperties": 1,
    }
    assert from_json_schema_type(
        data, type_string='object', allow_null=False, definitions=None
    ) == Object(
        allow_null=False,
        properties={
            "likes_coffee": Boolean(allow_null=False),
            "has_hair": Boolean(allow_null=False),
        },
        min_properties=1,
    )



# Generated at 2022-06-14 14:43:30.737323
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    schema = {
        "$ref": "#/definitions/A",
        "definitions": {
            "A": {"type": "string"},
            "B": {"type": "integer"},
        },
    }
    definitions = SchemaDefinitions()
    assert from_json_schema(schema, definitions=definitions) == String()
    assert definitions["#/definitions/A"] == String()
    assert definitions["#/definitions/B"] == Integer()



# Generated at 2022-06-14 14:43:35.403419
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    schema = {
        "type": "string",
        "minLength": 1,
        "maxLength": 5,
    }
    assert type_from_json_schema(
        schema, definitions=SchemaDefinitions()
    ).to_json_schema() == schema



# Generated at 2022-06-14 14:43:45.173199
# Unit test for function from_json_schema
def test_from_json_schema():
    field = from_json_schema({"type": "boolean"})
    assert field.validate(True) == True
    assert field.validate(False) == False
    assert field.validate(None) == None

    field = from_json_schema({"type": "integer", "minimum": 1, "maximum": 3})
    assert field.validate(3) == 3
    assert field.validate(0) == None
    assert field.validate(4) == None

    field = from_json_schema({"type": "number", "multipleOf": 10})
    assert field.validate(20.0) == 20.0
    assert field.validate(21.0) == None
    

# Generated at 2022-06-14 14:43:53.597795
# Unit test for function to_json_schema
def test_to_json_schema():
    v = Field(required=True)

    assert to_json_schema(v) == {"type": "object"}

    v = String()
    assert to_json_schema(v) == {"type": "string"}
    assert to_json_schema(v.allow_blank(False)) == {
        "type": "string",
        "minLength": 1,
    }
    assert to_json_schema(v.allow_blank(True)) == {"type": "string"}
    assert to_json_schema(v.min_length(2)) == {"type": "string", "minLength": 2}
    assert to_json_schema(v.max_length(5)) == {"type": "string", "maxLength": 5}