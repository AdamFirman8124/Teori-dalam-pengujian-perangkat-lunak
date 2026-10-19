

# Generated at 2024-06-04 19:57:40.137357
# Unit test for function type_from_json_schema
def test_type_from_json_schema():    # Test case 1: Single type string
    data = {"type": "string"}
    definitions = SchemaDefinitions()
    field = type_from_json_schema(data, definitions)
    assert isinstance(field, String)

    # Test case 2: Multiple type strings
    data = {"type": ["string", "null"]}
    field = type_from_json_schema(data, definitions)
    assert isinstance(field, Union)
    assert any(isinstance(item, String) for item in field.any_of)
    assert field.allow_null is True

    # Test case 3: No type strings, allow null
    data = {"type": []}
    field = type_from_json_schema(data, definitions)
    assert isinstance(field, Const)
    assert field.value is None

    # Test case 4: No type strings, do not allow null
    data = {"type": [], "nullable": False}
    field = type_from_json_schema(data, definitions)

# Generated at 2024-06-04 19:57:45.688587
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"},
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 19:57:50.953845
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():    data = {
        "anyOf": [
            {"type": "string", "minLength": 5},
            {"type": "integer", "minimum": 10}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 19:57:55.189321
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():    schema_data = {
        "allOf": [
            {"type": "string", "minLength": 5},
            {"type": "string", "maxLength": 10}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 19:57:57.379246
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 19:58:01.129370
# Unit test for function const_from_json_schema
def test_const_from_json_schema():    data = {"const": "fixed_value", "default": "default_value"}

# Generated at 2024-06-04 19:58:04.739422
# Unit test for function all_of_from_json_schema
def test_all_of_from_json_schema():    schema_data = {
        "allOf": [
            {"type": "string", "minLength": 5},
            {"type": "string", "maxLength": 10}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 19:58:07.790206
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"type": "number"},
        "default": "default_value"
    }

# Generated at 2024-06-04 19:58:10.441824
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"type": "number"},
        "default": "default_value"
    }

# Generated at 2024-06-04 19:58:15.565742
# Unit test for function to_json_schema
def test_to_json_schema():    from unittest import TestCase


# Generated at 2024-06-04 19:58:45.538006
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"},
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 19:58:49.925367
# Unit test for function from_json_schema_type
def test_from_json_schema_type():    data = {
        "type": "string",
        "minLength": 5,
        "maxLength": 10,
        "pattern": "^[a-zA-Z]+$",
        "default": "default"
    }

# Generated at 2024-06-04 19:58:53.201617
# Unit test for function from_json_schema_type
def test_from_json_schema_type():    # Test for type "number"
    data = {
        "type": "number",
        "minimum": 0,
        "maximum": 10,
        "exclusiveMinimum": 1,
        "exclusiveMaximum": 9,
        "multipleOf": 2,
        "default": 5
    }
    field = from_json_schema_type(data, "number", False, definitions)
    assert isinstance(field, Float)
    assert field.minimum == 0
    assert field.maximum == 10
    assert field.exclusive_minimum == 1
    assert field.exclusive_maximum == 9
    assert field.multiple_of == 2
    assert field.default == 5

    # Test for type "integer"

# Generated at 2024-06-04 19:58:57.255474
# Unit test for function to_json_schema
def test_to_json_schema():    # Test case for Any type
    any_field = Any()
    assert to_json_schema(any_field) == True

    # Test case for NeverMatch type
    never_match_field = NeverMatch()
    assert to_json_schema(never_match_field) == False

    # Test case for Reference type
    reference_field = Reference(to="#/definitions/SomeType", definitions={})
    expected_reference_schema = {
        "$ref": "#/definitions/SomeType",
        "definitions": {"SomeType": {}}
    }
    assert to_json_schema(reference_field) == expected_reference_schema

    # Test case for String type
    string_field = String(allow_null=True, min_length=1, max_length=10, pattern_regex=re.compile(r"^[a-z]+$"))

# Generated at 2024-06-04 19:58:59.959473
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 19:59:03.689323
# Unit test for function from_json_schema_type
def test_from_json_schema_type():    # Test for type "number"
    schema = {"type": "number", "minimum": 0, "maximum": 10}
    field = from_json_schema_type(schema, "number", False, definitions)
    assert isinstance(field, Float)
    assert field.minimum == 0
    assert field.maximum == 10

    # Test for type "integer"
    schema = {"type": "integer", "minimum": 0, "maximum": 10}
    field = from_json_schema_type(schema, "integer", False, definitions)
    assert isinstance(field, Integer)
    assert field.minimum == 0
    assert field.maximum == 10

    # Test for type "string"
    schema = {"type": "string", "minLength": 1, "maxLength": 5}
    field = from_json_schema_type(schema, "string", False, definitions)
    assert isinstance(field, String)

# Generated at 2024-06-04 19:59:06.829318
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():    schema_data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 19:59:10.788765
# Unit test for function to_json_schema
def test_to_json_schema():    from typing import Any, Dict, List, Union

# Generated at 2024-06-04 19:59:13.571975
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 19:59:17.728044
# Unit test for function from_json_schema
def test_from_json_schema():    # Test case 1: Boolean schema
    assert isinstance(from_json_schema(True), Any)
    assert isinstance(from_json_schema(False), NeverMatch)

    # Test case 2: Simple type schema
    schema = {"type": "string"}
    field = from_json_schema(schema)
    assert isinstance(field, String)

    # Test case 3: Enum schema
    schema = {"enum": ["red", "green", "blue"]}
    field = from_json_schema(schema)
    assert isinstance(field, Choice)
    assert field.choices == ["red", "green", "blue"]

    # Test case 4: Const schema
    schema = {"const": 42}
    field = from_json_schema(schema)
    assert isinstance(field, Const)
    assert field.const == 42

    # Test case 5: AllOf schema
    schema = {"allOf": [{"type": "string"}, {"minLength": 2}]}
    field

# Generated at 2024-06-04 19:59:48.068685
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"},
            {"type": "boolean"}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 19:59:51.145171
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"type": "number"},
        "default": "default_value"
    }

