

# Generated at 2026-11-03 06:19:00.635510
# Unit test for function below_threshold
def test_below_threshold():
# nonce:6ff6a963
    # All elements strictly below threshold
    assert module_0.below_threshold([1, 2, 4, 10], 100) == True
    # One element equal to threshold -> False
    assert module_0.below_threshold([1, 20, 4, 10], 20) == False
    # One element above threshold -> False
    assert module_0.below_threshold([1, 21, 4, 10], 20) == False
    # Empty list is vacuously below threshold
    assert module_0.below_threshold([], 5) == True
    # Single element cases
    assert module_0.below_threshold([4], 5) == True
    assert module_0.below_threshold([5], 5) == False
    assert module_0.below_threshold([6], 5) == False
    # Negative numbers
    assert module_0.below_threshold([-10, -5, -1], 0) == True
    assert module_0.below_threshold([-10, 0, -1], 0) == False
    # Threshold below all elements
    assert module_0.below_threshold([1, 2, 3], 0) == False
    # Violation at the first element
    assert module_0.below_threshold([100, 1, 2], 50) == False

# Generated at 2026-11-03 06:20:13.132172
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 4) == True
    # Element equal to threshold returns False
    assert module_0.below_threshold([1, 2, 4], 4) == False
    # Element above threshold returns False
    assert module_0.below_threshold([1, 5, 3], 4) == False
    # Empty list returns True
    assert module_0.below_threshold([], 10) == True
    # Single element below threshold
    assert module_0.below_threshold([0], 1) == True
    # Single element equal to threshold
    assert module_0.below_threshold([1], 1) == False
    # Negative numbers below threshold
    assert module_0.below_threshold([-5, -3, -1], 0) == True
    # Negative threshold with negative elements
    assert module_0.below_threshold([-5, -3], -4) == False
    # All elements well below threshold
    assert module_0.below_threshold([1, 2, 3], 100) == True
    # First element violates threshold
    assert module_0.below_threshold([10, 1, 2], 5) == False
    # Last element violates threshold
    assert module_0.below_threshold([1, 2, 10], 5) == False
    print("All tests passed!")


if __name__ == "__main__":
    test_below_threshold()

# Generated at 2026-11-03 06:20:51.318824
# Unit test for function below_threshold
def test_below_threshold():import unittest


class TestBelowThreshold(unittest.TestCase):
    def test_all_below(self):
        self.assertTrue(module_0.below_threshold([1, 2, 4, 10], 100))

    def test_one_equal(self):
        self.assertFalse(module_0.below_threshold([1, 20, 4, 10], 10))

    def test_one_above(self):
        self.assertFalse(module_0.below_threshold([1, 2, 15, 10], 10))

    def test_empty_list(self):
        self.assertTrue(module_0.below_threshold([], 5))

    def test_negative_threshold(self):
        self.assertTrue(module_0.below_threshold([-10, -5, -1], 0))

    def test_negative_elements_above(self):
        self.assertFalse(module_0.below_threshold([-10, -5, 1], 0))

    def test_all_equal(self):
        self.assertFalse(module_0.below_threshold([5, 5, 5], 5))

    def test_all_strictly_below(self):
        self.assertTrue(module_0.below_threshold([4, 4, 4], 5))

    def test_single_element_below(self):
        self.assertTrue(module_0.below_threshold([3], 4))

    def test_single_element_equal(self):
        self.assertFalse(module_0.below_threshold([4], 4))

    def test_single_element_above(self):
        self.assertFalse(module_0.below_threshold([5], 4))

    def test_negative_threshold_all_below(self):
        self.assertTrue(module_0.below_threshold([-3, -4], -2))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 06:21:59.394512
# Unit test for function below_threshold
def test_below_threshold():
# nonce:dec5a37c
    # Empty list - vacuously true
    assert module_0.below_threshold([], 5) == True
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3, 4], 5) == True
    # Element equal to threshold - should be False
    assert module_0.below_threshold([1, 5, 3], 5) == False
    # Element above threshold
    assert module_0.below_threshold([1, 2, 10], 5) == False
    # Single element below threshold
    assert module_0.below_threshold([4], 5) == True
    # Single element equal to threshold
    assert module_0.below_threshold([5], 5) == False
    # Single element above threshold
    assert module_0.below_threshold([6], 5) == False
    # Negative numbers all below threshold
    assert module_0.below_threshold([-10, -5, 0], 1) == True
    # Negative threshold exceeded by positive element
    assert module_0.below_threshold([-1, 0, 1], 0) == False
    # Negative threshold, all below
    assert module_0.below_threshold([-5, -3], 0) == True
    # Threshold of zero with negative elements
    assert module_0.below_threshold([-1, -2, -3], 0) == True
    # Large list all below threshold
    assert module_0.below_threshold(list(range(100)), 100) == True
    # Large list with one violator at the end
    assert module_0.below_threshold(list(range(99)) + [100], 100) == False
    # First element violates threshold
    assert module_0.below_threshold([10, 1, 2], 5) == False
    # Duplicate values below threshold
    assert module_0.below_threshold([2, 2, 2, 2], 3) == True
    # Duplicate values at threshold
    assert module_0.below_threshold([2, 2, 2, 2], 2) == False

# Generated at 2026-11-03 06:22:46.244641
# Unit test for function below_threshold
def test_below_threshold():import unittest


class TestBelowThreshold(unittest.TestCase):

    def test_all_below(self):
        self.assertTrue(module_0.below_threshold([1, 2, 3, 4], 5))

    def test_one_equal_to_threshold(self):
        self.assertFalse(module_0.below_threshold([1, 2, 4], 4))

    def test_one_above_threshold(self):
        self.assertFalse(module_0.below_threshold([1, 5, 3], 4))

    def test_empty_list(self):
        self.assertTrue(module_0.below_threshold([], 10))

    def test_single_element_below(self):
        self.assertTrue(module_0.below_threshold([9], 10))

    def test_single_element_equal(self):
        self.assertFalse(module_0.below_threshold([10], 10))

    def test_single_element_above(self):
        self.assertFalse(module_0.below_threshold([11], 10))

    def test_negative_numbers(self):
        self.assertTrue(module_0.below_threshold([-5, -1, -10], 0))

    def test_negative_threshold(self):
        self.assertFalse(module_0.below_threshold([1, 2], -1))

    def test_all_equal_threshold_large(self):
        self.assertFalse(module_0.below_threshold([4, 4, 4], 4))

    def test_first_element_fails(self):
        self.assertFalse(module_0.below_threshold([100, 1, 2, 3], 10))

    def test_last_element_fails(self):
        self.assertFalse(module_0.below_threshold([1, 2, 3, 100], 10))


if __name__ == "__main__":
    unittest.main()