# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem.fields import String
from typesystem.schemas import Reference, Schema


class ExampleSchema(Schema):
    name = String()


class OtherSchema(Schema):
    value = String()


def test_reference_with_schema_class_sets_target():
    # Covers lines 219-220: non-string `to` asserts subclass and stores target.
    reference = Reference(to=ExampleSchema)

    assert reference.to is ExampleSchema
    assert reference.definitions is None
    assert reference.target is ExampleSchema
    assert not hasattr(reference, "_target_string")


def test_reference_with_non_schema_class_raises_assertion_error():
    # Covers the assert branch at line 219.
    with pytest.raises(AssertionError):
        Reference(to=int)


def test_target_string_from_schema_class():
    # Covers lines 224-226: lazily derives the name from the target class.
    reference = Reference(to=ExampleSchema)

    assert reference.target_string == "ExampleSchema"
    # Cached on the instance, so a second access reuses the stored value.
    assert reference._target_string == "ExampleSchema"
    assert reference.target_string == "ExampleSchema"


def test_target_string_from_string_reference():
    # Covers the already-set branch of line 224.
    reference = Reference(to="ExampleSchema", definitions={"ExampleSchema": ExampleSchema})

    assert reference.target_string == "ExampleSchema"
    assert reference._target_string == "ExampleSchema"


def test_target_resolved_from_definitions():
    # Covers lines 230-235: string reference resolved through `definitions`.
    definitions = {"ExampleSchema": ExampleSchema, "OtherSchema": OtherSchema}
    reference = Reference(to="OtherSchema", definitions=definitions)

    assert reference.target is OtherSchema
    assert reference._target is OtherSchema
    # Cached after first resolution.
    assert reference.target is OtherSchema


def test_target_without_definitions_raises_assertion_error():
    # Covers the assertion failure branch at lines 231-233.
    reference = Reference(to="ExampleSchema")

    with pytest.raises(AssertionError) as exc_info:
        reference.target

    assert "String reference missing 'definitions'." in str(exc_info.value)
    assert not hasattr(reference, "_target")


def test_validate_null_allowed_returns_none():
    # Covers lines 238-239.
    reference = Reference(to=ExampleSchema, allow_null=True)

    assert reference.validate(None) is None


def test_validate_null_not_allowed_raises_validation_error():
    # Covers lines 240-241.
    reference = Reference(to=ExampleSchema)

    with pytest.raises(Exception) as exc_info:
        reference.validate(None)

    messages = exc_info.value.messages()
    assert [message.text for message in messages] == ["May not be null."]


def test_validate_delegates_to_target():
    # Covers line 242.
    reference = Reference(to=ExampleSchema)

    result = reference.validate({"name": "example"})

    assert isinstance(result, ExampleSchema)
    assert result["name"] == "example"


def test_validate_delegates_to_target_with_string_reference():
    # Covers line 242 via the string-reference resolution path.
    reference = Reference(to="ExampleSchema", definitions={"ExampleSchema": ExampleSchema})

    result = reference.validate({"name": "example"})

    assert isinstance(result, ExampleSchema)
    assert result["name"] == "example"


def test_validate_strict_is_forwarded():
    # Covers line 242 with the `strict` keyword forwarded to the target.
    reference = Reference(to=ExampleSchema)

    result = reference.validate({"name": "example"}, strict=True)

    assert isinstance(result, ExampleSchema)
    assert result["name"] == "example"


def test_serialize_none_returns_none():
    # Covers lines 245-246.
    reference = Reference(to=ExampleSchema)

    assert reference.serialize(None) is None


def test_serialize_mapping_returns_dict():
    # Covers line 247.
    reference = Reference(to=ExampleSchema)

    assert reference.serialize({"name": "example"}) == {"name": "example"}
    assert isinstance(reference.serialize({"name": "example"}), dict)
