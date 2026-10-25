# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

from typesystem.fields import Field
from typesystem.schemas import Schema


def test_schema_repr_includes_present_fields_and_sparse_indicator(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    class Example(Schema):
        name = Field()
        age = Field()

    instance = Example({"name": "Alice"})

    assert instance.is_sparse is True
    assert repr(instance) == "Example(name='Alice') [sparse]"


def test_schema_repr_includes_all_fields_without_sparse_indicator(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    class Example(Schema):
        name = Field()
        age = Field()

    instance = Example({"name": "Alice", "age": 30})

    assert instance.is_sparse is False
    assert repr(instance) == "Example(name='Alice', age=30)"
