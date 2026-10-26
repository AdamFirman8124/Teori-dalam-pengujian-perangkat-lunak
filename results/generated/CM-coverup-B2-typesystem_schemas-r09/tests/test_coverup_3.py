# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

import pytest

from typesystem.fields import Array, Object
from typesystem.schemas import SchemaDefinitions, Reference, set_definitions


def test_set_definitions_on_reference():
    definitions = SchemaDefinitions()
    ref = Reference(to="SomeSchema")
    assert ref.definitions is None

    set_definitions(ref, definitions)

    assert ref.definitions is definitions


def test_set_definitions_skips_reference_with_existing_definitions():
    existing = SchemaDefinitions()
    new = SchemaDefinitions()
    ref = Reference(to="SomeSchema", definitions=existing)

    set_definitions(ref, new)

    assert ref.definitions is existing


def test_set_definitions_on_array_with_list_items():
    definitions = SchemaDefinitions()
    ref1 = Reference(to="A")
    ref2 = Reference(to="B")
    array = Array(items=[ref1, ref2])

    set_definitions(array, definitions)

    assert ref1.definitions is definitions
    assert ref2.definitions is definitions


def test_set_definitions_on_array_with_single_item():
    definitions = SchemaDefinitions()
    ref = Reference(to="A")
    array = Array(items=ref)

    set_definitions(array, definitions)

    assert ref.definitions is definitions


def test_set_definitions_on_array_without_items():
    definitions = SchemaDefinitions()
    array = Array(items=None)

    # Must not raise; nothing to recurse into.
    set_definitions(array, definitions)


def test_set_definitions_on_object_properties():
    definitions = SchemaDefinitions()
    ref1 = Reference(to="A")
    ref2 = Reference(to="B")
    obj = Object(properties={"a": ref1, "b": ref2})

    set_definitions(obj, definitions)

    assert ref1.definitions is definitions
    assert ref2.definitions is definitions


def test_set_definitions_nested_recursion():
    definitions = SchemaDefinitions()
    ref = Reference(to="A")
    obj = Object(properties={"inner": Array(items=[ref])})

    set_definitions(obj, definitions)

    assert ref.definitions is definitions
