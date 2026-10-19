

# Generated at 2022-06-14 06:46:11.804025
# Unit test for function update_query_params
def test_update_query_params():
    result = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert result == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:46:21.460281
# Unit test for function update_query_params
def test_update_query_params():
    params = {"foo": "stuff", "biz": "bang"}
    url = update_query_params('http://example.com?foo=bar&biz=baz', params)
    assert url == 'http://example.com?biz=bang&foo=stuff'
    url = update_query_params('http://example.com?foo=bar&biz=baz', params, doseq=False)
    assert url == 'http://example.com?foo=stuff&biz=bang'
    url = update_query_params('http://example.com?foo=bar&biz=baz', {"foo": "stuff"})
    assert url == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:46:32.113813
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == "http://example.com?foo=stuff&biz=baz"
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff',biz='baz2')) == "http://example.com?foo=stuff&biz=baz2"
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff',biz='baz2',garply='blah')) == "http://example.com?foo=stuff&biz=baz2&garply=blah"


# Generated at 2022-06-14 06:46:36.917001
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz',
                               dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:46:42.392357
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='stuff2')) == 'http://example.com?biz=stuff2&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='stuff2', baz='stuff3')) == 'http://example.com?baz=stuff3&biz=stuff2&foo=stuff'

# Generated at 2022-06-14 06:46:48.854053
# Unit test for function update_query_params
def test_update_query_params():
    url_test = 'http://example.com?foo=bar&biz=baz'
    params_test = dict(foo='stuff')
    new_url_test = update_query_params(url_test, params_test)
    assert (new_url_test == 'http://example.com?foo=stuff&biz=baz')



# Generated at 2022-06-14 06:46:58.187203
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://example.com?foo=bar&biz=baz", {'foo': 'stuff'}) == "http://example.com?foo=stuff&biz=baz"
    assert update_query_params("http://example.com?foo=bar&biz=baz", {'foo': 'stuff', 'biz': 'quux'}) == "http://example.com?foo=stuff&biz=quux"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:47:00.870010
# Unit test for function update_query_params
def test_update_query_params():
    import doctest
    doctest.testmod(verbose=True)

# test_update_query_params()


# Generated at 2022-06-14 06:47:13.795866
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz&biz=buzz', dict(foo='stuff')) == 'http://example.com?biz=baz&biz=buzz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'biz'])) == 'http://example.com?biz=baz&foo=stuff&foo=biz'

# Generated at 2022-06-14 06:47:17.609713
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff')

# Generated at 2022-06-14 06:47:32.382995
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', hello=True)) == 'http://example.com?biz=baz&foo=stuff&hello=True'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', hello=True, biz='a')) == 'http://example.com?biz=a&foo=stuff&hello=True'

# Generated at 2022-06-14 06:47:37.147881
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?%s' % urlencode({'foo': 'stuff', 'biz':'baz'})

# Generated at 2022-06-14 06:47:44.380552
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?name=kong&age=15'
    params = {
        'name':'kong',
        'age':'12'
    }
    assert update_query_params(url, params) == 'http://example.com?name=kong&age=12'

# unit test
if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:47:52.318784
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?bar=baz', dict(foo='stuff')) == 'http://example.com?bar=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'

# Generated at 2022-06-14 06:47:57.925114
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

if __name__ == "__main__":
    test_update_query_params()
    sys.exit(0)

# Generated at 2022-06-14 06:48:08.687314
# Unit test for function update_query_params
def test_update_query_params():
    # Test simple update
    a = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', xyz="123"))
    assert a == 'http://example.com?xyz=123&foo=stuff&biz=baz'

    # Test adding new args
    b = update_query_params('http://example.com?foo=bar&biz=baz', dict(xyz="123"))
    assert b == 'http://example.com?xyz=123&foo=bar&biz=baz'

    # Test overwriting existing args
    c = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff']))
    assert c == 'http://example.com?foo=stuff&biz=baz'

    # Test

