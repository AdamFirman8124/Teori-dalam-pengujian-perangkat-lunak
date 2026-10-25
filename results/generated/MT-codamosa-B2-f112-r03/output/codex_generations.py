

# Generated at 2026-10-25 01:02:14.452152
# Unit test for function reverse_delete
def test_reverse_delete():
    # Delete chars, result is palindrome
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcd", "x") == ("abcd", False)   # nothing deleted
    assert module_0.reverse_delete("abcba", "x") == ("abcba", True)  # already palindrome
    assert module_0.reverse_delete("abccba", "a") == ("bccb", True)  # becomes palindrome
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("hello", "l") == ("heo", False)
    assert module_0.reverse_delete("", "abc") == ("", True)          # empty is palindrome
    assert module_0.reverse_delete("aaa", "a") == ("", True)         # all chars deleted
    assert module_0.reverse_delete("ab", "ab") == ("", True)
    print("All tests passed.")

test_reverse_delete()

# Generated at 2026-10-25 01:02:17.103876
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:19.530798
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:21.946884
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:24.361923
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:26.776993
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:29.191946
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:31.607220
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:34.022438
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:36.436327
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:38.850872
# Unit test for function reverse_delete

# Generated at 2026-10-25 01:02:42.410364
# Unit test for function reverse_delete
def test_reverse_delete():assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)