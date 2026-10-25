

# Generated at 2026-10-24 13:50:16.754387
# Unit test for function get_positive

# Generated at 2026-10-24 13:50:19.333907
# Unit test for function get_positive

# Generated at 2026-10-24 13:50:21.869703
# Unit test for function get_positive

# Generated at 2026-10-24 13:50:24.627208
# Unit test for function get_positive

# Generated at 2026-10-24 13:50:27.042235
# Unit test for function get_positive

# Generated at 2026-10-24 13:50:29.454400
# Unit test for function get_positive

# Generated at 2026-10-24 13:50:31.879104
# Unit test for function get_positive

# Generated at 2026-10-24 13:50:35.574866
# Unit test for function get_positive
def test_get_positive():assert module_0.get_positive([-3, -1, 0, 1, 2, 5]) == [1, 2, 5]

# Generated at 2026-10-24 13:50:36.939057
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([1, -1, 2, -2, 0, 3]) == [1, 2, 3]
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([-1, -2, -3]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([0, 0, 0]) == []

# Generated at 2026-10-24 13:50:38.315165
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([1, -1, 2, -2, 0, 3]) == [1, 2, 3]
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([-1, -2, -3]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([0, 0, 0]) == []