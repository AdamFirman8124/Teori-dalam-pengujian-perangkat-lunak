

# Generated at 2022-06-13 22:43:48.180280
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/tmp/foo.txt') == 'text/plain'

# Generated at 2022-06-13 22:43:57.298873
# Unit test for function get_content_type
def test_get_content_type():
    """
    >>> get_content_type('/path/to/foo.js')
    'application/javascript'
    >>> get_content_type('/path/to/bar.html')
    'text/html'
    >>> get_content_type('/path/to/baz.json')
    'application/json'
    >>> get_content_type('/path/to/qux.txt')
    'text/plain'
    >>> get_content_type('/path/to/quux.unknown')

    """
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 22:44:06.764773
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('data.json') == 'application/json'
    assert get_content_type('data.jSon') == 'application/json'
    assert get_content_type('data.jSOn') == 'application/json'
    assert get_content_type('data.jSON') == 'application/json'
    assert get_content_type('data.js') in ('text/javascript', 'application/x-javascript')
    assert get_content_type('data.js.map') in ('text/javascript', 'application/x-javascript')
    assert get_content_type('data.jpg') == 'image/jpeg'
    assert get_content_type('data.JPG') == 'image/jpeg'
    assert get_content_type('data.JPg') == 'image/jpeg'
    assert get

# Generated at 2022-06-13 22:44:12.936952
# Unit test for function get_content_type
def test_get_content_type():
    def test_valid(filename, expected):
        content_type = get_content_type(filename)
        if content_type != expected:
            print(
                'FAIL: get_content_type("%s") '
                'returned "%s" instead of "%s"'
                % (filename, content_type, expected)
            )

    def test_invalid(filename):
        content_type = get_content_type(filename)
        if content_type is not None:
            print(
                'FAIL: get_content_type("%s") '
                'returned "%s" instead of None'
                % (filename, content_type)
            )

    test_valid("foo/bar", "text/x-generic-template")
    test_valid("foo/bar.html", "text/html")
    test

# Generated at 2022-06-13 22:44:16.784815
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('README.txt') == 'text/plain'
    assert get_content_type('index.html') == 'text/html'
    assert get_content_type('test.pdf') == 'application/pdf'

# Generated at 2022-06-13 22:44:28.587817
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    import datetime
    now = datetime.datetime.utcnow().timestamp()
    headers = [
        # A malformed header
        ('Set-cookie', 'a=b c=d'),
        # A header with a token
        ('Set-cookie', 'a=b'),
        # A header with a quoted-string
        ('Set-cookie', 'b="c"'),
        # A header with a cookie that expires
        ('Set-cookie', 'd=e; Expires=Fri, 30 Mar 2018 14:12:21 GMT'),
        # A header with a cookie that expires with max-age
        ('Set-cookie', 'e=f; Max-Age=2'),
    ]
    expired_cookies = get_expired_cookies(headers=headers, now=now)
    assert len(expired_cookies) == 2

# Generated at 2022-06-13 22:44:32.962638
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.html') == 'text/html'
    assert get_content_type('test.gif') == 'image/gif'
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test') is None

# Generated at 2022-06-13 22:44:44.481479
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.json') == 'application/json'
    assert get_content_type('foo.pdf') == 'application/pdf'
    assert get_content_type('foo.jpeg') == 'image/jpeg'
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.jpe') == 'image/jpeg'
    assert get_content_type('foo.jfif') == 'image/jpeg'
    assert get_content_type('foo.jfif-tbnl') == 'image/jpeg'
    assert get_content_type('foo.jpx') == 'image/jpx'

# Generated at 2022-06-13 22:44:54.064857
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    now = time.time()
    cookie_header = 'k1=v1; Expires={0}; k2=v2; Expires={1}; Max-Age=500; k3=v3; k4=v4'.format(
        now, now
    )
    assert get_expired_cookies([('Set-Cookie', cookie_header)], now - 1) == []
    assert get_expired_cookies([('Set-Cookie', cookie_header)], now + 1) == [{'name': 'k2', 'path': '/'}]
    assert get_expired_cookies([('Set-Cookie', cookie_header)], now + 501) == [{'name': 'k3', 'path': '/'},
                                                                               {'name': 'k4', 'path': '/'}]

