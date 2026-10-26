

# Generated at 2026-10-25 14:11:12.956160
# Unit test for function largest_divisor

# Generated at 2026-10-25 14:11:15.369300
# Unit test for function largest_divisor

# Generated at 2026-10-25 14:11:17.788291
# Unit test for function largest_divisor

# Generated at 2026-10-25 14:11:20.696061
# Unit test for function largest_divisor

# Generated at 2026-10-25 14:11:23.137135
# Unit test for function largest_divisor

# Generated at 2026-10-25 14:11:25.553587
# Unit test for function largest_divisor

# Generated at 2026-10-25 14:11:27.971389
# Unit test for function largest_divisor

# Generated at 2026-10-25 14:11:35.420945
# Unit test for function largest_divisor
def test_largest_divisor():assert module_0.largest_divisor(12) == 6

# Generated at 2026-10-25 14:12:02.144360
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(13) == 1  # Prime number
    assert module_0.largest_divisor(2) == 1

    with pytest.raises(ValueError):
        module_0.largest_divisor(1)

# Generated at 2026-10-25 14:12:07.679845
# Unit test for function largest_divisor

# Generated at 2026-10-25 14:12:13.728847
# Unit test for function largest_divisor
def test_largest_divisor():assert module_0.largest_divisor(2) == 1