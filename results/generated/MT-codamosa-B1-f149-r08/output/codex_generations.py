

# Generated at 2026-10-25 10:18:35.882622
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

# Generated at 2026-10-25 10:18:37.269155
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

# Generated at 2026-10-25 10:18:39.687668
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:18:42.268035
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:18:44.669046
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:18:47.293891
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:18:54.736739
# Unit test for function sorted_list_sum
def test_sorted_list_sum():assert module_0.sorted_list_sum(["a", "ab", "abc", "abcd"]) == ["ab", "abcd"]

# Generated at 2026-10-25 10:18:59.399722
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