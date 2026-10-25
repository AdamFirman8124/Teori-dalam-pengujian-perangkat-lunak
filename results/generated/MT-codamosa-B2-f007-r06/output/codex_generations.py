

# Generated at 2026-10-24 06:08:08.140786
# Unit test for function filter_by_substring

# Generated at 2026-10-24 06:08:10.556235
# Unit test for function filter_by_substring

# Generated at 2026-10-24 06:08:19.650580
# Unit test for function filter_by_substring
def test_filter_by_substring():assert module_0.filter_by_substring(["apple", "banana", "apricot"], "ap") == ["apple", "apricot"]

# Generated at 2026-10-24 06:08:25.381094
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "berry") == []
    assert module_0.filter_by_substring(strings, "") == strings
    assert module_0.filter_by_substring([], "apple") == []

# Generated at 2026-10-24 06:08:29.358652
# Unit test for function filter_by_substring
def test_filter_by_substring():
    assert module_0.filter_by_substring(["apple", "banana", "pineapple"], "apple") == [
        "apple",
        "pineapple",
    ]
    assert module_0.filter_by_substring(["cat", "dog", "bird"], "fish") == []
    assert module_0.filter_by_substring([], "test") == []
    assert module_0.filter_by_substring(["Apple", "apple"], "apple") == ["apple"]
    assert module_0.filter_by_substring(["a", "b", "c"], "") == ["a", "b", "c"]

# Generated at 2026-10-24 06:08:34.193642
# Unit test for function filter_by_substring
def test_filter_by_substring():
    assert module_0.filter_by_substring(
        ["apple", "banana", "apricot", "grape"], "ap"
    ) == ["apple", "apricot", "grape"]

    assert module_0.filter_by_substring(["cat", "dog", "bird"], "fish") == []
    assert module_0.filter_by_substring([], "test") == []
    assert module_0.filter_by_substring(["one", "two"], "") == ["one", "two"]

# Generated at 2026-10-24 06:08:39.008535
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "an") == ["banana"]
    assert module_0.filter_by_substring(strings, "orange") == []
    assert module_0.filter_by_substring(strings, "") == strings
    assert module_0.filter_by_substring([], "apple") == []