

# Generated at 2026-11-02 09:20:49.377060
# Unit test for function search
def test_search():
    # Docstring example cases
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element lists
    assert module_0.search([1]) == 1          # freq(1)=1 >= 1
    assert module_0.search([2]) == -1         # freq(2)=1 < 2

    # All identical values
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([2, 2]) == 2
    assert module_0.search([6, 6, 6, 6, 6, 6]) == 6

    # Frequency exactly equal to value
    assert module_0.search([4, 4, 4, 4]) == 4

    # Multiple qualifying values -> return the greatest
    assert module_0.search([1, 1, 2, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Higher value appears, but with insufficient frequency
    assert module_0.search([1, 1, 1, 5, 5]) == 1
    assert module_0.search([2, 3, 3, 3, 3]) == 3

    # No qualifying value at all
    assert module_0.search([10, 10]) == -1
    assert module_0.search([7, 8, 9]) == -1

# Generated at 2026-11-02 09:22:42.262686
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

    def test_single_element_insufficient_freq(self):
        self.assertEqual(module_0.search([2]), -1)

    def test_all_ones(self):
        self.assertEqual(module_0.search([1, 1, 1, 1]), 1)

    def test_exact_frequency(self):
        self.assertEqual(module_0.search([3, 3, 3]), 3)

    def test_greatest_wins(self):
        # both 2 (freq 4) and 3 (freq 3) qualify; return the greatest
        self.assertEqual(module_0.search([2, 2, 2, 2, 3, 3, 3]), 3)

    def test_higher_value_lower_freq(self):
        self.assertEqual(module_0.search([1, 2, 3]), 1)

    def test_large_value_insufficient_freq(self):
        self.assertEqual(module_0.search([10, 10, 10]), -1)

    def test_five_repeated_five_times(self):
        self.assertEqual(module_0.search([5, 5, 5, 5, 5]), 5)

    def test_mixed_qualifying(self):
        self.assertEqual(module_0.search([2, 2, 1, 3, 3, 3, 3]), 3)

    def test_two_repeated_twice(self):
        self.assertEqual(module_0.search([2, 2]), 2)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 09:25:04.344751
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1  # frequency 1 < value 2
    assert module_0.search([5]) == -1

    # All elements the same and qualifying
    assert module_0.search([2, 2, 2]) == 2
    assert module_0.search([3, 3, 3, 3]) == 3
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # All elements the same but not qualifying
    assert module_0.search([1, 1, 1, 1, 1]) == 1  # 1 qualifies (freq 5 >= 1)
    assert module_0.search([4, 4, 4]) == -1       # freq 3 < 4

    # Greatest qualifying value should be returned
    assert module_0.search([1, 1, 2, 2, 3, 3, 3]) == 3
    assert module_0.search([1, 1, 1, 2, 2, 2, 2]) == 2
    assert module_0.search([2, 2, 3, 3, 3]) == 3

    # Only small values qualify
    assert module_0.search([1, 3, 4, 5]) == 1

    # Larger list mixing qualifying and non-qualifying values
    assert module_0.search([6, 6, 6, 6, 6, 6, 1, 2, 2]) == 6
    assert module_0.search([7, 7, 7, 1, 1]) == 1

    # Value appears exactly as many times as itself
    assert module_0.search([3, 1, 2, 3]) == 3

    print("All tests passed!")


test_search()

# Generated at 2026-11-02 09:27:38.458317
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

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3

    # Frequency greater than value
    assert module_0.search([1, 1, 1, 1]) == 1
    assert module_0.search([2, 2, 2, 2, 2]) == 2

    # Greatest qualifying value wins
    assert module_0.search([2, 3, 3, 5, 5, 5, 5, 5]) == 5
    assert module_0.search([1, 1, 2, 2, 2, 3, 3, 3, 3]) == 3

    # No qualifying value
    assert module_0.search([7, 7, 7]) == -1
    assert module_0.search([4, 4, 4, 1]) == 1

    # Duplicates with larger non-qualifying values
    assert module_0.search([3, 3, 9, 9, 9]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test_search()

# Generated at 2026-11-02 09:29:26.600447
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element list - frequency 1 >= value 1
    assert module_0.search([1]) == 1

    # Single element list - frequency 1 < value 2
    assert module_0.search([2]) == -1

    # All same values, frequency equals value
    assert module_0.search([3, 3, 3]) == 3

    # All same values, frequency less than value
    assert module_0.search([5, 5, 5, 5]) == -1

    # Frequency greater than value
    assert module_0.search([2, 2, 2, 2, 2]) == 2

    # Multiple candidates, should return greatest
    assert module_0.search([1, 1, 2, 2, 2, 3, 3, 3, 3]) == 3

    # No valid value exists
    assert module_0.search([10, 20, 30]) == -1

    # Large values with sufficient frequency
    assert module_0.search([100] * 100) == 100

    # Mixed list where only 1 qualifies
    assert module_0.search([1, 7, 8, 9]) == 1

    print("All test cases passed!")


if __name__ == "__main__":
    test_search()