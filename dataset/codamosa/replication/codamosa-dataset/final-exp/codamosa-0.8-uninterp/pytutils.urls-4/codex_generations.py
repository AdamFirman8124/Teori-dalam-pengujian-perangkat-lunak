

# Generated at 2022-06-14 06:46:13.195106
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:46:17.582507
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'crap': 'poop'}) == 'http://example.com?biz=baz&crap=poop&foo=stuff'

# Generated at 2022-06-14 06:46:20.777361
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com?foo=bar&biz=baz&test=testparam' == update_query_params('http://example.com?foo=bar&biz=baz', dict(test='testparam'))
    assert 'http://example.com?foo=stuff&biz=baz' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:46:26.116233
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:46:35.211153
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    url = update_query_params(url, params)

    assert url == 'http://example.com?foo=stuff&biz=baz', 'Check modified URL with params'

    # Test by adding a new param
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'bop': 'bap'}
    url = update_query_params(url, params)

    assert url == 'http://example.com?foo=bar&biz=baz&bop=bap', 'Check modified URL with new param'

# Generated at 2022-06-14 06:46:39.834621
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:46:43.572741
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://localhost:5000?foo=bar&biz=baz', dict(foo='stuff')) == 'http://localhost:5000?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:46:46.813877
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:46:50.145372
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:46:58.963495
# Unit test for function update_query_params
def test_update_query_params():
    original_url = 'http://example.com?foo=bar&biz=baz'
    updated_url = update_query_params(original_url, {'foo': 'stuff'})
    assert 'foo=stuff' in updated_url, "Should have updated the foo parameter"
    assert 'biz=baz' in updated_url, "Should not have removed other parameters"
    assert updated_url.startswith('http://example.com?'), "Should have preserved the original host and path"



# Generated at 2022-06-14 06:47:09.325266
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?foo=stuff&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff', biz='buz'))
    assert new_url == 'http://example.com?foo=stuff&biz=buz'



# Generated at 2022-06-14 06:47:22.284237
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'

    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'

    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff', new_param='new_value')) == 'http://example.com?foo=stuff&biz=baz&new_param=new_value'


#print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', new_param='new_value')))

# Generated at 2022-06-14 06:47:29.775113
# Unit test for function update_query_params
def test_update_query_params():
    url1 = 'http://example.com?foo=bar&biz=baz'
    url2 = 'http://example.com?foo=bar&biz=baz'
    print("Test 1: ", update_query_params(url1, dict(foo='stuff')))
    print("Test 2: ", update_query_params(url2, dict(foo='stuff', baz='mam')))

test_update_query_params()

# Generated at 2022-06-14 06:47:40.297009
# Unit test for function update_query_params
def test_update_query_params():

    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=baz&foo=stuff'

    params = dict(foo='stuff', biz='buzz')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=buzz&foo=stuff'

    params = dict(biz='buzz')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=buzz&foo=bar'

    url = 'http://example.com'
    params = dict(foo='stuff')
    new_url

# Generated at 2022-06-14 06:47:47.189271
# Unit test for function update_query_params
def test_update_query_params():
    input_url = 'https://api.twitter.com/1.1/trends/place.json?id=1'
    parameters = dict(woeid=123)
    expected_result = input_url.format(woeid=123)
    result = update_query_params(input_url, parameters)
    assert result == expected_result


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:47:56.407446
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz='bars')) == 'http://example.com?baz=bars&biz=baz&foo=stuff'

# Generated at 2022-06-14 06:48:07.100006
# Unit test for function update_query_params
def test_update_query_params():
    # One new parameter
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    # Multiple new parameters
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', foo2='stuff2')) == 'http://example.com?biz=baz&foo=stuff&foo2=stuff2'
    # New parameter in an empty query
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    # Empty query

