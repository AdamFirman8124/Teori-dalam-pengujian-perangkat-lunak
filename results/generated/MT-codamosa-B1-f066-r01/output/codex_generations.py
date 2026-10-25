

# Generated at 2026-10-24 20:41:11.389241
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == 198       # 65 + 66 + 67
    assert module_0.digitSum("aB3C!") == 133     # 66 + 67
    assert module_0.digitSum("Z") == 90

# Generated at 2026-10-24 20:41:15.686004
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("ABC") == 65 + 66 + 67
    assert module_0.digitSum("aB3C!") == 66 + 67

# Generated at 2026-10-24 20:41:20.920346
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == 198       # 65 + 66 + 67
    assert module_0.digitSum("aB3Z!") == 156     # 66 + 90
    assert module_0.digitSum("Hello World") == 159  # H (72) + W (87)

# Generated at 2026-10-24 20:41:24.964728
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB3D!") == ord("B") + ord("D")
    assert module_0.digitSum("Z") == 90

# Generated at 2026-10-24 20:41:33.812271
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == 198       # 65 + 66 + 67
    assert module_0.digitSum("aB3Z!") == 156     # 66 + 90
    assert module_0.digitSum("Hello World") == 159  # H (72) + W (87)