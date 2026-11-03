

# Generated at 2026-11-02 15:33:47.870665
# Unit test for function monotonic
def test_monotonic():import unittest


class TestMonotonic(unittest.TestCase):

    def test_increasing(self):
        self.assertTrue(module_0.monotonic([1, 2, 4, 20]))

    def test_decreasing(self):
        self.assertTrue(module_0.monotonic([5, 4, 3, 2, 1]))

    def test_not_monotonic(self):
        self.assertFalse(module_0.monotonic([1, 20, 4, 10]))

    def test_increasing_with_duplicates(self):
        self.assertTrue(module_0.monotonic([1, 2, 2, 3]))

    def test_decreasing_with_duplicates(self):
        self.assertTrue(module_0.monotonic([5, 4, 4, 2]))

    def test_all_equal(self):
        self.assertTrue(module_0.monotonic([7, 7, 7, 7]))

    def test_empty_list(self):
        self.assertTrue(module_0.monotonic([]))

    def test_single_element(self):
        self.assertTrue(module_0.monotonic([42]))

    def test_two_elements(self):
        self.assertTrue(module_0.monotonic([1, 2]))
        self.assertTrue(module_0.monotonic([2, 1]))

    def test_negative_numbers(self):
        self.assertTrue(module_0.monotonic([-3, -2, -1]))
        self.assertTrue(module_0.monotonic([-1, -2, -3]))
        self.assertFalse(module_0.monotonic([-1, -3, -2]))

    def test_floats(self):
        self.assertTrue(module_0.monotonic([1.1, 2.2, 3.3]))
        self.assertFalse(module_0.monotonic([1.1, 3.3, 2.2]))

    def test_mixed_types(self):
        self.assertTrue(module_0.monotonic([1, 2.5, 3]))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 15:35:01.882588
# Unit test for function monotonic
def test_monotonic():
    # Monotonically increasing
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Monotonically decreasing
    assert module_0.monotonic([5, 4, 3, 1]) == True
    # Non-decreasing with duplicates
    assert module_0.monotonic([1, 2, 2, 3]) == True
    # Non-increasing with duplicates
    assert module_0.monotonic([3, 2, 2, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 3, 2]) == False
    assert module_0.monotonic([4, 1, 3]) == False
    # Empty list is trivially monotonic
    assert module_0.monotonic([]) == True
    # Single element
    assert module_0.monotonic([7]) == True
    # Two elements
    assert module_0.monotonic([1, 2]) == True
    assert module_0.monotonic([2, 1]) == True
    assert module_0.monotonic([1, 1]) == True
    # All duplicates
    assert module_0.monotonic([5, 5, 5]) == True
    # Floats
    assert module_0.monotonic([1.5, 2.5, 2.5, 3.0]) == True
    assert module_0.monotonic([3.0, 2.5, 1.5]) == True
    assert module_0.monotonic([1.5, 3.0, 2.5]) == False

# Generated at 2026-11-02 15:35:46.640774
# Unit test for function monotonic
def test_monotonic():
    # Increasing list
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing list
    assert module_0.monotonic([5, 4, 3, 1]) == True
    # Non-monotonic list
    assert module_0.monotonic([1, 20, 4, 10]) == False
    # Strictly increasing
    assert module_0.monotonic([1, 2, 3, 4, 5]) == True
    # Strictly decreasing
    assert module_0.monotonic([10, 8, 6, 4, 2]) == True
    # Non-strict (duplicates adjacent) increasing
    assert module_0.monotonic([1, 2, 2, 3]) == True
    # Non-strict (duplicates adjacent) decreasing
    assert module_0.monotonic([5, 5, 3, 1]) == True
    # Empty list
    assert module_0.monotonic([]) == True
    # Single element
    assert module_0.monotonic([42]) == True
    # Two equal elements
    assert module_0.monotonic([7, 7]) == True
    # Mixed with floats
    assert module_0.monotonic([1.5, 2.5, 3.5]) == True
    assert module_0.monotonic([3.5, 2.5, 4.0]) == False
    # Negative numbers
    assert module_0.monotonic([-3, -2, -1]) == True
    assert module_0.monotonic([-1, -3, -2]) == False

# Generated at 2026-11-02 15:36:24.858648
# Unit test for function monotonic
def test_monotonic():
    # Monotonically increasing
    assert module_0.monotonic([1, 2, 3, 4, 5]) == True
    # Monotonically decreasing
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 3, 2, 4, 5]) == False
    # Empty list is monotonic
    assert module_0.monotonic([]) == True
    # Single element is monotonic
    assert module_0.monotonic([1]) == True
    # Two elements increasing
    assert module_0.monotonic([1, 2]) == True
    # Two elements decreasing
    assert module_0.monotonic([2, 1]) == True
    # All equal elements are monotonic
    assert module_0.monotonic([5, 5, 5, 5]) == True
    # Non-strictly increasing (with duplicates)
    assert module_0.monotonic([1, 2, 2, 3]) == True
    # Non-strictly decreasing (with duplicates)
    assert module_0.monotonic([3, 2, 2, 1]) == True
    # Negative numbers increasing
    assert module_0.monotonic([-5, -3, 0, 2]) == True
    # Negative numbers decreasing
    assert module_0.monotonic([-2, -3, -5]) == True
    # Floats increasing
    assert module_0.monotonic([1.1, 2.2, 3.3]) == True
    # Floats decreasing
    assert module_0.monotonic([3.3, 2.2, 1.1]) == True
    # Mixed floats and ints not monotonic
    assert module_0.monotonic([1.1, 2, 1.5]) == False
    # Strings increasing
    assert module_0.monotonic(['a', 'b', 'c']) == True
    # Strings decreasing
    assert module_0.monotonic(['c', 'b', 'a']) == True
    # Strings not monotonic
    assert module_0.monotonic(['a', 'c', 'b']) == False
    # Pathological case: increase then decrease
    assert module_0.monotonic([1, 2, 3, 3, 2, 1]) == False
    # First element break
    assert module_0.monotonic([2, 1, 3]) == False
    # Last element break
    assert module_0.monotonic([1, 3, 2]) == False

    print("All test cases passed!")


if __name__ == "__main__":
    test_monotonic()

    class TestMonotonic(unittest.TestCase):
        def test_increasing(self):
            self.assertTrue(module_0.monotonic([1, 2, 3, 4, 5]))

        def test_decreasing(self):
            self.assertTrue(module_0.monotonic([5, 4, 3, 2, 1]))

        def test_not_monotonic(self):
            self.assertFalse(module_0.monotonic([1, 3, 2, 4, 5]))

        def test_empty(self):
            self.assertTrue(module_0.monotonic([]))

        def test_single_element(self):
            self.assertTrue(module_0.monotonic([7]))

        def test_all_equal(self):
            self.assertTrue(module_0.monotonic([4, 4, 4]))

        def test_duplicates_increasing(self):
            self.assertTrue(module_0.monotonic([1, 2, 2, 3]))

        def test_duplicates_decreasing(self):
            self.assertTrue(module_0.monotonic([3, 3, 2, 1]))

        def test_negative_numbers(self):
            self.assertTrue(module_0.monotonic([-5, -3, 0, 2]))
            self.assertTrue(module_0.monotonic([-2, -3, -5]))

        def test_strings(self):
            self.assertTrue(module_0.monotonic(['a', 'b', 'c']))
            self.assertFalse(module_0.monotonic(['a', 'c', 'b']))

        def test_peak_pattern(self):
            self.assertFalse(module_0.monotonic([1, 2, 3, 2, 1]))

    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)

# Generated at 2026-11-02 15:37:26.200188
# Unit test for function monotonic
def test_monotonic():
    # Increasing lists
    assert module_0.monotonic([1, 2, 4, 20]) == True
    assert module_0.monotonic([1, 20, 4, 10]) == False
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    assert module_0.monotonic([1, 1, 1, 1]) == True  # constant list is both increasing and decreasing

    # Decreasing lists
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    assert module_0.monotonic([5, 4, 3, 4, 1]) == False
    assert module_0.monotonic([-1, -2, -3, -4]) == True

    # Non-monotonic lists
    assert module_0.monotonic([1, 3, 2]) == False
    assert module_0.monotonic([2, 1, 3]) == False
    assert module_0.monotonic([10, 5, 20, 1]) == False

    # Edge cases
    assert module_0.monotonic([]) == True          # empty list
    assert module_0.monotonic([7]) == True         # single element
    assert module_0.monotonic([1, 2]) == True      # two increasing elements
    assert module_0.monotonic([2, 1]) == True      # two decreasing elements

    # Lists with duplicates
    assert module_0.monotonic([1, 2, 2, 3]) == True
    assert module_0.monotonic([3, 3, 2, 1]) == True
    assert module_0.monotonic([1, 2, 3, 2]) == False

    # Mixed types of numbers
    assert module_0.monotonic([1.5, 2.5, 3.5]) == True
    assert module_0.monotonic([-3, -2.5, 0, 4]) == True
    assert module_0.monotonic([0, -1, 1]) == False