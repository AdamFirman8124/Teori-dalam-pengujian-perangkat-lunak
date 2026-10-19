

# Generated at 2022-06-14 15:48:41.210381
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    Run a unit test on method 'real_download' of class 'HtttFD'.
    """
    import functools
    
    # Set up logging
    ydl_opts = {
        'logger': MyLogger(),
    }
    
    # Create and configure an instance of class HttpFD
    hd = HttpFD(ydl_opts)
    hd.params = {
        'continuedl': False,
        'noresizebuffer': False,
        'retries': 2,
        'test': True,
        'xattr_set_filesize': False,
    }
    hd.report_error = functools.partial(MyLogger.error, hd.params['logger'])

# Generated at 2022-06-14 15:48:52.322839
# Unit test for constructor of class HttpFD

# Generated at 2022-06-14 15:49:05.421542
# Unit test for method real_download of class HttpFD

# Generated at 2022-06-14 15:49:16.027305
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import tempfile
    import shutil

    class TestFD(HttpFD):

        def _hook_progress(self, status):
            print(status)

        def report_error(self, msg):
            print(msg, file=sys.stderr)

        def to_screen(self, msg):
            print(msg, end='')

        def to_stderr(self, msg):
            print(msg, file=sys.stderr, end='')

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 15:49:20.166619
# Unit test for constructor of class HttpFD
def test_HttpFD():
    h = HttpFD('http://localhost', {'test': 'foobar'})
    (test, a, b) = pickle.loads(pickle.dumps(h))
    assert test == 'foobar'



# Generated at 2022-06-14 15:49:28.466991
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    fd = HttpFD({
            'nooverwrites': True,
            'continuedl': False,
            'noprogress': True,
            'quiet': True,
        })
    # fd.real_download('http://example.org/', 'test_file', {})
    fd.real_download('http://www.youtube.com/watch?v=3tBZ9O8zWL0&feature=youtube_gdata_player', 'test_file', {})
test_HttpFD_real_download()


# Generated at 2022-06-14 15:49:38.604318
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .extractor import get_info_extractor
    from .downloader import HttpFD

    class MyHttpFD(HttpFD):
        def __init__(self, ydl, params):
            super(MyHttpFD, self).__init__(ydl, params)
            self.count = 0

        def slow_down(self, start_time, now, byte_counter):
            super(MyHttpFD, self).slow_down(start_time, now, byte_counter)
            self.count += 1

        def best_block_size(self, elapsed_time, downloaded_bytes):
            return super(MyHttpFD, self).best_block_size(elapsed_time, downloaded_bytes)


# Generated at 2022-06-14 15:49:51.322742
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .utils import encode_compat_str

    # Test case 1: read from string
    test1_str = "A string"
    test1_fd = HttpFD(test1_str)
    assert(test1_fd.total_bytes == len(test1_str))
    read_str = test1_fd.read(1)
    assert(read_str == "A")
    test1_fd.seek(2)
    assert(test1_fd.read() == "string")

    # Test case 2: read from a list of strings
    test2_list = ["A string", " and", " another one."]
    test2_fd = HttpFD(test2_list)
    assert(test2_fd.total_bytes == sum(len(str) for str in test2_list))
    read_

# Generated at 2022-06-14 15:50:02.169524
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    cmd = [sys.executable, '-m', 'youtube_dl.downloader.http', '-i', '--no-progress', '--noplaylist', '-r', '2k', '--max-filesize', '1m', '-a', '-']
    url = 'https://www.openssl.org/source/openssl-1.0.1g.tar.gz'
    # Expected output:
    # [download] Destination: -
    # [download]   5.6% of ~1.0M at   1.0K/s ETA 00:01
    # [download]   9.4% of ~1.0M at   2.0K/s ETA 00:01
    # [download]  11.7% of ~1.0M at   3.0K/s ETA

# Generated at 2022-06-14 15:50:09.739632
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    HttpFD().params['simulate'] = True
    HttpFD().params['nooverwrites'] = True
    HttpFD().params['verbose'] = True
    HttpFD().params['retries'] = 1
    HttpFD().params['continuedl'] = False
    HttpFD().params['noresizebuffer'] = True
    HttpFD().params['test'] = True
    HttpFD().params['playlistend'] = 1
    HttpFD().params['outtmpl'] = '%(id)s.%(ext)s'
    HttpFD().params['noprogress'] = True
    HttpFD().params['format'] = 'all'
    HttpFD().params['listformats'] = False
    HttpFD().params['keepvideo'] = False



# Generated at 2022-06-14 15:50:53.705700
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from io import BytesIO

    def _fake_urlopen_handler():
        """Returns request handler for _fake_urlopen."""
        good_chunks = set(range(1025))
        chunk = None

        def _fake_urlopen(req):
            nonlocal chunk
            data_len = req.headers.get('Content-length')
            chunk = int(req.headers.get('Youtube-DL-Test-Chunk', '0'))
            if data_len is not None:
                assert int(data_len) == _TEST_FILE_SIZE
            if chunk not in good_chunks:
                raise compat_urllib_error.HTTPError(
                    req.get_full_url(), 416, 'Test', None, None)

# Generated at 2022-06-14 15:51:04.056837
# Unit test for constructor of class HttpFD
def test_HttpFD():
    class TestException(Exception):
        pass

    # Scenario 1: Successful single download without chunks
    ctx = DownloadContext(1, TestException, TestException, 'http://www.example.org/foo', 0)
    with open(encodeFilename('%(tmpfilename)s'), 'wb') as f:
        def test_urlopen(request):
            return _FakeUrlopen(f, {'Content-Length': '10'})
        fd = HttpFD(ctx, {}, test_urlopen)
        assert fd._open() is True
        assert fd.mode == 'wb'
        assert fd.name == '-1'
        assert fd.basename == encodeFilename(ctx.tmpfilename)
        assert fd.size == 10
        assert fd.tell() == 0

# Generated at 2022-06-14 15:51:13.559764
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    Testing real_download method of class HttpFD
    """
    import os
    import shutil
    import tempfile

    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl.utils import encodeFilename


    # Test downloader, progress handler and temporary files generator

    # This is an InfoExtractor for testing only, which simulates an HTTP server
    class TestIE(InfoExtractor):
        def _real_extract(self, url):
            # Allow setting URL query string and info properties
            url, smuggled_data = unsmuggle_url(url, {})
            query = compat_parse_qs(compat_urllib_parse_urlparse(url).query)
            info = {}

# Generated at 2022-06-14 15:51:26.547156
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class FakeYDL(object):
        def __init__(self, result_file):
            self.result_file = result_file
            self.probe_result = {
                'format': {
                    'url': 'http://server.com/file',
                },
            }

        def get_filename(self, info_dict):
            # pylint: disable=no-self-use
            return 'file'

        def urlopen(self, request):
            # pylint: disable=no-self-use
            assert request.type == 'http'
            url = request.get_full_url()
            assert url.startswith('http://server.com/file')
            assert len(request.headers) == 1  # User-Agent
            content_range = request.headers.get('Range')

# Generated at 2022-06-14 15:51:34.687334
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import io
    import gzip
    import shutil
    import tempfile
    from contextlib import contextmanager

    import pytest

    from ..utils import sanitize_open
    from ..utils import encodeFilename

    @contextmanager
    def _fake_stream(name, content):
        with io.BytesIO() as stream:
            stream.name = name
            stream.write(content)
            stream.flush()
            stream.seek(0)
            yield stream


# Generated at 2022-06-14 15:51:45.740042
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    from .utils import _html_search_meta
    from .compat import compat_urlretrieve

    class FakeYDL():
        'FakeYDL'

        def __init__(self):
            self.params = {
                'continuedl': True,
                'nooverwrites': True,
                'retries': 10,
                'test': True,
                'sleep_interval': 1,
                'usenetrc': False,
                'username': None,
                'password': None,
                'quiet': True,
                'forcetitle': False,
                'forceurl': False,
                'forcethumbnail': False,
                'forcedescription': False,
                'simulate': False,
                'skip_download': False,
                'format': None,
            }
            self

# Generated at 2022-06-14 15:51:57.750366
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import shutil
    import tempfile
    tmpdir = tempfile.mkdtemp()
    tmpextract = os.path.join(tmpdir, '%(id)s-%(ext)s')
    tmppart = os.path.join(tmpdir, '%(id)s-%(ext)s.part')
    tmptemplate = os.path.join(tmpdir, '%(id)s-%(ext)s.%%(partnum)s')

# Generated at 2022-06-14 15:52:10.304179
# Unit test for constructor of class HttpFD
def test_HttpFD():
    http_fd = HttpFD('http://example.com', {})
    # Incorrect URL
    assert not http_fd.real_download('ftp://bad.scheme.in.url', None)
    # Non-existent URL
    assert not http_fd.real_download('http://example.com/404', None)
    # Existent URL
    assert http_fd.real_download('http://example.com/200', None)
    # None as URL
    assert not http_fd.real_download(None, None)
    # Empty URL
    assert not http_fd.real_download('', None)
    # Bad test in _real_extract_url
    assert not http_fd.real_download('http://example.com/200', {'test': 'bad_test'})
    # Incorrect test in _real

# Generated at 2022-06-14 15:52:19.929910
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def _test_download(params):
        params = dict(params)
        chunk_size = params.pop('testchunkbyte')
        downloader = HttpFD(params, {})
        fd = downloader.retrieve({'url': 'https://www.youtube.com/watch?v=BaW_jenozKc',
                                  'player_url': 'https://www.youtube.com/watch?v=BaW_jenozKc',
                                  'player_url_basename': 'BaW_jenozKc',
                                  'test': True,
                                  'outtmpl': '-'})
        assert fd is not None
        while 1:
            d = fd.read(chunk_size)
            if d == b'':
                break
            print(d)
        fd.close()

# Generated at 2022-06-14 15:52:30.968274
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os

    test_url = 'http://techslides.com/demos/sample-videos/small.mp4'
    test_dst = 'small.mp4'

    def _test_download_file(ydl, dst, expected_size):
        ydl.params.update(dict(noprogress=True, quiet=True, verbose=False, nopart=True, forceurl=True, forcetitle=True, forceid=True, simulate=True))
        ydl._setup_opener()
        ydl.to_screen = lambda *args, **kargs: None
        ydl.report_error = lambda *args, **kargs: None

        mtime = None
        ydl.try_utime = lambda filename, filetime: filetime


# Generated at 2022-06-14 15:54:05.391937
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ydl = get_test_downloader()
    ydl.params['nooverwrites'] = True
    b = '0'
    try:
        fd = (ydl, 'http://localhost/%s' % b, b, 'wb')
        HttpFD(fd)
    finally:
        del ydl.params['nooverwrites']
    # These should all raise an exception
    fd = (ydl, 'http://localhost/%s' % b, 'bad', 'wb')
    assert((fd, None, b, 'wb') not in ydl._fd_cache.keys())
    assert_raises(AssertionError, HttpFD, fd)
    fd = (ydl, 'http://localhost/%s' % b, b, 'rb')

# Generated at 2022-06-14 15:54:17.243886
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test setup
    import os
    from youtube_dl.utils import encodeFilename, sanitize_open
    fd = HttpFD(
        {'test': True},
        'http://127.0.0.1:0/',
        {
            'url': 'http://127.0.0.1:0/',
        },
        'http://127.0.0.1:0/'
    )

    # Downloading file (byte_counter < data_len)
    res = fd.real_download(test_file_size=10)
    assert res == True
    assert os.path.isfile(encodeFilename(fd.tmpfilename))
    os.remove(encodeFilename(fd.tmpfilename))

    # Downloading file (byte_counter == data_len)
    res = fd.real

# Generated at 2022-06-14 15:54:26.002484
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Unit test for method real_download of class HttpFD
    stream = open(os.path.join(os.path.dirname(__file__), 'test.mp4'), 'rb')
    stream.seek(0, 2)
    stream_len = stream.tell()
    stream.seek(0, 0)

    class MockYtdl(object):
        def __init__(self):
            self.params = {'buffersize': 8192, 'noresizebuffer': False}

        def to_screen(self, *_):
            pass

        def to_stderr(self, *_):
            pass

        @staticmethod
        def urlopen(req):
            class MockResponse(object):
                def __init__(self, headers):
                    self.headers = headers

                def info(self):
                    return

# Generated at 2022-06-14 15:54:38.330629
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor import gen_extractors
    from .YoutubeDL import YoutubeDL
    from .compat import compat_tempfile
    from .utils import encode_data_uri

    def test_case(
            filename, size, is_test,
            start_len, end_len,
            expected_result,
            start_opt, end_opt,
            chunk_size, block_size,
            extractor_key=None, extractor_name=None, expected_status=None,
            expected_chunk_count=None, expected_data_len=None,
            max_filesize=None, min_filesize=None):

        def check_result(filename, result, data_len, status):
            def _read(filename):
                with open(encodeFilename(filename), 'rb') as f:
                    return f

# Generated at 2022-06-14 15:54:42.715611
# Unit test for constructor of class HttpFD
def test_HttpFD():
    assert isinstance(HttpFD({}, {'noprogress': True}, {}), HttpFD)
    assert isinstance(HttpFD({'noprogress': True}, {}, {}), HttpFD)
    assert isinstance(HttpFD({'noprogress': True}, {'noprogress': True}, {}), HttpFD)
    assert isinstance(HttpFD({}, {'logger': True}, {}), HttpFD)

# TODO: write unit tests for methods of class HttpFD
# See: http://stackoverflow.com/questions/18367631/python-how-to-test-private-methods-and-non-public-members

# Unit tests for methods of class WgetDownloader

# Generated at 2022-06-14 15:54:50.755231
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Preparation
    from io import BytesIO
    from urllib.parse import urlparse, parse_qs
    class DummyURLopener:

        def __init__(self, test_file_contents, test_headers):
            self.test_file_contents = test_file_contents
            self.test_headers = test_headers
            self.url_calls = []

        def open(self, url, data=None):

            class Result:

                def __init__(self, test_contents, test_headers):
                    self.test_contents = test_contents
                    self.test_headers = test_headers
                    self.read_calls = []
                    self.readline_calls = []

                def read(self, size=-1):
                    self.read_calls.append(size)

# Generated at 2022-06-14 15:55:01.781629
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test_transient_error():
        def test_retry(test_instance, transient_error, retries):
            url_data, url_headers, url_url, url_content_type = ('', {}, '', '')

            def urlopen(request):
                return MockHttp(url_data, url_headers, url_url, url_content_type)

            def hook(d):
                pass


# Generated at 2022-06-14 15:55:13.875434
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Make sure the test is run from the current directory
    try:
        testFile = '%s/%s' % (os.getcwd(), URL_TEST)
        open(testFile, 'rb')
    except:
        print('WARNING: Unit test for method real_download of class HttpFD needs file %s in current directory' % URL_TEST)
        return True
    t = HttpFD()
    assert t.real_download(URL_TEST, None, {'infoname': 'test'}, None)
    assert t.real_download(URL_TEST, None, {'infoname': 'test'}, 'test-test')
    assert t.real_download(URL_TEST, None, {'infoname': 'test'}, 'test-test', True)
    t.ydl.params

# Generated at 2022-06-14 15:55:19.717473
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Since we need to test stdout and stderr, we cannot inherit from
    # unittest.TestCase, but we need to manually pack the test method into a
    # TestCase instance and pass it to a TestSuite

    class Test(object):
        @staticmethod
        def _make_result(out, err):
            class Result(object):
                def __init__(self, out, err):
                    self.stdout = StringIO(out)
                    self.stderr = StringIO(err)
            return Result(out, err)

        @staticmethod
        def _check_result(out, err):
            # Just one simple test for now, download a small file
            Test.assertEqual(err.count('\r[youtube]'), 1)

# Generated at 2022-06-14 15:55:32.606276
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .compat import compat_http_server
    from .compat import compat_urllib_request

    class ThreadingServer(compat_http_server.ThreadingHTTPServer, object):
        allow_reuse_address = True
    class Handler(compat_http_server.BaseHTTPRequestHandler):
        server_version='A.B'
        sys_version='C'

        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'video/mp4')
            self.send_header('Content-length', '9176530')
            self.send_header('Content-range', 'bytes 0-9176529/9176530')
            self.send_header('Accept-Ranges', 'bytes')