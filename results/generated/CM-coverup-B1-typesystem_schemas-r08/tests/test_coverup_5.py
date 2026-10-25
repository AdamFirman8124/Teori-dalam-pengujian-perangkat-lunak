# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

from typesystem.schemas import Schema


def test_schema_equality_returns_false_for_different_type():
    class ExampleSchema(Schema):
        pass

    instance = ExampleSchema()

    assert instance.__eq__(object()) is False


def test_schema_equality_returns_false_for_different_field_values(monkeypatch):
    class ExampleSchema(Schema):
        pass

    monkeypatch.setattr(ExampleSchema, "fields", {"value": object()})

    left = ExampleSchema({"value": 1})
    right = ExampleSchema({"value": 2})

    assert left.__eq__(right) is False


def test_schema_equality_returns_true_for_equal_field_values(monkeypatch):
    class ExampleSchema(Schema):
        pass

    monkeypatch.setattr(ExampleSchema, "fields", {"value": object()})

    left = ExampleSchema({"value": 1})
    right = ExampleSchema({"value": 1})

    assert left.__eq__(right) is True
