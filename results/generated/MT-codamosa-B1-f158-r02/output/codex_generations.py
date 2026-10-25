

# Generated at 2026-10-24 11:21:12.378188
# Unit test for function find_max

# Generated at 2026-10-24 11:21:14.924197
# Unit test for function find_max

# Generated at 2026-10-24 11:21:17.429280
# Unit test for function find_max

# Generated at 2026-10-24 11:21:19.852083
# Unit test for function find_max

# Generated at 2026-10-24 11:21:45.689797
# Unit test for function find_max
def test_find_max():assert module_0.find_max(["aaa", "abc", "ab"]) == "abc"

# Generated at 2026-10-24 11:21:56.733935
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

# Generated at 2026-10-24 11:21:59.249453
# Unit test for function find_max

# Generated at 2026-10-24 11:22:01.699649
# Unit test for function find_max

# Generated at 2026-10-24 11:22:04.086585
# Unit test for function find_max

# Generated at 2026-10-24 11:22:06.504425
# Unit test for function find_max

# Generated at 2026-10-24 11:22:08.921972
# Unit test for function find_max

# Generated at 2026-10-24 11:22:11.438262
# Unit test for function find_max