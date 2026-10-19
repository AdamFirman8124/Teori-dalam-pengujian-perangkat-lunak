

# Generated at 2022-06-14 15:48:38.003813
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def _test(fd, data_len, min_filesize=None, max_filesize=None,
              retries=0, chunksize=None, test_result=True,
              xattr_set_filesize=None, **params):
        params = params.copy()
        params['write_info_json'] = False
        params['min_filesize'] = min_filesize
        params['max_filesize'] = max_filesize
        params['retries'] = retries
        params['http_chunk_size'] = chunksize
        params['xattr_set_filesize'] = xattr_set_filesize
        params = {k: v for k, v in params.items() if v is not None}
        test_result = bool(test_result)

# Generated at 2022-06-14 15:48:43.303323
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    hfd = HttpFD(params={'test': True}, info_dict={})
    hfd._TEST_FILE_SIZE = 10
    orig = hfd.best_block_size

    # The following two functions simulate responses of a http server.
    # The server starts to send test bytes with a block size of 10 bytes
    # and increases the block size after each response. The first 5
    # responses are sent with a block size smaller than 10 bytes and
    # the last 4 responses with a larger block size. The block size
    # needs to be adjusted to 10 bytes when reading the 3rd response.
    def _test_open_handler(hfd, url):
        class Resp(object):
            def __init__(self, block_size):
                self.info = lambda: {'Content-length': hfd._TEST_FILE_SIZE}


# Generated at 2022-06-14 15:48:53.262924
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import io
    import http_server
    from http_server import FakeHttpRequestHandler
    from http_server import FakeServer
    from http_server import MyFakeHTTPServer as Server
    import socket
    import threading
    import time

    # Create http server
    httpd = Server(('localhost', 0), FakeHttpRequestHandler)
    httpd.host, httpd.port = httpd.socket.getsockname()
    _server_thread = threading.Thread(target=httpd.serve_forever)
    _server_thread.setDaemon(True)
    _server_thread.start()

    # Set up parameters
    http_server.max_data_size = _TEST_FILE_SIZE * 10
    http_server.data_size = _TEST_FILE_SIZE

# Generated at 2022-06-14 15:49:07.285663
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # HttpFD._real_download should return None if the real download
    # procedure failed
    class TestException(Exception):
        pass
    from youtube_dl.downloader.http import HttpFD

    def hd(self, url, filename, info_dict):
        raise TestException()

    HttpFD._download_video_data = hd
    hfd = HttpFD(DictDownloader({}), 'foo', 'bar', {}, False, False)
    assert hfd._real_download(None, '.', {}) is False
    # HttpFD._real_download should be able to resume downloads
    # if resume is set to True
    def hd2(self, url, filename, info_dict):
        assert filename == 'foo'
        assert resume == True

    HttpFD._download_video_data = h

# Generated at 2022-06-14 15:49:10.504500
# Unit test for constructor of class HttpFD
def test_HttpFD():
    h1 = HttpFD(params={'noprogress': True})
    h2 = HttpFD(params={'progress_with_newline': True})
    h1.report_progress(1000, 1000)
    h2.report_progress(1000, 1000)


# Generated at 2022-06-14 15:49:24.514904
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test cases extracted from YouTubeIE youtube_dl/YoutubeDL.py test cases
    import time
    import pytest
    @pytest.fixture(scope="module")
    def t_log(request):
        import tempfile
        from contextlib import contextmanager
        from os.path import exists
        from os import remove
        from shutil import rmtree
        # TODO: implement direct testing of HttpFD.report_* methods instead of writing to a temporary file
        # TODO: make report output consistent (see #314)
        @contextmanager
        def t_log_main(log_file_name, log_file_mode, log_file_encoding):
            f = open(log_file_name, log_file_mode, encoding=log_file_encoding)
            f.write("\n")

# Generated at 2022-06-14 15:49:31.293000
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def test_write():
        s.write(b'0123456789')
        assert s.read() == b'0123456789'

    def test_write_nonblock():
        try:
            s.setblocking(False)
            s.write(b'0123456789')
            assert s.read() == b'0123456789'
        except (OSError, IOError):
            raise SkipTest('setting socket non-blocking is not supported')

    def test_incomplete_read():
        s.write(b'0123456789')
        assert s.read(3) == b'012'
        assert s.read(3) == b'345'
        assert s.read(3) == b'678'
        assert s.read(3) == b'9'

