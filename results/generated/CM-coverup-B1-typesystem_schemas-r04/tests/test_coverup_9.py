# file: project/typesystem/schemas.py:175-182
# asked: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}
# gained: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}

import pytest

from typesystem import String
from typesystem.schemas import Schema


class ExampleSchema(Schema):
    name = String()
    age = String()


def test_getitem_returns_serialized_value():
    """
    Covers lines 176-178 and 182: key present in self.fields and the
    attribute exists on the instance, so field.serialize(value) is returned.
    """
    instance = ExampleSchema(name="alice", age="30")

    result = instance["name"]

    assert result == "alice"
    assert instance["age"] == "30"


def test_getitem_unknown_key_raises_keyerror():
    """
    Covers lines 179-180: key is not in self.fields, so a KeyError is
    raised (with the original context suppressed via 'from None').
    """
    instance = ExampleSchema(name="alice", age="30")

    with pytest.raises(KeyError) as exc_info:
        instance["missing"]

    assert exc_info.value.args == ("missing",)
    # 'raise ... from None' suppresses the exception context.
    assert exc_info.value.__suppress_context__ is True


def test_getitem_field_without_attribute_raises_keyerror():
    """
    Covers the AttributeError branch of line 179: the key exists in
    self.fields but getattr(self, key) fails, so a KeyError is raised.
    """
    class PartialSchema(Schema):
        name = String()

    # Bypass Schema.__init__ so the 'name' attribute is never set.
    instance = object.__new__(PartialSchema)

    with pytest.raises(KeyError) as exc_info:
        instance["name"]

    assert exc_info.value.args == ("name",)
    assert exc_info.value.__suppress_context__ is True
