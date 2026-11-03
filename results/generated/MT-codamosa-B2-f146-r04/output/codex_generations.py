

# Generated at 2026-11-02 11:18:17.010054
# Unit test for function specialFilter
def test_specialFilter():
    # Empty list
    assert module_0.specialFilter([]) == 0

    # No numbers greater than 10
    assert module_0.specialFilter([5, -2, -3, 0]) == 0

    # Only 15 qualifies (first digit 1, last digit 5, both odd)
    assert module_0.specialFilter([15, -73, 14, -15]) == 1

    # 33 and 109 qualify (45 starts with even digit, 21 starts with even digit)
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # 111, 13, 15, 19, 31, 99 qualify (29 and 45 start with even digits)
    assert module_0.specialFilter([111, 13, 15, 19, 29, 31, 45, 99]) == 6

    # Single qualifying number
    assert module_0.specialFilter([11]) == 1

    # Numbers > 10 but with even first/last digits
    assert module_0.specialFilter([10, 12, 14, 20, 22]) == 0

    # All qualify
    assert module_0.specialFilter([97, 53]) == 2

    # Boundary: numbers equal to 10 are excluded
    assert module_0.specialFilter([10, 11]) == 1

    # Negative numbers are excluded even if digits are odd
    assert module_0.specialFilter([-13, -15, 13, 15]) == 2

    print("All tests passed!")


test_specialFilter()

# Generated at 2026-11-02 11:19:59.411074
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([11, 13, 15, 17, 19]) == 5
    assert module_0.specialFilter([2, 4, 6, 8, 10]) == 0
    assert module_0.specialFilter([12, 14, 16, 18]) == 0
    assert module_0.specialFilter([21, 23, 27]) == 0
    assert module_0.specialFilter([111, 135, 197]) == 3
    assert module_0.specialFilter([101]) == 1
    assert module_0.specialFilter([110]) == 0
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([9, 10, 11, 12, 13]) == 2

# Generated at 2026-11-02 11:21:20.006912
# Unit test for function specialFilter
def test_specialFilter():
# nonce:814bc9cf
    # Basic cases from typical examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # Single element cases
    assert module_0.specialFilter([11]) == 1   # first and last digit both odd
    assert module_0.specialFilter([12]) == 0   # last digit even
    assert module_0.specialFilter([10]) == 0   # not greater than 10
    assert module_0.specialFilter([21]) == 0   # first digit even

    # All qualifying numbers
    assert module_0.specialFilter([13, 17, 19]) == 3
    assert module_0.specialFilter([91, 93, 95]) == 3

    # None qualify (even first/last digits)
    assert module_0.specialFilter([22, 44, 66]) == 0

    # Negative numbers are not greater than 10
    assert module_0.specialFilter([-15, -17]) == 0

    # Boundary: exactly 10 and 11
    assert module_0.specialFilter([10, 11]) == 1

    # Mixed list with negatives and multi-digit numbers
    assert module_0.specialFilter([35, -35, 57, 100, 101, 999]) == 4  # 35, 57, 101, 999 qualify

    # Large numbers
    assert module_0.specialFilter([13579, 13578]) == 1

# Generated at 2026-11-02 11:24:41.017302
# Unit test for function specialFilter
def test_specialFilter():
    # No numbers greater than 10
    assert module_0.specialFilter([5, -2, 1, -5]) == 0
    # Only 15 qualifies (first digit 1 odd, last digit 5 odd)
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    # 33 and 109 qualify
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2
    # 93, 125, 121, 109 qualify
    assert module_0.specialFilter([43, -12, 93, 125, 121, 109]) == 4
    # 71, 75, 19 qualify
    assert module_0.specialFilter([71, -2, -33, 75, 21, 19]) == 3
    # Single element not greater than 10
    assert module_0.specialFilter([1]) == 0
    # Empty list
    assert module_0.specialFilter([]) == 0
    # Boundary: exactly 10 does not count
    assert module_0.specialFilter([10]) == 0
    # All qualifying numbers
    assert module_0.specialFilter([13, 17, 19, 31, 39]) == 5

# Generated at 2026-11-02 11:26:56.971292
# Unit test for function specialFilter
def test_specialFilter():
    # Basic example: only 15 has odd first and last digits and is > 10
    assert module_0.specialFilter([15, -73, 14, -15]) == 1

    # 33 and 109 qualify (45 has even first digit, 21 has even first digit)
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Empty list
    assert module_0.specialFilter([]) == 0

    # No numbers greater than 10
    assert module_0.specialFilter([-11, -13, 5, 9, 10, -1]) == 0

    # Exactly 10 is excluded (not strictly greater than 10)
    assert module_0.specialFilter([10]) == 0

    # 11 is the smallest qualifying number
    assert module_0.specialFilter([11]) == 1

    # All qualifying odd-digit numbers
    assert module_0.specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]) == 25

    # All even digits: none qualify
    assert module_0.specialFilter([22, 24, 46, 68, 80, 100]) == 0

    # Mixed: 3 qualify (15, 97, 33); 101 has even last digit; 7 not > 10
    assert module_0.specialFilter([15, 97, 33, 101, 7]) == 3

    # Negative numbers with odd digits but not > 10 do not count
    assert module_0.specialFilter([-15, -33, -97]) == 0

    # Larger numbers: 13579 and 97531 both qualify
    assert module_0.specialFilter([13579, 97531, 24680, 13578]) == 2

    # Duplicates should each be counted
    assert module_0.specialFilter([11, 11, 11]) == 3

    print("All tests passed!")


test_specialFilter()