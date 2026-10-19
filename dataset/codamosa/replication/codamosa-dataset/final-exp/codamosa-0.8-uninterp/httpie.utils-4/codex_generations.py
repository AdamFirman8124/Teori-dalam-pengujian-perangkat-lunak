

# Generated at 2022-06-13 22:43:54.619433
# Unit test for function get_content_type
def test_get_content_type():
    from click.testing import CliRunner

    runner = CliRunner()
    result = runner.invoke(get_content_type, ['../tests'])
    assert result.exit_code == 0
    assert result.output == 'text/x-python; charset=us-ascii\n'

# Generated at 2022-06-13 22:43:57.253969
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('a.txt') == 'text/plain'
    assert get_content_type('a.HTML') == 'text/html'

# Generated at 2022-06-13 22:44:06.734082
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    def assert_cookie_name_path(actual, expected):
        assert actual['name'] == expected['name']
        assert actual['path'] == expected['path']

    now = time.time()

# Generated at 2022-06-13 22:44:09.659005
# Unit test for function get_content_type
def test_get_content_type():
    filename = 'testfile.json'
    assert get_content_type(filename) == 'application/json'



# Generated at 2022-06-13 22:44:15.822008
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies(
        headers=[
            ('Set-Cookie', 'foo=bar; expires=Tue, 15-Feb-2021 20:02:29 GMT'),
            ('Set-Cookie', 'baz=42; max-age=60'),
            ('Set-Cookie', 'quux=.25; expires=Tue, 15-Feb-2021 20:02:31 GMT'),
        ],
        now=1613588549.665739,  # Tue, 15-Feb-2021 20:02:29 GMT
    ) == [
        {'name': 'foo', 'path': '/'},
        {'name': 'baz', 'path': '/'},
    ]

# Generated at 2022-06-13 22:44:27.904547
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [('Set-Cookie', 'bar=foo')]
    now = 0
    expired_cookies = get_expired_cookies(headers, now=now)
    assert expired_cookies == [{'name': 'bar', 'path': '/'}]

    headers = [('Set-Cookie', 'bar=foo; max-age=0')]
    now = 0
    expired_cookies = get_expired_cookies(headers, now=now)
    assert expired_cookies == [{'name': 'bar', 'path': '/'}]

    headers = [('Set-Cookie', 'bar=foo; Max-Age=0')]
    now = 0
    expired_cookies = get_expired_cookies(headers, now=now)

# Generated at 2022-06-13 22:44:38.085423
# Unit test for function get_content_type
def test_get_content_type():
    cases = [
        ('test.txt', 'text/plain'),
        ('test.jpeg', 'image/jpeg'),
        ('test', 'application/octet-stream'),
        ('test.txt.gz', 'application/x-gzip'),
        ('test.random', None),
    ]
    for filename, expected_content_type in cases:
        content_type = get_content_type(filename)
        assert content_type == expected_content_type, (
            'For filename {} expected content-type {}, got {}.'.format(
                filename, expected_content_type, content_type,
            )
        )

# Generated at 2022-06-13 22:44:47.989998
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()

    def cook(
        name: str,
        expires: str=None,
        max_age: str=None,
        path: str='/',
    ) -> dict:
        return {
            'name': name,
            'expires': time.strptime(expires, '%a, %d-%b-%Y %H:%M:%S %Z') \
                if expires is not None else None,
            'max-age': max_age,
            'path': path,
        }


# Generated at 2022-06-13 22:45:00.610509
# Unit test for function get_content_type
def test_get_content_type():
    """Tests the function `get_content_type()`."""
    assert get_content_type('test_file.csv') == 'text/csv'
    assert get_content_type('test_file.csv.gz') == 'application/gzip'
    assert get_content_type('test_file.txt') == 'text/plain'
    assert get_content_type('test_file.txt.gz') == 'application/gzip'
    assert get_content_type('test_file.xls') == 'application/vnd.ms-excel'
    assert get_content_type('test_file.xls.gz') == 'application/gzip'
    assert get_content_type('test_file.xml') == 'application/xml'

# Generated at 2022-06-13 22:45:10.099237
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    def assert_expired(
        now: float,
        cookie_headers: List[Tuple[str, str]],
        expected: List[dict]
    ) -> None:
        """
        Assert that `now`, `cookie_headers`, and `expected`, are equivalent.

        """
        assert get_expired_cookies(cookie_headers, now=now) == expected