# Generated at 2022-06-14 06:48:19.630661
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com', dict(foo=['bar'])) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com', dict(foo=['bar', 'baz'])) == 'http://example.com?foo=bar&foo=baz'



# Generated at 2022-06-14 06:48:29.115986
# Unit test for function update_query_params
def test_update_query_params():
    # test that adding a new parameter to the query params works
    url1 = 'http://example.com?foo=bar&biz=baz'
    url1_with_stuff = update_query_params(url1, dict(stuff='thing'))
    new_query_string = urlparse.urlsplit(url1_with_stuff).query
    assert new_query_string == 'foo=bar&biz=baz&stuff=thing', new_query_string

    # test that modifying one parameter in the query params works
    url1 = 'http://example.com?foo=bar&biz=baz'
    url1_with_stuff = update_query_params(url1, dict(foo='stuff'))
    new_query_string = urlparse.urlsplit(url1_with_stuff).query

# Generated at 2022-06-14 06:48:41.010985
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=None)) == 'http://example.com?biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['biz', 'baz'])) == 'http://example.com?biz=baz&foo=biz&foo=baz'

# Generated at 2022-06-14 06:48:48.596591
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='buzz')) == 'http://example.com?biz=buzz&foo=stuff'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:48:55.596063
# Unit test for function update_query_params
def test_update_query_params():
    """
    Test update_query_params
    """
    test_url = 'http://example.com?type=lemmings&foo=bar&biz=baz'
    expected_url = 'http://example.com?type=lemurs&foo=bar&biz=baz'
    tested_url = update_query_params(test_url, dict(type='lemurs'))

    assert tested_url == expected_url

# Generated at 2022-06-14 06:49:01.283458
# Unit test for function update_query_params
def test_update_query_params():
    params = {'foo': 'stuff'}
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, params)
    assert( new_url == 'http://example.com?foo=stuff&biz=baz')
    
    
    
    
    

# Generated at 2022-06-14 06:49:10.753190
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='stuff2')) == 'http://example.com?foo=stuff&biz=stuff2'
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'

# Generated at 2022-06-14 06:49:20.128074
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar', dict(bar='foo')) == 'http://example.com?bar=foo&foo=bar'
    assert update_query_params('http://example.com?foo=bar&foo=stuff', dict(bar='foo')) == 'http://example.com?bar=foo&foo=bar&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&bar=baz', dict(bar='foo')) == 'http://example.com?bar=foo&foo=bar'



# Generated at 2022-06-14 06:49:24.546042
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff', biz='bacon')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=bacon'



# Generated at 2022-06-14 06:49:36.829162
# Unit test for function update_query_params
def test_update_query_params():
    import itertools

    # Dictionaries with different equality combinations for values
    d1 = dict(a='b', c='d')
    d2 = dict(c='d', a='b')
    d3 = dict(c='d', a='e')
    d4 = dict(d='b', c='d')
    d5 = dict(a='b', c='d', e='f')

    # List of test inputs.

# Generated at 2022-06-14 06:49:45.702367
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'stuff2'])) == 'http://example.com?foo%5B%5D=stuff&foo%5B%5D=stuff2&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='stuff')) == 'http://example.com?foo=bar&biz=stuff'

# Generated at 2022-06-14 06:49:51.020772
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff', 'baz': 'quux'}
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz&baz=quux'

# Generated at 2022-06-14 06:49:56.792251
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar&biz=baz"
    params = dict(foo='stuff')
    result = update_query_params(url, params)
    expected = "http://example.com?biz=baz&foo=stuff"
    assert result == expected

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:50:10.291206
# Unit test for function update_query_params
def test_update_query_params():
    """ Test for the function update_query_params(). """

    # params
    params_test = {'test':'test_val'}
    params_test2 = {'test2':'test_val2'}
    params_test3 = {'test':'test_val3'}
    params_test4 = {'test3':'test_val4'}

    # Test 1: without params
    url_test_1 = 'http://example.com/'
    result_test_1 = update_query_params(url_test_1, params_test)
    expected_result_1 = 'http://example.com/?test=test_val'
    # if equal
    if result_test_1 == expected_result_1:
        print('Test 1: Success!')

