

# Generated at 2026-10-24 07:44:24.492465
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:26.909125
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:29.428955
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:31.928661
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:34.342208
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:36.927473
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:39.348459
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:41.763607
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:44.180925
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:46.595487
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:49.014330
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:51.428471
# Unit test for function is_happy

# Generated at 2026-10-24 07:44:52.816325
# Unit test for function is_happy
def test_is_happy():
    # valid
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abca") is True
    assert module_0.is_happy("abcd") is True

    # too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("ab") is False

    # duplicate adjacent
    assert module_0.is_happy("aab") is False
    assert module_0.is_happy("abb") is False

    # duplicate at distance 2
    assert module_0.is_happy("aba") is False
    assert module_0.is_happy("abcb") is False