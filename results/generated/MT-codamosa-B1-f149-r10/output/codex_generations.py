

# Generated at 2026-10-24 19:37:46.612582
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:37:49.028465
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:37:51.446211
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:37:53.861674
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:37:56.432574
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:37:58.849457
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:38:01.266714
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:38:03.682188
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:38:06.101185
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:38:12.809546
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert module_0.sorted_list_sum(["abc", "ab", "abcd", "a"]) == ["ab", "abcd"]
    assert module_0.sorted_list_sum(["a", "b", "c"]) == []
    assert module_0.sorted_list_sum([]) == []
    assert module_0.sorted_list_sum(["dd", "bb", "cc"]) == ["bb", "cc", "dd"]
    assert module_0.sorted_list_sum(["aaaa", "aa", "ab"]) == ["ab", "aa", "aaaa"]
    assert module_0.sorted_list_sum(["hello", "world"]) == []
    assert module_0.sorted_list_sum(["ab", "cd", "ef", "ghij"]) == ["ab", "cd", "ef", "ghij"]
    assert module_0.sorted_list_sum(["xy", "xyz", "xyzz", "x"]) == ["xy", "xyzz"]

test_sorted_list_sum()
print("All tests passed!")

# Generated at 2026-10-24 19:38:14.242605
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # empty list
    assert module_0.sorted_list_sum([]) == []

    # filters odd lengths
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["a", "b", "c"]) == []
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]

    # sorted by length ascending
    assert module_0.sorted_list_sum(["aaaa", "a", "aa", "aaa"]) == ["aa", "aaaa"]
    assert module_0.sorted_list_sum(["AI", "asdf", "school"]) == ["AI", "asdf", "school"]

    # same length -> sorted alphabetically
    assert module_0.sorted_list_sum(["ab", "aa", "cd", "a"]) == ["aa", "ab", "cd"]
    assert module_0.sorted_list_sum(["dc", "ba", "ab"]) == ["ab", "ba", "dc"]