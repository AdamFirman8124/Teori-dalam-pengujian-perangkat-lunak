

# Generated at 2026-11-03 02:35:15.534998
# Unit test for function total_match
def test_total_match():
    # nonce:7a7886b2
    # lst2 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # lst1 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # lst1 has smaller total length (single char vs many)
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5', '6', '7']) == ['4']

    # lst2 has smaller total length
    assert module_0.total_match(['1', '2', '3'], ['1', '2']) == ['1', '2']

    # equal total lengths -> returns lst1
    assert module_0.total_match(['ab', 'c'], ['a', 'bc']) == ['ab', 'c']
    assert module_0.total_match(['hi'], ['hi']) == ['hi']

    # empty list cases
    assert module_0.total_match([], ['a', 'b']) == []
    assert module_0.total_match(['abc'], []) == []
    assert module_0.total_match([], []) == []

    # identical lists
    assert module_0.total_match(['hello', 'world'], ['hello', 'world']) == ['hello', 'world']

    # strings with spaces count toward length
    assert module_0.total_match(['a b'], ['abc']) == ['abc']

# Generated at 2026-11-03 02:36:16.319362
# Unit test for function total_match
def test_total_match():
    # lst1 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    
    # lst2 has smaller total length
    assert module_0.total_match(['hI', 'Hi'], ['hi', 'admin', 'project']) == ['hI', 'Hi']
    
    # equal total lengths -> returns lst1
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    
    # lst1 empty
    assert module_0.total_match([], ['a', 'b']) == []
    
    # lst2 empty
    assert module_0.total_match(['a', 'b'], []) == []
    
    # both empty -> returns lst1
    assert module_0.total_match([], []) == []
    
    # single element lists
    assert module_0.total_match(['abc'], ['ab']) == ['ab']
    assert module_0.total_match(['ab'], ['abc']) == ['ab']
    
    # equal lengths with different content
    assert module_0.total_match(['ab', 'cd'], ['abcd']) == ['ab', 'cd']
    
    # identical lists
    assert module_0.total_match(['x', 'y'], ['x', 'y']) == ['x', 'y']

# Generated at 2026-11-03 02:37:08.480433
# Unit test for function total_match
def test_total_match():
    # lst1 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']

    # lst2 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert module_0.total_match(['hello'], ['a', 'b']) == ['a', 'b']

    # equal total lengths -> returns lst1
    assert module_0.total_match(['hi'], ['hi']) == ['hi']
    assert module_0.total_match(['ab', 'cd'], ['abcd']) == ['ab', 'cd']
    assert module_0.total_match(['four'], ['hi', 'hi']) == ['four']
    assert module_0.total_match(['hi', 'hi'], ['four']) == ['hi', 'hi']

    # empty list cases
    assert module_0.total_match([], ['hi']) == []
    assert module_0.total_match(['hi'], []) == []
    assert module_0.total_match([], []) == []

    # single-element lists
    assert module_0.total_match(['a'], ['bb']) == ['a']
    assert module_0.total_match(['bb'], ['a']) == ['a']

    # returns lst1 object itself on tie
    lst = ['x', 'yy']
    assert module_0.total_match(lst, ['zzz']) is lst

    print("All tests passed!")


if __name__ == "__main__":
    test_total_match()

# Generated at 2026-11-03 02:37:48.929294
# Unit test for function total_match
def test_total_match():
    # lst1 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    
    # lst1 has smaller total length (single chars)
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    
    # lst2 has smaller total length
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']
    
    # lst1 is empty (total length 0)
    assert module_0.total_match([], ['this']) == []
    
    # both lists empty
    assert module_0.total_match([], []) == []
    
    # lst2 is empty
    assert module_0.total_match(['a'], []) == []
    
    # equal total lengths -> returns lst1
    assert module_0.total_match(['ab'], ['cd']) == ['ab']
    assert module_0.total_match(['a', 'b'], ['ab']) == ['a', 'b']
    
    # single element lists
    assert module_0.total_match(['hello'], ['hi']) == ['hi']
    assert module_0.total_match(['hi'], ['hello']) == ['hi']
    
    # empty strings in lists
    assert module_0.total_match(['', ''], ['a']) == ['', '']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_total_match()

# Generated at 2026-11-03 02:38:41.566298
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    
    # lst2 has fewer total characters
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    
    # equal total lengths -> lst1 is returned
    assert module_0.total_match(['hi'], ['hi']) == ['hi']
    
    # lst1 empty
    assert module_0.total_match([], ['a', 'b']) == []
    
    # lst2 empty
    assert module_0.total_match(['a', 'b'], []) == []
    
    # both empty
    assert module_0.total_match([], []) == []
    
    # single-character lists
    assert module_0.total_match(['a'], ['ab']) == ['a']
    assert module_0.total_match(['ab'], ['a']) == ['a']
    
    # lst1 shorter when equal to lst2 length boundary
    assert module_0.total_match(['four'], ['four']) == ['four']
    
    # lst2 strictly shorter
    assert module_0.total_match(['longer', 'strings'], ['tiny']) == ['tiny']
    
    print("All tests passed!")

if __name__ == "__main__":
    test_total_match()