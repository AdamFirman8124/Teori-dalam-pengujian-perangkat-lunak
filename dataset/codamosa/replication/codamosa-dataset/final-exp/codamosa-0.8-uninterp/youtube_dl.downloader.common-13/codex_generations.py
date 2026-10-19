

# Generated at 2022-06-14 15:08:01.582034
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    """test undo_temp_name() method of class FileDownloader"""
    fd = FileDownloader(None, {})
    tt = [('abc', 'abc'),
          ('abc.part', 'abc'),
          ('abc.xyz.part', 'abc.xyz')]
    for (i, o) in tt:
        if fd.undo_temp_name(i) != o:
            raise ValueError('test %r failed' % i)


# Generated at 2022-06-14 15:08:12.248672
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader(None)
    fname = __name__ + '.txt'
    f = open(fname, 'w')
    f.write('test')
    f.close()
    st = os.stat(fname)
    assert st.st_mtime == int(time.time())
    # timestamp from 2 seconds in the future
    new_mtime = int(time.time() + 2)
    ret = fd.try_utime(fname, time.strftime('%Y%m%d%H%M.%S', time.gmtime(new_mtime)))
    st = os.stat(fname)
    if sys.platform.startswith('win') or sys.platform == 'cygwin':
        assert st.st_mtime == int(time.time())
        assert ret

# Generated at 2022-06-14 15:08:19.889882
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import collections
    import tempfile
    import os
    import stat

    # Create a dummy file
    fd = tempfile.NamedTemporaryFile(delete=False)
    fd.close()

    # Create a FileDownloader instance
    dler = FileDownloader(dict(), FileDownloader.gen_std_progress_hooks({}))

    # Try to change modification time to the current time
    ft_now = time.time()
    dler.try_utime(fd.name, format_time(ft_now))
    assert int(os.stat(fd.name).st_mtime) == int(ft_now)

    # Make sure 'Unknown time' doesn't work
    dler.try_utime(fd.name, 'Unknown time')

# Generated at 2022-06-14 15:08:30.461595
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # method slow_down with no rate_limit
    fd = FileDownloader({'ratelimit': None})
    fd.slow_down(0, 0, 0)

    # method slow_down with rate_limit < speed
    # (_speed = 2 bytes/second, rate_limit = 1 byte/second)
    # no sleep call
    fd = FileDownloader({'ratelimit': 1})
    fd.slow_down(0, 1, 2)

    # method slow_down with rate_limit > speed
    # (_speed = 2 bytes/second, rate_limit = 3 byte/second)
    # one sleep call
    fd = FileDownloader({'ratelimit': 3})
    fd.slow_down(0, 1, 2)


# Generated at 2022-06-14 15:08:36.320409
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    import filecmp
    import random
    import shutil
    import sys
    import tempfile
    import threading
    import time
    import unittest
    import urllib.error
    import urllib.parse

    class FakeYdl(object):
        pass

    class FakeYdlHooks(object):
        def __init__(self):
            self.hooks = {}

        def add(self, event, hook):
            if event not in self.hooks:
                self.hooks[event] = []
            self.hooks[event].append(hook)

        def remove(self, event, hook):
            if event in self.hooks:
                self.hooks[event].remove(hook)


# Generated at 2022-06-14 15:08:44.646383
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader({})
    assert fd.undo_temp_name('test.mp4') == 'test.mp4'
    assert fd.undo_temp_name('test.mp4.part') == 'test.mp4'


test_inp = (
    ('100b', 100),
    ('100k', 102400),
    ('100m', 104857600),
    ('100g', 107374182400),
)



# Generated at 2022-06-14 15:08:49.902376
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import robot_functions
    reload(robot_functions)
    from robot_functions import *
    
    # (this test is not needed)if 0:
    #     print('download(...)')
    #     youtube_url = 'https://www.youtube.com/watch?v=vw2QZW8OgYI'
    #     FileDownloader().download(youtube_url, 'test1.mp4')
    #     print('\tDone.')


