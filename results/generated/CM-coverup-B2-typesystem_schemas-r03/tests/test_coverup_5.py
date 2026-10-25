# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import typesystem


def test_schema_equality_returns_false_for_unrelated_type():
    class Example(typesystem.Schema):
        name = typesystem.String()

    instance = Example(name="Alice")

    assert instance.__eq__(object()) is False


def test_schema_equality_returns_false_when_field_values_differ():
    class Example(typesystem.Schema):
        name = typesystem.String()
        city = typesystem.String()

    first = Example(name="Alice", city="London")
    second = Example(name="Alice", city="Paris")

    assert first.__eq__(second) is False


def test_schema_equality_returns_true_when_all_field_values_match():
    class Example(typesystem.Schema):
        name = typesystem.String()
        city = typesystem.String()

    first = Example(name="Alice", city="London")
    second = Example(name="Alice", city="London")

    assert first.__eq__(second) is True


def test_empty_schemas_are_equal():
    class EmptySchema(typesystem.Schema):
        pass

    assert EmptySchema().__eq__(EmptySchema()) is True
