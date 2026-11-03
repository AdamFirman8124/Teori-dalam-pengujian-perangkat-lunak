

# Generated at 2026-11-03 01:58:17.963734
# Unit test for function simplify
def test_simplify():import unittest


def module_0.simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator / denom == int(numerator / denom)):
        return True
    return False


class TestSimplify(unittest.TestCase):

    def test_product_is_whole_number(self):
        self.assertTrue(module_0.simplify("1/5", "5/1"))

    def test_product_is_not_whole_number(self):
        self.assertFalse(module_0.simplify("1/2", "1/2"))

    def test_two_whole_numbers(self):
        self.assertTrue(module_0.simplify("2/1", "3/1"))

    def test_reciprocal_fractions(self):
        self.assertTrue(module_0.simplify("7/2", "2/7"))

    def test_fraction_times_whole(self):
        self.assertTrue(module_0.simplify("1/2", "4/1"))

    def test_non_whole_result(self):
        self.assertFalse(module_0.simplify("1/3", "2/1"))

    def test_zero_numerator(self):
        self.assertTrue(module_0.simplify("0/1", "5/2"))

    def test_large_numbers(self):
        self.assertTrue(module_0.simplify("100/3", "3/100"))

    def test_result_is_fraction(self):
        self.assertFalse(module_0.simplify("2/3", "3/4"))

    def test_multiplied_to_three(self):
        self.assertTrue(module_0.simplify("3/2", "2/1"))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 01:59:23.064882
# Unit test for function simplify
def test_simplify():
    # Product simplifies to a whole number
    assert module_0.simplify("1/2", "4/2") == True      # (1*4)/(2*2) = 4/4 = 1
    assert module_0.simplify("2/3", "3/4") == False     # (2*3)/(3*4) = 6/12 = 1/2
    assert module_0.simplify("1/2", "2/1") == True      # (1*2)/(2*1) = 2/2 = 1
    assert module_0.simplify("3/4", "4/3") == True      # (3*4)/(4*3) = 12/12 = 1
    assert module_0.simplify("1/3", "3/1") == True      # (1*3)/(3*1) = 3/3 = 1
    assert module_0.simplify("2/4", "4/2") == True      # (2*4)/(4*2) = 8/8 = 1
    assert module_0.simplify("7/2", "4/2") == True      # (7*4)/(2*2) = 28/4 = 7
    assert module_0.simplify("1/6", "2/1") == False     # (1*2)/(6*1) = 2/6 = 1/3
    assert module_0.simplify("1/2", "1/2") == False     # (1*1)/(2*2) = 1/4
    assert module_0.simplify("5/1", "3/1") == True      # (5*3)/(1*1) = 15/1 = 15
    assert module_0.simplify("0/5", "3/2") == True      # (0*3)/(5*2) = 0/10 = 0
    assert module_0.simplify("-1/2", "4/1") == True     # (-1*4)/(2*1) = -4/2 = -2
    assert module_0.simplify("-1/2", "3/1") == False    # (-1*3)/(2*1) = -3/2
    assert module_0.simplify("10/3", "3/10") == True    # (10*3)/(3*10) = 30/30 = 1
    assert module_0.simplify("9/4", "4/9") == True      # (9*4)/(4*9) = 36/36 = 1
    assert module_0.simplify("9/4", "2/9") == False     # (9*2)/(4*9) = 18/36 = 1/2

# Generated at 2026-11-03 02:00:31.369907
# Unit test for function simplify
def test_simplify():
    # Product is a whole number
    assert module_0.simplify("1/2", "2/1") == True      # (1*2)/(2*1) = 2/2 = 1
    assert module_0.simplify("4/2", "1/2") == True      # 4/4 = 1
    assert module_0.simplify("7/3", "3/7") == True      # 21/21 = 1
    assert module_0.simplify("1/3", "3/1") == True      # 3/3 = 1
    assert module_0.simplify("2/1", "5/2") == True      # 10/2 = 5
    assert module_0.simplify("0/5", "3/4") == True      # 0 is a whole number

    # Product is not a whole number
    assert module_0.simplify("1/2", "2/3") == False     # 2/6 = 1/3
    assert module_0.simplify("1/4", "1/4") == False     # 1/16
    assert module_0.simplify("3/2", "5/4") == False     # 15/8
    assert module_0.simplify("1/2", "1/2") == False     # 1/4

    # Negative values
    assert module_0.simplify("-1/2", "4/1") == True     # -4/2 = -2
    assert module_0.simplify("1/-2", "3/1") == False    # 3/-2

    # Larger numbers
    assert module_0.simplify("100/3", "3/100") == True  # 300/300 = 1
    assert module_0.simplify("100/7", "7/100") == True  # 700/700 = 1
    assert module_0.simplify("999/1000", "1000/999") == True

