# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

from typesystem.schemas import Schema


def test_schema_equality_rejects_different_type():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"value": object()}
    instance = ExampleSchema({"value": 1})

    assert instance.__eq__(object()) is False


def test_schema_equality_rejects_different_field_value():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"value": object()}
    first = ExampleSchema({"value": 1})
    second = ExampleSchema({"value": 2})

    assert first.__eq__(second) is False


def test_schema_equality_accepts_equal_field_values():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"value": object()}
    first = ExampleSchema({"value": 1})
    second = ExampleSchema({"value": 1})

    assert first.__eq__(second) is True
