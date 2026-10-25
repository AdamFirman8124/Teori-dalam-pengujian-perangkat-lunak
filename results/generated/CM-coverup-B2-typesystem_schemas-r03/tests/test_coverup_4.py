# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import pytest
from typesystem.fields import Field
from typesystem.schemas import Schema, SchemaDefinitions, SchemaMetaclass


def test_collects_declared_fields():
    class ExampleCollect(Schema):
        name = Field()
        count = Field()
        plain = 123

    assert list(ExampleCollect.fields.keys()) == ["name", "count"]
    assert "name" not in ExampleCollect.__dict__
    assert "count" not in ExampleCollect.__dict__
    assert ExampleCollect.plain == 123
    assert all(isinstance(v, Field) for v in ExampleCollect.fields.values())


def test_inherits_parent_fields():
    class ParentInherit(Schema):
        a = Field()

    class ChildInherit(ParentInherit):
        b = Field()

    assert "a" in ChildInherit.fields
    assert "b" in ChildInherit.fields
    assert set(ChildInherit.fields.keys()) == {"a", "b"}
    assert ChildInherit.fields["a"] is ParentInherit.fields["a"]


def test_child_field_not_overwritten_by_parent():
    class ParentOverride(Schema):
        a = Field()

    parent_field = ParentOverride.fields["a"]

    class ChildOverride(ParentOverride):
        a = Field()

    assert "a" in ChildOverride.fields
    assert isinstance(ChildOverride.fields["a"], Field)
    assert ChildOverride.fields["a"] is not parent_field


def test_ignores_non_field_in_base_fields():
    real_field = Field()

    class FakeBase:
        fields = {"not_a_field": 123, "real": real_field}

    NewType = SchemaMetaclass.__new__(
        SchemaMetaclass, "FakeChildXyz123", (FakeBase,), {}, definitions=None
    )
    assert "real" in NewType.fields
    assert NewType.fields["real"] is real_field
    assert "not_a_field" not in NewType.fields


def test_definitions_sets_and_registers():
    defs = SchemaDefinitions()
    NewType = SchemaMetaclass.__new__(
        SchemaMetaclass,
        "DefRegTestAbc123",
        (object,),
        {"x": Field(), "y": Field()},
        definitions=defs,
    )
    try:
        assert "x" in NewType.fields
        assert "y" in NewType.fields
        assert defs["DefRegTestAbc123"] is NewType
    finally:
        if "DefRegTestAbc123" in defs:
            del defs["DefRegTestAbc123"]


def test_definitions_with_inherited_fields():
    defs = SchemaDefinitions()
    Base = SchemaMetaclass.__new__(
        SchemaMetaclass,
        "DefBaseAbc456",
        (object,),
        {"a": Field()},
        definitions=defs,
    )
    Child = SchemaMetaclass.__new__(
        SchemaMetaclass,
        "DefChildAbc456",
        (Base,),
        {"b": Field()},
        definitions=defs,
    )
    try:
        assert set(Child.fields.keys()) == {"a", "b"}
        assert Child.fields["a"] is Base.fields["a"]
        assert defs["DefBaseAbc456"] is Base
        assert defs["DefChildAbc456"] is Child
    finally:
        for k in ("DefBaseAbc456", "DefChildAbc456"):
            if k in defs:
                del defs[k]
