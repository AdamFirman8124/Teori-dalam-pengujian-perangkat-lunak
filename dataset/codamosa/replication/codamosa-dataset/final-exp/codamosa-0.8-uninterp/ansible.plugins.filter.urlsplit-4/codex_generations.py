

# Generated at 2022-06-13 12:23:23.895825
# Unit test for function split_url
def test_split_url():
    filter_obj = FilterModule()
    split_url_func = filter_obj.filters()['urlsplit']
    assert split_url_func('http://docs.ansible.com/ansible/user_guide.html')['fragment'] == ''
    assert split_url_func('http://docs.ansible.com/ansible/user_guide.html')['netloc'] == 'docs.ansible.com'
    assert split_url_func('http://docs.ansible.com/ansible/user_guide.html')['path'] == '/ansible/user_guide.html'
    assert split_url_func('http://docs.ansible.com/ansible/user_guide.html')['query'] == ''

# Generated at 2022-06-13 12:23:32.350436
# Unit test for function split_url
def test_split_url():
    import json

    test = split_url('http://localhost/path?search=foo', query='query')
    assert test == 'search=foo', json.dumps(test)

    results = split_url('http://localhost/path?search=foo')
    assert results['query'] == 'search=foo', json.dumps(results)

    try:
        results = split_url('')
        assert False, json.dumps(results)
    except AssertionError as e:
        raise AnsibleFilterError(e)

# Generated at 2022-06-13 12:23:39.670027
# Unit test for function split_url
def test_split_url():
    expected = {
        'scheme': 'http',
        'netloc': 'www.example.com',
        'path': '/path/to/myfile.html',
        'query': 'key1=value1&key2=value2',
        'fragment': 'section1'
    }

    result = split_url('http://www.example.com/path/to/myfile.html?key1=value1&key2=value2#section1')

    assert result == expected


# Generated at 2022-06-13 12:23:46.514945
# Unit test for function split_url
def test_split_url():
    # Basic test
    url = 'http://www.example.com:80/html/docs/foo.html'
    result = split_url(url)

    assert result['scheme'] == 'http'
    assert result['netloc'] == 'www.example.com:80'
    assert result['path'] == '/html/docs/foo.html'

    # Test return of a single value
    result = split_url(url, query='scheme')
    assert result == 'http'

    # Test a value that doesn't exist
    try:
        split_url(url, query='bogus')
        assert False
    except AnsibleFilterError:
        assert True

    # Test a URL with query arguments

# Generated at 2022-06-13 12:23:57.226782
# Unit test for function split_url
def test_split_url():
    string = 'http://docs.ansible.com/ansible/latest/playbooks_filters.html'
    result = split_url(string)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'docs.ansible.com'
    assert result['path'] == '/ansible/latest/playbooks_filters.html'
    assert result['query'] == ''
    assert result['fragment'] == ''
    assert split_url(string, 'scheme') == 'http'
    assert split_url(string, 'netloc') == 'docs.ansible.com'
    assert split_url(string, 'path') == '/ansible/latest/playbooks_filters.html'
    assert split_url(string, 'query') == ''

# Generated at 2022-06-13 12:23:59.549700
# Unit test for function split_url
def test_split_url():
    assert split_url('https://www.google.com/search?q=urlsplit')['netloc'] == 'www.google.com'

# Generated at 2022-06-13 12:24:08.460489
# Unit test for function split_url
def test_split_url():
    """
    Split a url into components, and test if the selection
    of the desired fragment works.
    """
    # pylint: disable=invalid-name
    input_url = "http://www.mydomain.com/category/page?page=1&page_size=10"

    output = split_url(input_url)
    assert output == {
        'hostname': 'www.mydomain.com',
        'netloc': 'www.mydomain.com',
        'path': '/category/page',
        'query': 'page=1&page_size=10',
        'scheme': 'http',
        'fragment': '',
    }

    output = split_url(input_url, 'hostname')
    assert output == 'www.mydomain.com'

# Generated at 2022-06-13 12:24:15.002575
# Unit test for function split_url
def test_split_url():

    url = 'http://111.111.111.111:8000/s2/stat/'
    options = ('scheme', 'netloc', 'path', 'query')
    expected = {'scheme': 'http', 'netloc': '111.111.111.111:8000', 'path': '/s2/stat/', 'query': ''}

    for option in options:
        assert expected[option] == split_url(url, option)

    assert expected == split_url(url)

# Generated at 2022-06-13 12:24:25.315680
# Unit test for function split_url
def test_split_url():
    assert split_url('https://user:pass@www.example.com:8080/path;param?query=arg#fragment',
                     query='scheme') == 'https'
    assert split_url('https://user:pass@www.example.com:8080/path;param?query=arg#fragment',
                     query='netloc') == 'user:pass@www.example.com:8080'
    assert split_url('https://user:pass@www.example.com:8080/path;param?query=arg#fragment',
                     query='path') == '/path;param'
    assert split_url('https://user:pass@www.example.com:8080/path;param?query=arg#fragment',
                     query='params') == 'param'

# Generated at 2022-06-13 12:24:33.878907
# Unit test for function split_url
def test_split_url():
    from ansible.compat.tests import unittest
    import ansible.utils.urls as urls
