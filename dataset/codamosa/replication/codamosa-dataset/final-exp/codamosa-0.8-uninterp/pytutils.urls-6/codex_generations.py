

# Generated at 2022-06-14 06:46:12.904727
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert update_query_params(url, params) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:46:16.134753
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:46:29.372523
# Unit test for function update_query_params
def test_update_query_params():

    # update_query_params with no existing params
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com', dict(foo='stuff', baz='barz', more='stuff')) == 'http://example.com?more=stuff&baz=barz&foo=stuff'

    # update existing param
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params

# Generated at 2022-06-14 06:46:33.889763
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:46:47.027203
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff&more')) == 'http://example.com?biz=baz&foo=stuff%26more'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff','more'])) == 'http://example.com?biz=baz&foo=stuff&foo=more'

# Generated at 2022-06-14 06:46:51.947405
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    updated_url = update_query_params(url, params)
    assert updated_url == 'http://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:46:59.325364
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'), doseq=False) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff']), doseq=False) == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:47:12.517458
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    'http://example.com?...foo=stuff...'
    """
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', biz='buzz')) == 'http://example.com?biz=buzz&foo=stuff'

# Generated at 2022-06-14 06:47:18.517439
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff', biz='buzz')
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=buzz&foo=stuff'


if __name__ == '__main__':
    import doctest
    (failures, tests) = doctest.testmod()
    if failures > 0:
        raise Exception("%d failures in %d tests" % (failures, tests))

# Generated at 2022-06-14 06:47:23.588478
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz',
        dict(foo='stuff', biz='bar')) == 'http://example.com?biz=bar&foo=stuff'

# Generated at 2022-06-14 06:47:32.577373
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    expected = 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, params) == expected

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:47:41.014931
# Unit test for function update_query_params
def test_update_query_params():
    # case 1
    output_1 = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    exp_1 = 'http://example.com?biz=baz&foo=stuff'
    assert output_1 == exp_1

    # case 2
    output_2 = update_query_params('http://example.com?foo=bar&biz=baz', dict(a='1', b='2'))
    exp_2 = 'http://example.com?a=1&b=2&biz=baz&foo=bar'
    assert output_2 == exp_2


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:47:52.124485
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(
        'http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'
    assert update_query_params(
        'http://example.com?foo=bar', dict(foo='stuff',bar='baz')) == 'http://example.com?bar=baz&foo=stuff'
    assert update_query_params(
        'http://example.com?foo=bar&foo=bar2', dict(foo='stuff')) == 'http://example.com?foo=stuff'

# Generated at 2022-06-14 06:48:04.959886
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'}, False) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo':'stuff'}) == 'http://example.com?biz=baz&foo=stuff'
   

# Generated at 2022-06-14 06:48:11.977589
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com'
    new_url =  update_query_params(url, dict(foo='stuff'))

    assert new_url == 'http://example.com?foo=stuff'

    new_url = update_query_params(url + '?bar=baz', dict(foo='stuff'))

    assert new_url == 'http://example.com?foo=stuff&bar=baz'


if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:48:15.886766
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'



# Generated at 2022-06-14 06:48:27.171055
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'), True) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'), False) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'), True) != 'http://example.com?biz=baz&foo=bar'
    assert update_

# Generated at 2022-06-14 06:48:37.880293
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com:80/one?foo=bar&biz=baz#fragment', dict(foo='stuff')) == 'http://example.com:80/one?biz=baz&foo=stuff#fragment'
    assert update_query_params('http://example.com:80/one?biz=baz&foo=bar#fragment', dict(foo='stuff')) == 'http://example.com:80/one?biz=baz&foo=stuff#fragment'

# Generated at 2022-06-14 06:48:43.366669
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?foo=bar&biz=baz"
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:48:48.461190
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    expected = 'http://example.com?biz=baz&foo=stuff'

    actual = update_query_params(url, params)

    assert actual == expected

# Generated at 2022-06-14 06:48:56.956978
# Unit test for function update_query_params
def test_update_query_params():
    params = {
        'form': 'bar',
        'foo': 'biz'
    }
    url = 'https://example.com/search?foo=bar&form=ponies'
    url = update_query_params(url, params)
    assert url == 'https://example.com/search?foo=biz&form=bar'

test_update_query_params()

# Generated at 2022-06-14 06:49:03.233469
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?biz=baz&foo=stuff'

print(update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}))

# Generated at 2022-06-14 06:49:14.303182
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    output = update_query_params(url, params)

    assert 'foo=stuff' in output
    assert 'biz=baz' in output
    assert 'http://' in output

    # PyTest style
    assert update_query_params('http://example.com?foo=bar', dict(foo='stuff'))  == 'http://example.com?foo=stuff'

    # PyTest style with setup
    setup = 'from __main__ import update_query_params'
    assert eval(repr(update_query_params('http://example.com?foo=bar', dict(foo='stuff'))), setup) == 'http://example.com?foo=stuff'


# Generated at 2022-06-14 06:49:25.378572
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(baz='stuff')) == 'http://example.com?baz=stuff&biz=baz&foo=bar'
    assert update_query_params('http://example.com', dict(foo='stuff')) == 'http://example.com?foo=stuff'

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:49:30.257244
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> print update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    http://example.com/?foo=stuff&biz=baz

    """
    pass


