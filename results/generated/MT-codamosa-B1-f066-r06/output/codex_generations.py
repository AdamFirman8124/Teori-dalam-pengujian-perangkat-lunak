

# Generated at 2026-10-24 22:46:28.001702
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("ABC") == 65 + 66 + 67
    assert module_0.digitSum("aBcD") == 66 + 68
    assert module_0.digitSum("A1!Z") == 65 + 90

# Generated at 2026-10-24 22:46:32.740547
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")
    assert module_0.digitSum("Z") == 90

# Generated at 2026-10-24 22:46:38.638858
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")
    assert module_0.digitSum("Z") == 90

# Generated at 2026-10-24 22:46:42.836888
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")
    assert module_0.digitSum("12345") == 0

# Generated at 2026-10-24 22:46:47.854490
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")
    assert module_0.digitSum("Z") == 90