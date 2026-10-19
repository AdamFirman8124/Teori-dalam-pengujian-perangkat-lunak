

# Generated at 2022-06-14 15:08:06.601370
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    ydl = FileDownloader({})
    assert ydl.temp_name('blabla.mp4') == 'blabla.mp4.part'
    assert ydl.temp_name('/home/user/blabla.mp4') == '/home/user/blabla.mp4.part'
    assert ydl.temp_name('C:\\home\\user\\blabla.mp4') == 'C:\\home\\user\\blabla.mp4.part'



# Generated at 2022-06-14 15:08:07.342552
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    raise NotImplementedError

# Generated at 2022-06-14 15:08:16.124090
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    downloader = FileDownloader({})
    downloader.params['ratelimit'] = 10
    downloader.retries = 3
    retval = downloader.slow_down(time.time() - 5, time.time(), 50)
    assert retval is None
    retval = downloader.slow_down(time.time() - 5, time.time(), 20)
    assert retval is None
    retval = downloader.slow_down(time.time() - 5, time.time(), 9)
    assert retval is None
    retval = downloader.slow_down(time.time() - 5, time.time(), 10)
    assert retval is None
    retval = downloader.slow_down(time.time() - 5, time.time(), 11)
    assert retval == 1.0
    retval = downloader

# Generated at 2022-06-14 15:08:26.477326
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader({})
    assert fd.temp_name('a') == 'a.part'
    assert fd.temp_name('a.b') == 'a.b.part'
    assert fd.temp_name('a.b.c') == 'a.b.c.part'
    assert fd.temp_name('a/a') == 'a/a.part'
    assert fd.temp_name('a/a.b') == 'a/a.b.part'
    assert fd.temp_name('a/a.b.c') == 'a/a.b.c.part'

    fd = FileDownloader({'nopart': True})
    assert fd.temp_name('a') == 'a'
    assert fd.temp_name('a.b')

# Generated at 2022-06-14 15:08:34.769932
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    def t(f, s, o, e=None):
        o = o.format(**s)
        if e is None:
            e = o
        f._report_progress_status = lambda x: None
        f.report_progress(s)
        f.to_screen.assert_called_with(e, skip_eol=False)
        f.to_console_title.assert_called_with('youtube-dl ' + o)

    ydl = DummyYoutubeDL({'verbose': True, 'noprogress': False})
    f = FileDownloader(ydl, {})
    f.params['noprogress'] = False
    f.to_screen = mock.Mock()
    f.to_console_title = mock.Mock()


# Generated at 2022-06-14 15:08:40.798950
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    downloader = FileDownloader({}, None)
    info = {}
    info['filename'] = get_temp_filename()
    info['last_modified'] = 'Sun, 06 Nov 1994 08:49:37 GMT'

    def test(timestr):
        info['last_modified'] = timestr
        info['filetime'] = downloader.try_utime(info['filename'], info['last_modified'])
        assert timeconvert(timestr) == info['filetime']

    test('Sun, 06 Nov 1994 08:49:37 GMT')
    test('Sun, 06 Nov 1994 08:49:37')
    test('Sun, 06 Nov 1994 08:49 GMT')
    test('Sun, 06 Nov 1994 08:49')
    test('Sun, 06 Nov 1994 08:49 +0000')

# Generated at 2022-06-14 15:08:44.605544
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    def fake_download(filename, info):
        return filename == 'abc' and info == {'a': 4}

    fd = FileDownloader({})
    fd.real_download = fake_download

    assert fd.download('abc', {'a': 4})
    assert not fd.download('abcd', {'a': 4})
    assert not fd.download('abc', {'a': 5})
    assert not fd.download(1234, {'a': 4})
    assert not fd.download('abc', 'def')

if __name__ == '__main__':
    test_FileDownloader_download()

# Generated at 2022-06-14 15:08:52.514727
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    fd = FileDownloader(ydl)
    assert fd.undo_temp_name("filename") == "filename"
    assert fd.undo_temp_name("filename.part") == "filename"

    assert fd.undo_temp_name("filename.mp4") == "filename.mp4"
    assert fd.undo_temp_name("filename.mp4.part") == "filename.mp4"

