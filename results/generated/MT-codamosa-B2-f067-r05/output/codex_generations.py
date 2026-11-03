

# Generated at 2026-11-01 20:07:46.601347
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases with known quantities
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 11) == 0
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 1 oranges", 10) == 8
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19
    
    # Zero counts of named fruits
    assert module_0.fruit_distribution("0 apples and 0 oranges", 3) == 3
    assert module_0.fruit_distribution("0 apples and 0 oranges", 0) == 0
    
    # Multi-digit numbers
    assert module_0.fruit_distribution("12 apples and 34 oranges", 100) == 54
    assert module_0.fruit_distribution("999 apples and 999 oranges", 2000) == 2
    
    # String with no digits
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 5) == 5
    
    # Numbers embedded in larger words are not counted (isdigit fails)
    assert module_0.fruit_distribution("apples5 and oranges", 10) == 10
    
    # Single fruit type mentioned
    assert module_0.fruit_distribution("7 mangoes", 10) == 3
    
    print("All tests passed!")

if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-01 20:08:09.846404
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Typical case: two numbers in the string
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    # Only one number present
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    # Larger total
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    # Multi-digit numbers
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19
    # Numbers at start and end of string
    assert module_0.fruit_distribution("10 mangoes 20 bananas", 40) == 10
    # No digits at all -> everything is remaining fruit
    assert module_0.fruit_distribution("apples and oranges", 12) == 12
    # Sum equals n -> zero remaining
    assert module_0.fruit_distribution("4 apples and 6 oranges", 10) == 0
    # Negative result when described fruits exceed n
    assert module_0.fruit_distribution("15 apples and 10 oranges", 5) == -20
    print("All tests passed!")

if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-01 20:08:40.974770
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Two numbers in the string
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    # Single number in the string
    assert module_0.fruit_distribution("5 apples", 19) == 14
    # Numbers including zero
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    # Equal numbers
    assert module_0.fruit_distribution("1 apples and 1 oranges", 10) == 8
    # No numbers at all
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    # Sum exactly equals n
    assert module_0.fruit_distribution("5 apples and 5 oranges", 10) == 0
    # Sum exceeds n (negative result)
    assert module_0.fruit_distribution("10 apples and 5 oranges", 10) == -5
    # Larger numbers
    assert module_0.fruit_distribution("100 apples and 200 oranges", 500) == 200
    # Empty string
    assert module_0.fruit_distribution("", 5) == 5
    # Zero n and zero count
    assert module_0.fruit_distribution("0 apples", 0) == 0

# Generated at 2026-11-01 20:09:02.887421
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic test cases
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # No digits in string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 5) == 5

    # All digits, no other words
    assert module_0.fruit_distribution("3", 10) == 7
    assert module_0.fruit_distribution("7 2 1", 15) == 5

    # Multi-digit numbers
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000

    # Result is zero (all fruit accounted for)
    assert module_0.fruit_distribution("5 apples and 6 oranges", 11) == 0

    # Result is negative (more fruit than total)
    assert module_0.fruit_distribution("10 apples", 5) == -5

    # Numbers embedded with digits only as standalone tokens
    assert module_0.fruit_distribution("1 2 3 4 5", 15) == 0

    # Mixed spacing
    assert module_0.fruit_distribution("4 apples and  5   oranges", 12) == 3

    # Large values
    assert module_0.fruit_distribution("1000000 apples", 2000000) == 1000000

# Generated at 2026-11-01 20:09:22.516789
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic case: two numbers in the description
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    # Zeroes and ones
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("0 apples and 1 oranges", 5) == 4
    # Only one number mentioned
    assert module_0.fruit_distribution("10 apples", 20) == 10
    # No digits at all — all remaining fruits counted
    assert module_0.fruit_distribution("apples and oranges", 7) == 7
    # Multi-digit numbers
    assert module_0.fruit_distribution("100 apples and 45 oranges", 200) == 55
    # Digits sum exactly to n -> result is zero
    assert module_0.fruit_distribution("5 apples and 5 oranges", 10) == 0