

# Generated at 2022-06-14 06:46:10.089072
# Unit test for function update_query_params
def test_update_query_params():
    #TODO: Add logic
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:46:17.580494
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected = 'http://example.com?foo=stuff&biz=baz'
    actual = update_query_params(url, dict(foo='stuff'))
    assert_equal(expected, actual)
    actual = update_query_params(url, dict(foo='stuff'), doseq=False)
    assert_equal(expected, actual)
    actual = update_query_params(url, (('foo', 'stuff'),))
    assert_equal(expected, actual)
    actual = update_query_params(url, [('foo', 'stuff')])
    assert_equal(expected, actual)

#----------------------------------------------------------------------------


# Generated at 2022-06-14 06:46:19.760877
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com"
    assert update_query_params(url, dict(
            foo='bar'
    )) == 'http://example.com?foo=bar'



# Example Function

# Generated at 2022-06-14 06:46:22.675095
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://example.com?foo=bar&biz=baz", dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:46:34.451566
# Unit test for function update_query_params
def test_update_query_params():
    # Test basic functionality
    assert "http://example.com?foo=stuff" == update_query_params("http://example.com?foo=bar", dict(foo='stuff'))

    # Test new parameter
    assert "http://example.com?foo=bar&new_param=new_value" == update_query_params("http://example.com?foo=bar", dict(new_param='new_value'))

    # Test empty url and empty params
    assert "" == update_query_params("", dict())

    # Test empty url and non-empty params
    assert "new_param=new_value" == update_query_params("", dict(new_param='new_value'))

    # Test that multiple params are inserted

# Generated at 2022-06-14 06:46:46.584744
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz&biz=bang', dict(foo='stuff', biz='baz')) == 'http://example.com?biz=bang&biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(baz='stuff')) == 'http://example.com?biz=baz&baz=stuff&foo=bar'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:46:49.641099
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:47:02.997847
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    print(update_query_params(url, params))
    # Should print: http://example.com?foo=stuff&biz=baz
    # Try several other cases
    # Try several other cases
    params = dict(foo='stuff', bar='baz')
    print(update_query_params(url, params))


    url = 'http://example.com?foo=bar&biz=baz&arr=first&arr=second'
    params = dict(arr=['new'])
    print(update_query_params(url, params))
    # Should print: http://example.com?foo=bar&biz=baz&amp;arr=first&amp;arr=second&amp;arr=new

# Generated at 2022-06-14 06:47:09.991969
# Unit test for function update_query_params
def test_update_query_params():
    expected = 'http://example.com?foo=stuff&biz=baz'
    actual = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert expected == actual

    expected = 'http://example.com?foo=bar&biz=baz&foo=stuff&baz=bar'
    actual = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz='bar'))
    assert expected == actual

    expected = 'http://example.com?foo=bar&biz=baz&foo=stuff&baz=bar'
    actual = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz=['bar']))

# Generated at 2022-06-14 06:47:14.562618
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
           'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:47:20.843103
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:47:27.103017
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:47:36.375730
# Unit test for function update_query_params
def test_update_query_params():
    base_url = "http://example.org/over/there?foo=bar&biz=baz#here"
    params = {'foo': 'stuff', 'random': 'param'}

    expected_url = 'http://example.org/over/there?biz=baz&foo=stuff&random=param#here'
    actual_url = update_query_params(base_url, params)
    assert expected_url == actual_url


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:47:44.002197
# Unit test for function update_query_params
def test_update_query_params():

    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?foo=stuff&biz=baz'

    params = dict(foo='stuff', biz='stuff')
    assert update_query_params(url, params) == 'http://example.com?foo=stuff&biz=stuff'

# Generated at 2022-06-14 06:47:55.321114
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='baz2')) == 'http://example.com?biz=baz2&foo=stuff')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='baz2')) == 'http://example.com?biz=baz2&foo=bar')

# Generated at 2022-06-14 06:48:00.008281
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert 'foo=stuff' in new_url
    assert 'biz=baz' in new_url

# Generated at 2022-06-14 06:48:03.430230
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:48:07.855610
# Unit test for function update_query_params
def test_update_query_params():
    url = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert url == 'http://example.com?biz=baz&foo=stuff' or url == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:48:16.724902
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar&biz=baz"
    params = { "foo" : "stuff" }
    expected = "http://example.com?biz=baz&foo=stuff"

    assert update_query_params(url, params) == expected

if __name__ == '__main__':
    #
    # Run unit test
    #
    test_update_query_params()
    #
    # Run function with parameters passed through command line
    #
    pass

