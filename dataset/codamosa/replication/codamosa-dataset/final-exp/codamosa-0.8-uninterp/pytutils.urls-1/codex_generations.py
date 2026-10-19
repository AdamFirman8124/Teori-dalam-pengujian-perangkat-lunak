

# Generated at 2022-06-14 06:46:18.893298
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/messages?page=4&count=100'

    test_1 = update_query_params(url, dict(foo='bar'))
    assert test_1 == 'http://example.com/messages?page=4&count=100&foo=bar'

    test_2 = update_query_params(url, dict(page='5'))
    assert test_2 == 'http://example.com/messages?page=5&count=100'

    test_3 = update_query_params(url, dict(page='5', count='101'))
    assert test_3 == 'http://example.com/messages?page=5&count=101'

    test_4 = update_query_params(url, dict(page='6', count='102'))

# Generated at 2022-06-14 06:46:29.753197
# Unit test for function update_query_params
def test_update_query_params():
    assert (update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))) == 'http://example.com?biz=baz&foo=stuff'
    assert (update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='new'))) == 'http://example.com?biz=new&foo=stuff'
    assert (update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff']))) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:46:37.000985
# Unit test for function update_query_params
def test_update_query_params():
    url = 'https://api.box.com/2.0/files/4894423861'
    url_modified = update_query_params(url, {'fields': 'sha1,created_at'})
    assert url_modified == 'https://api.box.com/2.0/files/4894423861?fields=sha1%2Ccreated_at'
    url = 'https://api.box.com/2.0/files/4894423861?fields=sha1%2Ccreated_at'
    url_modified = update_query_params(url, {'fields': 'name,size'})
    assert url_modified == 'https://api.box.com/2.0/files/4894423861?fields=name%2Csize'

# Generated at 2022-06-14 06:46:42.433931
# Unit test for function update_query_params
def test_update_query_params():
    url1 = 'http://example.com/my/path?foo=bar&biz=baz'
    res1 = 'http://example.com/my/path?foo=bar&biz=baz'

    url2 = 'http://example.com/my/path?foo=bar&biz=baz'
    res2 = 'http://example.com/my/path?foo=stuff&biz=baz'

    url3 = 'http://example.com/my/path?foo=bar&biz=baz'
    res3 = 'http://example.com/my/path?foo=bar&biz=stuff'

    url4 = 'http://example.com/my/path?foo=bar&biz=baz'
    res4 = 'http://example.com/my/path?foo=stuff&biz=stuff'

   

# Generated at 2022-06-14 06:46:50.310719
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'


if __name__ == "__main__":
    print("Running unit tests for {} ...".format(__file__))
    print("--------------------------------------------------")
    print("update_query_params:")
    test_update_query_params()

# Generated at 2022-06-14 06:46:55.911431
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    expected = 'http://example.com?foo=stuff&biz=baz'
    result = update_query_params(url, params)
    assert result == expected


# Generated at 2022-06-14 06:47:03.009663
# Unit test for function update_query_params
def test_update_query_params():
    assert "http://example.com?foo=stuff&biz=baz" == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert "http://example.com?foo=stuff&biz=baz" == update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'})



# Generated at 2022-06-14 06:47:06.867459
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:47:13.224763
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, {'foo':'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, {'foo':'stuff', 'biz':'bang'}) == 'http://example.com?biz=bang&foo=stuff'

# Generated at 2022-06-14 06:47:21.340460
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(None, None) == ''
    assert update_query_params('', None) == ''
    assert update_query_params('/', None) == '/'
    assert update_query_params('/', '') == '/'
    assert update_query_params('/?', '') == '/?#'
    assert update_query_params('http://example.com/path', None) == 'http://example.com/path#'
    assert update_query_params('http://example.com/?foo=bar&biz=baz', None) == 'http://example.com/?foo=bar&biz=baz#'
    assert update_query_params('http://example.com/?foo=bar&biz=baz', '') == 'http://example.com/?foo=bar&biz=baz#'

# Generated at 2022-06-14 06:47:27.519699
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:47:34.554758
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    new_url = update_query_params(url, params, doseq=True)
    assert new_url == 'http://example.com?biz=baz&foo=stuff'


# Shortcut function to get a URL with a modified query string

# Generated at 2022-06-14 06:47:40.530311
# Unit test for function update_query_params
def test_update_query_params():
    url = 'https://map.stamen.com/watercolor?lat=-23.56&lon=-46.64'
    original_params = urlparse.parse_qs(urlparse.urlsplit(url).query)

    params = {'lat': '-23.56'}
    update_query_params(url, params)

# Generated at 2022-06-14 06:47:50.637534
# Unit test for function update_query_params
def test_update_query_params():
    """
    Testing the update_query_params function.
    """
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'

    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='bizness')) == 'http://example.com?foo=stuff&biz=bizness'

    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(xxx='yyy')) == 'http://example.com?foo=bar&biz=baz&xxx=yyy'


