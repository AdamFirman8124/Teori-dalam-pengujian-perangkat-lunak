

# Generated at 2026-10-25 06:53:25.591532
# Unit test for function compare
def test_compare():
    # all correct -> zeros
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    # one off by 1
    assert module_0.compare([1, 2, 3], [1, 2, 4]) == [0, 0, 1]
    # reversed
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    # negatives
    assert module_0.compare([-1, 5], [-3, 5]) == [2, 0]
    # floats
    assert module_0.compare([1.5, 2.0], [1.0, 3.5]) == [0.5, 1.5]
    # empty
    assert module_0.compare([], []) == []


if __name__ == "__main__":
    test_compare()
    print("all tests passed")

# Generated at 2026-10-25 06:53:28.028939
# Unit test for function compare

# Generated at 2026-10-25 06:53:30.485277
# Unit test for function compare

# Generated at 2026-10-25 06:53:32.893976
# Unit test for function compare

# Generated at 2026-10-25 06:53:35.310886
# Unit test for function compare

# Generated at 2026-10-25 06:53:37.722731
# Unit test for function compare

# Generated at 2026-10-25 06:53:40.136835
# Unit test for function compare

# Generated at 2026-10-25 06:53:42.556116
# Unit test for function compare

# Generated at 2026-10-25 06:53:44.970683
# Unit test for function compare

# Generated at 2026-10-25 06:53:47.384478
# Unit test for function compare

# Generated at 2026-10-25 06:53:49.807953
# Unit test for function compare

# Generated at 2026-10-25 06:53:52.219017
# Unit test for function compare

# Generated at 2026-10-25 06:53:54.633817
# Unit test for function compare