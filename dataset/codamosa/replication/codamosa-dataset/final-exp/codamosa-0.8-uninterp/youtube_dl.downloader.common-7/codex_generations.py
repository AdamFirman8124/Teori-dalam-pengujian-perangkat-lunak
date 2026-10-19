

# Generated at 2022-06-14 15:07:57.584300
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    assert FileDownloader.undo_temp_name('/a/b/c.part') == '/a/b/c'
    assert FileDownloader.undo_temp_name('abc.part') == 'abc'
    assert FileDownloader.undo_temp_name('.part') == ''
    assert FileDownloader.undo_temp_name('abc.PART') == 'abc'
    assert FileDownloader.undo_temp_name('abc.part.part') == 'abc.part'
    assert FileDownloader.undo_temp_name('part') == 'part'



# Generated at 2022-06-14 15:08:05.699408
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    """Unit test for method best_block_size of class FileDownloader"""

    # Test with a rate limit of 8KB/s
    now = time.time()
    last = now - 0.1
    fd = FileDownloader({'ratelimit': 8192})
    new_min = max(2048 / 2.0, 1.0)
    new_max = min(max(2048 * 2.0, 1.0), 4194304)  # max 4MB
    # Expected behavior:
    #   * dif < 0.001 -> return new_max
    #   * rate > new_max -> return new_max
    #   * rate < new_min -> return new_min
    #   * otherwise return rate

    dif = now - last
    res = fd.best_block_size(dif, 0)

# Generated at 2022-06-14 15:08:15.017807
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():

    d = FileDownloader(Params())

    def t(s):
        return timeconvert(s)

    # Neither old nor new time specified
    os.utime('nonexistent', None)  # Don't throw an exception
    # New time not specified
    d.try_utime('nonexistent', None)
    assert os.path.getmtime('nonexistent') == 0.0

    # Old time not specified
    d.try_utime('nonexistent', 'Mon, 03 Jun 2013 09:39:22 GMT')
    assert os.path.getmtime('nonexistent') == t('Mon, 03 Jun 2013 09:39:22 GMT')

    # Old time is specified

# Generated at 2022-06-14 15:08:19.947810
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    from youtube_dl.FileDownloader import FileDownloader
    fd = FileDownloader({})
    assert fd.undo_temp_name('0.part') == '0'
    assert fd.undo_temp_name('0.mp4.part') == '0.mp4'
    assert fd.undo_temp_name('0.mp4') == '0.mp4'


# Generated at 2022-06-14 15:08:30.874701
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # Test normal operation
    fd = FileDownloader({'ratelimit': 100*1024})
    start = time.time()
    speed = fd.calc_speed(start, start+0.1, 10*1024)
    assert speed == 1024*10
    time.sleep(0.09)
    fd.slow_down(start, None, 10*1024)
    speed = fd.calc_speed(start, time.time(), 10*1024)
    assert speed == 100*1024
    # Test when there is no rate limit
    fd = FileDownloader({})
    start = time.time()
    speed = fd.calc_speed(start, start+0.1, 10*1024)
    assert speed == 1024*10
    time.sleep(0.09)

# Generated at 2022-06-14 15:08:35.891105
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({'ratelimit': 500000})
    now = time.time()
    start = now - 0.1 # fd.calc_eta() returns None when (now - start) < 0.001
    slow_down(fd, start, now, 400000)
    assert fd.last_download_speed == 400000

    now = time.time()
    slow_down(fd, start, now, 400000)
    assert fd.last_download_speed == 400000

    now = time.time()
    slow_down(fd, start, now, 600000)
    assert fd.last_download_speed == 600000


