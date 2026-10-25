# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import pytest
import typesystem


def test_schema_init_from_dict_copies_only_known_present_fields():
    class Example(typesystem.Schema):
        name = typesystem.String()
        missing = typesystem.String()

    instance = Example({"name": "Alice", "unknown": "ignored"})

    assert instance.name == "Alice"
    assert not hasattr(instance, "missing")
    assert not hasattr(instance, "unknown")


def test_schema_init_from_object_copies_only_existing_known_attributes():
    class Example(typesystem.Schema):
        name = typesystem.String()
        missing = typesystem.String()

    class Source:
        name = "Alice"
        unknown = "ignored"

    instance = Example(Source())

    assert instance.name == "Alice"
    assert not hasattr(instance, "missing")
    assert not hasattr(instance, "unknown")


def test_schema_init_rejects_multiple_positional_arguments():
    class Example(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(AssertionError):
        Example({"name": "Alice"}, {"name": "Bob"})


def test_schema_init_rejects_positional_and_keyword_arguments_together():
    class Example(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(AssertionError):
        Example({"name": "Alice"}, name="Bob")


def test_schema_init_validates_keywords_and_applies_defaults():
    class Example(typesystem.Schema):
        count = typesystem.Integer()
        label = typesystem.String(default="fallback")
        optional = typesystem.String()

    instance = Example(count=3)

    assert instance.count == 3
    assert instance.label == "fallback"
    assert not hasattr(instance, "optional")


def test_schema_init_raises_type_error_for_invalid_field_value():
    class Example(typesystem.Schema):
        count = typesystem.Integer()

    with pytest.raises(TypeError) as exc_info:
        Example(count="not-an-integer")

    message = str(exc_info.value)
    assert message.startswith("Invalid argument 'count' for Example(). ")
    assert len(message) > len("Invalid argument 'count' for Example(). ")


def test_schema_init_rejects_unknown_keyword_argument():
    class Example(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(
        TypeError,
        match=r"^'extra' is an invalid keyword argument for Example\(\)\.$",
    ):
        Example(extra="value")
