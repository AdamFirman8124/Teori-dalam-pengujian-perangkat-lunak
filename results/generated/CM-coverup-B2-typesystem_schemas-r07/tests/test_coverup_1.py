# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

"""Tests for typesystem.schemas.Schema.__init__ (lines 96-131).

These tests exercise every branch of Schema.__init__:
  * positional argument given (dict item / non-dict item, present/missing keys)
  * keyword arguments (valid values, field defaults, validation failures)
  * leftover unknown keyword arguments
  * the assertion guards on len(args) and kwargs

No global state is mutated by these tests (the metaclass only registers
schemas when an explicit ``definitions`` mapping is passed), so no
monkeypatching/teardown is required; each test works on freshly created
instances and local helper classes.
"""

import pytest

from typesystem.fields import Integer, String
from typesystem.schemas import Schema


class Person(Schema):
    name = String()
    age = Integer(default=0)


def test_init_from_dict_sets_present_fields():
    person = Person({"name": "Alice", "age": 30})
    assert getattr(person, "name") == "Alice"
    assert getattr(person, "age") == 30


def test_init_from_dict_leaves_missing_fields_unset():
    # Covers the False branch of ``if key in item`` inside the dict path.
    person = Person({"name": "Alice"})
    assert getattr(person, "name") == "Alice"
    assert not hasattr(person, "age")


def test_init_from_object_copies_matching_attributes():
    # Covers the non-dict branch of ``isinstance(item, dict)``.
    class Obj:
        name = "Bob"
        age = 42
        extra = "ignored"

    person = Person(Obj())
    assert getattr(person, "name") == "Bob"
    assert getattr(person, "age") == 42


def test_init_from_object_leaves_missing_attributes_unset():
    # Covers the False branch of ``hasattr(item, key)``.
    class Obj:
        name = "Bob"

    person = Person(Obj())
    assert getattr(person, "name") == "Bob"
    assert not hasattr(person, "age")


def test_init_with_kwargs_validates_and_sets_values():
    person = Person(name="Alice", age=30)
    assert getattr(person, "name") == "Alice"
    assert getattr(person, "age") == 30


def test_init_with_kwargs_applies_field_defaults():
    # Covers ``elif schema.has_default():`` / ``get_default_value()``.
    person = Person(name="Alice")
    assert getattr(person, "name") == "Alice"
    assert getattr(person, "age") == 0


def test_init_skips_fields_without_kwarg_or_default():
    # Covers the False branch of ``elif schema.has_default():``.
    person = Person(age=5)
    assert getattr(person, "age") == 5
    assert not hasattr(person, "name")


def test_init_with_invalid_kwarg_raises_type_error():
    # Covers the ``if error:`` branch: validation failure is reported
    # as a TypeError built from the joined error messages.
    with pytest.raises(TypeError) as excinfo:
        Person(name=123)
    assert str(excinfo.value) == (
        "Invalid argument 'name' for Person(). Must be a string."
    )


def test_init_with_unknown_kwarg_raises_type_error():
    # Covers the trailing ``if kwargs:`` branch after a valid kwarg.
    with pytest.raises(TypeError) as excinfo:
        Person(name="Alice", unknown="oops")
    assert str(excinfo.value) == (
        "'unknown' is an invalid keyword argument for Person()."
    )


def test_init_with_only_unknown_kwargs_raises_type_error():
    # Same trailing branch, reached without any valid kwarg being set.
    with pytest.raises(TypeError) as excinfo:
        Person(unknown=1)
    assert str(excinfo.value) == (
        "'unknown' is an invalid keyword argument for Person()."
    )


def test_init_with_multiple_positional_args_asserts():
    # Covers ``assert len(args) == 1``.
    with pytest.raises(AssertionError):
        Person({"name": "Alice"}, {"name": "Bob"})


def test_init_with_positional_arg_and_kwargs_asserts():
    # Covers ``assert not kwargs``.
    with pytest.raises(AssertionError):
        Person({"name": "Alice"}, age=30)
