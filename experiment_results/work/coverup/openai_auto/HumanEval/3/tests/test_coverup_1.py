# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

from script_3 import below_zero


def test_below_zero_returns_false_when_balance_never_negative():
    operations = [1, 2, 3]

    assert below_zero(operations) is False

    balance = 0
    for op in operations:
        balance += op
        assert balance >= 0


def test_below_zero_returns_true_when_balance_falls_below_zero():
    operations = [1, 2, -4, 5]

    assert below_zero(operations) is True

    balance = 0
    fell_below_zero = False
    for op in operations:
        balance += op
        if balance < 0:
            fell_below_zero = True
            break

    assert fell_below_zero is True


def test_below_zero_returns_false_for_empty_operations():
    assert below_zero([]) is False