# Generated at 2022-06-14 15:49:43.783097
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # create file
    mkvmerge_temp_filename = tempfile.NamedTemporaryFile(suffix='.mkv')
    # create class
    http_fd = HttpFD()
    # set test file size
    http_fd.test_file_size = os.path.getsize(mkvmerge_temp_filename.name)
    # set test file
    http_fd.test_file = mkvmerge_temp_filename.name
    # set test chunk size
    http_fd.chunk_size = http_fd._TEST_FILE_SIZE
    # test real_download method
    http_fd.real_download(
        'http://localhost/',
        {'filename': '-', 'stream_info': {}},
        {'test': True, 'noresizebuffer': True}
    )


# Generated at 2022-06-14 15:49:55.406649
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import http.server
    import urllib.parse

    # If a string param is passed, it's taken as a filename
    assert HttpFD('http://www.example.com/a.txt', '-').name == '-'
    assert HttpFD('http://www.example.com/a.txt', '-').real_url == 'http://www.example.com/a.txt'
    assert HttpFD('http://www.example.com/a.txt', '-').close_allowed is True
    # If a tuple param is passed, the second element is taken as a filename
    assert HttpFD('http://www.example.com/a.txt', ('', '-')).name == '-'

# Generated at 2022-06-14 15:50:05.483745
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    file_size = 100
    chunk_size = 40
    first_range_size = 20
    second_range_size = 40
    url = 'http://example.com/f'
    response = {'status': 206, 'headers': {
        b'Content-Disposition': b'filename=f',
        b'Content-Length': str(file_size).encode('ascii'),
        b'Content-Range': b'bytes 0-%d/%d' % (first_range_size - 1, file_size),
    }}

# Generated at 2022-06-14 15:50:51.744050
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def mock_best_block_size(self, elapsed_time, bytes_downloaded):
        assert elapsed_time is not None
        assert bytes_downloaded > 0
        return self._TEST_FILE_SIZE

    orig_best_block_size = HttpFD._best_block_size

# Generated at 2022-06-14 15:51:02.696169
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import sys
    class YDLSocket:
        def __init__(self, s):
            self.s = s
        def makefile(self, mode, bufsize):
            return self.s
    class YDLUrlOpen:
        def __init__(self):
            self.urls = ['http://example.com']
            self.exception = None
        def __call__(self, *args, **kwargs):
            if self.exception:
                raise self.exception
            if self.urls:
                return compat_http_client.HTTPResponse(YDLSocket(open(self.urls.pop(0), 'rb')), method='GET')
        def add(self, url):
            self.urls.append(url)
        def setException(self, exception):
            self.ex

# Generated at 2022-06-14 15:51:12.644768
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(
        Download(params={}),
        'http://gdata.youtube.com/feeds/api/standardfeeds/%7Bhttp%3A%2F%2Fgdata.youtube.com%2Fschemas%2F2007%2Fkeywords.cat%7DMusic',
        {}
    )
    assert fd.real_download is None
    fd.real_download = 'foo'
    assert fd.real_download == 'foo'
    assert fd.url == 'http://gdata.youtube.com/feeds/api/standardfeeds/%7Bhttp%3A%2F%2Fgdata.youtube.com%2Fschemas%2F2007%2Fkeywords.cat%7DMusic'
    assert fd.headers == {}
   

# Generated at 2022-06-14 15:51:25.814063
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Same tests as in downloader/f4m.py
    from io import BytesIO
    from urllib.error import HTTPError
    from urllib.response import addinfourl
    from youtube_dl.downloader.common import (
        ContentTooShortError,
        FatalSampleException,
        RetryDownload,
    )

    # utility
    def urlopen(response, url='', data=None, *args, **kwargs):
        if isinstance(response, HTTPError):
            raise response
        else:
            return addinfourl(BytesIO(response), '', url, '', '')

    class FakeYDL:
        params = {
            'slow_down_factor': 2,
            'max_sleep_interval': 3,
            'force_generic_extractor': True,
        }

       

# Generated at 2022-06-14 15:51:32.950954
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test for python 2.x
    fd = HttpFD(None, None, None, None, blocksize=1048576)
    assert fd.buflist == []
    assert fd.left == ''
    assert fd.pos == 0
    assert fd.bufsize == 1048576

    # Test for python 3.x
    fd = HttpFD(None, None, None, None, blocksize=1048576)
    assert fd.buflist == []
    assert fd.left == b''
    assert fd.pos == 0
    assert fd.bufsize == 1048576