# Generated at 2022-06-14 06:50:27.532330
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff',hi='mom')) == 'http://example.com?foo=stuff&biz=baz&hi=mom'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='stuff')) == 'http://example.com?foo=bar&biz=stuff'

# Generated at 2022-06-14 06:50:35.144750
# Unit test for function update_query_params
def test_update_query_params():
    sample_url = "http://example.com?foo=bar&biz=baz"
    expected_updated_url = "http://example.com?foo=stuff&biz=baz"
    updated_url = update_query_params(sample_url, dict(foo='stuff'))
    assert updated_url == expected_updated_url

    sample_url = "http://example.com?foo=bar&biz=baz"
    expected_updated_url = "http://example.com?foo=stuff&biz=bam"
    updated_url = update_query_params(sample_url, dict(foo='stuff', biz='bam'))
    assert updated_url == expected_updated_url



# Generated at 2022-06-14 06:50:39.152315
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:50:46.220636
# Unit test for function update_query_params
def test_update_query_params():
    # Test no query parameters
    assert update_query_params("http://example.com", {}) == "http://example.com"

    # Test new query parameter
    assert update_query_params("http://example.com", {'foo': 'stuff', 'bar': 'baz'}) == "http://example.com?foo=stuff&bar=baz"

    # Test update of existing query parameter
    assert update_query_params("http://example.com?foo=bar", {'foo': 'stuff'}) == "http://example.com?foo=stuff"


# Generated at 2022-06-14 06:50:55.834701
# Unit test for function update_query_params
def test_update_query_params():
    url = "https://www.google.com/search?q=test+python&oq=test+python&aqs=chrome.0.0j69i57j0l4.4273j0&sourceid=chrome&ie=UTF-8"
    assert update_query_params(url, dict(q="pokemon",ie="UTF-16")) == "https://www.google.com/search?q=pokemon&oq=test+python&aqs=chrome.0.0j69i57j0l4.4273j0&sourceid=chrome&ie=UTF-16"



# Generated at 2022-06-14 06:51:08.985702
# Unit test for function update_query_params
def test_update_query_params():
    """
    Tests the update_query_params function.
    :author: Andoni Sooklaris
    :return: None
    """
    # Test normal case
    test_url = "http://example.com?foo=bar&biz=baz"
    params = { "foo" : "stuff", "biz": "buzz" }
    expected_url = "http://example.com?biz=buzz&foo=stuff"
    assert(update_query_params(test_url, params) == expected_url)

    # Test edge case where there was no query params before.
    test_url = "http://example.com"
    params = { "foo" : "stuff", "biz": "buzz" }
    expected_url = "http://example.com?biz=buzz&foo=stuff"

# Generated at 2022-06-14 06:51:15.511446
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://www.example.com/?foo=bar&blah=blah'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://www.example.com/?foo=stuff&blah=blah', new_url


#==============================================================================#


# Generated at 2022-06-14 06:51:27.122919
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar"
    assert update_query_params(url, dict(foo='stuff')) == "http://example.com?foo=stuff"
    url = "http://example.com?foo=bar&biz=baz"
    assert update_query_params(url, dict(foo='stuff')) == "http://example.com?foo=stuff&biz=baz"
    url = "http://example.com?foo=bar&biz=baz"
    assert update_query_params(url, dict(foo='stuff', biz='hey')) == "http://example.com?foo=stuff&biz=hey"
    url = "http://example.com?foo=bar&biz=baz"

# Generated at 2022-06-14 06:51:37.010573
# Unit test for function update_query_params
def test_update_query_params():
    url1 = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    newurl1 = update_query_params(url1, params)

    url2 = 'https://example.com:8080/stuff/index.html?foo=bar&biz=baz#frag'
    params = dict(foo='stuff')
    newurl2 = update_query_params(url2, params)

    url3 = 'https://example.com:8080/stuff/index.html?foo=bar&biz=baz#frag'
    params = dict(foo='stuff', biz='otherstuff')
    newurl3 = update_query_params(url3, params)


