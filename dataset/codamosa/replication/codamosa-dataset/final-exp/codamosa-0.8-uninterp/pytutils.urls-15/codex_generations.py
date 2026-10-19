

# Generated at 2022-06-14 06:46:16.214500
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff' )
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(boo='stuff' )
    assert update_query_params(url, params) == 'http://example.com?boo=stuff&biz=baz&foo=bar'



# Generated at 2022-06-14 06:46:20.753405
# Unit test for function update_query_params
def test_update_query_params():
    """Test update_query_params"""
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'

# Generated at 2022-06-14 06:46:27.097312
# Unit test for function update_query_params
def test_update_query_params():
    """
    Test for function update_query_params
    """
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz'


# Generated at 2022-06-14 06:46:33.514125
# Unit test for function update_query_params
def test_update_query_params():
    """ Unit test for function update_query_params """
    assert update_query_params('http://example.com', {'foo':'bar'}) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'}) == 'http://example.com?biz=baz&foo=stuff'

#Test it
test_update_query_params()

# Generated at 2022-06-14 06:46:46.975763
# Unit test for function update_query_params
def test_update_query_params():
    import nose.tools

    # Empty
    assert update_query_params('', dict(foo='bar')) == '?foo=bar'
    assert update_query_params('?', dict(foo='bar')) == '??foo=bar'

    # Different schemes
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'
    assert update_query_params('https://example.com', dict(foo='bar')) == 'https://example.com?foo=bar'

    # Different hosts
    assert update_query_params('http://foo.com', dict(foo='bar')) == 'http://foo.com?foo=bar'

# Generated at 2022-06-14 06:46:57.188998
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', fiz='faz')) == 'http://example.com?biz=baz&foo=stuff&fiz=faz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff'], fiz='faz')) == 'http://example.com?biz=baz&foo=stuff&fiz=faz'

# Generated at 2022-06-14 06:47:06.489871
# Unit test for function update_query_params
def test_update_query_params():
    http_url = 'http://example.com?foo=bar&biz=baz'
    https_url = 'https://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}

    new_http_url = update_query_params(http_url, params)
    new_https_url = update_query_params(https_url, params)

    assert new_http_url == 'http://example.com?foo=stuff&biz=baz'
    assert new_https_url == 'https://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:47:17.356261
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://www.example.com/', dict(foo='bar')) == 'http://www.example.com/?foo=bar'
    assert update_query_params('http://www.example.com/?foo=bar', dict(foo='baz')) == \
           'http://www.example.com/?foo=baz'
    assert update_query_params('http://www.example.com/?foo=bar', {}) == 'http://www.example.com/?foo=bar'
    assert update_query_params('http://www.example.com/?foo=bar', dict(foo='baz'), doseq=False) == \
           'http://www.example.com/?foo=baz'

# Generated at 2022-06-14 06:47:30.971166
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff','biz':'blah'}) == 'http://example.com?biz=blah&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', foo="stuff") == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:47:40.693518
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz&foo=test', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=test&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo':['stuff']}) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:47:51.282579
# Unit test for function update_query_params
def test_update_query_params():
    url = 'https://www.google.com?foo=bar&bar=foo'
    params = {'biz': 'bop'}
    assert update_query_params(url, params) == 'https://www.google.com?bar=foo&foo=bar&biz=bop'
    params = {'biz': ['bop', 'baz']}
    assert update_query_params(url, params) == 'https://www.google.com?bar=foo&foo=bar&biz=bop&biz=baz'

# Run unit tests.
test_update_query_params()

# Generated at 2022-06-14 06:47:56.456728
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'


# Decorators

# Generated at 2022-06-14 06:48:02.044186
# Unit test for function update_query_params
def test_update_query_params():
    base_url = 'http://example.com?foo=bar&biz=baz'
    updated_url = update_query_params(base_url, {'foo':'stuff', 'wow':'minor'})

    assert 'http://example.com?foo=stuff&biz=baz&wow=minor' == updated_url



# Generated at 2022-06-14 06:48:05.335792
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:48:09.309051
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))) == 'http://example.com?foo=stuff&biz=baz'

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:48:14.402778
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    result = update_query_params(url, params)
    assert result == 'http://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:48:22.011810
# Unit test for function update_query_params
def test_update_query_params():
    initial_url = 'http://example.com?foo=bar&biz=baz'
    final_url = update_query_params(initial_url, {'foo':'stuff'})
    assert final_url == 'http://example.com?foo=stuff&biz=baz'
    final_url = update_query_params(initial_url, {'foo':'stuff'}, False)
    assert final_url == 'http://example.com?foo=stuff&biz=baz'


# Generated at 2022-06-14 06:48:35.607397
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'

if __name__ == '__main__':
    for u in [
        'https://example.com',
        'https://example.com?foo=bar',
        'https://example.com?foo=bar&biz=baz',
        'https://example.com?foo=bar&biz=baz&biz=buzz'
    ]:
        print(update_query_params(u, dict(foo='stuff')))
    test_update_query_params()

# Generated at 2022-06-14 06:48:44.149588
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz='foo')) == 'http://example.com?biz=baz&foo=stuff&baz=foo'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'stuff2'])) == 'http://example.com?biz=baz&foo=stuff&foo=stuff2'

# Generated at 2022-06-14 06:48:55.921291
# Unit test for function update_query_params
def test_update_query_params():
    url = update_query_params("http://puddles.com/appointments/3?f=2&g=3", {'a': 1, 'b': 2})
    assert url == "http://puddles.com/appointments/3?a=1&b=2&f=2&g=3"
    url = update_query_params("http://puddles.com/appointments/3", {'a': 1, 'b': 2})
    assert url == "http://puddles.com/appointments/3?a=1&b=2"
    url = update_query_params("http://puddles.com/appointments/3?a=1&b=2", {})

# Generated at 2022-06-14 06:49:11.186087
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://localhost/test", params={'testing': 'true'}) == 'http://localhost/test?testing=true'
    assert update_query_params("http://localhost/test?testing=false", params={'testing': 'true'}) == 'http://localhost/test?testing=true'
    assert update_query_params("http://localhost/test?foo=bar&biz=baz", params={'foo': 'stuff'}) == 'http://localhost/test?foo=stuff&biz=baz'

# Test function if called from commandline
if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:49:16.589061
# Unit test for function update_query_params
def test_update_query_params():
    """
    Basic test for function update_query_params
    """
    assert update_query_params("http://example.com?foo=bar&biz=baz", dict(foo='stuff')) == \
           'http://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:49:23.151588
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected = 'http://example.com?foo=stuff&biz=baz'
    actual = update_query_params(url, {'foo': 'stuff'})
    assert expected == actual


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:49:28.417177
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_url = 'http://example.com?biz=baz&foo=stuff'

    updated_url = update_query_params(url, params)

    assert updated_url == expected_url


# Generated at 2022-06-14 06:49:37.160524
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(goo='stuff')) == 'http://example.com?biz=baz&foo=bar&goo=stuff'

test_update_query_params()

# Code to call update_query_params()

# Generated at 2022-06-14 06:49:41.826185
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    expected_res = 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(url, params) == expected_res



# Generated at 2022-06-14 06:49:47.892294
# Unit test for function update_query_params
def test_update_query_params():
    """
    Test function update_query_params
    """
    reference = 'http://example.com?foo=stuff&biz=baz'
    url = 'http://example.com?foo=bar&biz=baz'
    actual = update_query_params(url, {'foo': 'stuff'}, doseq=False)
    print(actual)
    assert actual == reference



# Generated at 2022-06-14 06:49:54.720558
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com/?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com/?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:50:00.066900
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)

    assert new_url == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:50:06.736497