# Generated at 2022-06-14 15:51:44.338596
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os
    import sys
    import tempfile
    import unittest
    import re

    from youtube_dl.YoutubeDL import YoutubeDL

    class TestHttpFD(HttpFD):
        def __init__(self, *args, **kwargs):
            self.test_data = kwargs.pop('test_data')
            HttpFD.__init__(self, *args, **kwargs)

        def _get_test_urls(self):
            return self.test_data

        def _prepare_url(self, url):
            """Returns a tuple (scheme, server, port, path) with the parsed URL.
            If the URL can't be parsed, a ValueError is thrown."""
            if not url.startswith('http'):
                url = 'mock_http_prefix' + url
           

# Generated at 2022-06-14 15:51:56.410908
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import tempfile
    import shutil
    import atexit
    test_dir = tempfile.mkdtemp(prefix='ytdl-test-')
    atexit.register(shutil.rmtree, test_dir, ignore_errors=True)
    test_file = os.path.join(test_dir, 'test.tmp')
    # Following tests doesn't require network connection
    for prefix in ('http://', 'https://'):
        for t in (0.1, 0.5, 1.0):
            fd = HttpFD(None, prefix + 'localhost', {'http_chunk_size': 1, 'sleep_interval': t, 'max_sleep_interval': t})
            # Test write to a file
            assert fd.write(b'abc') == 3

# Generated at 2022-06-14 15:52:08.980500
# Unit test for constructor of class HttpFD
def test_HttpFD():
    hfd = HttpFD(dict())
    assert(hfd.content_type == '')
    assert(hfd.title == '')
    assert(hfd.title_from_url == False)
    assert(hfd.thumbnail == '')
    assert(hfd.description == '')
    assert(hfd.uploader == '')
    assert(hfd.uploader_id == '')
    assert(hfd.upload_date == '')
    assert(hfd.license == '')
    assert(hfd.location == '')
    assert(not hfd.view_count)
    assert(not hfd.age_limit)
    assert(hfd.ext == '')
    assert(hfd.format == '')
    assert(hfd.player_url == '')

# Generated at 2022-06-14 15:52:19.228576
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def h1(s):
        return b''.join(('%02x' % ord(c)).encode(s) for c in s)
    def h(s):
        return b''.join(('%02x' % c).encode(s) for c in s)

# Generated at 2022-06-14 15:52:29.701921
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    params = ['--format', 'bestaudio']
    params += ['--proxy', 'localhost:8118']
    params += ['--no-check-certificate']
    params += ['--no-part']
    params += ['--socket-timeout', '10']
    params += ['--quiet']
    params += ['--no-mtime']
    params += ['-o', 'tmphttpfdfile.%(ext)s']
    params += ['-', 'http://speedtest.tele2.net/100MB.zip']
    fd = HttpFD(params)
    fd.prepare()
    fd.progress_hooks = [fd.print_status]
    fd.real_download(True)

# Generated at 2022-06-14 15:54:04.564174
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Hard coded test URL
    url = 'http://www.sourcefiles.org/Audio/Ringtones/ringtone_en_bravo_3gpp.3gp'
    # Test download
    try:
        fd = HttpFD(url, {'noprogress': True})
        assert fd.url == url
        assert fd.endbyte > 0
        assert fd.get_size() > 0
        assert fd.read(1)
        assert fd.read(1000)
    except Exception as e:
        sys.exit(u'ERROR: Unable to download test file: ' + compat_str(e))

if __name__ == '__main__':
    test_HttpFD()
    print('Test succeeded!')

# Generated at 2022-06-14 15:54:16.573511
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD('http://www.google.com')
    assert fd.real_url == 'http://www.google.com'
    assert fd.basename() == 'www.google.com'
    fd = HttpFD('http://www.google.com/dir1/dir2/dir3/dir4/dir5', 'title')
    assert fd.real_url == 'http://www.google.com/dir1/dir2/dir3/dir4/dir5'
    assert fd.basename() == 'title'
    fd = HttpFD('http://www.google.com/dir1/dir2/dir3/dir4/dir5', 'title.txt')

# Generated at 2022-06-14 15:54:25.595462
# Unit test for constructor of class HttpFD
def test_HttpFD():
    if not sys.platform.startswith('win'):
        return  # xattr not supported
    if os.getenv('YOUTUBE_DL_TESTS'):
        import shutil
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            filename = tf.name
        with open(filename + u'.part', 'wb') as f:
            f.write(b'1234')
        with open(filename + u'.part.info', 'wb') as f:
            f.write(b'1234')
        with open(filename + u'.part.info.tmp', 'wb') as f:
            pass

# Generated at 2022-06-14 15:54:37.963446
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test constructor of class HttpFD
    class FakeYDL(object):
        def __init__(self, params):
            self.params = params
        def to_screen(self, s):
            print(s)
    class FakeInfo(object):
        def __init__(self, params):
            self.params = params
    info = FakeInfo({})
    ydl = FakeYDL(info)
    fd = HttpFD(ydl, info, None, 'http://192.0.2.1/', {'http_chunk_size': 10})
    fd = HttpFD(ydl, info, None, 'http://192.0.2.1/', {'http_chunk_size': 10}, test=True)

# Generated at 2022-06-14 15:54:45.096758
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import youtube_dl.utils
    # create a concrete FD and call its real_download() method
    ctx = youtube_dl.FileDownloadContext('-', 0, 0, 'wb', False, False)
    # self.real_download(ctx, retries=0)
    httpfd = youtube_dl.f4m.HttpFD(ctx, {})
    httpfd.real_download(ctx, retries=0)
    # cannot test download as we don't have a test server
    return True

if __name__ == '__main__':
    test_HttpFD_real_download()

# Generated at 2022-06-14 15:54:54.495007
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import io
    import socket
    import threading
    import time

    import pytest
    from six.moves import http_server, socketserver

    # A request handler that always returns a specified HTTP error
    class CustomHandler(http_server.BaseHTTPRequestHandler):
        def __init__(self, request, client_address, server, error=404):
            self.error = error
            self.wbufsize = -1  # don't use buffer, use sendall()
            http_server.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

        def do_GET(self):
            self.send_error(self.error)

    # A threaded HTTP server for testing
    class ThreadedHTTPServer(socketserver.ThreadingMixIn, http_server.HTTPServer):
        pass

    #

# Generated at 2022-06-14 15:55:06.389828
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import json
    import datetime
    import time
    from .utils import DateRange, timeconvert
    from .compat import (
        compat_urllib_error, compat_urllib_parse, compat_http_client,
        compat_urllib_request, compat_socket, compat_os_path,
    )
    from .extractor import get_info_extractor
    from .YoutubeDL import YoutubeDL

    # Copy/paste/adapt from YoutubeDL.py
    def _match_entry(self, info_dict):
        """ Returns None iff the file should be downloaded """
        matchtitle = self.params.get('matchtitle', False)
        mathdesc = self.params.get('matchdesc', False)
        nooverwrites = self.params.get('nooverwrites', False)

# Generated at 2022-06-14 15:55:17.092918
# Unit test for constructor of class HttpFD
def test_HttpFD():
    s = "HTTP/1.1 200 OK\r\nContent-Length: 10\r\n\r\ndatadatada"
    fd = HttpFD(BytesIO(s.encode('utf-8')), 'http://example.com/')
    assert fd.read() == b'datadatada'
    fd.close()

    s = "HTTP/1.1 200 OK\r\nContent-Length: 10\r\n\r\ndatadatada"
    fd = HttpFD(BytesIO(s.encode('utf-8')), 'http://example.com/')
    assert fd.read() == b'datadatada'
    assert fd.read() == b''
    fd.close()


# Generated at 2022-06-14 15:55:22.921632
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor.common import InfoExtractor
    from .utils import prepend_extension
    from .compat import parse_qs
    from .downloader.common import FileDownloader

    class MyInfoExtractor(InfoExtractor):

        _TEST = {
            'url': 'http://video.google.com/videoplay?docid=-8351924403384451128',
            'file': 'KFoW8BZpHmc.flv',
            'info_dict': {
                'title': 'The Chipmunk Song (Christmas Don\'t Be Late)',
                'uploader': 'Ross Bagdasarian, Sr.',
            },
        }

        def report_download_webpage(self, *args, **kargs):
            pass


# Generated at 2022-06-14 15:55:34.913724
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import tempfile
    import shutil
    import socket

    class DummyHTTPHandler(compat_urllib_request.HTTPHandler):
        def __init__(self, test_file):
            compat_urllib_request.HTTPHandler.__init__(self)
            self._test_file = test_file

        def http_open(self, req):
            return self.do_open(self.get_http_connection, req)

        def get_http_connection(self, host, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
            return DummyHTTPConnection(host, self._test_file)

    class DummyHTTPConnection(compat_HTTPConnection):
        _test_file = None

        def __init__(self, host, test_file):
            self._test_file = test_file
           