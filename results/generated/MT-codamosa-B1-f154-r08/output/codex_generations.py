

# Generated at 2026-10-24 14:25:19.678270
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:25:22.093542
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:25:24.509180
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:25:26.925154
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:25:35.492597
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # basic rotation cases
    assert module_0.cycpattern_check("abcd", "abd") is False
    assert module_0.cycpattern_check("abab", "baa") is True
    assert module_0.cycpattern_check("efef", "eeff") is False
    assert module_0.cycpattern_check("himenss", "simen") is True
    assert module_0.cycpattern_check("himenss", "simens") is True
    assert module_0.cycpattern_check("himenss", "simenss") is True
    assert module_0.cycpattern_check("himenss", "simensss") is False

    # b longer than a -> impossible
    assert module_0.cycpattern_check("ab", "aba") is False

    # b is empty -> matches trivially
    assert module_0.cycpattern_check("abc", "") is True
    assert module_0.cycpattern_check("", "") is True

    # a empty, b not -> no match
    assert module_0.cycpattern_check("", "a") is False

    # exact substring (no rotation needed)
    assert module_0.cycpattern_check("hello", "ell") is True
    assert module_0.cycpattern_check("hello", "olle") is True

    # full rotation of entire a
    assert module_0.cycpattern_check("waterbottle", "erbottlewat") is True
    assert module_0.cycpattern_check("waterbottle", "botlewatter") is False

    # repeated characters / rotations
    assert module_0.cycpattern_check("aaaa", "aa") is True
    assert module_0.cycpattern_check("abcabc", "cab") is True
    assert module_0.cycpattern_check("abcabc", "acb") is False

    # single characters
    assert module_0.cycpattern_check("a", "a") is True
    assert module_0.cycpattern_check("a", "b") is False

# Generated at 2026-10-24 14:25:54.304252
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:25:56.825094
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:25:59.240180
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:26:01.654632
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:26:04.071036
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:26:06.485438
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:26:08.899475
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:26:11.315212
# Unit test for function cycpattern_check

# Generated at 2026-10-24 14:26:13.961066
# Unit test for function cycpattern_check