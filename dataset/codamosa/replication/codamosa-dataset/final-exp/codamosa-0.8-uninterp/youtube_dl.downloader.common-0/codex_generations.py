

# Generated at 2022-06-14 15:08:03.729043
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from .YoutubeDL import YoutubeDL
    obj = FileDownloader({}, YoutubeDL())


# Generated at 2022-06-14 15:08:13.511807
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    fd = FileDownloader({})
    assert fd.calc_speed(0, 0, 0) == None
    assert fd.calc_speed(10, 5, 1) == None
    assert fd.calc_speed(10, 10, 1) == None
    assert fd.calc_speed(0, 50, 1) == None
    assert fd.calc_speed(10, 15, 0) == None

    assert fd.calc_speed(10, 15, 1) == 0.2
    assert fd.calc_speed(10, 15, 100) == 20
    assert fd.calc_speed(10, 15, 200) == 40


# Generated at 2022-06-14 15:08:16.891072
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    
    a = FileDownloader(params={})
    if a.undo_temp_name('teste.pdf') == 'teste.pdf':
        print("test_FileDownloader_undo_temp_name passed")
    else:
        print("test_FileDownloader_undo_temp_name failed")
        

# Generated at 2022-06-14 15:08:27.340138
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # Load a file downloader
    params = {
        'outtmpl': '%(id)s%(ext)s',
        # This is a hack: we need to use the same object in all tests
        'nopart' : True,
        }
    downer = FileDownloader(params)

    assert downer.temp_name('abc') == 'abc'
    assert downer.temp_name('.abc') == '.abc'
    assert downer.temp_name('abc.def') == 'abc.part'
    assert downer.temp_name('/tmp/abc.def') == '/tmp/abc.part'
    assert downer.temp_name('c:/windows/temp/abc.def') == 'c:/windows/temp/abc.part'

# Generated at 2022-06-14 15:08:35.316895
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    def test_eta(start_time, now, current_bytes, total_bytes, expected_eta):
        fd = FileDownloader({})
        fd.report_progress = lambda s: s
        assert fd.calc_eta(start_time, now, current_bytes, total_bytes) == expected_eta

    test_eta(0, 1000, 0, 1000, 1000)
    test_eta(0, 1000, 1000, 1000, 0)
    test_eta(0, 1000, 500, 1000, 500)
    test_eta(0, 1000, 600, 1000, 400)
    test_eta(0, 1000, 500, 1000, 500)
    test_eta(0, 1000, 550, 1000, 450)
    test_eta(0, 1000, 0, 1000, 1000)

# Generated at 2022-06-14 15:08:46.066794
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Verify progress report for a download that finishes
    fake_dl = FakeFileDownloader()
    fake_dl.report_progress({
        'status': 'finished', '_percent_str': '51.1%', '_total_bytes_str': '524288',
        'downloaded_bytes': 268621, 'speed': 123456, 'elapsed': 3, 'eta': 0,
        'total_bytes': 524288})
    assert fake_dl.messages[-1] == '[download] 100% of 524.3KiB at 123.0KiB/s ETA 0 seconds'

    # Verify progress report for a download that doesn't finish
    fake_dl = FakeFileDownloader()

# Generated at 2022-06-14 15:08:52.954576
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    from .compat import StringIO

    class TestFD(FileDownloader):
        def to_screen(self, *args, **kargs):
            pass

        def to_stderr(self, message):
            pass

    # Base class for test cases for method FileDownloader.calc_eta
    class TestCase:
        def __init__(self, test_name, start=None, now=None, current=None, total=None, expected=None):
            self.test_name = test_name
            self.start = start
            self.now = now
            self.current = current
            self.total = total
            self.expected = expected

        def __str__(self):
            return self.test_name

    # Test cases for method FileDownloader.calc_eta

