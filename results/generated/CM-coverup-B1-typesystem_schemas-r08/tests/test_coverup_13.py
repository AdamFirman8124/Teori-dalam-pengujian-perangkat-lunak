# file: project/typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

from typesystem.fields import Field
from typesystem.schemas import Schema


def test_is_sparse_returns_true_when_field_is_missing(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    class ExampleSchema(Schema):
        required = Field()

    instance = ExampleSchema({})

    assert not hasattr(instance, "required")
    assert instance.is_sparse is True


def test_is_sparse_returns_false_when_all_fields_are_present(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    class ExampleSchema(Schema):
        required = Field()

    instance = ExampleSchema({"required": "value"})

    assert instance.required == "value"
    assert instance.is_sparse is False
