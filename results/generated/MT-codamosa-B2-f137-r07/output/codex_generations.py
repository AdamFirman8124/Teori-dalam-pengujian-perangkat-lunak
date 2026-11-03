

# Generated at 2026-11-02 17:35:27.459682
# Unit test for function compare_one
def test_compare_one():
    # Basic numeric comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5

    # String with comma as decimal separator
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("2,3", 1) == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("6", "5,1") == "6"

    # Equal values return None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one("1,0", "1.0") is None
    assert module_0.compare_one("1,0", 1) is None
    assert module_0.compare_one(2.5, 2.5) is None

    # Negative numbers
    assert module_0.compare_one(-1, 1) == 1
    assert module_0.compare_one(1, -1) == 1
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", -1) == "-1,5"

    # Float precision
    assert module_0.compare_one(0.1, 0.2) == 0.2
    assert module_0.compare_one("0,1", 0.2) == 0.2

    # Original value (not converted) is returned for strings
    result = module_0.compare_one("2,5", 2)
    assert result == "2,5" and isinstance(result, str)

    print("All compare_one tests passed!")

# Generated at 2026-11-02 17:37:23.732320
# Unit test for function compare_one
def test_compare_one():
    # Basic integer comparison
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(5, 3) == 5
    assert module_0.compare_one(10, 10) is None

    # Float comparison
    assert module_0.compare_one(2.5, 3.5) == 3.5
    assert module_0.compare_one(3.5, 2.5) == 3.5
    assert module_0.compare_one(2.5, 2.5) is None

    # String with dot decimal
    assert module_0.compare_one("2.3", "4.5") == "4.5"
    assert module_0.compare_one("4.5", "2.3") == "4.5"
    assert module_0.compare_one("2.3", "2.3") is None

    # String with comma decimal (European notation)
    assert module_0.compare_one("2,3", "4,5") == "4,5"
    assert module_0.compare_one("4,5", "2,3") == "4,5"
    assert module_0.compare_one("2,3", "2,3") is None

    # Mixed types: string vs int
    assert module_0.compare_one("5", 3) == "5"
    assert module_0.compare_one(3, "5") == "5"
    assert module_0.compare_one("5", 5) is None

    # Mixed types: string vs float
    assert module_0.compare_one("2.5", 3) == 3
    assert module_0.compare_one(3, "2,5") == 3

    # Negative numbers
    assert module_0.compare_one(-1, 2) == 2
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one(-2.5, -2.5) is None

    # Large values
    assert module_0.compare_one(1000, 999) == 1000
    assert module_0.compare_one("1000.1", 1000) == "1000.1"

# Generated at 2026-11-02 17:38:18.868716
# Unit test for function compare_one
def test_compare_one():
    # Basic integer comparisons
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(5, 5) is None

    # Float comparisons
    assert module_0.compare_one(2.5, 1.5) == 2.5
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(2.5, 2.5) is None

    # String comparisons (dot decimals)
    assert module_0.compare_one("1", "2") == "2"
    assert module_0.compare_one("2", "1") == "2"
    assert module_0.compare_one("1.5", "1.5") is None

    # Strings with comma decimal separators
    assert module_0.compare_one("1,5", "1") == "1,5"
    assert module_0.compare_one("1", "1,5") == "1,5"
    assert module_0.compare_one("1,5", "1,5") is None

    # Mixed types
    assert module_0.compare_one("1", 1.0) is None
    assert module_0.compare_one(2, "1") == 2
    assert module_0.compare_one("1", 2) == 2
    assert module_0.compare_one("2", 1) == "2"

    # Negative numbers
    assert module_0.compare_one(-1, 1) == 1
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", "-1") == "-1,5"

    # Zero handling
    assert module_0.compare_one(0, 0) is None
    assert module_0.compare_one(0, 1) == 1
    assert module_0.compare_one("0.1", 0.1) is None

    # Larger / precise values
    assert module_0.compare_one(100, 99.99) == 100
    assert module_0.compare_one("3.14159", "3.14159") is None

    print("All compare_one tests passed!")


if __name__ == "__main__":
    test_compare_one()

# Generated at 2026-11-02 17:39:14.151714
# Unit test for function compare_one
def test_compare_one():
    # Basic numeric comparisons
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2
    assert module_0.compare_one(10, 9.99) == 10

    # Equal values return None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(1.0, 1) is None
    assert module_0.compare_one(0, 0.0) is None

    # String inputs with comma decimal separators
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1,5", "1.5") is None
    assert module_0.compare_one("2,5", 2.5) is None

    # String inputs with dot decimal separators
    assert module_0.compare_one("1.5", 1) == "1.5"
    assert module_0.compare_one("0.1", "0.01") == "0.1"
    assert module_0.compare_one("3.14", 3) == "3.14"

    # Negative numbers
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one(-1.5, "-1,5") is None

    # Original values are returned unchanged (type preserved)
    result = module_0.compare_one(1, "2,3")
    assert result == "2,3" and isinstance(result, str)
    result = module_0.compare_one(2, "1,5")
    assert result == 2 and isinstance(result, int)

    # Invalid string input raises ValueError
    try:
        module_0.compare_one("abc", 1)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    print("All test_compare_one tests passed!")

# Generated at 2026-11-02 17:40:35.359582
# Unit test for function compare_one
def test_compare_one():
    # Integer comparisons
    assert module_0.compare_one(1, 5) == 5
    assert module_0.compare_one(5, 1) == 5
    assert module_0.compare_one(10, 2) == 10

    # Float comparisons
    assert module_0.compare_one(2.5, 1.5) == 2.5
    assert module_0.compare_one(1.5, 2.5) == 2.5

    # String comparisons
    assert module_0.compare_one("1", "2") == "2"
    assert module_0.compare_one("2", "1") == "2"

    # Strings with comma as decimal separator (European notation)
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("2,5", "1,5") == "2,5"
    assert module_0.compare_one("1,5", "1.5") is None

    # Equal values return None
    assert module_0.compare_one(5, 5) is None
    assert module_0.compare_one(5.0, 5) is None
    assert module_0.compare_one("5", "5") is None
    assert module_0.compare_one("5,0", "5.0") is None

    # Mixed types: original object is returned, not the converted one
    assert module_0.compare_one("2", 3) == 3
    assert module_0.compare_one(3, "2") == 3
    assert module_0.compare_one("2,5", 2.0) == "2,5"
    assert module_0.compare_one(2.0, "2,5") == "2,5"

    # Negative numbers
    assert module_0.compare_one(-1, -5) == -1
    assert module_0.compare_one(-5, -1) == -1
    assert module_0.compare_one(-1.5, -1.5) is None

    print("All tests passed!")


test_compare_one()