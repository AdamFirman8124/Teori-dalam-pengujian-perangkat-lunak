

# Generated at 2022-06-13 22:44:01.760898
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.tar.gz') == 'application/gzip'
    assert get_content_type('foo.tar.xz') == 'application/x-xz'
    assert get_content_type('foo.tar.bz2') == 'application/x-bzip2'
    assert get_content_type('foo.tar.Z') == 'application/x-compress'
    assert get_content_type('foo.tar.lzma') == 'application/x-lzma'
    assert get_content_type('foo.log') == 'text/plain'

# Generated at 2022-06-13 22:44:15.565259
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('f.txt') == 'text/plain'
    assert get_content_type('f.html') == 'text/html'
    assert get_content_type('f.json') == 'application/json'
    assert get_content_type('f.gif') == 'image/gif'
    assert get_content_type('f.jpeg') == 'image/jpeg'
    assert get_content_type('f.jpg') == 'image/jpeg'
    assert get_content_type('f.png') == 'image/png'
    assert get_content_type('f.py') == 'text/x-python'
    assert get_content_type('f.zip') == 'application/zip'
    assert get_content_type('f.gz') == 'application/x-gzip'

# Generated at 2022-06-13 22:44:19.540316
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/path/to/foo.csv') == 'text/csv'
    assert get_content_type('/path/to/bar.json') == 'application/json'
    assert get_content_type('/path/to/baz.mp3') == 'audio/mpeg'

# Generated at 2022-06-13 22:44:26.185533
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie',
         'foo=1; path=/; expires=Sun, 19-Jan-2020 16:20:12 GMT'),
        ('Set-Cookie',
         'bar=1; path=/; max-age=60'),
    ]

    expected = [
        {'name': 'foo', 'path': '/'},
    ]

    assert get_expired_cookies(headers=headers, now=1579579012) == expected

# Generated at 2022-06-13 22:44:34.717490
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    expired_cookies = get_expired_cookies([
        ('Set-Cookie',
         'mycookie=myvalue; Max-Age=1; Path=/'),
        ('Set-Cookie',
         'mycookie2=myvalue; Expires={}; Path=/'.format(
             time.strftime('%a, %d-%b-%Y %T GMT', time.gmtime(now + 1)))),
        ('Set-Cookie',
         'mycookie3=myvalue; Expires={}; Path=/'.format(
             time.strftime('%a, %d-%b-%Y %T GMT', time.gmtime(now - 1))))
    ], now=now)


# Generated at 2022-06-13 22:44:44.107481
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('sample.png') == 'image/png'
    assert get_content_type('sample.txt') == 'text/plain'
    assert get_content_type('sample.jpg') == 'image/jpeg'
    assert get_content_type('sample.jpeg') == 'image/jpeg'
    assert get_content_type('sample.html') == 'text/html'
    assert get_content_type('sample.htm') == 'text/html'

    assert get_content_type('sample_unknown.abc') is None
    assert get_content_type('sample_unknown') is None



# Generated at 2022-06-13 22:44:53.935895
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import requests

    s = requests.Session()

    def _assert(cookies, status_code, msg=None):
        if msg is None:
            msg = 'HTTP %s, cookies %s' % (status_code, repr_dict(cookies))
        if status_code == 302:
            s.get(url, allow_redirects=False)
        else:
            r = s.get(url)
            assert cookies == get_expired_cookies(r.headers), msg
            assert status_code == r.status_code, msg

    # Test various scenarios and make sure we can delete the cookies properly.
    url = 'http://httpbin.org/cookies/set/foo/bar'

# Generated at 2022-06-13 22:44:55.438155
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/path/to/whatever.foo') is None

# Generated at 2022-06-13 22:44:59.798119
# Unit test for function get_content_type
def test_get_content_type():
    """Test :py:func:`get_content_type`"""
    assert get_content_type(filename='/tmp/dummyfile.txt') == 'text/plain'
    assert get_content_type(filename='/tmp/dummyfile.tgz') == \
        'application/x-gtar'

# Generated at 2022-06-13 22:45:02.391752
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('index.html') == 'text/html'
    assert get_content_type('application/octet-stream') is None

# Generated at 2022-06-13 22:45:10.300023
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    """
    >>> import requests
    >>> p = requests.get('https://httpbin.org/get', auth=ExplicitNullAuth())
    >>> p.request.headers
    {'User-Agent': 'python-requests/2.9.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

    """


# Generated at 2022-06-13 22:45:16.775412
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('counter.log') == 'text/plain'
    assert get_content_type('image.png') == 'image/png'
    assert get_content_type('image.svg') == 'image/svg+xml'
    assert get_content_type('document.pdf') == 'application/pdf'
    assert get_content_type('data') is None

# Generated at 2022-06-13 22:45:23.412678
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.csv') == 'text/csv'
    assert get_content_type('foo.bin') == 'application/octet-stream'
    assert get_content_type('foo.xxx') == None

