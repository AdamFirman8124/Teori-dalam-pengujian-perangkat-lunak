

# Generated at 2026-10-25 07:05:37.370788
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # basic match
    assert module_0.filter_by_substring(["apple", "banana", "cherry"], "an") == ["banana"]
    # multiple matches, order preserved
    assert module_0.filter_by_substring(["cat", "bat", "car"], "ca") == ["cat", "car"]
    # no matches
    assert module_0.filter_by_substring(["apple", "banana"], "zzz") == []
    # empty input list
    assert module_0.filter_by_substring([], "a") == []
    # empty substring matches everything
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]
    # substring at start / end
    assert module_0.filter_by_substring(["hello", "shell", "help"], "hel") == ["hello", "help"]
    assert module_0.filter_by_substring(["hello", "shell", "help"], "ell") == ["hello", "shell"]
    # case sensitivity
    assert module_0.filter_by_substring(["Apple", "apple"], "app") == ["apple"]
    # empty strings in input
    assert module_0.filter_by_substring(["", "a"], "") == ["", "a"]
    assert module_0.filter_by_substring(["", "a"], "a") == ["a"]

# Generated at 2026-10-25 07:05:38.903126
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

# Generated at 2026-10-25 07:05:40.361556
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

# Generated at 2026-10-25 07:05:41.762289
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

# Generated at 2026-10-25 07:05:44.535877
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