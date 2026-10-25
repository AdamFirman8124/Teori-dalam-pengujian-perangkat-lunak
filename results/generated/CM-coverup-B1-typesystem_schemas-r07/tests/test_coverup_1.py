# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import pytest

from typesystem.fields import Integer, String
from typesystem.schemas import Schema


def test_schema_init_from_dict_copies_only_declared_present_fields():
    class ExampleSchema(Schema):
        name = String()
        count = Integer()

    instance = ExampleSchema({"name": 123, "extra": "ignored"})

    assert instance.name == 123
    assert not hasattr(instance, "count")
    assert not hasattr(instance, "extra")


def test_schema_init_from_object_copies_only_existing_declared_attributes():
    class ExampleSchema(Schema):
        name = String()
        count = Integer()

    class Source:
        name = "Alice"

    instance = ExampleSchema(Source())

    assert instance.name == "Alice"
    assert not hasattr(instance, "count")


def test_schema_init_rejects_multiple_positional_arguments():
    class ExampleSchema(Schema):
        name = String()

    with pytest.raises(AssertionError):
        ExampleSchema({"name": "Alice"}, {"name": "Bob"})


def test_schema_init_rejects_positional_and_keyword_arguments_together():
    class ExampleSchema(Schema):
        name = String()

    with pytest.raises(AssertionError):
        ExampleSchema({"name": "Alice"}, name="Bob")


def test_schema_init_validates_keywords_and_sets_defaults():
    class ExampleSchema(Schema):
        name = String(trim_whitespace=True)
        count = Integer(default=7)
        optional = String()

    instance = ExampleSchema(name="  Alice  ")

    assert instance.name == "Alice"
    assert instance.count == 7
    assert not hasattr(instance, "optional")


def test_schema_init_raises_type_error_for_invalid_field_value():
    class ExampleSchema(Schema):
        name = String(min_length=3)

    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(name="x")

    message = str(exc_info.value)
    assert "Invalid argument 'name' for ExampleSchema()." in message
    assert "Must have at least 3 characters." in message


def test_schema_init_rejects_unknown_keyword_argument():
    class ExampleSchema(Schema):
        name = String()

    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(name="Alice", unexpected=True)

    assert (
        str(exc_info.value)
        == "'unexpected' is an invalid keyword argument for ExampleSchema()."
    )
