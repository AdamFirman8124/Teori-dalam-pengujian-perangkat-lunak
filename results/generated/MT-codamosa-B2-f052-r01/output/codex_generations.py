

# Generated at 2026-10-24 04:14:00.407609
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:02.821461
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:05.237036
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:07.652938
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:10.070019
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:12.488040
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:14.906586
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:17.324318
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:19.743028
# Unit test for function below_threshold

# Generated at 2026-10-24 04:14:34.740754
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

# Generated at 2026-10-24 04:14:36.054993
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