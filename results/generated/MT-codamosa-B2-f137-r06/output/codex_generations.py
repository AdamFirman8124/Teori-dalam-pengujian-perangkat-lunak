

# Generated at 2026-11-02 22:41:22.005463
# Unit test for function compare_one
def test_compare_one():
    # Integer comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(5, 3) == 5

    # Float comparisons
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(3.7, 2.5) == 3.7

    # String comparisons
    assert module_0.compare_one("5", "6") == "6"
    assert module_0.compare_one("10", "2") == "10"

    # Strings with comma decimals (European format)
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("7,5", "7,4") == "7,5"

    # Equal values return None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one(2, 2) is None
    assert module_0.compare_one(2.0, 2.0) is None
    assert module_0.compare_one("2,5", "2.5") is None

    # Mixed types
    assert module_0.compare_one(0.1, "2,3") == "2,3"
    assert module_0.compare_one("3,14", 3) == "3,14"

    # Negative numbers
    assert module_0.compare_one(-5, 3) == 3
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", "-2") == "-1,5"

    # Original type is preserved in the return value
    assert isinstance(module_0.compare_one(1, 2.5), float)
    assert isinstance(module_0.compare_one(1, 2), int)
    assert isinstance(module_0.compare_one(1, "2.5"), str)
    assert isinstance(module_0.compare_one("1,5", 2), str)

    print("All compare_one tests passed!")


test_compare_one()

# Generated at 2026-11-02 22:44:30.286975
# Unit test for function compare_one
def test_compare_one():
    # Basic integer comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(5, 5) is None

    # Float comparisons
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1.5) == 2.5
    assert module_0.compare_one(2.5, 2.5) is None

    # String comparisons (with dot decimal separator)
    assert module_0.compare_one("1", "2") == "2"
    assert module_0.compare_one("2", "1") == "2"
    assert module_0.compare_one("1.5", "2.5") == "2.5"
    assert module_0.compare_one("2.5", "1.5") == "2.5"
    assert module_0.compare_one("1.0", "1") is None

    # String comparisons with comma decimal separator
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("2,5", "1,5") == "2,5"
    assert module_0.compare_one("1,0", "1.0") is None

    # Mixed types
    assert module_0.compare_one("2.5", 2) == "2.5"
    assert module_0.compare_one(2, "2.5") == "2.5"
    assert module_0.compare_one("3", 2) == "3"
    assert module_0.compare_one(3, "2") == 3

    # Negative numbers
    assert module_0.compare_one(-1, 1) == 1
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one(-1, -1) is None

    # Equal values of different representations
    assert module_0.compare_one(1.0, 1) is None
    assert module_0.compare_one("1,0", 1) is None

    print("All test cases passed!")


if __name__ == "__main__":
    test_compare_one()

# Generated at 2026-11-02 22:46:54.350436
# Unit test for function compare_one
def test_compare_one():
    # Integer comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(5, 5) is None

    # Float comparisons
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1.5) == 2.5
    assert module_0.compare_one(2.5, 2.5) is None

    # Mixed int and float
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(2, 2.0) is None

    # String comparisons (dot decimal)
    assert module_0.compare_one("1", "2") == "2"
    assert module_0.compare_one("2", "1") == "2"
    assert module_0.compare_one("1", "1") is None

    # String comparisons (comma decimal, European notation)
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("6", "5,1") == "6"

    # Mixed string and number
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("2,3", 1) == "2,3"
    assert module_0.compare_one("1", 1) is None

    # Original types are preserved (string returned as string)
    assert module_0.compare_one("3,5", 2) == "3,5"
    assert isinstance(module_0.compare_one("1,5", "2"), str)

    # Negative numbers
    assert module_0.compare_one(-1, 1) == 1
    assert module_0.compare_one(-2, -1) == -1

    print("All tests passed!")


test_compare_one()

# Generated at 2026-11-02 22:48:15.820691
# Unit test for function compare_one
def test_compare_one():
    # Basic numeric comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5

    # Equal values return None
    assert module_0.compare_one(2, 2) is None
    assert module_0.compare_one(2.0, 2) is None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one("1.0", "1") is None
    assert module_0.compare_one(0.5, "0,5") is None

    # String comparisons
    assert module_0.compare_one("1", "2") == "2"
    assert module_0.compare_one("2", "1") == "2"
    assert module_0.compare_one("10", "9") == "10"

    # Comma as decimal separator in strings
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("6", "5,1") == "6"
    assert module_0.compare_one(1, "2,5") == "2,5"

    # Returns the original value, not the converted one
    assert module_0.compare_one("2,5", 1) == "2,5"

    # Negative numbers
    assert module_0.compare_one(-1, 1) == 1
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one(-1.5, "-1,5") is None

# Generated at 2026-11-02 22:49:43.561330
# Unit test for function compare_one
def test_compare_one():
    # Numeric comparisons
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(-1, 1) == 1
    assert module_0.compare_one(0.5, 0.5) is None

    # String with comma decimal separator
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("2,3", 1) == "2,3"

    # Equal values of different types return None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one("1,1", "1.1") is None
    assert module_0.compare_one(1.0, "1,0") is None

    # Numeric (not lexicographic) comparison of numeric strings
    assert module_0.compare_one("2", "10") == "10"
    assert module_0.compare_one("-2", "-1") == "-1"

    # Original value returned, not converted
    assert module_0.compare_one("2.5", 1) == "2.5"