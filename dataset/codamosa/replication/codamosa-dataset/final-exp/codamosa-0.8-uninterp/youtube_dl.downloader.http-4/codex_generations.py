

# Generated at 2022-06-14 15:48:40.150338
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from . import compat_urllib_request
    from .utils import urlopen

    # This unit test can be used to simply test a download
    # Manually change block_size, when simulating a webserver without
    # support for Range header to allow producing an invalid header
    # Also change ctx.data_len if you want to test (partial) redownload
    class ctx: pass
    ctx.filename = 'testfile'
    ctx.tmpfilename = 'testfile.part'
    ctx.data = None
    ctx.data_len = None
    ctx.stream = None
    ctx.open_mode = 'wb'
    ctx.resume_len = 0
    ctx.chunk_size = None
    ctx.block_size = 1024*1024
    ctx.start_time = time

# Generated at 2022-06-14 15:48:51.546175
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    urlopen = compat_urllib_request.urlopen
    Request = sanitized_Request
    urlretrieve = compat_urllib_request.urlretrieve
    socket = compat_socket
    try:
        import ssl
    except ImportError:
        ssl = None
    class MockSocket:
        def __init__(self, *args, **kwargs):
            self._file = io.BytesIO()
            self.read_data = compat_b('')
            self.read_data_idx = 0
            self.read_data_len = None
            self.read_exhausts_data = False
            self.writable = io.BytesIO()

        def makefile(*args, **kwargs):
            return self._file

        def settimeout(self, timeout):
            pass


# Generated at 2022-06-14 15:49:03.704728
# Unit test for constructor of class HttpFD
def test_HttpFD():
    """
    Constructor of class HttpFD should not raise any exceptions for
    correct parameters.
    """
    # Base case
    h = HttpFD(None, {}, None)
    assert h is not None

    # Retry exceptions
    h = HttpFD(None, {}, None, retry_exceptions=())
    assert h is not None

    # Retry delay
    h = HttpFD(None, {}, None, retry_delay=300)
    assert h is not None

    # Max retries
    h = HttpFD(None, {}, None, max_retries=5000)
    assert h is not None

    # Custom headers
    h = HttpFD(None, {}, None, extra_headers={'Referer': 'http://www.example.com'})
    assert h is not None

   

# Generated at 2022-06-14 15:49:14.065503
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ydl = FakeYDL()
    info_dict = {'url':'http://127.0.0.1:3128/10MiB',
                 'http_headers':{}}
    fd = HttpFD(ydl, info_dict, {'continuedl':True, 'nooverwrites':True})
    assert fd.ydl is ydl
    assert fd.url == info_dict['url']
    assert fd.http_headers == info_dict['http_headers']
    assert fd.params == {'continuedl':True, 'nooverwrites':True}
    assert fd.resume_len == 0
    assert fd.start_time == 0.0


# Generated at 2022-06-14 15:49:20.531396
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    # This video is a bit long: 1000 seconds long
    YOUTUBE_VIDEO_ID = "Hj_1Q2eRlOg"
    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v=Hj_1Q2eRlOg'
    YOUTUBE_VIDEO_TITLE = 'David Gilmour - Rattle That Lock (Official Music Video)'

    # This video is very short: 10 seconds long
    # YOUTUBE_VIDEO_ID = "EwTZ2xpQwpA"
    # YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v=EwTZ2xpQwpA'
    # YOUTUBE_VIDEO_TITLE = 'youtube-dl test video "\'/\\ä↭𝕐'



# Generated at 2022-06-14 15:49:31.076704
# Unit test for constructor of class HttpFD
def test_HttpFD():
    assert HttpFD('http://www.google.com').size() > 0
    assert HttpFD('http://www.google.com/abcdefgh', 9).size() == 0
    assert HttpFD('http://www.google.com/abcdefgh', 9, 8).size() == 9
    assert HttpFD('http://www.google.com/abcdefgh', 8, 9).size() == 0
    assert HttpFD('http://www.google.com/abcdefgh', 8, -1).size() == 0
    assert HttpFD('http://www.google.com/abcdefgh', -1, 8).size() == 8
    assert HttpFD('http://www.google.com/abcdefgh', 0, 9).size() == 0

# Generated at 2022-06-14 15:49:43.486374
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # function name is not a typo
    def urlopen(request, data=None):
        class ContentTooShortError(compat_urllib_error.URLError):
            def __init__(self):
                pass
        class Response:
            def __init__(self, info, data):
                self.headers = compat_httplib_HTTPMessage(io.StringIO(info))
                self.data = data
            def read(self, size=None):
                if size is None:
                    chunk = self.data
                    self.data = ''
                    return chunk
                chunk = self.data[:size]
                self.data = self.data[size:]
                if len(self.data) == 0:
                    raise EOFError()
                return chunk
            def info(self):
                return self.headers


# Generated at 2022-06-14 15:49:55.086953
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor.common import InfoExtractor
    from .utils import HEADRequest, encodeArgument
    from .compat import compat_urllib_error
    import tempfile
    import shutil
    import random
    import re


    class MockYoutubeDl(object):
        def __init__(self):
            self.params = {'ratelimit': 1048576, 'retries': 10}

        def to_screen(self, message):
            pass

        def trouble(self, message, tb=None):
            pass

        def report_error(self, message, tb=None):
            pass

        def report_warning(self, message):
            pass

        def report_retry(self, message, count, retries):
            pass


# Generated at 2022-06-14 15:50:05.323480
# Unit test for constructor of class HttpFD
def test_HttpFD():
    downer = HttpFD()
    # Test HTTP download
    actual_filename = downer.try_download('http://127.0.0.1:' + str(test_port) + '/', {})
    if actual_filename != 'video.flv':
        raise ValueError('Wrong filename')
    # Test HTTP download (with 'Content-Disposition' header)
    actual_filename = downer.try_download('http://127.0.0.1:' + str(test_port) + '/Disposition', {})
    if actual_filename != 'another_video.flv':
        raise ValueError('Wrong filename')
    # Test HTTP download (with 'Content-Type' header)

# Generated at 2022-06-14 15:50:15.430809
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Create an instance
    h = HttpFD(
        _YoutubeDL({'noprogress': True}),
        'http://localhost/fo%20o/ba%7a.mp4',
        {'test_param': 'value'},
        'foobar',
        {'updatetime': False})

    # Test _prepare_request
    request = h._prepare_request()
    assert isinstance(request, compat_urllib_request.Request)
    assert request.get_full_url() == 'http://localhost/fo%20o/ba%7a.mp4'
    # Test header construction
    header_test_cases = [
        ('user-agent', 'youtube-dl/%s' % __version__),
        ('test_param', 'value'),
    ]

# Generated at 2022-06-14 15:51:00.024107
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test_part(f, expected_size, expected_status):
        part_size = 10
        ctx = DownloadContext(f, 'GET', {}, part_size)
        fd = HttpFD(ctx, 0)
        success = fd._real_download(is_test=True)
        assert success == (expected_status == 'finished')
        assert ctx.data_len == expected_size
        assert ctx.resume_len == 0
        assert ctx.open_mode == 'wb'
        if expected_status == 'finished':
            # Let's check that the expected data from the test file is there
            assert open(ctx.filename, 'rb').read() == b'Dead beef'

    # Test file

# Generated at 2022-06-14 15:51:10.613687
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test HttpFD's constructor
    counter = [0]  # some mutable
    def myread(size):
        counter[0] += 1
        if counter[0] == 1:
            return b'\n[download]   '
        elif counter[0] == 2:
            return b''
        elif counter[0] == 3:
            return b'filename.mp4'
        else:
            return b''
    h = HttpFD(myread, {'content-type': 'text/html'}, 'http://example.com/video.mp4', 'video.mp4', {})
    # readline
    assert h.readline() == b'[download] video.mp4 has already been downloaded'
    assert h.readline() == b''
    # fileno
    assert h.fileno()

# Generated at 2022-06-14 15:51:11.766114
# Unit test for constructor of class HttpFD
def test_HttpFD():
    pass



# Generated at 2022-06-14 15:51:22.702616
# Unit test for constructor of class HttpFD
def test_HttpFD():
    assert isinstance(HttpFD('http://www.example.com/a', {}, '-'), FileDownloader)
    assert isinstance(HttpFD('http://www.example.com/a', {}, 'a/b.txt'), FileDownloader)
    assert isinstance(HttpFD('http://www.example.com/a', {}, 'a/b.txt'), FileDownloader)
    assert isinstance(HttpFD('http://www.example.com/a', {}, '-'), FileDownloader)
    assert isinstance(HttpFD('http://www.example.com/a', {}, None), FileDownloader)

# Test for download function of class HttpFD

# Generated at 2022-06-14 15:51:32.535357
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from io import BytesIO
    from youtube_dl.FileDownloader import FileDownloader
    from youtube_dl.utils import format_bytes
    from youtube_dl.utils import encodeFilename

    fd = HttpFD(FileDownloader())

    # Placeholder for progress hook
    def progress_hook(status):
        pass

    stream = BytesIO()
    fd._do_download(
        dict(url='http://example.com/video', filename='-'),
        {'min_filesize': 10, 'max_filesize': 100, 'continuedl': True},
        {'test': True},
        stream, 'video',
        progress_hook)
    assert len(stream.getbuffer()) == fd._TEST_FILE_SIZE


# Generated at 2022-06-14 15:51:43.989053
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def download(self):
        params = {
            'format': 'best',
            'noprogress': True,
            'outtmpl': '%(id)s.%(ext)s',
        }

# Generated at 2022-06-14 15:51:56.046547
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Create temporary directory and file paths
    TEMP_DIR = tempfile.mkdtemp()
    TEMP_FILE_PATH1 = os.path.join(TEMP_DIR, 'tmp.file1')
    TEMP_FILE_PATH2 = os.path.join(TEMP_DIR, 'tmp.file2')
    # Build params dictionaries
    params1 = {'noprogress': True, 'retries': 0, 'ratelimit': 0, 'noresizebuffer': True}
    params2 = {'noprogress': True, 'retries': 0, 'ratelimit': 0, 'noresizebuffer': True, 'test': True}
    # Build instance of HttpFD
    hfd = HttpFD(HtmlFD(), params1)
    # Test HttpFD.real_download() method
    assert hfd

# Generated at 2022-06-14 15:52:07.608924
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import io
    r = compat_urllib_request.Request('http://www.example.com/')
    u = compat_urllib_request.urlopen(r)
    fd = HttpFD(u, 'wb')
    # Test the valid read range
    fd.seek(0)
    fd.read(5)
    fd.seek(2)
    fd.read(3)
    # Test the invalid read range
    fd.seek(1)
    fd.read(10)
    # Test the invalid write range (HTTP object do not support 'w' mode)
    payload = io.BytesIO(b'a'*10)
    fd.write(payload.read(10))

# Generated at 2022-06-14 15:52:18.271257
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class FakeYDL:
        params = {}
        def to_screen(self, msg):
            print(msg)
        def to_stderr(self, msg):
            print(msg)
        def urlopen(self, url_or_req, data=None, retries=None, timeout=None, headers=None):
            class FakeDownloader:
                def __init__(self, content, headers):
                    self.content = content
                    self.headers = headers
                def read(self, bytes_to_read):
                    if bytes_to_read >= len(self.content):
                        content = self.content
                        self.content = b''
                        return content
                    content = self.content[:bytes_to_read]
                    self.content = self.content[bytes_to_read:]
                    return content

# Generated at 2022-06-14 15:52:29.428234
# Unit test for constructor of class HttpFD
def test_HttpFD():
    tf = TempFile('test_httpfd').close()
    tf.seek(0, 2)
    tf.w.write('abcdef')
    tf.close()

    test_values = [('test_httpfd', 0, None),
                   ('test_httpfd', 0, 2),
                   ('test_httpfd', 3, None),
                   ('test_httpfd', 3, 2),
                   ('test_httpfd', 6, None),
                   ('test_httpfd', 6, 2),
                   ('test_httpfd', 7, None),
                   ('test_httpfd', 7, 2)]
    for (fn, pos, size) in test_values:
        tf = HttpFD(fn, pos, size)
        assert tf.size == size
        assert tf.pos == 0
        tf.close()

    tf = HttpFD

# Generated at 2022-06-14 15:54:06.284770
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def GetConnection():
        class InfoDict(object):
            def __init__(self):
                self.info = {}
                self.headers = {}
            def get(self, name, default=None):
                return self.info.get(name, default)
            def read(self, size):
                return b''
            def close(self):
                pass
        class InfoDictWithContentLength(InfoDict):
            def __init__(self, content_length):
                super(InfoDictWithContentLength, self).__init__()
                self.info['Content-Length'] = str(content_length)
        class InfoDictWithContentRange(InfoDict):
            def __init__(self, start, end, length):
                super(InfoDictWithContentRange, self).__init__()
                self.headers

# Generated at 2022-06-14 15:54:17.590448
# Unit test for constructor of class HttpFD
def test_HttpFD():
    """Test HttpFD constructor"""
    r = compat_urllib_request.Request('http://www.example.com')
    r.add_header('User-Agent', 'Test Agent')
    h = HttpFD(r, None, 'wb', 17, 9, lambda: False)
    assert h.length == 17
    assert h.byte_counter == 9
    assert h.start == 0
    assert h.end == 16
    assert h.user_agent == 'Test Agent'

    h = HttpFD(None, 'http://www.example.com', 'wb', 17, 9, lambda: False)
    assert h.length == 17
    assert h.byte_counter == 9
    assert h.start == 0
    assert h.end == 16
    assert h.user_agent == 'youtube-dl/'+__version__

