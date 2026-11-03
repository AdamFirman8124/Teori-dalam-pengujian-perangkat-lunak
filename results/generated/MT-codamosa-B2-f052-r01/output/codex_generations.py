

# Generated at 2026-11-02 14:49:06.526659
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 5) == True
    # Element equal to threshold -> False
    assert module_0.below_threshold([1, 5, 3], 5) == False
    # Element above threshold -> False
    assert module_0.below_threshold([1, 6, 3], 5) == False
    # Empty list -> True (no violations)
    assert module_0.below_threshold([], 5) == True
    # Single element below
    assert module_0.below_threshold([4], 5) == True
    # Single element equal to threshold
    assert module_0.below_threshold([5], 5) == False
    # Single element above threshold
    assert module_0.below_threshold([7], 5) == False
    # Negative numbers below threshold
    assert module_0.below_threshold([-10, -5, -1], 0) == True
    # Negative threshold with elements above it
    assert module_0.below_threshold([-10, -5, 0], -1) == False
    # All elements just below threshold
    assert module_0.below_threshold([1, 2, 3, 4], 5) == True
    # First element violates threshold
    assert module_0.below_threshold([10, 1, 2], 5) == False
    # Last element violates threshold
    assert module_0.below_threshold([1, 2, 10], 5) == False
    # Zero threshold
    assert module_0.below_threshold([-3, -2, -1], 0) == True
    assert module_0.below_threshold([0], 0) == False
    # Large numbers
    assert module_0.below_threshold([999, 1000], 1001) == True
    assert module_0.below_threshold([999, 1001], 1000) == False

# Generated at 2026-11-02 14:51:01.362177
# Unit test for function below_threshold
def test_below_threshold():import unittest


class TestBelowThreshold(unittest.TestCase):
    def test_all_below(self):
        self.assertTrue(module_0.below_threshold([1, 2, 3], 5))

    def test_equal_to_threshold(self):
        self.assertFalse(module_0.below_threshold([1, 5, 3], 5))

    def test_above_threshold(self):
        self.assertFalse(module_0.below_threshold([1, 2, 10], 5))

    def test_empty_list(self):
        self.assertTrue(module_0.below_threshold([], 5))

    def test_single_element_below(self):
        self.assertTrue(module_0.below_threshold([4], 5))

    def test_single_element_above(self):
        self.assertFalse(module_0.below_threshold([6], 5))

    def test_negative_numbers_below(self):
        self.assertTrue(module_0.below_threshold([-10, -5, 0], 1))

    def test_negative_threshold(self):
        self.assertTrue(module_0.below_threshold([-10, -5], -1))
        self.assertFalse(module_0.below_threshold([-10, 0], -1))

    def test_zero_threshold(self):
        self.assertTrue(module_0.below_threshold([-1, -2], 0))
        self.assertFalse(module_0.below_threshold([0], 0))

    def test_large_list(self):
        self.assertTrue(module_0.below_threshold(list(range(100)), 100))
        self.assertFalse(module_0.below_threshold(list(range(101)), 100))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 14:52:18.660482
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3, 4], 5) == True
    # Element equal to threshold should fail
    assert module_0.below_threshold([1, 2, 5, 4], 5) == False
    # Element above threshold should fail
    assert module_0.below_threshold([1, 2, 10, 4], 5) == False
    # Empty list returns True
    assert module_0.below_threshold([], 5) == True
    # Single element below threshold
    assert module_0.below_threshold([3], 5) == True
    # Single element equal to threshold
    assert module_0.below_threshold([5], 5) == False
    # Single element above threshold
    assert module_0.below_threshold([7], 5) == False
    # Negative numbers below threshold
    assert module_0.below_threshold([-5, -2, -1], 0) == True
    # Negative threshold
    assert module_0.below_threshold([-5, -2], -1) == True
    # Negative element fails against negative threshold
    assert module_0.below_threshold([-5, 0], -1) == False
    # All elements far below threshold
    assert module_0.below_threshold([0, 0, 0], 1) == True
    # Large values
    assert module_0.below_threshold([100, 200], 1000) == True
    assert module_0.below_threshold([100, 2000], 1000) == False
    # Last element fails
    assert module_0.below_threshold([1, 2, 3], 3) == False
    # First element fails
    assert module_0.below_threshold([10, 2, 3], 5) == False
    # Non-integer threshold comparisons
    assert module_0.below_threshold([1.5, 2.5], 3) == True
    assert module_0.below_threshold([1.5, 3.5], 3) == False
    # Boolean-like values (0/1)
    assert module_0.below_threshold([0, 0, 1], 2) == True
    assert module_0.below_threshold([1, 1], 1) == False

# Generated at 2026-11-02 14:53:06.522604
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3, 4], 5) == True
    assert module_0.below_threshold([1, 2, 3], 4) == True

    # Element equal to threshold (should return False)
    assert module_0.below_threshold([1, 2, 3], 3) == False

    # Element above threshold (should return False)
    assert module_0.below_threshold([1, 2, 10], 5) == False
    assert module_0.below_threshold([5, 1, 2], 3) == False

    # Empty list (vacuously true)
    assert module_0.below_threshold([], 0) == True
    assert module_0.below_threshold([], 100) == True

    # Single element cases
    assert module_0.below_threshold([1], 2) == True
    assert module_0.below_threshold([2], 2) == False
    assert module_0.below_threshold([3], 2) == False

    # Negative numbers
    assert module_0.below_threshold([-5, -1, 0], 1) == True
    assert module_0.below_threshold([-5, 0, 1], 1) == False
    assert module_0.below_threshold([-1, -2, -3], -1) == False

    # Threshold is zero
    assert module_0.below_threshold([-3, -1], 0) == True
    assert module_0.below_threshold([0, -1], 0) == False

    # All elements equal and below
    assert module_0.below_threshold([2, 2, 2], 3) == True

    # Large numbers
    assert module_0.below_threshold([10**6], 10**6 + 1) == True
    assert module_0.below_threshold([10**6], 10**6) == False

    # First element fails immediately
    assert module_0.below_threshold([100, 1, 2], 50) == False

    # Last element fails
    assert module_0.below_threshold([1, 2, 100], 50) == False

    print("All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_below_threshold()

# Generated at 2026-11-02 14:54:06.167856
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3, 4], 10) is True
    # One element equal to threshold -> False
    assert module_0.below_threshold([1, 2, 10, 4], 10) is False
    # One element above threshold -> False
    assert module_0.below_threshold([1, 20, 3], 10) is False
    # Empty list -> True (vacuously true)
    assert module_0.below_threshold([], 5) is True
    # Negative numbers below threshold
    assert module_0.below_threshold([-5, -1, 0], 1) is True
    # Negative numbers not below negative threshold
    assert module_0.below_threshold([-5, -1], -1) is False
    # Single element below
    assert module_0.below_threshold([4], 5) is True
    # Single element equal to threshold
    assert module_0.below_threshold([5], 5) is False
    # All elements just below threshold
    assert module_0.below_threshold([9, 8, 7], 10) is True
    # Large numbers
    assert module_0.below_threshold([1000000], 1000001) is True