# Unit test for function update_query_params
def test_update_query_params():
    tests = [
        ('http://example.com?foo=bar&biz=baz', dict(foo='stuff'), 'http://example.com?biz=baz&foo=stuff')
        ]

    for url, params, expected_url in tests:
        assert update_query_params(url, params) == expected_url

# Function denormalize_url

# Generated at 2022-06-14 06:50:24.139669
# Unit test for function update_query_params
def test_update_query_params():
    """
    Unit test for update_query_params function
    """
    test_url = 'http://example.com?foo=bar&biz=baz'
    test_params = {'foo':'stuff'}
    test_new_url = update_query_params(test_url, test_params)

    assert ('http://example.com?foo=stuff&biz=baz'==test_new_url)



# Generated at 2022-06-14 06:50:32.540354
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz&foo=spam', {'foo': 'stuff'}) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'biz': ['baz', 'spam']}) == 'http://example.com?foo=stuff&biz=baz&biz=spam'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:50:43.379102
# Unit test for function update_query_params
def test_update_query_params():
        # Create update_query_params() test inputs and expected outputs
        params = {'foo': 'stuff'}
        url = 'http://example.com?foo=bar&biz=baz'
        expected_output = 'http://example.com?biz=baz&foo=stuff'

        # Generate output with update_query_params()
        actual_output = update_query_params(url, params)

        # Compare expected output to actual output
        if actual_output == expected_output:
            print('Success!')
        else:
            print('No dice!') # Error message

# Create a test to see if update_query_params() works
test_update_query_params()

# Generated at 2022-06-14 06:50:50.701927
# Unit test for function update_query_params
def test_update_query_params():
    """
    Test to ensure that update_query_params is functioning properly
    """
    url = 'https://scan.coverity.com/projects/test'
    params = dict(foo='bar')

    url_replaced = 'https://scan.coverity.com/projects/test?foo=bar'
    url_modified = update_query_params(url, params)

    assert url_replaced == url_modified, 'update_query_params failed'



# Generated at 2022-06-14 06:51:01.998850
# Unit test for function update_query_params
def test_update_query_params():
    # Test for Query params present in the URL

    # Test for Query params not present in the URL
    updated_url = update_query_params("http://dummyurl.com/", dict(key1="value1", key2="value2"))
    expected_url = "http://dummyurl.com/?key1=value1&key2=value2"
    assert updated_url == expected_url

    # Test for both cases above
    updated_url = update_query_params("http://dummyurl.com/?key2=value2", dict(key1="value1", key2="value3"))
    expected_url = "http://dummyurl.com/?key1=value1&key2=value3"
    assert updated_url == expected_url

# Generated at 2022-06-14 06:51:06.110551
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

test_update_query_params()

# Generated at 2022-06-14 06:51:09.809048
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com?...foo=stuff...' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))

# Unit test functions

# Generated at 2022-06-14 06:51:13.955397
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com?foo=stuff&biz=baz' == \
        update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))



# Generated at 2022-06-14 06:51:25.069499
# Unit test for function update_query_params
def test_update_query_params():
    print("\n*** Testing update_query_params ***")
    assert update_query_params(
        'http://example.com?foo=bar',
        dict(foo='stuff')
    ) == 'http://example.com?foo=stuff'

    assert update_query_params(
        'http://example.com?foo=bar',
        dict(foo=['stuff', 'blah'])
    ) == 'http://example.com?foo=stuff&foo=blah'

    assert update_query_params(
        'http://example.com?foo=bar',
        dict(foo=['stuff', 'blah']),
        doseq=False
    ) == 'http://example.com?foo=stuff,blah'


# Generated at 2022-06-14 06:51:29.813279
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:51:54.951656
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz='bar')) == 'http://example.com?biz=baz&foo=stuff&baz=bar'

# Generated at 2022-06-14 06:52:05.809094
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'

if __name__ == "__main__":
    import os
    import sys
    import unittest
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from test_case.test_default_link import TestDefaultLinks
    from test_case.test_user_link import TestUserLinks

    test_classes_to_run = [TestDefaultLinks, TestUserLinks]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.load

