# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

from typesystem.schemas import Schema


def test_schema_iter_yields_only_fields_present_on_instance(monkeypatch):
    schema = Schema()

    monkeypatch.setattr(
        schema,
        "fields",
        {"present": object(), "missing": object()},
    )
    monkeypatch.setattr(schema, "present", "value", raising=False)

    assert list(schema) == ["present"]
    assert "missing" not in list(schema)
