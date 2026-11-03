

# Generated at 2026-11-03 02:44:35.466322
# Unit test for function filter_integers
def test_filter_integers():
    # All integers
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers
    assert module_0.filter_integers(['a', 'b', 'c']) == []

    # Mixed types
    assert module_0.filter_integers([1, 'a', 2.5, 3]) == [1, 3]

    # Empty list
    assert module_0.filter_integers([]) == []

    # None and floats filtered out
    assert module_0.filter_integers([None, 3.14, 'hello', 42, [1, 2]]) == [42]

    # Negative integers and zero
    assert module_0.filter_integers([-1, -2, 0]) == [-1, -2, 0]

    # Booleans are instances of int in Python
    assert module_0.filter_integers([True, False, 5]) == [True, False, 5]

    # Preserve order
    assert module_0.filter_integers([10, 'x', 20, 'y', 30]) == [10, 20, 30]

    # Input list is not modified
    values = [1, 'a', 2]
    result = module_0.filter_integers(values)
    assert values == [1, 'a', 2]
    assert result == [1, 2]

    # Large integers
    assert module_0.filter_integers([10**18, 'big', 10**9]) == [10**18, 10**9]

# Generated at 2026-11-03 02:47:02.467808
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: only ints kept
    assert module_0.filter_integers([1, 2.5, 'three', 4, None]) == [1, 4]
    # Empty list
    assert module_0.filter_integers([]) == []
    # All integers
    assert module_0.filter_integers([5, 10, 15]) == [5, 10, 15]
    # No integers
    assert module_0.filter_integers(['a', 2.5, None, [1]]) == []
    # Negative integers and zero
    assert module_0.filter_integers([-1, 0, 'x', 2.0]) == [-1, 0]
    # Order is preserved
    assert module_0.filter_integers([3, 'a', 1, 'b', 2]) == [3, 1, 2]
    # Booleans are instances of int in Python, so they are kept
    assert module_0.filter_integers([True, False, 'yes']) == [True, False]

# Generated at 2026-11-03 02:49:41.742918
# Unit test for function filter_integers
def test_filter_integers():
    # nonce:117b6e51
    # Mixed types: only integers are kept
    assert module_0.filter_integers(['a', 3.14, 5]) == [5]

    # Empty list returns an empty list
    assert module_0.filter_integers([]) == []

    # All integers are kept in original order
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers results in an empty list
    assert module_0.filter_integers(['hello', 4.5, None, [1], (2,)]) == []

    # Zero and negative integers are kept
    assert module_0.filter_integers([0, -1, 1.5, 'x']) == [0, -1]

    # Duplicates are preserved
    assert module_0.filter_integers([7, 7, 'a', 7]) == [7, 7, 7]

    # Large integers are kept
    assert module_0.filter_integers([10**18, 'big']) == [10**18]

    # Note: bool is a subclass of int, so booleans pass the isinstance check
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

# Generated at 2026-11-03 02:50:57.623427
# Unit test for function filter_integers
def test_filter_integers():
    assert module_0.filter_integers([]) == []
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers([1, 'a', 2.5, 3]) == [1, 3]
    assert module_0.filter_integers(['a', 'b', 'c']) == []
    assert module_0.filter_integers([1.0, 2, 'three', 4, None]) == [2, 4]
    assert module_0.filter_integers([-1, 0, 1]) == [-1, 0, 1]
    assert module_0.filter_integers([1, [2], {'a': 3}, 4]) == [1, 4]
    assert module_0.filter_integers([True, 5, False]) == [True, 5, False]  # bool is a subclass of int

# Generated at 2026-11-03 02:52:02.957496
# Unit test for function filter_integers
def test_filter_integers():
    # Test with mixed types
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers(['a', 'b', 'c']) == []
    assert module_0.filter_integers([1, 'a', 2.5, 3]) == [1, 3]
    assert module_0.filter_integers([]) == []

    # Test with various types
    assert module_0.filter_integers([None, True, False]) == [True, False]  # bool is subclass of int
    assert module_0.filter_integers([3.14, 'hello', 42, [1, 2], 7]) == [42, 7]
    assert module_0.filter_integers([-1, 0, 1]) == [-1, 0, 1]

    # Test with nested structures
    assert module_0.filter_integers([[1, 2], {'a': 3}, 4]) == [4]

    # Test with large numbers
    assert module_0.filter_integers([10**18, 'big', -10**18]) == [10**18, -10**18]

    print("All test cases passed!")


if __name__ == "__main__":
    test_filter_integers()