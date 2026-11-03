

# Generated at 2026-11-02 09:43:18.634816
# Unit test for function exchange
def test_exchange():
    # All elements in lst1 are even, no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    # Enough even numbers in lst2 to exchange
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    # Exact number of even numbers needed
    assert module_0.exchange([1, 2, 3], [4, 5, 6]) == "YES"
    # Not enough even numbers in lst2
    assert module_0.exchange([1, 3, 5, 7], [2, 4]) == "NO"
    # lst2 has no even numbers
    assert module_0.exchange([1, 3], []) == "NO"
    # lst1 has no odd numbers
    assert module_0.exchange([], [1, 3, 5]) == "YES"
    # Both lists empty
    assert module_0.exchange([], []) == "YES"
    # Negative numbers: -3 is odd, -2 is even
    assert module_0.exchange([-3, -1], [-2, -4]) == "YES"
    assert module_0.exchange([-3, -1, -5], [-2]) == "NO"
    # Zero is even
    assert module_0.exchange([1], [0]) == "YES"
    # More evens than needed in lst2
    assert module_0.exchange([1, 3], [2, 4, 6, 8]) == "YES"
    # Single element lists
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([3], [1]) == "NO"
    # Mixed parity cases
    assert module_0.exchange([1, 2, 4], [1, 2]) == "YES"
    assert module_0.exchange([1, 3, 2], [1, 3]) == "NO"

# Generated at 2026-11-02 09:44:32.715665
# Unit test for function exchange
def test_exchange():
    # lst1 already all even -> YES
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    
    # lst1 has odds, lst2 has enough evens to swap -> YES
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"
    
    # lst1 has more odds than lst2 has evens -> NO
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    
    # lst1 has odds, lst2 has no evens -> NO
    assert module_0.exchange([1, 2], [1, 3]) == "NO"
    
    # exact match: odds in lst1 equal evens in lst2 -> YES
    assert module_0.exchange([1, 3], [2, 4]) == "YES"
    
    # empty lst1 -> YES (no odds to exchange)
    assert module_0.exchange([], [1, 3, 5]) == "YES"
    
    # both lists empty -> YES
    assert module_0.exchange([], []) == "YES"
    
    # lst1 all odd, lst2 all even -> YES
    assert module_0.exchange([1, 3, 5, 7], [2, 4, 6, 8]) == "YES"
    
    # lst1 all odd, lst2 all odd -> NO
    assert module_0.exchange([1, 3], [1, 3]) == "NO"
    
    # negative numbers count correctly
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3], [-1, -3]) == "NO"
    
    # zero is even
    assert module_0.exchange([1], [0]) == "YES"
    
    # larger imbalance case -> NO
    assert module_0.exchange([1, 3, 5, 7, 9], [2]) == "NO"

# Generated at 2026-11-02 09:45:49.133070
# Unit test for function exchange
def test_exchange():
    # lst1 has odd numbers, lst2 has enough even numbers to swap
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"

    # Not enough even numbers in lst2 to replace odd numbers in lst1
    assert module_0.exchange([1, 3, 5], [2]) == "NO"

    # lst1 already all even
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # lst1 all odd, lst2 all even (exact match)
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # lst1 all odd, lst2 all odd
    assert module_0.exchange([1, 3], [5, 7]) == "NO"

    # Empty lst1 should always be YES
    assert module_0.exchange([], [1, 2, 3]) == "YES"

    # Both lists empty
    assert module_0.exchange([], []) == "YES"

    # Single element cases
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [3]) == "NO"
    assert module_0.exchange([2], [1]) == "YES"

    # Even numbers in lst1 don't count against, extra evens in lst2 help
    assert module_0.exchange([1, 1, 1, 2], [2, 2, 2, 2]) == "YES"

    # Negative numbers: -1 is odd, -2 is even
    assert module_0.exchange([-1], [-2]) == "YES"
    assert module_0.exchange([-1], [-3]) == "NO"
    assert module_0.exchange([-2], [1]) == "YES"

    # Zero is even
    assert module_0.exchange([1], [0]) == "YES"

    # Large lists
    assert module_0.exchange([1] * 100, [2] * 100) == "YES"
    assert module_0.exchange([1] * 101, [2] * 100) == "NO"

