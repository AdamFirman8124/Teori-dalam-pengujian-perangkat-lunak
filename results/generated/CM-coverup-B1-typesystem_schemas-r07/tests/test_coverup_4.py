# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import pytest

from typesystem.fields import Field
from typesystem.schemas import Reference, Schema, SchemaDefinitions


def test_schema_metaclass_collects_direct_fields():
    class DirectSchema(Schema):
        name = Field()
        age = Field()

    assert list(DirectSchema.fields) == ["name", "age"]
    assert isinstance(DirectSchema.fields["name"], Field)
    assert isinstance(DirectSchema.fields["age"], Field)
    assert "name" not in DirectSchema.__dict__
    assert "age" not in DirectSchema.__dict__


def test_schema_metaclass_inherits_base_fields():
    class BaseSchema(Schema):
        name = Field()
        shared = Field()

    class ChildSchema(BaseSchema):
        extra = Field()

    assert list(ChildSchema.fields) == ["name", "shared", "extra"]
    assert ChildSchema.fields["name"] is BaseSchema.fields["name"]
    assert ChildSchema.fields["shared"] is BaseSchema.fields["shared"]
    assert isinstance(ChildSchema.fields["extra"], Field)


def test_schema_metaclass_inherited_field_does_not_override_direct_field():
    class BaseSchema(Schema):
        name = Field()
        shared = Field()

    base_shared = BaseSchema.fields["shared"]

    class OverrideSchema(BaseSchema):
        shared = Field()

    assert list(OverrideSchema.fields) == ["name", "shared"]
    assert OverrideSchema.fields["name"] is BaseSchema.fields["name"]
    assert OverrideSchema.fields["shared"] is not base_shared
    assert isinstance(OverrideSchema.fields["shared"], Field)


def test_schema_metaclass_registers_schema_in_definitions():
    definitions = SchemaDefinitions()

    try:
        class DefinedSchema(Schema, definitions=definitions):
            ref = Reference(to="DefinedSchema")
            name = Field()

        assert definitions["DefinedSchema"] is DefinedSchema
        assert DefinedSchema.fields["ref"].definitions is definitions
        assert isinstance(DefinedSchema.fields["name"], Field)
    finally:
        if "DefinedSchema" in definitions:
            del definitions["DefinedSchema"]

    assert len(definitions) == 0


def test_schema_metaclass_sets_definitions_on_inherited_reference_fields():
    definitions = SchemaDefinitions()

    class BaseSchema(Schema):
        ref = Reference(to="BaseSchema")

    assert BaseSchema.fields["ref"].definitions is None

    try:
        class ChildSchema(BaseSchema, definitions=definitions):
            extra = Field()

        assert definitions["ChildSchema"] is ChildSchema
        assert ChildSchema.fields["ref"] is BaseSchema.fields["ref"]
        assert ChildSchema.fields["ref"].definitions is definitions
        assert isinstance(ChildSchema.fields["extra"], Field)
    finally:
        BaseSchema.fields["ref"].definitions = None
        if "ChildSchema" in definitions:
            del definitions["ChildSchema"]

    assert BaseSchema.fields["ref"].definitions is None
    assert len(definitions) == 0
