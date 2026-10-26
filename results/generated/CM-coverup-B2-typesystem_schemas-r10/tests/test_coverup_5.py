# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

import pytest

from typesystem import Schema, String


class ExampleSchema(Schema):
    name = String()
    nickname = String()


def test_iter_yields_fields_set_on_instance():
    instance = ExampleSchema(name="alice")
    # 'name' is set as an attribute, so hasattr() is True -> line 187 executes.
    assert list(iter(instance)) == ["name"]


def test_iter_skips_fields_not_set_on_instance():
    instance = ExampleSchema(name="alice")
    # 'nickname' is a declared field but was not passed in, so it is not
    # an attribute of the instance -> hasattr() is False -> line 186's
    # False branch is covered and 'nickname' is not yielded.
    assert "nickname" not in list(iter(instance))


def test_mapping_protocol_uses_iter():
    instance = ExampleSchema(name="bob")
    assert dict(instance) == {"name": "bob"}
    assert "nickname" not in dict(instance)
    assert len(instance) == 1
