

# Generated at 2026-11-02 23:48:12.432058
# Unit test for function filter_integers
def test_filter_integers():import unittest


class TestFilterIntegers(unittest.TestCase):

    def test_mixed_types(self):
        values = ['a', 3.14, 5]
        self.assertEqual(module_0.filter_integers(values), [5])

    def test_empty_list(self):
        self.assertEqual(module_0.filter_integers([]), [])

    def test_all_integers(self):
        self.assertEqual(module_0.filter_integers([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_no_integers(self):
        self.assertEqual(module_0.filter_integers(['a', 'b', 1.5, None]), [])

    def test_negative_integers(self):
        self.assertEqual(module_0.filter_integers([-1, 'x', -2.5, -3]), [-1, -3])

    def test_zero(self):
        self.assertEqual(module_0.filter_integers([0, 'zero', 0.0]), [0])

    def test_large_integers(self):
        self.assertEqual(module_0.filter_integers([10**18, 'big', 10**19]), [10**18, 10**19])

    def test_nested_structures_not_integers(self):
        self.assertEqual(module_0.filter_integers([[1], {'a': 1}, (1,), 7]), [7])

    def test_boolean_is_subclass_of_int(self):
        # bool is a subclass of int, so isinstance(True, int) is True
        self.assertEqual(module_0.filter_integers([True, False, 'x']), [True, False])

    def test_preserves_order(self):
        self.assertEqual(module_0.filter_integers([2, 'a', 1, 'b', 3]), [2, 1, 3])

    def test_does_not_match_float_that_equals_int(self):
        self.assertEqual(module_0.filter_integers([5.0, 5]), [5])


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 23:49:09.778436
# Unit test for function filter_integers
def test_filter_integers():
    # Mixed types: only integers are kept
    assert module_0.filter_integers([1, 2, 3, 'a', 'b', 4.5]) == [1, 2, 3]

    # Empty list returns empty list
    assert module_0.filter_integers([]) == []

    # No integers present
    assert module_0.filter_integers(['a', 'b', 3.14, None, [1], {'k': 1}]) == []

    # All integers, including negatives and zero
    assert module_0.filter_integers([-5, 0, 42]) == [-5, 0, 42]

    # Floats are excluded even when whole-valued
    assert module_0.filter_integers([1.0, 2.0, 7]) == [7]

    # Booleans are instances of int, so they are kept
    assert module_0.filter_integers([True, False, 'x']) == [True, False]

    # Order of integers is preserved
    assert module_0.filter_integers(['a', 3, 'b', 1, 2]) == [3, 1, 2]

    # Large integers are handled correctly
    assert module_0.filter_integers([10**18, 'big', 10**19]) == [10**18, 10**19]

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_integers()

# Generated at 2026-11-02 23:49:51.045510
# Unit test for function filter_integers
def test_filter_integers():
    # Test with a mixed list of types
    assert module_0.filter_integers([1, 2.5, 'a', 3, True, None]) == [1, 3, True]

    # Test with only integers
    assert module_0.filter_integers([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Test with no integers
    assert module_0.filter_integers(['a', 'b', 1.5, None]) == []

    # Test with empty list
    assert module_0.filter_integers([]) == []

    # Test with negative integers
    assert module_0.filter_integers([-1, -2, 0, 3.14, 'x']) == [-1, -2, 0]

    # Test with large integers
    assert module_0.filter_integers([10**18, 'big', 10**19]) == [10**18, 10**19]

    # Test result type
    result = module_0.filter_integers([1, 'a', 2])
    assert all(isinstance(x, int) for x in result)

    # Test that original list is not modified
    original = [1, 'a', 2.0]
    module_0.filter_integers(original)
    assert original == [1, 'a', 2.0]

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_integers()

# Generated at 2026-11-02 23:50:43.520169
# Unit test for function filter_integers
def test_filter_integers():
    # Test with mixed types
    assert module_0.filter_integers(['a', 3.14, 5]) == [5]
    assert module_0.filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]

    # Test with empty list
    assert module_0.filter_integers([]) == []

    # Test with only integers
    assert module_0.filter_integers([1, 2, 3]) == [1, 2, 3]

    # Test with no integers
    assert module_0.filter_integers(['a', 'b', 'c']) == []
    assert module_0.filter_integers([1.5, 2.7, 3.9]) == []
    assert module_0.filter_integers([None, True, '1']) == [True]

    # Test with negative integers and zero
    assert module_0.filter_integers([-1, 0, 1, 'x', 2.5]) == [-1, 0, 1]

    # Test with large integers
    assert module_0.filter_integers([10**18, 'large', 10**19]) == [10**18, 10**19]

    # Test with nested structures (should be filtered out)
    assert module_0.filter_integers([[1, 2], {'a': 1}, (1,), 42]) == [42]

    # Test preserving order
    assert module_0.filter_integers([3, 'a', 1, 'b', 2]) == [3, 1, 2]

    # Test with duplicates
    assert module_0.filter_integers([1, 1, 'x', 2, 2]) == [1, 1, 2]

    # Result should contain only ints
    result = module_0.filter_integers([1, 'two', 3.0, 4])
    assert all(isinstance(x, int) for x in result)
    assert result == [1, 4]


if __name__ == '__main__':
    test_filter_integers()
    print("All tests passed!")

# Generated at 2026-11-02 23:51:43.170183
# Unit test for function filter_integers
def test_filter_integers():
    # Empty list returns empty list
    assert module_0.filter_integers([]) == []

    # All integers are kept in order
    assert module_0.filter_integers([4, 6, 3]) == [4, 6, 3]

    # Floats are filtered out
    assert module_0.filter_integers([4, 6, 3.5]) == [4, 6]

    # Strings, None, lists, and dicts are filtered out
    assert module_0.filter_integers(["a", 23, 3.5, None, [1], 7]) == [23, 7]

    # Negative integers and zero are kept
    assert module_0.filter_integers([-1, 0, 2.5, -3.7]) == [-1, 0]

    # Large integers are kept
    assert module_0.filter_integers([10**18, 1.0]) == [10**18]

    # Booleans are instances of int in Python, so they are kept
    assert module_0.filter_integers([True, False, 5]) == [True, False, 5]

    # No integers present returns empty list
    assert module_0.filter_integers(["1", 2.0, None, {"a": 1}, (3,)]) == []


if __name__ == "__main__":
    test_filter_integers()
    print("All tests passed!")