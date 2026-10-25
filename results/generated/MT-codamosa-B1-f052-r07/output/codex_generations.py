

# Generated at 2026-10-24 07:18:03.236146
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 5) == True
    # Single element, below
    assert module_0.below_threshold([4], 5) == True
    # Element equal to threshold -> False
    assert module_0.below_threshold([1, 5, 2], 5) == False
    # Element above threshold -> False
    assert module_0.below_threshold([1, 6, 2], 5) == False
    # Empty list -> True (vacuously true)
    assert module_0.below_threshold([], 5) == True
    # Negative numbers below threshold
    assert module_0.below_threshold([-10, -1, 0], 1) == True
    # Negative threshold, element above it
    assert module_0.below_threshold([1, 2], -1) == False
    # First element fails immediately
    assert module_0.below_threshold([10, 1, 2], 5) == False

# Generated at 2026-10-24 07:18:04.575385
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 5) == True
    # Single element, below
    assert module_0.below_threshold([4], 5) == True
    # Element equal to threshold -> False
    assert module_0.below_threshold([1, 5, 2], 5) == False
    # Element above threshold -> False
    assert module_0.below_threshold([1, 6, 2], 5) == False
    # Empty list -> True (vacuously true)
    assert module_0.below_threshold([], 5) == True
    # Negative numbers below threshold
    assert module_0.below_threshold([-10, -1, 0], 1) == True
    # Negative threshold, element above it
    assert module_0.below_threshold([1, 2], -1) == False
    # First element fails immediately
    assert module_0.below_threshold([10, 1, 2], 5) == False

# Generated at 2026-10-24 07:18:05.886657
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 5) == True
    # Single element, below
    assert module_0.below_threshold([4], 5) == True
    # Element equal to threshold -> False
    assert module_0.below_threshold([1, 5, 2], 5) == False
    # Element above threshold -> False
    assert module_0.below_threshold([1, 6, 2], 5) == False
    # Empty list -> True (vacuously true)
    assert module_0.below_threshold([], 5) == True
    # Negative numbers below threshold
    assert module_0.below_threshold([-10, -1, 0], 1) == True
    # Negative threshold, element above it
    assert module_0.below_threshold([1, 2], -1) == False
    # First element fails immediately
    assert module_0.below_threshold([10, 1, 2], 5) == False

# Generated at 2026-10-24 07:18:07.200410
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 5) == True
    # Single element, below
    assert module_0.below_threshold([4], 5) == True
    # Element equal to threshold -> False
    assert module_0.below_threshold([1, 5, 2], 5) == False
    # Element above threshold -> False
    assert module_0.below_threshold([1, 6, 2], 5) == False
    # Empty list -> True (vacuously true)
    assert module_0.below_threshold([], 5) == True
    # Negative numbers below threshold
    assert module_0.below_threshold([-10, -1, 0], 1) == True
    # Negative threshold, element above it
    assert module_0.below_threshold([1, 2], -1) == False
    # First element fails immediately
    assert module_0.below_threshold([10, 1, 2], 5) == False

# Generated at 2026-10-24 07:18:08.503628
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 5) == True
    # Single element, below
    assert module_0.below_threshold([4], 5) == True
    # Element equal to threshold -> False
    assert module_0.below_threshold([1, 5, 2], 5) == False
    # Element above threshold -> False
    assert module_0.below_threshold([1, 6, 2], 5) == False
    # Empty list -> True (vacuously true)
    assert module_0.below_threshold([], 5) == True
    # Negative numbers below threshold
    assert module_0.below_threshold([-10, -1, 0], 1) == True
    # Negative threshold, element above it
    assert module_0.below_threshold([1, 2], -1) == False
    # First element fails immediately
    assert module_0.below_threshold([10, 1, 2], 5) == False