

# Generated at 2026-11-02 09:41:56.987997
# Unit test for function generate_integers
def test_generate_integers():
    # Both values within range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Partially out of range (clamped)
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 10) == [6, 8]
    assert module_0.generate_integers(0, 3) == [2]
    assert module_0.generate_integers(7, 20) == [8]

    # Entirely out of range
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(1, 1) == []

    # Equal values
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(8, 8) == [8]

    # Negative values
    assert module_0.generate_integers(-5, 3) == [2]
    assert module_0.generate_integers(-10, -1) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 09:43:13.888423
# Unit test for function generate_integers
def test_generate_integers():import unittest


class TestGenerateIntegers(unittest.TestCase):

    def test_basic_range(self):
        self.assertEqual(module_0.generate_integers(2, 8), [2, 4, 6, 8])

    def test_swapped_order(self):
        self.assertEqual(module_0.generate_integers(8, 2), [2, 4, 6, 8])

    def test_values_outside_bounds(self):
        self.assertEqual(module_0.generate_integers(1, 10), [2, 4, 6, 8])
        self.assertEqual(module_0.generate_integers(-5, 100), [2, 4, 6, 8])

    def test_narrow_range(self):
        self.assertEqual(module_0.generate_integers(3, 5), [4])
        self.assertEqual(module_0.generate_integers(5, 3), [4])

    def test_no_even_numbers(self):
        self.assertEqual(module_0.generate_integers(3, 3), [])
        self.assertEqual(module_0.generate_integers(9, 11), [])

    def test_single_even_value(self):
        self.assertEqual(module_0.generate_integers(4, 4), [4])

    def test_range_above_eight(self):
        self.assertEqual(module_0.generate_integers(9, 20), [])

    def test_negative_inputs(self):
        self.assertEqual(module_0.generate_integers(-10, -2), [])

    def test_mixed_negative_and_positive(self):
        self.assertEqual(module_0.generate_integers(-3, 4), [2, 4])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 09:44:28.296425
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case: full range within bounds
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]

    # Reversed arguments should give same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Range partially below lower clamp (2)
    assert module_0.generate_integers(1, 5) == [2, 4]

    # Range partially above upper clamp (8)
    assert module_0.generate_integers(7, 10) == [8]

    # Range entirely outside clamping bounds
    assert module_0.generate_integers(10, 14) == []

    assert module_0.generate_integers(0, 1) == []

    # Single value ranges
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(2, 2) == [2]

    # Single odd value yields empty list
    assert module_0.generate_integers(3, 3) == []

    # Reversed single value
    assert module_0.generate_integers(6, 6) == [6]

    # Both arguments below lower bound
    assert module_0.generate_integers(-5, 0) == []

    # Both arguments above upper bound
    assert module_0.generate_integers(9, 100) == []

    # Negative bounds clamped correctly
    assert module_0.generate_integers(-2, 3) == [2]

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 09:45:46.801828
# Unit test for function generate_integers
def test_generate_integers():
    # Basic cases: even numbers between a and b within [2, 8]
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Range entirely outside [2, 8] yields empty list
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(9, 9) == []

    # Lower bound clamped at 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]
    assert module_0.generate_integers(0, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(-3, 5) == [2, 4]

    # Upper bound clamped at 8
    assert module_0.generate_integers(7, 12) == [8]

    # Single-value ranges
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []  # odd value, no evens

    print("All tests passed!")

test_generate_integers()

# Generated at 2026-11-02 09:47:23.954243
# Unit test for function generate_integers
def test_generate_integers():
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(9, 20) == []
    assert module_0.generate_integers(0, 10) == [2, 4, 6, 8]