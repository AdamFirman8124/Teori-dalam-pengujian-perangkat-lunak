

# Generated at 2022-06-13 22:43:52.350917
# Unit test for function get_content_type
def test_get_content_type():
    import os
    import tempfile
    # Test normal path, using `mimetypes`
    fp, name = tempfile.mkstemp('.txt')
    with os.fdopen(fp, 'w'):
        pass
    assert get_content_type(name) == 'text/plain'

    # Test empty path
    assert get_content_type('') == None

# Generated at 2022-06-13 22:44:01.721986
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'COOKIE1=VALUE; Expires=Fri, 01 Jan 2016 00:00:00 GMT'),
        ('Set-Cookie', 'COOKIE2=VALUE'),
        ('Set-Cookie', 'COOKIE3=VALUE; Max-Age=10; Path=/'),
    ]
    now = time.time()
    cookies = get_expired_cookies(headers, now=now)
    assert cookies == [
        {'name': 'COOKIE2', 'path': '/'},
        {'name': 'COOKIE3', 'path': '/'}
    ]

# Generated at 2022-06-13 22:44:15.539638
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:44:17.334187
# Unit test for function get_content_type
def test_get_content_type():
    filename = __file__
    assert get_content_type(filename) == 'text/x-python'



# Generated at 2022-06-13 22:44:24.611480
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type(filename='test.json') == 'application/json'
    assert get_content_type(filename='test.xml') == 'application/xml'
    assert get_content_type(filename='test.png') == 'image/png'
    assert get_content_type(filename='test.txt') == 'text/plain'
    assert get_content_type(filename='test.pdf') == 'application/pdf'

# Generated at 2022-06-13 22:44:29.047519
# Unit test for function get_content_type
def test_get_content_type():
    assert (None == get_content_type('./not-existing-file'))
    assert ('application/json' == get_content_type('requests_mock_util.py'))
    assert ('text/html' == get_content_type('../README.md'))

# test_get_content_type()

# Generated at 2022-06-13 22:44:38.557612
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    headers = [
        ('Set-cookie', 'foo=BAR;'),
        ('Set-cookie', 'bar=FOO;'),
        ('Set-cookie', 'baz=BAM;Expires=Wed, 21 Oct 2015 07:28:00 GMT'),
        ('Set-cookie', 'bam=BAZ; Max-Age=1'),
    ]
    result = get_expired_cookies(headers, now)
    assert len(result) == 1
    assert result[0]['name'] == 'bam'
    assert result[0]['path'] == '/'

# Generated at 2022-06-13 22:44:48.262141
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:00.903369
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import datetime
    now = datetime.datetime.now(tz=datetime.timezone.utc)

# Generated at 2022-06-13 22:45:09.014009
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    cookie_name = 'foo'
    cookie_value = 'TEST'
    cookie_expires = time.time() + 5
    cookie_path = '/'
    header = 'Set-Cookie: %s=%s; Path=%s; Expires=%s' % (
        cookie_name,
        cookie_value,
        cookie_path,
        cookie_expires
    )
    headers = [(header, header)]
    expired_cookies = get_expired_cookies(headers, time.time())
    for expired_cookie in expired_cookies:
        assert expired_cookie['name'] == cookie_name
        assert expired_cookie['path'] == cookie_path

# Generated at 2022-06-13 22:45:23.074767
# Unit test for function get_content_type
def test_get_content_type():
    """
    >>> test_get_content_type()
    """
    from .utils_test import compare_content_files
    from .utils_test import get_test_data_file
    from .utils_test import get_test_data_file_content
    from .utils_test import get_tmpdir
    from .utils_test import run_with_tmpdir
    from .utils_test import write_to_tmpdir
    from six.moves.urllib.request import pathname2url

    def test_get_content_type_on_content(
        content: bytes,
        expected_content_type: str
    ):
        tmp_file = get_test_data_file()
        with open(tmp_file, 'wb') as f:
            f.write(content)

        mime, encoding = mimetypes

