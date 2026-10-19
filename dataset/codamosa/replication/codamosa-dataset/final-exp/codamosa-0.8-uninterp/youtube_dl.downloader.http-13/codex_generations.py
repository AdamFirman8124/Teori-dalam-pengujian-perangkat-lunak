

# Generated at 2022-06-14 15:48:45.015484
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test 1: Test default arguments:
    fd = HttpFD(None, params={'noprogress': True})
    assert fd.ydl is None
    assert fd.params['noprogress'] == True
    # Test 2: Test non-default arguments:
    fd = HttpFD({"foo": "bar"}, params={'noprogress': True})
    assert fd.ydl == {"foo": "bar"}
    assert fd.params['noprogress'] == True

if __name__ == '__main__':
    from .utils import get_suitable_downloader
    downloader = get_suitable_downloader('http')

# Generated at 2022-06-14 15:48:54.138420
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # _TEST_FILE_SIZE should be even, as it's split in half in the test
    class TestHttpFD(HttpFD):
        _TEST_FILE_SIZE = 1000

    info_dict = {
        'id': 'test',
        'display_id': 'test',
        'title': 'test',
        'ext': 'test',
        'format': 'test',
        'format_id': 'test',
    }

    def test_real_download(self):
        raise Exception('This should not be called.')

    class YDL:
        params = {
            'continuedl': True,
            'nooverwrites': True,
            'retries': 10,
            'test': True,
        }


# Generated at 2022-06-14 15:49:07.868239
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os
    import sys
    import shutil
    import tempfile
    import types
    import atexit
    import json
    import subprocess
    import contextlib

    @contextlib.contextmanager
    def _stdout():
        old = sys.stdout
        sys.stdout = io.StringIO()
        try:
            yield sys.stdout
        finally:
            sys.stdout = old

    async def async_print(*args, **kwargs):
        await asyncio.sleep(0)
        print(*args, **kwargs)

    def get_test_data_dir():
        return os.path.join(os.path.dirname(__file__), 'test_data')


# Generated at 2022-06-14 15:49:16.977813
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from . import YoutubeDL
    ydl = YoutubeDL()
    # Test with non-existant urls
    for url in ['http://127.0.0.1/nonexistant',
                'ftp://127.0.0.1/nonexistant',
                'https://127.0.0.1/nonexistant']:
        try:
            h = HttpFD(ydl, url)
            assert False
        except DownloadError:
            pass

    # Test with a nonexistent file
    try:
        h = HttpFD(ydl, 'http://127.0.0.1/nonexistant', {'noprogress': True})
        h.close()
        assert False
    except DownloadError:
        pass

# unit test for download function

# Generated at 2022-06-14 15:49:28.994024
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """Tests downloading a file with HTTP protocol using class HttpFD.

    Run with this command: youtube-dl --dump-intermediate-pages --test-httpfd
    """
    # Test parameters. Change at your will.
    test_url = 'https://www.iana.org/domains/example/'
    # Uncomment the next line for HTTP/1.0 test
    # test_url = test_url.replace('https://', 'http://', 1)
    # We would like to download only a portion of the file, so we just get a
    # few bytes. We may request several millions bytes and still get just few
    # kilobytes.
    # test_url += "robots.txt"
    # test_url += "foo/bar/baz.html"
    test_chunk_size = 8192
    test_

# Generated at 2022-06-14 15:49:39.724603
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import sys

    def test_equals(a, b):
        assert a == b, '%s != %s' % (a, b)

    dl = HttpFD(None, params={
        'usenetrc': False,
        'username': 'user',
        'password': 'pass',
    })
    test_equals(dl.ydl.params['http_header_names'], [
        'User-Agent',
        'Cookie',
        'Accept-Charset',
        'Accept-Encoding',
        'Connection',
        'Referer',
        'Range',
    ])

# Generated at 2022-06-14 15:49:52.340986
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    '''
    This function downloads a test file from the internet.
    '''

    # Settings
    _TEST_FILE_SIZE = 150000
    _TEST_URL = 'http://ipv4.download.thinkbroadband.com/200MB.zip'
    _TEST_TMP_FILENAME = '200MB.zip'

    # Action
    http_fd = HttpFD()
    http_fd._TEST_FILE_SIZE = _TEST_FILE_SIZE
    success = http_fd.real_download(
        {'url': _TEST_URL, 'filename': _TEST_TMP_FILENAME, 'test': True},
        {'test': True})

    # Assertion
    assert success
    assert os.path.exists(_TEST_TMP_FILENAME)
   

# Generated at 2022-06-14 15:49:57.522816
# Unit test for constructor of class HttpFD
def test_HttpFD():
    h = HttpFD('http://www.yahoo.com',
               {'outtmpl': '%(id)s.%(ext)s',
                'id': 'foo'})
    assert h.get_filename() == 'foo.flv'

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:50:08.557850
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test constructor of HttpFD
    source_url = 'http://www.quirksmode.org/html5/videos/big_buck_bunny.mp4'
    dest_file = 'big_buck_bunny.mp4'
    tmp_dest_file = dest_file + '.part'
    urlhandle = compat_urllib_request.urlopen(source_url)
    f = HttpFD(urlhandle, tmp_dest_file, dest_file)
    assert not f.closed
    assert f.mode == 'wb'
    assert f.tmpfilename == tmp_dest_file
    assert f.name == dest_file
    length = f.info().get('Content-Length')
    assert length is not None
    assert int(length) > 0

    # Downloading a small file
    max_blocks = 10

# Generated at 2022-06-14 15:50:16.563512
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test the file descriptor constructor
    # Note: it will be a compressed file by default
    fd = HttpFD('http://upload.wikimedia.org/wikipedia/commons/1/12/White_Rhino_Ceratotherium_simum.ogg')
    assert fd.size() > 0
    assert fd.size() == fd.get_size()
    assert fd.size() == fd.info().get('size', 0)
    assert fd.size() == fd.info().get('total_bytes', 0)
    assert not fd.data().info().get('Content-Encoding')
    assert fd.filename
    assert fd.get_filename()



# Generated at 2022-06-14 15:50:55.808219
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test_setup(func):
        def wrapper(*args, **kwargs):
            tmp_filename = tempfile.NamedTemporaryFile(delete=False).name
            kwargs['tmp_filename'] = tmp_filename
            try:
                return func(*args, **kwargs)
            finally:
                if os.path.exists(tmp_filename):
                    os.remove(tmp_filename)

        return wrapper

    @test_setup
    def test_1(tmp_filename):
        """Normal download"""

        def content_length(bytes_range):
            assert bytes_range == (0, None)
            return 5

        def get_data(bytes_range):
            assert bytes_range == (0, None)
            return b'12345'


# Generated at 2022-06-14 15:51:06.274589
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from youtube_dl.utils import DateRange
    from youtube_dl.utils import match_filter_func
    from youtube_dl.utils import encode_compat_str

    class FakeYDL:
        def __init__(self, params):
            self.params = params

        def report_destination(self, *args, **kwargs):
            pass

        def report_progress(self, *args, **kwargs):
            pass

        def urlopen(self, *args, **kwargs):
            class FakeHTTPResponse:
                def __init__(self, info, data, url=None):
                    self.info = lambda: info
                    self._data = data
                    self.geturl = lambda: url

                def read(self, n):
                    ret = self._data[:n]
                    self._data = self._

# Generated at 2022-06-14 15:51:18.575372
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # (path, content)
    to_create = [
        ('1', '1' * 100), ('2', '2' * 10), ('3', '3' * 100), ('4', '4' * 100), ('5', '5' * 100)]
    with make_server(to_create) as server:
        fd = HttpFD('http://localhost:%s/%s' % (server.port, '1'), 'wb', params=dict(noprogress=True))
        assert fd.real_download(params=dict(max_filesize=100))
        assert fd.downloaded == 100
        assert not os.path.exists(fd.tmpfilename)
        assert fd.tmpfilename == fd.filename
        assert open(fd.filename, 'rb').read() == b'1' * 100



# Generated at 2022-06-14 15:51:29.696342
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    orig_urlretrieve = compat_urllib_request.urlretrieve
    test_counter = [0]
    def urlretrieve(url, filename, reporthook=None, data=None):
        # The following strings are ordered in such a way, that the expected
        # output is correct when running the test on a console with utf-8 encoding.
        test_counter[0] += 1
        if test_counter[0] == 1:
            assert filename == '/home/user/test.flv'
            assert '\r\033[K[download]   0.0% of 42.00MiB at  0.00KiB/s ETA 42:00' in reporthook(0, 42 * 1024 * 1024, 42 * 1024 * 1024)

# Generated at 2022-06-14 15:51:42.286772
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # It's downloading https://dev.ytdl-org.github.io/test-file.dat via https
    # then checks its size.
    # Note: _TEST_FILE_SIZE is set to 2^10, so only first 1 KiB is actually downloaded
    from .urlrequest import compat_urllib_request, compat_urllib_error
    compat_urllib_request.install_opener(compat_urllib_request.build_opener(compat_urllib_request.HTTPHandler()))
    test_file_url = 'https://dev.ytdl-org.github.io/test-file.dat'
    retval = {}

# Generated at 2022-06-14 15:51:54.342602
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test_urlopen(request):
        class Foobar:
            def read(self, n):
                return b'foobar'
            def info(self):
                return {'Content-Length': '6'}

        class Requests(list):
            def get_full_url(self):
                return ''

        class Response:
            def __init__(self, code, msg):
                self.code = code
                self.msg = msg
                self.headers = {'Content-Length': '6'}

            def info(self):
                return self.headers

            def getcode(self):
                return self.code

        if isinstance(request, Requests):
            return Response(200, 'OK')
        elif request.get_full_url() == 'http://example.com/video.mp4':
            return

# Generated at 2022-06-14 15:51:58.220882
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Most of the tests are in test_http.py
    fd_http = HttpFD()
    fd_https = HttpFD()
    tm = tempfile.NamedTemporaryFile()
    tm.write(b'foobar')
    tm.flush()
    tm.seek(0)
    fd_tempfile = TempFileWrapper(tm)
    fd_http.close()
    HttpFD.close(fd_https)
    fd_tempfile.close()



# Generated at 2022-06-14 15:52:10.856692
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def _download_chunk(httpfd, dl_func, chunk_size):
        ctx = {}
        ctx['data_len'] = 40
        httpfd.real_download(ctx, dl_func, chunk_size)
        return ctx.get('resume_len')

    # entire file should be downloaded
    assert _download_chunk(HttpFD({}, DummyYDL()), None, 0) == 0
    assert _download_chunk(HttpFD({}, DummyYDL()), None, 20) == 0
    assert _download_chunk(HttpFD({}, DummyYDL()), None, 40) == 0

    # broken file of size 10 should be downloaded
    assert _download_chunk(HttpFD({}, DummyYDL()), lambda: 10, 0) == 10
    assert _download_chunk

# Generated at 2022-06-14 15:52:20.237474
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .compat import parse_qs
    from .utils import USER_AGENT

    # The test string has to start with "C" to avoid the risk of accidentally
    # hitting an existing file on the test system
    TESTFN = 'CYaHPOZHPsFZDdkgiJBo.test'
    TESTFN_UNICODE = '\xe0d2kw\x0c\x04\xa1s\xf7\x0btest'
    TEST_DATA = b'foobarbaz'

    class HeaderWrapper(object):
        def __init__(self, headers):
            self._headers = headers

        def getheaders(self, name):
            return self._headers.get(name)


# Generated at 2022-06-14 15:52:31.115246
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def noop(*args, **kwargs):
        pass

    def mocked_urlopen(req):
        return compat_urllib_request.addinfourl(
            compat_urllib_request.BytesIO(b'spam eggs'), 'fake header', req.get_full_url())

    fd = HttpFD(
        compat_urllib_request.Request('http://foo/bar'), {}, {}, {}, None, 'rb', {})
    fd.ydl.urlopen = mocked_urlopen
    fd.to_screen = noop
    fd.to_stderr = noop
    fd.report_error = noop
    fd.report_retry = noop
    fd.report_resuming_byte = noop
    fd.report_destination = noop

# Generated at 2022-06-14 15:54:13.715956
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    url = 'http://example.com/'
    params = {
        'format': 'best',
        'nooverwrites': True,
        'nocheckcertificate': True,
    }
    # a io.BytesIO subclass that raises socket.error with ECONNRESET errno on read() after certain amount of bytes
    class ECONNRESETBytesIO(io.BytesIO):
        def __init__(self, *args, **kwargs):
            io.BytesIO.__init__(self, *args, **kwargs)
            self._read_bytes = 0
        def read(self, *args, **kwargs):
            data = io.BytesIO.read(self, *args, **kwargs)
            self._read_bytes += len(data)

# Generated at 2022-06-14 15:54:19.851409
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # If a filename is not explicitly given,
    # then we download a test file using wget
    fd = HttpFD('http://ipv4.download.thinkbroadband.com/200MB.zip')
    content = fd.read(8192)
    fd.close()
    # If we have downloaded successfully the test file,
    # the content must start with the string
    if not content.startswith('PK'):
        raise AssertionError('Test file not downloaded')

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:54:33.181500
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def noop_downloader(*args, **kwargs):
        pass
    downloader = noop_downloader

    fd = HttpFD(downloader)
    d = fd._real_download
    # Check that the methods called by fd._real_download are the expected ones
    fd._hook_progress = lambda status: test_equal(status['status'], 'finished')
    d(dict(url='http://localhost/'))

    # Test without authentification
    fd.ydl = FakeYDL({'username': None, 'password': None})
    fd._hook_progress = lambda status: test_equal(status['status'], 'downloading')
    d(dict(url='http://localhost/'))

    # Test with authentification

# Generated at 2022-06-14 15:54:36.181736
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD('http://youtube-dl.org/homepage.html', {'test': 'Test param'})
    fd.retrieve()


# Generated at 2022-06-14 15:54:45.936122
# Unit test for constructor of class HttpFD
def test_HttpFD():
    class FakeHeadRequest(compat_urllib_request.Request):
        def get_method(self):
            return 'HEAD'
    req = FakeHeadRequest('http://localhost/test.mp4', headers={'Range': 'bytes=0-1023'})
    fd = HttpFD(req)
    assert fd.read(100) == b'\0' * 100
    assert fd.read(100) == b'\0' * 100
    assert fd.tell() == 200
    assert fd.seek(50) == 50
    assert fd.read(10) == b'\0' * 10

    req = FakeHeadRequest('http://localhost/test.mp4')
    fd = HttpFD(req)
    assert fd.read(100) == b'\0' * 100

# Generated at 2022-06-14 15:54:55.742040
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # set up global variables
    global stdout_binary_mode, stdin_binary_mode, stderr_binary_mode
    
    # remember the old stdout
    old_stdout = sys.stdout
    # print something to console
    print(u'\nTesting HttpFD.real_download()')
    
    # turn off buffering
    old_stdout.flush()
    
    # remember the old stdin
    old_stdin = sys.stdin
    # print something to console
    print(u'\nTesting HttpFD.real_download()')
    
    # turn off buffering
    old_stdin.flush()
    
    # remember the old stderr
    old_stderr = sys.stderr
    # print something to console

# Generated at 2022-06-14 15:55:07.904468
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import pathlib
    import tempfile
    import shutil
    test_dir = 'C:/Users/root/Documents/GitHub/YTDownloader/test/'#str(pathlib.Path(tempfile.gettempdir())/'test_http_fd/')
    http_fd = HttpFD()
    http_fd.params['continuedl'] = False
    http_fd.params['format'] = 'bestvideo+bestaudio'
    http_fd.params['nocheckcertificate'] = True
    http_fd.params['restrictfilenames'] = False
    http_fd.params['outtmpl'] = os.path.join(test_dir, '%(title)s-%(id)s.%(ext)s')

# Generated at 2022-06-14 15:55:18.166207
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('-- testing HttpFD class --')
    class TestDownloader(object):
        def __init__(self, params):
            self.params = params
        def to_screen(self, s):
            print(s)
        def to_stderr(self, s):
            self.to_screen(s)
        def trouble(self, s):
            raise Exception(s)
        def report_error(self, s):
            raise Exception(s)
        def report_warning(self, s):
            print(s)
        def slow_down(self, start, now, byte_counter):
            return
        def best_block_size(self, elapsed_time, bytes_downloaded):
            return 1024 * 8
        def calc_speed(self, start, now, bytes_downloaded):
            return 512 * 1024

# Generated at 2022-06-14 15:55:30.954640
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    # Given argument "url" with a valid URL to an existing file
    url = "http://archive.org/download/gissou.na.khaab/gissou.na.khaab_512kb.mp4"

    # And args dict with urls and params keys
    # (NOTE: "retries" and "continuedl" could be omitted since the default values would be used for them)
    args_dict = {
        "urls": [url],
        "params": {
            "retries": 2,
            "continuedl": False,
            "logger": None,
        },
    }

    # And get_bytes_range is a function that returns None
    def get_bytes_range(url):
        return None

    # And write_xattr is a function that returns None

# Generated at 2022-06-14 15:55:35.983390
# Unit test for constructor of class HttpFD
def test_HttpFD():
    handle, tmpfilename = tempfile.mkstemp()
    os.close(handle)
    fd = HttpFD(tmpfilename, -1, 10, 10)
    assert fd.read(5) == b'\0' * 5
    assert fd.read(5) == b'\0' * 5
    fd.close()
    os.remove(tmpfilename)