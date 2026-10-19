

# Generated at 2022-06-14 15:08:09.840582
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader({'nopart': False})
    assert fd.temp_name('abc') == 'abc.part'
    assert fd.temp_name('abc.mp4') == 'abc.mp4.part'
    assert fd.temp_name('/a/b/c/abc') == '/a/b/c/abc.part'
    assert fd.temp_name('/a/b/c/abc.mp4') == '/a/b/c/abc.mp4.part'
    assert fd.temp_name('c:/a/b/c/abc.mp4') == 'c:/a/b/c/abc.mp4.part'
    fd = FileDownloader({'nopart': True})
    assert fd.temp_name('abc') == 'abc'
   

# Generated at 2022-06-14 15:08:18.348468
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({})
    fd.to_screen = lambda *a, **k: None
    fd.to_console_title = lambda *a, **k: None
    assert fd.report_progress({'status': 'finished'}) is None
    assert fd.report_progress({'status': 'finished', 'total_bytes': 4, 'downloaded_bytes': 4}) is None
    assert fd.report_progress({'status': 'finished', 'total_bytes': 4, 'downloaded_bytes': 4, 'filename': '-'}) is None
    assert fd.report_progress({'status': 'finished', 'total_bytes': 4, 'downloaded_bytes': 4, 'filename': 'f'}) is None

# Generated at 2022-06-14 15:08:25.483217
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    """
    Test method report_progress of class FileDownloader
    """
    from __main__ import FileDownloader
    file_downloader = FileDownloader(
        params=dict())
    file_downloader.report_progress(
        status="downloading",
        downloaded_bytes=100,
        total_bytes=100,
        speed=1,
        eta=0,
        elapsed=10)
    print("Testing report_progress of FileDownloader: success!\n")



# Generated at 2022-06-14 15:08:34.241828
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader({})

    assert fd.parse_bytes('') is None
    assert fd.parse_bytes('1') == 1
    assert fd.parse_bytes('1b') == 1
    assert fd.parse_bytes('1k') == 1024
    assert fd.parse_bytes('1B') == 1
    assert fd.parse_bytes('1K') == 1024
    assert fd.parse_bytes('1m') == 1024 * 1024
    assert fd.parse_bytes('1M') == 1024 * 1024
    assert fd.parse_bytes('1g') == 1024 * 1024 * 1024
    assert fd.parse_bytes('1G') == 1024 * 1024 * 1024
    assert fd.parse_bytes('1t') == 1024 * 1024 * 1024 * 1024
    assert fd.parse_bytes

# Generated at 2022-06-14 15:08:37.659134
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(None, {'noprogress': True, 'logger': True})
    fd.params.update({'nopart': True})
    assert fd.temp_name('abc') == 'abc'
    fd.params.update({'nopart': False})
    assert fd.temp_name('abc') == 'abc.part'

# Generated at 2022-06-14 15:08:47.366958
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Create a fake info dict
    info_dict = dict()
    info_dict['id'] = 'test'
    info_dict['ext'] = 'test'
    info_dict['title'] = 'test'
    info_dict['alt_title'] = None
    info_dict['url'] = 'test'
    info_dict['thumbnail'] = 'test'
    info_dict['description'] = 'test'
    info_dict['uploader'] = 'test'
    info_dict['timestamp'] = 0
    info_dict['upload_date'] = '1970'
    info_dict['uploader_id'] = 'test'
    info_dict['location'] = 'test'
    info_dict['categories'] = []
    info_dict['tags'] = []
    info_dict['subtitles'] = None


# Generated at 2022-06-14 15:08:58.072344
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    def gen_values_for_test(target):
        # Generate values around the target in order to test all cases
        yield target
        while target > 0:
            target = target // 2
            yield target
            yield 2 * target
            yield target + 2 * target

    def test_FileDownloader_best_block_size_aux(target, kBps):
        fd = FileDownloader({'ratelimit': kBps})
        for bytes in gen_values_for_test(target):
            assert (
                fd.best_block_size(1.0, bytes) ==
                FileDownloader.best_block_size(1.0, bytes))
            assert (
                fd.best_block_size(1.0, bytes) ==
                target if target <= bytes else bytes)


# Generated at 2022-06-14 15:09:05.195376
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    tstart = time.time()
    time.sleep(1)
    tend = time.time()
    fd = FileDownloader({})
    assert fd.calc_speed(tstart, tend, 10) == 10
    assert fd.calc_speed(tstart, tend, 0) is None
    assert fd.calc_speed(tstart, 0, 10) is None
    assert fd.calc_speed(0, tend, 10) is None


