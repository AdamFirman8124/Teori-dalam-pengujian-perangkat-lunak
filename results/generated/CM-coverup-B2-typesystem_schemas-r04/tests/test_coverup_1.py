# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}

from types import SimpleNamespace

import pytest

from typesystem.fields import Field
from typesystem.schemas import Schema


class StubField(Field):
    def __init__(self, *, transform=None, error=None, default=None, has_default=False):
        super().__init__()
        self.transform = transform or (lambda value: value)
        self.error = error
        self.default_value = default
        self.default_available = has_default

    def validate_or_error(self, value, *, strict=False):
        return self.transform(value), self.error

    def has_default(self):
        return self.default_available

    def get_default_value(self):
        return self.default_value


@pytest.fixture(autouse=True)
def restore_field_creation_counter(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)


def test_schema_init_from_dict_copies_only_declared_present_fields():
    class ExampleSchema(Schema):
        first = StubField()
        second = StubField()

    instance = ExampleSchema({"first": 123, "undeclared": "ignored"})

    assert instance.first == 123
    assert not hasattr(instance, "second")
    assert not hasattr(instance, "undeclared")


def test_schema_init_from_object_copies_only_existing_declared_attributes():
    class ExampleSchema(Schema):
        first = StubField()
        second = StubField()

    source = SimpleNamespace(first="copied", undeclared="ignored")
    instance = ExampleSchema(source)

    assert instance.first == "copied"
    assert not hasattr(instance, "second")
    assert not hasattr(instance, "undeclared")


def test_schema_positional_init_requires_exactly_one_argument():
    class ExampleSchema(Schema):
        value = StubField()

    with pytest.raises(AssertionError):
        ExampleSchema({"value": 1}, {"value": 2})


def test_schema_positional_init_rejects_keyword_arguments():
    class ExampleSchema(Schema):
        value = StubField()

    with pytest.raises(AssertionError):
        ExampleSchema({"value": 1}, value=2)


def test_schema_keyword_init_validates_values_and_applies_defaults():
    class ExampleSchema(Schema):
        supplied = StubField(transform=lambda value: value.upper())
        defaulted = StubField(default="fallback", has_default=True)
        omitted = StubField()

    instance = ExampleSchema(supplied="accepted")

    assert instance.supplied == "ACCEPTED"
    assert instance.defaulted == "fallback"
    assert not hasattr(instance, "omitted")


def test_schema_keyword_init_reports_field_validation_errors():
    class DummyError:
        def messages(self):
            return [
                SimpleNamespace(text="first issue"),
                SimpleNamespace(text="second issue"),
            ]

    class InvalidSchema(Schema):
        value = StubField(error=DummyError())

    with pytest.raises(TypeError) as exc_info:
        InvalidSchema(value="invalid")

    assert str(exc_info.value) == (
        "Invalid argument 'value' for InvalidSchema(). "
        "first issue second issue"
    )


def test_schema_keyword_init_rejects_unknown_keyword_arguments():
    class ExampleSchema(Schema):
        value = StubField()

    with pytest.raises(TypeError) as exc_info:
        ExampleSchema(value="valid", unexpected="invalid")

    assert str(exc_info.value) == (
        "'unexpected' is an invalid keyword argument for ExampleSchema()."
    )
