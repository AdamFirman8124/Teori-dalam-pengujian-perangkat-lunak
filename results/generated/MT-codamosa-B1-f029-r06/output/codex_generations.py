

# Generated at 2026-10-24 05:51:41.345591
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:51:43.760262
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:51:46.177213
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:51:48.590764
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:51:51.004834
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:51:53.424587
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:51:55.968122
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:51:58.382279
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:52:00.797866
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:52:03.218148
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:52:05.630254
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 05:52:08.195216
# Unit test for function filter_by_prefix
def test_filter_by_prefix():assert module_0.filter_by_prefix(["apple", "apricot", "banana", "avocado"], "ap") == ["apple", "apricot"]

# Generated at 2026-10-24 05:52:14.464346
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "apricot", "banana", "application"]

    assert module_0.filter_by_prefix(strings, "ap") == [
        "apple",
        "apricot",
        "application",
    ]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "z") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(strings, "") == strings