# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem import fields
from typesystem.base import ValidationError
from typesystem.schemas import Reference, Schema


class ExampleSchema(Schema):
    name = fields.String()


def test_reference_with_schema_class_sets_target():
    # Covers lines 219-220 (assert issubclass + self._target = to)
    reference = Reference(to=ExampleSchema)

    assert reference.to is ExampleSchema
    assert reference.definitions is None
    assert reference.target is ExampleSchema
    assert not hasattr(reference, "_target_string")


def test_reference_with_string_sets_target_string():
    # Covers the isinstance(to, str) branch
    reference = Reference(to="ExampleSchema")

    assert reference.to == "ExampleSchema"
    assert reference.target_string == "ExampleSchema"
    assert not hasattr(reference, "_target")


def test_reference_target_string_derived_from_target():
    # Covers lines 224-226 (lazy _target_string from _target.__name__)
    reference = Reference(to=ExampleSchema)

    assert not hasattr(reference, "_target_string")
    assert reference.target_string == "ExampleSchema"
    assert reference._target_string == "ExampleSchema"
    # Second access hits the cached value (line 226 again)
    assert reference.target_string == "ExampleSchema"


def test_reference_target_resolved_from_definitions():
    # Covers lines 230-235 (lazy _target lookup in definitions)
    definitions = {"ExampleSchema": ExampleSchema}
    reference = Reference(to="ExampleSchema", definitions=definitions)

    assert not hasattr(reference, "_target")
    assert reference.target is ExampleSchema
    assert reference._target is ExampleSchema
    # Second access hits the cached value
    assert reference.target is ExampleSchema


def test_reference_target_without_definitions_raises():
    # Covers the assertion failure path in lines 231-233
    reference = Reference(to="ExampleSchema")

    with pytest.raises(AssertionError) as exc_info:
        reference.target

    assert "String reference missing 'definitions'." in str(exc_info.value)
    assert not hasattr(reference, "_target")


def test_reference_validate_null_allowed():
    # Covers lines 238-239
    reference = Reference(to=ExampleSchema, allow_null=True)

    assert reference.validate(None) is None


def test_reference_validate_null_not_allowed():
    # Covers lines 240-241
    reference = Reference(to=ExampleSchema)

    with pytest.raises(ValidationError) as exc_info:
        reference.validate(None)

    messages = exc_info.value.messages()
    assert [message.text for message in messages] == ["May not be null."]
    assert [message.code for message in messages] == ["null"]


def test_reference_validate_delegates_to_target():
    # Covers line 242 (Schema.validate returns a Schema instance)
    reference = Reference(to=ExampleSchema)

    result = reference.validate({"name": "example"})
    assert isinstance(result, ExampleSchema)
    assert dict(result) == {"name": "example"}

    with pytest.raises(ValidationError):
        reference.validate({})


def test_reference_validate_delegates_to_string_target():
    # Covers line 242 via the definitions-resolved target
    definitions = {"ExampleSchema": ExampleSchema}
    reference = Reference(to="ExampleSchema", definitions=definitions)

    result = reference.validate({"name": "example"})
    assert isinstance(result, ExampleSchema)
    assert dict(result) == {"name": "example"}


def test_reference_serialize():
    # Covers lines 245-247
    reference = Reference(to=ExampleSchema)

    assert reference.serialize(None) is None
    assert reference.serialize({"name": "example"}) == {"name": "example"}

    instance = ExampleSchema({"name": "example"})
    serialized = reference.serialize(instance)
    assert serialized == {"name": "example"}
    assert serialized is not instance
