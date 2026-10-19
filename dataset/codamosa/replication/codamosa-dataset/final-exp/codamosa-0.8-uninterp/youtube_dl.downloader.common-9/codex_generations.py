

# Generated at 2022-06-14 15:08:17.936051
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    from .YoutubeDL import YoutubeDL
    from .extractor import gen_extractors

    url = 'http://www.youtube.com/watch?v=JQbj7YpEX1U'
    fd = FileDownloader(YoutubeDL({'logger': object()}), url)
    extraction_gen = gen_extractors(fd)
    gen = fd._do_download(extraction_gen, {})
    info = next(gen)
    for p in gen:
        if not p:
            break
    assert info['status'] == 'finished'


# Generated at 2022-06-14 15:08:23.266433
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from io import StringIO
    f = StringIO()
    d = FileDownloader(FakeYDL({'verbose': True}))
    d._report_progress_status = lambda *args, **kargs: print(*args, **kargs, file=f)
    d.report_progress({'status': 'finished'})
    s = f.getvalue()
    assert_in('100%', s)
    assert_in('estimate', s)
    assert_in('ETA', s)

    f.truncate(0)
    f.seek(0)

    d.report_progress({'status': 'downloading', 'total_bytes': 300, 'total_bytes_estimate': 200, 'downloaded_bytes': 30, 'elapsed': 10, 'eta': 5, 'speed': 25})
    s = f.get

# Generated at 2022-06-14 15:08:32.879039
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = FileDownloader({})
    assert fd.best_block_size(1.0, 1000) == 512000
    assert fd.best_block_size(1.0, 500) == 250000
    assert fd.best_block_size(1.0, 1024 * 1024 * 1024 + 1) == 4194304
    assert fd.best_block_size(1.0, 0) == 1024
    assert fd.best_block_size(1.0, 1) == 512

    assert fd.best_block_size(1.0, 1024 * 1024 + 1) == 524288
    assert fd.best_block_size(1.0, 1024 * 1024) == 524288
    assert fd.best_block_size(1.0, 1024 * 1024 - 1) == 524288

# Generated at 2022-06-14 15:08:37.106052
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    assert(FileDownloader.format_retries(float('inf')) == 'inf')
    assert(FileDownloader.format_retries(0) == '0')
    assert(FileDownloader.format_retries(1) == '1')
    assert(FileDownloader.format_retries(5) == '5')
    assert(FileDownloader.format_retries(10.0) == '10')
    assert(FileDownloader.format_retries(10.5) == '10')



# Generated at 2022-06-14 15:08:42.549436
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert FileDownloader.parse_bytes('') is None
    assert FileDownloader.parse_bytes('0') == 0
    assert FileDownloader.parse_bytes('1') == 1
    assert FileDownloader.parse_bytes('1024') == 1024
    assert FileDownloader.parse_bytes('1.5k') == 1024 + 512
    assert FileDownloader.parse_bytes('2.5m') == 2 * 1024**2 + 512**2
    assert FileDownloader.parse_bytes('3.5g') == 3 * 1024**3 + 512**3
    assert FileDownloader.parse_bytes('4.5t') == 4 * 1024**4 + 512**4
    assert FileDownloader.parse_bytes('5.5p') == 5 * 1024**5 + 512**5
    assert FileDownloader.parse_bytes('6.5e')

# Generated at 2022-06-14 15:08:50.712433
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from io import BytesIO
    # get it from http://ipv4.download.thinkbroadband.com/5MB.zip
    test_video_url='http://ipv4.download.thinkbroadband.com/5MB.zip'
    test_video_name='5MB.zip'
    
    
    def test_hook(d):
        if d['status'] == 'downloading':
            speed = d['speed']
            #print('speed: ', speed)
            #print('downloaded: ', d['downloaded_bytes'])
            #print('total: ', d['total_bytes'])
            #print("ETA: ", d['eta'])
            #print("elapsed: ", d['elapsed'])
            #print("eta_seconds: ", d['eta_seconds'])
            #print("percent: ",