# Generated at 2022-06-14 06:48:19.929663
# Unit test for function update_query_params
def test_update_query_params():
    """
    When we pass a url, a parameter and a new value, the function must return the same url but with the updated value.
    """
    url = "http://localhost:8080/rest/history?a=b&c=d"
    params = {'a': 'x'}
    new_url = update_query_params(url, params)

    assert 'a=x' in new_url

    params = {'a': 'x', 'c': 'z'}
    new_url = update_query_params(url, params)

    assert 'a=x' in new_url
    assert 'c=z' in new_url
    assert 'a=b' not in new_url
    assert 'c=d' not in new_url


# Generated at 2022-06-14 06:48:24.965025
# Unit test for function update_query_params
def test_update_query_params():
    # TODO: add more tests (for query parameters, ...)
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'


# Modified from https://gist.github.com/botofante/5429462

# Generated at 2022-06-14 06:48:38.608474
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'baz': 'stuff'}) == 'http://example.com?baz=stuff&biz=baz&foo=stuff'
    assert update_query_params('http://example.com', {'foo': 'stuff', 'baz': 'stuff'}) == 'http://example.com?baz=stuff&foo=stuff'

# Generated at 2022-06-14 06:48:48.391088
# Unit test for function update_query_params
def test_update_query_params():
    
    URL_1 = 'http://example.com?foo=bar&biz=baz'
    URL_2 = update_query_params(URL_1, dict(foo='stuff'))
    print(URL_2)
    assert URL_2 == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:48:57.850393
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='stuff')) == 'http://example.com?biz=stuff&foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(baz='stuff')) == 'http://example.com?baz=stuff&biz=baz&foo=bar'

# Generated at 2022-06-14 06:49:11.028439
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == "http://example.com?biz=baz&foo=stuff"
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff&biz=other')) == "http://example.com?biz=baz&foo=stuff%26biz%3Dother"
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='other')) == "http://example.com?biz=other&foo=stuff"
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz=['other', 'other2']))

# Generated at 2022-06-14 06:49:23.557857
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', {'foo': 'stuff'}) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == \
                                                                                         'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz&biz=boz', {'foo' : 'stuff', 'biz': 'bak'}) == \
                                                                                                    'http://example.com?biz=bak&foo=stuff'

# Generated at 2022-06-14 06:49:28.082794
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'


# ==============================================================================
# IndexFile
# ==============================================================================

# Generated at 2022-06-14 06:49:39.621717
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://localhost?foo=bar&biz=baz'
    assert update_query_params(url, dict(foo='stuff')) == "http://localhost?foo=stuff&biz=baz"
    assert update_query_params(url, dict(biz='stuff')) == "http://localhost?foo=bar&biz=stuff"
    assert update_query_params(url, dict(foobar='stuff')) == "http://localhost?foo=bar&biz=baz&foobar=stuff"
    assert update_query_params(url, dict(foo='stuff', foobar='stuff')) == "http://localhost?foo=stuff&biz=baz&foobar=stuff"



# Generated at 2022-06-14 06:49:47.658759
# Unit test for function update_query_params
def test_update_query_params():
    assert "http://example.com?foo=stuff&biz=baz" == \
            update_query_params("http://example.com?foo=bar&biz=baz", dict(foo='stuff'))
    assert "http://example.com?foo=stuff&biz=baz" == \
            update_query_params("http://example.com?foo=bar&biz=baz", {'foo':'stuff'})



