# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import pytest
from typesystem import String
from typesystem.schemas import Schema


class ExampleSchema(Schema):
    name = String()
    age = String()


def test_eq_returns_false_for_non_schema_instance():
    schema = ExampleSchema(name="alice", age="30")
    assert (schema == "not a schema") is False
    assert (schema != "not a schema") is True


def test_eq_returns_false_for_other_class_instance():
    class OtherSchema(Schema):
        name = String()
        age = String()

    schema = ExampleSchema(name="alice", age="30")
    other = OtherSchema(name="alice", age="30")
    assert (schema == other) is False


def test_eq_returns_false_when_field_values_differ():
    schema = ExampleSchema(name="alice", age="30")
    other = ExampleSchema(name="different", age="30")
    assert (schema == other) is False
    assert (schema != other) is True


def test_eq_returns_true_when_all_fields_equal():
    schema = ExampleSchema(name="alice", age="30")
    other = ExampleSchema(name="alice", age="30")
    assert (schema == other) is True
    assert not (schema != other)
