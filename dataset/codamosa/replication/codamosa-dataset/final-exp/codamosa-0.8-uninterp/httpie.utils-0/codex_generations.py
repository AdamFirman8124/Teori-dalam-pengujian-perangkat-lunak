

# Generated at 2022-06-13 22:43:47.115065
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('a.txt') == 'text/plain'
    assert get_content_type('a.json') == 'application/json'
    assert get_content_type('a.js') == 'application/javascript'
    assert get_content_type('a.pdf') == 'application/pdf'
    assert get_content_type('a.xlsx') == 'application/vnd.openxmlformats-' \
                                     'officedocument.spreadsheetml.sheet'

# Generated at 2022-06-13 22:43:59.416073
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    name = 'JSESSIONID'
    path = '/crx/de'
    now = time.time()
    max_age_future = '3600'
    max_age_past = '0'
    expires_future = now + 3600
    expires_past = now - 3600
    expired = get_expired_cookies(
        headers=[
            ('Set-Cookie', '%s=value; path=%s; Max-Age=%s'
                % (name, path, max_age_past))
        ], now=now
    )
    assert len(expired) == 1
    assert expired[0]['name'] == name
    assert expired[0]['path'] == path

# Generated at 2022-06-13 22:44:07.338884
# Unit test for function get_content_type
def test_get_content_type():
    # Tests good content types
    assert get_content_type('index.html') == 'text/html'
    assert get_content_type('test.json') == 'application/json'
    # Tests bad content types (hence None)
    assert get_content_type('index.html.txt') is None
    assert get_content_type('test.js.txt') is None
    assert get_content_type('notreallyafile.txt') is None

# Generated at 2022-06-13 22:44:11.919346
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('filename.exe') == 'application/octet-stream'
    assert get_content_type('filename.mp4') == 'video/mp4'
    assert get_content_type('filename.css') == 'text/css'
    assert get_content_type('filename.html') == 'text/html'
    assert get_content_type('filename.txt') == 'text/plain'
    assert get_content_type('filename.py') == 'text/x-python'
    assert get_content_type('filename.rst') == 'text/x-rst'

# Generated at 2022-06-13 22:44:15.815576
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('some_name') is None
    assert get_content_type('some_name.jpg') == 'image/jpeg'
    assert get_content_type('some_name.jpeg') == 'image/jpeg'

# Generated at 2022-06-13 22:44:23.734377
# Unit test for function get_content_type
def test_get_content_type():
    assert 'application/json' == get_content_type('foo.json')
    assert not get_content_type('foo')
    assert 'text/plain' == get_content_type('foo.txt')
    assert 'text/plain' == get_content_type('foo.TXT')
    assert 'text/plain' == get_content_type('foo.Txt')
    assert 'text/plain' == get_content_type('foo.txt')



# Generated at 2022-06-13 22:44:32.776066
# Unit test for function get_content_type
def test_get_content_type():
    import os.path
    import unittest
    from unittest.mock import mock_open, patch

    class TestCase(unittest.TestCase):
        def test_good(self):
            expected = 'text/plain'
            with patch('mimetypes.MimeTypes.guess_type') as obj:
                obj.return_value = (expected, None)
                result = get_content_type('filename.txt')
            self.assertEqual(result, expected)

        def test_good_with_encoding(self):
            mimetype = 'text/plain'
            encoding = 'us-ascii'
            expected = '%s; charset=%s' % (mimetype, encoding)

# Generated at 2022-06-13 22:44:34.153120
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type("test.jpeg") == 'image/jpeg'

# Generated at 2022-06-13 22:44:39.924870
# Unit test for function get_content_type
def test_get_content_type():
    tests = [
        ('test.jpg', 'image/jpeg'),
        ('test.txt', 'text/plain'),
        ('test.json', 'application/json'),
        ('test.foo', None)
    ]
    for filename, content_type in tests:
        assert get_content_type(filename) == content_type



