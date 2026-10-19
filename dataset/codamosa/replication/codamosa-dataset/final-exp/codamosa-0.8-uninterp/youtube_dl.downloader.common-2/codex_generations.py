

# Generated at 2022-06-14 15:08:15.339035
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    # Convertion of seconds value to time-like string
    # with default format ('HH:MM:SS')
    # 0 seconds     -> '00:00:00'
    # 1 second      -> '00:00:01'
    # 10 seconds    -> '00:00:10'
    # 60 seconds    -> '00:01:00'
    # 61 seconds    -> '00:01:01'
    # 3600 seconds  -> '01:00:00'
    # 3601 seconds  -> '01:00:01'
    # 86400 seconds -> '24:00:00'
    # 86401 seconds -> '24:00:01'
    assert '00:00:00' == FileDownloader.format_seconds(0)
    assert '00:00:01' == FileDownloader.format_seconds(1)
   

# Generated at 2022-06-14 15:08:25.728765
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    if not os.path.exists('temp'):
        os.mkdir('temp')
    fd = open(os.path.join('temp', 'testfile'), 'wb')
    fd.write(b'foo')
    fd.close()

# Generated at 2022-06-14 15:08:30.945611
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    assert FileDownloader({}, None).temp_name('foo') == 'foo.part'
    assert FileDownloader({'nopart': True}, None).temp_name('foo') == 'foo'
    assert FileDownloader({'nopart': True}, None).temp_name('foo.bar') == 'foo.bar'
    assert FileDownloader({'nopart': True}, None).temp_name('foo.bar.baz') == 'foo.bar.baz'
    assert FileDownloader({'nopart': True}, None).temp_name('-').startswith('-')
    assert FileDownloader({'nopart': True}, None).temp_name('-').endswith('-part')
    

# Generated at 2022-06-14 15:08:36.705602
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    ydl = YoutubeDL()
    ydl._ies = [MockIE()]
    fd = FileDownloader(ydl, {'noprogress': False, 'progress_with_newline': True})
    fd.report_progress({'status': 'finished', 'filename': 'abc'})
    assertEqual(
        ydl._screen_file.getvalue(),
        '[download] abc has already been downloaded\n')
    ydl._screen_file.truncate(0)

    fd.report_progress({'status': 'downloading',
                        'downloaded_bytes': 1024,
                        'total_bytes_estimate': 10 * 1024,
                        'eta': 5})

# Generated at 2022-06-14 15:08:46.730905
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import io
    import sys

    class FakeFD(io.StringIO):
        def __init__(self):
            self.output = ''
            io.StringIO.__init__(self)

        def write(self, s):
            self.output += s

    class FakeYDL(object):
        def __init__(self):
            self.to_screen_value = ''
            self.to_screen_called = False

        def to_screen(self, s, skip_eol=False):
            self.to_screen_called = True
            self.to_screen_value += s
            if not skip_eol:
                self.to_screen_value += os.linesep

    ydl = FakeYDL()
    fd = FakeFD()

    old_stderr = sys.stderr
    sys

# Generated at 2022-06-14 15:08:57.550618
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Create a YoutubeDL object for testing
    ydl_opts = {}
    ydl = YoutubeDL(ydl_opts)
    # Initialize FileDownloader object from the YoutubeDL object
    fd = FileDownloader(ydl, None)

    # Test report_progress() with downloading status
    # expected output:
    #       '[download] Unknown % at Unknown speed ETA Unknown ETA'
    dl_status0 = {'status': 'downloading', 'elapsed': None,
                  'total_bytes_estimate': None, 'downloaded_bytes': None,
                  'speed': None, 'eta': None}
    fd.report_progress(dl_status0)
    # Test report_progress() with finished status
    # expected output:
    #       '[download] Download completed'

# Generated at 2022-06-14 15:09:07.961672
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    # Test exception if filename cannot be decoded
    fd = FileDownloader(params={})
    filename = b'cannot decode me'
    fd.report_file_already_downloaded(filename)
    # Test log is printed
    filename = 'can decode me'
    # NOTE: The following test is skipped for now as it fails for Python 3.4
    # fd.to_screen.assert_called_with('[download] %s has already been downloaded' % filename)
    # Test no log is printed
    filename = '-'
    fd.to_screen.assert_not_called()
    fd.report_file_already_downloaded(filename)
    fd.tearDown()

