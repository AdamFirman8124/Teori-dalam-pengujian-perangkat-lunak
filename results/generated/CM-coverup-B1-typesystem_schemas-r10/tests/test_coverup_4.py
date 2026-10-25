# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

from typesystem.fields import Field
from typesystem.schemas import Reference, Schema, SchemaDefinitions


def test_schema_metaclass_collects_declared_and_inherited_fields(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    inherited = Field()
    parent_shared = Field()

    class ParentSchema(Schema):
        inherited_field = inherited
        shared_field = parent_shared

    child_shared = Field()
    declared = Field()

    class ChildSchema(ParentSchema):
        shared_field = child_shared
        declared_field = declared

    assert "inherited_field" not in ParentSchema.__dict__
    assert "shared_field" not in ParentSchema.__dict__
    assert "declared_field" not in ChildSchema.__dict__
    assert "shared_field" not in ChildSchema.__dict__

    assert ChildSchema.fields == {
        "inherited_field": inherited,
        "shared_field": child_shared,
        "declared_field": declared,
    }
    assert ChildSchema.fields["shared_field"] is child_shared
    assert ChildSchema.fields["shared_field"] is not parent_shared


def test_schema_metaclass_sets_definitions_and_registers_schema(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)
    definitions = SchemaDefinitions()
    reference = Reference("DefinedSchema")

    try:
        class DefinedSchema(Schema, definitions=definitions):
            self_reference = reference

        assert DefinedSchema.fields == {"self_reference": reference}
        assert reference.definitions is definitions
        assert definitions["DefinedSchema"] is DefinedSchema
        assert reference.target is DefinedSchema
    finally:
        definitions.clear()
