

# Generated at 2022-06-14 15:08:01.480576
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    pass



# Generated at 2022-06-14 15:08:06.366518
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader('dummy')
    assert fd.undo_temp_name('abc.part') == 'abc'
    assert fd.undo_temp_name('abc.part.part') == 'abc.part'
    assert fd.undo_temp_name('abc') == 'abc'



# Generated at 2022-06-14 15:08:10.231327
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    downloader = FileDownloader({})
    assert downloader.undo_temp_name('file.mp4') == 'file.mp4'
    assert downloader.undo_temp_name('file.mp4.part') == 'file.mp4'



# Generated at 2022-06-14 15:08:16.571539
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    # Test data
    fd = FileDownloader({})
    fd._start_time = 1416734545.5
    # Expected results
    expected_speeds = [10., 100., 1000., 10000., 100000., 1000000., 10000000.]
    # Testing
    for i in expected_speeds:
        speed = fd.calc_speed(fd._start_time, fd._start_time + 1., i)
        assert speed == i, 'The returned speed %s is different from the expected speed %s' % (speed, i)


# Generated at 2022-06-14 15:08:26.108624
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    #assert FileDownloader.calc_speed(1, 2, 1) is None
    #assert FileDownloader.calc_speed(1, 2, 0) == float('inf')
    assert abs(FileDownloader.calc_speed(1, 3, 4) - 1.3333333333333333) < 0.00000000000001
    #assert FileDownloader.calc_speed(1, 1.1, 4) == 36.36363636363636
    #assert FileDownloader.calc_speed(1, 1.1, 0) is None
    #assert FileDownloader.calc_speed(1, 1.1, 1) == 9.090909090909092

test_FileDownloader_calc_speed()


# Generated at 2022-06-14 15:08:29.884665
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader({'outtmpl': u'%(title)s-%(id)s.%(ext)s'})
    filepath = u'%s-%s.webm' % (u'The Professor and the Madman',u'kmX9aTPbohg')
    assert fd.try_utime(filepath, u'Wed, 09 Dec 2015 04:51:10 GMT') == 1449586270

if __name__ == '__main__':
    test_FileDownloader_try_utime()

# Generated at 2022-06-14 15:08:36.887277
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    # TODO: complete the test
    pass



# Generated at 2022-06-14 15:08:46.886159
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    fd = FileDownloader(None, None)
    assert fd.best_block_size(1.0, 1000) == 4194304
    assert fd.best_block_size(1.0, 10240) == 262144
    assert fd.best_block_size(1.0, 102400) == 16384
    assert fd.best_block_size(1.0, 1024000) == 1024
    assert fd.best_block_size(1.0, 10240000) == 64
    assert fd.best_block_size(1.0, 102400000) == 4
    assert fd.best_block_size(1.0, 1024000000) == 1

    assert fd.best_block_size(1.0, 0) == 1

# Generated at 2022-06-14 15:08:51.888843
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    assert FileDownloader.calc_speed(1000, 1100, 1000) == 1000
    assert FileDownloader.calc_speed(1000, 1100, 2000) == 2000
    assert FileDownloader.calc_speed(1000, 1100, 4000) == 4000
    assert FileDownloader.calc_speed(1000, 1100, 0) is None

# Generated at 2022-06-14 15:08:56.386330
# Unit test for method format_retries of class FileDownloader
def test_FileDownloader_format_retries():
    fd = FileDownloader({})
    assert 'inf' == fd.format_retries(float('inf'))
    assert '3' == fd.format_retries(3)

if __name__ == '__main__':
    sys.exit(FieldStorage(sys.stdin).getfirst('test'))

# Generated at 2022-06-14 15:09:20.202781
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    # Test with rate limit = 0
    assert FileDownloader('','',{})._calc_rate(0, 0) == 0
    assert FileDownloader('','',{})._calc_rate(10, 0) == 0
    assert FileDownloader('','',{})._calc_rate(0, 10) == 0
    assert FileDownloader('','',{})._calc_rate(10, 10) == 0
    # Test with rate limit = 10
    assert FileDownloader('','',{})._calc_rate(10, 100) == 1000
    assert FileDownloader('','',{})._calc_rate(10, 10) == 100
    assert FileDownloader('','',{})._calc_rate(10, 1) == 10
    # Test with rate limit = -1 (capped to

