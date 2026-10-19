

# Generated at 2022-06-14 17:58:39.662013
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .common import devnull
    class FakePostProcessor(PostProcessor):
        def __init__(self, dl):
            super(FakePostProcessor, self).__init__(dl)
            self.utime_tried_files = []

        def try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
            self.utime_tried_files.append((path, atime, mtime, errnote))
            return super(FakePostProcessor, self).try_utime(path, atime, mtime, errnote)

    # Test try_utime

# Generated at 2022-06-14 17:58:50.630177
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time, sys, os
    if sys.platform == 'win32':
        import _winapi # pylint: disable=import-error
        _ = _winapi.CreateFile( # pylint: disable=unused-variable
            '.\\utime_test.txt',
            _winapi.GENERIC_WRITE,
            0, None, _winapi.CREATE_ALWAYS, 0, None)
        fp = '.\\utime_test.txt'
    else:
        fp = './utime_test.txt'
    f = open(fp, 'w')
    f.write('test')
    f.close()
    p = PostProcessor(None)

# Generated at 2022-06-14 17:59:01.768760
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..extractor import gen_extractors
    from ..utils import sanitize_open
    import tempfile
    import shutil
    import sys
    import os

    def load_extractor(self, ie_key):
        return gen_extractors()[ie_key]

    def get_temp_filename(self, filename):
        tempdir = tempfile.mkdtemp(prefix='youtubedl_test_' + self.params['outtmpl'].replace('%(ext)s', '').replace('%(autonumber)s', ''))
        return os.path.join(tempdir, filename)

    def report_error(self, *args):
        pass

    def report_warning(self, *args):
        pass


# Generated at 2022-06-14 17:59:11.072764
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import YoutubeIE
    from ..utils import unescapeHTML
    from ..downloader import get_suitable_downloader

    class FakeInfoExtractor(object):
        IE_NAME = 'test:fake'

    class FakePostProcessor(PostProcessor):
        def run(self, information):
            inf = {
                'title': 'Fake title',
                'ex_fake_info': 'fake informations',
                # 'upload_date': '20130617'
            }
            inf.update(information)
            information = inf

            # Create a fake file
            path = os.path.join(self._downloader.get_setting('ydl_cookie_jar'), 'temp_file')
            tmp_file = open(encodeFilename(path), 'wb')
            tmp_file.close()

            # Set filepath

# Generated at 2022-06-14 17:59:22.511938
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import os
    import tempfile
    import shutil
    import filecmp
    from ..downloader import FakeInfoExtractor

    # create temporary directory
    tmpdir = tempfile.mkdtemp(prefix='youtube-dl-postprocessor-test-')

    # create a file
    (handle, fn) = tempfile.mkstemp(prefix='test.txt-', dir=tmpdir)
    os.write(handle, b'aaaaaaaaaa')
    os.close(handle)

    # create test pp
    class TestPP(PostProcessor):
        def run(self, info):
            atime = int(time.time())
            mtime = int(time.time()) - 3600
            self.try_utime(fn, atime, mtime)
            return [], info

    # run test pp
   

# Generated at 2022-06-14 17:59:28.888637
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import time

    class FakeDownloader:
        def report_warning(self, msg):
            warnings.append(msg)

    pp = PostProcessor(downloader=FakeDownloader())
    pp.try_utime(__file__, 12345, 12345, 'test utime')
    assert os.path.getmtime(__file__) == time.gmtime(12345).tm_sec
    pp.try_utime(__file__, 12344, 12344, 'test utime')
    assert warnings[0] == 'test utime'

# Generated at 2022-06-14 17:59:38.395818
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import try_encode

    def _atime_mtime(path):
        st = os.stat(try_encode(path))
        return st.st_atime, st.st_mtime

    def _utime(path, atime, mtime):
        os.utime(try_encode(path), (atime, mtime))

    import tempfile
    import shutil
    import time