# Generated at 2022-06-13 22:45:25.404569
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    print(ExplicitNullAuth())  # It should not raise any error

# Generated at 2022-06-13 22:45:28.322911
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain; charset=us-ascii'

# Generated at 2022-06-13 22:45:31.587758
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    import requests
    req = requests.Request()
    req.auth = ExplicitNullAuth()
    assert req.auth(req) is req

# Generated at 2022-06-13 22:45:34.620528
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'hello': 'world'}) == "{'hello': 'world'}"


# Generated at 2022-06-13 22:45:40.656265
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    assert load_json_preserve_order('{"a": 1, "b": 2}') == {'a': 1, 'b': 2}
    assert type(load_json_preserve_order('{"a": 1, "b": 2}')) is OrderedDict
    # Should not fail
    assert load_json_preserve_order('1') == 1


# Generated at 2022-06-13 22:45:46.667243
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    json_str = '{"aa" : ["a", "b"], "bb": "cc"}'
    expected_odict = OrderedDict([('aa', ['a', 'b']), ('bb', 'cc')])
    actual_odict = load_json_preserve_order(json_str)
    assert actual_odict == expected_odict



# Generated at 2022-06-13 22:45:50.058107
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = '{"a": 1, "b": 2, "c": 3}'
    d = load_json_preserve_order(s)
    assert isinstance(d, OrderedDict)
    assert list(d.keys()) == ['a', 'b', 'c']

# Generated at 2022-06-13 22:45:54.033265
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    js = '{"a": 1, "b": 2}'
    js2 = '{"b": 2, "a": 1}'
    assert repr(load_json_preserve_order(js)) == repr(load_json_preserve_order(js2))

# Generated at 2022-06-13 22:46:06.212714
# Unit test for function get_content_type
def test_get_content_type():
    assert 'text/plain' == get_content_type('foo.txt')
    assert 'text/plain' == get_content_type('foo.TXT')
    assert 'text/x-python' == get_content_type('foo.py')
    assert 'text/x-python' == get_content_type('foo.PY')
    assert 'text/plain' == get_content_type('foo')
    assert 'application/octet-stream' == get_content_type('foo.bin')
    assert 'application/octet-stream' == get_content_type('foo.BIN')
    assert None is get_content_type('foo.bar')
    assert None is get_content_type('foo.BAR')
    assert None is get_content_type('foo.')

# Generated at 2022-06-13 22:46:17.785189
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



# Generated at 2022-06-13 22:46:19.435752
# Unit test for function humanize_bytes
def test_humanize_bytes():
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 22:46:20.114956
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:46:27.441657
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({}) == "{}"
    assert repr_dict({"a": 1}) == "{'a': 1}"
    assert repr_dict({"b": 1, "a": 2}) == "{'b': 1, 'a': 2}"

    d = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
    assert repr_dict(d) == "{'a': 1, 'b': 2, 'c': 3}"

# Generated at 2022-06-13 22:46:33.633684
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    test_dict = {'b': 1, 'a': 2}
    expected_dict = {'a': 2, 'b': 1}
    
    s = json.dumps(test_dict)
    result = load_json_preserve_order(s)
    assert(result == expected_dict)

# Generated at 2022-06-13 22:46:43.465610
# Unit test for function humanize_bytes
def test_humanize_bytes():
    tests = [
        (1, "1 B"),
        (1023, "1023 B"),
        (1024, "1.0 kB"),
        (1024 * 1023, "1023.0 kB"),
        (1024 * 1024, "1.0 MB"),
        (1024 * 1024 * 1023, "1023.0 MB"),
        (1024 * 1024 * 1024, "1.0 GB"),
        (1024 * 1024 * 1024 * 1023, "1023.0 GB"),
        (1024 * 1024 * 1024 * 1024, "1.0 PB"),
        (1024 * 1024 * 1024 * 1024 * 1023, "1023.0 PB"),
    ]

    for (n, expected) in tests:
        assert humanize_bytes(n) == expected


# Generated at 2022-06-13 22:46:51.995141
# Unit test for function humanize_bytes
def test_humanize_bytes():
    assert humanize_bytes(-42) == "-42 B"
    assert humanize_bytes(-42, 1) == "-42.0 B"
    assert humanize_bytes(-1000) == "-1000 B"
    assert humanize_bytes(-1024) == "-1.0 kB"
    assert humanize_bytes(-1024, 1) == "-1.0 kB"
    assert humanize_bytes(-1024, 2) == "-1.00 kB"
    assert humanize_bytes(-1024 * 123, 2) == "-123.00 kB"
    assert humanize_bytes(-1024 * 12342) == "-12.1 MB"
    assert humanize_bytes(-1024 * 12342, 2) == "-12.05 MB"
    assert humanize_bytes(-1024 * 1234, 2) == "-1.21 MB"
    assert humanize_bytes

# Generated at 2022-06-13 22:46:54.607676
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'a': 1}) == "{'a': 1}"