# Generated at 2022-06-13 22:44:49.028484
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:03.020350
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import freezegun
    from freezegun.api import FakeDatetime

    headers = [(
        'Set-Cookie',
        'foo=bar-max-age-12; Domain=pl; Path=/; Max-Age=12; '
        'Expires=Mon, 19-Jan-2015 17:40:43 GMT; '
    ), (
        'Set-Cookie',
        'baz=qux-expires-14; Domain=pl; Path=/; '
        'Expires=Mon, 19-Jan-2015 17:40:44 GMT; '
    )]
    now = time.time()

    # Case 1: with max-age

# Generated at 2022-06-13 22:45:06.892615
# Unit test for function get_content_type
def test_get_content_type():
    for filename, content_type in [
        ('foo.txt', 'text/plain'),
        ('bar.html', 'text/html'),
        ('baz.json', 'application/json')
    ]:
        assert get_content_type(filename) == content_type

# Generated at 2022-06-13 22:45:13.557731
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from http import client


# Generated at 2022-06-13 22:45:23.534221
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime
    from datetime import timedelta

    # Get current time
    now = datetime.now()

    # Set a time for a cookie to expire
    expires = now + timedelta(days=1)

    # Turn the expires into a string that is formatted correctly for a cookie
    cookie_expires = expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

    cookies = [
        'cookie1=chocolatechip; expires={}'.format(cookie_expires),
        'cookie2=peanutbutter; expires={}'.format(cookie_expires),
        'cookie3=blueberry; expires={}'.format(cookie_expires)
    ]

    # Add a few more cookies to the list, but set them to expire at a future date.
    cookies

# Generated at 2022-06-13 22:45:36.590895
# Unit test for function get_expired_cookies
def test_get_expired_cookies():  # pylint: disable=missing-docstring
    from dataclasses import asdict
    from fractions import Fraction
    from unittest.mock import Mock
    from urllib.parse import urlparse

    from hypothesis import given, strategies as st

    from s3_encryption_client_side import utils

    def gen_cookie() -> Tuple[str, str]:
        cookie_str = st.builds(
            lambda attrs: '; '.join('='.join(pair) for pair in attrs),
            st.dictionaries(
                st.just('name'),
                st.text(),
                min_size=1,
                max_size=1,
            ) + st.dictionaries(st.text(), st.text()),
        )

# Generated at 2022-06-13 22:45:46.021251
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:45:54.741240
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from itertools import groupby
    from http.cookies import SimpleCookie as Cookie

    def mk_headers(**kwargs):
        return [('Set-Cookie', mk_cookie(**kwargs).output(header=''))]

    def mk_cookie(domain='example.com', path='/', name='foo', max_age=None):
        cookie = Cookie()
        cookie[name] = 'bar'
        cookie[name]['domain'] = domain
        cookie[name]['path'] = path
        if max_age is not None:
            cookie[name]['max_age'] = max_age
        return cookie

    expired_cookies = get_expired_cookies(
        headers=mk_headers(max_age=0),
        now=1,
    )

# Generated at 2022-06-13 22:46:06.352542
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Server', 'nginx/1.2.3'),
        ('Date', 'Thu, 21 Feb 2013 10:59:44 GMT'),
        ('Content-Type', 'application/json'),
        ('Content-Length', '148'),
        ('Connection', 'keep-alive'),
        ('Set-Cookie', 'foo=bar; Domain=buzz.com; Path=/; Expires=Thu, 21 Feb 2013 11:00:44 GMT'),
        ('Set-Cookie', 'swarm=bee; Domain=buzz.com; Path=/; Expires=Thu, 21 Feb 2013 11:00:44 GMT; HttpOnly'),
    ]
    assert get_expired_cookies(headers) == []


# Generated at 2022-06-13 22:46:18.577585
# Unit test for function get_expired_cookies

# Generated at 2022-06-13 22:46:27.519507
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    request_headers = [
        ('Set-Cookie', 'foo=bar; expires=Thu, 19 Feb 2015 20:00:00 GMT'),
        ('Set-Cookie', 'baz=quux; expires=Fri, 19 Feb 2099 20:00:00 GMT'),
        ('Set-Cookie', 'baz=quux; expires=Fri, 19 Feb 2099 20:00:00 GMT'),
        ('Set-Cookie', 'baz=quux; path=/'),
        ('Set-Cookie', 'baz=quux; max-age=3600'),
        ('Set-Cookie', 'baz=quux; expires=Fri, 19 Feb 2015 19:59:00 GMT'),
    ]
    now = time.time()

    cookies = get_expired_cookies(headers=request_headers, now=now)

    assert len

