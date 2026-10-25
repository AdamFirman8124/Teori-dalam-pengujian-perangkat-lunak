# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem import Schema, fields
from typesystem.base import ValidationError
from typesystem.schemas import Reference


def test_reference_to_schema_class_sets_target_and_target_string():
    class Example(Schema):
        name = fields.String()

    reference = Reference(to=Example)

    assert reference.target is Example
    assert reference.target_string == "Example"
    assert reference.target_string == "Example"


def test_reference_to_string_resolves_target_from_definitions():
    class Example(Schema):
        name = fields.String()

    reference = Reference(to="Example", definitions={"Example": Example})

    assert reference.target_string == "Example"
    assert reference.target is Example
    assert reference.target is Example


def test_reference_to_string_without_definitions_raises_assertion_error():
    reference = Reference(to="Example")

    with pytest.raises(
        AssertionError, match="String reference missing 'definitions'."
    ):
        reference.target


def test_reference_validate_allow_null_returns_none():
    class Example(Schema):
        name = fields.String()

    reference = Reference(to=Example, allow_null=True)

    assert reference.validate(None) is None


def test_reference_validate_null_raises_validation_error():
    class Example(Schema):
        name = fields.String()

    reference = Reference(to=Example)

    with pytest.raises(ValidationError) as exc_info:
        reference.validate(None)

    messages = exc_info.value.messages()
    assert len(messages) == 1
    assert messages[0].code == "null"
    assert messages[0].text == "May not be null."


def test_reference_validate_delegates_to_target():
    class Example(Schema):
        name = fields.String()

    reference = Reference(to=Example)

    result = reference.validate({"name": "Ada"})

    assert isinstance(result, Example)
    assert result["name"] == "Ada"


def test_reference_serialize_none_and_schema_instance():
    class Example(Schema):
        name = fields.String()

    reference = Reference(to=Example)
    instance = Example({"name": "Ada"})

    assert reference.serialize(None) is None
    assert reference.serialize(instance) == {"name": "Ada"}
