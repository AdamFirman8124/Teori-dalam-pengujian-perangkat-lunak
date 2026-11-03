

# Generated at 2026-11-02 08:05:29.796767
# Unit test for function modp
def test_modp():
    assert module_0.modp(3, 5) == 3, "Expected 3 for module_0.modp(3, 5)"
    assert module_0.modp(1101, 101) == 2, "Expected 2 for module_0.modp(1101, 101)"
    assert module_0.modp(0, 101) == 1, "Expected 1 for module_0.modp(0, 101)"
    assert module_0.modp(3, 11) == 8, "Expected 8 for module_0.modp(3, 11)"
    assert module_0.modp(100, 101) == 1, "Expected 1 for module_0.modp(100, 101)"
    assert module_0.modp(1, 2) == 0, "Expected 0 for module_0.modp(1, 2)"
    assert module_0.modp(10, 1000) == 24, "Expected 24 for module_0.modp(10, 1000)"
    assert module_0.modp(5, 3) == 2, "Expected 2 for module_0.modp(5, 3)"
    assert module_0.modp(0, 1) == 0, "Expected 0 for module_0.modp(0, 1)"
    print("All tests passed!")


if __name__ == "__main__":
    test_modp()

# Generated at 2026-11-02 08:06:22.222517
# Unit test for function modp
def test_modp():import pytest


def test_modp_basic():
    """Test basic cases of modp."""
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(1, 101) == 2
    assert module_0.modp(2, 101) == 4
    assert module_0.modp(3, 101) == 8
    assert module_0.modp(4, 101) == 16
    assert module_0.modp(5, 101) == 32


def test_modp_examples():
    """Test examples from the spec."""
    assert module_0.modp(3, 5) == 3        # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(1101, 101) == 2   # 2^1101 mod 101 = 2
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(3, 11) == 8       # 2^3 = 8
    assert module_0.modp(100, 101) == 1    # 2^100 mod 101 = 1 (Fermat's little theorem)


def test_modp_wraparound():
    """Test that values wrap around correctly modulo p."""
    assert module_0.modp(10, 7) == 1024 % 7   # 2^10 = 1024, 1024 % 7 = 2
    assert module_0.modp(6, 13) == 64 % 13    # 2^6 = 64, 64 % 13 = 12


def test_modp_returns_in_range():
    """Test that results are always in the range [0, p)."""
    for n in range(0, 50):
        for p in range(2, 20):
            result = module_0.modp(n, p)
            assert 0 <= result < p


def test_modp_p_is_two():
    """Test with p = 2, result should be 0 for n >= 1."""
    assert module_0.modp(0, 2) == 1
    assert module_0.modp(1, 2) == 0
    assert module_0.modp(2, 2) == 0
    assert module_0.modp(100, 2) == 0


def test_modp_matches_pow():
    """Test that modp matches built-in pow(2, n, p)."""
    for n in range(0, 30):
        for p in [2, 3, 5, 7, 11, 13, 97, 101]:
            assert module_0.modp(n, p) == pow(2, n, p)


def test_modp_large_n():
    """Test with large n values."""
    assert module_0.modp(1000, 1000000007) == pow(2, 1000, 1000000007)
    assert module_0.modp(12345, 65537) == pow(2, 12345, 65537)

# Generated at 2026-11-02 08:07:19.366219
# Unit test for function modp
def test_modp():
    # Basic case: 2^3 mod 5 = 8 mod 5 = 3
    assert module_0.modp(3, 5) == 3

    # Zero exponent: 2^0 = 1
    assert module_0.modp(0, 101) == 1

    # 2^3 mod 11 = 8
    assert module_0.modp(3, 11) == 8

    # Fermat's little theorem: 2^100 mod 101 = 1
    assert module_0.modp(100, 101) == 1

    # Large exponent: 2^1101 mod 101 = 2
    assert module_0.modp(1101, 101) == 2

    # Cycle check: 2^30 mod 5 = 4
    assert module_0.modp(30, 5) == 4

    # Cycle check: 2^31 mod 5 = 3
    assert module_0.modp(31, 5) == 3

    # Modulus of 1 always yields 0
    assert module_0.modp(5, 1) == 0

    # Negative exponent returns initial value 1 (loop doesn't execute)
    assert module_0.modp(-3, 7) == 1

    print("All tests passed!")


test_modp()

# Generated at 2026-11-02 08:10:00.204010
# Unit test for function modp
def test_modp():
    # nonce:7abf279d
    assert module_0.modp(3, 5) == 3          # 2^3 = 8, 8 % 5 = 3
    assert module_0.modp(1101, 101) == 2     # 2^1101 % 101 = 2
    assert module_0.modp(0, 101) == 1        # 2^0 = 1
    assert module_0.modp(3, 11) == 8         # 2^3 = 8
    assert module_0.modp(100, 101) == 1      # 2^100 % 101 = 1 (Fermat's little theorem)
    assert module_0.modp(10, 7) == 2         # 2^10 = 1024, 1024 % 7 = 2
    assert module_0.modp(1, 3) == 2          # 2^1 % 3 = 2
    assert module_0.modp(5, 13) == 6         # 2^5 = 32, 32 % 13 = 6

# Generated at 2026-11-02 08:11:35.685984
# Unit test for function modp
def test_modp():
    # Basic cases
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(1, 101) == 2
    assert module_0.modp(2, 101) == 4
    assert module_0.modp(3, 101) == 8
    assert module_0.modp(5, 101) == 32

    # Modulus wraps the value
    assert module_0.modp(10, 101) == 1024 % 101  # 1024 % 101 = 14
    assert module_0.modp(3, 5) == 3              # 8 % 5 = 3
    assert module_0.modp(4, 3) == 1              # 16 % 3 = 1
    assert module_0.modp(10, 5) == 4             # 1024 % 5 = 4

    # Large exponent
    assert module_0.modp(100, 101) == pow(2, 100, 101)

    # Modulus of 1 always yields 0
    assert module_0.modp(7, 1) == 0
    assert module_0.modp(0, 1) == 0

    # Powers of two as modulus
    assert module_0.modp(8, 256) == 0     # 2^8 % 256 = 0
    assert module_0.modp(7, 256) == 128   # 2^7 % 256 = 128

    # Consistency with built-in pow for random-ish values
    for n, p in [(0, 7), (1, 13), (2, 17), (6, 19), (15, 31), (20, 97), (50, 1000003)]:
        assert module_0.modp(n, p) == pow(2, n, p), f"failed for n={n}, p={p}"

    # Result is always within [0, p)
    for n in range(20):
        for p in [2, 3, 5, 7, 13, 101]:
            result = module_0.modp(n, p)
            assert 0 <= result < p