# Generated at 2022-06-13 22:46:38.948470
# Unit test for function get_content_type
def test_get_content_type():
    from .workbench import Workbench
    from unittest import main
    wb = Workbench('NoCmdLine')
    assert wb.call(get_content_type, ['test.py']) == \
           'text/x-python; charset=us-ascii'
    assert wb.call(get_content_type, ['test.tar.gz']) == \
           'application/x-gzip; charset=binary'
    assert wb.call(get_content_type, ['test.png']) is None
    main()

if __name__ == '__main__':
    test_get_content_type()

# Generated at 2022-06-13 22:46:40.303362
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('index.html') == 'text/html'

# Generated at 2022-06-13 22:46:50.225016
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.gif') == 'image/gif'
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.jpeg') == 'image/jpeg'
    assert get_content_type('foo.pdf') == 'application/pdf'
    assert get_content_type('foo.doc') == 'application/msword'
    assert get_content_type('foo.docx') == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

# Generated at 2022-06-13 22:46:52.359800
# Unit test for function get_content_type
def test_get_content_type():
    from .test_helpers import assert_equal

    assert_equal(get_content_type('.bashrc'), 'text/plain')
    assert_equal(get_content_type('not-a-file'), None)

# Generated at 2022-06-13 22:47:00.449115
# Unit test for function get_content_type
def test_get_content_type():
    if get_content_type('/foo/bar') != 'application/octet-stream':
        raise AssertionError

    if get_content_type('/foo/bar.txt') != 'text/plain':
        raise AssertionError

    if get_content_type('/foo/bar.bin') != 'application/octet-stream':
        raise AssertionError

    if get_content_type('/foo/bar.bin.txt') != 'text/plain':
        raise AssertionError

# Generated at 2022-06-13 22:47:02.736764
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'

# Generated at 2022-06-13 22:47:06.035030
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.unknown') is None

# Generated at 2022-06-13 22:47:16.995859
# Unit test for function get_content_type
def test_get_content_type():
    test_data = [
        ('test.jpg', 'image/jpeg'),
        ('test.JPG', 'image/jpeg'),
        ('test.jpeg', 'image/jpeg'),
        ('test.JPEG', 'image/jpeg'),
        ('test.png', 'image/png'),
        ('test.PNG', 'image/png'),
        ('test.csv', 'text/csv'),
        ('test.txt', 'text/plain'),
        ('test.doc', None),
    ]

    for test_fname, test_result in test_data:
        res = get_content_type(test_fname)
        assert res == test_result, 'File {}, expected {}, got {}'.format(
            test_fname, test_result, res
        )


# Generated at 2022-06-13 22:47:18.944142
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type(r'C:\foo\bar.txt') == 'text/plain'

# Generated at 2022-06-13 22:47:29.244051
# Unit test for function get_content_type
def test_get_content_type():
    import os

    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, 'test_image.jpg')
    script_path = os.path.join(base_path, __file__)

    # Test with non-existent file
    # Should trigger a warning, but we cannot test for that here
    content_type = get_content_type('non-existent.jpg')
    assert content_type is None

    # Test with image file
    content_type = get_content_type(image_path)
    assert content_type == 'image/jpeg'

    # Test with script file
    content_type = get_content_type(script_path)
    assert content_type == 'text/x-python'



# Generated at 2022-06-13 22:47:31.555117
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('hallo.txt') == 'text/plain'

# Generated at 2022-06-13 22:47:34.856812
# Unit test for function get_content_type
def test_get_content_type():
    from nose.tools import eq_
    eq_(get_content_type('test.pdf'), 'application/pdf')
    eq_(get_content_type('test'), None)



# Generated at 2022-06-13 22:47:38.259052
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/path/to/file') is None
    assert get_content_type('/path/to/file.txt') == 'text/plain'

