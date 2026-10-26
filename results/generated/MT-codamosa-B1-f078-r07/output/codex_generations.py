

# Generated at 2026-10-25 06:17:21.519614
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:23.939547
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:26.356442
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:28.773310
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:31.192075
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:33.606436
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:36.023876
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:38.437923
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:40.880096
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:43.291845
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:45.705544
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:48.131588
# Unit test for function hex_key

# Generated at 2026-10-25 06:17:55.128284
# Unit test for function hex_key
def test_hex_key():
    # Test with all prime hex digits
    assert module_0.hex_key("2357BD") == 6
    # Test with no prime hex digits
    assert module_0.hex_key("014689ACEF") == 0
    # Test example from problem statements
    assert module_0.hex_key("AB") == 1
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("2020") == 2
    assert module_0.hex_key("123456789ABCDEF0") == 6
    # Test with repeated prime digits
    assert module_0.hex_key("222222") == 6
    # Test with mixed case handling (hex is typically uppercase)
    assert module_0.hex_key("FFFFFFFF") == 2  # F is not prime, but D... none here
    # Test empty string
    assert module_0.hex_key("") == 0
    # Test single character cases
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("4") == 0
    # Test with 'B' and 'D' primes specifically
    assert module_0.hex_key("BDBD") == 4
    assert module_0.hex_key("202020") == 6