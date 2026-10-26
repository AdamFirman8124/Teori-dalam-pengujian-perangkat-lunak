

# Generated at 2026-10-25 07:29:17.866079
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ('bcd', False)
    assert module_0.reverse_delete("abcdef", "b") == ('acdef', False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert module_0.reverse_delete("racecar", "b") == ('racecar', True)
    assert module_0.reverse_delete("a", "b") == ('a', True)
    assert module_0.reverse_delete("a", "a") == ('', True)
    assert module_0.reverse_delete("", "abc") == ('', True)
    assert module_0.reverse_delete("abc", "") == ('abc', False)
    assert module_0.reverse_delete("aaa", "a") == ('', True)

# Generated at 2026-10-25 07:29:20.017715
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ('bcd', False)
    assert module_0.reverse_delete("abcdef", "b") == ('acdef', False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert module_0.reverse_delete("racecar", "b") == ('racecar', True)
    assert module_0.reverse_delete("a", "b") == ('a', True)
    assert module_0.reverse_delete("a", "a") == ('', True)
    assert module_0.reverse_delete("", "abc") == ('', True)
    assert module_0.reverse_delete("abc", "") == ('abc', False)
    assert module_0.reverse_delete("aaa", "a") == ('', True)

# Generated at 2026-10-25 07:29:22.564257
# Unit test for function reverse_delete

# Generated at 2026-10-25 07:29:25.000423
# Unit test for function reverse_delete

# Generated at 2026-10-25 07:29:27.412754
# Unit test for function reverse_delete

# Generated at 2026-10-25 07:29:29.834029
# Unit test for function reverse_delete

# Generated at 2026-10-25 07:29:32.248921
# Unit test for function reverse_delete

# Generated at 2026-10-25 07:29:34.665230
# Unit test for function reverse_delete

# Generated at 2026-10-25 07:29:36.033962
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ('bcd', False)
    assert module_0.reverse_delete("abcdef", "b") == ('acdef', False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert module_0.reverse_delete("racecar", "b") == ('racecar', True)
    assert module_0.reverse_delete("a", "b") == ('a', True)
    assert module_0.reverse_delete("a", "a") == ('', True)
    assert module_0.reverse_delete("", "abc") == ('', True)
    assert module_0.reverse_delete("abc", "") == ('abc', False)
    assert module_0.reverse_delete("aaa", "a") == ('', True)