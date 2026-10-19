

# Generated at 2022-06-14 15:48:40.081128
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """Test real_download method for class HttpFD

    Arguments:
    --download-archive specifies a file into which all downloaded files'
    names will be written, one per line. This option is useful for
    resuming downloads.

    --min-filesize 1KB  do not accept any video smaller than 1KB as
                        successfully downloaded.

    --max-filesize 100KB do not accept any video larger than 100KB as
                        successfully downloaded.

    --test
        Download a test file to see whether the user-agent, cookies and
        proxies are correctly set.

    """
    fail_msg = 'test_HttpFD_real_download failed with reason: '
    url = 'http://127.0.0.1/file/1MB'

# Generated at 2022-06-14 15:48:51.503701
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """Function that tests the method real_download of the class HttpFD.

    It checks that a file with a given size is correctly downloaded by the
    method of a given HttpFD object.

    :param fd:
        The HttpFD object whose method will be tested.
    """

    # HttpFD object that will be used for testing
    fd = HttpFD(FakeYDL(), None, None)
    # Expected size of the downloaded file
    size_file = 1024
    # Tests the real_download method
    res = fd.real_download(FakeYDL(), url="http://localhost:8000",
        filename="-", info_dict={}, params={},
        add_header_row=None, test=True)
    assert(res)
    assert(fd.total_bytes == size_file)


# Generated at 2022-06-14 15:49:03.706151
# Unit test for constructor of class HttpFD
def test_HttpFD():
    c = HttpFD(params={'quiet': True}, ydl=DummyYDL())
    c.report_warning('warning')
    c.report_error('error')
    c.to_stderr('error')
    c.to_screen('error')
    # simulated file
    class SimulatedSocket(object):
        def __init__(self, test_fd, *args, **kwargs):
            self._test_fd = test_fd
        def makefile(self, _mode, _other):
            return self._test_fd

# Generated at 2022-06-14 15:49:13.093381
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test open with ChunkedEncodingError (extractor/common.py)
    CHUNKED_ENCODING_ERROR = compat_HTTPError('http error', None, None, None, StringIO('a'))
    CHUNKED_ENCODING_ERROR.fp._CHUNKED_ENCODING_ERROR = True

# Generated at 2022-06-14 15:49:23.936063
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Implement unit test for method real_download of class HttpFD

    # This file is not guaranteed to exist
    url = 'http://ipv4.download.thinkbroadband.com/100MB.zip'
    real_download(url, '100MB.zip', None, {})
    real_download(url, '100MB.zip', None, {}, {'test': True})
    real_download(url, '100MB.zip', None, {}, {'test': True, 'nooverwrites': True})
    real_download(url, '100MB.zip', None, {}, {'test': True, 'continuedl': True})

# Generated at 2022-06-14 15:49:32.474544
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    DP = DownloadProgressMock()
    FD = HttpFD(DP, {})
    # Test for a simple file, no retries, no resume
    stream_mock = StreamMock('range')
    result = FD.real_download(FD, 'test1', stream_mock, 'ab', 100, 0, 0, None)
    assert result
    assert stream_mock.range_start == 0
    assert stream_mock.range_end == 99
    assert DP.downs == [((0, 100), 'test1')]
    # Test for a simple file, no resume
    stream_mock = StreamMock('range')
    result = FD.real_download(FD, 'test2', stream_mock, 'ab', 100, 0, 1, None)
    assert result
    assert stream_mock.range_start

# Generated at 2022-06-14 15:49:38.446755
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Mock YDL class to get a correct __repr__
    class MockYDL(object):
        def __init__(self, params):
            self.params = params

    ydl = MockYDL({})
    fd = HttpFD(ydl, {'url': 'http://localhost/file'}, {})
    assert fd.__repr__()

# Generated at 2022-06-14 15:49:51.159223
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    min_filesize = 2**20
    max_filesize = 5*(2**20)
    params = {
        'nooverwrites': True,
        'continuedl': False,
        'noprogress': True,
        'logger': MockLogger(),
        'min_filesize': min_filesize,
        'max_filesize': max_filesize,
        'retries': 10,
        'socket_timeout': 60.0,
    }