# Generated at 2022-06-13 22:45:36.261487
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from nose.tools import assert_equal


# Generated at 2022-06-13 22:45:42.273776
# Unit test for function get_content_type
def test_get_content_type():
    import os
    import tempfile
    tmpdir = tempfile.mkdtemp()
    filename = os.path.join(tmpdir, 'foo.txt')
    with open(filename, 'w') as f:
        f.write('')
    assert 'text/plain' == get_content_type(filename)
    os.remove(filename)
    os.rmdir(tmpdir)

# Generated at 2022-06-13 22:45:49.656118
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    _get_expired_cookies = get_expired_cookies

# Generated at 2022-06-13 22:45:57.074031
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'foo=bar; expires=Wed, 19 May 2030 07:21:00 GMT'),
        ('Set-Cookie', 'bar=baz; expires=Wed, 19 May 2030 07:21:00 GMT; Path=/foo'),
        ('Set-Cookie', 'baz=bat; max-age=3600; path=/'),
    ]
    now = time.time()
    expired = get_expired_cookies(headers, now=now + 100)
    assert expired == [
        {'name': 'baz', 'path': '/'},
    ]

# Generated at 2022-06-13 22:46:07.328473
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'foo=bar; max-age=86400; path=/; domain=.example.org'),
        ('Set-Cookie', 'bar=baz; max-age=60; path=/; domain=.example.org'),
        (
            'Set-Cookie',
            'baz=quux; expires=Wed, 09 Jun 2021 10:18:14 GMT; path=/;'
            ' domain=.example.org'
        ),
        (
            'Set-Cookie',
            'quux=quuux; expires=Tue, 09 Jun 2020 10:18:14 GMT;'
            ' path=/; domain=.example.org'
        )
    ]
    now = time.time()
    cookies = get_expired_cookies(headers, now)

# Generated at 2022-06-13 22:46:19.481809
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'cookie-foo=bar; expires=')
    ]
    expired_cookies = get_expired_cookies(
        headers=headers,
        now=time.time()
    )
    assert expired_cookies == [{'name': 'cookie-foo', 'path': '/'}]

    headers = [
        ('Set-Cookie', 'cookie-foo=bar; max-age=1')
    ]
    expired_cookies = get_expired_cookies(
        headers=headers,
        now=time.time()
    )
    assert expired_cookies == []

    headers = [
        ('Set-Cookie', 'cookie-foo=bar; max-age=0')
    ]

# Generated at 2022-06-13 22:46:30.522674
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    expired_time = time.time()
    not_expired_time = expired_time + 1000
    expired_cookie = 'my_cookie=my_cookie_value; Path=/; Expires=%s'
    not_expired_cookie = 'my_cookie=my_cookie_value; Path=/; Expires=%s'

# Generated at 2022-06-13 22:46:41.774110
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:46:50.734220
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime, timedelta

    expires = datetime.utcnow() + timedelta(seconds=10)

# Generated at 2022-06-13 22:46:56.302676
# Unit test for function get_content_type
def test_get_content_type():
    content_type = get_content_type("filename.txt")
    assert content_type == 'text/plain'


# Generated at 2022-06-13 22:47:03.827157
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([]) == []
    assert get_expired_cookies(
        [
            ('Set-Cookie', 'foo=bar; path=/; Max-Age=60'),
            ('Set-Cookie', 'baz=qux; path=/; expires=Sun, 01 Jan 2018 00:00:00 GMT'),
            ('Set-Cookie', 'abc=def; path=/; expires=Sun, 01 Jan 1970 00:00:00 GMT'),
        ],
        now=0
    ) == [
        {'name': 'baz', 'path': '/'},
        {'name': 'abc', 'path': '/'},
    ]