# Generated at 2022-06-14 06:52:14.027935
# Unit test for function update_query_params
def test_update_query_params():
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')))
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', name='xxx')))
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', name='xxx', age=100)))
    return 0


# Generated at 2022-06-14 06:52:21.515595
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='NEWBAZ')) == 'http://example.com?foo=stuff&biz=NEWBAZ'
    assert update_query_params('http://example.com', dict(foo='stuff', biz='NEWBAZ')) == 'http://example.com?foo=stuff&biz=NEWBAZ'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:52:31.722768
# Unit test for function update_query_params
def test_update_query_params():
    """Tests the function update_query_params()"""

    testdata = [
        ['http://example.com', dict(), 'http://example.com'],
        ['http://example.com?foo=bar&biz=baz', dict(foo='stuff'), 'http://example.com?foo=stuff&biz=baz'],
        ['http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz=['qux', 'quux']), 'http://example.com?foo=stuff&biz=baz&baz=qux&baz=quux'],
    ]
    for test_url, test_params, test_result in testdata:
        result = update_query_params(test_url, test_params)

# Generated at 2022-06-14 06:52:37.677043
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'


# Generated at 2022-06-14 06:52:41.394010
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com"
    params = {'foo': 'stuff'}

    assert update_query_params(url, params) == "http://example.com?foo=stuff"

# Generated at 2022-06-14 06:52:46.215743
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:52:49.007291
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar&biz=baz"
    url = update_query_params(url, dict(foo='stuff'))
    assert url == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:52:56.909908
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://test.test/test.test?test=test"
    params = {
            "test1" : "test1",
            "test2" : "test2"
            }

    assert update_query_params(url, params) == "http://test.test/test.test?test=test&test1=test1&test2=test2"

if __name__ == '__main__':
    # Unit test
    test_update_query_params()

# Generated at 2022-06-14 06:53:44.036796
# Unit test for function update_query_params
def test_update_query_params():
    # Example1
    print(update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}))

    # Example2
    print(update_query_params('http://example.com', {'foo': 'stuff'}))


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:53:49.058231
# Unit test for function update_query_params
def test_update_query_params():
    new_url = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='foo'))
    assert new_url == 'http://example.com?foo=stuff&biz=baz&bar=foo'



# Generated at 2022-06-14 06:53:55.353206
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', {'foo': 'bar'}) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'biz': 'buzz'}) == 'http://example.com?biz=buzz&foo=stuff'



# Generated at 2022-06-14 06:54:00.104281
# Unit test for function update_query_params
def test_update_query_params():
    params = {'foo': 'stuff'}
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, params) == 'http://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:54:03.335326
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:54:09.380226
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'

    params = dict(foo='stuff', bizz=123)
    new_url = update_query_params(url, params)

    assert 'http://example.com?foo=stuff&biz=baz&bizz=123'
    assert new_url == 'http://example.com?foo=stuff&biz=baz&bizz=123'

# Generated at 2022-06-14 06:54:18.440421
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff', bar='far')) == 'http://example.com?foo=stuff&bar=far'
    assert update_query_params('http://example.com?foo=bar', dict(foo=['stuff', 'things'])) == 'http://example.com?foo=stuff&foo=things'

# Generated at 2022-06-14 06:54:24.040609
# Unit test for function update_query_params
def test_update_query_params():
    assert_equals('foo', {'bar': "1", 'baz': '2'}, update_query_params('foo', {'bar': "1", 'baz': '2'}))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:54:31.420591
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'), doseq=False) == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:54:35.512273
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:56:10.399474
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/foo/?biz=baz'
    params = dict(biz='stuff', foo='bar')

    assert update_query_params(url, params) == 'http://example.com/foo/?biz=stuff&foo=bar'

if __name__ == '__main__':
    print("Running update_query_params")
    test_update_query_params()