# Generated at 2022-06-14 15:09:19.731875
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    assert(FileDownloader.calc_eta(0.01, 0.01, 0) is None)
    assert(FileDownloader.calc_eta(0.01, 0.01, 1) is None)
    assert(FileDownloader.calc_eta(0.01, 0.01, 2) == 0)
    assert(FileDownloader.calc_eta(0.01, 0.00, 1) is None)
    assert(FileDownloader.calc_eta(0.01, 0.00, 2) is None)
    assert(FileDownloader.calc_eta(0.00, 0.01, 1) == 0)
    assert(FileDownloader.calc_eta(0.00, 0.01, 2) == 0)

# Generated at 2022-06-14 15:09:27.400009
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    assert FileDownloader.format_seconds(0) == '0:00'
    assert FileDownloader.format_seconds(1) == '0:01'
    assert FileDownloader.format_seconds(60) == '1:00'
    assert FileDownloader.format_seconds(601) == '10:01'
    assert FileDownloader.format_seconds(3601) == '1:00:01'
    assert FileDownloader.format_seconds(7255) == '2:00:55'
    assert FileDownloader.format_seconds(12*7255) == '24:00:00'



# Generated at 2022-06-14 15:09:37.075175
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert FileDownloader.parse_bytes('') is None
    assert FileDownloader.parse_bytes('42') == 42
    assert FileDownloader.parse_bytes('42k') == 42 * 1024
    assert FileDownloader.parse_bytes('42M') == 42 * 1024 ** 2
    assert FileDownloader.parse_bytes('42G') == 42 * 1024 ** 3
    assert FileDownloader.parse_bytes('42T') == 42 * 1024 ** 4
    assert FileDownloader.parse_bytes('42p') == 42 * 1024 ** 5
    assert FileDownloader.parse_bytes('42e') == 42 * 1024 ** 6
    assert FileDownloader.parse_bytes('42z') == 42 * 1024 ** 7
    assert FileDownloader.parse_bytes('42y') == 42 * 1024 ** 8

# Generated at 2022-06-14 15:10:02.252299
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from tempfile import mkdtemp
    from shutil import rmtree
    from io import open

    # Generates a temporary directory and file
    temp_dir = mkdtemp()
    temp_file = os.path.join(temp_dir, 'test.tmp')
    with open(temp_file, 'wb') as fh:
        fh.write(b'my test data')

    # Test that download is not slowed down when rate_limit is None
    fd = FileDownloader({'nooverwrites': True, 'retries': 0, 'quiet': True, 'ratelimit': None, 'outtmpl': temp_file}, None)
    d = {'status': 'downloading', 'total_bytes': None, 'downloaded_bytes': 0}
    t1 = time.time()

# Generated at 2022-06-14 15:10:11.850851
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    def bbs(elapsed_time, bytes):
        return FileDownloader(params={}).best_block_size(elapsed_time, bytes)

    assert bbs(1.0, 0) == 1
    assert bbs(5.0, 0) == 1
    assert bbs(1.0, 1) == 1
    assert bbs(0.01, 1024) == 1
    assert bbs(0.01, 1 * 1024 * 1024) == 16 * 1024
    assert bbs(0.01, 10 * 1024 * 1024) == 16 * 1024
    assert bbs(0.01, 100 * 1024 * 1024) == 16 * 1024
    assert bbs(0.1, 1 * 1024 * 1024) == 4 * 1024
    assert bbs(0.1, 10 * 1024 * 1024) == 4 * 1024

# Generated at 2022-06-14 15:10:24.131152
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import os
    import tempfile

    # Create a dummy FileDownloader
    fd = FileDownloader(FakeYDL(), {})

    # Create a temp file
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, 'file')
    open(temp_file, 'w').close()
    assert os.path.isfile(temp_file)

    # File should not have last modification time if None is given
    assert fd.try_utime(temp_file, None) is None
    assert os.path.getmtime(temp_file) == 0

    # Format should be allowed to have fractional seconds
    assert fd.try_utime(temp_file, '1970-01-01T00:00:00.5Z') == 500000

# Generated at 2022-06-14 15:10:34.181600
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(None)
    eq = assertEquals

    eq(fd.temp_name('abc'), 'abc.part')
    eq(fd.temp_name('abc.mp4'), 'abc.mp4.part')
    eq(fd.temp_name('abc.mp4.part'), 'abc.mp4.part.part')

    fd.params['nopart'] = True

    eq(fd.temp_name('abc'), 'abc')
    eq(fd.temp_name('abc.mp4'), 'abc.mp4')
    eq(fd.temp_name('abc.mp4.part'), 'abc.mp4.part')



# Generated at 2022-06-14 15:10:46.434161
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    filename = os.tmpnam()

# Generated at 2022-06-14 15:10:53.100034
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader({})

    if not os.path.exists('test_%s' % sys.executable):
        open('test_%s' % sys.executable, 'wb').close()
    
    try:
        fd.try_utime('test_%s' % sys.executable, 'Sun, 17 Aug 2008 16:27:35 GMT')

        stat = os.stat('test_%s' % sys.executable)
        assert stat.st_mtime == datetime.datetime(2008, 8, 17, 16, 27, 35).timestamp()
    finally:
        os.remove('test_%s' % sys.executable)

# Unit test method _debug_cmd of class FileDownloader

# Generated at 2022-06-14 15:10:58.234493
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    set_quit()
    a = FileDownloader({})
    assert a.calc_speed(0, 1, 8) == 8
    assert a.calc_speed(1, 0, 8) == None
    assert a.calc_speed(1, 2, 1024) == 512
    assert a.calc_speed(0, 0, 8) == None



# Generated at 2022-06-14 15:11:04.497934
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Create a FileDownloader instance
    fd = FileDownloader({})
    # Test youtube_dl/opener.py's test_utils.test_get_testdata_stream
    info_dict = {
        '_filename': 'test.mp4',
        'id': 'test',
        'title': 'test',
        'ext': 'mp4',
        'url': 'http://www.youtube.com/v/test.mp4',
        'format': 'test',
        'player_url': 'http://www.youtube.com/v/test.flv',
        'http_headers': {},
        '_test': True,
    }
    # Try to download the file
    filename = 'test.mp4'
    fd.download(filename, info_dict)
    # Check if the file exists


# Generated at 2022-06-14 15:11:17.243524
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    """Test the report_progress method of class FileDownloader"""

    # Define some fake attributes and methods
    def to_screen(self, *args, **kargs):
        print('to_screen: %s' % args[0])

    def to_console_title(self, *args, **kargs):
        print('to_console_title: %s' % args[0])

    params = {
        'noprogress': False,
        'progress_with_newline': False,
    }

    # Create a FileDownloader object
    fdl = FileDownloader(params, {'params': params}, {'params': params})

    # Define some fake status dictionaries and fake times

# Generated at 2022-06-14 15:11:22.318031
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Test empty last_modified_hdr
    fd = FileDownloader(None, params={'outtmpl': u'%(id)s%(ext)s'})
    filename = fd.ytdl_filename(u'videoid')
    with open(encodeFilename(filename), 'wb') as fh:
        fh.write(b'video content\n')
    assert os.path.exists(encodeFilename(filename))
    fd.try_utime(filename, u'')

    # Test invalid last_modified_hdr
    fd = FileDownloader(None, params={'outtmpl': u'%(id)s%(ext)s'})
    filename = fd.ytdl_filename(u'videoid')

# Generated at 2022-06-14 15:11:49.790035
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    ydl = YoutubeDL()
    t = time.time() + 10
    fd = FileDownloader(ydl)
    # This must return in less than 2 seconds
    fd.slow_down(t, t, 100 * 1024 * 1024)
    # This must return in less than 110ms
    fd.slow_down(t, t + 10, 100 * 1024 * 1024)



# Generated at 2022-06-14 15:12:01.696102
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    dler = FileDownloader(FakeYDL())
    dler.params['verbose'] = True

    def test(seconds, expected):
        result = dler.format_seconds(seconds)
        assert result == expected, 'Expected %s, got %s for %ss' % (expected, result, seconds)

    test(0, '0:00')
    test(5, '0:05')
    test(60, '1:00')
    test(61, '1:01')
    test(3600, '1:00:00')
    test(3601, '1:00:01')
    test(3660, '1:01:00')
    test(3661, '1:01:01')
    test(36000, '10:00:00')

