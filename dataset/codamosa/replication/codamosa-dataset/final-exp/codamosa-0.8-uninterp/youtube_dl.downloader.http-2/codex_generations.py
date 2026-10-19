

# Generated at 2022-06-14 15:48:41.096829
# Unit test for constructor of class HttpFD
def test_HttpFD():
    meta = {'tmpfilename': 'tmp'}
    http_fd = HttpFD(meta, dl=None, params={})
    filename = http_fd.prepare_filename(meta)
    assert filename == meta['tmpfilename']

    meta = {'tmpfilename': '-'}
    http_fd = HttpFD(meta, dl=None, params={})
    filename = http_fd.prepare_filename(meta)
    assert filename == 'tmp'

    meta = {'tmpfilename': 'tmp', 'outtmpl': '%(id)s'}
    http_fd = HttpFD(meta, dl=None, params={})
    filename = http_fd.prepare_filename(meta)
    assert filename == 'tmp'


# Generated at 2022-06-14 15:48:52.244523
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    from .utils import make_HTTPServer
    from .YoutubeDL import YoutubeDL

    DEBUG = False

    # Run a dummy HTTP server on localhost:9000
    from .tests import test_server

    TESTSERVER_PORT = 9000
    try:
        req_handler = make_HTTPServer(TESTSERVER_PORT, test_server.BaseRequestHandler)
        test_server.TestServerThread(req_handler).start()
        # Wait some time for the server to start
        time.sleep(1)
    except socket.error as e:
        if e.errno != errno.EADDRINUSE:
            raise


# Generated at 2022-06-14 15:49:01.137937
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class FakeYtdl(object):
        def __init__(self, params):
            self.params = params

        def to_screen(self, msg):
            pass

        def to_stdout(self, msg):
            pass

        def to_stderr(self, msg):
            pass

        def urlopen(self, request):
            if request.headers.get('Range') is not None:
                response = compat_urllib_request.addinfourl(
                    compat_StringIO('abcdefhijklmnopqrstuvwxyz'),
                    compat_httplib.HTTPMessage(),
                    request.get_full_url()
                )
                response.code = 416
                response.msg = 'Requested Range Not Satisfiable'

# Generated at 2022-06-14 15:49:13.341223
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # This is not a complete unit test, just a simple test for filename sanitization
    # First, make a utf-8 filename
    utf8_filename = os.fsdecode(b'\xf0\x9f\x8d\xba.txt')
    if sys.platform == 'win32':
        # Juggle the filename to make it invalid on Windows
        utf8_filename = utf8_filename.encode('utf-8').decode('utf-16-le')
    # Instantiate the class
    h = HttpFD(DummyYDL(), {}, {})
    # Set the filename
    h.tmpfilename = utf8_filename
    # Call the method with the problematic filename

# Generated at 2022-06-14 15:49:22.523205
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .utils import encodeArgument
    from .extractor import gen_extractors
    from .YoutubeDL import YoutubeDL

    fd = HttpFD(YoutubeDL(gen_extractors()), {'noprogress': True}, {}, {'url': encodeArgument('http://127.0.0.1:1/')})
    try:
        assert fd.read(5) == 0
    except compat_urllib_error.URLError as e:
        assert 'timed out' in str(e)
    fd.close()



# Generated at 2022-06-14 15:49:32.009770
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class TestHttpFD(HttpFD):
        def __init__(self, params, info_dict):
            self.to_screen_strs = []
            self.to_stderr_strs = []

        def to_screen(self, s):
            self.to_screen_strs.append(s)

        def to_stderr(self, s):
            self.to_stderr_strs.append(s)

        def report_error(self, s):
            self.to_stderr(s)

        def report_destination(self, s):
            self.to_screen(s)

        def report_retry(self, s, *args):
            self.to_stderr(s % args)

        def report_resuming_byte(self, s):
            self.to

# Generated at 2022-06-14 15:49:44.299883
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test HttpFD as it were a StringIO
    h = HttpFD(dummy_progress_hooks, None, 'test', 0)
    h.write('abc')
    h.write('def')
    h.reset()
    h.write('123')
    assert h.tell() == 3
    h.seek(0)
    assert h.read() == '123'
    h.seek(1)
    assert h.read() == '23'
    h.seek(0)
    assert h.read(1) == '1'
    assert h.read(2) == '23'
    h.seek(0)
    assert h.readline() == '123'
    assert h.readline() == ''
    h.close()



# Generated at 2022-06-14 15:49:56.092496
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test():
        print("Test started")
        class FakeLogger(object):
            def __getattr__(self, attr):
                return lambda x: None
        def urlopen(req):
            class FakeResponse(object):
                def __init__(self, headers):
                    self.headers = headers
                def info(self):
                    return self.headers
                def read(self, size):
                    return '1' * size
            class FakeRequest(object):
                def __init__(self, headers):
                    self.headers = headers
                def info(self):
                    return self.headers
            if req.headers.get('Range', None) is not None:
                return FakeResponse({'Content-Range': 'bytes 1000-1999/2000'})
            else:
                return FakeRequest({'Content-Length': '1000'})

# Generated at 2022-06-14 15:50:05.944106
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def _assert_called_times(mock, expected_times, msg=None):
        if mock.call_count != expected_times:
            args = (mock.call_args_list, expected_times, mock.call_count)
            raise ValueError(msg or 'call_args_list=%s, num_expected=%s, num_actual=%s' % args)

    def _make_mock_file(tmpfilename, mode='wb', size=None):
        file_mock = mock.MagicMock(wraps=io.BytesIO())
        file_mock.name = tmpfilename
        if mode == 'wb':
            if size is None:
                file_mock.write.side_effect = lambda buf: file_mock.seek(len(buf), io.SEEK_CUR)

# Generated at 2022-06-14 15:50:15.768599
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import shutil
    import tempfile
    import time
    from youtube_dl.utils import encodeFilename
    from youtube_dl.compat import urllib_request

    # Test HTTP Error 416 (Requested Range Not Satisfiable)
    # See https://github.com/rg3/youtube-dl/issues/6198
    def test_http_416(url):
        tempdir = tempfile.mkdtemp(prefix='youtubedl_test_')
        filename = '-o' + encodeFilename(os.path.join(tempdir, '%(extractor)s-%(id)s-%(title)s.%(ext)s'))

        def params_cb(ydl, new_params):
            assert 'outtmpl' not in new_params
            new_params['outtmpl'] = filename
            return new

# Generated at 2022-06-14 15:51:00.302464
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    Test the real_download method of HttpFD by downloading a specified url
    just a small piece of it and verifying that the downloaded content is correct.
    """

    # The url and the content of the small piece to be downloaded
    url = 'http://md5.jsontest.com/?text=example_text'
    content = """{
    "md5": "1b65aae6d7260b78a8415b4f4b81e423"
}"""

    # Prepare the download directory, HttpFD object, and the expected filename

# Generated at 2022-06-14 15:51:04.143450
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ctx = HttpFD(params={'continuedl': True, 'nooverwrites': True})
    fd = ctx.open('http://127.0.0.1/')
    fd.close()


# Generated at 2022-06-14 15:51:13.624327
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class FakeHttpFD(HttpFD):
        def __init__(self, params, won_resume=True):
            self.params = params
            self.won_resume = won_resume
            self.log = []

        def to_screen(self, s):
            self.log.append(s)

        def report_error(self, s):
            self.log.append(s)

        def report_retry(self, source_error, attempt_number, attempt_limit):
            self.log.append((source_error, attempt_number, attempt_limit))

        def report_file_already_downloaded(self, file_name):
            self.log.append(file_name)

        def report_unable_to_resume(self):
            self.log.append(None)


# Generated at 2022-06-14 15:51:26.596453
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():  # pragma: no cover
    import threading
    import time
    import math

    DEFAULT_BLOCK_SIZE = 1024 * 8

    def test(expected_range_start, expected_range_end, chunk_size, data_len,
             has_range, range_start, range_end,
             block_size, data_block_len, expected_byte_counter, expected_block_size):
        global count
        global server_response

        def check_request_headers(_, data):
            global count
            global server_response
            lines = data.splitlines()
            head = lines[0].split(None, 2)

# Generated at 2022-06-14 15:51:34.711233
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .utils import PreparedHttpRequest

    def test_urlopen(request):
        from .extractor import get_info_extractor
        from .extractor.common import InfoExtractor
        class FakeExtractor(InfoExtractor):
            IE_NAME = 'fake'

        req = PreparedHttpRequest(request)
        ie = get_info_extractor(FakeExtractor.IE_NAME)

        # Make sure that the prepared HTTP request has the same headers as the given request
        for header_name, header_value in request.headers.items():
            assert req.http_headers[header_name] == header_value

        return compat_urllib_request.urlopen(req)

    def test_writeln(line):
        pass

    def test_to_screen(msg):
        pass


# Generated at 2022-06-14 15:51:36.623748
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Needs to be run in a new process because of pycurl
    fd = FileDownloader({})
    try:
        fd.http_fd
    except Exception as e:
        print(e)


# Generated at 2022-06-14 15:51:46.594386
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """This function tests the real_download method of class HttpFD."""

    # The test needs the mock_server.py script
    data_server = subprocess.Popen(
        [sys.executable, '-u', os.path.join(os.path.dirname(__file__), 'mock_server.py'), '--mime-type=video/webm', '--content-length=102400'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True)

    # We need to read the mock server's address
    server_address_re = re.compile('HTTP server listening on (\S+)', flags=re.IGNORECASE)
    for x in data_server.stdout:
        m = server_address_re.match

# Generated at 2022-06-14 15:51:58.024385
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import tempfile
    import random
    import string
    random_filename = ''.join(random.choice(string.ascii_letters) for _ in range(16))
    random_data = b''

# Generated at 2022-06-14 15:52:10.588294
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test parameters
    test_file_size = 1024 * 1024  # 1 MiB
    test_url = 'http://127.0.0.1/%iB' % test_file_size
    tmp_filename = 'test.tmp'
    try:
        os.remove(tmp_filename)  # If tmp_filename already exists, remove it
    except OSError:
        pass
    progress_hooks = []  # Log of what _hook_progress() has been called with
    def _hook_progress(status):
        progress_hooks.append(status)
    class YDL:
        params = {
            'buffersize': '16384',
            'noresizebuffer': False,
            'test': True,
        }
        def toScreen(self, *args, **kargs):
            pass  #

# Generated at 2022-06-14 15:52:20.087727
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    The unit test uses the following URLs and files (named similarly to the URLs):
    https://github.com/ytdl-org/youtube-dl/raw/master/test/test.mp4
    https://github.com/ytdl-org/youtube-dl/raw/master/test/test%20with%20spaces.mp4
    https://github.com/ytdl-org/youtube-dl/raw/master/README.md
    https://httpbin.org/bytes/61
    https://httpbin.org/bytes/62
    https://httpbin.org/bytes/63
    https://httpbin.org/bytes/64
    """


# Generated at 2022-06-14 15:53:51.739185
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import io
    import random
    import sys
    import threading
    import time

    # Create mock socket
    class MockSocket(io.BytesIO):
        def __init__(self, *args, **kwargs):
            self.bufsize = kwargs.pop('bufsize', 16384)
            io.BytesIO.__init__(self, *args, **kwargs)
            self._wlock = threading.Lock()
            self.timeout = 0.5
            self.count = 0

        def read(self, n=-1):
            time.sleep(0.01)
            with self._wlock:
                self.count += 1
                data = io.BytesIO.read(self, n if n >= 0 else self.bufsize)
                return data


# Generated at 2022-06-14 15:54:04.024187
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Create a temporary file that is not going to be in use by anyone.
    (handle, tmpfile) = tempfile.mkstemp(prefix='test_youtube-dl_', suffix='.tmp')
    os.close(handle)
    os.remove(tmpfile)
    assert not os.path.exists(tmpfile)
    write = lambda s: open(tmpfile, 'wb').write(s)
    # We will use a temporary HTTPD as a test server
    tmpd = tempfile.mkdtemp(prefix='test_youtube-dl_')
    tmpurl = 'http://127.0.0.1:55545/'
    PORT = 55545

    class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
        """Main class to present webpages and authentication."""

# Generated at 2022-06-14 15:54:16.142497
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import http.client
    import re
    import subprocess
    import sys
    import urllib.error
    import urllib.request
    import tempfile
    import time
    import unittest

    class DummyYDL(object):
        def __init__(self, params):
            self.params = params
            self.to_screen_lock = threading.Lock()

        def to_screen(self, s):
            with self.to_screen_lock:
                sys.stderr.write(s + '\n')
                sys.stderr.flush()

        @staticmethod
        def trouble(s, tb=None):
            raise Exception(s)

        @staticmethod
        def urlopen(req):
            return urllib.request.urlopen(req)


# Generated at 2022-06-14 15:54:25.307859
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test for headers
    fd = HttpFD('http://www.google.com')
    assert fd.headers == {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
    }, fd.headers
    fd = HttpFD('http://www.google.com', {
        'test': 'value',
        'range': 'bytes=0-10',
    })
    assert fd.headers

# Generated at 2022-06-14 15:54:37.735289
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Download first chunk of a file
    ctx = DownloadContext('http://example.com/file')
    ctx.tmpfilename = 'file'
    ctx.open_mode = 'wb'
    ctx.chunk_size = 5
    def _real_download_hook(dic):
        assert 'status' in dic
        if dic['status'] == 'downloading':
            assert dic['filename'] == 'file'
            assert dic['tmpfilename'] == 'file'
            assert dc['downloaded_bytes'] == 0
            assert dc['total_bytes'] == None
            assert dic['eta'] == None
            assert dic['speed'] == 0
            assert dic['elapsed'] > 0
        elif dic['status'] == 'finished':
            assert dic['filename'] == 'file'

# Generated at 2022-06-14 15:54:47.329527
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import StringIO
    test_buf = StringIO("videoplayback" * 1000)
    info = {
        'url': 'http://example.com/video.mp4',
        'title': 'video',
        'id': 'videoid'
    }
    fd = HttpFD(test_buf, info)
    assert fd.len == len(test_buf.getvalue())
    assert fd.info().get('title') == 'video.mp4'
    assert fd.name.split('.')[-1] == 'mp4'
    assert fd.geturl() == 'http://example.com/video.mp4'
    assert fd.read(5) == 'video'
    assert fd.read(1000) == 'playback' * 1000
    fd.seek(0)

# Generated at 2022-06-14 15:54:57.888106
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    downloader = FakeDownloader()
    downloader.params.update({
        'continuedl': True,
        'nooverwrites': True,
        'retries': 3,
        'test': True,
    })
    info_dict = {
        'id': 'test',
        'url': 'http://127.0.0.1:8080/%s' % (os.path.basename(__file__)),
        'title': 'test',
        'ext': 'mp4',
        'format': 'fake',
        'player_url': None,
        'http_headers': {},
    }
    filename = sanitize_filename('test.mp4')
    tmpfilename = downloader.temp_name(filename)
    test_file = io.BytesIO(b'abcdefghijkl')

# Generated at 2022-06-14 15:55:10.651457
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # run real_download with small test file
    http_fd = HttpFD('', {})
    ctx = http_fd.ctx
    ctx.data_len = 10240
    ctx.block_size = 1024
    ctx.chunk_size = 1024
    ctx.filename = '-'
    ctx.tmpfilename = '-'
    ctx.open_mode = 'wb'
    ctx.data = compat_urllib_request.urlopen('https://github.com/rg3/youtube-dl/raw/master/test.sh')
    assert http_fd.real_download(is_test=True)
    ctx.stream.seek(0)

# Generated at 2022-06-14 15:55:19.688402
# Unit test for constructor of class HttpFD
def test_HttpFD():
    h = HttpFD()
    assert h._dispatch == {
        'idle': h._idle_state,
        'download': h._download_state,
    }
    assert h.state == 'idle'

# Generated at 2022-06-14 15:55:32.606173
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Constructor
    h = HttpFD(None, {}, None)
    # Test format_bytes()
    assert h.format_bytes(2) == '2.0 KiB'
    assert h.format_bytes(2 ** 10) == '1.0 MiB'
    assert h.format_bytes(2 ** 20) == '1.0 GiB'
    assert h.format_bytes(2 ** 30) == '1.0 TiB'
    # Test calc_percent()
    assert h.calc_percent(100, 1000) == '10.0%'
    # Test calc_eta()
    assert h.calc_eta(0, 10, 1000, 100) == '9.0 seconds'
    assert h.calc_eta(0, 60, 1000, 100) == '54.0 seconds'
    assert h