

# Generated at 2022-06-14 06:46:17.155132
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
           'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'), doseq=False) == \
           'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'thing'])) == \
           'http://example.com?biz=baz&foo=stuff&foo=thing'

# Generated at 2022-06-14 06:46:25.031068
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/'
    print ("test_update_query_params: url is ",url)

    params = dict(foo=123, bar=456, biz='stuff')
    print ("test_update_query_params: params is ",params)

    new_url = update_query_params(url, params)
    print ("test_update_query_params: new_url is ",new_url)


# Generated at 2022-06-14 06:46:35.874704
# Unit test for function update_query_params
def test_update_query_params():

    params = {'limit': 1, 'offset': 10}
    assert update_query_params('http://example.com?foo=bar&biz=baz', params) == 'http://example.com?biz=baz&foo=bar&limit=1&offset=10'
    assert update_query_params('http://example.com?foo=bar&biz=baz', params, False) == 'http://example.com?biz=baz&foo=bar&limit=1&offset=10'
    assert update_query_params('http://example.com?foo=bar&biz=baz&limit=1', params) == 'http://example.com?biz=baz&foo=bar&limit=1&offset=10'

# Generated at 2022-06-14 06:46:38.473783
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:46:40.339127
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'



# Generated at 2022-06-14 06:46:52.593234
# Unit test for function update_query_params

# Generated at 2022-06-14 06:47:05.639697
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': ['newstuff']}) == 'http://example.com?foo=newstuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:47:12.142179
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='thing')) == 'http://example.com?biz=thing&foo=stuff'

# Generated at 2022-06-14 06:47:18.433119
# Unit test for function update_query_params
def test_update_query_params():

    URL = 'http://www.spiegel.de/schlagzeilen/index.rss'

    params = {
        'foo': 'bar',
        'biz': 'baz'
    }
    url = update_query_params(URL, params)
    print(url)

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:47:32.010008
# Unit test for function update_query_params
def test_update_query_params():
    # There are several possibilities for the order in which query
    # params appear in a URL, and this function needs to generate the
    # same format as does the urls.py function url()

    # The trick is to build up the arguments to url() and to
    # update_query_params() in the same order, so the ordering of the
    # query params is the same.  It's difficult to compare the
    # generated URLs, but easy to compare the query params.

    # SortedDict must be used in order to guarantee the order of
    # arguments in the URL
    from collections import OrderedDict as SortedDict

    def compare(url1, url2):
        query_params1 = urlparse.parse_qs(urlparse.urlsplit(url1)[3])

# Generated at 2022-06-14 06:47:46.702236
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('/foo', {}) == '/foo'

    assert update_query_params('/foo', {'a': ''}) == '/foo?a='

    assert update_query_params('/foo?a=b', {'b': ''}) == '/foo?a=b&b='

    assert update_query_params('/foo?c=d', {'a': 'e'}) == '/foo?c=d&a=e'

    assert update_query_params('/foo?r=', {'s': 't'}) == '/foo?r=&s=t'

    assert update_query_params('/foo', {'p': []}) == '/foo?p='


# Generated at 2022-06-14 06:47:55.027423
# Unit test for function update_query_params
def test_update_query_params():
    # Test with a simple query string and a URL that already has a query string
    url = "http://example.com?foo=bar&biz=baz"
    params = {"foo": "stuff"}
    assert(update_query_params(url, params, doseq=True) == "http://example.com?foo=stuff&biz=baz")

    # Test with a simple query string and a URL that has no query string
    url = "http://example.com"
    params = {"foo": "stuff"}
    assert(update_query_params(url, params, doseq=True) == "http://example.com?foo=stuff")

# Generated at 2022-06-14 06:48:06.688689
# Unit test for function update_query_params
def test_update_query_params():

    # Notice the space in the string
    url = 'http://example.com?foo=bar&biz=baz'

    modified_url = update_query_params(url, dict(foo='stuff'))
    assert modified_url == 'http://example.com?biz=baz&foo=stuff', 'Results do not match'

    modified_url = update_query_params(url, dict(foo='stuff    '))
    assert modified_url == 'http://example.com?biz=baz&foo=stuff+', 'Results do not match'

    #Should not throw exception but just stop processing
    modified_url = update_query_params(url, dict(foo='stuff    dfgfgdfg', biz='   '))

