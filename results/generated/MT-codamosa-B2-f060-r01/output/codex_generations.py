

# Generated at 2026-11-03 04:54:10.972433
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic positive cases
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050

    # Verify against the closed-form formula n*(n+1)/2
    for n in range(1, 50):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2

    # Negative inputs produce an empty range, so the sum is 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

    # Large input sanity check
    assert module_0.sum_to_n(10000) == 10000 * 10001 // 2

# Generated at 2026-11-03 04:55:56.435701
# Unit test for function sum_to_n
def test_sum_to_n():
    # Test with 0
    assert module_0.sum_to_n(0) == 0
    
    # Test with 1
    assert module_0.sum_to_n(1) == 1
    
    # Test with a small positive number
    assert module_0.sum_to_n(5) == 15
    
    # Test with a larger number
    assert module_0.sum_to_n(10) == 55
    
    # Test with 100
    assert module_0.sum_to_n(100) == 5050
    
    # Test with a negative number (range is empty, sum is 0)
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0
    
    print("All tests passed!")

# Generated at 2026-11-03 04:58:38.138120
# Unit test for function sum_to_n
def test_sum_to_n():
    # Test with zero
    assert module_0.sum_to_n(0) == 0

    # Test with one
    assert module_0.sum_to_n(1) == 1

    # Test with small positive integers
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55

    # Test with larger numbers
    assert module_0.sum_to_n(100) == 5050
    assert module_0.sum_to_n(1000) == 500500

    # Test with negative input (empty range sums to 0)
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

    # Verify against closed-form formula n*(n+1)/2 for a range of values
    for n in range(0, 50):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2