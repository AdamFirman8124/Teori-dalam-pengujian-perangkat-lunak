

# Generated at 2026-10-25 02:32:30.147518
# Unit test for function below_zero

# Generated at 2026-10-25 02:32:32.563126
# Unit test for function below_zero

# Generated at 2026-10-25 02:32:34.988829
# Unit test for function below_zero

# Generated at 2026-10-25 02:32:37.580231
# Unit test for function below_zero

# Generated at 2026-10-25 02:32:39.996148
# Unit test for function below_zero

# Generated at 2026-10-25 02:32:42.410438
# Unit test for function below_zero

# Generated at 2026-10-25 02:32:44.827123
# Unit test for function below_zero

# Generated at 2026-10-25 02:32:49.119273
# Unit test for function below_zero
def test_below_zero():assert module_0.below_zero([]) is False

# Generated at 2026-10-25 02:32:55.608728
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op

# Generated at 2026-10-25 02:32:57.029523
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -3]) is False          # hits exactly 0, never below
    assert module_0.below_zero([1, 2, -4]) is True           # goes to -1
    assert module_0.below_zero([-1, 2]) is True              # negative on first op
    assert module_0.below_zero([]) is False                  # empty input
    assert module_0.below_zero([10, -5, -4]) is False        # dips but stays >= 0... (5, 1)
    assert module_0.below_zero([10, -5, -6]) is True         # dips below on last op