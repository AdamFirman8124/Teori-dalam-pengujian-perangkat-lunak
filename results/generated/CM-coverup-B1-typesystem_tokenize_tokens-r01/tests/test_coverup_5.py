# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

from typesystem.tokenize.tokens import ScalarToken, Token


def test_token_equality_rejects_non_token_and_mismatched_fields():
    token = ScalarToken("value", 1, 2)

    assert Token.__eq__(token, object()) is False
    assert Token.__eq__(token, ScalarToken("different", 1, 2)) is False
    assert Token.__eq__(token, ScalarToken("value", 0, 2)) is False
    assert Token.__eq__(token, ScalarToken("value", 1, 3)) is False


def test_token_equality_accepts_matching_value_and_indexes():
    token = ScalarToken("value", 1, 2, content="first")
    matching_token = ScalarToken("value", 1, 2, content="second")

    assert Token.__eq__(token, matching_token) is True
    assert token == matching_token
