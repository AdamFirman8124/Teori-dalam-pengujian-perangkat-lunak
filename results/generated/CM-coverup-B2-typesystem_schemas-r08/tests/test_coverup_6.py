# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

import pytest

from typesystem import Schema, String


class ExampleSchema(Schema):
    name = String()
    nickname = String(allow_null=True)


def test_iter_yields_fields_set_on_instance():
    instance = ExampleSchema(name="alice")
    # Both fields have values on the instance, so hasattr() is True for each
    # and line 187 yields both keys, in field-definition order.
    assert list(iter(instance)) == ["name", "nickname"]


def test_iter_skips_fields_not_set_on_instance():
    instance = ExampleSchema(name="alice")
    # Remove one attribute so hasattr() is False for it -> line 186's False
    # branch is covered and the key is not yielded.
    del instance.nickname
    assert not hasattr(instance, "nickname")

    assert list(iter(instance)) == ["name"]
    assert "nickname" not in list(iter(instance))


def test_mapping_protocol_uses_iter():
    instance = ExampleSchema(name="bob")
    assert dict(instance) == {"name": "bob", "nickname": None}
    assert len(instance) == 2

    del instance.nickname
    assert dict(instance) == {"name": "bob"}
    assert len(instance) == 1
    with pytest.raises(KeyError):
        instance["nickname"]