# Generated at 2022-06-14 06:49:35.381095
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff', bar='thing')
    new_url = update_query_params(url, params)
    assert 'http://example.com?foo=stuff&bar=thing&biz=baz' == new_url

# Generated at 2022-06-14 06:49:42.662686
# Unit test for function update_query_params
def test_update_query_params():
    """ Test for update_query_params """
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == \
        'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo=['stuff', 'things'])) == \
        'http://example.com?foo=stuff&foo=things&biz=baz'

# Generated at 2022-06-14 06:49:49.106831
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz&baz=baf'
    params = {'baz': 'baf', 'foo': 'stuff'}
    url = update_query_params(url, params)
    assert url == 'http://example.com?baz=baf&baz=baf&foo=stuff&biz=baz'



# Generated at 2022-06-14 06:50:01.344873
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://foo.com?x=23' == update_query_params('http://foo.com', dict(x='23'))
    assert 'http://foo.com?x=23&y=42' == update_query_params('http://foo.com?x=1', dict(x='23', y='42'))
    assert 'http://foo.com?x=y&x=z' == update_query_params('http://foo.com?x=y', dict(x='z'))
    assert 'http://foo.com?x=y&x=z' == update_query_params('http://foo.com?x=y&x=z', dict(x='z'))

# Generated at 2022-06-14 06:50:08.456608
# Unit test for function update_query_params
def test_update_query_params():
    test_url = "http://example.com?foo=bar&biz=baz"
    result_url = update_query_params(test_url, {"foo": "stuff"})
    expected_url = "http://example.com?biz=baz&foo=stuff"
    assert result_url == expected_url

if __name__ == "__main__":
    test_update_query_params()

# Generated at 2022-06-14 06:50:18.742589
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com', dict(foo='bar')) == 'http://example.com?foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='foo', bar='bar')) == 'http://example.com?bar=bar&biz=baz&foo=foo'
    assert not 'stuff' in update_query_params('http://example.com', dict(foo='bar'))

# Generated at 2022-06-14 06:50:24.978844
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='stuff')) == 'http://example.com?biz=stuff&foo=bar'

# Generated at 2022-06-14 06:50:29.940559
# Unit test for function update_query_params
def test_update_query_params():
    # Initialize
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    # Execute
    new_url = update_query_params(url, params)
    # Verify
    assert new_url == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:50:34.539800
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar'
    result = update_query_params(url, dict(foo='stuff'))
    assert result == 'http://example.com?foo=stuff'



