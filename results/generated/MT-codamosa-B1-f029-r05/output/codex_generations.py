

# Generated at 2026-10-25 01:14:01.533206
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 01:14:04.128745
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 01:14:06.543909
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 01:14:08.961948
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 01:14:13.558879
# Unit test for function filter_by_prefix
def test_filter_by_prefix():strings = ["apple", "apricot", "banana", "application", "grape"]

# Generated at 2026-10-25 01:14:17.512237
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == [
        "apple",
        "apricot",
    ]
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "A") == ["Apple"]

# Generated at 2026-10-25 01:14:22.010939
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(
        ["apple", "application", "banana", "apricot"], "ap"
    ) == ["apple", "application", "apricot"]

    assert module_0.filter_by_prefix(["cat", "dog", "bird"], "z") == []
    assert module_0.filter_by_prefix([], "test") == []
    assert module_0.filter_by_prefix(["test", "testing", "contest"], "test") == [
        "test",
        "testing",
    ]
    assert module_0.filter_by_prefix(["Apple", "apple"], "A") == ["Apple"]
    assert module_0.filter_by_prefix(["a", "b", ""], "") == ["a", "b", ""]

# Generated at 2026-10-25 01:14:26.425464
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings
    assert module_0.filter_by_prefix(strings, "AP") == []  # Case-sensitive