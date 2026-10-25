

# Generated at 2026-10-24 12:42:34.160840
# Unit test for function get_positive

# Generated at 2026-10-24 12:42:36.577582
# Unit test for function get_positive

# Generated at 2026-10-24 12:42:38.997448
# Unit test for function get_positive

# Generated at 2026-10-24 12:42:41.412674
# Unit test for function get_positive

# Generated at 2026-10-24 12:42:43.827010
# Unit test for function get_positive

# Generated at 2026-10-24 12:42:46.427271
# Unit test for function get_positive

# Generated at 2026-10-24 12:42:48.841155
# Unit test for function get_positive

# Generated at 2026-10-24 12:42:52.217682
# Unit test for function get_positive
def test_get_positive():assert module_0.get_positive([-3, -1, 0, 1, 2, 5]) == [1, 2, 5]

# Generated at 2026-10-24 12:42:53.568613
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([1, -1, 2, -2, 0, 3]) == [1, 2, 3]
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([-1, -2, -3]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([0, 0, 0]) == []

# Generated at 2026-10-24 12:42:54.932346
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([1, -1, 2, -2, 0, 3]) == [1, 2, 3]
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([-1, -2, -3]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([0, 0, 0]) == []