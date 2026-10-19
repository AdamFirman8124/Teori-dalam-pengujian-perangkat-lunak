

# Generated at 2022-06-14 15:08:04.175406
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from .YoutubeDL import YoutubeDL
    fd = FileDownloader({}, YoutubeDL())
    fd.params.update({
        'ratelimit': 20,
        'nooverwrites': True,
    })
    fd.report_destination('output.mp4')

    # First, test that slow_down() correctly sleep when ratelimit is reached
    byte_counter = 0
    start_time = time.time()
    for i in range(20):
        fd.slow_down(start_time, time.time(), byte_counter)
        byte_counter += 1024
    sleep_time = time.time() - start_time
    assert sleep_time > 0 and sleep_time <= 1

    # Then, test that slow_down() does not sleep if ratelimit is not reached
    byte_counter = 0
    start_

# Generated at 2022-06-14 15:08:13.825338
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    fd = FileDownloader({
        'retries': 10
    })
    assert fd.format_retries(0) == '0'
    assert fd.format_retries(10) == '10'
    assert fd.format_retries(float('inf')) == 'inf'
    assert fd.format_retries(float('inf')) == fd.format_retries(fd.params['retries'])
    assert fd.format_retries(float('nan')) == 'inf'
    assert fd.format_retries(float('nan')) == fd.format_retries(fd.params['retries'])
    assert fd.format_retries(math.inf) == 'inf'
    assert fd.format_retries(math.inf) == fd.format_ret

# Generated at 2022-06-14 15:08:23.775845
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def test(start, now, bytes_counter, limit, expected_sleep):
        fd = FileDownloader(None)

        # Mock time.sleep
        saved_time_sleep = time.sleep

        sleep_calls = 0

        def mock_time_sleep(t):
            nonlocal sleep_calls
            sleep_calls += 1
            assert t == expected_sleep

        time.sleep = mock_time_sleep

        # Call slow_down
        fd.slow_down(start, now, bytes_counter)

        # Restore time.sleep
        time.sleep = saved_time_sleep

        # Check that expected number of calls to time.sleep have been made
        assert sleep_calls == (1 if expected_sleep > 0 else 0)

    test(1, 10, 10, 20, 0)

# Generated at 2022-06-14 15:08:33.212461
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import warnings

    class MockFD(FileDownloader):
        def __init__(self, params):
            super(MockFD, self).__init__(params)
            self._sleeps = []
        
        def sleep(self, s):
            self._sleeps.append(s)
        
        def get_sleep_times(self):
            return self._sleeps
    
    def get_default_params():
        params = {
            'noprogress': True,
            'cachedir': False,
            'nooverwrites': False,
        }

        return params

    with warnings.catch_warnings(record=True):
        warnings.simplefilter('ignore')
        
        fd = MockFD(get_default_params())
        
        # Slow down with ratelimit 100kB/s and we've

# Generated at 2022-06-14 15:08:39.451727
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def test(msg, *args, **kargs):
        fd = FileDownloader(None, None, None)
        fd.to_screen = lambda *args, **kargs: None
        fd.format_bytes = lambda a: '%.2f' % a
        fd.format_eta = lambda a: '%.2f' % a
        fd.format_percent = lambda a: '%.2f' % a
        fd.to_console_title = lambda *args, **kargs: None

# Generated at 2022-06-14 15:08:48.687637
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    downloader = FileDownloader(params={})
    # speed is below limit
    fake_time = [0, 0]

    def fake_time_time():
        fake_time[0] += 1
        return fake_time[0]

    time.time = fake_time_time
    downloader.slow_down(0, None, 20)
    assert fake_time[0] == 1
    # speed is above limit
    downloader.slow_down(0, None, 100)
    assert fake_time[0] == 4
    # speed is over limit, but cannot sleep
    downloader.slow_down(0, 0, 100)
    assert fake_time[0] == 5
    # speed is below limit, downloaded bytes is 0, but can sleep
    downloader.slow_down(0, 1, 0)
    assert fake

