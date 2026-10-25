# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import pytest

from typesystem import Field, Integer, Schema, String


@pytest.fixture(autouse=True)
def preserve_field_creation_counter(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)


def test_schema_init_from_positional_dict_copies_only_declared_present_fields():
    class Example(Schema):
        name = String()
        age = Integer()

    instance = Example({"name": 123, "extra": "ignored"})

    assert instance.name == 123
    assert not hasattr(instance, "age")
    assert not hasattr(instance, "extra")


def test_schema_init_from_positional_object_copies_existing_declared_attributes():
    class Example(Schema):
        name = String()
        age = Integer()

    class Source:
        name = "Alice"
        extra = "ignored"

    instance = Example(Source())

    assert instance.name == "Alice"
    assert not hasattr(instance, "age")
    assert not hasattr(instance, "extra")


def test_schema_init_rejects_multiple_positional_arguments_and_mixed_arguments():
    class Example(Schema):
        name = String()

    with pytest.raises(AssertionError):
        Example({"name": "Alice"}, {"name": "Bob"})

    with pytest.raises(AssertionError):
        Example({"name": "Alice"}, name="Bob")


def test_schema_init_validates_keywords_applies_defaults_and_leaves_optional_missing():
    class Example(Schema):
        name = String()
        nickname = String(default="anonymous")
        age = Integer()

    instance = Example(name="  Alice  ")

    assert instance.name == "Alice"
    assert instance.nickname == "anonymous"
    assert not hasattr(instance, "age")


def test_schema_init_reports_invalid_field_value():
    class Example(Schema):
        name = String(min_length=3)

    with pytest.raises(TypeError) as exc_info:
        Example(name="x")

    message = str(exc_info.value)
    assert message.startswith("Invalid argument 'name' for Example().")
    assert "Must have at least 3 characters." in message


def test_schema_init_rejects_unknown_keyword_argument():
    class Example(Schema):
        name = String()

    with pytest.raises(TypeError) as exc_info:
        Example(name="Alice", unexpected=True)

    assert (
        str(exc_info.value)
        == "'unexpected' is an invalid keyword argument for Example()."
    )