# Generated at 2022-06-13 22:47:50.624367
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('filename') is None
    assert get_content_type('filename.ext') is None
    assert get_content_type('filename.extension') == \
           'application/octet-stream'
    assert get_content_type('filename.txt') == \
           'text/plain'
    assert get_content_type('filename.txt.compress') == \
           'application/x-compress'
    assert get_content_type('filename.txt.gzip') == \
           'application/x-gzip'
    assert get_content_type('filename.txt.gz') == \
           'application/x-gzip'
    assert get_content_type('filename.txt.bz2') == \
           'application/x-bzip2'

# Generated at 2022-06-13 22:47:58.028237
# Unit test for function get_content_type
def test_get_content_type():
    assert (get_content_type('test.txt') == 'text/plain')
    assert (get_content_type('test.png') == 'image/png')
    assert (get_content_type('test.pdf') == 'application/pdf')
    assert (get_content_type('test.js') == 'application/javascript')
    assert (get_content_type('test.gz') == 'application/x-gzip')


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 22:48:04.494216
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.svg') == 'image/svg+xml'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.png.txt') == 'image/png'
    assert get_content_type('foo.tar.gz') == 'application/x-gzip'
    assert get_content_type('foo.threejs') is None

# Generated at 2022-06-13 22:48:11.853898
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/path/to/file') is None
    assert get_content_type('/path/to/file.txt') == 'text/plain'
    assert get_content_type('/path/to/file.vcf') == 'text/x-vcard'
    assert get_content_type('/path/to/file.vcf.gpg') == 'text/x-vcard'

# Generated at 2022-06-13 22:48:18.326253
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('filename.txt') == 'text/plain'
    assert get_content_type('filename.html') == 'text/html'
    assert get_content_type('filename.jpg') == 'image/jpeg'
    assert get_content_type('filename.html.gz') == 'text/html'
    assert get_content_type('filename.htm.gzip') == 'text/html'
    assert not get_content_type('filename')

# Generated at 2022-06-13 22:48:23.895517
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('b.txt') == 'text/plain'
    assert get_content_type('d.html') == 'text/html'
    assert get_content_type('c.css') == 'text/css'
    assert get_content_type('a.js') == 'application/javascript'

# Generated at 2022-06-13 22:48:30.904672
# Unit test for function get_content_type
def test_get_content_type():

    assert get_content_type('index.html') == 'text/html'

    assert get_content_type('test_get_content_type.py') == \
        'text/x-python'

    assert get_content_type('test_get_content_type.jpg') == \
        'image/jpeg'

    assert get_content_type('test_get_content_type.pdf') == \
        'application/pdf'

    assert get_content_type('test_get_content_type.ogg') == \
        'audio/ogg'

# Generated at 2022-06-13 22:48:34.626748
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'a': 'b'}) == "{'a': 'b'}"

# Generated at 2022-06-13 22:48:35.505339
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    ExplicitNullAuth()

# Generated at 2022-06-13 22:48:38.758254
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    d = dict(a=1, b=2, c=3)
    s = json.dumps(d)  # type: str
    assert load_json_preserve_order(s) == d

# Generated at 2022-06-13 22:48:47.145750
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', '1=1; Path=/; Max-Age=3'),
        ('Set-Cookie', '2=2; Path=/; Expires=Wed, 09 Jun 2021 10:18:14 GMT'),
        ('Set-Cookie', '3=3; Path=/; Expires=Wed, 09 Jun 2021 10:18:14 GMT'),
        ('Set-Cookie', '4=4; Path=/; Expires=Wed, 09 Jun 2021 10:18:14 GMT'),
    ]
    now = time.time()
    # 2 and 3 should be expired
    assert [dict(name='2', path='/'), dict(name='3', path='/')] == get_expired_cookies(headers, now - 80)
    # 4 should be expired

# Generated at 2022-06-13 22:48:52.311065
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

# Generated at 2022-06-13 22:49:00.972957
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    assert 'a' in load_json_preserve_order('{"a":1}')
    assert 'b' in load_json_preserve_order('{"a":1,"b":2}')
    assert 'a' in load_json_preserve_order('{"a":1,"b":2}')
    assert load_json_preserve_order('{"a":1,"b":2}')['a'] == 1
    assert load_json_preserve_order('{"a":1,"b":2}')['b'] == 2

