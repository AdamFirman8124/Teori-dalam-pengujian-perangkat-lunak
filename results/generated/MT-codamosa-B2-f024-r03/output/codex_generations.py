

# Generated at 2026-11-02 21:31:20.394627
# Unit test for function largest_divisor
def test_largest_divisor():
    # Composite numbers: largest proper divisor is n divided by its smallest prime factor
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(6) == 3
    assert module_0.largest_divisor(8) == 4
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(360) == 180

    # Prime numbers: only proper divisor is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(5) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Perfect squares
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(49) == 7

    # Powers of two
    assert module_0.largest_divisor(16) == 8
    assert module_0.largest_divisor(64) == 32

    # Property check: result divides n, is strictly less than n,
    # and no larger proper divisor exists
    for n in range(2, 300):
        d = module_0.largest_divisor(n)
        assert 1 <= d < n
        assert n % d == 0
        assert not any(n % k == 0 for k in range(d + 1, n))


if __name__ == "__main__":
    test_largest_divisor()
    print("All tests passed.")
# nonce:aa5c14f9

# Generated at 2026-11-02 21:33:40.577823
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic cases
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(100) == 50

    # Prime numbers: largest divisor is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Perfect squares
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(25) == 5

    # Even numbers
    assert module_0.largest_divisor(8) == 4
    assert module_0.largest_divisor(16) == 8

    # Large number
    assert module_0.largest_divisor(1000000) == 500000

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_divisor()

# Generated at 2026-11-02 21:36:19.811416
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(1) == 0  # edge case: no divisors below 1 except 0... range(1) is empty, but 0 % anything
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(5) == 1
    assert module_0.largest_divisor(6) == 3
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(28) == 14
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(101) == 1  # prime number

    # Verify result always divides n
    for n in range(2, 200):
        d = module_0.largest_divisor(n)
        assert n % d == 0
        assert d < n
        # Ensure no larger divisor exists below n
        assert all(n % i != 0 for i in range(d + 1, n))

    # Error cases
    with pytest.raises(ZeroDivisionError):
        module_0.largest_divisor(1)  # range(1) yields i=0, causing division by zero