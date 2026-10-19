

# Generated at 2022-06-13 22:43:59.550346
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import copy
    import pytest

    now = 0.0
    then = 1.0
    later = 2.0
    much_later = 3.0


# Generated at 2022-06-13 22:44:13.526607
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'foo=bar; Path=/; Expires=Tue, 01 Jan 2019 00:00:00 GMT'),
        ('Set-Cookie', 'baz=quux; Path=/; Expires=Tue, 01 Jan 2019 00:00:00 GMT'),
        ('Set-Cookie', 'quuux=quuuux; Path=/; Expires=Tue, 01 Jan 2019 00:00:00 GMT'),
        ('Set-Cookie', 'corge=grault; Path=/; Expires=Tue, 01 Jan 2019 00:00:00 GMT'),
        ('Set-Cookie', 'garply=waldo; Path=/; Expires=Tue, 01 Jan 2019 00:00:00 GMT'),
    ]
    cookies = get_expired_cookies(headers=headers, now=1213613717.296)
   

# Generated at 2022-06-13 22:44:15.178482
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.png') == 'image/png'

# Generated at 2022-06-13 22:44:21.587526
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import time
    now = time.time()
    unix_time = lambda x: now + x
    headers = [
        ('Set-Cookie', 'test=test; Max-Age=10; Path=/path'),
        ('Set-Cookie', 'test2=test2; Max-Age=20; Path=/path2'),
        ('Set-Cookie', 'test3=test3; Path=/path3; Expires={:f}'.format(unix_time(10))),
        ('Set-Cookie', 'test4=test4; Path=/path4; Expires={:f}'.format(unix_time(20))),
    ]

# Generated at 2022-06-13 22:44:27.904599
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.bin') == 'application/octet-stream'
    assert get_content_type('/tmp/test.TXT') == 'text/plain'
    assert get_content_type('/tmp/test.BIN') == 'application/octet-stream'
    assert get_content_type('test') is None



# Generated at 2022-06-13 22:44:40.130274
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # Note: the cookie received by requests.py is not a dict but a list.
    # We need to convert it to a dict here.
    def _to_dict(cookie):
        return {
            'name': cookie['name'],
            'path': cookie['path']
        }

    def _assert_expired_cookies(
        headers,
        now,
        expected_expired_cookies
    ):
        expired_cookies = get_expired_cookies(
            headers=headers,
            now=now
        )
        assert set(map(_to_dict, expired_cookies)) == set(expected_expired_cookies)


# Generated at 2022-06-13 22:44:41.965344
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('file.png') == 'image/png'

# Generated at 2022-06-13 22:44:52.942826
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import datetime

    expired_past = datetime.datetime(year=2020, month=5, day=5)
    expired_future = datetime.datetime(year=2030, month=5, day=5)

    def to_expires_date(dt: datetime.datetime) -> str:
        return dt.strftime('%a, %d-%b-%Y %H:%M:%S %Z')

    def assert_expired(expected, headers, now=None, expired_count=None):
        expired = get_expired_cookies(headers=headers, now=now)
        print('expected', expected)
        print('got', expired)
        assert expected == expired
        if expired_count:
            assert len(expired) == expired_count, expired


# Generated at 2022-06-13 22:44:59.466999
# Unit test for function get_content_type
def test_get_content_type():
    # noinspection PyUnresolvedReferences
    """
    >>> print(get_content_type('test.txt'))
    text/plain
    >>> print(get_content_type('test.html'))
    text/html
    >>> print(get_content_type('test.md'))
    text/plain; charset=us-ascii
    >>> print(get_content_type('test.png'))
    image/png

    """

# Generated at 2022-06-13 22:45:10.090972
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from unittest import TestCase
    from datetime import datetime, timedelta, timezone

    def utc_offset() -> timedelta:
        dt = datetime.now()
        return dt.utcoffset() - dt.dst()

    def expired_cookies():
        now = time.time()
        utc_offset = datetime.now(timezone.utc).astimezone().utcoffset()
        # The second element in each tuple is the cookie expiration date
        # expressed in UTC timezone.

