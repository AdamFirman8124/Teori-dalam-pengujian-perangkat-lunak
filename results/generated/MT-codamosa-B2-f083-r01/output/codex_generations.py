

# Generated at 2026-11-03 03:46:39.477760
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit, only "1" starts or ends with 1
    assert module_0.starts_one_ends(1) == 1
    
    # Two digits: 10-19 (10 numbers) + 21,31,...,91 (8 numbers) = 18
    assert module_0.starts_one_ends(2) == 18
    
    # Three digits: 18 * 10
    assert module_0.starts_one_ends(3) == 180
    
    # Four digits: 18 * 100
    assert module_0.starts_one_ends(4) == 1800
    
    # Five digits: 18 * 1000
    assert module_0.starts_one_ends(5) == 18000
    
    # Larger case to verify formula scaling
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    
    print("All tests passed!")

test_starts_one_ends()

# Generated at 2026-11-03 03:47:51.875304
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit numbers, only 1 starts/ends with 1
    assert module_0.starts_one_ends(1) == 1
    # Two-digit numbers: 10-19 (10 numbers) plus 21,31,...,91 (9 numbers) = 19? No:
    # start with 1: 10-19 (10); end with 1: 11,21,...,91 (10); overlap: 11 (1)
    # total = 10 + 10 - 1 = 19? Formula says 18 * 10^0 = 18
    # Recount: end with 1 means last digit is 1: 11,21,31,...,91 -> 9 numbers (10 excluded since 10 ends in 0)
    # start with 1: 10-19 -> 10 numbers; overlap: 11 -> 1
    # total = 10 + 9 - 1 = 18
    assert module_0.starts_one_ends(2) == 18
    # Three-digit numbers
    assert module_0.starts_one_ends(3) == 180
    # Four-digit numbers
    assert module_0.starts_one_ends(4) == 1800
    # Five-digit numbers
    assert module_0.starts_one_ends(5) == 18000
    # Larger input follows 18 * 10^(n-2) pattern
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    assert module_0.starts_one_ends(15) == 18 * (10 ** 13)
    # Verify general formula holds for a range of inputs
    for n in range(2, 20):
        assert module_0.starts_one_ends(n) == 18 * (10 ** (n - 2))

# Generated at 2026-11-03 03:49:50.762130
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single-digit numbers, only "1" itself starts or ends with 1
    assert module_0.starts_one_ends(1) == 1

    # Two-digit numbers: 18 numbers start or end with 1
    assert module_0.starts_one_ends(2) == 18

    # Three-digit numbers: 180
    assert module_0.starts_one_ends(3) == 180

    # Four-digit numbers: 1800
    assert module_0.starts_one_ends(4) == 1800

    # Five-digit numbers: 18000
    assert module_0.starts_one_ends(5) == 18000

    # Larger input
    assert module_0.starts_one_ends(10) == 1800000000

    # Verify formula holds for general n
    for n in range(2, 8):
        assert module_0.starts_one_ends(n) == 18 * (10 ** (n - 2))

    print("All tests passed!")


if __name__ == "__main__":
    test_starts_one_ends()

# Generated at 2026-11-03 03:51:47.805589
# Unit test for function starts_one_ends
def test_starts_one_ends():
    assert module_0.starts_one_ends(1) == 1
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    print("All tests passed!")

test_starts_one_ends()

# Generated at 2026-11-03 03:54:20.384630
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: only the single digit 1 qualifies for n = 1
    assert module_0.starts_one_ends(1) == 1

    # Standard formula: 18 * 10^(n-2) for n >= 2
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000
    assert module_0.starts_one_ends(6) == 180000

    # Larger values
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    assert module_0.starts_one_ends(15) == 18 * (10 ** 13)

    # Results should always be positive integers
    for n in range(1, 20):
        result = module_0.starts_one_ends(n)
        assert isinstance(result, int)
        assert result > 0