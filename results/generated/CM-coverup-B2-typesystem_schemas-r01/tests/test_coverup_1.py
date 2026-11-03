# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import types

import pytest
import typesystem


class PersonSchema(typesystem.Schema):
    name = typesystem.String(max_length=10)
    age = typesystem.Integer()


class DefaultedSchema(typesystem.Schema):
    name = typesystem.String(default="anonymous")
    age = typesystem.Integer(default=0)


def test_init_with_full_dict_sets_all_fields():
    person = PersonSchema({"name": "Tom", "age": 3})
    assert person.name == "Tom"
    assert person.age == 3


def test_init_with_partial_dict_leaves_missing_fields_unset():
    person = PersonSchema({"name": "Tom"})
    assert person.name == "Tom"
    with pytest.raises(AttributeError):
        person.age  # noqa: B018


def test_init_with_dict_ignores_non_field_keys():
    person = PersonSchema({"name": "Tom", "bogus": "ignored"})
    assert person.name == "Tom"
    assert not hasattr(person, "bogus")


def test_init_with_object_copies_matching_attributes():
    source = types.SimpleNamespace(name="FromObject", age=7)
    person = PersonSchema(source)
    assert person.name == "FromObject"
    assert person.age == 7


def test_init_with_object_skips_missing_attributes():
    source = types.SimpleNamespace(name="FromObject")
    person = PersonSchema(source)
    assert person.name == "FromObject"
    with pytest.raises(AttributeError):
        person.age  # noqa: B018


def test_init_with_multiple_positional_args_asserts():
    with pytest.raises(AssertionError):
        PersonSchema({"name": "Tom"}, {"name": "Anna"})


def test_init_with_positional_arg_and_kwargs_asserts():
    with pytest.raises(AssertionError):
        PersonSchema({"name": "Tom"}, age=3)


def test_init_with_valid_kwargs_sets_validated_fields():
    person = PersonSchema(name="Tom", age=3)
    assert person.name == "Tom"
    assert person.age == 3


def test_init_with_partial_kwargs_leaves_other_fields_unset():
    person = PersonSchema(name="Tom")
    assert person.name == "Tom"
    with pytest.raises(AttributeError):
        person.age  # noqa: B018


def test_init_uses_defaults_for_missing_kwargs():
    person = DefaultedSchema()
    assert person.name == "anonymous"
    assert person.age == 0


def test_init_with_invalid_string_kwarg_raises_type_error():
    with pytest.raises(TypeError) as excinfo:
        PersonSchema(name="this name is far too long")
    assert str(excinfo.value).startswith("Invalid argument 'name' for PersonSchema(). ")


def test_init_with_invalid_integer_kwarg_raises_type_error():
    with pytest.raises(TypeError) as excinfo:
        PersonSchema(age="not a number")
    assert str(excinfo.value).startswith("Invalid argument 'age' for PersonSchema(). ")


def test_init_with_unknown_kwarg_raises_type_error():
    with pytest.raises(TypeError) as excinfo:
        PersonSchema(bogus=1)
    assert str(excinfo.value) == "'bogus' is an invalid keyword argument for PersonSchema()."


def test_init_with_valid_and_unknown_kwargs_raises_type_error():
    with pytest.raises(TypeError) as excinfo:
        PersonSchema(name="Tom", bogus=1)
    assert "'bogus' is an invalid keyword argument for PersonSchema()." in str(excinfo.value)
