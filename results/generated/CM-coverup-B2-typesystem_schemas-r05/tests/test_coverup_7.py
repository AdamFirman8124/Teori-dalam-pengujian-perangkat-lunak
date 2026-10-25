# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

import typesystem


def test_schema_repr_includes_all_present_fields():
    class Person(typesystem.Schema):
        name = typesystem.String()
        nickname = typesystem.String()

    person = Person({"name": "Ada", "nickname": "Enchantress"})

    assert person.is_sparse is False
    assert repr(person) == "Person(name='Ada', nickname='Enchantress')"


def test_schema_repr_marks_missing_fields_as_sparse():
    class Person(typesystem.Schema):
        name = typesystem.String()
        nickname = typesystem.String()

    person = Person({"name": "Ada"})

    assert person.is_sparse is True
    assert not hasattr(person, "nickname")
    assert repr(person) == "Person(name='Ada') [sparse]"
