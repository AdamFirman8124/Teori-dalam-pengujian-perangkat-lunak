

# Generated at 2022-06-14 06:46:12.412914
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    return True

# Generated at 2022-06-14 06:46:21.956017
# Unit test for function update_query_params
def test_update_query_params():
    # test for standard GET urls
    test_attrs = {'norm': 'http://example.com?foo=nope', 'new_params': dict(foo='bar')}
    result = update_query_params(url=test_attrs['norm'], params=test_attrs['new_params'])
    expected = 'http://example.com?foo=bar'
    assert result == expected

    # test for standard GET urls with multiple values
    test_attrs = {'norm': 'http://example.com?foo=nope', 'new_params': dict(foo=['bar', 'baz'])}
    result = update_query_params(url=test_attrs['norm'], params=test_attrs['new_params'])

# Generated at 2022-06-14 06:46:26.390182
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz',
        {'foo': 'stuff'}
    ) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:46:36.641255
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com?foo=bar', dict(foo='baz')) == 'http://example.com?foo=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='bar', baz='foo')) == 'http://example.com?baz=foo&foo=stuff&biz=bar'

# Generated at 2022-06-14 06:46:44.745987
# Unit test for function update_query_params
def test_update_query_params():
    import sys
    if sys.version_info.major > 2:
        assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?foo=stuff&biz=baz'
    else:
        assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?foo=stuff&biz=baz'


# Generated at 2022-06-14 06:46:46.954506
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:46:57.189038
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url,  {'foo' : 'stuff'})
    assert new_url == 'http://example.com?biz=baz&foo=stuff'
    new_url = update_query_params(url,  {'foo' : ['stuff', 'morestuff']})
    assert new_url == 'http://example.com?biz=baz&foo=stuff&foo=morestuff'
    new_url = update_query_params(url,  {'foo' : 'stuff', 'biz': 'newbiz'})
    assert new_url == 'http://example.com?biz=newbiz&foo=stuff'

# Generated at 2022-06-14 06:47:02.596675
# Unit test for function update_query_params
def test_update_query_params():
    url = 'https://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    expected = 'https://example.com?biz=baz&foo=stuff'
    assert new_url == expected



# Generated at 2022-06-14 06:47:14.889422
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?test=test', dict(test='test1')) == 'http://example.com?test=test1'
    assert update_query_params('http://example.com?test=test', dict(test='test1')) != 'http://example.com?test=test'
    assert update_query_params('http://example.com?test=', dict(test='test1')) == 'http://example.com?test=test1'
    assert update_query_params('http://example.com?test=', dict(test='test1')) != 'http://example.com?test='
    assert update_query_params('http://example.com?test=test', dict(test='')) == 'http://example.com?test='

# Generated at 2022-06-14 06:47:20.664484
# Unit test for function update_query_params
def test_update_query_params():
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')))
    print(update_query_params('http://example.com?biz=baz', dict(foo='stuff')))


if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:47:26.511116
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:47:34.968796
# Unit test for function update_query_params
def test_update_query_params():

    # Parameters
    URL = 'http://www.example.com'
    PARAMS = {
        'foo': 'bar',
        'boo': 'baz',
    }
    EXPECTED_URL = 'http://www.example.com?foo=bar&boo=baz'

    # Method under testing
    updated_url = update_query_params(URL, PARAMS)

    # Asserts
    assert updated_url == EXPECTED_URL

# Generated at 2022-06-14 06:47:47.893721
# Unit test for function update_query_params
def test_update_query_params():
    # Basic test
    assert update_query_params('http://example.com', {}) == 'http://example.com'
    assert update_query_params('http://example.com?a=b', {}) == 'http://example.com?a=b'
    assert update_query_params('http://example.com/?a=b', {}) == 'http://example.com/?a=b'
    assert update_query_params('http://example.com/?a=b', {'a': 'c'}) == 'http://example.com/?a=c'
    assert update_query_params('http://example.com/?a=b&c=d', {'e': 'f'}) == 'http://example.com/?a=b&c=d&e=f'

# Generated at 2022-06-14 06:47:56.750186
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://foo/path/to/resource?foo=bar&biz=baz', dict(foo='stuff')) == 'http://foo/path/to/resource?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:48:00.520517
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:48:06.416294
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff', 'test': 3, 'list': ['test1', 'test2']}
    url = update_query_params(url, params)
    new_params = urlparse.parse_qs(urlparse.urlsplit(url)[3])

    for k, v in params.items():
        assert new_params[k][0] == v