# Generated at 2022-06-14 15:08:58.755105
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    time_start = time.time()
    time_downloaded = time.time() - time_start
    bps = 2000000
    # class DummyFD(object):
    #     def __init__(self, params):
    #         self.params = params
    #     def to_screen(self, message):
    #         pass
    # fd = DummyFD({'ratelimit': bps})
    # fd.slow_down(time_start, time_downloaded, bps)
    # time_downloaded = time.time() - time_start
    # fd.slow_down(time_start, time_downloaded, bps)
    pass

# Generated at 2022-06-14 15:09:10.108876
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    assert FileDownloader.best_block_size(5.5, 100) == 4194304
    assert FileDownloader.best_block_size(2.5, 100) == 4194304
    assert FileDownloader.best_block_size(3.5, 100) == 262144
    assert FileDownloader.best_block_size(2.2, 100) == 262144
    assert FileDownloader.best_block_size(2.2, 1) == 128
    assert FileDownloader.best_block_size(0.1, 1) == 128
    assert FileDownloader.best_block_size(0.1, 1024) == 1024
    assert FileDownloader.best_block_size(0.1, 1025) == 1
    assert FileDownloader.best_block_size(0, 1025) == 1

# Unit test

# Generated at 2022-06-14 15:09:17.375153
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import os

    from .utils import running_in_virtualenv

    # Create temporary file
    tfn = temp_filename('.txt')
    with open(tfn, 'w') as tfp:
        tfp.write('Hello world')

    # Create temporary directory
    tdn = temp_filename('dir')
    os.mkdir(tdn)

    # Failed download
    fd = FileDownloader(
        None, {
            'noprogress': True,
            'quiet': True,
            'nooverwrites': True,
            'outtmpl': os.path.join(tdn, '%(title)s')
        })


# Generated at 2022-06-14 15:09:34.997268
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from collections import namedtuple

    TestCase = namedtuple('TestCase', [
        'status', 'total_bytes', 'downloaded_bytes', 'speed', 'eta', 'elapsed'])

# Generated at 2022-06-14 15:09:47.041711
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    # Time span is less than one millisecond -> no speed
    assert FileDownloader.calc_speed(0, 1, 0) is None
    assert FileDownloader.calc_speed(0, 1, 10) is None
    assert FileDownloader.calc_speed(0, 1, 100) is None
    assert FileDownloader.calc_speed(0, 1, 1000) is None

    # Time span is exactly one millisecond -> no speed
    assert FileDownloader.calc_speed(0, 1000, 0) is None
    assert FileDownloader.calc_speed(0, 1000, 10) is None
    assert FileDownloader.calc_speed(0, 1000, 100) is None
    assert FileDownloader.calc_speed(0, 1000, 1000) is None

    # Time span is greater than one millisecond -> speed

# Generated at 2022-06-14 15:09:56.050397
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    assert FileDownloader.best_block_size(None, 1) == 1
    assert FileDownloader.best_block_size(None, 1023) == 1023
    assert FileDownloader.best_block_size(None, 1024) == 1024
    assert FileDownloader.best_block_size(None, 1025) == 1536
    assert FileDownloader.best_block_size(None, 16384) == 16384
    assert FileDownloader.best_block_size(None, 10000) == 8192
    assert FileDownloader.best_block_size(None, 100000) == 4194304

    assert FileDownloader.best_block_size(0.5, 1) == 2
    assert FileDownloader.best_block_size(0.5, 1023) == 1024

# Generated at 2022-06-14 15:10:07.590699
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader(params={
        'outtmpl': '%(id)s',
        'continuedl': False,
    })
    test_values = [
        {
            "total_bytes": 80000,
            "downloaded_bytes": 64000,
            "speed": 600,
            "eta": 20,
            "status": "downloading",
        },
        {
            "total_bytes": 80000,
            "downloaded_bytes": 64000,
            "speed": 600,
            "eta": 20,
            "status": "finished",
        },
    ]