# Generated at 2022-06-13 22:45:21.038437
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    import json
    class a:
        def __init__(self):
            self.c = []
            self.c.append('d')
            self.c.append('e')
            self.b = []
            self.b.append('d')
            self.b.append('e')
        def as_dict(self):
            return {'b':self.b, 'c':self.c}
    json_str = json.dumps(a().as_dict())
    dictionary = load_json_preserve_order(json_str)
    assert dictionary['b'] == ['d','e']
    assert dictionary['c'] == ['d','e']

# Generated at 2022-06-13 22:45:33.969977
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from requests.cookies import RequestsCookieJar
    jar = RequestsCookieJar()

    def add_cookie(name, value='foobar', **attrs):
        """
        Add a cookie to the cookie jar.

        """
        raw = '%s=%s' % (name, value)
        header = '%s=%s; %s' % (
            name, value, '; '.join('%s=%s' % (k, v) for (k, v) in attrs.items())
        )
        jar.set_cookie(RequestsCookieJar(jar).from_string(header))

    now = time.time()

    add_cookie('foo', path='/x')
    add_cookie('bar', path='/y')


# Generated at 2022-06-13 22:45:37.490033
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({
        'a': 'b',
        'c': 'd'
    }) == "{\n    'a': 'b',\n    'c': 'd'\n}"

# Generated at 2022-06-13 22:45:38.239244
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    ExplicitNullAuth()

# Generated at 2022-06-13 22:45:49.903262
# Unit test for function get_content_type
def test_get_content_type():
    assert 'text/json' == get_content_type('foo.json')
    assert 'text/xml' == get_content_type('foo.xml')
    assert 'text/html' == get_content_type('foo.html')
    assert 'application/javascript' == get_content_type('foo.js')
    assert 'application/xml' == get_content_type('foo.xhtml')
    assert 'image/svg+xml' == get_content_type('foo.svg')
    assert 'image/png' == get_content_type('foo.png')
    assert 'image/jpeg' == get_content_type('foo.jpeg')
    assert 'image/jpeg' == get_content_type('foo.jpg')

# Generated at 2022-06-13 22:45:52.200206
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    ExplicitNullAuth()
    return


if __name__ == '__main__':
    test_ExplicitNullAuth()

# Generated at 2022-06-13 22:45:57.191239
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime, timedelta
    from itertools import islice

    now = datetime.now()
    now_str = now.strftime('%a, %d-%b-%Y %H:%M:%S %Z')
    one_day = timedelta(days=1)

    def attr_to_str(attr):
        name, value = attr
        return f'{name}={value}'

    def make_set_cookie(
            name,
            value,
            path='/',
            expires=None,
            max_age=None,
            http_only=False,
            secure=False,
            same_site='Lax'
    ):

        same_site = '; SameSite=' + same_site
        # NB: "None" means "without attributes"


# Generated at 2022-06-13 22:46:07.404803
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'a':1, 'b': 2}) == "{'a': 1, 'b': 2}"
    assert repr_dict({'a':1, 'b': {'c': 3}}) == "{'a': 1, 'b': {'c': 3}}"
    assert repr_dict({'a':1, 'b': [1, 2, 3]}) == "{'a': 1, 'b': [1, 2, 3]}"
    assert repr_dict({'a':1, 'b': (1, 2, 3)}) == "{'a': 1, 'b': (1, 2, 3)}"

# Generated at 2022-06-13 22:46:19.641897
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    """
    Unit test for method __call__ of class ExplicitNullAuth
    """
    import copy
    import http.cookiejar as http_cookiejar
    import os.path
    import os
    import shutil
    import tempfile

    def create_tmp(cookies: List[dict]):
        cj = http_cookiejar.MozillaCookieJar()
        for cookie in cookies:
            cj.set_cookie(http_cookiejar.Cookie(**cookie))
        return cj

    # Create temporary directory
    tmp_dir = tempfile.mkdtemp()

    # Create environment variable HOME and assign it temporary directory
    os.environ['HOME'] = tmp_dir

    # Create copy of cookies
    cookies = copy.deepcopy(COOKIES)

    # Create temporary cookie file and populate it with the cookies
    tmp

# Generated at 2022-06-13 22:46:25.372978
# Unit test for function get_content_type
def test_get_content_type():
    # Sample 1
    filename = "test_table.csv"
    assert get_content_type(filename) == 'text/csv'

    # Sample 2
    filename = "test_table.csv.gz"
    assert get_content_type(filename) == 'application/gzip'




