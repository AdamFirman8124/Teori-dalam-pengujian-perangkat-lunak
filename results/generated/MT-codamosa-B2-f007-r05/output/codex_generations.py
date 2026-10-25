

# Generated at 2026-10-24 12:57:46.638688
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

# Generated at 2026-10-24 12:57:49.147653
# Unit test for function filter_by_substring

# Generated at 2026-10-24 12:57:51.562454
# Unit test for function filter_by_substring

# Generated at 2026-10-24 12:57:53.976522
# Unit test for function filter_by_substring

# Generated at 2026-10-24 12:57:56.393499
# Unit test for function filter_by_substring

# Generated at 2026-10-24 12:57:59.090003
# Unit test for function filter_by_substring

# Generated at 2026-10-24 12:58:13.713456
# Unit test for function filter_by_substring
def test_filter_by_substring():strings = ["apple", "banana", "apricot", "grape"]

# Generated at 2026-10-24 12:58:15.139307
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

# Generated at 2026-10-24 12:58:16.571399
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