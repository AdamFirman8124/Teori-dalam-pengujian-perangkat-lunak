# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Object, String
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_set_definitions_sets_reference_and_preserves_existing_definitions():
    definitions = SchemaDefinitions()
    existing_definitions = SchemaDefinitions()

    unset_reference = Reference("UnsetTarget")
    configured_reference = Reference(
        "ConfiguredTarget", definitions=existing_definitions
    )

    set_definitions(unset_reference, definitions)
    set_definitions(configured_reference, definitions)

    assert unset_reference.definitions is definitions
    assert configured_reference.definitions is existing_definitions


def test_set_definitions_handles_all_array_item_variants():
    definitions = SchemaDefinitions()
    single_reference = Reference("SingleTarget")
    first_reference = Reference("FirstTarget")
    second_reference = Reference("SecondTarget")

    empty_array = Array()
    single_item_array = Array(items=single_reference)
    multiple_item_array = Array(items=(first_reference, second_reference))
    zero_length_array = Array(items=[])

    set_definitions(empty_array, definitions)
    set_definitions(single_item_array, definitions)
    set_definitions(multiple_item_array, definitions)
    set_definitions(zero_length_array, definitions)

    assert empty_array.items is None
    assert single_reference.definitions is definitions
    assert first_reference.definitions is definitions
    assert second_reference.definitions is definitions
    assert zero_length_array.items == []


def test_set_definitions_recurses_through_objects_and_ignores_leaf_fields():
    definitions = SchemaDefinitions()
    direct_reference = Reference("DirectTarget")
    nested_reference = Reference("NestedTarget")
    leaf = String()

    field = Object(
        properties={
            "direct": direct_reference,
            "nested": Array(
                items=Object(properties={"reference": nested_reference})
            ),
            "leaf": leaf,
            "empty_object": Object(),
        }
    )

    set_definitions(field, definitions)

    assert direct_reference.definitions is definitions
    assert nested_reference.definitions is definitions
    assert field.properties["leaf"] is leaf
    assert field.properties["empty_object"].properties == {}