# Generated at 2022-06-14 15:09:02.387693
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import subprocess
    import tempfile
    import shutil
    import time
    import os

    dl = FileDownloader({'noprogress': False, 'quiet': True})

    tmpdir = tempfile.mkdtemp()
    test_file = os.path.join(tmpdir, 'file')

    # Create a file
    with open(test_file, 'wb') as test_file_handle:
        test_file_handle.write(b'foobar')
        test_file_handle.flush()

    # Already downloaded file, don't check if it's the last line
    dl.report_progress({
        'status': 'finished',
    })

    # No ETA

# Generated at 2022-06-14 15:09:12.327599
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # This test ensures that the correct string is being displayed
    # when report_progress is called with a given status dict.
    # The statuses are as follows:
    # 1. Downloading
    # 2. Finished downloading
    # 3. Unknown ETA
    # 4. Single line progress
    # 5. No progress
    # 6. Resuming download
    # 7. Retrying download
    # 8. File already downloaded
    # 9. Unable to resume download
    fd = FileDownloader(None, None)

    # Test #1
    status = {'status': 'downloading', 'downloaded_bytes': 0, 'total_bytes': None,
              'total_bytes_estimate': None, 'eta': None, 'speed': None,
              'elapsed': None}
    expected = 'Unknown % at Unknown speed ETA Unknown ETA'

# Generated at 2022-06-14 15:09:16.746329
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    # Test infinity
    assert format_retries(float('inf')) == 'inf'

    # Test regular values
    assert format_retries(1) == '1'
    assert format_retries(10) == '10'

# Generated at 2022-06-14 15:09:34.511092
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    class TestDownloader(FileDownloader):
        def real_download(self, filename, info_dict):
            return True

    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    info = ydl.extract_info(test_urls[2], download=False)
    fd = TestDownloader(ydl, info)
    fd.download(os.path.join('test', 'test'))

# Unit tests for method calculate_percent

# Generated at 2022-06-14 15:09:46.725256
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # pylint: disable=missing-docstring
    import time
    import math

    def time_float():
        return time.time()

    def time_int():
        return math.floor(time_float())

    def time_sleep(secs):
        pass

    def calc_speed(start, now, bytes):
        dif = now - start
        if bytes == 0 or dif < 0.001:
            return None
        return float(bytes) / dif

    real_time = time
    real_calc_speed = FileDownloader.calc_speed
    real_sleep = time.sleep

# Generated at 2022-06-14 15:09:55.818768
# Unit test for method try_utime of class FileDownloader

# Generated at 2022-06-14 15:10:01.145367
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    '''
    From our observations the best block size is the average speed
    divided by 2
    '''
    downloader = FileDownloader(None, None)
    assert(downloader.best_block_size(1, 1) == 0.5)
    assert(downloader.best_block_size(1, 1024) == 512)

# Generated at 2022-06-14 15:10:11.174418
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader(None, {'nooverwrites': True})
    # Invalid dates (all are zero or negative)
    assert fd.try_utime('filename', 'Thu, 01 Jan 1970 00:00:00 +0000') is None
    assert fd.try_utime('filename', 'Sat, 01 Jan 2000 00:00:00 +0000') is None
    assert fd.try_utime('filename', 'Mon, 01 Jan 2000 00:00:00 +00') is None
    assert fd.try_utime('filename', 'Mon, 01 Jan 2000 00:00:00 +0000') is None
    assert fd.try_utime('filename', 'Mon, 01 Jan 2000 00:00:00 GMT') is None
    # Inexistent file

# Generated at 2022-06-14 15:10:12.426474
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # FIXME
    pass



# Generated at 2022-06-14 15:10:17.493347
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    filename, info_dict = "file.name", {"key":"value"}
    fd = FileDownloader(None, {}, None)
    fd.download(filename, info_dict)

'''
# test_FileDownloader_download()
test_FileDownloader_download()
'''

# Generated at 2022-06-14 15:10:26.455591
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    d = FileDownloader({})

    # Test: Download doesn't start yet
    s = {
        'status': 'waiting',
    }
    d.report_progress(s)
    assert(s['status'] == 'waiting')

    # Test: Download does start
    s = {
        'status': 'downloading',
        'speed': 0,
        'total_bytes': None,
        'downloaded_bytes': 0,
    }
    d.report_progress(s)
    assert(s['downloaded_bytes'] == 0)



# Generated at 2022-06-14 15:10:37.228538
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from ytdl_api.config import FileDownloaderParams
    from ytdl_api.YoutubeDL import YoutubeDL

    class DummyYoutubedl(YoutubeDL):

        def __init__(self, *args, **kargs):
            YoutubeDL.__init__(self, *args, **kargs)
            self.outputs = []

        def to_screen(self, *args, **kargs):
            self.outputs.append(('to_screen', args, kargs))

        def trouble(self, *args, **kargs):
            self.outputs.append(('trouble', args, kargs))

        def to_console_title(self, *args, **kargs):
            self.outputs.append(('to_console_title', args, kargs))


# Generated at 2022-06-14 15:10:49.248125
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    
    # Download video
    params = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': '%(id)s',
        'nooverwrites': True,
    }

    to_test = []
    to_test.append(('test_%(id)s.part', 'test_%(id)s'))
    to_test.append(('test.mp4', 'test.mp4'))
    to_test.append(('test.part.mp4', 'test.part.mp4'))

    for (test_in,test_out) in to_test:
        params['outtmpl'] = test_in
        assert(FileDownloader.undo_temp_name(params, test_in) == test_out)

# Generated at 2022-06-14 15:11:10.138873
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    assert FileDownloader.try_utime(
        '', timeconvert('Tue, 02 Jul 2013 01:45:34 GMT')) == 1372509934.0



# Generated at 2022-06-14 15:11:17.612654
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    fd = FileDownloader(params={})
    assert fd.format_retries(5) == '5'
    assert fd.format_retries(float('inf')) == 'inf'
    assert fd.format_retries(float('-inf')) == 'inf'
    assert fd.format_retries(float('nan')) == 'inf'
    assert fd.format_retries(None) == 'inf'



# Generated at 2022-06-14 15:11:22.651831
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import sys
    import pytest

    fd = FileDownloader(None, None)

    # As per issue:
    # https://github.com/ytdl-org/youtube-dl/issues/13662
    # The following line should be printed:
    #   [download] 0.0% of 734.05MiB at 5.24MiB/s ETA 00:02
    s = {
        'downloaded_bytes': 0,
        'total_bytes': 777727488,
        'speed': 5480032,
        'eta': 120,
        'status': 'downloading'
    }
    fd.report_progress(s)

# Generated at 2022-06-14 15:11:31.280321
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    f = FileDownloader({'nopart':True,})

    assert f.temp_name('abc') == 'abc'
    assert f.temp_name('/abc') == '/abc'
    assert f.temp_name('/abc.def') == '/abc.def'
    assert f.temp_name('/abc.def-5') == '/abc.def-5'
    assert f.temp_name('abc.def') == 'abc.def'
    assert f.temp_name('C:/abc') == 'C:/abc'
    assert f.temp_name('C:/abc.txt') == 'C:/abc.txt'
    assert f.temp_name('~/abc') == '~/abc'
    assert f.temp_name('~/abc.txt') == '~/abc.txt'
    assert f.temp

# Generated at 2022-06-14 15:11:43.568689
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # No rate limit.
    fd = FileDownloader({'ratelimit': None}, None)
    start_time = time.time()
    fd.slow_down(start_time, time.time(), 2240)
    elapsed_time = time.time() - start_time
    assert elapsed_time < 1
    # No rate limit, very fast transfer speed.
    fd = FileDownloader({'ratelimit': None}, None)
    start_time = time.time()
    fd.slow_down(start_time, time.time(), 1024 * 1024)
    elapsed_time = time.time() - start_time
    assert elapsed_time < 1
    # Rate limit, slower transfer speed.
    fd = FileDownloader({'ratelimit': 1024 * 1024}, None)
    start_time = time.time()
    f

