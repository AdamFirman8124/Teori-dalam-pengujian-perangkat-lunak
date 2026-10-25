# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 232, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest
from typesystem.schemas import Reference, Schema
from typesystem.fields import String
from typesystem.base import ValidationError


def test_reference_init_with_schema_class_sets_target_directly():
    class Person(Schema):
        name = String()

    ref = Reference(to=Person)
    # lines 219-220
    assert ref._target is Person
    assert ref.to is Person
    # line 230 false-branch (already has _target)
    assert ref.target is Person
    # lines 224-226 (lazy _target_string from _target)
    assert ref.target_string == "Person"
    assert ref._target_string == "Person"
    # cached second access still works
    assert ref.target_string == "Person"


def test_reference_string_target_resolves_via_definitions():
    definitions = {"Greeting": String()}
    ref = Reference(to="Greeting", definitions=definitions)
    # _target_string set at init, target_string returns directly
    assert ref._target_string == "Greeting"
    assert ref.target_string == "Greeting"
    # lines 230-235 (lazy _target from definitions)
    assert not hasattr(ref, "_target")
    assert ref.target is definitions["Greeting"]
    assert ref._target is definitions["Greeting"]
    # second access uses cached _target (line 230 false-branch)
    assert ref.target is definitions["Greeting"]


def test_reference_validate_none_allowed_returns_none():
    class Person(Schema):
        name = String()

    ref = Reference(to=Person, allow_null=True)
    # lines 238-239
    assert ref.validate(None) is None
    assert ref.validate(None, strict=True) is None


def test_reference_validate_none_disallowed_raises():
    class Person(Schema):
        name = String()

    ref = Reference(to=Person)
    assert ref.allow_null is False
    # lines 240-241
    with pytest.raises(ValidationError):
        ref.validate(None)
    with pytest.raises(ValidationError):
        ref.validate(None, strict=True)


def test_reference_validate_delegates_to_target():
    # delegation via string reference -> field target (line 242 + lines 230-235)
    definitions = {"Name": String()}
    ref = Reference(to="Name", definitions=definitions)
    assert ref.validate("hello") == "hello"
    assert ref.validate("hello", strict=True) == "hello"

    # delegation via class reference -> Schema target (line 242 + line 230 cached)
    class Person(Schema):
        name = String()

    ref2 = Reference(to=Person)
    result = ref2.validate({"name": "Alice"})
    assert isinstance(result, Person)
    assert result["name"] == "Alice"
    assert dict(result) == {"name": "Alice"}


def test_reference_serialize_none_and_value():
    class Person(Schema):
        name = String()

    ref = Reference(to=Person)
    # lines 245-246
    assert ref.serialize(None) is None
    # lines 245 + 247 with Schema instance
    person = Person(name="Bob")
    assert ref.serialize(person) == {"name": "Bob"}
    assert ref.serialize(person) == dict(person)
    # lines 245 + 247 with plain dict
    assert ref.serialize({"x": 1}) == {"x": 1}
