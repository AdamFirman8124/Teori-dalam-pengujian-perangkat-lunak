

# Generated at 2022-06-13 22:44:01.884313
# Unit test for function get_content_type
def test_get_content_type():
    # Test all valid content types
    assert(get_content_type('hello.txt') == 'text/plain')
    assert(get_content_type('hello.bin') == 'application/octet-stream')
    assert(get_content_type('hello.css') == 'text/css')
    assert(get_content_type('hello.c') == 'text/plain')
    assert(get_content_type('hello.cpp') == 'text/plain')
    assert(get_content_type('hello.py') == 'text/x-python-script')
    assert(get_content_type('hello.pyc') == 'application/x-python-code')
    assert(get_content_type('hello.pyo') == 'application/x-python-code')

# Generated at 2022-06-13 22:44:03.387116
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type(filename="test_filename") is None



# Generated at 2022-06-13 22:44:06.579418
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.html') == 'text/html'
    assert get_content_type('test.json') == 'application/json'

# Generated at 2022-06-13 22:44:08.407089
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('text.txt') == 'text/plain'

# Generated at 2022-06-13 22:44:18.955428
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from unittest.mock import Mock
    session = Mock()
    response = Mock()
    response.headers = {
        'Set-Cookie': 'foo=bar; Path=/; Domain=.example.test; '
        'Expires=Fri, 31 Dec 9999 23:59:59 GMT'
    },
    response.request.url = 'http://example.test/foo'
    session.send.return_value = response
    expired_cookies = get_expired_cookies(response.headers)
    assert expired_cookies == []
    expired_cookies = get_expired_cookies(response.headers,
                                    now=time.mktime(time.gmtime())+3600)
    assert expired_cookies == [{'name': 'foo', 'path': '/'}]

# Generated at 2022-06-13 22:44:29.266091
# Unit test for function get_content_type
def test_get_content_type():
    import os
    import mimetypes
    import tests.common as common

    TEST_FILES_DIR = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'test_files'
    )
    for filename in common.TEST_FILES:
        filepath = os.path.join(TEST_FILES_DIR, filename)
        mime, encoding = mimetypes.guess_type(filepath, strict=False)
        if mime:
            ct = get_content_type(filepath)
            assert ct == mime
            if encoding:
                ct_enc_exp = '{0}; charset={1}'.format(mime, encoding)
                assert ct == ct_enc_exp
        else:
            assert get_content

# Generated at 2022-06-13 22:44:36.171597
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.json') == 'application/json'
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.txt.gz') == 'application/gzip'
    assert get_content_type('foo.gz') == 'application/gzip'

# Generated at 2022-06-13 22:44:46.231496
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:44:49.445871
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('README.md') == 'text/x-markdown; charset=us-ascii'
    assert get_content_type('LICENSE') == 'text/plain; charset=us-ascii'

# Generated at 2022-06-13 22:45:01.458791
# Unit test for function get_content_type
def test_get_content_type():
    # https://tools.ietf.org/html/rfc2616#section-7.2.1
    # Note that the correct MIME type for HTML is "text/html",
    # not "text/html; charset=ISO-8859-4".
    assert get_content_type('index.html') == 'text/html'

    # https://tools.ietf.org/html/rfc2616#section-2.2
    # It is expected that the user's mail user agent will recognize
    # this as an invitation to send mail to "mary@host.domain".
    assert get_content_type('address.mailto') == 'message/external-body'

    # https://tools.ietf.org/html/rfc6648
    # Perhaps it is a PDF/UA-conformant file
    assert get_content

# Generated at 2022-06-13 22:45:12.164989
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    future = now + 5
    headers = [
        ('Set-Cookie', 'a=b; Path=/; Expires=%s' % time.strftime(
            '%a, %d-%b-%Y %H:%M:%S GMT', time.gmtime(future))),
        ('Set-Cookie', 'c=d; Path=/; Max-Age=5'),
        ('Set-Cookie', 'e=f; Path=/; Expires=%s' % time.strftime(
            '%a, %d-%b-%Y %H:%M:%S GMT', time.gmtime(now)))
    ]
    expired_cookies = get_expired_cookies(headers)
    assert len(expired_cookies) == 1
    assert expired_cook

# Generated at 2022-06-13 22:45:19.739312
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'foo=bar; Path=/'),
        ('Set-Cookie', 'qux=quux; Secure; HttpOnly; Path=/baz;'),
        ('Set-Cookie', 'frob=nitz; Expires=Mon, 21 Jul 1997 09:21:18 GMT;'),
    ]
    assert get_expired_cookies(headers) == [{'name': 'frob', 'path': '/'}]

# Generated at 2022-06-13 22:45:32.690069
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:41.267113
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from pathlib import Path
    with Path('sample_cookies.txt').open() as f:
        cookies = get_expired_cookies(
            [tuple(line.strip().split(': ', 1)) for line in f],
            now=time.time()
        )
        assert cookies == [
            {'name': 'baz', 'path': '/'},
            {'name': 'foo', 'path': '/'},
        ]


if __name__ == '__main__':
    test_get_expired_cookies()

# Generated at 2022-06-13 22:45:47.979760
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookie_str = 'JSESSIONID=C2065EBB17D6C0FE7D4023B1644D9F92; Path=/api/; HttpOnly; Secure'
    cookies = get_expired_cookies([
        ('Set-Cookie', cookie_str)
    ])
    assert cookies == [
        {
            'name': 'JSESSIONID',
            'path': '/api/'
        }
    ]