# Generated at 2022-06-14 06:50:00.708875
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("http://example.com?foo=bar&biz=baz",dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params("http://example.com?foo=bar&biz=baz",dict(foo='stuff',buzz='bzz')) == 'http://example.com?biz=baz&buzz=bzz&foo=stuff'
    assert update_query_params("http://example.com?foo=bar&biz=baz",dict(foo='stuff',x=["y","z"])) == 'http://example.com?biz=baz&foo=stuff&x=y&x=z'

# Generated at 2022-06-14 06:50:05.315769
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:50:11.794797
# Unit test for function update_query_params
def test_update_query_params():
    """
    Check the update_query_params function
    """
    expected = 'http://example.com?foo=stuff&biz=baz'
    result = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert result == expected

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:50:28.019020
# Unit test for function update_query_params
def test_update_query_params():
    url = update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'})
    print(url)
    # Should print http://example.com?foo=stuff&biz=baz

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:50:35.645734
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/index.html?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com/index.html?foo=stuff&biz=baz'

    url = 'http://example.com/index.html'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com/index.html?foo=stuff'

    url = 'http://example.com/index.html?foo=bar&foo=bar'
    new_url = update_query_params(url, dict(foo=['stuff', 'things']))

# Generated at 2022-06-14 06:50:42.403798
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, dict(qux='quux')) == 'http://example.com?biz=baz&foo=bar&qux=quux'