# Generated at 2022-06-13 22:47:15.825313
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:47:27.294653
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    sample_header_lines = [
        'Set-Cookie: foo=bar; Path=/; Max-Age=300',
        'Set-Cookie: baz=qux; Path=/; Max-Age=600',
        'Set-Cookie: sessionid=123; Path=/; Expires=Sun, 04 May 2014 18:11:00 GMT',
        'Set-Cookie: secure_sessionid=123; Path=/; '
        'Expires=Tue, 05 Jan 2038 18:11:00 GMT; secure',
        'Set-Cookie: sessionid=123; Path=/; Expires=Tue, 05 Jan 2038 18:11:00 GMT; secure',
    ]


# Generated at 2022-06-13 22:47:34.784821
# Unit test for function get_content_type

# Generated at 2022-06-13 22:47:38.566024
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type("/tmp/test.txt") == "text/plain"
    assert get_content_type("/tmp/test.rst") == "text/x-rst"

# Generated at 2022-06-13 22:47:50.544650
# Unit test for function get_content_type
def test_get_content_type():
    import os

    cwd = os.path.dirname(__file__)
    assert get_content_type(os.path.join(cwd, 'test_mime_types.txt')) == (
        'text/plain')
    assert get_content_type(os.path.join(cwd, 'test_mime_types.pdf')) == (
        'application/pdf')
    assert get_content_type(os.path.join(cwd, 'test_mime_types.gif')) == (
        'image/gif')
    assert get_content_type(os.path.join(cwd, 'test_mime_types.tgz')) == (
        'application/x-gtar')



# Generated at 2022-06-13 22:48:00.654103
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([
        ('Set-Cookie', 'a=1; Max-Age=60;'),
        ('Set-Cookie', 'b=2; Expires=Thu, 01-Jan-1970 00:00:00 GMT;'),
        ('Set-Cookie', 'c=3; Max-Age=120;'),
        ('Set-Cookie', 'd=4; Expires=Wed, 01-Jan-1970 00:00:00 GMT;'),
        ('Set-Cookie', 'e=5;'),
    ], now=0) == [  # Set to 1970-01-01 to force all cookies expired
        {'name': 'b', 'path': '/'},
        {'name': 'd', 'path': '/'},
    ]

# Generated at 2022-06-13 22:48:09.494876
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([('Set-Cookie', 'foo=bar')]) == []
    assert get_expired_cookies([('Set-Cookie', 'foo=bar; Expires=Wed, 27-Jan-2038 19:55:55 GMT')]) == [
        {'name': 'foo', 'path': '/'}
    ]
    assert get_expired_cookies([('Set-Cookie', 'foo=bar; Max-Age=0')]) == [
        {'name': 'foo', 'path': '/'}
    ]
    assert get_expired_cookies([('Set-Cookie', 'foo=bar; Max-Age=0; Path=/x')]) == [
        {'name': 'foo', 'path': '/x'}
    ]

# Generated at 2022-06-13 22:48:20.057257
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:48:31.838672
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('') is None
    assert get_content_type('.html') is None
    assert get_content_type('index.html') == 'text/html'
    assert get_content_type('/var/log/apache/index.html') == 'text/html'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.jpeg') == 'image/jpeg'
    assert get_content_type('foo.css') == 'text/css'
    assert get_content_type('foo.js') == 'application/javascript'
    assert (
        get_content_type('foo.js') ==
        'application/javascript'
    )

# Generated at 2022-06-13 22:48:43.163242
# Unit test for function get_content_type

# Generated at 2022-06-13 22:48:46.995896
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('file.txt') == 'text/plain'
    assert get_content_type('file.blah') is None

# Generated at 2022-06-13 22:48:52.937976
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type(filename='foo.txt') == 'text/plain'
    assert get_content_type(filename='foo.mp3') == 'audio/mpeg'
    assert get_content_type(filename='foo.mp4') == 'video/mp4'

