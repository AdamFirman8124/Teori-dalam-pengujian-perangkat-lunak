

# Generated at 2022-06-14 15:48:37.176284
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Constructor should not raise any exception on well-formed URLs
    for good_url in ['http://127.0.0.1/', 'http://www.example.com/',
            'http://user:passwd@www.example.com/',
            ]:
        HttpFD(good_url, {'noprogress': True})

    # Constructor should raise URLRequiredError on empty URL
    try:
        HttpFD('', {'noprogress': True})
        raise AssertionError('URLRequiredError not raised')
    except URLRequiredError:
        pass

    # Constructor should raise MaxDownloadsReached on more than 10 redirects

# Generated at 2022-06-14 15:48:45.866263
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # reading from
    h = HttpFD('http://www.google.com/', None, {}, {})
    s = h.read()
    assert (s.startswith(b'<!doctype html>'))
    assert (h.len == len(s))
    assert (h.tell() == len(s))

    # writing to
    h = HttpFD('http://www.google.com/', None, {}, {}, 'w')
    h.write(b'a')
    h.close()


# Generated at 2022-06-14 15:48:51.281748
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    from .extractor import gen_extractors, list_extractors
    from .post import YoutubeDL
    from .utils import urlopen, encodeFilename

    # Test _TEST_FILE_SIZE
    global _TEST_FILE_SIZE
    _TEST_FILE_SIZE = 64 * 1024

    ydl = YoutubeDL({'logger': YoutubeDL.std_logger, 'outtmpl': '-'})
    ydl._msg_queue = ydl._screen_file

    def test_download_url(url, info_dict, params=None, expected_bytes=None):
        def download(ydl, url, **params):
            url_handle = urlopen(url)
            url_handle.read()
            info_dict['url'] = url

# Generated at 2022-06-14 15:49:03.178061
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor.common import InfoExtractor
    from .utils import encode_compat_str
    from .compat import urlretrieve
    import os

    class TestIE(InfoExtractor):
        _WORKING = False
        _TEST = {
            'url': 'http://localhost:9000/',
            'file': 'test1.mp4',
            'info_dict': {
                'id': 'test1',
            },
            'expected_status': 200,
            'expected_status_test': None,
            'params': {
                'usenetrc': False,
                'username': 'test',
                'password': 'test',
            },
        }

        def report_download_webpage(self, *args, **kargs):
            pass


# Generated at 2022-06-14 15:49:11.513576
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # _TEST_FILE_SIZE is defined in real_download()
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL(dict(nooverwrites=True, forceurl=True, test=True))
    fd = HttpFD(
        ydl, dict(url='http://www.example.com/', filename='-'), lambda d: None,
        lambda d: False, lambda d: False)
    assert fd._TEST_FILE_SIZE == HttpFD.TEST_FILE_SIZE

# Generated at 2022-06-14 15:49:24.680949
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():

    class DummyYDL(object):
        def __init__(self):
            self.params = {
                'noprogress': True,
                'retries': 3,
                'continuedl': True,
            }

        def to_screen(self, msg):
            print(msg)

    ydl = DummyYDL()
    fd = HttpFD(ydl, {'url': 'http://127.0.0.1:8080/1MB.dat'}, {'noprogress': True})
    assert not fd.real_download(
        'testfilename', {'url': 'http://127.0.0.1:8080/1MB.dat'}, {})

    import BaseHTTPServer
    import threading

    server_started = threading.Event()


# Generated at 2022-06-14 15:49:31.579831
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    ctx = DownloadContext()
    ctx.tmpfilename = '-'
    ctx.filename = '-'
    ctx.url = 'http://127.0.0.1:8080/tests/data/test_3_bytes.data'
    ctx.stream = io.BytesIO()
    ctx.block_size = 1024 * 1024
    ctx.start_time = time.time()
    ctx.resume_len = 0
    ctx.open_mode = 'wb'
    ctx.data_len = None
    ctx.chunk_size = 0
    ctx.has_range = False
    ctx.is_resume = False

    info_dict = {}

    hd = HttpFD()
    hd._hook_progress = lambda d: None

    assert hd.real_download

# Generated at 2022-06-14 15:49:44.184007
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # WARNING: This test is not meant to be executed independently.
    #          It's only a part of test_download.
    from .concurrent import PBar
    from .YoutubeDL import YoutubeDL

    class FakeYDL(YoutubeDL):
        def __init__(self):
            self.to_screen = lambda *x: None

    class FakePBar(PBar):
        def __init__(self):
            self.fd = sys.stdout
        def __enter__(self):
            return self
        def __exit__(self, ex_type, ex_value, ex_traceback):
            pass
        def update(self, a):
            pass

    ydl = FakeYDL()
    pbar = FakePBar()

    def slow_down(start, now, bytes_so_far):
        time.sleep

# Generated at 2022-06-14 15:49:55.994032
# Unit test for constructor of class HttpFD

# Generated at 2022-06-14 15:50:05.866748
# Unit test for constructor of class HttpFD
def test_HttpFD():
    http_fd = HttpFD('http://www.example.com', {}, None)
    assert http_fd.read(5) == b'Hello'
    assert http_fd.tell() == len(b'Hello')
    assert http_fd.read(5) == b''
    assert http_fd.tell() == len(b'Hello')
    http_fd.close()

    http_fd = HttpFD('http://www.example.com', {}, {'skip_download': True})
    assert http_fd.read(5) == b''
    assert http_fd.tell() == 0
    assert http_fd.read(5) == b''
    assert http_fd.tell() == 0
    http_fd.close()


# Generated at 2022-06-14 15:50:41.207700
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(
        url='http://www.example.com',
        filename='-',
        data=None,
        params={})
    assert fd.url == 'http://www.example.com'
    assert fd.filename == '-'
    assert fd.data is None
    assert fd.params == {}


