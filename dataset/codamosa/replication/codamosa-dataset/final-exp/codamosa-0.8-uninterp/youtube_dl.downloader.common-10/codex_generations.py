

# Generated at 2022-06-14 15:08:13.387114
# Unit test for method format_percent of class FileDownloader
def test_FileDownloader_format_percent():
    # Test input without a width parameter
    s = [
        [0.0, '0.00%'],
        [0.1, '0.10%'],
        [0.01, '0.01%'],
        [0.001, '0.00%'],
        [0.001e10, '0.00%'],
        [0.010e10, '0.10%'],
        [1.00e10, '100.00%'],
        [1.01e10, '101.00%'],
        [1.001e10, '100.10%'],
        [1.111e10, '111.10%']
    ]

    for input, output in s:
        assert FileDownloader.format_percent(input) == output

    # Test input with a width

# Generated at 2022-06-14 15:08:18.666795
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    dl = FileDownloader({})
    assert dl.temp_name('-') == '-'
    assert dl.temp_name('/foo/bar/baz') == '/foo/bar/baz.part'
    assert dl.temp_name('qux.mp4') == 'qux.mp4.part'
    assert dl.temp_name('/foo/bar/baz/qux.mp4') == '/foo/bar/baz/qux.mp4.part'



# Generated at 2022-06-14 15:08:21.562388
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({})
    start = time.time()
    fd.slow_down(start, start, 1024)
    # Speed will be 1024 / 1s < 1024 / 1.2s
    assert time.time() - start < 1.2
    # Speed will be 1024 / 1s > 1024 / 0.8s
    assert time.time() - start > 0.8



# Generated at 2022-06-14 15:08:31.857078
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    """Unit test for FileDownloader::download (method)."""
    
    # Test data
    url = 'http://host/file.txt'
    filename = 'file'

# Generated at 2022-06-14 15:08:38.336868
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def _fake_time():
        _fake_time.counter += 1
        return _fake_time.counter
    _fake_time.counter = 0

    fd = FileDownloader(FakeYoutubeDl())
    fd.params['ratelimit'] = 10000

    fd.slow_down(0, _fake_time(), 10)
    assert _fake_time.counter == 0

    fd.slow_down(0, _fake_time(), 100)
    assert _fake_time.counter == 0

    fd.slow_down(0, _fake_time(), 500)
    assert _fake_time.counter == .1
    _fake_time.counter = 0

    fd.slow_down(0, _fake_time(), 1000)
    assert _fake_time.counter == .4
    _fake_time.counter

# Generated at 2022-06-14 15:08:47.873634
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({})
    fd.report_progress({})
    fd.report_progress({'status': 'downloading', 'total_bytes': 100, 'downloaded_bytes': 70, 'eta': None, 'elapsed': 5, 'speed': 100})
    fd.report_progress({'status': 'downloading', 'total_bytes': None, 'downloaded_bytes': 70, 'eta': None, 'elapsed': 5, 'speed': 100})
    fd.report_progress({'status': 'downloading', 'total_bytes': 100, 'downloaded_bytes': None, 'eta': None, 'elapsed': 5, 'speed': 100})

# Generated at 2022-06-14 15:08:58.543360
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # stub of report_progress (is a method of FileDownloader class)
    fd = FileDownloader({}, YoutubeDL(params={}))

    # test report_progress with status 'finished'
    s = {'status': 'finished'}
    fd.report_progress(s)
    assert output.getvalue().strip('\r\n\t ') == '100%'

    # test report_progress with status 'downloading'
    delattr(fd, '_report_progress_prev_line_length')
    s = {'status': 'downloading'}
    s['speed'] = 3000
    s['total_bytes'] = 1000
    s['downloaded_bytes'] = 0
    s['eta'] = 10
    fd.report_progress(s)

# Generated at 2022-06-14 15:09:09.951226
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def test(ydl, **kwargs):
        # We don't want to see the output of
        # FileDownloader.report_progress() in the test
        def silence_report_progress(s):
            pass
        fd = FileDownloader({'noprogress': True}, ydl)
        fd.add_progress_hook(silence_report_progress)
        fd.report_progress(kwargs)
    ydl = FakeYDL(params={
        'logger': True,
        'noprogress': True,
        'progress_with_newline': True,
        'nooverwrites': True,
    })
    test(ydl, status='finished', total_bytes=10240)

