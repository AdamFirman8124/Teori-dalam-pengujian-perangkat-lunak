

# Generated at 2022-06-13 12:23:25.777115
# Unit test for function split_url
def test_split_url():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six.moves.urllib.parse import urlunsplit
    result = split_url('http://www.example.com/path/file.html')
    assert result == {'netloc': 'www.example.com', 'path': '/path/file.html', 'scheme': 'http', 'query': '', 'fragment': ''}
    result = split_url('http://www.example.com/path/file.html', query='scheme')
    assert result == 'http'
    result = split_url('http://www.example.com/path/file.html', query='not_a_valid_query')
    assert not result

# Generated at 2022-06-13 12:23:37.860844
# Unit test for function split_url
def test_split_url():
    url = 'http://my.website.com:8080/test/dir/?query=value&a=1&b=2#anchor'
    s = split_url(url, query='scheme')
    assert s == 'http'
    s = split_url(url, query='hostname')
    assert s == 'my.website.com'
    s = split_url(url, query='port')
    assert s == 8080
    s = split_url(url, query='path')
    assert s == '/test/dir/'
    s = split_url(url, query='query')
    assert s == 'query=value&a=1&b=2'
    s = split_url(url, query='fragment')
    assert s == 'anchor'

# Generated at 2022-06-13 12:23:47.947422
# Unit test for function split_url
def test_split_url():
    from copy import copy
    from ansible.module_utils.six.moves.urllib.parse import urlsplit
    from ansible.utils.helpers import object_to_dict

    assert split_url('http://localhost/index.html') == object_to_dict(urlsplit('http://localhost/index.html'), exclude=['count', 'index', 'geturl', 'encode'])
    assert split_url('http://localhost/index.html', 'scheme') == 'http'
    assert split_url('http://localhost/index.html', 'netloc') == 'localhost'
    assert split_url('http://localhost/index.html', 'path') == '/index.html'
    assert split_url('http://localhost/index.html', 'query') == ''

# Generated at 2022-06-13 12:23:58.185598
# Unit test for function split_url
def test_split_url():
    from ansible.plugins.filter.core import split_url
    assert split_url('http://www.baidu.com:8080/index.php?a=1&b=2#frag') == {'scheme': 'http', 'hostname': 'www.baidu.com', 'port': 8080, 'path': '/index.php', 'query': 'a=1&b=2', 'fragment': 'frag'}
    assert split_url('http://www.baidu.com:8080/index.php?a=1&b=2#frag', query='scheme') == 'http'

# Generated at 2022-06-13 12:24:07.559293
# Unit test for function split_url
def test_split_url():
    from ansible.module_utils.six.moves.urllib.parse import urlparse
    url = urlparse('https://ansible.com:8080/posts/2018/11/14/15-ansible-2.8-release-blog/')

# Generated at 2022-06-13 12:24:15.294584
# Unit test for function split_url
def test_split_url():
    fs = FilterModule()
    assert fs.filters()['urlsplit']('scheme://username:password@hostname:9090/path?arg=value#fragment', 'scheme') == 'scheme'
    assert fs.filters()['urlsplit']('scheme://username:password@hostname:9090/path?arg=value#fragment', 'username') == 'username'
    assert fs.filters()['urlsplit']('scheme://username:password@hostname:9090/path?arg=value#fragment', 'password') == 'password'
    assert fs.filters()['urlsplit']('scheme://username:password@hostname:9090/path?arg=value#fragment', 'hostname') == 'hostname'

# Generated at 2022-06-13 12:24:15.888653
# Unit test for function split_url
def test_split_url():
    pass

# Generated at 2022-06-13 12:24:21.394470
# Unit test for function split_url
def test_split_url():
    urlsplit_test_dict = {'scheme': 'http', 'netloc': 'localhost:8080', 'path': '/', 'query': '', 'fragment': ''}
    assert split_url('http://localhost:8080') == urlsplit_test_dict
    assert split_url('http://localhost:8080')['netloc'] == 'localhost:8080'

# Generated at 2022-06-13 12:24:29.214621
# Unit test for function split_url
def test_split_url():
    def assert_result(url, query, expected):
        result = split_url(url, query)
        assert result == expected, "url: %s, query: %s, expected: %s, got: %s" % (url, query, expected, result)

    assert_result('http://user:pass@example.com:123/some/path?foo=bar&a=b#some-fragment', 'hostname', 'example.com')
    assert_result('http://user:pass@example.com:123/some/path?foo=bar&a=b#some-fragment', 'username', 'user')
    assert_result('http://user:pass@example.com:123/some/path?foo=bar&a=b#some-fragment', 'port', 123)

# Generated at 2022-06-13 12:24:36.136212
# Unit test for function split_url
def test_split_url():
    value = 'http://www.example.com:8080/path?arg=value#fragment'
    query = 'path'
    alias = 'urlsplit'

    results = helpers.object_to_dict(urlsplit(value), exclude=['count', 'index', 'geturl', 'encode'])
    if query in results:
        assert split_url(value, query, alias) == results[query]
    else:
        raise AnsibleFilterError(alias + ': unknown URL component: %s' % query)
