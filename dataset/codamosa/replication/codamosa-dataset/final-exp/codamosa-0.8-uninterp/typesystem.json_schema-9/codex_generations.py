

# Generated at 2022-06-14 14:35:53.796573
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    data = {
        "oneOf": [
            {
                "type": "integer",
                "minimum": 5,
                "maximum": 10,
                "const": 5,
            },
            {
                "type": "integer",
                "minimum": 8,
                "maximum": 10,
                "const": 9,
            },
            {
                "type": "integer",
                "minimum": 10,
                "maximum": 10,
                "const": 10,
            },
        ]
    }
    result = one_of_from_json_schema(data, definitions=None)
    assert len(result.one_of) == 3
    assert result.one_of[0].type_name == "Integer"


# Generated at 2022-06-14 14:35:56.129213
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    from_json_schema({"allOf": [{"type": "string"}, {"minLength": 1}]})



# Generated at 2022-06-14 14:36:06.051993
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    for i, case in enumerate(test_cases, start=1):
        with pytest.raises(AssertionError):
            one_of_from_json_schema({"oneOf": [{}, {}]}, None)
        with pytest.raises(AssertionError):
            one_of_from_json_schema({"oneOf": []}, None)
        with pytest.raises(AssertionError):
            one_of_from_json_schema({"oneOf": None}, None)
        with pytest.raises(AssertionError):
            one_of_from_json_schema({"oneOf": True}, None)



# Generated at 2022-06-14 14:36:11.710565
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():
  data = {"anyOf": [{"type": "integer"}, {"type": "string"}]}
  assert isinstance(any_of_from_json_schema(data, SchemaDefinitions()), Union)
  assert isinstance(any_of_from_json_schema(data, SchemaDefinitions()).any_of[0], Integer)
  assert isinstance(any_of_from_json_schema(data, SchemaDefinitions()).any_of[1], String)



# Generated at 2022-06-14 14:36:19.999506
# Unit test for function to_json_schema
def test_to_json_schema():
    class TestSchema(Schema):

        int_field: Integer(minimum=2, multiple_of=3)
        choice_field: Choice(choices=[("a", "A"), ("b", "B"), ("c", "C")])
    json_data = to_json_schema(TestSchema())
    assert json_data == {
        "type": "object",
        "properties": {
            "int_field": {
                "type": "integer",
                "minimum": 2,
                "multipleOf": 3
            },
            "choice_field": {
                "type": "string",
                "enum": ["a", "b", "c"]
            }
        },
        "required": ["int_field", "choice_field"]
    }



# Generated at 2022-06-14 14:36:24.718491
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():
    assert AllOf(all_of=[Integer(minimum=2)], default=None) == all_of_from_json_schema({"allOf":[{'type': 'number', 'minimum': 2}]},None)



# Generated at 2022-06-14 14:36:34.969738
# Unit test for function from_json_schema

# Generated at 2022-06-14 14:36:40.579500
# Unit test for function to_json_schema
def test_to_json_schema():
    from . import Schema

    class TestSchema(Schema):
        a = fields.Integer()
        b = fields.Integer()
        c = fields.Integer()
        d = fields.Integer()

    expect = {
        "type": "object",
        "properties": {
            "a": {"type": "integer"},
            "b": {"type": "integer"},
            "c": {"type": "integer"},
            "d": {"type": "integer"},
        },
        "required": ["a", "b", "c", "d"],
    }
    assert to_json_schema(TestSchema) == expect

# Generated at 2022-06-14 14:36:47.674759
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():
    json_schema_object = {'oneOf': [{'type': 'boolean'}, {'type': 'number'}]}
    test_object = one_of_from_json_schema(json_schema_object, definitions)
    assert test_object == {
        'one_of': [
            Boolean(
                allow_null=False,
            ),
            Number(
                allow_null=False,
            )
        ],
       'default': NO_DEFAULT
    }


# Generated at 2022-06-14 14:36:57.856478
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    # Test with no then or else clauses
    field = if_then_else_from_json_schema({"if": {"type": "integer"}}, SchemaDefinitions())
    assert field.if_clause.type == "integer"
    assert field.then_clause is None
    assert field.else_clause is None

    # Test with just then clause
    field = if_then_else_from_json_schema(
        {"if": {"type": "integer"}, "then": {"type": "string"}}, SchemaDefinitions()
    )
    assert field.if_clause.type == "integer"
    assert field.then_clause.type == "string"
    assert field.else_clause is None

    # Test with just else clause