# Generated at 2022-06-14 15:08:46.111392
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    class FakeDate(object):
        def __call__(self, *args, **kargs):
            return 1000

    def run_try_utime(filetime, date):
        filename = 'some_filename'
        fd = FileDownloader(None)
        fd.to_screen = lambda *args: None
        fake_stat = lambda filename: {'mtime': 1000}
        fd.stat = fake_stat

        with mock.patch('time.time', date):
            fd.try_utime(filename, filetime)

    # filetime and last-modified header match
    run_try_utime(date='Tue, 15 Nov 1994 12:45:26 GMT',
                  filetime=FakeDate())

    # filetime and last-modified header doesn't match

# Generated at 2022-06-14 15:08:53.008040
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Create a directory
    os.mkdir('test_folder')

    # Create a FileDownloader
    file_downloader = youtube_dl.FileDownloader(params={})
    file_downloader.params['outtmpl'] = 'test_folder/%(id)s.%(ext)s'
    file_downloader.add_progress_hook(lambda x: None) # Mock the progress hook

    # Create a fake info_dict

# Generated at 2022-06-14 15:09:02.421599
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    """ FileDownloader.try_utime unit test
    """
    import tempfile
    import shutil
    import stat
    from os.path import isdir, isfile
    from .utils import encodeFilename, compat_makedirs, compat_tempfile_gettempdir

    # Temporary directory to create files
    d = tempfile.mkdtemp(prefix='ydl-unittest_FileDownloader-')
    # Initialize FileDownloader with temp directory
    fd = FileDownloader('youtube-dl-test', {'outtmpl': d + '/%(id)s.%(ext)s'})

    # Test with a non existing file
    # The return value should be None
    assert fd.try_utime('fakefile', 'never') is None

    # Test with an existing directory
    # The return value should be None

# Generated at 2022-06-14 15:09:12.425694
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class TestDownloader(FileDownloader):
        def __init__(self, dl, params):
            self.dl = dl
            self.params = params
            self.calls = []

        def _sleep(self, s):
            self.calls.append(s)

    dl1 = TestDownloader(None, {'ratelimit': 100, 'retries': 0})
    dl1.slow_down(0, 0, 10)
    dl1.slow_down(0, 0, 90)
    dl1.slow_down(0, 0, 110)
    dl1.slow_down(0, 0, 10)
    assert dl1.calls == [0, 0, .1, .1]


# Generated at 2022-06-14 15:09:33.777207
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader()
    fd.params = {'nooverwrites':True}
    import os.path
    name = "Shang_Yu-Yu.mp4"
    fd.report_file_already_downloaded(name)
    def print_fail():
        print("error")
    #fd.report_file_already_downloaded = print_fail
    #fd.report_file_already_downloaded("name")

test_FileDownloader_report_file_already_downloaded()
 

# Generated at 2022-06-14 15:09:42.586231
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    ydl = FileDownloader({'ratelimit': 1})

    # No sleep
    ydl.slow_down(time.time(), time.time(), 1000)

    # Sleep for about 0.5 second
    ydl.slow_down(time.time(), time.time() + 0.5, 1000)

    # Should not sleep
    ydl.slow_down(time.time(), time.time(), 1500)

    # Should sleep for about 0.5 second
    ydl.slow_down(time.time(), time.time() + 0.5, 1500)


# Generated at 2022-06-14 15:09:53.046226
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from .YoutubeDL import YoutubeDL
    from .postprocessor.FFmpegMetadataPP import FFmpegMetadataPP

    filename = os.path.join(os.path.dirname(__file__), 'config_template')
    params = YoutubeDL(filename=filename).params

    # no limit
    params['ratelimit'] = None
    fd = FileDownloader(params=params, info_dict={})
    speed = fd.best_block_size(elapsed_time=1, bytes=3)
    assert speed == 1024 * 1024

    # no limit
    params['ratelimit'] = None
    fd = FileDownloader(params=params, info_dict={})
    speed = fd.best_block_size(elapsed_time=1, bytes=3)
    assert speed == 1024 * 1024

    # too slow


# Generated at 2022-06-14 15:10:01.654914
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    # Test without temp name
    filename = 'filename.f91'
    assert FileDownloader(None,None).undo_temp_name(filename) == filename
    # Test with temp name
    filename = 'filename.f91.part'
    assert FileDownloader(None,None).undo_temp_name(filename) == 'filename.f91'
    # Test on non-existing file
    filename = ''
    assert FileDownloader(None,None).undo_temp_name(filename) == filename
test_FileDownloader_undo_temp_name()


# Generated at 2022-06-14 15:10:11.467880
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = FileDownloader(None, {'ytdl_hook_filename': 'a'})
    assert fd.best_block_size(1, 10) == 10
    assert fd.best_block_size(10, 10) == 10
    assert fd.best_block_size(10, 1) == 1
    assert fd.best_block_size(10, 2621440) == 2621440
    assert fd.best_block_size(10, 1310720) == 1310720
    assert fd.best_block_size(10, 1310719) == 655360
    assert fd.best_block_size(0, 1) == 1
    assert fd.best_block_size(0, 2621440) == 2621440
    assert fd.best_block_size(0, 0)

# Generated at 2022-06-14 15:10:12.699469
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    assert False, "Test failed"


# Generated at 2022-06-14 15:10:25.068562
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from .extractor import YoutubeIE
    from .extractor.youtube import YoutubeIE as OldSock

    import time
    import random
    import sys

    class TestDownloader(FileDownloader):
        def real_download(self, filename, info_dict):
            return True

    ydl = TestDownloader({'ratelimit': '10k'})
    start = time.time()
    bytes = 0
    while time.time() - start < 5:
        elapsed = time.time() - start
        byte_counter = int(elapsed * (1024 * 10))
        bytes += byte_counter - bytes
        ydl.slow_down(start, time.time(), bytes)
        sys.stderr.write('.')
        time.sleep(random.random() / 10)
    print()
    print('Speed limit test passed')



# Generated at 2022-06-14 15:10:33.699899
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.Compat import compat_os_name
    downloader = FileDownloader(YoutubeDL(), {})
    if compat_os_name == 'nt':
        assert downloader.report_file_already_downloaded('C:\\Windows\\System32\\Drivers\\etc\\hosts') == '[download] The file has already been downloaded'
    else:
        assert downloader.report_file_already_downloaded('/etc/hosts') == '[download] /etc/hosts has already been downloaded'


# Generated at 2022-06-14 15:10:34.278413
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    pass
    

# Generated at 2022-06-14 15:10:46.527098
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile, time, shutil, os

    def _assert_utime(FileDownloader, filename, atime, mtime):
        assert os.path.isfile(filename)
        assert os.path.getatime(filename) == atime
        assert os.path.getmtime(filename) == mtime

    with tempfile.NamedTemporaryFile() as tf:
        # Write some data to the file
        tf.write(b'abc')
        # Create a FileDownloader
        fd = FileDownloader({})
        # Modify utime
        fd.try_utime(tf.name, None)
        _assert_utime(fd, tf.name, atime = time.time(), mtime = 0)

        # Modify utime again

# Generated at 2022-06-14 15:11:04.299436
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Downloader with a dummy get_view_count() method
    ydl = YoutubeDL({})

    def gvc():
        if ydl.gvc_calls == 0:
            ydl.gvc_calls = 1
            return None
        elif ydl.gvc_calls == 1:
            ydl.gvc_calls = 2
            return 100
        elif ydl.gvc_calls == 2:
            ydl.gvc_calls = 3
            return 1000000
        elif ydl.gvc_calls == 3:
            ydl.gvc_calls = 4
            return None
        else:
            assert False
    ydl.gvc_calls = 0
    ydl.get_view_count = gvc

    # Fake download
    fd = FileDownloader

