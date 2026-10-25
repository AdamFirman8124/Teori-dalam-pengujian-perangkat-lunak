# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

import pytest

from typesystem import Integer, String
from typesystem.schemas import Schema


class ExampleSchema(Schema):
    name = String()
    age = Integer()


def test_iter_yields_only_fields_set_as_attributes():
    # Instantiate with only one of the two fields, so that:
    # - 'name' is an attribute -> hasattr is True -> line 187 executes (yield)
    # - 'age' is in self.fields but not an attribute -> hasattr is False -> line 187 skipped
    instance = ExampleSchema(name="alice")

    keys = list(iter(instance))

    assert keys == ["name"]
    assert "age" not in keys


def test_iter_yields_all_fields_when_all_set():
    instance = ExampleSchema(name="alice", age=30)

    keys = list(iter(instance))

    assert sorted(keys) == ["age", "name"]
