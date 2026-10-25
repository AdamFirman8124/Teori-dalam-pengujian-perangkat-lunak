

# Generated at 2026-10-24 04:58:03.423921
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aA1Z!") == ord("A") + ord("Z")
    assert module_0.digitSum("HELLO") == 372

# Generated at 2026-10-24 04:58:08.216493
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("ABC") == 65 + 66 + 67
    assert module_0.digitSum("aB3D!") == 66 + 68

# Generated at 2026-10-24 04:58:15.789410
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc123") == 0
    assert module_0.digitSum("ABC") == 198  # 65 + 66 + 67
    assert module_0.digitSum("aB3D!") == 134  # 66 + 68

# Generated at 2026-10-24 04:58:21.323875
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == 65 + 66 + 67
    assert module_0.digitSum("aA1Z!") == 65 + 90
    assert module_0.digitSum("HELLO") == sum(map(ord, "HELLO"))

# Generated at 2026-10-24 04:58:23.737724
# Unit test for function digitSum

# Generated at 2026-10-24 04:58:26.152778
# Unit test for function digitSum

# Generated at 2026-10-24 04:58:28.567071
# Unit test for function digitSum