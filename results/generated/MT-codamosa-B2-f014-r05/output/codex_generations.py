

# Generated at 2026-10-24 14:47:15.069223
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:17.482701
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:19.899423
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:22.311248
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:24.724895
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:27.138540
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:29.578215
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:32.018371
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:34.447548
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:36.860674
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:39.275307
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:41.693972
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:47:44.107208
# Unit test for function all_prefixes

# Generated at 2026-10-24 14:48:12.810776
# Unit test for function all_prefixes
def test_all_prefixes():
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]
    assert module_0.all_prefixes("") == []
    assert module_0.all_prefixes("a") == ["a"]
    assert module_0.all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert module_0.all_prefixes("xy") == ["x", "xy"]