

# Generated at 2026-11-02 06:17:55.469315
# Unit test for function compare_one
def test_compare_one():
    # Integer comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(5, 5) is None

    # Float comparisons
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1.5) == 2.5
    assert module_0.compare_one(1.5, 1.5) is None

    # String comparisons
    assert module_0.compare_one("1", "2") == "2"
    assert module_0.compare_one("2", "1") == "2"
    assert module_0.compare_one("3.14", "3.14") is None

    # Strings with comma decimal separators
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("2,5", "1,5") == "2,5"
    assert module_0.compare_one("1,0", "1.0") is None

    # Mixed types (int, float, string)
    assert module_0.compare_one(1, "2.5") == "2.5"
    assert module_0.compare_one("2.5", 1) == "2.5"
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one(1, 1.0) is None

    # Original value is returned unchanged (not the converted form)
    assert module_0.compare_one("2,5", 1) == "2,5"
    assert module_0.compare_one(1, "2,5") == "2,5"

    # Negative numbers
    assert module_0.compare_one(-1, 1) == 1
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", "-1") == "-1"

    # Zero comparisons
    assert module_0.compare_one(0, 0.0) is None
    assert module_0.compare_one(0, 1) == 1

    print("All test cases passed!")


test_compare_one()

# Generated at 2026-11-02 06:18:00.208345
# Unit test for function compare_one
def test_compare_one():
    # Equal numeric values return None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(2.5, 2.5) is None
    assert module_0.compare_one("5", 5) is None
    assert module_0.compare_one("5.0", 5) is None

    # a > b returns a
    assert module_0.compare_one(1, 0) == 1
    assert module_0.compare_one(2.5, 2) == 2.5
    assert module_0.compare_one("2.5", 2) == "2.5"

    # b > a returns b
    assert module_0.compare_one(0, 1) == 1
    assert module_0.compare_one(2, 2.5) == 2.5
    assert module_0.compare_one(2, "2.5") == "2.5"

    # Strings with comma decimal separators are converted
    assert module_0.compare_one("1,5", "1,6") == "1,6"
    assert module_0.compare_one("1,5", "1,4") == "1,5"
    assert module_0.compare_one("1,5", "1.5") is None
    assert module_0.compare_one("2,3", 2.3) is None

    # Mixed types
    assert module_0.compare_one("10", 9) == "10"
    assert module_0.compare_one(9, "10") == "10"
    assert module_0.compare_one(True, 1) is None
    assert module_0.compare_one(True, 2) == 2

    # Negative numbers
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", -1.5) is None

# Generated at 2026-11-02 06:18:06.935895
# Unit test for function compare_one
def test_compare_one():
    # Basic numeric comparisons
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(-1, 1) == 1
    assert module_0.compare_one(1, -1) == 1

    # Equal values return None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(2.5, 2.5) is None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one(1, "1") is None

    # String comparisons with dot decimals
    assert module_0.compare_one("2.5", 1) == "2.5"
    assert module_0.compare_one(1, "2.5") == "2.5"
    assert module_0.compare_one("3.14", "2.71") == "3.14"

    # String comparisons with comma decimals
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("2,3", 1) == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("6", "5,1") == "6"

    # Comma decimals equal check
    assert module_0.compare_one("1,0", 1) is None
    assert module_0.compare_one("0,5", 0.5) is None

    # Mixed types
    assert module_0.compare_one(True, 0) == True
    assert module_0.compare_one(0, True) == True

    # Returns original value (not converted), preserving type
    result = module_0.compare_one("2,5", 1)
    assert result == "2,5" and isinstance(result, str)
    result = module_0.compare_one(3, "1,5")
    assert result == 3 and isinstance(result, int)

    # Invalid string raises ValueError
    try:
        module_0.compare_one("abc", 1)
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-11-02 06:18:14.534009
# Unit test for function compare_one
def test_compare_one():
    # Basic numeric comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1.5) == 2.5
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one(-2.5, -1.5) == -1.5

    # Equal values return None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(1.0, 1) is None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one(1, "1") is None
    assert module_0.compare_one("1", "1") is None

    # Strings with comma decimal separators
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("2,3", 1) == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("6", "5,1") == "6"
    assert module_0.compare_one("1,1", "1,1") is None
    assert module_0.compare_one("1,5", "1.5") is None  # equivalent after normalization

    # Mixed int/float/string comparisons
    assert module_0.compare_one("10", 5) == "10"
    assert module_0.compare_one(5, "10") == "10"
    assert module_0.compare_one(3.5, "3,4") == "3,4"
    assert module_0.compare_one("3,4", 3.5) == "3,4"

    # Original value/type is preserved in the result
    result = module_0.compare_one(1, "2.5")
    assert result == "2.5" and isinstance(result, str)
    result = module_0.compare_one("2,5", 1)
    assert result == "2,5" and isinstance(result, str)
    result = module_0.compare_one(1, 2.5)
    assert result == 2.5 and isinstance(result, float)
    result = module_0.compare_one("7", 3)
    assert result == "7" and isinstance(result, str)

    print("All tests passed!")


test_compare_one()

# Generated at 2026-11-02 06:18:23.635922
# Unit test for function compare_one
def test_compare_one():
    # Integer comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(5, 5) is None

    # Float comparisons
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1.5) == 2.5
    assert module_0.compare_one(3.14, 3.14) is None

    # String comparisons
    assert module_0.compare_one("1", "2") == "2"
    assert module_0.compare_one("2", "1") == "2"
    assert module_0.compare_one("1", "1") is None

    # Comma decimal strings (European format)
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("2,5", "1,5") == "2,5"
    assert module_0.compare_one("1,0", "1") is None

    # Mixed types
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("2,3", 1) == "2,3"
    assert module_0.compare_one("2.5", 2.5) is None
    assert module_0.compare_one(10, "9") == 10
    assert module_0.compare_one("10", 9) == "10"

    # Negatives and zero
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one(-1.5, -1.5) is None
    assert module_0.compare_one(0, 0) is None
    assert module_0.compare_one(0, 1) == 1
    assert module_0.compare_one(1, 0) == 1

    # Original (unconverted) values are returned, not the parsed floats
    result = module_0.compare_one("5,1", "6")
    assert result == "6" and isinstance(result, str)
    result = module_0.compare_one(2, "1,5")
    assert result == 2 and isinstance(result, int)