# Generated at 2022-06-14 17:59:48.922731
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader

    pp = PostProcessor(downloader=Downloader('test'))

    try:
        os.utime('file', (1, 2))
    except OSError as e:
        if e.errno == 2:
            class file(object):
                def __init__(self, path, mode):
                    pass
            file.__name__ = 'file'
            # monkey patching
            builtins_open = __builtins__['open']
            __builtins__['open'] = file
            pp.try_utime('file', 1, 2)
            assert 1 == 1
            # restore
            __builtins__['open'] = builtins_open
        else:
            raise

# Generated at 2022-06-14 17:59:50.705155
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert False, "Test not implemented"



# Generated at 2022-06-14 18:00:02.420560
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os as real_os
    import shutil
    import tempfile
    import sys

    def make_file(path, atime, mtime):
        fd, tmpname = tempfile.mkstemp(dir=os.path.dirname(path))
        with os.fdopen(fd, 'w') as f:
            f.write('')
        os.utime(tmpname, (atime, mtime))
        shutil.move(tmpname, path)

    # Make a temporary directory
    tmp = tempfile.mkdtemp()

# Generated at 2022-06-14 18:00:13.111143
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import calendar
    import time
    from subprocess import Popen, PIPE, STDOUT

    class DummyDownloader():
        def report_warning(self, errnote):
            print('Warning:', errnote)

    d = DummyDownloader()

    pp = PostProcessor(downloader=d)

    tmpdir = tempfile.mkdtemp()

    # Create test file
    f = tempfile.NamedTemporaryFile(dir=tmpdir, delete=False)
    f = open(f.name, 'w')
    f.write("foo")
    f.close()

    # Modify modification and access time

# Generated at 2022-06-14 18:00:25.919910
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .common import FakeYDL
    from .test_postprocessor_common import PostProcessorTestCase

    class DummyPostProcessor(PostProcessor):
        def __init__(self, *args, **kwargs):
            super(DummyPostProcessor, self).__init__(*args, **kwargs)
            self.can_update_utime_called = False
            self.update_utime_called_times = 0

        def can_update_utime(self):
            self.can_update_utime_called = True

        def try_utime(self, *args, **kwargs):
            self.update_utime_called_times += 1


# Generated at 2022-06-14 18:00:36.764444
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..downloader.http import HttpFD
    from ..downloader.http.http import HEADRequest

    class FakeFileDownloader(FileDownloader):
        def __init__(self, fake_postprocessor):
            super(FakeFileDownloader, self).__init__()
            self.fake_postprocessor = fake_postprocessor

        def to_screen(self, *args, **kargs):
            pass

        def report_warning(self, msg, *args, **kargs):
            self.warnings.append(msg % args)

    class HttpFdTest(HttpFD):
        def __init__(self, *args, **kargs):
            self._extra_info = {}
            super(HttpFdTest, self).__init__(*args, **kargs)



