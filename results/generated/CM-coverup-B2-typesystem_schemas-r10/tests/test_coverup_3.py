# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

"""Tests for typesystem.schemas.set_definitions (lines 37-48).

These tests are self-contained: ``set_definitions`` only mutates the field
objects passed to it, and every field used here is created locally inside a
test, so no global or shared state is touched and no cleanup/monkeypatching
is required.
"""

from typesystem.fields import Array, Field, Object
from typesystem.schemas import SchemaDefinitions, set_definitions

try:
    # Import `Reference` from the same namespace that `set_definitions`
    # resolves it from, so the isinstance() checks are guaranteed to match.
    from typesystem.schemas import Reference
except ImportError:  # pragma: no cover - depends on package layout
    from typesystem.fields import Reference


def test_reference_without_definitions_gets_them_set():
    """Lines 37-38: a string-referenced Reference adopts the definitions."""
    definitions = SchemaDefinitions()
    field = Reference(to="Pet")
    assert field.definitions is None

    result = set_definitions(field, definitions)

    assert result is None
    assert field.definitions is definitions


def test_reference_with_existing_definitions_is_left_alone():
    """Line 37 (false branch): already-populated definitions are preserved."""
    existing = SchemaDefinitions()
    replacement = SchemaDefinitions()
    field = Reference(to="Pet", definitions=existing)

    set_definitions(field, replacement)

    assert field.definitions is existing


def test_array_without_items_is_left_alone():
    """Line 40 (false branch): an Array without items is a no-op."""
    definitions = SchemaDefinitions()
    field = Array()
    assert field.items is None

    set_definitions(field, definitions)

    assert field.items is None


def test_array_with_empty_items_list():
    """Lines 40-41 with a zero-iteration loop over the items."""
    definitions = SchemaDefinitions()
    field = Array(items=[])

    set_definitions(field, definitions)

    assert field.items == []


def test_array_with_list_of_items_recurses_into_each_child():
    """Lines 41-43: every field in a list of items is visited."""
    definitions = SchemaDefinitions()
    first = Reference(to="A")
    second = Reference(to="B")
    plain = Field()
    field = Array(items=[first, second, plain])

    set_definitions(field, definitions)

    assert first.definitions is definitions
    assert second.definitions is definitions
    # A plain Field matches no branch and must stay untouched.
    assert getattr(plain, "definitions", None) is None


def test_array_with_single_item_field_recurses_into_it():
    """Line 45: a single (non-sequence) item field is visited."""
    definitions = SchemaDefinitions()
    child = Reference(to="A")
    field = Array(items=child)

    set_definitions(field, definitions)

    assert child.definitions is definitions


def test_object_recurses_into_each_property():
    """Lines 46-48: every property of an Object is visited."""
    definitions = SchemaDefinitions()
    first = Reference(to="A")
    second = Reference(to="B")
    plain = Field()
    field = Object(properties={"first": first, "second": second, "plain": plain})

    set_definitions(field, definitions)

    assert first.definitions is definitions
    assert second.definitions is definitions
    assert getattr(plain, "definitions", None) is None


def test_object_without_properties():
    """Lines 46-47 with a zero-iteration loop over the properties."""
    definitions = SchemaDefinitions()
    field = Object()

    set_definitions(field, definitions)

    assert field.properties == {}


def test_plain_field_is_left_alone():
    """A bare Field matches neither Reference, Array nor Object."""
    definitions = SchemaDefinitions()
    field = Field()

    set_definitions(field, definitions)

    assert getattr(field, "definitions", None) is None


def test_nested_structures_are_handled_recursively():
    """Recursion descends through nested Objects and Arrays."""
    definitions = SchemaDefinitions()
    list_child = Reference(to="Leaf")
    single_child = Reference(to="Single")
    nested_child = Reference(to="Nested")
    schema = Object(
        properties={
            "list": Array(items=[list_child]),
            "single": Array(items=single_child),
            "nested": Object(properties={"leaf": nested_child}),
        }
    )

    set_definitions(schema, definitions)

    assert list_child.definitions is definitions
    assert single_child.definitions is definitions
    assert nested_child.definitions is definitions
