# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f067 import fruit_distribution


def test_fruit_distribution_mixed_digits_and_words():
    # "5 apples and 6 oranges" -> digit tokens 5 and 6 are summed;
    # mangoes = 19 - (5 + 6) = 8
    result = fruit_distribution("5 apples and 6 oranges", 19)
    assert result == 8


def test_fruit_distribution_no_digit_tokens():
    # No numeric tokens -> sum(lis) == 0, so all remaining fruits are mangoes
    result = fruit_distribution("apples oranges", 10)
    assert result == 10


def test_fruit_distribution_empty_string():
    # "".split(' ') yields [''], whose isdigit() is False -> sum is 0
    result = fruit_distribution("", 7)
    assert result == 7


def test_fruit_distribution_zero_token():
    # "0".isdigit() is True and int("0") == 0, exercising the append branch
    result = fruit_distribution("0 apples", 5)
    assert result == 5


def test_fruit_distribution_multiple_digit_tokens():
    # Several digit tokens are all appended and summed: 20 - (2 + 3 + 4) = 11
    result = fruit_distribution("2 3 4", 20)
    assert result == 11
