

# Generated at 2026-10-24 23:18:52.112094
# Unit test for function is_happy

# Generated at 2026-10-24 23:18:54.531588
# Unit test for function is_happy

# Generated at 2026-10-24 23:18:56.948463
# Unit test for function is_happy

# Generated at 2026-10-24 23:18:59.536993
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:01.951664
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:04.367862
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:06.783179
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:09.228108
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:11.649742
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:14.066959
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:16.489430
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:18.903467
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:21.322857
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:23.739872
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:26.156719
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:28.579147
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:30.994210
# Unit test for function is_happy

# Generated at 2026-10-24 23:19:40.395576
# Unit test for function is_happy
def test_is_happy():assert module_0.is_happy("abc") is True

# Generated at 2026-10-24 23:19:41.724696
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 23:19:43.064500
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 23:19:44.399180
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 23:19:45.724901
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 23:19:47.050344
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 23:19:48.373662
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 23:19:49.695394
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 23:19:51.024666
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 23:19:52.358667
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails