

# Generated at 2026-10-25 06:53:06.154804
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

# Generated at 2026-10-25 06:53:07.588154
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

# Generated at 2026-10-25 06:53:09.021115
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

# Generated at 2026-10-25 06:53:11.084743
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

# Generated at 2026-10-25 06:53:12.482941
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