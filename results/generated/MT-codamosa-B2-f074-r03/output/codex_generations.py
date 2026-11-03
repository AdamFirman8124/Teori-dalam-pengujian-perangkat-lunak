

# Generated at 2026-11-02 20:15:53.616802
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters than lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']

    # lst2 has fewer total characters than lst1
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'hi', 'admin', 'project']

    # Equal total lengths should return lst1
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # lst1 shorter
    assert module_0.total_match(['a', 'bb', 'ccc'], ['zz']) == ['zz']

    # lst2 shorter
    assert module_0.total_match(['a', 'bb', 'ccc'], ['dddd']) == ['a', 'bb', 'ccc']

    # Equal lengths, returns lst1
    assert module_0.total_match(['ab'], ['cd']) == ['ab']

    # lst1 empty
    assert module_0.total_match([], ['a', 'b']) == []

    # lst2 empty
    assert module_0.total_match(['a', 'b'], []) == []

    # Both empty
    assert module_0.total_match([], []) == []

    # Single-character strings
    assert module_0.total_match(['x'], ['y', 'z']) == ['x']

    # Long strings vs many short strings with equal totals
    assert module_0.total_match(['abcde'], ['a', 'b', 'c', 'd', 'e']) == ['abcde']

    print("All tests passed!")


test_total_match()

# Generated at 2026-11-02 20:17:59.628787
# Unit test for function total_match
def test_total_match():
    # lst1 has smaller total length
    assert module_0.total_match(["hi", "admin"], ["hI", "Hi"]) == ["hi", "admin"]

    # lst2 has smaller total length
    assert module_0.total_match(["hi", "admin"], ["hi", "hi", "admin", "project"]) == ["hi", "admin"]

    # equal total lengths -> returns lst1
    assert module_0.total_match(["hi", "admin"], ["hi", "adm"]) == ["hi", "admin"]

    # both lists empty
    assert module_0.total_match([], []) == []

    # lst1 empty (shorter)
    assert module_0.total_match([], ["a", "b"]) == []

    # lst2 empty (shorter)
    assert module_0.total_match(["abc"], []) == []

    # single elements
    assert module_0.total_match(["a"], ["bb"]) == ["a"]
    assert module_0.total_match(["aaa"], ["b"]) == ["b"]

    # equal lengths with different contents -> returns lst1
    assert module_0.total_match(["ab"], ["cd"]) == ["ab"]

    # case sensitivity does not affect length comparison
    assert module_0.total_match(["ABC"], ["abc"]) == ["ABC"]

    # longer lists with mixed lengths
    assert module_0.total_match(["one", "two", "three"], ["four", "five"]) == ["four", "five"]

    print("All tests passed!")


if __name__ == "__main__":
    test_total_match()

# Generated at 2026-11-02 20:20:08.633002
# Unit test for function total_match
def test_total_match():
    # nonce:8733c643
    # lst2 has fewer total characters -> lst2 returned
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # lst2 has fewer total characters (7 vs 6) -> lst2 returned
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # lst1 has fewer total characters (1 vs 21) -> lst1 returned
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5', '6']) == ['4']

    # lst1 has fewer total characters (7 vs 9) -> lst1 returned
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi', 'admin']) == ['hi', 'admin']

    # lst1 has fewer total characters (7 vs 11) -> lst1 returned
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi', 'admin', 'hi']) == ['hi', 'admin']

    # both lists empty -> lst1 returned (l1 <= l2)
    assert module_0.total_match([], []) == []

    # lst1 empty, lst2 non-empty -> lst1 returned
    assert module_0.total_match([], ['a', 'b']) == []

    # lst2 empty, lst1 non-empty -> lst2 returned
    assert module_0.total_match(['a'], []) == []

    # equal total lengths (tie) -> lst1 returned
    assert module_0.total_match(['ab'], ['cd']) == ['ab']
    assert module_0.total_match(['abc'], ['de', 'f']) == ['abc']

    # single-element lists
    assert module_0.total_match(['hello'], ['hi']) == ['hi']
    assert module_0.total_match(['hi'], ['hello']) == ['hi']

# Generated at 2026-11-02 20:22:48.652479
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters than lst2
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    
    # lst2 has fewer total characters than lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    
    # lst1 shorter with empty strings in lst2
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    
    # lst2 shorter with empty strings in lst1
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5', '6', '7']) == ['4']
    
    # Equal total lengths -> lst1 is returned
    assert module_0.total_match(['abc'], ['de']) == ['abc']
    
    # Both lists empty
    assert module_0.total_match([], []) == []
    
    # lst1 empty, lst2 non-empty
    assert module_0.total_match([], ['a', 'b']) == []
    
    # lst2 empty, lst1 non-empty
    assert module_0.total_match(['a', 'b'], []) == ['a', 'b']
    
    # Single element lists
    assert module_0.total_match(['hello'], ['hi']) == ['hi']
    
    # Empty strings compared against non-empty
    assert module_0.total_match(['', ''], ['a']) == ['', '']
    
    # Equal lengths with multiple elements
    assert module_0.total_match(['a', 'b', 'c'], ['abc']) == ['a', 'b', 'c']
    
    # Unicode/multi-char strings
    assert module_0.total_match(['héllo'], ['wörld']) == ['héllo']

# Generated at 2026-11-02 20:24:16.087481
# Unit test for function total_match
def test_total_match():import unittest


class TestTotalMatch(unittest.TestCase):

    def test_lst1_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'Hi']), ['hi', 'admin'])

    def test_lst2_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_lst2_shorter_again(self):
        self.assertEqual(module_0.total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_equal_lengths_returns_lst1(self):
        self.assertEqual(module_0.total_match(['hi', 'hi'], ['hi', 'hi']), ['hi', 'hi'])

    def test_empty_lst1(self):
        self.assertEqual(module_0.total_match([], ['a', 'b']), [])

    def test_empty_lst2(self):
        self.assertEqual(module_0.total_match(['a', 'b'], []), [])

    def test_both_empty(self):
        self.assertEqual(module_0.total_match([], []), [])

    def test_single_elements(self):
        self.assertEqual(module_0.total_match(['abc'], ['ab']), ['ab'])

    def test_lst1_shorter_single(self):
        self.assertEqual(module_0.total_match(['ab'], ['abc']), ['ab'])

    def test_longer_lists(self):
        self.assertEqual(
            module_0.total_match(['one', 'two', 'three'], ['four', 'five']),
            ['four', 'five']
        )

    def test_return_identity_when_equal(self):
        lst1 = ['a', 'b']
        lst2 = ['ab']
        result = module_0.total_match(lst1, lst2)
        self.assertEqual(result, lst1)
        self.assertIs(result, lst1)


if __name__ == '__main__':
    unittest.main()