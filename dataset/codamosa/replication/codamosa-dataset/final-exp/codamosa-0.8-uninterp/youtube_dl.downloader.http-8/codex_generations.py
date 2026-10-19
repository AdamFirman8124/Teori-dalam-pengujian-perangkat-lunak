

# Generated at 2022-06-14 15:48:38.556655
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor import get_info_extractor
    from .extractor.common import InfoExtractor
    from .compat import USER_AGENT
    from .utils import format_bytes

    class FakeIE(InfoExtractor):
        def __init__(self, downloader=None):
            super(FakeIE, self).__init__(downloader)
            self._test_url = 'http://localhost/video.mp4'
            self._test_data_len = 2000000
            self._test_chunk_size = 1000000


# Generated at 2022-06-14 15:48:50.334614
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # 'url' is just some string that should make sanitize_url() return
    # the same string
    url = 'https://github.com/ytdl-org/youtube-dl/pull/1567'
    # 'data' is a list of strings that should constitute the data of
    # the returned string when read by read()
    data = ['Hello, world!\n']
    # 'headers' is a dict-like object that should be returned by
    # getheaders()
    headers = {
        'Content-Type': 'text/plain',
        'Content-Length': str(len(data[0])),
    }
    c = _HttpFD(url, data, headers)
    assert c.read() == data[0]
    assert c.read() == ''
    assert c.read() == ''

# Generated at 2022-06-14 15:48:57.603687
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(
        'http://www.youtube.com/watch?v=BaW_jenozKc',
        {'noprogress': True, 'retries': 10},
        '#t=1,2',
        {'url': 'http://www.youtube.com/watch?v=BaW_jenozKc'})
    assert fd.url == 'http://www.youtube.com/watch?v=BaW_jenozKc&t=1,2'
    assert fd.byte_count == 0

# The following is a test for the downloader

# Generated at 2022-06-14 15:49:10.744964
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os
    import shutil
    import tempfile
    import unittest
    import urllib.request

    class TestHttpFD(HttpFD):
        def __init__(self):
            HttpFD.__init__(self)
            self.params = {
                'noprogress': True,
                'logger': False,
                'test': True,
            }

        def report_error(self, *args, **argsv):
            pass

        def report_retry(self, *args, **argsv):
            pass

        def report_destination(self, *args, **argsv):
            pass

        def report_resuming_byte(self, *args, **argsv):
            pass

        def report_unable_to_resume(self, *args, **argsv):
            pass

# Generated at 2022-06-14 15:49:24.625508
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import os
    import tempfile
    from .utils import encodeFilename

    def urlretrieve(url, filename):
        assert url != '-'
        assert filename != '-'
        assert url in ('http://fake/video.mp4', 'http://fake/audio.mp3')
        if os.path.exists(encodeFilename(filename)):
            os.remove(encodeFilename(filename))
        open(encodeFilename(filename), 'wb').write(b'foobarbazqux' + url.encode('utf-8'))
        return os.path.getsize(encodeFilename(filename))

    def urlopen(request):
        assert request.get_full_url() in ('http://foo/bar.flv', 'http://foo/bar.mp4', 'http://foo/bar.ogg')
        assert request

# Generated at 2022-06-14 15:49:32.815107
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class FakeFile:
        def __init__(self, data=[]):
            self.data = data
            self.pos = 0

        def close(self):
            pass

        def __exit__(self):
            pass

        def read(self, length):
            # to check the state of 'before' and 'after' variables
            print('read:', self.pos, length)
            return self.data[self.pos : self.pos + length]

        def info(self):
            return { 'Content-length': sum(len(x) for x in self.data) }

    class FakeSocket:
        def __init__(self):
            pass

        def __call__(self, *args, **kwargs):
            return self.download(*args, **kwargs)


# Generated at 2022-06-14 15:49:41.298431
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Use test HTTP server located on localhost
    url = 'http://localhost:%d/' % (HttpServer.getPort(),)
    # Request a small file
    hfd = HttpFD(None, {'nooverwrites': True, 'continuedl': True})
    test_file = hfd.real_download(url, None)
    # Now compare its contents with contents of a known test file
    with open(test_file, 'rb') as f:
        content = f.read()
    with open('%s/%s' % (os.path.split(__file__)[0], '__testfile'), 'rb') as f:
        test_content = f.read()

