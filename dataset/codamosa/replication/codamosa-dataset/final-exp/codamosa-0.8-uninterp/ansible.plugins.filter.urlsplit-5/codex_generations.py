

# Generated at 2022-06-13 12:23:23.922232
# Unit test for function split_url
def test_split_url():
    assert split_url('scheme://user:pass@subdomain.nowhere.localhost:9000/path;parameters?query=value#section')['scheme'] == 'scheme'
    assert split_url('scheme://user:pass@subdomain.nowhere.localhost:9000/path;parameters?query=value#section')['username'] == 'user'
    assert split_url('scheme://user:pass@subdomain.nowhere.localhost:9000/path;parameters?query=value#section')['password'] == 'pass'
    assert split_url('scheme://user:pass@subdomain.nowhere.localhost:9000/path;parameters?query=value#section')['hostname'] == 'subdomain.nowhere.localhost'

# Generated at 2022-06-13 12:23:36.785958
# Unit test for function split_url
def test_split_url():

    fixture = 'http://user:pass@github.com:8080/ansible/ansible/issues/35294?foo=bar'
    full_result = {
        'scheme': 'http',
        'netloc': 'user:pass@github.com:8080',
        'path': '/ansible/ansible/issues/35294',
        'query': 'foo=bar',
        'fragment': ''
    }

    # Test an option is supplied
    assert split_url(fixture, 'scheme') == 'http'

    # Test an invalid option is supplied
    raised = False
    try:
        split_url(fixture, 'foo')
    except:
        raised = True
    assert raised

    # Test if no option is supplied and the complete dictionary is returned

# Generated at 2022-06-13 12:23:47.213460
# Unit test for function split_url
def test_split_url():
    # trailing slash
    assert {'netloc': 'www.example.com', 'path': '/path/to/', 'params': '', 'query': '', 'fragment': '', 'username': '', 'password': '', 'hostname': 'www.example.com', 'port': '', 'scheme': '', 'query_dict': {}} == split_url('www.example.com/path/to/')

    # http

# Generated at 2022-06-13 12:23:51.040497
# Unit test for function split_url
def test_split_url():
    test_url = split_url("https://www.example.com:8080/foo/bar?hello=world%20with%20spaces&foo=bar", "netloc")
    assert test_url == "www.example.com:8080"

# Generated at 2022-06-13 12:24:01.326296
# Unit test for function split_url
def test_split_url():
    import pytest
    from ansible.errors import AnsibleFilterError
    from ansible.utils.urls import split_url
    import urllib.parse
    import copy

    # Test standard input
    test = {
        'scheme': 'http',
        'netloc': 'www.ansible.com',
        'path': '/category/docs',
        'params': '',
        'query': 'field1=value1&field2=value2',
        'fragment': '',
    }

    url = urllib.parse.urlunsplit(test.values())
    url_parts = urllib.parse.urlsplit(url)
    test_parts = copy.copy(test)
    test_parts['count'] = 6
    test_parts['index'] = 0

# Generated at 2022-06-13 12:24:09.611634
# Unit test for function split_url
def test_split_url():

    assert split_url('https://www.example.com/index.php?id=ID-NUMBER') == 'https'
    assert split_url('https://www.example.com/index.php?id=ID-NUMBER', 'netloc') == 'www.example.com'
    assert split_url('https://www.example.com/index.php?id=ID-NUMBER', 'query') == 'id=ID-NUMBER'
    assert split_url('https://www.example.com/index.php?id=ID-NUMBER', 'scheme') == 'https'
    assert split_url('https://www.example.com/index.php?id=ID-NUMBER', 'path') == '/index.php'

# Generated at 2022-06-13 12:24:20.623300
# Unit test for function split_url
def test_split_url():
    '''
    Test the split_url filter
    '''
    url = 'http://user:pass@www.example.com:8080/path/to/file.py?option=test#test'

    # Test each query individually
    assert split_url(url, 'scheme') == 'http'
    assert split_url(url, 'netloc') == 'user:pass@www.example.com:8080'
    assert split_url(url, 'path') == '/path/to/file.py'
    assert split_url(url, 'query') == 'option=test'
    assert split_url(url, 'fragment') == 'test'

    # Test when no query is given
    results = split_url(url)
    assert isinstance(results, dict)

# Generated at 2022-06-13 12:24:28.781485
# Unit test for function split_url
def test_split_url():

    results = {'path': '/index.html', 'query': '', 'fragment': '', 'scheme': 'http', 'netloc': 'www.example.com'}

    assert split_url('http://www.example.com/index.html') == results
    assert split_url('http://www.example.com/index.html', 'netloc') == 'www.example.com'
    assert split_url('http://www.example.com/index.html', 'scheme') == 'http'
    assert split_url('http://www.example.com/index.html', 'path') == '/index.html'
    assert split_url('http://www.example.com/index.html', 'query') == ''

# Generated at 2022-06-13 12:24:35.240969
# Unit test for function split_url
def test_split_url():

    assert split_url('https://foo.com/bar') == {'hostname': 'foo.com', 'path': '/bar', 'scheme': 'https', 'query': '', 'netloc': 'foo.com', 'fragment': '', 'username': '', 'password': ''}
    assert split_url('https://forum.freeipa.org/viewtopic.php?f=3&t=29975&start=10', query='query') == 'f=3&t=29975&start=10'

# Generated at 2022-06-13 12:24:41.993960
# Unit test for function split_url
def test_split_url():
    test_url = "http://www.google.com:5984/database?param1=1&param2=2;session=abcdefg"
    assert split_url(test_url) == {'netloc': 'www.google.com:5984', 'path': '/database', 'query': 'param1=1&param2=2;session=abcdefg', 'scheme': 'http', 'fragment': '', 'username': '', 'password': '', 'hostname': 'www.google.com', 'port': '5984'}
    assert split_url(test_url, 'path') == '/database'
    assert split_url(test_url, 'query') == 'param1=1&param2=2;session=abcdefg'