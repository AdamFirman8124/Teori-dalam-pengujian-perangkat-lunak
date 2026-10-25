

# Generated at 2026-10-24 11:57:03.377928
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "orange", "grape"]

    result = module_0.filter_by_substring(strings, "apple")

    assert result == ["apple", "pineapple"]

# Generated at 2026-10-24 11:57:14.330493
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # basic filtering
    assert module_0.filter_by_substring(["apple", "banana", "apricot", "blueberry"], "ap") == ["apple", "apricot"]
    # no matches
    assert module_0.filter_by_substring(["cat", "dog", "bird"], "z") == []
    # empty input list
    assert module_0.filter_by_substring([], "test") == []
    # empty substring matches all
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]
    # case-sensitive matching
    assert module_0.filter_by_substring(["Apple", "apple", "APPLE"], "apple") == ["apple"]
    # substring equals whole string
    assert module_0.filter_by_substring(["test", "testing", "attest"], "test") == ["test", "testing", "attest"]

# Generated at 2026-10-24 11:57:21.756007
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # basic match
    assert module_0.filter_by_substring(["abc", "bacd", "cde", "array"], "a") == ["abc", "bacd", "array"]
    # no matches
    assert module_0.filter_by_substring(["abc", "def"], "z") == []
    # empty input list
    assert module_0.filter_by_substring([], "a") == []
    # empty substring matches everything
    assert module_0.filter_by_substring(["a", "", "b"], "") == ["a", "", "b"]
    # substring longer than any element
    assert module_0.filter_by_substring(["a", "b"], "abcdef") == []
    # case sensitivity
    assert module_0.filter_by_substring(["Apple", "apple"], "A") == ["Apple"]
    # match at start, middle, end
    assert module_0.filter_by_substring(["xay", "ax", "xa"], "a") == ["xay", "ax", "xa"]
    # exact element match
    assert module_0.filter_by_substring(["ab", "abc"], "ab") == ["ab", "abc"]
    # duplicates preserved
    assert module_0.filter_by_substring(["aa", "aa"], "a") == ["aa", "aa"]
    # input not mutated
    data = ["abc", "def"]
    module_0.filter_by_substring(data, "a")
    assert data == ["abc", "def"]

# Generated at 2026-10-24 11:57:24.376554
# Unit test for function filter_by_substring

# Generated at 2026-10-24 11:57:26.796974
# Unit test for function filter_by_substring

# Generated at 2026-10-24 11:57:53.548446
# Unit test for function filter_by_substring
def test_filter_by_substring():assert module_0.filter_by_substring(["apple", "banana", "apricot"], "ap") == ["apple", "apricot"]

# Generated at 2026-10-24 11:57:54.878396
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # basic match
    assert module_0.filter_by_substring(["abc", "bacd", "cde", "array"], "a") == ["abc", "bacd", "array"]
    # no matches
    assert module_0.filter_by_substring(["abc", "def"], "z") == []
    # empty input list
    assert module_0.filter_by_substring([], "a") == []
    # empty substring matches everything
    assert module_0.filter_by_substring(["a", "", "b"], "") == ["a", "", "b"]
    # substring longer than any element
    assert module_0.filter_by_substring(["a", "b"], "abcdef") == []
    # case sensitivity
    assert module_0.filter_by_substring(["Apple", "apple"], "A") == ["Apple"]
    # match at start, middle, end
    assert module_0.filter_by_substring(["xay", "ax", "xa"], "a") == ["xay", "ax", "xa"]
    # exact element match
    assert module_0.filter_by_substring(["ab", "abc"], "ab") == ["ab", "abc"]
    # duplicates preserved
    assert module_0.filter_by_substring(["aa", "aa"], "a") == ["aa", "aa"]
    # input not mutated
    data = ["abc", "def"]
    module_0.filter_by_substring(data, "a")
    assert data == ["abc", "def"]