# Generated at 2022-06-14 06:48:22.598801
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com?foo=stuff&biz=baz' == \
        update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:48:36.159975
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo=['stuff'], biz='stuff', new_key='new_val')
    new_url = update_query_params(url, params)

    parts = urlparse.urlsplit(new_url)
    query_params = urlparse.parse_qs(parts.query)
    assert parts.scheme == 'http'
    assert parts.netloc == 'example.com'
    assert parts.path == ''
    assert query_params['biz'] == ['stuff']
    assert query_params['new_key'] == ['new_val']


# vim: filetype=python

# Generated at 2022-06-14 06:48:44.174467
# Unit test for function update_query_params
def test_update_query_params():
    # no changes
    assert update_query_params('http://example.com?foo=bar&biz=baz', {}) == 'http://example.com?foo=bar&biz=baz'

    # force new query parameter
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'}) == 'http://example.com?foo=stuff&biz=baz'

    # add new query parameter
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'new':'parameter'}) == 'http://example.com?foo=bar&biz=baz&new=parameter'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:48:55.919841
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='boo')) == 'http://example.com?biz=boo&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='boo'), doseq=False) == 'http://example.com?biz=boo&foo=stuff'
   

# Generated at 2022-06-14 06:49:00.446852
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    result = update_query_params(url, params)
    assert('foo=stuff' in result)
    assert('biz=baz' in result)

# Generated at 2022-06-14 06:49:05.496395
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Function to generate a random integer between 1 and 4 for 'repeat'

# Generated at 2022-06-14 06:49:11.726768
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/?role-name=S3Access&external-id=Boto&color=blue'
    params = dict(role_name='S3Access', external_id='Boto')
    expected_url = 'http://example.com/?role_name=S3Access&external_id=Boto&color=blue'
    assert update_query_params(url, params) == expected_url

# Generated at 2022-06-14 06:49:23.888904
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='boz')) == 'http://example.com?foo=bar&biz=boz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='baz')) == 'http://example.com?foo=bar&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz=['biz', 'boz'])) == 'http://example.com?foo=bar&biz=biz&biz=boz'

# Generated at 2022-06-14 06:49:29.986376
# Unit test for function update_query_params
def test_update_query_params():
    url = 'https://test.com/?name=test&id=1'
    new_url = update_query_params(url, dict(type='test', id=20), True)
    url_validate=new_url=='https://test.com/?type=test&name=test&id=20'
    assert url_validate == True

#https://test.com/?type=test&name=test&id=20

# Generated at 2022-06-14 06:49:36.647798
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='buzz')) == 'http://example.com?foo=stuff&biz=buzz'

# Generated at 2022-06-14 06:49:42.610081
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz',
        dict(foo='stuff')
    ) == 'http://example.com?foo=stuff&biz=baz'

    assert update_query_params(
        'http://example.com',
        dict(foo='stuff')
    ) == 'http://example.com?foo=stuff'



# Generated at 2022-06-14 06:49:52.456821
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) ==
           'http://example.com?foo=stuff&biz=baz')


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:50:02.869133
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', param='anotherParam')) == 'http://example.com?biz=baz&foo=stuff&param=anotherParam'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'param': 'anotherParam'}) == 'http://example.com?biz=baz&foo=stuff&param=anotherParam'

# Generated at 2022-06-14 06:50:14.605219
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='foo')) == 'http://example.com?biz=foo&foo=bar'
    assert update_query_params('http://example.com?biz=baz&foo=bar', dict(biz='foo')) == 'http://example.com?biz=foo&foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(bar='foo')) == 'http://example.com?bar=foo&biz=baz&foo=bar'
    assert update_query

# Generated at 2022-06-14 06:50:22.814009
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['biz','baz'])) == 'http://example.com?biz=baz&foo=biz&foo=baz'

test_update_query_params()

# Generated at 2022-06-14 06:50:33.925173
# Unit test for function update_query_params
def test_update_query_params():
    url1 = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff', fez=12345)
    updated_url = update_query_params(url1, params)
    assert updated_url == 'http://example.com?fez=12345&foo=stuff&biz=baz'
    url2 = 'http://example.com'
    updated_url = update_query_params(url2, dict(foo='stuff'))
    assert updated_url == 'http://example.com?foo=stuff'
    url3 = 'http://example.com?foe=long&foe=strong'
    updated_url = update_query_params(url3, dict(foe='stuff'))
    assert updated_url == 'http://example.com?foe=stuff'


# Generated at 2022-06-14 06:50:41.517075
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    url = update_query_params(url, dict(foo='stuff'))
    assert url == 'http://example.com?foo=stuff&biz=baz'
    url = update_query_params(url, dict(foo='stuff', biz='baaz'))
    assert url == 'http://example.com?foo=stuff&biz=baaz'

