# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import typesystem.schemas as schemas
from typesystem.fields import Field


def test_schema_metaclass_collects_inherited_and_declared_fields(
    monkeypatch,
):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    calls = []
    original_set_definitions = schemas.set_definitions

    def tracking_set_definitions(field, definitions):
        calls.append((field, definitions))
        original_set_definitions(field, definitions)

    monkeypatch.setattr(schemas, "set_definitions", tracking_set_definitions)

    inherited_field = Field()
    parent_overridden_field = Field()

    class Parent(metaclass=schemas.SchemaMetaclass):
        inherited = inherited_field
        overridden = parent_overridden_field

    own_field = Field()
    child_overridden_field = Field()
    definitions = schemas.SchemaDefinitions()

    class Child(
        Parent,
        metaclass=schemas.SchemaMetaclass,
        definitions=definitions,
    ):
        own = own_field
        overridden = child_overridden_field

    assert list(Child.fields) == ["inherited", "own", "overridden"]
    assert Child.fields == {
        "inherited": inherited_field,
        "own": own_field,
        "overridden": child_overridden_field,
    }
    assert Child.fields["overridden"] is not parent_overridden_field
    assert "own" not in Child.__dict__
    assert "overridden" not in Child.__dict__
    assert calls == [
        (own_field, definitions),
        (child_overridden_field, definitions),
        (inherited_field, definitions),
    ]
    assert definitions["Child"] is Child
