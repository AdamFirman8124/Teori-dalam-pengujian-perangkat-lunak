

# Generated at 2022-06-13 22:43:58.929826
# Unit test for function get_content_type
def test_get_content_type():
    assert(get_content_type("test.dot.txt")=='text/plain')
    assert(get_content_type("test.dot.html")=='text/html')
    assert(get_content_type("test.dot.mp3")=='audio/mpeg')
    assert(get_content_type("test.dot.png")=='image/png')
    assert(get_content_type("test.dot.gif")=='image/gif')
    assert(get_content_type("test.dot.jpg")=='image/jpeg')
    assert(get_content_type("test.dot.jpeg")=='image/jpeg')

# Generated at 2022-06-13 22:44:04.373363
# Unit test for function get_content_type
def test_get_content_type():
    print(get_content_type('/tmp/index.html'))
    print(get_content_type('/tmp/index.html.gz'))
    print(get_content_type('/tmp/index.html.bz2'))
    print(get_content_type('/tmp/index.html.br'))



# Generated at 2022-06-13 22:44:14.396663
# Unit test for function get_content_type
def test_get_content_type():
    # pylint: disable=redefined-outer-name
    expected = {
        'text/plain': 'text/plain',
        'text/plain; charset=utf-8': 'text/plain; charset=utf-8',
        'text/x-c++src': 'text/x-c++src',
        'text/x-c++src; charset=utf-8': 'text/x-c++src; charset=utf-8',
    }
    for key, val in expected.items():
        assert val == get_content_type(key)



# Generated at 2022-06-13 22:44:21.345181
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime
    from uuid import uuid4
    from pytz import utc

    from freezegun import freeze_time

    from django.utils.encoding import iri_to_uri

    from .utils import get_expired_cookies


# Generated at 2022-06-13 22:44:31.206812
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/path/to/filename.csv') == 'text/csv'
    assert get_content_type('/path/to/filename.gif') == 'image/gif'
    assert get_content_type('/path/to/filename.js') == 'application/javascript'
    assert get_content_type('/path/to/filename.json') == 'application/json'
    assert get_content_type('/path/to/filename.text') is None
    assert get_content_type('/path/to/filename.txt') == 'text/plain'
    assert get_content_type('/path/to/filename.html') == 'text/html'
    assert get_content_type('/path/to/filename.png') == 'image/png'

# Generated at 2022-06-13 22:44:43.179413
# Unit test for function get_content_type
def test_get_content_type():
    import pytest
    from pathlib import Path

    def assert_content_type(filename, expected):
        assert get_content_type(filename) == expected

    # Generic extensions.
    extensions = {
        '.css': 'text/css',
        '.csv': 'text/csv',
        '.htm': 'text/html',
        '.html': 'text/html',
        '.js': 'text/javascript',
        '.txt': 'text/plain',
    }
    for filename, content_type in extensions.items():
        yield (assert_content_type, filename, content_type)

    # Image extensions.

# Generated at 2022-06-13 22:44:48.208093
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('xxx.png') == 'image/png'
    assert get_content_type('xxx.PNG') == 'image/png'
    assert get_content_type('xxx.PNG', strict=True) is None



# Generated at 2022-06-13 22:45:00.901587
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:10.288668
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:21.855841
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    sample_cookie_header = [
        ('Set-Cookie', 'foo=bar'),
        ('Set-Cookie', 'qux=baz; Max-Age=86400; path=/foo/; Secure; HttpOnly'),
    ]

    assert get_expired_cookies(headers=[]) == []

# Generated at 2022-06-13 22:45:36.698239
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'foo=bar; path=/; expires=Tue, 30-Mar-2100 12:34:56 GMT'),
        ('Set-Cookie', 'baz=bop; path=/; expires=Tue, 30-Mar-2020 12:34:56 GMT'),
        ('Set-Cookie', 'qux=quux; path=/; max-age=10000'),
        ('Set-Cookie', 'abc=123; path=/; max-age=0'),
    ]

    now = time.time()
    assert len(get_expired_cookies(
        headers=headers,
        now=now - 10001
    )) == 2

    assert len(get_expired_cookies(
        headers=headers,
        now=now + 9999
    )) == 0


# Generated at 2022-06-13 22:45:42.199022
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:50.064923
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    h = \
        ('Set-Cookie: foo=bar',
         'Set-Cookie: foo2=bar2; Path=/foobar; Max-Age=100',
         'Set-Cookie: foo3=bar3; Path=/foobar; Expires=Wed, 13 Jan 2021 22:23:01 GMT')
    now = time.time()
    assert get_expired_cookies(h, now) == []
    # Lets expire foo2.
    assert get_expired_cookies(h, now + 101) == \
           [{'name': 'foo2', 'path': '/foobar'}]

# Generated at 2022-06-13 22:45:59.513634
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime, timedelta

    past = datetime.now() - timedelta(minutes=60)
    future = datetime.now() + timedelta(minutes=60)
    now = datetime.now()


# Generated at 2022-06-13 22:46:06.802310
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from unittest import TestCase, mock

    class TestGetExpiredCookies(TestCase):
        @mock.patch('time.time')
        def test_no_cookies(self, _time):
            self.assertEqual(get_expired_cookies(headers=[]), [])

        @mock.patch('time.time')
        def test_expired_cookies(self, _time):
            _time.side_effect = [0, 5]
            headers = [('Set-Cookie', 'a=1; Max-Age=10')]
            self.assertEqual(
                get_expired_cookies(headers=headers),
                [{'name': 'a', 'path': '/'}]
            )

# Generated at 2022-06-13 22:46:18.980713
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    """
    Unit test for function ``get_expired_cookies``.

    """
    headers = [
        ('Set-Cookie', 'domain_1=foo; path=/; Max-Age=10'),
        ('Set-Cookie', 'domain_2=bar; path=/; expires=Wed, '
                       '01 Jan 2020 00:00:00 GMT'),
        ('Set-Cookie', 'domain_3=cookie; path=/; Max-Age=11'),
        ('Set-Cookie', 'domain_4=cake; path=/; expires=Wed, '
                       '01 Jan 2015 00:00:00 GMT')
    ]

    now = time.mktime(time.strptime('Wed, 01 Jan 2020 00:00:00',
                                    '%a, %d %b %Y %H:%M:%S'))


# Generated at 2022-06-13 22:46:27.812040
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    def _test_case(test_case):
        max_age_to_expires(cookies=test_case['cookies'])
        expired_cookies = get_expired_cookies(
            test_case['headers'],
            now=test_case['now']
        )
        assert expired_cookies == test_case['expected']


# Generated at 2022-06-13 22:46:40.217667
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import datetime

    now = int(time.time())

# Generated at 2022-06-13 22:46:49.449682
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    print('now', now)

    def do_test(cookies_str, expect):
        cookies = get_expired_cookies(headers=[('set-cookie', cookies_str)])
        assert cookies == expect, repr((cookies, cookies_str))

    do_test(
        cookies_str=(
            'dummy-cookie=dummy-value; '
            'Max-Age=86400; '
            'Path=/; '
            'domain=example.com; '
            'secure; '
            'HttpOnly; '
            'SameSite=Strict'
        ),
        expect=[],
    )


# Generated at 2022-06-13 22:46:55.342978
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import pytest
    num_cookies = [
        (1, 'Set-Cookie: name1=val1; path=/'),
        (2, 'Set-Cookie: name2=val2; path=/; Max-Age=150'),
        (3, 'Set-Cookie: name3=val3; path=/; Expires=Wed, 12 Dec 2018 17:48:52 GMT'),
    ]
    # HACK: <https://github.com/psf/requests/issues/5743>

# Generated at 2022-06-13 22:47:04.940730
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # type: () -> None
    """
    Test the function get_expired_cookies().
    """
    now = time.time()

    resp1 = {
        'set-cookie': [
            'a=1; domain=example.com; expires=Thu, 01 Jan 1970 00:00:00 GMT',
            'b=1; domain=example.com; expires=Thu, 01 Jan 1970 00:00:00 GMT',
        ]
    }
    assert get_expired_cookies(resp1.items(), now) == [
        {'name': 'a', 'path': '/'},
        {'name': 'b', 'path': '/'},
    ]


# Generated at 2022-06-13 22:47:16.476575
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([('set-cookie', 'a=b')]) == [
        {
            'name': 'a',
            'path': '/',
        },
    ]
    assert get_expired_cookies([
        ('set-cookie', 'a=b'),
        ('set-cookie', 'c=d'),
    ]) == [
        {
            'name': 'a',
            'path': '/',
        },
        {
            'name': 'c',
            'path': '/',
        },
    ]

# Generated at 2022-06-13 22:47:27.551011
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()

