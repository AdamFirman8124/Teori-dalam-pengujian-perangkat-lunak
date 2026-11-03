

# Generated at 2026-11-03 01:45:13.574908
# Unit test for function compare
def test_compare():
    # Test with identical lists - all differences should be 0
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test with completely different values
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test with mixed differences
    assert module_0.compare([1, 5, 3], [4, 2, 3]) == [3, 3, 0]

    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]

    # Test with empty lists
    assert module_0.compare([], []) == []

    # Test with floats
    assert module_0.compare([1.5, 2.5], [2.5, 1.5]) == [1.0, 1.0]

    # Test with single element lists
    assert module_0.compare([10], [3]) == [7]

    # Test absolute value behavior (order shouldn't matter)
    assert module_0.compare([5, 1, 8], [2, 4, 3]) == module_0.compare([2, 4, 3], [5, 1, 8])

    print("All test cases passed!")


if __name__ == "__main__":
    test_compare()

# Generated at 2026-11-03 01:46:22.771156
# Unit test for function compare
def test_compare():import unittest


def module_0.compare(game, guess):
    return [abs(x - y) for x, y in zip(game, guess)]


class TestCompare(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(module_0.compare([1, 2, 3, 4, 5, 1], [1, 1, 1, 1, 1, 1]),
                         [0, 1, 2, 3, 4, 0])

    def test_all_correct_guesses(self):
        self.assertEqual(module_0.compare([3, 5, 7], [3, 5, 7]), [0, 0, 0])

    def test_guess_lower_than_game(self):
        self.assertEqual(module_0.compare([10, 20, 30], [1, 2, 3]), [9, 18, 27])

    def test_guess_higher_than_game(self):
        self.assertEqual(module_0.compare([1, 2, 3], [10, 20, 30]), [9, 18, 27])

    def test_mixed_differences(self):
        self.assertEqual(module_0.compare([2, 8, 4], [5, 3, 9]), [3, 5, 5])

    def test_negative_numbers(self):
        self.assertEqual(module_0.compare([-1, -5, -10], [1, 5, 10]), [2, 10, 20])

    def test_single_element(self):
        self.assertEqual(module_0.compare([7], [3]), [4])

    def test_empty_lists(self):
        self.assertEqual(module_0.compare([], []), [])

    def test_result_is_non_negative(self):
        result = module_0.compare([1, 2, 3], [100, 0, -50])
        self.assertTrue(all(x >= 0 for x in result))

    def test_result_type_is_list(self):
        self.assertIsInstance(module_0.compare([1, 2], [3, 4]), list)

    def test_unequal_lengths_uses_shorter(self):
        self.assertEqual(module_0.compare([1, 2, 3, 4], [10, 20]), [9, 18])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 01:47:53.550668
# Unit test for function compare
def test_compare():
    # Test with exact matches (all differences should be 0)
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test with some differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test with mixed matches and differences
    assert module_0.compare([1, 2, 3, 4], [1, 4, 3, 2]) == [0, 2, 0, 2]

    # Test with single element lists
    assert module_0.compare([5], [5]) == [0]
    assert module_0.compare([5], [10]) == [5]

    # Test with empty lists
    assert module_0.compare([], []) == []

    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]
    assert module_0.compare([-5, -10], [-5, -3]) == [0, 7]

    # Test with zeros
    assert module_0.compare([0, 0], [0, 5]) == [0, 5]

    # Test with larger numbers
    assert module_0.compare([100, 200], [150, 100]) == [50, 100]

    # Test that result handles symmetric differences
    assert module_0.compare([3, 7], [10, 2]) == [7, 5]

    print("All test cases passed!")


if __name__ == "__main__":
    test_compare()

# Generated at 2026-11-03 01:49:30.067668
# Unit test for function compare
def test_compare():
    # Test with empty lists
    assert module_0.compare([], []) == []

    # Test with identical lists
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test with different lists
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test with mixed differences
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]

    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [-4, 5, -6]) == [3, 7, 3]

    # Test with single element lists
    assert module_0.compare([5], [10]) == [5]

    # Test result is absolute difference (order doesn't matter)
    assert module_0.compare([10, 20], [5, 25]) == [5, 5]
    assert module_0.compare([5, 25], [10, 20]) == [5, 5]

    # Test with floats
    assert module_0.compare([1.5, 2.5], [1.0, 3.0]) == [0.5, 0.5]

    # Test with zeros
    assert module_0.compare([0, 0], [0, 0]) == [0, 0]
    assert module_0.compare([0], [7]) == [7]

    # Test with large numbers
    assert module_0.compare([1000000], [999999]) == [1]

test_compare()
print("All tests passed!")

# Generated at 2026-11-03 01:50:25.340808
# Unit test for function compare
def test_compare():
    # Test case: some matches, some differences
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    
    # Test case: all guesses correct
    assert module_0.compare([0, 5, 0], [0, 5, 0]) == [0, 0, 0]
    
    # Test case: all guesses wrong
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    
    # Test case: single element
    assert module_0.compare([10], [3]) == [7]
    
    # Test case: negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]
    
    # Test case: empty lists
    assert module_0.compare([], []) == []
    
    # Test case: zero differences with mixed signs
    assert module_0.compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    
    print("All tests passed!")

test_compare()