# Generated at 2022-06-14 15:08:59.244396
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile
    from youtube_dl.utils import DateRange

    # noop
    with tempfile.NamedTemporaryFile() as tf:
        d = FileDownloader({})
        d.try_utime(tf.name, '1978-12-23T00:00:00+00:00')

    # set
    with tempfile.NamedTemporaryFile() as tf:
        d = FileDownloader({})
        timestamp = d.try_utime(tf.name, '1978-12-23T00:00:00+00:00')
        assert timestamp == 244076800

    # noop
    with tempfile.NamedTemporaryFile() as tf:
        d = FileDownloader({'date_range': DateRange('19780101', '19790101')})

# Generated at 2022-06-14 15:09:10.456551
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # test for format_percent
    fd = FileDownloader(None, None)
    assert fd.format_percent(10) == ' 10%'
    assert fd.format_percent(100) == '100%'
    assert fd.format_percent(None) == 'Unknown %'
    assert fd.format_percent(10.1) == ' 10%'
    assert fd.format_percent(99.9) == '100%'
    assert fd.format_percent(0.5) == '  0%'

    # test for format_bytes
    assert fd.format_bytes(10) == '10 B'
    assert fd.format_bytes(1000) == '1000 B'
    assert fd.format_bytes(10000) == '10.0 kB'
    assert fd.format_

# Generated at 2022-06-14 15:09:18.265948
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({'max_downloads': '10'})
    fd.params['ratelimit'] = '5K'
    fd.params['nooverwrites'] = 'True'
    fd.params['noprogress'] = 'True'
    fd.params['continuedl'] = 'True'

    fd.report_progress({'status': 'finished'})


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 15:09:27.182027
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = FileDownloader(None, None)  # Dummy downloader

    # Test with 0 bytes downloaded
    assert(fd.best_block_size(1, 0) == 4194304)

    # Test with 1 byte downloaded
    assert(fd.best_block_size(1, 1) == 1)

    # Test with 10 bytes downloaded
    assert(fd.best_block_size(1, 10) == 3)

    # Test with 100 bytes downloaded
    assert(fd.best_block_size(1, 100) == 9)

    # Test with 1000 bytes downloaded
    assert(fd.best_block_size(1, 1000) == 28)

    # Test with 10000 bytes downloaded
    assert(fd.best_block_size(1, 10000) == 101)

    # Test with 1 byte downloaded and 10 seconds elapsed time

# Generated at 2022-06-14 15:09:48.072461
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(YoutubeDL('/tmp'))
    assert fd.temp_name('somefilename') == 'somefilename.part'
    assert fd.temp_name('somefilename.part') == 'somefilename.part'
    assert fd.temp_name('/path/to/somefilename') == '/path/to/somefilename.part'
    assert fd.temp_name('/path/to/somefilename.part') == '/path/to/somefilename.part'
    assert fd.temp_name('-') == '-'
    assert fd.temp_name('/dev/stdout') == '/dev/stdout'
    assert fd.temp_name('/path/to/somefilename_that_already_exists') == '/path/to/somefilename_that_already_exists'

# Generated at 2022-06-14 15:09:56.705088
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import io
    import tempfile
    from youtube_dl.utils import encodeFilename, decodeFilename

    out_dir = tempfile.mkdtemp()
    out_file = os.path.join(out_dir, 'outfile')

    # Same timestamp on both file and header
    f = io.open(encodeFilename(out_file), 'w')
    f.close()
    timestamp = os.path.getmtime(encodeFilename(out_file))
    fd = FileDownloader({'outtmpl': out_file + '_%(etag)s'})
    fd.try_utime(out_file, timestamp)
    assert abs(os.path.getmtime(encodeFilename(out_file)) - timestamp) < 1

    # Header timestamp is None