# Generated at 2022-06-13 22:45:04.629712
# Unit test for function get_expired_cookies
def test_get_expired_cookies():
    # Time of reference:
    #   2016-05-12T20:06:20.076594
    now = 1463070380

    assert get_expired_cookies([
        ('Set-Cookie', 'session_id=session-id-value'),
        ('Set-Cookie', 'path=/; expires=Sat, 14-May-2016 20:06:20 GMT;'),
        ('Set-Cookie', 'path=/; max-age=0;'),
        ('Set-Cookie', 'path=/; max-age=3600;'),
    ], now=now) == [
        {'name': 'session_id', 'path': '/'},
        {'name': 'path', 'path': '/'},
    ]


# Generated at 2022-06-13 22:45:13.234133
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('some.jpg') == 'image/jpeg'
    assert get_content_type('some.jpeg') == 'image/jpeg'
    assert get_content_type('some.mp3') == 'audio/mpeg'
    assert get_content_type('some.gif') == 'image/gif'
    assert get_content_type('some.css') == 'text/css'
    assert get_content_type('some.html') == 'text/html'
    assert get_content_type('some.js') == 'text/javascript'
    assert get_content_type('some.png') == 'image/png'
    assert get_content_type('some.mov') == 'video/quicktime'
    assert get_content_type('some.mp4') == 'video/mp4'
   

# Generated at 2022-06-13 22:45:19.546786
# Unit test for function get_content_type
def test_get_content_type():
    """
    >>> get_content_type('foo.txt')
    'text/plain'
    >>> get_content_type('version.json')
    'application/json'
    >>> get_content_type('nope.nope') is None
    True

    """
    pass

__test__ = {
    'test_get_content_type': test_get_content_type,
}

# Generated at 2022-06-13 22:45:25.792549
# Unit test for function get_content_type
def test_get_content_type():
    # normal use
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.PNG') == 'image/png'
    # maybe it's an ISO-8859-1
    assert get_content_type('foo.iso-8859-1') == 'application/octet-stream'

# Generated at 2022-06-13 22:45:28.838963
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.bin') == 'application/octet-stream'

# Generated at 2022-06-13 22:45:32.649862
# Unit test for function get_content_type
def test_get_content_type():
    assert(get_content_type("filename.txt") == "text/plain")
    assert(get_content_type("filename.jpeg") == "image/jpeg")


# Generated at 2022-06-13 22:45:42.599087
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('') is None
    assert get_content_type('.') is None
    assert get_content_type('foo') is None
    assert get_content_type('foo.bar') is None
    assert get_content_type('foo.baz') is None
    assert get_content_type('foo.baz.txt') == 'text/plain'
    assert get_content_type('foo.baz.bin') is None
    assert get_content_type('foo.baz.bin.txt') == 'text/plain'
    assert get_content_type('foo.baz.txt.bin') == 'application/octet-stream'



# Generated at 2022-06-13 22:45:50.636666
# Unit test for function get_content_type
def test_get_content_type():

    # If a filename doesn't exist, get_content_type returns None
    assert get_content_type('./does not exist.txt') is None

    # Test some extensions that the mimetypes library doesn't know about
    assert get_content_type('__init__.py') == 'text/x-python'
    assert get_content_type('requirements.txt') == 'text/plain'

    # Test some extensions that the mimetypes does know about
    assert get_content_type('releases.yml') == 'text/x-yaml'
    assert get_content_type('index.html') == 'text/html'

# Generated at 2022-06-13 22:45:54.927367
# Unit test for function get_content_type
def test_get_content_type():
    assert 'text/html' == get_content_type('index.html')
    assert 'audio/mpeg' == get_content_type('foo.mp3')
    assert 'application/vnd.ms-word.document' == get_content_type('foo.doc')

# Generated at 2022-06-13 22:45:58.360777
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.not_real') == None

# Generated at 2022-06-13 22:46:08.156548
# Unit test for function get_content_type
def test_get_content_type():
    from . import get_content_type
    assert get_content_type("abc.pdf") == "application/pdf"
    assert get_content_type("abc.png") == "image/png"
    assert get_content_type("abc.jpg") == "image/jpeg"
    assert get_content_type("abc.jpeg") == "image/jpeg"
    assert get_content_type("abc.gif") == "image/gif"
    assert get_content_type("abc.txt") == "text/plain"
    assert get_content_type("abc.csv") == "text/csv"
    assert get_content_type("abc.html") == "text/html"
    assert get_content_type("abc.xhtml") == "text/html"

