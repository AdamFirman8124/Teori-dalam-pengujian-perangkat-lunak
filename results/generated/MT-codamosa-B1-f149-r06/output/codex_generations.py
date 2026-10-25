

# Generated at 2026-10-25 03:57:26.787851
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    values = ["a", "bb", "cccc", "ddd", "ee"]

    result = module_0.sorted_list_sum(values)

    assert result == ["bb", "ee", "cccc"]


def test_sorted_list_sum_with_no_even_length_strings():
    values = ["a", "xyz", "hello"]

    assert module_0.sorted_list_sum(values) == []


def test_sorted_list_sum_with_empty_list():
    assert module_0.sorted_list_sum([]) == []

# Generated at 2026-10-25 03:57:48.905566
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    assert module_0.sorted_list_sum(
        ["apple", "pear", "fig", "banana", "kiwi", "plum"]
    ) == ["kiwi", "pear", "plum", "banana"]

    assert module_0.sorted_list_sum(["aa", "bbbb", "cc", "dddddd"]) == [
        "aa", "cc", "bbbb", "dddddd"
    ]

    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []
    assert module_0.sorted_list_sum([]) == []

# Generated at 2026-10-25 03:58:11.433604
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    assert module_0.sorted_list_sum(["abc", "de", "fghi", "jk", "lmnopq"]) == [
        "de", "jk", "fghi", "lmnopq"
    ]
    assert module_0.sorted_list_sum([]) == []
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []
    assert module_0.sorted_list_sum(["zz", "bbbb", "aa"]) == ["aa", "zz", "bbbb"]

# Generated at 2026-10-25 03:58:27.920791
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

# Generated at 2026-10-25 03:58:44.406330
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