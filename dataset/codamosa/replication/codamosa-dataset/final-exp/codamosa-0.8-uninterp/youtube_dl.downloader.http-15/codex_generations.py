

# Generated at 2022-06-14 15:48:38.937286
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    class FakeHttpFD(HttpFD):
        def __init__(self, *args, **kwargs):
            HttpFD.__init__(self, *args, **kwargs)
            self.test_data = [
                ('0' * self._TEST_FILE_SIZE, None),
                ('0' * self._TEST_FILE_SIZE, None),
                ('0' * self._TEST_FILE_SIZE, None)
            ]
            self.test_data_index = 0

        def best_block_size(self, elapsed_time, bytes_downloaded):
            return 1024

        def calc_speed(self, start, now, bytes_downloaded):
            return 0

        def calc_eta(self, start, now, total_bytes, bytes_downloaded):
            return 0


# Generated at 2022-06-14 15:48:44.053302
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    success = True
    msg = ''

    test_data = ('test1234äöüß', 'test5678ΣΤΥΦΧΨΩ', 'test9abcβγδε')

    filename = 'test'
    size = sum(map(len, test_data))

    # Test for: non-chunked download

# Generated at 2022-06-14 15:48:53.655562
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from ssl import SSLError
    fd = HttpFD(sanitized_Request('https://google.com'),
                {'prefer_insecure': False, 'noprogress': True},
                'GET',
                None,
                None,
                None)
    fd.real_download()
    fd = HttpFD(sanitized_Request('http://youtube.com'),
                {'prefer_insecure': True, 'noprogress': True},
                'GET',
                None,
                None,
                None)
    fd.real_download()
    fd = HttpFD(sanitized_Request('http://localhost'),
                {'prefer_insecure': True, 'noprogress': True},
                'GET',
                None,
                None,
                None)
    f

# Generated at 2022-06-14 15:48:56.333320
# Unit test for constructor of class HttpFD
def test_HttpFD():
    assert HttpFD(urllib.request.urlopen('http://example.com/'), 'rb', 'http://example.com/', 'test.bin').size == 1183


# Generated at 2022-06-14 15:49:09.917345
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Test cases
    class TestCase:
        def __init__(self, url, headers, data_len, block_size, retries, resume_len, chunk_size, open_mode, result):
            self.url = url
            self.headers = headers
            self.data_len = data_len
            self.result = result
            self.block_size = block_size
            self.resume_len = resume_len
            self.chunk_size = chunk_size
            self.open_mode = open_mode
            self.retries = retries

# Generated at 2022-06-14 15:49:18.170515
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    ydl = FakeYDL()
    test_file_size = 100000
    http_fd = HttpFD(ydl, {'test': True, 'noresizebuffer': True, 'continuedl': 'true'})
    # Downloading the first part of the file
    succeeded = http_fd.real_download({
        'url': 'http://localhost/testfile',
        'tmpfilename': 'tmp_testfile_1',
        'resume_len': 0,
        'chunk_size': test_file_size / 2,
        'start_time': time.time(),
        'data_len': test_file_size,
        'retries': 0,
    })
    assert succeeded
    # Downloading the second part of the file

# Generated at 2022-06-14 15:49:29.712893
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    from .extractor import get_info_extractor
    import os
    import re
    import sys
    import tarfile
    import xml.etree.ElementTree as ET

    filename = '-_--_--__--_--_-__-_-_'
    ie = get_info_extractor('GenericIE', None)
    ie.set_downloader(None)
    class _op():
        def __init__(self):
            self.params = {
                'outtmpl': '%(id)s.%(ext)s',
                'nooverwrites': False,
                'forcetitle': True,
                'quiet': True,
            }
            self.report_destination = print
            self.to_stdout = sys.stdout.write
            self.to_stderr = sys.stder

# Generated at 2022-06-14 15:49:40.917217
# Unit test for constructor of class HttpFD
def test_HttpFD():
    """
    Try to test the constructor of the HttpFD object,
    we'll actually do a download of a small file for that.
    """
    import random

    class FakeYDL(object):
        def __init__(self, opts):
            self.opts = opts
            self.to_screen = object.__getattribute__(self, 'to_screen')

