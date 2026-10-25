# file: project/typesystem/schemas.py:189-190
# asked: {"lines": [190], "branches": []}
# gained: {"lines": [190], "branches": []}

import pytest

from typesystem import Schema, fields


def test_len_counts_fields_present_as_attributes():
    class Example(Schema):
        a = fields.Integer()
        b = fields.String()

    instance = Example(a=1, b="hello")

    assert hasattr(instance, "a")
    assert hasattr(instance, "b")
    assert len(instance) == 2


def test_len_skips_fields_missing_as_attributes():
    class Example(Schema):
        a = fields.Integer()
        b = fields.String()

    instance = Example(a=1, b="hello")
    assert len(instance) == 2

    del instance.b

    assert not hasattr(instance, "b")
    assert hasattr(instance, "a")
    assert len(instance) == 1


def test_len_of_schema_with_no_fields():
    class Empty(Schema):
        pass

    instance = Empty()

    assert len(instance) == 0
