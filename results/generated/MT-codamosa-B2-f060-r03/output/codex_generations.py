

# Generated at 2026-11-03 00:13:40.275810
# Unit test for function sum_to_n
def test_sum_to_n():
    # Test basic positive integers
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55

    # Test larger input
    assert module_0.sum_to_n(100) == 5050
    assert module_0.sum_to_n(1000) == 500500

    # Test negative input (range is empty, sum is 0)
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

    # Test consistency with formula n * (n + 1) / 2
    for n in range(0, 50):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()

# Generated at 2026-11-03 00:16:53.963699
# Unit test for function sum_to_n
def test_sum_to_n():
    # Base cases
    assert module_0.sum_to_n(0) == 0, "module_0.sum_to_n(0) should be 0"
    assert module_0.sum_to_n(1) == 1, "module_0.sum_to_n(1) should be 1"
    
    # Small known values
    assert module_0.sum_to_n(2) == 3, "module_0.sum_to_n(2) should be 3 (1+2)"
    assert module_0.sum_to_n(5) == 15, "module_0.sum_to_n(5) should be 15 (1+2+3+4+5)"
    assert module_0.sum_to_n(10) == 55, "module_0.sum_to_n(10) should be 55"
    
    # Verify against the closed-form formula n*(n+1)/2
    for n in range(0, 101):
        expected = n * (n + 1) // 2
        assert module_0.sum_to_n(n) == expected, f"module_0.sum_to_n({n}) should be {expected}"
    
    # Negative input: range(n+1) is empty, so sum is 0
    assert module_0.sum_to_n(-1) == 0, "module_0.sum_to_n(-1) should be 0"
    assert module_0.sum_to_n(-10) == 0, "module_0.sum_to_n(-10) should be 0"
    
    # Larger input
    assert module_0.sum_to_n(1000) == 500500, "module_0.sum_to_n(1000) should be 500500"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()

# Generated at 2026-11-03 00:19:20.732188
# Unit test for function sum_to_n
def test_sum_to_n():
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

# Generated at 2026-11-03 00:21:19.724835
# Unit test for function sum_to_n
def test_sum_to_n():
    # Base case: zero
    assert module_0.sum_to_n(0) == 0, "module_0.sum_to_n(0) should be 0"

    # Small positive values
    assert module_0.sum_to_n(1) == 1, "module_0.sum_to_n(1) should be 1"
    assert module_0.sum_to_n(2) == 3, "module_0.sum_to_n(2) should be 3"
    assert module_0.sum_to_n(5) == 15, "module_0.sum_to_n(5) should be 15"

    # Larger values
    assert module_0.sum_to_n(10) == 55, "module_0.sum_to_n(10) should be 55"
    assert module_0.sum_to_n(100) == 5050, "module_0.sum_to_n(100) should be 5050"

    # Negative input: range is empty, so sum is 0
    assert module_0.sum_to_n(-1) == 0, "module_0.sum_to_n(-1) should be 0"
    assert module_0.sum_to_n(-100) == 0, "module_0.sum_to_n(-100) should be 0"

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()