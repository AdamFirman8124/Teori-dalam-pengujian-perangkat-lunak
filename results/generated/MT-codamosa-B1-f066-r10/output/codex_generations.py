

# Generated at 2026-10-25 03:37:45.092852
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")

# Generated at 2026-10-25 03:37:57.782922
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aB1C!") == ord("B") + ord("C")
    assert module_0.digitSum("Hello World") == ord("H") + ord("W")

# Generated at 2026-10-25 03:38:12.120286
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("12345") == 15
    assert module_0.digitSum("a1b2c3") == 6
    assert module_0.digitSum("hello") == 0
    assert module_0.digitSum("A9B1") == 10

# Generated at 2026-10-25 03:38:23.486186
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("aBcD") == ord("B") + ord("D")
    assert module_0.digitSum("A1!") == ord("A")

# Generated at 2026-10-25 03:38:36.014771
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("aB3C!") == ord("B") + ord("C")
    assert module_0.digitSum("Hello World") == ord("H") + ord("W")