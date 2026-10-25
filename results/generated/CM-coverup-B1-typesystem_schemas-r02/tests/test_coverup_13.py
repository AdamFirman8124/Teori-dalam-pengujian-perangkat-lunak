# file: project/typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

from typesystem.schemas import Schema


def test_is_sparse_when_a_field_attribute_is_missing():
    class TestSchema(Schema):
        pass

    TestSchema.fields = {"present": object(), "missing": object()}
    instance = TestSchema({"present": "value"})

    assert hasattr(instance, "present")
    assert not hasattr(instance, "missing")
    assert instance.is_sparse is True


def test_is_sparse_when_all_field_attributes_are_present():
    class TestSchema(Schema):
        pass

    TestSchema.fields = {"first": object(), "second": object()}
    instance = TestSchema({"first": 1, "second": 2})

    assert hasattr(instance, "first")
    assert hasattr(instance, "second")
    assert instance.is_sparse is False
