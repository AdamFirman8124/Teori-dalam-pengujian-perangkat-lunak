# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

import pytest

from typesystem.fields import Array, Object, String
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_set_definitions_reference():
    definitions = SchemaDefinitions({"Foo": String()})
    ref = Reference("Foo")
    assert ref.definitions is None
    set_definitions(ref, definitions)
    assert ref.definitions is definitions


def test_set_definitions_reference_already_set():
    definitions = SchemaDefinitions({"Foo": String()})
    existing = SchemaDefinitions({"Bar": String()})
    ref = Reference("Foo", definitions=existing)
    set_definitions(ref, definitions)
    assert ref.definitions is existing


def test_set_definitions_array_multiple_items():
    definitions = SchemaDefinitions({"Foo": String()})
    ref1 = Reference("Foo")
    ref2 = Reference("Foo")
    array = Array(items=[ref1, ref2])
    set_definitions(array, definitions)
    assert ref1.definitions is definitions
    assert ref2.definitions is definitions


def test_set_definitions_array_single_item():
    definitions = SchemaDefinitions({"Foo": String()})
    ref = Reference("Foo")
    array = Array(items=ref)
    set_definitions(array, definitions)
    assert ref.definitions is definitions


def test_set_definitions_array_no_items():
    definitions = SchemaDefinitions({"Foo": String()})
    array = Array(items=None)
    set_definitions(array, definitions)
    assert array.items is None


def test_set_definitions_object_properties():
    definitions = SchemaDefinitions({"Foo": String()})
    ref1 = Reference("Foo")
    ref2 = Reference("Foo")
    obj = Object(properties={"a": ref1, "b": ref2})
    set_definitions(obj, definitions)
    assert ref1.definitions is definitions
    assert ref2.definitions is definitions


def test_set_definitions_nested():
    definitions = SchemaDefinitions({"Foo": String()})
    ref = Reference("Foo")
    obj = Object(properties={"a": Array(items=[ref])})
    set_definitions(obj, definitions)
    assert ref.definitions is definitions
