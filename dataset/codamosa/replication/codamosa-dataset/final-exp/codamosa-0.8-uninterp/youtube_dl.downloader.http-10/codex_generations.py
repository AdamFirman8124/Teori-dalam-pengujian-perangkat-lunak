

# Generated at 2022-06-14 15:48:40.307495
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from ytdl.utils import encodeFilename
    from ytdl.YoutubeDL import YoutubeDL
    import tempfile
    import shutil
    import sys

    def _run_func(func, *args):
        import ctypes
        FUNC = ctypes.CFUNCTYPE(ctypes.c_int)(func)
        return FUNC(*args)

    class _Stream(object):
        def __init__(self, fp):
            self.fp = fp
        def write(self, data):
            self.fp.write(data.decode('utf-8'))
        def close(self):
            self.fp.close()

    def _test_progress_hook(d):
        if d['status'] == 'downloading':
            dl_speed = d['speed']

# Generated at 2022-06-14 15:48:51.670552
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # A fake, public HTTP server
    class Server(object):
        def __init__(self, port):
            self._port = port
            self._server = None

        def __enter__(self):
            self._server = HTTPServer(('127.0.0.1', self._port), DummyHandler)
            self._server.timeout = 0.01
            self._server_thread = threading.Thread(target=self._server.serve_forever)
            self._server_thread.daemon = True
            self._server_thread.start()
            return self

        def handle_request(self):
            self._server.handle_request()

        def __exit__(self, type, value, traceback):
            self._server.shutdown()
            self._server.server_close()

# Generated at 2022-06-14 15:48:59.172904
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # It should not be possible to resume
    HttpFD.real_download(test_real_download_params('http://www.youtube.com/', {'http_chunk_size': 1000}))
    # But for this it should
    HttpFD.real_download(test_real_download_params('http://www.youtube.com/', {'http_chunk_size': None, 'http_skip_range': False}))
# HttpFD END



# Generated at 2022-06-14 15:49:02.265998
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import BytesIO
    hfd = HttpFD(BytesIO(b'test'), None, None)
    hfd.read(4)
    hfd.close()



# Generated at 2022-06-14 15:49:14.147624
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import io
    # Test compat_urllib_error.URLError
    urlopen_call_counter = 0
    def urlopen_side_effect(*args, **kwargs):
        nonlocal urlopen_call_counter
        urlopen_call_counter += 1
        if urlopen_call_counter == 1:
            raise compat_urllib_error.URLError('compat_urllib_error.URLError')
        return io.BytesIO(b'0123456789')
    with mock.patch('youtube_dl.utils.std_headers') as mock_std_headers:
        mock_std_headers.side_effect = lambda: {'User-Agent': 'test user agent'}
        with mock.patch('youtube_dl.utils.urlopen') as mock_urlopen:
            mock_

# Generated at 2022-06-14 15:49:26.695147
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import tempfile

    class FakeYDL:

        def __init__(self, params):
            self.params = params

        def to_screen(self, message):
            pass

        def to_stderr(self, message):
            pass

        def urlopen(self, request):
            # Make sure that the range header is set
            assert request.headers['Range']
            self.request_headers = request.headers
            self.request_url = request.full_url
            self.resume_len = int(request.headers['Range'][6:])  # skip 'bytes='
            return self

        def info(self):
            return {'Content-length': self._TEST_FILE_SIZE}

        def read(self, *args):
            return b'x' * args[0]  # return as many bytes as requested

# Generated at 2022-06-14 15:49:34.575901
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """Check that real_download behaves as expected with various arguments"""
    from .compat import urlopen
    from .utils import urlget_resume_retries
    from .extractor import get_info_extractor
    from .extractor.common import InfoExtractor
    # This helper class uses method real_download of class HttpFD
    class FakeYoutubeDL:
        def __init__(self, params):
            from .YoutubeDL import YoutubeDL
            self.params = params
            self.ydl = YoutubeDL(params)
        def to_screen(self, msg):
            # self.ydl.to_screen(msg)
            pass
        def urlopen(self, request):
            return urlopen(request)

# Generated at 2022-06-14 15:49:48.212091
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test HTTP connection
    print('Testing HTTP connection...')
    print('* Normal download')
    # Open http connection
    h = HttpFD('http://www.google.com/', {'nocheckcertificate': True})
    # Download a bit of data
    s = h.read(50000)
    # Close connection
    h.close()
    # Test if we got what we expected (this will fail if Google changes their page)
    assert s.startswith(b'<!doctype html><html')

    print('* Redirect')
    # Open http connection
    h = HttpFD('http://www.youtube.com/', {'nocheckcertificate': True})
    # Download a bit of data
    s = h.read(50000)
    # Close connection
    h.close()
    #

# Generated at 2022-06-14 15:49:59.493258
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test 1: no resuming
    dl = HttpFD(sanitized_Request('http://www.example.com/video.mp4'),
                {'params': {'continuedl': False}}).download()
    assert dl == (
        'GET',
        urlopen_hooks,
        'http://www.example.com/video.mp4',
        None,
        {'ytdl_hook': True, 'nocheckcertificate': False},
        None,
        False,
        False,
        False,
        True,
        {
            'continuedl': False,
            'noresizebuffer': False,
        },
        None,
        None)

    # Test 2: resuming

# Generated at 2022-06-14 15:50:10.665274
# Unit test for constructor of class HttpFD
def test_HttpFD():
    ydl = YoutubeDL()
    ydl.params['noprogress'] = True
    ydl.params['logger'] = FakeLogger()
    ydl.params['test'] = True
    http_fd = HttpFD(ydl, None, {'url': 'http://example.com/video.mp4', 'http_chunk_size': 1})
    http_fd.prepare_temp_file()

    info = http_fd.info
    if 'url' in info:
        del info['url']
    if 'http_chunk_size' in info:
        del info['http_chunk_size']

# Generated at 2022-06-14 15:50:47.070050
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # TODO: Add some unit test for this class.
    return None


# Test for HttpFD.best_block_size()

# Generated at 2022-06-14 15:50:53.280021
# Unit test for constructor of class HttpFD
def test_HttpFD():
    inst = HttpFD(
        {'logger': DummyLogger(), 'params': {'nopart': True, 'test': True}},
        {},
        'http://localhost/',
        {})
    assert inst.ydl is not None
    assert inst.params['test']


# Unit test
if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:51:03.798479
# Unit test for constructor of class HttpFD
def test_HttpFD():
    class TestException(Exception):
        pass

    def testopen(testfn, *args, **kwargs):
        f = open(testfn, *args, **kwargs)
        f.close()
        return f

    def testremove(testfn):
        os.unlink(testfn)


# Generated at 2022-06-14 15:51:12.838433
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .utils import parse_filesize, sanitize_open
    from .PostProcessor import PostProcessor

    def hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    ydl = YoutubeDL({'progress_hooks': [hook], 'continue_dl': True, 'nooverwrites': True})
    info_dict = {}
    p = PostProcessor(ydl, 'http://releases.ubuntu.com/12.04/ubuntu-12.04.5-desktop-amd64.iso.torrent', info_dict, {})
    info_dict['url'] = 'http://releases.ubuntu.com/12.04/ubuntu-12.04.5-desktop-amd64.iso.torrent'

# Generated at 2022-06-14 15:51:26.012912
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .extractor import gen_extractors

    ydl = YoutubeDL({'extractors': gen_extractors()})
    h = HttpFD(ydl, {'nooverwrites': True, 'continuedl': True, 'quiet': True})
    h.info_dict = {'id': 'ID', 'title': 'TITLE'}

    # Testing while-retry loop
    class MyHttpFD(HttpFD):
        def __init__(self):
            super(MyHttpFD, self).__init__(ypytdl.YoutubeDL(), {'nooverwrites': True, 'continuedl': True, 'quiet': True, 'format': '171'})
            self.info_dict = {'id': 'ID', 'title': 'TITLE'}
            self.retval = True



# Generated at 2022-06-14 15:51:34.384132
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('Testing HttpFD')
    # set verbose to True to see the results of the unit test
    verbose = True


# Generated at 2022-06-14 15:51:45.514724
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys
    import pytest
    from io import BytesIO

    class InjectResponse(HTTPResponse):

        def __init__(self, headers, body):
            super(InjectResponse, self).__init__(BytesIO(body), headers, 0)

    def make_inject_response(headers, body):

        def inject_response(req):
            return InjectResponse(headers, body)

        return inject_response

    class InjectUrlopen(object):

        def __init__(self, side_effect=None, return_value=None):
            if side_effect is not None:
                self.side_effect = side_effect
            else:
                assert return_value is not None
                self.return_value = return_value


# Generated at 2022-06-14 15:51:49.405868
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # TODO
    # Checking for error reporting
    # Slow connection
    # Checking for block sizes
    # Differently sized files
    # Overwriting
    # Pluggable transport
    pass

# Generated at 2022-06-14 15:51:59.411560
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # unit test for real_download
    import sys
    from .extractor import gen_extractors
    from .utils import prepend_extension
    import io

    for ie in gen_extractors():
        if ie.IE_NAME == 'generic':
            continue
        if ie.suitable(ie.ie_key()) and ie.ie_key()[0:4] == 'http':
            destfn = prepend_extension(ie.ie_key(), 'flv')
            print('Testing ' + ie.IE_NAME + ':' + ie.ie_key())
            ie.download(ie.ie_key())
            with open(destfn, 'rb') as stream:
                data = stream.read()
            print('  Downloaded ' + destfn)

# Generated at 2022-06-14 15:52:12.021160
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import testtools
    import time
    import amara.lib.httpstreamingclient
    import socket

    def decode(s):
        return s.decode('utf-8')

    def get_data(fd, fragment_size=None, max_bytes=None):
        retval = []
        if fragment_size is None:
            fragment_size = min(4 * 1024, max_bytes)
        if fragment_size <= 0:
            fragment_size = 4 * 1024
        while True:
            if max_bytes is not None:
                end_at = max_bytes - sum(map(len, retval))
                if end_at <= 0:
                    return b''.join(retval)
                if end_at < fragment_size:
                    fragment_size = end_at

# Generated at 2022-06-14 15:53:47.228492
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('-- Running HttpFD unit test')
    from .extractor import get_info_extractor
    from .utils import make_PSP_video_url
    from .compat import match_filter_func
    from .common import glob_escape
    from .common import InfoExtractor
    from .common import _parse_iso8601
    from .extractor.common import InfoExtractor
    from .extractor.common import SearchInfoExtractor
    from .extractor.common import YoutubeSearchListBaseInfoExtractor
    from .extractor.youtube import YoutubePlaylistIE
    from .downloader.common import FileDownloader
    from .downloader.external import ExternalFD
    import json
    import datetime
    import sys
    import re


# Generated at 2022-06-14 15:53:58.494813
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from io import StringIO
    from types import SimpleNamespace

    class InfoDict(dict):
        def __init__(self, *args, **kwargs):
            super(InfoDict, self).__init__(*args, **kwargs)
            self.__dict__ = self

    class FakeYDL(object):
        def __init__(self):
            self.progress_hooks = []
            self.trouble = 0

        def to_screen(self, *args, **kwargs):
            pass

        def to_stdout(self, *args, **kwargs):
            pass

        def to_stderr(self, *args, **kwargs):
            pass

        def report_error(self, *args, **kwargs):
            pass


# Generated at 2022-06-14 15:54:08.589633
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Some Python interpreters (buggy ones) don't have socket.create_connection
    # http://bugs.python.org/issue29559, https://github.com/rg3/youtube-dl/issues/7131
    # So we are using a no-op to whitelist those Python versions
    if (not compat_os_name == 'nt'
            and sys.version_info < (3, 7, 0)
            and sys.version_info >= (3, 6, 0)
            and not hasattr(socket, 'create_connection')):
        return

    global got_retryexception
    got_retryexception = False
    def retrysthread(sock, not_used, url, retries, timeout):
        global got_retryexception

