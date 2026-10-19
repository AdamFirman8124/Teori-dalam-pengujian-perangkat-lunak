

# Generated at 2022-06-13 12:23:33.976243
# Unit test for function split_url
def test_split_url():
    # Tests for the string 'https://en.wikipedia.org:8080/wiki/Manhole_(software)'
    # These are returned in dictionary form.
    assert split_url('https://en.wikipedia.org:8080/wiki/Manhole_(software)') == {
        'netloc': 'en.wikipedia.org:8080',
        'path': '/wiki/Manhole_(software)',
        'scheme': 'https',
        'params': '',
        'query': '',
        'fragment': '',
    }

    # Tests for the string 'http://user:password@host.com:8080/p/a/t/h?query=string#fragment'
    # These are returned in dictionary form.


# Generated at 2022-06-13 12:23:41.619830
# Unit test for function split_url
def test_split_url():
    """
    Tests for Ansible filters
    """
    # Test if the resuls are not exactly the same
    assert split_url("http://www.example.com") != "http://www.example.com"

    # Test if the results are in a dictionary format
    assert isinstance(split_url("http://www.example.com"), dict)

    # Test if the results contain the right number of elements
    assert len(split_url("http://www.example.com")) == 6

    # Test if the elements are correctly returned
    assert split_url("http://www.example.com")["scheme"] == "http"

# Generated at 2022-06-13 12:23:47.401978
# Unit test for function split_url
def test_split_url():
    input = ['https://www.example.com/foo/bar/', 'https://www.example.com/foo/bar/?moo=boo#poo', 'http://localhost/foo&bar?moo=boo', 'http://user:pass@localhost/foo&bar?moo=boo', 'http://user%40example.com:pass%40example.com@localhost/foo&bar?moo=boo']
    output = {'scheme': 'https', 'netloc': 'www.example.com', 'path': '/foo/bar/', 'query': '', 'fragment': ''}
    assert split_url(input[0], 'scheme') == output['scheme']
    assert split_url(input[0], 'netloc') == output['netloc']

# Generated at 2022-06-13 12:23:56.373628
# Unit test for function split_url
def test_split_url():
    def compare(results, expected):
        for r, e in zip(results, expected):
            if results[r] != e:
                raise Exception("Wrong parsing result: %s. Expected: %s" % (r, e))

    url = 'http://example.com:8080/index.html?flag=true#main'
    results = split_url(url)
    compare(results, ['http', 'example.com:8080', '/index.html', 'flag=true', 'main'])

    results = split_url(url, 'scheme')
    compare(results, ['http'])

    # Invalid component

# Generated at 2022-06-13 12:24:06.260685
# Unit test for function split_url
def test_split_url():
    assert split_url(value='http://foo.bar.com/a/b/c', query='scheme') == 'http'
    assert split_url(value='http://foo.bar.com/a/b/c', query='netloc') == 'foo.bar.com'
    assert split_url(value='http://foo.bar.com/a/b/c', query='path') == '/a/b/c'
    assert split_url(value='http://foo.bar.com/a/b/c', query='query') == ''
    assert split_url(value='http://foo.bar.com/a/b/c', query='fragment') == ''
    assert split_url(value='http://foo.bar.com/a/b/c', query='')['scheme'] == 'http'
   

# Generated at 2022-06-13 12:24:13.106994
# Unit test for function split_url
def test_split_url():
    results = split_url('https://www.example.com:443/foo?bar=baz#quux', query='port')
    assert results == 443
    results = split_url('https://www.example.com:443/foo?bar=baz#quux')
    assert results['scheme'] == 'https' and \
        results['netloc'] == 'www.example.com:443' and \
        results['path'] == '/foo' and \
        results['params'] == '' and \
        results['query'] == 'bar=baz' and \
        results['fragment'] == 'quux'

# Generated at 2022-06-13 12:24:21.066541
# Unit test for function split_url
def test_split_url():
    split_url_test = split_url('http://www.google.com/path/subpath?a=b&c=d#tag')
    assert split_url_test['scheme'] == 'http'
    assert split_url_test['netloc'] == 'www.google.com'
    assert split_url_test['path'] == '/path/subpath'
    assert split_url_test['params'] == ''
    assert split_url_test['query'] == 'a=b&c=d'
    assert split_url_test['fragment'] == 'tag'



# Generated at 2022-06-13 12:24:25.648314
# Unit test for function split_url
def test_split_url():
    url = 'https://www.example.com/'
    expected_results = {
        'scheme': 'https',
        'netloc': 'www.example.com',
        'path': '/',
        'params': '',
        'query': '',
        'fragment': ''
    }
    results = split_url(url)
    assert results == expected_results

# Generated at 2022-06-13 12:24:32.137112
# Unit test for function split_url
def test_split_url():
    url = 'https://ansible.com/ansible/author/jborean93'
    options = {
        'query': '',
        'scheme': 'https',
        'netloc': 'ansible.com',
        'path': '/ansible/author/jborean93',
        'params': '',
        'fragment': ''
    }

    for option, expected_result in options.items():
        assert split_url(url, query=option) == expected_result

# Generated at 2022-06-13 12:24:40.145676
# Unit test for function split_url