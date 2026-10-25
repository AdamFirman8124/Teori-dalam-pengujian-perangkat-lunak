# file: project/typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

from typesystem.schemas import Schema


def test_is_sparse_when_a_declared_field_is_missing():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"present": object(), "missing": object()}
    instance = ExampleSchema({"present": "value"})

    assert instance.present == "value"
    assert not hasattr(instance, "missing")
    assert instance.is_sparse is True


def test_is_not_sparse_when_all_declared_fields_are_present():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"first": object(), "second": object()}
    instance = ExampleSchema({"first": 1, "second": 2})

    assert instance.first == 1
    assert instance.second == 2
    assert instance.is_sparse is False
