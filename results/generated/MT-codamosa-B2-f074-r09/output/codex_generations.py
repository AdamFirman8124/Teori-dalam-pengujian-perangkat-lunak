

# Generated at 2026-11-02 23:32:22.559402
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters than lst2 -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # lst2 has fewer total characters than lst1 -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # equal total lengths -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'admin']

    # both lists empty -> return lst1
    assert module_0.total_match([], []) == []

    # lst1 empty -> return lst1
    assert module_0.total_match([], ['a', 'b', 'c']) == []

    # lst2 empty -> return lst2
    assert module_0.total_match(['a', 'b'], []) == []

    # single element lists
    assert module_0.total_match(['hello'], ['hi']) == ['hi']
    assert module_0.total_match(['hi'], ['hello']) == ['hi']

    # empty strings count as zero length
    assert module_0.total_match(['', ''], ['a']) == ['', '']

    # identical lists -> return lst1
    assert module_0.total_match(['abc'], ['abc']) == ['abc']

    print("All tests passed!")


test_total_match()

# Generated at 2026-11-02 23:33:11.925414
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']

    # lst2 has fewer total characters -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # equal total characters -> return lst1
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5', '6']) == ['4']

    # one list empty -> return the empty list
    assert module_0.total_match([], ['a', 'b']) == []
    assert module_0.total_match(['a', 'b'], []) == []

    # both empty -> return lst1 (empty)
    assert module_0.total_match([], []) == []

    # single element lists
    assert module_0.total_match(['abc'], ['de']) == ['de']
    assert module_0.total_match(['ab'], ['cde']) == ['ab']

    # identical lists (equal length) -> return lst1
    assert module_0.total_match(['x', 'y'], ['x', 'y']) == ['x', 'y']

    # strings containing spaces count toward length
    assert module_0.total_match(['a b'], ['abc']) == ['abc']

# Generated at 2026-11-02 23:34:24.545557
# Unit test for function total_match
def test_total_match():
# nonce:0a8da54a
    # lst1 has smaller total length -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    
    # lst2 has smaller total length -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    
    # equal total lengths -> return lst1 (l1 <= l2)
    assert module_0.total_match(['hi', 'admin'], ['hI', 'admin']) == ['hi', 'admin']
    
    # lst1 empty -> return lst1
    assert module_0.total_match([], ['a', 'b']) == []
    
    # lst2 empty -> return lst2
    assert module_0.total_match(['a', 'b'], []) == []
    
    # both empty -> return lst1
    assert module_0.total_match([], []) == []
    
    # single-element lists
    assert module_0.total_match(['abc'], ['ab']) == ['ab']
    assert module_0.total_match(['ab'], ['abc']) == ['ab']
    
    # equal single-element lists -> return lst1
    assert module_0.total_match(['abc'], ['abc']) == ['abc']
    
    # multiple elements with equal totals -> return lst1
    assert module_0.total_match(['a', 'bb'], ['aaa']) == ['a', 'bb']
    
    # lst2 much shorter
    assert module_0.total_match(['hello', 'world'], ['x']) == ['x']
    
    # empty strings count as zero length
    assert module_0.total_match(['', ''], ['']) == ['', '']
    
    print("All tests passed!")

if __name__ == "__main__":
    test_total_match()

# Generated at 2026-11-02 23:35:56.354520
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(['hi'], ['hello', 'world']) == ['hi']

    # lst2 has fewer total characters
    assert module_0.total_match(['hello', 'world'], ['hi']) == ['hi']

    # equal total lengths -> returns lst1
    assert module_0.total_match(['ab'], ['cd']) == ['ab']

    # lst1 empty
    assert module_0.total_match([], ['a', 'b']) == []

    # lst2 empty
    assert module_0.total_match(['a', 'b'], []) == []

    # both empty -> returns lst1
    assert module_0.total_match([], []) == []

    # multiple strings in lst1 with smaller total
    assert module_0.total_match(['a', 'b', 'c'], ['xy', 'zw']) == ['a', 'b', 'c']

    # multiple strings in lst2 with smaller total
    assert module_0.total_match(['xy', 'zw'], ['a', 'b', 'c']) == ['a', 'b', 'c']

    # single-character strings
    assert module_0.total_match(['a'], ['ab']) == ['a']

    # lst1 strictly longer -> lst2 returned
    assert module_0.total_match(['aaa'], ['b']) == ['b']

    print("All tests passed!")


if __name__ == "__main__":
    test_total_match()

# Generated at 2026-11-02 23:38:51.282465
# Unit test for function total_match
def test_total_match():import unittest


class TestTotalMatch(unittest.TestCase):

    def test_lst1_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'Hi']), ['hi', 'admin'])

    def test_lst2_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_equal_length_returns_lst1(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'hi']), ['hi', 'admin'])

    def test_single_element_lists(self):
        self.assertEqual(module_0.total_match(['abc'], ['ab']), ['ab'])
        self.assertEqual(module_0.total_match(['a'], ['abc']), ['a'])

    def test_both_empty(self):
        self.assertEqual(module_0.total_match([], []), [])

    def test_lst1_empty(self):
        self.assertEqual(module_0.total_match([], ['a', 'b']), [])

    def test_lst2_empty(self):
        self.assertEqual(module_0.total_match(['a', 'b'], []), [])

    def test_same_content(self):
        self.assertEqual(module_0.total_match(['aa'], ['aa']), ['aa'])

    def test_longer_list_fewer_chars(self):
        self.assertEqual(module_0.total_match(['a', 'b', 'c'], ['abcd']), ['a', 'b', 'c'])

    def test_returns_list_objects(self):
        result = module_0.total_match(['x'], ['yy'])
        self.assertIsInstance(result, list)
        self.assertEqual(result, ['x'])


if __name__ == '__main__':
    unittest.main()