# Generated at 2022-06-14 15:08:56.346803
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    from .compat import compat_kwargv

    def download(self, filename, info_dict):
        assert filename == '/dev/null'
        assert info_dict['__title'] == 'video'
        return True

    d = compat_kwargv(FileDownloader)
    d.real_download = download
    d.download('/dev/null', {'__title': 'video'})



# Generated at 2022-06-14 15:09:08.863571
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    def test(expected, elapsed, bytes):
        assert expected == FileDownloader(None).best_block_size(elapsed, bytes)
    yield test, 1, 0, 0
    yield test, 1, 0, 1
    yield test, 1024, 0, 1024
    yield test, 1023, 0, 1023
    yield test, 1, 0, 1023
    yield test, 1024, 0, 1025
    yield test, 1023, 0, 1026
    yield test, 1, 0, 2047
    yield test, 1024, 0, 2048
    yield test, 1023, 0, 2049
    yield test, 1, 0, 2049
    yield test, 1024, 0, 2051
    yield test, 1023, 0, 2050
    yield test, 1, 0, 3071
    yield test, 1024, 0, 3072
    yield

# Generated at 2022-06-14 15:09:20.810959
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    """Test method download of class FileDownloader."""

    from youtube_dl.extractor.youtube import YoutubeIE
    from youtube_dl.extractor.soundcloud import SoundcloudIE
    from youtube_dl.extractor.xhamster import XHamsterIE

    downloader = FileDownloader({})
    downloader.add_info_extractor(YoutubeIE())
    downloader.add_info_extractor(SoundcloudIE())
    downloader.add_info_extractor(XHamsterIE())

    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    info = downloader.extract_info(url)

    assert downloader.download(info)

    url = 'https://soundcloud.com/wavemusic/sets/deep-house-2014'
    info = downloader.ext

# Generated at 2022-06-14 15:09:28.989164
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    name = 'test'
    outtmpl = name + '-%(title)s.%(ext)s'
    ydl = FileDownloader({}, {'outtmpl': outtmpl})
    ydl.to_screen = lambda info: None
    ydl.params['noprogress'] = False
    ydl.report_progress = lambda s: None
    fd = FileDownloader({}, {'outtmpl': outtmpl})
    fd._report_progress_status = lambda msg: None
    fd.to_screen = lambda *args, **kargs: None
    fd.to_console_title = lambda *args, **kargs: None
    fd.report_destination(outtmpl % {'title': 'foo', 'ext': 'bar'})

# Generated at 2022-06-14 15:09:43.965554
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader({})

    # invalid format
    assert fd.try_utime('foobar', 'invalid') is None

    # date in the future
    assert fd.try_utime('foobar', str(int(time.time() + 1))) is None

    # date in the past
    assert fd.try_utime('foobar', str(int(time.time() - 1))) is not None


if __name__ == '__main__':
    test_FileDownloader_try_utime()

# Generated at 2022-06-14 15:09:53.124693
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class FakeFD(object):

        def __init__(self):
            self.sleep_was_called = False
            self.sleep_call_args = None

        def slow_down(self, start_time, now, byte_counter):
            self.sleep_was_called = True
            self.sleep_call_args = (start_time, now, byte_counter)

    fake_fd = FakeFD()
    fd = FileDownloader({})
    fd.fd = fake_fd
    fd.slow_down(1, 2, 3)
    assert fake_fd.sleep_was_called
    assert fake_fd.sleep_call_args == (1, 2, 3)


# Generated at 2022-06-14 15:10:04.845435
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    import random
    import time
    # random.seed(0) # uncomment to test with a fixed random seed
    block_sizes = []
    last_total_bytes = None
    last_start_time = time.time()
    last_end_time = time.time()
    fd = FileDownloader({})
    fd.add_progress_hook(lambda s: None)  # disable UI updates
    for _ in range(10000):
        # Simulate that a download has been running for 1-2 seconds
        last_start_time = (last_start_time + last_end_time) / 2 - random.uniform(0.5, 1.5)
        last_end_time = time.time()
        num_bytes_downloaded = random.randint(100000, 1000000)