# Generated at 2022-06-14 15:11:51.213056
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader({})
    assert fd.temp_name('a') == 'a.part'
    assert fd.temp_name('a.b') == 'a.b.part'
    assert fd.temp_name('a.b') == 'a.b.part'
    assert fd.temp_name('c:\\a') == 'c:\\a.part'
    assert fd.temp_name('c:/a') == 'c:/a.part'
    assert fd.temp_name('c:/a') == 'c:/a.part'
    assert fd.temp_name('/tmp/a') == '/tmp/a.part'
    assert fd.temp_name('/tmp/a') == '/tmp/a.part'

# Generated at 2022-06-14 15:12:02.771094
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    """This method tests the report_progress of class FileDownloader."""

    # Test without "ratelimit"
    params = {
        'verbose': True,
        'proxy': True
    }

    ydl = YoutubeDL(params)
    fd = FileDownloader(ydl)

    s = {
        'downloaded_bytes': '321321',
        'eta': 123,
        'elapsed': 0,
        'speed': 3,
        'total_bytes': '123123',
        'status': 'downloading',
        'total_bytes_estimate': '123123'
    }

    fd.report_progress(s)

    # Test with "ratelimit"
    params = {
        'verbose': True,
        'proxy': True,
        'ratelimit': 2
    }

    y

# Generated at 2022-06-14 15:12:15.555119
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Given
    fd = FileDownloader(None)

    # Tests with a non-existent file
    filename = tempfile.mktemp(suffix='.test', prefix='youtube-dl-utime-')
    expected_filetime = time.time() - 5
    last_modified_hdr = time.strftime(
        "%a, %d %b %Y %H:%M:%S GMT", time.gmtime(expected_filetime))
    assert not os.path.isfile(filename)

    # When
    actual_filetime = fd.try_utime(filename, last_modified_hdr)

    # Then
    assert actual_filetime is None
    assert not os.path.isfile(filename)

    # Tests with an existent file

# Generated at 2022-06-14 15:12:27.399676
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({})
    # These values should be sufficient to detect an error
    fd.params['ratelimit'] = 1
    fd.params['retries'] = 0

    start_time = time.time()
    # Should not sleep for the first chunk
    fd.slow_down(start_time, None, 0)
    # Should probably sleep for the second chunk
    fd.slow_down(start_time, None, 100)
    # Should sleep for the third chunk
    fd.slow_down(start_time, None, 200)
    # Sleep time should increase linearly
    sleep_time1 = time.time() - start_time
    fd.slow_down(start_time, None, 300)
    sleep_time2 = time.time() - start_time - sleep_time1
    f

# Generated at 2022-06-14 15:12:31.024029
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    fd = FileDownloader(None, params={})
    assert fd.download(None) == False

if __name__ == '__main__':
    # test_FileDownloader_download()
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 15:12:49.291514
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # Check if the method will correctly return the correct name
    # when the file exists and nopart is False
    fd = FileDownloader(YoutubeDL(), {})
    fd.params['nopart'] = False
    assert fd.temp_name('test') == 'test.part'
    # Check if the method will correctly return the correct name
    # when the file exists and nopart is True
    fd = FileDownloader(YoutubeDL(), {})
    fd.params['nopart'] = True
    assert fd.temp_name('test') == 'test'

# Generated at 2022-06-14 15:12:54.109266
# Unit test for method slow_down of class FileDownloader

# Generated at 2022-06-14 15:12:57.918976
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    assert FileDownloader.format_retries(float('inf')) == 'inf'
    assert FileDownloader.format_retries(1) == '1'
    assert FileDownloader.format_retries(float('NaN')) == 'inf'
    assert FileDownloader.format_retries(1.2) == '1'

# Generated at 2022-06-14 15:13:03.006097
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader(None)
    fd.report_file_already_downloaded('downloaded.mp4')

if __name__ == '__main__':
    test_FileDownloader_report_file_already_downloaded()

# Generated at 2022-06-14 15:13:12.713686
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Test for positive result (> 0)
    result = FileDownloader(FakeYtdl()).try_utime('filename', 'Mon, 02 Jul 2018 21:54:02 +0000')
    if result is None:
        print('Test case 1, no valid filetime.')
    elif result > 0:
        print('Test case 1, filetime is ', result)
    else:
        print('Test case 1, filetime is valid but not positive.')

    # Test for None
    result = FileDownloader(FakeYtdl()).try_utime('filename', 'Invalid time format')
    if result is None:
        print('Test case 2, no valid filetime.')
    else:
        print('Test case 2, filetime is valid but not expected.')

    # Test for zero

