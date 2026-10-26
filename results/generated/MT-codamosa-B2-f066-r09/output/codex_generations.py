

# Generated at 2026-10-25 09:52:21.078627
# Unit test for function digitSum
def test_digitSum():
    # empty string
    assert module_0.digitSum("") == 0
    # no uppercase -> ignored
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("123!@# ") == 0
    # single uppercase
    assert module_0.digitSum("Z") == 90  # ord('Z')
    assert module_0.digitSum("A") == 65  # ord('A')
    # all uppercase
    assert module_0.digitSum("ABC") == 65 + 66 + 67  # 198
    assert module_0.digitSum("HELLO") == 72 + 69 + 76 + 76 + 79  # 372
    # mixed case
    assert module_0.digitSum("aBcDe") == 66 + 68  # B + D = 134
    # uppercase mixed with digits/symbols/spaces
    assert module_0.digitSum("A1b2C3") == 65 + 67  # 132
    assert module_0.digitSum("aB cD") == 66 + 68  # 134

# Generated at 2026-10-25 09:52:25.788722
# Unit test for function digitSum
def test_digitSum():
    # empty string
    assert module_0.digitSum("") == 0
    # no uppercase -> ignored
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("123!@# ") == 0
    # single uppercase
    assert module_0.digitSum("Z") == 90  # ord('Z')
    assert module_0.digitSum("A") == 65  # ord('A')
    # all uppercase
    assert module_0.digitSum("ABC") == 65 + 66 + 67  # 198
    assert module_0.digitSum("HELLO") == 72 + 69 + 76 + 76 + 79  # 372
    # mixed case
    assert module_0.digitSum("aBcDe") == 66 + 68  # B + D = 134
    # uppercase mixed with digits/symbols/spaces
    assert module_0.digitSum("A1b2C3") == 65 + 67  # 132
    assert module_0.digitSum("aB cD") == 66 + 68  # 134

# Generated at 2026-10-25 09:52:27.428280
# Unit test for function digitSum
def test_digitSum():
    # empty string
    assert module_0.digitSum("") == 0
    # no uppercase -> ignored
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("123!@# ") == 0
    # single uppercase
    assert module_0.digitSum("Z") == 90  # ord('Z')
    assert module_0.digitSum("A") == 65  # ord('A')
    # all uppercase
    assert module_0.digitSum("ABC") == 65 + 66 + 67  # 198
    assert module_0.digitSum("HELLO") == 72 + 69 + 76 + 76 + 79  # 372
    # mixed case
    assert module_0.digitSum("aBcDe") == 66 + 68  # B + D = 134
    # uppercase mixed with digits/symbols/spaces
    assert module_0.digitSum("A1b2C3") == 65 + 67  # 132
    assert module_0.digitSum("aB cD") == 66 + 68  # 134

# Generated at 2026-10-25 09:52:36.233142
# Unit test for function digitSum
def test_digitSum():
    # empty string
    assert module_0.digitSum("") == 0
    # no uppercase -> ignored
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("123!@# ") == 0
    # single uppercase
    assert module_0.digitSum("Z") == 90  # ord('Z')
    assert module_0.digitSum("A") == 65  # ord('A')
    # all uppercase
    assert module_0.digitSum("ABC") == 65 + 66 + 67  # 198
    assert module_0.digitSum("HELLO") == 72 + 69 + 76 + 76 + 79  # 372
    # mixed case
    assert module_0.digitSum("aBcDe") == 66 + 68  # B + D = 134
    # uppercase mixed with digits/symbols/spaces
    assert module_0.digitSum("A1b2C3") == 65 + 67  # 132
    assert module_0.digitSum("aB cD") == 66 + 68  # 134

# Generated at 2026-10-25 09:52:39.002809
# Unit test for function digitSum
def test_digitSum():
    # empty string
    assert module_0.digitSum("") == 0
    # no uppercase -> ignored
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("123!@# ") == 0
    # single uppercase
    assert module_0.digitSum("Z") == 90  # ord('Z')
    assert module_0.digitSum("A") == 65  # ord('A')
    # all uppercase
    assert module_0.digitSum("ABC") == 65 + 66 + 67  # 198
    assert module_0.digitSum("HELLO") == 72 + 69 + 76 + 76 + 79  # 372
    # mixed case
    assert module_0.digitSum("aBcDe") == 66 + 68  # B + D = 134
    # uppercase mixed with digits/symbols/spaces
    assert module_0.digitSum("A1b2C3") == 65 + 67  # 132
    assert module_0.digitSum("aB cD") == 66 + 68  # 134