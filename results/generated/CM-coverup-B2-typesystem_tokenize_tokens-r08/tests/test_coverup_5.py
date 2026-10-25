# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


class ValueToken(Token):
    def _get_value(self):
        return self._value


def test_token_equality_returns_false_for_non_token():
    token = Token("value", 1, 2)

    assert (token == object()) is False


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (ValueToken("value", 1, 2), ValueToken("different", 1, 2), False),
        (ValueToken("value", 1, 2), ValueToken("value", 0, 2), False),
        (ValueToken("value", 1, 2), ValueToken("value", 1, 3), False),
        (ValueToken("value", 1, 2), ValueToken("value", 1, 2), True),
    ],
)
def test_token_equality_compares_value_and_indexes(left, right, expected):
    assert (left == right) is expected
