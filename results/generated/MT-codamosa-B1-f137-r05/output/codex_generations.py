

# Generated at 2026-10-25 02:36:47.433703
# Unit test for function compare_one
def test_compare_one():
    # Equal numeric values
    assert module_0.compare_one(10, 10) is None
    assert module_0.compare_one("10", 10) is None
    assert module_0.compare_one("1,5", 1.5) is None

    # First value is greater; return the original value
    assert module_0.compare_one(20, 10) == 20
    assert module_0.compare_one("2,5", 2.4) == "2,5"

    # Second value is greater; return the original value
    assert module_0.compare_one(5, 8) == 8
    assert module_0.compare_one("1,2", "1,3") == "1,3"

    # Negative values
    assert module_0.compare_one(-2, -5) == -2
    assert module_0.compare_one("-3,5", "-2,5") == "-2,5"

# Generated at 2026-10-25 02:36:56.866525
# Unit test for function compare_one
def test_compare_one():
    # Greater value is returned
    assert module_0.compare_one(10, 5) == 10
    assert module_0.compare_one(5, 10) == 10

    # Equal values return None
    assert module_0.compare_one(5, 5) is None
    assert module_0.compare_one("5", 5) is None
    assert module_0.compare_one("1,5", "1.5") is None

    # Strings using comma or dot as decimal separator
    assert module_0.compare_one("2,5", "2.4") == "2,5"
    assert module_0.compare_one("2,5", 3) == 3

    # Negative and floating-point values
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one(1.25, "1,5") == "1,5"

# Generated at 2026-10-25 02:37:02.802853
# Unit test for function compare_one
def test_compare_one():
    # Equal values
    assert module_0.compare_one(5, 5) is None
    assert module_0.compare_one("5", 5) is None
    assert module_0.compare_one("2,5", 2.5) is None

    # First value is larger
    assert module_0.compare_one(10, 5) == 10
    assert module_0.compare_one("10,5", "10.4") == "10,5"

    # Second value is larger
    assert module_0.compare_one(3, 7) == 7
    assert module_0.compare_one("1,2", "1,3") == "1,3"

    # Negative values
    assert module_0.compare_one(-2, -5) == -2
    assert module_0.compare_one("-3,5", "-2.5") == "-2.5"

# Generated at 2026-10-25 02:37:10.073458
# Unit test for function compare_one
def test_compare_one():
    assert module_0.compare_one(10, 5) == 10
    assert module_0.compare_one(5, 10) == 10
    assert module_0.compare_one(5, 5) is None

    assert module_0.compare_one("10", "5") == "10"
    assert module_0.compare_one("2,5", "2,4") == "2,5"
    assert module_0.compare_one("2,4", 2.5) == 2.5

    # Numerically equal values return None, even with different formats
    assert module_0.compare_one("2,5", 2.5) is None

    # Negative values
    assert module_0.compare_one(-3, -7) == -3

# Generated at 2026-10-25 02:37:15.295600
# Unit test for function compare_one
def test_compare_one():
    assert module_0.compare_one(10, 5) == 10
    assert module_0.compare_one(5, 10) == 10
    assert module_0.compare_one("10,5", "9.5") == "10,5"
    assert module_0.compare_one("-2", "-1") == "-1"
    assert module_0.compare_one(3, "3,0") is None
    assert module_0.compare_one("2,50", "2.5") is None