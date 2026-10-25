# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

from types import SimpleNamespace

import pytest
import typesystem
from typesystem.fields import Field


@pytest.fixture
def example_schema(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class Example(typesystem.Schema):
        name = typesystem.String()
        count = typesystem.Integer(default=7)
        optional = typesystem.String()

    return Example


def test_schema_initializes_from_dict_without_validation_or_defaults(example_schema):
    instance = example_schema(
        {
            "name": 123,
            "optional": "present",
            "unknown": "ignored",
        }
    )

    assert instance.name == 123
    assert instance.optional == "present"
    assert not hasattr(instance, "count")
    assert not hasattr(instance, "unknown")


def test_schema_initializes_from_object_attributes(example_schema):
    source = SimpleNamespace(name="Alice", count=4, unknown="ignored")

    instance = example_schema(source)

    assert instance.name == "Alice"
    assert instance.count == 4
    assert not hasattr(instance, "optional")
    assert not hasattr(instance, "unknown")


def test_schema_rejects_more_than_one_positional_argument(example_schema):
    with pytest.raises(AssertionError):
        example_schema({"name": "Alice"}, {"name": "Bob"})


def test_schema_rejects_positional_and_keyword_arguments(example_schema):
    with pytest.raises(AssertionError):
        example_schema({"name": "Alice"}, count=4)


def test_schema_validates_keywords_and_applies_defaults(example_schema):
    instance = example_schema(name="Alice", optional="available")

    assert instance.name == "Alice"
    assert instance.count == 7
    assert instance.optional == "available"


def test_schema_rejects_invalid_field_value(example_schema):
    with pytest.raises(TypeError) as exc_info:
        example_schema(name=123)

    message = str(exc_info.value)
    assert message.startswith("Invalid argument 'name' for Example().")
    assert len(message) > len("Invalid argument 'name' for Example().")


def test_schema_rejects_unknown_keyword_after_applying_defaults(example_schema):
    instance = example_schema.__new__(example_schema)

    with pytest.raises(
        TypeError,
        match=r"^'unexpected' is an invalid keyword argument for Example\(\)\.$",
    ):
        example_schema.__init__(instance, unexpected=True)

    assert instance.count == 7
    assert not hasattr(instance, "name")
    assert not hasattr(instance, "optional")
