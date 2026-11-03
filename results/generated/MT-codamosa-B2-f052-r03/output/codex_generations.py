

# Generated at 2026-11-02 20:13:01.189935
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3, 4], 5) == True
    # Element equal to threshold should fail
    assert module_0.below_threshold([1, 2, 5, 4], 5) == False
    # Element above threshold should fail
    assert module_0.below_threshold([1, 2, 6], 5) == False
    # Empty list vacuously true
    assert module_0.below_threshold([], 5) == True
    # Single element below threshold
    assert module_0.below_threshold([0], 1) == True
    # Single element equal to threshold
    assert module_0.below_threshold([1], 1) == False
    # Negative numbers
    assert module_0.below_threshold([-10, -5, -1], 0) == True
    assert module_0.below_threshold([-10, 0, -1], 0) == False
    # Threshold below all elements
    assert module_0.below_threshold([10, 20], 5) == False

# Generated at 2026-11-02 20:14:57.040784
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 4) == True
    assert module_0.below_threshold([1, 2, 4], 5) == True

    # Element equal to threshold should return False
    assert module_0.below_threshold([1, 2, 4], 4) == False

    # Element above threshold should return False
    assert module_0.below_threshold([1, 5, 3], 4) == False
    assert module_0.below_threshold([5], 4) == False

    # Empty list should return True (vacuously true)
    assert module_0.below_threshold([], 10) == True
    assert module_0.below_threshold([], 0) == True

    # Negative numbers
    assert module_0.below_threshold([-5, -3, -1], 0) == True
    assert module_0.below_threshold([-5, -3, 0], -1) == False
    assert module_0.below_threshold([-10, -20], -5) == True

    # Single element cases
    assert module_0.below_threshold([1], 2) == True
    assert module_0.below_threshold([2], 2) == False
    assert module_0.below_threshold([3], 2) == False

    # First element fails immediately
    assert module_0.below_threshold([10, 1, 2], 5) == False

    # Last element fails
    assert module_0.below_threshold([1, 2, 10], 5) == False

    # Zero threshold
    assert module_0.below_threshold([-1, -2], 0) == True
    assert module_0.below_threshold([0], 0) == False

    # Duplicates all below
    assert module_0.below_threshold([2, 2, 2], 3) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_below_threshold()

# Generated at 2026-11-02 20:16:36.154104
# Unit test for function below_threshold
def test_below_threshold():
    # All elements strictly below threshold
    assert module_0.below_threshold([1, 2, 3], 4) == True
    assert module_0.below_threshold([1, 2, 3], 10) == True

    # Element equal to threshold -> False (>= comparison)
    assert module_0.below_threshold([1, 2, 3], 3) == False
    assert module_0.below_threshold([4, 1, 2], 4) == False

    # Element above threshold -> False
    assert module_0.below_threshold([1, 5, 3], 4) == False
    assert module_0.below_threshold([4, 1, 2], 3) == False

    # Empty list -> True (no violations)
    assert module_0.below_threshold([], 0) == True

    # Single element cases
    assert module_0.below_threshold([0], 1) == True
    assert module_0.below_threshold([1], 1) == False
    assert module_0.below_threshold([5], 0) == False

    # Negative numbers
    assert module_0.below_threshold([-1, -2, -3], 0) == True
    assert module_0.below_threshold([-1, -2, -3], -2) == False
    assert module_0.below_threshold([-1, -2, -3], -3) == False

    # Duplicates at / below threshold
    assert module_0.below_threshold([2, 2, 2], 3) == True
    assert module_0.below_threshold([2, 2, 2], 2) == False

    # Zero threshold with positive list
    assert module_0.below_threshold([0, 0, 0], 1) == True
    assert module_0.below_threshold([0, 0, 1], 1) == False

# Generated at 2026-11-02 20:18:43.177840
# Unit test for function below_threshold
def test_below_threshold():
    # All elements below threshold
    assert module_0.below_threshold([1, 2, 3], 10) == True
    assert module_0.below_threshold([1, 2, 9], 10) == True

    # Element equal to threshold should return False
    assert module_0.below_threshold([1, 2, 3], 3) == False

    # Element above threshold should return False
    assert module_0.below_threshold([1, 2, 5], 4) == False

    # Empty list should return True (vacuously true)
    assert module_0.below_threshold([], 5) == True

    # Single element list
    assert module_0.below_threshold([4], 5) == True
    assert module_0.below_threshold([5], 5) == False
    assert module_0.below_threshold([6], 5) == False

    # Negative numbers
    assert module_0.below_threshold([-1, -2, -3], 0) == True
    assert module_0.below_threshold([-1, 0, -3], 0) == False

    # All elements equal to threshold
    assert module_0.below_threshold([3, 3, 3], 3) == False

# Generated at 2026-11-02 20:21:05.056614
# Unit test for function below_threshold
def test_below_threshold():
    # All elements strictly below threshold
    assert module_0.below_threshold([1, 2, 4, 10], 100) == True
    assert module_0.below_threshold([0, -1, -50], 0) == True

    # Element equal to threshold -> False
    assert module_0.below_threshold([1, 20, 4, 10], 20) == False
    assert module_0.below_threshold([5], 5) == False

    # Element above threshold -> False
    assert module_0.below_threshold([1, 2, 3], 2) == False
    assert module_0.below_threshold([100], 50) == False

    # Empty list -> True (vacuously true)
    assert module_0.below_threshold([], 10) == True

    # Single element below threshold
    assert module_0.below_threshold([3], 4) == True

    # Negative threshold values
    assert module_0.below_threshold([-10, -5, -3], -1) == True
    assert module_0.below_threshold([-10, 0, -3], -1) == False

    # First element fails
    assert module_0.below_threshold([10, 1, 2], 5) == False

    # Last element fails
    assert module_0.below_threshold([1, 2, 10], 5) == False

    # All elements equal to threshold
    assert module_0.below_threshold([3, 3, 3], 3) == False

    # Elements just below threshold
    assert module_0.below_threshold([2, 1, 0], 3) == True

    # Large threshold
    assert module_0.below_threshold([1, 2, 3, 4, 5], 1000000) == True

    print("All tests passed!")


class TestBelowThreshold(unittest.TestCase):
    def test_all_below(self):
        self.assertTrue(module_0.below_threshold([1, 2, 4, 10], 100))

    def test_equal_to_threshold(self):
        self.assertFalse(module_0.below_threshold([1, 20, 4, 10], 20))

    def test_above_threshold(self):
        self.assertFalse(module_0.below_threshold([1, 2, 3], 2))

    def test_empty_list(self):
        self.assertTrue(module_0.below_threshold([], 10))

    def test_single_element(self):
        self.assertTrue(module_0.below_threshold([3], 4))
        self.assertFalse(module_0.below_threshold([5], 5))

    def test_negative_numbers(self):
        self.assertTrue(module_0.below_threshold([-10, -5, -3], -1))
        self.assertFalse(module_0.below_threshold([-10, 0, -3], -1))

    def test_first_element_fails(self):
        self.assertFalse(module_0.below_threshold([10, 1, 2], 5))

    def test_last_element_fails(self):
        self.assertFalse(module_0.below_threshold([1, 2, 10], 5))

    def test_all_equal(self):
        self.assertFalse(module_0.below_threshold([3, 3, 3], 3))


if __name__ == "__main__":
    test_below_threshold()
    unittest.main()