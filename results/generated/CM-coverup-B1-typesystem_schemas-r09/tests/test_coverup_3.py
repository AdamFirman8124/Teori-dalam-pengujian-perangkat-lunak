# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

import pytest

from typesystem.fields import Array, Field, Object
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


@pytest.fixture(autouse=True)
def preserve_field_creation_counter(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)


def test_set_definitions_updates_reference_without_definitions():
    definitions = SchemaDefinitions()
    reference = Reference("Target")

    assert reference.definitions is None

    set_definitions(reference, definitions)

    assert reference.definitions is definitions


def test_set_definitions_preserves_existing_reference_definitions():
    existing_definitions = SchemaDefinitions()
    replacement_definitions = SchemaDefinitions()
    reference = Reference("Target", definitions=existing_definitions)

    set_definitions(reference, replacement_definitions)

    assert reference.definitions is existing_definitions


def test_set_definitions_recurses_through_arrays_and_objects():
    definitions = SchemaDefinitions()
    scalar_array_reference = Reference("ScalarArrayTarget")
    list_array_reference = Reference("ListArrayTarget")
    object_reference = Reference("ObjectTarget")

    array_without_items = Array()
    scalar_array = Array(items=scalar_array_reference)
    list_array = Array(
        items=[
            list_array_reference,
            Object(properties={"nested": object_reference}),
        ]
    )

    set_definitions(array_without_items, definitions)
    set_definitions(scalar_array, definitions)
    set_definitions(list_array, definitions)

    assert array_without_items.items is None
    assert scalar_array_reference.definitions is definitions
    assert list_array_reference.definitions is definitions
    assert object_reference.definitions is definitions
