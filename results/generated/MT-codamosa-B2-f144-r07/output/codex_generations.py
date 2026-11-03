

# Generated at 2026-11-02 22:28:47.606908
# Unit test for function simplify
def test_simplify():
    # Result is a whole number
    assert module_0.simplify("1/2", "2/1") == True      # 1/2 * 2/1 = 1
    assert module_0.simplify("1/3", "3/1") == True      # 1/3 * 3/1 = 1
    assert module_0.simplify("7/10", "10/7") == True    # 7/10 * 10/7 = 1
    assert module_0.simplify("2/10", "10/2") == True    # 2/10 * 10/2 = 1
    assert module_0.simplify("3/4", "4/3") == True      # 3/4 * 4/3 = 1
    assert module_0.simplify("1/2", "4/2") == True      # 1/2 * 4/2 = 1

    # Result is not a whole number
    assert module_0.simplify("1/2", "2/2") == False     # 1/2 * 2/2 = 1/2
    assert module_0.simplify("1/4", "2/2") == False     # 1/4 * 1 = 1/4
    assert module_0.simplify("2/3", "3/4") == False     # 2/3 * 3/4 = 1/2
    assert module_0.simplify("1/2", "1/2") == False     # 1/2 * 1/2 = 1/4
    assert module_0.simplify("5/6", "6/5") == True      # 5/6 * 6/5 = 1

    # Zero numerator
    assert module_0.simplify("0/2", "3/1") == True      # 0 * 3 = 0 (whole number)

    # Negative fractions
    assert module_0.simplify("-1/2", "2/1") == True     # -1/2 * 2 = -1
    assert module_0.simplify("1/2", "-2/1") == True     # 1/2 * -2 = -1
    assert module_0.simplify("-1/2", "1/2") == False    # -1/2 * 1/2 = -1/4
    assert module_0.simplify("-3/4", "-4/3") == True    # -3/4 * -4/3 = 1

    # Multi-digit numbers
    assert module_0.simplify("100/2", "1/50") == True   # 100/2 * 1/50 = 1
    assert module_0.simplify("12/7", "7/4") == True     # 12/7 * 7/4 = 3
    assert module_0.simplify("13/7", "7/4") == False    # 13/7 * 7/4 = 13/4

    # Improper fractions producing whole numbers
    assert module_0.simplify("9/2", "2/3") == True      # 9/2 * 2/3 = 3
    assert module_0.simplify("8/3", "3/2") == True      # 8/3 * 3/2 = 4

# Generated at 2026-11-02 22:30:17.073146
# Unit test for function simplify
def test_simplify():import unittest

class TestSimplify(unittest.TestCase):
    def test_whole_number_result(self):
        self.assertEqual(module_0.simplify("1/2", "2/1"), True)

    def test_fraction_result(self):
        self.assertEqual(module_0.simplify("1/2", "1/2"), False)

    def test_simplify_to_whole(self):
        self.assertEqual(module_0.simplify("2/4", "4/2"), True)

    def test_simplify_to_fraction(self):
        self.assertEqual(module_0.simplify("1/3", "1/3"), False)

    def test_zero_numerator(self):
        self.assertEqual(module_0.simplify("0/1", "1/2"), True)

    def test_negative_whole(self):
        self.assertEqual(module_0.simplify("-1/2", "2/1"), True)

    def test_negative_fraction(self):
        self.assertEqual(module_0.simplify("-1/2", "1/2"), False)

    def test_large_numbers(self):
        self.assertEqual(module_0.simplify("100/3", "3/100"), True)

    def test_one_over_one(self):
        self.assertEqual(module_0.simplify("1/1", "1/1"), True)

    def test_irreducible_fraction(self):
        self.assertEqual(module_0.simplify("7/13", "11/5"), False)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 22:31:17.026407
