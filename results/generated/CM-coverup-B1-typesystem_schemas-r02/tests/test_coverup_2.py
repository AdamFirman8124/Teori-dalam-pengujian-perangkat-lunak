# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem.base import ValidationError
from typesystem.fields import Field
from typesystem.schemas import Reference, Schema


def test_reference_with_schema_class(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class TargetSchema(Schema):
        pass

    reference = Reference(TargetSchema)

    assert reference.target is TargetSchema
    assert reference.target_string == "TargetSchema"
    assert reference.target_string == "TargetSchema"

    with pytest.raises(AssertionError):
        Reference(dict)


def test_string_reference_resolves_and_delegates_validation(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    class RecordingField(Field):
        def __init__(self):
            super().__init__()
            self.calls = []

        def validate(self, value, *, strict=False):
            self.calls.append((value, strict))
            return f"validated:{value}"

    target = RecordingField()
    reference = Reference("item", definitions={"item": target})

    assert reference.target_string == "item"
    assert reference.target is target
    assert reference.target is target
    assert reference.validate("value", strict=True) == "validated:value"
    assert target.calls == [("value", True)]


def test_string_reference_requires_definitions(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    reference = Reference("item")

    with pytest.raises(
        AssertionError, match="String reference missing 'definitions'"
    ):
        _ = reference.target


def test_reference_null_validation_and_serialization(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    nullable = Reference("item", definitions={}, allow_null=True)
    non_nullable = Reference("item", definitions={})

    assert nullable.validate(None) is None

    with pytest.raises(ValidationError, match="May not be null"):
        non_nullable.validate(None)

    assert non_nullable.serialize(None) is None

    source = {"name": "example"}
    serialized = non_nullable.serialize(source)

    assert serialized == source
    assert serialized is not source
