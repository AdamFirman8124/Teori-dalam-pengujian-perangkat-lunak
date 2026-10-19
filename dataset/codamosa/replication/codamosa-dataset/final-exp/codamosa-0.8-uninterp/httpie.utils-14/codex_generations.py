

# Generated at 2022-06-13 22:43:56.447666
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.html.bak') == 'text/html'
    assert get_content_type('foo.HTML') == 'text/html'
    assert get_content_type('foo.HTM') is None
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.bar') is None
    assert get_content_type('foo.baz.jpg') == 'image/jpeg'
    assert get_content_type('foo') is None



# Generated at 2022-06-13 22:44:06.290709
# Unit test for function get_expired_cookies
def test_get_expired_cookies():

    # Two cookies with Max-Age and Expires headers
    headers = [
        ('Set-Cookie', 'foo=bar; Max-Age=600'),
        ('Set-Cookie', 'biz=baz; Expires=Wed, 16 Dec 2015 17:37:13 GMT'),
    ]

    # Get all expired cookies
    expired_cookies = get_expired_cookies(headers, time.time() + 5000)

    # Check if the list has a cookie with name foo and path /
    # Check if the list has a cookie with name biz and path /
    assert not any(
        cookie['name'] == 'foo' and cookie['path'] == '/'
        for cookie in expired_cookies
    )

# Generated at 2022-06-13 22:44:08.138381
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.pdf') == 'application/pdf'

# Generated at 2022-06-13 22:44:18.830061
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'name=value; Path=/; httponly; Secure; Expires=Sat, '
                       '18 May 2019 00:00:00 GMT'),
        ('Set-Cookie', 'name=value; Path=/; httponly; Secure; Expires=Thu, '
                       '18 May 2017 00:00:00 GMT'),
        ('Set-Cookie', 'name=value; Path=/; httponly; Secure; Max-Age=86400'),
    ]

    cookies = get_expired_cookies(headers, time.time())
    assert len(cookies) == 2
    assert cookies[0]['name'] == 'name'
    assert cookies[1]['name'] == 'name'
    assert cookies[0]['path'] == '/'
    assert cookies[1]['path'] == '/'
   

# Generated at 2022-06-13 22:44:21.420828
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo') is None
    assert get_content_type(__file__) == 'text/x-python; charset=us-ascii'

# Generated at 2022-06-13 22:44:29.946857
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('example.png') == 'image/png'
    assert get_content_type('example.txt.gz') == 'application/x-gzip'
    assert get_content_type('example.txt') == 'text/plain'
    assert get_content_type('foo/example.txt') == 'text/plain'
    assert get_content_type('foo/bar/example.txt') is None
    assert get_content_type('example.png.txt') == 'text/plain'
    assert get_content_type('example.png.exe') == 'application/octet-stream'
    assert get_content_type('example.notatype') is None

# Generated at 2022-06-13 22:44:37.124518
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import json
    import pytest
    fixture_path = 'tests/fixtures/requests/expired-cookies.json'
    with open(fixture_path) as f:
        fixture = json.load(f)

    expected = get_expired_cookies(headers=fixture['headers'], now=fixture['now'])
    actual = fixture['expected']['expired_cookies']

    assert actual == expected

# Generated at 2022-06-13 22:44:41.968814
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.css') == 'text/css'
    assert get_content_type('foo.js') == 'application/javascript'
    assert get_content_type('foo.pdf') == 'application/pdf'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.jpeg') == 'image/jpeg'
    assert get_content_type('foo.gif') == 'image/gif'
    assert get_content_type('foo.svg') == 'image/svg+xml'

# Generated at 2022-06-13 22:44:47.042674
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foobar.html') == 'text/html'
    assert get_content_type('foobar.png') == 'image/png'
    assert get_content_type('foobar') is None

# Generated at 2022-06-13 22:44:49.790757
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('index.css') == 'text/css'
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.bin') is None

# Generated at 2022-06-13 22:45:03.631670
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([('Set-Cookie', 'foo=bar')]) == [
        {'name': 'foo', 'path': '/'}
    ]
    exp = 'Thu, 01 Jan 1970 00:00:01 GMT'
    assert get_expired_cookies([('Set-Cookie', f"foo=bar; Expires={exp}")]) == [
        {'name': 'foo', 'path': '/'}
    ]
    exp = 'Thu, 01 May 2029 00:00:01 GMT'
    assert get_expired_cookies([('Set-Cookie', f"foo=bar; Expires={exp}")]) == []

# Generated at 2022-06-13 22:45:12.992646
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    headers = (
        'Set-Cookie: foo=bar; expires=Fri, 30-Aug-2019 23:10:06 GMT;',
        'Set-Cookie: baz=qux; expires=Fri, 30-Aug-2019 23:10:06 GMT;',
        'Set-Cookie: lorem=ipsum; Max-Age=900;',
        'Set-Cookie: dolor=sit; Max-Age=1800;',
        'Set-Cookie: amet=consectetur; Max-Age=2700;',
    )
    expired = get_expired_cookies(
        [header.split(': ', 1) for header in headers],
        now=now
    )

# Generated at 2022-06-13 22:45:23.403867
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # Test something I found in `tidypy` source code.
    now = time.time()
    cookies = [
        {
            'name': 'foo',
            'value': 'bar',
            'expires': now - 1,
            'secure': True
        }, {
            'name': 'baz',
            'value': 'qux',
            'max-age': 5,
            'secure': True
        }
    ]

    # Translate max-age to expires.
    _max_age_to_expires(cookies=cookies, now=now)

    # Format cookies like they would be in Set-Cookie header.
    set_cookie_headers = [
        '='.join(pair) for cookie in cookies
        for pair in cookie.items()
    ]

    expired_cookies = get_

# Generated at 2022-06-13 22:45:34.132873
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    past = time.time() - 1.0
    future = time.time() + 1.0
    headers = [
        ('Content-Type', 'text/html;charset=utf-8'),
        ('Set-Cookie', 'X="d"; path=/; expires=0'),
        ('Set-Cookie', 'Y="a"; path=/'),
        ('Set-Cookie', 'Z="b"; path=/; expires={0}'.format(future)),
        ('Set-Cookie', 'W="c"; path=/; expires={0}'.format(past)),
    ]
    assert get_expired_cookies(headers=headers) == [
        {'name': 'W', 'path': '/'},
    ]

# Generated at 2022-06-13 22:45:44.528384
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import pprint
    from datetime import datetime, timedelta

    now = datetime.utcnow().timestamp()

    # Expire an hour from now, and pretend it was two hours old
    cookie = {
        'name': 'test-cookie',
        'max-age': str(timedelta(hours=1).total_seconds()),
        'path': '/'
    }

    # No `expires` attribute.
    headers = [('Set-Cookie', cookie)]
    expired_cookies = get_expired_cookies(headers, now=now - 7200)
    assert expired_cookies == [cookie]

    # With `expires` attribute.
    expires = now + cookie['max-age']

# Generated at 2022-06-13 22:45:55.905373
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([]) == []
    assert get_expired_cookies([('Set-Cookie', 'name=value')]) == []

    now = time.time()
    assert get_expired_cookies(
        [('Set-Cookie', 'name=value; Max-Age=0')], now=now
    ) == [{'path': '/', 'name': 'name'}]

    assert get_expired_cookies(
        [('Set-Cookie', 'name=value; Max-Age=1')], now=now
    ) == []

    assert get_expired_cookies(
        [('Set-Cookie', 'name=value; Max-Age=1')], now=now + 0.9
    ) == []


# Generated at 2022-06-13 22:46:07.018605
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime, timedelta
    import dateutil.parser
    import dateutil.tz

    now = datetime.now(dateutil.tz.utc)


# Generated at 2022-06-13 22:46:19.185546
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:46:30.470173
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'sessionid=abc; expires=Thu, 21-Dec-2017 22:35:31 GMT'),
        ('Set-Cookie', 'sessionid2=abc; expires=Fri, 21-Dec-2027 22:35:31 GMT'),
        ('Set-Cookie', 'sessionid3=abc; max-age=3600;'),
        ('Set-Cookie', 'sessionid4=abc; max-age=3600; Secure; HttpOnly; SameSite=Strict'),
        ('Set-Cookie', 'sessionid5=abc; max-age=-100; Secure; HttpOnly; SameSite=Strict'),
    ]
    expired_cookies = get_expired_cookies([(name, value) for name, value in headers])

# Generated at 2022-06-13 22:46:41.730912
# Unit test for function get_expired_cookies