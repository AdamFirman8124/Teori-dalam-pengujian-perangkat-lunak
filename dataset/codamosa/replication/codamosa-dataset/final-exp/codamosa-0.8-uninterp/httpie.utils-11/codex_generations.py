

# Generated at 2022-06-13 22:43:54.562663
# Unit test for function get_content_type

# Generated at 2022-06-13 22:44:05.221814
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import pytest
    from io import BytesIO
    from http.cookies import SimpleCookie

    # Test a single cookie
    headers = [
        (
            'Set-cookie',
            'ABC=ghi; Path=/; HttpOnly; Expires=Wed, 13 Jan 2021 22:23:01 GMT; Max-Age=300'
        )
    ]
    # Max-Age is 300 seconds
    now = 1610654375
    assert get_expired_cookies(headers, now) == [{'name': 'ABC', 'path': '/'}]
    # 5 minutes (300 seconds) later, the cookie is not expired yet
    now += 300
    assert get_expired_cookies(headers, now) == []

    # Test multiple cookies

# Generated at 2022-06-13 22:44:16.982753
# Unit test for function get_content_type
def test_get_content_type():
    from .test_helpers import _TestBase

    class TestGetContentType(_TestBase):

        def test_jpg_image(self):
            self.assertEqual(
                get_content_type('test.jpg'), 'image/jpeg'
            )

        def test_jpeg_image(self):
            self.assertEqual(
                get_content_type('test.jpeg'), 'image/jpeg'
            )

        def test_png_image(self):
            self.assertEqual(
                get_content_type('test.png'), 'image/png'
            )

        def test_unknown(self):
            self.assertEqual(
                get_content_type('test.xyz'), None
            )

# Generated at 2022-06-13 22:44:28.713236
# Unit test for function get_content_type

# Generated at 2022-06-13 22:44:35.578147
# Unit test for function get_content_type
def test_get_content_type():
    """
    Test get_content_type functions.

    """
    # content_type = get_content_type('abc.pdf')
    content_type = get_content_type('abc.jpg')
    content_type = get_content_type('abc.jpeg')
    content_type = get_content_type('abc.png')
    content_type = get_content_type('abc.gif')
    assert content_type == 'image/png'

# Generated at 2022-06-13 22:44:45.753290
# Unit test for function get_content_type
def test_get_content_type():
    cases = [
        ('foo.txt', 'text/plain'),
        ('foo.csv', 'text/plain'),
        ('foo.xlsx', 'application/vnd.openxmlformats-officedocument.'
                    'spreadsheetml.sheet'),
        ('foo.xml', 'application/xml'),
        ('foo.json', 'application/json'),
        ('foo.zip', 'application/zip'),
        ('foo.pdf', 'application/pdf'),
        ('foo.txt.gz', 'application/gzip'),
        ('foo.zip.gz', 'application/gzip'),
        ('foo.csv.gz', 'application/gzip'),
    ]

    for filename, content_type in cases:
        assert get_content_type(filename) == content_type

# Generated at 2022-06-13 22:44:50.290684
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.svg') == 'image/svg+xml'
    assert get_content_type('test.jpe') == 'image/jpeg'
    assert get_content_type('test.jpeg') == 'image/jpeg'
    assert get_content_type('test.jp2') == 'image/jp2'
    assert get_content_type('.jpeg') == 'image/jpeg'

# Generated at 2022-06-13 22:45:02.341025
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:11.115074
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', '1=1'),
        ('Set-Cookie', '2=2; Max-Age=0'),
        ('Set-Cookie', '3=3; Max-Age=10'),
        ('Set-Cookie', '4=4; Max-Age=1'),
        ('Set-Cookie', '5=5; Expires=Fri, 31 Dec 1999 23:59:59 GMT'),
        ('Set-Cookie', '6=6; Expires=Tue, 26 Jun 2029 15:18:29 GMT'),
    ]

# Generated at 2022-06-13 22:45:18.959009
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    cookies = get_expired_cookies(
        [('Set-Cookie', 'a=1; path=/; expires=%s' % now),
         ('set-cookie', 'b=2; path=/;')],
        now=now
    )
    assert len(cookies) == 2
    assert cookies == [
        {'name': 'a', 'path': '/'},
        {'name': 'b', 'path': '/'},
    ]

