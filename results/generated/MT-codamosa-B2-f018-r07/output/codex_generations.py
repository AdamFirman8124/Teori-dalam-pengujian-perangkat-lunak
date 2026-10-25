

# Generated at 2026-10-24 04:34:49.835504
# Unit test for function how_many_times
def test_how_many_times():
    assert module_0.how_many_times("hello world", "o") == 2
    assert module_0.how_many_times("banana", "ana") == 2  # Overlapping matches
    assert module_0.how_many_times("aaaa", "aa") == 3    # Overlapping matches
    assert module_0.how_many_times("python", "java") == 0
    assert module_0.how_many_times("", "a") == 0
    assert module_0.how_many_times("abc", "abc") == 1
    assert module_0.how_many_times("abc", "") == 4       # Empty substring occurs n + 1 times

# Generated at 2026-10-24 04:34:55.135444
# Unit test for function how_many_times
def test_how_many_times():
    assert module_0.how_many_times("hello", "l") == 2
    assert module_0.how_many_times("aaaa", "aa") == 3  # Overlapping occurrences
    assert module_0.how_many_times("hello world", "world") == 1
    assert module_0.how_many_times("hello", "x") == 0
    assert module_0.how_many_times("abc", "abcd") == 0
    assert module_0.how_many_times("", "a") == 0
    assert module_0.how_many_times("abc", "") == 4

# Generated at 2026-10-24 04:35:01.046087
# Unit test for function how_many_times
def test_how_many_times():
    assert module_0.how_many_times("hello world", "o") == 2
    assert module_0.how_many_times("banana", "ana") == 2  # Overlapping matches
    assert module_0.how_many_times("aaaa", "aa") == 3    # Overlapping matches
    assert module_0.how_many_times("python", "java") == 0
    assert module_0.how_many_times("test", "test") == 1
    assert module_0.how_many_times("", "a") == 0
    assert module_0.how_many_times("abc", "") == 4       # Empty string matches at each boundary

# Generated at 2026-10-24 04:35:03.461979
# Unit test for function how_many_times

# Generated at 2026-10-24 04:35:05.977669
# Unit test for function how_many_times

# Generated at 2026-10-24 04:35:19.731294
# Unit test for function how_many_times
def test_how_many_times():assert module_0.how_many_times("banana", "ana") == 2

# Generated at 2026-10-24 04:35:23.934465
# Unit test for function how_many_times
def test_how_many_times():
    assert module_0.how_many_times("hello world", "o") == 2
    assert module_0.how_many_times("abababa", "aba") == 3  # Overlapping matches
    assert module_0.how_many_times("aaaa", "aa") == 3      # Overlapping matches
    assert module_0.how_many_times("python", "java") == 0
    assert module_0.how_many_times("", "a") == 0
    assert module_0.how_many_times("abc", "abc") == 1