# Generated at 2022-06-13 22:45:58.659311
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:46:08.381239
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    def has_expired(headers: List[Tuple[str, str]], now: float = None) -> bool:
        return bool(get_expired_cookies(headers))

    # Not expired
    assert not has_expired([
        ('Set-Cookie', 'foo=bar'),
    ])
    assert not has_expired([
        ('Set-Cookie', 'foo=bar; Path=/'),
    ])
    assert not has_expired([
        ('Set-Cookie', 'foo=bar; Path=/; Max-Age=5'),
    ])
    assert not has_expired([
        ('Set-Cookie', 'foo=bar; Path=/; Expires=Sat, 12 May 2018 07:29:19 GMT'),
    ])

    # Expired (expiry in past)

# Generated at 2022-06-13 22:46:20.733611
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # Test successful parsing of simple cookie.
    assert get_expired_cookies([
        ('set-cookie', 'SESSION_ID="PsAjNg5IOW8="; Path=/')
    ]) == [{'name': 'SESSION_ID', 'path': '/'}]

    # Test successful parsing of cookie with `expires` and `path`.
    assert get_expired_cookies([
        ('set-cookie',
         'SESSION_ID="PsAjNg5IOW8="; expires=Tue, 15 Jan 2019 21:47:38 '
         'GMT; path=/')
    ]) == [{'name': 'SESSION_ID', 'path': '/'}]

    # Test successful parsing of cookie with `max-age` and `path`.

# Generated at 2022-06-13 22:46:31.159478
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import datetime

    # pylint: disable=invalid-name,line-too-long
    COOKIE_ATTRS = [
        # Value
        'foo=bar',
        # Name
        'name=foo',
        # Path
        'path=/',
        # Domain
        'domain=.github.com',
        # Max-age
        'max-age=0',
        # Expires
        'expires={expires}',
        # Secure
        'secure',
        # Http-only
        'HttpOnly',
        # Extension
        '__Host-session_something=something',
    ]
    # pylint: enable=invalid-name,line-too-long

# Generated at 2022-06-13 22:46:40.994612
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from pprint import pprint
    cookie_headers = [
        ('set-cookie', 'euconsent=foo; Max-Age=10'),
        ('Set-Cookie', 'foo=bar; Path=/cookie_path')
    ]
    assert get_expired_cookies(cookie_headers, now=100001) == [
        {'name': 'euconsent', 'path': '/'},
    ]
    assert get_expired_cookies(cookie_headers, now=100005) == [
        {'name': 'euconsent', 'path': '/'},
        {'name': 'foo', 'path': '/cookie_path'}
    ]

# Generated at 2022-06-13 22:46:47.219164
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('file.pdf') == 'application/pdf'
    assert get_content_type('file.txt') == 'text/plain'
    assert get_content_type('file.html') == 'text/html'
    assert get_content_type('file.json') == 'application/json'
    assert get_content_type('file.unknown') is None

# Generated at 2022-06-13 22:46:50.266688
# Unit test for function repr_dict
def test_repr_dict():
    a = {'aaa': 1, 'bbb': 2, 'ccc': 3}
    b = '{\'aaa\': 1, \'bbb\': 2, \'ccc\': 3}'
    assert repr_dict(a) == b

# Generated at 2022-06-13 22:46:58.089127
# Unit test for function humanize_bytes

# Generated at 2022-06-13 22:47:02.673784
# Unit test for function get_content_type
def test_get_content_type():
    filename = 'some_file.txt'
    mime, encoding = 'text/plain', 'UTF-8'
    content_type = '{mime}; charset={encoding}'.format(
        mime=mime, encoding=encoding
    )
    mimetypes.types_map['.txt'] = mime

    assert get_content_type(filename) == content_type



# Generated at 2022-06-13 22:47:13.244627
# Unit test for function humanize_bytes
def test_humanize_bytes():
    assert humanize_bytes(1) == '1 B'
    assert humanize_bytes(1024, 1) == '1.0 kB'
    assert humanize_bytes(1024 * 123, 1) == '123.0 kB'
    assert humanize_bytes(1024 * 12342, 1) == '12.1 MB'
    assert humanize_bytes(1024 * 12342, 2) == '12.05 MB'
    assert humanize_bytes(1024 * 1234, 2) == '1.21 MB'
    assert humanize_bytes(1024 * 1234 * 1111, 2) == '1.31 GB'
    assert humanize_bytes(1024 * 1234 * 1111, 1) == '1.3 GB'

# Generated at 2022-06-13 22:47:18.347023
# Unit test for function get_content_type
def test_get_content_type():
    assert(get_content_type('a.html') == 'text/html')
    assert(get_content_type('b.pdf') == 'application/pdf')
    assert(get_content_type('c.txt') == 'text/plain')
    assert(get_content_type('d.png') == 'image/png')
    assert(get_content_type('e') is None)



# Generated at 2022-06-13 22:47:28.830543
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:47:35.317503
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('data.csv') == 'text/plain; charset=utf-8'
    assert get_content_type('data.txt') == 'text/plain; charset=utf-8'
    assert get_content_type('foo.txt') == 'text/plain; charset=utf-8'

# Generated at 2022-06-13 22:47:36.047684
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:47:36.965280
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    auth = ExplicitNullAuth()
    assert auth is not None