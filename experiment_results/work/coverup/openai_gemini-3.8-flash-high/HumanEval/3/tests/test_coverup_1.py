# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

from script_3 import below_zero


def test_below_zero_never_negative():
    assert below_zero([1, 2, 3]) is False
    assert below_zero([]) is False
    assert below_zero([5, -5]) is False


def test_below_zero_goes_negative():
    assert below_zero([1, 2, -4, 5]) is True
    assert below_zero([-1]) is True
