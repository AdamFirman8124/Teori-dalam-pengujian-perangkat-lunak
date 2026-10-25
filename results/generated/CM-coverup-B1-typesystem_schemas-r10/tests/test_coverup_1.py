# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

import types

import pytest

from typesystem.fields import Field
from typesystem.schemas import Schema


class _StubField(Field):
    def __init__(self, *, result=None, error=None, has_default=False, default=None):
        super().__init__()
        self.result = result
        self.error = error
        self.default_available = has_default
        self.default_value = default
        self.calls = []

    def validate_or_error(self, value, *, strict=False):
        self.calls.append((value, strict))
        return self.result, self.error

    def has_default(self):
        return self.default_available

    def get_default_value(self):
        return self.default_value


def test_schema_positional_initialization_and_argument_assertions(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)
    first_field = _StubField()
    second_field = _StubField()

    class PositionalSchema(Schema):
        first = first_field
        second = second_field

    from_dict = PositionalSchema(
        {"first": "dictionary value", "unknown": "ignored"}
    )

    assert from_dict.first == "dictionary value"
    assert not hasattr(from_dict, "second")
    assert first_field.calls == []
    assert second_field.calls == []

    source = types.SimpleNamespace(first="object value", unknown="ignored")
    from_object = PositionalSchema(source)

    assert from_object.first == "object value"
    assert not hasattr(from_object, "second")
    assert first_field.calls == []
    assert second_field.calls == []

    with pytest.raises(AssertionError):
        PositionalSchema({}, {})

    with pytest.raises(AssertionError):
        PositionalSchema({}, unexpected=True)


def test_schema_keyword_validation_defaults_and_missing_values(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)
    supplied_field = _StubField(result="normalized")
    defaulted_field = _StubField(has_default=True, default="default value")
    absent_field = _StubField()

    class KeywordSchema(Schema):
        supplied = supplied_field
        defaulted = defaulted_field
        absent = absent_field

    instance = KeywordSchema(supplied="raw value")

    assert instance.supplied == "normalized"
    assert instance.defaulted == "default value"
    assert not hasattr(instance, "absent")
    assert supplied_field.calls == [("raw value", False)]
    assert defaulted_field.calls == []
    assert absent_field.calls == []


def test_schema_invalid_field_value_raises_descriptive_type_error(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    validation_error = types.SimpleNamespace(
        messages=lambda: [
            types.SimpleNamespace(text="first problem"),
            types.SimpleNamespace(text="second problem"),
        ]
    )
    invalid_field = _StubField(result=None, error=validation_error)

    class InvalidSchema(Schema):
        value = invalid_field

    with pytest.raises(
        TypeError,
        match=(
            r"^Invalid argument 'value' for InvalidSchema\(\)\. "
            r"first problem second problem$"
        ),
    ):
        InvalidSchema(value="invalid value")

    assert invalid_field.calls == [("invalid value", False)]


def test_schema_rejects_unknown_keyword_argument(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)
    known_field = _StubField()

    class KeywordSchema(Schema):
        known = known_field

    with pytest.raises(
        TypeError,
        match=r"^'extra' is an invalid keyword argument for KeywordSchema\(\)\.$",
    ):
        KeywordSchema(extra="unexpected")

    assert known_field.calls == []
