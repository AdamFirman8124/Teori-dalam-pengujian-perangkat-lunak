

# Generated at 2026-10-24 04:36:23.597909
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:26.008971
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:28.421839
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:30.832300
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:33.244172
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:35.656049
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:38.068408
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:40.479350
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:42.890818
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 04:36:47.658226
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "application", "banana", "app", "apricot"]

    assert module_0.filter_by_prefix(strings, "app") == [
        "apple",
        "application",
        "app",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "xyz") == []
    assert module_0.filter_by_prefix(strings, "") == strings
    assert module_0.filter_by_prefix([], "app") == []

# Generated at 2026-10-24 04:36:51.884948
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