# Generated at 2022-06-14 06:50:47.509074
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    updated_url = update_query_params(url, {'foo': 'stuff'})
    assert updated_url == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:51:00.267457
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> test_update_query_params()
    """
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff','things'])) == 'http://example.com?biz=baz&foo=stuff&foo=things'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff','things']), doseq=False) == 'http://example.com?biz=baz&foo=things'

# Generated at 2022-06-14 06:51:10.671250
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    result = update_query_params(url, params)
    expected = 'http://example.com?biz=baz&foo=stuff'
    assert result == expected, 'Expected {}, got {}'.format(expected, result)
    params = dict(toto='titi')
    result = update_query_params(url, params)
    expected = 'http://example.com?biz=baz&foo=bar&toto=titi'
    assert result == expected, 'Expected {}, got {}'.format(expected, result)
    result = update_query_params(url, params, False)
    expected = 'http://example.com?biz=baz&foo=bar&toto=titi'

# Generated at 2022-06-14 06:51:16.736475
# Unit test for function update_query_params
def test_update_query_params():
    # 'http://example.com?foo=bar&biz=baz'
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert 'http://example.com?biz=baz&foo=stuff' == update_query_params(url, params)



# Generated at 2022-06-14 06:51:21.374681
# Unit test for function update_query_params
def test_update_query_params():
    # URL string with all 5 components
    url = 'http://example.com/path?foo=bar&biz=baz#fragment'

    # Expected result
    expected = 'http://example.com/path?foo=stuff&biz=baz#fragment'

    # Update foo=bar to foo=stuff
    result = update_query_params(url, dict(foo='stuff'))

    # Should give the expected result
    assert(result==expected)

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:51:30.577203
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com?foo=bar&biz=baz' == update_query_params('http://example.com?foo=bar&biz=baz', {})
    assert 'http://example.com?foo=stuff&biz=baz' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert 'http://example.com?foo=stuff,stuff&biz=baz' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff','stuff']))


if __name__ == '__main__':
    test_update_query_params()
    print('Test OK')

# Generated at 2022-06-14 06:51:34.717052
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:52:05.164632
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com?foo=stuff' == update_query_params('http://example.com?foo=bar', dict(foo='stuff'))
    assert 'http://example.com?foo=stuff' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert 'http://example.com?foo=stuff&biz=baz' == update_query_params('http://example.com?biz=baz', dict(foo='stuff'))
    assert 'http://example.com?foo=stuff&biz=baz' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))

test_update_query_params()

# Generated at 2022-06-14 06:52:10.386063
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?foo=stuff&biz=baz'

test_update_query_params()

# Generated at 2022-06-14 06:52:15.792403
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
        'http://example.com?biz=baz&foo=stuff'
    print("Test passed")

# Call test function
test_update_query_params()

# Generated at 2022-06-14 06:52:18.994938
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com/?foo=stuff&biz=baz'


# Generated at 2022-06-14 06:52:22.851466
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:52:35.854092
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='buzz')) == 'http://example.com?foo=stuff&biz=buzz'
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(biz='buzz')) == 'http://example.com?foo=bar&biz=buzz'
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:52:40.437102
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com' \
                                                                                       '?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:52:51.637406
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'

    assert update_query_params(url, dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, dict(foo='stuff', biz='buzz')) == 'http://example.com?biz=buzz&foo=stuff'
    assert update_query_params(url, dict(foo='stuff', biz='buzz', jim='jam')) == 'http://example.com?biz=buzz&foo=stuff&jim=jam'
    assert update_query_params(url, dict(foo='stuff', biz='buzz', jim='jam')) == 'http://example.com?biz=buzz&foo=stuff&jim=jam'
   

# Generated at 2022-06-14 06:52:59.743151
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://www.example.com/foo/bar?a=5"
    params = {'a': 10, 'b': 20}
    new_url = update_query_params(url, params)

    assert new_url == "http://www.example.com/foo/bar?a=10&b=20"
    assert update_query_params("http://www.example.com/foo/bar?a=5", params) == "http://www.example.com/foo/bar?a=10&b=20"



# Generated at 2022-06-14 06:53:05.518925
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

#print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))) # http://example.com?biz=baz&foo=stuff

# Generated at 2022-06-14 06:53:52.506113
# Unit test for function update_query_params
def test_update_query_params():
    test_url = 'http://example.com?foo=bar&bar=baz'
    test_update = dict(foo='stuff', bar='morestuff')

    assert update_query_params(test_url, test_update) == 'http://example.com?bar=morestuff&foo=stuff'

update_query_params.__test__ = False

# Generated at 2022-06-14 06:53:57.884584
# Unit test for function update_query_params
def test_update_query_params():
    test_url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(test_url, {'foo': 'stuff'}) == expected_url



# Generated at 2022-06-14 06:54:09.921563
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', None,) == 'http://example.com'
    assert update_query_params('http://example.com', params = None,) == 'http://example.com'
    assert update_query_params('http://example.com', params = {'foo':'stuff'}) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com', params = {'foo':'stuff', 'biz':'buzz'}) == 'http://example.com?foo=stuff&biz=buzz'
    assert update_query_params('http://example.com?biz=buzz', params = {'foo':'stuff'}) == 'http://example.com?biz=buzz&foo=stuff'

# Generated at 2022-06-14 06:54:13.689072
# Unit test for function update_query_params
def test_update_query_params():
    assert (update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff')

# Generated at 2022-06-14 06:54:23.781463
# Unit test for function update_query_params
def test_update_query_params():
    params = {
        "k1": "v1",
        "k2": "v2",
        "k3": "v3"
    }
    url = "http://somewhere.com/someapp/resource/OBJECT-ID?k1=v1&k3=v3"
    new_url = update_query_params(url, params)
    assert new_url == "http://somewhere.com/someapp/resource/OBJECT-ID?k1=v1&k2=v2&k3=v3"



# Generated at 2022-06-14 06:54:29.611839
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz'


# Generated at 2022-06-14 06:54:36.256826
# Unit test for function update_query_params
def test_update_query_params():
    url = "https://www.example.com/foo/?type=l1&view=json&reviews=#"
    params = {'a': 'b'}
    assert update_query_params(url, params) ==  "https://www.example.com/foo/?a=b&type=l1&view=json&reviews="

# Generated at 2022-06-14 06:54:45.308156
# Unit test for function update_query_params
def test_update_query_params():
    # Test to check if it updates the url correctly
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    # Test to check if it adds new params if they arent already there
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, dict(baz='somebaz')) == 'http://example.com?biz=baz&baz=somebaz&foo=bar'
    # Test to check if it removes params from the url
    assert update_query_params(url, dict(foo=None)) == 'http://example.com?biz=baz'
    assert update_query_params

# Generated at 2022-06-14 06:54:52.261201
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': ['stuff1', 'stuff2']}) == 'http://example.com?biz=baz&foo=stuff1&foo=stuff2'

# Generated at 2022-06-14 06:54:58.018312
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(xyz=['a', 'b'])) == 'http://example.com?biz=baz&foo=bar&xyz=a&xyz=b'

