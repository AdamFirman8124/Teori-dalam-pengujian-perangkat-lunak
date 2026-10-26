

# Generated at 2026-10-25 10:44:53.222922
# Unit test for function is_palindrome
def test_is_palindrome():
    # --- should be True ---
    assert module_0.is_palindrome("") is True            # empty string
    assert module_0.is_palindrome("a") is True           # single char
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("racecar") is True     # odd length
    assert module_0.is_palindrome("abba") is True        # even length
    assert module_0.is_palindrome("abcddcba") is True

    # --- should be False ---
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("abc") is False        # mismatch at i=0 vs i=2
    assert module_0.is_palindrome("abca") is False       # mismatch at i=0 vs i=3
    assert module_0.is_palindrome("abcda") is False      # mismatch only in the middle
    assert module_0.is_palindrome("Racecar") is False    # case-sensitive by design

    # --- invalid input ---
    with pytest.raises(TypeError):
        module_0.is_palindrome(None)

# Generated at 2026-10-25 10:44:54.560339
# Unit test for function is_palindrome
def test_is_palindrome():
    # --- should be True ---
    assert module_0.is_palindrome("") is True            # empty string
    assert module_0.is_palindrome("a") is True           # single char
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("racecar") is True     # odd length
    assert module_0.is_palindrome("abba") is True        # even length
    assert module_0.is_palindrome("abcddcba") is True

    # --- should be False ---
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("abc") is False        # mismatch at i=0 vs i=2
    assert module_0.is_palindrome("abca") is False       # mismatch at i=0 vs i=3
    assert module_0.is_palindrome("abcda") is False      # mismatch only in the middle
    assert module_0.is_palindrome("Racecar") is False    # case-sensitive by design

    # --- invalid input ---
    with pytest.raises(TypeError):
        module_0.is_palindrome(None)

# Generated at 2026-10-25 10:44:55.906384
# Unit test for function is_palindrome
def test_is_palindrome():
    # --- should be True ---
    assert module_0.is_palindrome("") is True            # empty string
    assert module_0.is_palindrome("a") is True           # single char
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("racecar") is True     # odd length
    assert module_0.is_palindrome("abba") is True        # even length
    assert module_0.is_palindrome("abcddcba") is True

    # --- should be False ---
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("abc") is False        # mismatch at i=0 vs i=2
    assert module_0.is_palindrome("abca") is False       # mismatch at i=0 vs i=3
    assert module_0.is_palindrome("abcda") is False      # mismatch only in the middle
    assert module_0.is_palindrome("Racecar") is False    # case-sensitive by design

    # --- invalid input ---
    with pytest.raises(TypeError):
        module_0.is_palindrome(None)

# Generated at 2026-10-25 10:44:57.371591
# Unit test for function is_palindrome
def test_is_palindrome():
    # --- should be True ---
    assert module_0.is_palindrome("") is True            # empty string
    assert module_0.is_palindrome("a") is True           # single char
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("racecar") is True     # odd length
    assert module_0.is_palindrome("abba") is True        # even length
    assert module_0.is_palindrome("abcddcba") is True

    # --- should be False ---
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("abc") is False        # mismatch at i=0 vs i=2
    assert module_0.is_palindrome("abca") is False       # mismatch at i=0 vs i=3
    assert module_0.is_palindrome("abcda") is False      # mismatch only in the middle
    assert module_0.is_palindrome("Racecar") is False    # case-sensitive by design

    # --- invalid input ---
    with pytest.raises(TypeError):
        module_0.is_palindrome(None)

# Generated at 2026-10-25 10:44:58.804347
# Unit test for function is_palindrome
def test_is_palindrome():
    # --- should be True ---
    assert module_0.is_palindrome("") is True            # empty string
    assert module_0.is_palindrome("a") is True           # single char
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("racecar") is True     # odd length
    assert module_0.is_palindrome("abba") is True        # even length
    assert module_0.is_palindrome("abcddcba") is True

    # --- should be False ---
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("abc") is False        # mismatch at i=0 vs i=2
    assert module_0.is_palindrome("abca") is False       # mismatch at i=0 vs i=3
    assert module_0.is_palindrome("abcda") is False      # mismatch only in the middle
    assert module_0.is_palindrome("Racecar") is False    # case-sensitive by design

    # --- invalid input ---
    with pytest.raises(TypeError):
        module_0.is_palindrome(None)