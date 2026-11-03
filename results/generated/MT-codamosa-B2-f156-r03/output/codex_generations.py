

# Generated at 2026-11-02 20:52:59.995754
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single symbol values
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

    # Multi-symbol combinations
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(354) == "cccliv"
    assert module_0.int_to_mini_roman(1918) == "mcmxviii"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"

    # Boundary values
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"

    # Result is always lowercase
    result = module_0.int_to_mini_roman(2024)
    assert result == result.lower()

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 20:53:41.997574
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

    # Subtractive combinations
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(900) == "cm"

    # Mixed numbers
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(421) == "cdxxi"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Edge cases
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(6) == "vi"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"

    # Output must be lowercase
    assert module_0.int_to_mini_roman(1000).islower()

    print("All tests passed!")

# Generated at 2026-11-02 20:54:39.348423
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

    # Repeated symbols
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(30) == "xxx"
    assert module_0.int_to_mini_roman(3000) == "mmm"

    # Mixed values
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"

    # Boundary values
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"

    print("All tests passed!")


test_int_to_mini_roman()

# Generated at 2026-11-02 20:55:28.101259
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

    # Composite numbers
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(42) == "xlii"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"

    # Boundary / extremes
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"

    # Result is always lowercase
    for n in range(1, 4000):
        result = module_0.int_to_mini_roman(n)
        assert result == result.lower()
        assert result.islower() or result == ""

    # Round-trip sanity: lengths grow non-trivially with value
    assert len(module_0.int_to_mini_roman(1000)) < len(module_0.int_to_mini_roman(3999))

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 20:56:08.937145
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

    # Repeated symbols
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(20) == "xx"
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(2000) == "mm"

    # Compound values
    assert module_0.int_to_mini_roman(6) == "vi"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(42) == "xlii"
    assert module_0.int_to_mini_roman(99) == "xcix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(949) == "cmxlix"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Verify output is lowercase
    result = module_0.int_to_mini_roman(1666)
    assert result == result.lower()
    assert result == "mdclxvi"

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 20:56:51.072966
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    assert module_0.int_to_mini_roman(1) == 'i'
    assert module_0.int_to_mini_roman(4) == 'iv'
    assert module_0.int_to_mini_roman(5) == 'v'
    assert module_0.int_to_mini_roman(9) == 'ix'
    assert module_0.int_to_mini_roman(10) == 'x'
    assert module_0.int_to_mini_roman(14) == 'xiv'
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(40) == 'xl'
    assert module_0.int_to_mini_roman(58) == 'lviii'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(421) == 'cdxxi'
    assert module_0.int_to_mini_roman(900) == 'cm'
    assert module_0.int_to_mini_roman(1000) == 'm'
    assert module_0.int_to_mini_roman(1976) == 'mcmlxxvi'
    assert module_0.int_to_mini_roman(2024) == 'mmxxiv'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'
    assert module_0.int_to_mini_roman(3) == 'iii'
    assert module_0.int_to_mini_roman(3888) == 'mmmdccclxxxviii'

test_int_to_mini_roman()

# Generated at 2026-11-02 20:57:58.286440
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

    # Subtractive notation values
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(900) == "cm"

    # Repeated symbols
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(30) == "xxx"
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(3000) == "mmm"

    # Composite numbers
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(888) == "dcclxxxviii"
    assert module_0.int_to_mini_roman(1666) == "mdclxvi"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(2444) == "mmcdxliv"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"

    # Output must be lowercase
    result = module_0.int_to_mini_roman(1234)
    assert result == "mccxxxiv"
    assert result == result.lower()

    print("All tests passed!")

# Generated at 2026-11-02 20:59:45.286814
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single-symbol values
    assert module_0.int_to_mini_roman(1) == 'i'
    assert module_0.int_to_mini_roman(5) == 'v'
    assert module_0.int_to_mini_roman(10) == 'x'
    assert module_0.int_to_mini_roman(50) == 'l'
    assert module_0.int_to_mini_roman(100) == 'c'
    assert module_0.int_to_mini_roman(500) == 'd'
    assert module_0.int_to_mini_roman(1000) == 'm'

    # Subtractive notation values
    assert module_0.int_to_mini_roman(4) == 'iv'
    assert module_0.int_to_mini_roman(9) == 'ix'
    assert module_0.int_to_mini_roman(40) == 'xl'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(900) == 'cm'

    # Mixed combinations
    assert module_0.int_to_mini_roman(3) == 'iii'
    assert module_0.int_to_mini_roman(14) == 'xiv'
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'
    assert module_0.int_to_mini_roman(1994) == 'mcmxciv'
    assert module_0.int_to_mini_roman(2023) == 'mmxxiii'
    assert module_0.int_to_mini_roman(3549) == 'mmmdxlix'

    # Boundary values
    assert module_0.int_to_mini_roman(3888) == 'mmmdccclxxxviii'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'

    print("All tests passed!")


