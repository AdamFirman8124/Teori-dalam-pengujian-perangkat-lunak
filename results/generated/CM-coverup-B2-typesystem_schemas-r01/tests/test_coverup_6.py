# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

import pytest

from typesystem import String
from typesystem.schemas import Schema


class ExampleSchema(Schema):
    name = String()
    email = String()


def test_iter_yields_only_set_fields():
    # Instantiate with only one of the two fields, so `email` has no
    # attribute on the instance and must be skipped by __iter__.
    instance = ExampleSchema(name="alice")

    keys = list(iter(instance))

    assert keys == ["name"]
    assert "email" not in keys


def test_iter_yields_all_set_fields():
    instance = ExampleSchema(name="alice", email="alice@example.com")

    keys = list(iter(instance))

    assert keys == ["name", "email"]
    assert all(hasattr(instance, key) for key in keys)
