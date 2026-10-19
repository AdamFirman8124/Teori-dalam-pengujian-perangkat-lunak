

# Generated at 2022-06-13 22:43:57.011827
# Unit test for function get_content_type
def test_get_content_type():
    from sys import platform
    from tempfile import NamedTemporaryFile

    if platform in ['win32', 'cygwin']:
        # I'm not sure why this test doesn't pass on Windows...
        return

    with NamedTemporaryFile() as f:
        f.write(b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00')
        f.flush()
        mimetype = get_content_type(f.name)
    assert mimetype == 'image/gif'
# end test_get_content_type

# Generated at 2022-06-13 22:44:06.611901
# Unit test for function get_content_type
def test_get_content_type():
    assert (
        get_content_type('/path/to/index.html')
        == 'text/html'
    )
    assert (
        get_content_type('/path/to/image.png')
        == 'image/png'
    )
    assert (
        get_content_type('/path/to/image.PNG')
        == 'image/png'
    )
    assert (
        get_content_type('/path/to/image.PNG')
        == 'image/png'
    )
    assert (
        get_content_type('/path/to/image.svg')
        == 'image/svg+xml'
    )

# Generated at 2022-06-13 22:44:18.083235
# Unit test for function get_content_type
def test_get_content_type():

    assert get_content_type('some_file.txt') == 'text/plain'
    assert get_content_type('some_file.py') == 'text/x-python'
    assert get_content_type('some_file.png') == 'image/png'
    assert get_content_type('some_file.jpg') is None
    assert get_content_type('some_file.jpg.png') == 'image/png'
    assert get_content_type('some_file.mp4') == 'video/mp4'
    assert get_content_type('some_file.doc') == 'application/msword'
    assert get_content_type('some_file.mp3') == 'audio/mpeg'
    assert get_content_type('some_file.pdf') == 'application/pdf'
    assert get_content_

# Generated at 2022-06-13 22:44:24.265601
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/foo/bar/baz.txt') == 'text/plain'
    assert get_content_type('/foo/bar/baz') is None
    assert get_content_type('/foo/bar/baz.json') == 'application/json'
    assert get_content_type('/foo/bar/baz.svg') == 'image/svg+xml'

# Generated at 2022-06-13 22:44:27.697491
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.png') == 'image/png'
    assert get_content_type('test.jpg') == 'image/jpeg'
    assert get_content_type('test.jpeg') == 'image/jpeg'
    assert get_content_type('test.jpeg.jpg') == 'image/jpeg'

# Generated at 2022-06-13 22:44:37.656801
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    headers = [
        ('Set-Cookie', 'DoesntMatter=Foo'),
        ('Set-Cookie', 'BadMaxAge=Baz; Max-Age=one; path=/'),
        ('Set-Cookie', 'GoodMaxAge=Xyz; Max-Age=12345; path=/blabla'),
    ]

    cookies = get_expired_cookies(headers=headers, now=now)
    assert len(cookies) == 1
    assert cookies[0]['name'] == 'GoodMaxAge'
    assert cookies[0]['path'] == '/blabla'

# Generated at 2022-06-13 22:44:47.737269
# Unit test for function get_content_type

# Generated at 2022-06-13 22:44:55.339745
# Unit test for function get_content_type
def test_get_content_type():
    """Test get_content_type(filename) function."""
    assert get_content_type('requests.org') is None
    assert get_content_type('error.html') == 'text/html'
    assert get_content_type('error.html.gz') == 'text/html; charset=gzip'
    assert get_content_type('__init__.py') == 'text/x-python'

# Generated at 2022-06-13 22:44:58.524986
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('filename.html') == 'text/html'
    assert get_content_type('filename.html') == 'text/html'
    assert get_content_type('filename.html.x') is None

# Generated at 2022-06-13 22:45:02.235245
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.txt.gz') == 'text/plain'
    assert get_content_type('foo.txt.bz2') == 'text/plain'

# Generated at 2022-06-13 22:45:13.094175
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    """
    Test the function get_expired_cookies.

    """

# Generated at 2022-06-13 22:45:23.444499
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'c1=1; Max-Age=2'),
        ('Set-Cookie', 'c2=2; Expires=Tue, 18 Aug 2020 19:00:00 GMT'),
        ('Set-Cookie', 'c3=3; Expires=Wed, 19 Aug 2020 19:00:00 GMT'),
        ('Set-Cookie', 'c4=4; Expires=Thu, 20 Aug 2020 19:00:00 GMT'),
        ('Set-Cookie', 'c5=5'),
        ('Set-Cookie', 'c6=6; Path=/6'),
    ]

    now = time.mktime(time.strptime('2020-08-20 18:00:00 GMT', '%a, %d %b %Y %H:%M:%S %Z'))

    assert get

