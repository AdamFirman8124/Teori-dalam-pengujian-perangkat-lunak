

# Generated at 2026-10-25 14:20:47.566059
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("hello", "eo") == ("hll", False)
    assert module_0.reverse_delete("aaaa", "a") == ("", True)
    assert module_0.reverse_delete("", "abc") == ("", True)

# Generated at 2026-10-25 14:20:52.685194
# Unit test for function reverse_delete
def test_reverse_delete():
    # Basic cases: (result_string, is_palindrome)
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("abcdedcba", "abcdedcba") == ("", True)

    # Delete nothing
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("hello", "xyz") == ("hello", False)

    # Delete everything
    assert module_0.reverse_delete("aaaa", "a") == ("", True)

    # Case sensitivity: 'A' != 'a'
    assert module_0.reverse_delete("aA", "a") == ("A", True)
    assert module_0.reverse_delete("aA", "A") == ("a", True)

    # Empty string input
    assert module_0.reverse_delete("", "abc") == ("", True)

    # Result is palindrome only after deletion
    assert module_0.reverse_delete("abca", "b") == ("aca", True)
    assert module_0.reverse_delete("abca", "c") == ("aba", True)

    print("All tests passed!")


test_reverse_delete()

# Generated at 2026-10-25 14:21:00.710469
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("abc", "abc") == ("", True)

# Generated at 2026-10-25 14:21:08.455674
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("hello", "helo") == ("", True)
    assert module_0.reverse_delete("", "abc") == ("", True)

# Generated at 2026-10-25 14:21:17.173373
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("aabbcc", "bc") == ("aa", True)
    assert module_0.reverse_delete("abc", "abc") == ("", True)
    assert module_0.reverse_delete("", "abc") == ("", True)
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("hello", "x") == ("hello", False)