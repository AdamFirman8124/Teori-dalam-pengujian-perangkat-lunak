

# Generated at 2022-06-14 15:48:36.391383
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def check_d(d, expected_url, expected_resume_len, expected_open_mode):
        assert d.url == expected_url, 'url must be "%s"' % expected_url
        assert d.resume_len == expected_resume_len and d.open_mode == expected_open_mode, 'open_mode must be "%s" and resume_len must be %d' % (expected_open_mode, expected_resume_len)

    d = HttpFD('http://test.com/test.flv', 8324, 'wb')
    check_d(d, 'http://test.com/test.flv', 8324, 'wb')

    d = HttpFD('http://test.com/test.flv', 8324, 'ab')

# Generated at 2022-06-14 15:48:43.189361
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Create an object
    http_fd = HttpFD()

    # Create a fake environment for running the constructor
    fake_info = {'url': 'http://example.com'}

    # Run the constructor
    http_fd.real_initialize(fake_info)

    # Verify that the pointer to the info dictionary is stored properly
    assert http_fd.info == fake_info


# Generated at 2022-06-14 15:48:53.190756
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # In this test, the server will at first return a file of size 1MB
    # with a 200 HTTP status code and then an error with code 404.

    class TestServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            return

        def do_GET(self):
            global test_server_running
            self.send_response(200 if test_server_running else 404)
            self.end_headers()
            test_server_running = False
            self.wfile.write(b'\0' * 1048576)

    def serve_forever():
        server = HTTPServer(('localhost', 0), TestServerHandler)
        global test_server_url
        test_server_url = 'http://localhost:' + str(server.server_port) + '/'
       

# Generated at 2022-06-14 15:49:01.207970
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test_real_download(self, info_dict, filename, info_dict_str, data_len=None, best_block_size=1024 * 1024,
                           resumable=False, test_num=1):

        def _test_real_download_call(self, info_dict, filename, info_dict_str):
            real_download(self, info_dict, filename, info_dict_str)

        def _test_real_download_get_response(self, blocksize=16 * 1024):
            return _test_real_download_response(self, blocksize, resumable, data_len)

        self.to_screen = lambda *args, **kwargs: None
        self.to_stderr = lambda *args, **kwargs: None
        self.report_error = lambda msg: None

# Generated at 2022-06-14 15:49:07.271694
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Basic test
    obj = HttpFD(
        'http://www.google.com/',
        {'progress_hooks': [lambda d: None], 'max_filesize': 2000000},
        'google.htm')
    obj.download()

    # Test small max_filesize
    obj = HttpFD(
        'http://www.google.com/',
        {'progress_hooks': [lambda d: None], 'max_filesize': 100},
        'google.htm')
    try:
        obj.download()
    except MaxDownloadSizeExceeded:
        pass

    # Test big max_filesize

# Generated at 2022-06-14 15:49:17.012350
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # string describing (sub)set of errors that may happen during a successful test run
    # (and should be suppressed)
    expected_errors = [
        'unable to open for writing: [Errno 13] Permission denied',
        'unable to write data: [Errno 28] No space left on device',
    ]

    class TestBaseFD(BaseFD):
        # Fake methods
        def __init__(self, ydl, params, info_dict):
            self.tmpfilename = '-'
            self.filename = '-'
            self.http_headers = {}
        def _build_reply(self, ctx):
            return {}
        def _report_destination(self, filename):
            return

# Generated at 2022-06-14 15:49:29.039303
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import tempfile
    import shutil
    import sys
    import os.path

    try:
        os.environ.pop('http_proxy')
    except KeyError:
        pass

    temp_dir = tempfile.mkdtemp()
    filename = os.path.join(temp_dir, 'ydl_test')
    test_url = 'http://127.0.0.1:9230/dummyvideo.mp4'

    params = {
        'writedescription': False,
        'writeinfojson': False,
        'skip_download': True,
    }

    with youtube_dl.YoutubeDL(params) as ydl:
        ydl.add_default_info_extractors()

        if sys.version_info < (3, 0):
            from SocketServer import BaseServer

# Generated at 2022-06-14 15:49:39.779518
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .compat import stdout
    from .downloader import FileDownloader
    from .extractor import get_info_extractor

    class Dummy:
        pass

    class DummyIE(Dummy, InfoExtractor):
        pass

    ie = DummyIE(FileDownloader())

    # Test with test URL
    dl = HttpFD(ie, {}, DOWNLOADER_VERSION, DOWNLOAD_RETRIES)
    dl.add_info_extractor(get_info_extractor('YoutubeIE', ie))
    dl.params['continuedl'] = False
    dl.report_destination = dl.report_progress = lambda *x: None
    dl.to_screen = lambda *x: None
    dl.to_stderr = lambda *x: None

# Generated at 2022-06-14 15:49:52.395100
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # This test unit tests the real_download method of HttpFD(FileDownloader)
    # by downloading some test videos.
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    ydl.add_default_info_extractors()

# Generated at 2022-06-14 15:50:03.105513
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import shutil
    import tempfile
    import threading
    import time

    class FakeHeadRequestHandler(compat_http_server.BaseHTTPRequestHandler):
        def do_HEAD(self):
            self.send_response(200)
            self.send_header('Content-Length', self._content_length)
            self.send_header('Last-Modified', self._last_modified)
            self.end_headers()

            if hasattr(self, '_delay'):
                time.sleep(self._delay)

        def log_message(self, format, *args):
            # Override logging that spams sys.stderr
            return

    class FakeGetRequestHandler(FakeHeadRequestHandler):
        def do_GET(self):
            self.send_response(200)

# Generated at 2022-06-14 15:50:46.680961
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # setup
    ydl = FakeYDL()
    fd = HttpFD(ydl)
    fd.params['noprogress'] = True
    fd.params['retries'] = 10
    fd.params['test'] = True
    fd.report_error('hey')
    from . import YoutubeDLHandler
    fd.ydl_handler = YoutubeDLHandler()
    fd.ydl_handler.setFormatter(logging.Formatter())

# Generated at 2022-06-14 15:50:58.982989
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import socket
    import threading
    import time
    test_running = [True]

    class LocalHTTPServer(threading.Thread):
        def __init__(self):
            self.port = 0
            threading.Thread.__init__(self)

        def run(self):
            self.httpd = None
            for i in range(5):
                try:
                    self.httpd = SocketServer.TCPServer(
                        ('127.0.0.1', 0), HttpRequestHandler)
                    break
                except socket.error:
                    if i == 4:
                        raise
                    time.sleep(2)
            self.port = self.httpd.socket.getsockname()[1]
            while test_running[0]:
                self.httpd.handle_request()


# Generated at 2022-06-14 15:51:09.988389
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    hfd = FakeYDL()
    hfd.params['nooverwrites'] = True
    hfd.to_screen = lambda _: None
    hfd.to_stderr = lambda _: None
    hfd.report_error = lambda _: None
    hfd.report_retry = lambda *args: None
    hfd.report_destination = lambda _: None
    hfd.report_resuming_byte = lambda _: None
    hfd.report_unable_to_resume = lambda: None
    hfd.report_file_already_downloaded = lambda _: None
    hfd.undo_temp_name = lambda _: None
    hfd._hook_progress = lambda _: None
    hfd.calc_speed = lambda *args: None

# Generated at 2022-06-14 15:51:22.588218
# Unit test for constructor of class HttpFD

# Generated at 2022-06-14 15:51:26.750606
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import test_download
    # Check if retry is activated
    fd = HttpFD(
        test_download.TEST_URL,
        {
            'usenetrc': False,
            'username': 'unused',
            'password': 'unused',
            'verbose': True,
            'quiet': False,
            'ratelimit': 1048576,
            'nooverwrites': False,
            'retries': 5,
            'continuedl': False,
            'noprogress': False,
            'logtostderr': False,
        }
    )
    assert fd.max_retries() == 5
    # Check if ratelimit is activated

# Generated at 2022-06-14 15:51:27.790059
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Empty URLs shouldn't be accepted
    assert HttpFD('http://') == None


# Generated at 2022-06-14 15:51:40.412944
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class TestHttpFD(HttpFD):
        def __init__(self, *args, **kwargs):
            super(TestHttpFD, self).__init__(*args, **kwargs)
            self.test_success = False
            self.exc_raised = False
            self.extra_info = None
            self.expected_fragment_index = None
            self.retry_sleeps = []
            self.max_retries = 3

        def sleep(self, seconds):
            if self.retry_sleeps:
                retry_sleep = self.retry_sleeps.pop(0)
                assert retry_sleep == seconds


# Generated at 2022-06-14 15:51:48.760352
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # dummy subclass of HttpFD used by the unit test
    class HttpFD_Test(HttpFD):
        def real_download(self, filename, info_dict):
            return True

    # empty params
    params = {
        'usenetrc': False,
        'username': None,
        'password': None,
        'videopassword': None,
    }

    # Test no_check_certificate
    params['nocheckcertificate'] = True
    h = HttpFD_Test(params)
    assert h.ydl.nocheckcertificate
    params['nocheckcertificate'] = False
    h = HttpFD_Test(params)
    assert not h.ydl.nocheckcertificate

    # Test http_proxy
    params['http_proxy'] = None
    h = H

# Generated at 2022-06-14 15:51:59.071106
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    if os.path.exists('test'):
        shutil.rmtree('test')
    os.mkdir('test')
    test_file = 'test/test'
    fd = HttpFD(
        ydl, {
            'url': 'https://github.com/ytdl-org/youtube-dl/raw/master/youtube_dl/version.py',
            'params': {
                'nocheckcertificate': True,
                'quiet': True,
                'noprogress': True,
                'test': True,
            },
            'filename': test_file,
            'info_dict': {},
        },
        True
    )

    success = fd.real_download(fd.url, fd.params)
    size = os.path.getsize(test_file)


# Generated at 2022-06-14 15:52:11.568048
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import urllib
    import httplib

    class MockServer(object):
        """
        Fake HTTP server that supports only one request and returns fixed content
        """

        def __init__(self, data):
            self.data = data
            self.served = False

        def start(self):
            self.port = sanitized_Request('http://localhost/').get_port()
            self.server_thread = threading.Thread(
                target=lambda: test_HttpFD_real_download.test_httpserver.serve_forever(self))
            self.server_thread.daemon = True
            self.server_thread.start()

        def wait(self):
            self.server_thread.join()

        def handle_request(self, conn, addr):
            if self.served:
                conn.close()
           

# Generated at 2022-06-14 15:53:42.879173
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # A minimum test for real_download
    # Creates a test file with a known length and serves it with a simple HTTP server.
    # Then, checks that real_download can download the file completely.
    # This is just a unit test, so it creates a HttpFD instance, but it doesn't use
    # any of the other fields.
    test_dir_path = get_temp_dir()
    # Create a test file
    test_file_len = 2**16 + 1
    test_file_path = os.path.join(test_dir_path, 'test_file')
    with open(test_file_path, 'wb') as f:
        remaining = test_file_len
        while remaining:
            to_write = min(2**20, remaining)
            f.write(b'a' * to_write)


# Generated at 2022-06-14 15:53:50.688122
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    # Create a new object (using the test_server_factory)
    fd = HttpFD(global_params)
    fd.ydl = FakeYDL()

    class MockParams():
        def __init__(self, nocheckcertificate, retries, buffersize, noresizebuffer):
            self.nocheckcertificate = nocheckcertificate
            self.retries = retries
            self.buffersize = buffersize
            self.noresizebuffer = noresizebuffer

    class MockInfoDict():
        def __init__(self, filetime):
            self.filetime = filetime

    # Run the method

# Generated at 2022-06-14 15:54:02.984406
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import os
    import tempfile
    tmp = tempfile.TemporaryFile().name
    h = HttpFD()
    url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    assert h.real_download(url, {'outtmpl': tmp, 'quiet': True, 'nooverwrites': True, 'continuedl': True, 'noprogress': True})
    assert os.path.exists(tmp)

# Generated at 2022-06-14 15:54:15.317415
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
        Given an URL and test arguments,
        checks that `HttpFD.real_download` behaves as expected.
    """
    # args (list of strings): test arguments
    #      ports (list of integers): ports used to listen for HTTP connections
    #      content (string): content to send
    #      content_type (string): content type to send
    def _test_HttpFD_real_download(args, ports, content, content_type):
        server = _setup_server(ports[0], content, content_type)

        # create HttpFD object, use first available port

# Generated at 2022-06-14 15:54:24.581972
# Unit test for constructor of class HttpFD
def test_HttpFD():
    '''
    Running this function performs a unit test on HttpFD constructor.

    It requires an Internet connection.
    '''

    class DummyYDL(object):
        def __init__(self, params):
            self.params = params

        def to_screen(self, msg):
            print(msg)

        def trouble(self, msg, tb=None):
            raise Exception(msg)

    # Test URLs

# Generated at 2022-06-14 15:54:26.937831
# Unit test for constructor of class HttpFD
def test_HttpFD():
    assert (HttpFD(None, None, None, None) is not None)


# Generated at 2022-06-14 15:54:39.096174
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import threading
    import socket
    import mimetypes
    import testserver
    import random

    class TestServer(testserver.Server):
        """Test server that serves an HTTP resource with the given size."""

        def __init__(self, size):
            self.bytes_served = 0
            self.resource_size = size
            super(TestServer, self).__init__(socket.AF_INET6)

        def handle_request(self, conn, addr):
            self.bytes_served = 0
            self.send_response(conn, '200 OK', [('Content-Type', 'video/mp4')])

# Generated at 2022-06-14 15:54:43.702217
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test the constructor of class HttpFD. This is necessary
    # because the code mostly works with side-effects.

    class DummyHttpFD(HttpFD):
        """
        Dummy subclass of HttpFD.
        """

        def __init__(self, filename, info_dict):
            HttpFD.__init__(self, filename, info_dict)
            self.buf = b''

        def real_download(self, filename, info_dict):
            # Method that actually download a file by using methods
            # of the superclass HttpFD
            self.buf = b'hello, world!'
            return len(self.buf)

    info_dict = {
        'url': 'http://www.example.com/video.mp4',
        'title': 'Dummy Video Title',
    }

# Generated at 2022-06-14 15:54:51.253007
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
Unit test for the method real_download of class HttpFD.
It generates a random file and then tries to download it. It
compares the downloaded file with the original file.

For this unit test to work you need a web server in the local
machine running in port 8090. This web server must have the
directory test_html5lib (containing the test file) in its
document root.

To launch the web server you can use the following command
in linux:

$ python -m SimpleHTTPServer 8090

Or this one in windows:

> python -m http.server 8090
    """
    import random
    import base64
    from .compat import sha1
    from .utils import encodeFilename, sanitize_open
    import tempfile
    import os
    from .utils import encodeArgument

# Generated at 2022-06-14 15:55:01.174069
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Create the object
    h = HttpFD('http://www.google.com', {'noprogress': True})
    # Read a bit
    data = h.read(1024)
    if len(data) == 0:
        raise ValueError('no data returned')
    # Read to the end
    while True:
        ndata = h.read(1024)
        if len(ndata) == 0:
            break
        data += ndata
    if len(data) < 10000:
        raise ValueError('only %d bytes received' % len(data))
    # Print the first 500 characters
    print(str(data[:500]))

if __name__ == '__main__':
    test_HttpFD()