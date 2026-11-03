

# Generated at 2026-11-02 14:37:15.972208
# Unit test for function sum_to_n
def test_sum_to_n():
    # Test with small positive integers
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(3) == 6
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050

    # Test with larger input
    assert module_0.sum_to_n(1000) == 500500

    # Test with negative input (sum over empty range)
    assert module_0.sum_to_n(-5) == 0

    # Test result type
    assert isinstance(module_0.sum_to_n(7), int)

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()

# Generated at 2026-11-02 14:39:36.526803
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic cases
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15  # 1+2+3+4+5
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050

    # Negative input: range(n+1) is empty for n < 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

    # Larger input
    assert module_0.sum_to_n(1000) == 500500

    # Consistency check against formula n*(n+1)//2
    for n in range(0, 50):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()

# Generated at 2026-11-02 14:41:30.099143
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic positive cases
    assert module_0.sum_to_n(0) == 0, "module_0.sum_to_n(0) should be 0"
    assert module_0.sum_to_n(1) == 1, "module_0.sum_to_n(1) should be 1"
    assert module_0.sum_to_n(5) == 15, "module_0.sum_to_n(5) should be 15"
    assert module_0.sum_to_n(10) == 55, "module_0.sum_to_n(10) should be 55"
    assert module_0.sum_to_n(100) == 5050, "module_0.sum_to_n(100) should be 5050"

    # Edge case: negative input yields empty range -> 0
    assert module_0.sum_to_n(-1) == 0, "module_0.sum_to_n(-1) should be 0"
    assert module_0.sum_to_n(-100) == 0, "module_0.sum_to_n(-100) should be 0"

    # Large input sanity check using formula n*(n+1)//2
    n = 10000
    assert module_0.sum_to_n(n) == n * (n + 1) // 2, f"module_0.sum_to_n({n}) should be {n * (n + 1) // 2}"

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()

# Generated at 2026-11-02 14:45:38.372412
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic cases
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55

    # Larger value
    assert module_0.sum_to_n(100) == 5050

    # Negative input: range(n + 1) is empty, so result is 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

    # Cross-check against closed-form formula n * (n + 1) / 2
    for n in range(0, 50):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2


test_sum_to_n()
print("All tests passed!")