# Generated at 2022-06-14 15:09:10.642447
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader(NullYoutubeDL(), {})
    for s in ['0', '2048', '1234567890', '1023k', '1.5M', '2.5G', '1.1T']:
        assert fd.parse_bytes(s) == parse_filesize(s)
    assert fd.parse_bytes('1.1x') is None


# Generated at 2022-06-14 15:09:22.203991
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    obj = FileDownloader(None, None)

    # test for _best_block_size
    get_block_size = lambda t, s: obj.best_block_size(t, s)
    assert get_block_size(0, 0) == 1
    assert get_block_size(0.01, 100) == 5120
    assert get_block_size(0.01, 10240) == 10240
    assert get_block_size(0.001, 102400) == 512000
    assert get_block_size(1, 102400) == 512000

    # test for _best_block_size2
    get_block_size2 = lambda t, s: obj.best_block_size(t, s)
    assert get_block_size2(0, 0) == 1

# Generated at 2022-06-14 15:09:53.393689
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import shutil

    # Create empty file
    tmp_filename = os.path.join(os.path.expanduser('~'), 'tmp_filename')
    with open(tmp_filename, 'a'):
        os.utime(tmp_filename, None)

    # Check that last modified time is not 0
    assert os.path.getmtime(tmp_filename) != 0

    # Try to update last modified time of non existing file
    fd = FileDownloader({})
    fd._do_test_try_utime(tmp_filename, 'unknown', 0)
    assert os.path.getmtime(tmp_filename) != 0

    # Update last modified time using HTTP header value

# Generated at 2022-06-14 15:09:54.189648
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    return



# Generated at 2022-06-14 15:10:05.904506
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def call_slow_down(self, start, now, bytes):
        if now is None:
            now = time.time()
        return self.slow_down(start, now, bytes)

    # rate limit = None
    fd = FileDownloader({'ratelimit': None})
    fd.to_screen = lambda *x: None
    fd.sleep = lambda *x: None
    call_slow_down(fd, time.time(), None, 0)
    call_slow_down(fd, time.time(), None, 1)

    # rate limit = 1 B/s
    fd = FileDownloader({'ratelimit': 1})
    fd.to_screen = lambda *x: None
    fd.sleep = lambda x: None
    call_slow_down(fd, time.time(), None, 1)



# Generated at 2022-06-14 15:10:12.582257
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(None, None)
    # Test without rate limit
    start = time.time()
    fd.slow_down(start, start + 3, 3)  # Go super-fast, but don't sleep
    # Test with rate limit
    fd.params['ratelimit'] = 2
    fd.slow_down(start, start + 3, 3)  # Go super-fast, sleep 2 seconds
    assert time.time() - start == 2



# Generated at 2022-06-14 15:10:23.920078
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(None, None)

    # Test download speed under rate limit
    start = time.time()
    fd.slow_down(start, start+1, 2048)
    assert time.time()-start < 1.0

    # Test download speed over rate limit
    start = time.time()
    fd.slow_down(start, start+1, 4096)
    assert time.time()-start >= 1.0

    # Test download speed over rate limit, rate limit set to half the speed
    fd.params['ratelimit'] = 1024.0
    start = time.time()
    fd.slow_down(start, start+1, 4096)
    assert time.time()-start >= 2.0



# Generated at 2022-06-14 15:10:35.474552
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    ydl = YoutubeDL()
    ydl.params['ratelimit'] = 2
    ydl.params['retries'] = 0
    ydl.params['nooverwrites'] = True
    fd = FileDownloader(ydl, {'url': 'foo'})

    fd._do_slow_down(1.0, 100.0, 10.0)
    assert True

    fd._do_slow_down(5.5, 50.0, 10.0)
    assert True

    # The following 3 tests test that the download speed stays below the
    # rate limit.
    time.sleep(1.0)
    start = time.time()
    fd._do_slow_down(start, 0.0, 10.0)
    assert time.time() - start < 1.0