# Generated at 2022-06-13 22:48:58.295405
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('dummy.txt') == 'text/plain'
    assert get_content_type('dummy.png') == 'image/png'
    assert get_content_type('dummy.json') == 'text/json'



# Generated at 2022-06-13 22:49:01.267632
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('index.html') == 'text/html'
    assert get_content_type('index.html.gz') == 'application/gzip'

# Generated at 2022-06-13 22:49:03.577173
# Unit test for function get_content_type
def test_get_content_type():
    filename = 'test.txt'
    assert get_content_type(filename) == 'text/plain'


if __name__ == '__main__':
    test_get_content_type()

# Generated at 2022-06-13 22:49:07.062921
# Unit test for function get_content_type
def test_get_content_type():
    assert (get_content_type('foo.png') == 'image/png')
    assert (get_content_type('foo.jpeg') == 'image/jpeg')
    assert (get_content_type('foo.bmp') == 'image/bmp')
    assert (get_content_type('foo.text') is None)



# Generated at 2022-06-13 22:49:09.479851
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.png') == 'image/png'
    assert get_content_type('test.pdf') is None  # unknown type

# Generated at 2022-06-13 22:49:15.569295
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('file.txt') == 'text/plain'
    assert get_content_type('file.html') == 'text/html'
    assert get_content_type('file.htm') == 'text/html'
    assert get_content_type('file.py') == 'text/x-python'
    assert get_content_type('file.png') == 'image/png'
    assert get_content_type('README') is None
    assert get_content_type('.') is None

# Generated at 2022-06-13 22:49:28.514414
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    class request_mock:
        def __init__(self, headers):
            self.headers = headers
            self.auth = None

        def prepare_request(self, prep_req):
            return prep_req

    # Test when headers do not contain `authorization`.
    prep_req = request_mock({})
    request = prep_req.prepare_request(prep_req)
    assert not request.headers
    assert not request.auth

    # Test when headers contain `authorization`.
    auth = 'Basic, Basic YWxhZGRpbjpvcGVuc2VzYW1l'
    prep_req = request_mock({'authorization': auth})
    request = prep_req.prepare_request(prep_req)
    assert not request.headers
    assert not request.auth

# Generated at 2022-06-13 22:49:37.837833
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime, timedelta

    def _set_expired_cookie(name: str, path: Optional[str] = None) -> dict:
        return {'name': name,
                'value': 'value',
                'path': path,
                'expires': datetime.utcnow() - timedelta(minutes=1)}

    def _set_non_expired_cookie(name: str, path: Optional[str] = None) -> dict:
        return {'name': name,
                'value': 'value',
                'path': path,
                'expires': datetime.utcnow() + timedelta(minutes=1)}


# Generated at 2022-06-13 22:49:46.555538
# Unit test for function humanize_bytes
def test_humanize_bytes():
    test_data = [
        [1, '1 B'],
        [100, '100 B'],
        [1024, '1.0 kB'],
        [1024 * 123, '123.0 kB'],
        [1024 * 12342, '12.1 MB'],
        [1024 * 12342, '12.05 MB', 2],
        [1024 * 1234, '1.21 MB', 2],
        [1024 * 1234 * 1111, '1.31 GB', 2],
        [1024 * 1234 * 1111, '1.3 GB', 1],
    ]
    for t in test_data:
        assert humanize_bytes(t[0], *t[1:]) == t[1]

# Generated at 2022-06-13 22:49:47.534878
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    ExplicitNullAuth()({})



# Generated at 2022-06-13 22:49:54.075800
# Unit test for function get_content_type
def test_get_content_type():
    """
    >>> get_content_type('foo.txt')
    'text/plain'
    >>> get_content_type('foo.html')
    'text/html'
    >>> get_content_type('foo.xhtml')
    'application/xhtml+xml'
    >>> get_content_type('foo.pdf')
    'application/pdf'
    >>> get_content_type('foo.png')
    'image/png'
    >>> get_content_type('foo.xlsx')
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    """
    pass

