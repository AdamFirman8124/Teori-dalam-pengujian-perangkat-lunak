

# Generated at 2026-10-25 10:16:55.338083
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # basic filtering
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]

    # no matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []

    # empty input list
    assert module_0.filter_by_prefix([], "a") == []

    # empty prefix matches all
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]

    # case-sensitive
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

    # prefix longer than strings
    assert module_0.filter_by_prefix(["a", "ab"], "abc") == []

# Generated at 2026-10-25 10:17:03.222866
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # basic filtering
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]

    # no matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []

    # empty input list
    assert module_0.filter_by_prefix([], "a") == []

    # empty prefix matches all
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]

    # case-sensitive
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

    # prefix longer than strings
    assert module_0.filter_by_prefix(["a", "ab"], "abc") == []

# Generated at 2026-10-25 10:17:04.665138
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # basic filtering
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]

    # no matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []

    # empty input list
    assert module_0.filter_by_prefix([], "a") == []

    # empty prefix matches all
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]

    # case-sensitive
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

    # prefix longer than strings
    assert module_0.filter_by_prefix(["a", "ab"], "abc") == []

# Generated at 2026-10-25 10:17:06.202288
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # basic filtering
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]

    # no matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []

    # empty input list
    assert module_0.filter_by_prefix([], "a") == []

    # empty prefix matches all
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]

    # case-sensitive
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

    # prefix longer than strings
    assert module_0.filter_by_prefix(["a", "ab"], "abc") == []

# Generated at 2026-10-25 10:17:07.728230
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # basic filtering
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]

    # no matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []

    # empty input list
    assert module_0.filter_by_prefix([], "a") == []

    # empty prefix matches all
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]

    # case-sensitive
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

    # prefix longer than strings
    assert module_0.filter_by_prefix(["a", "ab"], "abc") == []