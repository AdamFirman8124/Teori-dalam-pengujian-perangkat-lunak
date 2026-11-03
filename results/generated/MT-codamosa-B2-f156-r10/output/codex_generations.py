

# Generated at 2026-11-03 02:16:12.123132
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Single symbol values
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

    # Composite values
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(80) == "lxxx"
    assert module_0.int_to_mini_roman(94) == "xciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Repetition of symbols
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(30) == "xxx"
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(3000) == "mmm"

    # Edge: smallest valid input
    assert module_0.int_to_mini_roman(1) == "i"

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-03 02:17:44.796003
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Single symbol values
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

    # Simple combinations
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(6) == "vi"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(26) == "xxvi"
    assert module_0.int_to_mini_roman(99) == "xcix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"

    # Larger numbers
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Results must be lowercase
    assert module_0.int_to_mini_roman(1000) == module_0.int_to_mini_roman(1000).lower()
    assert module_0.int_to_mini_roman(900) == "cm"
    assert module_0.int_to_mini_roman(900) != "CM"

    # Edge case: smallest valid input
    assert module_0.int_to_mini_roman(1) == "i"

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-03 02:19:16.752507
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

    # Subtractive combinations
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(900) == "cm"

    # Repeated symbols
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(20) == "xx"
    assert module_0.int_to_mini_roman(30) == "xxx"
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(3000) == "mmm"

    # Mixed values
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(354) == "cccliv"

    # Boundary values
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-03 02:21:36.938583
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(10) == "x"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(50) == "l"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(900) == "cm"
    assert module_0.int_to_mini_roman(1000) == "m"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"

# Generated at 2026-11-03 02:24:23.649707
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

    def test_single_digit_values(self):
        self.assertEqual(module_0.int_to_mini_roman(1), 'i')
        self.assertEqual(module_0.int_to_mini_roman(5), 'v')
        self.assertEqual(module_0.int_to_mini_roman(10), 'x')
        self.assertEqual(module_0.int_to_mini_roman(50), 'l')
        self.assertEqual(module_0.int_to_mini_roman(100), 'c')
        self.assertEqual(module_0.int_to_mini_roman(500), 'd')
        self.assertEqual(module_0.int_to_mini_roman(1000), 'm')

    def test_subtractive_pairs(self):
        self.assertEqual(module_0.int_to_mini_roman(4), 'iv')
        self.assertEqual(module_0.int_to_mini_roman(9), 'ix')
        self.assertEqual(module_0.int_to_mini_roman(40), 'xl')
        self.assertEqual(module_0.int_to_mini_roman(90), 'xc')
        self.assertEqual(module_0.int_to_mini_roman(400), 'cd')
        self.assertEqual(module_0.int_to_mini_roman(900), 'cm')

    def test_simple_combinations(self):
        self.assertEqual(module_0.int_to_mini_roman(2), 'ii')
        self.assertEqual(module_0.int_to_mini_roman(3), 'iii')
        self.assertEqual(module_0.int_to_mini_roman(6), 'vi')
        self.assertEqual(module_0.int_to_mini_roman(7), 'vii')
        self.assertEqual(module_0.int_to_mini_roman(8), 'viii')
        self.assertEqual(module_0.int_to_mini_roman(11), 'xi')
        self.assertEqual(module_0.int_to_mini_roman(14), 'xiv')
        self.assertEqual(module_0.int_to_mini_roman(19), 'xix')

    def test_known_examples(self):
        self.assertEqual(module_0.int_to_mini_roman(19), 'xix')
        self.assertEqual(module_0.int_to_mini_roman(152), 'clii')
        self.assertEqual(module_0.int_to_mini_roman(426), 'cdxxvi')
        self.assertEqual(module_0.int_to_mini_roman(1520), 'mdxx')

    def test_boundary_values(self):
        self.assertEqual(module_0.int_to_mini_roman(3999), 'mmmcmxcix')
        self.assertEqual(module_0.int_to_mini_roman(1000), 'm')
        self.assertEqual(module_0.int_to_mini_roman(999), 'cmxcix')
        self.assertEqual(module_0.int_to_mini_roman(99), 'xcix')

    def test_repeated_symbols(self):
        self.assertEqual(module_0.int_to_mini_roman(300), 'ccc')
        self.assertEqual(module_0.int_to_mini_roman(2000), 'mm')
        self.assertEqual(module_0.int_to_mini_roman(3888), 'mmmdccclxxxviii')

    def test_mixed_number(self):
        self.assertEqual(module_0.int_to_mini_roman(1994), 'mcmxciv')
        self.assertEqual(module_0.int_to_mini_roman(2024), 'mmxxiv')
        self.assertEqual(module_0.int_to_mini_roman(3549), 'mmmdxlix')

    def test_result_is_lowercase(self):
        result = module_0.int_to_mini_roman(1234)
        self.assertEqual(result, result.lower())
        self.assertEqual(result, 'mccxxxiv')


if __name__ == '__main__':
    unittest.main()