# Generated at 2022-06-13 22:46:28.312310
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    ExplicitNullAuth()

# Generated at 2022-06-13 22:46:33.677399
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'key':'value'}) == '{\'key\': \'value\'}'
    assert repr_dict({'key':{'key':'value'}}) == '{\'key\': {\'key\': \'value\'}}'

# Generated at 2022-06-13 22:46:42.772579
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'session=1234; Path=/'),
        ('Set-Cookie', 'expired=5; Path=/; Max-Age=2'),
    ]
    now = time.time()

    def cookiename(cookie):
        return cookie['name']

    assert cookiename(get_expired_cookies(headers, now)[0]) == 'expired'

    # After two seconds, expired cookie is expired!
    assert cookiename(get_expired_cookies(headers, now + 2)[0]) == 'session'


if __name__ == '__main__':
    import pytest
    import sys
    pytest.main(sys.argv)

# Generated at 2022-06-13 22:46:46.001582
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    json_string = '{"foo": "bar", "baz": "qux"}'
    assert load_json_preserve_order(json_string) == {'foo': 'bar', 'baz': 'qux'}

# Generated at 2022-06-13 22:46:53.316046
# Unit test for function get_content_type
def test_get_content_type():
    import sys

    if sys.version_info[0] >= 3:
        assert get_content_type('test.json') == 'application/json'
        assert get_content_type('Foo.exe') == 'application/octet-stream'
        assert get_content_type('foo.jpg') == 'image/jpeg'
        assert get_content_type('foo.jpeg') is None
        assert get_content_type('foo.pdf') == 'application/pdf'
    # mimetypes module does not provide mappings for .js files
    # on Windows platforms prior to Python 3.
    else:
        assert get_content_type('test.json') is None
        assert get_content_type('Foo.exe') == 'application/octet-stream'

# Generated at 2022-06-13 22:47:03.524012
# Unit test for function humanize_bytes
def test_humanize_bytes():
    tests = [
        (1024 * 1024 * 1024 * 32, "32.00 GB"),
        (1024 * 1024 * 1024 * 32 + 512 * 1024, "32.00 GB"),
        (1024 * 1024 * 1024 * 32 + 512 * 1024 * 1024, "33.49 GB"),
        (1024 * 1024 * 1024 * 34, "34.00 GB"),
        (1024 * 1024 * 1024 * 34 + 512 * 1024, "34.00 GB"),
        (1024 * 1024 * 1024 * 34 + 512 * 1024 * 1024, "35.49 GB"),
        (1024 * 1024 * 1024, "1.00 GB"),
        (1024 * 1024, "1.00 MB"),
        (1024, "1.00 kB"),
        (0, "0.00 B"),
    ]


# Generated at 2022-06-13 22:47:15.651289
# Unit test for function repr_dict
def test_repr_dict():
    # Empty dict
    t = {}
    assert repr_dict(t) == '{}'

    # Single-entry dict
    t = {'id': 'c81e728d9d4c2f636f067f89cc14862c'}
    assert repr_dict(t) == ("{'id': 'c81e728d9d4c2f636f067f89cc14862c'}")

    # Multi-entry dict
    t = {
        'id': 'c81e728d9d4c2f636f067f89cc14862c',
        'cookie': 'chocolate chip',
        'count': 42,
    }

# Generated at 2022-06-13 22:47:27.251245
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookies = [
        (
            'Set-Cookie',
            'session_id=12345; Max-Age=604800; '
            'Secure; HttpOnly; SameSite=Lax'
        ),
        (
            'Set-Cookie',
            'approved=yes; Expires=Sun, 01 Jan 2020 00:00:00 GMT; '
            'Domain=example.com; Path=/admin'
        ),
    ]
    expired = get_expired_cookies(headers=cookies, now=time.mktime(
        time.strptime('Sun, 02 Feb 2020 00:00:00 GMT', '%a, %d %b %Y %H:%M:%S %Z')
    ))
    assert expired == [{'name': 'approved', 'path': '/admin'}]

# Generated at 2022-06-13 22:47:29.536277
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({}) == "{}"
    assert repr_dict({'a': 1, 'b': 2}) == "{'a': 1, 'b': 2}"

# Generated at 2022-06-13 22:47:34.239794
# Unit test for function repr_dict
def test_repr_dict():
    d = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
    }
    assert repr_dict(d) == repr(d)