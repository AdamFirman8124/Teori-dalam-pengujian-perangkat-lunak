

# Generated at 2026-10-25 03:29:06.632680
# Unit test for function all_prefixes
def test_all_prefixes():
    # normal case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # single character
    assert module_0.all_prefixes("a") == ["a"]

    # empty string -> no prefixes
    assert module_0.all_prefixes("") == []

    # repeated characters
    assert module_0.all_prefixes("aaa") == ["a", "aa", "aaa"]

    # spaces / punctuation are just characters
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]

    # long input: count and endpoints
    s = "x" * 1000
    prefixes = module_0.all_prefixes(s)
    assert len(prefixes) == 1000
    assert prefixes[0] == "x"
    assert prefixes[-1] == s

    # original string is not mutated / prefixes are distinct objects
    s = "abc"
    module_0.all_prefixes(s)
    assert s == "abc"

# Generated at 2026-10-25 03:29:07.983626
# Unit test for function all_prefixes
def test_all_prefixes():
    # normal case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # single character
    assert module_0.all_prefixes("a") == ["a"]

    # empty string -> no prefixes
    assert module_0.all_prefixes("") == []

    # repeated characters
    assert module_0.all_prefixes("aaa") == ["a", "aa", "aaa"]

    # spaces / punctuation are just characters
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]

    # long input: count and endpoints
    s = "x" * 1000
    prefixes = module_0.all_prefixes(s)
    assert len(prefixes) == 1000
    assert prefixes[0] == "x"
    assert prefixes[-1] == s

    # original string is not mutated / prefixes are distinct objects
    s = "abc"
    module_0.all_prefixes(s)
    assert s == "abc"

# Generated at 2026-10-25 03:29:09.306013
# Unit test for function all_prefixes
def test_all_prefixes():
    # normal case
    assert module_0.all_prefixes("abc") == ["a", "ab", "abc"]

    # single character
    assert module_0.all_prefixes("a") == ["a"]

    # empty string -> no prefixes
    assert module_0.all_prefixes("") == []

    # repeated characters
    assert module_0.all_prefixes("aaa") == ["a", "aa", "aaa"]

    # spaces / punctuation are just characters
    assert module_0.all_prefixes("a b") == ["a", "a ", "a b"]

    # long input: count and endpoints
    s = "x" * 1000
    prefixes = module_0.all_prefixes(s)
    assert len(prefixes) == 1000
    assert prefixes[0] == "x"
    assert prefixes[-1] == s

    # original string is not mutated / prefixes are distinct objects
    s = "abc"
    module_0.all_prefixes(s)
    assert s == "abc"

# Generated at 2026-10-25 03:29:11.725169
# Unit test for function all_prefixes

# Generated at 2026-10-25 03:29:14.140154
# Unit test for function all_prefixes

# Generated at 2026-10-25 03:29:16.555212
# Unit test for function all_prefixes

# Generated at 2026-10-25 03:29:20.475775
# Unit test for function all_prefixes

# Generated at 2026-10-25 03:29:22.901375
# Unit test for function all_prefixes

# Generated at 2026-10-25 03:29:25.321749
# Unit test for function all_prefixes