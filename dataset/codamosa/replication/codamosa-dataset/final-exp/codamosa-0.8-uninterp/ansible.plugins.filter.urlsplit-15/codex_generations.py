

# Generated at 2022-06-13 12:23:20.246505
# Unit test for function split_url
def test_split_url():
    assert split_url('https://example.com:8080/some/path/?some=query') == {
        'scheme': 'https',
        'netloc': 'example.com:8080',
        'path': '/some/path/',
        'query': 'some=query'
    }

# Generated at 2022-06-13 12:23:28.311580
# Unit test for function split_url
def test_split_url():
    url = 'https://www.google.com/search?q=foo'
    assert split_url(url)['scheme'] == 'https'
    assert split_url(url)['netloc'] == 'www.google.com'
    assert split_url(url)['path'] == '/search'
    assert split_url(url)['query'] == 'q=foo'
    assert split_url(url)['fragment'] == ''

    assert split_url(url, 'scheme') == 'https'
    assert split_url(url, 'netloc') == 'www.google.com'
    assert split_url(url, 'path') == '/search'
    assert split_url(url, 'query') == 'q=foo'
    assert split_url(url, 'fragment') == ''

# Generated at 2022-06-13 12:23:39.031891
# Unit test for function split_url
def test_split_url():
    url = "http://username:password@www.example.com:123/path/to/file?key1=value1&key2=value2#fragment"
    assert split_url(url, 'scheme') == 'http'
    assert split_url(url, 'netloc') == 'username:password@www.example.com:123'
    assert split_url(url, 'path') == '/path/to/file'
    assert split_url(url, 'query') == 'key1=value1&key2=value2'
    assert split_url(url, 'fragment') == 'fragment'

    # The default alias is 'urlsplit', so the following two statements are the same.
    assert split_url(url) == split_url(url, alias='urlsplit')

    # Invalid query

# Generated at 2022-06-13 12:23:46.908987
# Unit test for function split_url
def test_split_url():
    given_url = "http://localhost"
    given_option = "scheme"
    given_result = "http"
    given_url_second = "http://localhost/path"
    given_option_second = "path"
    given_result_second = "/path"

    # If a query is supplied, make sure it's valid then return the results.
    # If no option is supplied, return the entire dictionary.
    assert split_url(given_url, given_option) == given_result
    assert split_url(given_url_second, given_option_second) == given_result_second

# Generated at 2022-06-13 12:23:50.012169
# Unit test for function split_url
def test_split_url():
    test = split_url("https://github.com/ansible/ansible/pull/17761?foo=bar")
    assert test == "pull/17761?foo=bar"

# Generated at 2022-06-13 12:24:00.301865
# Unit test for function split_url
def test_split_url():
    url = 'https://user:pass@github.com:8080/ansible/ansible/issues/17953?foo=bar#issuecomment-283384293'
    result = split_url(url, 'scheme')
    assert result == 'https'

    result = split_url(url, 'netloc')
    assert result == 'user:pass@github.com:8080'

    result = split_url(url, 'path')
    assert result == '/ansible/ansible/issues/17953'

    result = split_url(url, 'query')
    assert result == 'foo=bar'

    result = split_url(url, 'fragment')
    assert result == 'issuecomment-283384293'

    result = split_url(url)
    assert result['scheme'] == 'https'
   

# Generated at 2022-06-13 12:24:05.551260
# Unit test for function split_url
def test_split_url():
    input_value = "https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_documenting.html"
    result = split_url(input_value)
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'docs.ansible.com'
    assert result['path'] == '/ansible/latest/dev_guide/developing_modules_documenting.html'


# Generated at 2022-06-13 12:24:09.271800
# Unit test for function split_url
def test_split_url():
    s = "http://www.cwi.nl:80/%7Eguido/Python.html"
    r = {'fragment': '', 'netloc': 'www.cwi.nl:80', 'scheme': 'http', 'path': '/%7Eguido/Python.html', 'query': ''}

    assert r == split_url(s)

# Generated at 2022-06-13 12:24:19.935530
# Unit test for function split_url
def test_split_url():
    
    # Test 1: basic test
    test_url = "https://allinurl.com/example?key=value"
    assert split_url(test_url) == {
        'port': None,
        'netloc': 'allinurl.com',
        'path': '/example',
        'query': 'key=value',
        'scheme': 'https',
        'fragment': '',
    }, "Failed to split URL"

    # Test 2: get query
    assert split_url(test_url, 'query') == 'key=value', "Failed to get query"

    # Test 3: get fragment
    assert split_url(test_url, 'fragment') == '', "Failed to get fragment"

    # Test 4: get non-exist

# Generated at 2022-06-13 12:24:28.546217
# Unit test for function split_url
def test_split_url():
    # pylint: disable=redefined-outer-name,missing-docstring
    from ansible.plugins import filter_loader

    env = {'ANSIBLE_STRING_CONVERSION_ACTION': 'warn',
           'ANSIBLE_STRIP_UNDEFINED_FROM_LIST': 'no'}

    filter_loader.add_filter_plugin(FilterModule, 'urlsplit')

    assert split_url('https://docs.ansible.com/ansible/latest/', 'scheme') == 'https'
    assert split_url('https://docs.ansible.com/ansible/latest/', 'netloc') == 'docs.ansible.com'
    assert split_url('https://docs.ansible.com/ansible/latest/', 'path') == '/ansible/latest/'