# Generated at 2022-06-14 14:37:44.666263
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type(data={}, type_string="number", allow_null=True) == Float(allow_null=True)
    assert from_json_schema_type(data={}, type_string="integer", allow_null=True) == Integer(allow_null=True)
    assert from_json_schema_type(data={}, type_string="string", allow_null=True) == String(allow_null=True)
    assert from_json_schema_type(data={}, type_string="boolean", allow_null=True) == Boolean(allow_null=True)
    assert from_json_schema_type(data={}, type_string="array", allow_null=True) == Array(allow_null=True)

# Generated at 2022-06-14 14:37:51.849876
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():
    assert_match(
        if_then_else_from_json_schema({"if": {"type": "string"}, "then": {}}),
        {"type": "string"}
    )
    assert_match(
        if_then_else_from_json_schema({"if": {"type": "string"}, "else": {}}),
        {"type": "null"}
    )



# Generated at 2022-06-14 14:37:54.819313
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    assert ref_from_json_schema({"$ref": "#/definitions/Foo"}).to == "#/definitions/Foo"


# Generated at 2022-06-14 14:38:00.588259
# Unit test for function enum_from_json_schema
def test_enum_from_json_schema():
    enum_schema = {"enum": [1, 2, 3]}
    enum_field = enum_from_json_schema(enum_schema)
    assert enum_field.validate(1) == 1
    assert enum_field.validate(2) == 2
    assert enum_field.validate(3) == 3
    assert enum_field.validate(4) == "This value does not have a valid choice."
    assert enum_field.validate(None) == "This field may not be null."



# Generated at 2022-06-14 14:38:10.362021
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():
    data = {
        '$ref': '#/definitions/my_schema'
    }
    definitions = SchemaDefinitions()
    definitions['#/definitions/my_schema'] = Union(
        any_of=[
            String(min_length=5),
            Boolean()
        ]
    )
    field = ref_from_json_schema(data, definitions)
    assert isinstance(field, Reference)
    assert field.to == '#/definitions/my_schema'
    assert isinstance(field.resolve(definitions), Union)
    assert isinstance(field.resolve(definitions).any_of[0], String)
    assert field.resolve(definitions).any_of[0].min_length == 5

# Generated at 2022-06-14 14:38:18.234747
# Unit test for function to_json_schema
def test_to_json_schema():
    def assert_result_is_valid(data: dict):
        try:
            jsonschema.Draft7Validator(data).validate(data)
        except jsonschema.exceptions.ValidationError as exc:
            exc.context.append(data)
            raise

    assert_result_is_valid(to_json_schema(Any()))
    assert_result_is_valid(to_json_schema(NeverMatch()))
    assert_result_is_valid(to_json_schema(String()))
    assert_result_is_valid(to_json_schema(Integer()))
    assert_result_is_valid(to_json_schema(Float()))
    assert_result_is_valid(to_json_schema(Boolean()))

# Generated at 2022-06-14 14:38:28.118137
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    data = {
        "required": ["foo"],
        "properties": {
            "foo": {
                "type": "string",
                "minLength": 1,
                "maxLength": 3,
                "pattern": r"^[a-zA-Z]*$",
                "format": "date",
            }
        },
    }

    field = from_json_schema_type(data, "object", False, SchemaDefinitions())
    assert isinstance(field, Object)
    assert field.properties["foo"].type == "string"
    assert field.properties["foo"].min_length == 1
    assert field.properties["foo"].max_length == 3
    assert field.properties["foo"].pattern == re.compile("^[a-zA-Z]*$")
    assert field.properties

# Generated at 2022-06-14 14:38:33.131940
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {
        "not": {"type": "boolean"}
    }
    field = not_from_json_schema(data, definitions=definitions)
    assert isinstance(field, Not)
    assert isinstance(field.negated, Boolean)



