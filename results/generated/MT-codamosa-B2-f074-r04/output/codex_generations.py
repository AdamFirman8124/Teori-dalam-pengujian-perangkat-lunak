

# Generated at 2026-10-24 12:51:01.175895
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

# Generated at 2026-10-24 12:51:02.617634
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

# Generated at 2026-10-24 12:51:04.043626
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

# Generated at 2026-10-24 12:51:05.414686
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

# Generated at 2026-10-24 12:51:10.558458
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