# Generated at 2022-06-14 15:10:48.109605
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import sys
    import math

    # Fake FileDownloader.report_progress
    class FakeFD(FileDownloader):
        def __init__(self):
            pass

        def report_progress(self, s):
            sys.stdout.write('\r [%s]' % s['_percent_str'])
            sys.stdout.flush()

    fd = FakeFD()
    filename = '-'

    # Test percent string
    s = {'_percent_str': '1'}
    fd.report_progress(s)
    assert fd._last_percent_str == '1', 'Test 1 failed'

    s = {'_percent_str': '10'}
    fd.report_progress(s)
    assert fd._last_percent_str == '10', 'Test 10 failed'

    s

# Generated at 2022-06-14 15:10:58.195788
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    def check(bytestr, expected):
        assert FileDownloader.parse_bytes(bytestr) == expected

    # Decimal prefixes
    check('1', 1)
    check('10', 10)
    check('100', 100)
    check('1k', 1024)
    check('1.1k', 1024 + 102.4)
    check('1.2k', 1024 + 204.8)
    check('1.3k', 1024 + 307.2)
    check('1.4k', 1024 + 409.6)
    check('1.5k', 1024 + 512.0)
    check('1.6k', 1024 + 614.4)
    check('1.7k', 1024 + 716.8)
    check('1.8k', 1024 + 819.2)

# Generated at 2022-06-14 15:11:06.673431
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    """
    Description:
    Check method download of class FileDownloader
    
    Note:
    We are going to check if the download works fine, in order to do it we will create a temporary directory in the TEMP env variable, then we will create a temporary file inside this directory. The download method will perform download operation on the file and will return True if everything goes well. Finally, we will remove the directory and check the assertion, if the download method returns True, the test will pass, otherwise it will fail.
    
    """
    
    

# Create a temporary directory in the TEMP env variable
    temp_dir = tempfile.mkdtemp( prefix='temp_pytube_' )
# Create a temporary file inside the temporary directory created before
    temp_file_path = os.path.join( temp_dir, 'temp_video_file' )
    temp_file

# Generated at 2022-06-14 15:11:18.893397
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    class FileDownloaderSubclass(FileDownloader):
        def __init__(self, ydl):
            super(FileDownloaderSubclass, self).__init__(ydl)

    ydl = MockYdl()
    fd = FileDownloaderSubclass(ydl)
    assert fd.temp_name('foo') == 'foo'
    assert fd.temp_name('foo.part') == 'foo'
    assert fd.temp_name('foo-part.bar') == 'foo-part.bar'
    assert fd.temp_name('foo-part') == 'foo-part'
    assert fd.temp_name('foo-part.bar.part') == 'foo-part.bar'
    assert fd.temp_name('foo.part.bar') == 'foo.part.bar'


# Generated at 2022-06-14 15:11:33.395204
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    print('testing FileDownloader.download')

    sys.path.append(os.getcwd())

    import youtube_dl
    import os

    class MockInfoDict(dict):
        def __init__(self, test_file_size=None):
            self.test_file_size = test_file_size
            dict.__init__(self)

        def _set_info(self, name, value):
            self[name] = value

        def __setitem__(self, name, value):
            dict.__setitem__(self, name, value)
            if name == 'ext':
                self._set_info('url', 'http://www.youtube.com/watch?v=BaW_jenozKc&t=4s')

# Generated at 2022-06-14 15:11:46.187372
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    """
    Test the speed regulation by a mock object of FileDownloader
    """
    # --- This is the mock object
    class MockFD:
        def __init__(self):
            self.params = {'ratelimit': None}
            self.to_screen_calls = list()

        def to_screen(self, *args):
            self.to_screen_calls.extend(args)

    # --- This is the test
    fd = MockFD()
    for bytes in [None, 0, 1024, 1024*1024]:
        for duration in [None, 0.0, 0.1, 1.0]:
            for ratelimit in [None, 5*1024, 100*1024]:
                # --- Preparation
                fd.params['ratelimit'] = ratelimit
                # --- Test with no slow down

# Generated at 2022-06-14 15:11:59.367672
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert(FileDownloader.parse_bytes('0') == 0)
    assert(FileDownloader.parse_bytes('1') == 1)
    assert(FileDownloader.parse_bytes('-1') is None)
    assert(FileDownloader.parse_bytes('1k') == 1024)
    assert(FileDownloader.parse_bytes('1K') == 1024)
    assert(FileDownloader.parse_bytes('1ki') is None)
    assert(FileDownloader.parse_bytes('1m') == 1024 ** 2)
    assert(FileDownloader.parse_bytes('1M') == 1024 ** 2)
    assert(FileDownloader.parse_bytes(1024 ** 2) == 1024 ** 2)
    assert(FileDownloader.parse_bytes(1048576) == 1024 ** 2)

# Generated at 2022-06-14 15:12:03.009605
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    actual = FileDownloader.best_block_size(10000, 100)

    # The best block size should be 50, but since we want to
    # download blocks with a size of power-of-2, it will be 64
    expected = 64

    assert actual == expected


# Generated at 2022-06-14 15:12:15.698619
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import pytest
    ydl = YoutubeDL({'outtmpl': '%(title)s.%(ext)s', 'verbose': True})
    ydl.add_progress_hook(lambda status:
        None if status['filename'] == '-'
        else __test_FileDownloader_report_progress(status))
    status = {
        'filename': '-',
        'status': 'downloading',
        'total_bytes': None,
        'downloaded_bytes': None,
        'total_bytes_estimate': None,
        'elapsed': None,
        'speed': None,
        'eta': None,
    }
    fd = FileDownloader(ydl, {'format': 'bestaudio/best'}, {'ie_key': 'Youtube'})

# Generated at 2022-06-14 15:12:27.497281
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    from ydl import YDL
    class DummyFD(object):
        def __init__(self, d):
            self.d = d
        def real_download(self, filename, info_dict):
            self.d['filename'] = filename
            self.d['info_dict'] = info_dict
            return 'success'
    d = {'a': 1}
    def progress_hook(status):
        d['status'] = status
    fd = DummyFD(d)
    fd.params = {
        'sleep_interval': 0,
        'nooverwrites': False,
        'continuedl': True,
        'nopart': True,
        'verbose': True
    }
    fd.ydl = YDL()

# Generated at 2022-06-14 15:12:35.610645
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader({})
    timestr = 'Sun, 06 Nov 1994 08:49:37 GMT'
    time_tuple = (1994, 11, 6, 8, 49, 37, 0, 0, -1)
    filetime = time.mktime(time.struct_time(time_tuple))
    assert fd.try_utime('/tmp', timestr) == filetime
    assert fd.try_utime('/tmp', None) == None
    assert fd.try_utime('/tmp', 'Sun, 06 Nov 1994 08:49:37 GMT') == filetime
    assert fd.try_utime('/tmp', 'Invalid Date') == None

# Generated at 2022-06-14 15:12:48.082434
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    d = FileDownloader(None, params={'nooverwrites': True})
    assert d.best_block_size(10, 1000) == 512
    assert d.best_block_size(10, 1024 * 1024) == 4 * 1024
    assert d.best_block_size(3, 1000) == 1
    assert d.best_block_size(10, 2000) == 1024
    assert d.best_block_size(10, 4 * 1024 * 1024) == 4 * 1024
# FileDownloader._make_cmd restore original behavior of youtube-dl's
# FileDownloader class for _make_cmd function.
# The default '_make_cmd' function introduced in 0006a5c5e5e9a22c6a0dfd2c7fe546ab99a685d7
# with commit message "refactor: make downloader

# Generated at 2022-06-14 15:12:57.650017
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    params = {'logger': MockLogger()}
    fd = FileDownloader(params)

    s = {
        'status': 'finished',
    }
    fd.report_progress(s)
    assert s['elapsed'] is None
    assert s['_elapsed_str'] is None
    assert s['_eta_str'] is None
    assert s['_percent_str'] == '100%'
    assert s['_speed_str'] == 'Unknown speed'
    assert s['_total_bytes_str'] is None
    assert s['total_bytes'] is None
    assert fd.params['logger'].messages[0] == '[download] 100% of Unknown speed ETA Unknown ETA'
    assert fd.params['logger'].messages[1] == '[download] Download completed'

   

# Generated at 2022-06-14 15:13:10.144671
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    test_cases = [
        # 1. filename is a string
        {'filename': u'Temp_file', 'expected': u'[download] Temp_file has already been downloaded'},
        # 2. filename is a unicode string
        {'filename': u'Ähm_file', 'expected': u'[download] Ähm_file has already been downloaded'},
        {'filename': u'Ähm_file\u2713', 'expected': u'[download] Ähm_file✓ has already been downloaded'},
        # 3. filename is a writable object
        {'filename': io.StringIO(), 'expected': u'[download] The file has already been downloaded'}
    ]

    def get_msg(filename):
        msg_str = io.StringIO()

