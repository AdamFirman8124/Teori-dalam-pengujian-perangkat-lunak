

# Generated at 2026-11-02 11:14:30.708775
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element cases
    assert module_0.search([1]) == 1
    assert module_0.search([4]) == -1

    # All elements qualify, greatest returned
    assert module_0.search([5, 5, 5, 5, 5]) == 5
    assert module_0.search([3, 3, 3]) == 3

    # No element qualifies
    assert module_0.search([3, 3]) == -1
    assert module_0.search([2, 1, 1]) == 1

    # Mixed frequencies, greatest qualifying value returned
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([1, 1, 1, 2, 2, 2]) == 2
    assert module_0.search([2, 2, 2, 3, 3, 3, 3]) == 3

    # Frequency exactly equals the value
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Value with high frequency but larger value does not qualify
    assert module_0.search([2, 2, 2, 2, 10, 10]) == 2
    assert module_0.search([7, 7, 7, 7, 7, 7, 7]) == 7

    # Duplicates of qualifying number with others in between
    assert module_0.search([1, 5, 1, 5, 1, 5, 1]) == 1
    assert module_0.search([6, 6, 6, 6, 6, 6, 1, 1, 1, 1]) == 6

    print("All tests passed!")


if __name__ == "__main__":
    test_search()

# Generated at 2026-11-02 11:17:01.539679
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element lists
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # All same elements
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([3, 3]) == -1

    # Value 1 always qualifies if present (freq >= 1)
    assert module_0.search([1, 5, 5]) == 1

    # Ties resolved by greatest qualifying value
    assert module_0.search([2, 2, 1, 1, 1]) == 2
    assert module_0.search([1, 1, 1, 2, 2, 2]) == 2

    # Frequency exactly equal to value qualifies
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([4, 4, 4, 4, 4]) == 4

    # Larger qualifying value later in list wins
    assert module_0.search([2, 2, 3, 3, 3]) == 3

    # No qualifying value
    assert module_0.search([2, 2, 2, 3, 3]) == 2
    assert module_0.search([5, 6, 7]) == -1
    assert module_0.search([10, 10, 10]) == -1

    # Larger list
    assert module_0.search([1, 2, 3, 4, 5, 5, 5, 5, 5]) == 5

    print("All tests passed!")


test_search()

# Generated at 2026-11-02 11:18:44.915485
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([10]) == -1

    # All identical elements
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # No qualifying value
    assert module_0.search([2, 1]) == 1
    assert module_0.search([7, 7, 7]) == -1

    # Greatest qualifying value should be returned
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([1, 1, 2, 2, 3, 3, 3]) == 3

    # Value qualifies only at boundary frequency == value
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([4, 4, 4]) == -1

    # Larger list with mixed frequencies
    assert module_0.search([1, 2, 3, 4, 5, 6, 7] * 7) == 7
    assert module_0.search([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == 6

    # Frequency of 1 counts only if value is 1
    assert module_0.search([1, 5, 5]) == 1

# Generated at 2026-11-02 11:20:22.144417
# Unit test for function search
def test_search():import unittest


class TestSearch(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(module_0.search([4, 1, 2, 2, 3, 1]), 2)

    def test_example_2(self):
        self.assertEqual(module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_example_3(self):
        self.assertEqual(module_0.search([5, 5, 4, 4, 4]), -1)

    def test_single_element(self):
        self.assertEqual(module_0.search([1]), 1)

    def test_single_element_no_match(self):
        self.assertEqual(module_0.search([2]), -1)

    def test_all_same_value(self):
        self.assertEqual(module_0.search([3, 3, 3]), 3)

    def test_all_same_value_insufficient(self):
        self.assertEqual(module_0.search([5, 5]), -1)

    def test_greatest_valid_returned(self):
        # 2 appears twice, 1 appears twice; both qualify, greatest is 2
        self.assertEqual(module_0.search([1, 1, 2, 2]), 2)

    def test_larger_frequency_beats_value(self):
        # 4 appears 5 times, 3 appears 3 times; greatest qualifying is 4
        self.assertEqual(module_0.search([4, 4, 4, 4, 4, 3, 3, 3]), 4)

    def test_higher_value_lower_frequency(self):
        # 10 appears once, 2 appears twice; answer is 2
        self.assertEqual(module_0.search([10, 2, 2]), 2)

    def test_all_ones(self):
        self.assertEqual(module_0.search([1, 1, 1, 1]), 1)

    def test_no_valid_value(self):
        self.assertEqual(module_0.search([7, 3, 5]), -1)

    def test_frequency_exactly_equal(self):
        self.assertEqual(module_0.search([6, 6, 6, 6, 6, 6]), 6)

    def test_mixed_with_unqualified_high_values(self):
        # 1 appears 3 times, 5 appears 2 times, 9 appears once
        self.assertEqual(module_0.search([1, 1, 1, 5, 5, 9]), 1)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 11:21:52.764324
# Unit test for function search
def test_search():
    # Examples from the docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element lists
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # All same values
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([2, 2, 2, 2]) == 2
    assert module_0.search([5, 5, 5]) == -1

    # Frequency exactly equals value
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1, 2, 2, 3, 3, 3]) == 3

    # Multiple candidates, should return greatest
    assert module_0.search([1, 1, 2, 2, 2, 3, 3, 3, 3]) == 3

    # No valid value exists
    assert module_0.search([10, 10]) == -1
    assert module_0.search([100]) == -1

    # Value with frequency greater than value
    assert module_0.search([1, 1, 1, 1, 2, 2, 2]) == 2

    # Large frequency for small value only
    assert module_0.search([1, 1, 1, 5]) == 1

    # Mixed with larger values having insufficient frequency
    assert module_0.search([2, 2, 2, 7, 7]) == 2

    # Values appearing once
    assert module_0.search([1, 6, 7, 8]) == 1

    # Descending order list
    assert module_0.search([9, 9, 9, 9, 9, 4, 4, 4, 4]) == 4

    # Boundary: frequency just below value
    assert module_0.search([3, 3]) == -1

    # Boundary: frequency just at value
    assert module_0.search([3, 3, 3, 1, 1]) == 3

    print("All test_search tests passed!")


if __name__ == "__main__":
    test_search()