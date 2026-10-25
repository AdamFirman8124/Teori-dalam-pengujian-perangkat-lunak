

# Generated at 2026-10-24 14:17:15.515541
# Unit test for function compare
def test_compare():
    # Exact matches -> 0
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # All wrong -> absolute differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Mixed hits and misses
    assert module_0.compare([1, 2, 3, 4], [1, 2, 3, -4]) == [0, 0, 0, 8]

    # Negative numbers
    assert module_0.compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

    # Empty input -> empty output
    assert module_0.compare([], []) == []

    # Unequal lengths raise no error with zip, but should be tested intentionally
    assert module_0.compare([1, 2], [1]) == [0]  # zip truncates â document this behavior

    print("All tests passed!")

test_compare()

# Generated at 2026-10-24 14:17:18.117738
# Unit test for function compare

# Generated at 2026-10-24 14:17:20.532171
# Unit test for function compare

# Generated at 2026-10-24 14:17:22.948052
# Unit test for function compare

# Generated at 2026-10-24 14:17:25.360613
# Unit test for function compare

# Generated at 2026-10-24 14:17:27.778404
# Unit test for function compare

# Generated at 2026-10-24 14:17:30.194522
# Unit test for function compare

# Generated at 2026-10-24 14:17:32.609375
# Unit test for function compare

# Generated at 2026-10-24 14:17:35.026361
# Unit test for function compare

# Generated at 2026-10-24 14:17:37.438675
# Unit test for function compare

# Generated at 2026-10-24 14:17:39.851555
# Unit test for function compare

# Generated at 2026-10-24 14:17:42.276713
# Unit test for function compare

# Generated at 2026-10-24 14:17:44.690792
# Unit test for function compare