# Generated at 2022-06-14 06:50:52.410466
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:51:05.216279
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://www.google.com/?a=b", dict(c="d")) == "http://www.google.com/?a=b&c=d"
    assert update_query_params("http://www.google.com/?a=b", dict(a="c")) == "http://www.google.com/?a=c"
    assert update_query_params("http://www.google.com", dict(a="c")) == "http://www.google.com?a=c"
    assert update_query_params("http://www.google.com/?a=b", dict(a="c"), doseq=False) == "http://www.google.com/?a=c"

# Generated at 2022-06-14 06:51:16.722128
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo=['stuff'])) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?bar=foo', dict(foo=['stuff'])) == 'http://example.com?bar=foo&foo=stuff'
    assert update_query_params('http://example.com?bar=foo', dict(foo=[])) == 'http://example.com?bar=foo&foo='
    assert update_query_params('http://example.com?bar=foo&foo=hello', dict(foo=[])) == 'http://example.com?bar=foo&foo='

# Generated at 2022-06-14 06:51:25.504313
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', {"page":1, "page_size":100}) == 'http://example.com?page=1&page_size=100'
    assert update_query_params('http://example.com?page=1', {"page_size":100}) == 'http://example.com?page=1&page_size=100'
    assert update_query_params('http://example.com?page=1&page_size=100', {"page":10}) == 'http://example.com?page=10&page_size=100'

test_update_query_params()


# Generated at 2022-06-14 06:51:40.679372
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', [('foo', 'stuff')]) == 'http://example.com?foo=stuff&biz=baz'

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:51:54.032457
# Unit test for function update_query_params
def test_update_query_params():
    base_url = 'http://example.com'
    assert(update_query_params(base_url, {'foo': ['a', 'b', 'c']}) ==
           base_url + '?foo=a&foo=b&foo=c')
    assert(update_query_params(base_url, {'foo': ['a', 'b', 'c']},
                               doseq=False) == base_url + '?foo=abc')
    assert(update_query_params(base_url + '?foo=a', {'foo': 'b'}) ==
           base_url + '?foo=b')
    assert(update_query_params(base_url + '?foo=a&foo=b', {'foo': 'c'}) ==
           base_url + '?foo=c')



# Generated at 2022-06-14 06:52:05.449210
# Unit test for function update_query_params

# Generated at 2022-06-14 06:52:14.891549
# Unit test for function update_query_params
def test_update_query_params():
    assert (update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == "http://example.com?biz=baz&foo=stuff")
    assert (update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='new bar')) == "http://example.com?bar=new+bar&biz=baz&foo=stuff")

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:52:27.926865
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://example.com?foo=bar&biz=baz", {u'foo' : u'stuff'}) == "http://example.com?biz=baz&foo=stuff"
    assert update_query_params("http://example.com", {u'foo' : u'stuff'}) == "http://example.com?foo=stuff"
    assert update_query_params("http://example.com?foo=bar", {u'foo' : u'stuff'}) == "http://example.com?foo=stuff"
    assert update_query_params("http://example.com?foo=bar&biz=baz", {u'foo' : u'stuff'}) == "http://example.com?biz=baz&foo=stuff"


# Generated at 2022-06-14 06:52:37.749463
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz',
                               dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz',
                               dict(foo='stuff', bar=0)) == 'http://example.com?foo=stuff&bar=0&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz',
                               dict(foo='stuff', bar=0, asd='123')) == 'http://example.com?foo=stuff&bar=0&asd=123&biz=baz'



# Generated at 2022-06-14 06:52:39.062975
# Unit test for function update_query_params

# Generated at 2022-06-14 06:52:49.738689
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='biz')) == 'http://example.com?biz=biz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='biz'), False) == 'http://example.com?biz=biz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff1', biz='biz', foo='stuff2'), False) == 'http://example.com?biz=biz&foo=stuff2'

# Generated at 2022-06-14 06:53:01.904335
# Unit test for function update_query_params
def test_update_query_params():
    base_url = "https://www.google.com/maps/place/Union+Square,+New+York,+NY/@40.7358882,-73.9902966,17z/data=!3m1!4b1!4m5!3m4!1s0x89c2588c406903c1:0x61af67e8e467b600!8m2!3d40.7358882!4d-73.9881079"
    actual_url = update_query_params(base_url, {"b":"130"})