# Generated at 2022-06-13 22:45:22.923913
# Unit test for function humanize_bytes
def test_humanize_bytes():
    assert humanize_bytes(1) == '1 B'
    assert humanize_bytes(1024, precision=1) == '1.0 kB'
    assert humanize_bytes(1024 * 123, precision=1) == '123.0 kB'
    assert humanize_bytes(1024 * 12342, precision=1) == '12.1 MB'
    assert humanize_bytes(1024 * 12342, precision=2) == '12.05 MB'
    assert humanize_bytes(1024 * 1234, precision=2) == '1.21 MB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == '1.31 GB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == '1.3 GB'
    print('Tests passed')


# Unit test

# Generated at 2022-06-13 22:45:30.644962
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.svg') == 'image/svg+xml'
    assert get_content_type('foo.TXT') == 'text/plain'
    assert get_content_type('foo.TXT') == 'text/plain'

# Generated at 2022-06-13 22:45:39.672406
# Unit test for function get_content_type
def test_get_content_type():
    from .utils import get_content_type

    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('README') == 'text/plain'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.csv') == 'text/csv'
    assert get_content_type('foo.xls') == 'application/vnd.ms-excel'
    assert get_content_type('foo.docx') == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    assert get_content_type('foo.JPG') == 'image/jpeg'
    assert get_content_type('foo.tif') == 'image/tiff'

# Generated at 2022-06-13 22:45:47.704528
# Unit test for function get_content_type
def test_get_content_type():
    """
    ``get_content_type`` should return the Content-Type for known files,
    and None for unknown files.

    """
    tests = {
        'test.txt': 'text/plain',
        'test.pdf': 'application/pdf',
        'test.json': 'application/json',
        'test.unknown': None,
    }
    for filename, expected in tests.items():
        assert get_content_type(filename) == expected

# Generated at 2022-06-13 22:45:57.431966
# Unit test for function humanize_bytes
def test_humanize_bytes():
    assert humanize_bytes(1) == '1 B'
    assert humanize_bytes(1024, precision=1) == '1.0 kB'
    assert humanize_bytes(1024 * 123, precision=1) == '123.0 kB'
    assert humanize_bytes(1024 * 12342, precision=1) == '12.1 MB'
    assert humanize_bytes(1024 * 12342, precision=2) == '12.05 MB'
    assert humanize_bytes(1024 * 1234, precision=2) == '1.21 MB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == '1.31 GB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == '1.3 GB'

# Generated at 2022-06-13 22:46:03.020198
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/path/to/file.txt') == 'text/plain'
    assert get_content_type('/path/to/file.txt.gz') == 'application/x-gzip'
    assert get_content_type('/path/to/file.txt.bz2') == 'application/x-bzip2'
    assert get_content_type('/path/to/file.zip') == 'application/zip'
    assert get_content_type('/path/to/file.xml') == 'application/xml'
    assert get_content_type('/path/to/file.json') == 'application/json'
    assert get_content_type('/path/to/file.svg') == 'image/svg+xml'

# Generated at 2022-06-13 22:46:15.091145
# Unit test for function humanize_bytes
def test_humanize_bytes():
    assert humanize_bytes(1) == '1 B'
    assert humanize_bytes(1024, precision=1) == '1.0 kB'
    assert humanize_bytes(1024 * 123, precision=1) == '123.0 kB'
    assert humanize_bytes(1024 * 12342, precision=1) == '12.1 MB'
    assert humanize_bytes(1024 * 12342, precision=2) == '12.05 MB'
    assert humanize_bytes(1024 * 1234, precision=2) == '1.21 MB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == '1.31 GB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == '1.3 GB'
    return True

# Generated at 2022-06-13 22:46:16.440152
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test/test.test') == 'test/test'

# Generated at 2022-06-13 22:46:28.382983
# Unit test for function humanize_bytes