# Generated at 2022-06-13 22:47:34.900905
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # httpbin.org automatically truncates the response to 10 cookies.
    # We will construct the response containing 11 cookies.
    # Then the 11th cookie should be dropped.
    now = time.time()

# Generated at 2022-06-13 22:47:43.809064
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:47:52.947039
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # Set-Cookie: foo=bar, Expires=Wed, 09 Jun 2021 10:18:14 GMT
    # Set-Cookie: baz=qux, Max-Age=60*60
    headers = [
        ('Set-Cookie', 'foo=bar; Expires=Wed, 09 Jun 2021 10:18:14 GMT'),
        ('Set-Cookie', 'baz=qux; Max-Age=3600'),
    ]
    now = 1591763000.0  # Wed, 24 Jun 2020 11:30:00 GMT
    assert get_expired_cookies(headers=headers, now=now) == [
        {'name': 'foo', 'path': '/'},
    ]

# Generated at 2022-06-13 22:48:00.877285
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'session=abcdef; expires=Mon, 06-Jun-2016 16:37:59 GMT; secure'),
        ('Set-Cookie', 'session=abcdef2; expires=Mon, 06-Jun-2016 16:37:59 GMT; secure'),
    ]
    now = time.mktime(time.strptime('Mon, 06-Jun-2016 16:38:00 GMT', '%a, %d-%b-%Y %H:%M:%S %Z'))
    cookies = get_expired_cookies(headers, now=now)
    assert len(cookies) == 2
    assert cookies[0]['path'] == '/'
    assert cookies[0]['name'] == 'session'

# Generated at 2022-06-13 22:48:09.581096
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()

    def _test(
        cookies: List[Tuple[str, str]],
        now: float,
        *expected: Tuple[str, str]
    ):
        cookies = get_expired_cookies(cookies=cookies, now=now)
        assert len(cookies) == len(expected)
        for cookie, expected in zip(cookies, expected):
            assert (cookie['name'], cookie['path']) == expected

    # Expired cookie

# Generated at 2022-06-13 22:48:20.126449
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([]) == []

    assert get_expired_cookies(
        [('Set-Cookie', 'name=val')],
        now=100
    ) == []

    assert get_expired_cookies(
        [('Set-Cookie', 'name=val; Path=/; Expires=Wed, 23 Nov 2033 17:15:35 GMT')],
        now=100
    ) == [
        {'name': 'name', 'path': '/'}
    ]

    assert get_expired_cookies(
        [('Set-Cookie', 'name=val; Path=/; Max-Age=100')],
        now=100
    ) == [
        {'name': 'name', 'path': '/'}
    ]


# Generated at 2022-06-13 22:48:30.646340
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookie_headers = [
        ('Set-Cookie', 'a=1; Expires=Wed, 09 Jun 2021 10:18:14 GMT'),
        ('Set-Cookie', 'b=1; Expires=Wed, 09 Jun 2021 10:18:14 GMT'),
        ('Set-Cookie', 'c=1; expires=Wed, 09 Jun 2021 10:18:14 GMT')
    ]

    now = 1623024694
    expired_cookies = get_expired_cookies(headers=cookie_headers, now=now)

    assert len(expired_cookies) == 2
    assert 'a' in [c['name'] for c in expired_cookies]
    assert 'b' in [c['name'] for c in expired_cookies]

# Generated at 2022-06-13 22:48:42.396822
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookies = get_expired_cookies(
        headers=[
            ("Set-Cookie", "foo=bar; Expires=Wed, 22 Jun 2016 23:32:57 GMT; Path=/"),
            ("Set-Cookie", "foo=expired; Expires=Wed, 22 Jun 2016 01:32:57 GMT; Path=/"),
            ("Set-Cookie", "foo=max-age=1; Max-Age=1; Path=/"),
        ],
        now=1466633777.0
    )
    assert cookies == ([
        {
            'name': 'foo',
            'path': '/'
        },
        {
            'name': 'foo',
            'path': '/'
        }
    ])

# Generated at 2022-06-13 22:48:56.258651
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookie = {
        'name': 'foo',
        'value': 'bar',
        'domain': 'example.com',
        'path': '/',
        'expires': 20200130,
        'max-age': '10',
    }

