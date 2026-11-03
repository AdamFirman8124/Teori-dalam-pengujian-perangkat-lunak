

# Generated at 2026-11-01 20:31:09.596091
# Unit test for function generate_integers
def test_generate_integers():
    # Basic range with all even numbers
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Argument order shouldn't matter
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Values clamped to lower bound of 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(0, 5) == [2, 4]
    assert module_0.generate_integers(-3, 5) == [2, 4]
    # Values clamped to upper bound of 8
    assert module_0.generate_integers(6, 20) == [6, 8]
    assert module_0.generate_integers(0, 20) == [2, 4, 6, 8]
    # Range entirely outside [2, 8] yields empty list
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(-5, 1) == []
    # Single-value ranges
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(6, 6) == [6]
    assert module_0.generate_integers(7, 7) == []
    assert module_0.generate_integers(9, 9) == []
    # Odd-only ranges yield empty lists
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(5, 5) == []
    # Mixed ranges with partial even numbers
    assert module_0.generate_integers(3, 4) == [4]
    assert module_0.generate_integers(4, 7) == [4, 6]
    assert module_0.generate_integers(5, 8) == [6, 8]
    # Reversed mixed range
    assert module_0.generate_integers(7, 4) == [4, 6]
    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-01 20:31:25.915373
# Unit test for function generate_integers
def test_generate_integers():import unittest


class TestGenerateIntegers(unittest.TestCase):

    def test_basic_range(self):
        self.assertEqual(module_0.generate_integers(2, 8), [2, 4, 6, 8])

    def test_reversed_args(self):
        self.assertEqual(module_0.generate_integers(8, 2), [2, 4, 6, 8])

    def test_partial_range(self):
        self.assertEqual(module_0.generate_integers(1, 5), [2, 4])

    def test_clamped_upper(self):
        self.assertEqual(module_0.generate_integers(3, 12), [4, 6, 8])

    def test_clamped_lower(self):
        self.assertEqual(module_0.generate_integers(-5, 7), [2, 4, 6])

    def test_no_even_numbers(self):
        self.assertEqual(module_0.generate_integers(3, 3), [])

    def test_single_value(self):
        self.assertEqual(module_0.generate_integers(4, 4), [4])

    def test_out_of_range_high(self):
        self.assertEqual(module_0.generate_integers(10, 20), [])

    def test_negative_inputs(self):
        self.assertEqual(module_0.generate_integers(-10, -2), [])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 20:31:40.213163
# Unit test for function generate_integers
def test_generate_integers():
    # Both bounds within [2, 8]
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Arguments in reverse order should give same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Range clipped to lower bound of 2
    assert module_0.generate_integers(1, 3) == [2]
    # Range clipped to upper bound of 8
    assert module_0.generate_integers(0, 20) == [2, 4, 6, 8]
    # Range entirely above 8 -> empty
    assert module_0.generate_integers(10, 14) == []
    # Partial overlap: only even numbers in [3, 7]
    assert module_0.generate_integers(3, 7) == [4, 6]
    # Single value, odd -> empty
    assert module_0.generate_integers(5, 5) == []
    # Single value, even -> single element
    assert module_0.generate_integers(6, 6) == [6]
    # Negative and large bounds
    assert module_0.generate_integers(-5, 100) == [2, 4, 6, 8]

# Generated at 2026-11-01 20:32:01.717893
# Unit test for function generate_integers
def test_generate_integers():
    # nonce:48453666
    # Both values within [2, 8]
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]  # argument order irrelevant

    # Partial overlap with [2, 8]
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 9) == [6, 8]
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(9, 5) == [6, 8]
    assert module_0.generate_integers(5, 1) == [2, 4]

    # Single-value ranges
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(6, 6) == [6]
    assert module_0.generate_integers(3, 3) == []  # odd value yields nothing

    # Ranges entirely outside [2, 8]
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(9, 20) == []
    assert module_0.generate_integers(-5, 1) == []
    assert module_0.generate_integers(-4, -2) == []

    # Clamping at boundaries
    assert module_0.generate_integers(0, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(-10, 100) == [2, 4, 6, 8]
    assert module_0.generate_integers(-2, 3) == [2]

# Generated at 2026-11-01 20:32:34.197406
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case: both values within range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Order of arguments should not matter
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Range clamped at 2 on the low end
    assert module_0.generate_integers(1, 5) == [2, 4]
    # Range clamped at 8 on the high end
    assert module_0.generate_integers(6, 20) == [6, 8]
    # Both bounds outside [2, 8] -> empty list
    assert module_0.generate_integers(10, 14) == []
    # Single value range where value is even
    assert module_0.generate_integers(2, 2) == [2]
    # Single value range where value is odd
    assert module_0.generate_integers(3, 3) == []
    # No even numbers in the effective range
    assert module_0.generate_integers(5, 5) == []
    # Negative inputs clamp to lower bound 2
    assert module_0.generate_integers(-5, 4) == [2, 4]
    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()