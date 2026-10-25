# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

from typesystem.fields import Field, String
from typesystem.schemas import Reference, SchemaDefinitions, SchemaMetaclass


def test_metaclass_collects_declared_and_inherited_fields(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    inherited_field = String()

    class Base(metaclass=SchemaMetaclass):
        base_field = inherited_field

    declared_field = String()

    class Child(Base, metaclass=SchemaMetaclass):
        child_field = declared_field

    assert "base_field" not in Base.__dict__
    assert Base.fields == {"base_field": inherited_field}
    assert "child_field" not in Child.__dict__
    assert list(Child.fields) == ["base_field", "child_field"]
    assert Child.fields["base_field"] is inherited_field
    assert Child.fields["child_field"] is declared_field

    replacement_field = String()

    class Override(Base, metaclass=SchemaMetaclass):
        base_field = replacement_field

    assert Override.fields == {"base_field": replacement_field}
    assert Override.fields["base_field"] is not inherited_field


def test_metaclass_sets_definitions_and_registers_new_schema(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    definitions = SchemaDefinitions()
    reference = Reference("Target")

    class ReferencingSchema(
        metaclass=SchemaMetaclass,
        definitions=definitions,
    ):
        target = reference

    assert "target" not in ReferencingSchema.__dict__
    assert ReferencingSchema.fields == {"target": reference}
    assert reference.definitions is definitions
    assert definitions["ReferencingSchema"] is ReferencingSchema