# Generated at 2022-06-14 15:10:13.143501
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import random
    import time
    import tempfile
    import shutil
    from .YoutubeDL import YoutubeDL

    class TestFileDownloader(FileDownloader):
        def __init__(self):
            self.ydl = YoutubeDL()
            self.ydl.params['ratelimit'] = 20
            self.max_sleep_time_secs = 0.0

        def slow_down(self, start_time, now, byte_counter):
            FileDownloader.slow_down(self, start_time, now, byte_counter)
            if now is None:
                now = time.time()
            sleep_time = now - start_time - byte_counter / 20.0
            if sleep_time > self.max_sleep_time_secs:
                self.max_sleep_time_secs = sleep_time

   

# Generated at 2022-06-14 15:10:25.617087
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(FakeYDL())
    assert fd.temp_name('abc.mp4') == 'abc.mp4.part'
    assert fd.temp_name('/home/user/video.mp4') == '/home/user/video.mp4.part'
    assert fd.temp_name('\\home\\user\\video.mp4') == '\\home\\user\\video.mp4.part'
    assert fd.temp_name('C:\\Users\\user\\video.mp4') == 'C:\\Users\\user\\video.mp4.part'
    assert fd.temp_name('/tmp/video.mp4') == '/tmp/video.mp4.part'
    assert fd.temp_name('/tmp/video') == '/tmp/video.part'

# Generated at 2022-06-14 15:10:26.346742
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    pass

# Generated at 2022-06-14 15:10:37.155939
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    """Function to check if the class FileDownloader and its method report_progress work properly"""

# Generated at 2022-06-14 15:10:49.561748
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    from io import BytesIO
    from collections import OrderedDict
    ydl_opts = {
        'logger': MockLogger(),
        'progress_hooks': [],
        'nooverwrites': True,
        'continuedl': True,
        'nopart': True
    }

# Generated at 2022-06-14 15:10:59.554895
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(None, {})

    fd.params['nopart'] = True
    assert fd.temp_name('/tmp/xx') == '/tmp/xx'
    assert fd.temp_name('/tmp/xx.part') == '/tmp/xx'
    assert fd.temp_name('/tmp/xx.xx') == '/tmp/xx.xx'

    fd.params['nopart'] = False
    assert fd.temp_name('/tmp/xx') == '/tmp/xx.part'
    assert fd.temp_name('/tmp/xx.part') == '/tmp/xx.part'
    assert fd.temp_name('/tmp/xx.xx') == '/tmp/xx.xx'
    assert fd.temp_name('-') == '-'


# Generated at 2022-06-14 15:11:06.651825
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import time
    # First test with a rate_limit of None
    fd = FileDownloader(params={}, downloader=None)
    fd.params['ratelimit'] = None
    start = time.time()
    fd.slow_down(start, None, 0)
    etime = time.time() - start
    assert (etime < 0.001)
    # Second test with a fast rate_limit
    fd.params['ratelimit'] = 4000000
    start = time.time()
    fd.slow_down(start, None, 0)
    etime = time.time() - start
    assert (etime < 0.001)
    # Third test with a slow rate_limit
    fd.params['ratelimit'] = 1000
    start = time.time()

# Generated at 2022-06-14 15:11:23.010676
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def _write_file_content(fp, size):
        fp.write('%032x' % size)
        fp.flush()

    def _get_file_size(fp):
        p = fp.tell()
        fp.seek(0, 2)
        s = fp.tell()
        fp.seek(p, 0)
        return s

    def _get_stat_size(stat):
        return stat.st_size

    def _test_size(size_fn, progress_hooks):
        with tempfile.NamedTemporaryFile(suffix='.tmp') as f:
            _write_file_content(f, size_fn(f))

            for total_size in (10, 10000, 100000, 1000000):
                f.seek(0)


# Generated at 2022-06-14 15:11:31.561715
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    import pytest
    fd = FileDownloader(YoutubeDL(), {})
    assert fd.best_block_size(0, 0) == 1
    assert fd.best_block_size(0, 1) == 1
    assert fd.best_block_size(0, 2) == 2
    assert fd.best_block_size(0, 512) == 512
    assert fd.best_block_size(0, 513) == 1024
    assert fd.best_block_size(0, 1024) == 1024
    assert fd.best_block_size(0, 1025) == 2048
    assert fd.best_block_size(0, 1048576) == 4194304
    assert fd.best_block_size(0, 1048577) == 4194304
    assert fd.best_

# Generated at 2022-06-14 15:11:43.888582
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Create a FileDownloader instance
    fd = FileDownloader({}, {})
    # Use _do_download method and other functions to do the following tests
    # Test the download method when the download failed and raise an exception
    fd.report_error = lambda *args, **kargs: None
    fd._make_cmd = lambda *args, **kargs: ['echo']
    fd._run_cmd = lambda args, **kargs: (1, None, None)
    fd._do_download = lambda meta, location, filename: False
    assert fd.download('a.mp4', {'id': 'abc'}) == False

    # Test the download method when the file exists and should not overwrite
    fd.report_error = lambda *args, **kargs: None

# Generated at 2022-06-14 15:11:50.344475
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    """
    Check if method report_file_already_downloaded works correctly
    """
    x = FileDownloader({'outtmpl': '%(id)s%(ext)s', 'nooverwrites': True}, FakeYDL())
    assert x.report_file_already_downloaded('/tmp/foo/bar') is None
    y = FileDownloader({'outtmpl': '%(title)s-%(id)s%(ext)s', 'nooverwrites': True}, FakeYDL())
    assert y.report_file_already_downloaded('/tmp/foo/bar') is None



# Generated at 2022-06-14 15:12:02.138787
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader({'ratelimit': '5KiB'})
    start_time = time.time()
    fd.slow_down(start_time, start_time, 0)
    assert time.time() - start_time < 0.001  # No sleep
    fd.slow_down(start_time, start_time, 1024)
    assert time.time() - start_time < 0.001  # No sleep
    fd.slow_down(start_time, start_time, 5120)
    assert time.time() - start_time < 0.001  # No sleep
    fd.slow_down(start_time, start_time, 5.1 * 1024)
    assert 0.001 < time.time() - start_time < 0.002  # Sleep just enough


# Generated at 2022-06-14 15:12:15.052640
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    import os
    import tempfile
    from .common import FileDownloader
    from .common import limit_length
    from .compat import compat_httplib
    from .compat import compat_urllib_request
    from .compat import compat_urllib_response

    class Info(object):
        pass

    info = Info()

    block_size = 10240
    content_length = block_size * 10

    class Resp(object):
        def __init__(self):
            self.status = 200

        def info(self):
            i = compat_httplib.HTTPMessage(compat_io.BytesIO())
            i.addheader('Content-Length', str(content_length))
            return i

    with tempfile.NamedTemporaryFile() as f:
        tmpfilename = f.name


# Generated at 2022-06-14 15:12:23.117665
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    from .test.test_test_utils import TestDownloadUtils

    fd = FileDownloader(TestDownloadUtils())
    assert fd.calc_speed(0, 0, 0) == None
    assert fd.calc_speed(0, 1, 0) == None
    assert fd.calc_speed(0, 100, 0) == None
    assert fd.calc_speed(0, 0, 1) == None
    assert fd.calc_speed(0, 0, 100) == None
    assert fd.calc_speed(0, 1, 1) == 1.0
    assert fd.calc_speed(0, 1, 100) == 100.0
    assert fd.calc_speed(0, 100, 1) == 0.01

