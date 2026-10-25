# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import pytest
from typesystem.schemas import Schema
from typesystem.fields import String, Integer


def test_init_with_dict_arg_present_and_missing_keys():
    class Person(Schema):
        name = String()
        age = Integer(default=30)

    obj = Person({"name": "Alice", "extra": "ignored"})
    # key present -> setattr, key missing -> skipped, extra ignored
    assert obj.__dict__["name"] == "Alice"
    assert "age" not in obj.__dict__
    assert "extra" not in obj.__dict__


def test_init_with_object_arg_hasattr_true_and_false():
    class Person(Schema):
        name = String()
        age = Integer(default=30)

    class Obj:
        name = "Bob"
        unrelated = "x"

    obj = Person(Obj())
    assert obj.__dict__["name"] == "Bob"
    assert "age" not in obj.__dict__
    assert "unrelated" not in obj.__dict__


def test_init_with_kwargs_valid_value_and_default():
    class Person(Schema):
        name = String()
        age = Integer(default=30)

    # one field supplied (111 True, 114 False), one defaulted (111 False, 124 True)
    obj = Person(name="Carol")
    assert obj.__dict__["name"] == "Carol"
    assert obj.__dict__["age"] == 30

    obj2 = Person(name="Dave", age=25)
    assert obj2.__dict__["name"] == "Dave"
    assert obj2.__dict__["age"] == 25


def test_init_with_kwargs_missing_required_covers_no_default():
    class Mixed(Schema):
        name = String()
        age = Integer(default=30)

    # name: key not in kwargs and has_default() False -> skipped
    # age: key not in kwargs and has_default() True -> default applied
    # kwargs empty at end -> no error (127 False)
    obj = Mixed()
    assert "name" not in obj.__dict__
    assert obj.__dict__["age"] == 30


def test_init_with_kwargs_invalid_value_raises_type_error():
    class Person(Schema):
        name = String()
        age = Integer(default=30)

    # "" is blank and String(allow_blank=False) fails validation
    with pytest.raises(TypeError) as excinfo:
        Person(name="")
    msg = str(excinfo.value)
    assert "Invalid argument 'name'" in msg
    assert "Person" in msg


def test_init_with_invalid_integer_kwarg_raises_type_error():
    class Person(Schema):
        name = String()
        age = Integer()

    with pytest.raises(TypeError) as excinfo:
        Person(name="Frank", age="not-an-int")
    assert "Invalid argument 'age'" in excinfo.value.args[0]
    assert "Person" in excinfo.value.args[0]


def test_init_with_unknown_kwarg_raises_type_error():
    class Person(Schema):
        name = String()
        age = Integer(default=30)

    with pytest.raises(TypeError) as excinfo:
        Person(name="Grace", age=20, unknown=123)
    msg = str(excinfo.value)
    assert "'unknown' is an invalid keyword argument" in msg
    assert "Person" in msg


def test_init_assert_multiple_args_fails():
    class Person(Schema):
        name = String()

    with pytest.raises(AssertionError):
        Person({"name": "a"}, {"name": "b"})


def test_init_assert_args_plus_kwargs_fails():
    class Person(Schema):
        name = String()

    with pytest.raises(AssertionError):
        Person({"name": "a"}, name="b")
