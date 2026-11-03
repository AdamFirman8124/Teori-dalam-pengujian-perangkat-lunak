

# Generated at 2026-11-02 22:36:07.299882
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(144, 60) == 12

    # One number divides the other (order-independent)
    assert module_0.greatest_common_divisor(10, 5) == 5
    assert module_0.greatest_common_divisor(5, 10) == 5
    assert module_0.greatest_common_divisor(100, 25) == 25

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(1, 1) == 1

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative inputs (magnitude of result is the GCD)
    assert abs(module_0.greatest_common_divisor(-12, 18)) == 6
    assert abs(module_0.greatest_common_divisor(12, -18)) == 6
    assert abs(module_0.greatest_common_divisor(-12, -18)) == 6
    assert abs(module_0.greatest_common_divisor(-5, -10)) == 5

    # Larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**20, 2**15) == 2**15

    # Commutativity check
    assert module_0.greatest_common_divisor(462, 1071) == module_0.greatest_common_divisor(1071, 462)

    print("All tests passed!")


test_greatest_common_divisor()

# Generated at 2026-11-02 22:37:51.159562
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic positive cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6  # order shouldn't matter
    assert module_0.greatest_common_divisor(12, 8) == 4
    assert module_0.greatest_common_divisor(8, 12) == 4
    assert module_0.greatest_common_divisor(100, 75) == 25

    # One number divides the other
    assert module_0.greatest_common_divisor(10, 5) == 5
    assert module_0.greatest_common_divisor(5, 10) == 5
    assert module_0.greatest_common_divisor(21, 7) == 7

    # Coprime numbers (GCD is 1)
    assert module_0.greatest_common_divisor(7, 13) == 1
    assert module_0.greatest_common_divisor(17, 4) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # Prime numbers
    assert module_0.greatest_common_divisor(13, 17) == 1

    # Same numbers
    assert module_0.greatest_common_divisor(5, 5) == 5
    assert module_0.greatest_common_divisor(100, 100) == 100

    # Zero cases
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(270, 192) == 6

    print("All test cases passed!")


test_greatest_common_divisor()

# Generated at 2026-11-02 22:39:37.350933
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
# nonce:c6b1cc0f
    # Basic cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6

    # Coprime numbers
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(7, 13) == 1

    # One divides the other
    assert module_0.greatest_common_divisor(12, 36) == 12
    assert module_0.greatest_common_divisor(36, 12) == 12

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7

    # One is 1
    assert module_0.greatest_common_divisor(1, 999) == 1

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative numbers
    assert module_0.greatest_common_divisor(-48, 18) == 6
    assert abs(module_0.greatest_common_divisor(48, -18)) == 6
    assert abs(module_0.greatest_common_divisor(-48, -18)) == 6

    # Larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2 ** 20, 2 ** 15) == 2 ** 15

    # Cross-check against math.gcd over a range of values
    for x in range(-20, 21):
        for y in range(-20, 21):
            assert abs(module_0.greatest_common_divisor(x, y)) == math.gcd(x, y), (x, y)

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()

# Generated at 2026-11-02 22:40:41.552304
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6

    # Equal numbers
    assert module_0.greatest_common_divisor(12, 12) == 12

    # One operand is zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5

    # Both zero
    assert module_0.greatest_common_divisor(0, 0) == 0

    # One divides the other
    assert module_0.greatest_common_divisor(7, 21) == 7
    assert module_0.greatest_common_divisor(21, 7) == 7

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1

    # Larger classic case
    assert module_0.greatest_common_divisor(1071, 462) == 21

    # Consecutive integers are always coprime
    assert module_0.greatest_common_divisor(1000000, 999999) == 1

    # Commutativity check
    assert module_0.greatest_common_divisor(48, 18) == module_0.greatest_common_divisor(18, 48)

# Generated at 2026-11-02 22:42:45.253308
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(1071, 462) == 21

    # One number divides the other
    assert module_0.greatest_common_divisor(10, 5) == 5
    assert module_0.greatest_common_divisor(5, 10) == 5

    # Identical numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(1, 1) == 1

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(13, 8) == 1

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative input
    assert module_0.greatest_common_divisor(-4, 6) == 2

    # Large numbers
    assert module_0.greatest_common_divisor(2**20, 2**15) == 2**15

    # Commutativity property: gcd(a, b) == gcd(b, a)
    assert module_0.greatest_common_divisor(48, 18) == module_0.greatest_common_divisor(18, 48)