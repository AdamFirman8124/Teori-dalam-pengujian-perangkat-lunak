

# Generated at 2026-11-03 00:45:12.196410
# Unit test for function prod_signs
def test_prod_signs():
    # Test empty array returns None
    assert module_0.prod_signs([]) is None

    # Test arrays containing zero return 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -2]) == 0
    assert module_0.prod_signs([-1, 0, 0, 3]) == 0

    # Test all positive numbers
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Test odd number of negatives (sign is -1)
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Test even number of negatives (sign is +1)
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10

    # Test mixed with duplicates
    assert module_0.prod_signs([-2, -2, 4]) == 8
    assert module_0.prod_signs([-2, 2]) == -4

    print("All tests passed!")


if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-03 00:46:21.752203
# Unit test for function prod_signs
def test_prod_signs():import unittest


class TestProdSigns(unittest.TestCase):
    def test_empty_array(self):
        self.assertIsNone(module_0.prod_signs([]))

    def test_array_with_zero(self):
        self.assertEqual(module_0.prod_signs([1, 0, -3, 2]), 0)

    def test_all_positive(self):
        self.assertEqual(module_0.prod_signs([1, 2, 3]), 6)

    def test_odd_negatives(self):
        self.assertEqual(module_0.prod_signs([-1, 2, 3]), -6)

    def test_even_negatives(self):
        self.assertEqual(module_0.prod_signs([-1, -2, 3]), 6)

    def test_all_negative(self):
        self.assertEqual(module_0.prod_signs([-1, -2, -3]), -6)

    def test_single_positive(self):
        self.assertEqual(module_0.prod_signs([5]), 5)

    def test_single_negative(self):
        self.assertEqual(module_0.prod_signs([-5]), -5)

    def test_single_zero(self):
        self.assertEqual(module_0.prod_signs([0]), 0)

    def test_mixed_with_duplicates(self):
        self.assertEqual(module_0.prod_signs([-2, -2, 4, 1]), 9)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 00:47:53.496370
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None
    
    # Array containing zero returns 0
    assert module_0.prod_signs([0, 1, 2, -3]) == 0
    assert module_0.prod_signs([0]) == 0
    
    # Odd number of negatives -> negative result
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5
    
    # Even number of negatives -> positive result
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10
    
    # No negatives -> sum of absolute values
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([1]) == 1
    
    print("All tests passed!")

if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-03 00:48:45.096393
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero -> sum of absolute values but product is 0
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -2, 3]) == 0

    # No negatives -> positive product times sum of absolute values
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5, 4]) == 9

    # Odd number of negatives -> negative result
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5

    # Even number of negatives -> positive result
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10

# Generated at 2026-11-03 00:50:20.029775
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # All positive numbers: sign product is 1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Even number of negatives: sign product is 1
    assert module_0.prod_signs([-1, -2, -3]) == 6
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10

    # Odd number of negatives: sign product is -1
    assert module_0.prod_signs([-1, -2, 3]) == -6
    assert module_0.prod_signs([1, -2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5

    # Array containing zero: result is 0
    assert module_0.prod_signs([0, 1, -2, 3]) == 0
    assert module_0.prod_signs([0, -1, -2]) == 0

    # Single element arrays
    assert module_0.prod_signs([7]) == 7
    assert module_0.prod_signs([0]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_prod_signs()