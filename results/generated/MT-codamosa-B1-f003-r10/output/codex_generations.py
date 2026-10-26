

# Generated at 2026-10-25 07:24:51.635359
# Unit test for function below_zero

# Generated at 2026-10-25 07:24:54.049214
# Unit test for function below_zero

# Generated at 2026-10-25 07:24:56.462498
# Unit test for function below_zero

# Generated at 2026-10-25 07:24:58.876894
# Unit test for function below_zero

# Generated at 2026-10-25 07:25:01.637358
# Unit test for function below_zero
def test_below_zero():assert module_0.below_zero([1, 2, -4, 5]) is True

# Generated at 2026-10-25 07:25:03.097163
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 07:25:04.433381
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 07:25:05.793059
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op