# Generated at 2022-06-14 14:38:41.792704
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, type_string="number", allow_null=True) == Float(
        allow_null=True
    )
    assert from_json_schema_type({}, type_string="number") == Float()
    assert from_json_schema_type(
        {"minimum": 1}, type_string="number", allow_null=True
    ) == Float(allow_null=True, minimum=1)
    assert from_json_schema_type({"minimum": 1}, type_string="number") == Float(minimum=1)
    assert (
        from_json_schema_type({"minimum": 1}, type_string="integer", allow_null=True)
        == Integer(allow_null=True, minimum=1)
    )

# Generated at 2022-06-14 14:38:49.380541
# Unit test for function from_json_schema
def test_from_json_schema():
    data = {
        "type": "boolean",
        "enum": [True, False],
        "const": False,
    }
    field = from_json_schema(data)
    assert type(field) == Choice
    assert len(field.constraints) == 2
    assert type(field.constraints[0]) == Const
    assert field.constraints[0].value == False
    assert type(field.constraints[1]) == Const
    assert field.constraints[1].value == True



# Generated at 2022-06-14 14:39:51.845644
# Unit test for function from_json_schema
def test_from_json_schema():
    from typesystem.exceptions import ValidationError

    schema = from_json_schema(
        {
            "type": "object",
            "properties": {"foo": {"type": "string", "const": "bar"}},
            "required": ["foo"],
        }
    )

    schema.validate({"foo": "bar"})

    with pytest.raises(ValidationError) as excinfo:
        schema.validate({})
    assert excinfo.value.field_errors == {"foo": "Missing value."}

    with pytest.raises(ValidationError) as excinfo:
        schema.validate({"foo": "baz"})
    assert excinfo.value.field_errors == {"foo": "Must be 'bar'."}



# Generated at 2022-06-14 14:39:58.626586
# Unit test for function to_json_schema
def test_to_json_schema():
    schema = String.make(min_length=1, max_length=10, pattern_regex=re.compile(r".*"))
    data = to_json_schema(schema)
    assert isinstance(data, dict)
    assert data == {
        "type": "string",
        "minLength": 1,
        "maxLength": 10,
        "pattern": ".*",
    }


# Generated at 2022-06-14 14:40:08.198716
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    schema = {
        "type": "string",
        "minLength": 1,
        "maxLength": 10,
        "pattern": "^[0-9a-zA-Z]*$",
    }
    expected = String(
        min_length=1,
        max_length=10,
        format="regex",
        pattern=re.compile("^[0-9a-zA-Z]*$"),
    )
    assert from_json_schema(schema) == expected

    schema = {
        "type": ["string", "null"],
        "minLength": 1,
        "maxLength": 10,
        "pattern": "^[0-9a-zA-Z]*$",
    }

# Generated at 2022-06-14 14:40:13.397560
# Unit test for function not_from_json_schema
def test_not_from_json_schema():
    data = {"not": {"type": "null"}}
    field = not_from_json_schema(data, definitions=SchemaDefinitions())
    assert isinstance(field, Not)
    assert field.default == NO_DEFAULT
    assert isinstance(field.negated, NeverMatch)
    assert data == to_json_schema(field)



# Generated at 2022-06-14 14:40:17.890990
# Unit test for function to_json_schema
def test_to_json_schema():
    print("\n************************************************************")
    print("Testing JSON Schema conversion")
    print("************************************************************")

    def test(arg, expected):
        print("\n# Initial argument")
        print(arg)
        print("# Expected argument")
        print(expected)
        print("# Result")
        result = to_json_schema(arg)
        print(result)
        assert result == expected, f"{result!r} != {expected!r}"
        print("# OK")

    test(
        Any(),
        {"type": "any", "default": {"type": "any"}},
    )
    test(
        Any(default=None),
        {"type": "any", "default": None},
    )


# Generated at 2022-06-14 14:40:30.190270
# Unit test for function to_json_schema
def test_to_json_schema():
    data = to_json_schema(String())
    assert data == {"type": "string"}

    data = to_json_schema(Integer())
    assert data == {"type": "integer"}

    data = to_json_schema(Integer(maximum=100, exclusive_maximum=True))
    assert data == {
        "type": "integer",
        "maximum": 100,
        "exclusiveMaximum": True,
    }

    data = to_json_schema(
        IfThenElse(
            if_clause=String(pattern_regex=re.compile(r"^foo.*")),
            then_clause=Integer(minimum=0),
            else_clause=Integer(minimum=10),
        )
    )