# Generated at 2022-06-14 15:13:17.105879
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    downloader = FileDownloader("https://www.youtube.com/watch?v=jNQXAC9IVRw",
                                "test_videos/youtube_dl.py")
    assert downloader.undo_temp_name("test_videos/youtube_dl.py.part") == "test_videos/youtube_dl.py"

# Generated at 2022-06-14 15:13:26.461294
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    def gen_sample(url, num_chunks=10, chunk_size=1024):
        for i in range(num_chunks):
            yield b'X' * chunk_size

    from io import BytesIO
    assert FileDownloader._FileDownloader__write_chunks(
        BytesIO(), gen_sample('http://example.com/', chunk_size=1024, num_chunks=10),
        chunksize=1024)

    c = FileDownloader(None)
    c.report_destination = lambda f: None
    c.report_progress = lambda s: None
    c.to_screen = lambda s: None
    c.to_console_title = lambda s: None
    c.to_stderr = lambda s: None


# Generated at 2022-06-14 15:13:37.876021
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded(): 
    """
    Unit test for method report_file_already_downloaded of class FileDownloader
    """
    print('\nConstructing FileDownloader(parameters={}), please wait')
    try:
        fd = FileDownloader({})
    except SystemError:
        print('SystemError')
        return
    else:
        print('Done!')
    
    # report_file_already_downloaded(self, file_name):
    # No file_name parameter
    print('Executing FileDownloader.report_file_already_downloaded(file_name=None), please wait')
    try:
        fd.report_file_already_downloaded(file_name=None)
    except TypeError:
        print('TypeError')
        return
    else:
        print('Done!')
    

# Generated at 2022-06-14 15:13:45.557499
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader({})
    fd.params.update({
        'no_overwrites': False,
        'nopart': False,
        'continuedl': True
    })
    assert fd.temp_name('test.mp4') == 'test.mp4.part'
    fd.params['nopart'] = True
    assert fd.temp_name('test.mp4') == 'test.mp4'
    fd.params['nopart'] = False
    fd.params['continuedl'] = False
    assert fd.temp_name('test.mp4') == 'test.mp4'
    fd.params['continuedl'] = True
    fd.params['no_overwrites'] = True
    assert fd.temp_name('test.mp4')

# Generated at 2022-06-14 15:13:52.605376
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import time

    t1 = time.time()
    downloader = FileDownloader({'ratelimit': 10, 'nooverwrites': True})
    time.sleep(0.01)
    downloader.slow_down(t1, time.time(), 1)
    time.sleep(0.01)
    downloader.slow_down(t1, time.time(), 200 * 1024)
    time.sleep(0.01)
    downloader.slow_down(t1, time.time(), 10 * 1024)
    time.sleep(0.01)
    downloader.slow_down(t1, time.time(), 2.5 * 1024)
    time.sleep(0.01)
    downloader.slow_down(t1, time.time(), 5 * 1024)
    time.sleep(0.01)
    download

# Generated at 2022-06-14 15:14:08.540621
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Create a FileDownloader object with a mock for its real_download method
    fd = FileDownloader({}, NoopYoutubeDl(), None, None)
    fd.real_download = lambda *args, **kargs: None
    filename = 'filename'
    # Test download returns true when real_download returns none
    # (FileDownloader.download's return value is the return value of real_download)
    assert fd.download(filename, {})
    # Test what happens if filename exists and nooverwrites is True
    fd.params['nooverwrites'] = True
    fd.report_file_already_downloaded = lambda x: None
    fd._hook_progress = lambda x: None
    fd.to_screen = lambda x: None

