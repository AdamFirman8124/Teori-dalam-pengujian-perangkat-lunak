

# Generated at 2026-10-25 06:56:15.290215
# Unit test for function is_equal_to_sum_even
def test_is_equal_to_sum_even():
    # True: even numbers >= 8
    assert module_0.is_equal_to_sum_even(8) is True
    assert module_0.is_equal_to_sum_even(10) is True
    assert module_0.is_equal_to_sum_even(12) is True
    assert module_0.is_equal_to_sum_even(100) is True

    # False: odd numbers, even if >= 8
    assert module_0.is_equal_to_sum_even(9) is False
    assert module_0.is_equal_to_sum_even(11) is False
    assert module_0.is_equal_to_sum_even(15) is False

    # False: even numbers < 8
    assert module_0.is_equal_to_sum_even(6) is False
    assert module_0.is_equal_to_sum_even(4) is False
    assert module_0.is_equal_to_sum_even(2) is False
    assert module_0.is_equal_to_sum_even(0) is False

    # False: negative numbers
    assert module_0.is_equal_to_sum_even(-8) is False
    assert module_0.is_equal_to_sum_even(-10) is False

    # Boundary: 7 / 8 / 9
    assert module_0.is_equal_to_sum_even(7) is False
    assert module_0.is_equal_to_sum_even(8) is True
    assert module_0.is_equal_to_sum_even(9) is False

# Generated at 2026-10-25 06:56:17.705715
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:20.120464
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:22.534116
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:25.121314
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:27.544266
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:29.960751
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:32.373226
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:34.788327
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:37.205430
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:39.625388
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:42.059953
# Unit test for function is_equal_to_sum_even

# Generated at 2026-10-25 06:56:44.474526
# Unit test for function is_equal_to_sum_even