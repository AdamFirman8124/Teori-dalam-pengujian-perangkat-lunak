

# Generated at 2022-06-14 15:08:16.166416
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    test_cases = [
        ('100B', 100),
        ('100.0B', 100),
        ('100.0', 100),
        ('100', 100),
        ('5k', 5000),
        ('5K', 5000),
        ('5kb', 5000),
        ('5Kb', 5000),
        ('5kB', 5000),
        ('5KB', 5000),
        ('5m', 5000 * 1000),
        ('4M', 4000000),
        ('4G', 4000000000),
    ]
    for (test_input, expected_result) in test_cases:
        result = FileDownloader.parse_bytes(test_input)
        assert result == expected_result, '%s is expected to parse to %s but parsed as %s' % (test_input, expected_result, result)


# Generated at 2022-06-14 15:08:26.544527
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    class _FakeCrtc:
        def __init__(self):
            self.__width = 80
            self.__height = 24

        def get_wh(self):
            return (self.__width, self.__height)

    class _FakeTTY:
        def isatty(self):
            return True

        def fileno(self):
            return 1

        def write(self, s):
            pass

    fd = FileDownloader({}, None)
    fd._report_progress_prev_line_length = 0

    if sys.stderr.isatty() or os.name == 'nt':
        sys.stderr = _FakeTTY()
        assert sys.stderr.isatty() == True

# Generated at 2022-06-14 15:08:32.189796
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Test invalid dates
    fd = FileDownloader({})
    assert fd.try_utime('filename', '0') is None
    assert fd.try_utime('filename', '-0') is None
    assert fd.try_utime('filename', '-1000') is None
    assert fd.try_utime('filename', '01/01/01') is None
    assert fd.try_utime('filename', 'now') is None

    # Test valid dates
    for ds in '2001', '2001-02', '2001-02-03', '2001-02-03T04', '2001-02-03T04:05', '2001-02-03T04:05:06Z':
        t = timeconvert(ds)

# Generated at 2022-06-14 15:08:38.612676
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    def test(b, e, o, r, **kw):
        kw['min_blocksize'] = kw.get('min_blocksize', 1024)
        kw['max_blocksize'] = kw.get('max_blocksize', 4194304)
        kw['adjust_blocksize'] = kw.get('adjust_blocksize', True)
        dl = FileDownloader(params=kw)
        return dl.best_block_size(b, e, **o) == r
    assert test(1, 1, {}, 1)
    assert test(1, 1, {'downloaded_bytes': -1}, 1024)
    assert test(1, 1, {'downloaded_bytes': 0}, 1024)
    assert test(1, 1, {'downloaded_bytes': 1}, 1024)

# Generated at 2022-06-14 15:08:47.148006
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader({})
    assert fd.undo_temp_name('a.part') == 'a'
    assert fd.undo_temp_name('a') == 'a'
    assert fd.undo_temp_name('abc.part') == 'abc'
    assert fd.undo_temp_name('abc') == 'abc'
    assert fd.undo_temp_name('a.b.part') == 'a.b'
    assert fd.undo_temp_name('a.b') == 'a.b'
    assert fd.undo_temp_name('.part') == ''
    assert fd.undo_temp_name('') == ''



# Generated at 2022-06-14 15:08:52.561113
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    filename = 'testing_filename'
    downloader = FileDownloader({})
    temp_name = downloader.temp_name(filename)
    assert temp_name == filename + '.part'
    original_name = downloader.undo_temp_name(temp_name)
    assert filename == original_name
    assert temp_name == downloader.temp_name(filename)