# Generated at 2022-06-14 06:51:45.906442
# Unit test for function update_query_params
def test_update_query_params():
    print ("test_update_query_params starting")

    url = "http://example.com?foo=bar&biz=baz"
    params = {'foo':'stuff','foo2':'stuff2'}

    url = update_query_params(url,params)
    print (url)
    #assert url=='http://example.com?...foo=stuff...'

    print ("test_update_query_params complete")


"""
http://stackoverflow.com/questions/9070604/how-to-obtain-a-query-string-given-a-url
"""

# Generated at 2022-06-14 06:51:59.505338
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    
test_update_query_params()
 


# Generated at 2022-06-14 06:52:10.730159
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://localhost:5000/admin/user?page=3&keyword=xx'
    assert(update_query_params(url, {'page': 5}) == 'http://localhost:5000/admin/user?page=5&keyword=xx')
    assert(update_query_params(url, {'page': 5, 'keyword':'yy'}) == 'http://localhost:5000/admin/user?page=5&keyword=yy')
    assert(update_query_params(url, {'keyword':'yy'}) == 'http://localhost:5000/admin/user?page=3&keyword=yy')

test_update_query_params()

# Generated at 2022-06-14 06:52:19.283087
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('https://example.com?foo=bar&biz=baz', dict(foo='stuff'), False) == 'https://example.com?biz=baz&foo=stuff&foo=bar'


# Generated at 2022-06-14 06:52:24.402582
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=baz&foo=stuff', 'Wrong result from update_query_params'

# Generated at 2022-06-14 06:52:31.616563
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz='biz')) == 'http://example.com?baz=biz&biz=baz&foo=stuff'

# Generated at 2022-06-14 06:52:36.331959
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz='buzz')) == 'http://example.com?biz=baz&foo=stuff&baz=buzz')

# Generated at 2022-06-14 06:52:48.364542
# Unit test for function update_query_params

# Generated at 2022-06-14 06:52:53.947099
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'



# Generated at 2022-06-14 06:53:04.062205
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://foo.com?param1=value1&param2=value2", dict(param3="value3")) == "http://foo.com?param1=value1&param2=value2&param3=value3"

    assert update_query_params("http://foo.com?param1=value1&param2=value2", dict(param1="value1-1")) == "http://foo.com?param1=value1-1&param2=value2"

    assert update_query_params("http://foo.com", dict(param1="value1-1")) == "http://foo.com?param1=value1-1"


# Generated at 2022-06-14 06:53:14.312771
# Unit test for function update_query_params
def test_update_query_params():
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')))
    print(update_query_params('http://example.com', dict(foo='stuff')))
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='baz')))

# Dealing with RFC 3986 URI Components
#
# urllib.quote_plus
#     Performs quoting of the query string. Basically does the same thing as
#     urllib.quote, except that it also encodes spaces as plus signs.

# Generated at 2022-06-14 06:53:36.821672
# Unit test for function update_query_params
def test_update_query_params():
    url1 = 'http://example.com?foo=bar&biz=baz'
    url2 = update_query_params(url1, dict(foo='stuff'))
    assert url2 == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:53:46.573264
# Unit test for function update_query_params
def test_update_query_params():
    """
    Testcase for function update_query_params
    """
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    expected_result = 'http://example.com?foo=stuff&biz=baz'
    
    result = update_query_params(url, params, doseq=True)
    assert result == expected_result, 'Function update_query_params not working properly. Actual result: \'{}\', expected result: \'{}\''.format(result, expected_result)


# Generated at 2022-06-14 06:53:57.200821
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://example.com?foo=bar", {'foo': 'biz'}) == "http://example.com?foo=biz"
    assert update_query_params("http://example.com?foo=bar", {'biz': 'baz'}) == "http://example.com?foo=bar&biz=baz"
    assert update_query_params("http://example.com?foo=bar", {'biz': 'baz', 'foo': 'biz'}) == "http://example.com?foo=biz&biz=baz"
    assert update_query_params("http://example.com?foo=bar", {'biz': 'baz', 'foo': 'baz'}) == "http://example.com?foo=baz&biz=baz"