# Generated at 2022-06-14 15:10:20.028746
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    """Test FileDownloader._try_utime()."""
    import tempfile
    import shutil
    from os.path import exists, getsize, getmtime
    from os import utime
    from time import sleep, mktime, strptime, localtime
    from .utils import DateRange

    def format_time(t):
        """Format a time as Jan 1 1970 00:00:00."""

# Generated at 2022-06-14 15:10:32.360945
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    from io import BytesIO
    from .compat import compat_http_server
    from .compat import compat_urllib_request as urllib_request
    from .compat import compat_urllib_parse as urllib_parse
    from .compat import compat_urllib_error
    from .extractor import gen_extractors

    class DummyServer(compat_http_server.HTTPServer):
        def __init__(self, params, server_address):
            self.params = params
            self.current_file = None
            self.content_sent = 0
            self.next_sender = None
            self.user_agent = None
            self.accept_encoding = None
            self.range_requested = None
            self.range_sent = None
            self.range_requested

# Generated at 2022-06-14 15:10:44.148457
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    from os import path
    from .compat import str
    from .YoutubeDL import YoutubeDL
    from .utils import encodeFilename


# Generated at 2022-06-14 15:10:55.070083
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # Test for nopart
    fd = FileDownloader(None, {'nopart': True})
    assert(fd.temp_name('abc') == 'abc')
    assert(fd.temp_name('d\\ef/g/h') == 'd\\ef/g/h')
    assert(fd.temp_name('abc.def') == 'abc.def')

    # Test for normal case
    fd = FileDownloader(None, {'nopart': False})
    assert(fd.temp_name('abc') == 'abc.part')
    assert(fd.temp_name('d\\ef/g/h') == 'd\\ef/g/h.part')
    assert(fd.temp_name('abc.def') == 'abc.def.part')

    # Test for case where file exists
    fd

# Generated at 2022-06-14 15:11:03.112493
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    assert FileDownloader.calc_speed(0, 0, 0) is None
    assert FileDownloader.calc_speed(0, 0, 1234) is None
    assert FileDownloader.calc_speed(0, 0.001, 0) is None
    assert FileDownloader.calc_speed(0, 0.001, 1234) == 1234000

    assert FileDownloader.calc_speed(0, 5, 0) is None
    assert FileDownloader.calc_speed(2, 3, 1000) == 500

    assert FileDownloader.calc_speed(0, 60, 0) is None
    assert FileDownloader.calc_speed(0, 60, 1000000) == 16666.666666666668



# Generated at 2022-06-14 15:11:15.663762
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    from compat import compat_str
    assert FileDownloader.try_utime('filename', None) == None
    assert FileDownloader.try_utime('filename', 'unparseable_timestamp') == None
    assert FileDownloader.try_utime('filename', 'Jan 1 1970') == None
    assert FileDownloader.try_utime('filename', '1970-01-01') == None
    assert FileDownloader.try_utime('filename', '1970-01-01 00:00:00 GMT') == 0
    assert FileDownloader.try_utime('filename', '1970-01-01 00:00:00 +0000') == 0
    assert FileDownloader.try_utime('filename', '1970-01-01 00:00:00 +0300') == 10800

# Generated at 2022-06-14 15:11:47.703747
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    youtube_dl = YoutubeDL()
    f = FileDownloader(youtube_dl)

# Generated at 2022-06-14 15:12:00.561179
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    a = FileDownloader()
    assert a.format_seconds(1) == '00:01'
    assert a.format_seconds(10) == '00:10'
    assert a.format_seconds(60) == '01:00'
    assert a.format_seconds(180) == '03:00'
    assert a.format_seconds(18000) == '05:00:00'
    assert a.format_seconds(3600) == '01:00:00'
    assert a.format_seconds(0) == '00:00'
    assert a.format_seconds(3600.6) == '01:00:01'
    assert a.format_seconds(3601.6) == '01:00:02'
    assert a.format_seconds(3601) == '01:00:01'

# Generated at 2022-06-14 15:12:13.330655
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import urllib.request
    import urllib.error
    fd = FileDownloader({
        'limit_rate': '1k',
        'quiet': True,
        'verbose': False,
        'simulate': True,
    })
    geturl = 'http://127.0.0.1:%d/' % port
    try:
        urllib.request.urlopen(geturl, timeout=1)
        assert False
    except urllib.error.URLError as e:
        assert e.reason.errno == socket.timeout
    else:
        assert False
    with open(os.path.join(os.path.split(__file__)[0], 'files', 'test.mp4'), 'rb') as testfile:
        start_time, end_time = None, None


# Generated at 2022-06-14 15:12:22.159557
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    """
    Test that FileDownloader.download performs as expected.
    """
    download = FileDownloader({})
    # Test 1: Test a normal download
    download.report_destination = lambda x: print('[download] Destination: %s' % x)
    download.report_progress = lambda x: print('[download] %s' % x)
    download._report_progress_status = lambda x: print('[download] %s' % x)
    if download.download('TestFile.txt', {'url': 'www.test.com'}):
        print('[download] PASS: download succeeded')
    else:
        print('[download] FAIL: download failed')
    # Test 2: Test a download of a file that already exists

# Generated at 2022-06-14 15:12:25.045553
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader(params=None)
    assert 'hello.world' == fd.undo_temp_name('hello.world.temp')
    assert 'hello' == fd.undo_temp_name('hello.temp')
    assert 'hello.temp' == fd.undo_temp_name('hello.temp')
    assert 'hello' == fd.undo_temp_name('hello')

# Generated at 2022-06-14 15:12:34.854333
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    successes = 0
    failures = 0
    if FileDownloader.calc_speed(0, 0.1, 100) == 1000.0:
        successes += 1
    else:
        failures += 1
    if FileDownloader.calc_speed(0, 1, 1000) == 1000.0:
        successes += 1
    else:
        failures += 1
    if FileDownloader.calc_speed(0, 1, 10000) == 10000.0:
        successes += 1
    else:
        failures += 1
    if FileDownloader.calc_speed(0, 10, 100000) == 10000.0:
        successes += 1
    else:
        failures += 1
    if FileDownloader.calc_speed(0.5, 0.6, 1000) == 2000.0:
        successes += 1
    else:
        failures

# Generated at 2022-06-14 15:12:43.252418
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader({'nooverwrites': True})
    fd.report_file_already_downloaded('test_file')

    fd = FileDownloader({'nooverwrites': True})
    fd.report_file_already_downloaded('test_file')

    fd = FileDownloader({'nooverwrites': True})
    fd.report_file_already_downloaded('test_file_uft-8-name-\u2603')

# Generated at 2022-06-14 15:12:54.189427
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader()
    fd.report_progress({'status': 'finished'})
    fd.report_progress({'status': 'downloading', 'speed': '10', 'eta': 10, 'filename': 'a.txt', 'downloaded_bytes': 100, 'total_bytes': 1000})
    fd.report_progress({'status': 'downloading', 'speed': '10', 'eta': 10, 'filename': 'a.txt', 'downloaded_bytes': 100, 'total_bytes_estimate': 1000})
    fd.report_progress({'status': 'downloading', 'speed': '10', 'eta': 10, 'filename': 'a.txt', 'downloaded_bytes': 100, 'elapsed': 1})

# Generated at 2022-06-14 15:13:01.501055
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    assert FileDownloader.format_retries(float('inf')) == 'inf'
    assert FileDownloader.format_retries(0) == '0'
    assert FileDownloader.format_retries(5) == '5'
    assert FileDownloader.format_retries(5.5) == '5'
    assert FileDownloader.format_retries(5.6) == '6'



