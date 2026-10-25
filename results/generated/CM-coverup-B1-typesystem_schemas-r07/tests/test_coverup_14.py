# file: project/typesystem/schemas.py:189-190
# asked: {"lines": [190], "branches": []}
# gained: {"lines": [190], "branches": []}

from typesystem.schemas import Schema


def test_schema_len_counts_only_fields_present_on_instance():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {"present": object(), "missing": object()}
    instance = ExampleSchema({"present": "value"})

    assert hasattr(instance, "present")
    assert not hasattr(instance, "missing")
    assert len(instance) == 1
