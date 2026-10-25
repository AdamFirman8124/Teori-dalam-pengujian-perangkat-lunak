# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_token_equality_with_identical_tokens():
    left = ScalarToken("value", 1, 6)
    right = ScalarToken("value", 1, 6)

    assert left == right
    assert right == left


def test_token_equality_with_non_token():
    token = ScalarToken("value", 1, 6)

    assert not token.__eq__(object())


def test_token_equality_with_different_values():
    left = ScalarToken("left", 1, 6)
    right = ScalarToken("right", 1, 6)

    assert left != right


def test_token_equality_with_different_start_indices():
    left = ScalarToken("value", 1, 6)
    right = ScalarToken("value", 2, 6)

    assert left != right


def test_token_equality_with_different_end_indices():
    left = ScalarToken("value", 1, 6)
    right = ScalarToken("value", 1, 7)

    assert left != right
