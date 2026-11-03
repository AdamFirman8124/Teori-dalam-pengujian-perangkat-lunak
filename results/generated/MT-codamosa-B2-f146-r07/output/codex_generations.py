

# Generated at 2026-11-03 05:02:09.086958
# Unit test for function specialFilter
def test_specialFilter():
    # Basic cases with mixed positive/negative numbers
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Numbers not greater than 10 are excluded
    assert module_0.specialFilter([1, 3, 5, 7, 9, 10]) == 0
    assert module_0.specialFilter([-11, 0, 10]) == 0

    # Both first and last digits must be odd
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5
    assert module_0.specialFilter([12, 14, 16, 18]) == 0   # last digit even
    assert module_0.specialFilter([21, 31, 41, 81]) == 0   # first digit even

    # Multi-digit numbers
    assert module_0.specialFilter([111, 135, 357, 979]) == 4
    assert module_0.specialFilter([100, 110, 130]) == 0    # ends in 0
    assert module_0.specialFilter([999]) == 1

    # Larger mixed set
    assert module_0.specialFilter([15, 33, 57, 79, 97, 99, 20, 44, 68]) == 6

    # Single valid element
    assert module_0.specialFilter([71]) == 1

# Generated at 2026-11-03 05:03:44.724973
# Unit test for function specialFilter
def test_specialFilter():
    # Test with mixed positive and negative numbers
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    
    # Test with numbers where first and last digits are odd
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2
    
    # Test with empty list
    assert module_0.specialFilter([]) == 0
    
    # Test with numbers less than or equal to 10
    assert module_0.specialFilter([1, 3, 5, 7, 9, 10]) == 0
    
    # Test with all valid numbers
    assert module_0.specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]) == 25
    
    # Test with numbers having even first or last digits
    assert module_0.specialFilter([12, 14, 16, 18, 21, 23, 25, 27, 29]) == 0
    
    # Test with larger numbers
    assert module_0.specialFilter([135, 357, 579, 791, 913]) == 5
    
    # Test with single valid number
    assert module_0.specialFilter([97]) == 1
    
    # Test with numbers just above 10
    assert module_0.specialFilter([11, 12, 13]) == 2

# Generated at 2026-11-03 05:06:26.409617
# Unit test for function specialFilter
def test_specialFilter():
    # Basic examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # No numbers greater than 10
    assert module_0.specialFilter([1, 3, 5, 7, 9, 10, -11]) == 0

    # Numbers with even first or last digit are excluded
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5
    assert module_0.specialFilter([12, 14, 16, 18, 20]) == 0
    assert module_0.specialFilter([21, 23, 25, 27, 29]) == 0
    assert module_0.specialFilter([31, 33, 35, 37, 39]) == 5

    # Exactly 10 is excluded (not > 10)
    assert module_0.specialFilter([10]) == 0

    # Negative numbers are excluded even if digits are odd
    assert module_0.specialFilter([-11, -13, -19]) == 0

    # Multi-digit numbers with odd first and last digits
    assert module_0.specialFilter([111, 133, 155, 177, 199]) == 5
    assert module_0.specialFilter([101, 121, 141]) == 0

    # Large numbers
    assert module_0.specialFilter([98765, 12345, 55555]) == 2

    # Mixed list
    assert module_0.specialFilter([15, 22, 33, 44, 55, 66, 77, 88, 99]) == 4

# Generated at 2026-11-03 05:10:10.578634
# Unit test for function specialFilter
def test_specialFilter():
    # Test with mixed numbers: 15 and 33 have odd first/last digits and > 10
    assert module_0.specialFilter([15, 33, 21, 26]) == 2

    # Test with a larger set
    assert module_0.specialFilter([152, 323, 142, 187, 191]) == 3

    # Test with empty list
    assert module_0.specialFilter([]) == 0

    # Test where no numbers qualify
    assert module_0.specialFilter([12, 24, 30, 68]) == 0

    # Test with numbers <= 10 (should be excluded even if digits are odd)
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0

    # Test with single qualifying number
    assert module_0.specialFilter([11]) == 1

    # Test boundary: numbers just above 10
    assert module_0.specialFilter([10, 11, 12, 13]) == 2

    # Test larger numbers
    assert module_0.specialFilter([135, 357, 579, 913, 791]) == 5

    # Test with all qualifying numbers
    assert module_0.specialFilter([11, 13, 17, 19, 31]) == 5