# Generated at 2022-06-14 18:00:38.989035
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Test PostProcessor.try_utime() by mocking _downloader"""
    # TODO

# Generated at 2022-06-14 18:00:43.514481
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader
    fd = FileDownloader(None)
    pp = PostProcessor(fd)
    path = "nonexistant/file"
    # Do not throw exception when file does not exist
    pp.try_utime(path, 0.0, 0.0)
    # TODO: test that we can update existing file times

# Generated at 2022-06-14 18:00:49.655635
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    pp = PostProcessor(downloader=FileDownloader({}))
    path = encodeFilename('what ever')
    atime = 1383719449.01
    mtime = 1383719449.01
    errnote = 'Cannot update utime of file'
    try:
        os.utime(path, (atime, mtime))
    except Exception:
        raise
    return

# Generated at 2022-06-14 18:00:59.508732
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DownloaderMock(object):
        def __init__(self):
            self.warning_count = 0
        def report_warning(self, message):
            self.warning_count += 1

    class PostProcessorMock(PostProcessor):
        def run(self, info):
            self.try_utime(info['filepath'], 1, 2, 'errnote')
            return [], info

    import pytest
    import tempfile
    import os
    import time
    downloader = DownloaderMock()
    p = PostProcessorMock(downloader)
    (fd, filepath) = tempfile.mkstemp()
    f = os.fdopen(fd, 'wb+')
    info = {'filepath': filepath}

# Generated at 2022-06-14 18:01:10.060472
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import DateRange
    from .xattr_pp import XAttrMetadataPP
    import datetime

    class TestPP(XAttrMetadataPP):
        def __init__(self, downloader):
            XAttrMetadataPP.__init__(self, downloader)
            self.NOTICE = []

        def _write_string(self, filename, string, namespace, key):
            if string is None:
                if key == 'user.ytdl.filesize':
                    string = 'testing'
            return XAttrMetadataPP._write_string(self, filename, string, namespace, key)

        def report_notice(self, msg, *args):
            self.NOTICE.append(msg % args)


# Generated at 2022-06-14 18:01:21.493568
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import stat

    output_file = tempfile.NamedTemporaryFile(delete=False)
    output_file.write(b'data')
    output_file.close()

    class TmpDownloader(object):
        def report_warning(self, msg):
            print(msg)

    class TmpPostProcessor(PostProcessor):
        pass

    pp = TmpPostProcessor(TmpDownloader())
    os.utime(output_file.name, (0, 0))
    # Try update utime of file on read-only filesystem
    s = os.stat(output_file.name)
    os.chmod(output_file.name, s.st_mode & ~stat.S_IWRITE)

# Generated at 2022-06-14 18:01:26.781496
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import os

    test_file = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-14 18:01:32.737191
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    path = '/tmp/youtubedl_test_file'
    with open(path, 'w') as fh:
        fh.write('hi')
    pp.try_utime(path, 100, 101)

# Generated at 2022-06-14 18:01:42.223386
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # This test is based in a real use case of this method
    # encoder_rtmpdump.py calls self.try_utime with a fictitious path '.'
    # and an arbitrary mtime and atime
    pp = PostProcessor()
    pp.try_utime('.', 1523299131, 1523299131)
    pp.try_utime(bytes('.', 'utf-8'), 1523299131, 1523299131)
    pp.try_utime(u'.', 1523299131, 1523299131)

    assert True

# Generated at 2022-06-14 18:01:55.818724
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    sys.stderr.write('Testing PostProcessor.try_utime\n')
    from ..YoutubeDL import YoutubeDL
    import tempfile
    tmpf = tempfile.NamedTemporaryFile()
    tmpf.close()
    dler = YoutubeDL({'outtmpl': tmpf.name})
    tmpdler = YouTubeDL({'outtmpl': tmpf.name})
    postproc = PostProcessor(dler)

    # Test with an existing file
    tmpf = open(tmpf.name, 'w')

# Generated at 2022-06-14 18:02:02.719951
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    pp = PostProcessor(YoutubeDL())

    if not os.path.exists('testfile'):
        with open('testfile', 'w') as f:
            f.write('test file')

    os.utime('testfile', (1000, 2000))
    pp.try_utime('testfile', 3000, 4000)

    assert os.path.getatime('testfile') == 3000
    assert os.path.getmtime('testfile') == 4000

    # test on nonexistent files
    pp.try_utime('nonexistent', 1000, 2000, '')

    # cleanup
    os.remove('testfile')

# Generated at 2022-06-14 18:02:14.966189
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import os
    import datetime
    from ..utils import DateRange

    class TestPP(PostProcessor):
        def __init__(self, downloader):
            super(TestPP, self).__init__(downloader)

        def run(self, info):
            past = (datetime.datetime.now() - datetime.timedelta(hours=1)).timetuple()
            self.try_utime(info['filepath'], past.tm_atime, past.tm_mtime, errnote='Cannot update utime of file')
            return [], info

    from .fake_downloader import FakeYDL
    from .common import FakeYDLHandler

    with open('test_output.tmp', 'w') as f:
        f.write('hello world')


# Generated at 2022-06-14 18:02:27.198615
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .test_postprocessor import PostProcessorTestHelper
    from .test_postprocessor import expected_warning, expected_error

    # create YoutubeDL object
    ydl = YoutubeDL()

    # create PostProcessor object and set downloader
    pp = PostProcessorTestHelper(ydl)

    # call mocked os.utime and test that we call report_warning with default value
    pp.try_utime_mockos()
    expected_warning('Cannot update utime of file')

    # call mocked os.utime and test that we call report_warning with custom value
    pp.try_utime_mockos(errnote='test value')
    expected_warning('test value')

    # call mocked os.utime and test that we call report_error
    pp.try_utime

# Generated at 2022-06-14 18:02:28.592991
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """test try_utime of class PostProcessor"""
    pass

# Generated at 2022-06-14 18:02:37.511702
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import sys

    if sys.version_info >= (3, 0):
        from unittest import mock

    else:
        import mock

    from .common import PostProcessorTestCase

    class TestPostProcessor(PostProcessor):
        def run(self, info):
            self.try_utime(info['filepath'], 1, 2)
            return [], info

    local_path = os.path.abspath('file')
    with mock.patch('os.utime', side_effect=Exception):
        with PostProcessorTestCase(local_path) as test:
            _, _ = test.run_post_processor(TestPostProcessor)

            test.downloader.to_stderr.assert_called_once_with('Cannot update utime of file')

# Generated at 2022-06-14 18:02:45.311325
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        os.mkdir('testval')
    except OSError:
        pass # directory already exists
    f = open(os.path.join('testval', 'a'), 'w')
    f.write('hello')
    f.close()
    f = open(os.path.join('testval', 'b'), 'w')
    f.write('goodbye')
    f.close()
    pp = PostProcessor('dummy')
    pp.try_utime(os.path.join('testval', 'a'), 0, 0, errnote='Cannot updaet utime')
    pp.try_utime(os.path.join('testval', 'b'), -1, -1, errnote='Cannot updaet utime')

    # clean up

# Generated at 2022-06-14 18:02:53.826944
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import FakeDownloader
    from time import time
    pp = PostProcessor(FakeDownloader())
    for path, atime, mtime, errnote in [
            ('path/to/file.txt', time() - 1200, time() - 1200, None),  # normal case
            ('/', None, None, 'Cannot update utime of file'),  # path is not a file
            ('path/to/file.txt', time() + 1200, time() + 1200, 'Cannot update utime of file')]:  # future time
        try:
            pp.try_utime(path, atime, mtime, errnote)
        except Exception:
            pass

# Generated at 2022-06-14 18:03:06.345236
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractor
    from ..downloader import gen_downloader

    class MockPP(PostProcessor):
        def __init__(self, downloader):
            super(MockPP, self).__init__(downloader)

            # When utime raises TypeError, it is not considered as an error
            # https://github.com/ytdl-org/youtube-dl/issues/13250
            self.fail_on_utime = False

        def run(self, information):
            super(MockPP, self).run(information)
            _, information = super(MockPP, self).run(information)

            information['filepath'] = os.path.join(os.getcwd(), 'test.mp4')
            open(information['filepath'], 'a').close()  # Create an empty

# Generated at 2022-06-14 18:03:11.901097
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestClass(PostProcessor):
        def try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
            return PostProcessor.try_utime(self, path, atime, mtime, errnote)

    t = TestClass()
    t._downloader = type('DummyYDL', (object,), dict(params=dict(), report_warning=lambda self, x:None))()
    path = 'test'
    t.try_utime(path, 1, 2)

# Generated at 2022-06-14 18:03:19.721631
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    ydl = YoutubeDL({})
    pp = PostProcessor(ydl)

    with patch('os.utime') as patcher:
        patcher.side_effect = IOError()
        pp.try_utime('', 0, 0)
        ydl.to_screen.assert_called_with('[debug] Cannot update utime of file')

# Generated at 2022-06-14 18:03:28.247745
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Unitary test for try_utime method of PostProcessor class.
    """
    import time
    import shutil
    import tempfile

    # Create temp dir
    temp_dir = tempfile.mkdtemp(prefix='yt-dl-test-utime')

    # Use temp dir to create a temp file with specific name
    temp_file_path = os.path.join(temp_dir, "temp_file")
    with open(temp_file_path, mode="w") as tmp_f:
        tmp_f.write("Downloader")

    # Get file stats
    temp_file_mtime = os.path.getmtime(temp_file_path)

    # Try to change mtime to now, and check it has changed
    now = time.time()
    pp = PostProcessor(None)
   

