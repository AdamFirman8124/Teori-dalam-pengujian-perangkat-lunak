# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Object, String
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_direct_reference_sets_definitions():
    ref = Reference("Foo")
    assert ref.definitions is None
    defs = SchemaDefinitions()
    result = set_definitions(ref, defs)
    assert result is None
    assert ref.definitions is defs


def test_reference_with_existing_definitions_not_overwritten():
    original = SchemaDefinitions()
    other = SchemaDefinitions()
    ref = Reference("Foo", definitions=original)
    set_definitions(ref, other)
    assert ref.definitions is original
    assert ref.definitions is not other


def test_array_with_single_field_item_sets_nested_reference():
    ref = Reference("Foo")
    assert ref.definitions is None
    arr = Array(items=ref)
    defs = SchemaDefinitions()
    set_definitions(arr, defs)
    assert ref.definitions is defs


def test_array_with_list_items_sets_all_nested_references():
    ref1 = Reference("Foo")
    ref2 = Reference("Bar")
    arr = Array(items=[ref1, ref2])
    assert ref1.definitions is None
    assert ref2.definitions is None
    defs = SchemaDefinitions()
    set_definitions(arr, defs)
    assert ref1.definitions is defs
    assert ref2.definitions is defs


def test_array_with_tuple_items_sets_all_nested_references():
    ref1 = Reference("Foo")
    ref2 = Reference("Bar")
    arr = Array(items=None)
    # Array.__init__ normalises tuple -> list, so assign tuple directly
    # to exercise the tuple branch of isinstance(field.items, (tuple, list)).
    arr.items = (ref1, ref2)
    defs = SchemaDefinitions()
    set_definitions(arr, defs)
    assert ref1.definitions is defs
    assert ref2.definitions is defs


def test_array_with_none_items_does_nothing():
    arr = Array(items=None)
    assert arr.items is None
    defs = SchemaDefinitions()
    result = set_definitions(arr, defs)
    assert result is None
    assert arr.items is None


def test_object_sets_nested_reference_definitions():
    ref1 = Reference("Foo")
    ref2 = Reference("Bar")
    obj = Object(properties={"a": ref1, "b": ref2})
    defs = SchemaDefinitions()
    set_definitions(obj, defs)
    assert ref1.definitions is defs
    assert ref2.definitions is defs


def test_object_with_empty_properties_does_nothing():
    obj = Object(properties={})
    defs = SchemaDefinitions()
    result = set_definitions(obj, defs)
    assert result is None
    assert obj.properties == {}


def test_plain_field_does_nothing():
    field = String()
    defs = SchemaDefinitions()
    result = set_definitions(field, defs)
    assert result is None
    assert not hasattr(field, "definitions")


def test_nested_object_array_reference_recursion():
    inner_ref = Reference("Foo")
    arr = Array(items=[inner_ref])
    obj = Object(properties={"items": arr})
    outer = Array(items=obj)
    defs = SchemaDefinitions()
    set_definitions(outer, defs)
    assert inner_ref.definitions is defs
