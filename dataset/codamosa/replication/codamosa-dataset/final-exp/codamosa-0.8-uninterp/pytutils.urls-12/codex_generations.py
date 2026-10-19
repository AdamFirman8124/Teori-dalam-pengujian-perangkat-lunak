

# Generated at 2022-06-14 06:46:13.861324
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    # url = urlparse.urlparse(url)
    params = dict(foo='stuff')
    assert ['stuff'] == urlparse.parse_qs(update_query_params(url, params)).get('foo')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:46:22.367369
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(
        url,
        dict(foo='stuff')
    ) == 'http://example.com?biz=baz&foo=stuff'

    url = 'http://example.com'
    assert update_query_params(
        url,
        dict(foo='stuff')
    ) == 'http://example.com?foo=stuff'

    url = 'http://example.com?foo=bar&foo=baz'
    assert update_query_params(
        url,
        dict(foo='stuff')
    ) == 'http://example.com?foo=bar&foo=baz&foo=stuff'

# Generated at 2022-06-14 06:46:27.728423
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == "http://example.com?biz=baz&foo=stuff"
    print(new_url)



# Generated at 2022-06-14 06:46:34.227801
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz&biz=red&biz=blue'
    params = dict(foo='stuff', foo2='stuff2')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz&biz=red&biz=blue&foo2=stuff2'
test_update_query_params()


# Generated at 2022-06-14 06:46:39.582163
# Unit test for function update_query_params
def test_update_query_params():
    from nose.tools import assert_equal
    assert_equal(update_query_params('http://example.com?foo=bar&bar=baz', dict(foo='stuff', biz='boz')), 'http://example.com?bar=baz&biz=boz&foo=stuff')

# Generated at 2022-06-14 06:46:49.946773
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'things'])) == 'http://example.com?biz=baz&foo=stuff&foo=things'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'things']), doseq=False) == 'http://example.com?biz=baz&foo=%5B%27stuff%27%2C+%27things%27%5D'

# Generated at 2022-06-14 06:47:03.385727
# Unit test for function update_query_params
def test_update_query_params():

    # Single value fields
    assert 'http://example.com?a=b&c=stuff&&d=e' == update_query_params('http://example.com?a=b&c=d&d=e', dict(c='stuff')), 'Single value fields: 1'
    assert 'http://example.com?a=b&c=&d=e' == update_query_params('http://example.com?a=b&c=d&d=e', dict(c='')), 'Single value fields: 2'
    assert 'http://example.com?a=b&c=d&d=e' == update_query_params('http://example.com?a=b&c=d&d=e', dict(c=None)), 'Single value fields: 3'

# Generated at 2022-06-14 06:47:09.035919
# Unit test for function update_query_params
def test_update_query_params():
    # Call function
    url = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))

    # Check if the result is correct
    assert url == 'http://example.com?foo=stuff&biz=baz'

if __name__ == '__main__':
    if 'test_update_query_params' in dir():
        eval('test_%s()' % 'test_update_query_params')
    else:
        print('No unit test found for function %s' % 'update_query_params')

# Generated at 2022-06-14 06:47:20.991752
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))=='http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz&foo=buz', dict(foo='stuff'))=='http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz&foo=buz', dict(foo='stuff',biz='baz'))=='http://example.com?biz=baz&foo=stuff'

test_update_query_params()

# Generated at 2022-06-14 06:47:27.224786
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', myparam='good')) == 'http://example.com?biz=baz&foo=stuff&myparam=good'


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:47:33.451548
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:47:43.301606
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == expected_url


if __name__ == "__main__":
    unittest.main()
    # url = 'http://example.com?foo=bar&biz=baz'
    # params = dict(foo='stuff')
    # print update_query_params(url, params)

# Generated at 2022-06-14 06:47:50.951118
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz=None)) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff1', 'stuff2'], biz=None)) == 'http://example.com?foo=stuff1&foo=stuff2'

test_update_query_params()