# Generated at 2022-06-14 06:47:55.947879
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    updated_url = update_query_params(url, {'foo': 'stuff'})
    assert updated_url == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:48:04.910538
# Unit test for function update_query_params
def test_update_query_params():
    test_dict = {
        'http://example.com?foo=bar&biz=baz': {'foo': 'stuff'},
        'http://example.com?foo=bar&biz=baz': {'foo': 'stuff', 'fizz': 'buzz'},
        'http://example.com?foo=bar&biz=baz': {'foo': ['stuff', 'fizz']},
    }
    for url, params in test_dict.items():
        new_url = update_query_params(url, params)
        assert new_url != url

# Generated at 2022-06-14 06:48:15.932589
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        url='http://localhost:8000/api/v1/project',
        params={'foo': 'stuff'},
    ) == 'http://localhost:8000/api/v1/project?foo=stuff'
    assert update_query_params(
        url='http://localhost:8000/api/v1/project?foo=bar&biz=baz',
        params={'foo': 'stuff'},
    ) == 'http://localhost:8000/api/v1/project?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:48:24.912471
# Unit test for function update_query_params
def test_update_query_params():
    # test the functionality of update_query_params
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz'
    # test the functionality of update_query_params when it is used with a dict containing a list
    params = dict(foo=['stuff', 'stuff2'])
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&foo=stuff2&biz=baz'
    params = dict(foo=['stuff', 'stuff2'])
    new_url = update_query_params(url, params, True)

# Generated at 2022-06-14 06:48:32.039161
# Unit test for function update_query_params
def test_update_query_params():
    # given
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_result = 'http://example.com?foo=stuff&biz=baz'
    
    # when
    result = update_query_params(url, params)
    
    # then
    assert result == expected_result



# Generated at 2022-06-14 06:48:42.526134
# Unit test for function update_query_params
def test_update_query_params():
    # Check that a new query parameter is added
    url = 'https://127.0.0.1:5000/v3/auth/tokens?nocatalog'
    params = {'OS-FEDERATION':'saml2'}
    modified_url = update_query_params(url, params)
    # Check that the new query parameter is correctly inserted in the URL
    assert modified_url == 'https://127.0.0.1:5000/v3/auth/tokens?OS-FEDERATION=saml2&nocatalog'

    # Check that a query parameter is updated
    url = 'https://127.0.0.1:5000/v3/auth/tokens?OS-FEDERATION=saml2&nocatalog'

# Generated at 2022-06-14 06:48:48.862908
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'