# Generated at 2022-06-13 22:45:33.874019
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('file.txt') == 'text/plain'
    assert get_content_type('file.mp3') == 'audio/mpeg'
    assert get_content_type('file.zip') == 'application/zip'
    assert get_content_type('file.xml') == 'application/xml'
    assert get_content_type('file.xhtml') == 'application/xhtml+xml'
    assert get_content_type('file.html') == 'text/html; charset=ISO-8859-1'
    assert get_content_type('file.js') == 'application/javascript'
    assert get_content_type('file.json') == 'application/json'
    assert get_content_type('file.png') == 'image/png'

# Generated at 2022-06-13 22:45:37.758420
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('spam.jpg') == 'image/jpeg'
    assert get_content_type('spam.txt') == 'text/plain'
    assert get_content_type('spam.xyz') is None

# Generated at 2022-06-13 22:45:46.520701
# Unit test for function get_content_type
def test_get_content_type():
    # Import this here to avoid circular imports
    from httmock import HTTMock

    with HTTMock(mimetypes_get):
        assert get_content_type('test.txt') == 'text/plain; charset=us-ascii'
        assert get_content_type('test.pdf') == 'application/pdf'
        assert get_content_type(
            'test.html'
        ) == 'text/html; charset=iso8859-1'

    assert get_content_type('test.exe') is None



# Generated at 2022-06-13 22:45:53.363429
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('x.pdf') == 'application/pdf'
    assert get_content_type('x.PDF') == 'application/pdf'
    assert get_content_type('x.PDf') is None
    assert get_content_type('') is None
    assert get_content_type('.') is None
    assert get_content_type('..') is None

# Generated at 2022-06-13 22:45:59.545885
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.js') == 'application/javascript'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.css') == 'text/css'

# Generated at 2022-06-13 22:46:05.513678
# Unit test for function get_content_type
def test_get_content_type():
    mimetypes.init()
    assert get_content_type('foo.txt') == 'text/plain; charset=us-ascii'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.txt') == 'text/plain; charset=us-ascii'
    assert get_content_type('foo.txt') == 'text/plain; charset=us-ascii'
    assert get_content_type('foo.txt') == 'text/plain; charset=us-ascii'
    assert get_content_type('foo.txt') == 'text/plain; charset=us-ascii'

# Generated at 2022-06-13 22:46:12.114851
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('custom.gif') == 'image/gif'
    assert get_content_type('custom.jpg') == 'image/jpeg'
    assert get_content_type('custom.jpeg') == 'image/jpeg'
    assert get_content_type('custom.html') == 'text/html'
    assert get_content_type('custom.js') == 'application/javascript'



# Generated at 2022-06-13 22:46:20.399127
# Unit test for function get_content_type
def test_get_content_type():
    assert 'image/png' == get_content_type('foo.png')
    assert 'text/plain; charset=iso-8859-1' == get_content_type('foo.txt')
    assert 'text/plain; charset=utf-8' == get_content_type('foo.css')
    assert 'application/octet-stream' == get_content_type('foo.bin')
    assert 'application/octet-stream' == get_content_type('foo')
    assert not get_content_type('foo.blah')

# Generated at 2022-06-13 22:46:28.342360
# Unit test for function get_content_type
def test_get_content_type():
    filenames = [
        '',
        '.',
        '..',
        '/etc/passwd',
        '/dev/null',
        '/a/bcd',
        '/a/bcd.html',
        '/a/bcd.html.gz',
        'bcd',
        'bcd.html',
        'bcd.html.gz',
    ]
    for filename in filenames:
        print(filename)
        print(get_content_type(filename))
        print('---')

# Generated at 2022-06-13 22:46:33.729816
# Unit test for function get_content_type
def test_get_content_type():
    """
    Test that get_content_type works as expected.
    """

    sample_file = 'tests/sample.txt'
    content_type = get_content_type(sample_file)

    assert content_type == 'text/plain', content_type

# Generated at 2022-06-13 22:46:40.428905
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') is None
    assert get_content_type('foo.gif') == 'image/gif'
    assert get_content_type('foo.gif.txt') is None
    assert get_content_type('foo.gif') == 'image/gif'


# Generated at 2022-06-13 22:46:50.303696
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.csv') == 'text/csv'
    assert get_content_type('foo.csv.txt') == 'text/plain'
    assert get_content_type('foo.csv.gz') == 'application/gzip'
    assert get_content_type('foo.txt.gz') == 'application/gzip'
    assert get_content_type('foo.txt.bz2') == 'application/x-bzip2'
    assert get_content_type('foo.tar.gz') == 'application/gzip'
    assert get_content_type('foo.tar.bz2') == 'application/x-bzip2'
    assert get_content_type('foo.zip') == 'application/zip'

# Generated at 2022-06-13 22:46:51.424754
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.css') == 'text/css'



# Generated at 2022-06-13 22:46:52.854410
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('file.txt') == 'text/plain'

# Generated at 2022-06-13 22:47:03.196322
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('some-file.png') == 'image/png'
    assert get_content_type('some-file.pdf') == 'application/pdf'
    assert get_content_type('some-file.svg') == 'image/svg+xml'
    assert get_content_type('some-file.css') == 'text/css'
    assert get_content_type('some-file.html') == 'text/html'
    assert get_content_type('some-file.js') == 'application/javascript'

    assert not get_content_type('some-file.bz2')
    assert not get_content_type('some-file.dat')
    assert not get_content_type('some-file.txt')



# Generated at 2022-06-13 22:47:13.712728
# Unit test for function get_content_type
def test_get_content_type():
    """
    >>> assert get_content_type('file.txt') == 'text/plain'
    >>> assert get_content_type('file.html') == 'text/html'
    >>> assert get_content_type('file.pdf') == 'application/pdf'
    >>> assert get_content_type('file.png') == 'image/png'
    >>> assert get_content_type('file.jpg') == 'image/jpeg'
    >>> assert get_content_type('file.jpeg') == 'image/jpeg'
    >>> assert get_content_type('file.gif') == 'image/gif'
    >>> assert get_content_type('file.foo') is None

    """
    pass

# Generated at 2022-06-13 22:47:20.050377
# Unit test for function get_content_type
def test_get_content_type():
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(delete=False, suffix='.txt') as f:
        f.close()
        assert get_content_type(f.name) == 'text/plain'

    with NamedTemporaryFile(delete=False, suffix='.txt') as f:
        f.close()
        assert get_content_type(f.name + '.txt') == 'text/plain'

    with NamedTemporaryFile(delete=False, suffix='.html') as f:
        f.close()
        assert get_content_type(f.name) == 'text/html'

# Generated at 2022-06-13 22:47:28.225286
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.tar.gz') == 'application/x-tar'
    assert get_content_type('foo.zip') == 'application/zip'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.js') == 'application/javascript'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.css') == 'text/css'
    assert get_content_type('foo.json') == 'application/json'

# Generated at 2022-06-13 22:47:35.255213
# Unit test for function get_content_type
def test_get_content_type():
    import pytest
    filenames = [
        'hello.txt',
        'hello.TXT',
        'hello.Txt'
    ]
    for filename in filenames:
        content_type = get_content_type(filename)
        assert content_type == 'text/plain', content_type

    filenames = [
        'Hello.yaml',
        'hello.yaml',
        'Hello.yaml',
        'Hello.YAML',
        'Hello.Yaml',
        'Hello.YAML'
    ]

    for filename in filenames:
        content_type = get_content_type(filename)
        assert content_type == 'application/x-yaml', content_type


# Generated at 2022-06-13 22:47:36.806904
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('whatever.csv') == 'text/csv'

# Generated at 2022-06-13 22:47:49.180529
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    import json
    from collections import OrderedDict
    from pprint import pformat

    def test_load_json_preserve_order():
        s = '{"a": 6, "b": "foo", "c": true, "d": null}'
        d = {'b': 'foo', 'a': 6, 'c': True, 'd': None}
        assert load_json_preserve_order(s) == d
        assert repr_dict(d) == json.dumps(d, indent=4)

    test_load_json_preserve_order()

# Generated at 2022-06-13 22:47:54.094997
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'a': 'b'}) == "{'a': 'b'}"
    assert repr_dict(dict(a='b')) == "{'a': 'b'}"



# Generated at 2022-06-13 22:47:59.201719
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    a = '{"a": 1, "b": 2, "c": "three"}'
    assert load_json_preserve_order(a) == {
        'a': 1,
        'b': 2,
        'c': 'three'
    }

# Generated at 2022-06-13 22:48:09.062485
# Unit test for function humanize_bytes
def test_humanize_bytes():
    for num, expected in [
        (1, '1 B'),
        (1024, '1.0 kB'),
        (1024 * 123, '123.0 kB'),
        (1024 * 12342, '12.1 MB'),
        (1024 * 12342, '12.05 MB'),
        (1024 * 1234, '1.21 MB'),
        (1024 * 1234 * 1111, '1.31 GB'),
        (1024 * 1234 * 1111, '1.3 GB'),
    ]:
        answer = humanize_bytes(num)
        assert answer == expected, f'num: {num}, answer: {answer}'


if __name__ == '__main__':
    import sys
    import doctest
    status = 0

