

# Generated at 2026-10-24 14:14:03.165289
# Unit test for function total_match
def test_total_match():
    # lst1 total chars smaller -> return lst1
    assert module_0.total_match(['a', 'bb'], ['cccc']) == ['a', 'bb']

    # lst2 total chars smaller -> return lst2
    assert module_0.total_match(['hello', 'world'], ['hi']) == ['hi']

    # equal totals -> return lst1
    assert module_0.total_match(['ab', 'cd'], ['efgh']) == ['ab', 'cd']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

    # both empty
    assert module_0.total_match([], []) == []

    # empty strings
    assert module_0.total_match(['', ''], ['']) == ['', '']

# Generated at 2026-10-24 14:14:04.588855
# Unit test for function total_match
def test_total_match():
    # lst1 total chars smaller -> return lst1
    assert module_0.total_match(['a', 'bb'], ['cccc']) == ['a', 'bb']

    # lst2 total chars smaller -> return lst2
    assert module_0.total_match(['hello', 'world'], ['hi']) == ['hi']

    # equal totals -> return lst1
    assert module_0.total_match(['ab', 'cd'], ['efgh']) == ['ab', 'cd']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

    # both empty
    assert module_0.total_match([], []) == []

    # empty strings
    assert module_0.total_match(['', ''], ['']) == ['', '']

# Generated at 2026-10-24 14:14:06.044159
# Unit test for function total_match
def test_total_match():
    # lst1 total chars smaller -> return lst1
    assert module_0.total_match(['a', 'bb'], ['cccc']) == ['a', 'bb']

    # lst2 total chars smaller -> return lst2
    assert module_0.total_match(['hello', 'world'], ['hi']) == ['hi']

    # equal totals -> return lst1
    assert module_0.total_match(['ab', 'cd'], ['efgh']) == ['ab', 'cd']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

    # both empty
    assert module_0.total_match([], []) == []

    # empty strings
    assert module_0.total_match(['', ''], ['']) == ['', '']

# Generated at 2026-10-24 14:14:07.566963
# Unit test for function total_match
def test_total_match():
    # lst1 total chars smaller -> return lst1
    assert module_0.total_match(['a', 'bb'], ['cccc']) == ['a', 'bb']

    # lst2 total chars smaller -> return lst2
    assert module_0.total_match(['hello', 'world'], ['hi']) == ['hi']

    # equal totals -> return lst1
    assert module_0.total_match(['ab', 'cd'], ['efgh']) == ['ab', 'cd']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

    # both empty
    assert module_0.total_match([], []) == []

    # empty strings
    assert module_0.total_match(['', ''], ['']) == ['', '']

# Generated at 2026-10-24 14:14:13.811161
# Unit test for function total_match
def test_total_match():
    # lst1 shorter â returns lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']

    # lst2 shorter â returns lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # equal totals â returns lst1 (tie goes to lst1)
    assert module_0.total_match(['ab'], ['cd']) == ['ab']

    # empty lst1 wins (total 0)
    assert module_0.total_match([], ['a', 'b']) == []

    # both empty â returns lst1
    assert module_0.total_match([], []) == []

    # single vs multiple chars
    assert module_0.total_match(['a'], ['bb']) == ['a']

    print("All tests passed!")


test_total_match()