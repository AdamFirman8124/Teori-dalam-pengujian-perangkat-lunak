# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

from typesystem.schemas import Schema


def test_schema_iter_yields_only_fields_with_attributes(monkeypatch):
    schema = Schema()
    present_key = "_coverage_present_field"
    absent_key = "_coverage_absent_field"

    monkeypatch.setattr(
        schema,
        "fields",
        {present_key: object(), absent_key: object()},
    )
    monkeypatch.setattr(schema, present_key, "value", raising=False)

    assert hasattr(schema, present_key)
    assert not hasattr(schema, absent_key)
    assert list(schema) == [present_key]