# Generated at 2022-06-14 15:49:53.383196
# Unit test for constructor of class HttpFD
def test_HttpFD():
    tfn = 'http_test.txt'
    try:
        # test open_file
        content = b'http test file\n'
        with open(tfn, 'wb') as f:
            f.write(content)

        fd = HttpFD(None, tfn, 'wb')
        assert fd.name == tfn

        fd.write(b'hello\n')
        fd.close()

        with open(tfn, 'rb') as f:
            content = f.read()
        assert content == b'hello\n'

        # test open_url
        fd = HttpFD(None, 'http://google.com/nonexistent', 'wb')
        fd.close()

    finally:
        os.remove(tfn)


# Unit tests for the downloader #################################

# Generated at 2022-06-14 15:50:03.989855
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class FakeYDL(object):
        def __init__(self):
            self.params = {
                'ratelimit': 0,
                'retries': 10,
                'buffersize': 1024,
                'noresizebuffer': False,
                'test': True,
                'continuedl': False,
                'noprogress': False,
            }

        def to_screen(self, msg):
            print(msg)

        def trouble(self, msg, tb=None):
            print(msg)
            if tb:
                print(tb)

        def urlopen(self, req):
            class FakeUrlopen(object):
                def __init__(self):
                    self._len = 0

# Generated at 2022-06-14 15:50:06.568606
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Members
    h = HttpFD()
    assert h.params == {}
    assert h.ydl is None
    assert isinstance(h, FileDownloader)


# Generated at 2022-06-14 15:50:49.925322
# Unit test for constructor of class HttpFD
def test_HttpFD():
    myparams = {
        'noprogress': True,
        'logger': DummyLogger(),
        }
    dl = HttpFD(myparams)
    assert dl.params == myparams
    assert dl.prebuffer_size == 131072
    dl.to_screen('test')
    dl.to_stderr('test')
    dl.report_error('test')
    dl.report_warning('test')
    dl.report_retry('test', 1, 3)
    dl.report_file_already_downloaded('test')
    dl.report_unable_to_resume()
    dl.report_destination('test')
    assert dl.calc_percent(100, 100) == 100.0
    assert dl.calc_

# Generated at 2022-06-14 15:51:01.438395
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Fake import of 'encodeFilename' since this module imports BaseFD and
    # 'encodeFilename' from YoutubeDL.
    __builtins__.encodeFilename = lambda x: x
    return HttpFD(None, {}, None)

if __name__ == '__main__':
    # Test output format
    params = {
        'outtmpl': '%(title)s-%(id)s-%(autonumber)s.%(ext)s',
        'restrictfilenames': True,
        'nooverwrites': False,
    }
    # Test downloader
    d = HttpFD(params, {}, None)
    # Test file names
    info = {
        'id': 'test',
        'title': 'test',
        'url': 'http://test',
    }

# Generated at 2022-06-14 15:51:12.034969
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import platform
    if platform.system() == 'Linux':
        # This test should NOT be run on any other platform than Linux
        from .extractor.common import InfoExtractor
        from .utils import sanitize_open

        class TestIE(InfoExtractor):
            def report_warning(self, message):
                print(message)

        params = {'username': 'user', 'password': 'pass'}
        ie = TestIE(params)
        ie.to_screen = lambda message: print(message)
        assert ie.auth_info == params

        # 100MB
        filesize = 100 * 1024 * 1024
        # 5MB chunks
        chunksize = 5 * 1024 * 1024

        # Create a temporary file of known length

# Generated at 2022-06-14 15:51:24.788295
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # In this test we don't actually use ydl, so we can pass None
    fd = HttpFD(None, {'url': 'http://example.org/video.mp4'})
    # Test that a method that returns the size of the content raises an exception
    # if called before download()
    assert_raises(AssertionError, fd.get_size)
    assert_raises(AssertionError, fd.real_download, ('http://example.org/video.mp4', None), {}, {}, None)
    # The size is still unavailable
    assert_raises(AssertionError, fd.get_size)
    # Test that real_download() doesn't raise an exception
    fd.real_download(('http://example.org/video.mp4', None), {}, {}, None)

# Generated at 2022-06-14 15:51:33.819591
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from io import BytesIO
    from argparse import Namespace
    from youtube_dl.utils import sanitize_open
    from youtube_dl.downloader.http import HttpFD
    from youtube_dl.downloader.common import (
        limit_length,
        ContentTooShortError,
        FILE_NAME_MP4,
        FILE_NAME_UNKNOWN,
        FILE_NAME_HLS,
    )
    # Handle stdout
    def _stdout_write(s):
        pass
    # Handle debug
    def _debug_print(s):
        pass
    # Handle to_stderr
    def _to_stderr(s):
        pass

    class FakeYDL():
        params = Namespace()


# Generated at 2022-06-14 15:51:45.028061
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import sys
    import tempfile
    import testserver
    def test_construct(expected_status_code, **params):
        server = testserver.TestServer(expected_status_code)
        try:
            fd = HttpFD(server.server.host, server.server.port, params)
            if expected_status_code == 200:
                assert fd.status == 200
                body = fd.read()
                assert isinstance(body, bytes)
                assert body == b'hello world'
            else:
                assert fd.status == expected_status_code
        finally:
            server.terminate()
    test_construct(200)
    test_construct(200, range=None)
    test_construct(206, range=(0, 5))
    test_construct(416, range=(10, 15))
   

# Generated at 2022-06-14 15:51:57.116996
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def test(_ctx):
        _ctx.data_len = 40000
        if _ctx.chunk_size == 20000 and _ctx.resume_len == 0:
            # block size for the first chunk
            _ctx.block_size = 1000
        elif _ctx.chunk_size == 20000 and _ctx.resume_len == 20000:
            # block size for the second chunk
            _ctx.block_size = 2000
        else:
            raise ValueError('Strange values: %s' % _ctx)
        class DummyFile(object):
            def __init__(self):
                self.pos = 0
            def read(self, num):
                assert num == _ctx.block_size
                if self.pos == _ctx.data_len:
                    return b''

# Generated at 2022-06-14 15:52:09.949637
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Number of HttpFD instances created
    http_fd_counter = [0]

    class _HttpFD(HttpFD):
        # Override HttpFD._real_download() to avoid downloading anything
        def _real_download(self, *args, **kwargs):
            return

        def __init__(self, ydl, params):
            # count HttpFD instances
            http_fd_counter[0] += 1

            # record constructor arguments
            self.ydl = ydl
            self.params = params

            # call constructor of super class
            super(_HttpFD, self).__init__(ydl, params)

    # create an instance of YoutubeDL
    class _YoutubeDL(YoutubeDL):
        def __init__(self, *args, **kwargs):
            super(_YoutubeDL, self).__init__

# Generated at 2022-06-14 15:52:19.735040
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def retrieve_url(url, filename, **kwargs):
        fd = HttpFD(None, {})
        return fd.real_download(url, filename, **kwargs)

    for charset_urls in [['ascii', 'utf-8'], ['ascii', 'idna']]:
        for data in {'utf-8': b'\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba',
                     'idna': b'\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba',
                     'ascii': b'aeiou'}.items():
            url_prefix = 'http://test.test/'

# Generated at 2022-06-14 15:52:30.852373
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor import gen_extractors
    from .downloader.external import ExternalFD

    # We silence requests' logger
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    for ie in gen_extractors():
        if ie.IE_NAME == 'Youtube':
            url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
            ie = ie(ydl=YoutubeDL(params={'nocheckcertificate': True}))
            info_dict = ie.extract(url)

            # Check first video format
            video_url = info_dict['formats'][0]['url']
            fd = HttpFD(YoutubeDL(params={'nocheckcertificate': True}), video_url)
            fd.real

# Generated at 2022-06-14 15:54:03.030247
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(
        'http://www.example.com/video.flv',
        'wb',
        {'noprogress': True, 'quiet': True},
        None,
        None
    )

    assert fd.name == 'http://www.example.com/video.flv'
    assert fd.mode == 'wb'
    assert isinstance(fd.ydl, YoutubeDL)
    assert fd.params['noprogress'] == True


# Generated at 2022-06-14 15:54:11.906026
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    data = b'happy'
    class Info: pass
    class YDL:
        params = {'test': True}
        def to_screen(self, s): print(s)
        def to_stderr(self, s): print(s)
        def fix_url(self, s): return s
        def urlopen(self, req):
            data_len = req.headers.get('Content-Length')
            assert data_len == '5' or data_len is None
            res = compat_http_client.HTTPResponse(
                compat_http_client.HTTPConnection('127.0.0.1'),
                buffering=False)
            res.read = lambda n: data[n] if n < len(data) else b''
            res.close = lambda: None
            return res

