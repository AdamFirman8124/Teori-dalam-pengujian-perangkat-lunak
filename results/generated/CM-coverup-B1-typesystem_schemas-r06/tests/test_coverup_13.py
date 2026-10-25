# file: project/typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

from typesystem.schemas import Schema


def test_is_sparse_when_a_field_attribute_is_missing(monkeypatch):
    schema = Schema()
    monkeypatch.setattr(schema, "fields", {"present": object(), "missing": object()})
    monkeypatch.setattr(schema, "present", "value", raising=False)

    assert hasattr(schema, "present")
    assert not hasattr(schema, "missing")
    assert schema.is_sparse is True


def test_is_not_sparse_when_all_field_attributes_are_present(monkeypatch):
    schema = Schema()
    monkeypatch.setattr(schema, "fields", {"first": object(), "second": object()})
    monkeypatch.setattr(schema, "first", 1, raising=False)
    monkeypatch.setattr(schema, "second", 2, raising=False)

    assert hasattr(schema, "first")
    assert hasattr(schema, "second")
    assert schema.is_sparse is False
