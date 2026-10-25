

# Generated at 2026-10-24 11:23:46.050075
# Unit test for function compare_one
def test_compare_one():
    # given examples
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1", "2") == "2"

    # integers: larger wins, equal -> None
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(-5, -2) == -2
    assert module_0.compare_one(-1, 1) == 1

    # floats and mixed int / float
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(2, 2.0) is None
    assert module_0.compare_one(1, 1.0) is None

    # numeric strings, dot vs comma
    assert module_0.compare_one("1", "2.5") == "2.5"
    assert module_0.compare_one("1,2", "1.5") == "1.5"
    assert module_0.compare_one("1,5", "1.5") is None
    assert module_0.compare_one("3", "3,0") is None
    assert module_0.compare_one(0, "0,0") is None

    # returns original value, not converted value
    assert module_0.compare_one("2", 1) == "2"
    assert module_0.compare_one("1", 2) == 2
    assert module_0.compare_one("1,5", 1) == "1,5"
    assert module_0.compare_one(1, "1,5") == "1,5"

# Generated at 2026-10-24 11:24:02.640672
# Unit test for function compare_one
def test_compare_one():
    # given examples
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1", "2") == "2"

    # integers: larger wins, equal -> None
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(-5, -2) == -2
    assert module_0.compare_one(-1, 1) == 1

    # floats and mixed int / float
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(2, 2.0) is None
    assert module_0.compare_one(1, 1.0) is None

    # numeric strings, dot vs comma
    assert module_0.compare_one("1", "2.5") == "2.5"
    assert module_0.compare_one("1,2", "1.5") == "1.5"
    assert module_0.compare_one("1,5", "1.5") is None
    assert module_0.compare_one("3", "3,0") is None
    assert module_0.compare_one(0, "0,0") is None

    # returns original value, not converted value
    assert module_0.compare_one("2", 1) == "2"
    assert module_0.compare_one("1", 2) == 2
    assert module_0.compare_one("1,5", 1) == "1,5"
    assert module_0.compare_one(1, "1,5") == "1,5"

# Generated at 2026-10-24 11:24:22.408036
# Unit test for function compare_one
def test_compare_one():
    # Different types, numeric comparison
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1", 1) is None          # equal values, different types
    assert module_0.compare_one(2, 2) is None            # equal integers
    assert module_0.compare_one("1.0", "1,0") is None    # equal after comma normalization

    # Negative numbers
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

    # Zero vs negative
    assert module_0.compare_one(0, -1) == 0

    # Original types are preserved (string stays string, int stays int)
    assert isinstance(module_0.compare_one("2,5", 3), str)
    assert isinstance(module_0.compare_one(3, "2,5"), int)

    print("All compare_one tests passed.")


test_compare_one()

# Generated at 2026-10-24 11:24:24.827758
# Unit test for function compare_one

# Generated at 2026-10-24 11:24:27.242819
# Unit test for function compare_one

# Generated at 2026-10-24 11:24:29.658478
# Unit test for function compare_one

# Generated at 2026-10-24 11:24:32.073519
# Unit test for function compare_one

# Generated at 2026-10-24 11:24:34.490296
# Unit test for function compare_one

# Generated at 2026-10-24 11:24:45.307395
# Unit test for function compare_one
def test_compare_one():assert module_0.compare_one(1, 2) == 2