# Generated at 2022-06-13 22:46:15.686131
# Unit test for function get_content_type
def test_get_content_type():
    test_data = [
        ('test.xml', 'application/xml'),
        ('test-utf-8.txt', 'text/plain; charset=utf-8'),
        ('foo.gif', 'image/gif'),
        ('index.html', 'text/html'),
        ('index.htm', 'text/html'),
        ('index', None),
        ('test-missing-extension', None),
    ]
    for filename, content_type in test_data:
        assert get_content_type(filename) == content_type

# Generated at 2022-06-13 22:46:27.439524
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('abc') is None
    assert get_content_type('abc.txt') == 'text/plain'
    assert get_content_type('path/to/image.gif') == 'image/gif'
    assert get_content_type('path/to/image.jpeg') == 'image/jpeg'
    assert get_content_type('path/to/image.png') == 'image/png'
    assert get_content_type('path/to/pdf.pdf') == 'application/pdf'
    assert get_content_type('path/to/pdf.PDF') == 'application/pdf'
    assert get_content_type('path/to/pdf.Pdf') == 'application/pdf'
    assert get_content_type('path/to/zip.zip') == 'application/zip'
    assert get

# Generated at 2022-06-13 22:46:35.685328
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('a.txt') == 'text/plain'
    assert get_content_type('a.html') == 'text/html'
    assert get_content_type('a.css') == 'text/css'
    assert get_content_type('a.js') == 'application/javascript'
    assert get_content_type('a.json') == 'application/json'
    assert get_content_type('a.nonexistent_extension') is None

# Generated at 2022-06-13 22:46:41.905820
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.bmp') == 'image/bmp'
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.json') == 'application/json'

# Generated at 2022-06-13 22:46:50.734614
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('README.txt') == 'text/plain'
    assert get_content_type('README.html') == 'text/html'
    assert get_content_type('pic.gif') == 'image/gif'
    assert get_content_type('some.xml') == 'application/xml'
    assert get_content_type('some.yaml') == 'text/x-yaml'
    assert get_content_type('some.yml') == 'text/x-yaml'
    assert get_content_type('some.json') == 'application/json'
    assert get_content_type('some.js') == 'application/javascript'
    assert get_content_type('some.unknown') is None


# Generated at 2022-06-13 22:46:53.232448
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo') is None

# Generated at 2022-06-13 22:47:03.531182
# Unit test for function get_content_type
def test_get_content_type():
    from .src.httpbin import filename

    def test_get_content_type_impl(filename):
        content_type = get_content_type(filename)
        print('%s => "%s"' % (filename, content_type))

    test_get_content_type_impl('httpbin/static/image.png')
    test_get_content_type_impl('httpbin/static/random.jpg')
    test_get_content_type_impl('httpbin/static/image.svg')
    test_get_content_type_impl('httpbin/static/image.gif')
    test_get_content_type_impl('httpbin/static/image.jpg')
    test_get_content_type_impl('httpbin/static/random.pdf')

# Generated at 2022-06-13 22:47:11.269415
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.htm') == 'text/html'
    assert get_content_type('foo.png') == 'image/png'
    assert get_content_type('foo.jpg') == 'image/jpeg'
    assert get_content_type('foo.jar') == 'application/java-archive'

# Generated at 2022-06-13 22:47:18.103354
# Unit test for function get_content_type
def test_get_content_type():
    content_type = get_content_type('file.txt')
    assert content_type == 'text/plain'
    content_type = get_content_type('/home/file.txt')
    assert content_type == 'text/plain'
    content_type = get_content_type('file.pdf')
    assert content_type == 'application/pdf'
    content_type = get_content_type('file.bin')
    assert content_type == 'application/octet-stream'
    content_type = get_content_type('file.dv')
    assert content_type == 'video/dv'