# Generated at 2022-06-13 22:49:05.013431
# Unit test for function repr_dict
def test_repr_dict():
    d = OrderedDict([('foo', 42), ('bar', obj)])
    assert repr_dict(d) == (
        "OrderedDict([('foo', 42),\n"
        "             ('bar', <object object at 0x7f8501baae10>)])"
    )

# Generated at 2022-06-13 22:49:14.819817
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo') == 'text/plain'
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.html.gz') == 'application/x-gzip'
    assert get_content_type('foo.html.bz2') == 'application/x-bzip2'
    assert get_content_type('foo.html.zip') == 'application/zip'
    assert get_content_type('foo.html.xz') == 'application/x-xz'



# Generated at 2022-06-13 22:49:21.610195
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type("README.md") == "text/plain"
    assert get_content_type("fixtures/example.docx") == \
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    assert get_content_type("fixtures/example.xlsx") == \
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert get_content_type("fixtures/example.odt") == \
        "application/vnd.oasis.opendocument.text"
    assert get_content_type("fixtures/example.ods") == \
        "application/vnd.oasis.opendocument.spreadsheet"
    assert get_content_type("fixtures/example.pdf") == "application/pdf"


# Generated at 2022-06-13 22:49:26.200466
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():

    s = """
    {"a":1,"b":2,"c":3}
    """

    d = load_json_preserve_order(s)
    expected = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    assert d == expected

# Generated at 2022-06-13 22:49:37.679433
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

# Generated at 2022-06-13 22:49:46.916714
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

# Generated at 2022-06-13 22:49:54.900313
# Unit test for function get_content_type
def test_get_content_type():

    # Our test file
    from os import path
    from io import StringIO
    from tempfile import NamedTemporaryFile

    test_dir = path.dirname(__file__)
    ok_file_path = path.join(test_dir, 'assets/sample.txt')

    # Check against the valid file
    assert get_content_type(ok_file_path) == 'text/plain'

    # Check against the invalid file
    with NamedTemporaryFile('w', delete=False) as tmp:
        tmp.write('')

    try:
        assert get_content_type(tmp.name) is None
    finally:
        from os import remove
        remove(tmp.name)

    # Check against a stream
    assert get_content_type(StringIO('hello world')) is None

# Generated at 2022-06-13 22:49:57.501593
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth().__class__.__name__ == 'ExplicitNullAuth'
    try:
        ExplicitNullAuth()
    except Exception:
        assert False


# Generated at 2022-06-13 22:50:01.121295
# Unit test for function repr_dict
def test_repr_dict():
    result = repr_dict({
        'a': 'b',
        'c': {
            'd': 'e',
        }
    })
    assert result == "{'a': 'b', 'c': {'d': 'e'}}"

# Generated at 2022-06-13 22:50:05.184498
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    auth_object = ExplicitNullAuth()
    request_object = requests.Request()
    request_object.get_method = lambda: ''
    request_object.prepare_url = lambda: ''
    request_object.method = ''

    request_object2 = auth_object(request_object)

    return request_object2 is request_object

# Generated at 2022-06-13 22:50:10.197301
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    # Expected output : {'a': 1, 'b': '2', 'c': 3}
    assert load_json_preserve_order("{\"a\": 1, \"b\": \"2\", \"c\": 3}") \
        == {'a': 1, 'b': '2', 'c': 3}

    # Expected output : {'a': 1, 'b': '2', 'c': 3, 'd': [1, 2, 3]}
    assert load_json_preserve_order("{\"a\": 1, \"b\": \"2\", \"c\": 3, \"d\": [1, 2, 3]}") \
        == {'a': 1, 'b': '2', 'c': 3, 'd': [1, 2, 3]}

# Generated at 2022-06-13 22:50:17.765898
# Unit test for function humanize_bytes
def test_humanize_bytes():
    def h(n, precision=2):
        s = humanize_bytes(n, precision=precision)
        q, r = divmod(n, 1024)
        assert s == '%.*f %s' % (precision, r, {1: 'B', 0: ''}[q])

    h(1)
    h(1023, precision=0)
    h(1024)
    h(1024 * 1024 - 1, precision=0)
    h(1024 * 1024, precision=0)

