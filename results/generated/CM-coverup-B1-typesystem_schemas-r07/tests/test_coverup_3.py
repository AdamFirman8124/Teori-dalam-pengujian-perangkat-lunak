# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Field, Object
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_set_definitions_updates_reference_without_definitions():
    definitions = SchemaDefinitions()
    reference = Reference(to="Target")

    result = set_definitions(reference, definitions)

    assert result is None
    assert reference.definitions is definitions


def test_set_definitions_preserves_reference_existing_definitions():
    existing_definitions = SchemaDefinitions()
    replacement_definitions = SchemaDefinitions()
    reference = Reference(to="Target", definitions=existing_definitions)

    result = set_definitions(reference, replacement_definitions)

    assert result is None
    assert reference.definitions is existing_definitions


def test_set_definitions_handles_array_without_items():
    definitions = SchemaDefinitions()
    field = Array()

    result = set_definitions(field, definitions)

    assert result is None
    assert field.items is None


def test_set_definitions_recurses_into_single_array_item():
    definitions = SchemaDefinitions()
    reference = Reference(to="Target")
    field = Array(items=reference)

    result = set_definitions(field, definitions)

    assert result is None
    assert field.items is reference
    assert reference.definitions is definitions


def test_set_definitions_recurses_into_array_item_list():
    definitions = SchemaDefinitions()
    first_reference = Reference(to="FirstTarget")
    second_reference = Reference(to="SecondTarget")
    field = Array(items=[first_reference, second_reference])

    result = set_definitions(field, definitions)

    assert result is None
    assert first_reference.definitions is definitions
    assert second_reference.definitions is definitions


def test_set_definitions_recurses_into_object_properties():
    definitions = SchemaDefinitions()
    first_reference = Reference(to="FirstTarget")
    second_reference = Reference(to="SecondTarget")
    field = Object(
        properties={
            "first": first_reference,
            "second": second_reference,
        }
    )

    result = set_definitions(field, definitions)

    assert result is None
    assert first_reference.definitions is definitions
    assert second_reference.definitions is definitions


def test_set_definitions_ignores_unrelated_field():
    definitions = SchemaDefinitions()
    field = Field()

    result = set_definitions(field, definitions)

    assert result is None
