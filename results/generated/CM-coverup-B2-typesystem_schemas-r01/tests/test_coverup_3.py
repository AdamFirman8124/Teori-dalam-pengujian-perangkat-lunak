# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Object, String
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_set_definitions_assigns_definitions_to_reference():
    definitions = SchemaDefinitions()
    reference = Reference(to="MySchema")

    assert reference.definitions is None

    set_definitions(reference, definitions)

    assert reference.definitions is definitions


def test_set_definitions_preserves_existing_reference_definitions():
    existing_definitions = SchemaDefinitions()
    new_definitions = SchemaDefinitions()
    reference = Reference(to="MySchema", definitions=existing_definitions)

    set_definitions(reference, new_definitions)

    assert reference.definitions is existing_definitions


def test_set_definitions_recurses_into_array_list_items():
    definitions = SchemaDefinitions()
    first_reference = Reference(to="First")
    second_reference = Reference(to="Second")
    field = Array(items=[first_reference, second_reference])

    set_definitions(field, definitions)

    assert first_reference.definitions is definitions
    assert second_reference.definitions is definitions


def test_set_definitions_recurses_into_single_array_item():
    definitions = SchemaDefinitions()
    reference = Reference(to="Item")
    field = Array(items=reference)

    set_definitions(field, definitions)

    assert reference.definitions is definitions


def test_set_definitions_handles_array_without_items():
    definitions = SchemaDefinitions()
    field = Array(items=None)

    set_definitions(field, definitions)

    assert field.items is None


def test_set_definitions_recurses_into_object_properties():
    definitions = SchemaDefinitions()
    first_reference = Reference(to="First")
    second_reference = Reference(to="Second")
    field = Object(
        properties={
            "first": first_reference,
            "second": second_reference,
        }
    )

    set_definitions(field, definitions)

    assert first_reference.definitions is definitions
    assert second_reference.definitions is definitions


def test_set_definitions_recurses_through_nested_fields():
    definitions = SchemaDefinitions()
    nested_reference = Reference(to="Nested")
    direct_reference = Reference(to="Direct")
    field = Object(
        properties={
            "array": Array(items=[Array(items=nested_reference)]),
            "direct": direct_reference,
        }
    )

    set_definitions(field, definitions)

    assert nested_reference.definitions is definitions
    assert direct_reference.definitions is definitions


def test_set_definitions_leaves_plain_field_unchanged():
    definitions = SchemaDefinitions()
    field = String()

    set_definitions(field, definitions)

    assert not hasattr(field, "definitions")