# Generated at 2022-06-14 06:47:56.229964
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/foo?biz=baz&foo=bar'
    url2 = 'http://example.com/foo?biz=baz&foo=stuff'
    assert update_query_params(url, {'foo': 'stuff'}) == url2

# Generated at 2022-06-14 06:48:01.709264
# Unit test for function update_query_params
def test_update_query_params():
    test_url = 'http://example.com?foo=bar&biz=baz'
    test_params = {'foo': 'stuff', 'biz': 'buzz'}
    expected = 'http://example.com?biz=buzz&foo=stuff'
    actual = update_query_params(test_url, test_params)
    assert actual == expected

# Generated at 2022-06-14 06:48:05.695892
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_result = 'http://example.com?foo=stuff'
    res = update_query_params(url, dict(foo='stuff'))
    assert res == expected_result

# Generated at 2022-06-14 06:48:10.685763
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:48:14.926080
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    



# Generated at 2022-06-14 06:48:19.484944
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:48:24.965051
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == expected_url, 'failed to update query parameters'



# Generated at 2022-06-14 06:48:37.418570
# Unit test for function update_query_params
def test_update_query_params():
  assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
  print('All tests passed')

if __name__ == '__main__':
  test_update_query_params()

# Created by Paige Brinks, 5/5/2017
# update_query_params() and unit testing code added by P.C. Shades, 5/8/2017

# Generated at 2022-06-14 06:48:41.010608
# Unit test for function update_query_params
def test_update_query_params():
  url = 'http://example.com?foo=bar&biz=baz'
  params = {'foo': 'stuff'}
  new_url = update_query_params(url, params)
  assert new_url == "http://example.com?biz=baz&foo=stuff"

# Generated at 2022-06-14 06:48:50.061457
# Unit test for function update_query_params
def test_update_query_params():
    """
    unit test for function update_query_params
    """
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar=['baz', 'baz'])) == 'http://example.com?bar=baz&bar=baz&biz=baz&foo=stuff'

# Generated at 2022-06-14 06:48:57.981601
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com"
    new_url = update_query_params(url, dict(foo='bar'))
    assert new_url == "http://example.com?foo=bar"

    url = "http://example.com/?foo=bar"
    new_url = update_query_params(url, dict(biz='baz'))
    assert new_url == "http://example.com/?foo=bar&biz=baz"

    url = "http://example.com/?foo=bar&biz=baz"
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == "http://example.com/?foo=stuff&biz=baz"

# Generated at 2022-06-14 06:49:10.573511
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar&biz=baz"
    assert update_query_params(url, dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, dict(foo='stuff')) != 'http://example.com?biz=baz&foo=bar'
    assert update_query_params(url, dict(foo='stuff')) != 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(url, dict(foo='stuff')) != 'http://example.com?foo=bar'
    assert update_query_params(url, dict(foo='stuff')) != 'http://example.com?biz=baz'

# Generated at 2022-06-14 06:49:17.870311
# Unit test for function update_query_params
def test_update_query_params():
    expected_result = 'http://example.com?foo=stuff&bar=baz'
    result=update_query_params('http://example.com?foo=bar&bar=baz', dict(foo='stuff'))
    assert result==expected_result, 'function update_query_params does not return the expected result'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:49:28.815986
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff',foo2='stuff2')) == 'http://example.com?biz=baz&foo=stuff&foo2=stuff2'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff',foo2='stuff2',foo3='stuff3')) == 'http://example.com?biz=baz&foo=stuff&foo2=stuff2&foo3=stuff3'

# Generated at 2022-06-14 06:49:41.469061
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
           'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com/foo/bar?foo=bar&biz=baz', dict(foo='stuff', biz='baaaaz')) == \
           'http://example.com/foo/bar?biz=baaaaz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'stuff2'])) == \
           'http://example.com?biz=baz&foo=stuff&foo=stuff2'

# Generated at 2022-06-14 06:49:54.090736
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', foz='boz')) == 'http://example.com?foo=stuff&biz=baz&foz=boz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'boz'])) == 'http://example.com?foo=stuff&foo=boz&biz=baz'

# Generated at 2022-06-14 06:50:03.396641
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff', biz='baz')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar', foo='stuff') == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&bar=foo', foo='stuff') == 'http://example.com?bar=foo&foo=stuff'

# Generated at 2022-06-14 06:50:17.292374
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:50:21.215297
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:50:24.925816
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:50:32.844278
# Unit test for function update_query_params

# Generated at 2022-06-14 06:50:43.226443
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
           'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz=['baz', 'buzz'])) == \
           'http://example.com?biz=baz&biz=buzz&foo=stuff'

# Workaround for Python 2.6
exec('def with_metaclass(meta, *bases): return meta("NewBase", bases, {})')

# Generated at 2022-06-14 06:50:46.220515
# Unit test for function update_query_params
def test_update_query_params():
    """
    Test function update_query_params with an assertion
    """
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:50:58.479835
# Unit test for function update_query_params
def test_update_query_params():
    assert( update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff' )
    assert( update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff' )
    assert( update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='foo')) == 'http://example.com?biz=foo&foo=stuff' )
    assert( update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'bar'])) == 'http://example.com?biz=baz&foo=stuff&foo=bar' )
   

# Generated at 2022-06-14 06:51:05.348335
# Unit test for function update_query_params
def test_update_query_params():
    sampleUrl = 'http://python.org?foo=bar&biz=baz'
    result = update_query_params(sampleUrl, {'foo': 'stuff'})
    assert result == 'http://python.org?biz=baz&foo=stuff', \
           'Test update_query_params function: Got %s' % result



# Generated at 2022-06-14 06:51:12.088399
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&foo=alsothis&biz=baz', {'foo': 'this'}) == 'http://example.com?biz=baz&foo=this'


# TODO: Replace this with a function
b64encoder = codecs.getencoder(u'base64')
b64decoder = codecs.getdecoder(u'base64')


# Generated at 2022-06-14 06:51:19.580473
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected = 'http://example.com?foo=stuff&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert expected == new_url


if __name__ == '__main__':
    import sys, doctest
    sys.exit(doctest.testmod()[0])

# Generated at 2022-06-14 06:51:48.104840
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', {'foo': 'stuff'}) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'bar': 'stuff'}) == 'http://example.com?bar=stuff&biz=baz&foo=stuff'

# Generated at 2022-06-14 06:51:54.514286
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    new_url = update_query_params(url, params)

    assert new_url == 'http://example.com?biz=baz&foo=stuff'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:52:05.554560
# Unit test for function update_query_params
def test_update_query_params():
    assert(urlparse.parse_qs(
        urlparse.urlsplit("http://example.com/foo/bar?foo=bar&biz=baz#fragment").query
    ) == {'biz': ['baz'], 'foo': ['bar']})

    assert(
        update_query_params("http://example.com/foo/bar?foo=bar&biz=baz#fragment", dict(foo='stuff')) ==
        "http://example.com/foo/bar?foo=stuff&biz=baz#fragment"
    )

# Generated at 2022-06-14 06:52:18.607419
# Unit test for function update_query_params
def test_update_query_params():
    """
    Unit tests for function update_query_params
    """
    # Test some cases that are known to work
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(test='test')) == 'http://example.com?biz=baz&foo=bar&test=test'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', test='test')) == 'http://example.com?biz=baz&foo=stuff&test=test'


if __name__ == "__main__":
    test_

# Generated at 2022-06-14 06:52:23.659963
# Unit test for function update_query_params
def test_update_query_params():
    url1 = 'http://example.com?foo=bar&biz=baz'
    url2 = 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(url1, {'foo': 'stuff'}) == url2



# Generated at 2022-06-14 06:52:31.497895
# Unit test for function update_query_params
def test_update_query_params():
    url = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert url == 'http://example.com?biz=baz&foo=stuff'

    url = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='qux'))
    assert url == 'http://example.com?biz=qux&foo=stuff'