# Generated at 2022-06-13 22:50:22.636281
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    text = '{"b": 2, "a": 1}'
    obj = load_json_preserve_order(text)
    assert 'b' in obj
    assert 'a' in obj
    assert obj['b'] == 2
    assert obj['a'] == 1
    assert next(iter(obj)) == 'b'



# Generated at 2022-06-13 22:50:28.407165
# Unit test for function repr_dict
def test_repr_dict():
    original_dict = OrderedDict()
    original_dict['Name'] = 'Chen'
    original_dict['Age'] = 123
    original_dict['Birth'] = '2000-01-01'
    expected_repr = "OrderedDict([('Name', 'Chen'), ('Age', 123), ('Birth', '2000-01-01')])"
    assert repr_dict(original_dict) == expected_repr


# Generated at 2022-06-13 22:50:33.520959
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    auth = ExplicitNullAuth()
    assert auth

# Generated at 2022-06-13 22:50:34.357487
# Unit test for function humanize_bytes
def test_humanize_bytes():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 22:50:37.421447
# Unit test for function repr_dict
def test_repr_dict():
    actual = repr_dict({1: 2, 3: 4, 5: 6})
    expected = ("{1: 2,\n"
                " 3: 4,\n"
                " 5: 6}")
    assert actual == expected

# Generated at 2022-06-13 22:50:43.636662
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({'a': 1, 'b': 2}) == "{'a': 1, 'b': 2}"
    assert repr_dict([1, 2]) == "[1, 2]"
    assert repr_dict(OrderedDict([('a', 1), ('b', 2)])) == "{'a': 1, 'b': 2}"

# Generated at 2022-06-13 22:50:50.307493
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


# Generated at 2022-06-13 22:50:55.991708
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    from requests import Request, Session, adapters
    r = Request(method='GET', url='http://example.com/', auth=ExplicitNullAuth()).prepare()
    s = Session()
    s.mount('http://', adapters.HTTPAdapter())
    s.mount('https://', adapters.HTTPAdapter())
    s.send(r)



# Generated at 2022-06-13 22:50:57.347371
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    auth = ExplicitNullAuth()
    assert isinstance(auth, ExplicitNullAuth)

# Generated at 2022-06-13 22:50:57.885147
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    ExplicitNullAuth()

# Generated at 2022-06-13 22:51:01.250391
# Unit test for function get_content_type
def test_get_content_type():
    """
    Test if get_content_type works as intended
    """
    assert get_content_type('foobar') is None
    assert get_content_type('foobar.txt') == 'text/plain'
    assert get_content_type('foobar.txt.gz') == 'text/plain'
    assert get_content_type('foobar.txt.bzip2') == 'text/plain'
    assert get_content_type('foobar.json') == 'application/json'
    assert get_content_type('foobar.html') == 'text/html'



# Generated at 2022-06-13 22:51:12.173419
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

# Generated at 2022-06-13 22:51:24.207318
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.jpeg') == 'image/jpeg'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.bin') is None



# Generated at 2022-06-13 22:51:24.767680
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    assert ExplicitNullAuth()

# Generated at 2022-06-13 22:51:25.627732
# Unit test for function humanize_bytes
def test_humanize_bytes():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 22:51:29.492798
# Unit test for function repr_dict
def test_repr_dict():
    d = {"a": 1, "b": "b"}
    assert repr_dict(d) == "{'a': 1, 'b': 'b'}"

# Generated at 2022-06-13 22:51:37.182180
# Unit test for function repr_dict
def test_repr_dict():
    assert repr_dict({}) == "{}"
    assert repr_dict({'a': 1}) == "{'a': 1}"
    assert repr_dict({'a': 1, 'b': 2}) == "{'a': 1, 'b': 2}"
    assert repr_dict({
        'a': 1,
        'b': 2,
        'c': {
            'd': 3
        }
    }) == "{\n    'a': 1,\n    'b': 2,\n    'c': {\n        'd': 3\n    }\n}"

