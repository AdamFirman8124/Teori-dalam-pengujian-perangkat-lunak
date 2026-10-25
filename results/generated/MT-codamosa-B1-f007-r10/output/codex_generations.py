

# Generated at 2026-10-24 15:06:08.561800
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

# Generated at 2026-10-24 15:06:10.252999
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

# Generated at 2026-10-24 15:06:12.667484
# Unit test for function filter_by_substring

# Generated at 2026-10-24 15:06:15.080834
# Unit test for function filter_by_substring

# Generated at 2026-10-24 15:06:17.496972
# Unit test for function filter_by_substring

# Generated at 2026-10-24 15:06:19.915051
# Unit test for function filter_by_substring

# Generated at 2026-10-24 15:06:22.328208
# Unit test for function filter_by_substring

# Generated at 2026-10-24 15:06:24.740946
# Unit test for function filter_by_substring

# Generated at 2026-10-24 15:06:27.152146
# Unit test for function filter_by_substring

# Generated at 2026-10-24 15:06:29.565833
# Unit test for function filter_by_substring

# Generated at 2026-10-24 15:06:31.980275
# Unit test for function filter_by_substring