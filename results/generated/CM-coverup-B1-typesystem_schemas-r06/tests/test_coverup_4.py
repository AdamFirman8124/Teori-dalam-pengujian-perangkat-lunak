# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

from typesystem.fields import Field
from typesystem.schemas import Reference, Schema


def test_schema_metaclass_collects_declared_and_inherited_fields(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    inherited_field = Field()
    base_only_field = Field()

    class BaseSchema(Schema):
        inherited = inherited_field
        base_only = base_only_field

    replacement_field = Field()
    child_only_field = Field()

    class ChildSchema(BaseSchema):
        inherited = replacement_field
        child_only = child_only_field

    assert BaseSchema.fields == {
        "inherited": inherited_field,
        "base_only": base_only_field,
    }
    assert ChildSchema.fields == {
        "base_only": base_only_field,
        "inherited": replacement_field,
        "child_only": child_only_field,
    }
    assert "inherited" not in BaseSchema.__dict__
    assert "base_only" not in BaseSchema.__dict__
    assert "inherited" not in ChildSchema.__dict__
    assert "child_only" not in ChildSchema.__dict__


def test_schema_metaclass_sets_definitions_and_registers_schema(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    definitions = {}
    parent_reference = Reference("DefinedSchema")

    class DefinedSchema(Schema, definitions=definitions):
        parent = parent_reference

    assert DefinedSchema.fields == {"parent": parent_reference}
    assert parent_reference.definitions is definitions
    assert definitions == {"DefinedSchema": DefinedSchema}
