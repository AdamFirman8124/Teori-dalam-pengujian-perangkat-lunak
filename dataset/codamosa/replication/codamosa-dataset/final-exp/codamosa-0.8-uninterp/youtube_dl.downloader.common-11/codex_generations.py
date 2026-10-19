

# Generated at 2022-06-14 15:08:15.249307
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    # For a given (elapsed time, bytes), FileDownloader.best_block_size
    # should always return the same value.
    # We test that by performing a few (elapsed time, bytes) -> block_size
    # conversions and ensure that we get the same block size for all of them.
    consistency = {}
    for elapsed_time in (10.0, 20.0, 30.0, 40.0, 50.0):
        for bytes in (1048576, 2097152, 3145728, 4194304, 5242880):
            dl = FileDownloader({})
            block_size = dl.best_block_size(elapsed_time, bytes)
            consistency.setdefault((block_size, elapsed_time), set()).add(bytes)


# Generated at 2022-06-14 15:08:25.738889
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader({})
    assert fd.parse_bytes('1') == 1
    assert fd.parse_bytes('10') == 10
    assert fd.parse_bytes('100') == 100
    assert fd.parse_bytes('1k') == 1024
    assert fd.parse_bytes('1K') == 1024
    assert fd.parse_bytes('10K') == 10*1024
    assert fd.parse_bytes('1M') == 1024*1024
    assert fd.parse_bytes('1G') == 1024*1024*1024
    assert fd.parse_bytes('1.5k') == 1024 + 512
    assert fd.parse_bytes('1.1k') == 1024 + 100
    assert fd.parse_bytes('1.2k') == 1024 + 200
    assert fd.parse_

# Generated at 2022-06-14 15:08:31.505700
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import time

    # We create an instance of FileDownloader to use its slow_down method
    filename = 'fake_name'
    params = {
        'continuedl': True}
    fd = FileDownloader(params, None)

    # Test if the rate is infinite
    fd.params['ratelimit'] = None
    start_time = time.time()
    fd.slow_down(start_time, None, 10000000)
    assert time.time() - start_time < 0.00001
    # Test if we have to slow down
    fd.params['ratelimit'] = 5
    start_time = time.time()
    fd.slow_down(start_time, None, 10000000)
    assert time.time() - start_time > 0.2
    # Test if the rate is zero
    f

# Generated at 2022-06-14 15:08:37.093644
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # Test unit implementation
    import sys
    import tempfile
    temp_dir = tempfile.gettempdir()
    c = FileDownloader(None)
    #
    assert c.temp_name("a1") == "a1"
    #
    assert c.temp_name("a2.b") == "a2.b"
    #
    assert c.temp_name("a3.part.b") == "a3.part.b"
    #
    assert c.temp_name("a4") == "a4.part"
    #
    assert c.temp_name("a5.b") == "a5.b.part"
    #
    assert c.temp_name("a6.b.part") == "a6.b.part"
    #

# Generated at 2022-06-14 15:08:42.549558
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({})
    res = fd.report_progress({
        'downloaded_bytes': 1025,
        'total_bytes': 10240,
        'elapsed': 5,
        'speed': 1024,
        'status': 'downloading',
        })
    assert res == None
    res = fd.report_progress({
        'downloaded_bytes': 10240,
        'total_bytes': 10240,
        'elapsed': 5,
        'speed': 1024,
        'status': 'finished',
        })
    assert res == None
    res = fd.report_progress({
        'downloaded_bytes': 10240,
        'total_bytes': 10240,
        'elapsed': 5,
        'speed': 1024,
        'status': 'finished',
        })

# Generated at 2022-06-14 15:08:50.713231
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():

    def test_equal(blocksize, elapsed_time, bytes):
        if FileDownloader.best_block_size(elapsed_time, bytes) != blocksize:
            raise ValueError(
                'best_block_size returned %d instead of %d' %
                (FileDownloader.best_block_size(elapsed_time, bytes), blocksize))
    test_equal(4194304, 0.1, 4194304 * 2)
    test_equal(4194304, 0.1, 4194304 * 2 + 1)
    test_equal(4194304, 0.1, 4194304 * 2 - 1)
    test_equal(1, 0.1, 1)
    test_equal(4194304, 1, 4194304 * 2)

# Generated at 2022-06-14 15:08:56.129521
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    """
    Test FileDownloader.try_utime.
    """

    from ytdl_discord import utils

    fd = FileDownloader(ydl=None)
    filename = os.path.join(tempfile.gettempdir(), 'test_try_utime_filename')

