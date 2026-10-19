

# Generated at 2022-06-13 12:23:24.187739
# Unit test for function split_url
def test_split_url():
    input = "https://user:password@example.com:8080/d3DF3:cache/2/c8/ba/1/e/d3dF3C8ba1e04c9db8d6f272872f1ad6fe1.html"
    expected = {"scheme":"https","netloc":"user:password@example.com:8080","path":"/d3DF3:cache/2/c8/ba/1/e/d3dF3C8ba1e04c9db8d6f272872f1ad6fe1.html","params":"scheme","query":"","fragment":""}
    output = split_url(input)
    assert output == expected

# Generated at 2022-06-13 12:23:37.396829
# Unit test for function split_url
def test_split_url():
    val = "http://127.0.0.1:8080/api/v1/namespaces/default/pods"
    url_info = split_url(val)
    assert url_info['scheme'] == 'http', "Failed to get scheme, got: %s" % url_info['scheme']
    assert url_info['netloc'] == '127.0.0.1:8080', "Failed to get netloc, got: %s" % url_info['netloc']
    assert url_info['path'] == '/api/v1/namespaces/default/pods', "Failed to get path, got: %s" % url_info['path']
    assert url_info['hostname'] == '127.0.0.1', "Failed to get hostname, got: %s" % url_

# Generated at 2022-06-13 12:23:45.042305
# Unit test for function split_url
def test_split_url():
    # Test missing query param
    assert split_url('') == {}

    # Test valid query
    assert split_url('http://www.google.com', query='path') == '/'

    # Test invalid query
    try:
        split_url('http://www.google.com', query='invalid')
        raise AssertionError('Should have thrown error')
    except AnsibleFilterError:
        pass

    # Test default query
    assert split_url('http://www.google.com')['netloc'] == 'www.google.com'

# Generated at 2022-06-13 12:23:53.189676
# Unit test for function split_url
def test_split_url():

    # Create a test data structure
    test = dict(
        url = 'http://user:pass@example.com:80/path/to/file?foo=bar#anchor',
        expected_results = dict(
            scheme = 'http',
            netloc = 'user:pass@example.com:80',
            path = '/path/to/file',
            query = 'foo=bar',
            fragment = 'anchor'
        )
    )

    # Compare actual results with expected results
    assert split_url(test['url']) == test['expected_results']



# Generated at 2022-06-13 12:24:03.518942
# Unit test for function split_url
def test_split_url():
    arg = 'https://user:password@github.com:443/ansible/ansible-modules-core'
    arg2 = 'git+https://github.com/ansible/ansible-modules-core'
    arg3 = 'https://github.com/ansible/ansible-modules-core?state=open'
    test = split_url(arg, 'username')
    assert test == 'user'
    test2 = split_url(arg, 'password')
    assert test2 == 'password'
    test3 = split_url(arg, 'hostname')
    assert test3 == 'github.com'
    test4 = split_url(arg, 'netloc')
    assert test4 == 'user:password@github.com:443'
    test5 = split_url(arg, 'fragment')
    assert test5

# Generated at 2022-06-13 12:24:13.418873
# Unit test for function split_url
def test_split_url():
    urls = [
        'ftp://ftp.is.co.za/rfc/rfc1808.txt',
        'http://www.ietf.org/rfc/rfc2396.txt',
        'ldap://[2001:db8::7]/c=GB?objectClass?one',
        'mailto:John.Doe@example.com',
        'news:comp.infosystems.www.servers.unix',
        'tel:+1-816-555-1212',
        'telnet://192.0.2.16:80/',
        'urn:oasis:names:specification:docbook:dtd:xml:4.1.2']

    for url in urls:
        actual = split_url(url)

# Generated at 2022-06-13 12:24:24.038286
# Unit test for function split_url

# Generated at 2022-06-13 12:24:33.700374
# Unit test for function split_url

# Generated at 2022-06-13 12:24:41.250188
# Unit test for function split_url
def test_split_url():

    # Define the urls
    url1 = 'http://www.python.org/doc/#frag'
    url2 = 'https://user:pass@www.python.org:8080/doc/'
    url3 = 'http://192.168.1.1:8081/'

    # Split using the entire url.
    result = split_url(url1)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'www.python.org'
    assert result['path'] == '/doc/'
    assert result['query'] == ''
    assert result['fragment'] == 'frag'

    result = split_url(url2)
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'user:pass@www.python.org:8080'

# Generated at 2022-06-13 12:24:44.508232
# Unit test for function split_url
def test_split_url():
    url = 'http://www.google.com:80/'
    result = split_url(url, 'scheme')
    assert result == 'http'