# Generated at 2022-06-14 15:09:26.560592
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    print('---- Testing report_file_already_downloaded method')
    fd = FileDownloader(None, params={})
    fd.to_screen = lambda x : print('to_screen', x)
    print('Testing without unicode')
    fd.report_file_already_downloaded('foo')
    print('Testing with unicode')
    fd.report_file_already_downloaded(u'fóo')


# Generated at 2022-06-14 15:09:36.473677
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    from json import dumps
    from os.path import join as path_join
    from tempfile import gettempdir
    from time import sleep

    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader.common import FileDownloader

    from .test_downloader import UnitTestDownloader

    def download_hook(status):
        nonlocal progress_items

        if status['status'] == 'finished':
            progress_items.append(status)
        else:
            progress_items.append({
                'bytes': status['downloaded_bytes'],
                'eta': status['eta'],
                'filename': status['filename'],
                'speed': status['speed'],
            })

    # List that will keep the different values returned by the
    # report_progress function.
    progress_items = []

    #

# Generated at 2022-06-14 15:09:48.802709
# Unit test for method try_rename of class FileDownloader

# Generated at 2022-06-14 15:09:57.239862
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import time

    class FakeScreen:
        def __init__(self):
            self.out = []

        def write(self, output):
            self.out.append(output)

    fd = FileDownloader()
    fd.to_screen = FakeScreen()
    fd.params = {}

    # test for all known fields

# Generated at 2022-06-14 15:10:08.463395
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    from types import MethodType
    from tempfile import mkstemp
    from time import time

    def assertEquals(a, b):
        if not a == b:
            raise AssertionError("%s != %s" % (a, b))

    def assertTrue(a):
        if not a:
            raise AssertionError("%s is not True" % a)

    def assertFalse(a):
        if a:
            raise AssertionError("%s is not False" % a)

    def assertNone(a):
        if a is not None:
            raise AssertionError("%s is not None" % a)

    fd, filename = mkstemp()
    os.close(fd)
    os.remove(filename)


# Generated at 2022-06-14 15:10:14.315090
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    assert FileDownloader.calc_speed(0, 0, 0) is None
    assert FileDownloader.calc_speed(0, 0, 1) is None
    assert FileDownloader.calc_speed(0, 1, 0) is None
    assert FileDownloader.calc_speed(0, 1, 1) == 1

# Generated at 2022-06-14 15:10:26.893171
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    def test_assert(v, r):
        assert v == r

    fd = FileDownloader({})
    fd._ookies = {'youtube.com': {'name': 'name', 'value': 'value'}}

    test_assert(fd.calc_speed(0, 0, 0), None)
    test_assert(fd.calc_speed(0, 0.1234, 1000), 8189.18918918919)
    test_assert(fd.calc_speed(0, 1 / 10**6, 1000), 8000000.0)
    test_assert(fd.calc_speed(0, 2, 1000**2), 500000.0)
    test_assert(fd.calc_speed(0, 0.001, 1000**3), 1000000000.0)


# Generated at 2022-06-14 15:10:32.696430
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    from file_downloader import FileDownloader
    fd = FileDownloader({})
    filename = 'test.txt'
    fd.try_utime(filename, 'Sun, 9 Dec 2018 04:09:59 GMT')
    filetime = os.path.getmtime(filename)
    os.remove(filename)
    assert filetime == 1544599399
    

# Generated at 2022-06-14 15:10:44.468494
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    """Basic test for method temp_name of class FileDownloader."""
    fd = FileDownloader(params={'noprogress': True})
    assert fd.temp_name('x') == 'x.part'
    assert fd.temp_name('x.y') == 'x.part.y'
    assert fd.temp_name('x') == 'x.part'
    assert fd.temp_name('-') == '-'
    assert fd.temp_name('/path/to/x') == '/path/to/x.part'
    assert fd.temp_name('/path/to/x.y') == '/path/to/x.part.y'
    assert fd.temp_name('/path/to/x') == '/path/to/x.part'

# Generated at 2022-06-14 15:11:01.740209
# Unit test for method calc_speed of class FileDownloader
def test_FileDownloader_calc_speed():
    d = FileDownloader(None)
    assert d.calc_speed(0, 10, 0) is None
    assert d.calc_speed(0, 10, 12345) == 1234.5


