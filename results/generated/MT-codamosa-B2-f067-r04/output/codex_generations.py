

# Generated at 2026-11-01 19:48:32.755310
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Standard cases: digits embedded in descriptive text
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Multi-digit numbers in various positions
    assert module_0.fruit_distribution("10 apples and 20 oranges", 100) == 70
    assert module_0.fruit_distribution("1 apples and 0 oranges", 5) == 4

    # No digits present -> returns n unchanged
    assert module_0.fruit_distribution("apples and oranges", 10) == 10

    # Empty string -> returns n unchanged
    assert module_0.fruit_distribution("", 10) == 10

    # Only digits, no words
    assert module_0.fruit_distribution("3 4", 10) == 3

    # All fruits accounted for -> result is zero
    assert module_0.fruit_distribution("5 apples and 5 oranges", 10) == 0

# Generated at 2026-11-01 19:48:52.695446
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic test cases
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 1 oranges", 5) == 3

    # String with no digits
    assert module_0.fruit_distribution("apples and oranges", 10) == 10

    # String with only digits
    assert module_0.fruit_distribution("3 4 5", 15) == 3

    # Multi-digit numbers
    assert module_0.fruit_distribution("100 apples and 200 oranges", 350) == 50

    # Zero total fruits
    assert module_0.fruit_distribution("2 apples and 3 oranges", 5) == 0

    # Larger numbers
    assert module_0.fruit_distribution("10 apples", 100) == 90

    # Single digit in string
    assert module_0.fruit_distribution("7", 7) == 0

    # Multiple multi-digit numbers
    assert module_0.fruit_distribution("12 apples 34 oranges 56 mangoes", 150) == 48

    # Empty digit contribution
    assert module_0.fruit_distribution("no fruits here", 42) == 42

    print("All tests passed!")


test_fruit_distribution()

# Generated at 2026-11-01 19:49:20.049920
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic case with two counts
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    # Case with zero
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    # Multi-digit numbers
    assert module_0.fruit_distribution("10 apples and 20 oranges", 100) == 70
    # Single number only
    assert module_0.fruit_distribution("12 apples", 30) == 18
    # No digits at all
    assert module_0.fruit_distribution("no fruits here", 10) == 10
    # Empty string
    assert module_0.fruit_distribution("", 5) == 5
    # Result can be zero when all fruits accounted for
    assert module_0.fruit_distribution("4 mangoes and 6 bananas", 10) == 0
    print("All tests passed!")

test_fruit_distribution()

# Generated at 2026-11-01 19:49:33.975689
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases: string contains counts of apples and oranges
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 11) == 0
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Multi-digit numbers in the string
    assert module_0.fruit_distribution("12 apples and 34 oranges", 100) == 54
    assert module_0.fruit_distribution("99 apples and 99 oranges", 200) == 2

    # No digits present in the string: all fruits are mangoes
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 5) == 5

    # Single digit only
    assert module_0.fruit_distribution("7 apples", 12) == 5

    # Zero total fruits
    assert module_0.fruit_distribution("0 apples and 0 oranges", 0) == 0

    # Negative result allowed (n smaller than digit sum)
    assert module_0.fruit_distribution("3 apples and 4 oranges", 5) == -2

    # Digits embedded with non-digit characters are not counted
    assert module_0.fruit_distribution("abc123 apples and 4 oranges", 20) == 16

# Generated at 2026-11-01 19:49:45.196368
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Test with typical input
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 1 oranges", 2) == 0
    
    # Test with no digits in string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    
    # Test with only digits
    assert module_0.fruit_distribution("3 4 5", 20) == 8
    
    # Test with larger numbers
    assert module_0.fruit_distribution("100 apples", 100) == 0
    assert module_0.fruit_distribution("25 apples and 50 oranges", 100) == 25
    
    # Test with zero result
    assert module_0.fruit_distribution("2 apples", 2) == 0
    
    # Test with empty string
    assert module_0.fruit_distribution("", 5) == 5
    
    print("All tests passed!")

test_fruit_distribution()