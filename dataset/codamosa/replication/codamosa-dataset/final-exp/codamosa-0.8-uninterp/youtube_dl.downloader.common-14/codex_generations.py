

# Generated at 2022-06-14 15:08:22.035328
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class FileDownloaderTest(FileDownloader):
        def __init__(self):
            FileDownloader.__init__(self, params={})

        def report_progress(self, s):
            pass

        def to_screen(self, *args, **kargs):
            pass

        def to_stderr(self, message):
            pass

    fd_test = FileDownloaderTest()
    fd_test.params['ratelimit'] = 100
    fd_test.slow_down(time.time(), time.time(), 1000)
    fd_test.params['ratelimit'] = None
    fd_test.slow_down(time.time(), time.time(), 1000)


# Generated at 2022-06-14 15:08:32.091630
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    return
    downloader = FileDownloader(FakeInfoExtractor())
    downloader.params['noprogress'] = False

    # Test format_percent
    ok_(isinstance(FileDownloader.format_percent(0), str))
    ok_(FileDownloader.format_percent(0) == '  0%')
    ok_(FileDownloader.format_percent(0.4) == '  0%')
    ok_(FileDownloader.format_percent(0.5) == '  1%')
    ok_(FileDownloader.format_percent(0.66666) == '  1%')
    ok_(FileDownloader.format_percent(0.99999) == '100%')

    # Test format_eta
    ok_(isinstance(FileDownloader.format_eta(0), str))

# Generated at 2022-06-14 15:08:38.531315
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    fd = FileDownloader(None, { 'report_speed': True, 'retries': 0 })

    # A series of tests that are supposed to work
    fd.calc_speed(100, 110, 1000)
    fd.calc_speed(100, 110, 2000)
    fd.calc_speed(100, 110, 1000)
    fd.calc_speed(100, 110, 2000)
    fd.calc_speed(100, 110, 1000)
    fd.calc_speed(100, 110, 2000)
    fd.calc_speed(100, 110, 1000)

    # A series of tests that should be ignored
    fd.calc_speed(100, 90, 1000)   # start time after end time
    fd.calc_speed(100, 110, 0)    

# Generated at 2022-06-14 15:08:48.115058
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    class T(object):
        pass
    fd = FileDownloader({}, {}, {}, None, None)
    assert fd.best_block_size(1.0, 100) == 44
    assert fd.best_block_size(1.0, 200) == 50
    assert fd.best_block_size(1.0, 400) == 83
    assert fd.best_block_size(1.0, 600) == 100
    assert fd.best_block_size(1.0, 800) == 113
    assert fd.best_block_size(1.0, 1600) == 200
    assert fd.best_block_size(1.0, 3200) == 350
    assert fd.best_block_size(1.0, 6400) == 640
    assert fd.best_block_

# Generated at 2022-06-14 15:08:53.866138
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    ytdl = YoutubeDL()
    fd = FileDownloader(ytdl)

    info = {
        'start_time': time.time() - 0.08,
        'elapsed': 0.08,
        'total_bytes': 10240,
        'downloaded_bytes': 1024,
    }

    assert fd.calc_eta(**info) == 7.2



# Generated at 2022-06-14 15:09:00.952861
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    assert FileDownloader.undo_temp_name('foo.part') == 'foo'
    assert FileDownloader.undo_temp_name('foo.part.part') == 'foo.part'
    assert FileDownloader.undo_temp_name('foo.part-123') == 'foo.part-123'
    assert FileDownloader.undo_temp_name('foo.part.mp3') == 'foo.part.mp3'
    assert FileDownloader.undo_temp_name('foo.part.mp3-123') == 'foo.part.mp3-123'


# Generated at 2022-06-14 15:09:11.525747
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Test -o parameter
    assert FileDownloader('-o file.out', {'filepath': 'file.in'}).download('file.in', {}) is True
    assert FileDownloader('-o %(filepath)s', {'filepath': 'file'}).download('file', {}) is True
    assert FileDownloader('-o %(filepath)s', {'filepath': 'file'}).download('-', {}) is False
    # Test -c parameter
    assert FileDownloader('-c -o file.out', {'filepath': 'file.in'}).download('file.in', {}) is True
    # Test --no-overwrites parameter

# Generated at 2022-06-14 15:09:22.938792
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    from .utils import get_new_ytdl

    ytdl = get_new_ytdl()
    with make_tempdir() as tmpdir:
        temp_file = os.path.join(tmpdir, 'temp_file')

        assert os.path.exists(tmpdir)
        assert not os.path.exists(temp_file)

        with open(temp_file, 'w') as f:
            pass

        assert os.path.exists(temp_file)

        fd = FileDownloader(ytdl, {'nooverwrites': True}, {'youtube_id': 'blah'})

        with open(path_candidates_file, mode='w') as f:
            f.write(temp_file + '\n')

        assert fd.report_file_already_down

# Generated at 2022-06-14 15:09:34.148726
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    # Test for FileDownloader.calc_eta(start, current, total)
    # start = 0, current = 0, total = 0
    assert FileDownloader.calc_eta(0, 0, 0) is None
    # start = 0, current = 10, total = 0
    assert FileDownloader.calc_eta(0, 10, 0) is None
    # start = 0, current = 10, total = 10
    assert FileDownloader.calc_eta(0, 10, 10) is None
    # start = 0, current = 10, total = 20
    assert FileDownloader.calc_eta(0, 10, 20) == 10
    # start = 0, current = 0, total = 20
    assert FileDownloader.calc_eta(0, 0, 20) is None
    # start = 0, current = 20

# Generated at 2022-06-14 15:09:46.207123
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    dl = FileDownloader({})
    test_filename = "test.mp4"
    part_filename = dl.temp_name(test_filename)
    assert part_filename.endswith(".part")

    dl = FileDownloader({'nopart': True})
    part_filename = dl.temp_name(test_filename)
    assert part_filename == test_filename

    dl = FileDownloader({'continue_dl': True})
    part_filename = dl.temp_name(test_filename)
    assert part_filename.endswith(".part")

    dl = FileDownloader({'continue_dl': True, 'nopart': True})
    part_filename = dl.temp_name(test_filename)
    assert part_filename == test_filename
    # end of Unit test

# Generated at 2022-06-14 15:10:20.530465
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    x = FileDownloader({})
    assert x.temp_name('abc') == 'abc.part'
    x = FileDownloader({'nopart': True})
    assert x.temp_name('abc') == 'abc'
    x = FileDownloader({'nopart': True})
    assert x.temp_name('-') == '-'
    x = FileDownloader({'nopart': False})
    assert x.temp_name('-') == '-.part'
    x = FileDownloader({'nopart': False})
    assert x.temp_name('/dev/null') == '/dev/null.part'
    x = FileDownloader({'nopart': True})
    assert x.temp_name('/dev/null') == '/dev/null'


# Generated at 2022-06-14 15:10:32.936784
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def calc(d):
        downloader = FileDownloader({})
        downloader.report_progress(d)

    calc({'downloaded_bytes': 1000000, 'total_bytes': 2000000})
    calc({'downloaded_bytes': 1000000, 'total_bytes': 2000000, 'speed': 80000})
    calc({'downloaded_bytes': 0, 'total_bytes': 2000000, 'speed': 80000})
    calc({'downloaded_bytes': 1000000, 'total_bytes_estimate': 2000000, 'speed': 80000})
    calc({'downloaded_bytes': 1000000})
    calc({'downloaded_bytes': 1000000, 'speed': 80000})
    calc({'downloaded_bytes': 1000000, 'total_bytes': 0})

# Generated at 2022-06-14 15:10:45.048622
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    chunk_size = 5  # bytes

# Generated at 2022-06-14 15:10:49.799677
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({'ratelimit': 10}, None)
    assert fd.slow_down(0, 0, 0) is None
    assert fd.slow_down(10, 20, 10) is None
    assert fd.slow_down(10, 20, 20) is None
    time.sleep(1)



# Generated at 2022-06-14 15:10:58.238323
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    import math
    fd = FileDownloader(None, {'continuedl': True})
    assert fd.best_block_size(0, 0) == 1
    assert fd.best_block_size(0, 1) == 1
    assert fd.best_block_size(0, 10) == 1
    assert fd.best_block_size(0, 1000) == 8
    assert fd.best_block_size(0, 10000) == 64
    assert fd.best_block_size(0, 1000000) == 512
    assert fd.best_block_size(0, 4194304) == 1024
    assert fd.best_block_size(0, 4194305) == 2048

    assert fd.best_block_size(1, 4194304) == 4194304