# Generated at 2022-06-13 22:47:28.678257
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.html') == 'text/html'
    assert get_content_type('test.js') == 'application/javascript'
    assert get_content_type('test.py') == 'text/x-python'
    assert get_content_type('test.css') == 'text/css'
    assert get_content_type('test.java') == 'text/x-java-source'
    assert get_content_type('test.cpp') == 'text/x-c++src'
    assert get_content_type('test.cc') == 'text/x-c++src'
    assert get_content_type('test.c') == 'text/x-csrc'

# Generated at 2022-06-13 22:47:36.427424
# Unit test for function get_content_type
def test_get_content_type():
    import unittest
    from tempfile import NamedTemporaryFile

    # noinspection PyUnusedLocal
    class GetContentTypeTest(unittest.TestCase):
        def test_get_content_type_filename(self):
            f = NamedTemporaryFile(suffix='.bin')
            content_type = get_content_type(f.name)
            self.assertEqual(content_type, 'application/octet-stream')
            f.close()

        def test_get_content_type_filename_extension(self):
            f = NamedTemporaryFile(suffix='.bin')
            content_type = get_content_type(f.name + '.zip')
            self.assertEqual(content_type, 'application/zip')
            f.close()


# Generated at 2022-06-13 22:47:40.231834
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('hello.txt') == \
        'text/plain'
    assert get_content_type('hello.html') == \
        'text/html'
    assert get_content_type('hello.jpg') == \
        'image/jpeg'

# Generated at 2022-06-13 22:47:45.112378
# Unit test for function get_content_type
def test_get_content_type():
    """
    Unit tests for get_content_type
    """

    assert get_content_type('application/json') == 'application/json'
    assert get_content_type('application/json; charset=utf-8') == 'application/json; charset=utf-8'

# Generated at 2022-06-13 22:47:55.639281
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('README.rst') == 'text/x-rst'
    assert get_content_type('CHANGES.rst') == 'text/x-rst'
    assert get_content_type('LICENSE.rst') == 'text/x-rst'
    assert get_content_type('setup.cfg') == 'text/plain'
    assert get_content_type('setup.py') == 'text/x-python'
    assert get_content_type('tests.py') == 'text/x-python'
    assert get_content_type('Makefile') == 'text/x-makefile'
    assert get_content_type('test_helpers.py') == 'text/x-python'

# Generated at 2022-06-13 22:47:57.531402
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type(__file__) == 'text/x-python'

# Generated at 2022-06-13 22:48:06.432161
# Unit test for function get_content_type
def test_get_content_type():
    tests = []
    tests.append(('foo', 'text/plain'))
    tests.append(('foo.txt', 'text/plain'))
    tests.append(('foo.html', 'text/html'))
    tests.append(('foo.xhtml', 'application/xhtml+xml'))
    tests.append(('foo.js', 'application/javascript'))
    tests.append(('foo.json', 'application/json'))
    tests.append(('foo.css', 'text/css'))
    tests.append(('foo.pdf', 'application/pdf'))
    tests.append(('foo.xml', 'application/xml'))
    tests.append(('foo.svg', 'image/svg+xml'))

# Generated at 2022-06-13 22:48:09.575033
# Unit test for function get_content_type
def test_get_content_type():
    assert(get_content_type('example.pdf') == 'application/pdf')
    assert(get_content_type('example.jpg') == 'image/jpeg')


# Generated at 2022-06-13 22:48:20.126421
# Unit test for function get_content_type
def test_get_content_type():
    test_cases = (
        ('', None),
        ('a', None),
        ('a.txt', 'text/plain'),
        ('a/b', None),
        ('a/b.txt', 'text/plain'),
        ('a/b/c.txt', 'text/plain'),
        ('c.text/plain', None),
        ('d.json', 'application/json'),
        ('.hidden', None),
        ('.hidden.txt', 'text/plain'),
        ('.hidden/a.txt', 'text/plain'),
        ('a.txt.bmp', 'image/x-bmp'),
        # (u'a.txt.bmp', 'image/x-bmp'),
    )
    for x, y in test_cases:
        assert get_content_type(x) == y

