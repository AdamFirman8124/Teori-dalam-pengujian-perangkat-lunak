

# Generated at 2022-06-13 12:23:28.431010
# Unit test for function split_url

# Generated at 2022-06-13 12:23:39.193843
# Unit test for function split_url

# Generated at 2022-06-13 12:23:48.858039
# Unit test for function split_url

# Generated at 2022-06-13 12:23:59.118163
# Unit test for function split_url
def test_split_url():
    filters = FilterModule()

    http_url = split_url(filters, 'http://host.example.com:8080/path?foo=bar', 'scheme')
    assert http_url == 'http'

    https_url = split_url(filters, 'https://host.example.com:8080/path?foo=bar', 'scheme')
    assert https_url == 'https'

    host_url = split_url(filters, 'https://host.example.com:8080/path?foo=bar', 'hostname')
    assert host_url == 'host.example.com'

    port_url = split_url(filters, 'https://host.example.com:8080/path?foo=bar', 'port')
    assert port_url == '8080'

    path_url = split_url

# Generated at 2022-06-13 12:24:08.174775
# Unit test for function split_url
def test_split_url():
	from ansible.module_utils.six.moves.urllib.parse import urlunsplit
	url = "https://ansible.com/index.php?p=home"
	url_dict = split_url(url)
	assert url_dict['scheme'] == 'https'
	assert url_dict['netloc'] == 'ansible.com'
	assert url_dict['path'] == '/index.php'
	assert url_dict['query'] == 'p=home'
	assert url_dict['fragment'] == ''
	assert split_url(url, query='scheme') == 'https'
	assert split_url(url, query='netloc') == 'ansible.com'
	assert split_url(url, query='path') == '/index.php'

# Generated at 2022-06-13 12:24:15.268381
# Unit test for function split_url
def test_split_url():
    # Basic test
    test_url = 'http://example.org/path/to/file.html?key=value#top'
    result = split_url(test_url)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.org'
    assert result['path'] == '/path/to/file.html'
    assert result['query'] == 'key=value'
    assert result['fragment'] == 'top'
    # Specific query
    assert 'http' == split_url(test_url, 'scheme')
    # Unknown key
    try:
        split_url(test_url, 'unknown_key')
        assert False, "This line should never be reached"
    except AnsibleFilterError:
        pass

# Generated at 2022-06-13 12:24:25.461423
# Unit test for function split_url
def test_split_url():
    # Test empty values
    assert(split_url('', '', '') == {'scheme': '', 'netloc': '', 'path': '', 'query': '', 'fragment': ''})

    # Test scheme only
    assert(split_url('http:', '', '') == {'scheme': 'http', 'netloc': '', 'path': '', 'query': '', 'fragment': ''})

    # Test netloc only
    assert(split_url('//example.com', '', '') == {'scheme': '', 'netloc': 'example.com', 'path': '', 'query': '', 'fragment': ''})

    # Test path only

# Generated at 2022-06-13 12:24:31.310054
# Unit test for function split_url
def test_split_url():
    import ansible.utils.urls
    import sys
    import unittest
    import urllib2

    from ansible.utils.urls import open_url

    # Python 2.6 doesn't support context managers, so we'll use
    # this try block instead
    try:
        from contextlib import nested
    except:
        from ansible.utils.urls import nested

    from ansible.utils import url
    from ansible.utils.urls import http, iri_to_uri
    from ansible.utils.urls import _sanitize_url, urllib2_exception
    from ansible.utils.urls import _check_url_arg
    from ansible.utils.urls import _unsafe_proxy_bypass

    # Patch open_url so we don't actually hit a server
    old_

# Generated at 2022-06-13 12:24:39.483158
# Unit test for function split_url

# Generated at 2022-06-13 12:24:50.010073
# Unit test for function split_url
def test_split_url():
    url = 'http://www.ansible.com/blog?x=1&y=2'
    res = split_url(url)
    assert res['scheme'] == 'http'
    assert res['netloc'] == 'www.ansible.com'
    assert res['path'] == '/blog'
    assert res['query'] == 'x=1&y=2'
    assert res['fragment'] == ''
    assert res['username'] == ''
    assert res['password'] == ''
    assert res['hostname'] == 'www.ansible.com'
    assert res['port'] is None