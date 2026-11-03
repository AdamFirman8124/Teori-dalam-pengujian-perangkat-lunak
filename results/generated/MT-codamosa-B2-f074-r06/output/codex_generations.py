

# Generated at 2026-11-02 20:39:11.113139
# Unit test for function total_match
def test_total_match():
    # lst1 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    
    # lst2 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    
    # equal total lengths -> lst1 returned
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    
    # equal lengths, lst1 returned
    assert module_0.total_match(['ab'], ['cd']) == ['ab']
    
    # lst1 empty
    assert module_0.total_match([], ['a', 'b']) == []
    
    # lst2 empty
    assert module_0.total_match(['abc'], []) == []
    
    # both empty
    assert module_0.total_match([], []) == []
    
    # single element lists
    assert module_0.total_match(['a'], ['abc']) == ['a']
    assert module_0.total_match(['abc'], ['a']) == ['a']
    
    # lst1 shorter with same number of elements
    assert module_0.total_match(['x', 'y'], ['abc', 'def']) == ['x', 'y']
    
    # lst2 shorter with same number of elements
    assert module_0.total_match(['xxx', 'yyy'], ['a', 'b']) == ['a', 'b']
    
    # identical lists
    assert module_0.total_match(['test'], ['test']) == ['test']
    
    print("All tests passed!")

# Generated at 2026-11-02 20:40:35.884793
# Unit test for function total_match
def test_total_match():
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == '__main__':
    test_total_match()

# Generated at 2026-11-02 20:41:47.516519
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters than lst2 -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']

    # lst2 has fewer total characters than lst1 -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'hi', 'admin', 'project']

    # equal total lengths -> return lst1
    assert module_0.total_match(['hi'], ['hi']) == ['hi']

    # empty list has fewer characters -> return empty list (lst1)
    assert module_0.total_match([], ['a', 'b']) == []

    # empty list vs empty list -> return lst1
    assert module_0.total_match([], []) == []

    # lst1 empty, lst2 non-empty equal? lst2 shorter case with single chars
    assert module_0.total_match(['abc'], ['x']) == ['x']

    # multiple strings, lst2 shorter
    assert module_0.total_match(['four', 'five'], ['one']) == ['one']

    # lst1 shorter with mixed lengths
    assert module_0.total_match(['a', 'bb'], ['ccc', 'dddd']) == ['a', 'bb']

    # both non-empty, lst1 strictly shorter
    assert module_0.total_match(['x'], ['yy']) == ['x']

    # lst2 strictly shorter
    assert module_0.total_match(['xyz'], ['a']) == ['a']

    # equal totals with different distributions -> lst1
    assert module_0.total_match(['ab', 'cd'], ['abcd']) == ['ab', 'cd']

# Generated at 2026-11-02 20:43:46.857392
# Unit test for function total_match
def test_total_match():
    # lst2 has fewer total characters -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    # lst1 has fewer total characters -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    # equal totals -> return lst1
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert module_0.total_match(['a', 'bb'], ['ccc', '']) == ['a', 'bb']
    # empty list cases
    assert module_0.total_match(['hi', 'admin'], []) == []
    assert module_0.total_match([], ['x']) == []
    assert module_0.total_match([], []) == []
    # empty strings contribute zero length
    assert module_0.total_match(['', ''], ['a']) == ['', '']
    # single-element lists
    assert module_0.total_match(['abc'], ['ab']) == ['ab']
    assert module_0.total_match(['ab'], ['abc']) == ['ab']
    # returns the actual list objects (identity check)
    a = ['a', 'b']
    b = ['abc']
    assert module_0.total_match(a, b) is a
    c = ['abc']
    d = ['a']
    assert module_0.total_match(c, d) is d

# Generated at 2026-11-02 20:46:31.491700
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    
    # lst2 has fewer total characters
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    
    # lst2 has fewer total characters (single strings)
    assert module_0.total_match(['hi'], ['hi', 'hello']) == ['hi']
    
    # equal total lengths, returns lst1
    assert module_0.total_match(['hi'], ['hi']) == ['hi']
    
    # both lists empty
    assert module_0.total_match([], []) == []
    
    # lst1 empty, lst2 non-empty
    assert module_0.total_match([], ['a', 'b']) == []
    
    # lst2 empty, lst1 non-empty
    assert module_0.total_match(['a', 'b'], []) == []
    
    # single character strings
    assert module_0.total_match(['a'], ['b', 'c']) == ['a']
    
    # longer strings in lst2
    assert module_0.total_match(['abc'], ['x', 'y']) == ['x', 'y']
    
    # case sensitivity doesn't matter for length
    assert module_0.total_match(['AAA'], ['bb']) == ['bb']
    
    print("All tests passed!")

test_total_match()