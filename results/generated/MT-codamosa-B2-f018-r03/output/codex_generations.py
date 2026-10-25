

# Generated at 2026-10-24 14:53:47.898323
# Unit test for function how_many_times

# Generated at 2026-10-24 14:53:50.311710
# Unit test for function how_many_times

# Generated at 2026-10-24 14:53:52.850380
# Unit test for function how_many_times

# Generated at 2026-10-24 14:53:55.265554
# Unit test for function how_many_times

# Generated at 2026-10-24 14:53:57.677898
# Unit test for function how_many_times

# Generated at 2026-10-24 14:54:00.091835
# Unit test for function how_many_times

# Generated at 2026-10-24 14:54:02.506541
# Unit test for function how_many_times

# Generated at 2026-10-24 14:54:04.917896
# Unit test for function how_many_times

# Generated at 2026-10-24 14:54:07.335207
# Unit test for function how_many_times

# Generated at 2026-10-24 14:54:09.742331
# Unit test for function how_many_times

# Generated at 2026-10-24 14:54:12.159111
# Unit test for function how_many_times

# Generated at 2026-10-24 14:54:15.304000
# Unit test for function how_many_times
def test_how_many_times():
    assert module_0.how_many_times('', 'x') == 0
    assert module_0.how_many_times('aaa', 'a') == 3
    assert module_0.how_many_times('aaaa', 'aa') == 3
    assert module_0.how_many_times('abc', 'x') == 0
    assert module_0.how_many_times('abcabc', 'abc') == 2
    assert module_0.how_many_times('ababc', 'ab') == 2

# Generated at 2026-10-24 14:54:16.757818
# Unit test for function how_many_times
def test_how_many_times():
    # basic cases
    assert module_0.how_many_times("hello", "l") == 2
    assert module_0.how_many_times("catcowcat", "cat") == 2
    assert module_0.how_many_times("hello world", "o") == 2

    # not found
    assert module_0.how_many_times("abc", "d") == 0
    assert module_0.how_many_times("hello", "z") == 0

    # overlapping matches
    assert module_0.how_many_times("aaaa", "aa") == 3
    assert module_0.how_many_times("abababa", "aba") == 3
    assert module_0.how_many_times("AAA", "AA") == 2

    # exact match and single char
    assert module_0.how_many_times("abc", "abc") == 1
    assert module_0.how_many_times("a", "a") == 1

    # substring longer than string
    assert module_0.how_many_times("hi", "hello") == 0
    assert module_0.how_many_times("", "a") == 0

    # empty string cases
    assert module_0.how_many_times("", "") == 1
    assert module_0.how_many_times("abc", "") == 4
    assert module_0.how_many_times("", "abc") == 0

    # case sensitivity
    assert module_0.how_many_times("Hello", "h") == 0
    assert module_0.how_many_times("Hello", "H") == 1