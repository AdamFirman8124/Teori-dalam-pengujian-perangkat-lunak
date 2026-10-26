# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import typesystem


class Example(typesystem.Schema):
    name = typesystem.String()
    age = typesystem.Integer()


class Other(typesystem.Schema):
    name = typesystem.String()
    age = typesystem.Integer()


def test_eq_returns_false_for_non_schema_instance():
    example = Example(name="Alice", age=30)

    assert example.__eq__(object()) is False
    assert example.__eq__({"name": "Alice", "age": 30}) is False
    assert example.__eq__(None) is False
    assert example != object()


def test_eq_returns_true_for_equal_instances():
    first = Example(name="Alice", age=30)
    second = Example(name="Alice", age=30)

    assert first.__eq__(second) is True
    assert first == second
    assert not (first != second)


def test_eq_returns_false_when_field_values_differ():
    first = Example(name="Alice", age=30)
    different_name = Example(name="Bob", age=30)
    different_age = Example(name="Alice", age=31)

    assert first.__eq__(different_name) is False
    assert first != different_name
    assert first.__eq__(different_age) is False
    assert first != different_age


def test_eq_returns_false_for_different_schema_class():
    example = Example(name="Alice", age=30)
    other = Other(name="Alice", age=30)

    assert example.__eq__(other) is False
    assert example != other
