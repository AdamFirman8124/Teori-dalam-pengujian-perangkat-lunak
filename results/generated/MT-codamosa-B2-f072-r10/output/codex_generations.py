

# Generated at 2026-11-03 03:01:20.938233
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome with weight within limit
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    # Palindrome but too heavy
    assert module_0.will_it_fly([3, 2, 3], 1) == False
    # Not a palindrome
    assert module_0.will_it_fly([1, 2], 5) == False
    # Empty list (trivially palindrome, weight 0)
    assert module_0.will_it_fly([], 5) == True
    # Empty list with zero weight
    assert module_0.will_it_fly([], 0) == True
    # Single element within weight
    assert module_0.will_it_fly([5], 5) == True
    # Single element exceeding weight
    assert module_0.will_it_fly([5], 4) == False
    # Weight exactly equal to sum
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 9) == True
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 8) == False
    # Two-element palindrome
    assert module_0.will_it_fly([4, 4], 8) == True
    assert module_0.will_it_fly([4, 4], 7) == False
    # Two elements not palindrome
    assert module_0.will_it_fly([4, 5], 100) == False
    # Longer palindrome
    assert module_0.will_it_fly([1, 2, 3, 4, 3, 2, 1], 16) == True
    assert module_0.will_it_fly([1, 2, 3, 4, 3, 2, 1], 15) == False
    # Longer non-palindrome
    assert module_0.will_it_fly([1, 2, 3, 2, 2], 100) == False
    # Negative weight limit
    assert module_0.will_it_fly([1], -1) == False
    # Zero weight with zero-sum list
    assert module_0.will_it_fly([0, 0], 0) == True

# Generated at 2026-11-03 03:02:42.756552
# Unit test for function will_it_fly
def test_will_it_fly():
    # Object is balanced but too heavy -> False
    assert module_0.will_it_fly([3, 2, 3], 1) == False
    assert module_0.will_it_fly([3, 2, 3], 9) == False

    # Object is light but not balanced -> False
    assert module_0.will_it_fly([3], 5) == False
    assert module_0.will_it_fly([1, 2], 5) == False
    assert module_0.will_it_fly([1, 2, 3, 4], 100) == False

    # Object is light and balanced -> True
    assert module_0.will_it_fly([3, 2, 3], 8) == True
    assert module_0.will_it_fly([3], 3) == False
    assert module_0.will_it_fly([3], 4) == True
    assert module_0.will_it_fly([1, 2], 3) == False
    assert module_0.will_it_fly([1, 2], 4) == False
    assert module_0.will_it_fly([1, 2, 1], 4) == True

    # Edge cases
    assert module_0.will_it_fly([], 0) == True          # empty is balanced, sum 0 <= 0
    assert module_0.will_it_fly([], 5) == True
    assert module_0.will_it_fly([5], 5) == True         # single element palindrome, exactly at weight
    assert module_0.will_it_fly([5], 4) == False        # single element, too heavy
    assert module_0.will_it_fly([2, 2], 4) == True      # two-element palindrome, exactly at weight
    assert module_0.will_it_fly([2, 2], 3) == False     # too heavy
    assert module_0.will_it_fly([1, 2, 2, 1], 6) == True
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 9) == True
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 8) == False
    assert module_0.will_it_fly([0, 0], 0) == True      # zeros, exactly at weight

    print("All tests passed!")

# Generated at 2026-11-03 03:04:28.103537
# Unit test for function will_it_fly
def test_will_it_fly():
    # Object too heavy to fly
    assert module_0.will_it_fly([3, 2, 3], 7) == True
    assert module_0.will_it_fly([3, 2, 3], 1) == False   # sum=8 > 1
    assert module_0.will_it_fly([3, 2, 3], 8) == False   # sum=8 > 8 is False... sum==8, not greater

    # Not a palindrome
    assert module_0.will_it_fly([1, 2], 5) == False
    assert module_0.will_it_fly([1, 2, 3], 10) == False
    assert module_0.will_it_fly([3, 1, 2], 10) == False

    # Palindrome and light enough
    assert module_0.will_it_fly([3], 5) == True
    assert module_0.will_it_fly([1, 2, 1], 5) == True
    assert module_0.will_it_fly([1, 2, 1], 4) == True    # sum == w exactly
    assert module_0.will_it_fly([1, 2, 1], 3) == False   # sum=4 > 3

    # Empty list (trivially balanced, sum=0)
    assert module_0.will_it_fly([], 0) == True
    assert module_0.will_it_fly([], 5) == True

    # Single element edge cases
    assert module_0.will_it_fly([5], 5) == True
    assert module_0.will_it_fly([5], 4) == False

    # Two-element palindromes
    assert module_0.will_it_fly([2, 2], 4) == True
    assert module_0.will_it_fly([2, 2], 3) == False
    assert module_0.will_it_fly([2, 3], 10) == False

    # Longer palindromes
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 9) == True
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 8) == False

    # Zero weight
    assert module_0.will_it_fly([0, 0], 0) == True
    assert module_0.will_it_fly([1], 0) == False

