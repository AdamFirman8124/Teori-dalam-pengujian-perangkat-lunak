

# Generated at 2026-10-25 09:15:16.929989
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 09:15:18.479079
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 09:15:20.013369
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 09:15:21.565608
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 09:15:22.909030
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op