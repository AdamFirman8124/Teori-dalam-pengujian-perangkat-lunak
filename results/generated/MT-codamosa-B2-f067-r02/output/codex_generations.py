

# Generated at 2026-11-01 22:32:17.808076
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic case with two numbers in the string
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    # Case where one count is zero
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    # Larger total value
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    # Larger counts in the string
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19
    # Numbers in different positions within the string
    assert module_0.fruit_distribution("apples 12 and oranges 24", 50) == 14
    # Single number mentioned in the string
    assert module_0.fruit_distribution("10 mangoes only", 25) == 15
    # No numbers at all in the string
    assert module_0.fruit_distribution("just fruits here", 7) == 7
    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-01 22:32:37.364274
# Unit test for function fruit_distribution
def test_fruit_distribution():assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8

# Generated at 2026-11-01 22:33:03.885407
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases with two numbers in the string
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 11) == 0
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Single number in the string
    assert module_0.fruit_distribution("12 apples", 20) == 8
    assert module_0.fruit_distribution("7 apples", 7) == 0

    # No numbers in the string (all remaining)
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 5) == 5

    # Zero total
    assert module_0.fruit_distribution("3 apples", 3) == 0

    # Multi-digit numbers
    assert module_0.fruit_distribution("105 apples and 45 oranges", 200) == 50

    # Larger totals
    assert module_0.fruit_distribution("30 apples and 20 mangoes and 10 bananas", 100) == 40

# Generated at 2026-11-01 22:33:46.874796
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 0 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Edge cases
    assert module_0.fruit_distribution("apples and oranges", 10) == 10      # no digits in string
    assert module_0.fruit_distribution("", 5) == 5                          # empty string
    assert module_0.fruit_distribution("0 apples and 0 oranges", 0) == 0    # zero total
    assert module_0.fruit_distribution("7", 7) == 0                         # single number, all accounted for

    # Multiple numbers in string
    assert module_0.fruit_distribution("10 apples 20 oranges 5 bananas", 100) == 65

    # Negative result possible (more counted fruits than total)
    assert module_0.fruit_distribution("5 apples and 6 oranges", 10) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-01 22:34:11.984401
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 0 oranges", 3) == 2

    # Multi-digit numbers
    assert module_0.fruit_distribution("10 apples and 20 oranges", 100) == 70
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # No digits present in the string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 5) == 5

    # Sum of digits equals n
    assert module_0.fruit_distribution("3 apples and 4 oranges", 7) == 0

    # Single number only
    assert module_0.fruit_distribution("7 apples", 12) == 5