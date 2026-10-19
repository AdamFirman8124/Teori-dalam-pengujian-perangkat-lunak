

# Generated at 2022-06-14 15:48:44.624007
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # This function is only a unit test, do not use it as an example of how to use HttpFD

    # TODO: this unit test is not very useful, it should check the HttpFD.real_download()

    from .compat import compat_http_client

    class FakeOpener(object):
        def __init__(self, http_class=compat_http_client.HTTPConnection):
            self.http_class = http_class

        def open(self, req):
            return FakeHttp(self.http_class, req)

    class FakeHttp(object):
        def __init__(self, http_class, req):
            self.fp = FakeFile()
            self.code = 200
            self.reason = 'Fake'
            self.headers = compat_http_client.HTTPMessage(FakeFile())
            self

# Generated at 2022-06-14 15:48:53.940461
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # The test is supposed to download a small file and check whether the amount
    # of bytes downloaded is the expected
    filesize = 100
    expected_bytes = filesize * 2

    # Generate a temporary file
    temp_filename = tempfile.mkstemp()[1]
    # Fill it with some data
    with open(temp_filename, 'wb') as temp_file:
        temp_file.write(b'a' * filesize)

    class MyYDL(YDL):
        def __init__(self):
            YDL.__init__(self)

        def to_screen(self, message):
            # Disable any output
            pass

        def download(self, url_list):
            # We expect only one URL, not more
            assert len(url_list) == 1
            # It's a 'fake' URL

# Generated at 2022-06-14 15:48:58.776879
# Unit test for constructor of class HttpFD
def test_HttpFD():
    stream = HttpFD(urlopen('http://www.google.com/'), None, 'wb')
    assert stream.read(5) == b'<html'
    stream.close()


# Generated at 2022-06-14 15:49:11.571818
# Unit test for constructor of class HttpFD
def test_HttpFD():
    test = Downloader(None)

    def data_gen(size):
        offset = 0
        while size >= 0:
            part = min(8192, size)
            if part == 0:
                break
            size -= part
            offset += part
            yield compat_str(offset - part) + '-' + compat_str(offset - 1) + '/' + compat_str(size + offset)
        raise StopIteration

    class DummyHeadRequest(compat_urllib_request.Request):
        def get_method(self):
            return "HEAD"

    class DummyGetRequest(compat_urllib_request.Request):
        def get_method(self):
            return "GET"

    class DummyResponse(object):
        def __init__(self, resp):
            self._resp = resp


# Generated at 2022-06-14 15:49:14.011317
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD(None, {}, None)
    assert fd.pp is None



# Generated at 2022-06-14 15:49:26.548017
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """Tests the real_download method of HttpFD class."""
    # In this test we rely on YoutubeDL.urlopen() method that returns a
    # mock object with a read() method returning a specified number of zero
    # bytes. The reads are counted, so we can determine if the whole specified
    # number of bytes was actually read by real_download() method.

    # Set up a mock YoutubeDL instance
    class MockYoutubeDL:
        def __init__(self):
            self.downloaded = 0
        def urlopen(self, url):
            class MockHTTPResponse:
                def __init__(self, mock_ydl):
                    self.mock_ydl = mock_ydl
                # On read() we return a number of zero bytes as requested by
                # the caller of read(), but we count the number of bytes

# Generated at 2022-06-14 15:49:34.356318
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    """
    Testing the real_download() method of HttpFD class
    """
    from .testcases import YoutubeDL
    from .downloader import HttpFD

    class MyYoutubeDL(YoutubeDL):
        """
        Subclass to override methods of YoutubeDL class
        """
        def report_retry(self, *args):
            """
            Override method to avoid printing 'Retrying...' message
            """
        def report_destination(self, *args):
            """Override method to avoid printing into stdout 'destination' message"""
        def report_progress(self, *args, **kargs):
            """Override method to avoid printing into stdout 'progress' message"""

    ydl = MyYoutubeDL()
    fd = HttpFD(ydl)

# Generated at 2022-06-14 15:49:41.636727
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import random
    # Run test_normal first
    test_normal()
    # Reset params of HttpFD
    HttpFD.params = sanitize_open_kwargs({})
    # Set params of WgetFD
    WgetFD.params = sanitize_open_kwargs({})
    # Set params of CurlFD
    CurlFD.params = sanitize_open_kwargs({})
    # File to test
    filename = 'test-%08d.bin' % random.randrange(100000000)
    # Create new file
    with open(filename, 'wb') as f:
        for i in range(0, 1024):
            f.write(b'\0')
    # Set test url
    url = 'file://%s' % filename
    # Open file descriptor
    fd = HttpFD

