

# Generated at 2026-10-24 12:56:01.620339
# Unit test for function below_zero
def test_below_zero():
    # never drops below zero -> False
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([5, -5]) == False  # hits exactly zero, not below
    assert module_0.below_zero([10, -5, -5]) == False

    # drops below zero at some point -> True
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([1, -2]) == True
    assert module_0.below_zero([10, -5, -6]) == True
    assert module_0.below_zero([1, 2, -4, 5]) == True  # dips below then recovers

# Generated at 2026-10-24 12:56:03.334037
# Unit test for function below_zero
def test_below_zero():
    # never drops below zero -> False
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([5, -5]) == False  # hits exactly zero, not below
    assert module_0.below_zero([10, -5, -5]) == False

    # drops below zero at some point -> True
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([1, -2]) == True
    assert module_0.below_zero([10, -5, -6]) == True
    assert module_0.below_zero([1, 2, -4, 5]) == True  # dips below then recovers

# Generated at 2026-10-24 12:56:04.762660
# Unit test for function below_zero
def test_below_zero():
    # never drops below zero -> False
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([5, -5]) == False  # hits exactly zero, not below
    assert module_0.below_zero([10, -5, -5]) == False

    # drops below zero at some point -> True
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([1, -2]) == True
    assert module_0.below_zero([10, -5, -6]) == True
    assert module_0.below_zero([1, 2, -4, 5]) == True  # dips below then recovers

# Generated at 2026-10-24 12:56:32.356442
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([]) is False
    assert module_0.below_zero([1, 2, 3]) is False
    assert module_0.below_zero([-1]) is True
    assert module_0.below_zero([5, -3, -3]) is True
    assert module_0.below_zero([5, -5]) is False
    assert module_0.below_zero([2, -1, -1, 3]) is False

# Generated at 2026-10-24 12:56:50.263973
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, -4]) is True
    assert module_0.below_zero([1, 2, -3]) is False
    assert module_0.below_zero([-1]) is True
    assert module_0.below_zero([5, -2]) is False
    assert module_0.below_zero([]) is False