# Generated at 2022-06-14 15:11:08.097542
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    dl = FileDownloader(ydl, {'continuedl': True, 'nooverwrites': True})
    assert dl.temp_name('abc') == 'abc.part'
    assert dl.temp_name('abc.def') == 'abc.def.part'
    assert dl.temp_name('abc.def.ghi') == 'abc.def.ghi.part'
    assert dl.temp_name('-') == '-'
    assert dl.temp_name('.a-bc') == '.a-bc.part'
    assert dl.temp_name('a-bc.') == 'a-bc..part'
    assert dl.temp_name('') == '.part'



# Generated at 2022-06-14 15:11:19.967605
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import pytest
    from youtube_dl.YoutubeDL import YoutubeDL

    class Mock(YoutubeDL):
        @staticmethod
        def _get_best_downloader(ie_name):
            assert ie_name == 'fakeIE'
            return (MockFileDownloader, None)

    class MockFileDownloader(FileDownloader):
        def __init__(self, *args, **kwargs):
            super(MockFileDownloader, self).__init__(*args, **kwargs)
            self.download_called = False
            self.download_called_count = 0

        def real_download(self, *args, **kwargs):
            self.download_called = True
            self.download_called_count += 1
            return True

    ydl = Mock()

    # Test direct download
    # Test nooverwrit

# Generated at 2022-06-14 15:11:29.418215
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    def _test(filename, last_modified_hdr, expected_utime):
        assert FileDownloader.try_utime(filename, last_modified_hdr) == expected_utime
        assert (int(os.stat(filename).st_mtime) == expected_utime)

    # Test with a file
    fh, filename = tempfile.mkstemp()
    os.close(fh)
    os.utime(filename, (1000, 1000))

    _test(filename, None, 1000)
    _test(filename, 'INVALID_DATE', 0)
    _test(filename, 'Sat, 12 Feb 2011 20:57:38 GMT', 1297671458)

    _test(filename, 'Sat, 12 Feb 2011 20:57:38 +0000', 1297671458)

# Generated at 2022-06-14 15:11:33.617997
# Unit test for method try_rename of class FileDownloader
def test_FileDownloader_try_rename():
    FileDownloader.try_rename('file_name.part', 'file_name')
    FileDownloader.try_rename('file_name', 'file_name')
    FileDownloader.try_rename('file_name', 'file_name.part')
    # TODO: How to get FileDownloader.ReportError() in action?



# Generated at 2022-06-14 15:11:44.389484
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    fd = FileDownloader(YoutubeDL({}))
    filename = '__test_FileDownloader_try_utime.tmp'
    open(filename, 'w').close()
    assert fd.try_utime(filename, 'Thu, 29 Dec 1977 22:00:00 +0200') == 2248040000
    assert fd.try_utime(filename, 'Mon, 10 Oct 1977 01:30:00 -0302') == 2169754200
    assert os.path.getmtime(filename) == 2169754200
    assert fd.try_utime(filename, None) is None
    os.remove(filename)

# Generated at 2022-06-14 15:11:48.486159
# Unit test for method best_block_size of class FileDownloader
def test_FileDownloader_best_block_size():
    print(FileDownloader.best_block_size(0.1, 0))
    print(FileDownloader.best_block_size(0.1, 500))
    print(FileDownloader.best_block_size(0.5, 1000))
    print(FileDownloader.best_block_size(0.5, 1024*1024))

# Generated at 2022-06-14 15:12:00.839448
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    import sys
    
    import http.client
    import io
    import os
    import posixpath
    import re
    import shutil
    import signal
    import socket
    import ssl
    import subprocess
    import tempfile
    import types
    import unittest.mock
    
    from urllib.parse import urlparse
    from contextlib import closing
    
    import pytest
    
    try:
        from ssl import SSLContext
    except ImportError:
        # Backward compatibility with Python 2.7
        SSLContext = None
    
    # Python 2 backward compatibility
    if sys.version_info.major == 2:
        import SocketServer
        import BaseHTTPServer
        import SimpleHTTPServer
        import urlparse
    else:
        import socketserver as SocketServer

# Generated at 2022-06-14 15:12:01.462800
# Unit test for method download of class FileDownloader
def test_FileDownloader_download():
    pass

