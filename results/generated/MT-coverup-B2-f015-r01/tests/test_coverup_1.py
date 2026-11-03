# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f015


def test_string_sequence_zero():
    """n = 0 should produce a single element '0' (executes line 3, loop runs once)."""
    result = f015.string_sequence(0)
    assert result == '0'


def test_string_sequence_positive():
    """n = 5 should produce numbers 0 through 5, space-separated."""
    result = f015.string_sequence(5)
    assert result == '0 1 2 3 4 5'
    # Postcondition: number of tokens equals n + 1
    assert len(result.split(' ')) == 6
    # Postcondition: first element is 0, last element is n
    tokens = result.split(' ')
    assert tokens[0] == '0'
    assert tokens[-1] == '5'
    # Postcondition: tokens are consecutive integers
    assert [int(t) for t in tokens] == list(range(6))


def test_string_sequence_negative():
    """n < 0 yields an empty range, so the result is an empty string (line 3 still executes)."""
    result = f015.string_sequence(-1)
    assert result == ''