# Generated at 2022-06-14 15:54:18.641544
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor.common import InfoExtractor
    from .compat import compat_str

    class TestIE(InfoExtractor):
        def __init__(self, downloader=None):
            super(TestIE, self).__init__(downloader)
            TestIE._test_instance = self

    fd = HttpFD(TestIE(), {}, None, {})
    # test non-chunked download
    success = fd.real_download(
        {'url': 'http://localhost/1M', 'resume_len': 0, 'chunk_size': 0},
        '-'
    )
    data = compat_str(fd._fd.stream.getvalue(), 'utf-8')
    assert success
    assert len(data) == 1048576
    # test non-chunked download with too small amount of

# Generated at 2022-06-14 15:54:19.449970
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # TODO
    pass

# Generated at 2022-06-14 15:54:27.200602
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import sys
    from .compat import u

    # Read data
    info = {'url': 'http://localhost/foo.mp4', 'http_headers': {
        u('REFERER'): u('http://www.youtube.com/watch?v=BaW_jenozKc'),
        u('User-Agent'): u('Mozilla/5.0 (X11; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'),
        u('Range'): u('bytes=0-'),
    }}

# Generated at 2022-06-14 15:54:39.159040
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD('http://example.org/')
    assert fd.url == 'http://example.org/'
    fd = HttpFD('http://example.org/', params={'verbose': True}, headers={'User-Agent': 'IE'})
    assert fd.url == 'http://example.org/'
    assert fd.ydl.params['verbose']
    assert fd.ydl.params['headers']['User-Agent'] == 'IE'
    cj = compat_cookiejar.CookieJar()
    fd = HttpFD('http://example.org/', cookiejar=cj)
    assert fd.url == 'http://example.org/'
    assert fd.ydl.cookiejar is cj

# Generated at 2022-06-14 15:54:48.359688
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Create a simple test server
    class ThreadingSimpleServer(socketserver.ThreadingMixIn, test_server.Server):
        daemon_threads = True

        def finish_request(self, request, client_address):
            request.settimeout(1)
            test_server.Server.finish_request(self, request, client_address)

    server = ThreadingSimpleServer(('localhost', 0), test_server.QuitHandler)
    port = server.server_address[1]

    status_dict = {'bytes_downloaded': 0, 'tmpfilename': None, 'status': '', 'elapsed': 0}
    error_list = []
    server_running = True

    def _hook(status):
        status_dict.update(status)

# Generated at 2022-06-14 15:54:59.854760
# Unit test for constructor of class HttpFD
def test_HttpFD():
    try:
        fd = HttpFD('http://www.google.com/', {'noprogress': True})
    except ExtractorError as err:
        # If this error is not raised, this test case has failed
        assert False, err.__class__.__name__
    assert fd.url == 'http://www.google.com/'
    assert fd.headers == {}
    assert fd.params['noprogress'] == True
    try:
        fd = HttpFD('http://www.google.com/', {'noprogress': True}, {'Range': 'bytes=0-100'})
    except ExtractorError as err:
        assert False, err.__class__.__name__
    assert fd.url == 'http://www.google.com/'
    assert fd

# Generated at 2022-06-14 15:55:12.155822
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test the real_download method of class HttpFD
    # Download a real file (to CWD) and check its size is what it should be
    # Test requires internet connection
    import os
    import sys

    url_filename = {
        'url': 'http://www.example.com/test.html',
        'filename': 'test.html',
        'size': 1270,
    }
    # Set the user agent to an arbitrary string to prevent youtube-dl from
    # sending the default one, which identifies this program as youtube-dl
    # and thus causes some servers to block the connection
    httpfd = HttpFD(params={'test': True, 'nooverwrites': False, 'user_agent': 'Download Test'})