

# Generated at 2026-11-02 11:57:24.927197
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

    # Standard examples
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Repetition of symbols
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"

    print("All tests passed!")


test_int_to_mini_roman()

# Generated at 2026-11-02 12:00:12.652325
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

    # Multi-symbol numbers
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(38) == "xxxviii"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Edge case: smallest valid input
    assert module_0.int_to_mini_roman(1) == "i"

    # Repeated symbols
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(2000) == "mm"

    print("All tests passed!")


test_int_to_mini_roman()

# Generated at 2026-11-02 12:02:52.098716
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

    # Subtractive notation cases
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(900) == "cm"

    # Composite numbers
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"
    assert module_0.int_to_mini_roman(3549) == "mmmdxlix"

    # Repeated symbol cases
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(20) == "xx"
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(3000) == "mmm"

    # Edge case: zero yields empty string
    assert module_0.int_to_mini_roman(0) == ""

    # Result is always lowercase
    assert module_0.int_to_mini_roman(1994) == module_0.int_to_mini_roman(1994).lower()
    assert module_0.int_to_mini_roman(1234) == "mccxxxiv"

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 12:04:45.035152
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
    assert module_0.int_to_mini_roman(3) == 'iii'
    assert module_0.int_to_mini_roman(20) == 'xx'
    assert module_0.int_to_mini_roman(300) == 'ccc'
    assert module_0.int_to_mini_roman(2000) == 'mm'

    # Mixed numbers
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'
    assert module_0.int_to_mini_roman(354) == 'cccliv'
    assert module_0.int_to_mini_roman(421) == 'cdxxi'
    assert module_0.int_to_mini_roman(1987) == 'mcmlxxxvii'
    assert module_0.int_to_mini_roman(2023) == 'mmxxiii'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'

    # Boundary values
    assert module_0.int_to_mini_roman(3888) == 'mmmdccclxxxviii'
    assert module_0.int_to_mini_roman(999) == 'cmxcix'

    print("All tests passed!")


test_int_to_mini_roman()

# Generated at 2026-11-02 12:05:30.997783
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

    # Mixed values
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'
    assert module_0.int_to_mini_roman(58) == 'lviii'
    assert module_0.int_to_mini_roman(1994) == 'mcmxciv'
    assert module_0.int_to_mini_roman(2023) == 'mmxxiii'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'
    assert module_0.int_to_mini_roman(3549) == 'mmmdxlix'

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()