# Generated at 2022-06-14 15:09:02.102204
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    # Create dummy FileDownloader
    downloader = FileDownloader({}, YoutubeDL({}))

    # Test some cases
    assert downloader.try_utime(None, None) is None
    assert downloader.try_utime('filename', 'today') is None

    # Test some valid cases
    test_seconds = 1366506936
    test_time_str = '%d' % test_seconds
    test_file_name = 'test_file'
    open(test_file_name, 'w').close()

    assert downloader.try_utime(test_file_name, test_time_str) == test_seconds
    assert os.path.getmtime(test_file_name) == test_seconds

    os.remove(test_file_name)

    # Test some invalid cases
    test_file_name

# Generated at 2022-06-14 15:09:12.203558
# Unit test for method calc_percent of class FileDownloader
def test_FileDownloader_calc_percent():
    def calc_percent_test(s, e, c, total, percent):
        assert(FileDownloader.calc_percent(s, e, c, total) == percent)

    calc_percent_test(0, 1, 0, 0, None)
    calc_percent_test(0, 1, 1, 0, None)
    calc_percent_test(0, 1, 0, 1, 0)
    calc_percent_test(0, 1, 1, 1, 100)

    calc_percent_test(0, 1, 0, 10, 0)
    calc_percent_test(0, 1, 5, 10, 50)
    calc_percent_test(0, 1, 10, 10, 100)
    calc_percent_test(0, 1, 10, 11, int(100 * 10 / 11))

    calc_percent_test

# Generated at 2022-06-14 15:09:49.814113
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    """Test method download of class FileDownloader."""
    import copy
    import tempfile
    import shutil
    import http.client
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl.downloader.http import HTTPDownloader
    from youtube_dl.downloader.http import HttpFD

    def _build_fake_server(responses):
        """
        Builds a fake server that responds with the appropriate response for
        each request.
        """
        def _request_handler(*args, **kwargs):
            s = responses.pop(0)
            if isinstance(s, Exception):
                raise s
            return s
        s = FakeServer(request_handler=_request_handler)
        s.start()


# Generated at 2022-06-14 15:09:53.591894
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader(params=None,
        info_dict=None,
        filename='file',
        download_retcode=0,
        ydl=None)
    fd.report_file_already_downloaded("file")



# Generated at 2022-06-14 15:10:05.350256
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Test is a method of class FileDownloader, so it requieres a instance of that class
    # to start with
    from youtube_dl.YoutubeDL import YoutubeDL

    # We need a dummy function, so we can use the decorator
    def dummy_callback(dummy_arg):
        pass

    # Create a dummy instance of YoutubeDL, with a dummy progress hook
    ydl = YoutubeDL(params={'progress_hooks': [dummy_callback]})
    fd = FileDownloader(ydl, {'progress_hooks': [dummy_callback]})
    # Remove the progress hook
    #fd._progress_hooks = []

    # And some test cases

# Generated at 2022-06-14 15:10:16.740640
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    downloader = FileDownloader(params=dict())

    base_filename = u'%s-%s' % (
        test_filename, int(time.time()))

    temp_filename = base_filename + u'.part'
    temp_file = open(temp_filename, 'wb')

# Generated at 2022-06-14 15:10:29.138322
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    from io import BytesIO

    if 'TRAVIS' in os.environ and os.environ['TRAVIS'] == 'true':
        raise unittest.SkipTest('Skip unit tests on Travis (see https://github.com/rg3/youtube-dl/pull/5756)')

    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as f:
        f.close()

    # Create a fake file
    content = b'DEADBEEF'
    with open(f.name, 'wb') as f:
        f.write(content)

    class _Info:
        def __init__(self, server_headers):
            self.server_headers = server_headers


