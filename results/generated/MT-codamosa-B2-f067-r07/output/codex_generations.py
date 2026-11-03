

# Generated at 2026-11-02 13:04:43.713712
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 5) == 5
    assert module_0.fruit_distribution("0 apples", 0) == 0
    assert module_0.fruit_distribution("1 2 3 4", 10) == 0
    assert module_0.fruit_distribution("10 apples", 5) == -5

test_fruit_distribution()
print("All tests passed!")

# Generated at 2026-11-02 13:06:41.147791
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases: digits in string sum up, subtracted from n
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Edge case: no digits present in the string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 7) == 7

    # Edge case: all fruits accounted for, result is zero
    assert module_0.fruit_distribution("10 apples and 5 oranges", 15) == 0

    # Multi-digit numbers
    assert module_0.fruit_distribution("12 apples and 34 oranges", 100) == 54

    print("All test cases passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-02 13:09:23.440192
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Test with typical input
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Test with more complex strings
    assert module_0.fruit_distribution("10 apples and 20 oranges and 5 mangoes", 40) == 5
    assert module_0.fruit_distribution("1 apple and 1 orange and 1 banana", 10) == 7

    # Test with no digits in string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10

    # Test with only digits
    assert module_0.fruit_distribution("3 4 5", 15) == 3

    # Test with zero distribution
    assert module_0.fruit_distribution("5 apples and 5 oranges", 10) == 0

    # Test with large numbers
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000

    # Test with single item
    assert module_0.fruit_distribution("7 apples", 10) == 3

    # Test edge case: empty string
    assert module_0.fruit_distribution("", 5) == 5

    # Test with zero count
    assert module_0.fruit_distribution("0 apples and 0 oranges", 0) == 0

if __name__ == "__main__":
    test_fruit_distribution()
    print("All tests passed!")

# Generated at 2026-11-02 13:10:42.813578
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases: string contains counts of apples and oranges
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Only one number present
    assert module_0.fruit_distribution("5 apples", 10) == 5
    assert module_0.fruit_distribution("0 apples", 0) == 0

    # No digits in string, all fruits remain
    assert module_0.fruit_distribution("apples and oranges", 7) == 7
    assert module_0.fruit_distribution("", 10) == 10

    # Multi-digit numbers
    assert module_0.fruit_distribution("12 apples and 34 oranges", 100) == 54

    # Numbers with multiple occurrences
    assert module_0.fruit_distribution("1 apples 2 oranges 3 bananas", 10) == 4

    # Zero total
    assert module_0.fruit_distribution("0 apples and 0 oranges", 0) == 0

    # Negative result when digits sum exceeds n
    assert module_0.fruit_distribution("10 apples and 20 oranges", 5) == -25

    print("All test_fruit_distribution tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-02 13:11:42.717102
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases: extract digits from string, subtract sum from total
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Single digit group
    assert module_0.fruit_distribution("10 apples", 15) == 5

    # No digits in string: returns full total
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 7) == 7

    # Multiple number groups
    assert module_0.fruit_distribution("1 apples and 2 oranges and 3 mangoes", 10) == 4

    # Zero remaining fruits
    assert module_0.fruit_distribution("3 apples and 4 oranges", 7) == 0

    # Multi-digit numbers
    assert module_0.fruit_distribution("123 apples and 456 oranges", 1000) == 421

    print("All tests passed!")


test_fruit_distribution()