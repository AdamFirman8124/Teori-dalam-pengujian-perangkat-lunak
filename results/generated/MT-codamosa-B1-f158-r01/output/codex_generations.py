

# Generated at 2026-10-24 07:05:08.264614
# Unit test for function find_max
def test_find_max():
    # Word with the most distinct characters
    assert module_0.find_max(["apple", "banana", "pear"]) == "pear"

    # Repeated characters count only once
    assert module_0.find_max(["aaaa", "abc", "bbbbb"]) == "abc"

    # Ties are resolved lexicographically
    assert module_0.find_max(["bca", "abc", "cab"]) == "abc"

    # Single-word input
    assert module_0.find_max(["hello"]) == "hello"

# Generated at 2026-10-24 07:05:10.681444
# Unit test for function find_max

# Generated at 2026-10-24 07:05:13.097811
# Unit test for function find_max

# Generated at 2026-10-24 07:05:15.600845
# Unit test for function find_max

# Generated at 2026-10-24 07:05:21.274459
# Unit test for function find_max
def test_find_max():return min(words, key=lambda x: (-len(set(x)), x))

# Generated at 2026-10-24 07:05:26.387631
# Unit test for function find_max
def test_find_max():
    assert module_0.find_max(["apple", "banana", "orange"]) == "orange"
    assert module_0.find_max(["abc", "bca", "cab"]) == "abc"  # tie: lexicographically smallest
    assert module_0.find_max(["aaaa", "aabc", "abcd"]) == "abcd"
    assert module_0.find_max(["hello"]) == "hello"

# Generated at 2026-10-24 07:05:32.941698
# Unit test for function find_max
def test_find_max():
    assert module_0.find_max(["abc", "aaaa", "bcdef", "hello"]) == "bcdef"
    assert module_0.find_max(["banana", "abc", "cab"]) == "abc"  # Tie: alphabetical order
    assert module_0.find_max(["aabbcc", "abcd", "zzzzz"]) == "abcd"
    assert module_0.find_max(["python"]) == "python"