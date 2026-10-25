# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import pytest

import typesystem


class ExampleSchema(typesystem.Schema):
    name = typesystem.String()
    age = typesystem.Integer(default=0)


class OtherSchema(typesystem.Schema):
    title = typesystem.String()


def test_init_with_positional_dict():
    instance = ExampleSchema({"name": "alice", "age": 30})
    assert instance.name == "alice"
    assert instance.age == 30


def test_init_with_positional_dict_partial():
    instance = ExampleSchema({"name": "bob"})
    assert instance.name == "bob"
    # The dict branch only sets keys present in the dict; defaults are not applied.
    assert not hasattr(instance, "age")


def test_init_with_positional_object():
    class Obj:
        pass

    obj = Obj()
    obj.name = "carol"
    obj.age = 42
    instance = ExampleSchema(obj)
    assert instance.name == "carol"
    assert instance.age == 42


def test_init_with_positional_object_missing_attrs():
    class Obj:
        pass

    obj = Obj()
    obj.name = "dave"
    instance = ExampleSchema(obj)
    assert instance.name == "dave"
    assert not hasattr(instance, "age")


def test_init_with_positional_dict_and_kwargs_rejected():
    with pytest.raises(AssertionError):
        ExampleSchema({"name": "eve"}, extra="kwarg")


def test_init_with_multiple_positional_args_rejected():
    with pytest.raises(AssertionError):
        ExampleSchema({"name": "eve"}, {"name": "frank"})


def test_init_with_kwargs():
    instance = ExampleSchema(name="grace", age=33)
    assert instance.name == "grace"
    assert instance.age == 33


def test_init_with_kwargs_applies_defaults():
    instance = ExampleSchema(name="heidi")
    assert instance.name == "heidi"
    assert instance.age == 0


def test_init_with_invalid_kwarg_value_raises_type_error():
    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(name=123)
    assert "Invalid argument 'name' for ExampleSchema()." in str(exc_info.value)


def test_init_with_invalid_kwarg_value_error_text():
    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(age="not a number")
    message = str(exc_info.value)
    assert "Invalid argument 'age' for ExampleSchema()." in message
    assert "Must be a number." in message


def test_init_with_unknown_kwarg_raises_type_error():
    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(bogus="value")
    assert "'bogus' is an invalid keyword argument for ExampleSchema()." in str(
        exc_info.value
    )


def test_init_with_no_arguments():
    instance = OtherSchema()
    assert not hasattr(instance, "title")