# Generated at 2022-06-14 15:11:05.779892
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # Initialize a downloader object
    test_downloader = FileDownloader({})

    # Test byte_counter=0 (nothing to do)
    assert test_downloader.params.get('ratelimit') is None
    ret = test_downloader.slow_down(0, 0, 0)
    assert ret is None
    # Test rate limit is None (nothing to do)
    ret = test_downloader.slow_down(0, 0, 1)
    assert ret is None

    # Test rate limit is set
    test_downloader.params.update({'ratelimit': 1})
    # Test byte_counter=0 (nothing to do)
    ret = test_downloader.slow_down(0, 0, 0)
    assert ret is None
    # Test elapsed time and byte_counter=0 (nothing to do)

# Generated at 2022-06-14 15:11:18.439870
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    """Unit tests for FileDownloader.report_progress."""

    def _get_expected_progress_message(status):
        """Return expected progress message string."""
        if status[u'status'] == u'finished':
            if status.get(u'total_bytes') is not None:
                status[u'_total_bytes_str'] = '%sB' % format_bytes(status[u'total_bytes'])
            else:
                status[u'_total_bytes_str'] = 'Unknown size'
            if status.get(u'elapsed') is not None:
                status[u'_elapsed_str'] = FileDownloader.format_seconds(status[u'elapsed'])
            else:
                status[u'_elapsed_str'] = 'Unknown time'

# Generated at 2022-06-14 15:11:19.545229
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    pass
 

# Generated at 2022-06-14 15:11:29.045940
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = FileDownloader(FakeYDL())
    # Test < 1 KiB
    assert fd.best_block_size(1, 1000) == 512
    assert fd.best_block_size(2, 1000) == 256
    assert fd.best_block_size(4, 1000) == 128
    # Test for 1 KiB to 32 KiB
    assert fd.best_block_size(1, 1024) == 512
    assert fd.best_block_size(1, 2000) == 512
    assert fd.best_block_size(1, 4000) == 1024
    assert fd.best_block_size(1, 8192) == 2048
    assert fd.best_block_size(1, 16384) == 4096
    assert fd.best_block_size(1, 32768) == 8192


# Generated at 2022-06-14 15:11:40.440772
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from .YoutubeDL import YoutubeDL

    # Download at 1.1MiB/s
    start_time = time.time()
    fd = FileDownloader({'limit_rate': '1.1MiB'})
    fd.to_screen = mock.Mock()
    fd.slow_down(start_time, start_time + 20, 20 * 1024 * 1024)
    time.sleep(0.1)  # real download would end here
    fd.to_screen.assert_not_called()
    # Download at 0.5MiB/s
    start_time = time.time()
    fd = FileDownloader({'limit_rate': '0.5MiB'})
    fd.to_screen = mock.Mock()

# Generated at 2022-06-14 15:12:04.453308
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from .utils import encodeFilename

    print('[debug] start testing FileDownloader.slow_down')

    class Singleton:
        ...
    class FakeYTDL:
        ...
    class FakeParams:
        ...
    class FakeFD:
        def __init__(self, params, ydl=None):
            self.params = params
            self.ydl = FakeYTDL()

        def temp_name(self, filename):
            return filename

        def try_utime(self, filename, last_modified_hdr):
            return None

        def report_progress(self, s):
            pass
        def report_progress(self, s):
            pass

        def report_warning(self, *args, **kargs):
            pass

        def report_error(self, *args, **kargs):
            pass

# Generated at 2022-06-14 15:12:12.795517
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    path = os.path.join(TEST_TEMP_DIR, 'test_FileDownloader_try_utime.txt')
    if os.path.exists(path):
        os.unlink(path)
    with open(path, 'w'):
        pass
    fd = FileDownloader({})
    fd.try_utime(path, '1332960299.53')
    assert 1332960299.53 < os.stat(path).st_mtime < time.time()

# Generated at 2022-06-14 15:12:18.356226
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    # init_FileDownloader
    d = FileDownloader(None, None)
    # simple cases
    assert d.undo_temp_name('foo.part') == 'foo'
    assert d.undo_temp_name('foo') == 'foo'
    # only strip one .part
    assert d.undo_temp_name('foo.part.mp4') == 'foo.part.mp4'



# Generated at 2022-06-14 15:12:30.115271
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = FileDownloader()

    assert fd.best_block_size(0, 1) == 4
    assert fd.best_block_size(1, 1) == 4
    assert fd.best_block_size(2, 1) == 2
    assert fd.best_block_size(2, 4) == 4
    assert fd.best_block_size(2, 8) == 4
    assert fd.best_block_size(4, 1) == 4
    assert fd.best_block_size(4, 8) == 4
    assert fd.best_block_size(8, 1) == 4
    assert fd.best_block_size(8, 8) == 4
    assert fd.best_block_size(8, 16) == 4
    assert fd.best_block_size

