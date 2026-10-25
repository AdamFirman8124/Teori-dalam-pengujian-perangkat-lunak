# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

from typesystem.fields import Field
from typesystem.schemas import Schema


def test_iter_yields_only_set_fields():
    class MySchema(Schema):
        a = Field()
        b = Field()

    obj = MySchema({"a": "x"})
    assert list(obj) == ["a"]
    assert dict(obj) == {"a": "x"}
    assert list(iter(obj)) == ["a"]


def test_iter_empty_when_no_fields_set():
    class MySchema2(Schema):
        a = Field()
        b = Field()

    obj = MySchema2({})
    assert list(obj) == []
    assert dict(obj) == {}


def test_iter_yields_all_when_all_set():
    class MySchema3(Schema):
        a = Field()
        b = Field()

    obj = MySchema3({"a": 1, "b": 2})
    assert list(obj) == ["a", "b"]
    assert dict(obj) == {"a": 1, "b": 2}
