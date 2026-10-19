

# Generated at 2022-06-13 12:23:24.436561
# Unit test for function split_url
def test_split_url():

    assert split_url('https://www.example.com/path/name?a=1&b=2#test') == {
        'fragment': 'test',
        'netloc': 'www.example.com',
        'path': '/path/name',
        'query': 'a=1&b=2',
        'scheme': 'https'
    }

    assert split_url('https://www.example.com/path/name?a=1&b=2#test', 'scheme') == 'https'
    assert split_url('https://www.example.com/path/name?a=1&b=2#test', 'netloc') == 'www.example.com'
    assert split_url('https://www.example.com/path/name?a=1&b=2#test', 'path')

# Generated at 2022-06-13 12:23:36.896772
# Unit test for function split_url
def test_split_url():
    value = 'https://www.example.com:8443/path/to/file.html?key1=value1&key2=value2&key3=value3'
    url = split_url(value)

    assert url['scheme'] == 'https', "url['scheme'] is wrong"
    assert url['netloc'] == 'www.example.com:8443', "url['netloc'] is wrong"
    assert url['path'] == '/path/to/file.html', "url['path'] is wrong"
    assert url['query'] == 'key1=value1&key2=value2&key3=value3', "url['query'] is wrong"
    assert url['fragment'] == "", "url['fragment'] is wrong"

    # Test calling a query directly by name

# Generated at 2022-06-13 12:23:47.355628
# Unit test for function split_url
def test_split_url():
    assert split_url('http://example.com/foo/bar?a=1&b=2', 'scheme') == 'http'
    assert split_url('http://example.com/foo/bar?a=1&b=2', 'netloc') == 'example.com'
    assert split_url('http://example.com/foo/bar?a=1&b=2', 'path') == '/foo/bar'
    assert split_url('http://example.com/foo/bar?a=1&b=2', 'query') == 'a=1&b=2'
    assert split_url('http://example.com/foo/bar?a=1&b=2', 'fragment') is None

# Generated at 2022-06-13 12:23:56.336842
# Unit test for function split_url
def test_split_url():
    # Test no argument split
    value = 'http://stackoverflow.com/'
    msg = "The value %s should return a dictionary" % value

    assert type(split_url('')) == dict, msg

    # Test argument split
    value = "http://stackoverflow.com/search?q=ansible&page=1"
    msg = "The value %s should return a dictionary" % value

    assert type(split_url(value)) == dict, msg

    # Test argument split with query
    value = "http://stackoverflow.com/search?q=ansible&page=1"
    query = "netloc"
    msg = "The value %s should return a string" % query

    assert type(split_url(value, query)) == str, msg

    # Test argument split with invalid query

# Generated at 2022-06-13 12:24:06.221874
# Unit test for function split_url
def test_split_url():
    # Test a valid URL
    value = 'http://username:password@host.com:80/path?arg=value&arg2=value2#fragment'
    query = ''
    alias = 'urlsplit'

    test_results = {'scheme': 'http', 'path': '/path', 'netloc': 'username:password@host.com:80', 'query': 'arg=value&arg2=value2', 'fragment': 'fragment'}

    assert test_results == split_url(value, query, alias)

    # Test a query
    query = 'scheme'

    assert 'http' == split_url(value, query, alias)

    # Test an invalid query
    query = 'foo'

    # Ensure an exception is raised

# Generated at 2022-06-13 12:24:14.547414
# Unit test for function split_url
def test_split_url():
    value='https://www.google.com:8080/index.html?q=abc&p=123'
    expected_scheme='https'
    scheme=split_url(value, 'scheme')
    assert scheme == expected_scheme

    expected_netloc='www.google.com:8080'
    netloc=split_url(value, 'netloc')
    assert netloc == expected_netloc

    # Test that query is empty; the entire dictionary is returned
    expected='https://www.google.com:8080/index.html?q=abc&p=123'
    assert value == expected

    expected='www.google.com:8080'
    expected_netloc=split_url(value, 'netloc')
    assert netloc == expected_netloc


# Generated at 2022-06-13 12:24:24.985386
# Unit test for function split_url
def test_split_url():
    from ansible.utils.path import unfrackpath
    from ansible.module_utils.six.moves import cStringIO
    import sys
    import json
    expected = {}
    expected['scheme'] = 'http'
    expected['netloc'] = 'example.com'
    expected['path'] = '/path'
    expected['query'] = 'id=123&sid=3827'
    expected['fragment'] = 'section-1'
    url = 'http://example.com/path?id=123&sid=3827#section-1'
    results = split_url(url)
    assert expected == results
    results = split_url(url, 'scheme')
    assert expected['scheme'] == results
    results = split_url(url, 'netloc')
    assert expected['netloc'] == results


# Generated at 2022-06-13 12:24:35.611794
# Unit test for function split_url
def test_split_url():
    assert split_url('http://www.ansible.com/', query='scheme') == 'http'
    assert split_url('http://www.ansible.com/', query='scheme', alias='my_urlsplit') == 'http'
    assert split_url('https://www.ansible.com/', query='netloc') == 'www.ansible.com'
    assert split_url('https://www.ansible.com/', query='path') == '/'
    assert split_url('https://www.ansible.com/', query='query') == ''
    assert split_url('https://www.ansible.com/', query='fragment') == ''

# Generated at 2022-06-13 12:24:38.524292
# Unit test for function split_url
def test_split_url():
    assert split_url('ftp://ftp.kernel.org/foo/bar') == {'query': '', 'path': '/foo/bar',
                                                         'fragment': '', 'scheme': 'ftp', 'netloc': 'ftp.kernel.org'}

# Generated at 2022-06-13 12:24:45.663841
# Unit test for function split_url
def test_split_url():
    value = 'http://www.example.com:8080/path?arg=value#fragment'