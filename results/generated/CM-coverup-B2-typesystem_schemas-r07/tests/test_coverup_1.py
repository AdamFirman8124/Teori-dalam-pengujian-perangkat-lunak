# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 125], [127, 0], [127, 128]]}

import pytest

from typesystem import Schema, String, Integer


class ExampleSchema(Schema):
    name = String(default="unnamed")
    age = Integer(default=0)


def test_init_with_dict_arg():
    instance = ExampleSchema({"name": "alice", "age": 30})
    assert instance["name"] == "alice"
    assert instance["age"] == 30


def test_init_with_dict_arg_partial():
    # The dict/object branch returns early, so defaults are NOT applied.
    instance = ExampleSchema({"name": "bob"})
    assert instance["name"] == "bob"
    assert instance.name == "bob"
    assert "age" not in instance
    with pytest.raises(KeyError):
        instance["age"]


def test_init_with_object_arg():
    class Source:
        pass

    source = Source()
    source.name = "carol"
    source.age = 42
    instance = ExampleSchema(source)
    assert instance["name"] == "carol"
    assert instance["age"] == 42


def test_init_with_object_arg_missing_attrs():
    class Source:
        pass

    source = Source()
    source.name = "dave"
    instance = ExampleSchema(source)
    assert instance["name"] == "dave"
    assert "age" not in instance
    with pytest.raises(KeyError):
        instance["age"]


def test_init_with_valid_kwargs():
    instance = ExampleSchema(name="eve", age=25)
    assert instance["name"] == "eve"
    assert instance["age"] == 25


def test_init_with_invalid_kwarg_raises_type_error():
    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(age="not-an-integer")
    assert "Invalid argument 'age' for ExampleSchema()." in str(exc_info.value)


def test_init_with_unknown_kwarg_raises_type_error():
    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(bogus=1)
    assert "'bogus' is an invalid keyword argument for ExampleSchema()." in str(
        exc_info.value
    )


def test_init_with_no_args_uses_defaults():
    instance = ExampleSchema()
    assert instance["name"] == "unnamed"
    assert instance["age"] == 0


def test_init_with_multiple_args_fails():
    with pytest.raises(AssertionError):
        ExampleSchema({}, {})


def test_init_with_args_and_kwargs_fails():
    with pytest.raises(AssertionError):
        ExampleSchema({}, name="alice")
