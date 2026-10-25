

# Generated at 2026-10-24 16:04:16.561282
# Unit test for function below_threshold
def test_below_threshold():
    assert module_0.below_threshold([1, 2, 4, 10], 100) == True
    assert module_0.below_threshold([1, 2, 4, 10], 5) == False
    assert module_0.below_threshold([1, 2, 4, 10], 10) == False  # equal is not below
    assert module_0.below_threshold([], 5) == True
    assert module_0.below_threshold([-5, -2, 0], 1) == True

# Generated at 2026-10-24 16:04:17.939735
# Unit test for function below_threshold
def test_below_threshold():
    # all elements strictly below threshold
    assert module_0.below_threshold([1, 2, 4, 10], 100) is True
    assert module_0.below_threshold([1, 2, 3], 4) is True

    # one element equal to threshold -> False
    assert module_0.below_threshold([1, 2, 3], 3) is False

    # one element above threshold -> False
    assert module_0.below_threshold([1, 20, 4, 10], 5) is False
    assert module_0.below_threshold([1, 2, 30, 4], 10) is False

    # empty list -> vacuously True
    assert module_0.below_threshold([], 5) is True

    # negative numbers and threshold
    assert module_0.below_threshold([-10, -5, 0], 1) is True
    assert module_0.below_threshold([-10, -5, 0], 0) is False

# Generated at 2026-10-24 16:04:19.263970
# Unit test for function below_threshold
def test_below_threshold():
    assert module_0.below_threshold([1, 2, 4, 10], 100) == True
    assert module_0.below_threshold([1, 2, 4, 10], 5) == False
    assert module_0.below_threshold([1, 2, 4, 10], 10) == False  # equal is not below
    assert module_0.below_threshold([], 5) == True
    assert module_0.below_threshold([-5, -2, 0], 1) == True

# Generated at 2026-10-24 16:04:20.655647
# Unit test for function below_threshold
def test_below_threshold():
    assert module_0.below_threshold([1, 2, 4, 10], 100) == True
    assert module_0.below_threshold([1, 2, 4, 10], 5) == False
    assert module_0.below_threshold([1, 2, 4, 10], 10) == False  # equal is not below
    assert module_0.below_threshold([], 5) == True
    assert module_0.below_threshold([-5, -2, 0], 1) == True

# Generated at 2026-10-24 16:04:22.058902
# Unit test for function below_threshold
def test_below_threshold():
    assert module_0.below_threshold([1, 2, 4, 10], 100) == True
    assert module_0.below_threshold([1, 2, 4, 10], 5) == False
    assert module_0.below_threshold([1, 2, 4, 10], 10) == False  # equal is not below
    assert module_0.below_threshold([], 5) == True
    assert module_0.below_threshold([-5, -2, 0], 1) == True