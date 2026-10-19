

# Generated at 2022-06-14 15:48:30.577905
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    return 'TODO'

# Generated at 2022-06-14 15:48:41.768813
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test mode
    http_fd = HttpFD(Extractor(), FakeYDL())
    # Local test file
    http_fd.params['test'] = 1
    http_fd.params['continuedl'] = True
    # We can not use os.urandom() to generate a test file, because the file may contain \x00 bytes which will make curl fail
    http_fd.report_destination('http-test.bin')
    with open('http-test.bin', 'wb') as test_f:
        test_f.write(b'abcde')
    test_f.close()
    # Inject test urls
    http_fd._test_urls(['http://127.0.0.1:8080/http-test.bin'])
    # Run test

# Generated at 2022-06-14 15:48:44.431638
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Old-style class, so super() doesn't work
    HttpFD(FakeYDL())



# Generated at 2022-06-14 15:48:53.846516
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    (ctx, _, _) = sanitize_open('-', 'wb')
    data_len = 1000000
    s = fd_prepare_test(ctx, data_len)
    hfd = HttpFD(ctx.ydl, ctx)
    # Tests that block_size is adjusted correctly
    assert hfd.real_download(
        {'url': 'http://127.0.0.1:80000/', 'filename': '-', 'resume_len': 0, 'data_len': data_len, 'noprogress': True, 'test': True, 'retries': 0})
    assert s.getvalue() == ''.join([chr(i % 256) for i in xrange(data_len)])
    s.close()
    # Tests that download does not repeat if Content-length is unknown

# Generated at 2022-06-14 15:49:01.230836
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .compat import StringIO

    def fake_urlopen(request, *args, **kwargs):
        if request.get_full_url() == 'http://example.com/err':
            raise compat_urllib_error.HTTPError(request.get_full_url(), 404, 'Not Found', {}, None)
        if request.get_full_url() == 'http://example.com/ranges_not_supported':
            return StringIO('Ranges not supported')
        if request.get_full_url() == 'http://example.com/file':
            return StringIO(''.join(['%0.20f' % random.random() for _ in range(_TEST_FILE_SIZE)]))
        raise NotImplementedError('unhandled url %r' % request.get_full_url())


# Generated at 2022-06-14 15:49:11.622289
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    for i in range(3):
        assert HttpFD._TEST_FILE_SIZE == HttpFD(None, None)._TEST_FILE_SIZE
    if sys.version_info >= (3, 0, 0):
        assert HttpFD._TEST_FILE_SIZE == 100
    else:
        assert HttpFD._TEST_FILE_SIZE == 30
    # For some reason, PythonTestCase doesn't work with the first of these two classes (HttpFD)
    return True
# Test that the unit test passes
test_HttpFD_real_download()

# Create a subclass of HttpFD with an overriden report_Error method

# Generated at 2022-06-14 15:49:24.281077
# Unit test for constructor of class HttpFD
def test_HttpFD():
    h = HttpFD(None, {'noprogress': True}, None)
    h.to_screen('\n')
    h.to_stderr('\n')
    h.report_error('\n')
    h.report_retry('\n', 1, 2)
    h.report_resuming_byte(1)
    h.report_unable_to_resume()
    h.report_destination('\n')
    h.report_progress(1, 2)
    h.report_finish(1, 2)
    h.report_finish_err('\n')
    h.report_file_already_downloaded('\n')


# Class used to measure download speed (useful for rate-limiting).

# Generated at 2022-06-14 15:49:26.708644
# Unit test for constructor of class HttpFD
def test_HttpFD():
    url = 'http://localhost/'
    http_fd = HttpFD(url, {'noprogress': True}, {'http_chunk_size': 5})
    http_fd.close()

if __name__ == '__main__':
    _setup_opener()
    test_HttpFD()

# Generated at 2022-06-14 15:49:34.534282
# Unit test for constructor of class HttpFD
def test_HttpFD():
    class FakeYDL(object):
        params = {
            'nooverwrites': True,
            'continuedl': False,
            'noprogress': True,
            'logger': True,
            'test': True,
        }
        def __init__(self):
            self.to_screen_lock = threading.Lock()

        def to_screen(self, s):
            with self.to_screen_lock:
                sys.stderr.write(s)
                sys.stderr.flush()

        def trouble(self, *args, **kargs):
            pass

        def urlopen(self, *args, **kargs):
            return compat_urllib_request.urlopen(*args, **kargs)


# Generated at 2022-06-14 15:49:48.156906
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test module
    fd = HttpFD('http://example/')
    assert fd._urlhandle is None
    assert fd.filename == 'http://example/'
    assert fd.real_download is True
    assert fd.started is False
    assert fd.status()['basename'] == 'example'
    # Test download
    fd = HttpFD('http://www.google.com', {'nooverwrites': 'True'})
    assert fd.real_download is True
    fd = HttpFD('http://www.google.com', {'noprogress': 'True'})
    assert fd.real_download is True
    fd = HttpFD('http://www.google.com', {'continuedl': 'True'})

# Generated at 2022-06-14 15:50:29.221621
# Unit test for constructor of class HttpFD

# Generated at 2022-06-14 15:50:32.052098
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Just creating a HttpFD instance
    fd = HttpFD(
        'http://example.com/video.mp4',
        {
            'noprogress': True,
            'logger': YoutubeDLLogger(),
        })


# Generated at 2022-06-14 15:50:37.670768
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import BytesIO
    import sys
    import types
    import warnings

    def _run_test(params):
        content = 'this is a test and only a test'
        content_size = len(content)
        check_size = content_size
        if 'test_not_readable' in params:
            assert 'test_not_seekable' in params
            assert not params['test_not_readable']
        elif 'test_not_seekable' in params:
            assert not params['test_not_seekable']
            assert params.get('test_size', True)
        else:
            assert params.get('test_size', True)
            check_size = None
        if params.get('test_incomplete_read', False):
            assert params['test_incomplete_read'] > 0
            assert params

# Generated at 2022-06-14 15:50:49.752624
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ydl = getDownloader()
    d = HttpFD(ydl, {})
    d.add_info_extractor(FakeIE())
    d.params['usenetrc'] = False
    d.params['username'] = None
    d.params['password'] = None
    d.params['videopassword'] = None
    d.params['ap_username'] = None
    d.params['ap_password'] = None
    d.params['noprogress'] = True
    d.params['forcetitle'] = True
    d.params['forceurl'] = True
    d.params['forcethumbnail'] = True
    d.params['forcedescription'] = True
    d.params['simulate'] = True
    d.params['format'] = '22'

# Generated at 2022-06-14 15:51:01.350703
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def open_file(filename, mode):
        fd = open(filename, mode)
        fd.write(data)
        fd.close()

    data = 'abcdefghij'
    filename = '%s.test' % __name__

# Generated at 2022-06-14 15:51:02.242600
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    pass

# Generated at 2022-06-14 15:51:12.568572
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    LOG_FILE = 'test_HttpFD_real_download.log'
    LOG_LEVEL = 'DEBUG'
    TEST_VIDEO_URL = 'https://test.test/test.test'

    # ytdl main test object

# Generated at 2022-06-14 15:51:25.715197
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    # Create a temporary test file
    data = b'testtesttesttest'
    fd = tempfile.NamedTemporaryFile(mode='wb', delete=False)
    fd.write(data)
    fd.close()

    # Run real_download unit test with the test file
    class TestYDL(object):
        params = {}
        def __init__(self):
            self.to_screen = lambda *args, **kargs: None
            self.to_stderr = lambda *args, **kargs: None
        def report_error(self, *args, **kargs):
            raise Exception('%r %r' % (args, kargs))
        def slow_down(self, *args, **kargs): pass
        def best_block_size(self, *args, **kargs): return 1000


# Generated at 2022-06-14 15:51:34.233447
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor.common import InfoExtractor
    from .extractor import gen_extractors
    # Create an InfoExtractor object
    ies = gen_extractors() + [InfoExtractor(u'none')]
    ie = ies[0]

    # Create an TDownloader object
    ydl = object.__new__(youtube_dl.YoutubeDL)
    ydl.params = {}
    ydl.cache = None
    ydl.to_stderr = lambda *args: None
    ydl.to_screen = lambda *args: None
    ydl.report_warning = lambda *args: None
    ydl.report_error = lambda *args: None
    ydl.report_file_already_downloaded = lambda *args: None
    ydl.DownloadError = youtube_dl.DownloadError

# Generated at 2022-06-14 15:51:43.676457
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('Test HttpFD:')
    # open
    f = HttpFD(
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        {'https_proxy': 'http://127.0.0.1:8118'},
        'open'
    )
    # read
    buf = f.read(1)
    buf += f.read(1)
    buf += f.read(1)
    buf += f.read(1)
    print(buf)
    # close
    f.close()

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:52:52.841243
# Unit test for constructor of class HttpFD
def test_HttpFD():
    try:
        import urllib2
        u = urllib2
    except ImportError:
        import urllib.request as u
    # Play with HTTP FD
    fd = HttpFD(u.urlopen('http://www.google.com'), 100, 60)
    assert fd.read(10) == b'<!doctype '
    time.sleep(1.1)
    assert fd.read(10) == b''
    time.sleep(0.4)
    assert fd.read(10) == b'html><head'
    time.sleep(3)
    assert fd.read(10) == b'><meta cha'
    fd.close()
    print('Test passed.')



# Generated at 2022-06-14 15:53:03.291891
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import BytesIO
    from urllib.parse import parse_qs, urlparse
    from youtube_dl.extractor import gen_extractors
    import http.client
    body = 'This is a test'
    urlh = compat_urllib_request.Request('http://127.0.0.1/')
    urlh.add_header('Content-Type', 'text/plain')
    urlh.add_header('Content-Length', str(len(body)))
    urlh.add_header('Content-Disposition', 'attachment; filename=test.txt')
    urlh.add_header('Set-Cookie', 'foo=bar; max-age=3600')
    urlh.add_header('x-test', 'yes')

    conn = urlh.get_host()

# Generated at 2022-06-14 15:53:14.191901
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL(dict(nooverwrites=True, quiet=True))
    ydl.add_progress_hook(null_progress_hook)
    output = os.path.join(os.environ['TEST_OUTDIR'], 'output')
    FD = HttpFD(ydl, {}, output)
    assert FD.prepare_filename(output) == os.path.join(output, 'output')
    assert FD.prepare_filename(output) == os.path.join(output, 'output-1')
    FD.params['continuedl'] = True
    assert FD.prepare_filename(output) == os.path.join(output, 'output-2')
    filename = os.path.join(output, 'output-3')

# Generated at 2022-06-14 15:53:22.906654
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    Unit test for method real_download of class HttpFD
    """
    def _mock_reporthook(dummy, progress):
        """
        Mock of the reporthook method
        """
        return
    # TIMEOUT ERROR

# Generated at 2022-06-14 15:53:27.461073
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # TODO: implement
    pass

# class FragmentFD(HttpFD)
# This is a subclass of HttpFD used by FileDownloader to download fragments.


# Generated at 2022-06-14 15:53:36.198769
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import threading
    import socket
    socket.socket = compat_socket_socket
    threading.Thread = compat_threading_Thread
    # To get same behaviour on python 2 and 3
    class MockLogger(object):
        def debug(self, msg):
            pass
        def warning(self, msg):
            pass
    fake_ydl = FakeYDL()
    fd = HttpFD(fake_ydl, dict(noprogress=True, quiet=True))
    from .extractor import gen_extractors
    fd.gen_extractors = lambda info_dict: gen_extractors()
    fd.params['logger'] = MockLogger()
    fd.params.update({
        'ratelimit': 0,
        'noresizebuffer': True,
    })
    # Test HTTP

# Generated at 2022-06-14 15:53:41.705161
# Unit test for constructor of class HttpFD
def test_HttpFD():
    if sys.version_info >= (3, 0):
        test_result = subprocess.call([sys.executable, '-c', 'from __main__ import HttpFD'])
    else:
        test_result = subprocess.call([sys.executable, '-c', 'from __main__ import HttpFD'])
    if test_result != 0:
        sys.exit(1)

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:53:51.811227
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import http.server
    import socketserver
    from youtube_dl.compat import urlparse
    from youtube_dl.utils import encodeFilename, sanitize_open, get_filesize

    if sys.version_info < (3, 0, 0):
        raise ValueError('Python 3.0+ required')

    BDV = {}  # BiDirectional dict Values

    class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_HEAD(self):
            (scheme, netloc, path, params, query, fragment) = urlparse.urlparse(self.path)
            self.send_response(200)
            if path.endswith('/'):
                self.send_header('Content-type', 'text/plain')

# Generated at 2022-06-14 15:54:04.135897
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # We are testing internal method `real_download` of class
    # `youtube_dl.FileDownloader.HttpFD` with mocked `_hook_progress` method
    # and `best_block_size` method (which is static method and returns a
    # constant value).  The test is performed on file
    # `test/data/url/t.bin` which is the hexdump of string "t" and has
    # length of 1 byte.  We assume that first byte of the file is
    # downloaded in the first loop iteration.

    # Set block size for adjustment
    BLOCK_SIZE = 2**14

    # Set test file size
    TEST_FILE_SIZE = 1

    # Set test chunk size
    TEST_CHUNK_SIZE = 0

    # Set test fragment range
    TEST_FRAGMENT_START = 0
    TEST

# Generated at 2022-06-14 15:54:16.230391
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test setup
    class DummyYDL:
        def __init__(self, params):
            self.params = params
        def to_screen(self, message):
            self._screen_message = message
        def report_error(self, message):
            self._error_message = message
    from .extractor import gen_extractors
    params = {
        'outtmpl': 'video',
        'quiet': True,
        'noprogress': True,
    }
    # Test with non-existing URL
    ydl = DummyYDL(params)
    ydl.postprocessors = []
    fd = HttpFD(ydl, params)
    fd.test = True

# Generated at 2022-06-14 15:57:01.111589
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # a dict of all needed parameters of the
    # test for the real_download method
    params = {
        'url': 'http://ipv4.download.thinkbroadband.com/5MB.zip',
        # 'url': 'http://ipv4.download.thinkbroadband.com/1GB.zip',
        'retries': 10,
        'chunk_limit': 10,
        'nooverwrites': True,
    }
    # instanciate a test object
    test_obj = HttpFD()
    # method real_download needs this attribute
    test_obj.params = params
    # calling real_download method with the
    # specified test parameters
    ret = test_obj._do_download(params, True)
    print('return value of real_download: %s' % ret)


# Generated at 2022-06-14 15:57:08.932609
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import tempfile
    import urllib.request

    # test data
    data = 'this is a test'
    data_len = len(data)
    headers = {
        'Content-Type': 'video/mp4',
        'Content-Length': data_len,
    }

    # run http server
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = os.path.join(tempdir, 't.mp4')
        with open(test_file, 'wb') as fp:
            fp.write(data)

        httpd = HTTPServer(
            ('127.0.0.1', 0),
            SimpleHTTPRequestHandler,
            bind_and_activate=False,
        )
        httpd.socket.settimeout(3)
        httpd.allow_reuse_address

# Generated at 2022-06-14 15:57:19.593324
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ydl = YoutubeDL()
    ydl.params['prefer_insecure'] = False
    # First test: file downloading test
    # Create test file in test directory
    f = open('test1.tmp', 'w')
    f.write('first test')
    f.close()
    # Download it
    http_fd = HttpFD(ydl, {}, 'http://localhost:23131/test1.tmp', 'test1.txt', {}, None)
    assert http_fd.real_download(test=True)
    # Check if the file has been downloaded
    f = open('test1.txt', 'r')
    info = f.read()
    f.close()
    assert info == 'first test'
    # Test incomplete download
    # Create another test file in test directory

# Generated at 2022-06-14 15:57:26.410517
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    Unit test for method real_download of class HttpFD.

    TODO: make it more generic, so it can be used with any downloader object
    (not just specific to HttpFD)
    """
    # Imports
    import os.path
    #from youtube_dl.YoutubeDL import YoutubeDL
    import downloader

    class TestDownloader(downloader.HttpFD):
        # HTML of response (as plain string or bytes)
        TEST_DATA = b'This is a test.  And only a test.'

        # Size of response
        TEST_DATA_SIZE = len(TEST_DATA)

        # HTTP headers of response

# Generated at 2022-06-14 15:57:35.974679
# Unit test for method real_download of class HttpFD

# Generated at 2022-06-14 15:57:46.853823
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def _test_write():
        fd.write(b'blah')

    fd = HttpFD('dummyurl', 'dummyfilename', {'noprogress': True}, query={'arg': 'val'})
    assert fd.url == 'dummyurl?arg=val'
    assert fd.dummy == 'dummyfilename'
    assert fd.progressive is False

    _test_write()
    fd = HttpFD('url', 'fn', {}, None, False, lambda x: 'b' + x)
    assert fd.url == 'burl'
    assert isinstance(fd.data, compat_HTTPError)
    assert fd.data.code == 416
    assert not fd.progressive

    if sys.version_info >= (2, 6):
        _test_write

# Generated at 2022-06-14 15:57:49.491460
# Unit test for constructor of class HttpFD
def test_HttpFD():
    t = HttpFD('', {}, 0, 0)
    assert t.len == 0
    assert t.downloaded == 0
    assert t.pp is None
    assert t.n == 'http_headers'
    assert t.buf == ''
    assert t.data is None



# Generated at 2022-06-14 15:57:57.108037
# Unit test for constructor of class HttpFD
def test_HttpFD():
    file_desc = HttpFD(
        sanitized_Request('http://example.com/'),
        {'format': 'flv'},
        1000,
        0)
    assert file_desc == 'http://example.com/'
    assert file_desc.basename == 'example.com'
    assert file_desc.format == 'flv'
    for attr in ('filesize', 'continued_dl', 'tries'):
        assert getattr(file_desc, attr) == 1000

    res = sys.modules['__main__'].__dict__['res']
    win32 = sys.modules['__main__'].__dict__['win32']
    atexit = sys.modules['__main__'].__dict__['atexit']
    if res == 0:
        assert file_desc.next_number