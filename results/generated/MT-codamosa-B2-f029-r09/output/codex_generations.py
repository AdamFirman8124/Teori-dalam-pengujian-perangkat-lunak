

# Generated at 2026-10-24 23:42:36.556392
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
    assert module_0.filter_by_prefix(strings, "Ap") == []  # Case-sensitive

# Generated at 2026-10-24 23:42:40.751930
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "application", "banana", "apricot", "grape"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "application",
        "apricot",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings
    assert module_0.filter_by_prefix(["Apple", "apple"], "A") == ["Apple"]

# Generated at 2026-10-24 23:42:45.157199
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application", "Apple"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings
    assert module_0.filter_by_prefix(strings, "Ap") == ["Apple"]

# Generated at 2026-10-24 23:42:49.765659
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application", "Apple"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix(strings, "") == strings
    assert module_0.filter_by_prefix([], "ap") == []

# Generated at 2026-10-24 23:42:54.668859
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
    assert module_0.filter_by_prefix(strings, "") == strings
    assert module_0.filter_by_prefix([], "ap") == []