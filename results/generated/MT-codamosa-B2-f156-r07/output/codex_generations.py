

# Generated at 2026-11-02 11:18:54.798428
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(10) == "x"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(50) == "l"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(900) == "cm"
    assert module_0.int_to_mini_roman(1000) == "m"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(8) == "viii"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(42) == "xlii"
    assert module_0.int_to_mini_roman(87) == "lxxxvii"
    assert module_0.int_to_mini_roman(99) == "xcix"
    assert module_0.int_to_mini_roman(145) == "cxlv"
    assert module_0.int_to_mini_roman(421) == "cdxxi"
    assert module_0.int_to_mini_roman(1946) == "mcmxlvi"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 11:20:27.573377
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single-symbol values
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(10) == "x"
    assert module_0.int_to_mini_roman(50) == "l"
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(1000) == "m"

    # Subtractive pairs
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(900) == "cm"

    # Common examples
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(21) == "xxi"
    assert module_0.int_to_mini_roman(354) == "cccliv"
    assert module_0.int_to_mini_roman(99) == "xcix"
    assert module_0.int_to_mini_roman(999) == "cmxcix"
    assert module_0.int_to_mini_roman(1900) == "mcm"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"

    # Maximum standard value
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Round-trip sanity: length and character checks
    result = module_0.int_to_mini_roman(1234)
    assert result == "mccxxxiv"
    assert result.islower()

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 11:21:58.057448
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic values
    assert module_0.int_to_mini_roman(1) == 'i'
    assert module_0.int_to_mini_roman(4) == 'iv'
    assert module_0.int_to_mini_roman(5) == 'v'
    assert module_0.int_to_mini_roman(9) == 'ix'
    assert module_0.int_to_mini_roman(10) == 'x'
    assert module_0.int_to_mini_roman(40) == 'xl'
    assert module_0.int_to_mini_roman(50) == 'l'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(100) == 'c'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(500) == 'd'
    assert module_0.int_to_mini_roman(900) == 'cm'
    assert module_0.int_to_mini_roman(1000) == 'm'

    # Composite values
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'
    assert module_0.int_to_mini_roman(58) == 'lviii'
    assert module_0.int_to_mini_roman(1994) == 'mcmxciv'

    # Boundary values
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'
    assert module_0.int_to_mini_roman(2023) == 'mmxxii'

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 11:25:12.470955
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():import unittest


class TestIntToMiniRoman(unittest.TestCase):

    def test_single_values(self):
        self.assertEqual(module_0.int_to_mini_roman(1), "i")
        self.assertEqual(module_0.int_to_mini_roman(4), "iv")
        self.assertEqual(module_0.int_to_mini_roman(5), "v")
        self.assertEqual(module_0.int_to_mini_roman(9), "ix")
        self.assertEqual(module_0.int_to_mini_roman(10), "x")
        self.assertEqual(module_0.int_to_mini_roman(40), "xl")
        self.assertEqual(module_0.int_to_mini_roman(50), "l")
        self.assertEqual(module_0.int_to_mini_roman(90), "xc")
        self.assertEqual(module_0.int_to_mini_roman(100), "c")
        self.assertEqual(module_0.int_to_mini_roman(400), "cd")
        self.assertEqual(module_0.int_to_mini_roman(500), "d")
        self.assertEqual(module_0.int_to_mini_roman(900), "cm")
        self.assertEqual(module_0.int_to_mini_roman(1000), "m")

    def test_composite_numbers(self):
        self.assertEqual(module_0.int_to_mini_roman(19), "xix")
        self.assertEqual(module_0.int_to_mini_roman(152), "clii")
        self.assertEqual(module_0.int_to_mini_roman(426), "cdxxvi")
        self.assertEqual(module_0.int_to_mini_roman(2024), "mmxxiv")
        self.assertEqual(module_0.int_to_mini_roman(3999), "mmmcmxcix")

    def test_output_is_lowercase(self):
        result = module_0.int_to_mini_roman(1234)
        self.assertEqual(result, result.lower())

    def test_repeated_symbols(self):
        self.assertEqual(module_0.int_to_mini_roman(3), "iii")
        self.assertEqual(module_0.int_to_mini_roman(30), "xxx")
        self.assertEqual(module_0.int_to_mini_roman(300), "ccc")
        self.assertEqual(module_0.int_to_mini_roman(3000), "mmm")

    def test_mixed_composition(self):
        self.assertEqual(module_0.int_to_mini_roman(1994), "mcmxciv")
        self.assertEqual(module_0.int_to_mini_roman(3888), "mmmdccclxxxviii")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 11:27:21.521365
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Single symbols
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(10) == "x"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(50) == "l"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(900) == "cm"
    assert module_0.int_to_mini_roman(1000) == "m"

    # Repeated symbols
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(20) == "xx"
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(2000) == "mm"

    # Composite numbers
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(42) == "xlii"
    assert module_0.int_to_mini_roman(79) == "lxxix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(944) == "cmxliv"
    assert module_0.int_to_mini_roman(1666) == "mdclxvi"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Edge cases
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(58) == "lviii"

    # Verify output is always lowercase
    for n in range(1, 4000):
        result = module_0.int_to_mini_roman(n)
        assert result == result.lower()
        assert len(result) > 0

    print("All tests passed!")