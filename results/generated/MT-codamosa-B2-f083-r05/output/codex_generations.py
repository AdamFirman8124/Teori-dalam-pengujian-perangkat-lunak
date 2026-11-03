

# Generated at 2026-11-01 21:01:34.391701
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit — only "1" starts/ends with 1
    assert module_0.starts_one_ends(1) == 1
    
    # Two-digit numbers: 18 of them (1x or x1 patterns)
    assert module_0.starts_one_ends(2) == 18
    
    # Three-digit and beyond follow the formula 18 * 10^(n-2)
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000
    
    # Formula holds consistently for a range of inputs
    for n in range(6, 12):
        expected = 18 * (10 ** (n - 2))
        result = module_0.starts_one_ends(n)
        assert result == expected, f"Failed for n={n}: got {result}, expected {expected}"
        assert isinstance(result, int)
    
    print("All tests passed!")

# Generated at 2026-11-01 21:02:03.358274
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit numbers, only "1" qualifies
    assert module_0.starts_one_ends(1) == 1
    
    # Two digit numbers: starts or ends with 1 -> 18 numbers
    assert module_0.starts_one_ends(2) == 18
    
    # Three digit numbers
    assert module_0.starts_one_ends(3) == 180
    
    # Four digit numbers
    assert module_0.starts_one_ends(4) == 1800
    
    # Five digit numbers
    assert module_0.starts_one_ends(5) == 18000
    
    # Larger case to verify exponential growth pattern
    assert module_0.starts_one_ends(7) == 1800000
    
    print("All tests passed!")

# Generated at 2026-11-01 21:02:36.125467
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit numbers starting or ending with 1 is just "1"
    assert module_0.starts_one_ends(1) == 1
    
    # Two-digit numbers: 10-19 (start with 1) and 11,21,...,91 (end with 1), minus overlap 11
    assert module_0.starts_one_ends(2) == 18
    
    # Three-digit numbers
    assert module_0.starts_one_ends(3) == 180
    
    # Four-digit numbers
    assert module_0.starts_one_ends(4) == 1800
    
    # Five-digit numbers
    assert module_0.starts_one_ends(5) == 18000
    
    # Larger input checks formula scaling
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    
    print("All tests passed!")


test_starts_one_ends()

# Generated at 2026-11-01 21:03:38.084093
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single-digit numbers, only "1" starts or ends with 1
    assert module_0.starts_one_ends(1) == 1
    
    # Two-digit numbers: 10, 11, 12, ..., 19, 21, 31, ..., 91 (18 numbers)
    assert module_0.starts_one_ends(2) == 18
    
    # Three-digit numbers
    assert module_0.starts_one_ends(3) == 180
    
    # Four-digit numbers
    assert module_0.starts_one_ends(4) == 1800
    
    # Five-digit numbers
    assert module_0.starts_one_ends(5) == 18000
    
    # Large input check
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    
    print("All tests passed!")

if __name__ == "__main__":
    test_starts_one_ends()

# Generated at 2026-11-01 21:04:39.843907
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: n == 1 returns 1
    assert module_0.starts_one_ends(1) == 1

    # n == 2: 18 * 10^0 = 18
    assert module_0.starts_one_ends(2) == 18

    # n == 3: 18 * 10^1 = 180
    assert module_0.starts_one_ends(3) == 180

    # n == 4: 18 * 10^2 = 1800
    assert module_0.starts_one_ends(4) == 1800

    # n == 5: 18 * 10^3 = 18000
    assert module_0.starts_one_ends(5) == 18000

    # Larger value: n == 10 -> 18 * 10^8 = 1800000000
    assert module_0.starts_one_ends(10) == 1800000000

    # Verify formula holds generally for n >= 2
    for n in range(2, 15):
        assert module_0.starts_one_ends(n) == 18 * (10 ** (n - 2))

    # Result should always be positive
    for n in range(1, 15):
        assert module_0.starts_one_ends(n) > 0

    print("All tests passed!")


if __name__ == "__main__":
    test_starts_one_ends()