# Generated at 2022-06-13 22:50:03.938545
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    json_string_with_order = '{"4": "a", "5": "b", "1": "c"}'
    json_string_without_order = '{"5": "b", "1": "c", "4": "a"}'
    loaded_json_with_order = load_json_preserve_order(json_string_with_order)
    loaded_json_without_order = load_json_preserve_order(json_string_without_order)
    loaded_json_string_with_order = repr(loaded_json_with_order)
    loaded_json_string_without_order = repr(loaded_json_without_order)
    assert loaded_json_string_with_order == loaded_json_string_without_order


# Generated at 2022-06-13 22:50:09.252183
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = '{"a": "b", "c": "d"}'
    assert load_json_preserve_order(s) == {'a': 'b', 'c': 'd'}
    assert load_json_preserve_order(s) != {'c': 'd', 'a': 'b'}

# Generated at 2022-06-13 22:50:16.962529
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    # This should be semantically equivalent to the following:
    # >>> json.loads('{"b2": 3, "a": 42, "c": "foo"}')
    # OrderedDict([('b2', 3), ('a', 42), ('c', 'foo')])
    assert load_json_preserve_order('{"b2": 3, "a": 42, "c": "foo"}') == {
        'b2': 3, 'a': 42, 'c': 'foo'
    }

# Generated at 2022-06-13 22:50:20.368560
# Unit test for function repr_dict
def test_repr_dict():
    dict_ = {'key1':'value1', 'key2':'value2'}
    result = repr_dict(dict_)
    print(result)

# Generated at 2022-06-13 22:50:28.506956
# Unit test for function humanize_bytes
def test_humanize_bytes():
    """Test the humanize_bytes function"""
    assert humanize_bytes(1) == "1 B"
    assert humanize_bytes(1024, precision=1) == "1.0 kB"
    assert humanize_bytes(1024 * 123, precision=1) == "123.0 kB"
    assert humanize_bytes(1024 * 12342, precision=1) == "12.1 MB"
    assert humanize_bytes(1024 * 12342, precision=2) == "12.05 MB"
    assert humanize_bytes(1024 * 1234, precision=2) == "1.21 MB"
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == "1.31 GB"
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == "1.3 GB"

# Generated at 2022-06-13 22:50:37.039212
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    from io import BytesIO
    from requests.models import Response

    auth = ExplicitNullAuth()
    response = Response()
    response.raw = BytesIO(b'{"foo": "bar"}')
    response.headers['content-type'] = 'application/json'
    response.request.headers['Authorization'] = None
    auth(response)
    assert response.raw is not None
    assert response.json() == {'foo': 'bar'}
    assert response.request.headers['Authorization'] is None

# Generated at 2022-06-13 22:50:47.943140
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.exe') == 'application/octet-stream'
    assert get_content_type('test.bin') is None
    assert get_content_type('test.foo') is None
    assert get_content_type('test.foo.jpg') == 'image/jpeg'
    assert get_content_type('test.foo.bar') is None
    assert get_content_type('test.foo.bar.png') == 'image/png'
    assert get_content_type('test.foo.bar.jpg') == 'image/jpeg'
    assert get_content_type('test.foo.bar') is None


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 22:50:52.076157
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.pdf') == 'application/pdf'
    assert get_content_type('test.doc') is None

# Generated at 2022-06-13 22:51:02.322685
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
    # test if the content of the humanize output is

# Generated at 2022-06-13 22:51:13.488825
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    from requests.auth import HTTPDigestAuth
    from requests.models import Request

    headers = {
        'AUTHORIZATION': 'Basic CjAxYzBhYjBXYi5ceDNkOmI3LjU0NDIxMzQ='
        'YjQ2ODcwMjEwOWUxNDkyYTIyMjM=',
        'PROXY-AUTHENTICATE': 'Basic realm="myrealm"',
        'PROXY-AUTHORIZATION': 'Basic YjNhcWkyN3NjY2V2S2RvMjgyMm8ycjI4',
    }

    req = Request()
    req.body = None
    req.url = 'http://example.org/'
    req.method = 'GET'

