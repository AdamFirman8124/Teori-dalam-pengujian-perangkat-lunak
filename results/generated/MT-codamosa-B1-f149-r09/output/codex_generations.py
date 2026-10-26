

# Generated at 2026-10-25 10:00:18.558453
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:20.972038
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:23.385710
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:25.798847
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:28.282771
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:30.666942
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:33.075768
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:35.491799
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:37.906840
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:40.320928
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:42.734935
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:45.152947
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:47.568657
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:49.990140
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:52.402063
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:54.814951
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:57.229612
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:00:59.645987
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:01:02.061202
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:01:04.473670
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:01:06.890160
# Unit test for function sorted_list_sum

# Generated at 2026-10-25 10:01:11.632982
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

# Generated at 2026-10-25 10:01:27.807280
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

# Generated at 2026-10-25 10:01:30.364311
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

# Generated at 2026-10-25 10:01:33.734040
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

# Generated at 2026-10-25 10:01:37.726935
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

# Generated at 2026-10-25 10:01:40.287176
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

# Generated at 2026-10-25 10:01:47.109367
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

# Generated at 2026-10-25 10:01:49.092795
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