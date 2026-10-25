

# Generated at 2026-10-24 19:45:27.344118
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:45:29.758617
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:45:32.179586
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:45:34.596990
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:45:37.014102
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:45:39.431532
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 19:45:41.976660
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

# Generated at 2026-10-24 19:45:43.333720
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

# Generated at 2026-10-24 19:45:44.753227
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