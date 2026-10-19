

# Generated at 2022-06-13 22:43:57.981394
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type("plop.jpg") == "image/jpeg"
    assert get_content_type("plop.png") == "image/png"
    assert get_content_type("plop.html") == "text/html"
    assert get_content_type("plop.json") == "text/json"
    assert get_content_type("plop.css") == "text/css"
    assert get_content_type("plop.js") == "text/javascript"
    assert get_content_type("plop.svg") == "image/svg+xml"
    assert get_content_type("plop.xml") == "text/xml"
    assert get_content_type("plop.pdf") == "application/pdf"

# Generated at 2022-06-13 22:44:07.580763
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = 1551232622.0

# Generated at 2022-06-13 22:44:18.482205
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.JPG') == 'image/jpeg'
    assert get_content_type('foo.jpeg') is None
    assert get_content_type('foo.JPEG') is None


if __name__ == '__main__':
    import sys
    import unittest
    import doctest
    from typing import Dict, Sequence
    from datetime import datetime, timedelta
    from requests import Response
    from . import make_test_cases
    from . import util

    # - - - unittests - - -

    class Test_util(unittest.TestCase):
        # noinspection PyMethodMayBeStatic
        def test_util(self):
            doctest.testmod(util)
           

# Generated at 2022-06-13 22:44:20.172841
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo/bar.html') == 'text/html'
    assert get_content_type('foo/bar.js') == 'application/javascript'

# Generated at 2022-06-13 22:44:26.461147
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('filename.csv') == 'text/csv'
    assert get_content_type('filename.foo') is None
    assert get_content_type('filename.foo.csv') == 'text/csv'
    assert get_content_type('filename.csv.gz') == 'application/x-gzip'


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 22:44:34.830954
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    def assert_expected_cookies(headers, expected):
        assert get_expired_cookies(headers) == expected, headers

    assert_expected_cookies(
        headers=[
            ('Set-Cookie', 'key=value'),
            ('Set-Cookie', 'expires=Thu, 14 Jun 2018 20:05:48 GMT'),
        ],
        expected=[{
            'name': 'key',
            'path': '/',
        }]
    )

# Generated at 2022-06-13 22:44:45.681003
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:44:48.855459
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('text/plain') == 'text/plain'
    assert get_content_type('text/plain; charset=binary') == 'text/plain; charset=binary'

# Generated at 2022-06-13 22:44:54.554352
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.pdf') == 'application/pdf'
    assert get_content_type('foo.tar.gz') == 'application/gzip'
    assert get_content_type('foo.unknown_ext') is None

# Generated at 2022-06-13 22:45:05.154451
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime
    from dateutil.parser import parse
    from dateutil.tz import UTC


# Generated at 2022-06-13 22:45:13.580490
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookie = [('Set-Cookie', "test_cookie=test_value; domain=abc.com; expires=Sun, 12 Jan 2020 17:43:08 GMT; path=/")]
    test_cookie = get_expired_cookies(cookie, time.time())
    assert test_cookie == [], "Should return an empty list"

    cookie = [('Set-Cookie', "test_cookie=test_value; domain=abc.com; expires=Sun, 12 Jan 2000 17:43:08 GMT; path=/")]
    test_cookie = get_expired_cookies(cookie, time.time())
    assert test_cookie == [{'name': 'test_cookie', 'path': '/'}], "Should return an empty list"

# Generated at 2022-06-13 22:45:23.064655
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'foo=; path=/; expires=Sun, 27-May-2018 11:24:53 GMT'),
        ('Set-Cookie', 'bar=; path=/; expires=Wed, 30-May-2018 11:24:53 GMT'),
        ('Set-Cookie', 'baz=; path=/; expires=Wed, 30-May-2018 11:24:53 GMT'),
    ]

    now = 1527612493.0790768
    exp_result = [
        {
            'name': 'foo',
            'path': '/'
        }
    ]

    assert get_expired_cookies(headers=headers, now=now) == exp_result


# End of unit test

# Generated at 2022-06-13 22:45:36.261883
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    """
    This is the example from https://tools.ietf.org/html/rfc6265#section-4.1.2.2
    with the additional first and last set-cookie headers.
    """