# Generated at 2022-06-14 15:50:53.948020
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test HTTP download
    print('Testing HTTP download')
    # The following code is a test for the new HttpFD.real_download method. Steps:
    #  1) Create a temporary file of size at least _TEST_FILE_SIZE
    #  2) Create a HttpFD object
    #  3) Call real_download to download a part of the previously created temporary file
    #  4) Remove the temporary file

    tmp_filename = 'http_test_file'
    random_data = b'This is a test for the new HttpFD.real_download method.\n'
    f = open(tmp_filename, 'wb')
    for _ in range(HttpFD._TEST_FILE_SIZE // len(random_data)):
        f.write(random_data)
    f.close()
    http_fd = H

# Generated at 2022-06-14 15:51:04.192161
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def _test_downloader(ydl, expected_status, expected_filename, expected_headers, expected_count):
        class MyHttpFD(HttpFD):
            def __init__(self, ydl, filename, info_dict):
                HttpFD.__init__(self, ydl, filename, info_dict)
                self.count = 0
            def _do_download(self, url_or_request, filename, info_dict):
                self.count += 1
                assert url_or_request == expected_url or (isinstance(url_or_request, compat_urllib_request.Request) and url_or_request.get_full_url() == expected_url)
                assert filename == expected_filename
                assert info_dict == expected_info_dict
                assert set(self.ydl.http_headers.items())

# Generated at 2022-06-14 15:51:13.802188
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import test as _test
    import tempfile
    from ..downloader.common import FileDownloader
    from ..extractor import get_info_extractor
    from ..utils import encodeFilename
    from .http import HttpFD

    class FakeYDL(object):
        params = {
            'outtmpl': '/dev/null',
            'continuedl': False,
            'nooverwrites': False,
            'quiet': True,
            'ratelimit': None,
            'retries': 0,
            'buffersize': 8192,
        }

        def __init__(self, params):
            self.params = dict(self.params)
            self.params.update(params)

        def to_screen(self, *args, **kargs):
            pass


# Generated at 2022-06-14 15:51:26.740894
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test some expected behaviors
    import tempfile

    # 1) Test with a zero test file size
    tf = tempfile.NamedTemporaryFile()
    tf.close()
    downloader = HttpFD(
        {'nooverwrites': True, 'continuedl': False, 'noprogress': True})
    assert not downloader.real_download(
        {'url': 'http://127.0.0.1/?fill=0', 'test': True, 'filename': tf.name},
        None, 0)
    os.unlink(tf.name)

    # 2) Test with a test file size
    tf = tempfile.NamedTemporaryFile()
    tf.close()

# Generated at 2022-06-14 15:51:34.808708
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import inspect
    import random
    import os
    import io
    from ytdl_core.utils import webdl
    from ytdl_core.utils.data_structures import urlparse
    from ytdl_core.utils.file_io import striphtml
    import ytdl_core.utils.file_io
    from ytdl_core.compat import (compat_urllib_error, compat_urllib_request, comp_platform)
    from ytdl_core.compat.fd_utils import (compat_os_open, compat_os_fdopen, compat_os_fsync)
    from ytdl_core.compat.unquote_unreserved import compat_unquote_unreserved

# Generated at 2022-06-14 15:51:45.814989
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import tempfile
    fd, fname = tempfile.mkstemp(prefix='yt-dl-test-')
    os.close(fd)
    fd = open(fname, 'wb')
    fd.write(b'\0' * 1024 * 1024)
    fd.close()
    hfd = HttpFD(None, None, {'noprogress':True, 'retries':0})
    assert hfd.real_download({
        'filename': fname,
        'url': 'file:' + compat_urlquote(fname),
    }, {'test':True, 'quiet':True, 'format':'1'})
    assert os.path.exists(fname)
    hfd = HttpFD(None, None, {'noprogress':True, 'retries':0})


# Generated at 2022-06-14 15:51:57.750072
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Prepare
    url = 'https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi'
    info = {
        'url': url,
    }
    params = {
        'noprogress': False,  # simulate command-line args
        'forcetitle': True,   # simulate command-line args
        'continuedl': False,  # simulate command-line args
        'ratelimit': None,    # simulate command-line args
        'noresizebuffer': True,
        'test': True,  # enable test mode
    }
    # ydl = YoutubeDL(params)
    hdlfd = HttpFD(params, info)
    # Run and test

# Generated at 2022-06-14 15:52:03.165958
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    fd = HttpFD(temp_file.name, 'http://localhost/')
    fd.close()
    os.remove(temp_file.name)


# Generated at 2022-06-14 15:52:11.163155
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    sys.stderr = sys.stdout
    def hook(status):
        print(status)
    fd = HttpFD(hook)
    fd.params['nooverwrites'] = True
    fd.urlopen = lambda _: ['first', 'second']
    assert fd.real_download('http://example.com/test.mp4', 'test.mp4', 'test.tmp', 'wb')
    assert fd.real_download('http://example.com/test.mp4', 'test.mp4', 'test.tmp', 'wb')
    assert fd.real_download('http://example.com/test.mp4', 'test.mp4', 'test.tmp', 'wb', {'nooverwrites': False})

# Generated at 2022-06-14 15:53:35.518241
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def do_test(params, expected_result, expected_match_entry):
        from ..utils import cli_args
        from .options import readOptions
        opts = cli_args(('--%s=%s' % (k, v) for (k, v) in params.items()))
        if opts.verbose:
            opts.verbose += int(os.environ.get('YOUTUBEDL_DEBUG_VERBOSE', 0))
        opts.geturl = True

        opts.username = 'username'
        opts.password = 'password'
        opts.twofactor = '123456'
        opts.videopassword = 'video_password'
        opts.ap_username = 'ap_username'
        opts.ap_password = 'ap_password'


# Generated at 2022-06-14 15:53:47.153489
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import io
    import json
    import hashlib
    ydl = YoutubeDL(dict())
    # Test for default constructor
    data = b'abcdef'
    raw = compat_urllib_request.urlopen('http://127.0.0.1:9000/' + data.decode('ascii'))
    read_data = b''
    while True:
        new_data = raw.read(1)
        read_data += new_data
        if not new_data:
            break
    assert data == read_data
    raw.close()

    # Test for HttpFD constructor with only first parameter - data
    data = b'abcdef'
    hfd = HttpFD(ydl, data)
    read_data = b''

# Generated at 2022-06-14 15:53:58.161560
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Create the object to be tested
    h = HttpFD(None, {'continuedl': True, 'nooverwrites': True}, None)
    # Define the expected behaviour of method real_download

# Generated at 2022-06-14 15:54:09.863368
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test_real_download(ydl, params_get, filename, url, tmpfilename, info, retries, headers, chunk_size, res_code, content_length, num_blocks, block_size, data_length):
        class DummyYDL:
            def __init__(self, ydl):
                self.params = ydl.params

            def urlopen(self, request):
                class DummyResponse:
                    def __init__(self, headers):
                        self.headers = headers
                        self.code = res_code

                    def info(self):
                        return self.headers

                    def read(self, n):
                        if n > block_size:
                            n = block_size
                        return '0' * n

                return DummyResponse(headers)


# Generated at 2022-06-14 15:54:19.449912
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .extractor.common import InfoExtractor
    from .utils import DateRange

    class TestIE(InfoExtractor):
        def __init__(self, downloader=None):
            super(TestIE, self).__init__(downloader)

    ie = TestIE()


# Generated at 2022-06-14 15:54:20.882092
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    pass
    # FIXME: add unit test

# Generated at 2022-06-14 15:54:34.265316
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD('http://127.0.0.1/', None, {})
    print(repr(fd))
    print(fd.real_url)
    print(fd.headers)
    print(fd.get_header('content-type'))
    size = fd.get_size()
    print('Got size of %d' % size)
    read = fd.read(16)
    print('Read %d bytes: %r' % (len(read), read))
    read = fd.read(size)
    print('Read %d bytes: %r' % (len(read), read))
    # Now test the _retrieve() method
    fd2 = HttpFD('http://127.0.0.1/', 'http://127.0.0.1/', {})
   

# Generated at 2022-06-14 15:54:38.500974
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class _TestFD(HttpFD):
        def __init__(self, test, params, info_dict):
            HttpFD.__init__(self, params, info_dict)
            self.test = test

        def best_block_size(self, elapsed_time, bytes_downloaded):
            bs = HttpFD.best_block_size(self, elapsed_time, bytes_downloaded)
            self.test.assertTrue(bs > 0)
            return bs

        def slow_down(self, start_time, now, bytes_downloaded):
            pass

        def report_error(self, *args, **kargs):
            print(args, kargs)
            raise Exception(args)

        def report_retry(self, *args, **kargs):
            print(args, kargs)


# Generated at 2022-06-14 15:54:47.898477
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .extractor import gen_extractors
    from .extractor.common import InfoExtractor

    class MockYoutubeDL(object):
        def __init__(self, params):
            self._params = params
            self._ies = gen_extractors()

        @property
        def params(self):
            return self._params

        def to_screen(self, s):
            pass

        def report_warning(self, msg):
            pass

        def add_info_extractor(self, ie):
            self._ies.append(ie)


# Generated at 2022-06-14 15:54:58.770518
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ydl = YoutubeDL()
    ydl.params['continuedl'] = True
    ydl.params['simulate'] = True
    ydl.params['noprogress'] = True
    downer = HttpFD(ydl)
    downer.prepare_filename('http://www.example.com/')
    assert downer.info['tmpfilename'] == '-', 'output filename is set correctly'
    downer.prepare_filename('http://www.example.com/', 'abc.mp4')
    assert downer.info['tmpfilename'] == 'abc.mp4', 'output filename is set correctly'
    assert downer.info['filename'] == 'abc.mp4', 'output filename is set correctly'

    downer.prepare_filename('http://www.example.com/', 'abc.mp4')
