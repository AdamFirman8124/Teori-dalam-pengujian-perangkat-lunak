

# Generated at 2026-10-25 06:56:08.517437
# Unit test for function hex_key
def test_hex_key():
    # empty and non-prime cases
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("0000") == 0
    assert module_0.hex_key("0000FFFF") == 0
    assert module_0.hex_key("148AEF") == 0

    # single prime digits: 2,3,5,7,B=11,D=13
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1

    # mixed cases
    assert module_0.hex_key("AB") == 1 # A=10 no, B=11 yes
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("123456789ABCDEF") == 6

    # all prime digits
    assert module_0.hex_key("2357BD") == 6
    assert module_0.hex_key("2222") == 4

# Generated at 2026-10-25 06:56:09.983904
# Unit test for function hex_key
def test_hex_key():
    # empty and non-prime cases
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("0000") == 0
    assert module_0.hex_key("0000FFFF") == 0
    assert module_0.hex_key("148AEF") == 0

    # single prime digits: 2,3,5,7,B=11,D=13
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1

    # mixed cases
    assert module_0.hex_key("AB") == 1 # A=10 no, B=11 yes
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("123456789ABCDEF") == 6

    # all prime digits
    assert module_0.hex_key("2357BD") == 6
    assert module_0.hex_key("2222") == 4

# Generated at 2026-10-25 06:56:11.501880
# Unit test for function hex_key
def test_hex_key():
    # empty and non-prime cases
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("0000") == 0
    assert module_0.hex_key("0000FFFF") == 0
    assert module_0.hex_key("148AEF") == 0

    # single prime digits: 2,3,5,7,B=11,D=13
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1

    # mixed cases
    assert module_0.hex_key("AB") == 1 # A=10 no, B=11 yes
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("123456789ABCDEF") == 6

    # all prime digits
    assert module_0.hex_key("2357BD") == 6
    assert module_0.hex_key("2222") == 4

# Generated at 2026-10-25 06:56:14.185508
# Unit test for function hex_key

# Generated at 2026-10-25 06:56:16.890566
# Unit test for function hex_key

# Generated at 2026-10-25 06:56:19.315551
# Unit test for function hex_key

# Generated at 2026-10-25 06:56:21.723480
# Unit test for function hex_key

# Generated at 2026-10-25 06:56:24.137918
# Unit test for function hex_key

# Generated at 2026-10-25 06:56:26.554746
# Unit test for function hex_key