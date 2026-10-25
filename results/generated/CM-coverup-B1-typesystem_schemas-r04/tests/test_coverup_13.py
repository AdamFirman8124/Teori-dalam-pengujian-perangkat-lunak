# file: project/typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

import pytest

from typesystem import String
from typesystem.schemas import Schema


class PersonSchema(Schema):
    name = String()
    age = String()


def test_is_sparse_true_when_field_missing():
    # Instantiate with only one of the two fields: 'age' is not set,
    # so the schema is sparse and line 164 executes with a truthy result.
    person = PersonSchema(name="Alice")
    assert person.is_sparse is True


def test_is_sparse_false_when_all_fields_present():
    # Instantiate with all fields set: the comprehension yields an empty
    # list, so line 164 executes with a falsy result.
    person = PersonSchema(name="Alice", age="30")
    assert person.is_sparse is False
