

# Generated at 2026-10-25 11:46:34.286539
# Unit test for function largest_divisor

# Generated at 2026-10-25 11:46:49.299349
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(97) == 1

# Generated at 2026-10-25 11:46:51.955030
# Unit test for function largest_divisor

# Generated at 2026-10-25 11:46:54.375212
# Unit test for function largest_divisor

# Generated at 2026-10-25 11:46:56.788734
# Unit test for function largest_divisor

# Generated at 2026-10-25 11:46:59.404112
# Unit test for function largest_divisor

# Generated at 2026-10-25 11:47:01.817295
# Unit test for function largest_divisor

# Generated at 2026-10-25 11:47:04.233010
# Unit test for function largest_divisor

# Generated at 2026-10-25 11:47:18.301683
# Unit test for function largest_divisor
def test_largest_divisor():
    # Composite numbers: largest proper divisor is n / smallest_prime_factor
    assert module_0.largest_divisor(10) == 5      # 10 -> 5
    assert module_0.largest_divisor(15) == 5      # 15 -> 5
    assert module_0.largest_divisor(12) == 6      # 12 -> 6
    assert module_0.largest_divisor(49) == 7      # 49 -> 7
    assert module_0.largest_divisor(100) == 50    # 100 -> 50

    # Primes: largest proper divisor is always 1
    for p in [2, 3, 5, 7, 11, 13, 97, 101]:
        assert module_0.largest_divisor(p) == 1

    # Small values
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(6) == 3
    assert module_0.largest_divisor(9) == 3

    # Property check: result divides n and is less than n
    for n in range(2, 200):
        d = module_0.largest_divisor(n)
        assert n % d == 0
        assert 1 <= d < n

    # Result is the LARGEST such divisor (nothing between d and n divides n)
    for n in range(2, 200):
        d = module_0.largest_divisor(n)
        for k in range(d + 1, n):
            assert n % k != 0

    print("All tests passed.")

# Generated at 2026-10-25 11:47:19.715346
# Unit test for function largest_divisor

# Generated at 2026-10-25 11:47:21.679245
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(97) == 1