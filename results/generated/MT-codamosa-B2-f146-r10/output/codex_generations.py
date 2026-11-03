

# Generated at 2026-11-02 12:06:10.259538
# Unit test for function specialFilter

# Generated at 2026-11-02 12:06:52.102255
# Unit test for function specialFilter
def test_specialFilter():assert module_0.specialFilter([15, -73, 14, -15]) == 1

# Generated at 2026-11-02 12:07:15.128392
# Unit test for function specialFilter
def test_specialFilter():
    # Check some simple cases
    assert module_0.specialFilter([5, -2, 1, 43]) == 0  # 43 starts with even digit 4
    assert module_0.specialFilter([15, -73, 14, -15]) == 1  # only 15 has odd first and last digits
    assert module_0.specialFilter([33, 111, 97, 79]) == 4
    assert module_0.specialFilter([]) == 0

    # Edge cases: numbers not greater than 10 are ignored even if digits are odd
    assert module_0.specialFilter([1, 3, 5, 7, 9, 10]) == 0

    # All qualifying numbers
    assert module_0.specialFilter([11, 13, 15, 17, 19, 31, 111]) == 7

    # None qualify: even first or last digits
    assert module_0.specialFilter([20, 22, 24, 26, 28]) == 0
    assert module_0.specialFilter([12, 14, 16, 18]) == 0

    # Mixed list
    assert module_0.specialFilter([10, 11, 12, 13, 100, 135, 246]) == 3  # 11, 13, 135

    # Multi-digit edge: 100 ends in 0 (even)
    assert module_0.specialFilter([101]) == 1  # first 1, last 1
    assert module_0.specialFilter([999]) == 1
    assert module_0.specialFilter([219, 431, 813]) == 0  # first digits even

# Generated at 2026-11-02 12:08:03.326765
# Unit test for function specialFilter
def test_specialFilter():
    # Basic example cases
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # No numbers greater than 10 (including negatives, which are skipped)
    assert module_0.specialFilter([1, 3, 5, 7, 9, -11, -13]) == 0

    # Greater than 10 but even first or last digits
    assert module_0.specialFilter([12, 14, 20, 22, 24, 30]) == 0

    # Odd first digit but even last digit
    assert module_0.specialFilter([10, 12, 14, 16, 18, 30, 50]) == 0

    # Even first digit but odd last digit
    assert module_0.specialFilter([21, 23, 29, 41, 87]) == 0

    # Boundary value: exactly 10 is excluded
    assert module_0.specialFilter([10]) == 0

    # Smallest qualifying number
    assert module_0.specialFilter([11]) == 1

    # All qualifying teen numbers
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5

    # Multi-digit numbers with odd first and last digits
    assert module_0.specialFilter([101, 135, 357, 791, 939]) == 5

    # Mixed list
    assert module_0.specialFilter([10, 11, 12, 13, 20, 21, 22, 33, 44, 55, 100, 101]) == 5


if __name__ == "__main__":
    test_specialFilter()
    print("All tests passed!")

# Generated at 2026-11-02 12:09:52.447284
# Unit test for function specialFilter
def test_specialFilter():
    # Basic examples from the problem description
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # No numbers greater than 10
    assert module_0.specialFilter([1, 3, 5, 7, 9, -11, 10]) == 0

    # All numbers qualify
    assert module_0.specialFilter([11, 13, 15, 17, 19, 31, 97]) == 7

    # Numbers with even first or last digit are excluded
    assert module_0.specialFilter([21, 23, 12, 14, 100, 200]) == 0

    # Large numbers with odd first and last digits
    assert module_0.specialFilter([111, 13579, 97531, 12345]) == 3

    # Mixed positive and negative numbers
    assert module_0.specialFilter([-15, -37, 15, 37]) == 2

    # Exactly 10 should not count (not greater than 10)
    assert module_0.specialFilter([10]) == 0

    # 11 is the smallest qualifying number
    assert module_0.specialFilter([11]) == 1

# Generated at 2026-11-02 12:11:06.620841
# Unit test for function specialFilter
def test_specialFilter():
    # Basic example cases
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Numbers <= 10 are excluded even if digits are odd
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0

    # Boundary: 10 excluded, 11 included (first and last digits odd)
    assert module_0.specialFilter([10, 11]) == 1

    # All numbers qualify
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5

    # First digit even -> excluded
    assert module_0.specialFilter([21, 23, 25, 29]) == 0

    # Last digit even -> excluded
    assert module_0.specialFilter([31, 32, 33]) == 1

    # Last digit zero -> excluded
    assert module_0.specialFilter([100, 110, 130]) == 0

    # Multi-digit mixed list
    assert module_0.specialFilter([111, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == 5

    # Large numbers with odd first/last digits
    assert module_0.specialFilter([135, 357, 579, 979]) == 4

    # Negative numbers are excluded (not > 10)
    assert module_0.specialFilter([-11, -13, -15]) == 0

    # Duplicates are counted individually
    assert module_0.specialFilter([11, 11, 11]) == 3

    # Combination of qualifying and non-qualifying values
    assert module_0.specialFilter([2, 12, 14, 93, 101, 111, -33]) == 3

    print("All test cases passed!")


test_specialFilter()