# Generated at 2022-06-14 06:48:19.597560
# Unit test for function update_query_params
def test_update_query_params():
    # Test that update_query_params works as expected
    assert(update_query_params("http://example.com?foo=bar&biz=baz", dict(foo='stuff')) == "http://example.com?&biz=baz&foo=stuff")
    assert(update_query_params("http://example.com", dict(foo='stuff')) == "http://example.com?foo=stuff")
    assert(update_query_params("http://example.com?foo=bar&biz=baz", dict(foo='stuff', biz='bing')) == "http://example.com?&biz=bing&foo=stuff")

# Generated at 2022-06-14 06:48:21.021098
# Unit test for function update_query_params
def test_update_query_params():
    """
    """
    pass

# Generated at 2022-06-14 06:48:24.565484
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://example.com?foo=bar&biz=baz", dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:48:35.728637
# Unit test for function update_query_params
def test_update_query_params():

    # Simple
    assert ('http://example.com?foo=bar&biz=baz' == update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')))

    # Wrong type
    try:
        update_query_params(1, dict(foo='stuff'))
        assert False
    except TypeError as e:
        assert True

    # Wrong dictionnary
    try:
        update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=1))
        assert False
    except TypeError as e:
        assert True

# Generated at 2022-06-14 06:48:51.378812
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', {'foo': 'bar'}) == \
           'http://example.com?foo=bar'
    assert update_query_params('http://example.com?foo=bar', {'foo': 'biz'}) == \
           'http://example.com?foo=biz'
    assert update_query_params('http://example.com', {'biz': 'baz'}) == \
           'http://example.com?biz=baz'
    assert update_query_params('http://example.com?foo=bar', {'biz': 'baz'}) == \
           'http://example.com?foo=bar&biz=baz'

# Generated at 2022-06-14 06:48:54.803736
# Unit test for function update_query_params
def test_update_query_params():

    assert(update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}), 'http://example.com?foo=stuff&biz=baz')

# Generated at 2022-06-14 06:49:06.861471
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        "http://www.example.com/index.html?foo=bar", dict(foo="stuff")
    ) == "http://www.example.com/index.html?foo=stuff"

    assert update_query_params(
        "http://www.example.com/index.html?foo=bar", dict(foo="stuff", biz=1)
    ) == "http://www.example.com/index.html?foo=stuff&biz=1"

    assert update_query_params(
        "http://www.example.com/index.html?foo=bar", dict(foo="stuff", biz=1),
        doseq=False
    ) == "http://www.example.com/index.html?foo=stuff&biz=1"

# Generated at 2022-06-14 06:49:18.909015
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('http://example.com', {}) == 'http://example.com')
    assert(update_query_params('http://example.com?foo=bar', {}) == 'http://example.com?foo=bar')
    assert(update_query_params('http://example.com?foo=bar', {'foo': 'baz'}) == 'http://example.com?foo=baz')
    assert(update_query_params('http://example.com?foo=bar', {'foo': 'baz'}) == 'http://example.com?foo=baz')
    assert(update_query_params('http://example.com?foo=bar&foo=baz', {'foo': 'stuff'}) == 'http://example.com?foo=stuff')

# Generated at 2022-06-14 06:49:27.108323
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'

    assert update_query_params(url, dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, dict(foo='stuf', biz='stuff')) == 'http://example.com?biz=stuff&foo=stuf'
    assert update_query_params(url, dict(foo='stuf', biz='stuff', baz='boz')) == 'http://example.com?baz=boz&biz=stuff&foo=stuf'

# Generated at 2022-06-14 06:49:32.600772
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar&biz=baz"
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'

# Test della funzione
if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:49:40.343935
# Unit test for function update_query_params

# Generated at 2022-06-14 06:49:45.984727
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    actual_url = update_query_params(url, params)
    assert actual_url == expected_url

# Generated at 2022-06-14 06:49:50.367887
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz',
                               dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Function to determine whether a given value is likely to be a URL.

# Generated at 2022-06-14 06:49:57.877921
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='stuff2')) == 'http://example.com?foo=stuff&biz=baz&bar=stuff2'

# Generated at 2022-06-14 06:50:07.514288
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff', biz='stuff'))
    assert new_url == 'http://example.com?foo=stuff&biz=stuff'


# Generated at 2022-06-14 06:50:14.228425
# Unit test for function update_query_params
def test_update_query_params():
    test_input_1 = 'http://example.com?foo=bar&biz=baz'
    test_input_2 = dict(foo='stuff', bar=None)
    expected_result = 'http://example.com?foo=stuff&biz=baz'
    result = update_query_params(test_input_1, test_input_2)
    assert result == expected_result, 'Result was expected to be "%s" but was "%s".' % (expected_result, result)

# Generated at 2022-06-14 06:50:21.288393
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == expected_url

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:50:25.962993
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    result = update_query_params(url, params, doseq=True)
    print(result)

test_update_query_params()

# Generated at 2022-06-14 06:50:29.618945
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz') == 'http://example.com?biz=baz&foo=bar'

test_update_query_params()