# Generated at 2022-06-14 15:12:14.713578
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # Prepare parameters
    params = {'noprogress': True, 'nooverwrites': False, 'continuedl': False, 'nopart': False}
    params['writedescription'] = False
    params['ratelimit'] = None
    params['nocheckcertificate'] = False
    params['retries'] = 10
    params['buffersize'] = None
    params['noresizebuffer'] = False
    params['continuedl'] = True
    params['playliststart'] = 1
    params['playlistend'] = 100
    params['playlist_items'] = None
    params['logger'] = ''
    params['consoletitle'] = False
    params['noprogress'] = False
    params['progress_with_newline'] = True
    params['dump_intermediate_pages'] = False

# Generated at 2022-06-14 15:12:24.668785
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    def t(seconds, expected):
        assert FileDownloader.format_seconds(seconds) == expected
    for i in range(0, 60):
        t(i, '00:00:%02d' % i)
    for i in range(60, 60*60):
        t(i, '00:%02d:%02d' % (i//60, i%60))
    for i in range(60*60, 24*60*60):
        t(i, '%02d:%02d:%02d' % (i//3600, (i//60)%60, i%60))

if __name__ == '__main__':
    test_FileDownloader_format_seconds()

# Generated at 2022-06-14 15:12:33.484798
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader(YoutubeDL(),params={u'noprogress': False,
                        u'format': u'best',
                        u'progress_with_newline': False,
                        u'nooverwrites': False,
                        u'verbose': True,
                        u'continuedl': True,
                        u'nopart': False})
    fd.report_progress({'eta': 859,
                        'downloaded_bytes': 0,
                        'total_bytes': None,
                        'elapsed': 2,
                        'speed': 0,
                        'status': 'downloading'})
test_FileDownloader_report_progress()


# Generated at 2022-06-14 15:12:46.158807
# Unit test for method report_progress of class FileDownloader

# Generated at 2022-06-14 15:12:50.488878
# Unit test for method try_rename of class FileDownloader
def test_FileDownloader_try_rename():
    assert('dummy.part' == FileDownloader.temp_name('dummy'))
    assert('dummy' == FileDownloader.undo_temp_name('dummy.part'))
    assert('dummy' == FileDownloader.undo_temp_name('dummy'))

# Generated at 2022-06-14 15:12:59.360895
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile
    test_file_name = tempfile.mkstemp()[1]
    f = open(test_file_name, 'wb')
    f.write(b'foo')
    f.close()
    info = {
        'id': '1',
        'url': 'http://localhost/1',
        'title': '',
        'ext': 'mp4',
        'format': '',
        'duration': 1,
    }
    fd = FileDownloader(None, {'outtmpl': test_file_name})
    assert fd.try_utime(test_file_name, 'Sun, 6 Jul 2014 22:54:01 GMT')
    os.unlink(test_file_name)
# Now the try_utime has ben tested we can use it in the real download methods
   

# Generated at 2022-06-14 15:13:11.030950
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(params={'ratelimit': '0'})
    assert fd.calc_speed(0, 0, 0) is None
    assert fd.calc_speed(0, 0.0001, 10) is None
    assert fd.calc_speed(0, 1, 10) == 10
    assert fd.calc_speed(0, 1, 1023) == 1023
    assert fd.calc_speed(0, 1, 1024) == 1024
    assert fd.calc_speed(0, 1, 1025) == 1024
    assert fd.calc_speed(0, 1, 10240) == 1024
    assert fd.calc_speed(0, 1, 10475) == 1048
    assert fd.calc_speed(0, 1, 10485) == 1048

# Generated at 2022-06-14 15:13:20.582234
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from youtube_dl.YoutubeDL import YoutubeDL
    fd = FileDownloader({'id': 'testid', 'progress_with_newline': True, 'noprogress': False})
    fd.to_screen = lambda x: sys.stderr.write(x + '\n')
    fd.to_console_title = lambda _: None
    fd.ydl = YoutubeDL({})
    fd.report_progress({
        'status': 'finished',
    })

    # TODO: we don't check what FileDownloader.to_screen actually gets since
    # there is no reliable way to capture that.


# Generated at 2022-06-14 15:13:45.883266
# Unit test for method format_seconds of class FileDownloader
def test_FileDownloader_format_seconds():
    assert FileDownloader.format_seconds(0) == '0:00'
    assert FileDownloader.format_seconds(1) == '0:01'
    assert FileDownloader.format_seconds(11) == '0:11'
    assert FileDownloader.format_seconds(59) == '0:59'
    assert FileDownloader.format_seconds(60) == '1:00'
    assert FileDownloader.format_seconds(61) == '1:01'
    assert FileDownloader.format_seconds(601) == '10:01'
    assert FileDownloader.format_seconds(3601) == '01:00:01'
    assert FileDownloader.format_seconds(3661) == '01:01:01'
    assert FileDownloader.format_seconds(90061) == '01:01:01'



# Generated at 2022-06-14 15:13:54.413147
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    fd = FileDownloader({})
    fd.params['ratelimit'] = 5
    fd.params['retries'] = 1
    fd.params['buffersize'] = 10
    fd.params['noresizebuffer'] = False
    fd.params['test'] = False
    fd.params['continuedl'] = True
    fd.params['noprogress'] = False
    fd.params['logger'] = None
    fd.params['progress_with_newline'] = False
    fd.params['min_filesize'] = 1
    fd.params['max_filesize'] = -1
    fd.params['test'] = False
    fd.params['daterange'] = None
    fd.params['nopart'] = True

# Generated at 2022-06-14 15:14:05.412857
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # mox initialization
    m = mox.Mox()
    m.StubOutWithMock(FileDownloader, 'real_download')
    m.StubOutWithMock(FileDownloader, 'report_file_already_downloaded')
    m.StubOutWithMock(FileDownloader, 'report_progress')
    m.StubOutWithMock(FileDownloader, 'report_destination')
    m.StubOutWithMock(FileDownloader, 'report_resuming_byte')
    m.StubOutWithMock(FileDownloader, 'report_retry')
    m.StubOutWithMock(FileDownloader, 'report_unable_to_resume')
    # variables initialization
    params = dict()
    # mox initialization end

    # Test 1: nooverwrit

# Generated at 2022-06-14 15:14:06.431246
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # FIXME
    pass

# Generated at 2022-06-14 15:14:13.629649
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    class MyInfoDict(dict):
        def __repr__(self):
            return 'MyInfoDict'

    class MyFD(FileDownloader):
        def real_download(self, filename, info_dict):
            raise NotImplementedError

    # Test fallback
    params = {
        'continuedl': True,
        'noprogress': True,
        'nooverwrites': False,
        'outtmpl': '%(title)s-%(id)s.%(ext)s',
    }
    fd = MyFD(params)
    assert fd.temp_name('abc') == 'abc.part'

    # Test temp filename

# Generated at 2022-06-14 15:14:25.856092
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    # Test that non-positive integers passed as parameters raise an exception
    for n in [-2, -1, 0]:
        try:
            FileDownloader.best_block_size(n, n)
        except ValueError:
            pass
        else:
            raise AssertionError('Expected ValueError for n = %d' % n)

    # Test that the value is not rounded to a power of 2
    for n in [3, 4, 5, 6, 8, 9, 15, 16, 17]:
        assert FileDownloader.best_block_size(n, n) == n

    # Test the rounding to a power of 2
    for n in [7, 10, 11, 12, 13, 14, 18]:
        result = FileDownloader.best_block_size(n, n)

# Generated at 2022-06-14 15:14:38.216799
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    """
    Unit test for method try_utime of class FileDownloader

    """
    # File name
    fn = "test-file.txt"

    # Prepare an example file
    with open(fn, 'w') as f:
        f.write('test')

    # Get time of creation
    t_creation = os.stat(fn).st_mtime

    # Init FileDownloader
    fd = FileDownloader(None, {})

    # Call try_utime with a broken time
    fd.try_utime(fn, "broken")
    t_broken = os.stat(fn).st_mtime
    assert t_creation == t_broken, "try_utime does not stay silent with broken time"

    # Call try_utime with a proper time

# Generated at 2022-06-14 15:14:39.202067
# Unit test for method try_rename of class FileDownloader
def test_FileDownloader_try_rename():
    pass

# Generated at 2022-06-14 15:14:46.656139
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():

    import tempfile
    import unittest
    import shutil
    import sys
    import os

    def _write_file(filename, data):
        if sys.version_info[0] >= 3:
            f = open(filename, 'wb')
            f.write(data.encode('utf-8'))
        else:
            f = open(filename, 'w')
            f.write(data)
        f.close()

    class FakeYoutubeDL(object):
        def __init__(self, params):
            self.params = params

        def to_screen(self, msg):
            pass

        def to_console_title(self, msg):
            pass

        def trouble(self, msg):
            raise ValueError(msg)


# Generated at 2022-06-14 15:14:58.389879
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import datetime
    d = FileDownloader({})
    try:
        d.report_progress({
            'status': 'finished',
        })
    except Exception:
        pass
    else:
        assert False, 'Expected exception'
    try:
        d.report_progress({
            'status': 'downloading',
        })
    except Exception:
        pass
    else:
        assert False, 'Expected exception'
    try:
        d.report_progress({
            'status': 'downloading',
            'eta': None,
        })
    except Exception:
        pass
    else:
        assert False, 'Expected exception'
    try:
        d.report_progress({
            'status': 'downloading',
            'downloaded_bytes': None,
        })
    except Exception:
        pass

# Generated at 2022-06-14 15:15:23.486314
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def testit(status, expected):
        fd = FileDownloader({})
        fd.to_screen = lambda *args, **kargs: expected.append(args[0])
        fd.report_progress(status)
        assert not expected or expected == [expected[-1]]
        return expected
    assert testit({'status': 'finished', 'elapsed': 2, 'total_bytes': 100, 'total_bytes_estimate': 100},
                  ['[download] 100% of 100 in 00:00'])
    assert testit({'status': 'downloading', 'elapsed': 2, 'total_bytes_estimate': 100,
                   'downloaded_bytes': 20, 'total_bytes': 100, 'speed': 10},
                  ['[download] 20% of ~100 at 10B/s ETA 00:08'])


# Generated at 2022-06-14 15:15:32.088807
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader(None, params={})
    fd.to_screen = lambda s: s

    # Test 1: check if the message is correct when the file has already been downloaded
    assert fd.report_file_already_downloaded('abc') == '[download] abc has already been downloaded'

    # Test 2: check if the message is correct when the file has already been downloaded
    # and this file is not a str
    assert fd.report_file_already_downloaded(u'abc') == '[download] abc has already been downloaded'

    # Test 3: check if the message is correct if the file is '-'
    assert fd.report_file_already_downloaded('-') == '[download] The file has already been downloaded'

    # Test 4: check if the message is correct if the file is another type

# Generated at 2022-06-14 15:15:44.639989
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    filename = encodeFilename("test_FileDownloader_try_utime.txt")
    open(filename, "w").close()
    assert not downloader.try_utime("test_FileDownloader_try_utime.txt", "")
    assert not downloader.try_utime("test_FileDownloader_try_utime.txt", None)
    assert downloader.try_utime("test_FileDownloader_try_utime.txt", "Sat, 29 Oct 1994 19:43:31 GMT")
    os.remove(filename)
    assert not downloader.try_utime("test_FileDownloader_try_utime.txt", 1)

if __name__ == '__main__':
    test_FileDownloader_try_utime()

# Generated at 2022-06-14 15:15:54.028026
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def test(speed, rate_limit, duration, expected_sleep_time,
             min_sleep_interval):
        assert '%f' % expected_sleep_time == '%f' % FileDownloader.slow_down(
            speed, rate_limit, duration, min_sleep_interval), (
                speed, rate_limit, duration, expected_sleep_time,
                min_sleep_interval)
    # Don't sleep
    test(10, 11, 0.0, None, None)  # Speed < rate_limit
    test(10, 10, 0.0, None, None)  # Speed = rate_limit
    test(10, 9, 0.0, None, None)  # Speed > rate_limit
    test(10, 11, 0.0, None, 0.0)  # min_sleep_interval ==

# Generated at 2022-06-14 15:16:03.217386
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    config.stdout = compat_stderr = io.StringIO()
    fd = FileDownloader(params={}, ydl=object())
    fd.report_file_already_downloaded('foo.bar')
    assert (compat_stderr.getvalue() == '[download] foo.bar has already been downloaded\n')
    compat_stderr = io.StringIO()
    config.stdout = io.StringIO()
    os.environ['UNICODE_OUTPUT'] = '0'
    fd.report_file_already_downloaded('foo.bar')
    assert (compat_stderr == io.StringIO())
    assert (config.stdout.getvalue() == '[download] foo.bar has already been downloaded\n')

# Generated at 2022-06-14 15:16:09.386186
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def _test(fd, s):
        if fd.params.get('noprogress', False): return
        if s['status'] != 'downloading': return
        if s.get('eta') is not None:
            s['_eta_str'] = fd.format_eta(s['eta'])
        else:
            s['_eta_str'] = 'Unknown ETA'
        if s.get('total_bytes') and s.get('downloaded_bytes') is not None:
            s['_percent_str'] = fd.format_percent(100 * s['downloaded_bytes'] / s['total_bytes'])

# Generated at 2022-06-14 15:16:17.578474
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Test different static samples, e.g. from http://stackoverflow.com/a/313
    assert FileDownloader.format_percent(0.123) == "12%"
    assert FileDownloader.format_percent(1.2345) == "123%"
    assert FileDownloader.format_percent(12.3456) == "1,234%"
    assert FileDownloader.format_percent(123.4567) == "12,346%"
    assert FileDownloader.format_percent(1234.5678) == "123,458%"
    assert FileDownloader.format_percent(12345.6789) == "1,234,567%"
    assert FileDownloader.format_percent(123456.789) == "12,345,679%"

# Generated at 2022-06-14 15:16:26.470529
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    params = {
        'outtmpl': u'%(title)s.%(ext)s',
        'format': u'best'
    }
    fd = FileDownloader(params)

    # test unicode
    filename = fd.temp_name(u'abc')
    assert filename == u'abc', 'Failed to create temp file name'

    # test str
    filename = fd.temp_name('abc')
    assert filename == 'abc', 'Failed to create temp file name'

    # test .part
    filename = fd.temp_name('abc.exe')
    assert filename == 'abc.exe.part', 'Failed to create temp file name'

    # test nopart
    params['nopart'] = True
    filename = fd.temp_name('abc.exe')

# Generated at 2022-06-14 15:16:32.907994
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader(None)
    test_filename = 'test_FileDownloader_try_utime.tmp'
    open(test_filename, 'wb').close()
    TEST_UTC_TIME = 1373999525
    utc_time = fd.try_utime(test_filename, 'Sunday, Jul 21, 2013 1:05:00 PM GMT')
    os.unlink(test_filename)
    assert utc_time == TEST_UTC_TIME

# Generated at 2022-06-14 15:16:44.860086
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from youtube_dl.YoutubeDL import YoutubeDL
    from .compat import compat_urllib_parse_unquote
    from .url import format_bytes
    import sys
    import time
    fd = FileDownloader(YoutubeDL(
        {'forcejson': True, 'quiet': True,
         'forcetitle': True, 'simulate': True,
         'console_print_func': lambda s: sys.stdout.write(s + os.linesep)}))
    fd.params['ratelimit'] = 2 * 1024 * 1024

    # Slow down test
    start = time.time()
    fd.slow_down(start, start + 2, 1024 * 1024 * 1024)
    time.sleep(0.1)

# Generated at 2022-06-14 15:17:07.535462
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import time
    time_struct = time.strptime('Tue, 27 Mar 2012 22:07:01 GMT', '%a, %d %b %Y %H:%M:%S %Z')
    test_FileDownloader_try_utime.fd = FileDownloader(params = {})
    #test_FileDownloader_try_utime.fd.to_screen = lambda *args, **kargs: None
    assert test_FileDownloader_try_utime.fd.try_utime('test_utime.file', int(time.mktime(time_struct))) == int(time.mktime(time_struct))
    assert os.path.getmtime('test_utime.file') == 1232868704

#test_FileDownloader_try_utime()

# Generated at 2022-06-14 15:17:19.511796
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # FileDownloader.temp_name(filename)
    fd = FileDownloader({})
    fd.params.update({
        'nopart': True,
        'continuedl': False,
    })
    # normal case. Downloading a file
    filename = 'The-Lighthouse-2019.avi'
    assert fd.temp_name(filename) == filename
    # Downloading a file but nopart flag is enabled
    filename = 'The-Lighthouse-2019.avi'
    assert fd.temp_name(filename) == filename
    assert fd.params['nopart'] is True
    # Downloading a file but the file already exists
    filename = 'The-Lighthouse-2019'
    assert fd.temp_name(filename) == filename