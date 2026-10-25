# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Object, String
from typesystem.schemas import SchemaDefinitions, set_definitions
from typesystem.schemas import Reference


def test_set_definitions_reference():
    definitions = SchemaDefinitions({"Foo": String()})
    field = Reference(to="Foo")
    assert field.definitions is None
    set_definitions(field, definitions)
    assert field.definitions is definitions


def test_set_definitions_reference_already_set():
    definitions = SchemaDefinitions({"Foo": String()})
    existing = SchemaDefinitions({"Bar": String()})
    field = Reference(to="Foo", definitions=existing)
    set_definitions(field, definitions)
    assert field.definitions is existing


def test_set_definitions_array_with_list_items():
    definitions = SchemaDefinitions({"Foo": String()})
    ref = Reference(to="Foo")
    field = Array(items=[ref, String()])
    set_definitions(field, definitions)
    assert ref.definitions is definitions


def test_set_definitions_array_with_single_item():
    definitions = SchemaDefinitions({"Foo": String()})
    ref = Reference(to="Foo")
    field = Array(items=ref)
    set_definitions(field, definitions)
    assert ref.definitions is definitions


def test_set_definitions_array_without_items():
    definitions = SchemaDefinitions({"Foo": String()})
    field = Array(items=None)
    # Must not raise; nothing to recurse into.
    set_definitions(field, definitions)
    assert field.items is None


def test_set_definitions_object_properties():
    definitions = SchemaDefinitions({"Foo": String()})
    ref1 = Reference(to="Foo")
    ref2 = Reference(to="Foo")
    field = Object(properties={"a": ref1, "b": ref2})
    set_definitions(field, definitions)
    assert ref1.definitions is definitions
    assert ref2.definitions is definitions


def test_set_definitions_nested():
    definitions = SchemaDefinitions({"Foo": String()})
    ref = Reference(to="Foo")
    field = Object(properties={"a": Array(items=[Object(properties={"b": ref})])})
    set_definitions(field, definitions)
    assert ref.definitions is definitions