# Generated at 2022-06-14 18:03:38.343024
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import os
    import stat
    from ..YoutubeDL import YoutubeDL
    from ..utils import encodeFilename, decodeFilename

    def _test(filename, expected_atime, expected_mtime):
        ydl = YoutubeDL()
        pp = PostProcessor(ydl)
        # Update access and modification times of the file
        pp.try_utime(encodeFilename(filename), expected_atime, expected_mtime, errnote='test')
        # Check file metadata after method try_utime
        st = os.stat(encodeFilename(filename))
        atime = int(st.st_atime)
        mtime = int(st.st_mtime)
        return atime, mtime

    def _test_equal(filename, expected_atime, expected_mtime):
        atime, mtime

# Generated at 2022-06-14 18:03:48.048512
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import time
    import unittest
    from ..compat import (
        compat_os_path,
        compat_urllib_error,
    )

    from .fake_filesystem_unittest import TestCase
    from .fake_http_server import (
        FakeHTTPServer,
        TCP_SERVER_ADDRESS,
        TCP_SERVER_PORT,
    )


# Generated at 2022-06-14 18:03:59.066544
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import errno
    from tempfile import mkstemp
    from queue import Queue
    from subprocess import PIPE
    from shutil import rmtree
    import unittest
    from sys import version_info
    from threading import Thread
    from time import sleep
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    class MockDownloader(object):
        def __init__(self):
            self.params = {'verbose': False}
            self.to_screen = self.to_stdout = None
            self.to_stderr = lambda s: print(s, file=sys.stderr)
            self.to_console_title = None
            self.to_file = None
            self.filesystem_encoding = sys.getfilesystemencoding()

