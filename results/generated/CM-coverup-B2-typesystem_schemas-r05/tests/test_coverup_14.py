# file: project/typesystem/schemas.py:189-190
# asked: {"lines": [190], "branches": []}
# gained: {"lines": [190], "branches": []}

from typesystem import Schema, String


def test_schema_len_counts_only_fields_present_on_instance():
    class Person(Schema):
        name = String()
        email = String()

    person = Person(name="Alice")

    assert hasattr(person, "name")
    assert not hasattr(person, "email")
    assert len(person) == 1
