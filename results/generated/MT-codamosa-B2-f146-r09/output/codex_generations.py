

# Generated at 2026-11-03 01:20:57.507618
# Unit test for function specialFilter
def test_specialFilter():
    # Numbers <= 10 are ignored, even if odd
    assert module_0.specialFilter([5, -2, 1, -5]) == 0

    # Only 15 qualifies (starts and ends with odd digit)
    assert module_0.specialFilter([15, -73, 14, -15]) == 1

    # 33 and 109 qualify; 45 and 21 have even digits
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Single qualifying element
    assert module_0.specialFilter([11]) == 1

    # First digit odd but last digit even
    assert module_0.specialFilter([13, 17, 19]) == 3

    # Last digit odd but first digit even
    assert module_0.specialFilter([21, 41, 61]) == 0

    # Boundary: exactly 10 is not counted, 11 is
    assert module_0.specialFilter([10, 11, 12]) == 1

    # Larger numbers
    assert module_0.specialFilter([135, 357, 579, 975, 246]) == 4

    # Negative number with odd digits but not greater than 10
    assert module_0.specialFilter([-33, -55]) == 0

# Generated at 2026-11-03 01:22:23.522556
# Unit test for function specialFilter
def test_specialFilter():
    # Typical case: only numbers > 10 with odd first and last digits count
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # All numbers qualify (first and last digits odd, value > 10)
    assert module_0.specialFilter([11, 13, 57, 91]) == 4
    assert module_0.specialFilter([111, 133, 155]) == 3

    # Last digit even -> not counted
    assert module_0.specialFilter([12, 14, 18, 20]) == 0

    # First digit even -> not counted
    assert module_0.specialFilter([21, 23, 27, 29]) == 0

    # Numbers not greater than 10 -> not counted
    assert module_0.specialFilter([10, 9, 3, 5, -1]) == 0

    # All two-digit numbers with odd first/last digits
    assert module_0.specialFilter([97, 99, 95]) == 3

    # Mixed qualifying and non-qualifying values
    assert module_0.specialFilter([11, 12, 13, 22, 33, 44, 55]) == 4

    print("All tests passed!")


test_specialFilter()

# Generated at 2026-11-03 01:23:38.277698
# Unit test for function specialFilter
def test_specialFilter():
    # Basic case: numbers > 10 with odd first and last digits
    assert module_0.specialFilter([15, 33, 57, 79]) == 4

    # Numbers <= 10 should not be counted even with odd digits
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0

    # Numbers > 10 but with even first or last digit
    assert module_0.specialFilter([12, 22, 24, 40, 88]) == 0

    # Mixed list
    assert module_0.specialFilter([15, -2, 33, 11, 10, 12, 57]) == 4

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Boundary: 10 itself is not greater than 10
    assert module_0.specialFilter([10]) == 0

    # Smallest qualifying number is 11
    assert module_0.specialFilter([11]) == 1

    # Multi-digit numbers with odd first and last digits
    assert module_0.specialFilter([101, 135, 1357, 91359]) == 4

    # Multi-digit numbers with even digits at edges
    assert module_0.specialFilter([210, 5558, 825]) == 0

    # No qualifying numbers
    assert module_0.specialFilter([2, 4, 6, 8, 20, 22]) == 0

    # All qualifying numbers
    assert module_0.specialFilter([11, 13, 17, 19, 31, 33, 39]) == 7

    # Large numbers
    assert module_0.specialFilter([123456789, 987654321, 2468642]) == 2

    print("All tests passed!")


test_specialFilter()

# Generated at 2026-11-03 01:25:34.805016
# Unit test for function specialFilter
def test_specialFilter():
    # Test with typical cases
    assert module_0.specialFilter([15, -73, 14, -15]) == 1  # only 15 qualifies
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109 qualify
    
    # Test with empty list
    assert module_0.specialFilter([]) == 0
    
    # Test with numbers not greater than 10
    assert module_0.specialFilter([5, -11, 10, -15]) == 0  # none are > 10
    
    # Test with all qualifying numbers
    assert module_0.specialFilter([11, 13, 17, 19, 31, 33, 35, 37, 39]) == 9
    
    # Test with no qualifying numbers
    assert module_0.specialFilter([12, 14, 20, 22, 24, 30]) == 0
    
    # Test with mixed even/odd first and last digits
    assert module_0.specialFilter([23, 45, 67, 89, 101, 111]) == 3  # 67, 89, 111 qualify
    
    # Test with negative qualifying numbers (should be excluded as not > 10)
    assert module_0.specialFilter([-13, -17, -19]) == 0
    
    # Test with multi-digit numbers
    assert module_0.specialFilter([135, 357, 579, 791, 913]) == 5
    
    print("All test cases passed!")


# Run the tests
if __name__ == "__main__":
    test_specialFilter()

# Generated at 2026-11-03 01:26:42.805699
# Unit test for function specialFilter
def test_specialFilter():
    # Basic cases from typical examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Numbers not greater than 10
    assert module_0.specialFilter([1, 3, 5, 7, 9, -11, -13]) == 0

    # Exactly 10 or numbers ending in even digits
    assert module_0.specialFilter([10, 12, 14, 16, 18]) == 0

    # Numbers starting with even digits
    assert module_0.specialFilter([21, 23, 25, 29]) == 0

    # All two-digit numbers with odd first and last digits
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5

    # Multi-digit numbers
    assert module_0.specialFilter([111, 133, 199, 357, 979]) == 5
    assert module_0.specialFilter([101, 303, 505]) == 3

    # Mixed valid and invalid
    assert module_0.specialFilter([20, 22, 33, 44, 55, 66, 77, 88, 99]) == 4

    # Large numbers
    assert module_0.specialFilter([13579]) == 1
    assert module_0.specialFilter([13578]) == 0