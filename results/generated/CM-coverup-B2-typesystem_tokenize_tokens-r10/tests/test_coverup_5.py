# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

"""Tests targeting Token.__eq__ (typesystem/tokenize/tokens.py, lines 67-70).

These tests are pure/stateless: they only construct local Token objects and
compare them, so no monkeypatching or teardown is required to avoid state
pollution. ScalarToken is used because it is a concrete Token subclass that
implements _get_value() (the base Token._get_value raises NotImplementedError).
"""

from typesystem.tokenize.tokens import ScalarToken, Token


def make_token(value="x", start_index=0, end_index=1, content=""):
    """Build a concrete Token for comparison tests."""
    token = ScalarToken(
        value=value, start_index=start_index, end_index=end_index, content=content
    )
    assert isinstance(token, Token)
    return token


def test_token_eq_all_fields_equal():
    """Lines 67-70 all evaluate to True for identical tokens."""
    token_a = make_token()
    token_b = make_token()

    assert token_a == token_b
    assert token_a == token_a  # self-comparison also runs the full chain
    assert token_a.__eq__(token_b) is True
    assert not (token_a != token_b)


def test_token_eq_ignores_content():
    """__eq__ compares value and indices only; content is irrelevant."""
    token_a = make_token(content="first")
    token_b = make_token(content="second")

    assert token_a == token_b


def test_token_eq_different_value():
    """Line 68 False branch: differing values make tokens unequal."""
    token_a = make_token(value="x")
    token_b = make_token(value="y")

    assert token_a != token_b
    assert token_a.__eq__(token_b) is False
    assert not (token_a == token_b)


def test_token_eq_different_start_index():
    """Line 69 False branch: same value but different start index."""
    token_a = make_token(start_index=0)
    token_b = make_token(start_index=5)

    assert token_a != token_b
    assert token_a.__eq__(token_b) is False


def test_token_eq_different_end_index():
    """Line 70 False branch: same value and start index, different end index."""
    token_a = make_token(end_index=1)
    token_b = make_token(end_index=9)

    assert token_a != token_b
    assert token_a.__eq__(token_b) is False


def test_token_eq_against_non_token():
    """Line 67 False branch: comparison with a non-Token is always False."""
    token = make_token()

    assert token.__eq__("x") is False
    assert token.__eq__(None) is False
    assert token.__eq__(object()) is False
    assert token != "x"
    assert not (token == "x")