# Generated at 2024-06-04 19:59:54.906823
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 19:59:58.341173
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"type": "number"},
        "default": "default_value"
    }

# Generated at 2024-06-04 20:00:01.115690
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:00:04.728668
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():    data = {
        "anyOf": [
            {"type": "string", "minLength": 5},
            {"type": "number", "minimum": 10}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 20:00:09.498075
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:00:13.706740
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"type": "number"},
        "default": "default_value"
    }

# Generated at 2024-06-04 20:00:16.742692
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"minLength": 1},
        "default": "default_value"
    }

# Generated at 2024-06-04 20:00:21.369423
# Unit test for function from_json_schema
def test_from_json_schema():    # Test case for boolean schema
    assert isinstance(from_json_schema(True), Any)
    assert isinstance(from_json_schema(False), NeverMatch)

    # Test case for simple type schema
    schema = {"type": "string"}
    field = from_json_schema(schema)
    assert isinstance(field, String)

    # Test case for enum schema
    schema = {"enum": ["red", "green", "blue"]}
    field = from_json_schema(schema)
    assert isinstance(field, Choice)
    assert field.choices == ["red", "green", "blue"]

    # Test case for const schema
    schema = {"const": "constant_value"}
    field = from_json_schema(schema)
    assert isinstance(field, Const)
    assert field.const == "constant_value"

    # Test case for allOf schema
    schema = {"allOf": [{"type": "string"}, {"minLength": 2}]}
    field = from_json_schema(schema)

# Generated at 2024-06-04 20:00:58.847107
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():    data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 20:01:02.025873
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"minLength": 1},
        "default": "default_value"
    }

# Generated at 2024-06-04 20:01:03.594068
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:01:06.135770
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:01:10.930178
# Unit test for function to_json_schema
def test_to_json_schema():    # Test case for Any type
    any_field = Any()
    assert to_json_schema(any_field) == True

    # Test case for NeverMatch type
    never_match_field = NeverMatch()
    assert to_json_schema(never_match_field) == False

    # Test case for Reference type
    reference_field = Reference(to="#/definitions/Example", definitions={})
    expected_reference_schema = {
        "$ref": "#/definitions/Example",
        "definitions": {"Example": {}}
    }
    assert to_json_schema(reference_field) == expected_reference_schema

    # Test case for String type
    string_field = String(allow_null=True, min_length=1, max_length=10, pattern_regex=re.compile(r'^[a-z]+$'))

# Generated at 2024-06-04 20:01:14.283843
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:01:17.071797
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"type": "number"},
        "default": "default_value"
    }

# Generated at 2024-06-04 20:01:19.679854
# Unit test for function not_from_json_schema
def test_not_from_json_schema():    data = {
        "not": {
            "type": "string"
        }
    }

# Generated at 2024-06-04 20:01:23.210345
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:01:25.079746
# Unit test for function not_from_json_schema
def test_not_from_json_schema():    data = {
        "not": {
            "type": "string"
        }
    }

# Generated at 2024-06-04 20:02:38.639876
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:02:41.888875
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:02:52.947308
# Unit test for function type_from_json_schema
def test_type_from_json_schema():    definitions = SchemaDefinitions()

    # Test with a single type

# Generated at 2024-06-04 20:02:55.388229
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():    schema_data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"},
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 20:02:57.713515
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"type": "number"},
        "default": "default_value"
    }