# Generated at 2022-06-13 22:45:42.048969
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    header_set_cookie = [
        ('Set-Cookie', 'foo=bar; path=/; expires=Sun, 22 Feb 2020 01:18:35 GMT'),
        ('Set-Cookie', 'baz=qux; path=/; expires=Sun, 22 Feb 2020 00:18:35 GMT'),
        ('Set-Cookie', 'maxage=one; path=/; Max-Age=3600'),
        ('Set-Cookie', 'maxage=two; path=/; Max-Age=86_400'),
        ('Set-Cookie', 'maxage=three; path=/; Max-Age=7592000'),
        ('Set-Cookie', 'noexpire=four; path=/'),
        ('Set-Cookie', 'noexpire=five; path=/')]

# Generated at 2022-06-13 22:45:51.739382
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = 1500000000
    headers = [
        ('Set-Cookie', 'one=1; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT'),
        ('Set-Cookie', 'two=2; Path=/; Max-Age=0'),
        ('Set-Cookie', 'three=3; Path=/; Max-Age=2'),
        ('Set-Cookie', 'four=4; Path=/; Max-Age=4'),
    ]

    assert get_expired_cookies(headers, now=now) == [
        dict(name='one', path='/'),
        dict(name='two', path='/'),
    ]

    headers.extend([('Set-Cookie', 'five=5; Path=/; Max-Age=6')])


# Generated at 2022-06-13 22:46:00.182925
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from . import test

    headers = [
        ('Set-Cookie', 'A1=foo'),
        ('Set-Cookie', 'A2=foo; Max-Age=10'),
        ('Set-Cookie', 'A3=foo; Expires=Sat, 01 Jan 2116 00:00:00 GMT'),
        ('Set-Cookie', 'A4=foo; Expires=Sat, 01 Jan 2016 00:00:00 GMT'),
        ('Set-Cookie', 'A5=foo; Max-age=-10'),
        ('Set-Cookie', 'A6=foo; Max-Age=abcd'),
    ]

    # Fri, 01 Jan 2016 00:00:00 GMT

# Generated at 2022-06-13 22:46:09.193272
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # cookie with correct expires
    cookie_raw_1 = 'cookie_name=foo; expires=Sat, 01 Jan 2000 00:00:00 GMT; path=/'
    # cookie without expires
    cookie_raw_2 = 'cookie_name=foo; path=/'
    # cookie with wrong expires
    cookie_raw_3 = 'cookie_name=foo; expires=Sat, 01 Jan 3000 00:00:00 GMT; path=/'
    # cookie with max-age
    cookie_raw_4 = 'cookie_name=foo; max-age=2000000; path=/'

    # params
    now = time.time()


# Generated at 2022-06-13 22:46:21.366402
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime

    dt = datetime(2030, 1, 1, 0, 0, 0)
    expired_cookies = get_expired_cookies([
        ('Set-Cookie', 'foo=bar; Path=/'),
        ('Set-Cookie', f'foo2=bar2; Path=/; expires={dt}'),
        ('Set-Cookie', 'foo3=bar3; Path=/; Max-Age=0'),
        ('Set-Cookie', 'foo4=bar4; Path=/; Max-Age=10'),
    ], now=dt.timestamp() - 1)


# Generated at 2022-06-13 22:46:31.801315
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    assert get_expired_cookies([
        ('Set-Cookie', 'foo=bar; Max-Age=10; Path=/')
    ], now) == [
        {'name': 'foo', 'path': '/'}
    ]

# Generated at 2022-06-13 22:46:41.285458
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    expired_cookies = get_expired_cookies([
        ('Set-Cookie', 'banana=yellow; Path=/'),
        ('Set-Cookie', 'Yesterday=Spam; expires=Wed, 10-Apr-19 19:07:32 GMT; Path=/'),
        ('Set-Cookie', 'tomorrow=Spam; expires=Thu, 11-Apr-19 19:07:32 GMT; Path=/'),
        ('Set-Cookie', 'tomorrow2=Spam; expires=+100s; Path=/'),
    ], now=1554987252.0)
    assert repr_dict(expired_cookies) == '[{\'name\': \'Yesterday\', \'path\': \'/\'}]'