# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Object, String
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_reference_without_definitions_gets_definitions():
    definitions = SchemaDefinitions({"name": String()})
    field = Reference(to="name")
    assert field.definitions is None

    set_definitions(field, definitions)

    assert field.definitions is definitions


def test_reference_with_existing_definitions_not_overwritten():
    definitions = SchemaDefinitions({"name": String()})
    existing = SchemaDefinitions({"other": String()})
    field = Reference(to="name", definitions=existing)

    set_definitions(field, definitions)

    assert field.definitions is existing


def test_array_with_single_field_item():
    definitions = SchemaDefinitions({"name": String()})
    child = Reference(to="name")
    field = Array(items=child)

    set_definitions(field, definitions)

    assert child.definitions is definitions


def test_array_with_list_items():
    definitions = SchemaDefinitions({"a": String(), "b": String()})
    child_a = Reference(to="a")
    child_b = Reference(to="b")
    field = Array(items=[child_a, child_b])

    set_definitions(field, definitions)

    assert child_a.definitions is definitions
    assert child_b.definitions is definitions


def test_array_with_tuple_items():
    definitions = SchemaDefinitions({"a": String()})
    child = Reference(to="a")
    field = Array(items=child)
    # Array normalises tuple/list to list, so force a tuple to cover
    # the `isinstance(field.items, (tuple, list))` tuple branch.
    field.items = (child,)

    set_definitions(field, definitions)

    assert child.definitions is definitions


def test_array_with_no_items_is_noop():
    definitions = SchemaDefinitions({"a": String()})
    field = Array(items=None)

    set_definitions(field, definitions)

    assert field.items is None


def test_object_properties_recursion():
    definitions = SchemaDefinitions({"a": String(), "b": String()})
    child_a = Reference(to="a")
    child_b = Reference(to="b")
    field = Object(properties={"x": child_a, "y": child_b})

    set_definitions(field, definitions)

    assert child_a.definitions is definitions
    assert child_b.definitions is definitions


def test_nested_object_and_array_recursion():
    definitions = SchemaDefinitions({"a": String(), "b": String()})
    ref_single = Reference(to="a")
    ref_in_list = Reference(to="b")
    ref_in_object = Reference(to="a")
    inner_array = Array(items=[ref_in_list])
    inner_object = Object(properties={"nested": ref_in_object})
    outer = Object(properties={"arr": inner_array, "obj": inner_object, "single": Array(items=ref_single)})

    set_definitions(outer, definitions)

    assert ref_single.definitions is definitions
    assert ref_in_list.definitions is definitions
    assert ref_in_object.definitions is definitions


def test_plain_field_is_noop():
    definitions = SchemaDefinitions({"a": String()})
    field = String()

    set_definitions(field, definitions)

    assert isinstance(field, String)
