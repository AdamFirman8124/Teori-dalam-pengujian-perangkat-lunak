

# Generated at 2026-11-03 02:19:09.521601
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic positive cases
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6

    # One divides the other
    assert module_0.greatest_common_divisor(5, 10) == 5
    assert module_0.greatest_common_divisor(10, 5) == 5

    # Coprime numbers
    assert module_0.greatest_common_divisor(7, 13) == 1
    assert module_0.greatest_common_divisor(17, 4) == 1

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(1, 1) == 1

    # Zero cases
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative inputs (GCD is conventionally non-negative)
    assert abs(module_0.greatest_common_divisor(-12, 8)) == 4
    assert abs(module_0.greatest_common_divisor(12, -8)) == 4
    assert abs(module_0.greatest_common_divisor(-12, -8)) == 4

    # Larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**20, 2**15) == 2**15
    assert module_0.greatest_common_divisor(1000000, 999999) == 1

    print("All tests passed!")
# nonce:d44f5905

# Generated at 2026-11-03 02:21:30.292115
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(12, 8) == 4
    assert module_0.greatest_common_divisor(8, 12) == 4
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6

    # One number is zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # One divides the other
    assert module_0.greatest_common_divisor(7, 21) == 7
    assert module_0.greatest_common_divisor(100, 25) == 25

    # Equal numbers
    assert module_0.greatest_common_divisor(9, 9) == 9

    # Larger numbers
    assert module_0.greatest_common_divisor(123456, 789012) == 12

    # Negative numbers (compare via abs due to Python modulo sign semantics)
    assert abs(module_0.greatest_common_divisor(-12, 18)) == 6
    assert abs(module_0.greatest_common_divisor(12, -18)) == 6
    assert abs(module_0.greatest_common_divisor(-24, -36)) == 12

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()

# Generated at 2026-11-03 02:24:19.245295
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5

    # One argument is zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5

    # Both zero
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(100, 100) == 100

    # One divides the other
    assert module_0.greatest_common_divisor(12, 4) == 4
    assert module_0.greatest_common_divisor(4, 12) == 4

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # Negative numbers
    assert module_0.greatest_common_divisor(-48, 18) == 6
    assert module_0.greatest_common_divisor(48, -18) == 6
    assert module_0.greatest_common_divisor(-48, -18) == 6

    # Large numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(123456, 789012) == 12

    # Powers of two
    assert module_0.greatest_common_divisor(64, 32) == 32
    assert module_0.greatest_common_divisor(1024, 512) == 512

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()

# Generated at 2026-11-03 02:26:14.550141
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(12, 36) == 12

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(101, 103) == 1

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(100, 100) == 100

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # One divides the other
    assert module_0.greatest_common_divisor(10, 50) == 10
    assert module_0.greatest_common_divisor(50, 10) == 10

    # Larger numbers (classic Euclid example)
    assert module_0.greatest_common_divisor(1071, 462) == 21

    # Negative inputs (result magnitude should match positive gcd)
    assert abs(module_0.greatest_common_divisor(-48, 18)) == 6
    assert abs(module_0.greatest_common_divisor(48, -18)) == 6
    assert abs(module_0.greatest_common_divisor(-48, -18)) == 6

    # Cross-check against math.gcd on a range of values
    for x in range(0, 50):
        for y in range(0, 50):
            assert abs(module_0.greatest_common_divisor(x, y)) == math.gcd(x, y)

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()