# Generated at 2022-06-14 15:11:17.011157
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    # For a file size of 16, block sizes of 1, 2, 4, 8 and 16 should be used
    # with the given elapsed times (in seconds).
    block_size_test_cases = [
        (1, (1, )),
        (2, (1, 1)),
        (3, (1, 1, 1)),
        (4, (1, 1, 1, 1)),
        (5, (2, 2, 1)),
        (6, (2, 2, 1, 1)),
        (7, (4, 2, 1)),
        (8, (4, 2, 1, 1)),
        (9, (4, 2, 1, 1, 1)),
        (16, (4, 4, 4, 4)),
    ]

    fd = FileDownloader(None, None)


# Generated at 2022-06-14 15:11:26.715047
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    from youtube_dl.YoutubeDL import YoutubeDL
    from tempfile import mkstemp
    from os import close, remove
    from os.path import exists
    assert callable(FileDownloader.download)
    assert exists

    fd, fname = mkstemp('.tmp')
    close(fd)

# Generated at 2022-06-14 15:11:29.893524
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():

    # Arrange
    test_obj = FileDownloader()
    my_filename = "my_filename"

    # Act
    result = test_obj.temp_name(my_filename)

    # Assert
    assert result == "my_filename.part"

# Generated at 2022-06-14 15:11:33.618061
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    src = FileDownloader(ydl)
    assert src.download(os.path.join('dummy', 'file'), {'id': '12345', 'url': 'url', 'title': 'title'}) is False



# Generated at 2022-06-14 15:11:43.659672
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert None == FileDownloader.parse_bytes(None)
    assert 3000000 == FileDownloader.parse_bytes('3M')
    assert 3000000 == FileDownloader.parse_bytes('3.0M')
    assert 3000000 == FileDownloader.parse_bytes(' 3 M ')
    assert 300 == FileDownloader.parse_bytes(' 0.3 M ')
    assert 30000000000 == FileDownloader.parse_bytes('3G')
    assert 30 == FileDownloader.parse_bytes('30')
    assert None == FileDownloader.parse_bytes('e')

# Generated at 2022-06-14 15:11:48.480615
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import tempfile
    import io

    info_dict = {
        'title': 'Sample video'
    }
    test_fd = io.BytesIO()
    fd = FileDownloader(None, {'outtmpl': '%(title)s.f4v'}, {'progress_hooks': []})
    ret = fd.download(test_fd, info_dict)

    assert ret is True

# Generated at 2022-06-14 15:11:52.650504
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    _file_downloader = FileDownloader('', '')
    now = 10
    byte_counter = 0
    start_time = 0
    _file_downloader.slow_down(start_time, now, byte_counter)



# Generated at 2022-06-14 15:12:03.818566
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    """slow_down method should read the rate parameter and sleep
    accordingly when it is used on a download. This will test this
    behavior.
    """
    # Test Params Object
    Options = namedtuple('Options', [
        'ratelimit', 'noprogress', 'retries', 'buffersize', 'noresizebuffer',
        'continuedl', 'nopart', 'updatetime', 'test',
    ])
    options = Options(
        ratelimit = 10240, # 10 KB/s
        noprogress = True,
        retries = 5,
        buffersize = -1,
        noresizebuffer = '',
        continuedl = '',
        nopart = '',
        updatetime = '',
        test = '',
    )
    # Test the slow_down method
    f

# Generated at 2022-06-14 15:12:16.153349
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    # Test cases:
    # start - start time
    # now - current time
    # curr - current number of bytes downloaded
    # total - total bytes to be delivered
    # rate - expected rate of download in bytes per second
    # eta - expected time left in seconds
    #
    # If eta is None, then it does not matter what calc_eta returns, as long
    # as it is not an exception. This is used to make sure calc_eta does not
    # divide by zero.
    #
    # If rate is None, then the returned rate from calc_eta does not matter,
    # as long as it is greater than zero or an exception is thrown. Otherwise
    # it is compared to the rate returned by calc_eta to make sure it is
    # reasonable. All rates less than 2^15 bytes/second are reasonable.
    testcases