# Generated at 2022-06-14 15:10:33.845258
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader('', {})
    assert fd.temp_name('abc') == 'abc.part'
    assert fd.temp_name('abc.mkv') == 'abc.mkv.part'
    assert fd.temp_name('abc.part') == 'abc.part'

    fd.params['nopart'] = True
    assert fd.temp_name('abc') == 'abc'
    assert fd.temp_name('abc.mkv') == 'abc.mkv'
    assert fd.temp_name('abc.part') == 'abc.part'

    fd.params['nopart'] = False
    os.mkdir('abc.part')
    assert fd.temp_name('abc.part') == 'abc.part'

# Generated at 2022-06-14 15:10:45.998546
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from .extractor import InfoExtractor
    from .downloader import YoutubeDL
    from .compat import compat_str

    class FakeInfoExtractor(InfoExtractor):
        def __init__(self, downloader):
            InfoExtractor.__init__(self, downloader)

    class FakeDownloader(YoutubeDL):
        def __init__(self):
            YoutubeDL.__init__(self)
        @staticmethod
        def to_screen(message, skip_eol=False):
            pass
        @staticmethod
        def to_console_title(message):
            pass

    def _fake_report_progress(status):
        messages.append(status['_percent_str'] + ' ' + status['_speed_str'])

    extractor = FakeInfoExtractor(FakeDownloader())
    downloader = FileDownload

# Generated at 2022-06-14 15:10:53.491921
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    # Check that calc_speed returns None when both times are equal
    start_time = time.time()
    assert FileDownloader(None).calc_speed(start_time,start_time,10) == None
    
    # Check that calc_speed returns None for a very small time difference
    assert FileDownloader(None).calc_speed(start_time,start_time + 0.001,10) == None
    
    # Check that a reasonable result is returned when the time difference is high enough
    assert FileDownloader(None).calc_speed(start_time,start_time + 2,100) == 50


# Generated at 2022-06-14 15:10:57.039942
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    assert FileDownloader(None, None).temp_name('a') == 'a.part'
    assert FileDownloader(None, None).temp_name('a.part') == 'a.part'


# Generated at 2022-06-14 15:11:04.962189
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    """

    :return:
    """
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor
    class FakeInfoExtractor(InfoExtractor):
        def _real_extract(self, url):
            return {
                'id': '4/v/b/4vb9M6mM2YM',
                'display_id': '4vb9M6mM2YM',
                'ext': 'mp4',
                'title': 'test_url',
                'description': 'test url description'
                }
    class FakeYoutubeDL(YoutubeDL):
        def __init__(self, *args, **kargs):
            super(FakeYoutubeDL, self).__init__(*args, **kargs)
            self.ie = Fake

# Generated at 2022-06-14 15:11:17.402136
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    from datetime import datetime

    old_time = time.time()
    time.sleep(1)

    filename = 'test_FileDownloader_try_utime'
    with open(filename, 'w'):
        pass

    d = FileDownloader({'noprogress': True}, None)

    filetime = d.try_utime(filename, None)
    assert filetime is None

    filetime = d.try_utime(filename, '')
    assert filetime is None

    filetime = d.try_utime(filename, 'invalid')
    assert filetime is None

    filetime = d.try_utime(filename, datetime.now().ctime())
    assert filetime is None

    filetime = d.try_utime(filename, datetime.now().ctime() + ' GMT')

# Generated at 2022-06-14 15:11:22.448708
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    file_downloader = FileDownloader({})
    filename = 'index.html'
    info_dict = {}

    def check_download(filename, info_dict):
        return True

    file_downloader.real_download = check_download
    assert file_downloader.download(filename, info_dict) is True

    # Test continuedl
    file_downloader = FileDownloader({'continuedl': True})
    filename = 'test_FileDownloader_download.txt'
    info_dict = {}
    file_downloader.real_download = check_download
    assert file_downloader.download(filename, info_dict) is True
    with open(filename, 'w') as f:
        f.write('test')
    assert file_downloader.download(filename, info_dict) is True

# Generated at 2022-06-14 15:11:28.559692
# Unit test for method calc_speed of class FileDownloader

# Generated at 2022-06-14 15:11:34.480361
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    testcases = {
        '': None,
        '42': 42,
        '0': 0,
        '42.5': None,
        '4.2k': 4200,
        '1.2K': 1234,
        '1.0e0k': 1000,
        '1.0E0k': 1000,
        '1.0E+0k': 1000,
        '1.0E+1k': 10000,
        '1.85Mi': 1945600,
        '100.0Gi': 100000000000,
        '1.0E-1k': 100,
        '1.0E-1': 0,
        '1.0E-2': 0,
        '1.0G': 1073741824,
        '-1.0G': -1073741824,
    }
   

# Generated at 2022-06-14 15:11:35.330966
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    pass # test not implemented

# Generated at 2022-06-14 15:11:47.624669
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():

    from io import StringIO

    if not pytest.config.option.run_slow_tests:
        return

    old_stdout = sys.stdout

    def f():
        try:
            FileDownloader({'noprogress': False}).report_progress({
                'status': 'finished',
                'total_bytes': 100,
                'elapsed': 0.01,
            })
        except:
            traceback.print_exc(file=sys.stdout)
        finally:
            sys.stdout = old_stdout
            time.sleep(0.1)

    sys.stdout = StringIO()
    threading.Thread(target=f, name='test_FileDownloader_report_progress').start()
    for _ in range(10):
        sys.stdout.write('\b' * 100)

# Generated at 2022-06-14 15:12:00.462885
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class FakeFD(object):
        def __init__(self):
            self.time_start = time.time()
            self.time_end = None
            self.bytes_downloaded = 0

        def read(self, bytes_n):
            now = time.time()
            self.bytes_downloaded += bytes_n
            if self.time_end is None and self.bytes_downloaded > (1 << 20):
                self.time_end = now
            return 'A' * bytes_n

        def close(self):
            pass

    def test_FileDownloader_slow_down_calc():
        fd = FakeFD()

# Generated at 2022-06-14 15:12:06.732682
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader({})
    assert fd.undo_temp_name('abc.part') == 'abc'
    assert fd.undo_temp_name('abc') == 'abc'
    assert fd.undo_temp_name('.part') == ''
    assert fd.undo_temp_name('part') == 'part'



# Generated at 2022-06-14 15:12:18.441043
# Unit test for method parse_bytes of class FileDownloader
def test_FileDownloader_parse_bytes():
    # Test with a real number
    assert FileDownloader.parse_bytes('1') == 1
    # Test with a float number
    assert int(FileDownloader.parse_bytes('1.2')) == 1
    # Test with various SI prefixes
    assert FileDownloader.parse_bytes('1k') == 1 * 1000
    assert FileDownloader.parse_bytes('1M') == 1 * 1000 * 1000
    assert FileDownloader.parse_bytes('1G') == 1 * 1000 * 1000 * 1000
    # Test with IEC binary prefixes
    assert FileDownloader.parse_bytes('1Ki') == 1 << 10
    assert FileDownloader.parse_bytes('1Mi') == 1 << 20
    assert FileDownloader.parse_bytes('1Gi') == 1 << 30
    # Test with invalid suffixes

# Generated at 2022-06-14 15:12:25.159511
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(params=None,ydl=None)
    assert fd.slow_down(None, None, None) == None
    assert fd.slow_down(10, 11, 12) == None
    assert fd.slow_down(1, 2, 0) == None
    
    
if __name__ == "__main__":
    test_FileDownloader_slow_down()


# Generated at 2022-06-14 15:13:08.551350
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    from .extractor.youtube import YoutubeIE
    from .utils import encodeFilename

    def tn(name, nopart):
        fd = FileDownloader({
            'continuedl': False,
            'nopart': nopart,
            'outtmpl': name,
        })
        ie = YoutubeIE(fd)
        fd.add_info_extractor(ie)
        return fd.temp_name(ie.prepare_filename(ie.ie_key))

    # Test with a simple filename
    assert tn('abc.flv', False) == 'abc.flv.part'
    assert tn('abc.flv', True) == 'abc.flv'

    # Test with a filename containing a format selection

# Generated at 2022-06-14 15:13:19.963718
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader("/path/to/FileDownloader.py", None, {'nopart': True})
    assert fd.temp_name("/path/to/file.txt") == "/path/to/file.txt"
    assert fd.temp_name("/path/to/file.txt.part") == "/path/to/file.txt.part"
    assert fd.temp_name("/path/to/file") == "/path/to/file"

    fd = FileDownloader("/path/to/FileDownloader.py", None, {'nopart': False})
    assert fd.temp_name("/path/to/file.txt") == "/path/to/file.txt.part"

# Generated at 2022-06-14 15:13:30.973115
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    class FakeFileDownloader(FileDownloader):
        def __init__(self, *args, **kwargs):
            self.sleep_time = 0.0
            self.sleep_called = False

        def slow_down(self, *args):
            FileDownloader.slow_down(self, *args)
            self.sleep_called = True

        def sleep(self, time):
            self.sleep_called = True
            self.sleep_time = time

    test = FakeFileDownloader()
    test.params['ratelimit'] = 10240
    test.slow_down(10, 10, 512)
    assert test.sleep_called == False
    assert test.sleep_time == 0.0

    test.slow_down(10, 20, 512)
    assert test.sleep_called == True
    assert test.sleep_time

# Generated at 2022-06-14 15:13:42.527039
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    FILENAME = 'test_FileDownloader-%s.tmp' % os.getpid()
    HTTP_SERVER_CPV = 'http://127.0.0.1:%s/content-provider/video.mp4' % port
    HTTP_SERVER_CPV_WITH_RANGE = 'http://127.0.0.1:%s/content-provider-with-range/video.mp4' % port
    HTTP_SERVER_CPQ = 'http://127.0.0.1:%s/content-provider/video.mp4' % port
    HTTP_SERVER_CPQ_WITH_RANGE = 'http://127.0.0.1:%s/content-provider-with-range/video.mp4' % port
    HTTP_SERVER_NON_EXIST

# Generated at 2022-06-14 15:13:48.501750
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    fd = FileDownloader(None, params={'ratelimit': 10})
    startTime = time.time()
    fd.slow_down(startTime, startTime, 0)
    assert time.time() == startTime
    fd.slow_down(startTime, startTime, 1)
    assert time.time() == startTime
    fd.slow_down(startTime, startTime, 11)
    assert time.time() > startTime
# Different unit tests for method format_seconds of class FileDownloader

# Generated at 2022-06-14 15:13:59.203446
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    fd = FileDownloader(FakeYDL(), {})
    assert fd.temp_name('abc') == 'abc'
    assert fd.temp_name('a-b_c') == 'a-b_c'
    assert fd.temp_name(u'åæç') == u'åæç'

    params = {'nopart': True}
    fd = FileDownloader(FakeYDL(), params)
    assert fd.temp_name(u'åæç') == u'åæç'

    params = {'nopart': False}
    fd = FileDownloader(FakeYDL(), params)
    assert fd.temp_name(u'åæç') == u'åæç.part'
    assert fd.temp_name(u'åæç.part') == u

# Generated at 2022-06-14 15:13:59.820014
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    pass

# Generated at 2022-06-14 15:14:09.187940
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    from .YoutubeDL import YoutubeDL
    fd = FileDownloader({}, YoutubeDL({'ratelimit': '2'}))
    start_time = time.time()
    fd.slow_down(start_time, start_time, 4)
    assert time.time() - start_time < 0.1
    fd.slow_down(start_time, start_time + 1, 2)
    assert time.time() - start_time < 1.1
    fd.slow_down(start_time, start_time + 1, 4)
    assert time.time() - start_time > 1.9
    fd.slow_down(start_time, start_time + 1, 2.5)
    assert time.time() - start_time > 2.4

# Generated at 2022-06-14 15:14:15.705398
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import sys
    import time
    from test import util
    from test import test_utils

    if sys.platform == 'win32':
        with test_utils.DisableStderr():
            raise unittest.SkipTest('This test does not support Windows')

    class FakeInfoDict(object):
        def __init__(self, total_bytes=None, total_bytes_estimate=None):
            self._total_bytes = total_bytes
            self._total_bytes_estimate = total_bytes_estimate

        def __getitem__(self, key):
            return getattr(self, '_' + key)

    # Create fake method to replace FileDownloader.report_progress
    import mock
    original_report_progress = FileDownloader.report_progress

# Generated at 2022-06-14 15:14:25.649808
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # pylint: disable=W0212
    def test_slow_down(speed, rate_limit, sleep_time):
        fd = FileDownloader({'ratelimit': rate_limit})
        now = time.time()
        fd.slow_down(now - sleep_time, now, speed * sleep_time)

    test_slow_down(50, 70, 1)  # Too fast - slow down
    test_slow_down(50, 20, 1)  # Too slow - speed up
    test_slow_down(50, 30, 1)  # Just right - do nothing

    test_slow_down(50, 70, 1)



# Generated at 2022-06-14 15:14:55.560632
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FD(dict())
    fd.params['noprogress'] = False
    fd.to_screen = lambda x: None
    fd.report_progress(dict(
        status='finished',
        total_bytes=1000,
        elapsed=10,
    ))
    fd.report_progress(dict(
        status='downloading',
        downloaded_bytes=100,
        total_bytes=1000,
        total_bytes_estimate=1500,
        elapsed=1,
        eta=10,
        speed=1000,
    ))

# Generated at 2022-06-14 15:15:06.087459
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    downloader = FileDownloader(params=None)
    assert(downloader.temp_name('foo') == 'foo.part')
    downloader.params = {'nopart': True}
    assert(downloader.temp_name('foo') == 'foo')
    assert(downloader.temp_name('/foo/bar/baz') == '/foo/bar/baz')
    assert(downloader.temp_name('C:\\foo\\bar\\baz') == 'C:\\foo\\bar\\baz')
    downloader.params = {'nopart': False}
    assert(downloader.temp_name('C:\\foo\\bar\\baz') == 'C:\\foo\\bar\\baz.part')

# Generated at 2022-06-14 15:15:17.097004
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import os, tempfile
    from youtube_dl.utils import encode_compat_str

    # check download for non-existing file
    _, output_file_name = tempfile.mkstemp(prefix='yt-dl-test_', suffix='.tmp')
    assert not os.path.exists(output_file_name)
    fd = FileDownloader(None, params={
        'noprogress': True,
        'logger': YoutubeDLHandler(),
        'quiet': True,
        'continuedl': False,
        'nooverwrites': False
    })
    res = fd.download(output_file_name, {
        'url': 'foobar',
        'id': 'testvideoid',
        'ext': 'mp4',
        'format': 'best'
    })

# Generated at 2022-06-14 15:15:21.061872
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    try:
        FileDownloader.best_block_size(10, 200)
    except Exception:
        assert False, "FileDownloader.best_block_size throws exception"



# Generated at 2022-06-14 15:15:28.411010
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({})
    s_keys = ['_eta_str', '_elapsed_str', 'status', '_speed_str', 'downloaded_bytes', '_total_bytes_estimate_str', 'eta',
              '_total_bytes_str', 'elapsed', 'speed', '_downloaded_bytes_str', 'total_bytes_estimate', 'total_bytes']
    for s_key in s_keys:
        s = {'status': 'downloading'}
        s[s_key] = None
        fd.report_progress(s)
        assert (not fd.to_screen.called)



# Generated at 2022-06-14 15:15:41.727787
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    try:
        os.remove('test.tmp')
    except EnvironmentError:
        pass
    try:
        os.remove('test.tmp.part')
    except EnvironmentError:
        pass

    def testdlfn(*args, **kwargs):
        assert kwargs['test_dlfn_called']
        assert kwargs['url'] == 'http://example.org/'
        assert args[0] == 'test.tmp'
        return True

    fd = FileDownloader(None, {'test':True})
    fd.real_download = testdlfn
    assert not fd.download('test.tmp', {'url': 'http://example.org/', 'test_dlfn_called': True})

# Generated at 2022-06-14 15:15:44.750972
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    fd = FileDownloader(FakeYDL(), {})
    fd.report_file_already_downloaded('test')

# end class FileDownloader