# Generated at 2026-11-03 03:07:21.495119
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome with sum <= w -> True
    assert module_0.will_it_fly([1, 2, 1], 5) == True
    # Palindrome with sum == w -> True (boundary)
    assert module_0.will_it_fly([3, 2, 3], 8) == True
    # Palindrome but sum > w -> False
    assert module_0.will_it_fly([3, 2, 3], 1) == False
    # Not a palindrome, sum <= w -> False
    assert module_0.will_it_fly([1, 2], 5) == False
    # Not a palindrome and sum > w -> False
    assert module_0.will_it_fly([5, 2], 3) == False
    # Empty list -> True (trivially balanced, sum = 0)
    assert module_0.will_it_fly([], 10) == True
    # Empty list with w = 0 -> True (boundary)
    assert module_0.will_it_fly([], 0) == True
    # Single element <= w -> True
    assert module_0.will_it_fly([4], 4) == True
    # Single element > w -> False
    assert module_0.will_it_fly([4], 3) == False
    # Longer even-length palindrome -> True
    assert module_0.will_it_fly([1, 2, 2, 1], 6) == True
    # Longer even-length palindrome, sum > w -> False
    assert module_0.will_it_fly([1, 2, 2, 1], 5) == False
    # Longer odd-length palindrome -> True
    assert module_0.will_it_fly([1, 3, 5, 3, 1], 13) == True
    # Almost palindrome (middle mismatch) -> False
    assert module_0.will_it_fly([1, 2, 3, 2, 5], 100) == False
    # All identical elements -> True
    assert module_0.will_it_fly([2, 2, 2], 6) == True
    # Negative numbers forming palindrome with sum <= w -> True
    assert module_0.will_it_fly([-1, 0, -1], 0) == True
    # Negative numbers, sum > w -> False
    assert module_0.will_it_fly([-1, 0, -1], -5) == False

    print("All test_will_it_fly tests passed!")

if __name__ == "__main__":
    test_will_it_fly()

# Generated at 2026-11-03 03:10:02.163193
# Unit test for function will_it_fly
def test_will_it_fly():import unittest


class TestWillItFly(unittest.TestCase):

    def test_too_heavy(self):
        self.assertFalse(module_0.will_it_fly([3, 2, 3], 9))

    def test_not_palindrome(self):
        self.assertFalse(module_0.will_it_fly([1, 2], 5))

    def test_palindrome_and_light(self):
        self.assertTrue(module_0.will_it_fly([3, 2, 3], 9))

    def test_palindrome_exact_weight(self):
        self.assertTrue(module_0.will_it_fly([1, 2, 1], 4))

    def test_single_element_light(self):
        self.assertTrue(module_0.will_it_fly([5], 5))

    def test_single_element_too_heavy(self):
        self.assertFalse(module_0.will_it_fly([5], 4))

    def test_empty_list(self):
        self.assertTrue(module_0.will_it_fly([], 0))

    def test_empty_list_zero_weight(self):
        self.assertTrue(module_0.will_it_fly([], 0))

    def test_two_equal_elements(self):
        self.assertTrue(module_0.will_it_fly([2, 2], 4))

    def test_two_equal_elements_too_heavy(self):
        self.assertFalse(module_0.will_it_fly([2, 2], 3))

    def test_negative_numbers_palindrome(self):
        self.assertTrue(module_0.will_it_fly([-1, -1], -2))

    def test_negative_numbers_too_heavy(self):
        self.assertFalse(module_0.will_it_fly([-1, -1], -3))

    def test_long_palindrome(self):
        self.assertTrue(module_0.will_it_fly([1, 2, 3, 2, 1], 10))

    def test_long_non_palindrome(self):
        self.assertFalse(module_0.will_it_fly([1, 2, 3, 3, 1], 100))


if __name__ == "__main__":
    unittest.main()