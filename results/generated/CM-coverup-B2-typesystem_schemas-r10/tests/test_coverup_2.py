# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem.base import ValidationError
from typesystem.fields import String
from typesystem.schemas import Reference, Schema


class Example(Schema):
    name = String()


class NotASchema:
    pass


def test_reference_to_schema_class_sets_target():
    """Lines 219-220: 'to' is a Schema subclass, so _target is set directly."""
    ref = Reference(to=Example)
    assert ref.to is Example
    assert ref.definitions is None
    assert ref.target is Example


def test_reference_to_non_schema_class_raises():
    """Line 219 failing branch: 'to' is a class but not a Schema subclass."""
    with pytest.raises(AssertionError):
        Reference(to=NotASchema)


def test_target_string_from_schema_class():
    """Lines 224-226: target_string computed lazily from the Schema class name."""
    ref = Reference(to=Example)
    assert not hasattr(ref, "_target_string")
    assert ref.target_string == "Example"
    # The computed value is cached on the instance.
    assert ref._target_string == "Example"
    assert ref.target_string == "Example"


def test_target_string_from_string_reference():
    """Lines 224, 226: target_string already set for string references."""
    ref = Reference(to="Example", definitions={"Example": Example})
    assert ref.target_string == "Example"


def test_target_from_definitions():
    """Lines 230-235: target resolved lazily from definitions mapping."""
    ref = Reference(to="Example", definitions={"Example": Example})
    assert not hasattr(ref, "_target")
    assert ref.target is Example
    # The resolved target is cached on the instance.
    assert ref.target is Example


def test_target_without_definitions_raises():
    """Lines 231-233 failing branch: string reference without definitions."""
    ref = Reference(to="Example")
    with pytest.raises(AssertionError, match="String reference missing 'definitions'"):
        ref.target


def test_validate_none_with_allow_null():
    """Lines 238-239: None passes through when allow_null is set."""
    ref = Reference(to=Example, allow_null=True)
    assert ref.validate(None) is None


def test_validate_none_without_allow_null_raises():
    """Lines 240-241: None raises the 'null' validation error otherwise."""
    ref = Reference(to=Example)
    with pytest.raises(ValidationError) as exc_info:
        ref.validate(None)
    assert "May not be null." in str(exc_info.value)


def test_validate_delegates_to_target():
    """Line 242: non-None values are delegated to the target schema."""
    ref = Reference(to=Example)
    result = ref.validate({"name": "test"})
    assert isinstance(result, Example)
    assert result.name == "test"


def test_validate_with_string_reference_resolves_target():
    """Lines 230-235 and 242 together: lazy resolution during validation."""
    ref = Reference(to="Example", definitions={"Example": Example})
    result = ref.validate({"name": "test"})
    assert isinstance(result, Example)
    assert result.name == "test"


def test_validate_passes_strict_to_target(monkeypatch):
    """Line 242: both value and strict flag are forwarded to the target."""
    ref = Reference(to=Example)
    calls = {}

    def fake_validate(cls, value, *, strict=False):
        calls["value"] = value
        calls["strict"] = strict
        return "sentinel"

    monkeypatch.setattr(Example, "validate", classmethod(fake_validate))
    result = ref.validate({"name": "test"}, strict=True)
    assert result == "sentinel"
    assert calls == {"value": {"name": "test"}, "strict": True}


def test_serialize_none():
    """Lines 245-246: None serializes to None."""
    ref = Reference(to=Example)
    assert ref.serialize(None) is None


def test_serialize_instance():
    """Line 247: schema instances serialize to a plain dict."""
    ref = Reference(to=Example)
    instance = Example({"name": "test"})
    assert ref.serialize(instance) == {"name": "test"}