# Generated at 2022-06-14 15:12:41.433703
# Unit test for method report_file_already_downloaded of class FileDownloader

# Generated at 2022-06-14 15:12:47.652054
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    params = {
        'ratelimit': 3
    }
    fd = FileDownloader(params)

    time.sleep(1)
    now = time.time()
    start_time = now - 10

    for i in range (1,4):
        fd.slow_down(start_time, now, i * 100)
        time.sleep(1)

    time.sleep(1)
    now = time.time()
    start_time = now - 17
    fd.slow_down(start_time, now, 300)
    time.sleep(1)

    time.sleep(1)
    now = time.time()
    start_time = now - 3
    fd.slow_down(start_time, now, 1)
    time.sleep(1)



# Generated at 2022-06-14 15:12:54.350411
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class DummyYoutubeDL():

        def to_screen(self, msg):
            pass

        def trouble(self, msg):
            pass

        def report_warning(self, msg):
            pass

        def report_error(self, msg):
            pass

    ydl = DummyYoutubeDL()
    fd = FileDownloader(ydl, {})

    start = time.time()
    byte_counter = 0
    fd.slow_down(start, start, byte_counter)

    byte_counter = 100
    ratelimit_b = 100
    fd.params['ratelimit'] = ratelimit_b

    for i in range(10):
        now = time.time()
        fd.slow_down(start, now, byte_counter)
        byte_counter += ratelimit_b

# Generated at 2022-06-14 15:13:07.893325
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Testing downloader.
    from ytdl.utils import DateRange
    class FakeYdl(object):
        def __init__(self):
            self._screen_file = BytesIO()

        def to_screen(self, message, skip_eol=False):
            self._screen_file.write(message.encode('utf-8'))
            if not skip_eol:
                self._screen_file.write('\n'.encode('utf-8'))

        def to_console_title(self, message):
            pass

        def to_stderr(self, message):
            self.to_screen(message)

        def trouble(self, message, tb=None):
            self.to_stderr('ERROR: ' + message)


# Generated at 2022-06-14 15:13:17.563823
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(None, None)
    for filename in ['G:/1.avi', 'G:/2.test.wmf', 'G:/3.png', 'G:/4.txt', 'G:/5']:
        assert fd.temp_name(filename) == filename + '.part'
    fd.params['nopart'] = True
    for filename in ['G:/1.avi', 'G:/2.test.wmf', 'G:/3.png', 'G:/4.txt', 'G:/5']:
        assert fd.temp_name(filename) == filename

# Generated at 2022-06-14 15:13:26.800774
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class VersionInfo(object):
        def __init__(self, version):
            self.version = version

    fd = FileDownloader(VersionInfo('0.0'))

    def times(time_elapsed):
        return [0, 1, 9, 29, 99, 100, 199, 999, 1000, 1001, 1009, 1099,
                1099, 10100, 10999, 11000, 11001, 11009, 11099, 11099, 11100,
                11101]

    def speed_list(ratelimit, time_elapsed):
        return [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14,
                14, 15, 16]

    def sleep(t):
        time.sleep(t)

   

# Generated at 2022-06-14 15:13:45.748658
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    """Test if setting the last-modified time for a file works correctly."""
    if not os.path.isdir('/tmp'):
        raise UnitTestNotSupported(
            'The /tmp directory does not exist. Skipping this unit test')

    output_file = '/tmp/test_try_utime'
    if os.path.exists(output_file):
        os.remove(output_file)

    # Write a file
    with open(output_file, 'wb') as f:
        f.write(b'a' * 99)

    # Try to set the last-modified time to 0.
    f = FileDownloader({})
    f.try_utime(output_file, '0')
    # If the last-modified time equals 0, we can assume that the function
    # worked correctly.

# Generated at 2022-06-14 15:13:54.386063
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    dl = FileDownloader({'noprogress': True})
    dl.to_screen = lambda *args: print(args)  # noqa
    dl.report_progress({'status': 'finished'})
    dl.to_screen = lambda *args: None
    dl.report_progress({'status': 'finished'})

    dl.to_screen = lambda *args: print(args)  # noqa
    dl.report_progress({
        'status': 'downloading',
        'downloaded_bytes': 0,
        'speed': 0,
        'total_bytes': None,
        'eta': None,
    })

# Generated at 2022-06-14 15:13:59.637237
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class TestFileDownloader(FileDownloader):
        def __init__(self, ydl):
            FileDownloader.__init__(self, ydl)

    ydl = YoutubeDL()
    fd = TestFileDownloader(ydl)

    def get_format_progress_msg(param_dic):
        status = param_dic['status']
        assert status == 'downloading'
        d = {
            'downloaded_bytes': 1234,
            'total_bytes': 5678,
            'total_bytes_estimate': 0,
            'eta': 123,
            'speed': 6543,
        }
        d.update(param_dic)
        return fd.format_progress_string(d)


# Generated at 2022-06-14 15:14:05.638705
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    file_desc, filename = tempfile.mkstemp()
    os.close(file_desc)
    try:
        fd = FileDownloader({})
        timestr = 'Thu Oct  6 11:31:06 2016'
        filetime = timeconvert(timestr)
        fd.try_utime(filename, timestr)
        assert filetime == os.path.getmtime(filename)
    finally:
        os.remove(filename)

# Generated at 2022-06-14 15:14:12.852470
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    block_sizes = []
    for x in range(0, 5000000, 2):
        block_sizes.append(FileDownloader.best_block_size(
            x / 100.0, 1024))

    # min(1024, max(2*1024, min(5 MB, 1 MB / (x/100) )))
    def expected_block_sizes(x):
        return max(
            2048,
            min(
                1024 * 1024 * 5,
                1024 * 1024 / (x / 100.0)
            )
        )

    expected = [expected_block_sizes(x) for x in range(0, 100)]
    assert block_sizes[:100] == expected

    block_sizes = []

# Generated at 2022-06-14 15:14:25.259490
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    """$ ./get-flash-videos -d iana.org/playlists/pubcon-videos.xml"""

    def t(expected, elapsed_time, bytes, rate_limit):
        start_time = time.time() - elapsed_time
        now = time.time()
        fd = FileDownloader(FakeYDL())
        fd.params['ratelimit'] = rate_limit
        fd.slow_down(start_time, now, bytes)
        sleep_time = time.time() - now
        assert sleep_time == expected

    t(0.0, 0, 0, 1)
    t(0.0, 0, 1000, 1)
    t(0.0, 1.0, 1000, 1)
    t(0.0, 0.5, 1000, 1)

# Generated at 2022-06-14 15:14:28.165766
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    d = FileDownloader()
    d.report_file_already_downloaded('/file/already/exists')
    assert False


# Generated at 2022-06-14 15:14:40.116073
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    class FakeFD(FileDownloader):
        def __init__(self):
            params = {
                'noprogress': False,
                'start_time': 0.0,
            }
            FileDownloader.__init__(self, params)
            self.downloaded_bytes = 0
            self.total_bytes = 0
            self.lines_dumped = []
            self.to_screen_calls = []

        def to_screen(self, msg, skip_eol=False):
            self.lines_dumped.append(msg)
            self.to_screen_calls.append(skip_eol)

        def _write_string(self, msg):
            self.lines_dumped.append(msg)


# Generated at 2022-06-14 15:14:44.312106
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    dl = FileDownloader({}, MockYoutubeDL())
    dl.report_progress({'speed': 3, 'downloaded_bytes': 6, 'eta': 15})
    status_message = dl.ydl.msgs[0]
    assert '3.0 KiB/s' in status_message, status_message
    assert 'ETA' in status_message, status_message

# Generated at 2022-06-14 15:14:56.816600
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    class FakeYTDLSys(object):
        class FakeYTDLCompat(object):
            class FakeYTDLLoc(object):
                def decode(self, s):
                    return s
            def encode(self, s): return s
            def unicode_pprint(self, s):
                return s

        def compat_str(self, s): return s
        def compat_shlex_quote(self, s): return s
        def compat_urlparse(self, s): return s
        def compat_kwargs(self, s): return s
        def compat_interactive_shell(self, s):
            return False

        def compat_os_name(self):
            return 'posix'

        def compat_os_environ(self):
            return dict()


