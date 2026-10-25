

# Generated at 2026-10-24 06:05:12.158093
# Unit test for function rolling_max
def test_rolling_max():
    # Basic case
    assert module_0.rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Decreasing sequence
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
    # Mixed up/down
    assert module_0.rolling_max([3, 1, 4, 1, 5, 9, 2, 6]) == [3, 3, 4, 4, 5, 9, 9, 9]
    # Single element
    assert module_0.rolling_max([7]) == [7]
    # Negative numbers
    assert module_0.rolling_max([-5, -1, -3, -2]) == [-5, -1, -1, -1]
    # Duplicates
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]
    # Empty list
    assert module_0.rolling_max([]) == []
    print("All tests passed!")


test_rolling_max()

# Generated at 2026-10-24 06:05:14.684602
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:17.188985
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:19.605142
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:22.019675
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:24.433966
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:26.847806
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:29.263236
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:31.681492
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:34.231016
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:36.644848
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:39.063078
# Unit test for function rolling_max

# Generated at 2026-10-24 06:05:41.483595
# Unit test for function rolling_max