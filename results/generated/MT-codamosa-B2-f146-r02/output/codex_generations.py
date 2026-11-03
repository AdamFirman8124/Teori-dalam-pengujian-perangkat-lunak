

# Generated at 2026-11-02 00:12:18.202356
# Unit test for function specialFilter
def test_specialFilter():
    # Basic examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1   # only 15 qualifies
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 3  # 33, 45, 109 qualify

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Boundary: must be strictly greater than 10
    assert module_0.specialFilter([10]) == 0
    assert module_0.specialFilter([11]) == 1

    # Even digits disqualify
    assert module_0.specialFilter([12]) == 0   # last digit even
    assert module_0.specialFilter([21]) == 0   # first digit even
    assert module_0.specialFilter([22, 44, 68, 80]) == 0

    # All qualify
    assert module_0.specialFilter([13, 17, 19, 31]) == 4

    # Negatives are never > 10, so excluded
    assert module_0.specialFilter([-31, -57, -3, -15]) == 0

    # Multi-digit numbers with odd first/last digits
    assert module_0.specialFilter([111, 135, 79]) == 3

    # Single digits are not > 10
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0

    # Mixed bag
    assert module_0.specialFilter([97, 53, 60, -75, 100, 101]) == 3  # 97, 53, 101

    print("All test cases passed!")


if __name__ == "__main__":
    test_specialFilter()

# Generated at 2026-11-02 00:13:18.718961
# Unit test for function specialFilter
def test_specialFilter():
    # Empty list returns 0
    assert module_0.specialFilter([]) == 0

    # All elements match: > 10 with odd first and last digits
    assert module_0.specialFilter([15, 33, 71, 97]) == 4

    # First digit even -> not counted
    assert module_0.specialFilter([21, 23, 29]) == 0

    # Last digit even -> not counted
    assert module_0.specialFilter([12, 14, 16]) == 0

    # Mixed list: only 11, 33, 55 qualify
    assert module_0.specialFilter([11, 22, 33, 44, 55]) == 3

    # Numbers <= 10 never counted, even with odd digits
    assert module_0.specialFilter([1, 3, 5, 7, 9, 10]) == 0

    # Multi-digit numbers checked via string indexing
    assert module_0.specialFilter([135, 357, 246, 79]) == 3

    # Single matching element
    assert module_0.specialFilter([111]) == 1

    # Boundary value 10 itself excluded
    assert module_0.specialFilter([10, 11]) == 1


test_specialFilter()
print("All tests passed!")

# Generated at 2026-11-02 00:14:18.214082
# Unit test for function specialFilter
def test_specialFilter():
    # Classic examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1          # only 15 qualifies
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2   # 33 and 109 qualify

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Numbers <= 10 are excluded even if all digits are odd
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0
    assert module_0.specialFilter([9]) == 0

    # Boundary at 10
    assert module_0.specialFilter([10]) == 0
    assert module_0.specialFilter([11]) == 1

    # Even first digit excluded
    assert module_0.specialFilter([21, 23, 27, 29]) == 0

    # Even last digit excluded
    assert module_0.specialFilter([12, 14, 16, 18]) == 0

    # Both first and last digits odd
    assert module_0.specialFilter([13, 17, 19]) == 3

    # Multi-digit numbers
    assert module_0.specialFilter([135, 977, 246, 1002, 555]) == 3  # 135, 977, 555 qualify
    assert module_0.specialFilter([999999, 1000001, 1000000]) == 2  # 999999, 1000001 qualify

    # Negative numbers are never > 10
    assert module_0.specialFilter([-15, -33, -57, -11]) == 0

    # Mixed positives and negatives
    assert module_0.specialFilter([-13, 12, 31, 44]) == 1           # only 31 qualifies

    # Duplicates are counted individually
    assert module_0.specialFilter([15, 15, 15]) == 3
# nonce:596ccc49

# Generated at 2026-11-02 00:15:15.149034
# Unit test for function specialFilter
def test_specialFilter():
# nonce:4759aba0
    # Basic example: only 43 qualifies (> 10, starts and ends with odd digit)
    assert module_0.specialFilter([5, -2, 1, 43]) == 1

    # Empty list returns 0
    assert module_0.specialFilter([]) == 0

    # All two-digit numbers with odd first and last digits
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5

    # All even digits, none qualify
    assert module_0.specialFilter([20, 22, 24, 26, 28]) == 0

    # Odd first digit but even last digit
    assert module_0.specialFilter([21, 41, 61, 81]) == 0

    # Even first digit but odd last digit
    assert module_0.specialFilter([12, 34, 56, 78]) == 0

    # Boundary: 10 itself does not count (> 10 required)
    assert module_0.specialFilter([10]) == 0

    # Smallest qualifying value
    assert module_0.specialFilter([11]) == 1

    # Multi-digit numbers
    assert module_0.specialFilter([101, 303, 505, 707, 909]) == 5
    assert module_0.specialFilter([123, 145, 167]) == 3
    assert module_0.specialFilter([100, 200, 300]) == 0

    # Mixed results
    assert module_0.specialFilter([33, 44, 55, 66, 77]) == 3
    assert module_0.specialFilter([9, 10, 11, 12, 13]) == 2

    # Large numbers
    assert module_0.specialFilter([999, 1000, 1001]) == 1

    print("All tests passed!")

# Generated at 2026-11-02 00:16:13.312636
# Unit test for function specialFilter
def test_specialFilter():
    # nonce:8486e6a0
    assert module_0.specialFilter([5, -2, 1, 43]) == 0
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert module_0.specialFilter([43, -12, 93, 125, 121, 101]) == 4
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([22, 44, 66]) == 0
    assert module_0.specialFilter([13, 17, 19]) == 3
    assert module_0.specialFilter([10, 12, 20]) == 0
    assert module_0.specialFilter([135, 357, 579]) == 3
    assert module_0.specialFilter([31, 51, 71]) == 3
    assert module_0.specialFilter([2, 4, 6, 8]) == 0