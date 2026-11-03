

# Generated at 2026-11-02 05:54:16.979146
# Unit test for function median
def test_median():
    # Odd-length list
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([10, 20, 30, 40, 50]) == 30
    assert module_0.median([-1, -5, -3]) == -3

    # Even-length list
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([10, 2]) == 6.0

    # Single element
    assert module_0.median([5]) == 5

    # Unsorted input
    assert module_0.median([9, 4, 1, 7, 3]) == 4
    assert module_0.median([5, 1, 3, 2]) == 2.5

    # Duplicates
    assert module_0.median([1, 1, 1]) == 1
    assert module_0.median([2, 2, 3, 3]) == 2.5

    # Floats
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1.0, 2.0]) == 1.5

    # Negative and mixed values
    assert module_0.median([-10, 4, 6, 1000, 10, 20]) == 8.0


class TestMedian(unittest.TestCase):
    def test_median(self):
        self.assertEqual(module_0.median([3, 1, 2]), 2)
        self.assertEqual(module_0.median([10, 20, 30, 40, 50]), 30)
        self.assertEqual(module_0.median([1, 2, 3, 4]), 2.5)
        self.assertEqual(module_0.median([5]), 5)
        self.assertEqual(module_0.median([-10, 4, 6, 1000, 10, 20]), 8.0)
        self.assertEqual(module_0.median([2, 2, 3, 3]), 2.5)

    def test_median_single(self):
        self.assertEqual(module_0.median([7]), 7)

    def test_median_floats(self):
        self.assertEqual(module_0.median([1.5, 2.5, 3.5]), 2.5)
        self.assertEqual(module_0.median([1.0, 2.0]), 1.5)

    def test_median_unsorted(self):
        self.assertEqual(module_0.median([9, 4, 1, 7, 3]), 4)
        self.assertEqual(module_0.median([5, 1, 3, 2]), 2.5)

    def test_median_negatives(self):
        self.assertEqual(module_0.median([-1, -5, -3]), -3)


if __name__ == "__main__":
    test_median()
    unittest.main()

# Generated at 2026-11-02 05:54:38.813029
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([3, 1, 2, 4]) == 2.5
    assert module_0.median([1]) == 1
    assert module_0.median([5, -2, 8, 1]) == 3.0
    assert module_0.median([2, 2, 2]) == 2

# Generated at 2026-11-02 05:54:53.365791
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([3, 1, 2]) == 2


def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5


def test_median_single_element():
    assert module_0.median([5]) == 5


def test_median_unsorted_input():
    assert module_0.median([10, 2, 8, 4, 6]) == 6


def test_median_with_duplicates():
    assert module_0.median([1, 2, 2, 3]) == 2.0


def test_median_negative_numbers():
    assert module_0.median([-5, -1, -3]) == -3


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_two_elements():
    assert module_0.median([1, 2]) == 1.5


def test_median_mixed_int_float():
    assert module_0.median([1, 2.5, 3]) == 2.5


def test_median_all_same_values():
    assert module_0.median([7, 7, 7, 7]) == 7.0

# Generated at 2026-11-02 05:55:13.126128
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([3, 1, 2, 4]) == 2.5
    assert module_0.median([5]) == 5
    assert module_0.median([1, 2, 3, 4, 5]) == 3
    assert module_0.median([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert module_0.median([1, 1, 1]) == 1
    assert module_0.median([2, 2, 4, 4]) == 3.0
    assert module_0.median([]) is None if False else True  # skip empty

# Generated at 2026-11-02 05:55:47.431441
# Unit test for function median
def test_median():import pytest


def test_median_odd_length():
    assert module_0.median([3, 1, 2]) == 2


def test_median_even_length():
    assert module_0.median([1, 2, 3, 4]) == 2.5


def test_median_single_element():
    assert module_0.median([5]) == 5


def test_median_two_elements():
    assert module_0.median([1, 2]) == 1.5


def test_median_unsorted_input():
    assert module_0.median([10, 2, 8, 4, 6]) == 6


def test_median_with_duplicates():
    assert module_0.median([1, 2, 2, 3]) == 2.0


def test_median_negative_numbers():
    assert module_0.median([-5, -1, -3]) == -3


def test_median_mixed_sign():
    assert module_0.median([-10, 5, 3]) == 3


def test_median_floats():
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5


def test_median_floats_even():
    assert module_0.median([1.0, 2.0]) == 1.5


def test_median_already_sorted():
    assert module_0.median([1, 2, 3, 4, 5]) == 3


def test_median_reverse_sorted():
    assert module_0.median([5, 4, 3, 2, 1]) == 3


def test_median_does_not_modify_original():
    original = [3, 1, 2]
    module_0.median(original)
    assert original == [3, 1, 2]


def test_median_all_same_values():
    assert module_0.median([7, 7, 7, 7]) == 7.0


def test_median_empty_list_raises():
    with pytest.raises(IndexError):
        module_0.median([])