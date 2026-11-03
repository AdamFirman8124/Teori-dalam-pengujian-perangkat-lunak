

# Generated at 2026-11-02 12:44:19.422922
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases with two numbers
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 11) == 0
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Cases with zero
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("0 apples and 0 oranges", 5) == 5

    # Single number in string
    assert module_0.fruit_distribution("1", 3) == 2
    assert module_0.fruit_distribution("10 apples", 20) == 10

    # No numbers in string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 5) == 5

    # Numbers with other text mixed in
    assert module_0.fruit_distribution("3 apples and 4 oranges and 2 mangoes", 15) == 6

    # Larger values
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 10000) == 7000

    print("All tests passed!")


test_fruit_distribution()

# Generated at 2026-11-02 12:46:57.329522
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic case: digits and words mixed
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    # Single number in string
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    # Multiple multi-digit numbers
    assert module_0.fruit_distribution("10 apples and 20 oranges", 100) == 70
    # No digits at all - all fruits are mangoes
    assert module_0.fruit_distribution("apples and oranges", 15) == 15
    # Zero total fruits
    assert module_0.fruit_distribution("0 apples and 0 oranges", 0) == 0
    # Result can be zero when digits sum to n
    assert module_0.fruit_distribution("3 apples and 7 oranges", 10) == 0
    # Large numbers
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000
    # Repeated numbers in string
    assert module_0.fruit_distribution("2 apples and 2 oranges and 2 bananas", 10) == 4
    # Number followed immediately by punctuation (not digit-attached)
    assert module_0.fruit_distribution("1 apple, 2 oranges", 5) == 2
    # All fruits are accounted for except mangoes, large n
    assert module_0.fruit_distribution("1 apples and 1 oranges", 1000) == 998

    print("All tests passed!")

if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-02 12:49:27.254559
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases: string contains counts of apples and oranges
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 1 oranges", 5) == 3

    # Multi-digit numbers
    assert module_0.fruit_distribution("100 apples and 20 oranges", 150) == 30
    assert module_0.fruit_distribution("10 apples", 10) == 0

    # No digits in string: all fruits are mangoes
    assert module_0.fruit_distribution("apples and oranges", 7) == 7
    assert module_0.fruit_distribution("", 5) == 5

    # Zero total
    assert module_0.fruit_distribution("0 apples and 0 oranges", 0) == 0

    # Negative result (more counted fruits than total)
    assert module_0.fruit_distribution("3 apples and 4 oranges", 5) == -2

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-02 12:50:44.654472
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Multi-digit numbers
    assert module_0.fruit_distribution("12 apples and 34 oranges", 50) == 4
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 3000) == 0

    # Numbers embedded with words
    assert module_0.fruit_distribution("10 apples", 10) == 0
    assert module_0.fruit_distribution("apples and oranges", 7) == 7  # no digits

    # Empty string
    assert module_0.fruit_distribution("", 5) == 5

    # Digits only
    assert module_0.fruit_distribution("3 4 5", 12) == 0

    # Negative result possible
    assert module_0.fruit_distribution("10 apples and 10 oranges", 5) == -15

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()