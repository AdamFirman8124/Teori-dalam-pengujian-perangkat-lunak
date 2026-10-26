

# Generated at 2026-10-25 06:18:19.542548
# Unit test for function total_match
def test_total_match():
    # both empty -> tie, return lst1
    assert module_0.total_match([], []) == []

    # lst1 has fewer total chars -> return lst1
    assert module_0.total_match(['a'], ['ab', 'cd']) == ['a']
    assert module_0.total_match(['hi', 'admin'], ['hi', 'hi', 'hi', 'hi', 'hi']) == ['hi', 'admin']

    # lst2 has fewer total chars -> return lst2
    assert module_0.total_match(['ab', 'cd'], ['a']) == ['a']
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

    # tie -> return lst1 (l1 <= l2)
    assert module_0.total_match(['ab'], ['cd']) == ['ab']
    assert module_0.total_match([], ['a']) == []
    assert module_0.total_match(['a'], []) == []

# Generated at 2026-10-25 06:18:29.681481
# Unit test for function total_match
def test_total_match():
    # First list has fewer total characters
    lst1 = ["hi", "there"]      # 7 characters
    lst2 = ["hello", "world"]   # 10 characters
    assert module_0.total_match(lst1, lst2) == lst1

    # Second list has fewer total characters
    lst1 = ["hello", "world"]   # 10 characters
    lst2 = ["hi", "there"]      # 7 characters
    assert module_0.total_match(lst1, lst2) == lst2

    # Equal lengths: function should return the first list
    lst1 = ["abc"]               # 3 characters
    lst2 = ["de", "f"]           # 3 characters
    assert module_0.total_match(lst1, lst2) == lst1

    # Empty lists
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 06:18:32.214630
# Unit test for function total_match

# Generated at 2026-10-25 06:18:34.631037
# Unit test for function total_match

# Generated at 2026-10-25 06:18:37.046098
# Unit test for function total_match

# Generated at 2026-10-25 06:18:39.639356
# Unit test for function total_match

# Generated at 2026-10-25 06:18:42.053164
# Unit test for function total_match

# Generated at 2026-10-25 06:18:44.468285
# Unit test for function total_match

# Generated at 2026-10-25 06:18:46.881658
# Unit test for function total_match

# Generated at 2026-10-25 06:18:49.381966
# Unit test for function total_match

# Generated at 2026-10-25 06:18:51.798609
# Unit test for function total_match