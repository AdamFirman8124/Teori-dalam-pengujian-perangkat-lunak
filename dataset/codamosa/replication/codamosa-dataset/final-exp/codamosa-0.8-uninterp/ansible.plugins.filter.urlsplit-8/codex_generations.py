

# Generated at 2022-06-13 12:23:24.902384
# Unit test for function split_url
def test_split_url():
    '''
    Unit test for function split_url
    '''
    raw_url = 'http://www.ansible.com/user?name=jack&pass=secret#first'

    expected_results = {
        'scheme': 'http',
        'netloc': 'www.ansible.com',
        'path': '/user',
        'query': 'name=jack&pass=secret',
        'fragment': 'first'
    }
    actual_results = split_url(raw_url)
    assert actual_results == expected_results

    # Test with queries
    for query in ('scheme', 'netloc', 'path', 'query', 'fragment'):
        assert split_url(raw_url, query=query) == expected_results[query]

    # Test with invalid queries

# Generated at 2022-06-13 12:23:35.835807
# Unit test for function split_url
def test_split_url():
    url = 'http://test.test.test:8080/foo?bar=baz#test'
    results = split_url(url)

    assert results['scheme'] == 'http'
    assert results['netloc'] == 'test.test.test:8080'
    assert results['path'] == '/foo'
    assert results['query'] == 'bar=baz'
    assert results['fragment'] == 'test'
    assert results['username'] == None
    assert results['password'] == None
    assert results['hostname'] == 'test.test.test'
    assert results['port'] == 8080
    assert results['query_dict']['bar'] == 'baz'



# Generated at 2022-06-13 12:23:43.045919
# Unit test for function split_url
def test_split_url():
    """
    Returns a dictionary of components from a url.
    """
    from ansible.compat.tests import unittest

    url = 'http://www.example.org/path/file.html'

    expected = {'path': '/path/file.html', 'scheme': 'http',
                'netloc': 'www.example.org', 'query': '',
                'fragment': '', 'username': '', 'port': None,
                'hostname': 'www.example.org'}

    results = split_url(url)
    assert results == expected


if __name__ == '__main__':
    test_split_url()

# Generated at 2022-06-13 12:23:52.854713
# Unit test for function split_url
def test_split_url():
    assert split_url('http://example.com') == {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '',
        'query': '',
        'fragment': '',
    }
    assert split_url('http://example.com/foo/bar?param1=value1&param2=value2#fragment') == {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/foo/bar',
        'query': 'param1=value1&param2=value2',
        'fragment': 'fragment',
    }
    assert split_url('http://example.com/foo/bar?param1=value1&param2=value2#fragment', 'scheme') == 'http'

# Generated at 2022-06-13 12:24:00.508250
# Unit test for function split_url
def test_split_url():
    assert split_url.__name__ == 'split_url'
    assert split_url('http://example.com:123/foo/bar?q=1#anchor') == {'query': 'q=1', 'fragment': 'anchor', 'netloc': 'example.com:123', 'path': '/foo/bar', 'scheme': 'http'}
    assert split_url('http://example.com:123/foo/bar?q=1#anchor', 'query') == 'q=1'
    assert split_url('http://example.com:123/foo/bar?q=1#anchor', 'scheme') == 'http'
    assert split_url('http://example.com:123/foo/bar?q=1#anchor', 'fragment') == 'anchor'

# Generated at 2022-06-13 12:24:10.059461
# Unit test for function split_url
def test_split_url():
    assert 'admin' == split_url('https://admin:admin@localhost/admin?query=test#test', 'username')
    assert 'admin' == split_url('https://admin:admin@localhost/admin?query=test#test', 'password')
    assert 'localhost' == split_url('https://admin:admin@localhost/admin?query=test#test', 'hostname')
    assert '/admin' == split_url('https://admin:admin@localhost/admin?query=test#test', 'path')
    assert 'query=test' == split_url('https://admin:admin@localhost/admin?query=test#test', 'query')
    assert 'test' == split_url('https://admin:admin@localhost/admin?query=test#test', 'fragment')

# Generated at 2022-06-13 12:24:21.011555
# Unit test for function split_url
def test_split_url():
    assert 'foo' == split_url('http://www.example.com/index.html?foo=bar', 'query')
    assert 'foo%20bar' == split_url('http://www.example.com/index.html?foo%20bar=baz', 'query')

    assert 'www.example.com' == split_url('http://www.example.com/index.html?foo=bar', 'hostname')
    assert 'www.example.com' == split_url('http://www.example.com/index.html', 'hostname')

    assert '80' == split_url('http://www.example.com:80/index.html', 'port')

    assert 'http' == split_url('http://www.example.com:80/index.html', 'scheme')
    assert 'https' == split_url

# Generated at 2022-06-13 12:24:28.981619
# Unit test for function split_url
def test_split_url():

    url = 'https://1.2.3.4:8080/v1/state/hosts?pretty=true'
    assert split_url(url) == {
        'scheme': 'https',
        'netloc': '1.2.3.4:8080',
        'path': '/v1/state/hosts',
        'query': 'pretty=true',
        'fragment': ''
    }
    assert split_url(url, 'scheme') == 'https'
    assert split_url(url, 'netloc') == '1.2.3.4:8080'
    assert split_url(url, 'path') == '/v1/state/hosts'
    assert split_url(url, 'query') == 'pretty=true'
    assert split_url(url, 'fragment')

# Generated at 2022-06-13 12:24:38.257654
# Unit test for function split_url
def test_split_url():
    assert split_url('http://www.example.com:80/foo/bar?a=2', query='path') == '/foo/bar'  # No query specified
    assert split_url('http://www.example.com:80/foo/bar?a=2', query='port') == '80'
    assert split_url('http://www.example.com:80/foo/bar?a=2', query='hostname') == 'www.example.com'
    assert split_url('http://www.example.com:80/foo/bar?a=2', query='scheme') == 'http'
    assert split_url('http://www.example.com:80/foo/bar?a=2', query='query') == 'a=2'

# Generated at 2022-06-13 12:24:44.852950
# Unit test for function split_url
def test_split_url():
    value = 'https://example.com:8080/path/to/resource?id=1&type=2'
    expect = {
      'netloc': 'example.com:8080',
      'path': '/path/to/resource',
      'query': 'id=1&type=2',
      'fragment': '',
      'scheme': 'https',
    }
    results = split_url(value)
    assert results == expect, "Failed to parse URL %s properly" % value
    # Try to find a specific item from the URL
    assert split_url(value, 'fragment') == expect['fragment'], "Failed to parse URL fragment from %s" % value