# Generated at 2022-06-14 15:09:08.815165
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    TestData = [
        ("Test with default args", 0, 100, 8192),
        ("Test with bytes=0", 0, 0, 1),
        ("Test with elapsed_time=0.0", 0.0, 100, 4194304),
        ("Test with elapsed_time=0.0001", 0.0001, 100, 419430400),
        ("Test with bytes=1 and elapsed_time=0.1", 0.1, 1, 41943040),
        ("Test with bytes=1 and elapsed_time=0.001", 0.001, 1, 4194304),
        ("Test with bytes=10 and elapsed_time=0.1", 0.1, 10, 4194304),
    ]
    for (desc, elapsed_time, bytes, expResult) in TestData:
        res = FileDownloader.best_block_size

# Generated at 2022-06-14 15:09:13.978519
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():

    fd = FileDownloader({'continuedl' : True}, None)

    cases = [('foo', 'foo'), ('foo.part', 'foo'), ('foo-part', 'foo-part')]
    for case in cases:
        assert fd.undo_temp_name(case[0]) == case[1]


# Generated at 2022-06-14 15:09:24.898298
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({'noprogress': True})
    fd.to_screen = lambda *args, **kargs: sys.stdout.write(args[0])

    assert(fd.format_percent(0) == 'Unknown %')
    assert(fd.format_percent(0.0) == 'Unknown %')
    assert(fd.format_percent(0.0010) == 'Unknown %')
    assert(fd.format_percent(0.0100) == 'Unknown %')
    assert(fd.format_percent(0.01000) == 'Unknown %')
    assert(fd.format_percent(0.010000) == 'Unknown %')
    assert(fd.format_percent(1) == 'Unknown %')
    assert(fd.format_percent(0.5) == 'Unknown %')

# Generated at 2022-06-14 15:09:55.407477
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from StringIO import StringIO

    if hasattr(sys.stderr, 'isatty') and sys.stderr.isatty():
        class FakeStdErr(StringIO):
            def isatty(self):
                return True
    else:
        class FakeStdErr(StringIO):
            def isatty(self):
                return False
            def write(self, s):
                StringIO.write(self, s.replace('\x1b[K', ''))

    old_stderr = sys.stderr

# Generated at 2022-06-14 15:10:01.194628
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    f = FileDownloader({})
    assert f.calc_speed(100, 1000, 100000) == 1000
    assert f.calc_speed(100, 1000, 0) is None
    assert f.calc_speed(1000, 100, 100000) is None
    assert f.calc_speed(100, 1000, None) is None


# Generated at 2022-06-14 15:10:07.992806
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    #assert_method_returns_expected_result
    #assert_equal
    #assert_raises
    # FileDownloader.report_file_already_downloaded()
    print('test_FileDownloader_report_file_already_downloaded')
    main('https://www.youtube.com/watch?v=EwTZ2xpQwpA')
    # No need to assert anything. If it runs without crashing,
    # the test passes.

# Generated at 2022-06-14 15:10:13.754686
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class FakeDownloader(FileDownloader):
        def real_download(self, filename, info_dict):
            pass

    ydl = FakeDownloader(FakeInfoDict())
    ydl.slow_down(0, 0, 0)  # Does not crash


if __name__ == '__main__':
    test_FileDownloader_slow_down()

# Generated at 2022-06-14 15:10:26.284036
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    with unittest.mock.patch('youtube_dl.downloader.fancy_downloader.open', create=True) as open:
        ydl = FileDownloader(FakeYoutubeDL(), {})
        ydl.params['forceurl'] = True
        ydl.params['ratelimit'] = False
        ydl.params['nooverwrites'] = False
        ydl.params['continuedl'] = False
        ydl.params['noprogress'] = True
        ydl.params['quiet'] = True
        ydl.to_screen = unittest.mock.Mock()

        ydl.real_download = unittest.mock.Mock()

        # Test external downloader set

# Generated at 2022-06-14 15:10:37.120034
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    t = FileDownloader({})
    assert t.undo_temp_name('abc.part') == 'abc'
    assert t.undo_temp_name('abc') == 'abc'
    assert t.undo_temp_name('a/b/c/d.part') == 'a/b/c/d'
    assert t.undo_temp_name('a/b/c/d.part.part') == 'a/b/c/d.part'
    assert t.undo_temp_name('/a/b/c/d.part') == '/a/b/c/d'
    assert t.undo_temp_name('/a/b/c') == '/a/b/c'
    assert t.undo_temp_name('/a/b/c.part') == '/a/b/c'

