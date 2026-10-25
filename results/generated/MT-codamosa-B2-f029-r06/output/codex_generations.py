

# Generated at 2026-10-24 22:05:54.838189
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application", "cherry"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings

# Generated at 2026-10-24 22:05:58.845768
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application", "cherry"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings

# Generated at 2026-10-24 22:06:03.894547
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == [
        "apple",
        "apricot",
    ]
    assert module_0.filter_by_prefix(["cat", "dog"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "A") == ["Apple"]

# Generated at 2026-10-24 22:06:07.958976
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application", "berry"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "b") == ["banana", "berry"]
    assert module_0.filter_by_prefix(strings, "z") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings
    assert module_0.filter_by_prefix(["Apple", "apple"], "A") == ["Apple"]

# Generated at 2026-10-24 22:06:10.506895
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 22:06:13.052300
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 22:06:15.469613
# Unit test for function filter_by_prefix