

# Generated at 2026-11-03 01:59:47.186691
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Standard case: two numbers in the string
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10

    # Zero in the string
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2

    # Single digit numbers
    assert module_0.fruit_distribution("1 apples and 1 oranges", 10) == 8

    # No numbers in the string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10

    # Multi-digit numbers
    assert module_0.fruit_distribution("100 apples and 200 oranges", 350) == 50

    # Only one number in the string
    assert module_0.fruit_distribution("2 apples", 7) == 5

    # All fruits accounted for
    assert module_0.fruit_distribution("3 apples and 4 oranges", 7) == 0

    # Result can be negative if n is smaller than the sum
    assert module_0.fruit_distribution("10 apples and 5 oranges", 5) == -10

    # Larger numbers
    assert module_0.fruit_distribution("30 apples and 40 oranges", 100) == 30

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-03 02:00:51.738596
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases with known counts
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # String with multi-digit numbers
    assert module_0.fruit_distribution("12 apples and 34 oranges", 50) == 4

    # Only one number present
    assert module_0.fruit_distribution("5 apples", 10) == 5

    # No digits at all — all fruits are mangoes
    assert module_0.fruit_distribution("apples and oranges", 10) == 10

    # Zero remaining fruits
    assert module_0.fruit_distribution("3 apples and 7 oranges", 10) == 0

    # Large numbers
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000

    # Numbers with surrounding punctuation/words
    assert module_0.fruit_distribution("1 apple, 2 oranges and 3 mangoes", 10) == 4

    # Single digit string
    assert module_0.fruit_distribution("0", 5) == 5

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-03 02:02:11.920322
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases with two numbers in the string
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Single number in the string
    assert module_0.fruit_distribution("5 apples", 10) == 5
    assert module_0.fruit_distribution("1 mango", 1) == 0

    # No digits in the string — everything is the unknown fruit count
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 7) == 7

    # Multi-digit numbers mixed with words
    assert module_0.fruit_distribution("12 apples and 34 oranges and 4 mangoes", 100) == 50

    # Result can be zero
    assert module_0.fruit_distribution("3 apples and 4 oranges", 7) == 0

    # Numbers adjacent to punctuation still parsed via split
    assert module_0.fruit_distribution("2 apples, 3 oranges", 10) == 5

    # Large values
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-03 02:04:21.458973
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases from problem description
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # No digits in the string: all fruits are mangoes
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("one two three", 5) == 5

    # Empty string: no digits, return n unchanged
    assert module_0.fruit_distribution("", 7) == 7

    # Single digit-only token
    assert module_0.fruit_distribution("1", 5) == 4
    assert module_0.fruit_distribution("0", 10) == 10

    # Multi-digit numbers mixed with words
    assert module_0.fruit_distribution("10 apples 20 oranges 30 mangoes", 100) == 40
    assert module_0.fruit_distribution("12 apples and 34 oranges", 100) == 54

    # Numbers embedded at start/end of string
    assert module_0.fruit_distribution("3 apples and 4", 10) == 3
    assert module_0.fruit_distribution("7 apples", 7) == 0

    # Sum of digits exceeds n (negative result)
    assert module_0.fruit_distribution("50 apples", 10) == -40

    # Large values
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000

    print("All tests passed!")

test_fruit_distribution()

# Generated at 2026-11-03 02:05:23.508647
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic case with two counts
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10

    # Zero counts
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("0 apples and 0 oranges", 5) == 5

    # Equal distribution, result is zero
    assert module_0.fruit_distribution("1 apples and 1 oranges", 2) == 0

    # Multi-digit numbers
    assert module_0.fruit_distribution("10 apples and 20 oranges", 100) == 70
    assert module_0.fruit_distribution("100 apples and 200 oranges", 350) == 50

    # No digits in string
    assert module_0.fruit_distribution("apples and oranges", 7) == 7

    # Only digits in string
    assert module_0.fruit_distribution("3 4", 10) == 3

    # Single digit count
    assert module_0.fruit_distribution("2 apples", 5) == 3

    print("All tests passed!")

if __name__ == "__main__":
    test_fruit_distribution()