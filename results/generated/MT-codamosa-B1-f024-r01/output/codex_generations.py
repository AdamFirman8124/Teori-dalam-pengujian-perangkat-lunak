

# Generated at 2026-10-24 21:34:04.352692
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(2) == 1

# Generated at 2026-10-24 21:34:11.329090
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(2) == 1

# Generated at 2026-10-24 21:34:18.600990
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(2) == 1

    with pytest.raises(ValueError):
        module_0.largest_divisor(1)

# Generated at 2026-10-24 21:34:25.153272
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(13) == 1  # prime number
    assert module_0.largest_divisor(2) == 1

# Generated at 2026-10-24 21:34:32.220786
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(2) == 1