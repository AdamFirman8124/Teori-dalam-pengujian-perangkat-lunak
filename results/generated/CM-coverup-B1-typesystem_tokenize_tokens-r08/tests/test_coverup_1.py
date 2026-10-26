# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

from typesystem.tokenize.tokens import Token, DictToken


class _ScalarToken(Token):
    __hash__ = object.__hash__

    def _get_value(self):
        return self._value


def _make_key(value, start=0, end=1):
    return _ScalarToken(value, start, end, content=str(value))


def _make_value(value, start=0, end=1):
    return _ScalarToken(value, start, end, content=str(value))


def test_dict_token_init_builds_child_caches():
    key_token = _make_key("name", 0, 4)
    value_token = _make_value("example", 5, 12)
    token = DictToken({key_token: value_token}, 0, 12)

    assert token._value == {key_token: value_token}
    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}
    assert token._child_keys["name"] is key_token
    assert token._child_tokens["name"] is value_token


def test_dict_token_get_value():
    key1 = _make_key("a", 0, 1)
    val1 = _make_value(1, 2, 3)
    key2 = _make_key("b", 4, 5)
    val2 = _make_value(2, 6, 7)
    token = DictToken({key1: val1, key2: val2}, 0, 7)

    result = token._get_value()

    assert result == {"a": 1, "b": 2}
    assert token.value == {"a": 1, "b": 2}


def test_dict_token_get_value_empty():
    token = DictToken({}, 0, 2)

    assert token._value == {}
    assert token._child_keys == {}
    assert token._child_tokens == {}
    assert token._get_value() == {}
    assert token.value == {}


def test_dict_token_get_child_token():
    key_token = _make_key("x", 0, 1)
    value_token = _make_value("y", 1, 2)
    token = DictToken({key_token: value_token}, 0, 2)

    child = token._get_child_token("x")

    assert child is value_token
    assert child._value == "y"


def test_dict_token_get_key_token():
    key_token = _make_key("k", 0, 1)
    value_token = _make_value("v", 1, 2)
    token = DictToken({key_token: value_token}, 0, 2)

    found_key = token._get_key_token("k")

    assert found_key is key_token
    assert found_key._value == "k"
