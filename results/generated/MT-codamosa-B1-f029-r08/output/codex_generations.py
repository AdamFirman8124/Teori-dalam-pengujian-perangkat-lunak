

# Generated at 2026-10-25 09:47:57.983476
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:00.397972
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:02.809847
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:05.225016
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:07.637698
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:10.050027
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:12.464704
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:14.886157
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:17.296087
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:19.708402
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:22.122112
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 09:48:33.006374
# Unit test for function filter_by_prefix
def test_filter_by_prefix():strings = ["apple", "application", "banana", "app", "grape"]

# Generated at 2026-10-25 09:48:34.362660
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix([], 'a') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ab') == ['abc']
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'a') == ['abc']  # case-sensitive