# Generated at 2022-06-14 15:10:49.800343
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    fd = FileDownloader({})
    assert fd.format_retries(float('inf')) == 'inf'
    assert fd.format_retries(0) == '0'
    assert fd.format_retries(1) == '1'
    assert fd.format_retries(2) == '2'
    assert fd.format_retries(3) == '3'
    assert fd.format_retries(4) == '4'
    assert fd.format_retries(5) == '5'
    assert fd.format_retries(6) == '6'
    assert fd.format_retries(7) == '7'
    assert fd.format_retries(8) == '8'
    assert fd.format_retries(9) == '9'

# Generated at 2022-06-14 15:10:56.379105
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    print("testing FileDownloader.slow_down")
    from . import FakeYDL
    ydl = FakeYDL()
    f = FileDownloader(ydl, {'retries': 0})
    import time
    f.slow_down(time.time(), time.time(), 0)
    f.slow_down(time.time(), time.time(), 1024)
    f.slow_down(time.time(), time.time(), 1024*1024)
    if ydl.msgs:
        print("FAILED")
        print("\n".join(ydl.msgs))
    else:
        print("OK")


# Generated at 2022-06-14 15:11:04.557213
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile
    import os
    from datetime import timedelta
    fd, file_name = tempfile.mkstemp()

# Generated at 2022-06-14 15:11:09.968562
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader({})
    fd.report_file_already_downloaded(u'foo')
    fd.report_file_already_downloaded(u'bar')
    fd.report_file_already_downloaded(b'unicode')



# Generated at 2022-06-14 15:11:31.988842
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader({})

    assert fd.parse_bytes('21023') == 21023
    assert fd.parse_bytes('21023k') == 21023 * 1024
    assert fd.parse_bytes('2102M') == 21023 * 1024**2
    assert fd.parse_bytes('4G') == 4 * 1024**3
    assert fd.parse_bytes('4T') == 4 * 1024**4
    assert fd.parse_bytes('4P') == 4 * 1024**5
    assert fd.parse_bytes('4E') == 4 * 1024**6
    assert fd.parse_bytes('4Z') == 4 * 1024**7
    assert fd.parse_bytes('4Y') == 4 * 1024**8

# Generated at 2022-06-14 15:11:44.301012
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    class FakeYDL(object):
        params = {}
        def trouble(self, *args, **kargs):
            pass
    fd = FileDownloader(FakeYDL())
    assert fd.temp_name('a') == 'a'
    fd.params['nopart'] = True
    assert fd.temp_name('a') == 'a'
    fd.params['nopart'] = False
    assert fd.temp_name('a') == 'a.part'
    assert fd.temp_name('a.part') == 'a.part'
    assert fd.temp_name('.a.part') == '.a.part'
    d = PlatformSpecific()
    d.mkdir('a')
    assert fd.temp_name('a') == 'a.part'
    d.rm

# Generated at 2022-06-14 15:11:51.616460
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader(None, {})
    assert fd.parse_bytes("10") == 10
    assert fd.parse_bytes("10k") == 10 * 1024
    assert fd.parse_bytes("10M") == 10 * 1024**2
    assert fd.parse_bytes("10G") == 10 * 1024**3
    assert fd.parse_bytes("10T") == 10 * 1024**4
    assert fd.parse_bytes("10P") == 10 * 1024**5
    assert fd.parse_bytes("10E") == 10 * 1024**6
    assert fd.parse_bytes("10Y") == 10 * 1024**7
    assert fd.parse_bytes("10y") == 10 * 1024**7
    assert fd.parse_bytes("10.1k") == 10 * 1024 + 1024 / 10

# Generated at 2022-06-14 15:12:03.050229
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():

    # test case #1
    params = {'nopart': True, 'continue_dl': False, 'nooverwrites': False}
    fd = FileDownloader(params)
    assert fd.temp_name('abc.mp4') == 'abc.mp4'
    assert fd.temp_name('abc/abc.mp4') == 'abc/abc.mp4'
    assert fd.temp_name('abc/abc') == 'abc/abc'
    assert fd.temp_name('abc') == 'abc'

    # test case #2
    params = {'nopart': False, 'continue_dl': False, 'nooverwrites': False}
    fd = FileDownloader(params)
    assert fd.temp_name('abc.mp4') == 'abc.mp4.part'

