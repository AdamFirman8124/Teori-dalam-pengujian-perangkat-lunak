# file: project/typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

from typesystem.schemas import Schema


def test_is_sparse_when_a_field_is_missing(monkeypatch):
    class ExampleSchema(Schema):
        pass

    monkeypatch.setattr(
        ExampleSchema,
        "fields",
        {"present": object(), "missing": object()},
    )
    instance = ExampleSchema({"present": "value"})

    assert instance.present == "value"
    assert not hasattr(instance, "missing")
    assert instance.is_sparse is True


def test_is_sparse_when_all_fields_are_present(monkeypatch):
    class ExampleSchema(Schema):
        pass

    monkeypatch.setattr(
        ExampleSchema,
        "fields",
        {"first": object(), "second": object()},
    )
    instance = ExampleSchema({"first": 1, "second": 2})

    assert instance.first == 1
    assert instance.second == 2
    assert instance.is_sparse is False
