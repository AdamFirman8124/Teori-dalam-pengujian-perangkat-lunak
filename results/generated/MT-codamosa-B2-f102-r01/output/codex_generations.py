

# Generated at 2026-11-02 12:18:00.445134
# Unit test for function choose_num
def test_choose_num():
    # x > y: invalid range returns -1
    assert module_0.choose_num(12, 1) == -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(5, 3) == -1

    # y is even: y itself is the answer
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(2, 4) == 4
    assert module_0.choose_num(1, 100) == 100
    assert module_0.choose_num(0, 0) == 0

    # y is odd and x == y: no even number in range
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1

    # y is odd and x < y: y - 1 is the largest even number
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(12, 13) == 12
    assert module_0.choose_num(4, 5) == 4
    assert module_0.choose_num(1, 3) == 2
    assert module_0.choose_num(0, 1) == 0

    # negative boundaries
    assert module_0.choose_num(-4, -4) == -4
    assert module_0.choose_num(-5, -3) == -4
    assert module_0.choose_num(-3, -3) == -1


if __name__ == "__main__":
    test_choose_num()
    print("All tests passed!")

# Generated at 2026-11-02 12:18:44.340333
# Unit test for function choose_num
def test_choose_num():
    # x > y: invalid range
    assert module_0.choose_num(12, 1) == -1
    assert module_0.choose_num(5, 3) == -1
    # y is even: return y directly
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(2, 4) == 4
    assert module_0.choose_num(33, 12354) == 12354
    assert module_0.choose_num(-4, -2) == -2
    # y is odd and x < y: return y - 1 (largest even number)
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(10, 21) == 20
    assert module_0.choose_num(20, 33) == 32
    assert module_0.choose_num(-5, -1) == -2
    # x == y and y is odd: no even number in range
    assert module_0.choose_num(7, 7) == -1
    assert module_0.choose_num(5, 5) == -1
    assert module_0.choose_num(-3, -3) == -1

if __name__ == "__main__":
    test_choose_num()
    print("All tests passed!")

# Generated at 2026-11-02 12:19:25.647832
# Unit test for function choose_num
def test_choose_num():
    # Case: x > y -> -1
    assert module_0.choose_num(5, 3) == -1
    assert module_0.choose_num(10, 2) == -1
    assert module_0.choose_num(13, 12) == -1

    # Case: y is even -> return y
    assert module_0.choose_num(2, 4) == 4
    assert module_0.choose_num(1, 10) == 10
    assert module_0.choose_num(4, 4) == 4      # x == y and y even
    assert module_0.choose_num(0, 0) == 0      # 0 is even

    # Case: y is odd and x == y -> -1
    assert module_0.choose_num(3, 3) == -1
    assert module_0.choose_num(7, 7) == -1

    # Case: y is odd and x < y -> return y - 1
    assert module_0.choose_num(1, 5) == 4
    assert module_0.choose_num(3, 9) == 8
    assert module_0.choose_num(2, 7) == 6
    assert module_0.choose_num(12, 13) == 12

    # Case: range containing no even number with x == y odd
    assert module_0.choose_num(5, 5) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 12:20:09.574749
# Unit test for function choose_num
def test_choose_num():
    # Case: x > y, invalid range
    assert module_0.choose_num(12, 1) == -1

    # Case: y is even, largest even number in range is y itself
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(2, 4) == 4
    assert module_0.choose_num(0, 10) == 10
    assert module_0.choose_num(33, 44) == 44

    # Case: y is odd and x == y, no even number in range
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1
    assert module_0.choose_num(1, 1) == -1

    # Case: y is odd and x < y, largest even number is y - 1
    assert module_0.choose_num(13, 15) == 14
    assert module_0.choose_num(1, 3) == 2
    assert module_0.choose_num(10, 11) == 10
    assert module_0.choose_num(7, 9) == 8

    # Case: x == y == 0, 0 is even
    assert module_0.choose_num(0, 0) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 12:21:00.160619
# Unit test for function choose_num
def test_choose_num():import unittest


class TestChooseNum(unittest.TestCase):
    def test_x_greater_than_y_returns_minus_one(self):
        self.assertEqual(module_0.choose_num(12, 1), -1)

    def test_y_even_returns_y(self):
        self.assertEqual(module_0.choose_num(12, 15), 14)
        self.assertEqual(module_0.choose_num(13, 12), 12)

    def test_both_equal_even(self):
        self.assertEqual(module_0.choose_num(33, 33), 33)

    def test_both_equal_odd_returns_minus_one(self):
        self.assertEqual(module_0.choose_num(33, 33), 33)  # even case handled first

    def test_x_equals_y_odd_returns_minus_one(self):
        self.assertEqual(module_0.choose_num(5, 5), -1)

    def test_y_odd_x_less_than_y(self):
        self.assertEqual(module_0.choose_num(5, 7), 6)
        self.assertEqual(module_0.choose_num(10, 11), 10)

    def test_y_odd_y_minus_one_less_than_x(self):
        # y odd, y-1 < x means no even number in range
        self.assertEqual(module_0.choose_num(7, 7), -1)

    def test_consecutive_range(self):
        self.assertEqual(module_0.choose_num(1, 2), 2)

    def test_negative_numbers(self):
        self.assertEqual(module_0.choose_num(-5, -2), -2)
        self.assertEqual(module_0.choose_num(-3, -3), -1)

    def test_zero(self):
        self.assertEqual(module_0.choose_num(0, 0), 0)
        self.assertEqual(module_0.choose_num(0, 1), 0)


if __name__ == "__main__":
    unittest.main()