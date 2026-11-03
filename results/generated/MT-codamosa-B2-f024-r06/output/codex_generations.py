

# Generated at 2026-11-02 11:21:45.380103
# Unit test for function largest_divisor
def test_largest_divisor():
    # Composite numbers: largest proper divisor
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(6) == 3
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(36) == 18
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(100) == 50

    # Prime numbers: largest proper divisor is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Edge case: n=1 -> loop never runs, function returns None
    assert module_0.largest_divisor(1) is None

    # Property check: result divides n and is strictly less than n
    for n in range(2, 300):
        d = module_0.largest_divisor(n)
        assert 1 <= d < n
        assert n % d == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_divisor()

# Generated at 2026-11-02 11:24:57.344054
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(36) == 18

# Generated at 2026-11-02 11:27:11.684694
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic composite numbers
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(100) == 50

    # Perfect squares
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(36) == 18

    # Prime numbers -> largest (proper) divisor is 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Smallest valid input
    assert module_0.largest_divisor(2) == 1

    # Powers of two
    assert module_0.largest_divisor(8) == 4
    assert module_0.largest_divisor(1024) == 512

    print("All tests passed!")


test_largest_divisor()

# Generated at 2026-11-02 11:29:52.358821
# Unit test for function largest_divisor
def test_largest_divisor():
    # Composite numbers
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(36) == 18

    # Prime numbers -> largest divisor below n is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1

    # Edge case: n = 1 has no valid divisor (division by zero in loop)
    with pytest.raises(ZeroDivisionError):
        module_0.largest_divisor(1)