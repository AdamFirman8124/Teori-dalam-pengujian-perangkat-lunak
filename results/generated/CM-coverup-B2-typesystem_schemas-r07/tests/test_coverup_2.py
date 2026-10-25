# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem.base import ValidationError
from typesystem.fields import Field
from typesystem.schemas import Reference, Schema


def test_reference_with_schema_target_resolves_name_and_validates(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)
    calls = []
    validated = object()

    class TargetSchema(Schema):
        @classmethod
        def validate(cls, value, *, strict=False):
            calls.append((value, strict))
            return validated

    reference = Reference(TargetSchema)

    assert reference.target is TargetSchema
    assert reference.target_string == "TargetSchema"
    assert reference.target_string == "TargetSchema"
    assert reference.validate({"value": 1}, strict=True) is validated
    assert calls == [({"value": 1}, True)]


def test_reference_with_string_target_resolves_from_definitions(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class TargetSchema(Schema):
        pass

    definitions = {"Target": TargetSchema}
    reference = Reference("Target", definitions=definitions)

    assert reference.target_string == "Target"
    assert reference.target is TargetSchema
    assert reference.target is TargetSchema


def test_string_reference_without_definitions_raises_assertion(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)
    reference = Reference("MissingTarget")

    with pytest.raises(
        AssertionError, match="String reference missing 'definitions'\\."
    ):
        _ = reference.target


def test_reference_rejects_non_schema_target(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    with pytest.raises(AssertionError):
        Reference(object)


def test_reference_validate_handles_nullable_none(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class TargetSchema(Schema):
        @classmethod
        def validate(cls, value, *, strict=False):
            raise AssertionError("Target validation must not be called for None")

    reference = Reference(TargetSchema, allow_null=True)

    assert reference.validate(None) is None


def test_reference_validate_rejects_non_nullable_none(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class TargetSchema(Schema):
        pass

    reference = Reference(TargetSchema)

    with pytest.raises(ValidationError) as exc_info:
        reference.validate(None)

    message = exc_info.value.messages()[0]
    assert message.text == "May not be null."
    assert message.code == "null"


def test_reference_serialize_handles_none_and_mapping(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class TargetSchema(Schema):
        pass

    reference = Reference(TargetSchema)
    source = {"name": "example"}
    serialized = reference.serialize(source)

    assert reference.serialize(None) is None
    assert serialized == source
    assert serialized is not source
    assert source == {"name": "example"}
