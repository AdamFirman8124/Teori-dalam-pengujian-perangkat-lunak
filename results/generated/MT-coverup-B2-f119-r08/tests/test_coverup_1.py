# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import pytest

from f119 import match_parens


def _is_good(s):
    val = 0
    for ch in s:
        val += 1 if ch == '(' else -1
        if val < 0:
            return False
    return val == 0


def test_match_parens_first_order_good():
    # S1 = '()()' is good -> check(S1) True, short-circuits before check(S2)
    lst = ['()(', ')']
    result = match_parens(lst)
    assert result == 'Yes'
    assert _is_good(lst[0] + lst[1])


def test_match_parens_second_order_good():
    # S1 = ')(' fails early (val < 0), S2 = '()' is good
    lst = [')', '(']
    result = match_parens(lst)
    assert result == 'Yes'
    assert not _is_good(lst[0] + lst[1])
    assert _is_good(lst[1] + lst[0])


def test_match_parens_unbalanced_positive():
    # S1 = '((' never goes negative but ends with val != 0 -> False branch
    lst = ['(', '(']
    result = match_parens(lst)
    assert result == 'No'
    assert not _is_good(lst[0] + lst[1])
    assert not _is_good(lst[1] + lst[0])


def test_match_parens_both_closing():
    lst = [')', ')']
    result = match_parens(lst)
    assert result == 'No'
    assert not _is_good(lst[0] + lst[1])
    assert not _is_good(lst[1] + lst[0])


def test_match_parens_both_good():
    lst = ['()', '()']
    result = match_parens(lst)
    assert result == 'Yes'
    assert _is_good(lst[0] + lst[1])
    assert _is_good(lst[1] + lst[0])


@pytest.mark.parametrize(
    'lst, expected',
    [
        (['()(', ')'], 'Yes'),
        ([')', ')'], 'No'),
        (['(', ')'], 'Yes'),
        ([')', '('], 'Yes'),
        (['((', '))'], 'Yes'),
        ([')(', ')('], 'No'),
        (['()', '()'], 'Yes'),
        (['(', '('], 'No'),
    ],
)
def test_match_parens_returns_valid_answer(lst, expected):
    result = match_parens(lst)
    assert result in ('Yes', 'No')
    assert result == expected
    # Postcondition: 'Yes' iff at least one concatenation order is good
    assert (result == 'Yes') == (
        _is_good(lst[0] + lst[1]) or _is_good(lst[1] + lst[0])
    )
