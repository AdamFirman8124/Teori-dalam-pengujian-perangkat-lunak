# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

def test_below_zero_no_withdrawals():
    from script_3 import below_zero
    assert below_zero([]) is False
    assert below_zero([1, 2, 3]) is False


def test_below_zero_positive_then_negative():
    from script_3 import below_zero
    assert below_zero([1, 2, -4, 5]) is True
    assert below_zero([-1]) is True


def test_below_zero_returns_early():
    from script_3 import below_zero
    # should stop at the first negative balance
    assert below_zero([1, -2, -3]) is True


def test_below_zero_exact_zero_is_ok(monkeypatch):
    from script_3 import below_zero
    assert below_zero([5, -5, 1]) is False