# Generated at 2022-06-13 22:45:36.481783
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:41.845166
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = 1585104701
    assert get_expired_cookies(
        headers=[
            ('Set-Cookie', 'foo=bar; path=/; expires=Tue, 21-Apr-2020 13:43:07 GMT; secure; HttpOnly'),
            ('Set-Cookie', 'bar=baz; path=/; expires=Wed, 20-Apr-2023 13:43:07 GMT; secure; HttpOnly; SameSite=Strict'),
            ('Set-Cookie', 'zoo=zoo; path=/; Max-Age=900; secure; HttpOnly; SameSite=Lax'),
        ],
        now=now
    ) == [
        {
            'name': 'foo',
            'path': '/',
        }
    ]

# Generated at 2022-06-13 22:45:51.635360
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookies = [
        (
            'set-cookie',
            'session=.eJyrVkpVkpVslJQAQ7; '
            'Domain=mydomain.com; '
            'Expires=Sun, 07 Apr 2019 17:13:03 GMT; '
            'Max-Age=604800; '
            'Path=/'
        ),
        (
            'set-cookie',
            'country=US; '
            'Domain=mydomain.com; '
            'Expires=Sat, 06 Apr 2019 17:13:03 GMT; '
            'Max-Age=86400; '
            'Path=/'
        ),
    ]

    expired_cookies = get_expired_cookies(headers=cookies)


# Generated at 2022-06-13 22:46:00.160384
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    t = 0.0
    headers = [
        ('Set-Cookie', 'a=1; Path=/; Max-Age=2'),
        ('Set-Cookie', 'b=2; Path=/; Expires=Wed, 01 Jan 2020 00:00:00 GMT'),
        ('Set-Cookie', 'c=3; Path=/; Expires=Wed, 01 Jan 2018 00:00:00 GMT'),
    ]
    assert get_expired_cookies(headers=headers, now=t) == []
    assert get_expired_cookies(headers=headers, now=t+1) == []
    assert get_expired_cookies(headers=headers, now=t+2) == [
        {'name': 'c', 'path': '/'}
    ]

# Generated at 2022-06-13 22:46:08.483230
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'a=1; Max-Age=2'),
        ('Set-Cookie', 'b=1; Max-Age=1'),
        ('Set-Cookie', 'c=1; Expires=Sun, Jun 3 2018 13:33:20 GMT'),
        ('Set-Cookie', 'd=1; Expires=Sun, Jun 3 2018 13:32:56 GMT'),
    ]

    now = time.time() + 1

    assert get_expired_cookies(headers=headers, now=now) == [
        {'name': 'b', 'path': '/'},
        {'name': 'd', 'path': '/'},
    ]


# Generated at 2022-06-13 22:46:21.007152
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:46:24.781027
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    s = "__cfduid=d8ea49bd55d66f7b60d69fbc3a8c5a9ba1517285094; expires=Wed, 05-Mar-20 06:24:54 GMT; path=/; domain=.strat.io; HttpOnly; Secure;"  # noqa
    headers = [('set-cookie', s)]
    assert get_expired_cookies(headers, now=1517285308.362332) == []
    assert get_expired_cookies(headers, now=1517285305.362332) == [
        {'name': '__cfduid', 'path': '/'}
    ]

