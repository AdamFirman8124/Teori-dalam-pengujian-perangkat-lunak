

# Generated at 2026-11-02 08:06:40.968884
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic values
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(10) == "x"
    assert module_0.int_to_mini_roman(50) == "l"
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(1000) == "m"

    # Subtractive notation cases
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(900) == "cm"

    # Combined values
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(94) == "xciv"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"

    # Edge cases
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Result must always be lowercase
    assert module_0.int_to_mini_roman(1987).islower()


test_int_to_mini_roman()

# Generated at 2026-11-02 08:08:43.928789
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():import unittest


def module_0.int_to_mini_roman(number):
    
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i] 
            div -= 1
        i -= 1
    return res.lower()


class TestIntToMiniRoman(unittest.TestCase):

    def test_single_digits(self):
        self.assertEqual(module_0.int_to_mini_roman(1), "i")
        self.assertEqual(module_0.int_to_mini_roman(2), "ii")
        self.assertEqual(module_0.int_to_mini_roman(3), "iii")
        self.assertEqual(module_0.int_to_mini_roman(4), "iv")
        self.assertEqual(module_0.int_to_mini_roman(5), "v")
        self.assertEqual(module_0.int_to_mini_roman(6), "vi")
        self.assertEqual(module_0.int_to_mini_roman(9), "ix")

    def test_tens(self):
        self.assertEqual(module_0.int_to_mini_roman(10), "x")
        self.assertEqual(module_0.int_to_mini_roman(14), "xiv")
        self.assertEqual(module_0.int_to_mini_roman(19), "xix")
        self.assertEqual(module_0.int_to_mini_roman(40), "xl")
        self.assertEqual(module_0.int_to_mini_roman(90), "xc")

    def test_hundreds(self):
        self.assertEqual(module_0.int_to_mini_roman(100), "c")
        self.assertEqual(module_0.int_to_mini_roman(400), "cd")
        self.assertEqual(module_0.int_to_mini_roman(500), "d")
        self.assertEqual(module_0.int_to_mini_roman(900), "cm")

    def test_thousands(self):
        self.assertEqual(module_0.int_to_mini_roman(1000), "m")
        self.assertEqual(module_0.int_to_mini_roman(2000), "mm")
        self.assertEqual(module_0.int_to_mini_roman(3000), "mmm")

    def test_complex_numbers(self):
        self.assertEqual(module_0.int_to_mini_roman(1994), "mcmxciv")
        self.assertEqual(module_0.int_to_mini_roman(3999), "mmmcmxcix")
        self.assertEqual(module_0.int_to_mini_roman(426), "cdxxvi")
        self.assertEqual(module_0.int_to_mini_roman(152), "clii")
        self.assertEqual(module_0.int_to_mini_roman(2020), "mmxx")
        self.assertEqual(module_0.int_to_mini_roman(354), "cccliv")
        self.assertEqual(module_0.int_to_mini_roman(914), "cmxiv")
        self.assertEqual(module_0.int_to_mini_roman(81), "lxxxi")
        self.assertEqual(module_0.int_to_mini_roman(789), "dcclxxxix")

    def test_output_is_lowercase(self):
        result = module_0.int_to_mini_roman(1234)
        self.assertEqual(result, result.lower())
        self.assertEqual(result, "mccxxxiv")

    def test_boundary_values(self):
        self.assertEqual(module_0.int_to_mini_roman(1), "i")
        self.assertEqual(module_0.int_to_mini_roman(999), "cmxcix")
        self.assertEqual(module_0.int_to_mini_roman(1001), "mi")
        self.assertEqual(module_0.int_to_mini_roman(3999), "mmmcmxcix")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 08:11:23.794702
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'
    assert module_0.int_to_mini_roman(1) == 'i'
    assert module_0.int_to_mini_roman(4) == 'iv'
    assert module_0.int_to_mini_roman(9) == 'ix'
    assert module_0.int_to_mini_roman(14) == 'xiv'
    assert module_0.int_to_mini_roman(40) == 'xl'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(900) == 'cm'
    assert module_0.int_to_mini_roman(1000) == 'm'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'
    assert module_0.int_to_mini_roman(354) == 'cccliv'
    assert module_0.int_to_mini_roman(100) == 'c'
    assert module_0.int_to_mini_roman(2494) == 'mmcdxciv'
    print("All tests passed!")

# Generated at 2026-11-02 08:12:35.679415
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Single digit values
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(9) == "ix"

    # Tens
    assert module_0.int_to_mini_roman(10) == "x"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(35) == "xxxv"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(99) == "xcix"

    # Hundreds
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(900) == "cm"

    # Thousands
    assert module_0.int_to_mini_roman(1000) == "m"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxii"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    print("All test cases passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 08:13:15.937248
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single symbols
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

    # Combinations
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(944) == "cmxliv"

    # Larger numbers
    assert module_0.int_to_mini_roman(999) == "cmxcix"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Output must always be lowercase
    assert module_0.int_to_mini_roman(3888) == module_0.int_to_mini_roman(3888).lower()
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()