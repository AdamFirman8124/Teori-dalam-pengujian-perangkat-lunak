

# Generated at 2026-11-02 17:20:16.544006
# Unit test for function modp
def test_modp():
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(1101, 101) == 2
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(100, 101) == 1      # 2^100 % 101 = 1 (Fermat's little theorem)
    assert module_0.modp(1, 2) == 0          # 2^1 = 2, 2 % 2 = 0
    assert module_0.modp(10, 1000) == 24     # 2^10 = 1024, 1024 % 1000 = 24
    assert module_0.modp(5, 3) == 2          # 2^5 = 32, 32 % 3 = 2

# Generated at 2026-11-02 17:22:00.227071
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1, "2^0 mod 101 should be 1"
    assert module_0.modp(1, 3) == 2, "2^1 mod 3 should be 2"
    assert module_0.modp(2, 5) == 4, "2^2 mod 5 should be 4"
    assert module_0.modp(3, 5) == 3, "2^3 mod 5 should be 3"
    assert module_0.modp(3, 11) == 8, "2^3 mod 11 should be 8"
    
    # Result smaller than p, no wraparound
    assert module_0.modp(10, 1000000) == 1024, "2^10 mod 1000000 should be 1024"
    
    # Wraparound cases
    assert module_0.modp(5, 13) == 6, "2^5 mod 13 should be 6"
    assert module_0.modp(20, 41) == 1, "2^20 mod 41 should be 1"
    assert module_0.modp(100, 101) == 1, "2^100 mod 101 should be 1 (Fermat's little theorem)"
    assert module_0.modp(1101, 101) == 14, "2^1101 mod 101 should be 14"
    
    # Large n with small p
    assert module_0.modp(1000, 7) == pow(2, 1000, 7), "Large exponent consistency with pow()"
    
    # Edge case: p = 1, everything mod 1 is 0
    assert module_0.modp(5, 1) == 0, "Anything mod 1 should be 0"
    assert module_0.modp(0, 1) == 0, "2^0 mod 1 should be 0"
    
    # Consistency with built-in pow across a range
    for n in range(20):
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
            assert module_0.modp(n, p) == pow(2, n, p), \
                f"module_0.modp({n}, {p}) should equal pow(2, {n}, {p})"
    
    print("All tests passed!")

# Generated at 2026-11-02 17:23:28.349465
# Unit test for function modp
def test_modp():
    # nonce:47c54fd2
    # Basic cases
    assert module_0.modp(3, 5) == 3            # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(3, 11) == 8           # 2^3 = 8
    assert module_0.modp(0, 101) == 1          # 2^0 = 1
    assert module_0.modp(1, 101) == 2          # 2^1 = 2
    assert module_0.modp(10, 101) == 1024 % 101

    # Large exponents using Fermat's little theorem (101 is prime)
    assert module_0.modp(100, 101) == 1        # 2^100 ≡ 1 (mod 101)
    assert module_0.modp(1101, 101) == 2       # 2^1101 ≡ 2^(1101 % 100) = 2^1
    assert module_0.modp(110, 101) == 14       # 2^110 ≡ 2^10 = 1024 % 101

    # Cross-check against built-in pow for random-ish values
    for n, p in [(0, 1), (1, 2), (5, 7), (13, 17), (50, 97), (123, 1009)]:
        assert module_0.modp(n, p) == pow(2, n, p), f"failed for n={n}, p={p}"

    # Modulus of 1 always yields 0
    assert module_0.modp(7, 1) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 17:25:19.943141
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3        # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1        # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(3, 11) == 8       # 2^3 = 8
    assert module_0.modp(10, 101) == 10    # 2^10 = 1024, 1024 % 101 = 10

    # Edge cases
    assert module_0.modp(0, 101) == 1      # 2^0 = 1
    assert module_0.modp(1, 101) == 2      # 2^1 = 2
    assert module_0.modp(100, 101) == 1    # 2^100 % 101 = 1 (Fermat's little theorem)
    assert module_0.modp(1101, 101) == 2   # Large exponent

    # Large values
    assert module_0.modp(1000000, 1000000007) == pow(2, 1000000, 1000000007)
    assert module_0.modp(50, 1000000) == 73741817  # 2^50 % 10^6

# Generated at 2026-11-02 17:27:51.773431
# Unit test for function modp
def test_modp():
    # 2^3 % 5
    assert module_0.modp(3, 5) == 3
    # 2^1101 % 101
    assert module_0.modp(1101, 101) == 2
    # 2^0 % 101
    assert module_0.modp(0, 101) == 1
    # 2^3 % 11
    assert module_0.modp(3, 11) == 8
    # 2^100 % 101 (Fermat's little theorem: 2^100 ≡ 1 mod 101)
    assert module_0.modp(100, 101) == 1
    # 2^1 % 2
    assert module_0.modp(1, 2) == 0
    # 2^10 % 3
    assert module_0.modp(10, 3) == 1
    # Verify against Python's built-in pow
    assert module_0.modp(17, 7) == pow(2, 17, 7)
    assert module_0.modp(53, 13) == pow(2, 53, 13)
    # Large exponent consistency check
    assert module_0.modp(1000, 97) == pow(2, 1000, 97)