

# Generated at 2026-10-24 08:00:31.860360
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

# Generated at 2026-10-24 08:00:34.413141
# Unit test for function check_dict_case

# Generated at 2026-10-24 08:00:36.927135
# Unit test for function check_dict_case

# Generated at 2026-10-24 08:00:38.236105
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

# Generated at 2026-10-24 08:00:40.915487
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

# Generated at 2026-10-24 08:00:43.963482
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

# Generated at 2026-10-24 08:00:46.605291
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