# Generated at 2022-06-14 15:12:50.534755
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # input
    def test(input):
        fn = test_FileDownloader_report_progress.fn
        fn.to_screen = FakeOutput()
        fn.report_progress(input)

    test_FileDownloader_report_progress.fn = FileDownloader({})

    test({'elapsed': 0, 'total_bytes': 10, 'downloaded_bytes': 3,
          'speed': 10})
    eq('\r[download] 0.0% of 10 at 10.0/s ETA Unknown ETA',
       test_FileDownloader_report_progress.fn.to_screen.get_output())

    test({'elapsed': 5, 'total_bytes': 10, 'downloaded_bytes': 2,
          'speed': 10})

# Generated at 2022-06-14 15:12:59.394039
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class FakeYoutubeDl:
        def __init__(self):
            self.to_screen = lambda *a, **k: None
            self.to_console_title = lambda *a, **k: None

    class FakeFileDownloader(FileDownloader):
        # This method must not be used in unit test.
        # It is defined here just in case download() is called by some
        # mistake.
        def real_download(self, filename, info_dict):
            assert False

    def FakeProgressHook(a):
        assert a['filename'] == 'a'
        assert a['status'] == 'status'
        FakeProgressHook.called = True
    FakeProgressHook.called = False

    # status: downloading
    fd = FakeFileDownloader(FakeYoutubeDl(), None)
    fd.to_

# Generated at 2022-06-14 15:13:11.031219
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Arrange
    fileDownloader = FileDownloader({
        'noprogress': False,
        'continue_dl': True,
        'nopart': False})

    # Act
    statuses = [
        {'status': 'finished', 'total_bytes': 12345, 'eta': 1},
        {'status': 'downloading', 'eta': None, 'total_bytes': 12345, 'downloaded_bytes': 1, 'elapsed': 0.1, 'speed': 1.0},
        {'status': 'downloading', 'eta': 1, 'total_bytes': 12345, 'downloaded_bytes': 12344, 'elapsed': 1.0, 'speed': 1.0},
    ]


# Generated at 2022-06-14 15:13:15.278387
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    start_time=0
    now=0
    last_downloaded_bytes=0
    downloader=FileDownloader

# Generated at 2022-06-14 15:13:22.993542
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from .YoutubeDL import YoutubeDL

    ydl = YoutubeDL({'noprogress': True})
    fd = FileDownloader(ydl)
    fd.report_progress(
        {'downloaded_bytes': 200,
         'total_bytes': 100,
         'total_bytes_estimate': 100,
         'elapsed': 3,
         'eta': 5,
         'speed': 100,
         'filename': 'hello',
         'status': 'downloading'
         })
    assert fd.params['noprogress']


test_FileDownloader_report_progress.func_annotations = {}

# Generated at 2022-06-14 15:13:29.664050
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    def touch(filename, mod_time):
        try:
            os.utime(filename, (time.time(), mod_time))
        except Exception as e:
            raise RuntimeError('Failed to touch file %r: %r' % (filename, e))

    def assert_mtime_is(filename, expected_mtime):
        mtime = os.path.getmtime(encodeFilename(filename))
        if not (mtime == expected_mtime or mtime == expected_mtime + 1):
            raise RuntimeError(
                'Incorrect modification time of file %r: %r (expected: %r)'
                % (filename, mtime, expected_mtime))

    x = FileDownloader(None, params={})
    filename = os.path.join(tempfile.gettempdir(), 'tmp-mtime.txt')

# Generated at 2022-06-14 15:13:41.284957
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class TestLogger(object):
        def __init__(self, params):
            self.infos = []
        def to_screen(self, message, skip_eol=False):
            self.infos.append(message)
    params = {'progress_with_newline': True}
    logger = TestLogger(params)
    fd = FileDownloader({'logger': logger, 'params': params})
    fd.report_progress({'status': 'downloading', 'total_bytes': 100, 'downloaded_bytes': 20, 'elapsed': 100})
    fd.report_progress({'status': 'downloading', 'total_bytes': None, 'downloaded_bytes': 20, 'elapsed': 100})

