

# Generated at 2026-10-24 11:23:17.396636
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

# Generated at 2026-10-24 11:23:34.273425
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

# Generated at 2026-10-24 11:23:50.964188
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

# Generated at 2026-10-24 11:24:12.775917
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert module_0.sorted_list_sum([]) == []
    assert module_0.sorted_list_sum(["abc"]) == []
    assert module_0.sorted_list_sum(["a", "bb", "ccc", "dddd"]) == ["bb", "dddd"]
    # equal lengths -> alphabetical order
    assert module_0.sorted_list_sum(["cd", "ab", "ef"]) == ["ab", "cd", "ef"]
    assert module_0.sorted_list_sum(["xy", "ab", "ba"]) == ["ab", "ba", "xy"]
    print("All tests passed.")

test_sorted_list_sum()

# Generated at 2026-10-24 11:24:15.196376
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 11:24:17.613688
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 11:24:20.033051
# Unit test for function sorted_list_sum