# Generated at 2022-06-14 15:12:33.762335
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    t = time.time()

    fd = FileDownloader()
    fd.report_progress({'status': 'finished'})
    fd.report_progress({'status': 'downloading', 'total_bytes': 1000, 'downloaded_bytes': 500, 'elapsed': t - 100})
    fd.report_progress({'status': 'downloading', 'total_bytes': None, 'downloaded_bytes': 700, 'elapsed': t - 100, 'total_bytes_estimate': 1000})
    fd.report_progress({'status': 'downloading', 'total_bytes': None, 'downloaded_bytes': None, 'elapsed': t - 100,
        'total_bytes_estimate': 1000, 'speed': 50, 'eta': 10})

# Generated at 2022-06-14 15:12:46.428468
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    """ Simple test for the FileDownloader download method (unit test). """
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.close()

    info_dict = {
        'id': '12345',
        'title': 'test_video',
        'url': 'http://test_url/test.mp4',
        'ext': 'mp4',
        'http_headers': {'Cookie': 'foo=bar'},
        'username': 'testuser',
        'password': 'testpass',
    }

    # Test download with a single URL
    class mockFileDownloader(FileDownloader):
        def __init__(self, *args, **kwargs):
            FileDownloader.__init__(self, *args, **kwargs)


# Generated at 2022-06-14 15:12:56.492519
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({})
    # Method doesn't write anything in the normal case
    stderr_patcher = mock.patch('sys.stderr')
    stderr_patcher.start()
    fd.report_progress({})
    fd.report_progress({'status': 'finished'})
    assert (sys.stderr.write.call_count == 0)
    stderr_patcher.stop()

    # Test printing progress
    stdout_patcher = mock.patch('sys.stdout')
    stdout_mock = stdout_patcher.start()
    fd.params['noprogress'] = False
    fd.report_progress({'status': 'downloading',
                        'downloaded_bytes': 1024,
                        'speed': 8024, 'eta': 324})


# Generated at 2022-06-14 15:13:18.616228
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    import tempfile
    ydl = YoutubeDL()
    fd = FileDownloader(ydl, {'outtmpl': '%(ext)s.%(id)s.%(format)s.%(title)s.temp'})

    # Test with existing file
    with tempfile.NamedTemporaryFile() as f:
        assert fd.temp_name(f.name) == f.name + '.part'

    # Test with non existing file (if we ever change the behaviour so that
    # temp_name returns the actual filename in such case, this will fail)
    assert fd.temp_name(tempfile.mktemp()) == 'ext.id.format.title.temp.part'


# Generated at 2022-06-14 15:13:24.530338
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    fd = FileDownloader(YoutubeDL())
    assert fd.format_retries(None) == 'inf'
    assert fd.format_retries(float('inf')) == 'inf'
    assert fd.format_retries(1) == '1'
    assert fd.format_retries(5.5) == '5'


# Generated at 2022-06-14 15:13:30.020244
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader({})

    assert fd.undo_temp_name('blah.part') == 'blah'
    assert fd.undo_temp_name('blah.flv.part') == 'blah.flv'
    assert fd.undo_temp_name('blah') == 'blah'
    assert fd.undo_temp_name('') == ''


# Generated at 2022-06-14 15:13:38.643621
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({})
    fd.report_progress({'status': 'finished', 'elapsed': 100,
                        'total_bytes': 1000,
                        'downloaded_bytes': 1000})
    assert fd._report_progress_prev_line_length is None

    fd = FileDownloader({'verbose': True})
    fd.to_screen = lambda x: None
    fd.report_progress({'status': 'finished', 'elapsed': 0,
                        'total_bytes': 1000,
                        'downloaded_bytes': 1000})
    assert fd._report_progress_prev_line_length is None

if __name__ == "__main__":
    test_FileDownloader_report_progress()


