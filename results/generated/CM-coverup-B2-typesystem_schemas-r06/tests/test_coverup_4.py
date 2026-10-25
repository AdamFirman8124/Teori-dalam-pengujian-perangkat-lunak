# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

from typesystem.fields import Field
from typesystem.schemas import SchemaMetaclass


def test_declared_fields_are_collected(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)
    f1 = Field()
    f2 = Field()
    attrs = {"__module__": __name__, "a": f1, "b": f2, "plain": 123}
    New = SchemaMetaclass.__new__(SchemaMetaclass, "TCollected", (object,), dict(attrs))
    assert New.fields["a"] is f1
    assert New.fields["b"] is f2
    assert list(New.fields.keys()) == ["a", "b"]
    assert "a" not in New.__dict__
    assert "b" not in New.__dict__
    assert New.plain == 123


def test_inherits_base_fields_override_and_non_field(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)
    base_field = Field()
    Base = SchemaMetaclass.__new__(
        SchemaMetaclass, "TBaseInh", (object,), {"__module__": __name__, "base_attr": base_field}
    )
    assert Base.fields["base_attr"] is base_field

    real_field = Field()
    class FakeBase:
        fields = {"junk": 123, "real": real_field}

    override_field = Field()
    own_field = Field()
    Child = SchemaMetaclass.__new__(
        SchemaMetaclass,
        "TChildInh",
        (Base, FakeBase),
        {"__module__": __name__, "base_attr": override_field, "own": own_field},
    )
    # overriding field in subclass wins: covers `key not in fields` False branch
    assert Child.fields["base_attr"] is override_field
    assert Child.fields["base_attr"] is not base_field
    # inherited Field from plain base: covers `isinstance and not in` True branch
    assert Child.fields["real"] is real_field
    # non-Field entry in base fields is ignored: covers `isinstance` False branch
    assert "junk" not in Child.fields
    assert Child.fields["own"] is own_field
    assert "base_attr" not in Child.__dict__
    assert "own" not in Child.__dict__


def test_definitions_registers_type_and_sets_definitions(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)
    definitions = {}
    f = Field()
    New = SchemaMetaclass.__new__(
        SchemaMetaclass,
        "TWithDefs",
        (object,),
        {"__module__": __name__, "f": f},
        definitions=definitions,
    )
    assert definitions["TWithDefs"] is New
    assert New.fields["f"] is f
    assert "f" not in New.__dict__