# Generated at 2022-06-14 15:15:50.309705
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # Init a FileDownloader
    fd = FileDownloader({}, {'test':True}, None, None)
    # Test download function
    fd.download('test.txt', {'status': 'finished'})
    # Cleanup
    os.system('rm -rf test.txt')
    fd = None
if __name__ == "__main__":
    test_FileDownloader_download()

# Generated at 2022-06-14 15:16:00.321166
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():

    # Create a test downloader
    downloader = FileDownloader(
        params={
            'ratelimit': 1048576  # 1 MiB/s
        })

    # Create a mock time.time function
    time_counter = [
        0.0,  # Initialize
        1 * 1048576.0,  # First check: 1 MiB/s
        2 * 1048576.0,  # Second check: 1 MiB/s
        3 * 1048576.0,  # Third check: 1 MiB/s
        4 * 1048576.0,  # Fourth check: 1 MiB/s
    ]
    def time_time_mock():
        return time_counter.pop(0)
    time.time = time_time_mock

    # Prepare test values
    start = time.time()
    now

# Generated at 2022-06-14 15:16:11.690420
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import re
    import sys
    import unittest

    from .compat import is_py2
    from .utils import encode_compat_str

    # Set default timeout high to avoid running into timeouts on slow machines
    # and to avoid problems with processes being killed on some CI services
    TIMEOUT = 600

    class DummyYDL(object):
        def __init__(self):
            self.msgs = []

        def to_screen(self, *args, **kargs):
            self.msgs += args
            self.msgs += (kargs,)

        def to_console_title(self, *args, **kwargs):
            pass

    class FileDownloaderTest(unittest.TestCase):
        """
        Unit tests for _report_progress()
        """

# Generated at 2022-06-14 15:16:35.628056
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    """Test method format_retries of class FileDownloader."""
    # Test format_retries()
    fd = FileDownloader({})
    assert fd.format_retries(float('inf')), 'inf'
    assert fd.format_retries(float('inf') + 1), 'inf.'
    assert fd.format_retries(float('inf') - 1), 'inf'
    assert fd.format_retries(3.14), '3'
    assert fd.format_retries(0), '0'
test_FileDownloader_format_retries.func_name = 'test_format_retries'


# Generated at 2022-06-14 15:16:41.215084
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    def _try_utime(timestr):
        f = FileDownloader(None, None)
        res = f.try_utime('/tmp/u', timestr)
        return res
    # Test for good input format
    res = _try_utime('Thu, 03 Feb 2012 00:00:00 GMT')
    assert res == 1328185600
    # Test improper format happens
    res = _try_utime('Thu, 03 Feb 2012 00:00:00 GTM')
    assert res is None


# Generated at 2022-06-14 15:16:46.717809
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader()
    s = {
        'status': 'downloading',
        'total_bytes': 11234,
        'downloaded_bytes': 4446,
        'speed': 123,
        'eta': 1233
    }
    # The output of method report_progress of class FileDownloader is sent
    # to stdout. We can't test it because of this.
    fd.report_progress(s)

# Generated at 2022-06-14 15:16:58.501239
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import pytest
    from .postprocessor import FFmpegMetadataPP
    from .compat import str
    from .extractor import gen_extractors
    from .utils import DateRange

    yaie = gen_extractors()['youtube']()

# Generated at 2022-06-14 15:17:03.523389
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    fd = FileDownloader({})
    fd.to_screen = lambda *args: None
    fd.to_console_title = lambda *args: None

    fd.report_progress({
        'status': 'finished',
        'total_bytes': 4096,
    })

    fd.report_progress({
        'status': 'finished',
        'total_bytes': None,
    })


# Generated at 2022-06-14 15:17:10.511524
# Unit test for method try_utime of class FileDownloader

# Generated at 2022-06-14 15:17:18.092277
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    downloader = VideoDownloader()
    downloader.to_screen = lambda x: x
    assert '1' == downloader.format_retries(1)
    assert 'inf' == downloader.format_retries(float('inf'))
    assert 'no' == downloader.format_retries(float('NaN'))
    assert 'no' == downloader.format_retries(float('nan'))
test_FileDownloader_format_retries()