# Generated at 2022-06-14 15:49:53.719164
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import io
    # Create an in-memory 'file' that contains a YouTube page
    page = io.BytesIO(b'abc')
    page.filename = 'foo.html'
    page.url = 'http://www.youtube.com/'
    page.headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': '3'
    }
    page.code = 200
    # Run the constructor
    fd = HttpFD(page, {}, 'http://www.youtube.com/')
    # Results
    assert fd.name() == 'foo.html'
    assert fd.size() == 3
    assert fd.read() == b'abc'
    assert fd.read(2) == b'ab'
    assert fd.readline()

# Generated at 2022-06-14 15:50:04.298233
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Save current value of _TEST_FILE_SIZE
    TEST_FILE_SIZE_SAVED = HttpFD._TEST_FILE_SIZE

    HttpFD._TEST_FILE_SIZE = None
    assert HttpFD(None, None).real_download(
        {'url': 'https://example.com'}, '-'), 'non-chunked download failed'
    HttpFD._TEST_FILE_SIZE = None
    assert HttpFD(None, None).real_download(
        {'url': 'https://example.com'}, '-', {'noprogress': True}), 'non-chunked download failed with noprogress'

    HttpFD._TEST_FILE_SIZE = 100

# Generated at 2022-06-14 15:50:49.814517
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Getting the url specified in -U
    url = '--U' in sys.argv and sys.argv[sys.argv.index('-U') + 1] or 'http://127.0.0.1:3128'
    if 'http://' not in url:
        sys.exit('The specified URL is not valid.')
    sys.stdout.write('Testing with URL: %s ...' % url)
    sys.stdout.flush()
    # Creating the object
    fd = HttpFD('http://www.google.com', {'http_proxy': url}, 'test this', test=True)
    # Make sure the object was created properly
    if fd.real_downloader.name != 'HttpFD':
        sys.exit('FAIL!\nWrong downloader created.')

# Generated at 2022-06-14 15:51:01.395026
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    print("Testing real_download()")
    def httpdl(fname, tsize, chunk_size=None, retries=0):
        params = {'continuedl': True, 'nooverwrites': True}
        if chunk_size is not None:
            params['fragment_size'] = chunk_size
        hfd = HttpFD(null_get_ready(), nop_download, nop_report_error, nop_report_warning, nop_report_destination, nop_temp_name, nop_try_rename, null_hook, nop_report_resuming_byte, nop_report_retry, nop_report_file_already_downloaded, nop_report_unable_to_resume, params)
        data_len = tsize

# Generated at 2022-06-14 15:51:02.275888
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    pass

# Generated at 2022-06-14 15:51:04.228731
# Unit test for constructor of class HttpFD
def test_HttpFD():
    fd = HttpFD('http://www.google.com', {})
    assert fd.real_download('foo')
    assert os.path.exists('foo')
    os.remove('foo')

# Generated at 2022-06-14 15:51:13.911860
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    fd = HttpFD(None, {'continuedl': True, 'noprogress': True, 'quiet': True}, {})

    # Test 1: Just a fragment of a file should be downloaded
    ctx = DownloadContext()
    ctx.data_len = 20
    ctx.chunk_size = 7
    ctx.tmpfilename = 'tmp.test'
    if os.path.exists(ctx.tmpfilename):
        os.remove(ctx.tmpfilename)
    ctx.stream = io.open(ctx.tmpfilename, 'wb')
    ctx.start_time = time.time()
    ctx.open_mode = 'wb'
    ctx.data = io.StringIO('0123456789')
    fd.real_download(ctx, lambda *a, **k: None)


# Generated at 2022-06-14 15:51:22.163846
# Unit test for constructor of class HttpFD
def test_HttpFD():
    class FakeFD:
        def __init__(self, name):
            self.name = name
            self.blocks = []
        def write(self, b):
            self.blocks.append(b)
        def close(self):
            pass
    hd = HttpFD(None, FakeFD('test.tmp'), 'wb', None)
    hd.write(b'blab')
    hd.close()
    assert hd.blocks == [b'blab']



# Generated at 2022-06-14 15:51:27.415769
# Unit test for constructor of class HttpFD
def test_HttpFD():
    h = HttpFD('http://site.com/file.ext', {'test_option': 'test_value'})
    assert h.params['test_option'] == 'test_value'
    assert h.test()

if __name__ == '__main__':
    test_HttpFD()
    print('Test finished successfully')

# Generated at 2022-06-14 15:51:33.786795
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def print_hook(d):
        print(d)
    ydl = YoutubeDL({'progress_hooks': [print_hook], 'sleep_interval': 0.001})
    fd = HttpFD(ydl, 'http://quodlibet.readthedocs.org/en/latest/_images/dvdempire_logo.png', {'test': True}, {})
    if fd.test():
        print('Test passed')
    else:
        raise Exception('test failed!')
    fd.close()

if __name__ == '__main__':
    test_HttpFD()

# Generated at 2022-06-14 15:51:44.986044
# Unit test for constructor of class HttpFD
def test_HttpFD():
    import urllib.request
    import urllib.parse
    url = 'http://www.google.com/'
    tmp = 'TMP' + url
    stream = HttpFD(url, tmp)
    # stream.real_download(stream.url, stream.tmpfilename)

    stream = HttpFD(url, None)
    # stream.real_download(stream.url, stream.tmpfilename)
    test_str = b'HI THERE'
    f = stream.stream
    f.write(test_str)
    f.seek(0)
    assert test_str == f.read()

    stream = HttpFD(url, tmp, {'test': 'OK'})
    # stream.real_download(stream.url, stream.tmpfilename)
    f = stream.stream
    f.seek(0)

# Generated at 2022-06-14 15:51:57.028336
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from io import BytesIO
    from collections import OrderedDict
    TH = HttpFD()

    def _test_download(url, params):
        TH.params = params
        info_dict = OrderedDict()
        TH.add_info_dict({'id': 'testid'}, info_dict)
        return TH._do_download(
            info_dict,
            (url, {}),
            params.get('test', False),
            '-'
        )

    def _test_download_with(params, url, success=True):
        assert _test_download(url, params) == success, '%r failed'  % url

    # Test with a file-like object
    obj = BytesIO(b'abc')

# Generated at 2022-06-14 15:53:15.679661
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    def _test(ctx, data, expected_data_len, expected_block_sizes):
        size_counter = 0
        counter = 0
        data_len = len(data)
        while True:
            expected_block_size = expected_block_sizes[counter]
            counter += 1
            if expected_block_size is None:
                break
            read_block_size = ctx.data.read(expected_block_size)
            size_counter += len(read_block_size)
            assert data[size_counter - len(read_block_size):size_counter] == read_block_size
            if size_counter == data_len:
                break
        assert expected_data_len == data_len
    ydl = DummyYDL()
    ydl.params['retries'] = 0
    ydl

# Generated at 2022-06-14 15:53:23.819670
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # simulate params
    params = {
        'nooverwrites': True,
        'continuedl': True,
        'noprogress': True,
        'retries': 2,
        'buffersize': 16384,
        'ratelimit': None,
        'noresizebuffer': False,
        'test': True,
        'min_filesize': 50000,
        'max_filesize': 500000,
        'updatetime': False,
        'test_downloader': None,
        'xattr_set_filesize': False
    }

    # test data (content length, last modified header, file size, modified time, data)

# Generated at 2022-06-14 15:53:33.955616
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Params needed for real_download method
    params = {}
    params['quiet'] = True
    params['cachedir'] = False
    params['format'] = None
    params['simulate'] = True
    params['noprogress'] = True
    params['ratelimit'] = 0
    params['noresizebuffer'] = True
    params['retries'] = 0
    params['continuedl'] = True
    params['nooverwrites'] = False
    params['test'] = True
    params['consoletitle'] = False
    params['logtostderr'] = False
    params['nopart'] = False
    params['updatetime'] = True
    params['buffersize'] = None
    params['nocheckcertificate'] = False
    params['prefer_insecure'] = False
   

# Generated at 2022-06-14 15:53:43.011636
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import uuid
    from .compat import compat_cookiejar
    from .RtmpFD import RtmpFD
    from .extractor import get_info_extractor
    from .utils import encodeFilename


# Generated at 2022-06-14 15:53:52.325417
# Unit test for constructor of class HttpFD
def test_HttpFD():
    # Test constructor
    h = HttpFD(None, None, {'noprogress': True}, None)

    # Test block_size
    assert h.best_block_size(10.0, 1000) == 1000
    assert h.best_block_size(10.0 * 2 ** 20, 1000 * 2 ** 20) == 1000 * 2 ** 20
    assert h.best_block_size(2.5, 1000) == 1000
    assert h.best_block_size(1.0, 1000) == 1000
    assert h.best_block_size(0.5, 1000) == 500
    assert h.best_block_size(0.10, 1000) == 100
    assert h.best_block_size(1.0, 0) == 0
    assert h.best_block_size(0.5, 0) == 0


# Generated at 2022-06-14 15:54:04.409133
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp(prefix='youtube-dl-test_')
    # Make a dummy download
    params = {
        'outtmpl': os.path.join(temp_dir, 'test%(ext)s'),
        'ratelimit': 10,
        'nooverwrites': True,
        'quiet': True
    }
    dl = HttpFD(params)
    # Test file download
    dl._test_download_file('https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/31652459', {}, params)
    # Test chunked download

# Generated at 2022-06-14 15:54:16.445363
# Unit test for constructor of class HttpFD
def test_HttpFD():
    from .extractor import gen_extractors
    from .post import select_format
    ydl = YDL()
    ydl.add_default_info_extractors()
    ie = gen_extractors(ydl)['youtube']()
    ydl.process_ie_result(ie.extract('http://www.youtube.com/watch?v=BaW_jenozKc'), download=False)

    info = ydl.extract_info('http://www.youtube.com/watch?v=BaW_jenozKc', download=False)
    f = select_format(info['formats'], ydl.params)
    filename = ydl.prepare_filename(info)
    stream = HttpFD(ydl, info['url'], f, filename, {'noprogress': True})


# Generated at 2022-06-14 15:54:23.428026
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    # This function is called from test_suite.py
    # We only test that the function returns True
    # since it is too difficult to check downloading
    # a real file

    # Create a HttpFD object
    h = HttpFD(None, {}, None)
    if h is None:
        return False

    # Get a file to download
    a = h.get_test_video_file()
    if a is None:
        return False

    # Download the file
    return h.real_download(a[0], {}, a[1], a[2], a[3])

# Generated at 2022-06-14 15:54:34.103812
# Unit test for constructor of class HttpFD
def test_HttpFD():
    print('Testing HttpFD.__init__')
    print('Restarting http server')
    try:
        httpd.__init__()
    except socket.error as e:
        if e.errno != errno.EADDRINUSE:
            raise
        print('Server already running')
    else:
        print('Done')
    # Try to open a file
    data = HttpFD('http://localhost:%d/%s' % (server.port(), urllib.quote(__file__))).read()
    assert data.startswith('# Unit test for constructor of class HttpFD\n')


# Generated at 2022-06-14 15:54:44.332585
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    test_fd = HttpFD(None, {})
    test_fd.ydl.urlopen = lambda request: compat_http_client.HTTPResponse(
        FakeSocket(
            b'HTTP/1.1 200 OK\r\n'
            b'Content-Type: image/jpeg\r\n'
            b'Content-Length: ' + str(test_fd._TEST_FILE_SIZE).encode('ascii') + b'\r\n'
            b'\r\n' + b'data' * test_fd._TEST_FILE_SIZE
        )
    )
    test_fd.params['test'] = True

    # Test download of a small file
    test_tmp_file = NamedTemporaryFile(delete=False)
    test_tmp_file.close()
    ctx

# Generated at 2022-06-14 15:57:52.523508
# Unit test for constructor of class HttpFD
def test_HttpFD():
    def test_commandline(downloader, url):
        """Simulates what would happen on cmdline"""
        outtmpl = '%(id)s-%(ext)s'
        args = ['--format', 'best', '--outtmpl', outtmpl, url]
        opts = {}
        downloader.add_default_info_extractors()
        opts.update(downloader.default_options)
        opts.update(downloader.user_options)
        opts.update(downloader.read_options('youtube-dl'))
        parseOpts(downloader, args, opts)
        return HttpFD(downloader, opts)

    downloader = YoutubeDL()
    # test only OneFD
    downloader.params['nooverwrites'] = True
    # test only HttpFD

# Generated at 2022-06-14 15:57:58.265042
# Unit test for method real_download of class HttpFD
def test_HttpFD_real_download():
    import sys

    def hook_progress(status):
        print(status)

    def hook_temp_name(filename):
        return filename + '.part'

    http_fd = HttpFD(
        'https://github.com/ytdl-org/youtube-dl/archive/master.tar.gz',
        {'outtmpl': '%(id)s%(ext)s', 'progress_hooks': [hook_progress]},
        {'test': True},
        {},
        hook_temp_name,
    )
    assert http_fd.real_download(
        {'id': 'master', 'ext': '.tar.gz'},
        test=True,
        retries=10,
        chunk_size=1048576)
    os.remove('master.tar.gz.part')
# Unit test