# Generated at 2026-11-03 02:01:47.149019
# Unit test for function simplify
def test_simplify():
    # Whole number results
    assert module_0.simplify("1/2", "4/2") == True      # (1/2)*(4/2) = 1
    assert module_0.simplify("1/3", "3/1") == True      # (1/3)*(3/1) = 1
    assert module_0.simplify("2/4", "2/1") == True      # (2/4)*(2/1) = 1
    assert module_0.simplify("3/4", "4/3") == True      # (3/4)*(4/3) = 1
    assert module_0.simplify("5/1", "2/1") == True      # (5)*(2) = 10
    assert module_0.simplify("0/5", "3/4") == True      # 0 is a whole number

    # Non-whole number results
    assert module_0.simplify("7/10", "10/2") == False   # (7/10)*(10/2) = 3.5
    assert module_0.simplify("1/2", "1/2") == False     # (1/2)*(1/2) = 0.25
    assert module_0.simplify("2/3", "3/5") == False     # (2/3)*(3/5) = 0.4
    assert module_0.simplify("1/4", "1/4") == False     # (1/4)*(1/4) = 0.0625

    # Negative fractions
    assert module_0.simplify("-1/2", "4/2") == True     # (-1/2)*(4/2) = -1
    assert module_0.simplify("-1/2", "1/3") == False    # (-1/2)*(1/3) = -1/6

    # Larger numbers
    assert module_0.simplify("100/1", "1/100") == True  # 100 * 0.01 = 1
    assert module_0.simplify("999/3", "3/999") == True  # 333 * (1/333) = 1

    print("All tests passed!")


test_simplify()

# Generated at 2026-11-03 02:03:46.270401
# Unit test for function simplify
def test_simplify():
    # Products that result in a whole number -> True
    assert module_0.simplify("1/2", "2/1") == True      # (1*2)/(2*1) = 1
    assert module_0.simplify("1/5", "5/1") == True      # (1*5)/(5*1) = 1
    assert module_0.simplify("1/3", "3/1") == True      # (1*3)/(3*1) = 1
    assert module_0.simplify("2/4", "4/2") == True      # (2*4)/(4*2) = 1
    assert module_0.simplify("3/2", "2/3") == True      # (3*2)/(2*3) = 1
    assert module_0.simplify("1/6", "6/1") == True      # (1*6)/(6*1) = 1
    assert module_0.simplify("4/8", "8/4") == True      # (4*8)/(8*4) = 1
    assert module_0.simplify("5/10", "2/1") == True     # (5*2)/(10*1) = 1
    assert module_0.simplify("10/2", "1/5") == True     # (10*1)/(2*5) = 1

    # Products that do NOT result in a whole number -> False
    assert module_0.simplify("1/2", "1/2") == False     # (1*1)/(2*2) = 1/4
    assert module_0.simplify("1/3", "1/3") == False     # (1*1)/(3*3) = 1/9
    assert module_0.simplify("2/3", "3/4") == False     # (2*3)/(3*4) = 1/2
    assert module_0.simplify("7/4", "4/3") == False     # (7*4)/(4*3) = 7/3
    assert module_0.simplify("1/7", "2/3") == False     # (1*2)/(7*3) = 2/21

    # Products resulting in whole numbers greater than 1 -> True
    assert module_0.simplify("2/1", "3/1") == True      # (2*3)/(1*1) = 6
    assert module_0.simplify("6/2", "4/3") == True      # (6*4)/(2*3) = 4
    assert module_0.simplify("9/3", "5/3") == True      # (9*5)/(3*3) = 5

    # Zero numerator -> True (0 is a whole number)
    assert module_0.simplify("0/5", "3/4") == True      # (0*3)/(5*4) = 0

    # Larger numbers
    assert module_0.simplify("100/3", "3/100") == True  # (100*3)/(3*100) = 1
    assert module_0.simplify("100/7", "7/3") == False   # (100*7)/(7*3) = 100/3