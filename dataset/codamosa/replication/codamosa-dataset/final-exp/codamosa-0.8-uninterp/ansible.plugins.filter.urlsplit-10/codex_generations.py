

# Generated at 2022-06-13 12:23:25.622874
# Unit test for function split_url
def test_split_url():
    test_value = 'https://www.google.ie/search?q=test#test'
    test_scheme = 'https'
    test_host = 'www.google.ie'
    test_path = '/search'
    test_params = ''
    test_query = 'q=test'
    test_fragment = 'test'
    test_url = 'https://www.google.ie/search?q=test'
    test_netloc = 'www.google.ie'

    assert split_url(test_value, 'scheme') == test_scheme
    assert split_url(test_value, 'path') == test_path
    assert split_url(test_value, 'params') == test_params
    assert split_url(test_value, 'query') == test_query

# Generated at 2022-06-13 12:23:37.797314
# Unit test for function split_url
def test_split_url():
    def verify_url(value, query, result, alias='urlsplit'):
        if not isinstance(result, Exception):
            assert split_url(value, query, alias) == result, 'urlsplit filter returned %s instead of %s for query %s on value %s' \
                                                             % (split_url(value, query, alias), result, query, value)
        else:
            try:
                split_url(value, query, alias)
                assert False, 'urlsplit filter did not raise exception for query %s on value %s' % (query, value)
            except result:
                pass
            except Exception as ex:
                assert False, 'urlsplit filter raised exception %s instead of %s for query %s on value %s' \
                                % (ex, result, query, value)


# Generated at 2022-06-13 12:23:43.217559
# Unit test for function split_url
def test_split_url():
    u = "https://a@b.com/path?query#fragment"
    assert split_url(u, query='scheme') == 'https'
    assert split_url(u, query='netloc') == 'a@b.com'
    assert split_url(u, query='path') == '/path'
    assert split_url(u, query='query') == 'query'
    assert split_url(u, query='fragment') == 'fragment'

# Generated at 2022-06-13 12:23:49.920933
# Unit test for function split_url
def test_split_url():
    input_data = """https://user:pass@example.com:8042/over/there?name=ferret#nose \n \t"""
    expected_result = {'fragment': 'nose', 'netloc': 'user:pass@example.com:8042', 'scheme': 'https',
                       'path': '/over/there', 'query': 'name=ferret', 'username': 'user', 'password': 'pass',
                       'hostname': 'example.com', 'port': '8042'}
    result = split_url(input_data)
    assert result == expected_result

# Generated at 2022-06-13 12:23:53.985279
# Unit test for function split_url
def test_split_url():
    ''' Test for function split_url '''
    url = 'https://www.google.com'
    query = 'netloc'
    expected_output = 'www.google.com'
    output = split_url(url, query)
    assert expected_output == output, "Error splitting URL."

# Generated at 2022-06-13 12:24:04.341464
# Unit test for function split_url
def test_split_url():
    import os

    # Change working directory to folder containing this file.
    os.chdir(os.path.dirname(__file__))


# Generated at 2022-06-13 12:24:11.298131
# Unit test for function split_url
def test_split_url():
    url = 'https://user:pass@example.com:8080/path/to/resource?a=1&b=2#myfrag'

    # Test with no query
    results = split_url(value=url)
    assert results == {
        'scheme': 'https',
        'netloc': 'user:XXXXXXX@example.com:8080',
        'path': '/path/to/resource',
        'query': 'a=1&b=2',
        'fragment': 'myfrag',
    }

    # Test with query
    for query in results:
        assert split_url(value=url, query=query) == results[query]

    # Test with unknown query
    try:
        split_url(value=url, query='hostname')
    except AnsibleFilterError:
        pass

# Generated at 2022-06-13 12:24:19.140224
# Unit test for function split_url
def test_split_url():
    from ansible.module_utils.urls import url_argument_spec

    # Run split_url tests against the original implementation for comparison
    for test in url_argument_spec():
        url = test['uri']
        query = test['param']
        expected = test['expected']

        result = split_url(url, query=query)

        # Check that the returned result matches the expected value
        # If the result is a dict, check if all items in the dict matches
        if isinstance(result, dict):
            assert result == expected
        else:
            assert result == expected

# Generated at 2022-06-13 12:24:28.023875
# Unit test for function split_url
def test_split_url():

    url = 'http://foo:bar@www.example.com:8080/one/two/three?four=five&six=seven#eight'
    results = split_url(url)

    assert isinstance(results, dict)
    assert len(results) == 7
    assert results['scheme'] == 'http'
    assert results['username'] == 'foo'
    assert results['password'] == 'bar'
    assert results['hostname'] == 'www.example.com'
    assert results['port'] == 8080
    assert results['path'] == '/one/two/three'
    assert results['query'] == 'four=five&six=seven'
    assert results['fragment'] == 'eight'

    query_results = split_url(url, 'scheme')
    assert query_results == 'http'

# Generated at 2022-06-13 12:24:30.912677
# Unit test for function split_url
def test_split_url():
    params = dict(value='https://this.is.fake/uri?key=value',
                  query='',
                  alias='urlsplit')
    print(split_url(params))