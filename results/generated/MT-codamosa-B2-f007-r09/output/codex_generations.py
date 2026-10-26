

# Generated at 2026-10-25 11:07:10.113341
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "berry") == []
    assert module_0.filter_by_substring([], "apple") == []
    assert module_0.filter_by_substring(strings, "") == strings

# Generated at 2026-10-25 11:07:15.438935
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "an") == ["banana"]
    assert module_0.filter_by_substring(strings, "xyz") == []
    assert module_0.filter_by_substring([], "apple") == []
    assert module_0.filter_by_substring(strings, "") == strings

# Generated at 2026-10-25 11:07:19.329273
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "berry") == []
    assert module_0.filter_by_substring(strings, "") == strings
    assert module_0.filter_by_substring([], "apple") == []

# Generated at 2026-10-25 11:07:24.242944
# Unit test for function filter_by_substring
def test_filter_by_substring():
    assert module_0.filter_by_substring(
        ["apple", "banana", "pineapple", "orange"], "apple"
    ) == ["apple", "pineapple"]

    assert module_0.filter_by_substring(["cat", "dog", "bird"], "fish") == []
    assert module_0.filter_by_substring([], "test") == []
    assert module_0.filter_by_substring(["Apple", "apple"], "apple") == ["apple"]
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]

# Generated at 2026-10-25 11:07:28.851244
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "berry") == []
    assert module_0.filter_by_substring(strings, "") == strings
    assert module_0.filter_by_substring([], "apple") == []
    assert module_0.filter_by_substring(strings, "APPLE") == []  # Case-sensitive