

# Generated at 2026-10-24 19:49:50.227497
# Unit test for function same_chars

# Generated at 2026-10-24 19:49:57.801834
# Unit test for function same_chars
def test_same_chars():assert module_0.same_chars("abc", "cba") is True

# Generated at 2026-10-24 19:50:03.015634
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("", "") is True
    assert module_0.same_chars("a", "") is False
    assert module_0.same_chars("abc", "ABC") is False

# Generated at 2026-10-24 19:50:07.725834
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba")
    assert module_0.same_chars("aabbcc", "abc")
    assert module_0.same_chars("", "")

    assert not module_0.same_chars("abc", "abd")
    assert not module_0.same_chars("", "a")
    assert not module_0.same_chars("abc", "ABC")

# Generated at 2026-10-24 19:50:12.275434
# Unit test for function same_chars
def test_same_chars():
    assert module_0.same_chars("abc", "cba") is True
    assert module_0.same_chars("aabbcc", "abc") is True
    assert module_0.same_chars("", "") is True

    assert module_0.same_chars("abc", "abd") is False
    assert module_0.same_chars("abc", "") is False
    assert module_0.same_chars("a", "A") is False

# Generated at 2026-10-24 19:50:14.696377
# Unit test for function same_chars

# Generated at 2026-10-24 19:50:17.214645
# Unit test for function same_chars

# Generated at 2026-10-24 19:50:19.630797
# Unit test for function same_chars