# Generated at 2022-06-14 06:48:58.054121
# Unit test for function update_query_params
def test_update_query_params():
    assert (update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff')
    assert (update_query_params('https://example.com?foo=bar', dict(foo='stuff')) == 'https://example.com?foo=stuff')
    assert (update_query_params('ftp://example.com?foo=bar', dict(foo='stuff')) == 'ftp://example.com?foo=stuff')
    assert (update_query_params('example.com', dict(foo='stuff')) == 'example.com?foo=stuff')
    assert (update_query_params('example.com?', dict(foo='stuff')) == 'example.com?foo=stuff')

# Generated at 2022-06-14 06:49:11.069033
# Unit test for function update_query_params
def test_update_query_params():
    query_params = {'foo': 'stuff'}
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, query_params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz'

    url = 'https://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, query_params)
    assert new_url == 'https://example.com?foo=stuff&biz=baz'

    query_params = {'foo': 'stuff', 'biz':'baz'}
    url = 'http://example.com?'
    new_url = update_query_params(url, query_params)

# Generated at 2022-06-14 06:49:16.929570
# Unit test for function update_query_params
def test_update_query_params():
    """
    Test function update_query_params
    :return:
    """
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

test_update_query_params()

# Generated at 2022-06-14 06:49:28.923382
# Unit test for function update_query_params
def test_update_query_params():
    import json
    assert update_query_params("https://example.com?foo=bar&biz=baz", dict(foo='stuff')) == "https://example.com?foo=stuff&biz=baz"
    assert update_query_params("https://example.com?foo=bar&biz=baz", dict(foo='stuff', baz='baf')) == "https://example.com?foo=stuff&biz=baz&baz=baf"

# Generated at 2022-06-14 06:49:41.476415
# Unit test for function update_query_params
def test_update_query_params():
    test_url = 'http://example.com?foo=bar&biz=baz'
    assert(update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'}) == 'http://example.com?foo=stuff&biz=baz')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'hi':'mom'}) == 'http://example.com?biz=baz&foo=stuff&hi=mom')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff', 'hi': 'mom'}, doseq=False) == 'http://example.com?biz=baz&foo=stuff&hi=mom')

# Generated at 2022-06-14 06:49:54.086864
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://www.example.com/?foo=bar&baz=biz'
    params = {'foo': 'stuff'}
    actual_result = update_query_params(url, params, doseq=False)
    expected_result = 'http://www.example.com/?foo=stuff&baz=biz'
    assert (actual_result == expected_result)


if __name__ == '__main__':
    import sys
    import nose

# Generated at 2022-06-14 06:49:59.038521
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected = 'http://example.com?foo=stuff&biz=baz'
    actual = update_query_params(url, dict(foo='stuff'))
    assert actual == expected

# Generated at 2022-06-14 06:50:05.560463
# Unit test for function update_query_params
def test_update_query_params():
    """Test updating the query parameters in a URL."""
    foo_dict = {'foo': 'stuff'}
    url = update_query_params('http://example.com?foo=bar&biz=baz', foo_dict)
    assert "foo=stuff" in url
    assert "biz=baz" in url


# Generated at 2022-06-14 06:50:14.764764
# Unit test for function update_query_params
def test_update_query_params():
    # Test 1:
    test_url = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert test_url == 'http://example.com?foo=stuff&biz=baz'
    # Test 2:
    test_url = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', qaz='qux'))
    assert test_url == 'http://example.com?foo=stuff&biz=baz&qaz=qux'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:50:26.124597
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo' : 'stuff'}
    assert update_query_params(url, params) == 'http://example.com?foo=stuff&biz=baz'
    print('Passed')
    print('Documentation Test: ' + update_query_params.__doc__)


# Generated at 2022-06-14 06:50:31.565158
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'


# Generated at 2022-06-14 06:50:35.353127
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    assert 'foo=stuff' in update_query_params(url, dict(foo='stuff'))

# Generated at 2022-06-14 06:50:40.774465
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:50:52.228566
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='stuff')) == 'http://example.com?biz=stuff&foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff'])) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:51:02.904339
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params("https://api.data.gov/ed/collegescorecard/v1/schools.json?school.name=harvard&api_key=XXXXXXXXXXX", {'_fields': 'school.name,school.degrees_awarded.predominant'}) == 'https://api.data.gov/ed/collegescorecard/v1/schools.json?school.name=harvard&_fields=school.name,school.degrees_awarded.predominant&api_key=XXXXXXXXXXX'
test_update_query_params()

# Generated at 2022-06-14 06:51:08.264812
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    updated_url = 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, params) == updated_url


# Generated at 2022-06-14 06:51:22.112934
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz&foo=stuff', dict(foo='otherstuff')) == 'http://example.com?biz=baz&foo=otherstuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='otherstuff')) == 'http://example.com?foo=otherstuff&biz=baz'