# Generated at 2022-06-14 06:50:45.935932
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(baz='stuff')) == 'http://example.com?biz=baz&baz=stuff&foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(baz='stuff'), doseq=False) == 'http://example.com?biz=baz&foo=bar&baz=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz&foo=stuff', dict(foo='otherstuff'), doseq=False)

# Generated at 2022-06-14 06:50:50.746011
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    assert expected_url == update_query_params(url, dict(foo='stuff'))



# Generated at 2022-06-14 06:51:02.032312
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='foo')) == 'http://example.com?biz=foo&foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(biz='foo')) == 'http://example.com?biz=foo&foo=bar'
    assert update_query_params('http://example.com?foo=bar&biz=baz', None) == 'http://example.com?biz=baz&foo=bar'

# Generated at 2022-06-14 06:51:07.038917
# Unit test for function update_query_params
def test_update_query_params():
  url_new = update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
  # print('url_new:', url_new)
  assert url_new == 'http://example.com?biz=baz&foo=stuff', url_new


# Generated at 2022-06-14 06:51:12.349751
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    new_url = update_query_params(url, params)
    expected_url = 'http://example.com?biz=baz&foo=stuff'
    assert new_url == expected_url


# Generated at 2022-06-14 06:51:24.776761
# Unit test for function update_query_params
def test_update_query_params():
    url1 = 'http://example.com?foo=bar&biz=baz'
    url2 = update_query_params(url1, {'foo': 'stuff'})
    assert url2 == 'http://example.com?biz=baz&foo=stuff'
    url3 = update_query_params(url1, {'foo': 'stuff', 'bar': 'eeeerrrr'})
    assert url3 == 'http://example.com?bar=eeeerrrr&biz=baz&foo=stuff'
    url4 = update_query_params(url1, {'foo': ['stuff', 'yay']})
    assert url4 == 'http://example.com?biz=baz&foo=stuff&foo=yay'

# Generated at 2022-06-14 06:51:33.924924
# Unit test for function update_query_params
def test_update_query_params():
    pass



# Generated at 2022-06-14 06:51:45.322937
# Unit test for function update_query_params
def test_update_query_params():
    testurls = ['http://example.com', 'http://example.com?biz=baz', 'http://example.com?foo=bar&biz=baz']
    d = { 'foo': 'stuff', 'boo' : 'boo' }

    for url in testurls:
        print("\nTesting with: ")
        print("      URL: " + url)
        print("Parameters: ")
        for (key, value) in d.items():
            print("         " + key + " = " + value)
        print(" Result: ")
        print(update_query_params(url, d))


if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()

# Generated at 2022-06-14 06:51:57.106919
# Unit test for function update_query_params
def test_update_query_params():
    # Example from the docs
    assert 'http://example.com?biz=baz&foo=stuff' == update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff'))

    # Insert a new query parameter
    assert 'http://example.com?biz=baz&foo=bar&stuff=baz' == update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(stuff='baz'))

    # Update a query parameter
    assert 'http://example.com?biz=baz&foo=stuff' == update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff'))

    # Update a query parameter with the same key multiple times

# Generated at 2022-06-14 06:52:10.220959
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://example.com?a=1&b=2"
    new_url = update_query_params(url, dict(c=3, d=4))
    assert new_url == "http://example.com?a=1&b=2&c=3&d=4", \
        "update_query_params failed: {}".format(new_url)
    new_url = update_query_params(url, dict(a=5, b=6))
    assert new_url == "http://example.com?a=5&b=6", \
        "update_query_params failed: {}".format(new_url)
    new_url = update_query_params(url, dict(z=7))

