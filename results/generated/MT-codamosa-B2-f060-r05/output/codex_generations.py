

# Generated at 2026-11-03 01:12:28.873563
# Unit test for function sum_to_n
def test_sum_to_n():
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050
    assert module_0.sum_to_n(-5) == 0  # range(n+1) is empty for negative n

    # Larger value sanity check against formula n*(n+1)/2
    n = 1000
    assert module_0.sum_to_n(n) == n * (n + 1) // 2

# Generated at 2026-11-03 01:12:56.244312
# Unit test for function sum_to_n
def test_sum_to_n():assert module_0.sum_to_n(0) == 0, "module_0.sum_to_n(0) should be 0"

# Generated at 2026-11-03 01:13:49.676244
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic positive cases
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(5) == 15   # 1+2+3+4+5
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050

    # Edge case: n = 0
    assert module_0.sum_to_n(0) == 0

    # Negative input: range is empty, sum is 0
    assert module_0.sum_to_n(-1) == 0
    assert module_0.sum_to_n(-100) == 0

    # Larger input
    assert module_0.sum_to_n(1000) == 500500

    # Consistency with formula n*(n+1)//2
    for n in range(50):
        assert module_0.sum_to_n(n) == n * (n + 1) // 2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()

# Generated at 2026-11-03 01:14:46.098327
# Unit test for function sum_to_n
def test_sum_to_n():
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(2) == 3
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(30) == 465
    assert module_0.sum_to_n(100) == 5050

# Generated at 2026-11-03 01:15:26.860049
# Unit test for function sum_to_n
def test_sum_to_n():
    # Basic positive cases
    assert module_0.sum_to_n(0) == 0
    assert module_0.sum_to_n(1) == 1
    assert module_0.sum_to_n(5) == 15
    assert module_0.sum_to_n(10) == 55
    assert module_0.sum_to_n(100) == 5050

    # Negative input (range is empty, so sum is 0)
    assert module_0.sum_to_n(-5) == 0
    assert module_0.sum_to_n(-1) == 0

    # Large input
    assert module_0.sum_to_n(1000) == 500500

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_to_n()