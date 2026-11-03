

# Generated at 2026-11-02 19:32:58.285991
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
    assert module_0.int_to_mini_roman(50) == 'l'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(100) == 'c'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'
    assert module_0.int_to_mini_roman(500) == 'd'
    assert module_0.int_to_mini_roman(900) == 'cm'
    assert module_0.int_to_mini_roman(1000) == 'm'
    assert module_0.int_to_mini_roman(1994) == 'mcmxciv'
    assert module_0.int_to_mini_roman(3519) == 'mmmdxix'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'
    print("All tests passed!")

test_int_to_mini_roman()

# Generated at 2026-11-02 19:35:08.103510
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic conversions
    assert module_0.int_to_mini_roman(1) == 'i'
    assert module_0.int_to_mini_roman(4) == 'iv'
    assert module_0.int_to_mini_roman(9) == 'ix'
    assert module_0.int_to_mini_roman(14) == 'xiv'
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(40) == 'xl'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(900) == 'cm'
    assert module_0.int_to_mini_roman(1000) == 'm'

    # Composite numbers
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'
    assert module_0.int_to_mini_roman(999) == 'cmxcix'
    assert module_0.int_to_mini_roman(1994) == 'mcmxciv'
    assert module_0.int_to_mini_roman(3999) == 'mcmxcix'

    # Repeated symbols
    assert module_0.int_to_mini_roman(3) == 'iii'
    assert module_0.int_to_mini_roman(3888) == 'mmmdccclxxxviii'

    # Upper boundary
    assert module_0.int_to_mini_roman(1000) == 'm'

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 19:36:56.033251
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single-symbol values
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(10) == "x"

    # Repetition of symbols
    assert module_0.int_to_mini_roman(2) == "ii"
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(20) == "xx"
    assert module_0.int_to_mini_roman(30) == "xxx"
    assert module_0.int_to_mini_roman(300) == "ccc"
    assert module_0.int_to_mini_roman(3000) == "mmm"

    # Subtractive combinations
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(900) == "cm"

    # Mixed values
    assert module_0.int_to_mini_roman(50) == "l"
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(1000) == "m"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(944) == "cmxliv"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"

    # Boundary values
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Output is always lowercase
    assert module_0.int_to_mini_roman(1990) == "mcmxc"
    assert module_0.int_to_mini_roman(1990) == module_0.int_to_mini_roman(1990).lower()

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 19:38:22.982937
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Single symbol values
    assert module_0.int_to_mini_roman(1) == 'i'
    assert module_0.int_to_mini_roman(5) == 'v'
    assert module_0.int_to_mini_roman(10) == 'x'
    assert module_0.int_to_mini_roman(50) == 'l'
    assert module_0.int_to_mini_roman(100) == 'c'
    assert module_0.int_to_mini_roman(500) == 'd'
    assert module_0.int_to_mini_roman(1000) == 'm'

    # Repetition of symbols
    assert module_0.int_to_mini_roman(2) == 'ii'
    assert module_0.int_to_mini_roman(3) == 'iii'
    assert module_0.int_to_mini_roman(20) == 'xx'
    assert module_0.int_to_mini_roman(30) == 'xxx'
    assert module_0.int_to_mini_roman(300) == 'ccc'
    assert module_0.int_to_mini_roman(3000) == 'mmm'

    # Subtractive notation cases
    assert module_0.int_to_mini_roman(4) == 'iv'
    assert module_0.int_to_mini_roman(9) == 'ix'
    assert module_0.int_to_mini_roman(40) == 'xl'
    assert module_0.int_to_mini_roman(90) == 'xc'
    assert module_0.int_to_mini_roman(400) == 'cd'
    assert module_0.int_to_mini_roman(900) == 'cm'

    # Mixed combinations
    assert module_0.int_to_mini_roman(6) == 'vi'
    assert module_0.int_to_mini_roman(7) == 'vii'
    assert module_0.int_to_mini_roman(8) == 'viii'
    assert module_0.int_to_mini_roman(11) == 'xi'
    assert module_0.int_to_mini_roman(14) == 'xiv'
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(35) == 'xxxv'
    assert module_0.int_to_mini_roman(42) == 'xlii'
    assert module_0.int_to_mini_roman(58) == 'lviii'
    assert module_0.int_to_mini_roman(94) == 'xciv'
    assert module_0.int_to_mini_roman(421) == 'cdxxi'
    assert module_0.int_to_mini_roman(999) == 'cmxcix'

    # Larger / well-known values
    assert module_0.int_to_mini_roman(1987) == 'mcmlxxxvii'
    assert module_0.int_to_mini_roman(2024) == 'mmxxiv'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'

    # Output must always be lowercase
    for n in range(1, 4000):
        r = module_0.int_to_mini_roman(n)
        assert r == r.lower(), f"Output for {n} is not lowercase: {r}"
        assert set(r) <= set('ivxlcdm'), f"Invalid characters for {n}: {r}"

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 19:39:43.500356
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
# nonce:ca96d207
    # Single symbol values
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
    assert module_0.int_to_mini_roman(2) == 'ii'
    assert module_0.int_to_mini_roman(3) == 'iii'
    assert module_0.int_to_mini_roman(6) == 'vi'
    assert module_0.int_to_mini_roman(14) == 'xiv'
    assert module_0.int_to_mini_roman(19) == 'xix'
    assert module_0.int_to_mini_roman(42) == 'xlii'
    assert module_0.int_to_mini_roman(79) == 'lxxix'
    assert module_0.int_to_mini_roman(152) == 'clii'
    assert module_0.int_to_mini_roman(354) == 'cccliv'
    assert module_0.int_to_mini_roman(426) == 'cdxxvi'
    assert module_0.int_to_mini_roman(999) == 'cmxcix'
    assert module_0.int_to_mini_roman(1994) == 'mcmxciv'
    assert module_0.int_to_mini_roman(2024) == 'mmxxiv'
    assert module_0.int_to_mini_roman(3999) == 'mmmcmxcix'

    # Results must be lowercase
    assert module_0.int_to_mini_roman(1000) == module_0.int_to_mini_roman(1000).lower()
    assert module_0.int_to_mini_roman(3888) == 'mmmdccclxxxviii'

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()

# Generated at 2026-11-02 19:41:51.221010
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic single symbols
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
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(42) == "xlii"
    assert module_0.int_to_mini_roman(152) == "clii"
    assert module_0.int_to_mini_roman(426) == "cdxxvi"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(2024) == "mmxxiv"
    assert module_0.int_to_mini_roman(3888) == "mmmdccclxxxviii"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

    # Output is lowercase
    assert module_0.int_to_mini_roman(426) == module_0.int_to_mini_roman(426).lower()
    assert module_0.int_to_mini_roman(426).islower()

    print("All tests passed!")


if __name__ == "__main__":
    test_int_to_mini_roman()