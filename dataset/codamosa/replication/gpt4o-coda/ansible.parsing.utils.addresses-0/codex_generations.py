

# Generated at 2024-05-31 18:15:51.455009
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)
    assert parse_address("::1") == ("::1", None)

    # Test cases for valid addresses with ranges

# Generated at 2024-05-31 18:15:55.592235
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)
    
    # Test cases for valid addresses with ranges
    assert parse_address("192.168.1.[1:3]", allow_ranges=True) == ("192.168.1.[1:3]", None)

# Generated at 2024-05-31 18:15:59.309216
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)

    # Test cases for valid addresses with ranges
    assert parse_address("192.168.1.[1:3]", allow_ranges=True) == ("192.168.1.[1:3]", None)

# Generated at 2024-05-31 18:16:03.032225
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)

    # Test cases for valid addresses with ranges
    assert parse_address("192.168.1.[1:3]", allow_ranges=True) == ("192.168.1.[1:3]", None)

# Generated at 2024-05-31 18:16:08.429803
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)
    
    # Test cases for valid addresses with ranges
    assert parse_address("192.168.1.[1:3]", allow_ranges=True) == ("192.168.1.[1:3]", None)

# Generated at 2024-05-31 18:16:12.024466
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)
    assert parse_address("::1") == ("::1", None)

    # Test cases for valid addresses with ranges

# Generated at 2024-05-31 18:16:16.071485
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[example.com]:80") == ("example.com", 80)
    assert parse_address("::1") == ("::1", None)
    assert parse_address("[::1]:80") == ("::1", 80)

    # Test cases for valid addresses with ranges

# Generated at 2024-05-31 18:16:20.089098
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)
    
    # Test cases for valid addresses with ranges
    assert parse_address("192.168.1.[1:3]", allow_ranges=True) == ("192.168.1.[1:3]", None)

# Generated at 2024-05-31 18:16:23.277531
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)
    
    # Test cases for valid addresses with ranges
    assert parse_address("192.168.1.[1:3]", allow_ranges=True) == ("192.168.1.[1:3]", None)

# Generated at 2024-05-31 18:16:27.478888
# Unit test for function parse_address
def test_parse_address():    # Test cases for valid addresses without ranges
    assert parse_address("192.168.1.1") == ("192.168.1.1", None)
    assert parse_address("192.168.1.1:8080") == ("192.168.1.1", 8080)
    assert parse_address("[192.168.1.1]:8080") == ("192.168.1.1", 8080)
    assert parse_address("example.com") == ("example.com", None)
    assert parse_address("example.com:80") == ("example.com", 80)
    assert parse_address("[::1]:80") == ("::1", 80)
    
    # Test cases for valid addresses with ranges
    assert parse_address("192.168.1.[1:3]", allow_ranges=True) == ("192.168.1.[1:3]", None)