# Generated at 2022-06-13 22:51:16.031459
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    json_dict = load_json_preserve_order('{"a": 1, "b": 2}')
    assert list(json_dict.keys()) == ["a", "b"]

# Generated at 2022-06-13 22:51:18.750897
# Unit test for function repr_dict
def test_repr_dict():
    d = {'foo': 'bar', 'baz': 2**30}
    assert repr_dict(d) == "{'foo': 'bar', 'baz': 1073741824}"

# Generated at 2022-06-13 22:51:23.821451
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = '{"a": "A", "b": "B", "c": "C", "d": "D"}'
    assert load_json_preserve_order(s) == OrderedDict([('a', 'A'),
                                                       ('b', 'B'),
                                                       ('c', 'C'),
                                                       ('d', 'D')])

# Generated at 2022-06-13 22:51:29.147161
# Unit test for function humanize_bytes
def test_humanize_bytes():
    assert humanize_bytes(42) == '42 B'
    assert humanize_bytes(42 * 1024) == '42.0 kB'
    assert humanize_bytes(42 * 1024 * 1024) == '42.0 MB'
    assert humanize_bytes(42 * 1024 * 1024 * 1024) == '42.0 GB'
    assert humanize_bytes(42 * 1024 * 1024 * 1024 * 1024) == '42.0 TB'
    assert humanize_bytes(42 * 1024 * 1024 * 1024 * 1024 * 1024) == '42.0 PB'

# Generated at 2022-06-13 22:51:33.273357
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    auth = ExplicitNullAuth()
    try:
        e = None
        assert auth is not None
    except Exception as e:
        print("error in test_ExplicitNullAuth: " + str(e))
        assert False


# Generated at 2022-06-13 22:51:48.058294
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    from io import StringIO
    from json import dumps

    d = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    s = dumps(d, indent=1)
    test_d = load_json_preserve_order(s)
    assert type(test_d) == OrderedDict

    # Test with file-like object
    fp = StringIO(s)
    test_d = load_json_preserve_order(fp)
    assert type(test_d) == OrderedDict

# Generated at 2022-06-13 22:51:51.345804
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    assert load_json_preserve_order('{"a": 1, "b": 2, "c": 3}') == {'a': 1, 'b': 2, 'c': 3}
    assert list(load_json_preserve_order('{"a": 1, "b": 2, "c": 3}').keys()) == ['a', 'b', 'c']

# Generated at 2022-06-13 22:51:56.263337
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
  assert {'a': 1, 'b': 2} == load_json_preserve_order('{"a": 1, "b": 2}')
  assert {'a': 1, 'b': 2} == load_json_preserve_order('{"b": 2, "a": 1}')

# Generated at 2022-06-13 22:51:57.758371
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth(): # type: () -> None
    ExplicitNullAuth()

# Generated at 2022-06-13 22:52:02.077689
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    """
    Test of method ExplicitNullAuth.__call__
    """
    import pytest

    ExplicitNullAuth()(None)

    with pytest.raises(TypeError):
        ExplicitNullAuth()(1)

# Generated at 2022-06-13 22:52:03.687760
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    instance = ExplicitNullAuth()
    assert instance is not None

# Generated at 2022-06-13 22:52:06.379619
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    """
    Tests that ExplicitNullAuth can be initialized.
    """
    ExplicitNullAuth()

# Generated at 2022-06-13 22:52:06.916805
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:52:08.167120
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    class Request(object): pass

    r = Request()
    a = ExplicitNullAuth()
    assert a(r) is r

# Generated at 2022-06-13 22:52:09.591106
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

