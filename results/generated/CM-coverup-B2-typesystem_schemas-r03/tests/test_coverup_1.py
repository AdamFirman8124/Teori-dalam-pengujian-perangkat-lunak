# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import types

import pytest

import typesystem


def test_init_kwargs_valid_with_defaults_applied():
    class KwSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)
        age = typesystem.Integer(default=0)

    instance = KwSchema(name="Alice", age=30)
    assert instance.name == "Alice"
    assert instance.age == 30
    assert instance["name"] == "Alice"
    assert instance["age"] == 30


def test_init_kwargs_uses_field_default():
    class KwSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)
        age = typesystem.Integer(default=7)

    instance = KwSchema(name="Bob")
    assert instance.name == "Bob"
    assert instance.age == 7
    assert instance.__dict__["age"] == 7


def test_init_kwargs_missing_required_without_default():
    class KwSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)
        age = typesystem.Integer(default=7)

    instance = KwSchema(age=5)
    assert instance.age == 5
    assert "name" not in instance.__dict__
    assert not hasattr(instance, "name")


def test_init_kwargs_validation_error():
    class KwSchema(typesystem.Schema):
        name = typesystem.String(max_length=3)
        age = typesystem.Integer(default=0)

    with pytest.raises(TypeError) as exc_info:
        KwSchema(name="toolongvalue", age=1)
    message = str(exc_info.value)
    assert "'name'" in message
    assert "KwSchema" in message
    assert "Invalid argument" in message


def test_init_kwargs_invalid_keyword_argument():
    class KwSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)
        age = typesystem.Integer(default=0)

    with pytest.raises(TypeError) as exc_info:
        KwSchema(name="Alice", age=1, bogus=123)
    message = str(exc_info.value)
    assert "'bogus'" in message
    assert "KwSchema" in message
    assert "invalid keyword argument" in message


def test_init_positional_dict_all_keys_present():
    class DictSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)
        age = typesystem.Integer(default=99)

    instance = DictSchema({"name": "Alice", "age": 30})
    assert instance.name == "Alice"
    assert instance.age == 30
    assert instance.__dict__["name"] == "Alice"
    assert instance.__dict__["age"] == 30


def test_init_positional_dict_partial_keys():
    class DictSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)
        nickname = typesystem.String(max_length=50)

    instance = DictSchema({"name": "Alice"})
    assert instance.name == "Alice"
    assert "nickname" not in instance.__dict__
    assert not hasattr(instance, "nickname")


def test_init_positional_object_all_attrs_present():
    class ObjSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)
        age = typesystem.Integer(default=99)

    item = types.SimpleNamespace(name="Bob", age=42)
    instance = ObjSchema(item)
    assert instance.name == "Bob"
    assert instance.age == 42


def test_init_positional_object_partial_attrs():
    class ObjSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)
        nickname = typesystem.String(max_length=50)

    item = types.SimpleNamespace(name="Bob")
    instance = ObjSchema(item)
    assert instance.name == "Bob"
    assert "nickname" not in instance.__dict__
    assert not hasattr(instance, "nickname")


def test_init_assert_too_many_positional_args():
    class KwSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)

    with pytest.raises(AssertionError):
        KwSchema({"name": "Alice"}, {"name": "Bob"})


def test_init_assert_positional_and_kwargs():
    class KwSchema(typesystem.Schema):
        name = typesystem.String(max_length=50)

    with pytest.raises(AssertionError):
        KwSchema({"name": "Alice"}, name="Bob")
