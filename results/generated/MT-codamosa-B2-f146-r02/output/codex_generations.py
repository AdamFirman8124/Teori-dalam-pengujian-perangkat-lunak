

# Generated at 2026-10-25 03:35:24.351530
# Unit test for function specialFilter

# Generated at 2026-10-25 03:35:31.316658
# Unit test for function specialFilter
def test_specialFilter():
    # Positive: odd first and last digit, > 10
    assert module_0.specialFilter([15, 33, 73, 97]) == 4
    # Mixed: includes even digits, negatives, numbers <= 10
    assert module_0.specialFilter([12, 21, 10, -15, 135, 147]) == 1  # only 135 qualifies
    # Empty list
    assert module_0.specialFilter([]) == 0
    # Single-digit odd numbers excluded (not > 10)
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0
    # Boundary: exactly 11 qualifies, 10 does not
    assert module_0.specialFilter([10, 11]) == 1
    # Negative qualifying value: -31 -> first/last digit '3' and '1', but -31 <= 10? No: -31 is not > 10
    assert module_0.specialFilter([-31]) == 0
    # Multi-digit with odd first/last, even middle
    assert module_0.specialFilter([313, 575, 979, 580]) == 3

# Generated at 2026-10-25 03:35:38.415998
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -12, 3, 35]) == 2
    assert module_0.specialFilter([11, 13, 20, 33, 48, 79]) == 4
    assert module_0.specialFilter([10, 12, 24, 42, 100]) == 0
    assert module_0.specialFilter([]) == 0

# Generated at 2026-10-25 03:35:45.891795
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([1, 3, 5, 7, 9]) == 0
    assert module_0.specialFilter([10, 11, 13, 15, 17, 19]) == 5
    assert module_0.specialFilter([21, 23, 25, 27, 29]) == 0
    assert module_0.specialFilter([33, 45, 71, 99, 109]) == 4
    assert module_0.specialFilter([-11, -13, 0, 12, 24]) == 0

# Generated at 2026-10-25 03:35:52.585876
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, 12, 35, 87, 99, 10, -33]) == 3
    assert module_0.specialFilter([11, 13, 37, 95]) == 4
    assert module_0.specialFilter([12, 24, 82, 100]) == 0
    assert module_0.specialFilter([1, 3, 5, 7, 9, 10]) == 0
    assert module_0.specialFilter([]) == 0

# Generated at 2026-10-25 03:35:58.486492
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -73, 14, 3]) == 1
    assert module_0.specialFilter([33, 44, 101, 153, 75]) == 4
    assert module_0.specialFilter([10, 9, 2, -11]) == 0
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([]) == 0