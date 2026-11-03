

# Generated at 2026-11-02 08:11:38.745115
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6
    assert module_0.greatest_common_divisor(10, 25) == 5
    assert module_0.greatest_common_divisor(7, 13) == 1  # coprime numbers

    # One divides the other
    assert module_0.greatest_common_divisor(4, 12) == 4
    assert module_0.greatest_common_divisor(12, 4) == 4

    # Same numbers
    assert module_0.greatest_common_divisor(5, 5) == 5
    assert module_0.greatest_common_divisor(100, 100) == 100

    # With zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Coprime large numbers
    assert module_0.greatest_common_divisor(17, 19) == 1
    assert module_0.greatest_common_divisor(2**10 * 3, 2**10 * 5) == 2**10

    # Ones
    assert module_0.greatest_common_divisor(1, 1) == 1
    assert module_0.greatest_common_divisor(1, 999) == 1

    print("All tests passed!")

# Generated at 2026-11-02 08:12:41.846359
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6  # order shouldn't matter
    assert module_0.greatest_common_divisor(100, 25) == 25
    assert module_0.greatest_common_divisor(25, 100) == 25

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # One number is a multiple of the other
    assert module_0.greatest_common_divisor(7, 21) == 7
    assert module_0.greatest_common_divisor(21, 7) == 7

    # Equal numbers
    assert module_0.greatest_common_divisor(5, 5) == 5
    assert module_0.greatest_common_divisor(1, 1) == 1

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative numbers (GCD is conventionally positive)
    assert module_0.greatest_common_divisor(-48, 18) == 6
    assert module_0.greatest_common_divisor(48, -18) == 6
    assert module_0.greatest_common_divisor(-48, -18) == 6

    # Large numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**10, 2**5) == 2**5

    # Ones
    assert module_0.greatest_common_divisor(1, 999) == 1

# Generated at 2026-11-02 08:13:32.512430
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(12, 8) == 4
    assert module_0.greatest_common_divisor(8, 12) == 4  # order shouldn't matter
    assert module_0.greatest_common_divisor(48, 36) == 12
    assert module_0.greatest_common_divisor(36, 48) == 12

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(9, 28) == 1

    # One divides the other
    assert module_0.greatest_common_divisor(5, 20) == 5
    assert module_0.greatest_common_divisor(20, 5) == 5
    assert module_0.greatest_common_divisor(7, 49) == 7

    # Equal numbers
    assert module_0.greatest_common_divisor(10, 10) == 10
    assert module_0.greatest_common_divisor(1, 1) == 1

    # Involving zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Involving one
    assert module_0.greatest_common_divisor(1, 99) == 1
    assert module_0.greatest_common_divisor(99, 1) == 1

    # Negative numbers (GCD should be positive magnitude)
    assert module_0.greatest_common_divisor(-12, 8) == 4
    assert module_0.greatest_common_divisor(12, -8) == 4
    assert module_0.greatest_common_divisor(-12, -8) == 4

    # Large numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(123456789, 987654321) == 9
    assert module_0.greatest_common_divisor(2**20, 2**10) == 2**10

    # Prime numbers
    assert module_0.greatest_common_divisor(101, 103) == 1
    assert module_0.greatest_common_divisor(101, 202) == 101

    print("All tests passed!")


test_greatest_common_divisor()

# Generated at 2026-11-02 08:14:42.042392
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(12, 8) == 4
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(100, 25) == 25

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 5) == 1
    assert module_0.greatest_common_divisor(8, 9) == 1
    assert module_0.greatest_common_divisor(13, 7) == 1

    # One divides the other (order independent)
    assert module_0.greatest_common_divisor(10, 5) == 5
    assert module_0.greatest_common_divisor(5, 10) == 5
    assert module_0.greatest_common_divisor(13, 26) == 13

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7

    # Larger / classic Euclidean example
    assert module_0.greatest_common_divisor(1071, 462) == 21

    # Powers of two
    assert module_0.greatest_common_divisor(2**20, 2**15) == 2**15

    # Negative first argument (Euclidean algorithm handles it)
    assert module_0.greatest_common_divisor(-12, 8) == 4

    print("All tests passed!")

# Generated at 2026-11-02 08:15:24.437038
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6
    assert module_0.greatest_common_divisor(12, 8) == 4
    assert module_0.greatest_common_divisor(8, 12) == 4

    # One number divides the other
    assert module_0.greatest_common_divisor(5, 10) == 5
    assert module_0.greatest_common_divisor(10, 5) == 5
    assert module_0.greatest_common_divisor(100, 25) == 25

    # Coprime numbers
    assert module_0.greatest_common_divisor(7, 13) == 1
    assert module_0.greatest_common_divisor(17, 4) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # Equal numbers
    assert module_0.greatest_common_divisor(9, 9) == 9
    assert module_0.greatest_common_divisor(1, 1) == 1

    # Zero cases
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative numbers (matches Python's % semantics)
    assert module_0.greatest_common_divisor(-48, 18) == 6
    assert module_0.greatest_common_divisor(48, -18) == -6
    assert module_0.greatest_common_divisor(-48, -18) == -6
    assert abs(module_0.greatest_common_divisor(-12, -8)) == 4

    # Classic examples / larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**20, 2**15) == 2**15
    assert module_0.greatest_common_divisor(270, 192) == 6

    # Property check: gcd result divides both inputs
    for x, y in [(120, 28), (99, 33), (17, 5), (256, 96)]:
        g = module_0.greatest_common_divisor(x, y)
        assert x % g == 0 and y % g == 0

    print("All greatest_common_divisor tests passed!")


test_greatest_common_divisor()