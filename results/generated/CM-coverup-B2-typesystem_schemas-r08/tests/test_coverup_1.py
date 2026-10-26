# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import types
import pytest
import typesystem


def test_init_with_dict_full():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    p = Person({"name": "Alice", "age": 30})
    assert p.name == "Alice"
    assert p.age == 30
    assert p["name"] == "Alice"
    assert p["age"] == 30


def test_init_with_dict_partial_missing_key():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    p = Person({"name": "Bob"})
    assert p.name == "Bob"
    # 'age' was not in dict, so it must not have been set
    assert not hasattr(p, "age") or "age" not in list(iter(p))


def test_init_with_object_full():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    obj = types.SimpleNamespace(name="Carol", age=25)
    p = Person(obj)
    assert p.name == "Carol"
    assert p.age == 25


def test_init_with_object_partial_missing_attr():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    obj = types.SimpleNamespace(name="Dave")
    p = Person(obj)
    assert p.name == "Dave"
    assert not hasattr(p, "age")


def test_init_with_kwargs_valid():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    p = Person(name="Eve", age=40)
    assert p.name == "Eve"
    assert p.age == 40


def test_init_with_kwargs_uses_default_and_skips_missing():
    class Person(typesystem.Schema):
        name = typesystem.String()
        nickname = typesystem.String(default="nicky")
        age = typesystem.Integer()

    p = Person(name="Frank")
    assert p.name == "Frank"
    assert p.nickname == "nicky"
    # 'age' has no default and was not supplied, so no error and no value
    assert not hasattr(p, "age")


def test_init_with_kwargs_invalid_value_raises():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    with pytest.raises(TypeError) as excinfo:
        Person(name=123, age=30)
    msg = str(excinfo.value)
    assert "Invalid argument" in msg
    assert "'name'" in msg
    assert "Person" in msg


def test_init_with_kwargs_invalid_keyword_raises():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer(default=99)

    with pytest.raises(TypeError) as excinfo:
        Person(name="Grace", age=20, unknown="boom")
    msg = str(excinfo.value)
    assert "'unknown'" in msg
    assert "invalid keyword argument" in msg
    assert "Person" in msg


def test_init_assert_too_many_args():
    class Person(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(AssertionError):
        Person({"name": "a"}, {"name": "b"})


def test_init_assert_args_and_kwargs():
    class Person(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(AssertionError):
        Person({"name": "a"}, name="b")