# Generated at 2022-06-14 15:14:22.502505
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():

    class FakeTime(object):
        def __init__(self):
            self._time = 0.0
        def time(self):
            return self._time
        def sleep(self, interval):
            self._time += interval

    class FakeParams(object):
        def __init__(self, ratelimit=None):
            self.ratelimit = ratelimit

    def wrapped(fd, params=None, time_module=None):
        old_params = fd.params
        fd.params = params or FakeParams()
        old_time = fd.time
        fd.time = time_module or FakeTime()
        fd.slow_down(start_time=0, now=None, byte_counter=0)
        fd.params = old_params
        fd.time = old_time

    # rate

# Generated at 2022-06-14 15:14:30.363146
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # FileDownloader doesn't depend on YoutubeDL object
    ydl = YoutubeDL(None)
    fd = FileDownloader(ydl, None)
    assert(fd.temp_name('abcdefg') == 'abcdefg.part')
    assert(fd.temp_name('abcdefg.part') == 'abcdefg.part')
    assert(fd.temp_name('abcdefg.ABCDEFG') == 'abcdefg.ABCDEFG.part')
    assert(fd.temp_name('/path/to/file.ext') == '/path/to/file.ext.part')
    assert(fd.temp_name('/path/to/file.ext.part') == '/path/to/file.ext.part')

# Generated at 2022-06-14 15:14:41.080543
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # fails on Travis-CI
    if os.environ.get('TRAVIS') is not None:
        return
    # fails on AppVeyor-CI
    if os.environ.get('APPVEYOR') is not None:
        return
    # fails on GitLab-CI
    if os.environ.get('GITLAB_CI') is not None:
        return
    # fails on Windows
    if compat_os_name == 'nt':
        return
    # fails if unable to get last file modification time of the file
    try:
        os.utime(__file__, None)
    except:
        return
    # fails if unable to create a new temporary file

# Generated at 2022-06-14 15:14:53.816543
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # Test FileDownloader.slow_down()
    # Pre-conditions
    fd = FileDownloader(
        params={'ratelimit': 1048576},
        ydl=None,
        progress_hooks=[],
    )

    # Test
    time.sleep(0.01)
    start_time = time.time()
    fd.slow_down(start_time, None, 1048577)
    time.sleep(0.01)
    now = time.time()
    fd.slow_down(start_time, now, 1048577)
    assert now - start_time >= 0.01

    # Test with ratelimit == 0 to check that we don't sleep

# Generated at 2022-06-14 15:15:03.355884
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import datetime

    def _run_test(status, expected_line, **kwargs):
        time.time = time_time
        time.time.return_value = 1458729104.702857

        fd = FileDownloader(None, None)
        fd.to_screen.reset_mock()
        if kwargs.get('is_last_line') is True:
            fd.to_screen.side_effect = [None, ValueError('Stop iteration')]
        else:
            fd.to_screen.side_effect = ValueError('Stop iteration')

# Generated at 2022-06-14 15:15:12.337933
# Unit test for method report_progress of class FileDownloader

# Generated at 2022-06-14 15:15:21.338104
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    """Unit test for method report_progress"""
    print('Testing report_progress...')
    try:
        # Try to import
        import pytest
    except ImportError:
        print('pytest not installed. Skipping test.')
        return

    # Create an instance of class FileDownloader
    fd = FileDownloader()

    # Call report_progress with an invalid status
    # This should raise ValueError
    with pytest.raises(ValueError):
        fd.report_progress({'status': 'invalid status'})

    # This should not raise any exception
    fd.report_progress({'status': 'finished'})

# Generated at 2022-06-14 15:15:29.690909
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # Setup
    downloader = FileDownloader({
        'outtmpl': '%(id)s-%(ext)s',
        'nopart': False,
    })

    # Test
    # temp_name should be id + '.part'
    result = downloader.temp_name('a')
    # The file is not exist
    assert result == 'a.part'

    # Test
    # temp_name should be id if nopart is True
    result = downloader.temp_name('b')
    assert result == 'b'

    # Test
    # temp_name should be id if the file is not regular file
    result = downloader.temp_name('c')
    assert result == 'c'
test_FileDownloader_temp_name()


