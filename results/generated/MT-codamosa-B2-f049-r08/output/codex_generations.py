

# Generated at 2026-11-02 09:42:30.574549
# Unit test for function modp
def test_modp():
    assert module_0.modp(3, 5) == 3
    assert module_0.modp(4, 3) == 1
    assert module_0.modp(1101, 101) == 2
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(3, 11) == 8
    assert module_0.modp(100, 101) == 1
    assert module_0.modp(10, 1000000) == 1024
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(2, 5) == 4
    assert module_0.modp(5, 13) == 6
    assert module_0.modp(20, 7) == 2
    assert module_0.modp(50, 97) == pow(2, 50, 97)
    print("All tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 09:43:42.668885
# Unit test for function modp
def test_modp():
    # 2^0 mod any p is 1
    assert module_0.modp(0, 101) == 1
    # 2^3 = 8, 8 mod 5 = 3
    assert module_0.modp(3, 5) == 3
    # 2^3 = 8, 8 mod 11 = 8
    assert module_0.modp(3, 11) == 8
    # 2^10 = 1024, 1024 mod 11 = 1
    assert module_0.modp(10, 11) == 1
    # 2^100 mod 101 == 1 by Fermat's little theorem
    assert module_0.modp(100, 101) == 1
    # 2^1101 mod 101 == 2 (1101 mod 100 = 1)
    assert module_0.modp(1101, 101) == 2
    # mod larger than 2^n: result is 2^n itself
    assert module_0.modp(5, 100) == 32
    # large exponent works correctly
    assert module_0.modp(3 * 10 ** 5, 10) == 6

    print("All tests passed!")

if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 09:44:50.554055
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1          # 2^0 mod 101
    assert module_0.modp(1, 101) == 2          # 2^1 mod 101
    assert module_0.modp(3, 5) == 3            # 8 mod 5
    assert module_0.modp(3, 11) == 8           # 8 mod 11
    
    # Larger exponents
    assert module_0.modp(10, 101) == 14        # 1024 mod 101
    assert module_0.modp(100, 101) == 1        # Fermat's little theorem: 2^100 ≡ 1 mod 101
    assert module_0.modp(1101, 101) == 2       # 1101 = 11*100 + 1, so ≡ 2^1 mod 101
    assert module_0.modp(30, 5) == 4           # 2^30 mod 5
    assert module_0.modp(31, 5) == 3           # 2^31 mod 5
    
    # Modulus edge cases
    assert module_0.modp(2, 4) == 0            # 4 mod 4 = 0
    assert module_0.modp(5, 2) == 0            # 32 mod 2 = 0
    assert module_0.modp(10, 3) == 1           # 1024 mod 3 = 1
    
    # Consistency with built-in pow
    for n in range(0, 50):
        for p in range(2, 20):
            assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-11-02 09:46:17.801484
# Unit test for function modp
def test_modp():
    # nonce:826b2f9f
    # Basic cases
    assert module_0.modp(0, 101) == 1          # 2^0 mod 101 = 1
    assert module_0.modp(1, 101) == 2          # 2^1 mod 101 = 2
    assert module_0.modp(2, 101) == 4          # 2^2 mod 101 = 4
    assert module_0.modp(3, 11) == 8           # 2^3 mod 11 = 8
    assert module_0.modp(3, 5) == 3            # 8 mod 5 = 3
    assert module_0.modp(10, 101) == 14        # 1024 mod 101 = 14
    assert module_0.modp(11, 101) == 28        # 2048 mod 101 = 28
    assert module_0.modp(5, 3) == 2            # 32 mod 3 = 2

    # Fermat's little theorem: 2^(p-1) mod p == 1 for prime p
    assert module_0.modp(100, 101) == 1
    assert module_0.modp(10, 11) == 1

    # Wrap-around (n large relative to p)
    assert module_0.modp(100, 5) == 1          # 2^100 mod 5 = 1 (cycle of 4)

    # Edge case: p = 1
    assert module_0.modp(3, 1) == 0            # anything mod 1 is 0

    # Cross-check against built-in pow for a range of values
    for n in range(0, 50):
        for p in (1, 2, 3, 7, 101, 997):
            assert module_0.modp(n, p) == pow(2, n, p), f"module_0.modp({n}, {p}) mismatch"

    print("All tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 09:47:52.806534
# Unit test for function modp
def test_modp():
    # Basic cases: 2^n mod p
    assert module_0.modp(3, 5) == 3      # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(3, 11) == 8     # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(0, 101) == 1    # 2^0 = 1
    assert module_0.modp(1, 101) == 2    # 2^1 = 2
    assert module_0.modp(2, 101) == 4    # 2^2 = 4
    assert module_0.modp(10, 101) == 14  # 2^10 = 1024, 1024 % 101 = 14
    assert module_0.modp(100, 101) == 1  # Large exponent
    assert module_0.modp(1101, 101) == 2 # Very large exponent

    # Result should always be less than p (for n >= 1)
    for n in range(20):
        for p in range(2, 30):
            assert 0 <= module_0.modp(n, p) < p

    print("All tests passed!")


if __name__ == "__main__":
    test_modp()