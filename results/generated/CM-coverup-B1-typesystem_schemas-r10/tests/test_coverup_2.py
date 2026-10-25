# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem.base import ValidationError
from typesystem.fields import Field
from typesystem.schemas import Reference, Schema


def test_reference_with_schema_class_resolves_target_and_target_string(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class LocalSchema(Schema):
        pass

    reference = Reference(LocalSchema)

    assert reference.target is LocalSchema
    assert "_target_string" not in reference.__dict__
    assert reference.target_string == "LocalSchema"
    assert reference.__dict__["_target_string"] == "LocalSchema"

    with pytest.raises(AssertionError):
        Reference(int)


def test_string_reference_resolves_definition_and_requires_definitions(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    target = Field()
    definitions = {"Target": target}
    reference = Reference("Target", definitions=definitions)

    assert reference.target_string == "Target"
    assert "_target" not in reference.__dict__
    assert reference.target is target
    assert reference.__dict__["_target"] is target

    definitions["Target"] = Field()
    assert reference.target is target

    unresolved = Reference("Target")
    with pytest.raises(
        AssertionError, match="String reference missing 'definitions'"
    ):
        _ = unresolved.target


def test_reference_validate_handles_null_and_delegates_strict(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    calls = []
    validated_value = object()

    class TrackingField(Field):
        def validate(self, value, *, strict=False):
            calls.append((value, strict))
            return validated_value

    target = TrackingField()
    definitions = {"Target": target}

    nullable_reference = Reference(
        "Target", definitions=definitions, allow_null=True
    )
    assert nullable_reference.validate(None) is None
    assert calls == []

    required_reference = Reference("Target", definitions=definitions)
    with pytest.raises(ValidationError, match="May not be null"):
        required_reference.validate(None)
    assert calls == []

    value = object()
    assert required_reference.validate(value, strict=True) is validated_value
    assert calls == [(value, True)]


def test_reference_serialize_handles_none_and_mapping(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    reference = Reference("Target", definitions={"Target": Field()})

    assert reference.serialize(None) is None

    original = {"answer": 42}
    serialized = reference.serialize(original)

    assert serialized == original
    assert serialized is not original
