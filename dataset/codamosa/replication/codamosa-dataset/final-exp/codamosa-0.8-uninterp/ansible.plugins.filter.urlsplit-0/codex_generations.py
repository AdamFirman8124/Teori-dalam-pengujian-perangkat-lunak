

# Generated at 2022-06-13 12:23:25.854253
# Unit test for function split_url

# Generated at 2022-06-13 12:23:36.841629
# Unit test for function split_url
def test_split_url():
    url = 'http://www.google.com:80/index?q=ansible'
    assert split_url(url)['scheme'] == 'http'
    assert split_url(url, 'scheme') == 'http'

    assert split_url(url)['netloc'] == 'www.google.com:80'
    assert split_url(url, 'netloc') == 'www.google.com:80'

    assert split_url(url)['path'] == '/index'
    assert split_url(url, 'path') == '/index'

    assert split_url(url)['query'] == 'q=ansible'
    assert split_url(url, 'query') == 'q=ansible'

# Generated at 2022-06-13 12:23:47.285846
# Unit test for function split_url
def test_split_url():
    result = split_url("http://www.example.com:80/path?a=b#c=d", 'netloc')
    assert result == "www.example.com:80"
    result = split_url("http://www.example.com:80/path?a=b#c=d", 'scheme')
    assert result == "http"
    result = split_url("http://www.example.com:80/path?a=b#c=d", 'path')
    assert result == "/path"
    result = split_url("http://www.example.com:80/path?a=b#c=d", 'query')
    assert result == "a=b"
    result = split_url("http://www.example.com:80/path?a=b#c=d", 'fragment')


# Generated at 2022-06-13 12:23:57.896319
# Unit test for function split_url
def test_split_url():
    assert split_url('http://www.ansible.com/index.html?id=1&token=aaabbbccc')  == {
        'path': '/index.html', 'scheme': 'http', 'hostname': 'www.ansible.com', 'query': 'id=1&token=aaabbbccc', 'fragment': '', 'port': None, 'netloc': 'www.ansible.com', 'username': None, 'password': None}
    assert split_url('http://www.ansible.com/index.html', 'scheme') == 'http'
    try:
        split_url('http://www.ansible.com/index.html', 'component')
    except AnsibleFilterError as e:
        assert e.args[0] == 'urlsplit: unknown URL component: component'

# Generated at 2022-06-13 12:24:05.096498
# Unit test for function split_url
def test_split_url():

    # Test URL to be split
    url = 'http://www.example.com:80/path?q=foo#bar'

    # Expected result of splitting the test URL
    expected = {
        'scheme': 'http',
        'netloc': 'www.example.com:80',
        'path': '/path',
        'query': 'q=foo',
        'fragment': 'bar'
        }

    # Uses the given test URL as input data.
    actual = split_url(url)

    assert expected == actual, 'urlsplit failed to split %s' % url

# Generated at 2022-06-13 12:24:10.525278
# Unit test for function split_url
def test_split_url():
    value = 'scheme://username:password@hostname:8042/path?arg=value#fragment'
    expected = {
        'fragment': 'fragment',
        'hostname': 'hostname',
        'netloc': 'username:password@hostname:8042',
        'path': '/path',
        'port': 8042,
        'query': 'arg=value',
        'scheme': 'scheme',
        'username': 'username',
        'password': 'password',
        'query': 'arg=value'
    }
    assert expected == split_url(value)

# Generated at 2022-06-13 12:24:14.900734
# Unit test for function split_url
def test_split_url():
    from ansible.module_utils import basic
    from ansible.module_utils.parsing.convert_bool import boolean
    url = 'https://ansible.com/blog/hello_world'

    results = split_url(url, 'netloc')

    assert results == 'ansible.com'

# Generated at 2022-06-13 12:24:25.242810
# Unit test for function split_url
def test_split_url():
    res = split_url('http://www.example.com:8080/path/to/page?foo=bar#baz')
    assert res['scheme'] == 'http'
    assert res['netloc'] == 'www.example.com:8080'
    assert res['path'] == '/path/to/page'
    assert res['query'] == 'foo=bar'
    assert res['fragment'] == 'baz'
    assert res['username'] is None
    assert res['password'] is None
    assert res['hostname'] == 'www.example.com'
    assert res['port'] == 8080

    assert split_url('http://www.example.com:8080/path/to/page?foo=bar#baz', 'port') == 8080

# Generated at 2022-06-13 12:24:35.727425
# Unit test for function split_url
def test_split_url():

    assert split_url('http://www.example.com:8080') == {'fragment': '', 'netloc': 'www.example.com:8080', 'path': '', 'query': '', 'scheme': 'http'}
    assert split_url('http://www.example.com:8080/api/v1.0/endpoint?limit=1') == {'fragment': '', 'netloc': 'www.example.com:8080', 'path': '/api/v1.0/endpoint', 'query': 'limit=1', 'scheme': 'http'}
    assert split_url('http://www.example.com:8080/api/v1.0/endpoint?limit=1', query='scheme') == 'http'

# Generated at 2022-06-13 12:24:41.654834
# Unit test for function split_url
def test_split_url():

    """ Unit tests for ansible split_url filter """
    url = 'http://www.example.com:80/path?q=query#fragment'

    assert split_url(url=url, query='scheme') == 'http'
    assert split_url(url=url, query='netloc') == 'www.example.com:80'
    assert split_url(url=url, query='path') == '/path'
    assert split_url(url=url, query='query') == 'q=query'
    assert split_url(url=url, query='fragment') == 'fragment'
    assert split_url(url=url)['netloc'] == 'www.example.com:80'