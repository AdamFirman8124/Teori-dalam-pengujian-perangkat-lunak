

# Generated at 2026-11-02 00:46:05.171027
# Unit test for function sum_to_n
def test_sum_to_n():
    # Base cases
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    
    # Typical cases
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050
    
    # Larger input
    assert module_0.sum_to_n(1000) == 500500
    
    # Negative inputs yield empty range, so sum is 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

# Generated at 2026-11-02 00:47:36.661988
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic cases
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050

    # Larger input
    assert module_0.sum_to_n(1000) == 500500

    # Negative input: sum(range(0)) == 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

    # Verify against direct formula n*(n+1)//2 for a range of values
    for n in range(0, 50):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2

# Generated at 2026-11-02 00:48:56.747879
# Unit test for function sum_to_n
def test_sum_to_n():
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(3) == 6
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(30) == 465
    assert module_0.sum_to_n(100) == 5050
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0

# Generated at 2026-11-02 00:49:49.083282
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic cases
    assert module_0.sum_to_n(0) == 0          # sum of range(1) -> [0]
    assert module_0.sum_to_n(1) == 1          # 0 + 1
    assert module_0.sum_to_n(5) == 15         # 0+1+2+3+4+5
    assert module_0.sum_to_n(10) == 55        # 0..10
    assert module_0.sum_to_n(100) == 5050     # classic Gauss result

    # Larger input
    assert module_0.sum_to_n(1000) == 500500

    # Edge cases: negative inputs yield an empty range -> 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-10) == 0


if __name__ == "__main__":
    test_sum_to_n()
    print("All tests passed!")

# Generated at 2026-11-02 00:50:55.476576
# Unit test for function sum_to_n
def test_sum_to_n():
    # Test basic cases
    assert module_0.sum_to_n(0) == 0      # sum of range(1) -> [0]
    assert module_0.sum_to_n(1) == 1      # 0 + 1
    assert module_0.sum_to_n(2) == 3      # 0 + 1 + 2

    # Test typical values
    assert module_0.sum_to_n(5) == 15     # 0+1+2+3+4+5
    assert module_0.sum_to_n(10) == 55    # 0+...+10
    assert module_0.sum_to_n(100) == 5050 # Gauss formula check

    # Test larger value
    assert module_0.sum_to_n(1000) == 500500

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()