# Generated at 2022-06-14 15:12:14.396659
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    params = {}
    params['ratelimit'] = 5.0
    params['noprogress'] = False
    ydl = YoutubeDL(params)
    fd = FileDownloader(ydl)
    start = time.time()
    now = time.time()
    byte_counter = 5
    fd.slow_down(start, now, byte_counter)
    time.sleep(1)
    assert now - start == 1
    assert byte_counter == 5
    byte_counter = 8
    fd.slow_down(start, now, byte_counter)
    time.sleep(1)
    assert now - start == 2
    assert byte_counter == 8
    byte_counter = 10
    fd.slow_down(start, now, byte_counter)
    time.sleep(1)

# Generated at 2022-06-14 15:13:10.687564
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import os
    import time
    class FakeInfoDict:
        def __init__(self):
            self.status = 'finished'
            self.total_bytes = None
            self.total_bytes_estimate = None
            self.downloaded_bytes = 0
            self.elapsed = None
            self.eta = None
            self.speed = None

# Generated at 2022-06-14 15:13:18.535728
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    assert FileDownloader.undo_temp_name('abc') == 'abc'
    assert FileDownloader.undo_temp_name('abc.part') == 'abc'
    assert FileDownloader.undo_temp_name('/a/b/c') == '/a/b/c'
    assert FileDownloader.undo_temp_name('/a/b/c.part') == '/a/b/c'
    assert FileDownloader.undo_temp_name('/a/b/c.part.part') == '/a/b/c.part'

# Generated at 2022-06-14 15:13:27.537326
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    from youtube_dl.YoutubeDL import YoutubeDL
    import io
    fd = FileDownloader(YoutubeDL(), {})
    assert sys.stdout.encoding == 'UTF-8'
    # stdout is IO(TextIOWrapper) in Python3, TextIOWrapper in Python2
    assert isinstance(sys.stdout, io.TextIOWrapper)
    assert isinstance(sys.stderr, io.TextIOWrapper)

    with std_files_redirected(sys.stdout, sys.stderr):
        fd.report_file_already_downloaded('abc')
        fd.report_file_already_downloaded('a' + '\u20ac' + '\U0001f44d')

# Generated at 2022-06-14 15:13:28.663436
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    # Code here
    pass



# Generated at 2022-06-14 15:13:40.227001
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import sys
    import datetime
    from time import time as time_time
    # Run the test 25 times to try various combinations of time computations
    TESTS_RUN = 0
    while TESTS_RUN < 25:
        # Use a new downloader each time
        fd = FileDownloader({})
        # Manually set the last line length attribute
        if hasattr(fd, "_report_progress_prev_line_length"):
            del fd._report_progress_prev_line_length
        fd.to_screen = sys.stdout.write
        # Prepare the input for the downloader report_progress method
        for k in ['eta', 'total_bytes', 'downloaded_bytes', 'elapsed', 'speed', 'total_bytes_estimate']:
            v = None

# Generated at 2022-06-14 15:13:49.458058
# Unit test for method slow_down of class FileDownloader
def test_FileDownloader_slow_down():
    def dl(speed):
        ydl = FileDownloader( {'ratelimit': speed})
        ydl.slow_down(time.time(), None, 1024)
    dl(0)
    dl(4194304)
    dl(16777215)
    dl(1)
    dl(1024)
    dl(1048576)

if __name__ == '__main__':
    print('Testing FileDownloader.slow_down')
    test_FileDownloader_slow_down()
    print('Testing FileDownloader.calc_percent')
    for x in [0, 0.1, 100, 1000, None]:
        for y in [0, 0.1, 100, 1000, None]:
            print(x, y, FileDownloader.calc_percent(x, y))
   

# Generated at 2022-06-14 15:14:00.022139
# Unit test for method try_rename of class FileDownloader
def test_FileDownloader_try_rename():
    """
    Test method try_rename of class FileDownloader
    """
    import sys
    from youtube_dl.compat import compat_os_name
    from youtube_dl.utils import FileDownloader, encodeFilename, error_to_compat_str

    # Check for windows
    if compat_os_name == 'nt':
        raise Exception('This is just for testing on non-Windows platform')

    def _to_screen(self, str, skip_eol=False):
        sys.stdout.write(str)
        sys.stdout.flush()

    #temporarily override the method to_screen
    FileDownloader.to_screen = _to_screen

    #create the class instance
    fd = FileDownloader(params={}, info_dict={})

    #Test 1: Renaming of a file with a simple name

