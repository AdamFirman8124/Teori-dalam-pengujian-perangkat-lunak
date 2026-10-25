# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

from typesystem.schemas import Schema


def test_schema_equality_returns_false_for_different_type():
    class ExampleSchema(Schema):
        pass

    schema = ExampleSchema()
    assert schema.__eq__(object()) is False


def test_schema_equality_returns_false_for_different_field_values():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"first": object(), "second": object()}

    left = ExampleSchema({"first": "same", "second": 1})
    right = ExampleSchema({"first": "same", "second": 2})

    assert left.__eq__(right) is False


def test_schema_equality_returns_true_when_all_fields_match():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"first": object(), "second": object()}

    left = ExampleSchema({"first": "same", "second": 1})
    right = ExampleSchema({"first": "same", "second": 1})

    assert left.__eq__(right) is True
