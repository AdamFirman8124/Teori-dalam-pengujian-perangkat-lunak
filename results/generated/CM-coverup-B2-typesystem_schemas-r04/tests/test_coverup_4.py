# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import typesystem.schemas as schemas
from typesystem.fields import Field


def test_schema_metaclass_collects_declared_and_inherited_fields(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    inherited = Field()
    overridden_on_base = Field()

    class BaseSchema(schemas.Schema):
        inherited_field = inherited
        overridden_field = overridden_on_base

    override = Field()
    declared = Field()

    class ChildSchema(BaseSchema):
        overridden_field = override
        declared_field = declared

    assert ChildSchema.fields == {
        "inherited_field": inherited,
        "overridden_field": override,
        "declared_field": declared,
    }
    assert "declared_field" not in ChildSchema.__dict__
    assert "overridden_field" not in ChildSchema.__dict__
    assert ChildSchema.fields["overridden_field"] is not overridden_on_base


def test_schema_metaclass_sets_definitions_and_registers_new_schema(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    definitions = schemas.SchemaDefinitions()
    reference = schemas.Reference("DefinedSchema")

    class DefinedSchema(schemas.Schema, definitions=definitions):
        related = reference

    assert DefinedSchema.fields == {"related": reference}
    assert "related" not in DefinedSchema.__dict__
    assert reference.definitions is definitions
    assert definitions["DefinedSchema"] is DefinedSchema
