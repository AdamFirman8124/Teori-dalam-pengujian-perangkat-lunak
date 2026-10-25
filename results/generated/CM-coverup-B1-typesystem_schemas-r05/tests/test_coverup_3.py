# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

import pytest

from typesystem.fields import Array, Object, String
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_set_definitions_reference_with_no_definitions():
    definitions = SchemaDefinitions({"Example": String()})
    field = Reference("Example")
    assert field.definitions is None

    set_definitions(field, definitions)

    assert field.definitions is definitions


def test_set_definitions_reference_with_existing_definitions_is_untouched():
    existing = SchemaDefinitions({"Example": String()})
    other = SchemaDefinitions({"Other": String()})
    field = Reference("Example", definitions=existing)
    assert field.definitions is existing

    set_definitions(field, other)

    assert field.definitions is existing


def test_set_definitions_array_with_list_of_items():
    definitions = SchemaDefinitions({"Example": String()})
    ref = Reference("Example")
    field = Array(items=[ref, String()])

    set_definitions(field, definitions)

    assert ref.definitions is definitions


def test_set_definitions_array_with_single_item():
    definitions = SchemaDefinitions({"Example": String()})
    ref = Reference("Example")
    field = Array(items=ref)

    set_definitions(field, definitions)

    assert ref.definitions is definitions


def test_set_definitions_array_with_no_items():
    definitions = SchemaDefinitions({"Example": String()})
    field = Array()

    set_definitions(field, definitions)

    assert field.items is None


def test_set_definitions_object_properties():
    definitions = SchemaDefinitions({"Example": String()})
    ref = Reference("Example")
    field = Object(properties={"a": ref, "b": String()})

    set_definitions(field, definitions)

    assert field.properties["a"].definitions is definitions


def test_set_definitions_nested_structures():
    definitions = SchemaDefinitions({"Example": String()})
    inner_ref = Reference("Example")
    inner_array = Array(items=inner_ref)
    inner_object = Object(properties={"x": inner_array})
    outer_ref = Reference("Example")
    outer = Object(
        properties={
            "list": Array(items=[inner_object, outer_ref]),
            "single": Array(items=inner_object),
        }
    )

    set_definitions(outer, definitions)

    assert inner_ref.definitions is definitions
    assert outer_ref.definitions is definitions
    assert outer.properties["list"].items[0].properties["x"].items.definitions is definitions
    assert outer.properties["single"].items.properties["x"].items.definitions is definitions


def test_set_definitions_ignores_plain_fields():
    definitions = SchemaDefinitions({"Example": String()})
    field = String()

    set_definitions(field, definitions)

    assert not hasattr(field, "definitions") or field.definitions is not definitions
