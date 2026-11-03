

# Generated at 2026-11-02 18:08:16.785357
# Unit test for function filter_integers
def test_filter_integers():
    # All integers pass through unchanged
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # Mixed types: only ints are kept
    assert module_0.filter_integers(['a', 1, 'b', 2, 3.5, 4]) == [1, 2, 4]

    # Empty list returns empty list
    assert module_0.filter_integers([]) == []

    # No integers present returns empty list
    assert module_0.filter_integers(['x', 'y', None, 3.14]) == []

    # Negative numbers and zero are preserved
    assert module_0.filter_integers([-1, 0, 'text', 100]) == [-1, 0, 100]

    # Floats that are whole numbers are not ints, so excluded
    assert module_0.filter_integers([2.0, 3, 4.0]) == [3]

    # None values are excluded
    assert module_0.filter_integers([None, 5, None, 7]) == [5, 7]

    # Order is preserved
    assert module_0.filter_integers([9, 'a', 1, 'b', 5]) == [9, 1, 5]

    # Strings that look like numbers are excluded
    assert module_0.filter_integers(['10', 10, '20']) == [10]

# Generated at 2026-11-02 18:09:36.693930
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types
    assert module_0.filter_integers([1, 'two', 3.0, 4, True, None, 5]) == [1, 4, True, 5]
    # Only integers
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    # No integers
    assert module_0.filter_integers(['a', 2.5, None, [1], {'x': 1}]) == []
    # Empty list
    assert module_0.filter_integers([]) == []
    # Negative and zero integers
    assert module_0.filter_integers([-1, 0, 1, 'x', 2.5]) == [-1, 0, 1]
    # Large integers
    assert module_0.filter_integers([10**18, 'big', 10**19]) == [10**18, 10**19]
    # Nested containers are not integers
    assert module_0.filter_integers([[1], (2,), {3}]) == []
    # Booleans are instances of int in Python
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

# Generated at 2026-11-02 18:10:20.975614
# Unit test for function filter_integers
def test_filter_integers():
    # Empty list
    assert module_0.filter_integers([]) == []

    # All integers
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # Mixed types
    assert module_0.filter_integers(['a', 1, 'b', 2, 3.5, None]) == [1, 2]

    # Floats are excluded (even whole-valued floats)
    assert module_0.filter_integers([1.0, 2.5, 3]) == [3]

    # Strings are excluded
    assert module_0.filter_integers(['1', '2', 'three']) == []

    # None values are excluded
    assert module_0.filter_integers([None, 5, None]) == [5]

    # Nested lists are excluded
    assert module_0.filter_integers([[1], [2, 3], 4]) == [4]

    # Booleans are instances of int in Python (edge case behavior)
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

    # Negative integers and zero are kept
    assert module_0.filter_integers([-1, 0, 'x', 2]) == [-1, 0, 2]

    # Large integers
    assert module_0.filter_integers([10**18, 1.5]) == [10**18]

# Generated at 2026-11-02 18:11:22.775412
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: keep only integers
    assert module_0.filter_integers([1, 2, 'a', 'b', 3.5, 4]) == [1, 2, 4]

    # Empty list returns empty list
    assert module_0.filter_integers([]) == []

    # No integers present
    assert module_0.filter_integers(['a', 3.5, None, [1], {'k': 1}]) == []

    # All integers present
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # Negative integers and zero are kept
    assert module_0.filter_integers([-1, 0, 'x', 7]) == [-1, 0, 7]

    # Booleans are instances of int in Python (bool is subclass of int)
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

    # Order and duplicates preserved
    assert module_0.filter_integers([5, 'a', 5, 2.0, 5]) == [5, 5, 5]

    # Floats that are whole numbers are still excluded
    assert module_0.filter_integers([2.0, 3.0, 3]) == [3]

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_integers()

# Generated at 2026-11-02 18:12:16.221239
# Unit test for function filter_integers
def test_filter_integers():
    # Basic filtering of mixed types
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers(["a", 1, 2.5, 3]) == [1, 3]
    assert module_0.filter_integers([1.5, "hello", None, 42]) == [42]

    # Empty list
    assert module_0.filter_integers([]) == []

    # No integers present
    assert module_0.filter_integers(["a", "b", 3.14]) == []

    # Negative integers and zero
    assert module_0.filter_integers([-1, 0, 1]) == [-1, 0, 1]

    # Nested structures are not integers
    assert module_0.filter_integers([[1], {2}, (3,), 4]) == [4]

    # Large integers
    assert module_0.filter_integers([10**18, "big"]) == [10**18]

    # Floats with integer values are excluded
    assert module_0.filter_integers([1.0, 2.0, 3]) == [3]

    # Boolean values are instances of int in Python, so they are kept
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]