# Generated at 2022-06-13 22:46:40.680223
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    assert not get_expired_cookies([])
    assert get_expired_cookies([('Set-Cookie', 'cookie_name=cookie_value; max-age=7')], now=now)
    assert not get_expired_cookies([('Set-Cookie', 'cookie_name=cookie_value; max-age=7')], now=now+7)
    assert not get_expired_cookies([('Set-Cookie', 'cookie_name=cookie_value; expires=%s' % (now+7))], now=now)
    assert not get_expired_cookies([('Set-Cookie', 'cookie_name=cookie_value; expires=%s' % (now+7))], now=now+7)

# Generated at 2022-06-13 22:46:47.223925
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookies = get_expired_cookies(
        headers=[
            ('Set-Cookie', 'expires=1.1; Max-Age=0')
        ],
        now=2.2
    )
    assert len(cookies) == 1
    assert cookies[0] == {'name': 'expires', 'path': '/'}


# For use with pytest fixtures

# Generated at 2022-06-13 22:46:54.100460
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'A=1; Path=/my/path; Expires=Tue, 18 Aug 2020 07:28:42 GMT'),
        ('Set-Cookie', 'B=2; Path=/my/path/2; Max-Age=10'),
        ('Set-Cookie', 'C=3; Path=/my/path; Expires=Tue, 18 Aug 2020 07:28:42 GMT'),
        ('Set-Cookie', 'D=4; Expires=Tue, 18 Aug 2020 07:28:42 GMT'),
    ]
    now = time.mktime(time.strptime("Tue, 18 Aug 2020 07:28:42 GMT", "%a, %d %b %Y %H:%M:%S GMT"))
    expired = get_expired_cookies(headers, now)

# Generated at 2022-06-13 22:47:03.770550
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'a1=1; path=/; expires=Tue, 04 Jun 2019 10:47:16 GMT'),
        ('Set-Cookie', 'a2=2; path=/; max-age=60'),  # max-age in seconds
        ('Set-Cookie', 'a3=3; path=/; max-age=3600'),  # max-age in seconds
        ('Set-Cookie', 'a4=4; path=/; max-age='),  # not digits
        ('Set-Cookie', 'a5=5; path=/; max-age=abcd'),  # not digits
        ('Set-Cookie', 'a6=6; path=/; max-age=30'),  # max-age in seconds
    ]
    now = 1026008036

# Generated at 2022-06-13 22:47:18.353985
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime, timedelta

    def cookie_str_to_tuple(cookie_str: str) -> Tuple[str, str]:
        return cookie_str.split(': ')


# Generated at 2022-06-13 22:47:28.831196
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    yesterday = now - 86400

# Generated at 2022-06-13 22:47:35.546756
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = 1591850325

# Generated at 2022-06-13 22:47:44.009471
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from urllib.parse import urlencode
    from datetime import datetime, timedelta
    from email.utils import formatdate


# Generated at 2022-06-13 22:47:54.021404
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('Set-Cookie', 'foo=bar; Domain=example.com; Path=/'),
        ('Set-Cookie', 'bar=baz; Domain=example.com; Path=/; Max-Age=3600'),
        ('Set-Cookie', 'baz=qux; Domain=example.com; Path=/; Expires=Tue, 09-Oct-2018 04:18:48 GMT'),
    ]
    now = time.mktime(time.strptime('Tue, 09-Oct-2018 03:18:48 GMT', '%a, %d-%b-%Y %H:%M:%S GMT'))

# Generated at 2022-06-13 22:48:01.853942
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:48:10.067350
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # Expired cookies
    expired_headers = [
        ('Set-Cookie', 'a=b; max-age=0'),
        ('Set-Cookie', 'c=d; expires=Mon, 01 Jan 2018 00:00:00 GMT'),
        ('Set-Cookie', 'e=f; max-age=-1'),
    ]
    now = time.time()

    assert get_expired_cookies(expired_headers, now=now) == [
        {
            'name': 'a',
            'path': '/'
        }, {
            'name': 'e',
            'path': '/'
        }
    ]


# Generated at 2022-06-13 22:48:12.485442
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = '[{"a": {"b": 1}}]'
    assert load_json_preserve_order(s) == [{'a': {'b': 1}}]

