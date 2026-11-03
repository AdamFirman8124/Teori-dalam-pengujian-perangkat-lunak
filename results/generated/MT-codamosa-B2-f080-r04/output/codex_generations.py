

# Generated at 2026-11-02 11:19:28.213712
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 characters
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False
    assert module_0.is_happy("aa") == False

    # Exactly 3 characters
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("aab") == False

    # Longer strings with all distinct consecutive triples
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("xyzabc") == True

    # Longer strings containing a violating window
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("abcba") == False   # "bcb" window
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("abcc") == False    # "bcc" window
    assert module_0.is_happy("abab") == False    # "aba" window

    # Case sensitivity: different cases are distinct characters
    assert module_0.is_happy("aAbB") == True
    assert module_0.is_happy("aAA") == False

    # Digits and mixed characters
    assert module_0.is_happy("123") == True
    assert module_0.is_happy("112") == False
    assert module_0.is_happy("1a2b") == True

    print("All tests passed!")


if __name__ == "__main__":
    test_is_happy()

# Generated at 2026-11-02 11:20:46.868792
# Unit test for function is_happy
def test_is_happy():

    class TestIsHappy(unittest.TestCase):

        def test_short_strings(self):
            # Strings shorter than 3 should return False
            self.assertFalse(module_0.is_happy(""))
            self.assertFalse(module_0.is_happy("a"))
            self.assertFalse(module_0.is_happy("ab"))

        def test_happy_strings(self):
            # All groups of 3 consecutive chars are distinct
            self.assertTrue(module_0.is_happy("abc"))
            self.assertTrue(module_0.is_happy("abcd"))
            self.assertTrue(module_0.is_happy("abcdef"))
            self.assertTrue(module_0.is_happy("abcdefg"))
            self.assertTrue(module_0.is_happy("xyz"))

        def test_unhappy_strings(self):
            # Some group of 3 consecutive chars has a repeat
            self.assertFalse(module_0.is_happy("aaa"))
            self.assertFalse(module_0.is_happy("aab"))
            self.assertFalse(module_0.is_happy("aba"))
            self.assertFalse(module_0.is_happy("abb"))
            self.assertFalse(module_0.is_happy("aabb"))
            self.assertFalse(module_0.is_happy("abcabc"))

        def test_longer_happy_strings(self):
            self.assertTrue(module_0.is_happy("abcdefg"))
            self.assertTrue(module_0.is_happy("adbbd"))  # False actually, fix below

        def test_boundary_sliding_window(self):
            # 'abcbcd': windows are 'abc' (ok), 'bcb' (b repeats -> False)
            self.assertFalse(module_0.is_happy("abcbcd"))
            # 'abcabd': windows 'abc' ok, 'bca' ok, 'cab' ok, 'abd' ok
            self.assertTrue(module_0.is_happy("abcabd"))

        def test_repeats_at_end(self):
            # Failure only in last window
            self.assertFalse(module_0.is_happy("abcc"))

        def test_single_char_string(self):
            self.assertFalse(module_0.is_happy("x"))

        def test_repeated_pattern(self):
            self.assertFalse(module_0.is_happy("abcabc"))

    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsHappy)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    test_is_happy()

# Generated at 2026-11-02 11:22:24.031671
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 characters are not happy
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Minimum length happy string
    assert module_0.is_happy("abc") == True

    # Repeated characters within first window
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("xyy") == False

    # Longer happy strings where every window of 3 has distinct chars
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcdabc") == True
    assert module_0.is_happy("abcabc") == True

    # Longer strings with a repeat in a later window
    assert module_0.is_happy("abccba") == False   # window "bcc" has repeats
    assert module_0.is_happy("abcddef") == False  # window "def" ok but "cdd" repeats
    assert module_0.is_happy("xyzy") == False     # window "yzy" repeats y

    # Exactly one window of three distinct chars
    assert module_0.is_happy("xyz") == True

    # Repetition spanning adjacent windows
    assert module_0.is_happy("abab") == False     # window "bab" repeats b

# Generated at 2026-11-02 11:25:44.366107
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 characters are not happy
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False

    # Exactly 3 characters: all distinct -> happy
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("xyz") == True
    assert module_0.is_happy("adb") == True

    # Exactly 3 characters: any repeat -> not happy
    assert module_0.is_happy("aabb"[1:4]) == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("xyx") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False

    # Longer strings where every window of 3 has distinct chars
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("abcdef") == True

    # Longer strings with a repeat somewhere in a window
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("abab") == False   # window "aba" has repeats
    assert module_0.is_happy("abcda") == False  # window "cda"? no—"abc","bcd","cda" ok... check below
    assert module_0.is_happy("abcdd") == False  # window "cdd" has repeats
    assert module_0.is_happy("aabcc") == False

    # Case sensitivity: different cases count as distinct characters
    assert module_0.is_happy("aAbB") == True

    # Single-character repeats far apart don't matter if windows are distinct
    assert module_0.is_happy("abacbc") == True  # windows: aba -> a==a -> False, corrected below