# Generated at 2022-06-14 15:10:08.038112
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    def test_bbs(expected, elapsed_time, bytes):
        downloader = FileDownloader(DummyYoutubeDL({}), {})
        result = downloader.best_block_size(elapsed_time, bytes)
        print('%3.3f %7d %7d %7d' % (elapsed_time, bytes, result, expected))
        return result == expected

    # Best block size should be >= 1 and <= 4 MB
    assert test_bbs(True, 1, 0)
    assert test_bbs(True, 1, 1)
    assert test_bbs(True, 1, 10)
    assert test_bbs(True, 1, 1023)
    assert test_bbs(True, 1, 1024)
    assert test_bbs(True, 1, 1025)
    assert test_bbs

# Generated at 2022-06-14 15:10:20.477331
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    ydl = YoutubeDL()
    ydl.debug = True
    ydl.add_progress_hook()
    fd = FileDownloader(ydl, {}, {})
    video_id = 'test_id'
    fd.download('filename.mp4', {'id': video_id, 'ext': 'mp4'})
    fd.download('filename.mp4', {'id': video_id, 'ext': 'mp4'})

    fd.report_destination('filename.mp4')
    d = {'id': video_id, 'ext': 'mp4'}
    fd.download('filename.mp4', d)
    fd.download('filename.mp4', d)

    fd.download('filename.mp4', d)

# Generated at 2022-06-14 15:10:32.886338
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class FakeInfoDict(object):

        def __init__(self):
            self.name = u'test'

    class FakeFileDownloader(object):

        def __init__(self):
            self.params = {'noprogress': True}
            self._hook_progress = lambda x: None
            self.to_screen = lambda x, **k: None
            self.format_eta = FileDownloader.format_eta
            self.to_console_title = lambda x: None

    def _fmt(s):
        return s.replace('%', '%%')

    fd = FakeFileDownloader()

# Generated at 2022-06-14 15:10:39.351850
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    def _stderr_write(msg): pass

    def _screen_write(msg): pass

    downloader = FileDownloader(params={}, ydl=DummyYDL({}))
    downloader._stderr_write = _stderr_write
    downloader.to_screen = _screen_write
    downloader.report_file_already_downloaded("You've got mail.mp3")
    downloader.report_file_already_downloaded("/tmp/You've got mail.mp3")

test_FileDownloader_report_file_already_downloaded()


# Generated at 2022-06-14 15:10:45.705944
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    x = lambda s: s

    # Test for status "finished"
    fd = FileDownloader(None, params={})
    fd.report_progress = x
    fd.report_progress({'status': 'finished'})
    fd.report_progress({'status': 'finished', 'total_bytes': 1234567890, 'elapsed': 42.42})

    # Test for status "downloading"
    fd.report_progress({'status': 'downloading', 'speed': 123.456789, 'eta': 42.42, 'downloaded_bytes': 1234567890})
    fd.report_progress({'status': 'downloading', 'speed': 123.456789, 'eta': 42.42, 'downloaded_bytes': 1234567890, 'total_bytes': 10**10})

# Generated at 2022-06-14 15:10:56.235934
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import tempfile
    tempdir = tempfile.mkdtemp()
    tempfile0 = os.path.join(tempdir, 'tempfile')
    tempfile1 = os.path.join(tempdir, 'tempfile.part')
    open(tempfile0, 'wb').close()
    open(tempfile1, 'wb').close()

    errfile = io.BytesIO()
    fd = FileDownloader({'outtmpl': tempfile0, 'continuedl': False}, errfile, stdout=errfile)

# Generated at 2022-06-14 15:10:56.840982
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    pass

# Generated at 2022-06-14 15:11:02.759868
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    # Typical case
    assert(FileDownloader.best_block_size(100.0, 40000) == 10000)
    # Small download
    assert(FileDownloader.best_block_size(5.0, 10) == 10)
    # Very slow download
    assert(FileDownloader.best_block_size(120.0, 2000) == 1)