# Generated at 2022-06-13 22:48:15.410597
# Unit test for function get_content_type
def test_get_content_type():
    # Test a known file type.
    filename = 'test_get_content_type.py'
    ct = get_content_type(filename)
    assert ct == 'text/x-python'

    # Test an unknown file type.
    filename = 'test_get_content_type.unknown'
    ct = get_content_type(filename)
    assert ct == None

# Generated at 2022-06-13 22:48:22.535679
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    def is_expired(expires: Optional[float]) -> bool:
        return expires is not None and expires <= now

    now = time.time()

# Generated at 2022-06-13 22:48:28.173039
# Unit test for function repr_dict
def test_repr_dict():
    d = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'subkey1': 'subvalue1',
            'subkey2': 'subvalue2',
        },
        'key4': {
            'subkey1': [
                'subvalue1',
                'subvalue2',
            ],
        },
    }
    r = repr_dict(d)

# Generated at 2022-06-13 22:48:40.071469
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'c2=v2; Max-Age=2; Path=/'),
        ('Set-Cookie', 'c3=v3; Max-Age=3; Path=/'),
        ('Set-Cookie', 'c4=v4; Max-Age=4; Path=/'),
        ('Set-Cookie', 'c1=v1; Expires=Wed, 01 Jan 2020 00:00:00 GMT; Path=/'),
    ]
    now = time.mktime(time.strptime('2019-12-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

    expired_cookies = get_expired_cookies(headers=headers, now=now)

# Generated at 2022-06-13 22:48:47.968408
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    """Test the core functionality of get_expired_cookies."""
    # Examples taken from HttpWatch
    # <https://kb.httpwatch.com/help/httpwatch8/Public/CookieAttributes.htm>
    assert get_expired_cookies([
        ('Set-Cookie', 'Name="Value"; Path="/"'),
    ]) == []

    assert get_expired_cookies([
        ('Set-Cookie', 'Name=Value; Path=/'),
    ]) == []

    assert get_expired_cookies([
        ('Set-Cookie', 'Name="Value"; Path="/"'),
        ('Set-Cookie', 'Name=Value; Path=/'),
        ('Set-Cookie', 'Name=Value; Path=/'),
        ('Set-Cookie', 'Name=Value; Path=/'),
    ]) == []



# Generated at 2022-06-13 22:48:51.316205
# Unit test for function repr_dict
def test_repr_dict():
    d = {'a': 1, 'b': 'two', 'c': [1, 2]}
    assert repr_dict(d) == pformat(d, width=1)

# Generated at 2022-06-13 22:48:56.393918
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    ExplicitNullAuth()

# Generated at 2022-06-13 22:49:05.469026
# Unit test for function repr_dict
def test_repr_dict():
    d = {
        'foo': 'bar',
        'baz': ['quux', 'quuz'],
        'corge': {'grault': 'garply', 'waldo': 'fred'},
        'qux': True,
        'quzz': None,
        'corge2': {'grault2': []},
    }
    assert repr_dict(d) == """\
{'baz': ['quux', 'quuz'],
 'corge': {'grault': 'garply', 'waldo': 'fred'},
 'corge2': {'grault2': []},
 'foo': 'bar',
 'qux': True,
 'quzz': None}"""

# Generated at 2022-06-13 22:49:08.062891
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()



# Generated at 2022-06-13 22:49:16.696087
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

# Generated at 2022-06-13 22:49:21.439272
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    """
    The class "ExplicitNullAuth" should not have a constructor.
    """
    try:
        ExplicitNullAuth()
    except TypeError:
        pass
    else:
        raise Exception('ExplicitNullAuth should not have a constructor')

# Generated at 2022-06-13 22:49:24.643282
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    """Unit test for method __call__ of class ExplicitNullAuth."""
    cookie_jar = ExplicitNullAuth()
    assert cookie_jar.__call__("request") == "request"

# Generated at 2022-06-13 22:49:25.228489
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:49:30.295574
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = '{"a": "a", "b": "b", "c": "c"}'
    expected = OrderedDict([('a', 'a'), ('b', 'b'), ('c', 'c')])
    assert load_json_preserve_order(s) == expected



# Generated at 2022-06-13 22:49:37.679070
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('README.md') == 'text/markdown'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.zip') == 'application/zip'
    assert get_content_type('foo.pdf') == 'application/pdf'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.other') == None

if __name__ == '__main__':
    test_get_content_type()

# Generated at 2022-06-13 22:49:47.118115
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    expires_header = 'expires=%s' % time.strftime('%a, %d-%b-%Y %H:%M:%S GMT', time.gmtime(now + 60))