# Generated at 2022-06-14 14:40:37.830799
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert from_json_schema_type({}, "boolean", True, None) == Boolean(allow_null=True)
    assert from_json_schema_type({}, "null", True, None) == Const(None)
    assert from_json_schema_type({}, "integer", True, None) == Integer(allow_null=True)
    assert from_json_schema_type({}, "number", True, None) == Float(allow_null=True)
    assert from_json_schema_type({}, "string", True, None) == String(allow_null=True)
    assert from_json_schema_type({}, "array", True, None) == Array(allow_null=True)
    assert from_json_schema_type({}, "object", True, None) == Object(allow_null=True)

# Generated at 2022-06-14 14:40:48.996016
# Unit test for function to_json_schema
def test_to_json_schema():
    data = to_json_schema(Schema(name="Test", fields={"test": String(max_length=10)}))
    assert data == {"type": "object", "properties": {"test": {"type": "string", "maxLength": 10}}, "required": ["test"]}
    data = to_json_schema(Array(items=Integer(maximum=0), additional_items=False))
    assert data == {"type": "array", "items": {"type": "integer", "maximum": 0}, "additionalItems": False}
    data = to_json_schema(Object(pattern_properties={r"^test\w+": String(max_length=10)}))
    assert data == {"type": "object", "patternProperties": {"^test\\w+": {"type": "string", "maxLength": 10}}}
    data

# Generated at 2022-06-14 14:41:01.591597
# Unit test for function to_json_schema
def test_to_json_schema():
    class Foo(Schema):
        name = String(max_length=5)

    foo_schema = to_json_schema(Foo)
    assert set(foo_schema.keys()) == {"definitions", "properties", "type"}
    assert foo_schema["type"] == "object"
    assert foo_schema["properties"]["name"]["type"] == "string"
    assert foo_schema["properties"]["name"]["maxLength"] == 5

    foo = Foo()
    assert foo.validate({"name": "hello"}) is None
    assert foo.validate({"name": "hello world"}) == {
        "name": ["Ensure this field has no more than 5 characters."]
    }


# Generated at 2022-06-14 14:41:11.380749
# Unit test for function type_from_json_schema
def test_type_from_json_schema():
    # Test when "type" is "null"
    data = {"type": "null"}
    field = type_from_json_schema(data, definitions=definitions)
    assert isinstance(field, Const)
    assert field.value is None

    # Test when "type" is "string"
    data = {"type": "string"}
    field = type_from_json_schema(data, definitions=definitions)
    assert isinstance(field, String)

    # Test when "type" is "integer"
    data = {"type": "integer"}
    field = type_from_json_schema(data, definitions=definitions)
    assert isinstance(field, Integer)

    # Test when "type" is "number"
    data = {"type": "number"}

# Generated at 2022-06-14 14:41:38.194838
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema({}) == Any()
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()
    schema = from_json_schema({"type": "string"})
    assert isinstance(schema, String)
    assert schema.to_json_schema() == {"type": "string"}


# Generated at 2022-06-14 14:41:47.199754
# Unit test for function to_json_schema
def test_to_json_schema():

    class TestSchema(Schema):
        foo: typing.List[int]

    actual = to_json_schema(TestSchema)
    expected = {
        "definitions": {},
        "properties": {"foo": {"items": {"type": "integer"}, "type": "array"}},
        "required": ["foo"],
        "type": "object",
    }
    assert actual == expected, (
        f"Function to_json_schema doesn't produce expected JSON schema. Actual:\n"
        f"{actual!r}\n\nExpected:\n{expected!r}"
    )



# Generated at 2022-06-14 14:41:58.409771
# Unit test for function to_json_schema
def test_to_json_schema():
    from ionize.schema import Integer, Schema

    class JsonSchema(Schema):
        number = Integer(default=42)

    data = to_json_schema(JsonSchema)
    assert data == {
        "type": "object",
        "properties": {"number": {"type": "number"}},
        "required": ["number"],
        "default": {"number": 42},
    }
    assert data["properties"]["number"] == {
        "type": "number"
    }

    class JsonSchema(Schema):
        optional_number = Integer()

    data = to_json_schema(JsonSchema)
    assert data == {
        "type": "object",
        "properties": {"optional_number": {"type": "number"}},
        "default": {},
    }

