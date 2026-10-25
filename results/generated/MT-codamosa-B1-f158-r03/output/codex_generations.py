

# Generated at 2026-10-24 22:54:07.058478
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

# Generated at 2026-10-24 22:54:08.435839
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

# Generated at 2026-10-24 22:54:09.917195
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

# Generated at 2026-10-24 22:54:11.351200
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

# Generated at 2026-10-24 22:54:12.784433
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