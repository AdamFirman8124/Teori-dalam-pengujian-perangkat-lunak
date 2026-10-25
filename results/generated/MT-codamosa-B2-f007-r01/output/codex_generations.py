

# Generated at 2026-10-24 04:22:14.635733
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "pineapple", "banana", "apricot"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "ap") == ["apple", "pineapple", "apricot"]
    assert module_0.filter_by_substring(strings, "orange") == []
    assert module_0.filter_by_substring([], "apple") == []
    assert module_0.filter_by_substring(strings, "") == strings
    assert module_0.filter_by_substring(strings, "Apple") == []  # Case-sensitive

# Generated at 2026-10-24 04:22:18.521831
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "an") == ["banana"]
    assert module_0.filter_by_substring(strings, "orange") == []
    assert module_0.filter_by_substring(strings, "") == strings
    assert module_0.filter_by_substring([], "apple") == []

# Generated at 2026-10-24 04:22:23.138899
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "orange"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "berry") == []
    assert module_0.filter_by_substring([], "apple") == []
    assert module_0.filter_by_substring(strings, "") == strings

# Generated at 2026-10-24 04:22:27.954631
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "berry") == []
    assert module_0.filter_by_substring(strings, "") == strings
    assert module_0.filter_by_substring([], "apple") == []

# Generated at 2026-10-24 04:22:32.142217
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    assert module_0.filter_by_substring(strings, "apple") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "xyz") == []
    assert module_0.filter_by_substring([], "apple") == []
    assert module_0.filter_by_substring(strings, "") == strings
    assert module_0.filter_by_substring(strings, "Apple") == []  # Case-sensitive