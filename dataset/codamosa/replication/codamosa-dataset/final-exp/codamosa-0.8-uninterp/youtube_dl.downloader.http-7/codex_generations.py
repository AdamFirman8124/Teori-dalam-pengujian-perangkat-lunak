

# Generated at 2022-06-14 15:48:39.518500
# Unit test for constructor of class HttpFD
def test_HttpFD():
    class FakeYDL(object):
        params = {}
        def __init__(self):
            self._progress_hooks = []  # You'll be able to use this to add progress hooks for testing

    test_class = HttpFD(FakeYDL())
    test_class._test()
    print('Done!')

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:48:40.979489
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import test_http_fd as _test_http_fd
    _test_http_fd.main()

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:48:52.168656
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # download a small file in one chunk
    ydl = YoutubeDL()
    filename = '-'
    fd = HttpFD(ydl, {'test': True}, 'http://www.youtube.com', 'videoid', 'title',
            test=True, retries=5, chunksize=0,
            start_time=time.time())
    assert fd.real_download({
        'tmpfilename': '-',
        'filename': filename,
        'url': 'http://127.0.0.1:8791/100b',
        'expected_size': 100,
        })
    assert sys.stdout.getvalue() == b'100b'

    # download a small file in two chunks
    sys.stdout = io.BytesIO()

# Generated at 2022-06-14 15:49:05.073868
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import io
    import tempfile
    import unittest
    import urllib.request

    class MockResponse(object):
        def __init__(self, headers):
            self.headers = headers

    class MockDownloader(object):
        def __init__(self):
            pass

        def urlopen(self, *args, **kwargs):
            return MockResponse({'content-length': '100500'})

    class MockYtdl(object):
        def __init__(self):
            pass

        def to_screen(self, *args, **kwargs):
            pass

    class MockInfoDict(object):
        def __init__(self):
            pass

    class TestUrlopen(unittest.TestCase):
        tmpfile = None
        tmpfile_name = None


# Generated at 2022-06-14 15:49:15.823877
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(fake_urlopen('http://example.com/video.mp4'), 'rb')
    assert fd._read(5) == b'hello'
    assert fd.tell() == 5
    fd.seek(0)
    assert fd.read(5) == b'hello'
    assert fd.tell() == 5
    fd.seek(2)
    assert fd.read(5) == b'llohe'
    assert fd.tell() == 7
    fd.seek(-3, whence=2)
    assert fd.read(5) == b'er.mp'
    assert fd.read(5) == b'4'
    assert fd.read(1) == b''
    assert fd.read(1) == b''

# Generated at 2022-06-14 15:49:28.067168
# Unit test for constructor of class HttpFD

# Generated at 2022-06-14 15:49:34.526039
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    # Perform a test download.
    class TestFD(HttpFD):
        def __init__(self):
            params = {
                'test': True,
                'nopart': True,
                'retries': 3,
                'buffersize': 10,
            }
            super(TestFD, self).__init__(params)

        def report_retry(self, error, count, retries):
            return

        def report_error(self, msg):
            return

        def report_destination(self, filename):
            return

    fd = TestFD()

    class TestResponse:
        """A response-like object which simulates a delayed download,
        either successful or unsuccessful"""

        def __init__(self, data, delayed=3, code=200):
            self.data = data

# Generated at 2022-06-14 15:49:48.155884
# Unit test for constructor of class HttpFD
def test_HttpFD():
    """Test HttpFD class with http URL."""
    info = {
        'url': 'http://www.youtube.com/watch?v=BaW_jenozKc',
        'id': 'BaW_jenozKc',
    }
    ie = InfoExtractor()
    ie.set_downloader(DummyDl())
    ie.params.update(dict(noprogress=True, nopart=True, quiet=True))
    info['extractor'] = ie
    fd = HttpFD(ie, info, {})

    assert(fd.filename == 'BaW_jenozKc.flv')
    assert(fd.name == 'videoplayback')

# Generated at 2022-06-14 15:49:59.437140
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Create a mock socket
    class MockSocket:
        def __init__(sself):
            sself.s = [b'Hello ', b'World']
            sself.i = 0

        def makefile(self, mode, bufsize=None):
            return self

        def read(self, bufsize=None):
            if self.i >= len(self.s):
                return b''
            else:
                val = self.s[self.i]
                self.i += 1
                return val

        def close(self):
            return True

    # Create an HttpFD object
    import sys
    ve_stdout = sys.stdout
    test_socket = MockSocket()
    test_server = 'www.example.com'
    test_port = 80
    test_urlh = compat_urllib_

# Generated at 2022-06-14 15:50:10.612372
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .utils import encodeFilename
    from .compat import sanitize_open
    import re

    def fake_best_block_size(a, b):
        return 8192

    # In order to test real_download with a test file larger than _TEST_FILE_SIZE,
    # _TEST_FILE_SIZE has to be increased. However, if the test file is too large
    # (MBs or even GBs) it is not desired to download it during unit tests.
    # In order to test real_download with a large test file (e.g. 1GB)
    # _TEST_FILE_SIZE has to be manually set to None before calling real_download.
    # See test_main() function for an example.
    _TEST_FILE_SIZE = 1024**2


# Generated at 2022-06-14 15:50:56.517849
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import tempfile
    from io import BytesIO
    from collections import namedtuple
    import socket
    import ssl

    class _FakeOpener(object):
        def __init__(self, response):
            self.response = response

        def open(self, request, timeout=None):
            return self.response

    class _FakeConnection(object):
        def __init__(self, data, resp_headers=None, status=200):
            self.data = BytesIO(data)
            self.resp_headers = resp_headers or {}
            self.info = self.resp_headers.__getitem__
            self.status = status

        def getcode(self):
            return self.status


# Generated at 2022-06-14 15:51:07.299424
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import doctest
    HttpFD.params = {}
    HttpFD.params['noprogress'] = False
    HttpFD.params['logger'] = None
    HttpFD.params['retries'] = 5
    HttpFD.params['continuedl'] = False
    HttpFD.params['noresizebuffer'] = False
    HttpFD.params['ratelimit'] = 0
    HttpFD.params['buffersize'] = 8192
    HttpFD.params['test'] = True
    HttpFD.ydl = FakeYoutubeDl()
    HttpFD.report_error = lambda *args, **kargs: None
    HttpFD.report_retry = lambda *args, **kargs: None

# Generated at 2022-06-14 15:51:19.225237
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    vid = mp4
    ydl = YoutubeDL(dict(quiet=True, noprogress=True, nooverwrites=True, test=True,
        outtmpl='%(tmp)s%(title)s.%(ext)s',
    ))

    # First establish connection without requesting a range
    # (ctx.chunk_size = 0)
    class FakeSocket:
        def read(self, size):
            assert size == 0
            return b''
        def info(self):
            return {}
    ctx = _DownloadContext(ydl, url, None, 0, {}, None, None)
    ctx.data = FakeSocket()
    ctx.open_mode = 'wb'
    ctx.data_len = None
    ctx.resume_len = 0
    assert HttpFD._real

# Generated at 2022-06-14 15:51:28.378882
# Unit test for constructor of class HttpFD
def test_HttpFD():
    """Just run the constructor of HttpFD. It does nothing but it used to crash."""
    for format_param in (None, 'm4a', 'bestaudio[ext=m4a]/best'):
        for verbose in (True, False):
            for quiet in (True, False):
                for no_warnings in (True, False):
                    HttpFD(None, {
                        'format': format_param,
                        'verbose': verbose,
                        'quiet': quiet,
                        'no_warnings': no_warnings,
                    })

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:51:40.883563
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd1 = HttpFD(None, {}, 'http://example.com/file.name')
    assert fd1.geturl() == 'http://example.com/file.name'
    assert fd1.realurl == 'http://example.com/file.name'
    assert fd1.size is None

    fd2 = HttpFD(None, {}, 'http://example.com/file.name', {'Content-Length': '7243'})
    assert fd2.size == 7243
    assert fd2.realurl is None

    fd3 = HttpFD(fd2, {}, 'http://example.com/file.name')
    assert fd3.geturl() == 'http://example.com/file.name'
    assert fd3.size == 7243
    assert fd

# Generated at 2022-06-14 15:51:49.845112
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import test_http_server
    srv = test_http_server.TestHTTPServer()

# Generated at 2022-06-14 15:51:59.590273
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .compat import parse_qsl
    def test_urlopen(url):
        """Simulate urlopen()"""
        class info(object):
            """Simulate info()"""
            def __init__(self, url):
                query = urlparse(url).query
                self.dict = dict(parse_qsl(query))
            def get(self, key, default=None):
                return self.dict.get(key, default)
        class data(object):
            """Simulate the returned data of the urlopen()"""
            def __init__(self, url):
                self.info = info(url)
            def read(self, size= -1):
                return b'a' * size
        return data(url)


# Generated at 2022-06-14 15:52:12.182226
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import os

    def make_readline(s):
        def readline():
            return s
        return readline
    def make_read(s):
        def read(n):
            return s
        return read


# Generated at 2022-06-14 15:52:18.520165
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # call the method with some arguments
    kwargs = {
        'cmd': 'download',
        'filename': '-',
        'info_dict': {},
        'test': True,
        'resume_len': 0,
        'retries': 5,
    }
    h = HttpFD(YouTubeDL(params={}))
    h._TEST_FILE_SIZE = 5000 # set max test file size
    h.real_download('http://example.com', **kwargs)


# Generated at 2022-06-14 15:52:29.745649
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # purpose: ensure that HttpFD.real_download returns correct values in
    #          correct cases
    # method:  create object and call method
    # result:  should return False, if an error occurs
    #          should return True, if no error occurs
    _debug = True

    # -------------------------------------------------------------------
    # -- settings
    _err_messages = [
        'Connection reset by peer',
        'Connection to server interrupted',
        'Connection to server timed out',
        'Connection to server lost',
        'Unable to resume',
        'DontReport',
        'unable to open for writing',
        'Did not get any data blocks',
        'Could not download',
        'giving up after',
        'Exceeded file size',
        'Exceeded max download limit'
    ]

# Generated at 2022-06-14 15:53:33.917868
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os.path
    import shutil
    import tempfile
    import threading
    import time
    from .compat import compat_http_client
    from .utils import iso639_2_lang
    from .socks import SocksFD
    from .DownloadContext import DownloadContext
    from .FileDownloader import FileDownloader
    from .FileDownloader import safe_filename
    from .RtmpFD import RtmpFD
    from .utils import encodeFilename
    from .utils import write_xattr

    class UnitTestFD(HttpFD):
        """
        File downloader for unit testing real_download() method of class HttpFD
        """
        _TEST_FILE_SIZE = 10485760

# Generated at 2022-06-14 15:53:40.987053
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test with a network connection
    fd = HttpFD('http://www.google.com/', None, {'nopart': True})
    assert fd.size() > 1000
    assert fd.size() < 2000
    data = fd.read(1000)
    assert data.startswith(b'<!doctype html>')
    assert fd.read(1000) == data
    assert fd.read(1000) == data
    fd.close()

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:53:51.666505
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class EndOfDownload(Exception): pass

    def report_destination(filename):
        pass

    def report_progress(downloaded_bytes, total_bytes, tmpfilename):
        if downloaded_bytes == 4:
            raise EndOfDownload()

    def report_failure(message):
        raise Exception(message)

    def report_warning(message):
        raise Exception(message)

    def report_retry(count, retries):
        pass

    def report_file_already_downloaded(filename):
        raise Exception('Already downloaded: ' + filename)

    def report_unable_to_resume(filename):
        raise Exception('Unable to resume: ' + filename)

    def report_resuming_byte(byte_counter):
        raise Exception('Resuming from: ' + str(byte_counter))


# Generated at 2022-06-14 15:54:03.917621
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from youtube_dl.downloader.http import HttpFD
    from collections import namedtuple
    Params = namedtuple('Params', ['test', 'verbose', 'noresizebuffer'])
    params = Params(test=True, verbose=True, noresizebuffer=False)
    fd = HttpFD(params, 'http://example.com/')
    content_len = 1234
    fd.urlopen_result = namedtuple('Response', ['headers'])({'Content-Length': content_len})
    fd.data = [
        b'abc',
        b'def',
    ]
    fd.real_download()
    assert fd.downloaded_bytes == content_len
    assert fd.content_type == 'text/plain'

# Generated at 2022-06-14 15:54:05.495983
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Testing exceptions
    assert_raises(TypeError, HttpFD)
    

# Generated at 2022-06-14 15:54:17.325009
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import io
    import gzip
    import tempfile
    import zlib
    class FakeYDL(object):
        def _write_info_file(self, *args, **kargs):
            pass
        def urlopen(self, *args, **kargs):
            return FakeUrlOpen(*args, **kargs)
    class FakeUrlOpen(io.BytesIO):
        def __init__(self, request, *args, **kargs):
            from io import BytesIO
            self.request = request
            self.code = 200
            self.headers = {}
            if request.headers.get('Range', '').startswith('bytes='):
                self.code = 206
            if request.headers.get('Accept-Encoding', '').find('gzip') != -1:
                self.headers['Content-Encoding']

# Generated at 2022-06-14 15:54:26.026698
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test 1: Invalid URLs
    invalid_urls = [
        'http://',
        'http://foo.bar/video.mp4/../../a.flv',
        ]
    for url in invalid_urls:
        try:
            HttpFD(url, {}, None)
            assert False, 'Invalid URL accepted'
        except AssertionError:
            raise
        except Exception:
            pass

    # Test 2: Valid URLs

# Generated at 2022-06-14 15:54:34.973080
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import tempfile
    tmp = tempfile.NamedTemporaryFile()
    tmp_name = encodeFilename(tmp.name)
    tmp.write(b'foobarbaz')
    tmp.close()
    fd = HttpFD(tmp_name)
    assert fd.read(3) == b'foo'
    assert fd.read(2) == b'ba'
    assert fd.read(4) == b'rbaz'
    fd.close()

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:54:44.962573
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import copy

    import subprocess
    import sys
    import http.client
    import socket
    import random

    _DEFAULT_BLOCK_SIZE = 1024 * 256
    _TEST_FILE_SIZE = 1024 * 1024

    # modified HttpFD with _TEST_FILE_SIZE set to 1MB
    class HttpFD_test(HttpFD):
        def __init__(self, ydl, params):
            HttpFD.__init__(self, ydl, params)
            self._TEST_FILE_SIZE = _TEST_FILE_SIZE

    # test HTTP server

# Generated at 2022-06-14 15:54:54.310001
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .compat import compat_urllib_request
    from .utils import write_json_file
    from .compat import urlretrieve
    url = 'http://www.youtube.com/get_video'
    data = {'video_id': 'BaW_jenozKc', 't': 'vjVQa1PpcFOkTuT6zB3Fyqw3I_o3-F2g'}
    post_data = compat_urllib_request.urlencode(data).encode('ascii')
    request = compat_urllib_request.Request(url, post_data, {'Content-type': 'application/x-www-form-urlencoded'})
    (fname, headers) = urlretrieve(request, 'testvideo.flv')

# Generated at 2022-06-14 15:56:38.890698
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Setup
    fd = HttpFD(None, None, {
        # __init__ params
        'quiet': True,
        'nooverwrites': True,
        'continuedl': True,
        'ratelimit': 1024,
        'retries': 3,
        'buffersize': 512,
        'noresizebuffer': False,
        'test': False,
        'min_filesize': 0,
        'max_filesize': float('inf'),
        'updatetime': True,
        'test': True,
        'xattr_set_filesize': False,
    })
    class DummyYDL:
        def __init__(self):
            self.params = {'ratelimit': 1024}
        def to_screen(self, msg):
            print(msg)

# Generated at 2022-06-14 15:56:44.617524
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """Test if HttpFD._real_download() returns correct values based on input and if it doesn't leave stuff behind on file system."""
    def gen_data(start, length):
        return b'a'*length

    def raise_for_range(headers):
        if not headers or 'Range' not in headers:
            return
        m = re.search(r'bytes=(\d+)-(\d+)?', headers['Range'])
        if not m:
            return
        range_start = int(m.group(1))
        range_end = int(m.group(2))
        if range_end is None:
            range_end = length
        length = range_end - range_start + 1

# Generated at 2022-06-14 15:56:52.241306
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    '''
    Perform a series of tests on method real_download

    :return: True on success, False on failure.
    '''
    import types

    # Create a dummy progress hook
    progress_hook = lambda status: None
    progress_hook = types.MethodType(progress_hook, None)

    # Create a dummy slow_down method
    def slow_down(start, now, downloaded):
        return None
    slow_down = types.MethodType(slow_down, None)

    # Create a dummy best_block_size method
    def best_block_size(elapsed_time, bytes_downloaded):
        return 1024
    best_block_size = types.MethodType(best_block_size, None)

    # Create a dummy try_utime method

# Generated at 2022-06-14 15:57:01.936631
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import shutil, urllib.request
    import http.server, threading
    from socket import timeout as SocketTimeoutException
    from youtube_dl.utils import encodeFilename


    class HttpServer(http.server.HTTPServer):
        """HTTP server that shuts itself down after a single request.

        Reference: http://stackoverflow.com/q/4621032/35070
        """

        def get_request(self):
            request, client_address = self.socket.accept()
            # self.shutdown()
            self.socket.close()
            return request, client_address

    class HttpHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, world!')

# Generated at 2022-06-14 15:57:09.368495
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # On Windows the file is locked
    if os.name == 'nt':
        return None

    class FakeYDL:
        def __init__(self):
            self.to_screen_lock = threading.Lock()
            self.to_screen_buffer = b''
        def to_screen(self, s):
            if isinstance(s, str):
                s = s.encode('ascii', 'ignore')
            with self.to_screen_lock:
                self.to_screen_buffer += s

    # Create a file for chunked download
    # (so not all data will be available at once)
    with open(TESTFN, 'wb') as stream:
        for n in itertools.count(1):
            chunk = os.urandom(n)
            stream.write(chunk)

# Generated at 2022-06-14 15:57:19.956133
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(
        'http://127.0.0.1:8080/bad',
        {}, {}, {},
        None, None, None, None, 'http', False, False,
        None, None,
        None, None, None, None)
    assert fd.ydl is None

    class YDL(object):
        def __init__(self, params):
            self.params = params

        def to_stderr(self, msg):
            print(msg)

        def chunk_size(self):
            return self.params.get('chunksize', 1024 * 1024)

        def report_error(self, msg, tb=None):
            pass

        def report_warning(self, msg):
            pass


# Generated at 2022-06-14 15:57:26.706779
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def report_mock(self, *args, **kwargs): return
    def report_retry_mock(self, *args, **kwargs): return
    def report_destination_mock(self, *args, **kwargs): return
    def calc_speed_mock(self, *args, **kwargs): return
    def best_block_size_mock(self, *args, **kwargs): return
    def slow_down_mock(self, *args, **kwargs): return
    def to_screen_mock(self, *args, **kwargs): return
    def download(self, url, filename, info_dict):
        return self.real_download(url, filename, info_dict, None, None)
    # HttpFD._TEST_FILE_SIZE = 1024  # bytes
    # H

# Generated at 2022-06-14 15:57:32.637204
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    fake_screen = FakeScreen()
    # Arguments to the download() method below:
    # {
    #   'min_filesize': 100,
    #   'max_filesize': 100,
    #   'cachedir': False,
    #   'continuedl': False,
    #   'ratelimit': None,
    #   'noresizebuffer': False,
    #   'retries': 10,
    #   'nooverwrites': False,
    #   'test': True,
    #   'fragment_retries': 10,
    #   'keepvideo': False,
    #   'buffersize': None,
    #   'noprogress': False,
    #   'test': True,
    #   'http_chunk_size': None,
    #   '

# Generated at 2022-06-14 15:57:42.184871
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    orig_download = HttpFD._do_download
    def _do_download(self, ctx):
        if ctx.filename == 'tmp1':
            raise compat_urllib_error.HTTPError(
                'tmp', 417, 'Fake error', compat_httplib.HTTPMessage(compat_StringIO.StringIO()),
                compat_StringIO.StringIO('Fake error message'))
        elif ctx.filename == 'tmp2':
            raise compat_urllib_error.HTTPError(
                'tmp', 500, 'Fake error', compat_httplib.HTTPMessage(compat_StringIO.StringIO()),
                compat_StringIO.StringIO('Fake error message'))
    HttpFD._do_download = _do_download

# Generated at 2022-06-14 15:57:51.339276
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def _test_retry(urlopen, retries, results):
        _urlopen = compat_urllib_request.urlopen
        _urlretrieve = compat_urllib_request.urlretrieve
        compat_urllib_request.urlretrieve = lambda *args, **kwargs: (args, kwargs)
        def urlopen(url, *args, **kwargs):
            compat_urllib_request.urlopen = _urlopen
            return urlopen(url, *args, **kwargs)
        compat_urllib_request.urlopen = urlopen
        _errnos = [None, socket.error, io.FileNotFoundError, compat_urllib_error.URLError]