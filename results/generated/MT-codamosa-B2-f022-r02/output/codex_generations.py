

# Generated at 2026-10-24 04:10:54.590399
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: keep only ints
    assert module_0.filter_integers([1, 2, "three", 4.5, None]) == [1, 2, 4]

    # All integers pass through
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers -> empty list
    assert module_0.filter_integers(["a", 3.14, None, [1], {"x": 1}]) == []

    # Empty input
    assert module_0.filter_integers([]) == []

    # Negative and zero
    assert module_0.filter_integers([-5, 0, "0", 5.0]) == [-5, 0]

    # Floats that look whole are still excluded
    assert module_0.filter_integers([7.0, 7, 7.5]) == [7]

    # Order is preserved
    assert module_0.filter_integers([9, "x", 8, "y", 7]) == [9, 8, 7]


test_filter_integers()
print("All tests passed.")

# Generated at 2026-10-24 04:10:55.910302
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: keep only ints
    assert module_0.filter_integers([1, 2, "three", 4.5, None]) == [1, 2, 4]

    # All integers pass through
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers -> empty list
    assert module_0.filter_integers(["a", 3.14, None, [1], {"x": 1}]) == []

    # Empty input
    assert module_0.filter_integers([]) == []

    # Negative and zero
    assert module_0.filter_integers([-5, 0, "0", 5.0]) == [-5, 0]

    # Floats that look whole are still excluded
    assert module_0.filter_integers([7.0, 7, 7.5]) == [7]

    # Order is preserved
    assert module_0.filter_integers([9, "x", 8, "y", 7]) == [9, 8, 7]


test_filter_integers()
print("All tests passed.")

# Generated at 2026-10-24 04:10:57.234366
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: keep only ints
    assert module_0.filter_integers([1, 2, "three", 4.5, None]) == [1, 2, 4]

    # All integers pass through
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers -> empty list
    assert module_0.filter_integers(["a", 3.14, None, [1], {"x": 1}]) == []

    # Empty input
    assert module_0.filter_integers([]) == []

    # Negative and zero
    assert module_0.filter_integers([-5, 0, "0", 5.0]) == [-5, 0]

    # Floats that look whole are still excluded
    assert module_0.filter_integers([7.0, 7, 7.5]) == [7]

    # Order is preserved
    assert module_0.filter_integers([9, "x", 8, "y", 7]) == [9, 8, 7]


test_filter_integers()
print("All tests passed.")

# Generated at 2026-10-24 04:10:58.546282
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: keep only ints
    assert module_0.filter_integers([1, 2, "three", 4.5, None]) == [1, 2, 4]

    # All integers pass through
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers -> empty list
    assert module_0.filter_integers(["a", 3.14, None, [1], {"x": 1}]) == []

    # Empty input
    assert module_0.filter_integers([]) == []

    # Negative and zero
    assert module_0.filter_integers([-5, 0, "0", 5.0]) == [-5, 0]

    # Floats that look whole are still excluded
    assert module_0.filter_integers([7.0, 7, 7.5]) == [7]

    # Order is preserved
    assert module_0.filter_integers([9, "x", 8, "y", 7]) == [9, 8, 7]


test_filter_integers()
print("All tests passed.")

# Generated at 2026-10-24 04:10:59.845770
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: keep only ints
    assert module_0.filter_integers([1, 2, "three", 4.5, None]) == [1, 2, 4]

    # All integers pass through
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers -> empty list
    assert module_0.filter_integers(["a", 3.14, None, [1], {"x": 1}]) == []

    # Empty input
    assert module_0.filter_integers([]) == []

    # Negative and zero
    assert module_0.filter_integers([-5, 0, "0", 5.0]) == [-5, 0]

    # Floats that look whole are still excluded
    assert module_0.filter_integers([7.0, 7, 7.5]) == [7]

    # Order is preserved
    assert module_0.filter_integers([9, "x", 8, "y", 7]) == [9, 8, 7]


test_filter_integers()
print("All tests passed.")