# Generated at 2022-06-14 18:04:05.209865
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    downloader = lambda: None
    downloader.report_warning = lambda x: None
    pp = PostProcessor(downloader)
    try:
        pp.try_utime(None, 0, 0)
    except Exception:
        assert False, 'PP failed to update utime of file'
    assert True, 'PP successfully updated utime of file'

# Generated at 2022-06-14 18:04:14.187287
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import os
    import time
    import datetime
    from utils import DateRange

    tmp_dir = tempfile.mkdtemp()


# Generated at 2022-06-14 18:04:18.341917
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyDownloader(object):
        def report_warning(self, mess):
            pass
    pp = PostProcessor(DummyDownloader())
    # should not raise any exception
    pp.try_utime('/tmp/nonexistent', 1, 1)

# Generated at 2022-06-14 18:04:30.220387
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Some old version of youtube-dl don't have a PostProcessor
    class, this method tests if a current version of youtube-dl
    has it.
    """
    import youtube_dl.postprocessor
    assert youtube_dl.postprocessor.PostProcessor(None).try_utime
    assert youtube_dl.postprocessor.PostProcessor(None).try_utime('', 0, 0)

# Generated at 2022-06-14 18:04:41.053594
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    from ..compat import open
    from ..utils import DateRange
    from tempfile import mkdtemp
    import time
    import os

    def write_file(f):
        f.write(b'Test of try_utime')
        f.close()

    def write_and_open(temp_dir):
        f = open(os.path.join(temp_dir, 'test_try_utime'), 'wb')
        write_file(f)
        return open(os.path.join(temp_dir, 'test_try_utime'), 'rb')

    temp_dir = mkdtemp()
    f = write_and_open(temp_dir)

    os.utime(f.name, (0, 0))
    post_processor = PostProcessor(None)

# Generated at 2022-06-14 18:04:51.788749
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from youtube_dl.YoutubeDL import YoutubeDL
    from tempfile import mkdtemp
    from shutil import rmtree
    from yt_dl_postprocessor.postprocessor import PostProcessor

    tmpdir = mkdtemp()

    f = open(tmpdir + '/test.txt', 'w')
    f.close()

    import time
    atime = time.time() - 3600
    mtime = time.time() - 10

    pp = PostProcessor(None)
    pp.try_utime(tmpdir + '/test.txt', atime, mtime)

    f = open(tmpdir + '/test.txt', 'r')
    f.close()

    os.remove(tmpdir + '/test.txt')

    import shutil
    shutil.rmtree(tmpdir)
    
    return True

# Generated at 2022-06-14 18:04:58.985660
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import calendar
    import datetime
    import time
    from ..utils import (
        match_filter_func,
        DownloadContext,
        FileDownloader,
        PostProcessor,
        YoutubeDL,
    )
    file_size = 1024
    # Writing file
    test_file_path = tempfile.mkstemp()[1]
    with open(test_file_path, 'wb') as out_file:
        out_file.write(file_size * 'a')
    # First info object for writing utime

# Generated at 2022-06-14 18:05:09.704824
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile
    from datetime import datetime, timedelta

    import pytest
    from ..utils import (
        date_from_str,
        DateRange
    )

    # Test that try_utime success
    class TestDownloader:
        def __init__(self, report_warning):
            self.report_warning = report_warning
    def test_report_warning(msg):
        assert msg == 'Cannot update utime of file'

    pp = PostProcessor(TestDownloader(test_report_warning))
    with NamedTemporaryFile('w') as f:
        f.write('test')
        f.flush()
        # Get the file creation time

# Generated at 2022-06-14 18:05:20.378843
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    from .utils import DateRange
    from .downloader.common import FileDownloader
    from .compat import is_py2

    tmpdir = tempfile.mkdtemp()

    # Create a temp file with a random utime
    fd, path = tempfile.mkstemp(dir=tmpdir)
    os.close(fd)
    stat = os.stat(encodeFilename(path))

    # Creating a downloader
    params = {
        'nopart': True,
        'fixup': 'detect_or_warn',
        'outtmpl': '%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessor_args': '-ar 44100',
        'keepvideo': True,
    }
    d

# Generated at 2022-06-14 18:05:30.706175
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Create a PostProcessor object
    pp = PostProcessor()
    # Patch pp._downloader.report_warning to check if the error message is correctly set
    pp._downloader = Mock()

    # Prepare a file
    with open("test_PostProcessor_try_utime", 'wb') as f_out:
        f_out.write("This is a test file")

    # Update file time
    pp.try_utime("test_PostProcessor_try_utime", 1598964473, 1598964473)

    # Check if the file time is updated
    assert os.path.getmtime("test_PostProcessor_try_utime") == 1598964473
    # Check if the error message was not printed This method returns a tuple, the first element is a list of the files
    assert pp._downloader.report_

# Generated at 2022-06-14 18:05:43.167404
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # TODO Probably better, faster, more robust way to test file modification time
    from tempfile import mkstemp
    from time import time

    # Create a temporary file and write to it
    handle, tmp = mkstemp()
    with open(tmp, 'wb') as f:
        f.write(b'test')

    # Get modification time of the temporary file
    stat = os.lstat(tmp)
    atime = stat.st_atime
    mtime = stat.st_mtime

    # Modify time a second before and after the file was written
    atime_delta = -1
    mtime_delta = 1
    new_atime = atime + atime_delta
    new_mtime = mtime + mtime_delta

    # Create new Downloader object
    downloader = object()


# Generated at 2022-06-14 18:05:50.491804
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import time
    import unittest
    from .make_tmpdir import make_tmpdir
    from .downloader import Downloader

    class TestPP(PostProcessor):
        pass

    class TestDownloader(Downloader):
        """Test Downloader that can be used with PostProcessor class"""
        def is_fake_infile_valid(self, infile):
            """Determine if the fake infile is valid."""
            return path_exists(infile)

        def report_warning(self, message):
            """Report a warning."""
            self.reported_warnings.append(message)

    def path_exists(infile):
        """Determine if the path exists."""
        return os.path.exists(infile)


# Generated at 2022-06-14 18:06:02.519977
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import datetime

    # prepare some files to be created on file system
    # 1. file should exists
    # 2. file should be newer than last day
    # 3. file should be older than last day
    # 4. file should be newer than last day
    # 5. file should be older than last day
    # 6. file should be older than last day
    # 7. file should be older than last day
    # 8. file should be older than last day
    time_of_current_hour = time.time() - time.time() % 3600
    time_of_last_day = time_of_current_hour - 3600 * 24
    time_of_last_hour = time_of_last_day + 3600 * 23

    # file exists
    file1 = tempfile.TemporaryFile

# Generated at 2022-06-14 18:06:24.070009
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)  # test PostProcessor instance
    f = open('/tmp/test_ytdl_try_utime', 'w')
    f.close()  # create test file
    pp.try_utime('/tmp/test_ytdl_try_utime', 100000, 200000)  # test utime
    os.remove('/tmp/test_ytdl_try_utime')  # delete test file

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:06:33.101383
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import subprocess
    import tempfile
    import time
    from ..utils import PostProcessor

    class MockDownloader(object):
        def report_warning(self, msg):
            self.warning = msg

    class MockFile(object):
        def __init__(self, name):
            self.name = name
            self.fd = open(name, 'wb')

        def write(self, data):
            self.fd.write(data)

        def close(self):
            self.fd.close()

    files_to_delete = []

    def my_remove(filepath):
        global files_to_delete
        files_to_delete.append(filepath)

    def my_utime(filepath, atime, mtime):
        raise Exception('utime failed')

    pp = PostProcessor

# Generated at 2022-06-14 18:06:43.770160
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import FakeYDL
    from . import (
        FFmpegPostProcessor, FFmpegMetadataPP, FFmpegExtractAudioPP,
        XAttrMetadataPP,
        EmbedThumbnailPP,
        FixupStupidTagsPP,
        DescriptionPP,
        IdPP,
        YoutubeDlPP,
    )
    import os
    import os.path
    import tempfile
    import shutil
    import subprocess
    from datetime import datetime, timedelta

    # Move to a temporary directory
    temp_dir = tempfile.mkdtemp()
    old_dir = os.getcwd()
    os.chdir(temp_dir)

    # Take a file
    test_file = os.path.join(old_dir, 'test', 'test.mp3')

    # The timestamp of test.

# Generated at 2022-06-14 18:06:55.081777
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil
    import tempfile
    fd, temp_path = tempfile.mkstemp(prefix='youtubedl-test_')
    os.close(fd)

    try:
        t = time.time()
        pp = PostProcessor(None)
        # touch file
        pp.try_utime(temp_path, 0, 0)

        # test atime and mtime were updated
        assert t <= os.path.getatime(temp_path)
        assert t <= os.path.getmtime(temp_path)

        # test negative mtime
        pp.try_utime(temp_path, 0, -1)
        assert os.path.getmtime(temp_path) <= 0

    finally:
        os.unlink(temp_path)

# Generated at 2022-06-14 18:07:04.951193
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import sys

    class FakeDownloader():
        def __init__(self, warn_note):
            self.warn_note = warn_note

        def report_warning(self, note):
            self.warn_note = note

    class FakePostProcessor():
        def __init__(self, downloader):
            self.downloader = downloader

        def try_utime(self, *args, **kwargs):
            super(FakePostProcessor, self).try_utime(*args, **kwargs)

    test_file = 'test_utime.txt'
    with open(test_file, 'w'):
        pass
    stat = os.stat(test_file)
    utime_list = [stat.st_atime, stat.st_mtime]

    # a failed try_utime

# Generated at 2022-06-14 18:07:08.929373
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime('cp949-win.txt', 1, 2, '')
    pp.try_utime('cp949-unix.txt', 1, 2, '')

# Generated at 2022-06-14 18:07:18.048147
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockOs:
        def __init__(self):
            self.called = []
        def utime(self, path, t):
            self.called.append((path, t))

    class MockDownloader:
        def __init__(self):
            self.warned = []
        def report_warning(self, msg):
            self.warned.append(msg)

    pp = PostProcessor(downloader=MockDownloader())
    pp.os = MockOs()

    # Test utime cannot be updated
    pp.try_utime('path', 100, 200)
    assert pp.os.called == [('path', (100, 200))]
    assert pp.downloader.warned == ['Cannot update utime of file']

    # Test utime can be updated

# Generated at 2022-06-14 18:07:28.146935
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    # Test PostProcessor.try_utime
    import shutil
    import stat
    import time
    import tempfile
    import unittest

    class FakeDownloader(object):
        """Fake Downloader class.

        It simulates the behavior of the downloader, without actually
        downloading the file."""

        def __init__(self):
            self._num_warnings = 0

        def report_warning(self, message):
            """Fake report_warning.

            It simply counts the number of warnings reported."""
            self._num_warnings += 1

    class TestPostProcessor(PostProcessor):
        """TestPostProcessor class.

        It's a dummy PostProcessor for testing the try_utime method.
        """


# Generated at 2022-06-14 18:07:35.264396
# Unit test for method try_utime of class PostProcessor

# Generated at 2022-06-14 18:07:42.826618
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test if the method try_utime of class PostProcessor throw
    an exception when the file does not exist
    """
    import errno

    class Dummy(object):
        def __init__(self):
            self.params = {}

        def report_warning(self, errnote):
            raise Exception(errnote)

    class PP(PostProcessor):
        def __init__(self):
            self._downloader = Dummy()

    pp = PP()
    try:
        pp.try_utime('', None, None)
    except Exception as e:
        if 'No such file' in str(e):
            return True
        raise
    raise Exception('Exception not raised')



# Generated at 2022-06-14 18:08:21.107698
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import os
    import os.path

    filename = 'test'
    directory = 'testing'

    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, filename)

    open(file_path, 'wb')

    t = PostProcessor(None)
    t.try_utime(file_path, 1000, 2000)

    atime, mtime = os.stat(file_path)[7:9]
    assert abs(atime- 1000) <= 1, 'Error updating access time'
    assert abs(mtime- 2000) <= 1, 'Error updating modification time'

    shutil.rmtree(temp_dir)


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:08:29.648188
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test try_utime
    """
    import sys
    import tempfile
    from .downloader import Downloader

    if sys.platform == 'win32':
        import ctypes
        from .compat import compat_ctypes_win32
        from .compat import compat_opath

        # win32 doesn't allow setting file creation time
        # see http://bugs.python.org/issue13684
        # so we have to set the date by hand,
        # and this function is only used when converting audio,
        # so we don't need to support more than 1 second precision
        def set_file_creation_time(path, d_time):
            compat_ctypes_win32.CreateFileW.restype = ctypes.c_void_p