# Generated at 2022-06-14 06:48:13.138601
# Unit test for function update_query_params
def test_update_query_params():
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    assert(update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == expected_url)


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:48:23.546225
# Unit test for function update_query_params
def test_update_query_params():
    # Simple examples
    assert 'http://example.com?foo=stuff&biz=baz'==update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert 'http://example.com?foo=stuff&biz=baz'==update_query_params('http://example.com?foo=bar&biz=baz', foo='stuff')
    assert 'http://example.com?foo=stuff&biz=baz'==update_query_params('http://example.com?foo=bar&biz=baz', [('foo', 'stuff')])

# Generated at 2022-06-14 06:48:37.131794
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', {'foo': 'stuff'}) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar', {'foo': 'stuff'}) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'new': 'thing'}) == 'http://example.com?biz=baz&foo=stuff&new=thing'

# Generated at 2022-06-14 06:48:43.123018
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff', biz='baz')
    url_with_params = update_query_params(url, params)
    assert url_with_params == 'http://example.com?foo=stuff&biz=baz', \
           "update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='baz')) == 'http://example.com?foo=stuff&biz=baz'"

# Generated at 2022-06-14 06:48:46.254104
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:48:54.534528
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://localhost:8080/?'
    url = update_query_params(url, params={'server':'localhost'})
    url = update_query_params(url, params={'server':'localhost'})
    url = update_query_params(url, params={'server':'foo'})
    url = update_query_params(url, params={'server':'bar'})

    assert url == 'http://localhost:8080/?server=bar'

test_update_query_params()

# Generated at 2022-06-14 06:49:03.078679
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com?foo=stuff&biz=baz' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert 'http://example.com?foo=stuff&biz=baz&foo=stuff' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'), doseq=False)

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:49:15.241834
# Unit test for function update_query_params
def test_update_query_params():
    query_params = {}
    url = 'https://example.com/'
    assert update_query_params(url, query_params) == url

    url = 'http://example.com'
    assert update_query_params(url, query_params) == url

    url = 'http://example.com/'
    assert update_query_params(url, query_params) == url

    url = 'https://example.com'
    assert update_query_params(url, query_params) == url

    url = 'https://example.com?foo=bar&biz=baz'
    query_params = {}
    assert update_query_params(url, query_params) == url

    url = 'https://example.com?foo=bar&biz=baz'
    query_params = {'foo': 'stuff'}


# Generated at 2022-06-14 06:49:26.101028
# Unit test for function update_query_params
def test_update_query_params():
    # Test if query parameters are added to a url
    url1 = "http://example.com?foo=bar&biz=baz"
    url2 = update_query_params(url1, dict(foo='stuff'))
    assert url2 == "http://example.com?foo=stuff&biz=baz"

    # Test if query parameters are updated in a url
    url3 = "http://example.com?foo=bar"
    url4 = update_query_params(url3, dict(foo='stuff'))
    assert url4 == "http://example.com?foo=stuff"

    # Test if query parameters are update with multiple values
    url5 = "http://example.com?foo=bar"
    url6 = update_query_params(url5, dict(foo=['stuff', 'other_stuff']))

