

# Generated at 2026-10-24 04:35:03.720996
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:35:06.219352
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:35:14.085631
# Unit test for function filter_by_prefix
def test_filter_by_prefix():assert module_0.filter_by_prefix(["apple", "apricot", "banana", "avocado"], "ap") == ["apple", "apricot"]

# Generated at 2026-10-24 04:35:19.122578
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == [
        "apple",
        "apricot",
    ]
    assert module_0.filter_by_prefix(["cat", "dog", "bird"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["Apple", "apple"], "A") == ["Apple"]
    assert module_0.filter_by_prefix(["one", "two"], "") == ["one", "two"]

# Generated at 2026-10-24 04:35:23.663697
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == [
        "apple",
        "apricot",
    ]
    assert module_0.filter_by_prefix(["car", "cat", "dog"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["Apple", "apple"], "A") == ["Apple"]
    assert module_0.filter_by_prefix(["one", "two"], "") == ["one", "two"]

# Generated at 2026-10-24 04:35:29.855850
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

# Generated at 2026-10-24 04:35:34.162636
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "z") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings