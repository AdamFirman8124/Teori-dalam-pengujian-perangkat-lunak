

# Generated at 2022-06-14 15:08:06.561040
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class FileDownloaderSubclass(FileDownloader):
        def __init__(self):
            self.sleep_count = 0
            FileDownloader.__init__(self, ydl=None, params={'ratelimit': 2})

        def to_screen(self, *args, **kargs):
            pass

        def to_stderr(self, *args, **kargs):
            pass

        def to_console_title(self, *args, **kargs):
            pass

        def trouble(self, *args, **kargs):
            pass

        def report_warning(self, *args, **kargs):
            pass

        def report_error(self, *args, **kargs):
            pass

        def slow_down(self, start_time, now, byte_counter):
            """Override just for unit testing"""

# Generated at 2022-06-14 15:08:16.131633
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    return (re.sub(' +', ' ', """
    >>> fd = FileDownloader(None, params={})
    >>> fd.try_utime('test.mp3', None)

    >>> import os
    >>> open('test.mp3', 'w').write('test')
    4
    >>> import time
    >>> time.sleep(1)
    >>> os.utime('test.mp3', (time.time(), time.time() - 100))

    >>> fd.try_utime('test.mp3', 'now')
    >>> import os.path
    >>> print('%d' % int(os.path.getmtime('test.mp3')))
    >>>
    """ + ' ' + str(int(time.time())))).split('\n')[1:-1]


# Generated at 2022-06-14 15:08:23.894401
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Test setup

    # Create a dictionary containing the status
    s = {
        'status' : 'downloading',
        'eta' : 1234,
        'total_bytes' : 1234567,
        'downloaded_bytes' : 123456,
        'speed' : 123,
        'elapsed' : 2,
    }

    # Instantiate a FileDownloader
    f = FileDownloader({})

    # Test report_progress
    assert (f.report_progress(s))

if __name__ == '__main__':
    raise Exception('This file is not meant to be run.')

# Generated at 2022-06-14 15:08:31.523969
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    downloader = FileDownloader({})
    #assertEqual(downloader.undo_temp_name("/tmp/a.part"), "/tmp/a")
    assert(downloader.undo_temp_name("/tmp/a.part") == "/tmp/a")
    #assertEqual(downloader.undo_temp_name("C:\\a.part"), "C:\\a")
    #assertEqual(downloader.undo_temp_name("/tmp/a"), "/tmp/a")
    return 0


# Generated at 2022-06-14 15:08:38.109341
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader({})
    fd.params['nopart'] = True
    assert fd.temp_name('a.b') == 'a.b'
    assert fd.temp_name('a') == 'a'
    assert fd.temp_name('.b') == '.b'
    assert fd.temp_name('a/b') == 'a/b'
    fd.params['nopart'] = False
    assert fd.temp_name('a.b') == 'a.b.part'
    assert fd.temp_name('a') == 'a.part'
    assert fd.temp_name('.b') == '.b.part'
    assert fd.temp_name('a/b') == 'a/b.part'

# Generated at 2022-06-14 15:08:47.690380
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    tp = Test_Progress()
    FileDownloader._report_progress_status = tp._report_progress_status
    # Test edge cases
    tp.start()
    FileDownloader.report_progress({'status': 'finished'})
    FileDownloader.report_progress({'status': 'finished',
                                    'total_bytes': 10})
    FileDownloader.report_progress({'status': 'downloading',
                                    'speed': 10})
    tp.check(
        'Unknown % of Unknown speed ETA Unknown ETA\n'
        'Unknown % of Unknown speed ETA Unknown ETA\n'
        'Unknown % of 10.0b/s ETA Unknown ETA\n')
    tp.stop()
    # Test reports
    tp.start()

# Generated at 2022-06-14 15:08:51.747745
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    fd = FileDownloader()
    fd.calc_speed(0,10,100) == 10

    fd.calc_speed(0,-10,100) == None

    fd.calc_speed(0,10,0) == None

# Generated at 2022-06-14 15:09:01.554682
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    """Tests for FileDownloader.best_block_size()."""

    assert FileDownloader.best_block_size(1.3, 10) == 10
    assert FileDownloader.best_block_size(0.0, 10) == 4194304
    assert FileDownloader.best_block_size(0.5, 1) == 2
    assert FileDownloader.best_block_size(0.5, 10) == 6
    assert FileDownloader.best_block_size(1.0, 1) == 1
    assert FileDownloader.best_block_size(1.0, 10) == 5
    assert FileDownloader.best_block_size(2.0, 1) == 1
    assert FileDownloader.best_block_size(2.0, 10) == 2
    assert FileDownloader.best_block_size

# Generated at 2022-06-14 15:09:07.263597
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    fd = FileDownloader(YoutubeDL(), 'http://foo.bar/video.mp4', params={})
    now = time.time()
    assert fd.calc_speed(now, now, 0) == None
    assert fd.calc_speed(now, now+1, 10) == 10.0


# Generated at 2022-06-14 15:09:08.766907
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    assert(FileDownloader.download('') == false)

# Generated at 2022-06-14 15:09:44.800142
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    """FileDownloader.slow_down: Tests for the rate limit of the download."""

    def _mock_time_sleep_func(n):
        _mock_time_sleep_func.n = n
        return _mock_time_sleep_func.retval

    _mock_time_sleep_func.n = None

    class MockFD(FileDownloader):
        def __init__(self, params):
            FileDownloader.__init__(self, params)
            self.rate_limit = self.params.get('ratelimit')

    fd = MockFD({'ratelimit': 4})
    rate_limit = float(fd.rate_limit)

    _mock_time_sleep_func.retval = 0

    fd.slow_down(0, 0, 0)  # No effect when byte_counter

# Generated at 2022-06-14 15:09:54.534623
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    """$Id: FileDownloader.py 2578 2012-05-15 10:10:54Z valtron $"""
    get_unit_entry = lambda str: FileDownloader.parse_bytes(str)

    assert 981 == get_unit_entry('981')
    assert 981 == get_unit_entry('0x3d5')
    assert 981 == get_unit_entry('0X3D5')
    assert 981 == get_unit_entry('0xd5')
    assert 981 == get_unit_entry('0XD5')
    assert 981 == get_unit_entry('0b11010101')
    assert 981 == get_unit_entry('0B11010101')
    assert 981 == get_unit_entry('0o1625')
    assert 981 == get_unit_entry

# Generated at 2022-06-14 15:10:06.227801
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    dld = FileDownloader({})
    def _os_utime(f, t):
        assert(f == 'a')
        assert(t[1] == 123)
        return
    dld.try_utime('a', '123')
    dld.try_utime(None, '123')
    dld.try_utime('a', None)
    dld.try_utime('a', 'bla')
    dld.try_utime('a', '123')
    orig_utime = os.utime
    try:
        os.utime = _os_utime
        dld.try_utime('a', '123')
    finally:
        os.utime = orig_utime


if __name__ == '__main__':
    test_FileDownloader_try_

# Generated at 2022-06-14 15:10:07.641201
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    assert FileDownloader.download("a.txt", "b.txt") is False

# Generated at 2022-06-14 15:10:15.946585
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert FileDownloader.parse_bytes('2M') == 2*1024*1024
    assert FileDownloader.parse_bytes('12B') == 12
    assert FileDownloader.parse_bytes('5k') == 5*1024
    assert FileDownloader.parse_bytes('22') == 22
    assert FileDownloader.parse_bytes('2G') == 2*1024*1024*1024
    assert FileDownloader.parse_bytes('') is None
    assert FileDownloader.parse_bytes('foo') is None



# Generated at 2022-06-14 15:10:28.264876
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    class TestFD(FileDownloader):
        # Override real_download to avoid using an actual download process
        def real_download(self, filename, info):
            return True

    # This test uses a dummy subclass of FileDownloader because it is not
    # possible to test report_progress directly in FileDownloader due to its
    # use of to_screen.

    # Try with no progress
    fd = TestFD('', {})
    fd.params['noprogress'] = True
    fd.report_progress({'status': 'finished'})
    assert fd.to_screen_calls == []

    # Try with progress
    fd = TestFD('', {})
    fd.report_progress({'status': 'finished'})

# Generated at 2022-06-14 15:10:33.892958
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    downloader = FileDownloader({})
    assert downloader.calc_speed(10, 20, 10) is None
    assert downloader.calc_speed(0, 0, 0) is None
    assert downloader.calc_speed(10, 20, 0) == 0
    assert downloader.calc_speed(10, 20, 5) == 0.5



# Generated at 2022-06-14 15:10:46.047342
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class FakeFileDownloader(FileDownloader):
        def report_progress(self, s):
            super(FakeFileDownloader, self).report_progress(s)
            self.reported_status = s

    print('Testing report_progress status=finished')
    fd = FakeFileDownloader({'noprogress': False})
    fd.report_progress({'status': 'finished', 'total_bytes': 100, 'elapsed': 12.34})

    download_elapsed_str = fd.format_seconds(12.34)

# Generated at 2022-06-14 15:10:48.915258
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    ret = FileDownloader.download(yt_url='https://youtube.com/watch?v=x0p4Og5zV4U')
    assert ret == 0
    ret = FileDownloader.download(yt_url='https://youtube.com/watch?v=XXXX')
    assert ret < 0

# Generated at 2022-06-14 15:10:54.202339
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    st = time.time()
    time.sleep(1)
    bs = FileDownloader.best_block_size(time.time() - st, 1024)
    if bs < 512:
        raise ValueError('FileDownloader.best_block_size returned %d' % bs)
    if bs > 2048:
        raise ValueError('FileDownloader.best_block_size returned %d' % bs)


if __name__ == '__main__':
    test_FileDownloader_best_block_size()

# Generated at 2022-06-14 15:11:33.855016
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    msg="[download] %s has already been downloaded"% filename
    target_part=FileDownloader()
    target_part.report_file_already_downloaded(filename)
    assert msg==target_part.msg_template



# Generated at 2022-06-14 15:11:46.531488
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Set up
    fd = FileDownloader(None)

    # Test
    # Testcase 1: status is 'finished'
    # Expected: '[download] 100% of 1 at 2/s ETA 3'
    fd.report_progress({
        'status': 'finished',
        'total_bytes': 1,
        'downloaded_bytes': 1,
        'speed': 2,
        'eta': 3
    })
    # Testcase 1: status is 'downloading', total_bytes and downloaded_bytes is given
    # Expected: '[download] 50% of 1 at 2/s ETA 3'

# Generated at 2022-06-14 15:11:59.201924
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    params = config.get_default_copy()

    youtubedl_path = config.get_executable()
    if not youtubedl_path:
        print('%r is not installed, skipping test' % config.YOUTUBE_DL_BINARY)
        return

    fd = FileDownloader(params, FileDownloader._FakeYDL(), None)
    start = time.time()
    fd.slow_down(start, start + 0.1, 1 * 1024 * 1024)
    assert time.time() - start < 0.1
    fd.slow_down(start, start + 0.1, 5 * 1024 * 1024)
    assert 0.1 - 0.01 < time.time() - start < 0.1


test_FileDownloader_slow_down()

# Generated at 2022-06-14 15:12:01.135293
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Not much to test here
    fd = FileDownloader({})
    fd.report_progress({})



# Generated at 2022-06-14 15:12:13.819893
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(params={
        'continuedl': False,
        'noprogress': False,
        'nopart': False,
        'ratelimit': 1000000,
    })

    # Set start_time to 1 second in the past
    now = time.time()
    start_time = now - 1

    # We don't sleep if the elapsed time is less than 0.001 seconds, nearly
    # impossible to test, so we just assume that works correctly.

    # We won't sleep if the rate is under the limit
    speed = fd.calc_speed(start_time, now, 1)
    assert speed == 1.0
    fd.slow_down(start_time, now, 1)

    # We will sleep if the rate is over the limit

# Generated at 2022-06-14 15:12:25.635811
# Unit test for method report_file_already_downloaded of class FileDownloader

# Generated at 2022-06-14 15:12:35.220099
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def testreport(fd, download_status):
        return fd._test_report_progress(download_status)

    def test(value, expected):
        fd = FileDownloader({})
        assert expected == testreport(fd, value)

    test({
        'total_bytes': 10,
        'downloaded_bytes': 5,
        'speed': 1,
        'eta': 10,
        'status': 'downloading'
    }, '[download]   5% of 10 at 1 Unknown speed ETA 10 seconds')

    test({
        'downloaded_bytes': 5,
        'elapsed': 5,
        'speed': 1,
        'status': 'downloading'
    }, '[download]   5 at 1 Unknown speed')


# Generated at 2022-06-14 15:12:47.747151
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def _test_slow_down(downloader, bytes, rate_limit, sleep_time):
        start_time = time.time()
        downloader.slow_down(start_time, None, bytes)
        stop_time = time.time()
        assert stop_time - start_time >= sleep_time
        assert stop_time - start_time - sleep_time < 0.01
        # If we take too much time to execute the test the following assertion
        # may not be valid
        # assert downloader.calc_speed(start_time, stop_time, bytes) == rate_limit

    def _test_slow_down_limit(downloader, sleep_time):
        _test_slow_down(downloader, 524288, 524288, sleep_time)

# Generated at 2022-06-14 15:12:54.432747
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader(YoutubeDL(), {})
    # Test normal case
    fd.report_progress(
        {
            'status': 'downloading',
            'filename': 'foo.flv',
            'total_bytes': 100,
            'downloaded_bytes': 20,
            'total_bytes_estimate': 100,
            'elapsed': 10,
            'eta': 10,
            'speed': 2,
        })
    assert sys.stdout.getvalue() == '[download]   2.0% of 100 bytes at 20.0 bytes/s ETA 00:00'
    sys.stdout.truncate(0)
    # Test rounding

# Generated at 2022-06-14 15:13:07.892712
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    import os
    if os.path.exists('tempname'):
        os.unlink('tempname')
    if os.path.exists('tempname.part'):
        os.unlink('tempname.part')
    fd = FileDownloader({})
    part = fd.temp_name('tempname')
    assert part == 'tempname.part'
    assert not os.path.exists('tempname.part')
    part = fd.temp_name('tempname')
    assert part == 'tempname.part'
    assert not os.path.exists('tempname.part')
    part = fd.temp_name('tempname.part')
    assert part == 'tempname.part'
    assert not os.path.exists('tempname.part')
    part = fd.temp_

# Generated at 2022-06-14 15:13:58.915829
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    def data(speed, eta, min_bed_down, max_bed_down):
        return (speed, eta, min_bed_down, max_bed_down)


# Generated at 2022-06-14 15:14:04.542078
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    assert FileDownloader.undo_temp_name('filename') == 'filename'
    assert FileDownloader.undo_temp_name('filename.part') == 'filename'
    assert FileDownloader.undo_temp_name('filename.part.part') == 'filename.part'
    assert FileDownloader.undo_temp_name('') == ''
    assert FileDownloader.undo_temp_name('.part') == ''


# Generated at 2022-06-14 15:14:08.345210
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    return

    assert FileDownloader.undo_temp_name('foo') == 'foo'
    assert FileDownloader.undo_temp_name('foo.part') == 'foo'
    assert FileDownloader.undo_temp_name('foo.part.part') == 'foo.part'



# Generated at 2022-06-14 15:14:21.875495
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    def mk_FileDownloader(params=None, **kargs):
        if params is None:
            params = {'usenetrc': False}
        return FileDownloader(params, **kargs)
    def mk_urlopen(head_request, data):
        def urlopen(req):
            class U:
                def getheader(self, header):
                    return {'content-type': 'video/webm'}[header.lower()]
                def read(self):
                    return data
            if req.get_method() == 'HEAD':
                return U()
            else:
                raise AssertionError('Unexpected request for %r' % req.get_full_url())
        return urlopen

# Generated at 2022-06-14 15:14:30.225955
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    class MockInfoDict(dict):
        pass

    f = FileDownloader()

    # Test with no ETA and no total bytes
    s = MockInfoDict()
    s.update([
        ('downloaded_bytes', 1024),
        ('total_bytes', None),
        ('eta', None),
        ('speed', 64)
    ])
    f.to_screen = lambda x: x
    assert f.report_progress(s) is None

    # Test with ETA and no total bytes
    s = MockInfoDict()
    s.update([
        ('downloaded_bytes', 1024),
        ('total_bytes', None),
        ('eta', 60),
        ('speed', 64)
    ])
    assert f.report_progress(s) is None

    # Test "finished" status
    s = MockInfoDict

# Generated at 2022-06-14 15:14:41.041082
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import time
    def timeconvert(timestr):
        return None
    assert None == try_utime(None, None)
    assert None == try_utime(None, "1")
    assert None == try_utime("1", None)

    import os
    assert None == try_utime(os.path.join(os.getcwd(), '1.txt'), "1")
    assert None == try_utime(os.path.join(os.getcwd(), '1.txt') + '.part', "1")

    with open(os.path.join(os.getcwd(), '1.txt'), 'w') as f:
        now = time.time()
        assert None != try_utime(os.path.join(os.getcwd(), '1.txt'), str(now))

# Generated at 2022-06-14 15:14:53.769116
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class FakeParams(object):
        def __getitem__(self, key):
            if key == 'noprogress':
                return False
            return None

    class FakeYoutubeDL(object):
        params = FakeParams()

        def to_screen(self, *args, **kargs):
            pass

    ydl = FakeYoutubeDL()

    class FakeFD(object):
        def __init__(self):
            self._times = [0.0] * 10
            self._bytes = [0] * 10
            self._sleeped = 0.0

        def __call__(self):
            self._times[:-1] = self._times[1:]
            self._times[-1] = time.time()
            self._bytes[:-1] = self._bytes[1:]

# Generated at 2022-06-14 15:14:59.097518
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    df = FileDownloader({'nopart':True})
    assert df.temp_name('foo.mp4') == 'foo.mp4'
    df.params['nopart'] = False
    assert df.temp_name('foo.mp4') == 'foo.mp4.part'

if __name__ == '__main__':
    test_FileDownloader_temp_name()

# Generated at 2022-06-14 15:15:09.289310
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = FileDownloader(None, None)
    assert fd.best_block_size(20, 400) == 100
    assert fd.best_block_size(50, 1000) == 200
    assert fd.best_block_size(4, 10) == 2
    assert fd.best_block_size(4, 8) == 2
    assert fd.best_block_size(4, 5) == 1
    assert fd.best_block_size(100, 1) == 1
    assert fd.best_block_size(1000, 10) == 100
    assert fd.best_block_size(1, 2) == 1
    assert fd.best_block_size(5, 10) == 2
    assert fd.best_block_size(100, 2000) == 100
    assert fd.best

# Generated at 2022-06-14 15:15:16.616756
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    fd = FileDownloader({})
    assert fd.calc_speed(10000, 10010, 750000) == 74900
    assert fd.calc_speed(10000, 10010, 0) is None
    assert fd.calc_speed(10000, 10010, None) is None
    assert fd.calc_speed(10000, 9990, 750000) is None

