

# Generated at 2026-10-24 11:22:17.636799
# Unit test for function find_max

# Generated at 2026-10-24 11:22:20.055197
# Unit test for function find_max

# Generated at 2026-10-24 11:22:22.472736
# Unit test for function find_max

# Generated at 2026-10-24 11:22:24.889561
# Unit test for function find_max

# Generated at 2026-10-24 11:22:27.308011
# Unit test for function find_max

# Generated at 2026-10-24 11:22:39.796664
# Unit test for function find_max
def test_find_max():assert module_0.find_max(["apple", "banana", "xyz"]) == "apple"

# Generated at 2026-10-24 11:22:41.230120
# Unit test for function find_max
def test_find_max():
    # most unique characters wins
    assert module_0.find_max(["a", "ab", "abc"]) == "abc"
    assert module_0.find_max(["aaaaa", "ab"]) == "ab"
    assert module_0.find_max(["hello", "world"]) == "world"  # 4 vs 5 unique

    # tie-break: lexicographically smallest
    assert module_0.find_max(["abd", "abc"]) == "abc"
    assert module_0.find_max(["cab", "bca", "abc"]) == "abc"

    # single element
    assert module_0.find_max(["solo"]) == "solo"

    # empty list raises IndexError
    try:
        module_0.find_max([])
        assert False, "Expected IndexError for empty list"
    except IndexError:
        pass

# Generated at 2026-10-24 11:22:42.586907
# Unit test for function find_max
def test_find_max():
    # most unique characters wins
    assert module_0.find_max(["a", "ab", "abc"]) == "abc"
    assert module_0.find_max(["aaaaa", "ab"]) == "ab"
    assert module_0.find_max(["hello", "world"]) == "world"  # 4 vs 5 unique

    # tie-break: lexicographically smallest
    assert module_0.find_max(["abd", "abc"]) == "abc"
    assert module_0.find_max(["cab", "bca", "abc"]) == "abc"

    # single element
    assert module_0.find_max(["solo"]) == "solo"

    # empty list raises IndexError
    try:
        module_0.find_max([])
        assert False, "Expected IndexError for empty list"
    except IndexError:
        pass

# Generated at 2026-10-24 11:22:43.940247
# Unit test for function find_max
def test_find_max():
    # most unique characters wins
    assert module_0.find_max(["a", "ab", "abc"]) == "abc"
    assert module_0.find_max(["aaaaa", "ab"]) == "ab"
    assert module_0.find_max(["hello", "world"]) == "world"  # 4 vs 5 unique

    # tie-break: lexicographically smallest
    assert module_0.find_max(["abd", "abc"]) == "abc"
    assert module_0.find_max(["cab", "bca", "abc"]) == "abc"

    # single element
    assert module_0.find_max(["solo"]) == "solo"

    # empty list raises IndexError
    try:
        module_0.find_max([])
        assert False, "Expected IndexError for empty list"
    except IndexError:
        pass