# Generated at 2022-06-14 06:52:19.508356
# Unit test for function update_query_params
def test_update_query_params():
    assert 'http://example.com?foo=stuff&biz=baz' == update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    assert 'http://example.com?foo=stuff&biz=baz&foo=bar' == update_query_params('http://example.com?foo=stuff&biz=baz', dict(foo='bar'))
    assert 'http://example.com?foo=stuff&biz=baz&foo=bar' == update_query_params('http://example.com?foo=stuff&biz=baz', dict(foo=['bar']))


# Generated at 2022-06-14 06:52:30.237785
# Unit test for function update_query_params
def test_update_query_params():
    """
    Unit test for function update_query_params
    """
    assert(update_query_params('http://example.com', {'foo': 'bar'}) == 'http://example.com/?foo=bar')
    assert(update_query_params('http://example.com?foo=bar', {'foo': 'baz'}) == 'http://example.com/?foo=baz')
    assert(update_query_params('http://example.com/?foo=bar', {'biz': 'baz'}) == 'http://example.com/?foo=bar&biz=baz')
    assert(update_query_params('http://example.com?foo=bar', {'foo': 'stuff'}) == 'http://example.com/?foo=stuff')

# Generated at 2022-06-14 06:52:43.075079
# Unit test for function update_query_params
def test_update_query_params():
    import random
    import string
    import unittest

    class TestSequenceFunctions(unittest.TestCase):

        def setUp(self):
            self.url = 'http://example.com'
            self.update_params = {}
            for i in range(2):
                self.update_params[random.choice(string.ascii_letters)] = random.choice(string.ascii_letters)

        def test_url_not_changed(self):
            new_url = update_query_params(self.url, self.update_params)
            self.assertNotEqual(self.url, new_url)

        def test_update_params_added(self):
            new_url = update_query_params(self.url, self.update_params)

# Generated at 2022-06-14 06:52:54.438830
# Unit test for function update_query_params

# Generated at 2022-06-14 06:52:58.841240
# Unit test for function update_query_params
def test_update_query_params():
    """
    >>> update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    'http://example.com?...foo=stuff...'
    """
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 06:53:07.543427
# Unit test for function update_query_params
def test_update_query_params():
    # Test call with only optional arguments.
    args = (
        'http://example.com/path?foo=bar&biz=baz',
        dict(foo='stuff', new='value')
    )

    expected = 'http://example.com/path?biz=baz&foo=stuff&new=value'
    assert update_query_params(*args) == expected

    # Test call with only required arguments.
    args = (
        'http://example.com/path?foo=bar&biz=baz',
        dict(foo='stuff', new='value'),
        False
    )

    expected = 'http://example.com/path?foo=stuff&new=value'
    assert update_query_params(*args) == expected

# Generated at 2022-06-14 06:53:19.248476
# Unit test for function update_query_params
def test_update_query_params():
    print('\nUnit test for function update_query_params')

    print(update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')))

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:53:24.986469
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com/path?page=1&page_size=10&page_size=20'
    new_url = update_query_params(url, {'page_size': 15})
    assert new_url == 'http://example.com/path?page=1&page_size=15'



# Generated at 2022-06-14 06:53:31.660468
# Unit test for function update_query_params
def test_update_query_params():
    url = "http://www.example.com?a=1&b=2&c=3&d=4"
    new_url = update_query_params(url, {'a': 5, 'e': 6})
    assert new_url == "http://www.example.com?a=5&b=2&c=3&d=4&e=6"

# Generated at 2022-06-14 06:53:36.215621
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    expected_url = 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url, dict(foo='stuff')) == expected_url




# Generated at 2022-06-14 06:53:42.676696
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, params={'foo':'stuff'})
    assert new_url == 'http://example.com?foo=stuff&biz=baz'


# Adapted from
# http://code.activestate.com/recipes/576694-orderedset/

# Generated at 2022-06-14 06:53:50.717124
# Unit test for function update_query_params
def test_update_query_params():
    print("**** unit test ****")
    url = "https://example.com/query?q=foo+bar&start=0&count=10"
    new_url = update_query_params(url, params={"start": 10, "count": 30})
    print("old url is: ", url)
    print("new url is: ", new_url)
    return None


