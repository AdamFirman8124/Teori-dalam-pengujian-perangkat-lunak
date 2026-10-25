

# Generated at 2026-10-24 21:19:46.958403
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    assert module_0.int_to_mini_roman(0) == ""
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(58) == "lviii"
    assert module_0.int_to_mini_roman(944) == "cmxliv"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"
    assert module_0.int_to_mini_roman(3999) == "mmmcmxcix"

# Generated at 2026-10-24 21:19:54.126704
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

# Generated at 2026-10-24 21:19:56.751900
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 21:19:59.168437
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 21:20:01.584964
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 21:20:04.003820
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 21:20:06.420053
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 21:20:08.839793
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 21:20:11.261993
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 21:20:13.677029
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 21:20:16.094508
# Unit test for function int_to_mini_roman