

# Generated at 2026-10-24 21:57:37.855807
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB3D!") == ord("B") + ord("D")
    assert module_0.digitSum("Z") == ord("Z")

# Generated at 2026-10-24 21:57:43.022268
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc123") == 0
    assert module_0.digitSum("ABC") == 198  # 65 + 66 + 67
    assert module_0.digitSum("aB3Z!") == 156  # 66 + 90

# Generated at 2026-10-24 21:57:48.143629
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc123") == 0
    assert module_0.digitSum("ABC") == 198          # 65 + 66 + 67
    assert module_0.digitSum("aB3Z!") == 156        # 66 + 90
    assert module_0.digitSum("Hello World") == 159  # H (72) + W (87)

# Generated at 2026-10-24 21:57:52.480237
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("A") == ord("A")
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")

# Generated at 2026-10-24 21:57:54.864092
# Unit test for function digitSum

# Generated at 2026-10-24 21:57:57.284441
# Unit test for function digitSum

# Generated at 2026-10-24 21:57:59.702863
# Unit test for function digitSum