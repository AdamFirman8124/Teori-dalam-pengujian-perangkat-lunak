

# Generated at 2026-10-24 07:17:23.188187
# Unit test for function check_dict_case
def test_check_dict_case():
    assert module_0.check_dict_case({"a": 1, "b": 2}) is True
    assert module_0.check_dict_case({"A": 1, "B": 2}) is True
    assert module_0.check_dict_case({"a": 1, "B": 2}) is False
    assert module_0.check_dict_case({"A": 1, "b": 2}) is False
    assert module_0.check_dict_case({}) is False
    assert module_0.check_dict_case({"a": 1, "2": 2}) is False
    assert module_0.check_dict_case({1: "a"}) is False
    assert module_0.check_dict_case({"A": 1, "B": 2, "c": 3}) is False
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) is False
    assert module_0.check_dict_case({"A": 1, "a": 2}) is False
    print("all tests passed")


test_check_dict_case()

# Generated at 2026-10-24 07:17:25.882243
# Unit test for function check_dict_case

# Generated at 2026-10-24 07:17:28.389153
# Unit test for function check_dict_case

# Generated at 2026-10-24 07:17:30.801366
# Unit test for function check_dict_case

# Generated at 2026-10-24 07:17:33.370115
# Unit test for function check_dict_case

# Generated at 2026-10-24 07:17:35.795006
# Unit test for function check_dict_case

# Generated at 2026-10-24 07:17:38.226485
# Unit test for function check_dict_case

# Generated at 2026-10-24 07:17:40.631653
# Unit test for function check_dict_case

# Generated at 2026-10-24 07:17:47.364557
# Unit test for function check_dict_case
def test_check_dict_case():
    # All lowercase keys -> True
    assert module_0.check_dict_case({"apple": 1, "banana": 2}) is True
    # All uppercase keys -> True
    assert module_0.check_dict_case({"APPLE": 1, "BANANA": 2}) is True
    # Single lowercase key -> True
    assert module_0.check_dict_case({"a": 1}) is True
    # Single uppercase key -> True
    assert module_0.check_dict_case({"A": 1}) is True
    # Empty dict -> False
    assert module_0.check_dict_case({}) is False
    # Mixed case keys -> False
    assert module_0.check_dict_case({"apple": 1, "BANANA": 2}) is False
    # Non-string key -> False
    assert module_0.check_dict_case({1: "a", "b": 2}) is False
    assert module_0.check_dict_case({"a": 1, 2: "b"}) is False
    # Key with neither all-upper nor all-lower -> False
    assert module_0.check_dict_case({"Apple": 1}) is False
    assert module_0.check_dict_case({"aBc": 1}) is False
    # Mixed valid/invalid string casing -> False
    assert module_0.check_dict_case({"a": 1, "bC": 2}) is False
    # All keys uppercase including multi-char -> True
    assert module_0.check_dict_case({"A": 1, "BC": 2, "DEF": 3}) is True

# Generated at 2026-10-24 07:17:50.063101
# Unit test for function check_dict_case
def test_check_dict_case():
    assert module_0.check_dict_case({"a": 1, "b": 2}) is True
    assert module_0.check_dict_case({"A": 1, "B": 2}) is True
    assert module_0.check_dict_case({"a": 1, "B": 2}) is False
    assert module_0.check_dict_case({"A": 1, "b": 2}) is False
    assert module_0.check_dict_case({}) is False
    assert module_0.check_dict_case({"a": 1, "2": 2}) is False
    assert module_0.check_dict_case({1: "a"}) is False
    assert module_0.check_dict_case({"A": 1, "B": 2, "c": 3}) is False
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) is False
    assert module_0.check_dict_case({"A": 1, "a": 2}) is False
    print("all tests passed")


test_check_dict_case()