# Generated at 2022-06-13 22:46:33.513621
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    h = [
        # The following three Set-Cookie headers should result in
        # cookies being expired.
        ('Set-Cookie', 'e_id=foo; Expires=Thu, 01 Jan 1970 00:00:00 GMT'),
        ('Set-Cookie', 'e_id=bar; Max-Age=0'),
        ('Set-Cookie', 'e_id=bax; Max-Age=0; Expires=Thu, 01 Jan 1970 00:00:00 GMT'),

        # This one should not:
        ('Set-Cookie', 'e_id=baz; Expires=Thu, 01 Jan 2027 00:00:00 GMT')
    ]


# Generated at 2022-06-13 22:46:38.599574
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('a.txt') == 'text/plain'
    assert get_content_type('a.html') == 'text/html'
    assert get_content_type('a.unknown') is None



# Generated at 2022-06-13 22:46:42.657801
# Unit test for function repr_dict
def test_repr_dict():
    from nose.tools import eq_

    eq_(repr_dict({'a': 1, 'b': 2}), "{'a': 1, 'b': 2}")
    eq_(repr_dict(OrderedDict([('a', 1), ('b', 2)])), "{'a': 1, 'b': 2}")

# Generated at 2022-06-13 22:46:43.589114
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    auth = ExplicitNullAuth()



# Generated at 2022-06-13 22:46:52.105143
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = 1578392646.662436
    headers = [
        ('set-cookie', 'name'),
        ('Set-Cookie', 'expires=Thu, 01 Jan 1970 00:00:00 GMT'),
        ('set-Cookie', 'expires=Wed, 01 Jan 2025 00:00:00 GMT'),
        ('set-Cookie', 'max-age=86400'),
        ('set-Cookie', 'max-age=3600; path=/'),
        ('set-Cookie', 'max-age=-1'),
    ]

# Generated at 2022-06-13 22:47:00.273059
# Unit test for function get_content_type
def test_get_content_type():
    """
    Test the content type detection.

    """
    assert get_content_type('testdata/example.json') == 'application/json'
    assert get_content_type('testdata/example.html') == 'text/html'
    assert get_content_type('testdata/example.txt') == 'text/plain'
    assert get_content_type('testdata/example.zip') == 'application/zip'
    assert get_content_type('testdata/example.unsupported') is None



# Generated at 2022-06-13 22:47:12.933748
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    import unittest
    import requests.compat
    from requests.compat import urljoin

    from unittest import mock
    from . import get_resource_path

    class ExplicitNullAuthTestCase(unittest.TestCase):
        """Test all of the functionality of class ExplicitNullAuth.
        """
        longMessage = True

        def setUp(self):
            """Set up the testing environment.
            """
            self.session = requests.Session()
            self.auth = ExplicitNullAuth()
            self.session.auth = self.auth
            self.ratelimit_reached_url = urljoin(
                'file:///',
                requests.compat.quote(
                    get_resource_path('ratelimit_reached'),
                    safe='/:'
                )
            )


# Generated at 2022-06-13 22:47:20.745548
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:47:30.283385
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # A cookie as defined by RFC6265.
    # <http://tools.ietf.org/html/rfc6265#section-4.1>
    cookie_a_httponly = (
        'Set-Cookie: a=b; Expires=Tue, 15-Jan-2013 21:47:38 GMT;'
        ' Path=/; Domain=.example.com; HttpOnly'
    )
    # A cookie with a `max-age` attribute.
    cookie_b_max_age = (
        'Set-Cookie: b=c; Max-Age=120; Path=/; Domain=.localhost; HttpOnly'
    )

    headers = [cookie_a_httponly, cookie_b_max_age]
    expired_cookies = get_expired_cookies(headers, now=time.time())


# Generated at 2022-06-13 22:47:32.220175
# Unit test for function get_content_type
def test_get_content_type():
    filename = 'requests_toolbelt/__init__.py'
    content_type = get_content_type(filename)
    assert content_type == 'text/x-python'