# Generated at 2022-06-14 15:11:23.224863
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(None, None)
    assert fd.temp_name('blah/bloh.part') == 'blah/bloh.part'
    assert fd.temp_name('blah/bloh') == 'blah/bloh.part'
    assert fd.temp_name('bloh.part') == 'bloh.part'
    assert fd.temp_name('bloh') == 'bloh.part'
    assert fd.temp_name('.') == '.'
    assert fd.temp_name('blah/') == 'blah/'
    assert fd.temp_name('/blah/bloh') == '/blah/bloh.part'
    assert fd.temp_name('/blah/bloh.part') == '/blah/bloh.part'

# Generated at 2022-06-14 15:11:31.682950
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    _TEST_FILENAME = 'test_FileDownloader_try_utime'
    def _test_file_created_at(timestamp):
        f = open(_TEST_FILENAME, 'w')
        os.utime(_TEST_FILENAME, (timestamp, timestamp))
        f.close()

    _test_file_created_at(0)
    fd = FileDownloader(FakeYDL(), {'noprogress': True})
    assert fd.try_utime(_TEST_FILENAME, '1970-01-01T00:00:00+00:00') is None
    _test_file_created_at(0)

# Generated at 2022-06-14 15:11:44.026273
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(FakeInfoExtractor())
    fd.params.update({'ratelimit': '0.01'})
    assert fd._start_time == 0.0
    assert fd._bytes_downloaded == 0.0
    fd.slow_down(0, 0.0, 0); time.sleep(0.01)
    assert fd._start_time <= time.time()
    assert fd._bytes_downloaded <= 0.0

    fd._start_time = 0.0
    fd._bytes_downloaded = 0.0
    fd.slow_down(0, 0.0, 100); time.sleep(0.01)
    assert fd._start_time <= time.time()
    assert fd._bytes_downloaded <= 100

    fd._start_time = 0.

# Generated at 2022-06-14 15:11:49.969816
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    resdict = {'downloaded_bytes': 1234, 'status': 'finished', 'elapsed': 0.42}
    fd = FileDownloader(YoutubeDL())
    fd._report_progress_prev_line_length = None
    fd.report_progress(resdict)
    fd._report_progress_prev_line_length = 0
    fd.report_progress(resdict)
    resdict = {'downloaded_bytes': None, 'status': 'finished', 'elapsed': 0.42}
    fd.report_progress(resdict)


# Generated at 2022-06-14 15:12:01.830731
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.params['nopart'] = True
    fd = FileDownloader(ydl, {'url': 'http://host.com/file.ext'})
    assert(fd.temp_name('/path/to/file.ext') == '/path/to/file.ext')
    assert(fd.temp_name('/path/to/file.ext') == '/path/to/file.ext')

    ydl.params['nopart'] = False
    fd = FileDownloader(ydl, {'url': 'http://host.com/file.ext'})
    assert(fd.temp_name('/path/to/file.ext') == '/path/to/file.ext.part')

# Generated at 2022-06-14 15:12:10.187580
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    assert FileDownloader.format_retries(float('inf')) == 'inf'
    assert FileDownloader.format_retries(0) == '0'
    assert FileDownloader.format_retries(1) == '1'
    assert FileDownloader.format_retries(1.1) == '1'
    assert FileDownloader.format_retries(1.9) == '1'
    assert FileDownloader.format_retries(2) == '2'



# Generated at 2022-06-14 15:12:19.709435
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    ydl = FakeYDL()
    fd = FileDownloader(ydl, {'ratelimit': 10})
    start = time.time()
    fd.slow_down(start, start + 10, 100)
    assert time.time() - start < 9
    fd.slow_down(start, start + 10, 9)
    assert time.time() - start < 9
    fd.slow_down(start, start + 10, 10)
    assert time.time() - start < 9
    fd.slow_down(start, start + 10, 11)
    assert time.time() - start < 10
    fd.slow_down(start, start + 10, 110)
    assert time.time() - start < 9