# Generated at 2022-06-14 15:12:10.670010
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    ydl = YoutubeDL()
    ydl.params = {}
    ydl.to_screen = lambda x: print(x)
    ydl.to_console_title = lambda x: print(x)
    fd = FileDownloader(ydl)
    fd.report_progress({
        'status': 'downloading',
        '_percent_str': '3.14%',
        '_eta_str': '2:59',
        '_speed_str': '21.6KiB/s',
        '_total_bytes_str': '100KiB',
        'downloaded_bytes': 31415})

    fd.report_progress({
        'status': 'finished',
        'total_bytes': 100*1024})

# Generated at 2022-06-14 15:12:20.564695
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from youtube_dl.YoutubeDL import YoutubeDL

    ydl = YoutubeDL({})

    ydl.to_screen = lambda x: None
    ydl.to_console_title = lambda x: None
    ydl_fd = FileDownloader(ydl, {'noprogress': False})
    ydl.report_warning = lambda *args, **kargs: None

    def x(): pass
    ydl_fd.add_progress_hook(x)
    ydl_fd.report_progress({
        'status': 'downloading',
        'filename': 'foo',
        'eta': 10,
        'total_bytes_estimate': 100,
        'downloaded_bytes': 10,
        'speed': 1,
    })

    from collections import namedtuple
    Status = namedtuple('Status', 'status')

# Generated at 2022-06-14 15:12:31.980047
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    dl = FileDownloader({})
    dl.params = {'buffer_size': '512'}
    assert dl.best_block_size(0.0, 0) == 512
    assert dl.best_block_size(0.0, 1024) == 1024
    assert dl.best_block_size(0.0, 4096) == 4096
    assert dl.best_block_size(0.0, 16777216) == 4194304

    dl.params = {'buffer_size': '4M'}
    assert dl.best_block_size(0.0, 0) == 4194304
    assert dl.best_block_size(0.0, 1024) == 4194304
    assert dl.best_block_size(0.0, 4096) == 4194304
    assert d

# Generated at 2022-06-14 15:12:44.683407
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def _test(rate_limit, now, start_time, byte_counter, expected_sleep):
        sleep_time = sdt.slow_down(start_time, now, byte_counter)
        assert sleep_time == expected_sleep, \
            'Rate limit %s, now %s, start_time %s, byte_counter %s, expected_sleep: %s, got %s' % \
            (rate_limit, now, start_time, byte_counter, expected_sleep, sleep_time)
    sdt = FileDownloader({'ratelimit': None})
    _test(None, 1.0, 0.0, 100, None)
    _test(None, 1.0, 0.0, 0, None)
    sdt = FileDownloader({'ratelimit': 50})

# Generated at 2022-06-14 15:12:55.318711
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():

    def blocksize_helper(best_block_size_func, t, s, b, r):
        res = best_block_size_func(t, b)
        if res != r:
            raise ValueError('TEST FAILED: best_block_size(%s, %s) returned %s, should be %s' %
                             (t, b, res, r))

    blocksize_helper(FileDownloader.best_block_size, 0, 0, 1, 1)
    blocksize_helper(FileDownloader.best_block_size, 0.001, 1, 1, 4194304)
    blocksize_helper(FileDownloader.best_block_size, 0.1, 10, 1, 1)

# Generated at 2022-06-14 15:13:07.501698
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    from ..utils import encode_compat_str

    handle, testfilename = tempfile.mkstemp(prefix=encode_compat_str('youtube-dl-'))
    os.close(handle)
    handle, testfilename_part = tempfile.mkstemp(prefix=encode_compat_str('youtube-dl-%s.' % os.path.basename(testfilename)))
    os.close(handle)

    fd = FileDownloader(DummyYtdl(), {'noprogress': True})

    assert fd.undo_temp_name(testfilename_part) == testfilename

    os.unlink(testfilename_part)
    os.unlink(testfilename)


# Generated at 2022-06-14 15:13:37.973450
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    def test(rate, seconds):
        assert FileDownloader.calc_speed(0, rate * seconds, rate * seconds) == rate
    test(5, 0.5)
    test(5, 0.9)
    test(5, 1)
    test(5, 1.1)
    test(5, 1.5)
    test(5, 2)

# Generated at 2022-06-14 15:13:47.947904
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    url = r'http://localhost/index.html'

# Generated at 2022-06-14 15:13:54.041830
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({'ratelimit': 1048576})
    fd.slow_down(1000.0, 1000.0, 1048576)  # 1024*1024
    fd.slow_down(1000.0, 1000.0, 512000)  # 500*1024
    fd.slow_down(1000.0, 1000.0, 131072)  # 128*1024



# Generated at 2022-06-14 15:13:55.794842
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    assert(FileDownloader.undo_temp_name('abc.part') == 'abc')
    assert(FileDownloader.undo_temp_name('abc') == 'abc')


# Generated at 2022-06-14 15:14:01.349241
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # Arrange
    fd = FileDownloader({'ratelimit': 500})

    # Act
    for i in range(4):
        fd.slow_down(0, 0, 1024)

    # Assert
    assert fd.slow_start is None



# Generated at 2022-06-14 15:14:10.199697
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    if not isinstance(FileDownloader.parse_bytes('2048'), int):
        return False
    if not isinstance(FileDownloader.parse_bytes('2048k'), int):
        return False
    if not isinstance(FileDownloader.parse_bytes('2m'), int):
        return False
    if not isinstance(FileDownloader.parse_bytes('2M'), int):
        return False
    if not isinstance(FileDownloader.parse_bytes('2G'), int):
        return False
    if not isinstance(FileDownloader.parse_bytes('2T'), int):
        return False
    if not isinstance(FileDownloader.parse_bytes('2P'), int):
        return False
    if not isinstance(FileDownloader.parse_bytes('2E'), int):
        return False

# Generated at 2022-06-14 15:14:18.827527
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    """Check that method report_file_already_downloaded works correctly"""
    fd = FileDownloader({})
    fd.to_screen = lambda s: s
    # Test normal behaviour
    assert fd.report_file_already_downloaded("foo") == None
    # Test that UnicodeEncodeError is handled correctly
    assert fd.report_file_already_downloaded("fooä") == None

if __name__ == '__main__':
    test_FileDownloader_report_file_already_downloaded()

# Generated at 2022-06-14 15:14:28.943744
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    # Create a test FileDownloader object
    fd = FileDownloader({})
    fd.report_progress({
        'downloaded_bytes': 0,
        'total_bytes': 100,
        'total_bytes_estimate': 100,
        'elapsed': 1
    })
    # Make sure it can print a percent sign
    fd.report_progress({
        'downloaded_bytes': 0,
        'total_bytes': None,
        'total_bytes_estimate': 100,
        'elapsed': 1
    })
    # Make sure it can handle unknown sizes
    fd.report_progress({
        'downloaded_bytes': 0,
        'total_bytes': None,
        'total_bytes_estimate': None,
        'elapsed': 1
    })
    # Make sure it can handle missing

# Generated at 2022-06-14 15:14:40.654986
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def _elapsed_time(start):
        return time.time() - start

    # Fake elapsed time
    fd = FileDownloader({'ratelimit': 5})
    now = time.time()
    start_time = now - 1.0
    fd.slow_down(start_time, now, 100)

    # Bytes are too few
    start_time = time.time()
    fd.slow_down(start_time, now, 3)

    # Time elapsed is too short
    start_time = time.time()
    fd.slow_down(start_time, _elapsed_time(start_time) + .001, 200)

    # Below rate limit
    start_time = time.time()

# Generated at 2022-06-14 15:14:47.607527
# Unit test for method try_rename of class FileDownloader
def test_FileDownloader_try_rename():
    from youtube_dl.YoutubeDL import YoutubeDL

    def _FileDownloader(*args, **kwargs):
        _FileDownloader.fd = FileDownloader(*args, **kwargs)

    _FileDownloader.fd = None

    FileDownloader.__init__ = _FileDownloader

    def try_rename(self, old_filename, new_filename):
        try_rename.called = True
        try_rename.args = (old_filename, new_filename)
        try_rename.called_with_self = self

    FileDownloader.try_rename = try_rename

# Generated at 2022-06-14 15:15:40.153445
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import unittest
    import tempfile
    import os
    import shutil

    class FakeInfoDict(object):
        def __init__(self, name, length=0, age_limit=0, a_format=None, url=None):
            self.age_limit = age_limit
            self.name = name
            self.length = length
            self.formats = [a_format]
            self.url = url
            self.populated = True

        def __getitem__(self, key):
            return getattr(self, key)

    class FakeSubclass(FileDownloader):
        def real_download(self, filename, info_dict):
            return True

    def fake_time():
        return 0.0

    def fake_sleep(x):
        pass


# Generated at 2022-06-14 15:15:44.374363
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    d = FileDownloader({})
    assert d.undo_temp_name('a.part') == 'a'
    assert d.undo_temp_name('a') == 'a'

# Generated at 2022-06-14 15:15:53.828556
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import unittest

    class Test(unittest.TestCase):
        def test(self):
            a = FileDownloader({})

            a._report_progress_status = lambda x, y: self.assertEqual(
                x, '[download] x% of y at z ETA t')
            a.report_progress({'_percent_str': 'x',
                               '_speed_str': 'z',
                               '_eta_str': 't',
                               'status': 'downloading',
                               'total_bytes': 'y'})

            a._report_progress_status = lambda x, y: self.assertEqual(
                x, '[download] x% of ~y at z ETA t')

# Generated at 2022-06-14 15:16:02.814944
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader(None, None)
    assert fd.parse_bytes('1') == 1
    assert fd.parse_bytes('1k') == 1 * (1 << 10)
    assert fd.parse_bytes('1M') == 1 * (1 << 20)
    assert fd.parse_bytes('1G') == 1 * (1 << 30)
    assert fd.parse_bytes('1T') == 1 * (1 << 40)
    assert fd.parse_bytes('1P') == 1 * (1 << 50)
    assert fd.parse_bytes('1E') == 1 * (1 << 60)
    assert fd.parse_bytes('1Z') == 1 * (1 << 70)
    assert fd.parse_bytes('1Y') == 1 * (1 << 80)
    assert fd

# Generated at 2022-06-14 15:16:08.898480
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    # Setup
    fd = FileDownloader({})
    fd.to_screen = lambda x: x
    fd.report_file_already_downloaded('a')
    # Exercise
    result = fd.to_screen('[download] %s has already been downloaded' % 'a')
    # Verify
    assert result == '[download] a has already been downloaded'


# Generated at 2022-06-14 15:16:10.356685
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # TODO: Test report_progress method
    pass



# Generated at 2022-06-14 15:16:17.162688
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader({}, None)

    tests = [
        # Negative tests
        (None, None),
        (0, None),
        (12012012012012011, None),
        # Positive tests
        (133713371337, 133713371337),
        (133713371337, 133713371337.133713371337),
        (133713371337.133713371337, 133713371337.133713371337),
    ]

    for test in tests:
        assert(fd.try_utime('test', test[0]) == test[1])

# Generated at 2022-06-14 15:16:26.260568
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    fd = FileDownloader({})

    filename = '-'
    info_dict = {'url': 'http://www.youtube.com/watch?v=BaW_jenozKc',
                 'id': 'BaW_jenozKc',
                 'title': 'youtube-dl test video "\'/\\ä↭𝕐',
                 'ext': 'mp4',
                 'format': 'low',
                 'format_id': 'low',
                 'format_note': 'low',
                 'width': 64,
                 'height': 26,
                 'resolution': '64x26',
                 'filesize': 950,
                 'format_list': [],
                 '_filename': 'youtube-dl test video "\'/\\ä↭𝕐.f137.mp4',
                 }
    info_dict_nopart

# Generated at 2022-06-14 15:16:31.178172
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import random
    import time
    random.seed(0)
    fd = FileDownloader({'ratelimit': 10.0})
    byte_counter = 0
    start = time.time()
    for i in range(1000):
        fd.slow_down(start, time.time(), byte_counter)

# Generated at 2022-06-14 15:16:40.351086
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    ydl = FileDownloader({})
    # report_progress can produce outputs on stdout, so we
    # have to redirect stdout to something
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    ydl.report_progress({
        'status': 'finished',
        'total_bytes': 1024,
        'elapsed': 11.99
    })
    assert new_stdout.getvalue() == '[download] 100% of 1.00KiB in 12s\n'

    new_stdout.seek(0)
    new_stdout.truncate(0)

# Generated at 2022-06-14 15:17:08.706249
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    from youtube_dl import FileDownloader
    fd = FileDownloader({})
    assert fd.format_retries(2) == '2'
    assert fd.format_retries(float('inf')) == 'inf'



# Generated at 2022-06-14 15:17:20.038493
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    # Test for case filename is substr of other file and vice-versa
    # Test#1
    filename_1 = 'testfile.txt'
    filename_2 = 'testfile'
    fd = FileDownloader(nullYoutubeDl(), nullOptions())
    fd.report_file_already_downloaded(filename_1)
    fd.report_file_already_downloaded(filename_2)
    # Test#2
    filename_1 = 'testfile'
    filename_2 = 'testfile.txt'
    fd = FileDownloader(nullYoutubeDl(), nullOptions())
    fd.report_file_already_downloaded(filename_1)
    fd.report_file_already_downloaded(filename_2)

