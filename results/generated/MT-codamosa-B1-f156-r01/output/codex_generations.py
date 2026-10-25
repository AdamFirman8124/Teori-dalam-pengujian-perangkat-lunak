

# Generated at 2026-10-25 03:54:57.598814
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    test_cases = {
        0: "",
        1: "i",
        4: "iv",
        9: "ix",
        14: "xiv",
        40: "xl",
        49: "xlix",
        90: "xc",
        400: "cd",
        944: "cmxliv",
        1994: "mcmxciv",
        3999: "mmmcmxcix",
    }

    for number, expected in test_cases.items():
        assert module_0.int_to_mini_roman(number) == expected

# Generated at 2026-10-25 03:55:08.447547
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    test_cases = {
        0: "",
        1: "i",
        3: "iii",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m",
        58: "lviii",
        1994: "mcmxciv",
        3999: "mmmcmxcix",
    }

    for number, expected in test_cases.items():
        assert module_0.int_to_mini_roman(number) == expected

# Generated at 2026-10-25 03:55:14.386717
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    test_cases = {
        1: "i",
        3: "iii",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        49: "xlix",
        50: "l",
        90: "xc",
        99: "xcix",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1994: "mcmxciv",
        3999: "mmmcmxcix",
    }

    for number, expected in test_cases.items():
        assert module_0.int_to_mini_roman(number) == expected

# Generated at 2026-10-25 03:55:20.629658
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    test_cases = {
        0: "",
        1: "i",
        3: "iii",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m",
        1994: "mcmxciv",
        2024: "mmxxiv",
        3999: "mmmcmxcix",
    }

    for number, expected in test_cases.items():
        assert module_0.int_to_mini_roman(number) == expected

# Generated at 2026-10-25 03:55:23.046290
# Unit test for function int_to_mini_roman

# Generated at 2026-10-25 03:55:25.461727
# Unit test for function int_to_mini_roman

# Generated at 2026-10-25 03:55:27.883801
# Unit test for function int_to_mini_roman