# Generated at 2022-06-13 22:48:16.791465
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('filename.txt') == 'text/plain'
    assert get_content_type('filename.json') == 'application/json'
    assert get_content_type('filename.css') == 'text/css'
    assert get_content_type('filename.jpg') == 'image/jpeg'
    assert get_content_type('filename.png') == 'image/png'
    assert get_content_type('filename.gif') == 'image/gif'

# Generated at 2022-06-13 22:48:28.981012
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    json_str = """
        {
            "a": 1,
            "b": 2,
            "c": 3
        }
    """
    r = load_json_preserve_order(json_str)
    assert 'a' == list(r.keys())[0]
    assert 'b' == list(r.keys())[1]
    assert 'c' == list(r.keys())[2]
    assert 'a' == list(iter(r))[0]
    assert 'b' == list(iter(r))[1]
    assert 'c' == list(iter(r))[2]
    assert 'a' == list(r.values())[0]
    assert 'b' == list(r.values())[1]
    assert 'c' == list(r.values())[2]

# Generated at 2022-06-13 22:48:36.353069
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    assert load_json_preserve_order('{"foo": 42, "bar": "baz"}') == OrderedDict([('foo', 42), ('bar', 'baz')])
    assert load_json_preserve_order('[1, 2, 3]') == [1, 2, 3]
    assert load_json_preserve_order('"string"') == 'string'
    assert load_json_preserve_order('null') is None


# Generated at 2022-06-13 22:48:38.758238
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    test_dict = {'c': 3, 'b': 2, 'a': 1}
    assert load_json_preserve_order(json.dumps(test_dict)) == test_dict

# Generated at 2022-06-13 22:48:47.145226
# Unit test for function humanize_bytes
def test_humanize_bytes():
    if humanize_bytes(1) != '1 B':
        raise ValueError("Expected '1 B', got: %s" % humanize_bytes(1))
    if humanize_bytes(1024, 1) != '1.0 kB':
        raise ValueError("Expected '1.0 kB', got: %s" % humanize_bytes(1024, 1))
    if humanize_bytes(1024 * 123, 1) != '123.0 kB':
        raise ValueError("Expected '123.0 kB', got: %s" % humanize_bytes(1024 * 123, 1))
    if humanize_bytes(1024 * 12342, 1) != '12.1 MB':
        raise ValueError("Expected '12.1 MB', got: %s" % humanize_bytes(1024 * 12342, 1))
   

# Generated at 2022-06-13 22:48:52.194394
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    cookie_expires = now + 86400
    cookie_max_age = '86400'
    cookie_path = '/'
    cookie_name = 'test'
    headers = [
        ('Set-Cookie', '%s=%s; Expires=%s; Max-Age=%s; Path=%s; HttpOnly' % (
            cookie_name,
            'deleted',
            time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(cookie_expires)),
            cookie_max_age,
            cookie_path,
        )),
    ]
    expired_cookies = [
        {
            'path': cookie_path,
            'name': cookie_name
        }
    ]
    assert get

# Generated at 2022-06-13 22:48:53.494347
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth() is not None

# Generated at 2022-06-13 22:48:55.602695
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from ipdb import set_trace
    set_trace()

# Generated at 2022-06-13 22:49:04.149515
# Unit test for function humanize_bytes
def test_humanize_bytes():
    test_pairs = [
        (0, '0 B'),
        (1, '1 B'),
        (10, '10 B'),
        (100, '100 B'),
        (1000, '1000 B'),
        (1024, '1.0 kB'),
        (1024 * 1024, '1.0 MB'),
        (1024 ** 3, '1.0 GB'),
        (1024 ** 3 * 5, '5.0 GB'),
    ]
    # noinspection PyTypeChecker
    for nbytes, expected in test_pairs:
        # noinspection PyTypeChecker
        assert humanize_bytes(nbytes) == expected

# Generated at 2022-06-13 22:49:29.172036
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from functools import partial

    expires = partial(
        dict,
        name='session',
        **{'path': '/', 'expires': time.time() + 7200}
    )
    assert get_expired_cookies([('Set-Cookie', 'session=a; Path=/')]) == []

    assert get_expired_cookies([('Set-Cookie', 'session=b; Path=/')], 0) == [
        expires(),
    ]

    assert get_expired_cookies([('Set-Cookie', 'session=b; Path=/')], 7200) == []