# Generated at 2022-06-14 15:13:48.464724
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    assert FileDownloader.format_percent(0) == '0.0%'
    assert FileDownloader.format_percent(1) == '1.0%'
    assert FileDownloader.format_percent(0.34) == '34.3%'
    assert FileDownloader.format_percent(0.3434523) == '34.3%'
    assert FileDownloader.format_percent(0.3444523) == '34.4%'
    assert FileDownloader.format_percent(0.3446523) == '34.5%'
    assert FileDownloader.format_percent(0.3447523) == '34.5%'
    assert FileDownloader.format_percent(0.3449000) == '34.5%'

# Generated at 2022-06-14 15:13:59.076365
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    dl = FileDownloader({})
    dl.format_percent = lambda x: '%d' % x
    dl.to_screen = lambda x, y=False: sys.stdout.write(x + '\n' if y else x)
    dl.format_eta = lambda x: 'eta%d' % x
    dl.report_progress({'total_bytes': 20, 'status': 'downloading', 'downloaded_bytes': 10})
    assert sys.stdout.getvalue() == '[download] 50% at Unknown speed ETA etaNone\r\x1b[K\n'

    sys.stdout.seek(0)
    sys.stdout.truncate()

# Generated at 2022-06-14 15:14:08.546883
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    dl = FileDownloader(None, {'noprogress': False})
    dl.report_progress({
        'downloaded_bytes': 100,
        'total_bytes': 1000,
        'tmpfilename': 'abc',
        'filename': 'abc',
        'status': 'downloading',
        'eta': None,
        'speed': None
    })
    assert 'Unknown ETA' in dl.last_progess_msg
    assert 'Unknown speed' in dl.last_progess_msg
    dl.report_progress({
        'downloaded_bytes': 100,
        'total_bytes': 1000,
        'tmpfilename': 'abc',
        'filename': 'abc',
        'status': 'downloading',
        'eta': 1,
        'speed': None
    })

# Generated at 2022-06-14 15:14:22.513377
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from youtube_dl.downloader import FileDownloader
    from types import SimpleNamespace

    fd = FileDownloader({})

    s = SimpleNamespace(status='downloading')
    assert not fd._report_progress_prev_line_length
    fd.report_progress(s)

    s.eta = 12.5
    fd.report_progress(s)
    assert not fd._report_progress_prev_line_length

    s.elapsed = 12.5
    s.downloaded_bytes = 1
    s.total_bytes = 1
    s.speed = 100
    fd.report_progress(s)
    assert fd._report_progress_prev_line_length == 19

    s.status = 'finished'
    fd.report_progress(s)
    assert fd._report_progress

# Generated at 2022-06-14 15:14:25.451110
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    fd = FileDownloader({})
    assert fd.calc_speed(100, 200, 5) == 2.5
    assert fd.calc_speed(100, 200, 50) == 5


# Generated at 2022-06-14 15:14:37.801463
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import tempfile
    import os
    import time
    # Test without last-modified
    fd, n = tempfile.mkstemp()
    fd = os.fdopen(fd, 'wb')
    fd.write(b'hi')
    fd.close()
    assert get_filesize(n) == 2
    assert FileDownloader.try_utime(n, None) is None
    assert get_filesize(n) == 2
    os.remove(n)
    # Test with last-modified
    fd, n = tempfile.mkstemp()
    fd = os.fdopen(fd, 'wb')
    fd.write(b'hi')
    fd.close()
    assert get_filesize(n) == 2
    time.sleep(1)
    timestamp = time.time

# Generated at 2022-06-14 15:15:02.107276
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # the method currently uses nested dicts, which is impossible to create
    # with py.test fixtures; hence, we need to use plain functions with
    # fixtures as parameters
    def check_report_progress(progress_hooks, params, s, s_expected):
        fd = FileDownloader({})
        fd._progress_hooks = progress_hooks
        fd.params = params
        fd.report_progress(s)
        assert s_expected == s

    def check_report_progress_noprogress(s, s_expected):
        params = {'noprogress': True}
        check_report_progress([], params, s, s_expected)


# Generated at 2022-06-14 15:15:11.575833
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    d = FileDownloader({}, None)
    assert d.parse_bytes(None) is None
    assert d.parse_bytes('') is None
    assert d.parse_bytes('bytes=-1') is None
    assert d.parse_bytes('bytes=0') == 0
    assert d.parse_bytes('bytes=1') == 1
    assert d.parse_bytes('bytes=10') == 10
    assert d.parse_bytes('bytes=10.1') == 10.1
    assert d.parse_bytes('bytes=10,100') == 10
    assert d.parse_bytes('bytes=10.5') == 10.5
    assert d.parse_bytes('bytes=0-') == 0
    assert d.parse_bytes('bytes=10-') == 10
    assert d.parse_bytes('bytes=-10') == -10

# Generated at 2022-06-14 15:15:19.738601
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    args = [
        (100, 0, 0, None),
        (100, 0, 1, 100 * (1 - 0)),
        (100, 50, 10, 100 * (1 - 50.0 / 10)),
        (100, 0, 10, 100 * (1 - 0 / 10)),
        (100, 99, 10, 100 * (1 - 99.0 / 10)),
    ]
    for total, current, start, expected in args:
        assert expected == FileDownloader.calc_eta(total, current, start)



# Generated at 2022-06-14 15:15:29.208235
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    class Dummy_FileDownloader(FileDownloader):
        def __init__(self, *args, **kwargs):
            self.to_screen_calls = []
            self.to_console_title_calls = []

        def to_screen(self, *args, **kwargs):
            self.to_screen_calls.append((args, kwargs))

        def to_console_title(self, *args, **kwargs):
            self.to_console_title_calls.append((args, kwargs))

    def test_report_progress():
        fd = Dummy_FileDownloader(params={'verbose': True, 'noprogress': False})

# Generated at 2022-06-14 15:15:42.000101
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    dl = FileDownloader(None, params={})
    orig = dl.temp_name('abc')
    assert dl.undo_temp_name(orig) == 'abc'
    assert dl.undo_temp_name(dl.ydl_filename(orig)) == 'abc.ytdl'
    assert dl.undo_temp_name(orig) == 'abc'

    orig = dl.temp_name('/path/to/abc')
    assert dl.undo_temp_name(orig) == '/path/to/abc'
    assert dl.undo_temp_name(orig + '.part') == '/path/to/abc'
    assert dl.undo_temp_name(orig + '.ytdl') == '/path/to/abc'


# Generated at 2022-06-14 15:15:52.274823
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    ydl = YoutubeDL()
    fd = FileDownloader(ydl)

    assert fd.temp_name('file') == 'file.part'
    assert fd.temp_name('/tmp/file') == '/tmp/file.part'
    assert fd.temp_name('file.ext') == 'file.ext.part'

    ydl.params['nopart'] = True
    assert fd.temp_name('file') == 'file'
    assert fd.temp_name('/tmp/file') == '/tmp/file'
    assert fd.temp_name('file.ext') == 'file.ext'

    ydl.params['nopart'] = False
    os.mkdir(encodeFilename('file'))

# Generated at 2022-06-14 15:16:01.559355
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert FileDownloader.parse_bytes("10") == 10
    assert FileDownloader.parse_bytes("1.0") == 1
    assert FileDownloader.parse_bytes("1", "KB") == 1024
    assert FileDownloader.parse_bytes("1.0", "KB") == 1024
    assert FileDownloader.parse_bytes("1", "MB") == 1024**2
    assert FileDownloader.parse_bytes("1.0", "MB") == 1024**2
    assert FileDownloader.parse_bytes("1", "GB") == 1024**3
    assert FileDownloader.parse_bytes("1.0", "GB") == 1024**3
    assert FileDownloader.parse_bytes("1", "TB") == 1024**4
    assert FileDownloader.parse_bytes("1.0", "TB") == 1024**4
    assert File

# Generated at 2022-06-14 15:16:12.426296
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    from youtube_dl.downloader import FileDownloader
    assert FileDownloader.parse_bytes('0') is None
    assert FileDownloader.parse_bytes('b') is None
    assert FileDownloader.parse_bytes('x') is None
    assert FileDownloader.parse_bytes('1.0') is None
    assert FileDownloader.parse_bytes('1b') == 1
    assert FileDownloader.parse_bytes('1B') == 1
    assert FileDownloader.parse_bytes('1.0b') is None
    assert FileDownloader.parse_bytes('1.0B') is None
    assert FileDownloader.parse_bytes('1k') == 1024
    assert FileDownloader.parse_bytes('1K') == 1024
    assert FileDownloader.parse_bytes('1m') == 1024 ** 2

# Generated at 2022-06-14 15:16:24.372112
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    UPPER_CASE = [('3.1k', 3156),
                  ('3.1K', 3156),
                  ('3.1m', 3276200),
                  ('3.1M', 3276200),
                  ('3.1g', 34359738000),
                  ('3.1G', 34359738000)]
    for human, machine in UPPER_CASE:
        assert FileDownloader.parse_bytes(human) == machine

    LOWER_CASE = [('3.1k', 3156),
                  ('3.1K', 3156),
                  ('3.1m', 3276200),
                  ('3.1M', 3276200),
                  ('3.1g', 34359738000),
                  ('3.1G', 34359738000)]

# Generated at 2022-06-14 15:16:35.028768
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    assert FileDownloader.parse_bytes('') is None
    assert FileDownloader.parse_bytes('1') is None
    assert FileDownloader.parse_bytes('x') is None
    assert FileDownloader.parse_bytes('1x') is None
    assert FileDownloader.parse_bytes('0.5k') is None
    assert FileDownloader.parse_bytes('1.5k') == 1536
    assert FileDownloader.parse_bytes('123K') == 123 * 1024
    assert FileDownloader.parse_bytes('123M') == 123 * 1024 * 1024
    assert FileDownloader.parse_bytes('123Ki') == 123 * 1024
    assert FileDownloader.parse_bytes('123Mi') == 123 * 1024 * 1024
    assert FileDownloader.parse_bytes('123KB') == 123 * 1000

# Generated at 2022-06-14 15:17:01.612793
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from collections import namedtuple

# Generated at 2022-06-14 15:17:09.369344
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    FileDownloader._report_progress_prev_line_length = 0
    FileDownloader._report_progress_status = lambda FileDownloader, msg: print(msg)
    fd = FileDownloader(Params())
    # Test finished
    fd.report_progress({
        'status': 'finished',
        'total_bytes': 100 * 1024 * 1024,
        'elapsed': 15.0,
    })
    # Test downloading
    fd.report_progress({
        'status': 'downloading',
        'total_bytes': None,
        'total_bytes_estimate': 100 * 1024 * 1024,
        'downloaded_bytes': 52 * 1024 * 1024,
        'elapsed': 14.0,
        'speed': 5 * 1024 * 1024,
        'eta': 1,
    })
    # Test downloading
   

# Generated at 2022-06-14 15:17:20.780398
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader(None, None)
    # Print format_bytes
    class _FakeInfo(dict):
        pass
    info_dict = _FakeInfo({'timestamp': datetime.datetime(2014, 2, 5, 14, 52, 2)})
    if time.daylight:
        if time.localtime(time.mktime(info_dict['timestamp'].timetuple()))[-1]:
            # If daylight saving time is in effect, timestamp in info_dict was created in non-DST timezone
            # and therefore has to be corrected by one hour
            info_dict['timestamp'] = info_dict['timestamp'] + datetime.timedelta(hours=1)
    d1 = time.mktime(info_dict['timestamp'].timetuple())
    filename = u'test'
