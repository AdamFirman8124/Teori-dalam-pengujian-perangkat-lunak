

# Generated at 2026-10-24 04:21:17.800942
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc123") == 0
    assert module_0.digitSum("ABC") == 65 + 66 + 67
    assert module_0.digitSum("aB3D!") == 66 + 68
    assert module_0.digitSum("Z") == 90

# Generated at 2026-10-24 04:21:22.081180
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB3D!") == ord("B") + ord("D")
    assert module_0.digitSum("Z") == 90

# Generated at 2026-10-24 04:21:26.405194
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB3Z!") == ord("B") + ord("Z")
    assert module_0.digitSum("HELLO") == sum(map(ord, "HELLO"))

# Generated at 2026-10-24 04:21:31.111313
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")
    assert module_0.digitSum("Z") == 90

# Generated at 2026-10-24 04:21:36.334709
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == 198       # 65 + 66 + 67
    assert module_0.digitSum("aB3Z!") == 156     # 66 + 90
    assert module_0.digitSum("AA") == 130