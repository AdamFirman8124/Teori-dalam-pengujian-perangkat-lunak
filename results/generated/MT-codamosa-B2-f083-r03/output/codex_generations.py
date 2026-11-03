

# Generated at 2026-11-02 14:13:20.990607
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: n == 1 -> only the number 1 itself
    assert module_0.starts_one_ends(1) == 1

    # Formula cases: 18 * 10^(n-2)
    assert module_0.starts_one_ends(2) == 18          # 18 * 10^0
    assert module_0.starts_one_ends(3) == 180         # 18 * 10^1
    assert module_0.starts_one_ends(4) == 1800        # 18 * 10^2
    assert module_0.starts_one_ends(5) == 18000       # 18 * 10^3

    # Larger n still follows the formula
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    assert module_0.starts_one_ends(20) == 18 * (10 ** 18)

    # Cross-check against brute force for small n
    def brute_force(n):
        count = 0
        for i in range(10 ** (n - 1), 10 ** n):
            s = str(i)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        return count

    for n in range(1, 5):
        assert module_0.starts_one_ends(n) == brute_force(n), f"Mismatch at n={n}"

    print("All tests passed!")


if __name__ == "__main__":
    test_starts_one_ends()

# Generated at 2026-11-02 14:15:12.279636
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit numbers, only "1" starts or ends with 1
    assert module_0.starts_one_ends(1) == 1

    # Two-digit numbers: 18 numbers start or end with 1
    assert module_0.starts_one_ends(2) == 18

    # Three-digit numbers
    assert module_0.starts_one_ends(3) == 180

    # Four-digit numbers
    assert module_0.starts_one_ends(4) == 1800

    # Five-digit numbers
    assert module_0.starts_one_ends(5) == 18000

    # Larger value to verify formula scaling
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)

    # Verify the general formula for a range of values
    for n in range(2, 8):
        assert module_0.starts_one_ends(n) == 18 * (10 ** (n - 2))

    print("All tests passed!")


if __name__ == "__main__":
    test_starts_one_ends()

# Generated at 2026-11-02 14:16:51.587992
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit numbers, only "1" starts or ends with 1
    assert module_0.starts_one_ends(1) == 1
    
    # Two-digit numbers: 18 numbers start or end with 1
    assert module_0.starts_one_ends(2) == 18
    
    # Three-digit numbers
    assert module_0.starts_one_ends(3) == 180
    
    # Four-digit numbers
    assert module_0.starts_one_ends(4) == 1800
    
    # Five-digit numbers
    assert module_0.starts_one_ends(5) == 18000
    
    # Ten-digit numbers
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    
    # Brute-force verification for small n
    def brute_force(n):
        count = 0
        for i in range(10 ** (n - 1), 10 ** n):
            s = str(i)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        return count
    
    for n in range(1, 5):
        assert module_0.starts_one_ends(n) == brute_force(n), f"Mismatch at n={n}"
    
    # Result should always be positive for valid input
    assert module_0.starts_one_ends(6) > 0
    
    print("All tests passed!")

if __name__ == "__main__":
    test_starts_one_ends()

# Generated at 2026-11-02 14:18:09.905467
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: only the number 1 qualifies for n = 1
    assert module_0.starts_one_ends(1) == 1

    # Two-digit numbers: 10-19 (start with 1) plus 21,31,...,91 (end with 1), 11 counted once
    assert module_0.starts_one_ends(2) == 18

    # General formula: 18 * 10^(n-2)
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000
    assert module_0.starts_one_ends(6) == 180000

    # Larger input
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    assert module_0.starts_one_ends(15) == 18 * (10 ** 13)

    print("All tests passed!")


test_starts_one_ends()

# Generated at 2026-11-02 14:19:57.990642
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit
    assert module_0.starts_one_ends(1) == 1

    # Two-digit numbers: 10-19 (start with 1) plus 11,21,...,91 (end with 1), minus overlap
    assert module_0.starts_one_ends(2) == 18

    # Three-digit numbers
    assert module_0.starts_one_ends(3) == 180

    # Four-digit numbers
    assert module_0.starts_one_ends(4) == 1800

    # Five-digit numbers
    assert module_0.starts_one_ends(5) == 18000

    # Larger input
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)

    # Verify formula consistency for a range of n > 1
    for n in range(2, 12):
        assert module_0.starts_one_ends(n) == 18 * (10 ** (n - 2))

    # Verify result is a positive integer
    for n in range(1, 12):
        result = module_0.starts_one_ends(n)
        assert isinstance(result, int)
        assert result > 0

    print("All tests passed!")