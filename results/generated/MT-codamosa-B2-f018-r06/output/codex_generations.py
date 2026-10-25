

# Generated at 2026-10-24 12:56:59.183577
# Unit test for function how_many_times
def test_how_many_times():
    assert module_0.how_many_times("banana", "ana") == 2  # overlapping matches
    assert module_0.how_many_times("hello", "l") == 2
    assert module_0.how_many_times("aaaa", "aa") == 3  # overlapping matches
    assert module_0.how_many_times("hello", "world") == 0
    assert module_0.how_many_times("", "a") == 0
    assert module_0.how_many_times("abc", "abcd") == 0

# Generated at 2026-10-24 12:57:28.743914
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

# Generated at 2026-10-24 12:57:30.129810
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

# Generated at 2026-10-24 12:57:31.511981
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

# Generated at 2026-10-24 12:57:32.948761
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