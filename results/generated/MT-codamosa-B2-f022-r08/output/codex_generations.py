

# Generated at 2026-11-02 07:49:06.957193
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: only ints kept
    assert module_0.filter_integers(['a', 3.14, 5]) == [5]
    
    # All integers
    assert module_0.filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Empty list
    assert module_0.filter_integers([]) == []
    
    # No integers
    assert module_0.filter_integers(['a', 'b', 'c']) == []
    assert module_0.filter_integers([1.5, 2.7, None]) == []
    
    # Negative and zero integers
    assert module_0.filter_integers([7, 0, -3, 2.5, 'x', None]) == [7, 0, -3]
    
    # Nested structures and other objects are excluded
    assert module_0.filter_integers([1, 'two', 3.0, 4, [5], {'six': 6}]) == [1, 4]
    
    # Note: bool is a subclass of int, so True/False pass through
    assert module_0.filter_integers([True, False, 1, 'a']) == [True, False, 1]
    
    # Floats with integer values are still excluded
    assert module_0.filter_integers([5.0, 5]) == [5]

# Generated at 2026-11-02 07:49:34.605874
# Unit test for function filter_integers
def test_filter_integers():
    # Test with mixed types
    assert module_0.filter_integers([1, 2.5, 'a', 3, None]) == [1, 3]

    # Test with only integers
    assert module_0.filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test with no integers
    assert module_0.filter_integers(['a', 'b', 1.5, 2.5, None, [1], (2,)]) == []

    # Test with empty list
    assert module_0.filter_integers([]) == []

    # Test with negative integers
    assert module_0.filter_integers([-1, -2, 'x', 0, 3.14]) == [-1, -2, 0]

    # Test with floats (should be excluded, even whole-valued floats)
    assert module_0.filter_integers([1.0, 2.0, 3]) == [3]

    # Test with booleans (bool is a subclass of int, so included)
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

    # Test with strings that look like integers
    assert module_0.filter_integers(['1', '2', 3]) == [3]

    # Test with nested containers
    assert module_0.filter_integers([[1, 2], {'a': 3}, 4]) == [4]

    # Test with large integers
    assert module_0.filter_integers([10**18, 'big', 10**19]) == [10**18, 10**19]

    # Test result type
    result = module_0.filter_integers([1, 'a', 2.5])
    assert all(isinstance(x, int) for x in result)
    assert isinstance(result, list)


if __name__ == "__main__":
    test_filter_integers()
    print("All tests passed!")

# Generated at 2026-11-02 07:49:42.075761
# Unit test for function filter_integers
def test_filter_integers():
    # Test with all integers
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # Test with mixed types
    assert module_0.filter_integers([1, 'a', 2.5, 3]) == [1, 3]

    # Test with no integers
    assert module_0.filter_integers(['a', 'b', 3.14]) == []

    # Test with empty list
    assert module_0.filter_integers([]) == []

    # Test with nested structures (should not recurse)
    assert module_0.filter_integers([[1], 2, (3,)]) == [2]

    # Test with floats that are whole numbers (should be excluded)
    assert module_0.filter_integers([1.0, 2.0, 3]) == [3]

    # Test with booleans (bool is subclass of int, so included)
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

    # Test with None and other types
    assert module_0.filter_integers([None, 5, {}, 'x']) == [5]

    # Test with negative integers and zero
    assert module_0.filter_integers([-1, 0, 1, 'z']) == [-1, 0, 1]

    # Test order preservation
    assert module_0.filter_integers(['a', 10, 'b', 20, 'c']) == [10, 20]

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_integers()

# Generated at 2026-11-02 07:50:15.666034
# Unit test for function filter_integers
def test_filter_integers():
    assert module_0.filter_integers(['a', 3.14, 5]) == [5]
    assert module_0.filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert module_0.filter_integers([]) == []
    assert module_0.filter_integers([4.5, 'hello', None, 42]) == [42]
    assert module_0.filter_integers(['1', 2.0, 3, True]) == [3, True]


if __name__ == "__main__":
    test_filter_integers()
    print("All tests passed!")

# Generated at 2026-11-02 07:50:50.099579
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: only integers kept
    assert module_0.filter_integers([1, 'a', 2.5, 3, None]) == [1, 3]

    # All integers
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # No integers
    assert module_0.filter_integers(['a', 'b', 3.5, None]) == []

    # Empty list
    assert module_0.filter_integers([]) == []

    # Negative integers and zero
    assert module_0.filter_integers([-1, 0, 'x', 5]) == [-1, 0, 5]

    # Booleans are instances of int in Python, so they are kept
    assert module_0.filter_integers([True, False, 1]) == [True, False, 1]

    # Complex types excluded
    assert module_0.filter_integers([[1], {'a': 2}, (3,), 4]) == [4]

    # Order preserved
    assert module_0.filter_integers([9, 'z', 8, 2.2, 7]) == [9, 8, 7]

    # Large integers
    assert module_0.filter_integers([10**18, 'big', -10**18]) == [10**18, -10**18]