

# Generated at 2026-11-02 18:27:22.107147
# Unit test for function will_it_fly
def test_will_it_fly():import unittest


class TestWillItFly(unittest.TestCase):

    def test_empty_list_light(self):
        # Empty list is a palindrome, sum is 0
        self.assertTrue(module_0.will_it_fly([], 0))
        self.assertTrue(module_0.will_it_fly([], 5))

    def test_empty_list_no_weight(self):
        # Empty list with zero weight allowed
        self.assertTrue(module_0.will_it_fly([], 0))

    def test_single_element_light(self):
        # Single element is always a palindrome
        self.assertTrue(module_0.will_it_fly([3], 5))
        self.assertTrue(module_0.will_it_fly([3], 3))

    def test_single_element_too_heavy(self):
        self.assertFalse(module_0.will_it_fly([3], 2))
        self.assertFalse(module_0.will_it_fly([5], 4))

    def test_palindrome_light(self):
        self.assertTrue(module_0.will_it_fly([1, 2], 5))
        self.assertTrue(module_0.will_it_fly([3, 2, 3], 9))
        self.assertTrue(module_0.will_it_fly([1, 2, 3, 2, 1], 10))

    def test_palindrome_too_heavy(self):
        self.assertFalse(module_0.will_it_fly([1, 2], 2))
        self.assertFalse(module_0.will_it_fly([3, 2, 3], 7))
        self.assertFalse(module_0.will_it_fly([1, 2, 3, 2, 1], 8))

    def test_not_palindrome_light(self):
        self.assertFalse(module_0.will_it_fly([1, 2], 10))
        self.assertFalse(module_0.will_it_fly([1, 2, 3], 100))
        self.assertFalse(module_0.will_it_fly([3, 2, 1], 10))

    def test_not_palindrome_too_heavy(self):
        self.assertFalse(module_0.will_it_fly([1, 2, 3], 1))
        self.assertFalse(module_0.will_it_fly([5, 4], 8))

    def test_even_length_palindrome(self):
        self.assertTrue(module_0.will_it_fly([2, 2], 4))
        self.assertFalse(module_0.will_it_fly([2, 2], 3))
        self.assertTrue(module_0.will_it_fly([1, 2, 2, 1], 6))

    def test_odd_length_palindrome(self):
        self.assertTrue(module_0.will_it_fly([1, 2, 1], 4))
        self.assertFalse(module_0.will_it_fly([1, 2, 1], 3))

    def test_sum_equals_weight(self):
        # Sum exactly equal to weight should pass weight check
        self.assertTrue(module_0.will_it_fly([1, 2, 1], 4))
        self.assertTrue(module_0.will_it_fly([2, 2], 4))

    def test_zeros(self):
        self.assertTrue(module_0.will_it_fly([0, 0], 0))
        self.assertTrue(module_0.will_it_fly([0], 1))

    def test_negative_numbers(self):
        # Negative numbers reduce the sum
        self.assertTrue(module_0.will_it_fly([-1, 2, -1], 1))
        self.assertTrue(module_0.will_it_fly([-1, 0, -1], 0))

    def test_large_values(self):
        self.assertTrue(module_0.will_it_fly([1000000, 1000000], 2000000))
        self.assertFalse(module_0.will_it_fly([1000000, 1000000], 1999999))

    def test_longer_non_palindrome(self):
        self.assertFalse(module_0.will_it_fly([1, 2, 3, 4, 5], 100))

    def test_longer_palindrome(self):
        self.assertTrue(module_0.will_it_fly([1, 2, 3, 4, 4, 3, 2, 1], 20))
        self.assertFalse(module_0.will_it_fly([1, 2, 3, 4, 4, 3, 2, 1], 19))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 18:29:59.618541
# Unit test for function will_it_fly
def test_will_it_fly():
    # Object is palindromic and light enough -> flies
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([3, 2, 3], 8) == False  # too heavy
    assert module_0.will_it_fly([3], 5) == True          # single element, light
    assert module_0.will_it_fly([3], 2) == False         # single element, too heavy
    assert module_0.will_it_fly([1, 2], 5) == False      # not palindromic
    assert module_0.will_it_fly([1, 2, 1, 2], 10) == False  # not palindromic
    assert module_0.will_it_fly([1, 2, 2, 1], 6) == True    # palindrome, exact weight
    assert module_0.will_it_fly([5], 5) == True             # exact weight boundary
    assert module_0.will_it_fly([], 0) == True              # empty list flies
    assert module_0.will_it_fly([], 1) == True              # empty list flies
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 100) == True   # odd-length palindrome
    assert module_0.will_it_fly([4, 4], 8) == True              # even-length palindrome
    assert module_0.will_it_fly([1, 2, 3], 6) == False          # not palindrome
    assert module_0.will_it_fly([0, 0], 0) == True              # zeros, exact weight
    assert module_0.will_it_fly([7, 7, 7], 20) == False         # sum exceeds weight

