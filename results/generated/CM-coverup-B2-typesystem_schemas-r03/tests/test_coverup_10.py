# file: project/typesystem/schemas.py:133-140
# asked: {"lines": [135, 136, 137, 138, 139], "branches": []}
# gained: {"lines": [135, 136, 137, 138, 139], "branches": []}

import typesystem.fields as fields
from typesystem.fields import Object
from typesystem.schemas import Schema


def test_make_validator_non_strict_with_mixed_fields():
    class Person(Schema):
        name = fields.String()
        nickname = fields.String(default="")

    validator = Person.make_validator()

    assert isinstance(validator, Object)
    assert validator.properties == Person.fields
    assert validator.required == ["name"]
    assert validator.additional_properties is None

    # Postconditions: required field enforced, optional field not required.
    value, error = validator.validate_or_error({"name": "Alice"})
    assert error is None
    assert value["name"] == "Alice"

    _, missing_error = validator.validate_or_error({})
    assert missing_error is not None


def test_make_validator_strict_forbids_additional_properties():
    class Item(Schema):
        title = fields.String()
        description = fields.String(default="n/a")

    validator = Item.make_validator(strict=True)

    assert isinstance(validator, Object)
    assert validator.properties == Item.fields
    assert validator.required == ["title"]
    assert validator.additional_properties is False

    # Postconditions: valid input passes, missing required fails.
    value, error = validator.validate_or_error({"title": "hello"})
    assert error is None
    assert value["title"] == "hello"

    _, missing_error = validator.validate_or_error({})
    assert missing_error is not None

    # Postcondition: strict validator rejects additional properties.
    _, extra_error = validator.validate_or_error({"title": "hello", "extra": "nope"})
    assert extra_error is not None
