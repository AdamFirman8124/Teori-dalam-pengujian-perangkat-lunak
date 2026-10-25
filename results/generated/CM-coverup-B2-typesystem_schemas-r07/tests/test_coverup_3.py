# file: project/typesystem/schemas.py:32-48
# asked: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

from typesystem.fields import Array, Field, Object, String
from typesystem.schemas import Reference, SchemaDefinitions, set_definitions


def test_set_definitions_recurses_through_references_arrays_and_objects(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", Field._creation_counter)

    definitions = SchemaDefinitions()
    existing_definitions = SchemaDefinitions()

    direct_reference = Reference("Direct")
    preserved_reference = Reference("Preserved", definitions=existing_definitions)
    list_reference = Reference("ListItem")
    single_reference = Reference("SingleItem")

    list_array = Array(items=[list_reference, preserved_reference, String()])
    single_array = Array(items=single_reference)
    empty_array = Array()
    field = Object(
        properties={
            "direct": direct_reference,
            "list": list_array,
            "single": single_array,
            "empty": empty_array,
        }
    )

    set_definitions(field, definitions)

    assert direct_reference.definitions is definitions
    assert list_reference.definitions is definitions
    assert single_reference.definitions is definitions
    assert preserved_reference.definitions is existing_definitions
    assert empty_array.items is None
    assert field.properties["list"] is list_array
    assert field.properties["single"] is single_array