# Generated at 2022-06-14 15:50:01.901711
# Unit test for constructor of class HttpFD
def test_HttpFD():
    params = {
        'usenetrc': False,
        'username': 'test',
        'password': 'test',
        'twofactor': None,
        'videopassword': None,
        'ap_mso': None,
        'ap_username': None,
        'ap_password': None,
        'noprogress': True,
        'quiet': True,
        'verbose': True,
        'retries': 0,
        'continuedl': False,
        'noresizebuffer': False,
        'logtostderr': False,
        'consoletitle': False,
        'nopart': False,
        'updatetime': False,
        'test': True,
    }


# Generated at 2022-06-14 15:50:09.633195
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import tempfile
    import urllib.request

    tn = tempfile.mkstemp(prefix='youtubedl-test-http-fd-')
    tn_name = tn[1]
    os.write(tn[0], b'foo')
    os.close(tn[0])

    tn_size = os.path.getsize(tn_name)

    with open(tn_name, 'rb') as f:
        tn_data = f.read()

    urlh = urllib.request.urlopen('file://' + quote(tn_name))
    tn_size_remote = int(urlh.headers['Content-length'])
    tn_data_remote = urlh.read()
    urlh.close()

    assert tn_size == tn_size_remote


# Generated at 2022-06-14 15:50:54.107979
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test interaction with file descriptor
    s = StringIO('foobar')
    fd = HttpFD(s, 0)
    assert fd.read(3) == 'foo'
    info = fd.info()
    assert info.getheader('Content-Type') == 'unknown/unknown'
    assert info.get_all('Content-Length') == [None]
    fd.close()

    # Test interaction with info dict
    s = StringIO('foobar')
    fd = HttpFD(s, 0, {'Content-Length': '6'})
    assert fd.read(3) == 'foo'
    info = fd.info()
    assert info.getheader('Content-Type') == 'unknown/unknown'
    assert info.get_all('Content-Length') == ['6']

# Generated at 2022-06-14 15:51:04.258378
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Batch run tests
    import glob
    import os.path

    for f in glob.glob(os.path.join(os.path.dirname(__file__), 'test', '*.py')):
        name = os.path.basename(f)
        if name.startswith('test_') and name.endswith('.py'):
            if name == 'test_real_download.py':
                continue
            __import__('test.%s' % name[:-3], locals(), globals())
            print('Testing %s' % name)
            test_module = sys.modules['test.%s' % name[:-3]]
            if getattr(test_module, '__test__', False) is False:
                print('ERROR: Test %s is disabled' % name)
                continue
            test

# Generated at 2022-06-14 15:51:13.156853
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD('http://www.gnu.org/software/gettext/manual/gettext.html')
    assert fd.real_url == 'http://www.gnu.org/software/gettext/manual/gettext.html'
    fd.close()
    fd = HttpFD('http://www.gnu.org/software/gettext/manual/gettext.html', params={'nofragments': True, 'testcookie': 'testvalue'})
    assert fd.real_url == 'http://www.gnu.org/software/gettext/manual/gettext.html'
    fd.close()


if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:51:26.204898
# Unit test for constructor of class HttpFD
def test_HttpFD():
    """Run the test for HttpFD."""
    import random
    import urlparse

    def test(total_len, block_len, start, end):
        url_info = urlparse.urlparse('http://example.com/test')
        headers = {'content-length': str(total_len)}
        http_test_server = compat_http_server.test_server_base.HttpServerTestBase(
            block_len=(block_len, block_len),
            content_length=(total_len, total_len),
            filename='test',
            headers=headers)
        http_test_server.start()
        ctx = {'tmpfilename': 'test', 'start_time': time.time()}
        h = HttpFD(ctx, url_info, {'start': start, 'end': end})

# Generated at 2022-06-14 15:51:34.498723
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .utils import compat_http_server
    from .utils import datetime_strptime
    from tempfile import NamedTemporaryFile
    from .compat import urllib_error

    class NoRangeRequestHandler(compat_http_server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-Length', '1024')
            self.end_headers()

            # not sending any response body to cause socket.error('unexpected EOF') upon download

    class RangeRequestHandler(compat_http_server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.headers.get('Range', None) is None:
                NoRangeRequestHandler.do_GET(self)
                return

            self.send_response(206)
           

# Generated at 2022-06-14 15:51:41.636902
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Create an instance
    h = HttpFD('http://localhost/', {'noprogress': True})
    # Check if get_size returns None
    assert h.get_size() is None
    # Check if name is empty
    assert h.name == ''
    # Check if real_download returns None
    assert h.real_download(False) is False

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:51:50.991016
# Unit test for method real_download of class HttpFD

# Generated at 2022-06-14 15:51:59.807767
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import tempfile
    (fd, fn) = tempfile.mkstemp()
    fd = os.fdopen(fd, 'wb')
    fd.write(b'content')
    fd.close()
    h = HttpFD(fn, (0, 3))
    assert h.read() == b'con'
    h.close()
    h = HttpFD(fn, (3, 6))
    assert h.readline() == b'tent'
    h.close()
    h = HttpFD(fn, None)
    assert h.readline() == b'content'
    h.close()
    os.remove(fn)

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:52:12.334058
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test with a valid URL
    http_fd = HttpFD('http://www.example.org', {'noprogress': True})
    assert isinstance(http_fd, HttpFD)
    http_fd.close()

    # Test with an invalid URL
    try:
        http_fd = HttpFD('http://not_a_valid_url', {'noprogress': True})
        http_fd.close()
        assert False
    except IOError:
        pass
    except Exception:
        assert False

    # Test invalid methods

# Generated at 2022-06-14 15:52:21.000520
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .extractor import gen_extractors

    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    params = {
        'usenetrc': '',
        'username': '',
        'password': '',
        'quiet': True,
        'forceurl': True,
        'forcetitle': True,
        'forcethumbnail': True,
        'forcedescription': True,
        'forcefilename': True,
        'forceduration': True,
        'forcejson': True,
    }

    # Test 1: Test that URL opener is created with custom context factory
    hd = HttpFD(gen_extractors(params), params, url)
    assert hd._opener.context_factory is not None

    # Test 2: Test that URL opener is

# Generated at 2022-06-14 15:53:22.345093
# Unit test for constructor of class HttpFD
def test_HttpFD():

    testdesc1 = ('http://www.google.com/index.html', {})
    testdesc2 = ('http://www.google.com/non_existent_file.html', {})
    for testdesc in [testdesc1, testdesc2]:
        fd = HttpFD(testdesc[0], testdesc[1])
        assert fd.url == testdesc[0], 'HttpFD(%s): url should be %s' % (testdesc, testdesc[0])
        assert fd.friendly_name() == fd.url, 'HttpFD(%s): friendly_name() should be %s' % (testdesc, fd.url)



# Generated at 2022-06-14 15:53:24.173683
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(u'http://localhost/%C3%A4')
    assert fd.real_url == 'http://localhost/%C3%A4'



# Generated at 2022-06-14 15:53:34.025208
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from . import YoutubeDL
    from .utils import encodeFilename
    from .extractor import get_info_extractor

    ydl = YoutubeDL(params={
        'nooverwrites': True,
        'quiet': True,
        'simulate': True,
        'format': 'best',
        'outtmpl': '%(id)s%(ext)s',
    })
    data = {
        'id': 'testid'
    }
    ie = get_info_extractor(ydl, 'Generic')
    info_dict = {}
    ie._setup_download(info_dict, data)
    assert not ydl._is_live

    test_infile = __file__
    test_filesize = os.path.getsize(test_infile)

# Generated at 2022-06-14 15:53:43.044655
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    df = HttpFD(None, {'nooverwrites': True, 'noprogress': True})
    url = 'http://localhost:8080/test_file_%s'
    tmp_filename = 'test_file'
    filename = os.path.join(TEST_TMPDIR, 'test_file')
    df.params['test'] = True

    httpd = create_webserver(port=8080)

    # Test for correct download
    # (1) Assert return value equals True
    # (2) Assert that number of requests is equal to 1
    #
    httpd.data = 'Test file'
    httpd.resume_len = 0
    assert(df.real_download(url % 1, filename, tmp_filename=tmp_filename) == True)

# Generated at 2022-06-14 15:53:50.829027
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test method real_download with various download sizes.
    # `count` is the number of test iterations performed.
    # `count_pass` is the number of test iterations passed.
    count, count_pass = 0, 0
    for i in range(0, 600, 100):
        count += 1
        # Create a test file of size i. This file is retrieved by real_download().
        s = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(i)])# Create a test file of size i. This file is retrieved by real_download().
        s = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(i)])
        test_file = io.BytesIO(s.encode('ascii'))

        #

# Generated at 2022-06-14 15:54:03.105939
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import http.server as http_server
    import threading
    import time

    import youtube_dl

    class MyHandler(http_server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello HTTP!')

    srvr = http_server.HTTPServer(('0.0.0.0', 0), MyHandler)
    thread = threading.Thread(target=srvr.serve_forever)
    thread.daemon = True
    thread.start()
    time.sleep(0.2)

# Generated at 2022-06-14 15:54:15.410999
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .extractor import gen_extractors
    from .utils import ExtractorError

    fd = HttpFD(gen_extractors(), params={'noprogress': True})
    filename = fd.prepare_filename('test_%(title)s_%(id)s')
    assert filename == 'test_-_-'


# Generated at 2022-06-14 15:54:24.731199
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import os
    import datetime
    import tempfile
    import urllib
    import random
    import string
    from subprocess import Popen, PIPE, STDOUT
    from .downloader import FileDownloader
    from .extractor.common import InfoExtractor
    from .extractor.youtube import YoutubeIE

    class MockYoutubeIE(YoutubeIE):
        def _real_extract(self, url):
            return self.url_result(url, 'Youtube', video_id=url, video_title=url)

    def rm_rf(path):
        def _onerror(func, path, exc_info):
            if not os.access(path, os.W_OK):
                # Is the error an access error?
                os.chmod(path, stat.S_IWUSR)

# Generated at 2022-06-14 15:54:37.316113
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    # File with given size (in bytes) will be created in a current directory
    # to test if HttpFD.real_download() works properly
    FILE_SIZE = 1024

    class TestServer(object):
        """
        A simple http server that serves a file of specified size, simulating
        different network conditions
        """
        def __init__(self, file_size):
            assert file_size > 0
            self.file_size = file_size
            self.written_bytes = 0
            self.start_time = time.time()

        def serve_file(self, filename):
            if filename == '/':
                self.written_bytes = 0
                self.start_time = time.time()  # resetting time

# Generated at 2022-06-14 15:54:42.025073
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    import io
    import os
    import shutil
    import sys
    import tempfile

    from youtube_dl.utils import encodeFilename

    def close_all():
        for fd in fds:
            if fd is not None and not fd.closed:
                fd.close()

    def open_file(params):
        to_stdout = params.get('outtmpl') == '-' or (
            params.get('continuedl') and params.get('nopart'))
        if to_stdout:
            fd = sys.stdout
            if fd.encoding is None:
                fd = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            tmpfilename = '-'
        else:
            fd, tmpfilename = tempfile.mkstemp()

# Generated at 2022-06-14 15:56:39.322375
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test all three cases of the constructor:
    # Case 1: Both 'urlhandle' and 'filename' are not None.
    # Case 2: 'urlhandle' is not None and 'filename' is None.
    # Case 3: 'urlhandle' is None and 'filename' is not None.


    class FakeURLHandle(object):
        pass


    class FakeFileHandle(object):
        pass


    # Case 1
    fd1 = HttpFD(FakeURLHandle(), FakeFileHandle())
    if not (fd1.urlhandle is not None and fd1.filename is not None and fd1.handle is None):
        print('Test 1 failed!')
        sys.exit(1)

    # Case 2
    fd2 = HttpFD(FakeURLHandle(), None)

# Generated at 2022-06-14 15:56:44.899985
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def check_read():
        chunk = hfd.read(8192)
        assert isinstance(chunk, bytes_stdin)
        assert len(chunk) <= 8192
        return chunk
    hfd = HttpFD(urllib2.urlopen('http://www.example.com'), 'rb', 8192, None, None)
    assert hfd.read(0) == b''
    assert hfd.read(1) == b'<'
    assert hfd.read(2) == b'!d'
    assert hfd.read(8191) == check_read()
    assert hfd.read() == check_read()
    assert hfd.read() == check_read()
    assert hfd.read1(1) == b'>'

# Generated at 2022-06-14 15:56:52.350117
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import tempfile
    from .utils import encodeFilename
    from .extractor import get_suitable_downloader
    from .downloader import YoutubeDL
    from .compat import compat_urllib_error

    # Get an extractor
    ydl = YoutubeDL({})
    ie = get_suitable_downloader(ydl, 'http://example.com/video.htm')

    # Create a temporary file
    tfn = tempfile.mkstemp()[1]
    filename = encodeFilename(tfn)

    # Get correctly written data
    data = (b'http://example.com/video.htm', {}, {'noprogress': True}, None)
    ie.extract_info(data)
    correct_data = ie._downloader.ydl.cache.load(*data[:-1])

    # Write data

# Generated at 2022-06-14 15:56:57.080770
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # The following are necessary for the unit test
    class FakeYTDL(object):
        def __init__(self):
            self.params = {'nooverwrites': False, 'quiet': True,
                    'ratelimit': None, 'retries': 10,
                    'continuedl': True, 'noresizebuffer': False,
                    'test': True, 'min_filesize': 1, 'max_filesize': 10000000000,
                    'buffersize': None, 'noprogress': False, 'logger': None,
                    'outtmpl': '%(id)s-%(title)s.%(ext)s'}
        def urlopen(self, req):
            return FakeUrlOpen(req)
    class FakeUrlOpen(object):
        def __init__(self, req):
            self.req

# Generated at 2022-06-14 15:57:06.472029
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import BytesIO
    total_bytes = 33000
    block_size = 3000
    h = HeadRequestHandler()
    body = b'\0'*total_bytes
    h.protocol_version = 'HTTP/1.0'
    h.wfile = BytesIO()
    h._write_headers()
    h.send_header('Content-Length', str(total_bytes))
    h.end_headers()
    h.wfile.write(body)

    fd = HttpFD(h, block_size)
    assert hasattr(fd, 'name')
    assert fd.name == '<http>'
    assert hasattr(fd, 'mode')
    assert fd.mode == 'rb'
    assert hasattr(fd, 'closed')
    assert not fd.closed
    assert has

# Generated at 2022-06-14 15:57:17.123063
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # _TEST_FILE_SIZE is set to 5MB
    TEST_FILE_URL = 'http://ipv4.download.thinkbroadband.com/5MB.zip'
    TEST_FILE_SIZE = 5242880
    # This method is too long and complex, so we've decided to make use
    # of a simple unit test.
    # Unfortunately, unittest module is not available on python 2.6
    # so we must resort to this.
    # The idea here is download a fixed-size file and make sure the
    # returned object has the expected size
    # Create the object
    ydl_opts = {
        'simulate': True,
        'quiet': True,
        'min_filesize': TEST_FILE_SIZE,
        'max_filesize': TEST_FILE_SIZE,
    }

# Generated at 2022-06-14 15:57:21.372971
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test with real HTTP server
    from .utils import prepend_extension
    from .extractor import gen_extractors
    from .downloader import gen_ydl_info_extractors
    test_url = 'http://127.0.0.1:8080/%s' % compat_urllib_parse.quote_plus('привет мир.txt')
    info_dict = {
        'id': 'test video',
        'ext': 'txt',
        'title': 'test привет',
        'requested_formats': [{
            'url': test_url,
        }],
    }
    for ie in gen_extractors():
        for ie_result in ie.extract(test_url):
            assert ie_result is not None

# Generated at 2022-06-14 15:57:22.050400
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # TODO: write this test function
    pass


# Generated at 2022-06-14 15:57:26.677112
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    class FakeYDL:
        def urlopen(*urlopen_args, **urlopen_kwargs):
            if urlopen_args[1].get_full_url().startswith('http://127.0.0.1/chunked'):
                info_dict = {'content-type': 'text/plain'}

                class FakeResponse(object):
                    def __init__(self, code):
                        self.code = code

                    def info(self):
                        return info_dict

                    def read(self, size=1):
                        return b'a' * size

                if urlopen_args[1].get_full_url().endswith('/206'):
                    return FakeResponse(206)

# Generated at 2022-06-14 15:57:36.007095
# Unit test for constructor of class HttpFD
def test_HttpFD():
    url = 'http://www.youtube.com/watch?v=BaW_jenozKc'