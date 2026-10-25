# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

from typesystem.schemas import Schema


def test_schema_iter_yields_only_fields_present_on_instance():
    schema = Schema()
    schema.fields = {"present": object(), "missing": object()}
    schema.present = "value"

    iterator = iter(schema)

    assert next(iterator) == "present"
    assert list(iterator) == []
    assert schema.present == "value"
    assert not hasattr(schema, "missing")
