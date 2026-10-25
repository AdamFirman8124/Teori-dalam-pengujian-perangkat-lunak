# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem.base import ValidationError
from typesystem.schemas import Reference, Schema


def test_reference_with_schema_target_resolves_target_and_target_string():
    class TargetSchema(Schema):
        pass

    reference = Reference(TargetSchema)

    assert reference.target is TargetSchema
    assert reference.target_string == "TargetSchema"
    assert reference.target_string == "TargetSchema"


def test_reference_rejects_non_schema_class_target():
    with pytest.raises(AssertionError):
        Reference(dict)


def test_string_reference_resolves_target_from_definitions_and_caches_it():
    class TargetSchema(Schema):
        pass

    definitions = {"Target": TargetSchema}
    reference = Reference("Target", definitions=definitions)

    assert reference.target_string == "Target"
    assert reference.target is TargetSchema

    definitions["Target"] = object
    assert reference.target is TargetSchema


def test_string_reference_without_definitions_raises_assertion():
    reference = Reference("Target")

    with pytest.raises(
        AssertionError, match="String reference missing 'definitions'"
    ):
        _ = reference.target


def test_reference_validate_handles_null_and_delegates_strict_validation():
    calls = []
    validated_value = object()

    class TargetSchema(Schema):
        @classmethod
        def validate(cls, value, *, strict=False):
            calls.append((value, strict))
            return validated_value

    nullable_reference = Reference(TargetSchema, allow_null=True)
    assert nullable_reference.validate(None) is None
    assert calls == []

    reference = Reference(TargetSchema)

    with pytest.raises(ValidationError, match="May not be null"):
        reference.validate(None)

    value = {"example": "value"}
    assert reference.validate(value, strict=True) is validated_value
    assert calls == [(value, True)]


def test_reference_serialize_handles_none_and_mapping_values():
    class TargetSchema(Schema):
        pass

    reference = Reference(TargetSchema)
    value = {"key": "value"}

    assert reference.serialize(None) is None

    serialized = reference.serialize(value)
    assert serialized == value
    assert serialized is not value