# Generated at 2022-06-14 15:13:47.147679
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    class file(object):
        def __init__(self, src, dest):
            self.name = src
            self.dest = dest
        def read(self):
            return open(self.name, 'rb').read()
    try:
        os.remove('./test_FileDownloader_try_utime_src')
    except:
        pass
    try:
        os.remove('./test_FileDownloader_try_utime_dst')
    except:
        pass
    src = open('./test_FileDownloader_try_utime_src', 'wb')
    src.write(b'foo')
    src.close()
    open('./test_FileDownloader_try_utime_dst', 'wb').close()

# Generated at 2022-06-14 15:13:58.283196
# Unit test for method parse_bytes of class FileDownloader

# Generated at 2022-06-14 15:14:07.787272
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():

    assert '0:00:00' == FileDownloader.format_seconds(0)
    assert '0:00:00' == FileDownloader.format_seconds(0.0)
    assert '0:00:01' == FileDownloader.format_seconds(1)
    assert '0:01:00' == FileDownloader.format_seconds(60)
    assert '1:00:00' == FileDownloader.format_seconds(3600)
    assert '1:00:00' == FileDownloader.format_seconds(3600.0)
    assert '1:01:01' == FileDownloader.format_seconds(3661)

    assert '0:00:00.500' == FileDownloader.format_seconds(0.5)

# Generated at 2022-06-14 15:14:19.798688
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    args = ['-f', 'bestaudio', 'https://www.youtube.com/watch?v=xf6_vTARnYg', '--no-playlist']
    fd = FileDownloader(YoutubeDL(params=args), args[-1], args[-2])
    fd.slow_down(0, 1, 1024)
    fd.params['ratelimit'] = None
    fd.slow_down(0, 1, 1024)
    fd.params['ratelimit'] = 1024
    fd._sleep_time = 1
    fd.slow_down(0, 0, 0)
    fd.params['ratelimit'] = 0
    fd.slow_down(0, 0, 0)


# Generated at 2022-06-14 15:14:27.118642
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    fd = FileDownloader(FakeInfoExtractor(), {}, True)
    # test a simple case
    assert fd.calc_eta(0.0, 0.0, 10, 100) == 10
    # test a simple case
    assert fd.calc_eta(0.0, 10.0, 100, 1000) == 90
    # test a division by zero
    assert fd.calc_eta(0.0, 0.0, 10, 0) == None


# Generated at 2022-06-14 15:14:37.327147
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    assert FileDownloader.undo_temp_name('test.test.test') == 'test.test.test'
    assert FileDownloader.undo_temp_name('test.test.test.part') == 'test.test.test'
    assert FileDownloader.undo_temp_name('test.test.test.partaa') == 'test.test.test.partaa'
    assert FileDownloader.undo_temp_name('test.part') == 'test'
    assert FileDownloader.undo_temp_name('test.partaa') == 'test.partaa'
    assert FileDownloader.undo_temp_name('test.') == 'test.'

# Generated at 2022-06-14 15:14:49.557942
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    def _test_size(size):
        fd = FileDownloader({})
        for cursize in [0, 1, size, size - 1, size + 1, 2 * size, 2 * size - 1, 2 * size + 1]:
            assert fd.best_block_size(1, cursize) == size
            assert fd.best_block_size(10, cursize) == size
            assert fd.best_block_size(100, cursize) == size
    _test_size(1)
    _test_size(1024)
    _test_size(10 * 1024)
    _test_size(100 * 1024)
    _test_size(1024 * 1024)
    _test_size(10 * 1024 * 1024)
    _test_size(100 * 1024 * 1024)

# Generated at 2022-06-14 15:15:00.173816
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    """Unit testing for method report_progress of class FileDownloader.
    """
    # Define function that will be passed as a parameter to report_progress.
    def test_print_status(status):
        # Print the status
        print(status)

    # Create a FileDownloader object.
    fd = FileDownloader({}, youtube_dl.FileDownloader)

    # Test the report_progress method.
    for i in range(10):
        # Test values for status.
        status = {'downloaded_bytes': i * 100,
                  'total_bytes': 1000,
                  'download_percent_str': i * 100,
                  'speed': i * 100,
                  'eta': (10 - i) * 100,
                  'status': 'downloading'}

        # Call the report progress method with the test_print_status function

# Generated at 2022-06-14 15:15:10.222483
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    _f = FileDownloader({})
    f = (_f.try_utime, '%(filename)s', None)
    mt = '123456789'
    t = time.time() - 123456.7
    assert f[0](f[1] % {'filename': 'filename'}, f[2]) is None
    assert f[0](f[1] % {'filename': 'filename'}, mt) is None
    assert f[0](f[1] % {'filename': 'filename'}, '0') is None
    assert f[0](f[1] % {'filename': 'filename'}, '0.0') is None
    assert f[0](f[1] % {'filename': 'filename'}, 'abc') is None

# Generated at 2022-06-14 15:15:22.071720
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    import unittest
    import attr

    class TestParams(object):
        def __init__(self, nopart):
            self.nopart = nopart

    @attr.s
    class TestFileDownloader(FileDownloader):
        params = attr.ib()

    def check_temp_name(nopart, filename, expected):
        fd = TestFileDownloader(params=TestParams(nopart=nopart))
        temp_name = fd.temp_name(filename)
        assert temp_name == expected, \
            "temp_name('%s') for nopart=%s should be %s, not %s" % (
                filename, nopart, expected, temp_name)

    # temp_name without nopart

# Generated at 2022-06-14 15:16:09.874822
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    pass

# Generated at 2022-06-14 15:16:17.874715
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    open(encodeFilename(os.path.join(TEST_TMPDIR, 'foo')), 'wb').close()
    fd = FileDownloader(DummyYDL())
    progress = {
        'filename': 'foo',
        'status': 'downloading',
        'downloaded_bytes': 10,
        'total_bytes': 20,
        'speed': 'n/a',
    }
    fd.report_destination('foo')
    fd.report_progress(progress)

    progress.update({
        'eta': 1200,
        'total_bytes_estimate': 20,
    })
    fd.report_progress(progress)

    progress.update({
        'speed': 'n/a',
        'eta': None,
        'elapsed': 0,
    })
    fd.report

# Generated at 2022-06-14 15:16:26.665067
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Set up some test files
    def _save_time(name):
        fd, path = mkstemp(name)
        os.fdopen(fd).close()
        os.utime(path, (1, 2))
        return path

    file_name = _save_time('_test-FileDownloader_try_utime-%s')

# Generated at 2022-06-14 15:16:35.122104
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class TestFileDownloader(object):
        def __init__(self, **kw):
            self.__dict__ = kw
            self.__dict__.setdefault('params', {})
            self.__dict__.setdefault('to_screen', lambda *a, **k: None)

    d = TestFileDownloader()

    d.params.update({'ratelimit': 1048576, 'noprogress': True})

    start = time.time()
    cur = 0
    while cur < 1000000:
        d.slow_down(start, None, cur)
        cur += 1000

    print('OK')


# Generated at 2022-06-14 15:16:45.992607
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    try: # screen is not defined
        screen = None
    except Exception: # screen is not defined
        screen = None


# Generated at 2022-06-14 15:16:56.786794
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    def _run(nopart, filename, expected):
        params = {
            'nopart': nopart,
        }
        ydl = YoutubeDL(params)
        fd = FileDownloader(ydl, {'url': 'http://example.com/video.mp4'}, {'id': 'video.mp4'})
        assert fd.temp_name(filename) == expected
    _run(False, 'filename.mp4', 'filename.mp4.part')
    _run(False, '-', '-')
    _run(True, 'filename.mp4', 'filename.mp4')
    _run(True, '-', '-')


# Generated at 2022-06-14 15:17:06.071074
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import tempfile
    import shutil
    import os.path

    dl = FileDownloader({})
    tmpd = tempfile.mkdtemp()
    tmpf = os.path.join(tmpd, 'a')
    tmpf2 = dl.temp_name(tmpf)
    outf, outfname = tempfile.mkstemp()
    os.close(outf)
    outf = file(outfname, 'wb')
    outf2 = file(tmpf2, 'wb')
    os.unlink(outfname)


# Generated at 2022-06-14 15:17:18.277205
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import time
    from .utils import get_pycurl_version
    if not get_pycurl_version() or get_pycurl_version() < (7, 42, 0):
        # TODO: Actually test this method. This will run only if we use
        # internal curl
        return
    fd = FileDownloader(dict())
    fd.to_screen = lambda x: sys.stderr.write(x + '\n')
    fd.report_progress({
        'downloaded_bytes': 0,
        'elapsed': 0,
        'eta': 0,
        'speed': 0,
        'status': 'downloading',
        'total_bytes': None,
        'total_bytes_estimate': 1000,
    })