# Generated at 2022-06-14 15:12:28.415778
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    # Arrange
    import sys
    from io import StringIO
    from unittest.mock import patch

    saved_stdout = sys.stdout

    new_stdout = StringIO()
    sys.stdout = new_stdout

    fd = FileDownloader({}, {})

    # Act
    fd.report_file_already_downloaded("file_name")

    # Assert
    sys.stdout = saved_stdout
    assert new_stdout.getvalue() == "[download] file_name has already been downloaded\n"


# Generated at 2022-06-14 15:12:37.610772
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    # This is a test code for the method report_progress of class FileDownloader.
    # It is executed when this module is being executed as a main program.

    # Create a test object of FileDownloader
    test_object = FileDownloader(params={})

    test_object.to_screen = lambda *args: sys.stdout.write(' '.join(args) + '\n')

    # Create a test hook function
    def hook_function(status):
        print()
        print(status)

    test_object.add_progress_hook(hook_function)

    # Call the method under test
    test_object.report_progress({'status': 'finished'})


# Generated at 2022-06-14 15:12:47.027952
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Not passing a last_modified_hdr
    fd = FileDownloader({})
    fd.to_screen = lambda *args, **kargs: None
    assert fd.try_utime('', None) is None

    # Passing a last_modified_hdr that timeconvert can't parse
    fd = FileDownloader({})
    fd.to_screen = lambda *args, **kargs: None
    assert fd.try_utime('', 'foobar') is None

# Downloading file from given url
import urllib.request

# Generated at 2022-06-14 15:13:12.240674
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():

    def bbs_test(elapsed_time, bytes, expected_best_block_size):
        fd = FileDownloader({}, {})
        best_block_size = fd.best_block_size(elapsed_time, bytes)
        if expected_best_block_size != best_block_size:
            raise AssertionError(
                'best_block_size(%s, %s) returned %s instead of %s' %
                (elapsed_time, bytes, best_block_size, expected_best_block_size))

    # best_block_size should never return a value lower than 1
    bbs_test(3.0, 0, 1)  # Lowest possible rate
    bbs_test(0.0, 0, 1)  # Zero rate

    # Test various rates
    bbs_test

# Generated at 2022-06-14 15:13:22.851074
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = None

# Generated at 2022-06-14 15:13:27.536691
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(None)
    assert fd._calc_rate(0, 0) is None
    assert fd._calc_rate(0, 1) is None
    assert fd._calc_rate(1, 1) == 1.0
    assert fd._calc_rate(10, 1) is None
    assert fd._calc_rate(200, 10) == 20.0

# Generated at 2022-06-14 15:13:38.945492
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    params = [('nopart', True), ('cachedir', False)]
    fd = FileDownloader(params)
    assert fd.temp_name('foo') == 'foo'
    assert fd.temp_name('foo.part') == 'foo.part'
    assert fd.temp_name('foo.part') == 'foo.part'
    assert_raises(Exception, fd.temp_name, u'\u2603')
    assert_raises(Exception, fd.temp_name, u'\u2603')
    assert_raises(Exception, fd.temp_name, u'\u2603.part')
    assert_raises(Exception, fd.temp_name, u'\u2603.part')

# Generated at 2022-06-14 15:13:48.755303
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    def get_utime(filename):
        return os.stat(filename).st_mtime

    filename = 'test_file'

    # Unnecessary utime() call
    with open(filename, 'wb') as f:
        f.write(bytes(1))
    utime = get_utime(filename)
    FileDownloader(None, None).try_utime(filename, None)
    assert(get_utime(filename) == utime)

    # Actual utime() call
    FileDownloader(None, None).try_utime(filename, format_time(utime + 1))
    assert(get_utime(filename) > utime)

    # Invalid time format
    FileDownloader(None, None).try_utime(filename, 'invalid_time')