# Generated at 2022-06-14 06:49:35.215527
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'

    # If a parameter is repeated, we must ensure that the result is alphabetically sorted.
    # This is to prevent a hash (e.g. for caching purposes) from differentiating between
    # 'foo=bar&foo=baz' and 'foo=baz&foo=bar'.
    assert update_query_params('http://example.com?foo=bar&foo=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&foo=stuff'

# Generated at 2022-06-14 06:49:38.390019
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'

    params = dict(foo='stuff')
    updated_url = update_query_params(url, params)

    assert updated_url == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:49:44.195439
# Unit test for function update_query_params
def test_update_query_params():
    # Test passes
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    # Test fails
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?baz=stuff&biz=baz'

# Generated at 2022-06-14 06:49:48.828251
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    pass
# Test update_query_params function
test_update_query_params()

# Generated at 2022-06-14 06:50:01.204436
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com/?foo=stuff' == update_query_params('http://example.com/?foo=bar', {'foo': 'stuff'})
    assert 'http://example.com/?foo=stuff' == update_query_params('http://example.com/', {'foo': 'stuff'})
    assert 'http://example.com/?foo=stuff' == update_query_params('http://example.com', {'foo': 'stuff'})
    assert 'http://example.com/?foo=stuff' == update_query_params('http://example.com?', {'foo': 'stuff'})
    assert 'http://example.com/?foo=stuff' == update_query_params('http://example.com/?', {'foo': 'stuff'})

    assert 'http://example.com/?foo=stuff' == update_query

# Generated at 2022-06-14 06:50:12.667020
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> test_update_query_params()
    Test of update_query_params passed
    """
    url = 'http://example.com/test/test.cgi?test=test&test1=test1'
    params = {'test': 'test2', 'test3': 'test3'}
    new_url = update_query_params(url, params)
    assert 'test=test2' in new_url
    assert 'test1=test1' in new_url
    assert 'test3=test3' in new_url
    print('Test of update_query_params passed')


# Test of function
if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:50:17.563493
# Unit test for function update_query_params
def test_update_query_params():

    # test.py
    # import pytest
    # from my_module import *

    # def test_increment():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'  # noqa

    # test_increment()



# Generated at 2022-06-14 06:50:29.771585
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?boy=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff','things'])) == 'http://example.com?foo=stuff&foo=things&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff','things']), doseq=False) == 'http://example.com?foo=stuff&foo=things&biz=baz'

# Generated at 2022-06-14 06:50:38.209238
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
        'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:50:46.977251
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://example.com?foo=bar&biz=baz", dict(foo='stuff')) == "http://example.com?foo=stuff&biz=baz"
    assert update_query_params("http://example.com?foo=bar&biz=baz", dict(foo=['stuff', 'more'])) == "http://example.com?foo=stuff&foo=more&biz=baz"
    assert update_query_params("http://example.com?foo=bar&biz=baz", dict(foo='stuff'), doseq=False) == "http://example.com?foo=stuff&biz=baz"

# Generated at 2022-06-14 06:50:52.629000
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', something='else')) == 'http://example.com?foo=stuff&biz=baz&something=else'

# http://stackoverflow.com/a/14733555

# Generated at 2022-06-14 06:51:06.952876
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> test_update_query_params()
    """
    url = 'https://www.example.com/?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'https://www.example.com/?foo=stuff&biz=baz'

    new_url = update_query_params(url, dict(foo='stuff', bing='bong'))
    assert new_url == 'https://www.example.com/?foo=stuff&biz=baz&bing=bong'

    new_url = update_query_params(url, dict())
    assert new_url == 'https://www.example.com/?foo=bar&biz=baz'

    with pytest.raises(AssertionError):
        url

# Generated at 2022-06-14 06:51:17.792351
# Unit test for function update_query_params
def test_update_query_params():

    # We want to do a single test, which tests all four cases:
    # 1.  Update a single parameter
    # 2.  Update a single parameter more than once
    # 3.  Insert a new parameter
    # 4.  Insert a new parameter more than once

    test_url = 'http://example.com?foo=bar&biz=baz'

# Generated at 2022-06-14 06:51:22.175743
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    result = update_query_params(url, dict(foo='stuff'))
    print('result',result)
    

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:51:30.170124
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
            'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
            'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(
            'http://example.com', dict(foo='bar')) == \
            'http://example.com?foo=bar'
    assert update_query_params(
            'http://example.com?foo=bar', dict(foo='stuff')) == \
            'http://example.com?foo=stuff'
    assert update_query_params(
            'http://example.com?foo=bar', dict(foo='stuff')) == \
            'http://example.com?foo=stuff'

# Generated at 2022-06-14 06:51:39.695789
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(url, dict(foo='stuff')) == expected_url

    url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?foo=stuff&biz=baz&x=y'
    assert update_query_params(url, dict(foo='stuff', x='y')) == expected_url