# Generated at 2022-06-14 15:09:21.508685
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # case 1: download rate is lower than rate limit
    # return value: None
    filedownloader = FileDownloader(YoutubeDL(), params={'ratelimit': '120'})
    assert filedownloader.slow_down(0.0, time.time(), 1024) is None

    # case 2: download takes less than 1 millisecond
    # return value: None
    assert filedownloader.slow_down(0.0, 0.0, 1024) is None

    # case 3: download rate is greater than the rate limit
    # return value: None
    filedownloader = FileDownloader(YoutubeDL(), params={'ratelimit': '10'})
    assert filedownloader.slow_down(0.0, time.time(), 1024) is not None
    # FIXME: make the code actually sleep



# Generated at 2022-06-14 15:09:32.762843
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from io import BytesIO
    from collections import deque
    import pytest

    class DummyDownloader(FileDownloader):
        def real_download(self, filename, info_dict):
            return True

    # When has no ratelimit, should not slow down

    with DummyDownloader(params={}) as ydl:
        assert ydl.slow_down(0, 0, 10) is None

    # When has ratelimit, but high speed, should not slow down

    with DummyDownloader(params={'ratelimit': 100}) as ydl:
        assert ydl.slow_down(0, 0.1, 1000000) is None

    # When has ratelimit, but low speed, should slow down


# Generated at 2022-06-14 15:09:52.005659
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    dl = FileDownloader({})
    f = tempfile.NamedTemporaryFile()
    f.close()
    assert not os.path.exists(f.name)
    dl.try_utime(f.name, None)  # Should not fail if file doesn't exists
    dl.try_utime(f.name, 'asdasd')  # Should not fail if the time is invalid
    assert dl.try_utime(f.name, 'Thu, 01 Jan 1970 00:00:00 +0000') is None
    assert dl.try_utime(f.name, 'Thu, 01 Jan 1970 00:00:00') is None
    assert dl.try_utime(f.name, 'Thu Jan  1 00:00:00 1970') is None

# Generated at 2022-06-14 15:10:03.683050
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from io import BytesIO
    output = BytesIO()

    class DummyYDL:
        def to_screen(self, s):
            output.write(s.encode('utf8'))

    fd = FileDownloader(DummyYDL(), {'format': 'best', 'quiet': True})

    def slow_down(byte_counter, elapsed):
        fd.slow_down(time.time(), time.time() + elapsed, byte_counter)

    slow_down(0, 0)
    assert output.getvalue() == b''
    output.seek(0)
    output.truncate()

    # Test rate limit
    slow_down(10, 0.1)
    assert output.getvalue() == b''
    output.seek(0)
    output.truncate()

    # Test rate

# Generated at 2022-06-14 15:10:07.541803
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader(None, {'continuedl': False})
    assert fd.undo_temp_name('foo.part') == 'foo'
    assert fd.undo_temp_name('foo') == 'foo'

# Generated at 2022-06-14 15:10:19.976547
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():

    def test(params, expected_filename):
        filename = 'test filename.mp4'
        fd = FileDownloader({})
        fd.params = params
        temp_filename = fd.temp_name(filename)
        assert expected_filename == temp_filename
    # Regular filename
    test({}, 'test filename.mp4.part')
    # -nopart
    test({'nopart': True}, 'test filename.mp4')
    # -o FILE
    test({'outtmpl': 'test.%(ext)s'}, 'test.part')
    # -o 'FILE' (note the quotes)
    test({'outtmpl': 'test.%(ext)s'}, 'test.part')
    # -o FILE.extension

# Generated at 2022-06-14 15:10:25.241139
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile
    filename = tempfile.mkstemp()[1]
    fd = open(filename, 'wb')
    fd.write(b'\x00' * 10000)
    fd.close()

    filenames = [filename]

    dl = FileDownloader({})
    dl.to_screen = lambda *x: None

    # None last_modified_hdr should do nothing
    dl.try_utime(filename, None)
    assert os.path.getmtime(filename) == int(time.time())

    # Invalid last_modified_hdr
    dl.try_utime(filename, 'Sat, 31 Jul 2010')
    assert os.path.getmtime(filename) == int(time.time())

    # Valid last_modified_hdr

