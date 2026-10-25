

# Generated at 2026-10-24 22:52:05.198918
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

# Generated at 2026-10-24 22:52:06.557920
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

# Generated at 2026-10-24 22:52:07.958485
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

# Generated at 2026-10-24 22:52:09.399890
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

# Generated at 2026-10-24 22:52:10.746503
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