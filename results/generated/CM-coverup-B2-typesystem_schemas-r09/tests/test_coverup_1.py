# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import pytest

from typesystem.fields import Integer, String
from typesystem.schemas import Schema


def test_init_with_dict_sets_fields_present_in_dict():
    class Example(Schema):
        name = String()
        age = Integer()

    instance = Example({"name": "Alice", "extra": "ignored"})
    assert instance.name == "Alice"
    # Fields missing from the dict are left unset.
    assert not hasattr(instance, "age")
    # Keys that are not schema fields are ignored.
    assert not hasattr(instance, "extra")


def test_init_with_dict_does_not_validate_values():
    class Example(Schema):
        name = String()

    instance = Example({"name": 123})
    assert instance.name == 123


def test_init_with_object_copies_matching_attributes():
    class Example(Schema):
        name = String()
        age = Integer()

    class Obj:
        name = "Bob"
        unrelated = 42

    instance = Example(Obj())
    assert instance.name == "Bob"
    # Attributes missing on the object are not copied.
    assert not hasattr(instance, "age")
    assert not hasattr(instance, "unrelated")


def test_init_with_multiple_positional_args_raises_assertion_error():
    class Example(Schema):
        name = String()

    with pytest.raises(AssertionError):
        Example({"name": "x"}, {"name": "y"})


def test_init_with_positional_arg_and_kwargs_raises_assertion_error():
    class Example(Schema):
        name = String()

    with pytest.raises(AssertionError):
        Example({"name": "x"}, name="y")


def test_init_with_valid_kwargs_sets_validated_values():
    class Example(Schema):
        name = String()
        age = Integer()

    instance = Example(name="Alice", age=30)
    assert instance.name == "Alice"
    assert instance.age == 30


def test_init_with_invalid_kwarg_raises_type_error():
    class Example(Schema):
        name = String()

    with pytest.raises(TypeError) as excinfo:
        Example(name=123)
    message = str(excinfo.value)
    assert message.startswith("Invalid argument 'name' for Example().")
    assert "Must be a string" in message


def test_init_with_invalid_integer_kwarg_raises_type_error():
    class Example(Schema):
        age = Integer()

    with pytest.raises(TypeError) as excinfo:
        Example(age="not a number")
    message = str(excinfo.value)
    assert message.startswith("Invalid argument 'age' for Example().")
    assert "Must be a number" in message


def test_init_uses_field_defaults_for_missing_kwargs():
    class Example(Schema):
        name = String(default="anonymous")
        age = Integer(default=0)

    instance = Example()
    assert instance.name == "anonymous"
    assert instance.age == 0


def test_init_explicit_kwarg_overrides_default():
    class Example(Schema):
        name = String(default="anonymous")

    instance = Example(name="Alice")
    assert instance.name == "Alice"


def test_init_leaves_field_without_default_unset_when_kwarg_missing():
    class Example(Schema):
        name = String()
        age = Integer()

    instance = Example(name="Alice")
    assert instance.name == "Alice"
    assert not hasattr(instance, "age")


def test_init_with_unknown_kwarg_raises_type_error():
    class Example(Schema):
        name = String()

    with pytest.raises(TypeError) as excinfo:
        Example(name="Alice", unknown="oops")
    assert str(excinfo.value) == "'unknown' is an invalid keyword argument for Example()."