# Generated at 2022-06-14 15:08:57.863520
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    import sys
    import os
    import shutil
    import tempfile
    import unittest

    def _touch(filename):
        with open(filename, 'a'):
            pass

    def _remove(filename):
        os.remove(filename)

    class TestFileDownloader(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()
            self.to_delete = []

        def tearDown(self):
            try:
                shutil.rmtree(self.tmpdir)
            except Exception as e:
                if sys.exc_info()[0] == OSError:
                    pass
                else:
                    raise e

# Generated at 2022-06-14 15:09:09.426853
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader(params={}, ydl=None)

    assert fd.parse_bytes('1') == 1
    assert fd.parse_bytes('1.5') == 1
    assert fd.parse_bytes('12') == 12
    assert fd.parse_bytes('1.25k') == 1280
    assert fd.parse_bytes('2k') == 2048
    assert fd.parse_bytes('3.5M') == 3686400
    assert fd.parse_bytes('4.7G') == 5067886592
    assert fd.parse_bytes('5.1T') == 561375366635520
    assert fd.parse_bytes('-1') == None
    assert fd.parse_bytes('-1.5') == None
    assert fd.parse_bytes('a')

# Generated at 2022-06-14 15:09:21.150191
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class FakeFileDownloader:
        def __init__(self, params={}):
            self.params = params
            self.params['nooverwrites'] = False
            self.params['noprogress'] = False
            self.params['sleep_interval'] = None
            self.params['max_sleep_interval'] = None
            self.params['ratelimit'] = None
            self.to_screen = lambda x: None

    fd = FileDownloader({'ratelimit': '10240'})
    fd._debug_cmd = lambda x: None

    def sleep_and_get_time(s):
        time.sleep(s)
        return time.time()

    fd.to_screen = lambda x: None
    # Speed is under the limit

# Generated at 2022-06-14 15:09:29.213967
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(
        params={'nopart': True},
        ydl=YoutubeDL({})
    )
    assert fd.temp_name('abc.part') == 'abc.part'
    assert fd.temp_name('abc.xyz.part') == 'abc.xyz.part'
    assert fd.temp_name('abc.part.xyz') == 'abc.part.xyz'
    assert fd.temp_name('abc') == 'abc.part'
    assert fd.temp_name('/dir/to/abc') == '/dir/to/abc.part'

    fd = FileDownloader(
        params={'nopart': False},
        ydl=YoutubeDL({})
    )

# Generated at 2022-06-14 15:10:07.310439
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    assert FileDownloader.format_seconds(0) == '0:00'
    assert FileDownloader.format_seconds(1) == '0:01'
    assert FileDownloader.format_seconds(2) == '0:02'
    assert FileDownloader.format_seconds(59) == '0:59'
    assert FileDownloader.format_seconds(60) == '1:00'
    assert FileDownloader.format_seconds(61) == '1:01'
    assert FileDownloader.format_seconds(3599) == '59:59'
    assert FileDownloader.format_seconds(3600) == '1:00:00'
    assert FileDownloader.format_seconds(3601) == '1:00:01'

# Generated at 2022-06-14 15:10:19.721680
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    ydl = FakeYoutubeDL()
    fd = FileDownloader(ydl, {})
    d = {
        'downloaded_bytes': 1024,
        'total_bytes': 2048,
        'tmpfilename': 'filename.f',
        'filename': 'filename.f',
        'status': 'downloading',
        'elapsed': 1,
        'speed': None,
        'eta': 10,
    }

    d['_percent_str'] = fd.format_percent(50)
    assert ('[download] %(_percent_str)s of %(_total_bytes_str)s at %(_speed_str)s ETA %(_eta_str)s' % d) == '50% of 2.0KiB at Unknown speed ETA 00:10'

# Generated at 2022-06-14 15:10:27.464231
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    with open('temp_name.out', 'wb') as outf:
        outf.write(b'foo')

    assert FileDownloader(params={}).temp_name('temp_name.out') == 'temp_name.out.part'
    assert FileDownloader(params={'nopart': True}).temp_name('temp_name.out') == 'temp_name.out'

    os.unlink('temp_name.out')

# Generated at 2022-06-14 15:10:37.781024
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(None, None)
    fd.params = {'ratelimit': None}
    assert fd.slow_down(0., 0., 0) is None
    assert fd.slow_down(0., 0.1, 0) is None
    assert fd.slow_down(0., 0., 10) is None
    fd.params = {'ratelimit': 10}
    assert fd.slow_down(0., 0.1, 0) is None
    assert fd.slow_down(0., 0.1, 100) is None
    assert fd.slow_down(0., 0., 100) is not None
    assert fd.slow_down(0., 0.5, 100) is not None
    assert fd.slow_down(0., 0., 10) is None
    time.sleep

# Generated at 2022-06-14 15:10:41.435089
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    assert FileDownloader.undo_temp_name('') == ''
    assert FileDownloader.undo_temp_name('.part') == ''
    assert FileDownloader.undo_temp_name('video.mkv.part') == 'video.mkv'
    assert FileDownloader.undo_temp_name('video.mkv') == 'video.mkv'



# Generated at 2022-06-14 15:10:50.061765
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    # file_downloader_instance.undo_temp_name("some_filename.part") == "some_filename"
    sample_filename = "some_filename"
    assert FileDownloader(None, None, None).undo_temp_name(sample_filename + ".part") == sample_filename
    # file_downloader_instance_2.undo_temp_name("some_filename") == "some_filename"
    sample_filename_2 = "some_filename"
    assert FileDownloader(None, None, None).undo_temp_name(sample_filename_2) == sample_filename_2


# Generated at 2022-06-14 15:11:00.165197
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    """Test the parse_bytes method of FileDownloader."""
    fd = FileDownloader({'test': 1}, None)

    def assert_parsed(bytestr, result):
        assert fd.parse_bytes(bytestr) == result

    assert_parsed(None, None)
    assert_parsed('', None)
    assert_parsed('foo', None)
    assert_parsed('1', 1)
    assert_parsed('2k', 2 * 1024)
    assert_parsed('2.5k', 3 * 1024)
    assert_parsed('3M', 3 * 1024 ** 2)
    assert_parsed('3.5M', 4 * 1024 ** 2)
    assert_parsed('3.5m', 4 * 1024 ** 2)
    assert_

# Generated at 2022-06-14 15:11:07.460347
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import time
    import unittest

    class FileDownloaderTestCase(unittest.TestCase):
        def setUp(self):
            self.downloader = FileDownloader()

        def test_FileDownloader_slow_down(self):
            self.downloader.params['ratelimit'] = 500
            for i in range(10):
                start_time = time.time()
                self.downloader.slow_down(start_time, None, 10000)
                self.assertTrue(
                    0.19 < time.time() - start_time < 0.21,
                    'slow_down is broken.')

    suite = unittest.TestLoader().loadTestsFromTestCase(FileDownloaderTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-14 15:11:11.323709
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    downloader = FileDownloader(None, None)
    for file_name in TEST_FILENAMES:
        downloader.report_file_already_downloaded(file_name)

# Generated at 2022-06-14 15:11:22.261607
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    filename = 'foo.mp4'
    params = {'ratelimit': 5}
    ydl = YoutubeDL(params)
    # for the coverage (globals)
    if 'SUBPROCESS_SETUP_LOCK' not in globals():
        globals()['SUBPROCESS_SETUP_LOCK'] = threading.Lock()
    fd = FileDownloader(ydl, params)

    # ratelimit is None
    params = {'ratelimit': None}
    fd = FileDownloader(ydl, params)
    fd.slow_down(0, 0, 0)

    # downloaded_byte is 0
    params = {'ratelimit': 5}
    fd = FileDownloader(ydl, params)
    fd.slow_down(0, 0, 0)

    # ratelimit is

# Generated at 2022-06-14 15:11:39.478033
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Check that the function returns a timestamp for RFC 1123-compliant
    # timestamps
    fd = FileDownloader({})
    assert fd.try_utime('any_file', 'Thu, 01 Jan 1970 00:00:00 GMT') == 0
    assert fd.try_utime(
        'any_file', 'Tue, 02 Jan 2018 22:39:48 GMT') == 1514898388

    # Check that the function returns None for non-RFC 1123-compliant timestamps
    assert fd.try_utime('any_file', 'any_string') is None

# Generated at 2022-06-14 15:11:40.632027
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    assert True


# Generated at 2022-06-14 15:11:49.790173
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader({})
    def t(v, r):
        a = fd.parse_bytes(v)
        if a != r:
            raise AssertionError('%s != %s' % (a, r))
    t('12345', 12345)
    t('12k', 12 * 1024)
    t('12K', 12 * 1024)
    t('12m', 12 * 1024 * 1024)
    t('12M', 12 * 1024 * 1024)
    t('12g', 12 * 1024 * 1024 * 1024)
    t('12G', 12 * 1024 * 1024 * 1024)
    t('1.0g', int(1.0 * 1024 * 1024 * 1024))
    t('1.2g', int(1.2 * 1024 * 1024 * 1024))

# Generated at 2022-06-14 15:12:01.696012
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import time
    import os
    from .utils import encodeArgument
    dl = FileDownloader({})
    def _get_slow_down_sleep_time():
        if os.name == 'nt':
            times_filename = encodeArgument('times.txt')
            if os.path.exists(times_filename):
                os.remove(times_filename)
        else:
            times_filename = '/dev/shm/ytdl-times.txt'
        with open(times_filename, 'a') as f:
            curr = time.time()
            f.write('%f\n' % curr)
            prev = curr
            if os.path.exists(times_filename):
                with open(times_filename, 'r') as f:
                    for l in f.readlines():
                        prev

# Generated at 2022-06-14 15:12:14.660439
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    from youtube_dl.YoutubeDL import YoutubeDL


    def _try_utime(fd, filetime):
        assert fd._try_utime('nonexistentfilename', filetime) is None
        fd.to_screen('Nonexistent file passed')
        with open(file_name, 'w') as f:
            f.write('dummy content')
        assert fd._try_utime(file_name, filetime) == filetime
        fd.to_screen('Existent file passed')

    fd = FileDownloader({'outtmpl': '%(id)s-%(uploader)s-%(title)s.%(ext)s'}, YoutubeDL())

    fd.to_screen = lambda *x: None

    filetime = 1401854862.0

# Generated at 2022-06-14 15:12:22.868668
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class MockYDL(object):
        def __init__(self):
            self.to_screen_calls = []
            self.to_console_title_calls = []
        def to_screen(self, msg, skip_eol=False):
            self.to_screen_calls.append((msg, skip_eol))
        def to_console_title(self, msg):
            self.to_console_title_calls.append(msg)
    ydl = MockYDL()
    fd = FileDownloader(None, {'ydl': ydl})
    fd.report_progress({'status': 'finished'})
    fd.report_progress({'status': 'foo'})
    assert ydl.to_screen_calls == [
        ('[download] Download completed', True),
    ]

# Generated at 2022-06-14 15:12:33.567633
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    import re
    def check_temp_name(test_case, test_name, fname, nopart, expected):
        fd = FileDownloader({
                'nopart': nopart,
                'outtmpl': '__test__%(id)s__%(ext)s',
            }, None)
        temp_name = fd.temp_name(fname)
        if temp_name != expected:
            test_case.fail('%s: expected %s, got %s' % (
                test_name, expected, temp_name))
        if fname != fd.undo_temp_name(temp_name):
            test_case.fail('%s: expected %s, got %s' % (
                test_name, fname, fd.undo_temp_name(temp_name)))

   

# Generated at 2022-06-14 15:12:46.266924
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    def _run_test(start, current, total, now, eta):
        fd = FileDownloader(YoutubeDL({}))
        fd.to_screen = lambda msg: msg
        assert fd.calc_eta(start, now, current, total) == eta
    _run_test(2, 10, 20, 12, 10)
    _run_test(2, 0, 20, 4, 0)
    _run_test(2, 0, 20, 6, 5)
    _run_test(2, 0, 20, 3, 0)
    _run_test(2, 1, 20, 3, 0)
    _run_test(2, 20, 20, 4, 2)
    _run_test(2, 20, 20, 3, 0)

# Generated at 2022-06-14 15:12:56.332023
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    u"""(test_FileDownloader_calc_eta)"""
    fd = FileDownloader({})
    # Test 1: from 0 to 10 with a speed of 5, it should take 2 seconds
    eta = fd.calc_eta(0, 0, 5, 10)
    assert eta == 2, "Test 1 in test_FileDownloader_calc_eta failed: %r != 2" % eta
    # Test 2: using negative values and checking if it returns None
    eta = fd.calc_eta(0, 0, -5, -10)
    assert eta == None, "Test 2 in test_FileDownloader_calc_eta failed: %r != None" % eta
    # Test 3: from 0 to 3 with a speed of 2, it should take 2 seconds (ETA is rounded down)
   

# Generated at 2022-06-14 15:13:09.259824
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from sys import stderr
    from contextlib import contextmanager

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    @contextmanager
    def _fake_stderr():
        orig_stderr = stderr
        fake_stderr = stderr = StringIO()
        try:
            yield fake_stderr
        finally:
            stderr = orig_stderr

    fd = FileDownloader({'noprogress': False})

# Generated at 2022-06-14 15:13:33.997475
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.FileDownloader import FileDownloader
    f = io.BytesIO()
    ydl = YoutubeDL(f)
    fd = FileDownloader(ydl)
    fd.report_file_already_downloaded('foo')
    assert f.getvalue().decode('utf-8') == '[download] foo has already been downloaded\n'



# Generated at 2022-06-14 15:13:45.435220
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({'logger': MockLogger()})
    # Test 1: no rate limit
    params = {
        'ratelimit': None
    }
    res = fd.slow_down(time.time(), time.time() + 10, 10 * (1024 ** 2), params)
    assert res is None
    # Test 2: rate limit
    params = {
        'ratelimit': 10 * (1024 ** 2)
    }
    res = fd.slow_down(time.time(), time.time() + 10, 10 * (1024 ** 2), params)
    assert res is None
    res = fd.slow_down(time.time(), time.time() + 5, 10 * (1024 ** 2), params)
    assert res == 5

# Generated at 2022-06-14 15:13:52.533998
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Object to be tested
    fd = FileDownloader({})

    # Tests
    # With percent
    test_ret = fd.report_progress({'status' : 'downloading', '_percent_str' : '42%', '_speed_str' : '1.3KiB/s',
                                   '_eta_str' : '3 minutes and 2 seconds'})
    assert test_ret is None

    # Without percent
    test_ret = fd.report_progress({'status' : 'downloading', '_speed_str' : '1.3KiB/s', '_eta_str' : '3 minutes and 2 seconds'})
    assert test_ret is None

    # Without eta

# Generated at 2022-06-14 15:13:58.352187
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert FileDownloader.parse_bytes('1.2') is None
    assert FileDownloader.parse_bytes('a') is None
    assert FileDownloader.parse_bytes(None) is None
    assert FileDownloader.parse_bytes('') is None
    assert FileDownloader.parse_bytes('1024') == 1024
    assert FileDownloader.parse_bytes('1 k') == 1024
    assert FileDownloader.parse_bytes('1 m') == 1024**2
    assert FileDownloader.parse_bytes('1 g') == 1024**3
    assert FileDownloader.parse_bytes('1 t') == 1024**4
    assert FileDownloader.parse_bytes('1 p') == 1024**5
    assert FileDownloader.parse_bytes('1 e') == 1024**6

# Generated at 2022-06-14 15:14:07.235515
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    tests = [
        ('1k', 1024),
        ('1K', 1024),
        ('2048', 2048),
        ('2k', 2048),
        ('2K', 2048),
        ('2m', 2097152),
        ('2.5k', 2560),
        ('2.5K', 2560),
        ('32.5k', 33408),
        ('32.5K', 33408),
        ('2g', 2147483648),
        ('2G', 2147483648)
    ]

    for (test_bytes, result_int) in tests:
        test_result_int = FileDownloader.parse_bytes(test_bytes)
        assert(test_result_int == result_int)


# Generated at 2022-06-14 15:14:09.897847
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader(None, {})
    assert fd.parse_bytes('1') == 1
    assert fd.parse_bytes('2k') == 2 * 1024
    assert fd.parse_bytes('3M') == 3 * 1024 * 1024

# Generated at 2022-06-14 15:14:11.175568
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # TODO
    assert False



# Generated at 2022-06-14 15:14:24.211357
# Unit test for method parse_bytes of class FileDownloader

# Generated at 2022-06-14 15:14:36.945238
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    def do_test_report_progress(params, test_in, test_out):
        fd = FileDownloader(params)
        fd.report_progress(test_in)
        print('Test FileDownloader.report_progress with:\n%s\nExpected:\n%s' % (
            test_in, test_out))
        if test_out != fd.ydl._screen_file.getvalue():
            print('Got:\n%s' % fd.ydl._screen_file.getvalue())
            raise ValueError('Test for method FileDownloader.report_progress failed.')
        fd.ydl._screen_file.seek(0)
        fd.ydl._screen_file.truncate(0)

    params = {'noprogress': False}

    do_test_report

# Generated at 2022-06-14 15:14:39.818782
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    FileDownloader._try_utime('test', 'Thu, 07 Feb 2014 09:47:29 GMT')

if __name__ == '__main__':
    test_FileDownloader_try_utime()

# Generated at 2022-06-14 15:15:14.731032
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Test the FileDownloader method try_utime
    downloader = FileDownloader({})

    def try_utime(filename, last_modified_hdr):
        downloader.try_utime(filename, last_modified_hdr)

    filename = '/tmp/test.file'

    def file_exists(filename):
        return os.path.isfile(filename)

    def file_delete(filename):
        os.unlink(filename)

    fd = os.open(filename, os.O_CREAT)
    os.write(fd, b' ')
    os.close(fd)

# Generated at 2022-06-14 15:15:20.665104
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import os
    import time
    import tempfile

    file_content = b'TESTING FILE_CONTENT'
    fd, tmp_fn = tempfile.mkstemp(suffix='youtube-dl-test.tmp')
    f = open(tmp_fn, 'wb')
    f.write(file_content)
    f.close()
    os.close(fd)


# Generated at 2022-06-14 15:15:29.537337
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    # Test cases (value, #expected result)
    test_cases = {
        'a string without numbers': (None, ),
        '1.53k': (1530, ),
        '99.3g': (99.3*1024*1024*1024, ),
        '100M': (100*1024*1024, ),
        '+123.4 K': (123.4*1024, ),
        '+5.67e8b': (5.67*1e8, ),
        '-5.67e5a': (None, ),
        '100l': (None, ),
        '100.3q': (None, ),
        '0.0001z': (None, ),
        'Inf': (float('inf'), ),
    }


# Generated at 2022-06-14 15:15:42.378448
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class TestFileDownloader(FileDownloader):

        def __init__(self, ydl, params):
            super(TestFileDownloader, self).__init__(ydl, params)
            self._msgs = []

        def to_screen(self, msg, skip_eol=False):
            self._msgs.append(msg)

    ydl = YoutubeDL(dict())
    ydl.params['noprogress'] = False
    ydl.params['progress_with_newline'] = False
    fd = TestFileDownloader(ydl, dict())

    s = dict(
        downloaded_bytes=0,
        elapsed=0,
        status='downloading',
    )
    fd.report_progress(s)

# Generated at 2022-06-14 15:15:50.255599
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    class FakeFileDownloader:
        def to_screen(self, message):
            self.last_message = message
    fd = FakeFileDownloader()
    # Test with UnicodeEncodeError
    fd.report_file_already_downloaded('abcضصث ')
    assert fd.last_message == '[download] The file has already been downloaded'
    # Test without UnicodeEncodeError
    fd.report_file_already_downloaded('abc')
    assert fd.last_message == '[download] abc has already been downloaded'
 

# Generated at 2022-06-14 15:16:00.333953
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from io import BytesIO
    from .YoutubeDL import YoutubeDL # TODO: Move this to ydl.py and import from there.
    from .extractor.common import InfoExtractor
    from .postprocessor.ffmpeg import FFmpegPostProcessor

    # This test is designed to use the module name as a prefix for its test
    # class names to ensure they do not conflict with classes defined in other
    # modules.
    class MockYoutubeDl(YoutubeDL):
        def __init__(self):
            self.to_screen_calls = []
            self.to_console_title_calls = []

        def to_screen(self, msg):
            self.to_screen_calls.append(msg)


# Generated at 2022-06-14 15:16:06.885969
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():

    with make_temp_directory() as td:
        filename = os.path.join(td, 'foo')
        open(filename, 'wb').write(b'x')

        class DummyDownloader(FileDownloader):
            def __init__(self, params, filename):
                FileDownloader.__init__(self, params)
                self.filename = filename

        dl = DummyDownloader({}, filename)

        def get_file_utime(filename):
            return os.path.getmtime(filename)

        assert get_file_utime(filename) == 0
        dl.try_utime(filename, '2014')
        assert get_file_utime(filename) == 1388534400
        dl.try_utime(filename, '2014-12-31 00:00:00')

# Generated at 2022-06-14 15:16:09.908383
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    fd = FileDownloader()

    assert fd.format_retries(1.1) == '1.1'
    assert fd.format_retries(float('inf')) == 'inf'


# Generated at 2022-06-14 15:16:15.302076
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import os
    import ConfigParser
    import tempfile
    import shutil

    # Save original encoder
    (temp_fd, temp_filename) = tempfile.mkstemp(prefix='youtube-dl-test_')
    import youtube_dl.FileDownloader
    tmp_FileDownloader_slow_down = youtube_dl.FileDownloader.FileDownloader.slow_down
    def _slow_down(old_self, start_time, now, byte_counter):
        def get_config():
            c = ConfigParser.ConfigParser()
            c.read(os.path.join(temp_directory, 'config'))
            return c
        import youtube_dl.postprocessor
        youtube_dl.postprocessor.getConfig = get_config

# Generated at 2022-06-14 15:16:22.305034
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    from .YoutubeDL import YoutubeDL
    from .extractor import gen_extractors
    from .version import __version__

    downloader = FileDownloader({}, YoutubeDL(YoutubeDL.params))
    downloader.to_screen = lambda x: print(x)
    downloader.report_file_already_downloaded(__version__)

if __name__ == '__main__':
    test_FileDownloader_report_file_already_downloaded()

# Generated at 2022-06-14 15:17:00.095963
# Unit test for method report_progress of class FileDownloader

# Generated at 2022-06-14 15:17:08.459339
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # Test for a non existing file
    fd = FileDownloader('http://example.com/', {'nopart': True})
    assert fd.temp_name('foo.flv') == 'foo.flv'
    fd = FileDownloader('http://example.com/', {})
    assert fd.temp_name('foo.flv') == 'foo.flv.part'
    fd = FileDownloader('http://example.com/', {})
    assert fd.temp_name('-') == '-'
    # Test for a directory
    if not os.name == 'nt':
        dirname = 'bar_dir'

# Generated at 2022-06-14 15:17:20.188532
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    """
    FileDownloader.temp_name(self, filename)
    """
    def _test(filename, expected):
        real = FileDownloader(None).temp_name(filename)
        assert real == expected, ['%s != %s' % (real, expected)]

    params = {'nopart': True}
    _test('lol.mp4', 'lol.mp4', params)
    params = {'nopart': False}
    _test('lol.mp4', 'lol.mp4.part', params)
    _test('/path/to/file with spaces/video.mp4', '/path/to/file with spaces/video.mp4.part')