# Generated at 2022-06-14 15:54:20.807065
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    fd = HttpFD(None)
    fd._TEST_FILE_SIZE = 1000
    # Data block size logic
    # If server does not advertise data block size, should be limited to _TEST_FILE_SIZE
    # but not less than 10k and not greater than 1M
    assert fd.best_block_size(10, 10) == fd._TEST_FILE_SIZE
    assert fd.best_block_size(10, 10) <= fd._TEST_FILE_SIZE
    assert fd.best_block_size(10, 10) <= 1048576
    assert fd.best_block_size(10, 10) >= 10240
    # If server advertises data block size, should not exceed it
    assert fd.best_block_size(10, 100) == 100
    # Minimum block size is

# Generated at 2022-06-14 15:54:34.163239
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import tempfile
    import unittest

    class Params(dict):
        def get(self, *args, **kwargs):
            return dict.get(self, *args, **kwargs)

        def __getitem__(self, *args, **kwargs):
            return dict.__getitem__(self, *args, **kwargs)

        def __setitem__(self, *args, **kwargs):
            return dict.__setitem__(self, *args, **kwargs)

    class FakeYoutubeDL(object):
        def __init__(self, params):
            self.params = params
            self.to_stderr = lambda msg: None
            self.to_screen = lambda msg: None
            self.report_error = lambda msg: None

# Generated at 2022-06-14 15:54:39.132658
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test data
    test_url = 'http://ipv4.download.thinkbroadband.com/1GB.zip'
    test_file = 'test_file'
    test_data_len = 1048576000
    # Create mock objects
    self_mock = Mock(params={'ratelimit': None, 'retries': 0, 'buffersize': '16384'})
    self_mock.report_destination = Mock(side_effect=lambda filename: self_mock.last_report_destination_filename == filename)
    self_mock.report_error = Mock(side_effect=lambda err: self_mock.last_report_error_msg == err)

# Generated at 2022-06-14 15:54:48.325878
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('-- running test_HttpFD...')
    import unittest
    import tempfile
    import shutil
    import time
    import os
    import sys
    import subprocess
    import fcntl
    import select

    class HttpFDTest(unittest.TestCase):
        def setUp(self):
            self.test_dir = tempfile.mkdtemp(prefix='youtubedl-test-unit-httptools-')
            self.server_proc = subprocess.Popen([
                sys.executable,
                '-m', 'http.server', '--bind', '127.0.0.1', '0'
            ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, cwd=self.test_dir)
            server_line = self.server_

# Generated at 2022-06-14 15:54:59.783735
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class _FakeYDL(object):

        def __init__(self, *args, **kwargs):
            self.params = {}

        def to_screen(self, msg):
            self._screen_msg = msg

        def urlopen(self, request, *args, **kwargs):
            class _FakeResp(object):

                def __init__(self, data_blocks):
                    self._data_blocks = data_blocks

                def info(self):
                    return {'Content-length': str(sum(map(len, self._data_blocks)))}

                def read(self, n):
                    content = self._data_blocks.pop(0)
                    return content[:n]

            class _FakeUrllibError(object):

                def __init__(self, reason):
                    self.reason = reason


# Generated at 2022-06-14 15:55:12.059213
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test constructor without params
    dl = HttpFD()
    assert dl.params['retries'] == 10
    assert dl.params['continuedl'] == True
    assert dl.params['noprogress'] == False
    assert dl.params['sleepinterval'] == 5
    assert dl.params['max_sleep_interval'] == 15

    # Test with params
    params = {
        'noprogress': True,
        'sleepinterval': 3,
        'max_sleep_interval': 10,
        'continuedl': False,
        'retries': 5,
        'test': True
    }
    dl = HttpFD(params)
    assert dl.params['retries'] == 5
    assert dl.params['continuedl'] == False
    assert dl

# Generated at 2022-06-14 15:55:17.248932
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ydl = YoutubeDL()
    ydl.prepare_filename = lambda x: x
    url = 'http://example.com/video.mp4'
    fd = HttpFD(ydl, url, {'noprogress': True})
    assert fd.url == url
    assert fd.ydl is ydl

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:55:23.001669
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import copy
    from youtube_dl.FileDownloader import FileDownloader
    from youtube_dl.compat import compat_urllib_request
    from tempfile import mkstemp
    from urlparse import urlparse
    from os import unlink, close, remove
    from errno import EISDIR

    # We just have to have a FileDownloader instance for HttpFD to work
    ydl = FileDownloader()
    ydl.params['nooverwrites'] = True

    def test_download(ydl, tmpfilename, url, params):
        fd = orig_HttpFD(ydl, tmpfilename, url, params)
        fd.real_download()
        return fd.downloaded_bytes

    # Basic test, 1 byte download