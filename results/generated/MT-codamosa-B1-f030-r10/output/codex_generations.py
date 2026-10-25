

# Generated at 2026-10-24 06:33:17.696637
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2]) == []
    assert module_0.get_positive([0, -1, 0]) == []
    assert module_0.get_positive([]) == []

# Generated at 2026-10-24 06:33:20.193269
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:22.610698
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:25.023217
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:27.524851
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:29.938921
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:32.354829
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:34.768895
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:37.276401
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:39.693747
# Unit test for function get_positive

# Generated at 2026-10-24 06:33:48.830421
# Unit test for function get_positive
def test_get_positive():
    # Typical mixed list
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    # All positive
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    # All negative
    assert module_0.get_positive([-1, -2, -3]) == []
    # Empty list
    assert module_0.get_positive([]) == []
    # Zero is not positive
    assert module_0.get_positive([0, 1, -1]) == [1]
    # Duplicates and floats
    assert module_0.get_positive([-3.5, 3.5, 2, -2]) == [3.5, 2]
    # Single element
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []