

# Generated at 2022-06-14 15:48:46.756899
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from ytdl.downloader import HttpFD
    from ytdl.utils import _parse_bytes

    # Returns a string with a total length of byte_len that is filled with ch
    def make_string(ch, byte_len):
        return ch * int(byte_len / len(ch)) + ch[:byte_len % len(ch)]

    # Returns an instance of class HttpFD that performs a number of GET requests
    # to its own mock server, which is managed by instances of class MockHandler
    # and class MockServer.
    # A stream of bytes is produced by the mock server with total length of data_len
    # and chunk_size on each request.
    # The byte stream is represented as a byte sequence, where every byte
    # is equal to its ordinal number. For example, the first byte is equal to 0x00,

# Generated at 2022-06-14 15:48:52.296333
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    fd = HttpFD(YoutubeDL(), {'nooverwrites': True, 'continuedl': False, 'quiet': True}, None, None)
    # test_urls = [('http://ipv4.download.thinkbroadband.com/10MB.zip', '10MB.zip'), ('http://ipv4.download.thinkbroadband.com/5MB.zip', '5MB.zip'), ('http://ipv4.download.thinkbroadband.com/1MB.zip', '1MB.zip'), ('http://ipv4.download.thinkbroadband.com/512KB.zip', '512KB.zip'), ('http://ipv4.download.thinkbroadband.com/200KB.zip', '200KB.zip'), ('http://ipv4.download.thinkbroadband.com/100KB.zip', '100

# Generated at 2022-06-14 15:49:01.185705
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test(description, params, orig_url, file_size, count, retries, expected_length, expected_retry, expected_count):
        urlh = URLH(orig_url)
        urlh.data_len = None
        urlh.downloaded_bytes = 0
        for _ in range(count):
            partial_status = {
                'filename': 'dummy',
                'status': 'downloading',
                'total_bytes': file_size,
                'downloaded_bytes': urlh.downloaded_bytes,
            }
            fn = lambda x: None
            res = HttpFD._real_download(
                HttpFD({'nopart': True, 'retries': retries}),
                urlh, params, fn, fn, partial=partial_status)

# Generated at 2022-06-14 15:49:13.379850
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os
    import shutil
    import tempfile

    from youtube_dl.FileDownloader import FileDownloader
    from youtube_dl.utils import encodeFilename, sanitize_open

    from compat import StringIO

    _TEST_URL = 'https://github.com/rg3/youtube-dl/raw/master/README.md'

    # Define methods to be mocked
    class MockYTDL(object):

        def __init__(self, outtmpl=None):
            self.params = {
                'outtmpl': outtmpl if outtmpl else '%(id)s.%(ext)s',
                'noprogress': True,
                'logger': FileDownloader(self).report_warning
            }
            self.to_screen = print
            self.to_stderr = print

# Generated at 2022-06-14 15:49:26.059310
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os
    import sys
    import shutil
    import tempfile
    from .compat import compat_http_server
    from .compat import compat_urllib_request
    from .compat import compat_urllib_error
    from .compat import compat_urllib_parse

    def get_open_port():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 0))
        port = s.getsockname()[1]
        s.close()
        return port

    class MyHandler(compat_http_server.BaseHTTPRequestHandler):
        def do_HEAD(self):
            self.send_response(200)
            self.send_header('Content-Length', len(data_1))

# Generated at 2022-06-14 15:49:28.277886
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('Testing HttpFD constructor')
    h = HttpFD(None, {'nooverwrites': True}, None)
    print('HttpFD constructor succeded')

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:49:38.212062
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ydl = YoutubeDL({'nooverwrites': True})
    assert not ydl.params['nopart']
    assert not ydl.params['continuedl']
    assert ydl.params['nooverwrites']
    test_url = 'http://repository.example.com/video.mp4'
    assert HttpFD(ydl, test_url).url == test_url

    ydl = YoutubeDL({'nopart': True})
    assert ydl.params['nopart']
    assert not ydl.params['continuedl']
    assert not ydl.params['nooverwrites']
    assert HttpFD(ydl, test_url).url == test_url

    ydl = YoutubeDL({'continuedl': True})
    assert not ydl.params['nopart']

# Generated at 2022-06-14 15:49:50.995087
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    url = 'http://test.test/test.test'
    c = HttpFD().open(url)
    c._test_download = True

    def _hook_progress(status):
        #print(status)
        if status['status'] == 'finished':
            assert status['downloaded_bytes'] == status['total_bytes'] == c._TEST_FILE_SIZE
        else:
            assert status['status'] == 'downloading'
            assert status['downloaded_bytes'] > 0
            assert status['total_bytes'] is None
    c._hook_progress = _hook_progress

# Generated at 2022-06-14 15:49:59.136858
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Create a HTTP connection object
    h = HttpFD(cache=False)

    # Downloading this should trigger an exception
    # (this is the URL of an empty file)
    test_url = 'http://ipv4.download.thinkbroadband.com/100MB.zip'

    # Set the HTTP header
    h.add_header('Range', 'bytes=0-1048575')
    # Actually do the download
    h.download(test_url, {'test': True})


if __name__ == "__main__":
    test_HttpFD()

# Generated at 2022-06-14 15:50:07.922868
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Create an object of HttpFD class
    hfd = HttpFD(params = { 'continuedl': True, 'noprogress': True },
                 ydl = None, # not used by real_download
                 info_dict = {})
    # Create a temporary file and download a file to it
    fd, filename = tempfile.mkstemp(suffix = u'.temp')

# Generated at 2022-06-14 15:50:56.455362
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import sys
    import tempfile
    info_dict = {
        'url': 'http://127.0.0.1/',
        'http_headers': {'Range': 'bytes=0-2061'},
    }
    print(('Testing: %s' % str(info_dict)))
    tmp_file, tmp_filename = tempfile.mkstemp(prefix='yt-dl')
    os.close(tmp_file)

# Generated at 2022-06-14 15:51:04.705366
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Constructor test
    fd = HttpFD(
        sanitize_url('http://www.example.com/'),
        {'progress_hooks': [lambda *a, **ka: None]})
    assert fd.urlh.status == 200  # pylint: disable=no-member
    assert fd.url == 'http://www.example.com/'
    assert fd.downloaded_bytes == 0
    assert fd.total_bytes is None
    assert fd.filename is None
    assert fd.tmpfilename is None
    assert fd.urlh is not None


# Generated at 2022-06-14 15:51:13.993778
# Unit test for constructor of class HttpFD

# Generated at 2022-06-14 15:51:26.932408
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # download url
    url = 'http://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_2mb.mp4'
    # path to download file
    filename = 'big_buck_bunny.mp4'
    # Object to download
    h = HttpFD(url, filename, None, None)
    # test httpfd_read()

# Generated at 2022-06-14 15:51:38.750269
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import StringIO
    out = StringIO()

    # Prevent file deletion
    open = real_open

    # Constructor test
    hfd = HttpFD(out, {'nooverwrites': True})
    assert hfd.fd == out
    assert hfd.tmpfile == '-'
    assert hfd.mode == 'wb'
    assert hfd.total == -1
    assert hfd.downloaded == 0
    assert hfd.prev_progress == 0
    assert not hfd.finished
    hfd.close()
    assert hfd.fd is None
    assert hfd.tmpfile is None
    assert hfd.mode is None

    # Test temp file creation
    hfd = HttpFD(out, {'continuedl': True})
    assert hfd.fd

# Generated at 2022-06-14 15:51:43.227371
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD('http://example.com/')
    assert fd.url == 'http://example.com/'
    fd = HttpFD('http://example.com/', {'noprogress': True})
    assert fd.params == {'noprogress': True}



# Generated at 2022-06-14 15:51:55.549199
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # First test with no failures
    _TEST_URL = 'http://127.0.0.1:8080/content?id=0'

    class FakeYdl:
        def __init__(self):
            self.to_screen_count = 0

        def to_screen(self, *args, **kwargs):
            self.to_screen_count += 1

        def to_stderr(self, *args, **kwargs):
            pass

        def urlopen(self, request):
            if 'Range' in request.headers:
                byte_offset = int(request.headers['Range'][6:-1])
            else:
                byte_offset = 0
            length = 5

            resp = compat_http_client.HTTPResponse(self)
            resp.length = length

# Generated at 2022-06-14 15:52:08.279975
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test with normal parameters
    hfd = HttpFD('http://localhost/', {'noprogress':True}, None)
    # Test with wrong URL
    try:
        hfd = HttpFD('htt://localhost/', {'noprogress':True}, None)
        assert False
    except (compat_urllib_error.URLError, socket.timeout):
        pass
    # Test with wrong port
    try:
        hfd = HttpFD('http://localhost:1/', {'noprogress':True}, None)
        assert False
    except (compat_urllib_error.URLError, socket.timeout):
        pass
    # Test with non-HTTP URL

# Generated at 2022-06-14 15:52:18.758625
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # HttpFD.real_download does not work without HTTP server, so this test
    # does not do the whole work
    # If the following test fails, try running the whole test suite again
    # It sometimes happens that the HTTP server started by another test
    # is still running so this test passes
    # TODO: prepare a better test
    import socket
    import threading
    params = {
        'usenetrc': False,
        'username': 'unittest',
        'password': 'unittest',
        'noprogress': True,
        'forcetitle': True,
        'quiet': True,
        'simulate': True,
        'format': '22',
    }
    params.update(stdout_encode_fn=lambda x: x)
    ydl = YoutubeDL(params)
   

# Generated at 2022-06-14 15:52:27.002135
# Unit test for constructor of class HttpFD
def test_HttpFD():
    h = HttpFD('http://www.google.com/index.html', { 'noprogress': True })
    assert h.filename == 'index.html'
    assert h.expected_size is None
    assert h.method == 'GET'
    assert h.url == 'http://www.google.com/index.html'
    assert h.fd is None
    assert h.headers == {}
    assert h.params == { 'noprogress': True }
    assert h.real_download == True


# Generated at 2022-06-14 15:54:08.984293
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # This method calls slow_down and best_block_size for multiple times,
    # but ignore these methods for now.
    class DummyYDL:
        def to_screen(self, *args):
            print(args)
        def report_error(self, *args):
            print(args)
        def report_retry(self, *args):
            print(args)
        def report_resuming_byte(self, *args):
            print(args)
        @staticmethod
        def calc_speed(start, *args):
            return 1024**2
        @staticmethod
        def calc_eta(start, *args):
            return 5
        def slow_down(self, start, now, bytes):
            pass
        def best_block_size(self, elapsed, new_bytes):
            return 1024**2

   

# Generated at 2022-06-14 15:54:16.051851
# Unit test for constructor of class HttpFD
def test_HttpFD():
    http_fd = HttpFD(
        None, 'http://example.com/sample.mp4', {
            'http_chunk_size': 10,
            'min_filesize': 50,
            'max_filesize': 100,
            'retries': 2,
        }, None)
    assert http_fd.chunk_size == 10
    assert http_fd.min_filesize == 50
    assert http_fd.max_filesize == 100
    assert http_fd.retries == 2



# Generated at 2022-06-14 15:54:25.207908
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    f = HttpFD(None, None, {'nooverwrites': True, 'continuedl': True}, None)
    class Context():
        pass
    ctx = Context()
    ctx.tmpfilename = 'tmpfilename'
    ctx.filename = 'filename'
    ctx.data = io.BytesIO(b'mock')
    ctx.stream = io.BytesIO()
    ctx.open_mode = 'wb'
    ctx.chunk_size = 0
    ctx.is_test = True
    f._find_api_info('http://example.com/', ctx)
    f._do_download(ctx, 1, 1)
    assert ctx.stream.getvalue() == b'mock', ctx.stream.getvalue()
    assert ctx.open_mode == 'ab'

# Generated at 2022-06-14 15:54:37.641198
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .utils import QueryDict
    from .compat import compat_http_server
    import threading
    import time

    class MyHandler(compat_http_server.BaseHTTPRequestHandler):
        def do_HEAD(s):
            s.send_response(200)
            s.send_header('Content-Type', 'video/mp4')
            s.send_header('Content-Length', str(s.server.content_length))
            s.end_headers()

        def do_GET(s):
            s.server._ready_event.set()
            s.send_response(200)
            s.send_header('Content-Type', 'video/mp4')
            s.send_header('Content-Length', str(s.server.content_length))
            s.end_headers()

# Generated at 2022-06-14 15:54:47.288495
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import http.client
    import socket
    import urllib.request

    # Step 1: Download a small test file
    url = 'http://localhost/~rg3/youtube-dl/test/test1.jpg'
    dest = 'test1.jpg'
    c = http.client.HTTPConnection('localhost')
    c.request('GET', '/~rg3/youtube-dl/test/test1.jpg')
    data = c.getresponse()
    with open(dest, 'wb') as f:
        f.write(data.read())

    # Step 2: Another small test file
    url = 'http://localhost/~rg3/youtube-dl/test/test2.jpg'
    dest = 'test2.jpg'
    c = http.client.HTTPConnection('localhost')

# Generated at 2022-06-14 15:54:57.719950
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    with contextlib.ExitStack() as stack:
        # Set up context
        ctx = stack.enter_context(MockContext())
        ctx.data_len = 10
        f = HttpFD(ctx.canceled, MockYDL(ctx), ctx.params)
        result = ctx.result = mock.MagicMock()
        # Test: success
        ctx.data = mock.MagicMock()
        ctx.data.read.side_effect = [
            b'aaa',
            b'bb',
            b'c',
            b''
        ]
        ctx.stream = mock.MagicMock()
        result.return_value = True
        f.real_download(ctx, 0, 10)

# Generated at 2022-06-14 15:55:10.481822
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Create a dummy output file
    with io.open('test_HttpFD.out', 'wb') as outf:
        outf.write(b'Testing the downloader\n')

    def _hook(_):
        pass

    df = HttpFD({'noprogress': True, 'quiet': True}, _hook)
    url = 'https://github.com/rg3/youtube-dl/blob/master/LICENSE?raw=true'
    # Test that a file with partial download can be resumed

# Generated at 2022-06-14 15:55:19.624805
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os.path
    import sys
    import tempfile
    import threading
    import time
    import urllib.error
    import urllib.parse
    import urllib.request
    from io import BytesIO

    from .compat import bytes_to_intlist
    from .utils import (
        format_bytes,
        encodeFilename,
        sanitize_open,
        sanitized_Request,
        write_xattr,
    )

    from .http import HttpFD
    from .http import compat_urllib_request
    from .http import compat_urllib_error
    from .http import compat_urllib_parse

    TIMEOUT = 3.0


    class FakeServer(object):
        def __init__(self, **kwargs):
            self.kwargs = kwargs

# Generated at 2022-06-14 15:55:31.679965
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import BytesIO
    from urllib.parse import urlsplit
    headers = {'Content-Type': 'text/html'}
    url = 'http://127.0.0.1/'
    body = b'<html>\n</html>'
    data = BytesIO(body)
    hd = HttpFD(data, headers, url)
    # url
    assert url == hd.url
    assert url == hd.geturl()
    assert urlsplit(url).netloc == hd.host
    # content
    assert body == hd.read()
    # headers
    assert headers == hd.headers

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:55:39.988410
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import io
    fd = io.BytesIO(b'\xe2\x98\x83\n\xe2\x98')
    assert HttpFD(fd, {}).read(100) == b'\xe2\x98\x83\n\xe2\x98'
    assert HttpFD(fd, {}).read(2) == b'\xe2\x98'
    assert HttpFD(fd, {}).read(100) == b''
    fd = io.BytesIO(b'\xe2\x98\x83\n\xe2\x98')
    assert HttpFD(fd, {}, test=True).read(2) == b'\xe2\x98'
    assert HttpFD(fd, {}, test=True).read(2) == b'\x83\n'