# Generated at 2022-06-14 15:13:49.338507
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    ydl = YoutubeDL()
    ydl.params['verbose'] = False
    ydl.report_warning = lambda *args, **kargs: None
    fd = FileDownloader(ydl, None)

    fd.to_screen = lambda s: None
    fd.to_console_title = lambda s: None

    # Speed is None
    fd._report_progress_prev_line_length = 1
    fd.report_progress(
        {'status': 'downloading', '_percent_str': '33', '_speed_str': 'Unknown speed', '_eta_str': 'Unknown ETA',
         '_total_bytes_str': 'Unknown size'})

# Generated at 2022-06-14 15:13:59.934882
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile
    import os
    import shutil
    class _testFileDownloader(FileDownloader):
        def __init__(self, params):
            self._params = params
            tempdir = tempfile.mkdtemp()
            self._tmpfilename = os.path.join(tempdir, 'foo.tmp')
            self._tmpfile = open(self._tmpfilename, 'wb')
        def to_screen(self, *args, **kargs):
            pass
        def to_console_title(self, *args, **kargs):
            pass
        def trouble(self, *args, **kargs):
            pass
        def report_warning(self, *args, **kargs):
            pass
        def report_error(self, *args, **kargs):
            pass

# Generated at 2022-06-14 15:14:09.254037
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    dl = FileDownloader({'nopart': False})
    assert dl.temp_name('bla') == 'bla.part'
    assert dl.temp_name('bla.mp4') == 'bla.mp4.part'
    assert dl.temp_name('bla.part') == 'bla.part.part' # Shouldn't happen
    assert dl.temp_name('bla.part.mp4') == 'bla.part.mp4.part' # Shouldn't happen
    assert dl.temp_name(u'\xf6\xe4\xfc') == u'\xf6\xe4\xfc.part'

# Generated at 2022-06-14 15:14:46.483905
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    dl = FileDownloader({})
    assert dl.temp_name('abc') == 'abc.part'
    assert dl.temp_name('-').startswith('-' + os.path.sep)
    assert '.' not in dl.temp_name('-')

    dl = FileDownloader({'nopart': True})
    assert dl.temp_name('abc') == 'abc'
    assert dl.temp_name('-') == '-'

    dl = FileDownloader({'nopart': True})
    dst = 'this file already exists and is not a directory'
    assert dl.temp_name(dst) == dst
# unit tests for FileDownloader module
from __future__ import unicode_literals

from tempfile import NamedTemporaryFile


import pytest


# Generated at 2022-06-14 15:14:58.280614
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    if not hasattr(sys.stdin, 'isatty') or not sys.stdin.isatty():
        print('No need to test FileDownloader.best_block_size')
        return

    import itertools
    import random
    import subprocess
    import shutil
    import tempfile
    import time
    import sys

    # Determine the terminal width
    columns = shutil.get_terminal_size().columns

    # Set a dummy --console-title
    opts = {'console_title': True}

    # Prepare a long enough title
    title = ' ' * columns
    app = FileDownloader(opts)
    app.to_console_title(title)

    # Prepare a list of candidates that we will iterate over

# Generated at 2022-06-14 15:15:08.548347
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile
    import time
    from .utils import DateRange

    fd, tmppath = tempfile.mkstemp()
    os.close(fd)
    os.utime(tmppath, (0, 0))

    def check_range(r, s, e):
        assert (r.start == s)
        assert (r.end == e)

    def check_file_time(time_str, start, end):
        fd = FileDownloader({})
        fd.try_utime(tmppath, time_str)
        s = os.path.getmtime(tmppath)
        e = os.path.getatime(tmppath)
        check_range(DateRange(s, e), start, end)

    def check_now():
        x = time.time()

