# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

from typesystem.fields import Field, String
from typesystem.schemas import Reference, Schema, SchemaDefinitions


def test_metaclass_collects_declared_and_inherited_fields(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    inherited_field = String()
    base_override_field = String()

    class BaseSchema(Schema):
        inherited = inherited_field
        overridden = base_override_field

    BaseSchema.fields["ignored_non_field"] = object()

    child_override_field = String()
    declared_field = String()

    class ChildSchema(BaseSchema):
        overridden = child_override_field
        declared = declared_field

    assert "overridden" not in ChildSchema.__dict__
    assert "declared" not in ChildSchema.__dict__
    assert list(ChildSchema.fields) == ["inherited", "overridden", "declared"]
    assert ChildSchema.fields["inherited"] is inherited_field
    assert ChildSchema.fields["overridden"] is child_override_field
    assert ChildSchema.fields["overridden"] is not base_override_field
    assert ChildSchema.fields["declared"] is declared_field
    assert "ignored_non_field" not in ChildSchema.fields


def test_metaclass_sets_definitions_and_registers_schema(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    definitions = SchemaDefinitions()
    parent_field = Reference("RegisteredSchema")

    class RegisteredSchema(Schema, definitions=definitions):
        parent = parent_field

    assert "parent" not in RegisteredSchema.__dict__
    assert RegisteredSchema.fields == {"parent": parent_field}
    assert parent_field.definitions is definitions
    assert definitions["RegisteredSchema"] is RegisteredSchema
    assert parent_field.target is RegisteredSchema
