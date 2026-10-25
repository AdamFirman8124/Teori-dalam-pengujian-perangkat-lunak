# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

from typesystem.fields import Integer, String
from typesystem.schemas import Schema


def test_repr_full():
    class Person(Schema):
        name = String()
        age = Integer()

    obj = Person(name="Alice", age=30)
    assert hasattr(obj, "name")
    assert hasattr(obj, "age")
    assert obj.is_sparse is False
    result = repr(obj)
    assert result == "Person(name='Alice', age=30)"
    assert "[sparse]" not in result


def test_repr_sparse_missing_attr():
    class Person(Schema):
        name = String()
        age = Integer()

    obj = Person(name="Bob")
    assert hasattr(obj, "name")
    assert not hasattr(obj, "age")
    assert obj.is_sparse is True
    result = repr(obj)
    assert result == "Person(name='Bob') [sparse]"
    assert "age" not in result


def test_repr_empty_schema():
    class Empty(Schema):
        pass

    obj = Empty()
    assert obj.is_sparse is False
    result = repr(obj)
    assert result == "Empty()"
