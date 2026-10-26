

# Generated at 2026-10-25 12:21:43.488703
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "hello", "hi"]) == "hello"

# Generated at 2026-10-25 12:22:31.206978
# Unit test for function longest
def test_longest():
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest([]) is None

    # If multiple strings have the same maximum length,
    # the first one should be returned.
    assert module_0.longest(["one", "two", "four", "five"]) == "four"

# Generated at 2026-10-25 12:22:40.526507
# Unit test for function longest
def test_longest():
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["same", "size"]) == "same"  # first longest string
    assert module_0.longest([""]) == ""
    assert module_0.longest([]) is None

# Generated at 2026-10-25 12:22:51.585602
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "three"]) == "three"

    # When multiple strings have the same length, the first is returned
    assert module_0.longest(["apple", "grape", "pear"]) == "apple"

# Generated at 2026-10-25 12:23:39.393106
# Unit test for function longest

# Generated at 2026-10-25 12:23:53.740451
# Unit test for function longest
def test_longest():assert module_0.longest(["a", "bb", "c"]) == "bb"

# Generated at 2026-10-25 12:24:11.765005
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest string
    assert module_0.longest(["", "hello", "hi"]) == "hello"

# Generated at 2026-10-25 12:24:34.855069
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "hello", "hi"]) == "hello"

# Generated at 2026-10-25 12:24:41.992517
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:24:43.506610
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:24:51.493283
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:24:53.487235
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:25:20.072408
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["cat", "dog", "bird"]) == "cat"  # first longest is returned
    assert module_0.longest(["", "a"]) == "a"

# Generated at 2026-10-25 12:26:12.392094
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "hello", "hi"]) == "hello"

# Generated at 2026-10-25 12:26:42.294969
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-25 12:27:28.869805
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:27:30.750977
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:27:43.230504
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"  # returns the first longest string
    assert module_0.longest(["same", "same"]) == "same"
    assert module_0.longest([""]) == ""

# Generated at 2026-10-25 12:28:08.003223
# Unit test for function longest
def test_longest():
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest([]) is None


def test_longest_returns_first_string_on_tie():
    assert module_0.longest(["apple", "grape", "pear"]) == "apple"


def test_longest_with_empty_strings():
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-25 12:28:09.538568
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:28:12.099261
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:28:21.054785
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:29:09.442364
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "abcd", "xy"]) == "abcd"
    assert module_0.longest(["hello", "world"]) == "hello"  # first longest is returned
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-25 12:29:56.650550
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a", "abc", "ab"]) == "abc"
    assert module_0.longest(["hello", "world"]) == "hello"  # first longest is returned
    assert module_0.longest(["single"]) == "single"
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-25 12:29:58.165744
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "bb", "c"]) == "bb"
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    # on tie, returns first longest
    assert module_0.longest(["bb", "aa"]) == "bb"
    assert module_0.longest(["a", "bb", "cc", "d"]) == "bb"
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-25 12:30:27.677034
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "hello", "hi"]) == "hello"

# Generated at 2026-10-25 12:31:15.377024
# Unit test for function longest

# Generated at 2026-10-25 12:31:17.260758
# Unit test for function longest
def test_longest():assert module_0.longest(["a", "bb", "c"]) == "bb"