

# Generated at 2026-10-24 14:38:03.119417
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

# Generated at 2026-10-24 14:38:40.834044
# Unit test for function find_max
def test_find_max():
    # Most distinct letters wins
    assert module_0.find_max(["ab", "abcd", "abc"]) == "abcd"
    # Repeated letters don't add
    assert module_0.find_max(["aaaa", "ab"]) == "ab"
    # Tie -> alphabetically first
    assert module_0.find_max(["ba", "ab", "ac"]) == "ab"
    assert module_0.find_max(["xyz", "abc", "def"]) == "abc"
    # Single word / empty string
    assert module_0.find_max(["only"]) == "only"
    assert module_0.find_max(["", "a"]) == "a"
    print("All tests passed")

if __name__ == "__main__":
    test_find_max()

# Generated at 2026-10-24 14:38:42.234571
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

# Generated at 2026-10-24 14:38:43.670127
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

# Generated at 2026-10-24 14:38:45.082655
# Unit test for function find_max
def test_find_max():
    # Most distinct letters wins
    assert module_0.find_max(["ab", "abcd", "abc"]) == "abcd"
    # Repeated letters don't add
    assert module_0.find_max(["aaaa", "ab"]) == "ab"
    # Tie -> alphabetically first
    assert module_0.find_max(["ba", "ab", "ac"]) == "ab"
    assert module_0.find_max(["xyz", "abc", "def"]) == "abc"
    # Single word / empty string
    assert module_0.find_max(["only"]) == "only"
    assert module_0.find_max(["", "a"]) == "a"
    print("All tests passed")

if __name__ == "__main__":
    test_find_max()