# Generated at 2022-06-14 15:15:42.540755
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    ydl = YoutubeDL({'verbose': True})
    fd = FileDownloader(ydl, {'ignoreerrors': True})
    fd.to_screen = lambda *args, **kargs: None
    fd.params['verbose'] = True
    fd.report_progress({
        'status': 'finished',
        'filename': 'foo.mp4',
        'total_bytes': 1024 * 1024 * 1024 * 2,
        'elapsed': 300,
    })
    fd.report_destination('foo.mp4')

# Generated at 2022-06-14 15:16:00.472333
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    file_time = time.mktime((2014, 1, 1, 0, 0, 0, 0, 0, -1))

    # Test empty header
    assert FileDownloader.try_utime('test', None) is None

    # Test invalid header
    assert FileDownloader.try_utime('test', 'invalid') is None

    # Test valid header
    assert FileDownloader.try_utime('test', time.ctime(file_time)) == file_time



# Generated at 2022-06-14 15:16:07.958946
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader({})
    
    fd.report_file_already_downloaded('sample_file')
    assert fd.fd.report_file_already_downloaded('sample_file') == True
    
    if os.path.exists('sample_file'):
        os.remove('sample_file')
    else:
        print("The file does not exist")
test_FileDownloader_report_file_already_downloaded()


# Generated at 2022-06-14 15:16:14.281350
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({'ratelimit': 1})
    fd.slow_down(1, 1, 0)
    fd.slow_down(1, 0, 1)

    # Non-unicode
    fd.slow_down(1, 1, 1)
    fd.slow_down(1, 1, 2)

    # Unicode
    fd.slow_down(1, 1, unichr(1))
    fd.slow_down(1, 1, unichr(2))


# Generated at 2022-06-14 15:16:24.954071
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import tempfile

    # Set of parameters to test

# Generated at 2022-06-14 15:16:35.583684
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import unittest.mock as mock
    from .YoutubeDL import YoutubeDL

    class MockFD(FileDownloader):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.methods_called = []

        def slow_down(self, *args, **kwargs):
            self.methods_called.append(('slow_down', args, kwargs))

    fd = MockFD(YoutubeDL())

    def assert_called(called, *args, **kwargs):
        if not called:
            raise AssertionError('%s not called' % called)

# Generated at 2022-06-14 15:16:46.117155
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # We will override the sleep method in order to spy on it
    fd = FileDownloader({
        'sleep_interval': 1,
        'max_sleep_interval': 5,
    })

    sleep_spy = {
        'calls': 0,
        'args': [],
    }

    def sleep(time):
        sleep_spy['calls'] += 1
        sleep_spy['args'].append(time)

    fd.sleep = sleep

    # Initialize download rates
    block_size = 0
    elapsed_time = 0.0
    byte_counter = 0
    start_time = time.time() - 1

    # Test with a low download rate and retries being infinite
    fd.params['retries'] = float('inf')
    rate_limit = 100
    fd.params

# Generated at 2022-06-14 15:16:58.190544
# Unit test for method best_block_size of class FileDownloader

# Generated at 2022-06-14 15:17:07.119827
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    fd = FileDownloader({'nopart': True, 'no_mtime': True})
    fd.report_destination = lambda *args: None
    fd.report_progress = lambda *args: None
    fd.report_error = lambda *args: None
    fd.report_warning = lambda *args: None
    fd.to_screen = lambda *args, **kargs: None

    # Test writing to stdout

# Generated at 2022-06-14 15:17:19.256823
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    def _temp_name_test(
            initial_name,
            nopart,
            expected_output,
            noprogress=False,
            params=None):
        fd = FileDownloader({
            'nopart': nopart,
            'noprogress': noprogress,
        })
        if params is not None and isinstance(params, dict):
            fd.params.update(params)
        temp_name = fd.temp_name(initial_name)
        assert_equals(temp_name, expected_output)

    yield _temp_name_test, 'example1.flv', False, 'example1.flv.part'
    yield _temp_name_test, 'example2.flv', True, 'example2.flv'
    yield _temp_name_test