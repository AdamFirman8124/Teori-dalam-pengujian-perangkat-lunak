# file: project/typesystem/schemas.py:189-190
# asked: {"lines": [190], "branches": []}
# gained: {"lines": [190], "branches": []}

from typesystem.schemas import Schema


def test_schema_len_empty():
    class S(Schema):
        pass

    S.fields = {"a": object(), "b": object()}
    instance = object.__new__(S)
    assert len(instance) == 0
    assert len([key for key in instance.fields if hasattr(instance, key)]) == 0


def test_schema_len_partial():
    class S(Schema):
        pass

    S.fields = {"a": object(), "b": object()}
    instance = object.__new__(S)
    object.__setattr__(instance, "a", 1)
    assert hasattr(instance, "a") is True
    assert hasattr(instance, "b") is False
    assert len(instance) == 1


def test_schema_len_full():
    class S(Schema):
        pass

    S.fields = {"a": object(), "b": object()}
    instance = object.__new__(S)
    object.__setattr__(instance, "a", 1)
    object.__setattr__(instance, "b", 2)
    assert len(instance) == 2