# Generated at 2022-06-13 22:51:39.668389
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'

# Generated at 2022-06-13 22:51:50.720631
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


# Generated at 2022-06-13 22:52:01.168077
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    from datetime import datetime
    import time


# Generated at 2022-06-13 22:52:02.777692
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type(__file__) == 'text/x-python'

# Generated at 2022-06-13 22:52:04.682143
# Unit test for method __call__ of class ExplicitNullAuth
def test_ExplicitNullAuth___call__():
    assert ExplicitNullAuth()({}) == {}

# Generated at 2022-06-13 22:52:24.705652
# Unit test for function get_content_type
def test_get_content_type():
    assert not get_content_type(None)
    assert not get_content_type('')
    assert get_content_type(__file__) == 'text/x-python'
    assert get_content_type('test.jpg') == 'image/jpeg'

# Generated at 2022-06-13 22:52:28.232202
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = '{"key2": "value2", "key1": "value1"}'
    d = {
        'key1': 'value1',
        'key2': 'value2'
    }
    assert load_json_preserve_order(s) == d

# Generated at 2022-06-13 22:52:29.087790
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    pass

# Generated at 2022-06-13 22:52:40.202121
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    assert get_expired_cookies([]) == []

    r1 = [
        ('Set-Cookie', f'{name}=value; max-age=30')
        for name in 'c1 c2 c3'.split()
    ]
    assert get_expired_cookies(r1, now=1000) == []
    assert get_expired_cookies(r1, now=2000) == []
    assert get_expired_cookies(r1, now=3000) == []
    assert get_expired_cookies(r1, now=4000) == [
        {'name': 'c1', 'path': '/'},
        {'name': 'c2', 'path': '/'},
        {'name': 'c3', 'path': '/'}
    ]


# Generated at 2022-06-13 22:52:43.376642
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = """{
    "a": 1,
    "b": 2,
    "c": 3
    }"""

    result = load_json_preserve_order(s)
    assert list(result.keys()) == ["a", "b", "c"]



# Generated at 2022-06-13 22:52:48.226170
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    s = '[{"a": 1, "b": 2}, {"c": 3}, {"d": 4}]'
    actual = load_json_preserve_order(s)
    expected = json.loads(s, object_pairs_hook=OrderedDict)
    assert actual == expected, "Failed to load JSON preserving order"

# Generated at 2022-06-13 22:52:56.114707
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('filename.jpg') == 'image/jpeg'
    assert get_content_type('filename.jpeg') == 'image/jpeg'
    assert get_content_type('filename.mp4') == 'video/mp4'
    assert get_content_type('filename.mp3') == 'audio/mpeg'
    assert get_content_type('filename.svg') == 'image/svg+xml'
    assert get_content_type('filename.txt') == 'text/plain'

# Generated at 2022-06-13 22:52:56.943974
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    ExplicitNullAuth()

# Generated at 2022-06-13 22:52:58.450233
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    Auth = ExplicitNullAuth()
    assert Auth

# Generated at 2022-06-13 22:53:00.270216
# Unit test for constructor of class ExplicitNullAuth
def test_ExplicitNullAuth():
    auth = ExplicitNullAuth()

# Generated at 2022-06-13 22:53:36.679658
# Unit test for function load_json_preserve_order
def test_load_json_preserve_order():
    import json
    print(json.dumps(load_json_preserve_order('{"a": 1}')))

test_load_json_preserve_order()

# Generated at 2022-06-13 22:53:52.593865
# Unit test for function humanize_bytes
def test_humanize_bytes():
    def hb(n, precision=2):
        return humanize_bytes(n, precision=precision)

    assert hb(1) == '1 B'
    assert hb(1, 1) == '1.0 B'
    assert hb(1024, 1) == '1.0 kB'
    assert hb(1024 * 123, 1) == '123.0 kB'
    assert hb(1024 * 12342, 1) == '12.1 MB'
    assert hb(1024 * 12342, 2) == '12.05 MB'
    assert hb(1024 * 1234, 2) == '1.21 MB'
    assert hb(1024 * 1234 * 1111, 2) == '1.31 GB'