# Generated at 2022-06-14 06:50:34.539809
# Unit test for function update_query_params
def test_update_query_params():
    result = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert result == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:50:39.710587
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'

test_update_query_params()


# Generated at 2022-06-14 06:50:51.645569
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://foo.bar', {'a': 1, 'b': 2}) == "http://foo.bar?a=1&b=2"
    assert update_query_params('http://foo.bar?a=1', {'b': 2}) == "http://foo.bar?a=1&b=2"
    assert update_query_params('http://foo.bar?a=1', {'a': 2}) == "http://foo.bar?a=2"
    assert update_query_params('http://foo.bar?a=1&a=2', {'a': 3}) == "http://foo.bar?a=3"

# Generated at 2022-06-14 06:51:00.630049
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com:8000?foo=bar&biz=baz'
    url_test = update_query_params(url, dict(foo='stuff', age=42))
    assert url_test == 'http://example.com:8000?foo=stuff&biz=baz&age=42'

# Add your own tests here


if __name__ == '__main__':
    # Run the tests in this file
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:51:07.943383
# Unit test for function update_query_params
def test_update_query_params():
    update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?&foo=stuff&biz=baz'
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')))

# Generated at 2022-06-14 06:51:21.347953
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected = 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, dict(foo='stuff')) == expected

    url = 'http://example.com?foo=bar&biz=baz'
    expected = 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, dict(foo='stuff')) == expected


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 06:51:32.032773
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?foo=stuff&biz=baz'
    new_url = update_query_params(new_url, dict(baz='stuff'))
    assert new_url == 'http://example.com?foo=stuff&biz=baz&baz=stuff'
    new_url = update_query_params(new_url, dict(foo='morestuff', baz='otherstuff'))
    assert new_url == 'http://example.com?foo=morestuff&biz=baz&baz=otherstuff'
    new_url = update_query_params(new_url, dict(biz='stuff'))


# Generated at 2022-06-14 06:51:44.339021
# Unit test for function update_query_params

# Generated at 2022-06-14 06:51:56.527075
# Unit test for function update_query_params
def test_update_query_params():
    # Test single occurrences
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff', biz='baz')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff', biz='baz'), doseq=False) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:52:06.232896
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://www.example.com/search?q=simon+muster"
    new_url = update_query_params(url, dict(q="krapfen"))
    assert new_url == "http://www.example.com/search?q=krapfen"

    new_url = update_query_params(url, new_param="ostern")
    assert new_url == "http://www.example.com/search?q=simon+muster&new_param=ostern"

# Execute unit test
if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:52:19.062706
# Unit test for function update_query_params
def test_update_query_params():
    # Test 1 - Add new query param
    url = "http://localhost/rest/api/2/project/KAN/versions"
    params = {'maxResults': 50}
    result = update_query_params(url, params)
    expected_result = 'http://localhost/rest/api/2/project/KAN/versions?maxResults=50'
    assert (result == expected_result)

    # Test 2 - Update existing query param
    url = "http://localhost/rest/api/2/issue/KAN-3?fields=summary,project"
    params = {'fields': "summary,project,issuetype"}
    result = update_query_params(url, params)

# Generated at 2022-06-14 06:52:29.992467
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz&biz=boo'
    expected_url = 'http://example.com?foo=stuff&biz=baz&biz=boo&baz=bing'
    updated_url = update_query_params(url, dict(foo='stuff', baz='bing'))
    assert updated_url == expected_url

if __name__ == "__main__":
    import sys
    import doctest
    doctest.testmod()
    print("Unit tests:")
    print("=" * 70)
    doctest.testmod(sys.modules[__name__])
    print("=" * 70)
    print("If you don't see any errors, everything is OK.")

# Generated at 2022-06-14 06:52:36.331892
# Unit test for function update_query_params
def test_update_query_params():
    # Arrange: Define test input
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')

    # Act: Call function
    url_out = update_query_params(url, params)

    # Assert: Test results
    ok_(url_out == 'http://example.com?foo=stuff&biz=baz')

# Generated at 2022-06-14 06:52:48.365468
# Unit test for function update_query_params
def test_update_query_params():
    url = update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')
    )
    assert url == 'http://example.com?biz=baz&foo=stuff'

    url = update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='bizz')
    )
    assert url == 'http://example.com?biz=bizz&foo=stuff'

    url = update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='bizz', bizbuzz='bizzbuzz')
    )

# Generated at 2022-06-14 06:52:52.650918
# Unit test for function update_query_params
def test_update_query_params():
    update_query_params('http://example.com/?foo=bar&biz=baz', dict(foo='stuff'))
    return 1

test_update_query_params()

# Generated at 2022-06-14 06:53:18.191315
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz&key=old#fragment'
    params = {'foo': 'stuff', 'key': 'new'}
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz&key=new#fragment'
    print('Passed')

