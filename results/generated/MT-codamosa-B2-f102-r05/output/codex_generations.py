

# Generated at 2026-11-02 23:38:29.268303
# Unit test for function choose_num
def test_choose_num():import unittest


class TestChooseNum(unittest.TestCase):

    def test_x_greater_than_y_returns_minus_one(self):
        self.assertEqual(module_0.choose_num(12, 1), -1)
        self.assertEqual(module_0.choose_num(5, 3), -1)

    def test_y_even_returns_y(self):
        self.assertEqual(module_0.choose_num(12, 15), 14)
        self.assertEqual(module_0.choose_num(13, 12), 12)
        self.assertEqual(module_0.choose_num(2, 10), 10)

    def test_x_equals_y_odd_returns_minus_one(self):
        self.assertEqual(module_0.choose_num(5, 5), -1)
        self.assertEqual(module_0.choose_num(7, 7), -1)

    def test_x_equals_y_even_returns_y(self):
        self.assertEqual(module_0.choose_num(4, 4), 4)
        self.assertEqual(module_0.choose_num(6, 6), 6)

    def test_y_odd_x_less_than_y_returns_y_minus_one(self):
        self.assertEqual(module_0.choose_num(12, 13), 12)
        self.assertEqual(module_0.choose_num(1, 3), 2)
        self.assertEqual(module_0.choose_num(10, 21), 20)

    def test_zero_boundary(self):
        self.assertEqual(module_0.choose_num(0, 0), 0)
        self.assertEqual(module_0.choose_num(0, 1), 0)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 23:40:18.341762
# Unit test for function choose_num
def test_choose_num():
    # x > y should return -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(100, 50) == -1

    # y is even -> return y
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(10, 20) == 20
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(3, 8) == 8
    assert module_0.choose_num(33, 34) == 34

    # x == y and y is odd -> return -1
    assert module_0.choose_num(11, 11) == -1
    assert module_0.choose_num(5, 5) == -1
    assert module_0.choose_num(33, 33) == -1

    # x == y and y is even -> return y
    assert module_0.choose_num(10, 10) == 10
    assert module_0.choose_num(0, 0) == 0

    # y is odd, x < y -> return y - 1
    assert module_0.choose_num(2, 7) == 6
    assert module_0.choose_num(1, 9) == 8
    assert module_0.choose_num(46, 49) == 48

    print("All tests passed!")


test_choose_num()

# Generated at 2026-11-02 23:41:38.454606
# Unit test for function choose_num
def test_choose_num():
    # Case 1: x > y -> no valid range
    assert module_0.choose_num(5, 3) == -1
    assert module_0.choose_num(10, 2) == -1

    # Case 2: y is even -> return y
    assert module_0.choose_num(1, 4) == 4
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(33, 12354) == 12354
    assert module_0.choose_num(0, 0) == 0

    # Case 3: x == y and y is odd -> no even number in range
    assert module_0.choose_num(3, 3) == -1
    assert module_0.choose_num(13, 13) == -1

    # Case 4: y is odd and x < y -> return y - 1 (largest even <= y)
    assert module_0.choose_num(1, 5) == 4
    assert module_0.choose_num(2, 7) == 6
    assert module_0.choose_num(547, 549) == 548

    # Edge cases: zero and negative numbers
    assert module_0.choose_num(-4, -4) == -4
    assert module_0.choose_num(-3, -3) == -1
    assert module_0.choose_num(-3, -2) == -2
    assert module_0.choose_num(-5, -3) == -4
    assert module_0.choose_num(-2, -3) == -1

    print("All tests passed!")

# nonce:b9290bf6

# Generated at 2026-11-02 23:42:43.111337
# Unit test for function choose_num
def test_choose_num():
    # x > y should return -1
    assert module_0.choose_num(12, 1) == -1
    assert module_0.choose_num(5, 4) == -1

    # y is even, return y
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(13, 12) == 12
    assert module_0.choose_num(2, 4) == 4

    # x == y and y is odd, return -1
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1

    # y is odd and x < y, return y - 1 (largest even in range)
    assert module_0.choose_num(12, 13) == 12
    assert module_0.choose_num(3, 5) == 4
    assert module_0.choose_num(10, 11) == 10

    # both equal and even, return y
    assert module_0.choose_num(6, 6) == 6

    print("All tests passed!")

test_choose_num()

# Generated at 2026-11-02 23:44:38.223513
# Unit test for function choose_num
def test_choose_num():
    # y is even, return y
    assert module_0.choose_num(12, 14) == 14
    assert module_0.choose_num(1, 4) == 4
    assert module_0.choose_num(0, 0) == 0
    assert module_0.choose_num(10, 10) == 10
    assert module_0.choose_num(-4, -2) == -2

    # y is odd, x < y, return y - 1
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(1, 3) == 2
    assert module_0.choose_num(33, 12353) == 12352
    assert module_0.choose_num(2, 5) == 4
    assert module_0.choose_num(-3, -1) == -2

    # x > y, return -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(5, 3) == -1
    assert module_0.choose_num(100, 99) == -1

    # x == y and y is odd, return -1
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(5, 5) == -1
    assert module_0.choose_num(7, 7) == -1

    # x == y and y is even, return y
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(0, 0) == 0

    # No even number in range at all
    assert module_0.choose_num(3, 3) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()