# Generated at 2022-06-13 22:48:31.237128
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('app.css') == 'text/css'
    assert get_content_type('app.js') == 'application/javascript'
    assert get_content_type('text.txt') == 'text/plain'
    assert get_content_type('image.gif') == 'image/gif'
    assert get_content_type('image.jpg') == 'image/jpeg'
    assert get_content_type('image.png') == 'image/png'
    assert get_content_type('image.webp') == 'image/webp'
    assert get_content_type('text.properties') == 'text/x-java-properties'
    assert get_content_type('app.xml') == 'application/xml'
    assert get_content_type('app.json') == 'application/json'

# Generated at 2022-06-13 22:48:38.228683
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('/tmp/foo.txt') == 'text/plain'
    assert get_content_type('/tmp/foo.TXT') == 'text/plain'
    assert get_content_type('/tmp/foo.tar') == 'application/x-tar'
    assert get_content_type('/tmp/foo') is None
    assert get_content_type('/tmp/foo.z') is None

# Generated at 2022-06-13 22:48:48.414382
# Unit test for function get_content_type
def test_get_content_type():
    """
    Calling ``get_content_type()`` with a filename should return the
    appropriate content type in the format ``'text/plain; charset=UTF-8'``, or
    ``None`` if the file type is unknown.

    """
    type_by_filename = {
        'README.txt': 'text/plain; charset=iso-8859-1',
        'index.html': 'text/html; charset=UTF-8',
        'test.pdf': 'application/pdf',
    }
    for filename, content_type in type_by_filename.items():
        assert get_content_type(filename) == content_type

# Generated at 2022-06-13 22:48:57.624336
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('index.html') == 'text/html'
    assert get_content_type('images.gif') == 'image/gif'
    assert get_content_type('images.jpeg') == 'image/jpeg'
    assert get_content_type('images.svg') == 'image/svg+xml'
    assert get_content_type('images.svgz') == 'image/svg+xml'
    assert get_content_type('images.svgz', strict=True) is None

# Generated at 2022-06-13 22:49:01.976127
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.txt') == 'text/plain'
    assert get_content_type('foo.html') == 'text/html'
    assert get_content_type('foo.json') == 'application/json'
    assert get_content_type('foo.unknown') is None

# Generated at 2022-06-13 22:49:05.621400
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('filename') is None
    assert get_content_type('filename.html') == 'text/html'
    assert get_content_type('filename.css') == 'text/css'
    assert get_content_type('filename.js') == 'application/javascript'



# Generated at 2022-06-13 22:49:11.710965
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.txt') is None
    assert get_content_type('test.pdf') == 'application/pdf'
    assert get_content_type('test.docx') == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'


# Generated at 2022-06-13 22:49:21.000720
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test.a.txt') == 'text/plain'
    assert get_content_type('test.a.jsonl') == 'application/x-jsonlines'
    assert get_content_type('test.a.json') == 'application/json'
    assert get_content_type('test.a.png') == 'image/png'
    assert get_content_type('test.a.jpg') == 'image/jpeg'
    assert get_content_type('test.a.jpeg') == 'image/jpeg'
    assert get_content_type('test.a.tif') == 'image/tiff'
    assert get_content_type('test.a.tiff') == 'image/tiff'
    assert get_content_type('test.a.gif') == 'image/gif'


# Generated at 2022-06-13 22:49:23.107319
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('foo.html') == 'text/html'

# Generated at 2022-06-13 22:49:24.449635
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type(filename='for_test') is None



# Generated at 2022-06-13 22:49:30.111533
# Unit test for function get_content_type
def test_get_content_type():
    assert get_content_type('test/test.html') == 'text/html'
    assert get_content_type('test/test.xhtml') == 'application/xhtml+xml'
    assert get_content_type('test/test.png') == 'image/png'
    assert get_content_type('test/test.xlsx') == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    assert get_content_type('test/test.jpg') == 'image/jpeg'

# Generated at 2022-06-13 22:49:37.019576
# Unit test for function get_content_type
def test_get_content_type():
    # pylint: disable=missing-function-docstring
    assert get_content_type('test.txt') == 'text/plain'
    assert get_content_type('test.svg') is None
    assert get_content_type('test.svg') is None
    assert get_content_type('test.svgz') == \
        'image/svg+xml'
    assert get_content_type('test.sVg') == \
        'image/svg+xml'
    assert get_content_type('test.svg+xml') is None