# Run the unit test if we are main
if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:53:21.748908
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://base.url.com?foo=bar', dict(foo='stuff')) == 'http://base.url.com?foo=stuff'


# Generated at 2022-06-14 06:53:33.442984
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='baz')) == 'http://example.com?bar=baz&biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='baz'), doseq=False) == 'http://example.com?bar=baz&biz=baz&foo=stuff'

# Generated at 2022-06-14 06:53:37.630880
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    test = update_query_params(url, params)
    print(test)

# Code here
if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:53:43.245907
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com/?biz=baz&foo=stuff'


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:53:47.318307
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:53:52.188782
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    assert expected_url == update_query_params(url, params)


# Generated at 2022-06-14 06:53:57.885295
# Unit test for function update_query_params
def test_update_query_params():
    """
    Example unit test for update_query_params

    >>> test_update_query_params()
    'http://example.com?...foo=stuff...'
    """
    return update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))

# Generated at 2022-06-14 06:54:04.929080
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://my.site', {'foo': 'bar'}) == 'http://my.site?foo=bar'
    assert update_query_params('http://my.site?foo=bar', {'foo': 'other'}) == 'http://my.site?foo=other'
    assert update_query_params('http://my.site?foo=bar', {'another': 'stuff'}) == 'http://my.site?foo=bar&another=stuff'

if __name__ == '__main__': # pragma: no cover
    from nose.core import run_exit
    run_exit(argv=['nosetests', __file__])

# Generated at 2022-06-14 06:54:12.910912
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?key1=value1&key2=value2',
                               {'key3': 'value3', 'key4': 'value4'}) == \
           'http://example.com?key1=value1&key2=value2&key3=value3&key4=value4'
    assert update_query_params('http://example.com?key1=value1&key2=value2',
                               {'key1': 'value1b', 'key2': 'value2b'}) == \
           'http://example.com?key1=value1b&key2=value2b'

# Generated at 2022-06-14 06:54:57.641525
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': ['stuff', 'things']}) == 'http://example.com?biz=baz&foo=things&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'buzz': 'things'}) == 'http://example.com?biz=baz&buzz=things&foo=stuff'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:55:09.824629
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?biz=baz', dict(foo='stuff')) == \
        'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(
        'http://example.com?biz=baz', dict(foo='stuff'), doseq=False) == \
        'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(
        'http://example.com?biz=baz', dict(foo=['stuff'])) == \
        'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:55:15.226970
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='stuff')) == 'http://example.com?bar=stuff&foo=stuff&biz=baz'

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:55:21.848720
# Unit test for function update_query_params
def test_update_query_params():
    new_url = update_query_params(
        "http://example.com/publish.html?foo=bar&biz=baz", {
            'foo': 'stuff',
            'hello': 'world'
        }
    )
    if new_url != 'http://example.com/publish.html?biz=baz&foo=stuff&hello=world':
        raise Exception("Failed Update-Query-Params test")



# Generated at 2022-06-14 06:55:31.360488
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', liz='yass')) == 'http://example.com?foo=stuff&biz=baz&liz=yass'

if __name__ == '__main__':
    test_update_query_params()
    exit(0)

# Generated at 2022-06-14 06:55:42.242568
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz#bing'
    url2 = 'http://example.com?foo=bar&biz=baz&foo=bong#bing'
    url_stuff = 'http://example.com?foo=stuff&biz=baz#bing'
    url_stuff_bong = 'http://example.com?foo=stuff&biz=baz&foo=bong#bing'
    url_stuff_bar = 'http://example.com?foo=stuff&biz=baz&foo=bar#bing'

    assert update_query_params(url, {'foo': 'stuff'}) == url_stuff
    assert update_query_params(url2, {'foo': 'stuff'}) == url_stuff_bong

# Generated at 2022-06-14 06:55:55.499169
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {"foo": "stuff"}) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {"foo": "stuff"}, doseq=False) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {"foo": "stuff", "foo": "moarstuff"}, doseq=False) == 'http://example.com?foo=moarstuff&biz=baz'

# Generated at 2022-06-14 06:56:07.750313
# Unit test for function update_query_params
def test_update_query_params():
    urls = [
        'http://example.com',
        'http://example.com?foo=bar&biz=baz&foo=bar2',
        'http://example.com?bar=foo&baz=bar',
        'http://example.com?foo=bar&biz=baz&foo=bar2',
        'http://example.com?bar=foo&baz=biz',
        'http://example.com?foo=bar&baz=biz&biz=baz&foo=bar2',
        'http://example.com?foo=bar&biz=baz',
        'http://example.com?foo=bar&bar=x',
        'http://example.com?foo=bar&biz=baz&foo=bar2&bar=x'
    ]
