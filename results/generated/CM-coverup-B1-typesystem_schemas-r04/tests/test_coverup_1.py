# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 125], [127, 0], [127, 128]]}

import pytest

from typesystem import String, Schema


class ExampleSchema(Schema):
    name = String(default="anon")
    age = String()


class Other:
    def __init__(self) -> None:
        self.name = "from-attr"
        self.age = "42"


def test_init_with_dict_arg():
    instance = ExampleSchema({"name": "alice", "age": "30"})
    assert instance["name"] == "alice"
    assert instance["age"] == "30"


def test_init_with_dict_arg_partial():
    # The args path only sets keys present in the dict; defaults are not applied.
    instance = ExampleSchema({"age": "30"})
    assert instance["age"] == "30"
    with pytest.raises(KeyError):
        instance["name"]


def test_init_with_object_arg():
    instance = ExampleSchema(Other())
    assert instance["name"] == "from-attr"
    assert instance["age"] == "42"


def test_init_with_object_arg_partial():
    class Partial:
        name = "only-name"

    # The args path only copies attributes that exist on the item.
    instance = ExampleSchema(Partial())
    assert instance["name"] == "only-name"
    with pytest.raises(KeyError):
        instance["age"]


def test_init_with_multiple_args_raises():
    with pytest.raises(AssertionError):
        ExampleSchema({"name": "a"}, {"name": "b"})


def test_init_with_args_and_kwargs_raises():
    with pytest.raises(AssertionError):
        ExampleSchema({"name": "a"}, age="30")


def test_init_with_kwargs():
    instance = ExampleSchema(name="bob", age="55")
    assert instance["name"] == "bob"
    assert instance["age"] == "55"


def test_init_with_default_only():
    instance = ExampleSchema(age="1")
    assert instance["name"] == "anon"
    assert instance["age"] == "1"


def test_init_with_invalid_kwarg_value_raises_typeerror():
    with pytest.raises(TypeError) as excinfo:
        ExampleSchema(name=123, age="1")
    assert "Invalid argument 'name' for ExampleSchema()." in str(excinfo.value)


def test_init_with_unknown_kwarg_raises_typeerror():
    with pytest.raises(TypeError) as excinfo:
        ExampleSchema(age="1", bogus="x")
    assert "'bogus' is an invalid keyword argument for ExampleSchema()." in str(
        excinfo.value
    )
