

# Generated at 2026-11-02 17:17:35.527020
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3        # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1        # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(0, 101) == 1      # 2^0 = 1
    assert module_0.modp(3, 11) == 8       # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(100, 101) == 1    # 2^100 % 101 = 1
    assert module_0.modp(1101, 101) == 2   # 2^1101 % 101 = 2
    assert module_0.modp(10, 1000000) == 24  # 2^10 = 1024

    # Edge cases
    assert module_0.modp(1, 2) == 0        # 2^1 = 2, 2 % 2 = 0
    assert module_0.modp(2, 3) == 1        # 2^2 = 4, 4 % 3 = 1
    assert module_0.modp(5, 50) == 32      # 2^5 = 32, 32 % 50 = 32

    print("All test cases passed!")

if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 17:17:56.502610
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(1101, 101) == 2     # 2^1101 mod 101 = 2
    assert module_0.modp(100, 101) == 1      # 2^100 mod 101 = 1

    # Edge cases
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(0, 1) == 0          # 1 % 1 = 0
    assert module_0.modp(1, 2) == 0          # 2 % 2 = 0
    assert module_0.modp(1, 3) == 2          # 2 % 3 = 2

    # Larger values
    assert module_0.modp(10, 1000000) == 1024       # 2^10 = 1024
    assert module_0.modp(20, 1000000007) == 1048576 # 2^20 = 1048576
    assert module_0.modp(64, 1000) == 536           # 2^64 mod 1000 = 536

    print("All tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 17:18:04.470137
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3        # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1        # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(0, 101) == 1      # 2^0 = 1
    assert module_0.modp(1, 2) == 0        # 2^1 = 2, 2 % 2 = 0
    assert module_0.modp(10, 7) == 3       # 2^10 = 1024, 1024 % 7 = 3
    assert module_0.modp(3, 11) == 8       # 2^3 = 8, 8 % 11 = 8

    # Large exponent cases
    assert module_0.modp(1101, 101) == 2   # known value from examples
    assert module_0.modp(100, 101) == 1    # 2^100 mod 101 = 1 (Fermat's little theorem)
    assert module_0.modp(30, 5) == 4       # 2^30 mod 5 = 4
    assert module_0.modp(31, 5) == 3       # 2^31 mod 5 = 3

    # Edge cases
    assert module_0.modp(0, 1) == 0        # anything mod 1 is 0
    assert module_0.modp(5, 3) == 2        # 2^5 = 32, 32 % 3 = 2

    print("All test cases passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 17:18:24.808982
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1          # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(100, 101) == 1      # 2^100 mod 101 = 1 (Fermat's little theorem)
    assert module_0.modp(1101, 101) == 14    # Large exponent case
    assert module_0.modp(10, 1000000) == 1024  # 2^10 = 1024

    # Edge cases
    assert module_0.modp(1, 2) == 0          # 2^1 = 2, 2 % 2 = 0
    assert module_0.modp(2, 2) == 0          # 2^2 = 4, 4 % 2 = 0
    assert module_0.modp(5, 1000000007) == 32  # Large prime modulus

    print("All test_modp tests passed!")

test_modp()

# Generated at 2026-11-02 17:19:16.195288
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3          # 2^3 = 8 % 5 = 3
    assert module_0.modp(3, 11) == 8         # 2^3 = 8 % 11 = 8
    assert module_0.modp(4, 3) == 1          # 2^4 = 16 % 3 = 1

    # Larger exponents with modular reduction
    assert module_0.modp(1101, 101) == 2
    assert module_0.modp(100, 101) == 1
    assert module_0.modp(30, 5) == 4         # 2^30 % 5 = 4

    # Edge cases
    assert module_0.modp(10, 2) == 0         # any power of 2 mod 2 is 0
    assert module_0.modp(5, 1000000007) == 32
    assert module_0.modp(20, 65537) == (1 << 20) % 65537

    # Cross-check against pow(2, n, p) for random-ish values
    for n, p in [(0, 7), (1, 7), (2, 7), (7, 13), (15, 17), (63, 1000003), (256, 998244353)]:
        assert module_0.modp(n, p) == pow(2, n, p), f"failed for n={n}, p={p}"

    print("All modp tests passed!")


if __name__ == "__main__":
    test_modp()