# Generated at 2022-06-14 15:14:07.456270
# Unit test for method calc_eta of class FileDownloader
def test_FileDownloader_calc_eta():
    fd = FileDownloader({})
    assert fd.calc_eta(0,0,0) == None
    assert fd.calc_eta(0,1,1) == None
    assert fd.calc_eta(0,0,1) == None
    assert fd.calc_eta(0,1,2) == 1
    assert fd.calc_eta(1,2,3) == 1
    assert fd.calc_eta(3,12,13) == 1
    assert fd.calc_eta(0,12,13) == None

# Generated at 2022-06-14 15:14:14.238267
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    cases = [
        ('abc.part', 'abc'),
        ('abc.mp4.part', 'abc.mp4'),
        ('abc-def-xyz.part', 'abc-def-xyz')
    ]

    for case in cases:
        assert FileDownloader(youtube_dl()).undo_temp_name(case[0]) == case[1]


# Generated at 2022-06-14 15:14:26.242812
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    from youtube_dl.utils import DateRange
    from datetime import datetime

    fd = FileDownloader({})

    # The file does not exist
    assert fd.try_utime('foobar1992', '2010-01-01T01:01:01Z') is None

    # The file exists and was modified at the same time of the given
    # last-modified-header
    with open('foobar1992', 'w') as f:
        f.write('test')
    assert os.path.isfile('foobar1992')
    assert fd.try_utime('foobar1992', '2010-01-01T01:01:01Z') == 1262304661.0
    os.remove('foobar1992')

    # The file exists and was modified later than the given
    # last-modified-header

# Generated at 2022-06-14 15:15:44.694707
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader(params={})

    assert fd.undo_temp_name("f.part") == "f"
    assert fd.undo_temp_name("f.part.part") == "f.part"
    assert fd.undo_temp_name("f.part.foobar") == "f.part.foobar"
    assert fd.undo_temp_name("f.part1.part2") == "f.part1.part2"
    assert fd.undo_temp_name("f") == "f"
    assert fd.undo_temp_name("f.bar") == "f.bar"
    assert fd.undo_temp_name("f.bar.part.part") == "f.bar.part.part"

# Generated at 2022-06-14 15:15:50.052056
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    path = encodeFilename('data')
    if not os.path.exists(path):
        os.mkdir(path)
    output_file_path = encodeFilename(os.path.join(path, 'test_file.txt'))
    with open(output_file_path, 'w') as test_file:
        test_file.write('test')
    fd = FileDownloader({'outtmpl': u'data/%(title)s.%(ext)s'})
    # Test with correct last modified time
    fd.try_utime(u'test_file.txt', 'Fri, May 23, 2014 15:24:19 GMT')
    # Test with wrong last modified time
    fd.try_utime(u'test_file.txt', '9999999999999')
    # Test with wrong last modified

# Generated at 2022-06-14 15:15:59.564037
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import pytest
    fd = FileDownloader(None)
    fd.report_progress({'status':'downloading', 'downloaded_bytes':10, 'total_bytes':10, 'speed':0, 'eta':0})
    assert fd.to_screen.called == False
    fd.report_progress({'status':'downloading', 'downloaded_bytes':10, 'total_bytes':10, 'speed':0, 'eta':0})
    assert fd.to_screen.called == False
    fd.report_progress({'status':'finished', 'downloaded_bytes':10, 'total_bytes':10, 'speed':0, 'eta':0})
    assert fd.to_screen.called == True


# Generated at 2022-06-14 15:16:11.182798
# Unit test for method undo_temp_name of class FileDownloader
def test_FileDownloader_undo_temp_name():
    fd = FileDownloader(FakeYoutubeDl())
    assert fd.undo_temp_name('test.part') == 'test'
    assert fd.undo_temp_name('test.part') == 'test'
    assert fd.undo_temp_name('foo.bar-test.part') == 'foo.bar-test'
    assert fd.undo_temp_name('test') == 'test'
    assert fd.undo_temp_name('test.part.part') == 'test.part'
    assert fd.undo_temp_name('test.part.part') == 'test.part'
    assert fd.undo_temp_name('test.part.baz.part') == 'test.part.baz'
    assert fd.undo_temp_name('test.part.baz.part')

