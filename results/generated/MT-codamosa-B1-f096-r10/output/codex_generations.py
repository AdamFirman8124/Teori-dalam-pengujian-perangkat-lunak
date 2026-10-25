

# Generated at 2026-10-24 12:33:19.351609
# Unit test for function count_up_to

# Generated at 2026-10-24 12:33:21.918178
# Unit test for function count_up_to

# Generated at 2026-10-24 12:33:24.335622
# Unit test for function count_up_to

# Generated at 2026-10-24 12:33:32.803606
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(12) == [2, 3, 5, 7, 11]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # Result must be strictly increasing
    result = module_0.count_up_to(50)
    assert all(a < b for a, b in zip(result, result[1:]))
    # Every returned value is prime (no divisors up to sqrt)
    for p in result:
        assert all(p % d != 0 for d in range(2, int(p ** 0.5) + 1))
    # No primes missed below n
    assert set(result) == {p for p in range(2, 50) if all(p % d != 0 for d in range(2, int(p ** 0.5) + 1))}

test_count_up_to()
print("All tests passed.")

# Generated at 2026-10-24 12:33:34.115163
# Unit test for function count_up_to
def test_count_up_to():
    # Basic cases
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(2) == []          # range excludes 2
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(-5) == []

    # Boundary: n is exclusive
    assert module_0.count_up_to(11) == [2, 3, 5, 7]

    # Larger check
    result = module_0.count_up_to(30)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Types
    assert all(isinstance(p, int) for p in module_0.count_up_to(20))

    print("All tests passed!")


test_count_up_to()

# Generated at 2026-10-24 12:33:35.432928
# Unit test for function count_up_to
def test_count_up_to():
    # Basic cases
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(2) == []          # range excludes 2
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(-5) == []

    # Boundary: n is exclusive
    assert module_0.count_up_to(11) == [2, 3, 5, 7]

    # Larger check
    result = module_0.count_up_to(30)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Types
    assert all(isinstance(p, int) for p in module_0.count_up_to(20))

    print("All tests passed!")


test_count_up_to()

# Generated at 2026-10-24 12:33:36.743609
# Unit test for function count_up_to
def test_count_up_to():
    # Basic cases
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(2) == []          # range excludes 2
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(-5) == []

    # Boundary: n is exclusive
    assert module_0.count_up_to(11) == [2, 3, 5, 7]

    # Larger check
    result = module_0.count_up_to(30)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Types
    assert all(isinstance(p, int) for p in module_0.count_up_to(20))

    print("All tests passed!")


test_count_up_to()