# Generated at 2022-06-14 06:51:30.147500
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='baz', hello='world')) == 'http://example.com?biz=baz&foo=stuff&hello=world'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff, thing')) == 'http://example.com?biz=baz&foo=stuff%2C%20thing'

# Generated at 2022-06-14 06:51:35.837100
# Unit test for function update_query_params

# Generated at 2022-06-14 06:51:51.691049
# Unit test for function update_query_params
def test_update_query_params():
    foobar_url = 'http://example.com?foo=bar&biz=baz'
    assert 'http://example.com?foo=stuff&biz=baz' == update_query_params(foobar_url, dict(foo='stuff'))



# Generated at 2022-06-14 06:52:03.437624
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?biz=baz&foo=stuff'
    new_url = update_query_params(url, {'foo': 'stuff'})
    assert new_url == expected_url
    new_url = update_query_params(url, {'foo': 'stuff', 'test': 'me'})
    assert new_url == 'http://example.com?biz=baz&foo=stuff&test=me'
    new_url = update_query_params(url, {'foo': ['stuff', 'me']}, False)
    assert new_url == 'http://example.com?biz=baz&foo=stuff&foo=me'

# Generated at 2022-06-14 06:52:10.576560
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?a=1&b=1&c=1'
    expected = 'http://example.com?a=2&b=2&c=1'
    new_url = update_query_params(url, {'a': '2', 'b': '2'})
    assert new_url == expected

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:52:14.608384
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:52:19.363549
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_result = 'http://example.com?biz=baz&foo=stuff'
    params = {'foo': 'stuff'}
    result = update_query_params(url, params)
    assert expected_result == result
    

# Generated at 2022-06-14 06:52:24.610540
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?foo=stuff&biz=baz'

test_update_query_params()

# Generated at 2022-06-14 06:52:36.472135
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='boaz')) == 'http://example.com?biz=boaz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'booz'])) == 'http://example.com?biz=baz&foo=stuff&foo=booz'

# Generated at 2022-06-14 06:52:47.495468
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/foo?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com/foo?biz=baz&foo=stuff'
    # Test that using a dict(list) as the params argument still works,
    # since the function used to break with this.
    params = dict(foo=['bar', 'baz'])
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com/foo?foo=bar&foo=baz&biz=baz'



# Generated at 2022-06-14 06:52:52.206829
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:53:00.300196
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', piz='paz')) == 'http://example.com?biz=baz&foo=stuff&piz=paz'

#if __name__ == '__main__':
#    test_update_query_params()

# Generated at 2022-06-14 06:53:23.781426
# Unit test for function update_query_params
def test_update_query_params():
    url1 = 'http://example.com?foo=bar&biz=baz'
    url2 = 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(url1, dict(foo='stuff')) == url2


# Generated at 2022-06-14 06:53:36.671578
# Unit test for function update_query_params
def test_update_query_params():
    # Check that the same parameters are replaced
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff'])) == 'http://example.com?biz=baz&foo=stuff')
    assert(update_query_params('http://example.com?foo=bar&biz=baz', {'foo': ['stuff']}) == 'http://example.com?biz=baz&foo=stuff')

# Generated at 2022-06-14 06:53:49.642664
# Unit test for function update_query_params
def test_update_query_params():
    params1 = {"foo": "bar", "biz": "baz"}
    params2 = {"foo": "stuff"}

    assert update_query_params('http://example.com', params1) == "http://example.com?foo=bar&biz=baz"
    assert update_query_params('http://example.com', params2) == "http://example.com?foo=stuff"
    assert update_query_params('http://example.com?foo=bar&biz=baz', params2) == "http://example.com?foo=stuff&biz=baz"
    assert update_query_params('http://example.com?foo=bar&biz=baz', params1) == "http://example.com?foo=bar&biz=baz"


if __name__ == '__main__':
    test_update_

