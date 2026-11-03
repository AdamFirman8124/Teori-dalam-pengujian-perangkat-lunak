

# Generated at 2026-11-02 15:44:46.460371
# Unit test for function total_match
def test_total_match():import unittest


class TestTotalMatch(unittest.TestCase):

    def test_lst1_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_lst2_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_equal_lengths(self):
        self.assertEqual(module_0.total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_both_empty(self):
        self.assertEqual(module_0.total_match([], []), [])

    def test_lst1_empty(self):
        self.assertEqual(module_0.total_match([], ['a', 'b']), [])

    def test_lst2_empty(self):
        self.assertEqual(module_0.total_match(['a', 'b'], []), [])

    def test_single_elements(self):
        self.assertEqual(module_0.total_match(['abc'], ['de']), ['de'])

    def test_equal_lengths_returns_lst1(self):
        self.assertEqual(module_0.total_match(['ab'], ['cd']), ['ab'])


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 15:47:17.338905
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters, should return lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    
    # lst2 has fewer total characters, should return lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    
    # Equal total lengths, should return lst1
    assert module_0.total_match(['hi'], ['hi']) == ['hi']
    
    # Single elements comparison
    assert module_0.total_match(['abc'], ['ab']) == ['ab']
    assert module_0.total_match(['a'], ['ab']) == ['a']
    
    # Empty list has 0 total length, so it wins (or ties)
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []
    assert module_0.total_match([], []) == []
    
    # Equal totals with multiple elements, returns lst1
    assert module_0.total_match(['ab', 'cd'], ['a', 'bcd']) == ['ab', 'cd']
    
    # Lists with identical content
    assert module_0.total_match(['hello'], ['hello']) == ['hello']
    
    # lst1 longer, lst2 shorter wins
    assert module_0.total_match(['aaaa', 'bb'], ['c']) == ['c']

# Generated at 2026-11-02 15:48:32.335890
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    
    # lst2 has fewer total characters
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    
    # equal total lengths -> returns lst1
    assert module_0.total_match(['hi'], ['hi']) == ['hi']
    
    # lst1 empty
    assert module_0.total_match([], ['hi', 'there']) == []
    
    # lst2 empty
    assert module_0.total_match(['a', 'b'], []) == []
    
    # both empty -> returns lst1
    assert module_0.total_match([], []) == []
    
    # single-element lists
    assert module_0.total_match(['abc'], ['ab']) == ['ab']
    assert module_0.total_match(['a'], ['abc']) == ['a']
    
    # multi-element comparison
    assert module_0.total_match(['four'], ['one', 'two']) == ['four']
    assert module_0.total_match(['one', 'two'], ['four']) == ['four']
    
    # identical content
    assert module_0.total_match(['same', 'size'], ['same', 'size']) == ['same', 'size']

# Generated at 2026-11-02 15:49:47.979446
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    # lst2 has fewer total characters
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi', 'hI']) == ['hI', 'Hi', 'hI']
    # equal total lengths -> lst1 returned
    assert module_0.total_match(['hi', 'hi'], ['ab', 'cd']) == ['hi', 'hi']
    # single elements vs multiple
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    # both lists empty
    assert module_0.total_match([], []) == []
    # lst1 empty (shorter)
    assert module_0.total_match([], ['a', 'b']) == []
    # lst2 empty (shorter or equal)
    assert module_0.total_match(['a'], []) == []
    # empty string elements count as zero length
    assert module_0.total_match(['', ''], ['x']) == ['', '']
    # identical lists
    assert module_0.total_match(['abc'], ['abc']) == ['abc']
# nonce:c5ebf19b

# Generated at 2026-11-02 15:51:55.242323
# Unit test for function total_match
def test_total_match():import unittest


class TestTotalMatch(unittest.TestCase):

    def test_lst1_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'Hi']), ['hi', 'admin'])

    def test_lst2_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_equal_lengths_returns_lst1(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'admin']), ['hi', 'admin'])

    def test_lst1_empty(self):
        self.assertEqual(module_0.total_match([], ['a', 'b']), [])

    def test_lst2_empty(self):
        self.assertEqual(module_0.total_match(['a', 'b'], []), [])

    def test_both_empty(self):
        self.assertEqual(module_0.total_match([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(module_0.total_match(['abc'], ['de']), ['de'])

    def test_single_element_vs_multiple(self):
        self.assertEqual(module_0.total_match(['hello'], ['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_identical_lists(self):
        self.assertEqual(module_0.total_match(['x', 'y'], ['x', 'y']), ['x', 'y'])

    def test_empty_string_elements(self):
        self.assertEqual(module_0.total_match(['', ''], ['']), ['', ''])

    def test_longer_lst1(self):
        self.assertEqual(module_0.total_match(['aaaa'], ['b']), ['b'])

    def test_result_is_original_list(self):
        lst1 = ['ab']
        lst2 = ['cd', 'e']
        result = module_0.total_match(lst1, lst2)
        self.assertIs(result, lst2)


if __name__ == '__main__':
    unittest.main()