# Unit test for function simplify
def test_simplify():
    assert module_0.simplify("1/5", "5/1") == True
    assert module_0.simplify("1/6", "2/1") == False
    assert module_0.simplify("7/10", "10/2") == False
    assert module_0.simplify("2/4", "2/1") == True
    assert module_0.simplify("3/4", "4/3") == True
    assert module_0.simplify("1/3", "3/1") == True
    assert module_0.simplify("0/1", "5/1") == True
    assert module_0.simplify("1/2", "1/2") == False
    assert module_0.simplify("5/1", "1/5") == True
    assert module_0.simplify("6/2", "3/1") == True
    assert module_0.simplify("9/10", "10/3") == False
    assert module_0.simplify("100/7", "7/100") == True

# Generated at 2026-11-02 22:32:24.203663
# Unit test for function simplify
def test_simplify():import unittest


class TestSimplify(unittest.TestCase):

    def test_product_whole_number(self):
        # 1/5 * 5/1 = 1
        self.assertTrue(module_0.simplify("1/5", "5/1"))

    def test_product_whole_number_two(self):
        # 1/6 * 2/1 = 1/3 -> not whole
        self.assertFalse(module_0.simplify("1/6", "2/1"))

    def test_product_whole_number_three(self):
        # 7/3 * 3/7 = 1
        self.assertTrue(module_0.simplify("7/3", "3/7"))

    def test_product_not_whole(self):
        # 1/2 * 1/2 = 1/4
        self.assertFalse(module_0.simplify("1/2", "1/2"))

    def test_product_not_whole_two(self):
        # 2/3 * 3/4 = 1/2
        self.assertFalse(module_0.simplify("2/3", "3/4"))

    def test_product_multi_whole(self):
        # 1/2 * 4/1 = 2
        self.assertTrue(module_0.simplify("1/2", "4/1"))

    def test_product_integer_times_integer(self):
        # 2/1 * 3/1 = 6
        self.assertTrue(module_0.simplify("2/1", "3/1"))

    def test_product_large_numbers(self):
        # 100/7 * 7/100 = 1
        self.assertTrue(module_0.simplify("100/7", "7/100"))

    def test_product_large_numbers_false(self):
        # 100/7 * 7/3 is not whole
        self.assertFalse(module_0.simplify("100/7", "7/3"))

    def test_product_negative_result_not_whole(self):
        # -1/2 * 1/3 -> not whole
        self.assertFalse(module_0.simplify("-1/2", "1/3"))

    def test_product_negative_whole(self):
        # -1/2 * 4/1 = -2
        self.assertTrue(module_0.simplify("-1/2", "4/1"))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 22:34:19.704198
# Unit test for function simplify
def test_simplify():
    # Product is exactly 1
    assert module_0.simplify("1/2", "2/1") == True
    assert module_0.simplify("1/3", "3/1") == True
    assert module_0.simplify("2/8", "4/1") == True   # 8/8 = 1

    # Product is a whole number greater than 1
    assert module_0.simplify("7/2", "2/1") == True   # 14/2 = 7
    assert module_0.simplify("5/1", "1/1") == True   # 5
    assert module_0.simplify("3/9", "9/3") == True   # 27/27 = 3
    assert module_0.simplify("1/7", "14/2") == True  # 14/14 = 1

    # Product is not a whole number
    assert module_0.simplify("1/2", "3/1") == False  # 3/2
    assert module_0.simplify("1/4", "2/3") == False  # 2/12
    assert module_0.simplify("1/5", "1/5") == False  # 1/25
    assert module_0.simplify("2/3", "3/5") == False  # 6/15

    # Numerator zero -> product is 0, a whole number
    assert module_0.simplify("0/1", "5/2") == True
    assert module_0.simplify("0/3", "1/3") == True

    # Negative fractions
    assert module_0.simplify("-1/2", "2/1") == True   # -2/2 = -1
    assert module_0.simplify("-1/2", "3/1") == False  # -3/2
    assert module_0.simplify("-2/4", "-4/2") == True  # 8/8 = 1

    # Whole number inputs
    assert module_0.simplify("1/1", "1/1") == True
    assert module_0.simplify("10/1", "1/10") == True

    print("All test_simplify tests passed!")


if __name__ == "__main__":
    test_simplify()