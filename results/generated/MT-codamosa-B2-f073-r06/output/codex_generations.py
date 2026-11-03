

# Generated at 2026-11-02 20:12:30.658903
# Unit test for function smallest_change
def test_smallest_change():import unittest


class TestSmallestChange(unittest.TestCase):

    def test_already_palindrome(self):
        self.assertEqual(module_0.smallest_change([1, 2, 3, 2, 1]), 0)

    def test_even_palindrome(self):
        self.assertEqual(module_0.smallest_change([1, 2, 2, 1]), 0)

    def test_single_element(self):
        self.assertEqual(module_0.smallest_change([5]), 0)

    def test_empty_array(self):
        self.assertEqual(module_0.smallest_change([]), 0)

    def test_one_change_needed(self):
        self.assertEqual(module_0.smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)

    def test_all_mismatch(self):
        self.assertEqual(module_0.smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_two_elements_match(self):
        self.assertEqual(module_0.smallest_change([7, 7]), 0)

    def test_two_elements_mismatch(self):
        self.assertEqual(module_0.smallest_change([7, 8]), 1)

    def test_mixed_palindrome(self):
        self.assertEqual(module_0.smallest_change([1, 2, 3, 4, 3, 2, 1]), 0)

    def test_example_from_problem(self):
        self.assertEqual(module_0.smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)

    def test_partial_palindrome(self):
        self.assertEqual(module_0.smallest_change([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_three_elements(self):
        self.assertEqual(module_0.smallest_change([1, 2, 1]), 0)
        self.assertEqual(module_0.smallest_change([1, 2, 3]), 1)

    def test_negative_numbers(self):
        self.assertEqual(module_0.smallest_change([-1, -2, -1]), 0)
        self.assertEqual(module_0.smallest_change([-1, -2, -3]), 1)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 20:14:16.271939
# Unit test for function smallest_change
def test_smallest_change():
    # Palindromic arrays need no changes
    assert module_0.smallest_change([1, 2, 3, 2, 1]) == 0
    assert module_0.smallest_change([5, 5, 5, 5]) == 0
    # Edge cases: empty and single-element arrays
    assert module_0.smallest_change([]) == 0
    assert module_0.smallest_change([7]) == 0
    # Two-element arrays
    assert module_0.smallest_change([5, 5]) == 0
    assert module_0.smallest_change([5, 3]) == 1
    # Even-length arrays
    assert module_0.smallest_change([1, 2, 3, 4]) == 2
    assert module_0.smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    # Odd-length arrays (middle element ignored)
    assert module_0.smallest_change([1, 4, 2]) == 1
    assert module_0.smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert module_0.smallest_change([1, 2, 5, 2, 3]) == 1
    assert module_0.smallest_change([1, 4, 4, 2]) == 1
    # Works with negative numbers
    assert module_0.smallest_change([-1, 0, -1]) == 0
    assert module_0.smallest_change([-1, 0, 1]) == 1


if __name__ == "__main__":
    test_smallest_change()
    print("All tests passed!")

# Generated at 2026-11-02 20:16:02.893900
# Unit test for function smallest_change
def test_smallest_change():
    # Already palindromic arrays
    assert module_0.smallest_change([]) == 0                # empty array
    assert module_0.smallest_change([1]) == 0               # single element
    assert module_0.smallest_change([1, 1]) == 0            # two equal elements
    assert module_0.smallest_change([1, 2, 3, 2, 1]) == 0   # odd-length palindrome
    assert module_0.smallest_change([1, 2, 2, 1]) == 0      # even-length palindrome
    assert module_0.smallest_change([5, 5, 5, 5, 5]) == 0   # all identical

    # Single change needed
    assert module_0.smallest_change([1, 2]) == 1
    assert module_0.smallest_change([1, 4, 2]) == 1
    assert module_0.smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4

    # Multiple changes needed
    assert module_0.smallest_change([1, 2, 3, 4, 3, 2, 2]) == 2
    assert module_0.smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
    assert module_0.smallest_change([1, 2, 3, 4, 5, 6, 7, 8]) == 4
    assert module_0.smallest_change([1, 4, 2, 3, 2, 5]) == 2

    # Arrays with negative numbers
    assert module_0.smallest_change([-1, -2, -1]) == 0
    assert module_0.smallest_change([-1, 2, -1]) == 0
    assert module_0.smallest_change([-1, -2, -3]) == 2

    # Middle element never requires a change
    assert module_0.smallest_change([1, 2, 99, 2, 1]) == 0

    # Larger case
    assert module_0.smallest_change([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 0
    assert module_0.smallest_change([1, 1, 1, 2, 3, 4, 5, 5]) == 3

    print("All tests passed!")


test_smallest_change()

# Generated at 2026-11-02 20:18:09.250577
# Unit test for function smallest_change
def test_smallest_change():
    # Already a palindrome
    assert module_0.smallest_change([1, 2, 3, 2, 1]) == 0
    assert module_0.smallest_change([1, 2, 3, 3, 2, 1]) == 0
    assert module_0.smallest_change([1, 1, 1, 1]) == 0

    # Single element or empty array is trivially a palindrome
    assert module_0.smallest_change([]) == 0
    assert module_0.smallest_change([5]) == 0

    # Two elements that differ need one change
    assert module_0.smallest_change([1, 2]) == 1
    assert module_0.smallest_change([2, 2]) == 0

    # Examples requiring multiple changes
    assert module_0.smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert module_0.smallest_change([1, 2, 3, 4, 3, 2, 2]) == 2
    assert module_0.smallest_change([1, 4, 2]) == 1
    assert module_0.smallest_change([1, 4, 4, 2]) == 1

    # Odd-length array with mismatched pairs
    assert module_0.smallest_change([1, 2, 3, 4, 5]) == 2
    assert module_0.smallest_change([10, 20, 30]) == 1

    # Negative numbers
    assert module_0.smallest_change([-1, -2, -1]) == 0
    assert module_0.smallest_change([-1, -2, -3]) == 1

    # Mixed values
    assert module_0.smallest_change([0, 0, 0, 0, 0]) == 0
    assert module_0.smallest_change([1, 2, 1, 2]) == 2

    print("All tests passed!")


test_smallest_change()

# Generated at 2026-11-02 20:20:43.450949
# Unit test for function smallest_change
def test_smallest_change():
    # Already palindromic arrays -> 0 changes
    assert module_0.smallest_change([]) == 0
    assert module_0.smallest_change([1]) == 0
    assert module_0.smallest_change([1, 1]) == 0
    assert module_0.smallest_change([1, 2, 1]) == 0
    assert module_0.smallest_change([1, 2, 2, 1]) == 0
    assert module_0.smallest_change([1, 2, 3, 3, 2, 1]) == 0
    assert module_0.smallest_change([1, 2, 3, 4, 3, 2, 2, 1]) == 0
    assert module_0.smallest_change([5, 5, 5, 5]) == 0

    # One change needed
    assert module_0.smallest_change([1, 2]) == 1
    assert module_0.smallest_change([1, 2, 3]) == 1
    assert module_0.smallest_change([1, 4, 2]) == 1
    assert module_0.smallest_change([1, 4, 4, 2]) == 1
    assert module_0.smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1

    # Multiple changes needed
    assert module_0.smallest_change([1, 4, 2, 3]) == 2
    assert module_0.smallest_change([1, 2, 3, 4, 5]) == 2
    assert module_0.smallest_change([1, 2, 3, 4, 5, 6]) == 3
    assert module_0.smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4

    print("All tests passed!")


test_smallest_change()