# Generated at 2022-06-14 15:13:59.349391
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Test for cases we can not set mtime (fails on windows)
    fd = FileDownloader(params={'outtmpl': '%(id)s.mp4'},
                        ydl=YoutubeDL(params={}))
    for f in ('/test/test.mp4', '/test/test', '/test/test.mp4/test.mp4'):
        fd.try_utime(f, None)
        fd.try_utime(f, 'invalid')
    # Test for valid case
    f = 'test.mp4'
    open(f, 'w').close()
    fd.try_utime(f, '20/04/1998')
    st = os.stat(f)
    assert st.st_mtime == 888681600

# Generated at 2022-06-14 15:14:08.771258
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # To test this method we need a fake class FileDownloader
    class FakeFileDownloader:
        def __init__(self, rate_limit, params={}):
            self.rate_limit = rate_limit
            self.params = params
        def to_screen(self, *args, **kargs):
            pass

    assert not FakeFileDownloader(None).rate_limit
    assert not FakeFileDownloader(None, {'ratelimit': None}).rate_limit
    assert not FakeFileDownloader(None).params.get('ratelimit')
    assert not FakeFileDownloader(None, {'ratelimit': None}).params.get('ratelimit')
    # speed up download
    assert FakeFileDownloader(1024, {'ratelimit': None, 'retries': 6, 'sleep_interval': 3}).rate_limit
   

# Generated at 2022-06-14 15:14:14.119822
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    a = FileDownloader({})
    assert a.undo_temp_name('a.part') == 'a'
    assert a.undo_temp_name('a') == 'a'
    assert a.undo_temp_name('.part') == '.part'


# Generated at 2022-06-14 15:14:26.165784
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    fd = FileDownloader(None, {})

# Generated at 2022-06-14 15:14:38.494350
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert(FileDownloader.parse_bytes('42') == 42)
    assert(FileDownloader.parse_bytes('42b') == 42)
    assert(FileDownloader.parse_bytes('42K') == 42*1024)
    assert(FileDownloader.parse_bytes('42kB') == 42*1024)
    assert(FileDownloader.parse_bytes('42KB') == 42*1024)
    assert(FileDownloader.parse_bytes('42 MB') == 42*1024*1024)
    assert(FileDownloader.parse_bytes('42Gb') == 42*1024*1024*1024)
    assert(FileDownloader.parse_bytes('42 TB') == 42*1024*1024*1024*1024)
    assert(FileDownloader.parse_bytes('42PB') == 42*1024*1024*1024*1024*1024)

# Generated at 2022-06-14 15:14:57.164379
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    # [((bytes text, answer), ...)]
    testing_set = [
        [('0', 0)],
        [('12', 12)],
        [('1k', 1000)],
        [('2 K', 2000)],
        [('2Ki', 2048)],
        [('2.5 K', 2500)],
        [('3.5m', 3500000)],
        [('4M', 4000000)],
        [('5 MiB', 5242880)],
        [('6.7 GiB', 715827882)],
        [('8 GB', 8000000000)],
        [('9g', 9000000000)],
        [('10 Gi', 10737418240)],
#        [('11GiB', 12094627968)],  # Not supported yet
    ]

# Generated at 2022-06-14 15:15:06.682813
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = FileDownloader({})
    # empty list
    assert fd.best_block_size([], 100) == 4194304

    # no values over 1MB
    blocksizes = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]
    assert fd.best_block_size(blocksizes, 100) == 4194304
    # there are values over 1MB
    blocksizes = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000,
                  1000000, 5000000, 10000000, 50000000, 100000000, 500000000, 1000000000]
    assert fd.best_block_size(blocksizes, 100) == 4194304


# Generated at 2022-06-14 15:15:11.576515
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    fd = FileDownloader({"sleep_interval": 1})
    start_time = time.time()
    fd.slow_down(start_time, None, 1024)
    elapsed = time.time() - start_time
    assert elapsed >= 1
    os.remove(temp_file.name)

