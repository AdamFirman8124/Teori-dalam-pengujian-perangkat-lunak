# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import pytest

import typesystem
from typesystem.schemas import Schema


class _Person:
    """A plain (non-dict) object carrying attributes, for the object branch."""

    def __init__(self):
        self.name = "from-object"
        self.extra = "not-a-field"


@pytest.fixture
def person_schema():
    # The Schema subclass is created inside the fixture so that no global
    # state is created or polluted; it is garbage-collected after each test.
    class PersonSchema(Schema):
        name = typesystem.String()
        age = typesystem.Integer(default=0)

    return PersonSchema


def test_init_with_dict_argument_sets_matching_fields(person_schema):
    instance = person_schema({"name": "Alice"})
    assert instance.name == "Alice"
    # The dict branch returns early: defaults are *not* applied and keys
    # missing from the dict are skipped entirely.
    assert not hasattr(instance, "age")


def test_init_with_empty_dict_argument(person_schema):
    instance = person_schema({})
    assert not hasattr(instance, "name")
    assert not hasattr(instance, "age")


def test_init_with_object_argument_copies_attributes(person_schema):
    instance = person_schema(_Person())
    assert instance.name == "from-object"
    # Attributes that are not schema fields are not copied.
    assert not hasattr(instance, "extra")
    # Fields missing on the object are skipped (no defaults applied here).
    assert not hasattr(instance, "age")


def test_init_with_kwargs_validates_and_applies_defaults(person_schema):
    instance = person_schema(name="Alice")
    assert instance.name == "Alice"
    assert instance.age == 0  # default value applied for missing field


def test_init_with_no_arguments_applies_defaults_only(person_schema):
    instance = person_schema()
    assert instance.age == 0
    # 'name' has no default and was not supplied: nothing is set for it.
    assert not hasattr(instance, "name")


def test_init_with_invalid_kwarg_raises_type_error(person_schema):
    with pytest.raises(TypeError) as excinfo:
        person_schema(name=123)
    message = str(excinfo.value)
    assert message.startswith("Invalid argument 'name' for PersonSchema().")
    assert "Must be a string" in message


def test_init_with_unknown_kwarg_raises_type_error(person_schema):
    with pytest.raises(TypeError) as excinfo:
        person_schema(name="Alice", unknown="oops")
    assert str(excinfo.value) == (
        "'unknown' is an invalid keyword argument for PersonSchema()."
    )


def test_init_with_multiple_positional_args_asserts(person_schema):
    with pytest.raises(AssertionError):
        person_schema({}, {})


def test_init_with_positional_arg_and_kwargs_asserts(person_schema):
    with pytest.raises(AssertionError):
        person_schema({}, name="Alice")
