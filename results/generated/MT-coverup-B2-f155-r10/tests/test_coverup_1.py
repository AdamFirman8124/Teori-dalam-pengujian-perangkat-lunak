# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

def test_even_odd_count_covers_even_odd_and_negative_digits():
    from f155 import even_odd_count

    assert even_odd_count(123456) == (3, 3)
    assert even_odd_count(-2047) == (3, 1)
    assert even_odd_count(0) == (1, 0)
