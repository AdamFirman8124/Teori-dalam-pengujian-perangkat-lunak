

# Generated at 2026-11-02 18:49:03.833937
# Unit test for function total_match
def test_total_match():import unittest


class TestTotalMatch(unittest.TestCase):

    def test_lst1_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hI', 'Hi']), ['hi', 'admin'])

    def test_lst2_shorter(self):
        self.assertEqual(module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_lst2_shorter_again(self):
        self.assertEqual(module_0.total_match(['4'], ['1', '2', '3', '4', '5', '6']), ['4'])

    def test_equal_lengths_returns_lst1(self):
        self.assertEqual(module_0.total_match(['hi', 'hi'], ['hi', 'hi']), ['hi', 'hi'])

    def test_both_empty(self):
        self.assertEqual(module_0.total_match([], []), [])

    def test_lst1_empty(self):
        self.assertEqual(module_0.total_match([], ['a', 'b']), [])

    def test_lst2_empty(self):
        self.assertEqual(module_0.total_match(['a', 'b'], []), [])

    def test_single_chars(self):
        self.assertEqual(module_0.total_match(['a'], ['b', 'c']), ['a'])

    def test_lst1_longer(self):
        self.assertEqual(module_0.total_match(['abc', 'def', 'ghi'], ['x']), ['x'])

    def test_equal_length_different_content(self):
        self.assertEqual(module_0.total_match(['ab'], ['cd']), ['ab'])


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 18:50:09.482802
# Unit test for function total_match
def test_total_match():
    # lst1 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    assert module_0.total_match(['a'], ['ab', 'cd']) == ['a']

    # lst2 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert module_0.total_match(['ab', 'cd'], ['a']) == ['a']

    # equal total lengths -> returns lst1
    assert module_0.total_match(['ab'], ['cd']) == ['ab']
    assert module_0.total_match(['a', 'b'], ['ab']) == ['a', 'b']

    # empty lists
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []
    assert module_0.total_match([], []) == []

    # single-element lists
    assert module_0.total_match(['hello'], ['hi']) == ['hi']
    assert module_0.total_match(['hi'], ['hello']) == ['hi']

    # identical lists
    assert module_0.total_match(['abc', 'de'], ['abc', 'de']) == ['abc', 'de']

    # one empty string
    assert module_0.total_match([''], ['a']) == ['']
    assert module_0.total_match(['a'], ['']) == ['']

    print("All tests passed!")


test_total_match()

# Generated at 2026-11-02 18:51:30.450335
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total chars than lst2 -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']

    # lst2 has fewer total chars than lst1 -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # equal total chars -> return lst1
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # lst1 shorter with single elements
    assert module_0.total_match(['a'], ['ab']) == ['a']

    # lst2 shorter with single elements
    assert module_0.total_match(['abc'], ['a']) == ['a']

    # empty lst1 vs non-empty lst2 -> return lst1
    assert module_0.total_match([], ['a', 'b']) == []

    # non-empty lst1 vs empty lst2 -> return lst2
    assert module_0.total_match(['a', 'b'], []) == []

    # both empty -> return lst1
    assert module_0.total_match([], []) == []

    # lists with empty strings
    assert module_0.total_match(['', ''], ['a']) == ['', '']
    assert module_0.total_match(['a'], ['', '']) == ['', '']

    # equal totals with different distributions -> return lst1
    assert module_0.total_match(['ab', 'cd'], ['abcd']) == ['ab', 'cd']

    # longer strings in lst2
    assert module_0.total_match(['one', 'two'], ['three']) == ['one', 'two']

    print("All tests passed!")


if __name__ == "__main__":
    test_total_match()

# Generated at 2026-11-02 18:53:24.250247
# Unit test for function total_match
def test_total_match():import unittest


class TestTotalMatch(unittest.TestCase):

    def test_lst1_shorter(self):
        self.assertEqual(module_0.total_match(['hi'], ['hello', 'world']), ['hi'])

    def test_lst2_shorter(self):
        self.assertEqual(module_0.total_match(['hello', 'world'], ['hi']), ['hi'])

    def test_equal_lengths_returns_lst1(self):
        self.assertEqual(module_0.total_match(['ab'], ['cd']), ['ab'])

    def test_both_empty(self):
        self.assertEqual(module_0.total_match([], []), [])

    def test_lst1_empty(self):
        self.assertEqual(module_0.total_match([], ['a', 'b']), [])

    def test_lst2_empty(self):
        self.assertEqual(module_0.total_match(['a', 'b'], []), [])

    def test_single_elements(self):
        self.assertEqual(module_0.total_match(['abc'], ['xy']), ['xy'])

    def test_identical_lists(self):
        self.assertEqual(module_0.total_match(['a', 'b'], ['a', 'b']), ['a', 'b'])

    def test_multiple_strings_lst1(self):
        self.assertEqual(module_0.total_match(['a', 'bb', 'c'], ['dddd']), ['a', 'bb', 'c'])

    def test_multiple_strings_lst2(self):
        self.assertEqual(module_0.total_match(['dddd'], ['a', 'bb', 'c']), ['a', 'bb', 'c'])

    def test_empty_strings(self):
        self.assertEqual(module_0.total_match(['', ''], ['']), ['', ''])

    def test_long_vs_short(self):
        self.assertEqual(
            module_0.total_match(['four', ''], ['one', 'two']),
            ['one', 'two']
        )


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 18:55:40.337423
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total chars -> returns lst1
    assert module_0.total_match(['hi'], ['hello', 'world']) == ['hi']

    # lst2 has fewer total chars -> returns lst2
    assert module_0.total_match(['hello', 'world'], ['hi']) == ['hi']

    # equal total lengths -> returns lst1 (l1 <= l2)
    assert module_0.total_match(['ab'], ['cd']) == ['ab']

    # both lists empty -> equal (0 <= 0), returns lst1
    assert module_0.total_match([], []) == []

    # lst1 empty -> returns lst1
    assert module_0.total_match([], ['a', 'b']) == []

    # lst2 empty -> returns lst2
    assert module_0.total_match(['a'], []) == []

    # empty strings count as zero length
    assert module_0.total_match(['', ''], ['x']) == ['', '']

    # single-character lists
    assert module_0.total_match(['a'], ['b']) == ['a']

    # many short strings vs one long string
    assert module_0.total_match(['a', 'b', 'c'], ['abc']) == ['abc']

    # long list vs short list
    assert module_0.total_match(['four'], ['one', 'two']) == ['four']

    # identical content -> equal, returns lst1
    assert module_0.total_match(['same'], ['same']) == ['same']

    # difference of one character
    assert module_0.total_match(['abc'], ['abcd']) == ['abc']

    # multi-character check
    assert module_0.total_match(['123', '45'], ['12345']) == ['12345']

    # strings with spaces count their full length
    assert module_0.total_match(['a b'], ['ab']) == ['ab']

    # unicode strings count length correctly
    assert module_0.total_match(['héllo'], ['hi']) == ['hi']