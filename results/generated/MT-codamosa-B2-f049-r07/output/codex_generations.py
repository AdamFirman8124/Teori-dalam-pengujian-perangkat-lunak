

# Generated at 2026-11-03 01:14:43.961951
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1, "2^0 mod anything should be 1"
    assert module_0.modp(1, 5) == 2, "2^1 mod 5 should be 2"
    assert module_0.modp(2, 5) == 4, "2^2 mod 5 should be 4"
    assert module_0.modp(3, 5) == 3, "2^3 mod 5 should be 3"
    assert module_0.modp(4, 5) == 1, "2^4 mod 5 should be 1"

    # Larger exponents
    assert module_0.modp(10, 101) == 14, "2^10 mod 101 should be 14"
    assert module_0.modp(5, 3) == 2, "2^5 mod 3 should be 2"
    assert module_0.modp(3, 11) == 8, "2^3 mod 11 should be 8"

    # Fermat's little theorem: 2^(p-1) mod p == 1 for prime p
    assert module_0.modp(100, 101) == 1, "2^100 mod 101 should be 1"
    assert module_0.modp(6, 7) == 1, "2^6 mod 7 should be 1"

    # Modulus of 2 always yields 1 for n >= 1, and 1 for n == 0
    assert module_0.modp(0, 2) == 1, "2^0 mod 2 should be 1"
    assert module_0.modp(7, 2) == 1, "2^7 mod 2 should be 1"

    # Modulus of 1 always yields 0
    assert module_0.modp(10, 1) == 0, "anything mod 1 should be 0"

    # Large exponent check against pow
    assert module_0.modp(50, 1000000007) == pow(2, 50, 1000000007), \
        "2^50 mod 1000000007 should match built-in pow"

    print("All modp tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-03 01:15:25.424786
# Unit test for function modp
def test_modp():
    # Basic cases: 2^n mod p
    assert module_0.modp(3, 5) == 3        # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(4, 3) == 1        # 2^4 = 16, 16 % 3 = 1
    assert module_0.modp(3, 11) == 8       # 2^3 = 8, 8 % 11 = 8

    # Edge case: n = 0 -> ret stays 1
    assert module_0.modp(0, 101) == 1

    # Edge case: n = 1
    assert module_0.modp(1, 3) == 2

    # Result wraps to 0 when p divides 2^n
    assert module_0.modp(1, 2) == 0
    assert module_0.modp(10, 1024) == 0

    # Large exponents
    assert module_0.modp(10, 1000000) == 1024
    assert module_0.modp(1101, 101) == 2
    assert module_0.modp(100, 101) == 1

    # p = 1 always yields 0
    assert module_0.modp(5, 1) == 0
    assert module_0.modp(0, 1) == 0

    # Consistency with Python's built-in pow
    for n, p in [(7, 13), (20, 97), (55, 89), (123, 1009)]:
        assert module_0.modp(n, p) == pow(2, n, p)

    print("All test_modp tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-03 01:16:16.731643
# Unit test for function modp
def test_modp():
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(1101, 101) == 2     # known case
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(1, 5) == 2          # 2^1 % 5 = 2
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(100, 101) == 1      # 2^100 % 101 = 1 (Fermat's little theorem)
    assert module_0.modp(10, 1000000) == 1024  # 2^10 = 1024 < 1000000
    assert module_0.modp(30, 5) == 1         # 2^30 % 5 = 1
    assert module_0.modp(15, 2) == 0         # any even result mod 2 = 0
    print("All tests passed!")

# Generated at 2026-11-03 01:17:22.772896
# Unit test for function modp
def test_modp():
    # Basic cases: 2^n mod p
    assert module_0.modp(3, 5) == 3          # 8 mod 5
    assert module_0.modp(3, 11) == 8         # 8 mod 11
    assert module_0.modp(5, 3) == 2          # 32 mod 3
    assert module_0.modp(10, 1000) == 24     # 1024 mod 1000

    # Edge cases
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(1, 101) == 2        # 2^1 = 2
    assert module_0.modp(0, 1) == 0          # anything mod 1 is 0

    # Known example from spec
    assert module_0.modp(1101, 101) == 2
    assert module_0.modp(100, 101) == 1

    # Large values
    assert module_0.modp(1000, 1000000007) == 2 ** 1000 % 1000000007

    # Property check against direct computation
    for n in range(0, 50):
        for p in [2, 3, 7, 13, 101]:
            assert module_0.modp(n, p) == (2 ** n) % p

    print("All modp tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-03 01:18:32.198567
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(10, 3) == 1         # 2^10 = 1024, 1024 % 3 = 1
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8, 8 % 11 = 8
    assert module_0.modp(5, 3) == 2          # 2^5 = 32, 32 % 3 = 2

    # Edge cases
    assert module_0.modp(1, 2) == 0          # 2^1 = 2, 2 % 2 = 0
    assert module_0.modp(1, 3) == 2          # 2^1 = 2, 2 % 3 = 2

    # Large values (Fermat's little theorem: 2^(p-1) % p == 1 for prime p)
    assert module_0.modp(100, 101) == 1
    assert module_0.modp(15, 1093) == pow(2, 15, 1093)

    # Cross-check against Python's built-in pow for random-ish inputs
    for n, p in [(4, 50), (7, 12), (20, 7), (50, 1000000007)]:
        assert module_0.modp(n, p) == pow(2, n, p)

    print("All modp tests passed!")


if __name__ == "__main__":
    test_modp()