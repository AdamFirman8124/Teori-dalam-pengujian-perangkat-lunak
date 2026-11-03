

# Generated at 2026-11-03 04:52:39.118600
# Unit test for function specialFilter
def test_specialFilter():
    # Numbers > 10 with both first and last digits odd
    assert module_0.specialFilter([15, 33, 73, 97]) == 4
    assert module_0.specialFilter([11, 13, 17, 19, 31]) == 5

    # Numbers > 10 but with even first or last digit
    assert module_0.specialFilter([12, 14, 20, 22, 24]) == 0
    assert module_0.specialFilter([21, 23, 29]) == 0  # first digit even
    assert module_0.specialFilter([30, 50, 70]) == 0  # last digit even

    # Numbers <= 10 should not count even if digits are odd
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0
    assert module_0.specialFilter([9, 10]) == 0

    # Boundary case: 11 is the smallest valid number
    assert module_0.specialFilter([10, 11]) == 1

    # Mixed list
    assert module_0.specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99]) == 5
    assert module_0.specialFilter([15, -2, 10, 13, 8, 97]) == 3

    # Larger numbers
    assert module_0.specialFilter([111, 135, 357, 979]) == 4
    assert module_0.specialFilter([100, 102, 110]) == 0

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Single element lists
    assert module_0.specialFilter([15]) == 1
    assert module_0.specialFilter([16]) == 0

    print("All tests passed!")

# Generated at 2026-11-03 04:54:58.591557
# Unit test for function specialFilter
def test_specialFilter():
    # Typical cases
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # All single-digit odd numbers (not > 10)
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0

    # All qualifying two-digit odd numbers
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5

    # Even first or last digits excluded
    assert module_0.specialFilter([12, 14, 16, 18, 20]) == 0
    assert module_0.specialFilter([21, 41, 61]) == 0

    # Boundary: 10 is not > 10
    assert module_0.specialFilter([10, 20, 30]) == 0

    # Negative numbers never qualify
    assert module_0.specialFilter([-11, -13, -15]) == 0

    # Multi-digit numbers with odd first/last digits
    assert module_0.specialFilter([101, 103, 105]) == 3
    assert module_0.specialFilter([91, 93, 95, 97, 99]) == 5

    # Mixed case
    assert module_0.specialFilter([57, 88, -109, 2, 75, 10]) == 3


if __name__ == "__main__":
    test_specialFilter()
    print("All tests passed!")

# Generated at 2026-11-03 04:56:48.167732
# Unit test for function specialFilter
def test_specialFilter():
    # Basic cases with mixed positive/negative numbers
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Numbers not greater than 10 are excluded
    assert module_0.specialFilter([1, 3, 5, 7, 9, 10, -11]) == 0

    # Single qualifying number
    assert module_0.specialFilter([11]) == 0  # first digit 1 is odd, last digit 1 is odd, but 11 > 10 -> wait, 11 qualifies

# Generated at 2026-11-03 04:59:23.918745
# Unit test for function specialFilter
def test_specialFilter():
    # Empty list
    assert module_0.specialFilter([]) == 0

    # No numbers greater than 10
    assert module_0.specialFilter([5, -2, 1, -5]) == 0

    # Only one qualifying number (15: starts with 1, ends with 5)
    assert module_0.specialFilter([15, -73, 14, -15]) == 1

    # Two qualifying numbers (33 and 109)
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Numbers greater than 10 but with even first/last digits
    assert module_0.specialFilter([12, 14, 16, 20]) == 0

    # Numbers with odd first digit but even last digit
    assert module_0.specialFilter([31, 51, 71]) == 0

    # Numbers with even first digit but odd last digit
    assert module_0.specialFilter([23, 45, 67]) == 0

    # All numbers qualify
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5

    # Boundary: 10 is not greater than 10, 11 qualifies
    assert module_0.specialFilter([10, 11]) == 1

    # Larger numbers
    assert module_0.specialFilter([135, 357, 579, 975, 246]) == 4

    print("All test cases passed!")


test_specialFilter()