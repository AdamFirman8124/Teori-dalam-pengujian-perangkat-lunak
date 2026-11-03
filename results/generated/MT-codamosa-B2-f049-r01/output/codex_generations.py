

# Generated at 2026-11-02 00:17:22.635760
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1          # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(1, 10) == 2         # 2^1 = 2
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, less than modulus
    assert module_0.modp(10, 1024) == 0      # 2^10 = 1024, divisible by modulus
    assert module_0.modp(100, 101) == 1      # Fermat's little theorem: 2^100 mod 101 = 1
    assert module_0.modp(1101, 101) == 2     # Large exponent case
    assert module_0.modp(50, 7) == pow(2, 50, 7)
    print("test_modp passed")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 00:17:57.452305
# Unit test for function modp
def test_modp():
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(1101, 101) == 2     # large exponent case
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(100, 101) == 1      # 2^100 % 101 = 1
    assert module_0.modp(1, 2) == 0          # 2^1 = 2, 2 % 2 = 0
    assert module_0.modp(10, 7) == 2         # 2^10 = 1024, 1024 % 7 = 2
    print("All tests passed!")

test_modp()

# Generated at 2026-11-02 00:18:44.554608
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1          # 2^0 mod 101 = 1
    assert module_0.modp(1, 5) == 2            # 2^1 mod 5 = 2
    assert module_0.modp(3, 5) == 3            # 2^3 mod 5 = 8 % 5 = 3
    assert module_0.modp(3, 11) == 8           # 2^3 mod 11 = 8

    # Larger exponents with modular reduction
    assert module_0.modp(10, 7) == 2           # 1024 % 7 = 2
    assert module_0.modp(100, 101) == 1        # 2^100 mod 101 = 1
    assert module_0.modp(1101, 101) == 2       # known reference value

    # Modulus of 1 always yields 0
    assert module_0.modp(5, 1) == 0
    assert module_0.modp(0, 1) == 0

    # Exponent where result is exactly modulus (reduces to 0)
    assert module_0.modp(1, 2) == 0            # 2 % 2 = 0

    # Cross-check against built-in pow for consistency
    import random
    for _ in range(20):
        n = random.randint(0, 500)
        p = random.randint(2, 1000)
        assert module_0.modp(n, p) == pow(2, n, p)

    print("All modp tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 00:20:59.931090
# Unit test for function modp
def test_modp():
    # Basic known values
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1          # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(1, 101) == 2        # 2^1 = 2
    assert module_0.modp(10, 101) == 1024 % 101

    # Classic edge case
    assert module_0.modp(1101, 101) == 14

    # Modulus of 1 always yields 0 (for n >= 1); 1 % 1 = 0 for n = 0
    assert module_0.modp(5, 1) == 0
    assert module_0.modp(0, 1) == 0

    # Modulus of 2 yields 0 for n >= 1
    assert module_0.modp(7, 2) == 0

    # Result never exceeds modulus - 1
    result = module_0.modp(50, 13)
    assert 0 <= result < 13

    # Cross-check against built-in pow
    import random
    for _ in range(20):
        n = random.randint(0, 500)
        p = random.randint(2, 1000)
        assert module_0.modp(n, p) == pow(2, n, p)

    print("All tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 00:23:28.410643
# Unit test for function modp
def test_modp():
    # Base cases
    assert module_0.modp(0, 101) == 1, "2^0 mod any p should be 1"
    assert module_0.modp(1, 101) == 2, "2^1 mod 101 should be 2"

    # Small values
    assert module_0.modp(3, 5) == 3, "2^3 mod 5 should be 3"
    assert module_0.modp(3, 11) == 8, "2^3 mod 11 should be 8"
    assert module_0.modp(5, 13) == 6, "2^5 mod 13 should be 6"

    # Larger exponent with wraparound
    assert module_0.modp(10, 101) == 14, "2^10 mod 101 should be 14"

    # Fermat's little theorem: 2^(p-1) mod p == 1 for prime p
    assert module_0.modp(100, 101) == 1, "2^100 mod 101 should be 1 (Fermat)"
    assert module_0.modp(1000, 101) == 1, "2^1000 mod 101 should be 1"

    # Very small modulus
    assert module_0.modp(4, 2) == 0, "2^4 mod 2 should be 0"
    assert module_0.modp(1, 3) == 2, "2^1 mod 3 should be 2"

    # Consistency with pow built-in for random-ish values
    for n, p in [(17, 23), (50, 97), (123, 1000000007)]:
        assert module_0.modp(n, p) == pow(2, n, p), f"module_0.modp({n}, {p}) should match pow(2, {n}, {p})"

# nonce:83942755