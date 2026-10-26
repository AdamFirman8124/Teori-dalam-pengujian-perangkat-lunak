

# Generated at 2026-10-25 12:34:16.404298
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:34:31.080005
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dict -> False
    assert module_0.check_dict_case({}) == False

    # Single lowercase key -> True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key -> True
    assert module_0.check_dict_case({"A": 1}) == True

    # All keys uppercase -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # All keys lowercase -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # Mixed upper/lower keys -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2, "C": 3}) == False

    # Non-string key -> False
    assert module_0.check_dict_case({1: "a", "b": 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: "b"}) == False

    # Title-case / mixed-case string keys (neither isupper nor islower) -> False
    assert module_0.check_dict_case({"Hello": 1}) == False
    assert module_0.check_dict_case({"aBc": 1}) == False

    # Keys with no cased characters -> False
    assert module_0.check_dict_case({"1": 1}) == False

    # Lowercase keys including digits/digits appended -> True
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True

    # Uppercase keys including punctuation -> True
    assert module_0.check_dict_case({"A1": 1, "B2": 2}) == True

    # First key determines state; a later non-matching key -> False
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) == False

    # Uppercase then lowercase only after break is irrelevant: order matters
    assert module_0.check_dict_case({"A": 1, "B": 2, "c": 3}) == False

# Generated at 2026-10-25 12:34:49.419819
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:34:52.057342
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:34:54.474494
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:34:57.051781
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:34:59.476056
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:35:02.087173
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:35:04.497186
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:35:06.912043
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:35:09.325169
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:35:11.739108
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:35:14.215142
# Unit test for function check_dict_case

# Generated at 2026-10-25 12:35:16.603280
# Unit test for function check_dict_case