# Generated at 2022-06-14 06:54:01.747588
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')

    updated_url = update_query_params(url, params)
    assert updated_url == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:54:05.882881
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) \
        == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:54:11.901918
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar&biz=baz"
    params = dict(foo='stuff')
    if update_query_params(url, params) == 'http://example.com?foo=stuff&biz=baz':
        print ("test_update_query_params: ", "OK!")
    else:
        print ("test_update_query_params: ", "Test failed!")

#test_update_query_params()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:54:24.160969
# Unit test for function update_query_params
def test_update_query_params():
    base_url = "http://www.example.com"
    path = "/path/to/resource/"
    params = dict(foo="bar", baz="buz")
    url = base_url + path
    new_url = update_query_params(url, params)
    assert new_url == base_url + path + '?' + urlencode(params, doseq=True)

    query_string = "foo=bar&biz=baz"
    url += '?' + query_string
    new_url = update_query_params(url, params)
    assert new_url == base_url + path + '?' + urlencode(params, doseq=True)



# Generated at 2022-06-14 06:54:29.616817
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'

    new_url = update_query_params(url, {'foo': 'stuff'})

    assert new_url == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:54:35.273927
# Unit test for function update_query_params
def test_update_query_params():
    testurl = "http://example.com?foo=bar&biz=baz"
    params = {'foo': 'stuff'}

    expected = "http://example.com?biz=baz&foo=stuff"
    assert update_query_params(testurl, params) == expected

# Generated at 2022-06-14 06:54:44.878667
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff', 'foo2':'stuff'}, False) == 'http://example.com?biz=baz&foo=stuff&foo2=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'a':[1,2,3], 'b':'a'}) == 'http://example.com?a=1&a=2&a=3&biz=baz&foo=bar&b=a'

# Generated at 2022-06-14 06:55:27.014167
# Unit test for function update_query_params
def test_update_query_params():
    url = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert url == 'http://example.com?foo=stuff&biz=baz'


# Generated at 2022-06-14 06:55:37.191720
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('https://example.com/foo?bar=baz', {'bar': 'stuff'}) == 'https://example.com/foo?bar=stuff'
    assert update_query_params('https://example.com/foo?bar=baz&quux=quuux', {'bar': 'stuff'}) == 'https://example.com/foo?bar=stuff&quux=quuux'
    assert update_query_params('https://example.com/foo?bar=baz', {'bar': 'stuff', 'quux': 'quuux'}) == 'https://example.com/foo?bar=stuff&quux=quuux'



# Generated at 2022-06-14 06:55:42.729345
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?a=1&b=2"
    new_url = update_query_params(url, dict(a='3', c=3))
    print(new_url)
    assert new_url == 'http://example.com?a=3&b=2&c=3'


if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:55:49.899065
# Unit test for function update_query_params
def test_update_query_params():
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')))
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'more'])))
    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='stuff')))



# Generated at 2022-06-14 06:55:58.612485
# Unit test for function update_query_params
def test_update_query_params():
    url = 'https://www.google.com/search?q=sise&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=np&source=hp&q=ssise'
    params = {'q':'sise'}
    print(update_query_params(url, params))

test_update_query_params()

# Generated at 2022-06-14 06:56:05.087727
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == "http://example.com?foo=stuff&biz=baz"
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='bar')) == "http://example.com?foo=stuff&biz=baz&bar=bar"

# Generated at 2022-06-14 06:56:15.198712
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == "http://example.com?foo=stuff&biz=baz"
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'baz': 'qux'}) == "http://example.com?foo=stuff&biz=baz&baz=qux"
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'baz': 'qux'}, doseq=False) == "http://example.com?foo=stuff&biz=baz&baz=qux"