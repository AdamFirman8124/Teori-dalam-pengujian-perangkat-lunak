# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

from typesystem.tokenize.tokens import DictToken, ScalarToken


def _scalar(value):
    return ScalarToken(value, 0, 1)


def test_dict_token_init_and_get_value():
    key_token = _scalar("a")
    value_token = _scalar(1)
    token = DictToken({key_token: value_token}, 0, 10)

    assert token._child_keys == {"a": key_token}
    assert token._child_tokens == {"a": value_token}
    assert token._get_value() == {"a": 1}


def test_dict_token_get_child_token():
    key_token = _scalar("a")
    value_token = _scalar(1)
    token = DictToken({key_token: value_token}, 0, 10)

    assert token._get_child_token("a") is value_token


def test_dict_token_get_key_token():
    key_token = _scalar("a")
    value_token = _scalar(1)
    token = DictToken({key_token: value_token}, 0, 10)

    assert token._get_key_token("a") is key_token


def test_dict_token_nested_values():
    inner_key = _scalar("x")
    inner_value = _scalar(True)
    inner = DictToken({inner_key: inner_value}, 0, 5)

    outer_key = _scalar("outer")
    token = DictToken({outer_key: inner}, 0, 20)

    assert token._get_value() == {"outer": {"x": True}}
    assert token._get_child_token("outer") is inner
    assert token._get_key_token("outer") is outer_key