# Generated at 2024-06-04 20:02:59.798278
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"},
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 20:03:11.032604
# Unit test for function from_json_schema_type
def test_from_json_schema_type():    data = {
        "type": "string",
        "minLength": 5,
        "maxLength": 10,
        "pattern": "^[a-zA-Z]+$",
        "default": "default"
    }

# Generated at 2024-06-04 20:03:13.768139
# Unit test for function one_of_from_json_schema
def test_one_of_from_json_schema():    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"},
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 20:03:17.436925
# Unit test for function to_json_schema
def test_to_json_schema():    # Test case for Any type
    any_field = Any()
    assert to_json_schema(any_field) == True

    # Test case for NeverMatch type
    never_match_field = NeverMatch()
    assert to_json_schema(never_match_field) == False

    # Test case for Reference type
    reference_field = Reference(to="some_ref", definitions={})
    assert to_json_schema(reference_field) == {"$ref": "#/definitions/some_ref"}

    # Test case for String type
    string_field = String(allow_null=True, min_length=1, max_length=10, pattern_regex=re.compile(r"^\w+$"), format="email")
    expected_string_schema = {
        "type": ["string", "null"],
        "minLength": 1,
        "maxLength": 10,
        "pattern": r"^\w+$",
        "format": "email"
    }
    assert to_json_schema(string_field)

# Generated at 2024-06-04 20:03:18.959868
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:05:24.553599
# Unit test for function to_json_schema
def test_to_json_schema():    # Test case for Any type
    any_field = Any()
    assert to_json_schema(any_field) == True

    # Test case for NeverMatch type
    never_match_field = NeverMatch()
    assert to_json_schema(never_match_field) == False

    # Test case for Reference type
    reference_field = Reference(to="#/definitions/SomeType", definitions={})
    expected_reference_schema = {
        "$ref": "#/definitions/SomeType",
        "definitions": {"SomeType": {}}
    }
    assert to_json_schema(reference_field) == expected_reference_schema

    # Test case for String type
    string_field = String(allow_null=True, min_length=1, max_length=10, pattern_regex=re.compile(r'^[a-z]+$'))

# Generated at 2024-06-04 20:05:27.504082
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():    schema_data = {
        "anyOf": [
            {"type": "string", "minLength": 5},
            {"type": "number", "minimum": 10}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 20:05:29.386972
# Unit test for function not_from_json_schema
def test_not_from_json_schema():    schema = {
        "not": {
            "type": "string"
        }
    }

# Generated at 2024-06-04 20:05:32.171737
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():    schema_data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"},
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 20:05:34.382955
# Unit test for function ref_from_json_schema
def test_ref_from_json_schema():    definitions = SchemaDefinitions()

# Generated at 2024-06-04 20:05:38.283210
# Unit test for function from_json_schema_type
def test_from_json_schema_type():    data = {
        "type": "number",
        "minimum": 0,
        "maximum": 10,
        "exclusiveMinimum": 1,
        "exclusiveMaximum": 9,
        "multipleOf": 2,
        "default": 4
    }

# Generated at 2024-06-04 20:05:40.552541
# Unit test for function if_then_else_from_json_schema
def test_if_then_else_from_json_schema():    data = {
        "if": {"type": "string"},
        "then": {"minLength": 5},
        "else": {"type": "number"}
    }

# Generated at 2024-06-04 20:05:46.137612
# Unit test for function to_json_schema
def test_to_json_schema():    # Test case for Any type
    any_field = Any()
    assert to_json_schema(any_field) == True

    # Test case for NeverMatch type
    never_match_field = NeverMatch()
    assert to_json_schema(never_match_field) == False

    # Test case for Reference type
    reference_field = Reference(to="#/definitions/SomeType", definitions={})
    expected_reference_schema = {
        "$ref": "#/definitions/SomeType",
        "definitions": {"SomeType": {}}
    }
    assert to_json_schema(reference_field) == expected_reference_schema

    # Test case for String type
    string_field = String(allow_null=True, min_length=1, max_length=10, pattern_regex=re.compile(r"^[a-z]+$"))

# Generated at 2024-06-04 20:05:49.507256
# Unit test for function any_of_from_json_schema
def test_any_of_from_json_schema():    data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }

# Generated at 2024-06-04 20:05:53.153568
# Unit test for function to_json_schema
def test_to_json_schema():    # Test case for Any type
    any_field = Any()
    assert to_json_schema(any_field) == True

    # Test case for NeverMatch type
    never_match_field = NeverMatch()
    assert to_json_schema(never_match_field) == False

    # Test case for Reference type
    reference_field = Reference(to="some_ref", definitions={})
    expected_reference_schema = {
        "$ref": "#/definitions/some_ref",
        "definitions": {"some_ref": {}}
    }
    assert to_json_schema(reference_field) == expected_reference_schema

    # Test case for String type
    string_field = String(allow_null=True, min_length=1, max_length=10, pattern_regex=re.compile(r'^[a-z]+$'))