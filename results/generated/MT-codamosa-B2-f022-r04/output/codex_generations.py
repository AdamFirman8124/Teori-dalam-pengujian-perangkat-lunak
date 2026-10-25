

# Generated at 2026-10-24 16:07:57.667384
# Unit test for function filter_integers

# Generated at 2026-10-24 16:08:00.079798
# Unit test for function filter_integers

# Generated at 2026-10-24 16:08:02.679459
# Unit test for function filter_integers

# Generated at 2026-10-24 16:08:05.089378
# Unit test for function filter_integers

# Generated at 2026-10-24 16:08:07.501403
# Unit test for function filter_integers

# Generated at 2026-10-24 16:08:10.138406
# Unit test for function filter_integers

# Generated at 2026-10-24 16:08:12.555228
# Unit test for function filter_integers

# Generated at 2026-10-24 16:08:14.967849
# Unit test for function filter_integers

# Generated at 2026-10-24 16:08:31.577291
# Unit test for function filter_integers
def test_filter_integers():
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers([1, 'a', 2.5, 3, True, None]) == [1, 3]
    assert module_0.filter_integers([]) == []
    assert module_0.filter_integers(['x', 'y']) == []
    assert module_0.filter_integers([0, -1, 3.14, 100]) == [0, -1, 100]

# Generated at 2026-10-24 16:08:33.215101
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types
    assert module_0.filter_integers([1, 2, 'a', 3.5, None]) == [1, 2, 3]
    # Only integers
    assert module_0.filter_integers([10, 20, 30]) == [10, 20, 30]
    # No integers
    assert module_0.filter_integers(['x', 4.2, None, [1]]) == []
    # Empty list
    assert module_0.filter_integers([]) == []
    # Negative and zero
    assert module_0.filter_integers([-1, 0, 1, 'z']) == [-1, 0, 1]
    # Large ints
    assert module_0.filter_integers([10**18, 'big']) == [10**18]
    print("All tests passed.")


test_filter_integers()

# Generated at 2026-10-24 16:08:34.648194
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types
    assert module_0.filter_integers([1, 2, 'a', 3.5, None]) == [1, 2, 3]
    # Only integers
    assert module_0.filter_integers([10, 20, 30]) == [10, 20, 30]
    # No integers
    assert module_0.filter_integers(['x', 4.2, None, [1]]) == []
    # Empty list
    assert module_0.filter_integers([]) == []
    # Negative and zero
    assert module_0.filter_integers([-1, 0, 1, 'z']) == [-1, 0, 1]
    # Large ints
    assert module_0.filter_integers([10**18, 'big']) == [10**18]
    print("All tests passed.")


test_filter_integers()