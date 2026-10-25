# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Field, Object
from typesystem.schemas import SchemaDefinitions, set_definitions

try:
    from typesystem.schemas import Reference
except ImportError:  # fallback if re-exported elsewhere
    from typesystem.fields import Reference  # type: ignore


def _fresh_definitions():
    try:
        return SchemaDefinitions({"Foo": Field()})
    except Exception:
        return SchemaDefinitions()


def _make_reference(definitions=None, ref_name="Foo"):
    r = None
    candidates = [
        lambda: Reference(ref_name),
        lambda: Reference(ref=ref_name),
        lambda: Reference(reference=ref_name),
        lambda: Reference(ref_name, definitions=definitions),
    ]
    for make in candidates:
        try:
            r = make()
            break
        except Exception:
            continue
    if r is None:
        r = Reference.__new__(Reference)
    # Force desired precondition regardless of constructor signature.
    r.definitions = definitions
    if not hasattr(r, "ref"):
        try:
            r.ref = ref_name
        except Exception:
            pass
    return r


def test_set_definitions_reference_without_definitions():
    defs = _fresh_definitions()
    ref = _make_reference(definitions=None)
    assert ref.definitions is None
    set_definitions(ref, defs)
    assert ref.definitions is defs


def test_set_definitions_reference_with_existing_definitions_keeps():
    defs_old = _fresh_definitions()
    defs_new = _fresh_definitions()
    assert defs_old is not defs_new
    ref = _make_reference(definitions=defs_old)
    assert ref.definitions is defs_old
    set_definitions(ref, defs_new)
    # Branch: isinstance Reference True but definitions is not None -> no overwrite.
    assert ref.definitions is defs_old
    assert ref.definitions is not defs_new


def test_set_definitions_array_single_item():
    defs = _fresh_definitions()
    inner = _make_reference(definitions=None)
    arr = Array(items=inner)
    assert arr.items is inner
    set_definitions(arr, defs)
    # Covers: Array True, items is not None True, isinstance(tuple,list) False -> else
    assert inner.definitions is defs


def test_set_definitions_array_list_items():
    defs = _fresh_definitions()
    inner1 = _make_reference(definitions=None)
    inner2 = _make_reference(definitions=None)
    arr = Array(items=[inner1, inner2])
    assert isinstance(arr.items, list)
    set_definitions(arr, defs)
    # Covers: Array True, items is not None True, isinstance(tuple,list) True, loop
    assert inner1.definitions is defs
    assert inner2.definitions is defs


def test_set_definitions_array_tuple_items():
    defs = _fresh_definitions()
    inner1 = _make_reference(definitions=None)
    inner2 = _make_reference(definitions=None)
    arr = Array(items=[inner1])
    # Force tuple to explicitly execute tuple branch of isinstance(field.items, (tuple, list))
    arr.items = (inner1, inner2)
    assert isinstance(arr.items, tuple)
    set_definitions(arr, defs)
    assert inner1.definitions is defs
    assert inner2.definitions is defs


def test_set_definitions_array_no_items():
    defs = _fresh_definitions()
    arr = Array(items=None)
    assert arr.items is None
    set_definitions(arr, defs)
    # Covers: Array True, items is not None False -> no recursion
    assert arr.items is None


def test_set_definitions_object_properties():
    defs = _fresh_definitions()
    inner1 = _make_reference(definitions=None)
    inner2 = _make_reference(definitions=None)
    obj = Object(properties={"a": inner1, "b": inner2})
    set_definitions(obj, defs)
    # Covers: Object branch + for loop over properties.values()
    assert inner1.definitions is defs
    assert inner2.definitions is defs


def test_set_definitions_nested_object_in_array_and_array_in_object():
    defs = _fresh_definitions()
    ref1 = _make_reference(definitions=None)
    ref2 = _make_reference(definitions=None)
    ref3 = _make_reference(definitions=None)
    inner_obj = Object(properties={"x": ref1})
    inner_arr = Array(items=[ref2, ref3])
    outer_arr = Array(items=inner_obj)
    outer_obj = Object(properties={"arr": inner_arr})
    set_definitions(outer_arr, defs)
    set_definitions(outer_obj, defs)
    assert ref1.definitions is defs
    assert ref2.definitions is defs
    assert ref3.definitions is defs


def test_set_definitions_plain_field_noop():
    defs = _fresh_definitions()
    plain = Field()
    # Covers: not Reference, not Array, not Object -> all conditions False
    set_definitions(plain, defs)
    assert not hasattr(plain, "definitions") or getattr(plain, "definitions", None) is not defs


def test_set_definitions_object_empty_properties():
    defs = _fresh_definitions()
    obj = Object(properties={})
    assert list(obj.properties.values()) == []
    set_definitions(obj, defs)
    assert list(obj.properties.values()) == []
