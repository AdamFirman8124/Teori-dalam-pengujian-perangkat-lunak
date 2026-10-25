

# Generated at 2026-10-25 04:40:29.178610
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("a", "a") == ("", True)
    assert module_0.reverse_delete("", "abc") == ("", True)
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("hello", "helo") == ("", True)

# Generated at 2026-10-25 04:40:35.061098
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("hello", "helo") == ("", True)


test_reverse_delete()

# Generated at 2026-10-25 04:40:40.181664
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("level", "") == ("level", True)
    assert module_0.reverse_delete("hello", "helo") == ("", True)
    assert module_0.reverse_delete("", "abc") == ("", True)
    assert module_0.reverse_delete("aabbcc", "b") == ("aacc", True)

# Generated at 2026-10-25 04:40:50.011028
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdef", "b") == ("acdef", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("abcba", "") == ("abcba", True)
    assert module_0.reverse_delete("", "abc") == ("", True)
    assert module_0.reverse_delete("aaaa", "a") == ("", True)
    assert module_0.reverse_delete("racecar", "e") == ("raccar", True)

# Generated at 2026-10-25 04:40:54.832248
# Unit test for function reverse_delete
def test_reverse_delete():
    assert module_0.reverse_delete("abcde", "ae") == ("bcd", False)
    assert module_0.reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert module_0.reverse_delete("racecar", "") == ("racecar", True)
    assert module_0.reverse_delete("hello", "helo") == ("", True)
    assert module_0.reverse_delete("", "abc") == ("", True)
    assert module_0.reverse_delete("aabbcc", "ac") == ("bb", True)