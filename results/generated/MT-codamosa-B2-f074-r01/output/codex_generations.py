

# Generated at 2026-11-02 13:36:03.442239
# Unit test for function total_match
def test_total_match():import unittest


class TestTotalMatch(unittest.TestCase):

    def test_lst1_shorter(self):
        self.assertEqual(module_0.total_match(["hi", "admin"], ["hI", "Hi"]), ["hi", "admin"])

    def test_lst2_shorter(self):
        self.assertEqual(module_0.total_match(["hi", "admin"], ["hI", "hi", "hi"]), ["hI", "hi", "hi"])

    def test_equal_lengths_returns_lst1(self):
        self.assertEqual(module_0.total_match(["hi", "admin"], ["hi", "hi"]), ["hi", "admin"])

    def test_both_empty(self):
        self.assertEqual(module_0.total_match([], []), [])

    def test_lst1_empty(self):
        self.assertEqual(module_0.total_match([], ["a", "b"]), [])

    def test_lst2_empty(self):
        self.assertEqual(module_0.total_match(["a", "b"], []), [])

    def test_single_elements(self):
        self.assertEqual(module_0.total_match(["abc"], ["ab"]), ["ab"])

    def test_single_elements_lst1_shorter(self):
        self.assertEqual(module_0.total_match(["a"], ["abc"]), ["a"])

    def test_empty_strings(self):
        self.assertEqual(module_0.total_match(["", ""], ["a"]), ["", ""])

    def test_identical_lists(self):
        self.assertEqual(module_0.total_match(["x", "y"], ["x", "y"]), ["x", "y"])

    def test_returns_lst1_object_when_equal(self):
        lst1 = ["a"]
        result = module_0.total_match(lst1, ["a"])
        self.assertIs(result, lst1)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 13:37:04.799252
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total chars than lst2 -> return lst1
    assert module_0.total_match(['hi'], ['hello', 'world']) == ['hi']

    # lst2 has fewer total chars than lst1 -> return lst2
    assert module_0.total_match(['hello', 'world'], ['hi']) == ['hi']

    # equal total lengths -> return lst1
    assert module_0.total_match(['ab', 'cd'], ['ef', 'gh']) == ['ab', 'cd']

    # both lists empty -> return lst1 (empty)
    assert module_0.total_match([], []) == []

    # lst1 empty -> return lst1
    assert module_0.total_match([], ['a', 'b']) == []

    # lst2 empty -> return lst2
    assert module_0.total_match(['a', 'b'], []) == []

    # single-character strings
    assert module_0.total_match(['a'], ['b', 'c']) == ['a']
    assert module_0.total_match(['a', 'b'], ['c']) == ['c']

    # empty strings within lists
    assert module_0.total_match(['', ''], ['a']) == ['', '']
    assert module_0.total_match(['a'], ['', '']) == ['', '']

    # mixed lengths
    assert module_0.total_match(['abc'], ['de', 'f']) == ['abc']  # 3 vs 3, tie -> lst1
    assert module_0.total_match(['abc', 'de'], ['xyz']) == ['xyz']  # 5 vs 3

    # longer lists
    assert module_0.total_match(['one', 'two', 'three'], ['four', 'five']) == ['four', 'five']  # 12 vs 9
    assert module_0.total_match(['four', 'five'], ['one', 'two', 'three']) == ['four', 'five']  # 9 vs 12

    # lists with identical content
    assert module_0.total_match(['same', 'same'], ['same', 'same']) == ['same', 'same']

    # strings with spaces and special characters
    assert module_0.total_match(['a b'], ['!@#', '$']) == ['a b']  # 3 vs 4

    # unicode strings
    assert module_0.total_match(['héllo'], ['wörld!']) == ['héllo']  # 5 vs 6

    # returned list is the actual input list (identity check)
    lst1 = ['x']
    lst2 = ['yy', 'zz']
    assert module_0.total_match(lst1, lst2) is lst1
    assert module_0.total_match(lst2, lst1) is lst2

# Generated at 2026-11-02 13:37:49.779054
# Unit test for function total_match
def test_total_match():
    # lst1 has smaller total length
    assert module_0.total_match(["hi", "admin"], ["hI", "Hi"]) == ["hI", "Hi"]

    # lst2 has smaller total length
    assert module_0.total_match(["hi", "admin"], ["hi", "hi", "admin", "project"]) == ["hi", "admin"]
    assert module_0.total_match(["4"], ["1", "2", "3", "4", "5"]) == ["4"]

    # Equal total lengths - returns lst1
    assert module_0.total_match(["hi", "hi"], ["hi", "hi"]) == ["hi", "hi"]
    assert module_0.total_match(["abc"], ["xyz"]) == ["abc"]

    # Empty lists
    assert module_0.total_match([], ["a", "b"]) == []
    assert module_0.total_match(["a", "b"], []) == []
    assert module_0.total_match([], []) == []

    # Single element lists
    assert module_0.total_match(["hello"], ["x"]) == ["x"]
    assert module_0.total_match(["x"], ["hello"]) == ["x"]

    # Lists with empty strings
    assert module_0.total_match(["", ""], ["a"]) == ["", ""]

    # Case where one list has more elements but smaller total length
    assert module_0.total_match(["aaaa"], ["a", "a", "a"]) == ["a", "a", "a"]

    print("All tests passed!")


test_total_match()

# Generated at 2026-11-02 13:38:57.423143
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters than lst2 -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']

    # lst2 has fewer total characters than lst1 -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # lst2 has fewer total characters -> return lst2
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['1', '2', '3', '4', '5']

    # Equal total lengths -> lst1 returned (l1 <= l2)
    assert module_0.total_match(['hi', 'hi'], ['ab', 'cd']) == ['hi', 'hi']

    # Both lists empty -> return lst1
    assert module_0.total_match([], []) == []

    # lst1 empty -> lst1 has 0 chars, returned
    assert module_0.total_match([], ['abc']) == []

    # lst2 empty -> lst2 has fewer chars, returned
    assert module_0.total_match(['abc'], []) == []

    # Single-element lists
    assert module_0.total_match(['a'], ['bb']) == ['a']
    assert module_0.total_match(['aa'], ['b']) == ['b']

    # Same list on both sides -> equal lengths, return lst1
    assert module_0.total_match(['x', 'y'], ['x', 'y']) == ['x', 'y']

# Generated at 2026-11-02 13:39:52.275646
# Unit test for function total_match
def test_total_match():
    # lst1 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    
    # lst2 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5', '6']) == ['4']
    
    # equal total lengths -> returns lst1
    assert module_0.total_match(['hi', 'admin'], ['hi', 'admin']) == ['hi', 'admin']
    assert module_0.total_match(['ab'], ['cd']) == ['ab']
    
    # empty list cases
    assert module_0.total_match([], ['a', 'b']) == []
    assert module_0.total_match(['a', 'b'], []) == []
    assert module_0.total_match([], []) == []
    
    # single element lists
    assert module_0.total_match(['hello'], ['hi']) == ['hi']
    assert module_0.total_match(['hi'], ['hello']) == ['hi']
    
    # lists with empty strings
    assert module_0.total_match(['', ''], ['a']) == ['', '']
    assert module_0.total_match(['a'], ['', '']) == ['', '']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_total_match()