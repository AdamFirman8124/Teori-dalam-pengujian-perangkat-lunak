# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 125], [127, 0], [127, 128]]}

import pytest

from typesystem import Integer, Schema, String


class Example(Schema):
    name = String()
    age = Integer(default=0)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def test_init_with_single_dict_positional_arg():
    obj = Example({"name": "alice", "age": 30})
    assert obj["name"] == "alice"
    assert obj["age"] == 30


def test_init_with_single_dict_positional_arg_partial_keys():
    # Keys not present in the dict are simply skipped (no default applied).
    obj = Example({"name": "alice"})
    assert obj["name"] == "alice"
    assert "age" not in obj


def test_init_with_single_object_positional_arg():
    obj = Example(Person(name="bob", age=42))
    assert obj["name"] == "bob"
    assert obj["age"] == 42


def test_init_with_single_object_positional_arg_partial_attrs():
    class Partial:
        pass

    p = Partial()
    p.name = "carl"
    obj = Example(p)
    assert obj["name"] == "carl"
    assert "age" not in obj


def test_init_with_kwargs():
    obj = Example(name="dave", age=50)
    assert obj["name"] == "dave"
    assert obj["age"] == 50


def test_init_with_invalid_kwarg_value_raises_type_error():
    with pytest.raises(TypeError) as excinfo:
        Example(name=None)
    message = str(excinfo.value)
    assert "Invalid argument 'name' for Example()." in message


def test_init_with_default_value_applied():
    obj = Example(name="erin")
    assert obj["name"] == "erin"
    assert obj["age"] == 0


def test_init_with_unknown_kwarg_raises_type_error():
    with pytest.raises(TypeError) as excinfo:
        Example(name="frank", bogus=1)
    message = str(excinfo.value)
    assert "'bogus' is an invalid keyword argument for Example()." in message


def test_init_with_multiple_positional_args_raises_assertion_error():
    with pytest.raises(AssertionError):
        Example({"name": "alice"}, {"name": "bob"})


def test_init_with_positional_arg_and_kwargs_raises_assertion_error():
    with pytest.raises(AssertionError):
        Example({"name": "alice"}, age=1)