# Generated at 2022-06-14 15:16:23.324763
# Unit test for method report_file_already_downloaded of class FileDownloader
def test_FileDownloader_report_file_already_downloaded():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import encodeFilename
    ydl = YoutubeDL()
    ydl.params['nooverwrites'] = True
    # Encode all the unicode characters to avoid UnicodeEncodeError
    filename = encodeFilename('Drôle de parcours')
    # Open and close the file to create it
    open(filename, 'w').close()
    fd = FileDownloader(ydl, {})
    try:
        # This should not throw an exception
        fd.report_file_already_downloaded(filename)
    finally:
        # Remove the file
        os.remove(filename)

if __name__ == '__main__':
    test_FileDownloader_report_file_already_downloaded()



# Generated at 2022-06-14 15:16:33.911769
# Unit test for method try_utime of class FileDownloader
def test_FileDownloader_try_utime():
    import os
    import datetime

    # Create a temporary file
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    fname = f.name

    def get_mtime():
        return os.path.getmtime(fname)

    # Write some stuff to the file and make sure time has changed
    before_writing = datetime.datetime.now()
    with open(fname, 'w') as f:
        f.write('test')
    after_writing = datetime.datetime.now()
    assert get_mtime() > time.mktime(before_writing.timetuple())
    assert get_mtime() < time.mktime(after_writing.timetuple())

    # Test FileDownloader.try_utime
    fd = FileDownloader({})

# Generated at 2022-06-14 15:16:41.992882
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    import io
    import sys
    import time
    from .YoutubeDL import YoutubeDL
    from .YoutubeDLHandler import YoutubeDLHandler
    from .compat import is_py2, is_win32

    def skip_for_platform(*platforms):
        if sys.platform in platforms:
            pytest.skip()

    if not is_py2:
        skip_for_platform('win32')

    class FakeYDL(YoutubeDL):
        def to_screen(self, message, skip_eol=False):
            print(message, file=self._screen_file)
            self._screen_file.flush()
            if not skip_eol:
                print(file=self._screen_file)
                self._screen_file.flush()

        def to_console_title(self, message):
            pass

   

# Generated at 2022-06-14 15:16:52.715596
# Unit test for method report_progress of class FileDownloader
def test_FileDownloader_report_progress():
    bytes_range = range(0, 1000000, 16384)
    bytes_range.append(1000000)
    seconds_range = range(0, 100, 10)
    seconds_range.append(100)
    for speed, eta, downloaded_bytes, total_bytes, total_bytes_estimate, elapsed in itertools.product(
            bytes_range, seconds_range, bytes_range, bytes_range, bytes_range, seconds_range):
        assert speed == FileDownloader.calc_speed(
            elapsed - 10, elapsed, downloaded_bytes)
        if total_bytes > 0:
            assert eta == FileDownloader.calc_eta(
                start=elapsed - 10, now=elapsed,
                downloaded_bytes=downloaded_bytes, total_bytes=total_bytes)

# Generated at 2022-06-14 15:17:02.844649
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    def output_test(input_filename, expected_output):
        downloader = FileDownloader({})
        result = downloader.temp_name(input_filename)
        print(expected_output)
        print(result)
        assert(expected_output == result)

    output_test('filename.mp4', 'filename.mp4.part')
    output_test('-', '-')
    output_test('/path/to/filename.mp4', '/path/to/filename.mp4.part')
    output_test('nopart', 'nopart')
    output_test('/path/to/nopart', '/path/to/nopart')

    os.mkdir('./nopart_directory_test')

# Generated at 2022-06-14 15:17:14.969910
# Unit test for method temp_name of class FileDownloader
def test_FileDownloader_temp_name():
    # Test for http://site.com/image.jpg
    assert 'image.jpg' == FileDownloader.temp_name('image.jpg')

    # Test for http://site.com/video.mp4
    assert 'video.mp4' == FileDownloader.temp_name('video.mp4')

    # Test for /absolute/path/to/file.mp4
    assert '/absolute/path/to/file.mp4' == FileDownloader.temp_name('/absolute/path/to/file.mp4')

    # Test for image.jpg with nopart params
    assert 'image.jpg' == FileDownloader.temp_name('image.jpg', {'nopart': True})

    # Test for http://site.com/image.jpg with nopart params
    assert 'image.jpg' == FileDownloader.temp