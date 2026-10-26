

# Generated at 2026-10-25 12:12:16.420913
# Unit test for function total_match
def test_total_match():
    # both empty -> return first
    assert module_0.total_match([], []) == []

    # 7 chars vs 4 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # 7 chars vs 16 chars -> return first
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # 7 chars vs 6 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # 1 char vs 5 chars -> return first
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # equal total -> return first
    assert module_0.total_match(['a', 'b'], ['c', 'd']) == ['a', 'b']
    assert module_0.total_match(['hi'], ['hi']) == ['hi']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

# Generated at 2026-10-25 12:12:17.938078
# Unit test for function total_match
def test_total_match():
    # both empty -> return first
    assert module_0.total_match([], []) == []

    # 7 chars vs 4 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # 7 chars vs 16 chars -> return first
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # 7 chars vs 6 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # 1 char vs 5 chars -> return first
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # equal total -> return first
    assert module_0.total_match(['a', 'b'], ['c', 'd']) == ['a', 'b']
    assert module_0.total_match(['hi'], ['hi']) == ['hi']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

# Generated at 2026-10-25 12:12:24.220265
# Unit test for function total_match
def test_total_match():
    # both empty -> return first
    assert module_0.total_match([], []) == []

    # 7 chars vs 4 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # 7 chars vs 16 chars -> return first
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # 7 chars vs 6 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # 1 char vs 5 chars -> return first
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # equal total -> return first
    assert module_0.total_match(['a', 'b'], ['c', 'd']) == ['a', 'b']
    assert module_0.total_match(['hi'], ['hi']) == ['hi']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

# Generated at 2026-10-25 12:12:30.500069
# Unit test for function total_match
def test_total_match():
    # both empty -> return first
    assert module_0.total_match([], []) == []

    # 7 chars vs 4 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # 7 chars vs 16 chars -> return first
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # 7 chars vs 6 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # 1 char vs 5 chars -> return first
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # equal total -> return first
    assert module_0.total_match(['a', 'b'], ['c', 'd']) == ['a', 'b']
    assert module_0.total_match(['hi'], ['hi']) == ['hi']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

# Generated at 2026-10-25 12:12:33.885482
# Unit test for function total_match
def test_total_match():
    # both empty -> return first
    assert module_0.total_match([], []) == []

    # 7 chars vs 4 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # 7 chars vs 16 chars -> return first
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

    # 7 chars vs 6 chars -> return second
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

    # 1 char vs 5 chars -> return first
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

    # equal total -> return first
    assert module_0.total_match(['a', 'b'], ['c', 'd']) == ['a', 'b']
    assert module_0.total_match(['hi'], ['hi']) == ['hi']

    # empty vs non-empty
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []