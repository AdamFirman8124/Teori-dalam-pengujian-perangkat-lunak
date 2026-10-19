

# Generated at 2022-06-14 15:48:45.978431
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .compat import gzip_compat
    from .utils import encodeFilename
    from .extractor import gen_extractors
    from .extractor.common import InfoExtractor
    ydl = InfoExtractor(gen_extractors())

    from .extractor import YoutubeIE
    class FakeYoutubeIE(YoutubeIE):
        def _real_extract(self, url):
            return {
                'id': '8jPQjjsBbIc',
                'url': 'http://techslides.com/demos/sample-videos/small.mp4',
                'upload_date': '20121002',
                'extractor': 'FakeYoutube',
                'uploader': 'Michael',
                'title': 'The small.',
            }

# Generated at 2022-06-14 15:48:51.404425
# Unit test for constructor of class HttpFD

# Generated at 2022-06-14 15:49:03.472787
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import io
    import http.server
    import socketserver
    import threading
    import unittest

    class HttpServerHandler(http.server.SimpleHTTPRequestHandler):
        def send_head(self):
            self.send_response(http.client.PARTIAL_CONTENT)
            self.send_header('Content-Range', 'bytes %d-%d/%d' %
                                                 (0, self._TEST_FILE_SIZE - 1, self._TEST_FILE_SIZE))
            self.send_header('Content-Length', 0)
            self.end_headers()

        def do_GET(self):
            f = io.BytesIO()
            f.write(b"ab" * int(self._TEST_FILE_SIZE / 2))
            f.seek(0)
            self.send_head

# Generated at 2022-06-14 15:49:14.841378
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os
    import re
    import zlib
    import shutil
    import tempfile
    import random
    from urllib.parse import parse_qs, urlsplit
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from threading import Thread
    from socket import socket
    
    test_server_address = 'localhost'
    test_server_port = 6666
    test_server_url = 'http://%s:%d' % (test_server_address, test_server_port)
    test_server_socket = None
    range_request_recv = False
    range_pattern = re.compile('bytes=(?P<range_start>-?\d+)?-(?P<range_end>-?\d+)?')


# Generated at 2022-06-14 15:49:16.040844
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    pass


# Generated at 2022-06-14 15:49:28.246491
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import tempfile
    import shutil
    import os.path
    import sys
    import urllib.parse
    import urllib.request

    # Random data
    data = urandom(1000)

    # Create a temporary folder
    temp = tempfile.mkdtemp()

# Generated at 2022-06-14 15:49:34.586168
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Create HTTP connection to test server
    sock = socket.socket()
    server_address = 'localhost', 9999
    sock.connect(server_address)
    connection = HTTPConnection(*server_address)
    connection.sock = sock
    connection.debuglevel = 1

    # Make HEAD request to receive headers
    connection.request(
        'HEAD',
        'test.php',
        None,
        {'Range': 'bytes=0-1023'})
    res = connection.getresponse()

    # Create new HttpFD object
    hfd = HttpFD(
        res,
        False,
        {'noprogress': True,
         'continuedl': True})

    # Test read() method
    data = hfd.read(1024)
    assert isinstance(data, bytes)

# Generated at 2022-06-14 15:49:42.881850
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(urlopen('http://google.com'))
    assert fd.read()
    assert fd.read(1000)
    assert fd.readline()
    assert fd.readline(1000)
    assert list(fd.iter_lines())
    assert list(fd.iter_lines(1000))
    assert not fd.close()
    assert fd.fileno() >= 0


# Generated at 2022-06-14 15:49:44.831376
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import doctest
    doctest.testmod(HttpFD)



# Generated at 2022-06-14 15:49:56.578361
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Because we need to verify file size, we don't test
    # output to stdout
    class TestFD(HttpFD):
        def __init__(self, params, info, filename):
            HttpFD.__init__(self, params, info)
            self.filename = filename

        def prepare_filename(self, info):
            return self.filename

        def report_progress(self, *args, **kargs):
            pass

        def report_error(self, *args, **kargs):
            pass

        def report_retry(self, *args, **kargs):
            pass

        def report_resuming_byte(self, *args, **kargs):
            pass

        def report_unable_to_resume(self, *args, **kargs):
            pass


# Generated at 2022-06-14 15:50:35.249052
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import threading
    import tempfile
    import socket
    import time
    import os
    import sys

    def mock_urlopen(request, timeout=None):
        check_header(request.headers)
        return MockSocket(request.get_full_url())

    class MockSocket(io.BufferedIOBase):
        def __init__(self, url):
            self.data = io.BytesIO(b'<html/>')
            self.url = url
            self.data_len = len(self.data.getvalue())
            self.info = {
                'Content-Length': self.data_len,
                'Last-Modified': 'Fri, 05 Jul 2013 07:19:57 GMT',
                }

        def getheader(self, name, default=None):
            return self.info.get(name, default)

# Generated at 2022-06-14 15:50:44.600451
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD()
    fd.addcookies({'foo': 'bar'})
    fd.addcookies({'foo2': 'bar2'})
    fd.add_header('Test', 'test')
    fd.add_header('Test2', 'test2')
    fd.filename = 'test.mp4'
    assert fd.geturl() == 'test.mp4'
    assert fd.headers['Cookie'] == 'foo=bar; foo2=bar2'
    assert fd.headers['Test'] == 'test'
    assert fd.headers['Test2'] == 'test2'
    fd.close()



# Generated at 2022-06-14 15:50:57.316082
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def _test(pretend, max_bytes):
        params = {'pretend': pretend, 'noprogress': False, 'verbose': True, 'consoletitle': False}
        with mock.patch('youtube_dl.postprocessor.FFmpegPostProcessor.run') as ffmpeg_mock:
            fd = HttpFD('http://i.am.a/test.bin', params, {})
            res = fd.real_download()
            assert res
            assert fd.downloaded < max_bytes
            return fd.downloaded
    with mock.patch('youtube_dl.utils.urlopen') as urlopen_mock:
        buf = b'a' * 16 * 1024
        bytes_read = 0

        def read_mock(size):
            nonlocal bytes_read

# Generated at 2022-06-14 15:51:08.095968
# Unit test for constructor of class HttpFD
def test_HttpFD():
    h = HttpFD(None, {}, {})

    # Test chunk_size
    # For chunk_size of 0, download will be performed in a single connection
    h.chunk_size = 0
    h.ydl = DummyYDL()
    h.test('http://example.com/1.bin', '-', 'wb')

    h.chunk_size = None
    h.ydl = DummyYDL()
    h.test('http://example.com/1.bin', '-', 'wb')

    # Test for chunk_size > 0
    # Download should be performed in several connections
    h.chunk_size = 1
    h.ydl = DummyYDL()
    h.test('http://example.com/1.bin', '-', 'wb')

# Generated at 2022-06-14 15:51:15.673120
# Unit test for constructor of class HttpFD
def test_HttpFD():
    """Test HttpFD constructor."""

    # Check exception raise when no url or filename is given
    try:
        fd = HttpFD()
        raise Exception(
            'HttpFD constructor accepts no argument.', fd.url, fd.filename)
    except TypeError as err:
        pass

    url = 'http://example.com/'
    fd = HttpFD(url)
    if fd.url != url:
        raise Exception('HttpFD does not have the expected url.')
    if fd.filename is not None:
        raise Exception('HttpFD filename should be None.')

    filename = 'example.html'
    fd = HttpFD(url, filename)
    if fd.url != url:
        raise Exception('HttpFD does not have the expected url.')

# Generated at 2022-06-14 15:51:27.656212
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test_real_download(HttpFD, formats, opts, expected_res=True):
        fd = HttpFD('http://example.com/test.bin', None, {})
        return fd.real_download(formats, opts) == expected_res

    # 1. Test successful download of a small file

# Generated at 2022-06-14 15:51:40.303724
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import youtube_dl.FileDownloader
    import youtube_dl.utils
    xdl = youtube_dl.FileDownloader.FileDownloader({'outtmpl': '%(id)s.%(ext)s'}, {'test': True})
    xdl.add_info_extractor(youtube_dl.InfoExtractor.InfoExtractor())
    xdl.result = {'id': 'test'}
    xdl.prepare_filename()
    xdl.params['test'] = True
    xdl.to_screen = youtube_dl.utils.noop
    xdl.report_error = youtube_dl.utils.noop
    fd = HttpFD(xdl, {})
    # test download

# Generated at 2022-06-14 15:51:48.641251
# Unit test for constructor of class HttpFD
def test_HttpFD():
    url_tpl = 'http://127.0.0.1:%d/test_%s'
    # Expected output strings

# Generated at 2022-06-14 15:51:59.004630
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    f = HttpFD(None, {'nooverwrites': True})
    f._TEST_FILE_SIZE = 5
    # This is a download test, so URLs below don't actually work
    # (**) means large file; (***) means that the URL won't exist
    # For testing, we use files that are guaranteed to be available (on this host)
    # We create a file of the appropriate size for each test (so we don't have
    # to keep re-downloading the same file)

# Generated at 2022-06-14 15:52:11.458089
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from io import StringIO
    from .extractor.common import InfoExtractor
    from .compat import compat_urllib_parse_unquote
    from .utils import str_to_bytes
    from .downloader import BaseFD

    class LocalFD(BaseFD):
        def __init__(self, params):
            super(LocalFD, self).__init__(params)
            self.test_data = str_to_bytes(compat_urllib_parse_unquote(self.params.get('test_data')))
            self.test_data_length = len(self.test_data)
            self.test_urls = [x.format(self.test_data_length) for x in self.params.get('test_urls')]

# Generated at 2022-06-14 15:53:38.369992
# Unit test for constructor of class HttpFD
def test_HttpFD():
    if 'darwin' in sys.platform:
        import warnings
        warnings.warn("filesystem encoding test disabled on darwin")
        return
    assert HttpFD(FakeYDL(), 'http://localhost/x' + ('x' * 1000)).test()


# Generated at 2022-06-14 15:53:45.847237
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class TestException(Exception):
        pass

    class RaiseRetryDownload(object):
        def __init__(self, exc):
            self.exc = exc

        def read(self, *args, **kargs):
            raise self.exc

    class SucceedDownloadDownloader(object):
        def __init__(self, exc):
            self.exc = exc

        def urlopen(self, *args, **kargs):
            if self.exc:
                raise self.exc
            else:
                return DummyDownloader()

    class FakeFileDownloader(object):
        def urlopen(self, *args, **kargs):
            return RaiseRetryDownload(TestException)


# Generated at 2022-06-14 15:53:55.562203
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test cases
    # return (url, filename, info_dict)
    class TestCase:
        def __init__(self, url, filename, info_dict):
            self.url = url
            self.filename = filename
            self.info_dict = info_dict

# Generated at 2022-06-14 15:54:06.973616
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Encoding for test unicode strings
    ENCODING = 'utf-8'
    # Base URL providing test downloads
    TEST_URL_BASE = 'https://github.com/ytdl-org/youtube-dl/raw/master/test/files/'
    # File name for test download
    TEST_FILENAME = 'test_%(test_id)s_%(format_id)s.mp4'
    # Dictionary with format ids and corresponding file names

# Generated at 2022-06-14 15:54:18.028284
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('-- testing HttpFD')
    import urllib
    import urllib.request
    from .extractor.common import InfoExtractor
    urlh = urllib.request.urlopen('https://www.google.com')
    info_dict = {
        'id': 'test_id',
        'ext': 'flv',
        'title': 'test_video',
        'url': 'http://www.example.com/video.ext',
        'thumbnail': 'http://www.example.com/thumbnail.jpg',
        'description': 'test description',
    }
    ie = InfoExtractor()
    ie.set_info(info_dict)

    # Test 1: Test if HttpFD returns the same data when mode = rb and mode = r

# Generated at 2022-06-14 15:54:26.462516
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp(prefix='youtube-dl-test-')


# Generated at 2022-06-14 15:54:38.742000
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import time
    import random
    import socket
    import os

    FORMAT_ID = 'nil'
    DEST_FILENAME = '-'
    INFO = {'id': FORMAT_ID}
    PARAMS = {'format': FORMAT_ID, 'outtmpl': DEST_FILENAME}

    def generate_content(content_length):
        def calc_checksum(s):
            retval = 0
            for c in s:
                retval += ord(c)
            return retval

        def gen_data(length):
            s = ''
            while len(s) < length:
                chunk = random.randrange(1, 1024)
                s += os.urandom(chunk)
            return s[:length]

        data_len = 0
        checksum = 0

# Generated at 2022-06-14 15:54:48.044866
# Unit test for constructor of class HttpFD

# Generated at 2022-06-14 15:54:59.021414
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .extractor import get_info_extractor
    # Test YoutubeIE
    ie = get_info_extractor('Youtube', downloader=FakeYDL())
    # Test data

# Generated at 2022-06-14 15:55:11.621266
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test case 1.
    fd = HttpFD('http://www.python.org', {'http_headers': {'Range': 'bytes=0-5'}})
    assert fd.get_headers()['Content-length'] == '6'
    assert fd.datestr().startswith('Sat, 01 Jan 2011')
    assert fd.real_url.startswith('http://www.python.org/')
    assert fd.real_download_size() == 3324
    assert fd.content_type == 'text/html; charset=utf-8'
    assert fd.get_filename() == 'index.html'
    t = fd.read(len(fd.data))
    assert t == fd.data
    assert fd.tell() == len(fd.data)
    f