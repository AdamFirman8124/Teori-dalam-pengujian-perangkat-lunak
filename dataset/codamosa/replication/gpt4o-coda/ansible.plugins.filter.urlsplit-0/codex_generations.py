

# Generated at 2024-06-01 06:26:59.859740
# Unit test for function split_url
def test_split_url():    # Test case 1: Split a full URL
    url = "http://www.example.com:80/path;params?query=arg#frag"
    expected_result = {
        'scheme': 'http',
        'netloc': 'www.example.com:80',
        'path': '/path',
        'params': 'params',
        'query': 'query=arg',
        'fragment': 'frag',
        'username': None,
        'password': None,
        'hostname': 'www.example.com',
        'port': 80
    }
    assert split_url(url) == expected_result

    # Test case 2: Query specific component
    assert split_url(url, 'scheme') == 'http'
    assert split_url(url, 'netloc') == 'www.example.com:80'
    assert split_url(url, 'path') == '/path'
    assert split_url(url, 'params') == 'params'

# Generated at 2024-06-01 06:27:02.586923
# Unit test for function split_url
def test_split_url():    # Test case 1: Split URL without query
    url = "http://example.com/path?query=1#fragment"
    expected_result = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=1',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    assert split_url(url) == expected_result

    # Test case 2: Split URL with query for 'scheme'
    assert split_url(url, 'scheme') == 'http'

    # Test case 3: Split URL with query for 'netloc'
    assert split_url(url, 'netloc') == 'example.com'

    # Test case 4: Split URL with query for 'path'
    assert split_url(url, 'path') == '/path'



# Generated at 2024-06-01 06:27:04.968042
# Unit test for function split_url
def test_split_url():    # Test case 1: Split URL without query
    url = "http://example.com/path?query=1#fragment"
    expected_result = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=1',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    assert split_url(url) == expected_result

    # Test case 2: Split URL with query for 'scheme'
    assert split_url(url, 'scheme') == 'http'

    # Test case 3: Split URL with query for 'netloc'
    assert split_url(url, 'netloc') == 'example.com'

    # Test case 4: Split URL with query for 'path'
    assert split_url(url, 'path') == '/path'



# Generated at 2024-06-01 06:27:08.323308
# Unit test for function split_url

# Generated at 2024-06-01 06:27:11.142306
# Unit test for function split_url

# Generated at 2024-06-01 06:27:15.870850
# Unit test for function split_url

# Generated at 2024-06-01 06:27:19.595286
# Unit test for function split_url
def test_split_url():
    # Test case 1: Valid URL with no query
    url = "http://example.com/path?query=1#fragment"
    result = split_url(url)
    expected = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=1',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Valid URL with query for 'scheme'
    result = split_url(url, query='scheme')
    expected = 'http'
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Valid URL with query for 'netloc'

# Generated at 2024-06-01 06:27:22.137647
# Unit test for function split_url

# Generated at 2024-06-01 06:27:24.840391
# Unit test for function split_url
def test_split_url():    # Test case 1: Split URL without query
    url = "http://example.com/path?query=1#fragment"
    expected_result = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=1',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    assert split_url(url) == expected_result

    # Test case 2: Split URL with query for 'scheme'
    assert split_url(url, 'scheme') == 'http'

    # Test case 3: Split URL with query for 'netloc'
    assert split_url(url, 'netloc') == 'example.com'

    # Test case 4: Split URL with invalid query

# Generated at 2024-06-01 06:27:28.226941
# Unit test for function split_url
def test_split_url():    # Test case 1: Split URL without query
    url = "http://example.com/path?query=1#fragment"
    expected_result = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=1',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    assert split_url(url) == expected_result

    # Test case 2: Split URL with query for 'scheme'
    assert split_url(url, 'scheme') == 'http'

    # Test case 3: Split URL with query for 'netloc'
    assert split_url(url, 'netloc') == 'example.com'

    # Test case 4: Split URL with query for 'path'
    assert split_url(url, 'path') == '/path'