# Generated at 2022-06-14 15:10:36.415120
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    ydl = YoutubeDL({})
    expected = {
        'filename': 'test.mp4',
        'status': 'finished',
        'total_bytes': 3,
    }

    class NullFD(object):
        def __init__(self):
            self.isatty = lambda: False
            self.closed = False
        def close(self):
            self.closed = True

    class FD(NullFD):
        def __init__(self, filename, status, total_bytes):
            NullFD.__init__(self)
            self.filename = filename
            self.status = status
            self.total_bytes = total_bytes
            self.written = 0

        def write(self, buffer):
            self.written += len(buffer)

# Generated at 2022-06-14 15:10:49.021238
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # filename does not matter
    down = FileDownloader({'verbose': True}, None, None)
    # zero bytes
    down.slow_down(0, 0, 0)
    down.slow_down(0, 2, 0)
    down.slow_down(0, 100, 0)
    # 1000 bytes in 2 seconds at a rate of 500bytes/s
    down.slow_down(0, 2, 1000)
    down.slow_down(0, 3, 1000)
    # 1000 bytes in 1 second at a rate of 1000bytes/s
    down.slow_down(0, 1, 1000)
    down.slow_down(0, 2, 1000)
    # Sleep function tests are made elsewhere
    down.slow_down(0, 0.1, 1000)

# Generated at 2022-06-14 15:10:57.570551
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    """Test cases for method FileDownloader.report_progress()"""

    import mock
    fd = FileDownloader(None)
    fd.report_progress(
        {
            'status': 'downloading',
            'total_bytes': None,
            'elapsed': 0,
            'eta': None,
            'speed': '0',
            'downloaded_bytes': 0,
        })

    fd.report_progress(
        {
            'status': 'downloading',
            'total_bytes': None,
            'elapsed': 0,
            'eta': None,
            'speed': '0',
            'downloaded_bytes': None,
        })


# Generated at 2022-06-14 15:11:06.264923
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    def check_format_seconds(sec, expected):
        assert FileDownloader.format_seconds(sec) == expected
    check_format_seconds(0, '0:00')
    check_format_seconds(0.125, '0:00')
    check_format_seconds(9.93, '9.9')
    check_format_seconds(9.99, '9.9')
    check_format_seconds(9.995, '10.0')
    check_format_seconds(10, '10.0')
    check_format_seconds(9.5, '9.5')
    check_format_seconds(59.99, '59.9')
    check_format_seconds(59.995, '1:00')
    check_format_seconds(60, '1:00')

# Generated at 2022-06-14 15:11:14.819284
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(None, params={'ratelimit': '10'})
    start = time.time()
    fd.slow_down(start, start, 0)
    assert time.time() == start
    fd.slow_down(start, start, 1)
    assert time.time() - start > 0.1
    fd.slow_down(start, start, 11)
    assert time.time() - start > 0.2



# Generated at 2022-06-14 15:11:30.450939
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():

    from .extractor.youtube import YoutubeIE
    from .compat import compat_str

    try:
        from io import BytesIO as mute_stdout
    except ImportError:
        from compat import mute_stdout


# Generated at 2022-06-14 15:11:36.615021
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    assert FileDownloader.format_retries(float('inf')) == 'inf'
    assert FileDownloader.format_retries(1.2) == '1'
    assert FileDownloader.format_retries(3) == '3'
    assert FileDownloader.format_retries(0) == '0'
    assert FileDownloader.format_retries(False) == '0'



# Generated at 2022-06-14 15:11:47.739597
# Unit test for method slow_down of class FileDownloader

# Generated at 2022-06-14 15:12:00.561993
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def test(fd, s, expected):
        setattr(fd, 'to_screen', lambda *_: None)
        fd._report_progress_prev_line_length = 0
        fd.report_progress(s)
        assert fd._report_progress_prev_line_length == len(expected)
        assert fd.to_screen.call_count == 1
        args, kwargs = fd.to_screen.call_args
        assert kwargs == {'skip_eol': False}
        assert args[0] == expected
    fd = FileDownloader({})

# Generated at 2022-06-14 15:12:09.518927
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Create a dummy file
    fd, fn = tempfile.mkstemp()
    f = os.fdopen(fd, "wb")
    f.close()

    # We changed the file so the modification time should be different from
    # the original
    orig_st = os.stat(fn)
    orig_mtime = orig_st.st_mtime

    # Create a FileDownloader and try to restore the original modification time
    fd = FileDownloader(params=None)
    fd.try_utime(fn, orig_mtime)

    # Get the new modification time
    new_st = os.stat(fn)
    new_mtime = new_st.st_mtime

    # The modification time should be unchanged
    assert orig_mtime == new_mtime

    # Cleanup
    os.remove

