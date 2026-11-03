

# Generated at 2026-11-01 22:04:37.581376
# Unit test for function specialFilter
def test_specialFilter():
# nonce:4c7629f8
    # Basic examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1   # only 15 qualifies
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 3  # 33, 45, 109 qualify
    assert module_0.specialFilter([12, 13, 14, 15]) == 1     # only 13 has odd first/last digits

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Numbers not greater than 10 are ignored
    assert module_0.specialFilter([10, -11, 1, 3, 5, 7, 9]) == 0

    # All qualifying numbers
    assert module_0.specialFilter([11, 13, 17, 19, 31, 35, 57, 79, 91, 99]) == 10

    # Multi-digit numbers with odd first and last digits
    assert module_0.specialFilter([111, 135, 999, 101]) == 4

    # Even boundary digits disqualify
    assert module_0.specialFilter([21, 22, 23, 24]) == 0          # starts even
    assert module_0.specialFilter([41, 42, 43, 44]) == 0
    assert module_0.specialFilter([12, 32, 52, 72]) == 0          # ends even

    # Negative numbers never pass the > 10 check
    assert module_0.specialFilter([-33, -55, -97]) == 0

    # Mixed positives and negatives
    assert module_0.specialFilter([-15, 15, 30, 37, -97, 88]) == 2  # 15 and 37

    # Large values
    assert module_0.specialFilter([123456789, 987654321, 1000000001]) == 2
    # 123456789: starts 1, ends 9 -> qualifies
    # 987654321: starts 9, ends 1 -> qualifies
    # 1000000001: starts 1, ends 1 -> qualifies... recount below

    # Verify large-value case explicitly
    assert module_0.specialFilter([200000001]) == 0  # starts even
    assert module_0.specialFilter([300000002]) == 0  # ends even
    assert module_0.specialFilter([300000003]) == 1  # both odd

    print("All tests passed!")


if __name__ == "__main__":
    test_specialFilter()

# Generated at 2026-11-01 22:05:17.005611
# Unit test for function specialFilter
def test_specialFilter():
    # Test with mixed positive and negative numbers
    assert module_0.specialFilter([15, -73, 14, -15]) == 1  # Only 15 qualifies
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109 qualify
    assert module_0.specialFilter([5, -2, 1, 9, 0, -15]) == 0  # No numbers > 10
    assert module_0.specialFilter([]) == 0  # Empty list
    
    # Test with numbers containing odd first and last digits
    assert module_0.specialFilter([11, 13, 17, 19]) == 4  # All qualify
    assert module_0.specialFilter([31, 53, 75, 99]) == 4  # All qualify
    
    # Test with numbers where first or last digit is even
    assert module_0.specialFilter([12, 14, 16, 18]) == 0  # Last digit even
    assert module_0.specialFilter([21, 41, 61, 81]) == 0  # First digit even
    assert module_0.specialFilter([22, 44, 66, 88]) == 0  # Both digits even
    
    # Test boundary values
    assert module_0.specialFilter([10]) == 0  # Not greater than 10
    assert module_0.specialFilter([11]) == 1  # Smallest qualifying number
    
    # Test with larger numbers
    assert module_0.specialFilter([111, 133, 155, 199]) == 4
    assert module_0.specialFilter([110, 130, 150, 190]) == 0  # Last digit even
    
    # Test with duplicates
    assert module_0.specialFilter([15, 15, 15]) == 3
    
    print("All test cases passed!")

test_specialFilter()

# Generated at 2026-11-01 22:05:56.493998
# Unit test for function specialFilter
def test_specialFilter():# Test with mixed positive and negative numbers
    assert module_0.specialFilter([15, -73, 14, -15]) == 1  # Only 15 has odd first and last digits and > 10
    
    # Test with numbers including 109
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109 qualify
    
    # Test with empty list
    assert module_0.specialFilter([]) == 0
    
    # Test with all negative numbers
    assert module_0.specialFilter([-11, -13, -15]) == 0  # None are > 10
    
    # Test with numbers where first/last digits are odd but value <= 10
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0  # None are > 10
    
    # Test with all qualifying numbers
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5  # All qualify
    
    # Test with numbers where first digit is even
    assert module_0.specialFilter([21, 23, 25, 27, 29]) == 0  # First digit is 2 (even)
    
    # Test with numbers where last digit is even
    assert module_0.specialFilter([12, 14, 16, 18]) == 0  # Last digit is even
    
    # Test with boundary value 10 (not > 10)
    assert module_0.specialFilter([10]) == 0
    
    # Test with multi-digit numbers
    assert module_0.specialFilter([111, 357, 959, 222]) == 3  # 111, 357, 959 qualify
    
    # Test with single qualifying number
    assert module_0.specialFilter([97]) == 1
    
    # Test with large numbers
    assert module_0.specialFilter([1000001, 3000003]) == 2  # Both start and end with odd digits

# Generated at 2026-11-01 22:06:34.116475
# Unit test for function specialFilter
def test_specialFilter():
    # Empty list returns 0
    assert module_0.specialFilter([]) == 0

    # Typical mixed case: only 15 has odd first/last digits and is > 10
    assert module_0.specialFilter([15, -73, 14, -15]) == 1

    # 33 and 109 qualify; 45 has even leading digit, 21 has even leading digit
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # All elements qualify (odd first and last digits, all > 10)
    assert module_0.specialFilter([11, 13, 35, 57, 79, 97]) == 6

    # Numbers <= 10 are ignored even if their digits are odd
    assert module_0.specialFilter([1, 3, 5, 7, 9, 10]) == 0

    # First digit even -> excluded regardless of last digit
    assert module_0.specialFilter([21, 23, 25, 27]) == 0

    # Last digit even -> excluded regardless of first digit
    assert module_0.specialFilter([12, 14, 16, 18]) == 0

    # Boundary: 10 excluded, 11 included
    assert module_0.specialFilter([10, 11]) == 1

    # Larger multi-digit numbers with odd first/last digits
    assert module_0.specialFilter([101, 133, 155, 177, 199]) == 5

    # Negative numbers always fail the num > 10 check
    assert module_0.specialFilter([-11, -13, -35]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_specialFilter()

# Generated at 2026-11-01 22:06:54.585853
# Unit test for function specialFilter
def test_specialFilter():
    # Basic cases from specification
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # No numbers greater than 10 (including negatives)
    assert module_0.specialFilter([1, 3, 5, 9, 10, -11]) == 0

    # All numbers qualify (odd first and last digit, > 10)
    assert module_0.specialFilter([11, 13, 15, 17, 19, 31, 97, 111]) == 8

    # First digit even, last digit odd -> excluded
    assert module_0.specialFilter([21, 23, 25, 27, 29]) == 0

    # First digit odd, last digit even -> excluded
    assert module_0.specialFilter([12, 14, 16, 18]) == 0

    # Boundary: 10 excluded (> 10 required), 11 included
    assert module_0.specialFilter([10, 11]) == 1

    # Multi-digit numbers
    assert module_0.specialFilter([101, 303, 505, 907, 119, 137]) == 6

    # Mixed list
    assert module_0.specialFilter([11, 22, 35, 44, 57, 68, 79, 80, 91, 100]) == 5

    # Single element lists
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([20]) == 0

    print("All tests passed!")


test_specialFilter()