# Generated at 2022-06-14 14:42:05.283724
# Unit test for function to_json_schema
def test_to_json_schema():
    def test_case(schema, expected):
        actual = to_json_schema(schema)
        assert actual == expected

    test_case(
        String(),
        {
            "type": "string",
        },
    )

# Generated at 2022-06-14 14:42:16.365193
# Unit test for function to_json_schema
def test_to_json_schema():
    assert to_json_schema(Any()) == True
    assert to_json_schema(NeverMatch()) == False
    assert to_json_schema(String(allow_blank=True)) == {"type": "string"}
    assert to_json_schema(String(allow_null=True, allow_blank=True)) == {
        "type": ["string", "null"]
    }
    assert to_json_schema(String(max_length=5, min_length=2, max_length=5)) == {
        "type": "string",
        "minLength": 2,
        "maxLength": 5,
        "default": None,
        "examples": [],
    }

# Generated at 2022-06-14 14:42:20.638211
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    for type_string in {
        "number",
        "integer",
        "string",
        "boolean",
        "array",
        "object",
    }:
        assert isinstance(from_json_schema_type({}, type_string=type_string), Field)



# Generated at 2022-06-14 14:42:26.940374
# Unit test for function from_json_schema_type
def test_from_json_schema_type():
    assert isinstance(
        from_json_schema_type({"type": "integer"}, "integer", False, None), Integer
    )
    assert isinstance(
        from_json_schema_type({"type": "boolean"}, "boolean", False, None), Boolean
    )
    assert isinstance(
        from_json_schema_type({"type": "number"}, "number", False, None), Float
    )
    assert isinstance(
        from_json_schema_type({"type": "string"}, "string", False, None), String
    )
    assert isinstance(
        from_json_schema_type({"type": "null"}, "null", True, None), Const
    )



# Generated at 2022-06-14 14:42:38.959827
# Unit test for function to_json_schema
def test_to_json_schema():
    _field = {"a": Integer(), "b": String()}
    _schema = Schema(_field)

    # assert isinstance(_schema, Schema), "Schema is not instance of Schema class"
    assert isinstance(_schema, JSONSchemaMixin), f"Schema is not instance of JSONSchemaMixin"
    assert isinstance(_schema, JSONSchemaMixin), f"_field is not instance of JSONSchemaMixin"

    assert isinstance(_schema.make_validator(), Object), "Schema's validator is not instance of Object class"
    schema_field = _schema.make_validator()

    output = to_json_schema(_schema)
    # print(output)


# Generated at 2022-06-14 14:42:51.183805
# Unit test for function to_json_schema
def test_to_json_schema():
    # pylint: disable=too-many-statements,too-many-locals,too-many-branches
    # pylint: disable=invalid-name,redefined-outer-name,unused-argument
    # pylint: disable=too-many-arguments,redefined-outer-name
    # pylint: disable=no-self-use,redefined-outer-name
    from .fields import *
    from .schema import Schema

    class TestSchema(Schema):
        def __init__(self):
            self.field_string = String(min_length=5, max_length=10)
            self.field_integer = Integer(multiple_of=3, minimum=1, maximum=100)

# Generated at 2022-06-14 14:43:02.560065
# Unit test for function to_json_schema
def test_to_json_schema():
    from .fields import (
        Any,
        AllOf,
        Array,
        Boolean,
        Choice,
        Const,
        Decimal,
        Dictionary,
        Float,
        IfThenElse,
        Integer,
        Not,
        Null,
        Object,
        OneOf,
        Schema,
        String,
        Union,
    )
    from .valspec import Specification

    class Author(Schema):
        name = String()

    class ValidationSchema(Schema):
        id = Integer()
        title = String()
        author = Author(nullable=True)
        categories = Array(String(), max_items=3, unique_items=True)
        price = Float(minimum=0.0, maximum=1000.0)

