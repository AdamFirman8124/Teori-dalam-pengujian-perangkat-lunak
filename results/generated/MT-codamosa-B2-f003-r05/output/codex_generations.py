

# Generated at 2026-10-24 12:59:40.965585
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, -2]) is True
    assert module_0.below_zero([1, -1]) is False
    assert module_0.below_zero([-1]) is True
    assert module_0.below_zero([]) is False
    assert module_0.below_zero([3, -1, -2]) is False

# Generated at 2026-10-24 12:59:42.351945
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

# Generated at 2026-10-24 12:59:43.828891
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

# Generated at 2026-10-24 12:59:45.277433
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

# Generated at 2026-10-24 12:59:46.634081
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