# Generated at 2022-06-13 22:47:42.208493
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import requests

    now = time.time()
    cookie = 'name=value; Path=/; Expires=Fri, 11-Dec-2087 16:44:40 GMT'
    url = 'http://www.google.com/'
    cookies = requests.utils.dict_from_cookiejar(requests.get(url).cookies)
    cookies['cookie'] = cookie
    s = requests.utils.cookiejar_from_dict(cookies)
    headers = requests.utils.dict_from_cookiejar(s)
    assert not get_expired_cookies(headers=list(headers.items()), now=now)

    cookie = 'name=value; Path=/; Max-Age=0'
    url = 'http://www.google.com/'

# Generated at 2022-06-13 22:47:47.208914
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    import requests
    auth = ExplicitNullAuth()
    request = requests.PreparedRequest()
    assert auth(request) is request

# Generated at 2022-06-13 22:47:49.825538
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    assert load_json_preserve_order('{"a": 1, "b": 2}') == OrderedDict([('a', 1), ('b', 2)])

# Generated at 2022-06-13 22:47:51.371464
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:47:55.129533
# Unit test for function repr_dict
def test_repr_dict():
    d = {'a': 1, 'b': 2}
    s = repr_dict(d)
    assert s == "{\n    'a': 1,\n    'b': 2\n}"

# Generated at 2022-06-13 22:47:59.245295
# Unit test for function repr_dict
def test_repr_dict():
    d = {'a':1, 'b':2, 'c':3}
    assert repr_dict(d) == "{'a': 1, 'b': 2, 'c': 3}"


# Generated at 2022-06-13 22:48:06.368009
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('README.md') is None
    assert get_content_type('foobar.mkv') == 'video/x-matroska'
    assert get_content_type('foobar.mkv') == 'video/x-matroska'
    assert get_content_type('foo.tar.xz') == 'application/x-xz-compressed-tar'

# Generated at 2022-06-13 22:48:18.175812
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from inspect import cleandoc

    now = time.time()

# Generated at 2022-06-13 22:48:19.442951
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'a': 'b'}) == "{'a': 'b'}"

# Generated at 2022-06-13 22:48:24.010017
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({}) == '{}'
    assert repr_dict({'a': 'b'}) == "{'a': 'b'}"
    assert repr_dict({'a': 1}) == "{'a': 1}"

# Generated at 2022-06-13 22:48:26.969903
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = """{"a": 1, "b": 2}"""
    result = load_json_preserve_order(s)
    assert result.keys() == ['a', 'b']

# Generated at 2022-06-13 22:48:43.034795
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'food1=value1; Expires=Mon, 09-Jan-2017 10:07:26 GMT; Path=/'),
        ('Set-Cookie', 'food2=value2; Expires=Mon, 09-Jan-2017 10:07:26 GMT; Path=/'),
        ('Set-Cookie', 'food3=value3; Max-Age=300; Path=/'),
        ('Set-Cookie', 'food4=value4; Expires=Mon, 09-Jan-2017 10:07:26 GMT; Path=/'),
    ]
    now = 1484896045.926992
    actual = get_expired_cookies(headers, now=now)


# Generated at 2022-06-13 22:48:57.059240
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    past = now - 100
    future = now + 100

# Generated at 2022-06-13 22:49:06.381331
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    # load_json_preserve_order preserves the dictionary parsed from JSON,
    # and in Python 3, the order of the items in the dictionary.
    # The returned value should be dict type
    assert type(load_json_preserve_order('{"a": "a", "b": "b"}')) == dict
    assert type(load_json_preserve_order('{"c": "c", "d": "d"}')) == dict

    # load_json_preserve_order preservers the dictionary parsed from JSON,
    # and in Python 3, the order of the items in the dictionary.
    assert load_json_preserve_order('{"a": "a", "b": "b"}') == {'a': 'a', 'b': 'b'}

