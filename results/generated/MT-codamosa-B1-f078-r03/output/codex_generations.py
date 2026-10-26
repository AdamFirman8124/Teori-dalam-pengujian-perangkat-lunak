

# Generated at 2026-10-25 11:13:36.489374
# Unit test for function hex_key
def test_hex_key():
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("1") == 0
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("2357BD") == 6
    assert module_0.hex_key("0123456789ABCDEF") == 6
    assert module_0.hex_key("CAFEBABE") == 2
    assert module_0.hex_key("DEADBEEF") == 3
    assert module_0.hex_key("222BBB") == 6

# Generated at 2026-10-25 11:13:42.716206
# Unit test for function hex_key
def test_hex_key():
    assert module_0.hex_key("AB") == 1
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("1234567890ABCDEF") == 6
    assert module_0.hex_key("FACE") == 0
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("2233BBDD") == 8

# Generated at 2026-10-25 11:13:51.112768
# Unit test for function hex_key
def test_hex_key():
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("FACE") == 0
    assert module_0.hex_key("B0D2") == 3
    assert module_0.hex_key("123456789ABCDEF") == 6
    assert module_0.hex_key("222BBB") == 6

# Generated at 2026-10-25 11:13:55.809451
# Unit test for function hex_key
def test_hex_key():
    assert module_0.hex_key("AB") == 1
    assert module_0.hex_key("ABCDEF") == 2
    assert module_0.hex_key("1234567890") == 4
    assert module_0.hex_key("BDBD") == 4
    assert module_0.hex_key("014689ACEF") == 0
    assert module_0.hex_key("") == 0

# Generated at 2026-10-25 11:14:01.968693
# Unit test for function hex_key
def test_hex_key():
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("1234567890") == 4
    assert module_0.hex_key("ABCDEF") == 2
    assert module_0.hex_key("2357BD") == 6
    assert module_0.hex_key("AAAA") == 0
    assert module_0.hex_key("22BDF") == 4