# Generated at 2022-06-14 06:51:52.989959
# Unit test for function update_query_params
def test_update_query_params():
    a = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert a == 'http://example.com?biz=baz&foo=stuff'

    a = update_query_params('http://example.com?foo=bar', dict(biz='baz'))
    assert a == 'http://example.com?biz=baz&foo=bar'

    a = update_query_params('http://example.com?foo=bar', dict(biz='baz'), False)
    assert a == 'http://example.com?biz=baz&foo=bar'

    a = update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='biz'))

# Generated at 2022-06-14 06:52:04.887100
# Unit test for function update_query_params
def test_update_query_params():
    # Test with existing param, value and single value
    result = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert result == 'http://example.com?foo=stuff&biz=baz'

    # Test with multiple params
    result = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='bazza', buzz='bazz'))
    assert result == 'http://example.com?foo=stuff&biz=bazza&buzz=bazz'

    # Test with multiple values
    result = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'biz']), doseq=False)

# Generated at 2022-06-14 06:52:16.288982
# Unit test for function update_query_params
def test_update_query_params():
    assert (update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))) == 'http://example.com?biz=baz&foo=stuff'




# Generated at 2022-06-14 06:52:21.726973
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    result = 'http://example.com?foo=stuff&biz=baz'
    assert(result == update_query_params(url, dict(foo='stuff')))

# Generated at 2022-06-14 06:52:27.917531
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = { 'foo' : 'stuff' }
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'

if __name__ == '__main__':
    from nose import runmodule
    runmodule()

# Generated at 2022-06-14 06:52:33.206377
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar&biz=baz"
    params = {
        "foo": "stuff",
    }
    assert(update_query_params(url, params) == "http://example.com?foo=stuff&biz=baz")


# ----------------------------------------------------------------------------------------------------------------------

# Generated at 2022-06-14 06:52:46.338398
# Unit test for function update_query_params
def test_update_query_params():
    # Test data
    INPUT_URL = 'http://example.com?foo=bar&biz=baz'
    PARAMS = dict(foo='stuff')
    # Test if function works in same way as in example
    assert update_query_params(INPUT_URL, PARAMS) == 'http://example.com?foo=stuff&biz=baz'
    # Test for URL without parameters
    assert update_query_params('http://example.com', PARAMS) == 'http://example.com?foo=stuff'
    # Test for URL with empty string as parameters
    assert update_query_params('http://example.com?', PARAMS) == 'http://example.com?foo=stuff'
    # Test for URL with nonexistent parameters

# Generated at 2022-06-14 06:52:49.905436
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo':'stuff', 'bang':'pow'}
    expected_url = 'http://example.com?bang=pow&biz=baz&foo=stuff'
    assert update_query_params(url, params) == expected_url

# Generated at 2022-06-14 06:52:55.282397
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    url_new = 'http://example.com?foo=stuff&biz=baz'
    params = {'foo':'stuff'}
    assert(url_new == update_query_params(url, params))


# Generated at 2022-06-14 06:52:58.783535
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'




# Generated at 2022-06-14 06:53:02.942013
# Unit test for function update_query_params
def test_update_query_params():
    url = 'https://example.com/?resourceGroup=project1&resource=foo'
    params = dict(resource='bar')
    result_url = 'https://example.com/?resource=bar&resourceGroup=project1'
    assert(update_query_params(url, params) == result_url)

# Generated at 2022-06-14 06:53:15.441922
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?foo=stuff&biz=baz'

    new_url = update_query_params(url, dict(foo='stuff', more='params'))
    assert new_url == 'http://example.com?foo=stuff&biz=baz&more=params'

    new_url = update_query_params(url, [('foo', 'stuff'), ('more', 'params')])
    assert new_url == 'http://example.com?foo=stuff&biz=baz&more=params'


# Generated at 2022-06-14 06:53:37.396001
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:53:39.542064
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'


# Generated at 2022-06-14 06:53:41.222965
# Unit test for function update_query_params
def test_update_query_params():
    # TODO: implement this function
    return "not implemented"


# Generated at 2022-06-14 06:53:54.040039
# Unit test for function update_query_params

