# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest
from unittest.mock import MagicMock
from typesystem.base import ValidationError
from typesystem.schemas import Reference, Schema


def test_reference_init_with_schema_class():
    class Widget(Schema):
        pass

    ref = Reference(to=Widget)
    assert ref.to is Widget
    assert ref._target is Widget
    assert ref.target is Widget
    assert not hasattr(ref, "_target_string") or ref._target_string is not None


def test_reference_init_with_invalid_class_raises():
    with pytest.raises(AssertionError):
        Reference(to=int)


def test_reference_target_string_from_class():
    class Gadget(Schema):
        pass

    ref = Reference(to=Gadget)
    # _target_string not set yet for class-based reference
    assert ref._target is Gadget
    assert "_target_string" not in ref.__dict__
    # line 224-226: derive from _target.__name__
    assert ref.target_string == "Gadget"
    assert ref._target_string == "Gadget"
    # cached branch: second access returns same without recomputing
    assert ref.target_string == "Gadget"


def test_reference_target_string_from_str():
    class Widget(Schema):
        pass

    ref = Reference(to="Widget", definitions={"Widget": Widget})
    assert ref._target_string == "Widget"
    assert ref.target_string == "Widget"
    # cached access still works
    assert ref.target_string == "Widget"


def test_reference_target_lazy_resolution_and_cache():
    class Item(Schema):
        pass

    definitions = {"Item": Item}
    ref = Reference(to="Item", definitions=definitions)
    assert "_target" not in ref.__dict__
    # lines 230-235: lazy lookup via definitions
    first = ref.target
    assert first is Item
    assert ref._target is Item
    # cached branch: hasattr is True
    second = ref.target
    assert second is Item
    assert second is first


def test_reference_target_missing_definitions_asserts():
    ref = Reference(to="Missing")
    assert ref.definitions is None
    with pytest.raises(AssertionError, match="String reference missing 'definitions'"):
        _ = ref.target


def test_reference_validate_allow_null_returns_none():
    class Widget(Schema):
        pass

    ref = Reference(to=Widget, allow_null=True)
    assert ref.allow_null is True
    assert ref.validate(None) is None
    assert ref.validate(None, strict=True) is None
    assert ref.validate(None, strict=False) is None


def test_reference_validate_null_without_allow_null_raises():
    class Widget(Schema):
        pass

    ref = Reference(to=Widget)
    assert ref.allow_null is False
    with pytest.raises(ValidationError):
        ref.validate(None)
    with pytest.raises(ValidationError):
        ref.validate(None, strict=True)


def test_reference_validate_delegates_to_target():
    class Empty(Schema):
        pass

    ref = Reference(to=Empty)
    result = ref.validate({})
    assert isinstance(result, Empty)
    assert dict(result) == {}

    # strict passthrough verified with a mock target
    mock_target = MagicMock()
    mock_target.validate.return_value = "validated-value"
    mock_ref = Reference(to="Mocked", definitions={"Mocked": mock_target})
    assert mock_ref.validate("input-value", strict=True) == "validated-value"
    mock_target.validate.assert_called_once_with("input-value", strict=True)

    mock_target2 = MagicMock()
    mock_target2.validate.return_value = "other"
    mock_ref2 = Reference(to="Mocked2", definitions={"Mocked2": mock_target2})
    assert mock_ref2.validate("x", strict=False) == "other"
    mock_target2.validate.assert_called_once_with("x", strict=False)


def test_reference_serialize_none_and_dict():
    class Widget(Schema):
        pass

    ref = Reference(to=Widget)
    assert ref.serialize(None) is None

    assert ref.serialize({"a": 1}) == {"a": 1}
    assert ref.serialize({}) == {}

    instance = Widget()
    assert ref.serialize(instance) == dict(instance) == {}

    # string-based reference serializes the same way
    ref2 = Reference(to="Widget", definitions={"Widget": Widget})
    assert ref2.serialize(None) is None
    assert ref2.serialize({"x": 2}) == {"x": 2}