# Generated at 2022-06-14 06:54:01.212111
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> test_update_query_params()
    """

    def get(url):
        return urlparse.urlparse(url).query

    def check(url, params, expected_query, doseq):
        modified_url = update_query_params(url, params, doseq)
        modified_query = get(modified_url)
        assert modified_query == expected_query,  modified_query + ' != ' + expected_query

    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff', hello='world')
    expected_query = urlencode(params)
    check(url, params, expected_query, True)


# Generated at 2022-06-14 06:54:05.823731
# Unit test for function update_query_params
def test_update_query_params():
    assert 'https://example.com?foo=stuff&biz=baz' == update_query_params('https://example.com?foo=bar&biz=baz', dict(foo='stuff'))

test_update_query_params()

# Generated at 2022-06-14 06:54:13.183760
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))=='http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz='ttt')) == 'http://example.com?biz=baz&baz=ttt&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz=['123', '456'])) == 'http://example.com?biz=baz&baz=123&baz=456&foo=stuff'

# Generated at 2022-06-14 06:54:20.929319
# Unit test for function update_query_params
def test_update_query_params():
    url = update_query_params('http://example.com', {'foo':'bar'})
    assert url == 'http://example.com?foo=bar'
    url = update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'})
    assert url == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:54:25.245025
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://localhost:8080/test'
    params = dict(token='TEST')
    new_url = update_query_params(url, params, doseq=False)
    assert new_url == 'http://localhost:8080/test?token=TEST'

# Generated at 2022-06-14 06:54:29.615143
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com/?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:54:34.008946
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:55:02.186394
# Unit test for function update_query_params
def test_update_query_params():
    url='http://example.com?foo=bar'
    new_url=update_query_params(url,{'foo':'stuff'})
    assert new_url=='http://example.com?foo=stuff'


# Unit test to preserve original values if doseq=True

# Generated at 2022-06-14 06:55:13.491720
# Unit test for function update_query_params
def test_update_query_params():
    from nose.tools import eq_
    eq_('http://example.com?foo=stuff&biz=baz', update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')))
    eq_('http://example.com?foo=stuff&biz=baz', update_query_params('http://example.com?foo=bar&biz=baz', foo='stuff'))



if __name__ == '__main__':
    import sys
    import doctest

    status = 0
    if len(sys.argv) == 1:
        # Run unit tests when there are no arguments
        status = doctest.testmod()[0]
    else:
        # Otherwise, execute the utility functions.
        func = globals()[sys.argv[1]]

# Generated at 2022-06-14 06:55:18.609892
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'


# Syntax sugar

# Generated at 2022-06-14 06:55:29.522378
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='fuzz')) == 'http://example.com?biz=fuzz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='fuzz', fiz='buzz')) == 'http://example.com?biz=fuzz&fiz=buzz&foo=stuff'

# Generated at 2022-06-14 06:55:34.122966
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:55:40.189198
# Unit test for function update_query_params
def test_update_query_params():
    assert u'http://example.com?foo=stuff&biz=baz' == update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'})

if __name__ == "__main__":
    test_update_query_params()
    #print(update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'}))

# Generated at 2022-06-14 06:55:46.998425
# Unit test for function update_query_params
def test_update_query_params():

    # Test URL parsing
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com/', dict(foo='bar')) == 'http://example.com/?foo=bar'
    assert update_query_params('http://example.com/?', dict(foo='bar')) == 'http://example.com/?foo=bar'
    assert update_query_params('http://example.com/foo', dict(foo='bar')) == 'http://example.com/foo?foo=bar'
    assert update

# Generated at 2022-06-14 06:55:54.615000
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', new='params')) == 'http://example.com?biz=baz&foo=stuff&new=params'


# Generated at 2022-06-14 06:56:07.181356
# Unit test for function update_query_params
def test_update_query_params():
    url = update_query_params('http://example.com?foo=bar&biz=baz',
                              dict(foo='stuff'))
    assert url == "http://example.com?biz=baz&foo=stuff"
    url = update_query_params('http://example.com?foo=bar&biz=baz',
                              dict(foo='stuff', bar=['baz', 'blarh']))
    assert url == "http://example.com?bar=baz&bar=blarh&biz=baz&foo=stuff"

# Dict of query parameters, for constructing URLs