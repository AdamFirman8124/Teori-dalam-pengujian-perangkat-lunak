

# Generated at 2026-11-03 01:12:42.498442
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([0, -1, -2, 3]) == 0
    assert module_0.prod_signs([-1, 1, -1, 1]) == 0 or module_0.prod_signs([-1, 1, -1, 1]) == 4
    assert module_0.prod_signs([-3, -3]) == 6
    print("All tests passed!")

test_prod_signs()

# Generated at 2026-11-03 01:13:25.622277
# Unit test for function prod_signs
def test_prod_signs():
# nonce:4cf69feb
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([0, -1, 2, 3]) == 0
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10
    assert module_0.prod_signs([2, 4, 6]) == 12
    assert module_0.prod_signs([-2, -4, 6]) == -12

# Generated at 2026-11-03 01:14:25.733622
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing 0 returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -2]) == 0
    assert module_0.prod_signs([-3, 0, 4]) == 0

    # No negatives (even count = 0) -> positive result
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([2, 2]) == 4
    assert module_0.prod_signs([5]) == 5

    # Even number of negatives -> positive result
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10
    assert module_0.prod_signs([-1, 1]) == 2

    # Odd number of negatives -> negative result
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-2, -2, -2]) == -6

    # Larger mixed example
    assert module_0.prod_signs([-1, 2, -3, 4, -5]) == -15  # 3 negatives, sum of abs = 15

    print("All tests passed!")


test_prod_signs()

# Generated at 2026-11-03 01:15:10.907352
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([1, 0, 2, 3]) == 0
    assert module_0.prod_signs([-1, 0, 5]) == 0
    assert module_0.prod_signs([0]) == 0

    # No negatives: sign product is +1, result is sum of abs values
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([2, 4, 6]) == 12

    # Even number of negatives: sign product is +1
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10
    assert module_0.prod_signs([-2, -4]) == 6

    # Odd number of negatives: sign product is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([1, -2, 3, -4, 5]) == -15
    assert module_0.prod_signs([-1, -2, -3]) == -6

# Generated at 2026-11-03 01:16:03.321422
# Unit test for function prod_signs
def test_prod_signs():import unittest


class TestProdSigns(unittest.TestCase):

    def test_empty_array(self):
        self.assertIsNone(module_0.prod_signs([]))

    def test_contains_zero(self):
        self.assertEqual(module_0.prod_signs([0, 1]), 0)
        self.assertEqual(module_0.prod_signs([1, 0, -2, 3]), 0)
        self.assertEqual(module_0.prod_signs([0]), 0)

    def test_odd_number_of_negatives(self):
        self.assertEqual(module_0.prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(module_0.prod_signs([-1, -2, -3]), -6)
        self.assertEqual(module_0.prod_signs([-5]), -5)

    def test_even_number_of_negatives(self):
        self.assertEqual(module_0.prod_signs([1, 2, -2, -4]), 9)
        self.assertEqual(module_0.prod_signs([-1, -2]), 3)

    def test_all_positive(self):
        self.assertEqual(module_0.prod_signs([1, 2, 3]), 6)
        self.assertEqual(module_0.prod_signs([5]), 5)

    def test_all_negative(self):
        self.assertEqual(module_0.prod_signs([-1, -2, -3, -4]), 10)

    def test_result_matches_expected_formula(self):
        arr = [3, -5, 7, -2]
        expected = (-1) ** len([x for x in arr if x < 0]) * sum(abs(x) for x in arr)
        self.assertEqual(module_0.prod_signs(arr), expected)


if __name__ == "__main__":
    unittest.main()