# Generated at 2022-06-14 15:54:20.532449
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    fd = HttpFD('http://127.0.0.1:8081/?test', {'test_download': True}, 'rb')
    fd.real_download('-')


# Generated at 2022-06-14 15:54:33.886691
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def test_basic_url(url, params={}):
        # Test basic download
        # Open file
        fd = HttpFD(test_basic_url.ydl, url, params)
        # Read all data
        s = fd.read()
        fd.close()
        assert(s == b'foobar')
        # Check that file size matches the one specified
        assert(fd.size == len(s))
        # Check filename
        assert(re.match(r'^[a-zA-Z0-9_-]+\.(?:part\.mp4|flv|f4v|webm|mkv|mp3|aac)$', fd.title))
        # Check that file is not considered as a real stream
        assert(not fd.is_live)
    test_basic_url.yd

# Generated at 2022-06-14 15:54:44.148302
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    This function tests the real_download method in class HttpFD.
    """
    # A few test functions
    def _test_no_testfile(params, info_dict):
        """Test function that should not work with the test file."""
        raise AssertionError(
            'This test should not be run with a test file.')

    def _test_chunks(params, info_dict):
        """Download the file in chunks."""
        params['testchunksize'] = 200
        return download_with_http_fallback(params, info_dict)

    def _test_seekable(params, info_dict):
        """Download the file in any way possible, just check that it is seekable."""
        download_with_http_fallback(params, info_dict)

# Generated at 2022-06-14 15:54:53.207197
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Assume public/private keys for unit test
    # We don't want to pollute the keystore with our test keys
    params = {
        'key': 'test',
        'noprogress': True,
        'nopart': True,
        'quiet': True,
        'retries': 3,
    }
    urlh = compat_urllib_request.urlopen(_TEST_GPG_KEY_URL)
    # Download a small file
    small_test_file_url = 'https://raw.githubusercontent.com/rg3/youtube-dl/master/youtube_dl/version.py'
    # Expected length of small file
    small_test_file_bytes = int(urlh.info().get('Content-Length'))
    # Download a large file

# Generated at 2022-06-14 15:55:04.436286
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Prepare parameters
    params = {
        'noprogress': False,
        'progress_with_newline': True,
        'continuedl': False,
        'ratelimit': None,
        'retries': 10,
        'warc_filename': 'dummy.warc.gz',
        'test': False,
    }

    class FakeYDL(object):
        def __init__(self):
            self.params = params

        def to_screen(self, message):
            pass

        def trouble(self, message, tb=None):
            raise Exception(message)

        def report_error(self, message, tb=None):
            raise Exception(message)

        def report_warning(self, message):
            pass


# Generated at 2022-06-14 15:55:15.912467
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test 1. Simple download
    h = HttpFD(
        'http://www.youtube.com/watch?v=BaW_jenozKc', {'nooverwrites': True})
    assert h.get_filename() == 'youtube-BaW_jenozKc.flv'
    # Test 2. Download with custom output template
    h = HttpFD(
        'http://www.youtube.com/watch?v=BaW_jenozKc',
        {'nooverwrites': True, 'outtmpl': '%(id)s.%(ext)s'})
    assert h.get_filename() == 'BaW_jenozKc.flv'
    # Test 3. Test conflict resolution

# Generated at 2022-06-14 15:55:21.415752
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import json
    from .YoutubeDL import YoutubeDL

    class DummyYDL(YoutubeDL):
        def __init__(self, *args, **kwargs):
            super(DummyYDL, self).__init__(*args, **kwargs)
            self._info_dict = {}

        def process_info(self, info_dict):
            self._info_dict = info_dict

    ydl = DummyYDL({
        'quiet': True,
        'simulate': True,
        'skip_download': True,
        'nooverwrites': True,
        'outtmpl': '%(id)s.%(ext)s',
    })

    def _test(url, expected_info_dict, expected_retcode):
        retcode = ydl.download([url])
        info_dict

# Generated at 2022-06-14 15:55:31.995691
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """This function tests HttpFD's real_download method"""
    class TestFD(object):
        """A test file downloader that raises an exception on download"""

        def __init__(self, params):
            self.params = params
            self.to_screen = lambda *args, **kargs: True

        def real_download(self, filename, info_dict):
            """This is the method that has to be tested"""
            raise Exception('This is just a dummy exception')

    hfd = HttpFD('http://example.com/dummy.mp4', {}, TestFD)
    assert hfd.real_download('-', {}) is False