# Generated at 2022-06-14 14:43:24.116372
# Unit test for function to_json_schema
def test_to_json_schema():
    # type: () -> None
    import json

    class Person(Schema):
        name = String(max_length=500, allow_empty=False)
        age = Integer(minimum=0, maximum=150)
        date_of_death = String(allow_empty=True)

    class Thing(Schema):
        name = String(max_length=100, allow_empty=False)
        person = Person()
        date_of_death = String(allow_empty=True)

    class DeathCertificate(Schema):
        cause_of_death = String(allow_empty=False)
        thing = Field(Thing)

        def clean_thing(self, thing):
            # type: (Thing) -> Thing
            thing.date_of_death = self.cause_of_death
            return thing

    death_certificate

# Generated at 2022-06-14 14:43:33.365250
# Unit test for function to_json_schema
def test_to_json_schema():

    class Height(Schema):
        feet = Integer(minimum=0, maximum=9)
        inches = Integer(minimum=0, maximum=11)

        def is_valid(self, value):
            return (
                0 <= value.feet <= 9
                and 0 <= value.inches <= 11
                and value.feet != 9 or value.inches == 0
            )

    class Person(Schema):
        name = String(allow_null=False)
        age = Integer(minimum=0)
        height = Height()

    serialized = to_json_schema(Person)

# Generated at 2022-06-14 14:43:39.940400
# Unit test for function from_json_schema
def test_from_json_schema():
    assert from_json_schema(True) == Any()
    assert from_json_schema(False) == NeverMatch()

    assert from_json_schema({"type": "boolean"}) == Boolean()
    assert from_json_schema({"type": "integer"}) == Integer()
    assert from_json_schema({"type": "number"}) == Number()
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"type": "object"}) == Object()
    assert from_json_schema({"type": "array"}) == Array()
    assert from_json_schema({"type": ["boolean", "integer"]}) == Choice(
        options=(Boolean(), Integer())
    )


# Generated at 2022-06-14 14:43:48.459025
# Unit test for function from_json_schema
def test_from_json_schema():
    # Enum
    assert from_json_schema({"enum": ["foo", "bar"]}) == Choice(["foo", "bar"])
    assert from_json_schema({"enum": ["foo", "bar"], "type": "string"}) == Choice(
        ["foo", "bar"]
    )

    # String
    assert from_json_schema({"type": "string"}) == String()
    assert from_json_schema({"minLength": 5}) == String(min_length=5)
    assert from_json_schema({"maxLength": 10}) == String(max_length=10)
    assert from_json_schema({"pattern": "^\\d{3}$"}) == String(pattern=re.compile("^\\d{3}$"))

# Generated at 2022-06-14 14:43:56.137268
# Unit test for function from_json_schema

# Generated at 2022-06-14 14:44:04.597020
# Unit test for function to_json_schema
def test_to_json_schema():
    from . import String, Integer, Array
    from .json import from_json_schema

    field = String(
        allow_null=True,
        min_length=1,
        max_length=10,
        pattern="abc",
        format="date",
        default="a",
        description="string field",
        title="string field",
    )
    schema = to_json_schema(field)
    assert schema == {
        "type": ["string", "null"],
        "default": "a",
        "description": "string field",
        "title": "string field",
        "minLength": 1,
        "maxLength": 10,
        "pattern": "abc",
        "format": "date",
    }
    field2 = from_json_schema(schema)
    assert field == field2

# Generated at 2022-06-14 14:44:12.716045
# Unit test for function to_json_schema
def test_to_json_schema():
    class Simple(Schema):
        field = String()

    class SimpleWithOptional(Schema):
        field = String(allow_null=True)

    class SimpleWithRequired(Schema):
        field = String(required=True)

    class SimpleWithDefault(Schema):
        field = String(default="x")

    class SimpleWithConst(Schema):
        field = Const("value")

    class SimpleWithEnum(Schema):
        field = Choice(choices=[("a", "a"), ("b", "b")])

    class SimpleWithDefaultIfNone(Schema):
        field = String(default_if_none="default")

    class SimpleWithAllOf(Schema):
        field = AllOf(
            String(min_length=1), String(max_length=10), String(default="x")
        )

   