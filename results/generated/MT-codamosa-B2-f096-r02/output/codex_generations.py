

# Generated at 2026-11-02 15:11:26.937580
# Unit test for function count_up_to
def test_count_up_to():
    # n less than 2 yields no primes
    assert module_0.count_up_to(-1) == []
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []

    # n = 2: range(2, 2) is empty
    assert module_0.count_up_to(2) == []

    # n = 3: only 2 is below 3
    assert module_0.count_up_to(3) == [2]

    # n = 5: primes below 5
    assert module_0.count_up_to(5) == [2, 3]

    # n = 10: primes below 10
    assert module_0.count_up_to(10) == [2, 3, 5, 7]

    # n = 20: primes below 20
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # n = 30: primes below 30
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Result contains only primes
    result = module_0.count_up_to(50)
    for p in result:
        assert all(p % j != 0 for j in range(2, p)), f"{p} is not prime"

    # Result is strictly increasing
    assert result == sorted(result)
    assert len(result) == len(set(result))

    print("All tests passed!")


if __name__ == "__main__":
    test_count_up_to()

# Generated at 2026-11-02 15:15:06.089729
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(-5) == []

# Generated at 2026-11-02 15:16:35.887265
# Unit test for function count_up_to
def test_count_up_to():
    # Test with a normal range
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    
    # Test with larger range
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    
    # Test with n = 2 (no primes less than 2)
    assert module_0.count_up_to(2) == []
    
    # Test with n = 3 (only prime less than 3 is 2)
    assert module_0.count_up_to(3) == [2]
    
    # Test with n = 0 and negative n (empty result)
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(-5) == []
    
    # Test that result is a list
    assert isinstance(module_0.count_up_to(5), list)
    
    # Test exact boundary: n=5 should include primes up to but not including 5
    assert module_0.count_up_to(5) == [2, 3]
    
    # Test n=6 should include 5
    assert module_0.count_up_to(6) == [2, 3, 5]
    
    print("All tests passed!")


test_count_up_to()

# Generated at 2026-11-02 15:18:57.043051
# Unit test for function count_up_to
def test_count_up_to():
    # Edge cases: empty results
    assert module_0.count_up_to(-5) == []
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []

    # Small values
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(5) == [2, 3]

    # Typical cases
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Boundary: primes strictly less than n (n itself excluded)
    assert module_0.count_up_to(7) == [2, 3, 5]
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(13) == [2, 3, 5, 7, 11]

    # Properties: sorted, no duplicates, all prime
    result = module_0.count_up_to(100)
    assert result == sorted(result)
    assert len(result) == len(set(result))
    assert len(result) == 25  # number of primes below 100
    for p in result:
        assert all(p % j != 0 for j in range(2, p)), f"{p} is not prime"
        assert p >= 2

    print("All tests passed!")


test_count_up_to()