

# Generated at 2026-11-02 11:36:22.579601
# Unit test for function validate_yaml
def test_validate_yaml():
    if yaml is None:
        return  # Skip test if pyyaml is not installed.

    import pytest

    from typesystem import Array, Boolean, Integer, String

    # Test valid YAML string validation against a schema.
    class Person(Schema):
        name = String()
        age = Integer()

    value, error = module_0.validate_yaml("name: Jane\nage: 30\n", validator=Person)
    assert value == {"name": "Jane", "age": 30}
    assert error is None

    # Test valid YAML bytes validation.
    value, error = module_0.validate_yaml(b"name: Jane\nage: 30\n", validator=Person)
    assert value == {"name": "Jane", "age": 30}
    assert error is None

    # Test validation error with positional information.
    value, error = module_0.validate_yaml("name: Jane\nage: thirty\n", validator=Person)
    assert value is None
    assert error is not None
    assert error.code == "parse_error"
    assert error.message == "Expected a number."
    assert error.position is not None
    assert error.position.line_no == 2
    assert error.position.column_no == 6
    assert error.position.char_index == 16

    # Test required field missing with positional information.
    value, error = module_0.validate_yaml("name: Jane\n", validator=Person)
    assert value is None
    assert error is not None
    assert error.code == "required"
    assert error.message == "The field 'age' is required."
    assert error.position is not None
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    # Test validating against a simple field instance.
    value, error = module_0.validate_yaml("123", validator=Integer())
    assert value == 123
    assert error is None

    # Test validation failure against a simple field instance.
    value, error = module_0.validate_yaml("abc", validator=Integer())
    assert value is None
    assert error is not None
    assert error.code == "parse_error"
    assert error.position is not None
    assert error.position.line_no == 1

    # Test list validation with positions.
    value, error = module_0.validate_yaml("[1, 2, 3]", validator=Array(items=Integer()))
    assert value == [1, 2, 3]
    assert error is None

    # Test error inside a nested structure points to correct position.
    value, error = module_0.validate_yaml("- 1\n- two\n", validator=Array(items=Integer()))
    assert value is None
    assert error is not None
    assert error.code == "parse_error"
    assert error.position is not None
    assert error.position.line_no == 2

    # Test YAML parse errors raise ParseError.
    with pytest.raises(ParseError):
        module_0.validate_yaml("{ invalid", validator=Person)

    # Test empty content raises ParseError with clear message.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("", validator=Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.message == "No content."
    assert exc_info.value.position is not None
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

    # Test whitespace-only content raises ParseError.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n  \n", validator=Person)
    assert exc_info.value.code == "no_content"

    # Test boolean and float field validation.
    value, error = module_0.validate_yaml("flag: true\n", validator=Schema.build(fields={"flag": Boolean()}))
    assert value == {"flag": True}
    assert error is None

    # Test null values.
    class Nullable(Schema):
        value = String(allow_null=True)

    value, error = module_0.validate_yaml("value: null\n", validator=Nullable)
    assert value == {"value": None}
    assert error is None

# Generated at 2026-11-02 11:42:36.270947
# Unit test for function tokenize_yaml