# Generated at 2022-06-14 06:54:05.078829
# Unit test for function update_query_params
def test_update_query_params():
    """
    Unit test for function update_query_params
    :return: None
    """
    print('Testing function update_query_params')

    test_url = "http://bbs.byr.cn/article/JobInfo/1234?page=1#1"

    print( "Original url: ", test_url)
    print( "Updated url: ", update_query_params(test_url, {"page" : 2}))
    print( "Updated url: ", update_query_params(test_url, {"page" : 2}, False))
# End of function test_update_query_params


if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:54:09.884058
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    url_expected = 'http://example.com?...foo=stuff...'
    params = dict(foo='stuff')
    url_actual = update_query_params(url, params)
    assert url_expected == url_actual


# Generated at 2022-06-14 06:54:15.577677
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:54:21.377992
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> test_update_query_params()
    'http://example.com?biz=baz&foo=stuff'
    """
    return update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))


# Generated at 2022-06-14 06:54:26.386337
# Unit test for function update_query_params
def test_update_query_params():
    original = 'http://example.com?foo=bar&biz=baz&house=floe'
    modified = update_query_params(original, dict(foo='stuff', house='cave'))
    assert 'foo=stuff' in modified
    assert 'foo=bar' not in modified
    assert 'house=cave' in modified
    assert 'house=floe' not in modified



# Generated at 2022-06-14 06:54:33.481535
# Unit test for function update_query_params
def test_update_query_params():
    assert "http://example.com/?foo=stuff&biz=baz" == update_query_params("http://example.com?foo=bar&biz=baz", {"foo": "stuff"})
    assert "http://example.com/?foo=stuff&biz=baz" == update_query_params("http://example.com/?foo=bar&biz=baz", {"foo": "stuff"})
    
test_update_query_params()

# Generated at 2022-06-14 06:55:18.113928
# Unit test for function update_query_params
def test_update_query_params():
    """
    Test update_query_params function

    :return: None
    """

    url = 'http://www.google.com/test?s=testfoo&b=testbar'
    params = {'s': 'foo', 'b': 'bar'}
    new_url = update_query_params(url, params)

    assert new_url == 'http://www.google.com/test?s=foo&b=bar'


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=[__file__, '-vvs', '-x', '--pdb', '--pdb-failure'],
                   exit=False)

# Generated at 2022-06-14 06:55:29.005864
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='stuff')) == 'http://example.com?biz=stuff&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'stuff1'], biz=['stuff', 'stuff1'])) == 'http://example.com?biz=stuff&biz=stuff1&foo=stuff&foo=stuff1'

# Generated at 2022-06-14 06:55:33.510871
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo1=bar&foo2=baz', dict(foo1='stuff', foo3='buzz')) == 'http://example.com?foo3=buzz&foo2=baz&foo1=stuff'

# Generated at 2022-06-14 06:55:43.214788
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://example.com/", dict(foo='bar', biz='baz')) == "http://example.com/?foo=bar&biz=baz"
    assert update_query_params("http://example.com/?foo=bar", dict(biz='baz')) == "http://example.com/?foo=bar&biz=baz"
    assert update_query_params("http://example.com/?foo=bar&biz=baz", dict(foo='stuff')) == "http://example.com/?foo=stuff&biz=baz"
    assert update_query_params("http://example.com/?biz=baz", dict(foo='stuff')) == "http://example.com/?biz=baz&foo=stuff"

# Generated at 2022-06-14 06:55:56.526719
# Unit test for function update_query_params
def test_update_query_params():
    # Tests of various string inputs
    assert update_query_params('www.example.com', {'foo': 'bar'}) == \
                                'www.example.com?foo=bar'
    assert update_query_params('www.example.com?', {'foo': 'bar'}) == \
                                'www.example.com?foo=bar'
    assert update_query_params('www.example.com?foo=bar', {'foo': 'bar'}) == \
                                'www.example.com?foo=bar'
    assert update_query_params('www.example.com?foo=bar', {'foo1': 'bar1'}) == \
                                'www.example.com?foo=bar&foo1=bar1'

# Generated at 2022-06-14 06:56:07.861833
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) ==
        'http://example.com?biz=baz&foo=stuff')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar=3)) ==
        'http://example.com?bar=3&biz=baz&foo=stuff')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar=3, cat=['a'])) ==
        'http://example.com?bar=3&biz=baz&cat=a&foo=stuff')