# Generated at 2022-06-14 15:12:17.666594
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(params={'sleep_interval': 10})
    assert fd.slow_down(time.time(), None, 100) == None
    assert fd.slow_down(time.time()-10, time.time()-5, 10) == None
    assert fd.slow_down(time.time()-10, time.time()-5, 20) == None
    assert math.fabs(fd.slow_down(time.time()-10, time.time()-5, 15) - 5) < 0.1


# Test the method calc_eta

# Generated at 2022-06-14 15:12:29.870660
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class TestFileDownloader(FileDownloader):
        def __init__(self, params):
            FileDownloader.__init__(self, params)
            self.screen_data = []
        def to_screen(self, msg, skip_eol=False):
            self.screen_data.append(msg)
        def to_console_title(self, msg):
            pass

    dl = TestFileDownloader({})
    dl.report_progress({'status': 'downloading'})
    expected = ['[download]   0% of Unknown size at Unknown speed ETA Unknown ETA',
                '[download]   0% of Unknown size at Unknown speed']
    assert dl.screen_data == expected
    dl.screen_data = []


# Generated at 2022-06-14 15:12:37.622667
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import pytest
    from ytdl import FileDownloader
    from utils import FakeYDL
    from collections import OrderedDict
    fd = FileDownloader(FakeYDL(), {})
    # Test for various reports
    fd.report_progress(OrderedDict([('status', 'downloading'),
                                    ('_percent_str', '30%'),
                                    ('_eta_str', '1:01:01'),
                                    ('_speed_str', '5.5MiB/s'),
                                    ('_total_bytes_str', '200MiB')]))
    assert FakeYDL.messages == ['30% of 200MiB at 5.5MiB/s ETA 1:01:01']

    FakeYDL.messages = []

# Generated at 2022-06-14 15:12:49.879209
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    d = FileDownloader({})

    # Test normal download
    d.report_progress({'status': 'finished',
                       'total_bytes': 10,
                       'downloaded_bytes': 10,
                       'eta': 0,
                       'speed': 10.0,
                       'elapsed': 1.0})
    # Test unfinished download
    d.report_progress({'status': 'downloading',
                       'total_bytes': 10,
                       'downloaded_bytes': 4,
                       'eta': 5,
                       'speed': 3.3,
                       'elapsed': 1.0})
    # Test download with total_bytes_estimate

# Generated at 2022-06-14 15:12:58.933509
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    """Tests for method slow_down of class FileDownloader"""
    def _test_with_elapsed(elapsed, limit, expected):
        ret = FileDownloader.slow_down(elapsed, elapsed, limit)
        if ret != expected:
            print('Test failed on elapsed %f, limit %f, expected %f' % (elapsed, limit, expected))
            sys.exit(1)
        ret = FileDownloader.slow_down(0, elapsed, limit)
        if ret != expected:
            print('Test failed on elapsed %f, limit %f, expected %f' % (elapsed, limit, expected))
            sys.exit(1)
    print('Test with low rate limits')
    _test_with_elapsed(1, 2, 0.5)

# Generated at 2022-06-14 15:13:15.699245
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    test_cases = [
        ('a\u00a3', 'a?.part'),
        ('asdf/ asdf', 'asdf/ asdf.part'),
        ('a7sdf', 'a7sdf.part'),
        ('-7sdf', '-7sdf.part'),
        ('sdf', 'sdf.part'),
        ('sdf.ext', 'sdf.ext.part'),
        ('sdf-sdf_sdf-sdf.ext', 'sdf-sdf_sdf-sdf.ext.part'),
    ]
    for original, expected in test_cases:
        assert expected == FileDownloader({}).temp_name(original)
        assert original == FileDownloader({}).undo_temp_name(expected)
    return 'ok'


# Generated at 2022-06-14 15:13:25.271056
# Unit test for method try_rename of class FileDownloader
def test_FileDownloader_try_rename():
    import tempfile
    import shutil
    old_filename = tempfile.mkstemp(prefix='tmp', suffix='tmp')[1]
    with open(old_filename, 'w') as f:
        f.write('This is a test file for FileDownloader.try_rename')
    new_filename = tempfile.mkstemp(prefix='tmp', suffix='tmp')[1]
    fd = FileDownloader(None, None) # no need to really test all FileDownloader functions
    fd.try_rename(old_filename, new_filename)
    assert open(new_filename, 'r').read() == 'This is a test file for FileDownloader.try_rename'
    shutil.rmtree(os.path.dirname(old_filename), ignore_errors=True)
    shutil.rmt

# Generated at 2022-06-14 15:13:36.731480
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    class InfoDict(object):
        def __init__(self, info_dict):
            self.info_dict = info_dict
        def __getitem__(self, key):
            return self.info_dict[key]

    class FakeFileDownloader(FileDownloader):
        def __init__(self, params):
            FileDownloader.__init__(self, params)
            self.download_count = 0
            self.downloaded_file = False
            self.download_used_filename = False
        def real_download(self, filename, info_dict):
            self.download_count += 1
            if filename == 'a':
                self.downloaded_file = 'a'
            elif filename == 'b':
                self.downloaded_file = 'b'

# Generated at 2022-06-14 15:13:40.388483
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # This method is marked for deprecation
    t = FileDownloader({})
    assert t.download('nonexistant/file/foo.bar', {}) == False

# Test for method real_download of class FileDownloader

# Generated at 2022-06-14 15:13:49.550009
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    global progressHookCalled
    progressHookCalled = False

    def progressHook(status):
        global progressHookCalled
        progressHookCalled = True

    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.to_screen = lambda *args: None
    ydl.to_console_title = lambda *args: None
    fd = FileDownloader(ydl, dict())
    fd.add_progress_hook(progressHook)
    fd.report_progress({
        '_percent_str': '12.3%',
        '_eta_str': '-',
        '_speed_str': '-b/s',
        'filename': 'test.flv',
        'status': 'downloading',
    })

    assert progressHook

# Generated at 2022-06-14 15:14:00.151584
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    def test_one(timestr, expected):
        obj = FileDownloader({})

        filename = 'filename'

        touched_filename = obj.try_utime(
            filename,
            timestr
        )

        if touched_filename is None:
            assert expected is None
        else:
            (atime, mtime) = touched_filename

            assert mtime == expected

    test_one(
        timestr=None,
        expected=None
    )

    test_one(
        timestr='',
        expected=None
    )

    test_one(
        timestr='now',
        expected=time.time()
    )

    test_one(
        timestr='yesterday',
        expected=time.time() - 24 * 3600
    )


# Generated at 2022-06-14 15:14:02.794480
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader({}, {})
    assert fd.try_utime('/nonexistent', 'Thu, 01 Jan 1970 00:00:00 +0000') is None


# Generated at 2022-06-14 15:14:11.202134
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    class FakeYoutubeDL:
        params = {}
    fd = FileDownloader({}, FakeYoutubeDL())
    fd.report_destination = lambda x: x
    fd.report_progress = lambda x: x
    # Check that continuedl works
    fd.params['continuedl'] = True
    assert fd.download('test.mp4', {}) is True
    # Check that nooverwrites works
    fd.params['continuedl'] = False
    fd.params['nooverwrites'] = True
    assert fd.download('test.mp4', {}) is True
    assert fd.download('-', {}) is True
    fd.params['nooverwrites'] = False
    assert fd.download('-', {}) is False
    # Check that min/max_

# Generated at 2022-06-14 15:14:17.558846
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Unit test for method download of class FileDownloader
    import requests
    import warnings
    warnings.filterwarnings('ignore')
    # adding retries to requests
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=1, max_retries=10)
    session.mount('http://', adapter)
    session.mount('https://', adapter)


    url_list = ['https://www.youtube.com/watch?v=ubxSz6hjR6o', 'https://www.youtube.com/watch?v=7VmHc9yMxmI']

# Generated at 2022-06-14 15:14:18.269049
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    pass

# Generated at 2022-06-14 15:14:37.674154
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    d = FileDownloader({
        'noprogress': False,
        'ratelimit': None,
        'retries': 3
    })
    s = dict(
        status='downloading',
        downloaded_bytes=10,
        total_bytes=None,
        total_bytes_estimate=100,
        elapsed=5,
        eta=100,
        speed=2
    )

    def t(expected, **kwargs):
        s.update(**kwargs)
        if expected is not None:
            if expected[-1] == '\n':
                expected = expected[:-1]
        d.report_progress(s)
        if expected is not None:
            assert d._report_progress_prev_line_length == len(expected)

# Generated at 2022-06-14 15:14:41.325616
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    downloader = FileDownloader({'retries': 50}, None)
    assert downloader.format_retries(50) == '50'
    assert downloader.format_retries(float('inf')) == 'inf'


# Generated at 2022-06-14 15:14:54.120512
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Test method try_utime of class FileDownloader
    # with no argument
    fd = FileDownloader({})
    fd.try_utime(None, None)

    # with only file
    with tempfile.NamedTemporaryFile() as tf:
        fd.try_utime(tf.name, None)
        assert (os.path.getmtime(encodeFilename(tf.name)) >= time.time() - 1)

    # with only file and date
    with tempfile.NamedTemporaryFile() as tf:
        date = 'Fri, 07 Jul 2017 12:26:43 GMT'
        fd.try_utime(tf.name, date)

# Generated at 2022-06-14 15:15:03.426709
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    starting_time = time.time()
    f = FileDownloader({'ratelimit': '200'})
    f.slow_down(starting_time, None, 0)
    time.sleep(0.1)
    f.slow_down(starting_time, None, 0)
    time.sleep(0.1)
    f.slow_down(starting_time, None, 0)
    time.sleep(0.1)
    f.slow_down(starting_time, None, 0)
    time.sleep(0.1)
    f.slow_down(starting_time, None, 0)
    time.sleep(0.1)
    f.slow_down(starting_time, None, 0)
    time.sleep(0.1)
    elapsed_time = time.time() - starting_time

    assert 3

# Generated at 2022-06-14 15:15:12.369710
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader(None, params={})

    def t(status):
        if 'total_bytes' in status:
            del status['total_bytes']
        s = status
        if status['status'] == 'finished':
            assert s == {'_speed_str': '0.00 B/s', 'elapsed': 0, 'status': 'finished', 'filename': 'no-output', 'total_bytes': None, '_elapsed_str': '0:00:00', '_percent_str': 'Unknown %', '_total_bytes_str': '?'}
        elif status['status'] == 'downloading':
            assert s == {'downloaded_bytes': '0', 'speed': 0, 'eta': None, 'total_bytes': None, 'status': 'downloading', 'filename': 'no-output'}

# Generated at 2022-06-14 15:15:17.089217
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    assert FileDownloader.format_seconds(3) == '3.00s'
    assert FileDownloader.format_seconds(3.5) == '3.50s'
    assert FileDownloader.format_seconds(61) == '1m 1s'
    assert FileDownloader.format_seconds(61.5) == '1m 1s'
    assert FileDownloader.format_seconds(3662) == '1h 1m 2s'
    assert FileDownloader.format_seconds(36621) == '10h 10m 21s'



# Generated at 2022-06-14 15:15:27.474547
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    # Test 10 for normal use
    d = FileDownloader(params={})
    assert d.best_block_size(elapsed_time=5, bytes=1000) == 200
    assert d.best_block_size(elapsed_time=5, bytes=10000) == 2000
    assert d.best_block_size(elapsed_time=5, bytes=100000) == 4000
    assert d.best_block_size(elapsed_time=5, bytes=1000000) == 4194304
    assert d.best_block_size(elapsed_time=5, bytes=10000000) == 4194304
    # Test 20 for same rate, except estimation is higher
    assert d.best_block_size(elapsed_time=5, bytes=1000,
                             total_bytes=10000000) == 4194304

# Generated at 2022-06-14 15:15:34.639027
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    for s in [2, 8, 32, 128, 256, 1024, 2 * 1024, 2 * 1024 + 512]:
        d = FileDownloader({'ratelimit': 1024, 'noprogress': True})
        start = time.time()
        d.slow_down(start, None, s)
        end = time.time()
        assert end - start <= 1



