# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem.base import ValidationError
from typesystem.fields import Field
from typesystem.schemas import Reference, Schema


@pytest.fixture(autouse=True)
def restore_field_creation_counter(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)


def test_reference_with_schema_class_resolves_target_and_target_string():
    class TargetSchema(Schema):
        pass

    reference = Reference(TargetSchema)

    assert reference.target is TargetSchema
    assert reference.target_string == "TargetSchema"
    assert reference.target_string == "TargetSchema"


def test_reference_rejects_non_schema_class():
    with pytest.raises(AssertionError):
        Reference(object)


def test_string_reference_resolves_definition_and_forwards_strict_validation():
    calls = []

    class RecordingField(Field):
        def validate(self, value, *, strict=False):
            calls.append((value, strict))
            return {"validated": value}

    target = RecordingField()
    reference = Reference("target", definitions={"target": target})

    assert reference.target_string == "target"
    assert reference.target is target
    assert reference.target is target
    assert reference.validate("value", strict=True) == {"validated": "value"}
    assert calls == [("value", True)]


def test_string_reference_without_definitions_raises_assertion():
    reference = Reference("missing")

    with pytest.raises(
        AssertionError, match="String reference missing 'definitions'"
    ):
        reference.target


def test_reference_validate_handles_nullable_and_non_nullable_none():
    nullable = Reference("unused", allow_null=True)
    required = Reference("unused")

    assert nullable.validate(None) is None

    with pytest.raises(ValidationError) as exc_info:
        required.validate(None)

    assert "May not be null." in str(exc_info.value)


def test_reference_serialize_handles_none_and_mapping_values():
    class TargetSchema(Schema):
        pass

    reference = Reference(TargetSchema)
    source = {"name": "example"}

    assert reference.serialize(None) is None

    serialized = reference.serialize(source)
    assert serialized == source
    assert serialized is not source