# Generated at 2026-11-02 09:47:28.968699
# Unit test for function exchange
def test_exchange():
# nonce:2fc5ff70
    # lst1 already all even
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # odd elements in lst1, enough even elements in lst2 to swap
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"

    # not enough even elements in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"

    # equal counts (even >= odd boundary)
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # zero counts as even
    assert module_0.exchange([0], [1]) == "YES"
    assert module_0.exchange([0, 1], [0]) == "YES"

    # negative numbers: Python modulo keeps -1 % 2 == 1
    assert module_0.exchange([-1, -3], [-2, -4, -6]) == "YES"
    assert module_0.exchange([-1, -3, -5], [-2]) == "NO"
    assert module_0.exchange([-2, -4], [1, 3]) == "YES"

    # empty lst1: nothing to fix
    assert module_0.exchange([], [1, 3]) == "YES"

    # empty lst2 with odds in lst1: cannot fix
    assert module_0.exchange([1], []) == "NO"
    assert module_0.exchange([], []) == "YES"

    # single element cases
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [3]) == "NO"
    assert module_0.exchange([2], [3]) == "YES"

    # larger mixed cases
    assert module_0.exchange([1, 2, 3, 5, 7], [2, 4, 6, 8, 10]) == "YES"
    assert module_0.exchange([1, 2, 3, 5, 7, 9], [2, 4, 6]) == "NO"
    assert module_0.exchange([2, 2, 2], [1]) == "YES"

    # duplicates count individually
    assert module_0.exchange([1, 1, 1], [2, 2, 2]) == "YES"
    assert module_0.exchange([1, 1, 1, 1], [2, 2, 2]) == "NO"

# Generated at 2026-11-02 09:50:04.521132
# Unit test for function exchange
def test_exchange():import unittest


class TestExchange(unittest.TestCase):

    def test_all_even_lst1_empty_lst2(self):
        # No odd numbers to exchange, should be YES
        self.assertEqual(module_0.exchange([2, 4, 6], []), "YES")

    def test_equal_counts(self):
        # One odd in lst1, one even in lst2 -> exchange possible
        self.assertEqual(module_0.exchange([1, 2, 3], [2, 4]), "YES")

    def test_enough_evens(self):
        # More evens in lst2 than odds in lst1
        self.assertEqual(module_0.exchange([1, 5, 3], [2, 4, 6, 8]), "YES")

    def test_not_enough_evens(self):
        # More odds in lst1 than evens in lst2
        self.assertEqual(module_0.exchange([1, 3, 5], [2]), "NO")

    def test_no_odds_no_evens(self):
        self.assertEqual(module_0.exchange([2, 4], [1, 3]), "YES")

    def test_all_odd_all_odd(self):
        self.assertEqual(module_0.exchange([1, 3], [5, 7]), "NO")

    def test_empty_both(self):
        self.assertEqual(module_0.exchange([], []), "YES")

    def test_empty_lst1(self):
        self.assertEqual(module_0.exchange([], [2, 4]), "YES")

    def test_empty_lst2(self):
        self.assertEqual(module_0.exchange([1, 2], []), "NO")

    def test_negative_numbers(self):
        # Negative odd: -3 % 2 == 1 in Python, negative even: -2 % 2 == 0
        self.assertEqual(module_0.exchange([-3, 2], [-2, 4]), "YES")
        self.assertEqual(module_0.exchange([-3, -5], [-2]), "NO")

    def test_single_elements(self):
        self.assertEqual(module_0.exchange([1], [2]), "YES")
        self.assertEqual(module_0.exchange([1], [3]), "NO")
        self.assertEqual(module_0.exchange([2], [2]), "YES")

    def test_large_lists(self):
        lst1 = list(range(1, 51))          # 25 odds
        lst2 = list(range(2, 102, 2))      # 50 evens
        self.assertEqual(module_0.exchange(lst1, lst2), "YES")
        self.assertEqual(module_0.exchange(lst1, [2]), "NO")

    def test_zero_is_even(self):
        self.assertEqual(module_0.exchange([1], [0]), "YES")
        self.assertEqual(module_0.exchange([1, 3], [0]), "NO")


if __name__ == "__main__":
    unittest.main()