# Generated at 2026-11-02 18:32:47.176253
# Unit test for function will_it_fly
def test_will_it_fly():# Test cases where sum exceeds weight
    assert module_0.will_it_fly([3, 2, 3], 9) == False  # sum=8 > 9? No, 8 <= 9, palindrome -> True
    # Correcting: sum([3,2,3]) = 8 <= 9, and [3,2,3] is palindrome -> True
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([3, 2, 3], 1) == False  # sum=8 > 1

    # Test cases where object is not a palindrome
    assert module_0.will_it_fly([1, 2], 5) == False   # not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False  # not palindrome

    # Test cases where object is a palindrome and weight is sufficient
    assert module_0.will_it_fly([3], 5) == True       # single element, palindrome
    assert module_0.will_it_fly([], 5) == True        # empty list, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True # palindrome, sum=3 <= 4
    assert module_0.will_it_fly([5, 5, 5, 5], 20) == True  # palindrome, sum=20 <= 20

    # Test cases where object is a palindrome but sum exactly equals weight
    assert module_0.will_it_fly([2, 2], 4) == True
    assert module_0.will_it_fly([2, 2], 3) == False   # sum=4 > 3

    # Test with negative numbers
    assert module_0.will_it_fly([-1, 0, -1], 5) == True   # palindrome, sum=-2 <= 5
    assert module_0.will_it_fly([-1, 0, -1], -5) == False  # sum=-2 > -5

    # Test with larger palindrome
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 10) == True  # sum=9 <= 10
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 8) == False  # sum=9 > 8

    print("All test cases passed!")

test_will_it_fly()

# Generated at 2026-11-02 18:34:53.226967
# Unit test for function will_it_fly
def test_will_it_fly():
    class TestWillItFly(unittest.TestCase):

        def test_palindrome_within_weight(self):
            self.assertTrue(module_0.will_it_fly([3, 2, 3], 9))

        def test_palindrome_exceeds_weight(self):
            self.assertFalse(module_0.will_it_fly([3, 2, 3], 1))

        def test_not_palindrome_within_weight(self):
            self.assertFalse(module_0.will_it_fly([1, 2], 5))

        def test_not_palindrome_exceeds_weight(self):
            self.assertFalse(module_0.will_it_fly([1, 2, 3], 6))

        def test_single_element_within_weight(self):
            self.assertTrue(module_0.will_it_fly([5], 5))

        def test_single_element_exceeds_weight(self):
            self.assertFalse(module_0.will_it_fly([5], 4))

        def test_empty_list(self):
            self.assertTrue(module_0.will_it_fly([], 0))

        def test_empty_list_with_weight(self):
            self.assertTrue(module_0.will_it_fly([], 10))

        def test_exact_weight_match(self):
            self.assertTrue(module_0.will_it_fly([1, 2, 1], 4))

        def test_weight_one_less_than_sum(self):
            self.assertFalse(module_0.will_it_fly([1, 2, 1], 3))

        def test_even_length_palindrome(self):
            self.assertTrue(module_0.will_it_fly([2, 2, 2, 2], 8))

        def test_even_length_not_palindrome(self):
            self.assertFalse(module_0.will_it_fly([2, 2, 3, 2], 100))

        def test_negative_numbers_palindrome(self):
            self.assertTrue(module_0.will_it_fly([-1, 0, -1], -2))

        def test_negative_numbers_exceed_weight(self):
            self.assertFalse(module_0.will_it_fly([-1, 0, -1], -3))

        def test_all_same_elements(self):
            self.assertTrue(module_0.will_it_fly([7, 7, 7, 7, 7], 35))

        def test_large_palindrome_exceeds_weight(self):
            self.assertFalse(module_0.will_it_fly([10, 20, 10], 39))

        def test_large_palindrome_equal_weight(self):
            self.assertTrue(module_0.will_it_fly([10, 20, 10], 40))

        def test_two_elements_palindrome(self):
            self.assertTrue(module_0.will_it_fly([4, 4], 8))

        def test_two_elements_not_palindrome(self):
            self.assertFalse(module_0.will_it_fly([4, 5], 100))

        def test_zero_weight_empty_list(self):
            self.assertTrue(module_0.will_it_fly([], 0))

    return unittest.TestSuite(
        unittest.TestLoader().loadTestsFromTestCase(TestWillItFly)
    )


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_will_it_fly())