if __name__ == "__main__":
    test_update_query_params()
    print("the unit test is done")

# Generated at 2022-06-14 06:53:59.900652
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='baz')) == 'http://example.com?bar=baz&biz=baz&foo=stuff'
    assert update_query_params(
        'http://example.com?foo=bar&biz=baz', dict(foo='stuff', baz='biz')) == 'http://example.com?baz=biz&biz=baz&foo=stuff'

# Generated at 2022-06-14 06:54:05.825645
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert url != new_url, 'Expected URLs to be different'
    assert 'foo=stuff' in new_url, 'Expected new URL to contain "foo=stuff"'

# Generated at 2022-06-14 06:54:11.876746
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?biz=baz&foo=stuff'

    url = 'http://example.com?foo=bar'
    new_url = update_query_params(url, dict(foo='stuff', biz='baz'))
    assert new_url == 'http://example.com?biz=baz&foo=stuff'

# Generated at 2022-06-14 06:54:18.756672
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff', 'baz': 'qux'}
    new_url = update_query_params(url, params)
    assert new_url == 'http://example.com?biz=baz&foo=stuff&baz=qux'

# Generated at 2022-06-14 06:54:39.888907
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?&foo=stuff&biz=baz'



# Generated at 2022-06-14 06:54:43.709483
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', foo='stuff') == \
        'http://example.com?biz=baz&foo=stuff'


# Generated at 2022-06-14 06:54:49.050122
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == \
           'http://example.com?foo=stuff&biz=baz'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:54:54.368032
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    new_url = update_query_params(url, dict(foo='stuff'))
    assert new_url == 'http://example.com?biz=baz&foo=stuff'

if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:54:57.251981
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# This is our test

# Generated at 2022-06-14 06:55:09.723483
# Unit test for function update_query_params
def test_update_query_params():
    assert(update_query_params('', {}) == '')
    assert(update_query_params('', {'foo': 'bar'}) == 'foo=bar')
    assert(update_query_params('?foo=bar', {'foo': 'bar'}) == '?foo=bar')
    assert(update_query_params('?foo=bar', {'bar': 'baz'}) == '?foo=bar&bar=baz')
    assert(update_query_params('?foo=bar', {'foo': 'baz'}) == '?foo=baz')

    assert(update_query_params('', {'foo': 'bar', 'biz': 'baz'}) == 'biz=baz&foo=bar')

# Generated at 2022-06-14 06:55:19.108915
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com'
    url_with_qp = 'http://example.com?foo=bar&biz=baz'
    url_with_qp_2 = 'http://example.com?biz=baz&foo=bar'
    params = dict(foo='stuff')

    assert update_query_params(url, params) == 'http://example.com?foo=stuff'
    assert update_query_params(url_with_qp, params) == 'http://example.com?biz=baz&foo=stuff'
    assert update_query_params(url_with_qp_2, params) == 'http://example.com?biz=baz&foo=stuff'



# Generated at 2022-06-14 06:55:31.026399
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar=['oops', 'yeah'])) == 'http://example.com?foo=stuff&bar=oops&bar=yeah&biz=baz'
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff', bar='oops', biz='yeah')) == 'http://example.com?foo=stuff&bar=oops&biz=yeah'

# Generated at 2022-06-14 06:55:35.687341
# Unit test for function update_query_params
def test_update_query_params():
    assert update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff')) == 'http://example.com?biz=baz&foo=stuff'

# Run unit tests
if __name__ == '__main__':
    test_update_query_params()

# Generated at 2022-06-14 06:55:39.263456
# Unit test for function update_query_params
def test_update_query_params():
    url = 'http://example.com?foo=bar&biz=baz'
    params = dict(foo='stuff')
    assert 'http://example.com?...foo=stuff...' == update_query_params(url, params)