# Generated at 2022-06-13 22:49:06.092952
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'a=1; domain=.kwako.opendata.dk; path=/; expires=Thu, 01-Jan-1970 00:00:10 GMT'),
        ('Set-Cookie', 'b=2; domain=.kwako.opendata.dk; path=/; expires=Thu, 01-Jan-1970 00:00:20 GMT'),
        ('Set-Cookie', 'c=3; domain=.kwako.opendata.dk; path=/; max-age=10'),
        ('Set-Cookie', 'd=4; domain=.kwako.opendata.dk; path=/; max-age=20'),
    ]

# Generated at 2022-06-13 22:49:16.519847
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from requests.cookies import create_cookie

    now = now = time.time()

    expired_cookie = create_cookie(
        'expired', '0',
        expires=now - 1
    )
    expired_cookie2 = create_cookie(
        'expired2', '0',
        expires=now - 1,
        max_age=1
    )
    expired_cookie3 = create_cookie(
        'expired3', '0',
        max_age=1
    )

    set_cookie_headers = [
        expired_cookie.output(header='').strip(),
        expired_cookie2.output(header='').strip(),
        expired_cookie3.output(header='').strip(),
    ]


# Generated at 2022-06-13 22:49:28.219299
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'foo=bar; Path=/'),
        ('Set-Cookie', 'foo=baz; Max-Age=1; Path=/'),
        ('Set-Cookie', 'foo=qux; Max-Age=2; Path=/')
    ]

    cookies = get_expired_cookies(headers=headers, now=0)
    assert len(cookies) == 1
    assert cookies[0] == {'name': 'foo', 'path': '/'}

    cookies = get_expired_cookies(headers=headers, now=1)
    assert len(cookies) == 1
    assert cookies[0] == {'name': 'foo', 'path': '/'}

    cookies = get_expired_cookies(headers=headers, now=2)
    assert len(cookies)

# Generated at 2022-06-13 22:49:37.648900
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    expired_cookies = get_expired_cookies(
        headers=[
            ('Set-Cookie',
             'key1=value1; Expires=Tue, 30 Oct 2018 17:07:11 GMT'),
            ('Set-Cookie',
             'key2=value2; Max-Age=100'),
            ('Set-Cookie',
             'key3=value3; Max-Age=100; Path=/'),
            ('Set-Cookie',
             'key4=value4; Path=/; Max-Age=100'),
        ],
        now=1509366031
    )

# Generated at 2022-06-13 22:49:44.952193
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([]) == []

    now = time.time()
    assert get_expired_cookies([
        ('Set-Cookie', 'foo=bar; Path=/; Expires=%s' % time.ctime(now + 100)),
        ('Set-Cookie', 'baz=qux; Path=/; Expires=%s' % time.ctime(now - 100)),
    ], now=now) == [
        {
            'name': 'baz',
            'path': '/'
        }
    ]

# Generated at 2022-06-13 22:49:52.874517
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    expired_cookies = get_expired_cookies(
        headers=[
            ('Set-Cookie', 'a=0; path=/foo; expires=Tue, '
             '27 Jun 2017 13:09:18 GMT'),
            ('Set-Cookie', 'b=0; path=/foo; max-age=0')
        ],
        now=now
    )
    assert expired_cookies == [
        {
            'name': 'a',
            'path': '/foo',
        },
        {
            'name': 'b',
            'path': '/foo',
        }
    ]

# Generated at 2022-06-13 22:50:03.645412
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import timedelta
    from http.cookiejar import CookieJar
    from http.cookies import SimpleCookie
    from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

    import pytest

    from ..utils import get_expired_cookies
    from .mocks.httpserver import requests_mock_datadir

    now = 1558671263.8223431

    # Schema:
    #   test: A test name
    #   url: The url to match against
    #   query_string: The query string to use, if any
    #   cookie_header: The cookies in a Set-Cookie response header
    #   cookie_jar: The cookie jar used in request
    #   cookies_to_clear: The expected cookies to clear

# Generated at 2022-06-13 22:50:12.940803
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from .test.helpers import make_response

    res = make_response()
    time1 = time.time()
    time2 = time1 + 50
    time3 = time2 + 50
    time4 = time3 + 50
    time5 = time4 + 50
    res.headers['Set-Cookie'] = "sessionid=1; expires={};".format(
        make_expires(time1 + 50),
    )
    res.headers['Set-Cookie'] = "sessionid=2; expires={};".format(
        make_expires(time2 + 50),
    )
    res.headers['Set-Cookie'] = "sessionid=3; expires={};".format(
        make_expires(time3 + 50),
    )