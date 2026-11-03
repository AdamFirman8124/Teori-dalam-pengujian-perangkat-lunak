

# Generated at 2026-11-01 23:08:57.479375
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total chars -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']

    # lst2 has fewer total chars -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # equal total chars -> return lst1
    assert module_0.total_match(['abc'], ['def']) == ['abc']
    assert module_0.total_match(['a', 'b'], ['c', 'd']) == ['a', 'b']

    # single vs multiple elements
    assert module_0.total_match(['hello'], ['a', 'b']) == ['a', 'b']
    assert module_0.total_match(['a', 'b'], ['hello']) == ['a', 'b']

    # empty list edge cases
    assert module_0.total_match([], []) == []
    assert module_0.total_match([], ['x']) == []
    assert module_0.total_match(['x'], []) == []

    # one list empty of strings but non-empty structure
    assert module_0.total_match([''], ['a']) == ['']
    assert module_0.total_match(['a'], ['']) == ['']

    # longer strings vs more strings
    assert module_0.total_match(['aaaa'], ['b', 'b', 'b']) == ['b', 'b', 'b']

    print("All tests passed!")


if __name__ == "__main__":
    test_total_match()

# Generated at 2026-11-01 23:09:19.495919
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']

    # lst2 has fewer total characters -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # single-element lists
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # tie in total length -> return lst1
    assert module_0.total_match(['ab'], ['a', 'b']) == ['ab']
    lst1 = ['xy']
    lst2 = ['x', 'y']
    assert module_0.total_match(lst1, lst2) is lst1

    # empty list cases
    assert module_0.total_match([], []) == []
    assert module_0.total_match([], ['a', 'b']) == []
    assert module_0.total_match(['abc'], []) == []

    # longer strings vs many short strings
    assert module_0.total_match(['hello'], ['a', 'bc']) == ['a', 'bc']
    assert module_0.total_match(['a', 'bc'], ['hello']) == ['a', 'bc']

    print("All tests passed!")


if __name__ == "__main__":
    test_total_match()

# Generated at 2026-11-01 23:09:35.882174
# Unit test for function total_match
def test_total_match():
    # Tie in total length -> returns lst1 (due to <=)
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']
    assert module_0.total_match(['ab'], ['cd']) == ['ab']

    # lst1 has smaller total length -> returns lst1
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert module_0.total_match(['a'], ['bb']) == ['a']

    # lst2 has smaller total length -> returns lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # Empty list edge cases (empty list always has total length 0)
    assert module_0.total_match([], []) == []
    assert module_0.total_match([], ['this']) == []
    assert module_0.total_match(['this'], []) == []

# nonce:d3b05de4

# Generated at 2026-11-01 23:10:09.878338
# Unit test for function total_match
def test_total_match():
# nonce:78d3622f
    # Both lists empty -> returns lst1
    assert module_0.total_match([], []) == []

    # lst2 has fewer total characters -> returns lst2
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']

    # lst1 has fewer total characters -> returns lst1
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # lst1 has fewer total characters -> returns lst1
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # lst2 has fewer total characters -> returns lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # lst2 has fewer total characters -> returns lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # Equal total lengths (7 == 7) -> returns lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']

    # lst1 empty (0 chars) -> returns lst1
    assert module_0.total_match([], ['this']) == []

    # lst2 empty (0 chars) -> returns lst2
    assert module_0.total_match(['this'], []) == []

# Generated at 2026-11-01 23:10:34.975844
# Unit test for function total_match
def test_total_match():import unittest


class TestTotalMatch(unittest.TestCase):

    def test_lst1_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'Hi']), ['hi', 'admin'])

    def test_lst2_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_lst2_shorter_multiple(self):
        self.assertEqual(module_0.total_match(['4'], ['1', '2', '3', '4', '5', '6']), ['4'])

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

    def test_empty_strings(self):
        self.assertEqual(module_0.total_match(['', ''], ['']), ['', ''])

    def test_lst1_shorter_single_chars(self):
        self.assertEqual(module_0.total_match(['a', 'b'], ['abc']), ['a', 'b'])

    def test_returns_original_list_objects(self):
        lst1 = ['x']
        lst2 = ['y', 'z']
        result = module_0.total_match(lst1, lst2)
        self.assertIs(result, lst1)


if __name__ == '__main__':
    unittest.main()