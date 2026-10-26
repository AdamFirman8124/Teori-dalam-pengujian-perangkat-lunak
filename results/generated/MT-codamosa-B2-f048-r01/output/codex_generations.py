

# Generated at 2026-10-25 08:45:19.811655
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

# Generated at 2026-10-25 08:45:22.229399
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:24.657299
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:27.074378
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:29.492715
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:31.908652
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:34.326614
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:36.746857
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:39.165230
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:41.582517
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:43.999649
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:46.418308
# Unit test for function is_palindrome

# Generated at 2026-10-25 08:45:48.834592
# Unit test for function is_palindrome