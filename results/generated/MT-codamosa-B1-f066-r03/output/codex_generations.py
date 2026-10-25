

# Generated at 2026-10-24 08:00:57.175281
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("ABC") == 198
    assert module_0.digitSum("aB3D!") == 134
    assert module_0.digitSum("HELLO") == 372

# Generated at 2026-10-24 08:01:03.852630
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == 198       # 65 + 66 + 67
    assert module_0.digitSum("aB1C!") == 133     # 66 + 67
    assert module_0.digitSum("Z") == 90

# Generated at 2026-10-24 08:01:09.153219
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc123") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")
    assert module_0.digitSum("Z") == ord("Z")

# Generated at 2026-10-24 08:01:13.304149
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")
    assert module_0.digitSum("Z") == 90