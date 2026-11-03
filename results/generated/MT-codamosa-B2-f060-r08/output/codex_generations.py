

# Generated at 2026-11-02 12:15:38.728952
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

    # Negative input yields empty range, so sum is 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

    # Cross-check against formula n * (n + 1) / 2
    for n in range(0, 200):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2

    print("All tests passed!")

# Generated at 2026-11-02 12:17:30.134622
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic positive cases
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55

    # Larger input
    assert module_0.sum_to_n(100) == 5050
    assert module_0.sum_to_n(1000) == 500500

    # Negative input: range(n + 1) is empty, so result is 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

# Generated at 2026-11-02 12:18:20.783504
# Unit test for function sum_to_n
def test_sum_to_n():
    # Test with zero
    assert module_0.sum_to_n(0) == 0

    # Test with small positive integers
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55

    # Test with larger number
    assert module_0.sum_to_n(100) == 5050

    # Test with a large number
    assert module_0.sum_to_n(1000) == 500500

    # Test with negative input (range is empty, so sum is 0)
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

    print("All tests passed!")


# Run the test
test_sum_to_n()

# Generated at 2026-11-02 12:19:12.213900
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic positive cases
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(5) == 15      # 1+2+3+4+5
    assert module_0.sum_to_n(6) == 21
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050

    # Edge cases
    assert module_0.sum_to_n(0) == 0       # empty range
    assert module_0.sum_to_n(-1) == 0      # negative input yields empty range
    assert module_0.sum_to_n(-100) == 0

    # Large input
    assert module_0.sum_to_n(1000) == 500500

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()

# Generated at 2026-11-02 12:19:53.402583
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic positive cases
    assert module_0.sum_to_n(0) == 0, "module_0.sum_to_n(0) should be 0"
    assert module_0.sum_to_n(1) == 1, "module_0.sum_to_n(1) should be 1"
    assert module_0.sum_to_n(5) == 15, "module_0.sum_to_n(5) should be 15"
    assert module_0.sum_to_n(10) == 55, "module_0.sum_to_n(10) should be 55"
    assert module_0.sum_to_n(100) == 5050, "module_0.sum_to_n(100) should be 5050"

    # Larger value
    assert module_0.sum_to_n(1000) == 500500, "module_0.sum_to_n(1000) should be 500500"

    # Negative input: range(n+1) is empty, so sum is 0
    assert module_0.sum_to_n(-1) == 0, "module_0.sum_to_n(-1) should be 0 (empty range)"
    assert module_0.sum_to_n(-10) == 0, "module_0.sum_to_n(-10) should be 0 (empty range)"

    # Cross-check against formula n*(n+1)/2 for several values
    for n in range(0, 50):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2, f"module_0.sum_to_n({n}) should match formula"

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()