# Generated at 2022-06-14 15:15:46.961373
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(None, params={'nooverwrites': True, 'ratelimit': 4, 'noprogress': True})
    # Test rate limit exceeded
    assert fd.calc_speed(0, 1, 8) == 8
    fd.slow_down(0, 1, 8)
    assert fd.calc_speed(0, 2, 16) == 8
    fd.slow_down(0, 2, 16)
    assert fd.calc_speed(0, 3, 24) == 8
    fd.slow_down(0, 3, 24)
    assert fd.calc_speed(0, 4, 32) == 8
    # Test rate limit not exceeded
    fd.slow_down(0, 4, 32)

# Generated at 2022-06-14 15:15:50.436853
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    downloader = FileDownloader(DummyYoutubeDl())
    downloader.report_file_already_downloaded('file.mp4')


# Generated at 2022-06-14 15:16:22.083818
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    fd = FileDownloader(FakeYDL(), {'logger': DummyLogger()})
    # test 1
    fd._start = 100
    assert fd._calc_speed(110) == 10

    # test 2
    fd._calc_speed = None
    assert fd._calc_speed(110) is None

    # test 3 with negative numbers
    fd._start = 20
    assert fd._calc_speed(10) == -10


# Generated at 2022-06-14 15:16:32.908824
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    test_cases = [
        ('02/13/13 8:29', 1360788140),
        ('Fri, 02 Aug 2013 06:06:43 +0000', 1375462403),
        ('Thu, 18 Jul 2013 07:04:02 GMT', 1374129842),
        ('Tue, 11 Feb 2014 23:49:22 -0000', 1392235762),
        # Probably not supported
        # ('11 Feb 2014 23:49:22 -0000', 1392235762),
        # ('2014-02-11T23:49:22-0000', 1392235762),
        # ('2014-02-11T23:49:22+0000', 1392235762),
    ]

    for date_str, date_secs in test_cases:
        fd = FileDownloader({})

# Generated at 2022-06-14 15:16:41.485693
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    from os import remove
    from tempfile import mkstemp
    from youtube_dl.utils import encodeFilename

    fd, name = mkstemp()
    close(fd)

    info = {
        'id': 'test',
        'title': 'test',
        'url': 'http://127.0.0.1:55555/',
        'playlist_index': 1,
        '_filename': name,
        'ext': 'mp4',
        'extractor': 'test',
        'extractor_key': 'test',
        'webpage_url': 'test',
        'webpage_url_basename': 'test',
    }

    # empty file
    ydl = MyYoutubeDL()
    dl = FileDownloader(ydl, info)
    dl.report_destination(name)

# Generated at 2022-06-14 15:16:50.035339
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile

# Generated at 2022-06-14 15:16:57.155982
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime(): 
    import datetime
    assert FileDownloader.try_utime('test', datetime.datetime.now().strftime('%c'))
    assert FileDownloader.try_utime('test', 'Today') is None
    assert FileDownloader.try_utime('test', None) is None
    assert FileDownloader.try_utime('test', 'Mon, 17 Feb 2014 00:27:43 GMT') == 1392600130
# Test for method parse_bytes of class FileDownloader

# Generated at 2022-06-14 15:16:59.772776
# Unit test for method try_rename of class FileDownloader
def test_FileDownloader_try_rename():
    fd = FileDownloader()
    # test that it returns without error in case of valid input
    fd.try_rename("old_filename", "new_filename")


# Generated at 2022-06-14 15:17:08.297811
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import pytest


    class TestFileDownloader(FileDownloader):
        def __init__(self, params):
            super(TestFileDownloader, self).__init__(params)
            self.last_time = None

        def slow_down(self, start_time, now, byte_counter):
            resp = super(TestFileDownloader, self).slow_down(start_time, now, byte_counter)
            self.last_time = now
            return resp

    fd = TestFileDownloader(params={'test_option': True})

    assert fd.last_time is None
    fd.slow_down(0, 0, 0)
    assert fd.last_time == 0
    fd.last_time = None

    # test with byte counter zero

# Generated at 2022-06-14 15:17:09.053031
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    pass





# Generated at 2022-06-14 15:17:13.064154
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    assert FileDownloader.format_retries(0) == u'0'
    assert FileDownloader.format_retries(1) == u'1'
    assert FileDownloader.format_retries(None) == u'inf'
    assert FileDownloader.format_retries(float('inf')) == u'inf'
    assert FileDownloader.format_retries(6) == u'6'
    assert FileDownloader.format_retries(1000) == u'1000'
    assert FileDownloader.format_retries(float('inf')) == u'inf'

