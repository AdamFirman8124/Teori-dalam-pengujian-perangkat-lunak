

# Generated at 2022-06-13 22:44:01.475294
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookie_data = [
        'foo=bar; expires=Mon, 30-Mar-2038 00:00:00 GMT; path=/; HttpOnly',
        'bar=foo; max-age=86400; path=/; secure; HttpOnly',
        'bar2=foo2; domain=example.com; '
        'expires=Tue, 30-Apr-2019 00:00:00 GMT; path=/; HttpOnly',
        'bar3=foo3; domain=example.com; path=/; HttpOnly',
    ]
    cookies = get_expired_cookies([
        ('Set-Cookie', cookie) for cookie in cookie_data
    ], now=time.time())
    assert len(cookies) == 1
    assert cookies[0]['name'] == 'bar3'



# Generated at 2022-06-13 22:44:13.698723
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('set-cookie', 'foo=bar; domain=example.com; path=/; secure; HttpOnly'),
        ('set-cookie', 'foo=baz; Max-Age=86400; Path=/; Expires=Wed, 01 Jan 2020 00:00:00 GMT; Secure'),
        ('set-cookie', 'foo=qux; max-age=3600; Path=/; Expires=Wed, 01 Jan 2020 00:00:00 GMT; Secure'),
    ]
    now = time.time()
    assert get_expired_cookies(headers, now=now) == []
    assert get_expired_cookies(headers, now=now + 86400) == [
        {
            'name': 'foo',
            'path': '/'
        }
    ]

# Generated at 2022-06-13 22:44:23.158049
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.svg') == 'image/svg+xml'
    assert get_content_type('foo.SVG') == 'image/svg+xml'
    assert get_content_type('foo.svg') == 'image/svg+xml'
    assert get_content_type('foo.htm') == 'text/html'
    assert get_content_type('foo.js') == 'application/javascript'
    assert get_content_type('foo.mp3') == 'audio/mpeg'
    assert get_content_type('foo.mp4') == 'video/mp4'
    assert get_content_type('foo.ogg') == 'audio/ogg'
    assert get_content_type('foo.ogv')

# Generated at 2022-06-13 22:44:32.188672
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import requests

    expired = get_expired_cookies(
        headers=[
            ('Set-Cookie', 'a_session=a'),
            ('Set-Cookie', 'b_session=b; Expires=Wed, 21 Oct 2015 07:28:00 GMT'),
            ('Set-Cookie', 'c_token=c; Max-Age=0')
        ],
        now=time.time()
    )

    assert expired == [
        {'name': 'b_session', 'path': '/'},
        {'name': 'c_token', 'path': '/'},
    ]

    # Demonstrate that the expired cookie can now be set
    r = requests.get('http://localhost:5000/', cookies={'a_session': 'a'})
    assert r.status_code == 200

# Generated at 2022-06-13 22:44:43.799327
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    # expired cookie
    expired = now - 1
    # non-expired non-persistent cookie
    non_expired = now + 1000
    # non-expired persistent cookie
    persistent = now + 100
    # cookies

# Generated at 2022-06-13 22:44:53.777454
# Unit test for function get_content_type
def test_get_content_type():
    mime, enc = mimetypes.guess_type('foo.txt')
    assert get_content_type('foo.txt') == '%s; charset=%s' % (mime, enc)

    mime, enc = mimetypes.guess_type('foo.txt.gz')
    assert get_content_type('foo.txt.gz') == '%s; charset=%s' % (mime, enc)

    mime, enc = mimetypes.guess_type('foo.txt.bz2')
    assert get_content_type('foo.txt.bz2') == '%s; charset=%s' % (mime, enc)

    assert get_content_type('foo.txtx') is None
    assert get_content_type('foo.txt.zst') is None

# Generated at 2022-06-13 22:44:55.288086
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('file.csv') == 'text/csv'

# Generated at 2022-06-13 22:44:57.683447
# Unit test for function get_content_type
def test_get_content_type():
    content_type = get_content_type('some_file.html')
    assert content_type == 'text/html'

# Generated at 2022-06-13 22:45:07.915862
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    expired_cookie_1 = {'name': 'foo', 'path': '/'}
    expired_cookie_2 = {'name': 'bar', 'path': '/'}
    valid_cookie = {'name': 'baz', 'path': '/'}
    now = time.time()
    header_attrs = [
        ('Set-Cookie', 'foo=1; path=/; expires="%s"; Secure' % now),
        ('Set-Cookie', 'bar=2; path=/; max-age="%s"' % now),
        ('Set-Cookie', 'baz=3; path=/; max-age="%s"' % (2 * now))
    ]

