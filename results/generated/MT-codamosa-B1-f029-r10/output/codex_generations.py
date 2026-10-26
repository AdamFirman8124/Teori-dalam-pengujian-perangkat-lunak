

# Generated at 2026-10-25 10:07:45.332199
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

# Generated at 2026-10-25 10:07:46.735384
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

# Generated at 2026-10-25 10:08:03.931509
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

# Generated at 2026-10-25 10:08:06.347272
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 10:08:08.932226
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 10:08:11.346970
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 10:08:13.761696
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 10:08:16.177312
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 10:08:18.591304
# Unit test for function filter_by_prefix