test_int_to_mini_roman()

# Generated at 2026-11-02 21:00:07.764999
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic cases
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'

    # Smallest and largest valid inputs
    assert module_0.int_to_mini_roman(1) == 'i'
    assert module_0.int_to_mini_roman(1000) == 'm'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'

    # Subtractive notation cases
    assert module_0.int_to_mini_roman(4) == 'iv'
    assert module_0.int_to_mini_roman(9) == 'ix'
    assert module_0.int_to_mini_roman(14) == 'xiv'
    assert module_0.int_to_mini_roman(40) == 'xl'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(500) == 'd'
    assert module_0.int_to_mini_roman(900) == 'cm'

    # Repetition cases
    assert module_0.int_to_mini_roman(3) == 'iii'
    assert module_0.int_to_mini_roman(30) == 'xxx'
    assert module_0.int_to_mini_roman(300) == 'ccc'
    assert module_0.int_to_mini_roman(3888) == 'mmmdccclxxxviii'

    # Mixed composite cases
    assert module_0.int_to_mini_roman(58) == 'lviii'
    assert module_0.int_to_mini_roman(1994) == 'mcmxciv'
    assert module_0.int_to_mini_roman(2024) == 'mmxxiv'

    # Result is always lowercase
    for n in range(1, 1000):
        r = module_0.int_to_mini_roman(n)
        assert r == r.lower()
        assert r == r.lower()

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()
# nonce:4735710d

# Generated at 2026-11-02 21:00:30.400729
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(10) == "x"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(50) == "l"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(900) == "cm"
    assert module_0.int_to_mini_roman(1000) == "m"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"
    print("All tests passed!")

test_int_to_mini_roman()

# Generated at 2026-11-02 21:00:46.472956
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single symbol values
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

    # Composite numbers
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(66) == "lxvi"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(354) == "cccliv"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(1987) == "mcmlxxxvii"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"

    # Boundary values
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 21:01:23.592485
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single symbols
    assert module_0.int_to_mini_roman(1) == 'i'
    assert module_0.int_to_mini_roman(5) == 'v'
    assert module_0.int_to_mini_roman(10) == 'x'
    assert module_0.int_to_mini_roman(50) == 'l'
    assert module_0.int_to_mini_roman(100) == 'c'
    assert module_0.int_to_mini_roman(500) == 'd'
    assert module_0.int_to_mini_roman(1000) == 'm'

    # Subtractive combinations
    assert module_0.int_to_mini_roman(4) == 'iv'
    assert module_0.int_to_mini_roman(9) == 'ix'
    assert module_0.int_to_mini_roman(40) == 'xl'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(900) == 'cm'

    # Repeated symbols
    assert module_0.int_to_mini_roman(2) == 'ii'
    assert module_0.int_to_mini_roman(3) == 'iii'
    assert module_0.int_to_mini_roman(20) == 'xx'
    assert module_0.int_to_mini_roman(30) == 'xxx'
    assert module_0.int_to_mini_roman(3000) == 'mmm'

    # Mixed numbers
    assert module_0.int_to_mini_roman(14) == 'xiv'
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(58) == 'lviii'
    assert module_0.int_to_mini_roman(1994) == 'mcmxciv'
    assert module_0.int_to_mini_roman(2020) == 'mmxx'
    assert module_0.int_to_mini_roman(354) == 'cccliv'
    assert module_0.int_to_mini_roman(4267) == 'mmcdlxvii'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'

# Generated at 2026-11-02 21:01:46.571839
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single-symbol cases
    assert module_0.int_to_mini_roman(1) == "i"
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

    # Multi-symbol combinations
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(354) == "cccliv"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"

    # Boundary values
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"

    print("All tests passed!")


test_int_to_mini_roman()

# Generated at 2026-11-02 21:02:18.857871
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single symbol values
    assert module_0.int_to_mini_roman(1) == "i"
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

    # Repetition cases
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(20) == "xx"
    assert module_0.int_to_mini_roman(30) == "xxx"
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(3000) == "mmm"

    # Mixed/composite numbers
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"

    # Edge cases: upper and lower bounds
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    print("All tests passed!")


test_int_to_mini_roman()