# Generated at 2022-06-13 22:45:09.352249
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.html') == 'text/html'



# Generated at 2022-06-13 22:45:23.065462
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = 1.0
    headers = [
        ('Set-Cookie', 'a=1; Max-Age=1; Expires=2'),
        ('Set-Cookie', 'b=2; Max-Age=1; Expires=0.1'),
        ('Set-Cookie', 'c=3'),
        ('Set-Cookie', 'd=4; Max-Age=a'),
        ('Set-Cookie', 'e=5; Max-Age=-1; Expires=1.1'),
    ]

    assert get_expired_cookies(
        headers=headers,
        now=now
    ) == [
        {'path': '/', 'name': 'b'},
        {'path': '/', 'name': 'd'},
        {'path': '/', 'name': 'e'},
    ]




# Generated at 2022-06-13 22:45:36.261266
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookies = [
        'foo=bar; Path=/; Expires=Wed, 28 Aug 2019 16:25:19 GMT',
        'bar=baz; Path=/; Expires=Wed, 28 Aug 2019 16:25:19 GMT',
        'baz=qux; Path=/; Expires=Wed, 28 Aug 2019 16:25:19 GMT',
        (
            'qux=quux; Path=/; Expires=Wed, 28 Aug 2019 16:25:19 GMT'
            '; HttpOnly; Secure'
        ),
    ]
    headers = [('Set-Cookie', cookie) for cookie in cookies]
    expired = get_expired_cookies(headers=headers, now=1566866000)

# Generated at 2022-06-13 22:45:45.841520
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import datetime
    now = time.mktime(datetime.datetime.now().timetuple())


# Generated at 2022-06-13 22:45:52.075810
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('set-cookie', ('foo=bar; path=/; expires='
                        'Tue, 23 Oct 2018 05:36:12 GMT')),
        ('set-cookie', ('foo2=bar2; path=/')),
        ('set-cookie', ('foo3=bar3; path=/; max-age=3600'))
    ]
    now = 1540265773
    cookies = get_expired_cookies(headers, now=now)
    assert len(cookies) == 1
    assert cookies[0] == {'name': 'foo2', 'path': '/'}

# Generated at 2022-06-13 22:45:53.019411
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    pass

# Generated at 2022-06-13 22:46:05.358936
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # Set cookie that is expired
    now = 1000
    headers = [
        ('weird', 'header'),
        ('Set-Cookie', 'foo=bar'),
        ('Set-Cookie', 'baz=quux; Max-Age=10; Path=/'),
        ('Set-Cookie', 'baz=quux; Expires=Sat, 06 Dec 2014 06:06:06 GMT; Path=/'),
        ('Set-Cookie', 'baz=quux; Max-Age=0; Path=/'),
        # Two expired cookies, one expired, one valid
        ('Set-Cookie', 'quux=xyz; Max-Age=1; Path=/; Expires=Sat, 06 Dec 2014 06:06:00 GMT'),
    ]
    expired_cookies = get_expired_cookies(headers=headers, now=now)
   

# Generated at 2022-06-13 22:46:17.080221
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:46:26.880624
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import time
    import random
    import pytest

# Generated at 2022-06-13 22:46:35.763509
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import datetime
    import time

    now = time.time()
    present = now + 60
    future = now + 600

    def to_ns_cookie_string(cookie):
        return '; '.join(f"{k}={v}" for k, v in cookie.items())

    def to_headers(cookies):
        lines = (to_ns_cookie_string(cookie) for cookie in cookies)
        return '\n'.join(f"Set-Cookie: {line}" for line in lines)

    session = requests.session()


# Generated at 2022-06-13 22:46:46.120572
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import pytest
    import datetime
    past_timestamp = datetime.datetime(1970, 1, 1).strftime("%a, %d %b %Y %H:%M:%S %Z")
    future_timestamp = datetime.datetime(2038, 1, 1).strftime("%a, %d %b %Y %H:%M:%S %Z")
    now_config = 3600
    # Basic test
    headers = [
        ('Set-Cookie', 'foo=; expires=' + past_timestamp + '; path=/'),
        ('Set-Cookie', 'bar=; max-age=0; path=/'),
    ]
    expected = [{'name': 'foo', 'path': '/'}, {'name': 'bar', 'path': '/'}]
    assert get_ex