# Generated at 2022-06-13 22:49:11.337587
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from unittest import mock
    from datetime import datetime, timedelta

    now = mock.Mock(return_value=datetime.utcfromtimestamp(1524639998))
    headers = [
        (
            'Set-Cookie',
            'duration=short; Expires=Tue, 15 May 2018 01:03:18 GMT; HttpOnly; Path=/'
        ),
        (
            'Set-Cookie',
            'duration=long; max-age=630720000; HttpOnly; Path=/'
        ),
        (
            'Set-Cookie',
            'duration=short; Expires=Tue, 15 May 2018 01:03:18 GMT; HttpOnly; Path=/foo/'
        )
    ]

    now = datetime.utcfromtimestamp(1524639998)


# Generated at 2022-06-13 22:49:13.584128
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:49:14.228583
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    ExplicitNullAuth()

# Generated at 2022-06-13 22:49:21.519447
# Unit test for function humanize_bytes

# Generated at 2022-06-13 22:49:25.493410
# Unit test for function get_content_type
def test_get_content_type():
    test_json = 'test.json'
    assert get_content_type(test_json) == 'application/json'


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 22:49:28.105129
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    request = requests.Request('GET', 'https://example.com')
    auth = ExplicitNullAuth()
    request = auth(request)
    assert request is not None, 'request should be not None'

# Generated at 2022-06-13 22:49:29.496414
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/tmp/test.jpg') == 'image/jpeg'

# Generated at 2022-06-13 22:49:47.259739
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # type: () -> None
    """
    Unit test for function get_expired_cookies
    """
    import datetime
    import unittest
    import requests

    unittest.TestCase.assertDictEqual # type: ignore
    unittest.TestCase.assertEqual     # type: ignore

    class GetExpiredCookiesTest(unittest.TestCase):
        def test_no_cookies(self):
            res = requests.Response()
            cookies = get_expired_cookies(res.headers)
            self.assertEqual(0, len(cookies))

        def test_no_expired_cookies(self):
            res = requests.Response()
            res.headers.append(('Set-Cookie', 'foo=bar; path=/'))

# Generated at 2022-06-13 22:49:49.985468
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    a = ExplicitNullAuth()
    # "TypeError: __call__() takes 2 positional arguments but 3 were given"
    # This would happen if __call__ was an instance method
    a()

# Generated at 2022-06-13 22:49:50.553667
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:50:01.673061
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    # This minimal test just tests that .netrc is ignored.
    import logging
    import netrc
    from unittest.mock import patch
    from requests.auth import HTTPBasicAuth
    from requests.auth import HTTPDigestAuth

    # This is the test environment for this unit test.
    # The .netrc file contains credentials for some host names,
    # but NOT for 'this.host.invalid', which is the host name
    # that the test will use.
    with open(__file__, 'rb') as this_module_file:
        test_netrc = this_module_file.read()
    netrc_filename = 'explicit-null-auth-test.netrc'

# Generated at 2022-06-13 22:50:02.218042
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:50:04.298948
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    req = requests.Request('GET', 'http://localhost/')
    prepared = ExplicitNullAuth()(req)
    assert prepared.headers == {}

# Generated at 2022-06-13 22:50:13.021256
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:50:25.424698
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:50:32.299966
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = '{"a": 2, "b": 1}'
    assert load_json_preserve_order(s) == OrderedDict([('a', 2), ('b', 1)])

    s = '{"b": 1, "a": 2}'
    assert load_json_preserve_order(s) == OrderedDict([('b', 1), ('a', 2)])

# Generated at 2022-06-13 22:50:40.464607
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({}) == '{}'
    assert repr_dict({'a': 1}) == "{'a': 1}"
    assert repr_dict({'a': 1, 'b': 2}) == "{'a': 1, 'b': 2}"
    assert repr_dict({'b': 2, 'a': 1}) == "{'b': 2, 'a': 1}"
    assert repr_dict({'a': 1, 'b': [2, 3]}) == "{'a': 1, 'b': [2, 3]}"
    assert repr_dict({'a': 1, 'b': {'c': 3}}) == "{'a': 1, 'b': {'c': 3}}"