# Generated at 2022-06-14 15:13:12.009313
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    def assert_bs(exp, elap, bytes, ratelimit):
        bs = FileDownloader.best_block_size(elap, bytes, ratelimit)
        assert bs == exp, 'Expected best_block_size = %d != %d = inferred' % (exp, bs)

    assert_bs(4194304, 10.0, 41943040, None)  # 4 MB
    assert_bs(1048576, 10.0, 10485760, None)  # 1 MB
    assert_bs(524288, 10.0, 5242880, None)  # 512 KB
    assert_bs(262144, 10.0, 2621440, None)  # 256 KB
    assert_bs(131072, 10.0, 1310720, None)  # 128 KB

# Generated at 2022-06-14 15:13:27.254861
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    fd = FileDownloader(params={})
    pairs = (
        (1, '0:01'),
        (2, '0:02'),
        (59, '0:59'),
        (60, '1:00'),
        (61, '1:01'),
        (62, '1:02'),
        (3600, '1:00:00'),
        (3601, '1:00:01'),
        (3602, '1:00:02'),
    )
    for input, output in pairs:
        assert fd.format_seconds(input) == output

# Generated at 2022-06-14 15:13:38.705064
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import http.client
    import tempfile
    from test.test_dir_fd import test_dirfd_mock

    with tempfile.TemporaryDirectory() as temp_dir:
        with test_dirfd_mock.MockFdopen(temp_dir) as (dirfd, f):
            fd = os.open('exist_file.txt', os.O_WRONLY | os.O_CREAT, 0o600)
            os.close(fd)

            res = FileDownloader().try_utime('exist_file.txt', 'Wed, 09 Feb 1994 22:23:32 GMT')

            assert res is not None

# Generated at 2022-06-14 15:13:45.484149
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    assert FileDownloader.format_retries(float('inf')) == 'inf'
    assert FileDownloader.format_retries(1.0) == '1'
    assert FileDownloader.format_retries(0.9) == '1'
    assert FileDownloader.format_retries(0.0) == 'no more'
    assert FileDownloader.format_retries(float('nan')) == 'inf'
    assert FileDownloader.format_retries(1.2) == '1'



# Generated at 2022-06-14 15:13:52.583450
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    def _test(status, eta, speed, downloaded_bytes, total_bytes, elapsed,
              format_percent, format_eta, format_speed, format_bytes):
        s = {
            'status': status,
            'eta': eta,
            'speed': speed,
            'downloaded_bytes': downloaded_bytes,
            'total_bytes': total_bytes,
            'elapsed': elapsed
        }

        class Output(object):
            def __init__(self):
                self.msg = ''

            def write(self, msg):
                self.msg += msg

            def flush(self):
                pass

        output = Output()

        fd = FileDownloader({'progress_with_newline': True, 'noprogress': False})
        fd.to_screen = output.write

# Generated at 2022-06-14 15:13:57.638155
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader({})
    def _utime(fn, t):
        if fn != 'tmp':
            raise ValueError
        assert t == (4712, 815)
        raise IOError(errno.EPERM, 'Permission denied')

    filename, last_modified_hdr = 'tmp', 'Wed, 23 Feb 1983 12:46:40 GMT'
    orig_utime = os.utime
    os.utime = _utime
    try:
        fd.try_utime('tmp', 'Wed, 23 Feb 1983 12:46:40 GMT')
    finally:
        os.utime = orig_utime



# Generated at 2022-06-14 15:14:07.458237
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import sys
    import time
    import unittest
    from collections import namedtuple

    class TestFileDownloader(FileDownloader):
        def __init__(self, params):
            self.to_screen_value = ''
            self.to_stderr_value = ''
            self.to_console_title_value = ''
            FileDownloader.__init__(self, params)

        def to_screen(self, *args, **kargs):
            self.to_screen_value += u' '.join(map(decodeArgument, args))
            self.to_screen_value += u'\n'

        def to_stderr(self, *args, **kargs):
            self.to_stderr_value += u' '.join(map(decodeArgument, args))
            self.to

# Generated at 2022-06-14 15:14:20.333911
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    x = FileDownloader()

    # Try 'Unknown %' with no total bytes
    x.report_progress({
        'status': 'downloading',
        'speed': 7355,
        'eta': 7194,
        'downloaded_bytes': 524288,
    })

    # Try with total bytes, but no downloaded bytes
    x.report_progress({
        'status': 'downloading',
        'speed': 7355,
        'eta': 7194,
        'total_bytes': None,
        'downloaded_bytes': None,
    })

    # Try with total bytes, with downloaded bytes

# Generated at 2022-06-14 15:14:29.780964
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-14 15:14:40.868913
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def _test(rate_limit, expected_sleep_time, elapsed_time, downloaded_bytes):
        start_time = time.time() - elapsed_time
        fd = FileDownloader({
            'sleep_interval': 0.1,
            'ratelimit': rate_limit
        }, None)
        fd.slow_down(start_time, None, downloaded_bytes)
        return time.time() - start_time - elapsed_time

    # Test equal to rate limit
    assert_almost_equal(_test(100, None, 0.5, 50), 0)
    # Test higher than rate limit
    # Downloading 10 bytes more than the allowed to,
    # should sleep (100 - 10) / 100 = 0.1 seconds more
    # than the actual download time.

# Generated at 2022-06-14 15:14:53.574269
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({}, None)
    fd.format_percent = lambda x: '%.2f%%' % (x * 100)
    fd.format_eta = lambda x: 'eta'
    fd.format_speed = lambda x: '%.2f' % x

    fd.report_progress({'status': 'finished', 'total_bytes': 5188})
    fd.report_progress({'status': 'finished', 'total_bytes': 5188, 'total_bytes_estimate': 5188 * 2})

    fd.report_progress({'status': 'downloading', 'downloaded_bytes': 987654321, 'total_bytes': 5188})
    fd.report_progress({'status': 'downloading', 'downloaded_bytes': 1234, 'elapsed': 1})
    fd

# Generated at 2022-06-14 15:15:28.813917
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    class TestFD(BaseFD):
        def __init__(self, params):
            self.params = params
            self.to_screen_buffer = ''
            self.report_progress_buffer = []

        def to_screen(self, message, skip_eol=False):
            self.to_screen_buffer += message + ('\n' if not skip_eol else '')

        def _report_progress_status(self, msg, is_last_line=False):
            self.report_progress_buffer.append(msg)

        def report_progress(self, s):
            """Report download progress."""
            if s['status'] == 'finished':
                self.to_screen('[download] Download completed')

    downloader = TestFD({})
    downloader.report_file_already_downloaded('filename')
   

# Generated at 2022-06-14 15:15:30.857361
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # TODO
    #raise NotImplementedError
    pass


# Generated at 2022-06-14 15:15:36.317228
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader({})
    fd.report_file_already_downloaded(filename='file')
    fd.report_file_already_downloaded(filename=u'\u2665')
    fd.report_file_already_downloaded(filename=b'unicode_error')

# Generated at 2022-06-14 15:15:48.398138
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    class DummyFD(object):
        def __init__(self, filename):
            self.filename = filename


# Generated at 2022-06-14 15:15:56.523802
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    """
    Tests for method best_block_size of class FileDownloader
    """
    downloader = FileDownloader(None)
    print("test_FileDownloader_best_block_size")
    print("---")

    def print_test_result(elapsed_time, bytes, expected, actual):
        print("Test (elapsed_time=%s, bytes=%s, expected=%s):" % (elapsed_time, bytes, expected))
        print("-> result: %s" % actual)

    def perform_test(elapsed_time, bytes, expected):
        actual_result = downloader.best_block_size(elapsed_time, bytes)
        print_test_result(elapsed_time, bytes, expected, actual_result)

    perform_test(0.001, 0, 4194304)
   

# Generated at 2022-06-14 15:16:07.435323
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    """Unit test for method try_utime of class FileDownloader"""
    import tempfile
    from .utils import DateRange
    from .extractor.common import InfoExtractor

    # Create a temporary file
    tmp_fd, tmp_filename = tempfile.mkstemp()
    os.close(tmp_fd)
    os.remove(tmp_filename)

    # Create a FileDowloader object
    ie = InfoExtractor()
    ie.params = {}
    ie._downloader = FileDownloader({}, ie, None)
    ie._downloader.params = {'outtmpl': tmp_filename}

    # Create a file
    with open(tmp_filename, 'wb') as f:
        f.write("test_FileDownloader.test_try_utime")

    # Test a valid HTTP header

# Generated at 2022-06-14 15:16:15.106645
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # is the difference between start / end time of sleep smaller than 1 second?
    class DummyYDL(object):
        def to_screen(self, *args, **kargs):
            pass

    class DummyFD(FileDownloader):
        def real_download(self, filename, info_dict):
            return True

    fd = DummyFD(DummyYDL())
    fd.params['nooverwrites'] = True

    start_time = time.time()
    fd.slow_down(start_time, None, 5000001)
    end_time = time.time()
    diff = end_time - start_time
    assert diff < 1



# Generated at 2022-06-14 15:16:25.196813
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    if sys.version_info >= (3,3):
        fd = FileDownloader()
        assert fd.calc_speed(1.0, 1.0, 1) is None
        assert fd.calc_speed(1.0, 1.0, 0) is None
        assert fd.calc_speed(1.0, 2.0, 0) is None
        assert fd.calc_speed(1.0, 2.0, 1) == 0.5
        assert fd.calc_speed(1.0, 2.0, 2) == 1.0
        assert fd.calc_speed(1.0, 3.0, 3) == 1.0
        assert fd.calc_speed(1.0, 5.0, 2) == 0.4
        assert fd.calc

# Generated at 2022-06-14 15:16:35.843224
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    info_dict = {}

    file_downloader = FileDownloader(
        config_params={},
        params={},
        filename='foo.bar',
        info_dict=info_dict)  # Won't really work

    status = {'filename': 'foo.bar'}

    # Test no last_modified_hdr
    info_dict['last_modified_hdr'] = None
    file_downloader.try_utime(**status)

    info_dict['last_modified_hdr'] = 'Mon, 21 Jan 2013 17:04:00 GMT'
    file_downloader.try_utime(**status)

    # Test bogus
    info_dict['last_modified_hdr'] = 'Chicken soup for the soul.'
    file_downloader.try_utime(**status)

    # Test bogus
    info

# Generated at 2022-06-14 15:16:40.578673
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    """test_test_FileDownloader_try_utime"""
    dl = FileDownloader
    assert dl.try_utime('file', None) is None
    assert dl.try_utime('file', 'header') is None
    assert dl.try_utime('file', '0') == 0

# Generated at 2022-06-14 15:16:58.100350
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import time
    import random

    # This will run until the clock time changes to the next second
    random.seed()
    while True:
        ydl = FileDownloader({})
        prev_time = time.time()
        ydl.slow_down(prev_time, prev_time, random.randint(0, 1000))
        cur_time = time.time()
        tm = time.localtime(cur_time)
        if cur_time - prev_time > 1.0 or tm.tm_sec != time.localtime(prev_time).tm_sec:
            break


# Generated at 2022-06-14 15:17:07.042142
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    class FakeInfoDict(object):
        def __init__(self, fields={}):
            self.fields = fields

        def get(self, field, default=None):
            return self.fields.get(field, default)


# Generated at 2022-06-14 15:17:15.841256
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    filename = 'out.mp4'
    last_modified_hdr = 'Fri, 05 Jul 2013 13:49:24 GMT'
    
    assert last_modified_hdr == FileDownloader.try_utime(filename, last_modified_hdr)

    filename = 'out2.mp4'
    last_modified_hdr = 'Fri, 05 Jul 2013 13:49:24 -0003'

    assert last_modified_hdr == FileDownloader.try_utime(filename, last_modified_hdr)