# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest
from typesystem.schemas import Reference, Schema


def test_reference_init_with_class_target():
    class Target(Schema):
        pass

    ref = Reference(to=Target)
    assert ref.to is Target
    assert ref._target is Target
    # `target` property when `_target` already exists (hasattr True branch)
    assert ref.target is Target


def test_reference_target_string_derived_from_class():
    class MyModel(Schema):
        pass

    ref = Reference(to=MyModel)
    assert not hasattr(ref, "_target_string")
    # covers missing lines 224-226
    assert ref.target_string == "MyModel"
    assert ref._target_string == "MyModel"
    # cached path (hasattr True branch)
    assert ref.target_string == "MyModel"


def test_reference_target_string_direct_for_str():
    class Other(Schema):
        pass

    ref = Reference(to="Other", definitions={"Other": Other})
    # _target_string already set, direct return branch
    assert ref.target_string == "Other"
    assert ref.target_string == "Other"


def test_reference_target_resolves_via_definitions():
    class Item(Schema):
        pass

    defs = {"Item": Item}
    ref = Reference(to="Item", definitions=defs)
    assert not hasattr(ref, "_target")
    # covers missing lines 230-235
    assert ref.target is Item
    # second access uses cached _target
    assert ref.target is Item
    assert ref.definitions is defs
    assert ref.to == "Item"


def test_reference_target_missing_definitions_asserts():
    ref = Reference(to="Missing")
    assert ref.definitions is None
    with pytest.raises(AssertionError, match="String reference missing"):
        _ = ref.target


def test_reference_init_invalid_target_asserts():
    with pytest.raises(AssertionError):
        Reference(to=int)


def test_reference_validate_allow_null_returns_none():
    class T1(Schema):
        pass

    ref = Reference(to=T1, allow_null=True)
    assert ref.allow_null is True
    assert ref.validate(None) is None
    assert ref.validate(None, strict=True) is None


def test_reference_validate_null_raises():
    class T2(Schema):
        pass

    ref = Reference(to=T2)
    assert ref.allow_null is False
    with pytest.raises(Exception) as exc_info:
        ref.validate(None)
    assert "May not be null" in str(exc_info.value)
    with pytest.raises(Exception):
        ref.validate(None, strict=True)


def test_reference_validate_delegates_to_target():
    class T3(Schema):
        pass

    ref = Reference(to=T3)
    result = ref.validate({})
    assert isinstance(result, T3)
    result_strict = ref.validate({}, strict=True)
    assert isinstance(result_strict, T3)

    # string reference delegation
    ref2 = Reference(to="T3", definitions={"T3": T3})
    result2 = ref2.validate({})
    assert isinstance(result2, T3)


def test_reference_validate_forwards_strict(monkeypatch):
    class Target(Schema):
        pass

    ref = Reference(to=Target)
    seen = {}
    original = Target.validate

    def spy(value, strict=False):
        seen["value"] = value
        seen["strict"] = strict
        return original(value, strict=strict)

    monkeypatch.setattr(Target, "validate", spy)
    try:
        out = ref.validate({}, strict=True)
        assert seen["value"] == {}
        assert seen["strict"] is True
        assert isinstance(out, Target)
        out2 = ref.validate({}, strict=False)
        assert seen["strict"] is False
        assert isinstance(out2, Target)
    finally:
        # monkeypatch auto-undoes, explicit check that attribute exists
        assert hasattr(Target, "validate")


def test_reference_serialize_none_and_value():
    class T4(Schema):
        pass

    ref = Reference(to=T4)
    # covers lines 245-246
    assert ref.serialize(None) is None

    # covers line 247 with Schema instance
    obj = T4()
    assert ref.serialize(obj) == {}
    assert ref.serialize(obj) == dict(obj)

    # covers line 247 with content to verify dict conversion
    assert ref.serialize({"a": 1}) == {"a": 1}
