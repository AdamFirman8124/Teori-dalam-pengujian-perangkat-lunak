

# Generated at 2026-11-02 22:54:41.452575
# Unit test for function digits
def test_digits():
    # Single odd digit
    assert module_0.digits(1) == 1
    assert module_0.digits(3) == 3
    assert module_0.digits(5) == 5
    assert module_0.digits(7) == 7
    assert module_0.digits(9) == 9

    # No odd digits -> 0
    assert module_0.digits(0) == 0
    assert module_0.digits(4) == 0
    assert module_0.digits(22) == 0
    assert module_0.digits(2468) == 0
    assert module_0.digits(888) == 0

    # Mixed even and odd digits -> product of odd digits
    assert module_0.digits(12) == 1
    assert module_0.digits(235) == 15
    assert module_0.digits(2357) == 105
    assert module_0.digits(12345) == 15
    assert module_0.digits(13579) == 945
    assert module_0.digits(2461) == 1
    assert module_0.digits(455) == 25
    assert module_0.digits(999) == 729
    assert module_0.digits(105) == 5

    # Large numbers
    assert module_0.digits(123456789) == 945

    print("All tests passed!")


if __name__ == "__main__":
    test_digits()

# Generated at 2026-11-02 22:59:12.910585
# Unit test for function digits
def test_digits():
    # Single odd digit
    assert module_0.digits(1) == 1
    assert module_0.digits(3) == 3
    assert module_0.digits(7) == 7

    # Single even digit -> no odd digits, return 0
    assert module_0.digits(4) == 0
    assert module_0.digits(0) == 0
    assert module_0.digits(8) == 0

    # Mixed digits: only odd digits contribute to product
    assert module_0.digits(235) == 15      # 3 * 5
    assert module_0.digits(123456) == 15   # 1 * 3 * 5
    assert module_0.digits(2468) == 0      # all even

    # Repeated odd digits
    assert module_0.digits(111) == 1
    assert module_0.digits(999) == 729
    assert module_0.digits(333) == 27

    # Digit 1 is odd and multiplies as identity
    assert module_0.digits(12) == 1
    assert module_0.digits(1246) == 1

    # Larger numbers
    assert module_0.digits(579) == 315     # 5 * 7 * 9
    assert module_0.digits(1202468) == 1   # only odd digit is 1

    print("All tests passed!")

test_digits()