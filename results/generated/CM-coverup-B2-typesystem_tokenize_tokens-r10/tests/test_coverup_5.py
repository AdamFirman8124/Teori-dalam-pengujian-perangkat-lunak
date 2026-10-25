# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_token_equality_rejects_non_token():
    token = ScalarToken("value", 1, 2)

    assert (token == object()) is False


def test_token_equality_rejects_different_value():
    left = ScalarToken("value", 1, 2)
    right = ScalarToken("different", 1, 2)

    assert (left == right) is False


def test_token_equality_rejects_different_start_index():
    left = ScalarToken("value", 1, 2)
    right = ScalarToken("value", 0, 2)

    assert (left == right) is False


def test_token_equality_rejects_different_end_index():
    left = ScalarToken("value", 1, 2)
    right = ScalarToken("value", 1, 3)

    assert (left == right) is False


def test_tokens_with_matching_value_and_indexes_are_equal():
    left = ScalarToken("value", 1, 2)
    right = ScalarToken("value", 1, 2)

    assert (left == right) is True