# Generated at 2022-06-14 06:53:05.827295
# Unit test for function update_query_params
def test_update_query_params():
    '''

    :return:
    '''
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:53:34.592999
# Unit test for function update_query_params
def test_update_query_params():
    # Format
    assert (update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) ==
            'http://example.com?biz=baz&foo=stuff')
    assert (update_query_params('http://example.com?foo=bar&biz=baz', foo='stuff') ==
            'http://example.com?biz=baz&foo=stuff')
    assert (update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) ==
            'http://example.com?biz=baz&foo=stuff')

# Generated at 2022-06-14 06:53:43.245141
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
        'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'new': 'thing'}) == \
        'http://example.com?biz=baz&foo=stuff&new=thing'

# Generated at 2022-06-14 06:53:50.033257
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz',dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz',dict(biz='stuff')) == 'http://example.com?biz=stuff&foo=bar'



# Generated at 2022-06-14 06:53:56.187190
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', foo2='more')) == 'http://example.com?biz=baz&foo=stuff&foo2=more'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=[1, 2])) == 'http://example.com?biz=baz&foo=1&foo=2'

# Generated at 2022-06-14 06:54:05.332044
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://foo.com/bar?q=spam&q=cheese', {'q': 'eggs'}) == 'http://foo.com/bar?q=eggs'
    assert update_query_params(
        'http://example.com/stuff?foo=bar&foo=baz', dict(foo='biz')
    ) == 'http://example.com/stuff?foo=biz'
    assert update_query_params(
        'http://example.com/stuff?foo=bar&foo=baz', dict(foo=['biz'])
    ) == 'http://example.com/stuff?foo=biz'

# Generated at 2022-06-14 06:54:12.409742
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', new='here')) == 'http://example.com?biz=baz&foo=stuff&new=here'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff1', 'stuff2'])) == 'http://example.com?biz=baz&foo=stuff1&foo=stuff2'


# Generated at 2022-06-14 06:54:18.379838
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?c=3&a=1'
    result = update_query_params(url, {'a': '2', 'b': '3'})
    assert 'http://example.com?c=3&a=2&b=3' == result


# Generated at 2022-06-14 06:54:26.359243
# Unit test for function update_query_params
def test_update_query_params():
    # Test for python 2
    try: import urlparse
    except ImportError: pass
    else:
        assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'

    # Test for python 3
    if sys.version_info >= (3,0):
        assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:54:33.427738
# Unit test for function update_query_params
def test_update_query_params():

    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', foo2 ='stuff2')) == 'http://example.com?foo=stuff&biz=baz&foo2=stuff2')
    assert(update_query_params('http://example.com', dict(foo='stuff', foo2 ='stuff2')) == 'http://example.com?foo=stuff&foo2=stuff2')

# Generated at 2022-06-14 06:54:38.959622
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff', biz='buzz')
    expected = 'http://example.com?foo=stuff&biz=buzz'

    assert update_query_params(url, params) == expected


# Generated at 2022-06-14 06:55:18.408489
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:55:25.041006
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff', bar='buzz'))
    assert new_url == 'http://example.com?foo=stuff&biz=baz&bar=buzz'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:55:32.697260
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('https://example.com', {}) == 'https://example.com'
    assert update_query_params('https://example.com?foo=bar', {'a': 1, 'b': 2}) == 'https://example.com?a=1&b=2&foo=bar'
    assert update_query_params('https://example.com?foo=bar', {'a': [1,2,3]}) == 'https://example.com?a=1&a=2&a=3&foo=bar'
    assert update_query_params('https://example.com?foo=bar', {'foo': 'baz'}) == 'https://example.com?foo=baz'



# Generated at 2022-06-14 06:55:43.358104
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com/?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com/?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='baz')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'

# Generated at 2022-06-14 06:55:56.636741
# Unit test for function update_query_params
def test_update_query_params():
    url = "https://www.google.com/search?q=query+string&oq=query+string&ie=UTF-8&hl=en&client=safari&gfe_rd=cr&dcr=0&ei=_9Y9Wb7aOcLAdgTzma2QAQ"
    params = {'foo': 'stuff', 'biz': 'baz'}
    new_url = update_query_params(url, params)
    assert new_url is not None

# Generated at 2022-06-14 06:56:05.967553
# Unit test for function update_query_params
def test_update_query_params():
    URL = 'http://www.example.com?foo=bar&biz=baz'
    assert update_query_params(URL, dict(foo='stuff')) == 'http://www.example.com?biz=baz&foo=stuff'
    assert update_query_params(URL, dict(foo='stuff', boz='code')) == 'http://www.example.com?biz=baz&boz=code&foo=stuff'
    assert update_query_params(URL, dict(foo='stuff', boz='code', bar='baz')) == 'http://www.example.com?bar=baz&biz=baz&boz=code&foo=stuff'

