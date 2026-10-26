# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem import Schema, fields
from typesystem.base import ValidationError
from typesystem.schemas import Reference


def test_reference_with_schema_class_sets_target_and_target_string():
    class Example(Schema):
        name = fields.String()

    ref = Reference(to=Example)

    assert ref.to is Example
    assert ref.definitions is None
    # __init__ took the non-string branch: _target set eagerly.
    assert ref.target is Example
    # target_string is derived lazily from the class name.
    assert ref.target_string == "Example"


def test_reference_with_string_and_definitions_resolves_lazily():
    class Example(Schema):
        name = fields.String()

    definitions = {"Example": Example}
    ref = Reference(to="Example", definitions=definitions)

    assert ref.to == "Example"
    assert ref.definitions is definitions
    # String branch: _target_string set in __init__, _target resolved on demand.
    assert ref.target_string == "Example"
    assert ref.target is Example
    # Second access hits the cached branch.
    assert ref.target is Example


def test_reference_string_without_definitions_raises_assertion_error():
    ref = Reference(to="Example")

    with pytest.raises(AssertionError) as exc_info:
        ref.target

    assert "String reference missing 'definitions'." in str(exc_info.value)


def test_reference_rejects_non_schema_class():
    with pytest.raises(AssertionError):
        Reference(to=int)


def test_reference_validate_null_allowed():
    class Example(Schema):
        name = fields.String()

    ref = Reference(to=Example, allow_null=True)

    assert ref.validate(None) is None


def test_reference_validate_null_not_allowed():
    class Example(Schema):
        name = fields.String()

    ref = Reference(to=Example)

    with pytest.raises(ValidationError) as exc_info:
        ref.validate(None)

    assert exc_info.value.messages()[0].text == "May not be null."


def test_reference_validate_delegates_to_target():
    class Example(Schema):
        age = fields.Integer()

    ref = Reference(to=Example)

    validated = ref.validate({"age": 3})
    assert isinstance(validated, Example)
    assert validated.age == 3

    with pytest.raises(ValidationError):
        ref.validate({"age": "not-a-number"})


def test_reference_validate_delegates_through_string_reference():
    class Example(Schema):
        age = fields.Integer()

    ref = Reference(to="Example", definitions={"Example": Example})

    validated = ref.validate({"age": 3})
    assert isinstance(validated, Example)
    assert validated.age == 3


def test_reference_serialize():
    class Example(Schema):
        name = fields.String()

    ref = Reference(to=Example)

    assert ref.serialize(None) is None
    assert ref.serialize(Example(name="abc")) == {"name": "abc"}
