

# Generated at 2026-10-24 04:47:17.565109
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Odd-length strings removed
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    # Even-length strings kept, sorted by length
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Mixed lengths: shorter even-length first
    assert module_0.sorted_list_sum(["abc", "abcd", "ab"]) == ["ab", "abcd"]

    # Ties in length fall back to alphabetical order
    assert module_0.sorted_list_sum(["bb", "aa", "cc"]) == ["aa", "bb", "cc"]

    # Edge cases
    assert module_0.sorted_list_sum([]) == []
    assert module_0.sorted_list_sum(["a", "bbb", "ccccc"]) == []  # all odd-length

    print("All tests passed!")


test_sorted_list_sum()

# Generated at 2026-10-24 04:47:20.085663
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:22.496773
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:24.993782
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:27.406932
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:29.823385
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:32.234937
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:34.650440
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:37.066384
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:39.478628
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:41.891589
# Unit test for function sorted_list_sum

# Generated at 2026-10-24 04:47:47.201779
# Unit test for function sorted_list_sum
def test_sorted_list_sum():assert module_0.sorted_list_sum(["aaa", "bb", "c", "dddd", "aa", "ee"]) == ["aa", "bb", "ee", "dddd"]