# Generated at 2022-06-13 22:49:32.119447
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    assert load_json_preserve_order('{"a": 0, "b": 1, "c": 2}') == {"a": 0, "b": 1, "c": 2}

# Generated at 2022-06-13 22:49:45.910828
# Unit test for function humanize_bytes
def test_humanize_bytes():
    assert humanize_bytes(1) == '1 B'
    assert humanize_bytes(1024, precision=1) == '1.0 kB'
    assert humanize_bytes(1024 * 123, precision=1) == '123.0 kB'
    assert humanize_bytes(1024 * 12342, precision=1) == '12.1 MB'
    assert humanize_bytes(1024 * 12342, precision=2) == '12.05 MB'
    assert humanize_bytes(1024 * 1234, precision=2) == '1.21 MB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == '1.31 GB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == '1.3 GB'

# Generated at 2022-06-13 22:49:53.101722
# Unit test for function repr_dict
def test_repr_dict():
    import random
    for _ in range(10):
        d = {
            str(random.randint(0, 1000000)):str(random.randint(0, 1000000)),
            str(random.randint(0, 1000000)):str(random.randint(0, 1000000)),
            str(random.randint(0, 1000000)):str(random.randint(0, 1000000)),
            str(random.randint(0, 1000000)):str(random.randint(0, 1000000))
        }
        assert repr_dict(d) == pformat(d)

# Generated at 2022-06-13 22:50:03.754461
# Unit test for function humanize_bytes
def test_humanize_bytes():
    # Author: Doug Latornell
    # Licence: MIT
    # URL: https://code.activestate.com/recipes/577081/

    def test_examples():
        assert humanize_bytes(1) == "1 B"
        assert humanize_bytes(1024, precision=1) == "1.0 kB"
        assert humanize_bytes(1024 * 123, precision=1) == "123.0 kB"
        assert humanize_bytes(1024 * 12342, precision=1) == "12.1 MB"
        assert humanize_bytes(1024 * 12342, precision=2) == "12.05 MB"
        assert humanize_bytes(1024 * 1234, precision=2) == "1.21 MB"

# Generated at 2022-06-13 22:50:12.759528
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    test_data = [
        (
            '{"key1": "val1", "key2": "val2"}',
            dict(key1='val1', key2='val2')
        ),
        (
            '{"key2": "val2", "key1": "val1"}',
            dict(key2='val2', key1='val1')
        ),
        (
            '{"key1": ["val1", "val2"], "key2": "val3"}',
            dict(key1=list(('val1', 'val2')), key2='val3')
        ),
    ]
    for json_data, obj_data in test_data:
        obj = load_json_preserve_order(json_data)
        assert obj == obj_data

# Generated at 2022-06-13 22:50:19.194028
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookie = 'sessionid=123ABC; Path=/; Max-Age=2627200; Expires=Tue, 14-Aug-20 08:24:33 GMT; HttpOnly; Secure'
    expired_cookies = get_expired_cookies([('set-cookie', cookie)], now=time.time() + 86400)
    assert expired_cookies == [{'name': 'sessionid', 'path': '/'}]

# Generated at 2022-06-13 22:50:21.811829
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'a': 123, 'b': [1, 2, 3]}) == '{\'a\': 123, \'b\': [1, 2, 3]}'

# Generated at 2022-06-13 22:50:27.717410
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    """
    Unit test for method __call__ of the class ExplicitNullAuth.
    """

    class request:
        '''
        Pretend class for a requests request.
        '''

        def __init__(self):
            self.method = 'POST'

    # ExplicitNullAuth method __call__ should return self.
    my_null_auth = ExplicitNullAuth()
    assert my_null_auth(request()) == request()

# Generated at 2022-06-13 22:50:38.650312
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    """A unit test for load_json_preserve_order."""
    source = (
        '[{"b": 1, "a": 2}, {"c": 2, "a": 1}, {"a": 0, "b": 1},'
        ' {"d": 0, "a": 1}, {"c": 1, "b": 2}, {"d": 0, "b": 2}]'
    )