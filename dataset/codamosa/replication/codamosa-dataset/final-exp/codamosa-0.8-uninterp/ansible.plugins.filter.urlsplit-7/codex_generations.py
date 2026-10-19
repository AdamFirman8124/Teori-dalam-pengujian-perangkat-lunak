

# Generated at 2022-06-13 12:23:23.895124
# Unit test for function split_url
def test_split_url():
    import ansible_collections.community.general.tests.unit.compat.mock as mock_unittest
    from ansible_collections.community.general.plugins.filters.url import split_url
    m = mock_unittest.Mock()
    m.urlsplit = m
    m.return_value = m
    m.test = 'test'
    m.scheme = 'scheme'
    m.netloc = 'netloc'
    m.path = 'path'
    m.query = 'query'
    m.fragment = 'fragment'
    m.username = 'username'
    m.password = 'password'
    m.hostname = 'hostname'
    m.port = 'port'
    result = split_url('test_url')

# Generated at 2022-06-13 12:23:36.785813
# Unit test for function split_url
def test_split_url():
    from ansible.module_utils.six.moves.urllib.parse import urlunsplit
    tests = dict(
        basic='http://www.ansible.com/forum?id=123',
        hard_code='http://www.ansible.com/forum?id=123',
        urlunsplit='http://www.ansible.com/forum?id=123',
        dict='http://www.ansible.com/forum?id=123',
        list='http://www.ansible.com/forum?id=123',
        tuple='http://www.ansible.com/forum?id=123',
    )
    for test in tests.values():
        u = urlsplit(test)


# Generated at 2022-06-13 12:23:47.213011
# Unit test for function split_url
def test_split_url():
    """
    test_split_url:
    URL = https://user:pass@host:80/path;param?query=arg#frag
    """

    # Test that query returns the expected value
    assert split_url('https://user:pass@host:80/path;param?query=arg#frag', 'scheme') == 'https'
    assert split_url('https://user:pass@host:80/path;param?query=arg#frag', 'netloc') == 'user:pass@host:80'
    assert split_url('https://user:pass@host:80/path;param?query=arg#frag', 'path') == '/path;param'
    assert split_url('https://user:pass@host:80/path;param?query=arg#frag', 'params') == 'param'
   

# Generated at 2022-06-13 12:23:57.849411
# Unit test for function split_url

# Generated at 2022-06-13 12:24:06.998670
# Unit test for function split_url
def test_split_url():
    assert split_url('ftp://ftp.debian.org/debian') == {'netloc': u'ftp.debian.org', 'path': u'/debian', 'scheme': u'ftp'}
    assert split_url('ftp://ftp.debian.org/debian', 'scheme') == 'ftp'
    assert split_url('ftp://ftp.debian.org/debian?q=foo&y=bar', 'query') == 'q=foo&y=bar'
    assert split_url('http://example.org/foo(bar)baz', 'path') == '/foo(bar)baz'
    assert split_url('http://example.org/foo%20bar', 'path') == '/foo bar'

test_split_url()

# Generated at 2022-06-13 12:24:15.082243
# Unit test for function split_url
def test_split_url():
    value = 'http://user:pass@localhost:8080/path;param?a=1&b=x#anchor'
    results = {
        'url'     : value,
        'scheme'  : 'http',
        'netloc'  : 'user:pass@localhost:8080',
        'path'    : '/path;param',
        'params'  : 'param',
        'query'   : 'a=1&b=x',
        'fragment': 'anchor',
        'username': 'user',
        'password': 'pass',
        'hostname': 'localhost',
        'port'    : 8080,
    }

    instance = FilterModule()
    urlsplit = instance.filters()['urlsplit']
    assert urlsplit(value) == results
    assert ur

# Generated at 2022-06-13 12:24:24.755401
# Unit test for function split_url
def test_split_url():
    url = 'http://www.example.com/path/to/file.txt?key1=val1&key2=val2#some-fragment'

    test_scenarios = (
        # Test query parameter
        ('scheme', 'http'),
        ('netloc', 'www.example.com'),
        ('path', '/path/to/file.txt'),
        ('query', 'key1=val1&key2=val2'),
        ('fragment', 'some-fragment'),
        # Test invalid query parameter
        ('test', AnsibleFilterError),
    )

    for (query, expected) in test_scenarios:
        yield (run_split_url_test, url, query, expected)



# Generated at 2022-06-13 12:24:35.544571
# Unit test for function split_url
def test_split_url():
    from ansible.module_utils.six.moves.urllib.parse import urlunsplit
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    assert split_url('https://www.example.com/path/to/resource?foo=bar&baz=qux#fragment') == {'fragment': 'fragment', 'scheme': 'https', 'netloc': 'www.example.com', 'path': '/path/to/resource', 'query': 'foo=bar&baz=qux'}
    assert split_url('https://www.example.com/path/to/resource?foo=bar&baz=qux#fragment', 'netloc') == 'www.example.com'

# Generated at 2022-06-13 12:24:38.155964
# Unit test for function split_url
def test_split_url():
    uri = 'http://www.cwi.nl:80/%7Eguido/Python.html?q=python'
    result = split_url(uri, query='scheme')
    assert result == 'http'

# Generated at 2022-06-13 12:24:42.546036
# Unit test for function split_url
def test_split_url():
    assert split_url('http://www.example.com/pages/', query='scheme') == 'http'
    assert split_url('http://www.example.com/pages/', query='netloc') == 'www.example.com'
    assert split_url('http://www.example.com/pages/', query='path') == '/pages/'
    assert split_url('http://www.example.com/pages/', query='query') == ''