# Generated at 2022-06-14 15:15:49.059865
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    downloader = FileDownloader(None)

    # Test a few corner cases
    assert downloader.calc_speed(0, 0, 0) is None
    assert downloader.calc_speed(0, 0, 1) is None
    assert downloader.calc_speed(0, 1, 0) is None

    # Test regular case
    assert downloader.calc_speed(1, 2, 1) == 0.5

    # Test with bytes
    assert downloader.calc_speed(1, 2, 1024) == 512

    # Test with bytes and a 0 second interval
    assert downloader.calc_speed(1, 1, 1024) == 1024

    # Test with bytes and a fractional interval
    assert downloader.calc_speed(1, 1.5, 1024) == 683

    # Test with a negative start time

# Generated at 2022-06-14 15:15:58.801282
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    ydl = YoutubeDL({})

    fd = FileDownloader(ydl, None)
    assert fd.temp_name('%(id)s.f251.mp4') == '%(id)s.f251.mp4'
    assert fd.temp_name('abc.mp4') == 'abc.part'
    assert fd.temp_name('/home/s/b/abc.mp4') == '/home/s/b/abc.part'
    assert fd.temp_name('\\home\\s\\b\\abc.mp4') == '\\home\\s\\b\\abc.part'
    assert fd.temp_name('') == ''
    assert fd.temp_name('-') == '-'



# Generated at 2022-06-14 15:16:04.843758
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    # Test 1: speed should be None when total = None
    assert FileDownloader.calc_speed(0, 10, 1, None) == None
    # Test 2: speed should be None when duration is less than 0.001
    assert FileDownloader.calc_speed(0, 0, 1, 1) == None


# Generated at 2022-06-14 15:16:14.443121
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader(params={'verbose': True})
    default_filename = 'default.tmp'
    myfile = open(encodeFilename(default_filename), 'wb')
    myfile.write(b'Hello World')
    myfile.close()
    filename = 'test.tmp'
    myfile = open(encodeFilename(filename), 'wb')
    myfile.write(b'Hello World')
    myfile.close()
    assert(fd.try_utime(default_filename, None) is None)
    assert(fd.try_utime(filename, None) is None)
    time1 = time.strftime('%a, %d %b %Y %X GMT', time.gmtime())
    assert(fd.try_utime(filename, time1) is not None)

# Generated at 2022-06-14 15:16:24.986443
# Unit test for method temp_name of class FileDownloader

# Generated at 2022-06-14 15:16:35.627081
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class ReportProgressTest(object):
        def __init__(self, result):
            self.result = result
            self.i = 0
        def __call__(self, c):
            self.i += 1
            self.result.append(('test-%d' % self.i, c))

    # Testing completeness of the report
    result = []
    fd = FileDownloader(YoutubeDL(params = {
        'noprogress': False,
    }), params = {
        'noprogress': False,
    })
    fd.add_progress_hook(ReportProgressTest(result))

# Generated at 2022-06-14 15:16:46.158247
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class FakeInfoDict(object):
        def __init__(self, speed, eta, elapsed, downloaded_bytes, total_bytes_estimate):
            self.speed, self.eta, self.elapsed = speed, eta, elapsed
            self.downloaded_bytes, self.total_bytes_estimate = downloaded_bytes, total_bytes_estimate
    
    class FakeYDL(object):
        def __init__(self):
            self.to_screen = lambda s: None
            self.params = {}
            self.params['noprogress'] = False
            self.params['nopart'] = True
            self.params['progress_with_newline'] = True
            self.params['continuedl'] = True
        

# Generated at 2022-06-14 15:16:53.091378
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    assert FileDownloader.format_retries(float('inf')) == 'inf'
    assert FileDownloader.format_retries(3.14) == '3'
    assert FileDownloader.format_retries(1) == '1'
    assert FileDownloader.format_retries(0) == 'inf'
    assert FileDownloader.format_retries(-3) == 'inf'


# Generated at 2022-06-14 15:17:03.164572
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Test using known values
    filetime = time.mktime((2010, 1, 2, 3, 4, 5, 6, 7, -1))
    filename = u'test/äüö.txt'
    try:
        os.mkdir(u'test')
        with open(filename, 'wb') as f:
            pass
        fd = FileDownloader({'outtmpl': u'%(title)s'}, {'title': 'video'})
        fd.try_utime(filename, 'Sat, 02 Jan 2010 03:04:05 GMT')
        assert os.path.getmtime(filename) == filetime
    finally:
        if os.path.exists(filename):
            os.remove(filename)

# Generated at 2022-06-14 15:17:15.467167
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(params={'nopart': True})
    a = 'foo'
    b = fd.temp_name(a)
    assert(a == b)
