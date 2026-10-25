

# Generated at 2026-10-24 06:04:12.878371
# Unit test for function is_equal_to_sum_even
def test_is_equal_to_sum_even():
    assert module_0.is_equal_to_sum_even(8) is True
    assert module_0.is_equal_to_sum_even(10) is True
    assert module_0.is_equal_to_sum_even(100) is True

    assert module_0.is_equal_to_sum_even(7) is False
    assert module_0.is_equal_to_sum_even(9) is False
    assert module_0.is_equal_to_sum_even(0) is False
    assert module_0.is_equal_to_sum_even(-8) is False

# Generated at 2026-10-24 06:04:19.419817
# Unit test for function is_equal_to_sum_even
def test_is_equal_to_sum_even():
    assert module_0.is_equal_to_sum_even(8) is True
    assert module_0.is_equal_to_sum_even(10) is True
    assert module_0.is_equal_to_sum_even(100) is True

    assert module_0.is_equal_to_sum_even(6) is False
    assert module_0.is_equal_to_sum_even(7) is False
    assert module_0.is_equal_to_sum_even(9) is False
    assert module_0.is_equal_to_sum_even(0) is False
    assert module_0.is_equal_to_sum_even(-8) is False

# Generated at 2026-10-24 06:04:24.445963
# Unit test for function is_equal_to_sum_even
def test_is_equal_to_sum_even():
    assert module_0.is_equal_to_sum_even(8) is True
    assert module_0.is_equal_to_sum_even(10) is True
    assert module_0.is_equal_to_sum_even(100) is True

    assert module_0.is_equal_to_sum_even(7) is False
    assert module_0.is_equal_to_sum_even(6) is False
    assert module_0.is_equal_to_sum_even(9) is False
    assert module_0.is_equal_to_sum_even(-8) is False

# Generated at 2026-10-24 06:04:29.969024
# Unit test for function is_equal_to_sum_even
def test_is_equal_to_sum_even():
    assert module_0.is_equal_to_sum_even(8) is True
    assert module_0.is_equal_to_sum_even(10) is True
    assert module_0.is_equal_to_sum_even(100) is True

    assert module_0.is_equal_to_sum_even(7) is False
    assert module_0.is_equal_to_sum_even(6) is False
    assert module_0.is_equal_to_sum_even(9) is False
    assert module_0.is_equal_to_sum_even(0) is False
    assert module_0.is_equal_to_sum_even(-8) is False

# Generated at 2026-10-24 06:04:37.443051
# Unit test for function is_equal_to_sum_even
def test_is_equal_to_sum_even():
    # Valid even numbers
    assert module_0.is_equal_to_sum_even(8) is True
    assert module_0.is_equal_to_sum_even(10) is True
    assert module_0.is_equal_to_sum_even(100) is True

    # Even numbers below the minimum
    assert module_0.is_equal_to_sum_even(0) is False
    assert module_0.is_equal_to_sum_even(2) is False
    assert module_0.is_equal_to_sum_even(6) is False

    # Odd numbers
    assert module_0.is_equal_to_sum_even(7) is False
    assert module_0.is_equal_to_sum_even(9) is False
    assert module_0.is_equal_to_sum_even(101) is False