

# Generated at 2026-10-25 14:19:49.708328
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "apricot", "grape"]

    result = module_0.filter_by_substring(strings, "ap")

    assert result == ["apple", "apricot", "grape"]

# Generated at 2026-10-25 14:19:57.900994
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "apricot", "pineapple"]

    assert module_0.filter_by_substring(strings, "app") == ["apple", "pineapple"]
    assert module_0.filter_by_substring(strings, "ban") == ["banana"]
    assert module_0.filter_by_substring(strings, "xyz") == []
    assert module_0.filter_by_substring([], "app") == []

# Generated at 2026-10-25 14:20:04.951214
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "pineapple", "grape"]

    result = module_0.filter_by_substring(strings, "apple")

    assert result == ["apple", "pineapple"]

# Generated at 2026-10-25 14:20:06.399543
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # basic match
    assert module_0.filter_by_substring(["apple", "banana", "cherry"], "an") == ["banana"]
    # multiple matches preserve order
    assert module_0.filter_by_substring(["cat", "car", "dog", "scar"], "ca") == ["cat", "car", "scar"]
    # no match
    assert module_0.filter_by_substring(["a", "b"], "z") == []
    # empty substring matches everything
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]
    # empty input
    assert module_0.filter_by_substring([], "a") == []
    # substring equal to whole element
    assert module_0.filter_by_substring(["abc"], "abc") == ["abc"]
    # case sensitivity
    assert module_0.filter_by_substring(["Apple"], "apple") == []
    # does not mutate input
    data = ["apple", "banana"]
    module_0.filter_by_substring(data, "an")
    assert data == ["apple", "banana"]

# Generated at 2026-10-25 14:20:13.056393
# Unit test for function filter_by_substring
def test_filter_by_substring():
    strings = ["apple", "banana", "apricot", "grape", "pear"]

    result = module_0.filter_by_substring(strings, "ap")

    assert result == ["apple", "apricot", "grape"]