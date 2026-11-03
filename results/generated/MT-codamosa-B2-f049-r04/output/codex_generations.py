

# Generated at 2026-11-03 03:18:35.882081
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(1, 101) == 2
    assert module_0.modp(2, 101) == 4
    assert module_0.modp(3, 11) == 8
    assert module_0.modp(5, 3) == 2  # 2^5 = 32, 32 % 3 = 2
    assert module_0.modp(10, 101) == 14  # 1024 % 101 = 14
    assert module_0.modp(100, 101) == 1  # Fermat's little theorem: 2^100 ≡ 1 (mod 101)
    assert module_0.modp(7, 13) == 11  # 128 % 13 = 11
    assert module_0.modp(3, 5) == 3  # 8 % 5 = 3
    assert module_0.modp(4, 17) == 16  # 16 % 17 = 16
    assert module_0.modp(1, 2) == 0  # 2 % 2 = 0
    assert module_0.modp(0, 5) == 1  # 2^0 = 1

# Generated at 2026-11-03 03:20:06.120053
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1          # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8

    # Edge cases
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(1, 2) == 0          # 2^1 = 2, 2 % 2 = 0
    assert module_0.modp(10, 1000000) == 1024  # 2^10 = 1024

    # Large exponent cases
    assert module_0.modp(1101, 101) == 2
    assert module_0.modp(100, 101) == 1      # Fermat's little theorem: 2^100 % 101 = 1
    assert module_0.modp(30, 5) == 4         # 2^30 % 5 = 4

    # Modulus of 1 always yields 0
    assert module_0.modp(5, 1) == 0

    # Verify against Python's built-in pow
    for n, p in [(0, 7), (1, 7), (7, 13), (13, 17), (50, 97), (256, 65537)]:
        assert module_0.modp(n, p) == pow(2, n, p)

    print("All test_modp tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-03 03:21:48.111243
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1          # 2^0 mod 101 = 1
    assert module_0.modp(1, 101) == 2          # 2^1 mod 101 = 2
    assert module_0.modp(3, 11) == 8           # 2^3 mod 11 = 8
    assert module_0.modp(3, 5) == 3            # 2^3 mod 5 = 8 mod 5 = 3
    assert module_0.modp(10, 1000) == 24       # 2^10 mod 1000 = 1024 mod 1000 = 24
    assert module_0.modp(5, 3) == 2            # 2^5 mod 3 = 32 mod 3 = 2

    # Fermat's little theorem: 101 is prime, so 2^100 mod 101 == 1
    assert module_0.modp(100, 101) == 1

    # Larger exponent
    assert module_0.modp(11, 101) == 28        # 2^11 mod 101 = 2048 mod 101 = 28
    assert module_0.modp(20, 33) == (2 ** 20) % 33

    # Result should never exceed p-1 (for p > 1)
    for n in range(15):
        for p in (3, 7, 11, 101):
            assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-11-03 03:26:43.638561
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1          # 2^0 mod 101 = 1
    assert module_0.modp(1, 101) == 2          # 2^1 mod 101 = 2
    assert module_0.modp(3, 5) == 3            # 8 mod 5 = 3
    assert module_0.modp(3, 11) == 8           # 8 mod 11 = 8
    assert module_0.modp(4, 16) == 0           # 16 mod 16 = 0

    # Known reference cases
    assert module_0.modp(110, 101) == 14       # 2^110 mod 101
    assert module_0.modp(100, 101) == 1        # Fermat's little theorem: 2^100 mod 101 = 1
    assert module_0.modp(30, 5) == 4           # 2^30 mod 5 = 4
    assert module_0.modp(31, 5) == 3           # 2^31 mod 5 = 3

    # Larger values
    assert module_0.modp(10, 3) == 1           # 1024 mod 3 = 1
    assert module_0.modp(50, 1000000) == 56224 # 2^50 mod 10^6

    # Modulus of 1 always yields 0
    assert module_0.modp(7, 1) == 0

    # Consistency with Python's built-in pow
    for n, p in [(0, 2), (5, 7), (13, 17), (64, 257), (128, 65537)]:
        assert module_0.modp(n, p) == pow(2, n, p)