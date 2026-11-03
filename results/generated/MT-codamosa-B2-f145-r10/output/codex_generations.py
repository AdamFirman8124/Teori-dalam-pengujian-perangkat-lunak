

# Generated at 2026-11-03 00:18:12.329648
# Unit test for function order_by_points
def test_order_by_points():import unittest


class TestOrderByPoints(unittest.TestCase):

    def test_mixed_positive_negative(self):
        # keys: 1->1, 11->2, -1->-1, -11->0, -12->1
        self.assertEqual(module_0.order_by_points([1, 11, -1, -11, -12]),
                         [-1, -11, 1, -12, 11])

    def test_docstring_example(self):
        self.assertEqual(module_0.order_by_points([0, 6, 6, -76, -21, 23, 4]),
                         [-76, -21, 0, 4, 23, 6, 6])

    def test_duplicates_and_multidigit(self):
        # keys: 1234->10, 423->9, 463->13, 145->10, 2->2
        self.assertEqual(module_0.order_by_points([1234, 423, 463, 145, 2, 423, 423]),
                         [2, 423, 423, 423, 1234, 145, 463])

    def test_stability_for_equal_keys(self):
        # 56 and 65 both have digit sum 11; original order preserved
        self.assertEqual(module_0.order_by_points([65, 56, 11]), [11, 65, 56])

    def test_negative_first_digit_sign(self):
        # -76 -> (-7) + 6 = -1 ; -21 -> (-2) + 1 = -1
        self.assertEqual(module_0.order_by_points([-76, -21]), [-76, -21])

    def test_empty_list(self):
        self.assertEqual(module_0.order_by_points([]), [])

    def test_single_element(self):
        self.assertEqual(module_0.order_by_points([999]), [999])

    def test_all_negative(self):
        # keys: -10 -> -1, -20 -> -2, -3 -> -3
        self.assertEqual(module_0.order_by_points([-10, -20, -3]), [-3, -20, -10])

    def test_zero(self):
        self.assertEqual(module_0.order_by_points([0, 1, -1]), [-1, 0, 1])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 00:20:06.644867
# Unit test for function order_by_points
def test_order_by_points():
    # Classic example: digits_sum keys are [-1, 0, 1, 1, 2]
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Equal digit sums preserve original (stable) order
    assert module_0.order_by_points([123456, 654321]) == [123456, 654321]
    assert module_0.order_by_points([56, 65]) == [56, 65]

    # Empty and single-element lists
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([0]) == [0]

    # Negative first digit makes key negative
    assert module_0.order_by_points([0, 10, -10]) == [-10, 0, 10]
    assert module_0.order_by_points([-5, 5]) == [-5, 5]
    assert module_0.order_by_points([99, -99]) == [-99, 99]

    # Mixed values: keys are 3, 2, 4, -4
    assert module_0.order_by_points([12, -13, 4, -4]) == [-4, -13, 12, 4]

    # Multi-digit negatives: key(-21) = -2+1 = -1, key(-3) = -3
    assert module_0.order_by_points([-21, -3, 2]) == [-3, -21, 2]

# Generated at 2026-11-03 00:22:38.166516
# Unit test for function order_by_points
def test_order_by_points():
    # nonce:efdc525f
    # Basic sorting by digit sum
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert module_0.order_by_points([1234, 4231, 12, 1]) == [1, 12, 1234, 4231]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element and zero
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([5]) == [5]
    assert module_0.order_by_points([10, 0, 1]) == [0, 10, 1]

    # Negative numbers: first digit is negated in the sum
    assert module_0.order_by_points([-56, -65, 56, 65]) == [-65, -56, 56, 65]
    assert module_0.order_by_points([-99, 99, 0, -1]) == [-1, -99, 0, 99]

    # Ties preserve original order (stable sort)
    assert module_0.order_by_points([21, 12]) == [21, 12]
    assert module_0.order_by_points([111, 3, 30]) == [111, 3, 30]
    assert module_0.order_by_points([100, 10, 1000]) == [100, 10, 1000]

    # Already sorted input
    assert module_0.order_by_points([1, 2, 3]) == [1, 2, 3]

    # Reverse-sorted input
    assert module_0.order_by_points([30, 20, 10]) == [10, 20, 30]

    # Duplicates
    assert module_0.order_by_points([12, 12, 3]) == [3, 12, 12]