# file: project/typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

from typesystem.schemas import Schema


def test_schema_is_sparse_for_missing_and_present_fields(monkeypatch):
    class ExampleSchema(Schema):
        pass

    monkeypatch.setattr(
        ExampleSchema,
        "fields",
        {"first": object(), "second": object()},
    )

    sparse = ExampleSchema({"first": "value"})
    assert sparse.first == "value"
    assert not hasattr(sparse, "second")
    assert sparse.is_sparse is True

    complete = ExampleSchema({"first": "value", "second": 2})
    assert complete.first == "value"
    assert complete.second == 2
    assert complete.is_sparse is False
