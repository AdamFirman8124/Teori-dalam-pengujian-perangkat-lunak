

# Generated at 2026-11-02 10:14:36.049184
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1          # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(1, 10) == 2         # 2^1 = 2
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8

    # Larger exponent
    assert module_0.modp(10, 101) == 14      # 2^10 = 1024, 1024 % 101 = 14
    assert module_0.modp(100, 101) == 1      # Fermat's little theorem: 2^100 % 101 = 1
    assert module_0.modp(1101, 101) == 2     # large exponent case

    # Edge cases
    assert module_0.modp(5, 1) == 0          # anything mod 1 is 0
    assert module_0.modp(10, 2) == 0         # 2^10 mod 2 = 0
    assert module_0.modp(30, 5) == 4         # 2^30 mod 5 = 4
    assert module_0.modp(31, 11) == 2        # 2^10 % 11 = 1, so 2^31 % 11 = 2

    # Verify consistency with Python's built-in pow
    for n in range(0, 50):
        for p in [2, 3, 5, 7, 11, 97, 101]:
            assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-11-02 10:15:12.992977
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1          # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8

    # Edge cases
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(1, 101) == 2        # 2^1 = 2
    assert module_0.modp(100, 101) == 1      # large exponent
    assert module_0.modp(1101, 101) == 2     # very large exponent

    # Modulus of 2 always yields 0 for n >= 1
    assert module_0.modp(1, 2) == 0
    assert module_0.modp(10, 2) == 0

    # Zero result check
    assert module_0.modp(5, 32) == 0         # 2^5 = 32, 32 % 32 = 0

    # Cross-check with pow built-in
    for n in range(0, 20):
        for p in range(2, 20):
            assert module_0.modp(n, p) == pow(2, n, p)

if __name__ == "__main__":
    test_modp()
    print("All tests passed!")

# Generated at 2026-11-02 10:15:50.266114
# Unit test for function modp
def test_modp():
    assert module_0.modp(3, 5) == 3
    assert module_0.modp(1101, 101) == 2
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(3, 11) == 8
    assert module_0.modp(100, 101) == 1
    assert module_0.modp(10, 1000000) == 24
    assert module_0.modp(1, 2) == 0
    assert module_0.modp(5, 3) == 2
    assert module_0.modp(20, 7) == 4
    assert module_0.modp(50, 97) == pow(2, 50, 97)

# Generated at 2026-11-02 10:17:23.565837
# Unit test for function modp
def test_modp():
    assert module_0.modp(3, 5) == 3
    assert module_0.modp(4, 3) == 1
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(1, 11) == 2
    assert module_0.modp(10, 101) == 14
    assert module_0.modp(100, 101) == 1
    assert module_0.modp(30, 5) == 4
    assert module_0.modp(31, 5) == 3
    assert module_0.modp(2, 3) == 1
    assert module_0.modp(5, 3) == 2
    assert module_0.modp(1, 2) == 0

# Generated at 2026-11-02 10:18:54.949888
# Unit test for function modp
def test_modp():
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(1101, 101) == 2     # 2^1101 % 101 == 2
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(100, 101) == 1      # 2^100 % 101 == 1
    assert module_0.modp(30, 5) == 4         # 2^30 % 5 == 4
    assert module_0.modp(31, 5) == 3         # 2^31 % 5 == 3
    assert module_0.modp(1, 2) == 0          # 2^1 = 2, 2 % 2 = 0
    assert module_0.modp(10, 1) == 0         # anything mod 1 is 0