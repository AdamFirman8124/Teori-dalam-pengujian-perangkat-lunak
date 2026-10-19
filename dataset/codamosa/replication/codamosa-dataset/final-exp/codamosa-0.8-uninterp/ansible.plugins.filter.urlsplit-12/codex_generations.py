

# Generated at 2022-06-13 12:23:28.350167
# Unit test for function split_url
def test_split_url():
    assert split_url('http://www.example.com/foo/bar?alpha=beta') == {
        'netloc': 'www.example.com',
        'path': '/foo/bar',
        'scheme': 'http',
        'query': 'alpha=beta',
        'fragment': '',
        'username': '',
        'password': '',
        'hostname': 'www.example.com',
        'port': None
    }

    assert split_url('http://www.example.com/foo/bar?alpha=beta', 'query') == 'alpha=beta'
    assert split_url('http://www.example.com/foo/bar?alpha=beta', 'port') == None


# Generated at 2022-06-13 12:23:39.117204
# Unit test for function split_url
def test_split_url():
    ''' Test for function split_url '''
    url = "http://www.example.com:8000/path/path2?k1=v1&k2=v2#fr"
    assert split_url(url) == {
        'hostname': 'www.example.com',
        'netloc': 'www.example.com:8000',
        'query': 'k1=v1&k2=v2',
        'scheme': 'http',
        'username': '',
        'path': '/path/path2',
        'port': 8000,
        'password': '',
        'fragment': 'fr'
    }
    assert split_url(url, 'path') == '/path/path2'

# Generated at 2022-06-13 12:23:48.786908
# Unit test for function split_url
def test_split_url():

    urls = ['https://test.example.com/foo/bar?a=b&c=d', 'http://www.foo.bar/baz/qux/', 'www.foo.bar/baz/qux/?a=1&b=2', 'http://user:pass@example.com']

    for url in urls:
        print("urlsplit(%s):\n%s" % (url, split_url(url)))
        print("urlsplit(%s,query=scheme):\n%s" % (url, split_url(url, 'scheme')))
        print("urlsplit(%s,query=netloc):\n%s" % (url, split_url(url, 'netloc')))

# Generated at 2022-06-13 12:23:58.953024
# Unit test for function split_url
def test_split_url():
    assert split_url('http://www.cnn.com') == {'netloc': 'www.cnn.com', 'path': '', 'query': '', 'scheme': 'http', 'fragment': ''}
    assert split_url('http://www.cnn.com/') == {'netloc': 'www.cnn.com', 'path': '/', 'query': '', 'scheme': 'http', 'fragment': ''}
    assert split_url('http://www.cnn.com/path/to/page') == {'netloc': 'www.cnn.com', 'path': '/path/to/page', 'query': '', 'scheme': 'http', 'fragment': ''}
    assert split_url('http://www.cnn.com/path/to/page?foo=bar')

# Generated at 2022-06-13 12:24:08.103998
# Unit test for function split_url
def test_split_url():
    # valid urls
    assert {
        'scheme': 'http',
        'netloc': 'www.python.org',
        'path': '/',
        'query': '',
        'fragment': ''
    } == split_url('http://www.python.org/')
    assert {
        'scheme': 'http',
        'netloc': 'www.python.org',
        'path': '/',
        'query': '',
        'fragment': ''
    } == split_url('http://www.python.org/')
    assert {
        'scheme': 'http',
        'netloc': 'www.python.org',
        'path': '/',
        'query': '',
        'fragment': ''
    } == split_url('http://www.python.org')

# Generated at 2022-06-13 12:24:15.437849
# Unit test for function split_url
def test_split_url():
    # query
    assert split_url('http://www.example.com/foo/bar?a=1&b=2', 'query', alias='') == 'a=1&b=2'
    assert split_url('http://www.example.com/foo/bar?a=1&b=2', 'path', alias='') == '/foo/bar'
    assert split_url('http://www.example.com/foo/bar?a=1&b=2', 'scheme', alias='') == 'http'
    assert split_url('http://www.example.com/foo/bar?a=1&b=2', 'query', alias='') == 'a=1&b=2'

    # full query

# Generated at 2022-06-13 12:24:25.648528
# Unit test for function split_url
def test_split_url():

    url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=ansible"

    assert split_url(url) == {'netloc': 'www.google.com', 'path': '/webhp', 'scheme': 'https', 'query': 'sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8', 'fragment': 'q=ansible'}
    assert split_url(url, 'netloc') == 'www.google.com'
    assert split_url(url, 'path') == '/webhp'
    assert split_url(url, 'scheme') == 'https'

# Generated at 2022-06-13 12:24:35.917298
# Unit test for function split_url
def test_split_url():
    # Unit test for function split_url
    # Test regular expressions

    TEST_URL_1 = "https://github.com/ansible/ansible/blob/devel/lib/ansible/modules/files/lineinfile.py"
    TEST_URL_2 = "https://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/modules/files/lineinfile.py?token=AAABBB"
    TEST_URL_3 = "https://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/modules/files/lineinfile.py"

# Generated at 2022-06-13 12:24:44.087074
# Unit test for function split_url
def test_split_url():

    import pytest

    url = 'http://user:pass@example.com:80/path/to/page?q=foo#bar'
    dct = {'scheme': 'http',
           'netloc': 'user:pass@example.com:80',
           'path': '/path/to/page',
           'query': 'q=foo',
           'fragment': 'bar',
           'username': 'user',
           'password': 'pass',
           'hostname': 'example.com',
           'port': 80}

    assert split_url(url, 'scheme') == 'http'
    assert split_url(url, query='scheme') == 'http'
    assert split_url(url, 'scheme', alias='test') == 'http'


# Generated at 2022-06-13 12:24:57.836151
# Unit test for function split_url
def test_split_url():
    ''' Ensure that URLs split correctly '''

    u = 'user:pass@www.example.com:8080/path/to/page/page2?query=true&query2=true#ref'

    # The entire URL
    assert(u == split_url(u))

    # Common URL components
    assert(split_url(u, query='scheme') == '')
    assert(split_url(u, query='netloc') == 'user:pass@www.example.com:8080')
    assert(split_url(u, query='path') == '/path/to/page/page2')
    assert(split_url(u, query='query') == 'query=true&query2=true')
    assert(split_url(u, query='fragment') == 'ref')

    # Less common URL components
   