# Generated at 2022-06-14 06:52:44.299088
# Unit test for function update_query_params
def test_update_query_params():
    assert ('http://example.com?foo=stuff&biz=baz' ==
            update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')))
    assert ('http://example.com?foo=stuff&biz=baz' ==
            update_query_params('http://example.com?foo=bar&biz=baz&biz=qux', dict(foo='stuff')))
    assert ('http://example.com?foo=stuff&biz=baz' ==
            update_query_params('http://example.com?biz=baz', dict(foo='stuff')))

# Generated at 2022-06-14 06:52:49.711402
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> test_update_query_params()
    """
    url = 'http://example.com?foo=bar&foo=baz&biz=baz'
    new_url1 = update_query_params(url, dict(foo='stuff'))
    print(new_url1)
    new_url2 = update_query_params(url, dict(foo='stuff', biz='buzz'))
    print(new_url2)

# Generated at 2022-06-14 06:52:55.106763
# Unit test for function update_query_params
def test_update_query_params():
    """
    Doctests here.
    """
    # Simple check
    assert 'foo=stuff' in update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:53:03.922066
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='boz')) == 'http://example.com?biz=boz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='boz', hi='there')) == 'http://example.com?biz=boz&foo=stuff&hi=there'

test_update_query_params()

# Generated at 2022-06-14 06:53:55.637813
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.org?foo=bar', {'foo': 'stuff'}) == 'http://example.org?foo=stuff'
    assert update_query_params('http://example.org?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.org?biz=baz&foo=stuff'
    assert update_query_params('http://example.org', {'foo': 'stuff'}) == 'http://example.org?foo=stuff'
    assert update_query_params('http://example.org?foo=bar', {'foo': 'stuff', 'biz':'baz'}) == 'http://example.org?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:54:00.828564
# Unit test for function update_query_params
def test_update_query_params():
    """
    Test update_query_params function

    :return: True if test is passed
    :rtype: bool
    """
    url = update_query_params("https://google.com", dict(foo="bar"))
    print("update_query_params: " + url)
    return True

# Generated at 2022-06-14 06:54:10.777900
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://www.example.com?a=1&b=2', {'b': '3'}) == 'http://www.example.com?a=1&b=3'
    assert update_query_params('http://www.example.com?a=1&b=2', {'c': '3'}) == 'http://www.example.com?a=1&b=2&c=3'
    assert update_query_params('http://www.example.com', {'a': '1'}) == 'http://www.example.com?a=1'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:54:22.496929
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', {'foo': 'stuff'}) == \
               'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == \
               'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': ['stuff', 'morestuff']}) == \
               'http://example.com?foo=stuff&foo=morestuff&biz=baz'

# Generated at 2022-06-14 06:54:27.605745
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://www.example.com', dict(foo='stuff')) == 'http://www.example.com?foo=stuff'
    assert update_query_params('http://www.example.com?foo=bar', dict(foo='stuff')) == 'http://www.example.com?foo=stuff'
    assert update_query_params('http://www.example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://www.example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:54:35.809727
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='1')) == 'http://example.com?biz=1&foo=stuff')


#-------------------------------------------------------------------------------

# Generated at 2022-06-14 06:54:41.056866
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# --------------------------------------------------------------------

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:54:50.557437
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff&x[x]=y')) == 'http://example.com?biz=baz&foo=stuff%26x%5Bx%5D%3Dy'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:54:56.996955
# Unit test for function update_query_params
def test_update_query_params():
    # Scenario:
    # Given a URL
    # When updating the URL
    # need to URL encode spaces; = ? &
    # # is not allowed
    # Then return URL with the parameters updated
    # Example:
    # 'http://example.com?foo=bar&biz=baz'
    # dict(foo=stuff)
    # 'http://example.com?...foo=stuff...'
    print(update_query_params('http://example.com?foo=bar&biz=baz&q=test%20case', dict(foo='stuff')))

test_update_query_params()

# Generated at 2022-06-14 06:55:01.305542
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

