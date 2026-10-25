# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

from typesystem.schemas import Schema


def test_schema_repr_includes_all_present_fields() -> None:
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"name": object(), "count": object()}
    instance = ExampleSchema({"name": "Ada", "count": 3})

    assert instance.is_sparse is False
    assert repr(instance) == "ExampleSchema(name='Ada', count=3)"


def test_schema_repr_omits_missing_fields_and_marks_sparse() -> None:
    class SparseSchema(Schema):
        pass

    SparseSchema.fields = {"name": object(), "count": object()}
    instance = SparseSchema({"name": "Ada"})

    assert not hasattr(instance, "count")
    assert instance.is_sparse is True
    assert repr(instance) == "SparseSchema(name='Ada') [sparse]"