# Generated at 2022-06-14 15:15:12.368494
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    for r in iter_reports():
        fdld = FileDownloader(ydl=None, params=None)
        fdld.report_progress(r)
        r['_elapsed_str'] = fdld.format_seconds(r['elapsed'])
        fdld.report_progress(r)
# TODO: test FileDownloader.download()



# Generated at 2022-06-14 15:15:23.736370
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import os
    from tempfile import mkstemp
    from time import time, sleep
    from .utils import encodeFilename

    # Create a test file
    fd, filename = mkstemp()
    os.close(fd)

    def try_utime(fd, filename, last_modified_hdr):
        # Set the file's modification time
        t = time()
        os.utime(filename, (t, t))

        # Invoke try_utime and check that the modification time is correct
        try_utime = FileDownloader({}).try_utime
        assert try_utime(encodeFilename(filename), last_modified_hdr) == t

        # Check that the modification time is not changed if we invoke again
        # try_utime
        sleep(0.01)
        new_t = try_utime

# Generated at 2022-06-14 15:15:32.234208
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import unittest

    class TestFileDownloader(FileDownloader):
        def slow_down(self, start_time, now, bytes):
            slow_down_called_with = (
                (start_time, now, bytes),
                {'ratelimit': self.params['ratelimit']})
            return slow_down_called_with

    class TestDownloader(unittest.TestCase):
        def setUp(self):
            self.fd = TestFileDownloader({'ratelimit': 1})

        def test_slow_down_inf_ratelimit(self):
            self.fd.params['ratelimit'] = float('inf')
            result = self.fd.slow_down(0, 1, 1024)
            self.assertEqual(result, None)


# Generated at 2022-06-14 15:15:44.799571
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    assert(FileDownloader._FileDownloader__temp_name('abc.mp4', None) == 'abc.mp4.part')
    assert(FileDownloader._FileDownloader__temp_name('/root/abc.mp4', None) == '/root/abc.mp4.part')
    assert(FileDownloader._FileDownloader__temp_name('/root/abc.mp4', {'nopart': True, 'continuedl': True}) == '/root/abc.mp4.part')
    assert(FileDownloader._FileDownloader__temp_name('/root/abc.mp4', {'nopart': True, 'continuedl': False}) == '/root/abc.mp4')

# Generated at 2022-06-14 15:15:50.149248
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import tempfile
    from subprocess import Popen, PIPE, STDOUT, check_output
    exec_test_cmd = '{} -c {}'.format(sys.executable, repr(compat_shlex_quote(
        'from __main__ import test_FileDownloader_slow_down_helper, FileDownloader; '
        'test_FileDownloader_slow_down_helper(FileDownloader())')))
    def test(ratelimit, expected_time):
        p = Popen(
            [sys.executable, '-c', 'import time; print(time.time())'],
            stdout=PIPE, stderr=STDOUT)
        start_time = float(p.communicate()[0])

# Generated at 2022-06-14 15:16:00.215104
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    if sys.platform == 'win32':
        return
    def _check(filename, timestr, expected):
        fd = FileDownloader({})
        f = open(filename, 'wb')
        f.write(b'123')
        f.close()
        try:
            fd.try_utime(filename, timestr)
            stat_res = os.stat(filename)
            assert stat_res.st_mtime == expected, 'Expected %f but got %f' % (
                expected, stat_res.st_mtime)
        finally:
            if os.path.exists(filename):
                os.remove(filename)

# Generated at 2022-06-14 15:16:07.386568
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(params={})
    assert 'test.part' == fd.temp_name('test')
    assert 'test.part' == fd.temp_name('test.part')
    assert 'test' == fd.temp_name('test', now=lambda: True)
    assert 'test' == fd.temp_name('test', now=lambda: False)
# Test for method undo_temp_name of class FileDownloader