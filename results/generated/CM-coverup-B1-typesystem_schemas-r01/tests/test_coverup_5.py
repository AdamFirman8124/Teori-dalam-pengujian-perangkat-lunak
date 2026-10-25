# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import pytest

import typesystem


def make_schema_class():
    class Example(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    return Example


def test_eq_returns_false_for_non_schema_instance():
    Example = make_schema_class()
    instance = Example(name="alice", age=30)

    assert (instance == "not a schema") is False
    assert (instance == 42) is False
    assert (instance == None) is False  # noqa: E711


def test_eq_returns_false_for_other_schema_class_instance():
    Example = make_schema_class()

    class Other(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    a = Example(name="alice", age=30)
    b = Other(name="alice", age=30)

    assert (a == b) is False


def test_eq_returns_true_for_equal_field_values():
    Example = make_schema_class()
    a = Example(name="alice", age=30)
    b = Example(name="alice", age=30)

    assert a == b
    assert b == a


def test_eq_returns_false_for_unequal_field_values():
    Example = make_schema_class()
    a = Example(name="alice", age=30)
    b = Example(name="alice", age=31)
    c = Example(name="bob", age=30)

    assert (a == b) is False
    assert (a == c) is False
    assert (b == c) is False


def test_eq_returns_true_for_same_instance():
    Example = make_schema_class()
    a = Example(name="alice", age=30)

    assert a == a
