

# Generated at 2026-11-02 18:26:01.109499
# Unit test for function starts_one_ends
def test_starts_one_ends():
# nonce:5308b9d9
    # Base case: n == 1 returns 1 (only the number 1 itself)
    assert module_0.starts_one_ends(1) == 1

    # n == 2: 18 * 10^0 = 18
    assert module_0.starts_one_ends(2) == 18

    # n == 3: 18 * 10^1 = 180
    assert module_0.starts_one_ends(3) == 180

    # n == 4: 18 * 10^2 = 1800
    assert module_0.starts_one_ends(4) == 1800

    # n == 5: 18 * 10^3 = 18000
    assert module_0.starts_one_ends(5) == 18000

    # Larger case: n == 10 -> 18 * 10^8
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)

    # Verify formula holds across a range of n >= 2
    for n in range(2, 15):
        assert module_0.starts_one_ends(n) == 18 * (10 ** (n - 2))

    # Results should be positive integers
    for n in range(1, 10):
        result = module_0.starts_one_ends(n)
        assert isinstance(result, int)
        assert result > 0

    print("All tests passed!")


if __name__ == "__main__":
    test_starts_one_ends()

# Generated at 2026-11-02 18:27:54.545769
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit numbers, only 1 starts or ends with 1
    assert module_0.starts_one_ends(1) == 1
    
    # Two-digit numbers: 10,11,12,...,19 (start with 1) and 11,21,31,...,91 (end with 1), minus 11 counted twice
    assert module_0.starts_one_ends(2) == 18
    
    # Three-digit numbers
    assert module_0.starts_one_ends(3) == 180
    
    # Four-digit numbers
    assert module_0.starts_one_ends(4) == 1800
    
    # Larger input
    assert module_0.starts_one_ends(5) == 18000
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    
    # Verify formula generalization: result is 18 * 10^(n-2) for n >= 2
    for n in range(2, 8):
        assert module_0.starts_one_ends(n) == 18 * (10 ** (n - 2))
    
    print("All tests passed!")

if __name__ == "__main__":
    test_starts_one_ends()

# Generated at 2026-11-02 18:30:27.471472
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case
    assert module_0.starts_one_ends(1) == 1

    # Known values from formula 18 * 10^(n-2)
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000
    assert module_0.starts_one_ends(6) == 180000
    assert module_0.starts_one_ends(7) == 1800000
    assert module_0.starts_one_ends(8) == 18000000
    assert module_0.starts_one_ends(9) == 180000000
    assert module_0.starts_one_ends(10) == 1800000000

    # Formula holds for a range of n >= 2
    for n in range(2, 16):
        assert module_0.starts_one_ends(n) == 18 * (10 ** (n - 2))

    # Large n (big integer result)
    assert module_0.starts_one_ends(20) == 18 * (10 ** 18)
    assert isinstance(module_0.starts_one_ends(20), int)

    # Brute-force verification for small n
    def brute_force(n):
        count = 0
        for x in range(10 ** (n - 1), 10 ** n):
            s = str(x)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        return count

    for n in (1, 2, 3, 4):
        assert module_0.starts_one_ends(n) == brute_force(n)


test_starts_one_ends()
print("All tests passed!")

# Generated at 2026-11-02 18:33:16.709676
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # Base case: single digit number (just 1)
    assert module_0.starts_one_ends(1) == 1
    
    # Two-digit numbers starting or ending with 1
    # (10-19 start with 1, and 21, 31, ..., 91 end with 1)
    assert module_0.starts_one_ends(2) == 18
    
    # Three-digit numbers
    assert module_0.starts_one_ends(3) == 180
    
    # Four-digit numbers
    assert module_0.starts_one_ends(4) == 1800
    
    # Five-digit numbers
    assert module_0.starts_one_ends(5) == 18000
    
    # Larger input to verify formula scaling
    assert module_0.starts_one_ends(10) == 18 * (10 ** 8)
    
    # Verify results are positive integers
    for n in range(1, 8):
        result = module_0.starts_one_ends(n)
        assert isinstance(result, int)
        assert result > 0
    
    print("All tests passed!")

test_starts_one_ends()