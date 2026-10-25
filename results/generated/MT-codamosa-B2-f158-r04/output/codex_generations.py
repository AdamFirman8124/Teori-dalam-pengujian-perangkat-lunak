

# Generated at 2026-10-24 12:23:27.282499
# Unit test for function find_max

# Generated at 2026-10-24 12:23:29.700694
# Unit test for function find_max

# Generated at 2026-10-24 12:23:32.110400
# Unit test for function find_max

# Generated at 2026-10-24 12:23:34.528114
# Unit test for function find_max

# Generated at 2026-10-24 12:23:36.944813
# Unit test for function find_max

# Generated at 2026-10-24 12:23:39.361322
# Unit test for function find_max

# Generated at 2026-10-24 12:23:41.774126
# Unit test for function find_max

# Generated at 2026-10-24 12:23:44.187672
# Unit test for function find_max

# Generated at 2026-10-24 12:23:46.601156
# Unit test for function find_max

# Generated at 2026-10-24 12:23:49.015771
# Unit test for function find_max

# Generated at 2026-10-24 12:23:51.424591
# Unit test for function find_max

# Generated at 2026-10-24 12:23:53.837056
# Unit test for function find_max

# Generated at 2026-10-24 12:24:01.198589
# Unit test for function find_max
def test_find_max():
    # Basic cases: unique character count decides the winner
    assert module_0.find_max(["name", "of", "string"]) == "string"
    assert module_0.find_max(["name", "enam", "game"]) == "enam"
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Tie on unique count -> lexicographically smallest wins
    assert module_0.find_max(["abc", "cba", "bac"]) == "abc"
    assert module_0.find_max(["ab", "cd", "ef"]) == "ab"

    # Single element
    assert module_0.find_max(["hello"]) == "hello"

    # Empty string element
    assert module_0.find_max(["", "a"]) == "a"

    # Duplicates of characters reduce unique count
    assert module_0.find_max(["aabb", "ab", "zz"]) == "ab"

    # Mixed lengths and ties
    assert module_0.find_max(["apple", "banana", "cherry"]) == "banana"

    print("All tests passed!")

if __name__ == "__main__":
    test_find_max()