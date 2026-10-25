# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Field, Object
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_set_definitions_assigns_to_bare_reference():
    definitions = SchemaDefinitions()
    field = Reference("Foo")
    assert field.definitions is None
    set_definitions(field, definitions)
    assert field.definitions is definitions


def test_set_definitions_does_not_overwrite_existing_definitions():
    definitions_a = SchemaDefinitions()
    definitions_b = SchemaDefinitions()
    field = Reference("Foo", definitions=definitions_a)
    set_definitions(field, definitions_b)
    assert field.definitions is definitions_a


def test_set_definitions_array_with_single_item():
    definitions = SchemaDefinitions()
    child = Reference("Foo")
    field = Array(items=child)
    set_definitions(field, definitions)
    assert child.definitions is definitions
    assert field.items is child


def test_set_definitions_array_with_list_items():
    definitions = SchemaDefinitions()
    child1 = Reference("A")
    child2 = Reference("B")
    field = Array(items=[child1, child2])
    set_definitions(field, definitions)
    assert child1.definitions is definitions
    assert child2.definitions is definitions


def test_set_definitions_array_with_tuple_items():
    definitions = SchemaDefinitions()
    child1 = Reference("A")
    child2 = Reference("B")
    field = Array(items=None)
    field.items = (child1, child2)
    set_definitions(field, definitions)
    assert child1.definitions is definitions
    assert child2.definitions is definitions


def test_set_definitions_array_with_no_items():
    definitions = SchemaDefinitions()
    field = Array(items=None)
    set_definitions(field, definitions)
    assert field.items is None


def test_set_definitions_array_with_empty_list_items():
    definitions = SchemaDefinitions()
    field = Array(items=[])
    set_definitions(field, definitions)
    assert field.items == []


def test_set_definitions_object_with_properties():
    definitions = SchemaDefinitions()
    child1 = Reference("A")
    child2 = Reference("B")
    field = Object(properties={"a": child1, "b": child2})
    set_definitions(field, definitions)
    assert child1.definitions is definitions
    assert child2.definitions is definitions


def test_set_definitions_object_empty():
    definitions = SchemaDefinitions()
    field = Object(properties={})
    set_definitions(field, definitions)
    assert field.properties == {}


def test_set_definitions_plain_field_is_ignored():
    definitions = SchemaDefinitions()
    field = Field()
    set_definitions(field, definitions)
    assert not hasattr(field, "definitions")


def test_set_definitions_nested_object_array_reference():
    definitions = SchemaDefinitions()
    inner_ref = Reference("Inner")
    arr = Array(items=inner_ref)
    obj = Object(properties={"arr": arr})
    outer = Array(items=[obj, Reference("Other")])
    set_definitions(outer, definitions)
    assert inner_ref.definitions is definitions
    assert outer.items[1].definitions is definitions
