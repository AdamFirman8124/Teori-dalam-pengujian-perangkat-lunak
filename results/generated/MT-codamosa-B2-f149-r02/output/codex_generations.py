

# Generated at 2026-10-24 23:42:04.611741
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 23:42:07.177465
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 23:42:09.733855
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 23:42:12.157702
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 23:42:17.712587
# Unit test for function sorted_list_sum
def test_sorted_list_sum():result = module_0.sorted_list_sum(["aaaa", "b", "cc", "ddd", "bb"])

# Generated at 2026-10-24 23:42:23.958390
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Filters out odd-length strings, sorts by length then alphabetically
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert module_0.sorted_list_sum(["abc", "abcd", "a", "aa"]) == ["aa", "abcd"]
    assert module_0.sorted_list_sum([]) == []
    assert module_0.sorted_list_sum(["a", "bbb", "c"]) == []
    # Same length -> alphabetical order (from the pre-sort)
    assert module_0.sorted_list_sum(["dd", "cc", "bb"]) == ["bb", "cc", "dd"]
    # Mixed lengths, all even
    assert module_0.sorted_list_sum(["aaaa", "bb", "cc"]) == ["bb", "cc", "aaaa"]

test_sorted_list_sum()
print("All tests passed")

# Generated at 2026-10-24 23:42:25.285417
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Filters out odd-length strings, sorts by length then alphabetically
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert module_0.sorted_list_sum(["abc", "abcd", "a", "aa"]) == ["aa", "abcd"]
    assert module_0.sorted_list_sum([]) == []
    assert module_0.sorted_list_sum(["a", "bbb", "c"]) == []
    # Same length -> alphabetical order (from the pre-sort)
    assert module_0.sorted_list_sum(["dd", "cc", "bb"]) == ["bb", "cc", "dd"]
    # Mixed lengths, all even
    assert module_0.sorted_list_sum(["aaaa", "bb", "cc"]) == ["bb", "cc", "aaaa"]

test_sorted_list_sum()
print("All tests passed")

# Generated at 2026-10-24 23:42:26.611098
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Filters out odd-length strings, sorts by length then alphabetically
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert module_0.sorted_list_sum(["abc", "abcd", "a", "aa"]) == ["aa", "abcd"]
    assert module_0.sorted_list_sum([]) == []
    assert module_0.sorted_list_sum(["a", "bbb", "c"]) == []
    # Same length -> alphabetical order (from the pre-sort)
    assert module_0.sorted_list_sum(["dd", "cc", "bb"]) == ["bb", "cc", "dd"]
    # Mixed lengths, all even
    assert module_0.sorted_list_sum(["aaaa", "bb", "cc"]) == ["bb", "cc", "aaaa"]

test_sorted_list_sum()
print("All tests passed")