# Generated at 2022-06-14 15:49:53.240334
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    Test the HttpFD real_download method.
    """
    with tmppath() as path:
        ydl = FakeYDL()

        # Testing with a simple text file.
        # A simple text file should be downloaded correctly.
        fd = HttpFD(ydl, {}, 'http://localhost/simple-text-file.txt', {'noprogress': True})
        fd.params['outtmpl'] = path
        fd.real_download(True)
        assert os.path.exists(path)
        with io.open(path, encoding='utf-8') as f:
            assert f.read() == 'Test file for youtube-dl\n'

        # We will now try to download a large file.
        # We just want to test that we can download the file, not measure speed


# Generated at 2022-06-14 15:50:03.899142
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test no resuming
    fd = HttpFD(
        'http://www.example.com/video.mp4', {
            'nopart': True,
            'continuedl': False,
            'noresizebuffer': True,
            'retries': 0
        }, '-'
    )

    # Test resuming
    fd = HttpFD(
        'http://www.example.com/video.mp4', {
            'nopart': True,
            'continuedl': True,
            'noresizebuffer': True,
            'retries': 0
        }, '-'
    )

    # Test file already exists

# Generated at 2022-06-14 15:50:53.819952
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test 1: check the use of Content-Length header, if present
    # in the server response
    content_length_headers = {
        'content-length' : 1024
    }

    c = HttpFD(content_length_headers, lambda _: '')
    assert c.get_size() == 1024

    # Test 2: check that get_size() returns None if there is no
    # Content-Length header
    headers = {}
    c = HttpFD(headers, lambda _: '')
    assert c.get_size() is None

    # Test 3: if Content-Length is not an integer, it should be ignored
    content_length_headers = {
        'content-length' : 'noaccurate'
    }

    c = HttpFD(content_length_headers, lambda _: '')
    assert c.get

# Generated at 2022-06-14 15:51:04.126160
# Unit test for constructor of class HttpFD
def test_HttpFD():
    """Run test for HttpFD constructor"""

    from sys import version_info

    # pylint: disable=too-many-locals,too-many-branches,too-many-statements,too-many-nested-blocks

    ###########
    # Helpers #
    ###########

    def b64encode(s):
        """Encode string to base64"""

        import base64
        return base64.b64encode(s.encode('utf-8')).decode('ascii')

    def b64decode(s):
        """Decode base64 encoded string"""

        import base64
        return base64.b64decode(s.encode('ascii')).decode('utf-8')

    ############
    # Settings #
    ############

    # Debug output for

# Generated at 2022-06-14 15:51:13.648241
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import BytesIO
    from urllib.request import Request
    from urllib.error import HTTPError
    req = Request('http://localhost/test')
    try:
        raise HTTPError(req.get_full_url(), 403, 'Forbidden', None, None)
    except HTTPError as e:
        fd = HttpFD(e)
        assert fd.read(10) == b'Forbidden\n'
        assert fd.read() == b'Access to the URL http://localhost/test is forbidden'
        fd.close()

    req = Request('http://localhost/test')
    try:
        raise HTTPError(req.get_full_url(), 404, 'Not Found', None, None)
    except HTTPError as e:
        fd = HttpFD(e)
        assert fd

# Generated at 2022-06-14 15:51:26.595382
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Define a function that can be used as a hook function for external tests
    def null_hook(*args, **argd):
        return
    # Prepare a context for testing HttpFD.real_download
    # (see class HttpFD documentation for context details)
    context = {
        'url': 'http://example.org/random',
        'chunk_size': 10,
        'tmpfilename': 'tmp',
        'open_mode': 'wb+',
        'max_chunk_size': 100,
        'blocksize': 10,
        'resume_len': 0,
        'fd': 5,
        'length': None,
        'retries': 3,
        'file_size': 30,  # This is used by best_block_size and slow_down
        'test': True
    }
    #

# Generated at 2022-06-14 15:51:37.571241
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Setup: create a non-existent directory, a dummy file and a dummy file of 1 MB
    import tempfile
    import os
    test_dir = tempfile.mkdtemp()
    test_file = os.path.join(test_dir,'test.file')
    file(test_file, 'w').write('x')
    test_size = 1024 * 1024  # bytes
    test_large_file = os.path.join(test_dir,'test_large.file')
    file(test_large_file, 'w').write('x' * test_size)
    # Test: download a dummy file of 1 byte

# Generated at 2022-06-14 15:51:45.883598
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    check_execution = True
    check_execution = False
    if check_execution:
        # Get all non-empty lines of the file
        import os
        file_path = os.path.join(os.path.dirname(__file__), 'debug', 'test_files', 'file_1.ts')
        all_lines = []
        with open(file_path, 'rb') as f:
            for chunk in f:
                for line in chunk.split(b'\n'):
                    if line and not line.isspace():
                        all_lines.append(line)

    hfd = HttpFD(None, {'noprogress': True, 'retries': 0})
    hfd.report_destination = lambda filename: None

# Generated at 2022-06-14 15:51:57.073614
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(0, None, {'noprogress': True})
    fd.report_retry('asd', 2, 4)
    fd.report_resuming_byte(10)
    fd.report_destination('-')
    fd.to_screen('test')
    fd.to_stderr('error')
    fd.report_progress(10, 1000, 10, 1000)
    fd.report_error('error')
    fd.report_unable_to_resume()
    fd.report_file_already_downloaded(None)
    fd.report_finish(None)

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:52:09.949970
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import BytesIO
    fd = HttpFD(BytesIO(b'foobar'), None)
    # FD is not seekable and has no length
    assert fd.isatty() is False
    assert fd.seekable() is False
    assert fd.readable() is True
    assert fd.writable() is True
    assert fd.fileno() is None
    assert fd.get_size() is None
    assert fd.tell() == 0
    assert fd.read(3) == b'foo'
    assert fd.readline() == b'bar'
    assert fd.readline() == b''
    assert fd.readline(10) == b''
    assert fd.tell() == 6

    fd.close()
    fd.close()


# Generated at 2022-06-14 15:52:12.200742
# Unit test for constructor of class HttpFD
def test_HttpFD():
    downloader = YoutubeDL()
    datalen = 10
    fd = HttpFD(downloader, None, '', datalen, {}, {}, None)
    assert(fd.datalen == datalen)


# Generated at 2022-06-14 15:52:23.175914
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test case 1: Both start and end are specified
    fd = HttpFD('http://3v4l.org/TEST', {'headers': {'Range': 'bytes=1-100'}})
    assert fd.start == 1
    assert fd.end == 100

    # Test case 2: Only start is specified
    fd = HttpFD('http://3v4l.org/TEST', {'headers': {'Range': 'bytes=101-'}})
    assert fd.start == 101
    assert fd.end == None

    # Test case 3: Only end is specified
    fd = HttpFD('http://3v4l.org/TEST', {'headers': {'Range': 'bytes=-99'}})
    assert fd.start == None
    assert fd.end == 99



# Generated at 2022-06-14 15:54:07.127613
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from youtube_dl.utils import HttpFD

    # The following test uses a connection to a public web-server to
    # test the functionality of HttpFD.

    # We download a file from archive.org
    # This is a 1MiB file which should avoid any speed issues.
    # (The first bytes of this file are used as md5sum check in the code below.)
    url = 'http://archive.org/download/WiggleWiggle/Wiggle%20Wiggle%20-%20Wiggle%20Wiggle%20%28Official%20Music%20Video%29_512kb.mp4'

    file_size = 1048576
    http_url_open = compat_urllib_request.urlopen

    # Test 1: Test without resume
    fd1 = HttpFD(url, http_url_open)
   

# Generated at 2022-06-14 15:54:18.104033
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    urlh = compat_urllib_request.urlopen
    def urlopen_test(req):
        data = io.BytesIO(b'\x00' * 1048576)
        headers = {'Content-length': '1048576'}
        resp = compat_urllib_request.addinfourl(data, headers, req.full_url)
        resp.code = 200
        resp.headers = headers
        resp.msg = headers
        return resp
    def retry(self, *args, **kargs):
        pass
    def _hook_progress(self, *args, **kargs):
        pass
    fd = HttpFD()
    fd.retry = retry.__get__(fd, HttpFD)

# Generated at 2022-06-14 15:54:26.545489
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """Tests for real_download method of HttpFD class."""

    class DummyYDL():
        params = {
            'noprogress': True,
            'format': 'best',
            'outtmpl': '%(id)s.%(ext)s',
            'nooverwrites': False,
            'test': True,
            'nocheckcertificate': False,
            'prefer_insecure': False,
        }
        progress_hooks = []
        _screen_file = sys.stderr
        _err_file = sys.stdout
        _total_bytes_estimate = 0
        # A dummy value for slow_down method
        _rate_multiplier = 1.0
        _sleep_interval = None


# Generated at 2022-06-14 15:54:31.006275
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD('http://www.google.com', params={'noprogress':True})
    assert(fd is not None)
    assert(fd.read(4) == '<!do')
    fd.close()



# Generated at 2022-06-14 15:54:33.396889
# Unit test for constructor of class HttpFD
def test_HttpFD():
    assert HttpFD(None, {}, {}).__class__.__name__ == 'HttpFD'


# Generated at 2022-06-14 15:54:43.728685
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import io
    import sys
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.compat import compat_http_server
    from youtube_dl.utils import sanitize_open

    def gen_data(length, block_size=8192):
        """
        Generate a string of size 'length' made of random ascii characters.
        This is used as the content of the fake files that we download.
        """
        assert block_size > 0
        return ''.join(chr(random.randint(1, 126)) for i in range(block_size)).encode('ascii') * (length // block_size)

    def serve_content(handler):
        # send headers
        handler.send_response(200)

# Generated at 2022-06-14 15:54:50.887623
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    h = HttpFD(ydl, {}, {})
    assert h.fileno() == -1
    url = 'http://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Collage_of_Nine_Dogs.jpg/800px-Collage_of_Nine_Dogs.jpg'
    h.prepare_url(url)
    assert h.fileno() > 0
    assert os.read(h.fileno(), 1) == b'\377'
    assert os.read(h.fileno(), None)
    assert os.read(h.fileno(), None) == b''



# Generated at 2022-06-14 15:55:01.835876
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # URLs
    url = 'http://upload.wikimedia.org/wikipedia/commons/2/21/Attempting_to_upload_a_very_large_file_to_Commons.webm'
    url_single_chunk = 'http://upload.wikimedia.org/wikipedia/commons/5/5f/Math_is_Fun.ogg'

    # Parameters

# Generated at 2022-06-14 15:55:13.874900
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Simulate YouTube servers redirecting to beginning of download
    def redirect(req):
        class R:
            def __init__(self, code, rurl):
                self.code = code
                self.rurl = rurl

            def info(self):
                class I:
                    def __init__(self):
                        self.dict = dict(Location=self.rurl)

                    def get(self, name):
                        return self.dict.get(name, '')

                return I()
        return R(302, req.get_full_url())

    test_url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    test_url_basename = 'videoplayback'

# Generated at 2022-06-14 15:55:21.341546
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('-- BEGIN -- test_HttpFD')

    # Test case: file exists
    fd = HttpFD('http://www.google.com', {'nopart': True, 'test': True}, {'test': True})
    assert fd.real_download, 'fd.real_download should be True.'
    assert not fd.isok(), 'fd.isok() should return False.'
    assert fd.get_filesize() is not None, 'fd.get_filesize() shouldn\'t return None.'
    assert fd.get_filesize() > 0, 'fd.get_filesize() should return a positive integer value.'
    assert fd.get_filename() is None, 'fd.get_filename() should return None.'
    assert not fd.done(), 'fd.done() should return False.'