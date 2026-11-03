

# Generated at 2026-11-02 13:10:52.858329
# Unit test for function filter_integers
def test_filter_integers():
    # Test with mixed types
    assert module_0.filter_integers([1, 2, 3, 'a', 'b', 4.5]) == [1, 2, 3]

    # Test with only integers
    assert module_0.filter_integers([10, 20, 30]) == [10, 20, 30]

    # Test with no integers
    assert module_0.filter_integers(['a', 'b', 3.14, None, [1], {'k': 1}]) == []

    # Test with empty list
    assert module_0.filter_integers([]) == []

    # Test with negative integers and zero
    assert module_0.filter_integers([-1, 0, 1, 'x', 2.0]) == [-1, 0, 1]

    # Test with booleans (bool is subclass of int in Python)
    assert module_0.filter_integers([True, False, 5]) == [True, False, 5]

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_integers()

# Generated at 2026-11-02 13:12:00.943851
# Unit test for function filter_integers
def test_filter_integers():
    # All integers pass through unchanged
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # Mixed types: only integers kept
    assert module_0.filter_integers([1, 'a', 2.5, 3]) == [1, 3]
    assert module_0.filter_integers(['1', 1, '2', 2]) == [1, 2]

    # Empty list returns empty list
    assert module_0.filter_integers([]) == []

    # No integers at all
    assert module_0.filter_integers(['a', 'b', 'c']) == []
    assert module_0.filter_integers([1.5, 2.5, 'hello']) == []

    # Zero and negative integers are kept
    assert module_0.filter_integers([0]) == [0]
    assert module_0.filter_integers([-1, -2, 3]) == [-1, -2, 3]

    # Floats are excluded, even whole-valued ones
    assert module_0.filter_integers([3.0]) == []

    # None and nested containers are excluded
    assert module_0.filter_integers([None, [1, 2], 5]) == [5]

    # Booleans are ints in Python, so they are kept by isinstance check
    assert module_0.filter_integers([None, True, 5]) == [True, 5]

    # Order is preserved
    assert module_0.filter_integers([4, 'x', 2, None, 9]) == [4, 2, 9]

    print("All test_filter_integers tests passed!")


if __name__ == "__main__":
    test_filter_integers()

# Generated at 2026-11-02 13:13:49.983540
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: only integers should be kept
    assert module_0.filter_integers([1, 2.5, 'three', 4, None, 5]) == [1, 4, 5]

    # All integers
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers
    assert module_0.filter_integers(['a', 'b', 3.14, None, [1]]) == []

    # Empty list
    assert module_0.filter_integers([]) == []

    # Negative integers and zero
    assert module_0.filter_integers([-1, -2.5, 0, 3]) == [-1, 0, 3]

    # Strings that look like integers are not included
    assert module_0.filter_integers(['1', '2', 3]) == [3]

    # Floats with integer values are not included
    assert module_0.filter_integers([1.0, 2.0, 3]) == [3]

    # Booleans are instances of int, so they are included
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

    # Order is preserved
    assert module_0.filter_integers([3, 'x', 1, 2.5, 2]) == [3, 1, 2]

# Generated at 2026-11-02 13:15:27.854647
# Unit test for function filter_integers
def test_filter_integers():
# nonce:acb6d36e
    # Test with a mixed list of types
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]
    assert module_0.filter_integers([1, 'a', 2.5, 3]) == [1, 3]
    assert module_0.filter_integers(['a', 'b', 'c']) == []
    assert module_0.filter_integers([1.5, 2.5, 3.5]) == []
    assert module_0.filter_integers([]) == []
    assert module_0.filter_integers([None, True, False, 1, 'x', [1], {2}]) == [1]
    assert module_0.filter_integers([-1, -2, 0, 1]) == [-1, -2, 0, 1]
    assert module_0.filter_integers(['1', '2', 3]) == [3]

    # Nested structures should not be traversed
    assert module_0.filter_integers([[1, 2], [3, 4]]) == []

    # Large integers
    assert module_0.filter_integers([10**18, 'big']) == [10**18]

    print("All test cases passed!")

# Generated at 2026-11-02 13:18:53.598374
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: keep only integers
    assert module_0.filter_integers([1, 2.5, 'three', 4]) == [1, 4]
    assert module_0.filter_integers(['a', 1, 'b', 2, 3.14, 3]) == [1, 2, 3]

    # Empty list
    assert module_0.filter_integers([]) == []

    # All integers
    assert module_0.filter_integers([10, 20, 30]) == [10, 20, 30]

    # No integers
    assert module_0.filter_integers(['a', 3.14, None, [1], {'k': 1}, (2,)]) == []

    # Negative numbers and zero
    assert module_0.filter_integers([-1, 0, 1.5, 2]) == [-1, 0, 2]

    # Order preserved
    assert module_0.filter_integers([5, 'x', 3, 1.0, 8]) == [5, 3, 8]

    # Note: bool is a subclass of int in Python, so booleans pass the filter
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

    # Large integers
    assert module_0.filter_integers([10**18, 0.1, -10**18]) == [10**18, -10**18]


if __name__ == "__main__":
    test_filter_integers()
    print("All tests passed!")