# Generated at 2022-06-14 15:15:18.167744
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl.downloader.f4m import F4mFD
    from youtube_dl.downloader.hls import HlsFD
    from youtube_dl.downloader.http import HttpFD
    from youtube_dl.downloader.fragment import FragmentFD
    from youtube_dl.downloader.dash import DASHFD
    from youtube_dl.downloader.rtmp import RTMPFD
    from youtube_dl.downloader.ism import IsmFD
    from youtube_dl.utils import format_bytes
    ies = []
    ie = InfoExtractor(ies, None)


# Generated at 2022-06-14 15:15:28.440459
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert FileDownloader.parse_bytes(None) is None
    assert FileDownloader.parse_bytes('') is None

    assert FileDownloader.parse_bytes('0') == 0
    assert FileDownloader.parse_bytes('1') == 1
    assert FileDownloader.parse_bytes('2') == 2
    assert FileDownloader.parse_bytes('3') == 3
    assert FileDownloader.parse_bytes('4') == 4
    assert FileDownloader.parse_bytes('5') == 5
    assert FileDownloader.parse_bytes('6') == 6
    assert FileDownloader.parse_bytes('7') == 7
    assert FileDownloader.parse_bytes('8') == 8
    assert FileDownloader.parse_bytes('9') == 9

    assert FileDownloader.parse_bytes('10') == 10
    assert FileDownload

# Generated at 2022-06-14 15:15:41.727697
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    """
    file_downloader.try_utime
    """

    # Init
    fd = FileDownloader({})

    # Format time
    now = time.time()

    # Get right and wrong time
    right_time = time.strftime(u'%Y%m%d%H%M.%S', time.localtime(now))
    wrong_time = time.strftime(u'%Y%m%d%H%M.%S', time.localtime(now - (60 * 60)))

    # Test wrong and right time
    assert fd.try_utime('/tmp/testfile', wrong_time) == None
    assert int(fd.try_utime('/tmp/testfile', right_time)) >= int(now)

    # Test return

# Generated at 2022-06-14 15:15:52.116621
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class TestClass(FileDownloader):
        def __init__(self):
            self.params = {'ratelimit': 10.}
            self.sleeped = 0.

        def sleep(self, t):
            self.sleeped = t

    s = {'status': 'downloading', 'elapsed': 0, 'speed': 0, 'downloaded_bytes': 0, 'total_bytes': 0}

    t = TestClass()

    # Should not sleep if elapsed time is less than 0.001 seconds
    t.slow_down(0, 0.0005, 1)
    assert t.sleeped == 0.

    # Should not sleep if elapsed time is less than 0.001 seconds
    t.slow_down(0, 0.0005, 0)
    assert t.sleeped == 0.

    # Should not sleep if download speed is less

# Generated at 2022-06-14 15:15:59.227679
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    d = FileDownloader({})
    assert(d.undo_temp_name('one') == 'one')
    assert(d.undo_temp_name('one.part') == 'one')
    assert(d.undo_temp_name('one-1.part') == 'one-1')
    assert(d.undo_temp_name('one.part-1') == 'one.part-1')
    assert(d.undo_temp_name('one-1.part-2') == 'one-1.part-2')


# Generated at 2022-06-14 15:16:10.948629
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({})

    for i in range(0, 1000):
        fd.report_progress({
            'downloaded_bytes': i * 1000,
            'total_bytes': None,
            'total_bytes_estimate': None,
            'elapsed': 8 * 60 * 60,
            'speed': i,
            'eta': None,
            'status': 'downloading'})
        time.sleep(0.01)

    print('\n')


# Generated at 2022-06-14 15:16:18.472375
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    from .YoutubeDL import YoutubeDL
    from .utils import DateRange

    data = open('test/data/%s.test' % sys._getframe().f_code.co_name, 'rb').read()
    old_open = compat_urllib_request.urlopen

    def _urlopen(request):
        return BytesIO(data)
    compat_urllib_request.urlopen = _urlopen

    class MockInfo:

        def __init__(self):
            self.headers = dict()

    ydl = YoutubeDL(dict(simulate=True))
    fd = FileDownloader(ydl,
                        dict(last_modified=True))