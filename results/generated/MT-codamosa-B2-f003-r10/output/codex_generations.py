

# Generated at 2026-10-25 06:16:37.375549
# Unit test for function below_zero

# Generated at 2026-10-25 06:16:39.792093
# Unit test for function below_zero

# Generated at 2026-10-25 06:16:42.208123
# Unit test for function below_zero

# Generated at 2026-10-25 06:16:44.623734
# Unit test for function below_zero

# Generated at 2026-10-25 06:16:47.037543
# Unit test for function below_zero

# Generated at 2026-10-25 06:16:52.399997
# Unit test for function below_zero
def test_below_zero():assert module_0.below_zero([1, 2, -4, 5]) is True

# Generated at 2026-10-25 06:16:53.804389
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 06:16:55.578033
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 06:16:56.990259
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op