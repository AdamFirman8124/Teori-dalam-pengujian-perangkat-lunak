

# Generated at 2026-10-25 03:16:43.329356
# Unit test for function filter_by_prefix

# Generated at 2026-10-25 03:16:48.118768
# Unit test for function filter_by_prefix
def test_filter_by_prefix():strings = ["apple", "apricot", "banana", "application", "grape"]

# Generated at 2026-10-25 03:16:53.034202
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application", "berry"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings

# Generated at 2026-10-25 03:16:56.370547
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application", "grape"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings

# Generated at 2026-10-25 03:17:00.307844
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

# Generated at 2026-10-25 03:17:04.640565
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(
        ["apple", "apricot", "banana", "application"], "ap"
    ) == ["apple", "apricot", "application"]

    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(["apple", "Apple"], "A") == ["Apple"]
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]