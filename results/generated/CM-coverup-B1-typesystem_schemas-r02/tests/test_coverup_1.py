# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import pytest

from typesystem.fields import Field
from typesystem.schemas import Schema


def test_schema_init_from_dict_and_object(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class PassthroughField(Field):
        pass

    class ExampleSchema(Schema):
        first = PassthroughField()
        second = PassthroughField()

    from_dict = ExampleSchema({"first": "dict value", "ignored": "unused"})

    assert from_dict.first == "dict value"
    assert not hasattr(from_dict, "second")
    assert not hasattr(from_dict, "ignored")

    class Source:
        second = "object value"

    from_object = ExampleSchema(Source())

    assert not hasattr(from_object, "first")
    assert from_object.second == "object value"


def test_schema_positional_argument_assertions(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class PassthroughField(Field):
        pass

    class ExampleSchema(Schema):
        value = PassthroughField()

    with pytest.raises(AssertionError):
        ExampleSchema({}, {})

    with pytest.raises(AssertionError):
        ExampleSchema({}, value="not allowed with positional arguments")


def test_schema_keyword_validation_defaults_and_missing_values(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class ValidatingField(Field):
        def validate_or_error(self, value, *, strict=False):
            return value.upper(), None

        def has_default(self):
            return False

    class DefaultField(Field):
        def has_default(self):
            return True

        def get_default_value(self):
            return "default value"

    class RequiredField(Field):
        def has_default(self):
            return False

    class ExampleSchema(Schema):
        supplied = ValidatingField()
        defaulted = DefaultField()
        missing = RequiredField()

    instance = ExampleSchema(supplied="accepted")

    assert instance.supplied == "ACCEPTED"
    assert instance.defaulted == "default value"
    assert not hasattr(instance, "missing")


def test_schema_invalid_field_value_raises_descriptive_type_error(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class Message:
        def __init__(self, text):
            self.text = text

    class Error:
        def messages(self):
            return [Message("first problem"), Message("second problem")]

    class RejectingField(Field):
        def validate_or_error(self, value, *, strict=False):
            return None, Error()

    class ExampleSchema(Schema):
        value = RejectingField()

    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(value="invalid")

    assert str(exc_info.value) == (
        "Invalid argument 'value' for ExampleSchema(). "
        "first problem second problem"
    )


def test_schema_rejects_unknown_keyword_argument(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class ValidatingField(Field):
        def validate_or_error(self, value, *, strict=False):
            return value, None

        def has_default(self):
            return False

    class ExampleSchema(Schema):
        value = ValidatingField()

    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(value="valid", extra="unexpected")

    assert str(exc_info.value) == (
        "'extra' is an invalid keyword argument for ExampleSchema()."
    )
