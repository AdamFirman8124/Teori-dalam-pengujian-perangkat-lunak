

# Generated at 2022-06-14 17:58:38.442308
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MyPostProcessor(PostProcessor):
        def __init__(self):
            super(MyPostProcessor, self).__init__()
            self.atime = None
            self.mtime = None

        def run(self, information):
            self.try_utime(information['filepath'], self.atime, self.mtime)
            return [], information  # by default, keep file and do nothing

    import mock
    import time

    pp = MyPostProcessor()
    pp.atime = 100
    pp.mtime = 200
    with mock.patch('os.utime') as mock_utime, mock.patch('time.time') as mock_time:
        mock_time.return_value = 100
        pp.run({'filepath': 'some/path'})

# Generated at 2022-06-14 17:58:39.286997
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    raise NotImplementedError

# Generated at 2022-06-14 17:58:44.655679
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    # create a temporary file
    from tempfile import mkstemp as create_temporary_file
    import time
    (test_file_descriptor, test_filepath) = create_temporary_file()
    os.close(test_file_descriptor)
    ydl = YoutubeDL()
    pp = PostProcessor(ydl)
    # test_file is already created, so we should not be able to set its creation time
    pp.try_utime(test_filepath, 0, 0)
    # we should be able to set its modification time
    pp.try_utime(test_filepath, time.time(), time.time())

# Generated at 2022-06-14 17:58:56.985748
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .common import FakeFile
    from tempfile import mkdtemp
    from os import utime, utime, remove, rmdir
    from time import time
    from datetime import datetime


# Generated at 2022-06-14 17:59:00.161612
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import FakeYDL
    f = FakeYDL()
    p = PostProcessor(f)
    p.try_utime(None, None, None)

# Generated at 2022-06-14 17:59:09.807079
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import shutil
    import os.path

    tempdir = tempfile.mkdtemp()
    tempdir2 = tempfile.mkdtemp()
    shutil.copy2(os.path.join(os.path.dirname(__file__), 'test.mp3'), tempdir)
    filename_1 = os.path.join(tempdir, 'test.mp3')
    filename_2 = os.path.join(tempdir2, 'test.mp3')
    shutil.move(filename_1, filename_2)
    access_time = os.path.getatime(filename_2)
    modification_time = os.path.getmtime(filename_2)
    time.sleep(1)
    pp = PostProcessor(None)

# Generated at 2022-06-14 17:59:21.374855
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest

    class TestPostProcessor(PostProcessor):
        def run(self, information):
            self.try_utime('foo', 1, 1, 'bar')

    class PostProcessorTest(unittest.TestCase):
        def test_try_utime(self):
            testpp = TestPostProcessor()
            self.assertRaises(PostProcessingError, testpp.run, {})

    testsuite = unittest.TestSuite()
    testsuite.addTest(PostProcessorTest('test_try_utime'))
    return testsuite


if __name__ == '__main__':
    unittest.main(defaultTest='test_PostProcessor_try_utime')

# Generated at 2022-06-14 17:59:30.369876
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Python version
    from sys import version_info as _sys_version_info
    py_major = _sys_version_info.major
    py_minor = _sys_version_info.minor

    if py_major == 2:
        # Python 2
        import mock
        import __builtin__ as builtins
    elif py_major == 3:
        # Python 3
        import unittest.mock
        import builtins
    else:
        # unknown Python version
        raise Exception('Unknown Python version %s.%s' % (py_major, py_minor))

    # create PostProcessor instance and mock downloader
    class DummyDownloader:
        pass
    downloader = DummyDownloader()
    downloader.report_warning = mock.Mock(spec=lambda *a, **kw: None)

# Generated at 2022-06-14 17:59:39.192918
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    import time
    now = time.time()
    try:
        os.remove('testfile')
    except Exception:
        pass
    f = open('testfile', 'wb')
    f.write('a')
    f.close()
    try:
        os.remove('testfile_symlink')
    except Exception:
        pass
    os.symlink('testfile', 'testfile_symlink')
    pp.try_utime('testfile', now - 100, now - 200)
    assert os.stat('testfile').st_atime == now - 100
    assert os.stat('testfile').st_mtime == now - 200
    pp.try_utime('testfile_symlink', now - 100, now)

# Generated at 2022-06-14 17:59:48.481040
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import time
    import shutil
    import tempfile

    if sys.version_info[0] > 2:
        from io import StringIO as compat_StringIO
    else:
        from StringIO import StringIO as compat_StringIO

    tdir = tempfile.mkdtemp() + '.dir'
    os.mkdir(tdir)
    tmpfile = os.path.join(tdir, 'tmpfile')
    with open(tmpfile, 'w') as fte:
        fte.write('dummy information')

    def try_utime(path, atime, mtime):
        try:
            os.utime(encodeFilename(path), (atime, mtime))
        except:
            return False
        return True


# Generated at 2022-06-14 18:00:02.072153
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil

# Generated at 2022-06-14 18:00:08.983012
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .extractor import InfoExtractor
    from .downloader import FileDownloader

    ie = InfoExtractor()
    ie.set_downloader(FileDownloader({'outtmpl': '%(id)s'}))
    pp = PostProcessor(ie.params)
    extracted = {'id': 'foo'}
    pp.run(extracted)
    pp.try_utime('foo', 100, 200)



# Generated at 2022-06-14 18:00:15.680008
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakePostProcessor(PostProcessor):
        def __init__(self):
            self._downloader = {'params': {}}

    pp = FakePostProcessor()
    assert pp.try_utime('/path/to/file', 1, 2) is None
    assert pp.try_utime('/path/to/file', 1, 2, 'Error') is None
    assert pp.try_utime('/path/to/file', 1, 2, 'Error') is None

# Generated at 2022-06-14 18:00:26.617768
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time
    import stat
    import os

    filename = 'somefile.ext'
    tdir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:00:28.015526
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert True
    # TODO: implement test for method try_utime

# Generated at 2022-06-14 18:00:36.414259
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Test is performed only if utime is available
    if hasattr(os, 'utime'):
        from tempfile import TemporaryFile
        from datetime import datetime

        def test_utime(s, atime, mtime):
            pp = PostProcessor(None)

            # Create a dummy file and set current time
            f = TemporaryFile(mode='w+t')
            f.write(s)
            f.seek(0)
            now = datetime.now()

            # Use method try_utime and check if time modified is equal to the requested one
            pp.try_utime(f.name, atime, mtime)
            modified = datetime.fromtimestamp(os.stat(f.name).st_mtime)
            assert modified == mtime

            # Close file
            f.close()

        #

# Generated at 2022-06-14 18:00:44.978157
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Before using the method try_utime, the file must be exist.
    # Here, create a file and add a few lines in the file.
    f = open('a', 'w')
    f.write('test_PostProcessor_try_utime')
    f.close()  # close the file after writing.

    post_processor = PostProcessor()
    post_processor.try_utime('a', 0, 0, errnote='test_PostProcessor_try_utime')
    os.remove('a')  # finally, delete the file we created.


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:00:54.349181
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FileDownloader
    from ..__main__ import parseOpts

    # We need two directories to work with, one empty and another that exists
    # with a non-empty file in it, which will be used to test the call to utime
    # after deletion of the working file.
    import tempfile

    tempdir = None
    olddir = None
    testdir = None
    tempdir = tempfile.mkdtemp()
    olddir = tempfile.mkdtemp()
    testdir = tempfile.mkdtemp()
    tempfile.TemporaryFile(dir=olddir).close()


# Generated at 2022-06-14 18:01:04.539034
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile

    temp_dir = tempfile.gettempdir()
    pp = PostProcessor(downloader=None)
    filename = 'nonexistent_file'
    path = os.path.join(temp_dir, filename)
    try:
        os.remove(path)
    except OSError:
        pass

    assert not os.path.exists(path)
    pp.try_utime(path, 0, 0)
    assert not os.path.exists(path)

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:01:13.426806
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import os
    import datetime

    pp = PostProcessor(None)
    dir = tempfile.mkdtemp()
    path = os.path.join(dir, 'test.txt')
    with open(path, 'w') as f:
        f.write('foo')
    atime = os.path.getatime(path)
    mtime = os.path.getmtime(path)
    assert atime == mtime == os.path.getmtime(path)
    deltatime = datetime.timedelta(days=1)
    mtime += deltatime.total_seconds()
    mtime_new = os.path.getmtime(path)
    assert mtime_new == mtime
    atime_new = os.path.getatime

# Generated at 2022-06-14 18:01:17.259716
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:01:28.163103
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import re
    import sys
    import tempfile
    import shutil
    import subprocess

    # downloader for test
    class DummyDownloader(object):
        def __init__(self, warning_calls):
            self.warning_calls = warning_calls
        def report_warning(self, warning):
            self.warning_calls.append(warning)

    # post processor for test
    class DummyPostProcessor(PostProcessor):
        def run(self, info):
            return [], info

    # flag for avoid circular reference
    done_test_try_utime = [False]

    def test_PostProcessor_try_utime(path, sys_type, tmp_path, warning_calls):
        if done_test_try_utime[0]:
            return

       

# Generated at 2022-06-14 18:01:35.214777
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        os.mkdir("test_postprocessor_try_utime")
    except OSError:
        return

# Generated at 2022-06-14 18:01:39.032495
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Tests the method try_utime of the class PostProcessor.
    The method has to return None if the file exists and None
    if the file doesn't exist.
    """
    raise NotImplementedError

# Generated at 2022-06-14 18:01:46.860403
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from ..compat import setenv
    from subprocess import call

    # Make a temporary directory for testing
    import random
    import string
    import  tempfile
    tmpd = tempfile.mkdtemp()
    setenv('TEST_TMPDIR', tmpd)
    testf = tmpd + '/test_file'
    with open(testf, 'w') as f:
        f.write('test file')

    # Test without fail
    pp = PostProcessor(Downloader())
    pp.try_utime(testf, 1, 1)

    # Test with fail
    pp = PostProcessor(Downloader())
    pp.try_utime(testf + '2', 1, 1)

# Generated at 2022-06-14 18:01:55.156836
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    pp = PostProcessor(None)
    try:
        fd, fname = tempfile.mkstemp()
        test_file = open(fname, 'w')
        # If test file was created successfully
        if test_file:
            test_file.close()
            pp.try_utime(fname, 1, 1, errnote='test failing utime')
            os.close(fd)
            os.remove(fname)
    except Exception:
        pass

# Generated at 2022-06-14 18:01:57.445087
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime('nonexistent', 1388534400, 1388534400)

# Generated at 2022-06-14 18:02:00.540616
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    downloader = FileDownloader({'nopart': True, 'quiet': True})
    dp = PostProcessor(downloader)
    dp.try_utime('test_test.test', 1, 2)

# Generated at 2022-06-14 18:02:03.012601
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # run test_postprocessor_try_utime.sh
    from .test_postprocessor_try_utime import main as _main
    return _main()

# Generated at 2022-06-14 18:02:15.010872
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from io import BytesIO as StringIO
    from .test_test_test import FakeYDL
    pp = PostProcessor({})
    pp._downloader = FakeYDL()
    pp.try_utime('/path/to', 12345, 67890)
    assert pp._downloader.msgs == ['[debug] Cannot update utime of file']
    assert pp._downloader.msgs == []
    pp._downloader.params['verbose'] = True
    pp.try_utime('/path/to', 12345, 67890)
    assert pp._downloader.msgs == ['ERROR: Cannot update utime of file']

    f = StringIO()
    pp._downloader._downloaded_file_handle = f

# Generated at 2022-06-14 18:02:22.347116
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    filepath = './logo.png'
    open(filepath, 'w').close()
    pp.try_utime(filepath, 1, 2)
    pp.try_utime(filepath, 1, 2, 'Cant update utime')
    os.remove(filepath)

# Generated at 2022-06-14 18:02:32.890958
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import shutil
    from .utils import DateRange, ShellCommandResult

    from .postprocessor import PostProcessor

    tempdir = tempfile.mkdtemp()
    origpath = os.path.join(tempdir, 'origfile')
    newpath = os.path.join(tempdir, 'newfile')

    def set_mtime_command(mtime, filename):
        return ShellCommandResult(stdout='', stderr='', exit_code=0, cmd='touch -m -d @{} {}'.format(int(mtime), filename))


    touch_success_result = ShellCommandResult(stdout='', stderr='', exit_code=0, cmd='touch -m -d @{} {}'.format(0, origpath))
    touch_failure_result = ShellCommand

# Generated at 2022-06-14 18:02:43.917013
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time

    # Create a dummy post processor
    class DummyDownloader:
        def report_warning(self, msg):
            print(msg)

    pp = PostProcessor(DummyDownloader())

    # Create a sample file
    tmp_dir = tempfile.mkdtemp()
    tmp_file = os.path.join(tmp_dir, 'postprocessor_try_utime_test.txt')
    with open(tmp_file, 'w') as f:
        f.write(u'This is a test file for utime\n')

    # Check the current utime
    s = os.stat(tmp_file)
    atime_first = s.st_atime
    mtime_first = s.st_mtime
    atime_second = atime_first

# Generated at 2022-06-14 18:02:54.307383
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import pytest
    import datetime
    from ..compat import str, file

    class MockDownloader:

        def report_warning(self, errnote):
            self.errnote = errnote

    class MockPostProcessor(PostProcessor):

        def __init__(self, downloader):
            super(MockPostProcessor, self).__init__()
            self.downloader = downloader

    with open('test.txt', 'w') as f:
        f.write('test')
    time = lambda: datetime.datetime(2015, 6, 24, 12, 36, 18, dtype=datetime.datetime)
    with pytest.raises(Exception):
        atime = time()
        mtime = time()
        mock_downloader = MockDownloader()
        mock_post_processor = MockPostProcess

# Generated at 2022-06-14 18:03:04.453258
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..utils import DateRange
    from ..extractor.common import InfoExtractor
    from ..compat import compat_urllib_request
    def test_hook(dl):
        dl.params['max_downloads'] = 1
        dl.add_info_extractor(TestIE(dl))
    class TestIE(InfoExtractor):
        def __init__(self, ydl):
            InfoExtractor.__init__(self, ydl)
        def report_download_webpage(self, *args, **kargs):
            return self.report_extraction(
                *args, **kargs)

# Generated at 2022-06-14 18:03:12.601466
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from time import time
    from tempfile import mkstemp
    from shutil import rmtree
    from tempfile import mkdtemp
    from io import open
    from os import utime, path
    from youtube_dl.compat import compat_str

    orig_st = time()
    file = open(mkstemp()[1], 'wb')
    file.close()
    outdir = path.abspath(mkdtemp())
    path = path.join(outdir, compat_str(orig_st))
    os.rename(file.name, path)
    os.utime(path, (orig_st, orig_st))
    os.utime(path, (orig_st, orig_st))
    pp = PostProcessor(None)

# Generated at 2022-06-14 18:03:13.280273
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:03:20.990293
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # We don't want to touch the system while running the unit test
    import tempfile
    import time
    import shutil
    path = tempfile.mktemp()
    with open(path, 'wb') as f:
        f.write(b'Y')
    atime = time.time()
    time.sleep(1)
    mtime = time.time()
    pp = PostProcessor(None)
    pp.try_utime(path, atime, mtime)
    shutil.rmtree(path)

# Generated at 2022-06-14 18:03:25.042855
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime("test.py", 0, 0)
    # TODO: check that the result is correct. The try_utime call currently
    # hasn't got any side effects, but that might change in the future...
    # (e.g. when file(s) are created)

# Generated at 2022-06-14 18:03:27.696417
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert os.utime('abc', (1, 2)) == NotImplemented

# Generated at 2022-06-14 18:03:46.632806
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkstemp
    from datetime import datetime
    from shutil import rmtree
    import time
    import pytest
    import sys

    @classmethod
    def setUpClass():
        _, PostProcessor.tmpfile = mkstemp(suffix='.test', prefix='youtubedl_test_')

    @classmethod
    def tearDownClass():
        os.remove(PostProcessor.tmpfile)

    def setUp(self):
        self.downloader = lambda: None
        self.downloader.report_warning = lambda x: None
        self.test = PostProcessor(self.downloader)

    def test_utime_fails(self):
        self.test.try_utime(PostProcessor.tmpfile, None, None)


# Generated at 2022-06-14 18:03:57.796473
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import stat
    import shutil
    import tempfile
    import time
    import os

    t = tempfile.mkstemp('_pytube_test')
    os.close(t[0])
    filepath = t[1]

    atime = time.time() - 3000
    mtime = time.time() - 2000

    m_time = time.localtime()
    m_time = (m_time.tm_year, m_time.tm_mon, m_time.tm_mday, m_time.tm_hour, m_time.tm_min,
              m_time.tm_sec, m_time.tm_wday, m_time.tm_yday, m_time.tm_isdst)

    f = open(filepath, 'w')
    f.close()
    os.utime

# Generated at 2022-06-14 18:04:09.488135
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    # Mock try_utime
    import sys
    postProcessor = PostProcessor()
    def mock_utime(path, atime, mtime):
        postProcessor.utime_called = True
    def mock_report_warning(errnote):
        postProcessor.errnote = errnote

    postProcessor.utime = mock_utime
    postProcessor.report_warning = mock_report_warning

    # Test with a file path
    path = 'test.txt'
    atime = 123.0
    mtime = 456.0
    postProcessor.try_utime(path, atime, mtime)
    if not postProcessor.utime_called:
        sys.exit(2)
    if postProcessor.errnote:
        sys.exit(3)

    # Test with an exception

# Generated at 2022-06-14 18:04:19.334097
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyDownloader:
        def report_warning(self, errnote):
            pass

    class DummyPostProcessor(PostProcessor):
        def __init__(self, downloader, filepath):
            PostProcessor.__init__(self, downloader)
            self.filepath = filepath

        def run(self, information):
            return [], information

    def check_utime(atime, mtime, errnote):
        post = DummyPostProcessor(DummyDownloader(), 'dummy.mp3')
        post.try_utime(post.filepath, atime, mtime, errnote)

    check_utime(123456789.0, 135792468.0, 'Expected value')

# Generated at 2022-06-14 18:04:30.653117
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FakeYDL

    class PP(PostProcessor):

        def run(self, info):
            filepath = info['filepath']
            assert filepath.endswith('.mkv')
            self.try_utime(filepath, 0, 0, errnote='a test')
            return [filepath]

    ydl = FakeYDL()
    ydl.params['prefer_ffmpeg'] = False
    ydl.params['keepvideo'] = True

    info = {
        'id': 'abc',
        'title': 'abc',
        'formats': [{
            'format_id': 'VGA',
            'ext': 'mkv',
        }],
        '_type': 'video',
    }
    ret = PP(ydl).run(info)

# Generated at 2022-06-14 18:04:34.250480
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile

    with tempfile.NamedTemporaryFile() as f:
        a = PostProcessor()
        a.try_utime(f.name, time.time() - 1000, time.time() - 1000)

# Generated at 2022-06-14 18:04:45.625463
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import Downloader
    from .extractor import Extractor
    import hashlib
    import os
    import shutil
    import tempfile
    import time

    dummy_content = b'Dummy video'

    video_filename = 'video'

    class DummyExtractor(Extractor):
        def __init__(self):
            Extractor.__init__(self, 'Dummy Extractor')

        def extract(self, url):
            return [{
                'id': 'Dummy video',
            }]

    class DummyDownloader(Downloader):
        def __init__(self, params, extractor):
            Downloader.__init__(self, params)
            self._extractor = extractor

        def real_download(self, filename, info_dict):
            video_filename = filename

# Generated at 2022-06-14 18:04:55.599593
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    if sys.version_info >= (3, 0) and sys.platform.startswith('win'):
        # On Windows there is no way to update utime of a file
        import unittest.mock
        with unittest.mock.patch('os.utime') as utime:
            class DummyPP(PostProcessor):
                def __init__(self):
                    pass
            pp = DummyPP()
            pp.try_utime('/path/to/file', 1, 2)
            assert not utime.called
    else:
        import os
        import tempfile
        from .common import FakeYDL

        path = tempfile.mkstemp()[1]


# Generated at 2022-06-14 18:05:02.189843
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader():
        def report_warning(self, note):
            assert note == 'Cannot update utime of file'
    pp = PostProcessor(FakeDownloader())
    import time
    import tempfile
    f = tempfile.NamedTemporaryFile()
    t = time.time()
    pp.try_utime(f.name, mtime=t, atime=t)

# Generated at 2022-06-14 18:05:10.886625
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    from ..utils import save_to_file
    from ..compat import compat_open

    def write_able(func, path):
        """Decorator that wraps func so that it returns whether it was able
        to write to path."""
        def wrapper(path, *args):
            try:
                func(path, *args)
                return True
            except OSError:
                return False
        return lambda *args: wrapper(path, *args)

    fd, temp_path = tempfile.mkstemp()
    os.close(fd)

# Generated at 2022-06-14 18:05:32.669476
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import sys
    import shutil
    import tempfile
    import subprocess
    import stat

    def make_temp_file(name):
        with open(name, 'w'):
            pass

    def make_temp_dir(name, files):
        os.mkdir(name)
        for f in files:
            make_temp_file(os.path.join(name, f))

    def get_files(dir):
        return [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

    def get_dirs(dir):
        return [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]


# Generated at 2022-06-14 18:05:44.586044
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import prepend_extension
    from .common import FFmpegPostProcessor
    from .xattrpp import XAttrMetadataPP
    from .execafterdownload import ExecAfterDownloadPP

    # Initialize
    fd = FileDownloader({})
    fd.params['writethumbnail'] = True
    fd.params['embedthumbnail'] = True
    fd.params['outtmpl'] = '%(title)s.%(ext)s'
    fd.params['restrictfilenames'] = True
    fd.params['quiet'] = True
    pp0 = XAttrMetadataPP(fd)
    pp1 = FFmpegPostProcessor(fd)
    pp2 = ExecAfterDownloadPP(fd)

    # Prepare postprocessors' test

# Generated at 2022-06-14 18:05:55.628077
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # We cannot test except on Windows and Linux
    if os.name == 'nt':
        from ..utils import win32_get_uac_admin_rights
        with win32_get_uac_admin_rights():
            from . import _test_file
            from ..utils import sanitize_filename
            from ..compat import compat_tempfile
            tempdir = compat_tempfile.mkdtemp()
            filepath = os.path.join(tempdir, sanitize_filename(_test_file.name) + "test")
            with open(filepath, "wb") as f:
                f.write(b"test")


# Generated at 2022-06-14 18:06:04.550866
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # PostProcessor class is not supposed to be instantiated
    pp = PostProcessor()
    # Create a file with current time
    tmpfile = 'test_PostProcessor_try_utime.tmp'
    with open(tmpfile, 'wb') as f:
        f.write(b'foo')
    # Get file times
    (atime, mtime) = os.stat(tmpfile).st_atime, os.stat(tmpfile).st_mtime
    # Change mtime
    pp.try_utime(tmpfile, atime, mtime + 10)
    # Check mtime was changed
    assert os.stat(tmpfile).st_mtime == mtime + 10, 'Changing mtime failed'
    # Change atime
    pp.try_utime(tmpfile, atime + 10, mtime)


# Generated at 2022-06-14 18:06:13.154314
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkstemp
    from time import time
    from ..utils import FileDownloader
    from .infoextractors import gen_extractors
    from .xattrpp import XAttrMetadataPP

    downloader = FileDownloader({})
    downloader.add_info_extractor(gen_extractors(downloader))
    downloader.add_post_processor(XAttrMetadataPP(downloader))

    _, fpath = mkstemp(prefix='youtubedl_test_')
    test_time = time()


# Generated at 2022-06-14 18:06:24.070250
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import os

    tmpdir = tempfile.mkdtemp()
    path = os.path.join(tmpdir, 'test.txt')

    pp = PostProcessor(None)

    # path does not exist
    exc = None
    try:
        pp.try_utime(path, 0, 0)
    except Exception as err:
        exc = err
    assert isinstance(exc, PostProcessingError)

    open(path, 'w').close()

    assert os.path.getmtime(path) == os.path.getatime(path)

    # success
    pp.try_utime(path, 0, 100)

    assert os.path.getmtime(path) == 100
    assert os.path.getatime(path) == 0

    # success with float

# Generated at 2022-06-14 18:06:33.100594
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import compat_mock
    pp = PostProcessor()

    # Test case 1: Exception occurs
    with compat_mock.patch('ytdl.postprocessor.os') as mock_os:
        mock_os.utime.side_effect = Exception('Cannot update utime of file')
        pp.try_utime('any file', 'any atime', 'any mtime')
        mock_os.utime.assert_called_with('any file', ('any atime', 'any mtime'))
    # Test case 2: Exception doesn't occur
    with compat_mock.patch('ytdl.postprocessor.os') as mock_os:
        mock_os.utime.side_effect = None
        pp.try_utime('any file', 'any atime', 'any mtime')
        mock

# Generated at 2022-06-14 18:06:43.770961
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil

    from ..downloader import Downloader
    from ..utils import sanitize_open

    post = PostProcessor(Downloader())
    filename = os.path.join('temp_utime', 'original_video.mp4')
    os.makedirs(os.path.dirname(filename))
    f = sanitize_open(filename, 'w')
    f.write('abc')
    f.close()
    time.sleep(1)
    post.try_utime(filename, 100.0, 200.0, errnote='test try_utime')
    stat = os.stat(filename)
    shutil.rmtree('temp_utime')

# Generated at 2022-06-14 18:06:55.079735
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import filecmp
    import os
    import shutil
    import sys
    import tempfile

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    # If a directory is not available (e.g. /tmp), try another one
    tmpdir = tmpdir if os.path.isdir(tmpdir) else tempfile.mkdtemp()

    # Create a test file in the temporary directory
    test_file = 'test.txt'
    test_file_path = os.path.join(tmpdir, test_file)
    with open(test_file_path, 'w') as f:
        f.write('test')

    # Create a backup of the test file
    backup_file = test_file + '.bak'

# Generated at 2022-06-14 18:07:04.952073
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    try:
        from random import Random
        from tempfile import mktemp
        from test.test_support import run_unittest
        from unittest import TestCase
    except ImportError:
        return

    if sys.version_info < (2, 7):
        return

    class UtimeTest(TestCase):
        def setUp(self):
            self.tmpfile = mktemp()
            f = open(self.tmpfile, 'w')
            f.write('testing\n')
            f.close()

        def test_try_utime(self):
            # Basic test of set_utime
            import os
            import time
            import stat

            post_processor = PostProcessor(None)


# Generated at 2022-06-14 18:07:35.389718
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import re
    import subprocess
    import copy
    import threading
    import tempfile
    import sys
    import os
    import time
    import http.server
    import urllib

    class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            m = re.match(r'/([^/]+).mp3', self.path)
            if m:
                filename = m.group(1)
                self.send_response(200)
                self.send_header('Content-Type', 'audio/mpeg')
                self.end_headers()
                fp = open(os.path.join(tempdir, filename) + '.mp3', 'rb')
                fp.seek(offset)
                data = fp.read(length)
                fp.close()

# Generated at 2022-06-14 18:07:43.727935
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import subprocess
    import tempfile
    import shutil
    import datetime
    import stat
    import platform

    # We need to use a fixed timestamp, so we can compare it later
    timestamp = 1212313351.0

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a file which has mtime as mentioned timestamp
    subprocess.Popen(['/bin/touch', '--no-create', '-t',
                      '%12.0f' % timestamp, os.path.join(tmpdir, 'testfile')]).communicate()


# Generated at 2022-06-14 18:07:47.522636
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime(__file__, 1, 1)
    pp.try_utime(__file__ + '.nofile', 1, 1)

# Generated at 2022-06-14 18:07:52.287997
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def __init__(self):
            PostProcessor.__init__(self)
        def test_try_utime(self, path, atime, mtime):
            return self.try_utime(path, atime, mtime)
    TestPostProcessor().test_try_utime(__file__, 1000, 2000)

# Generated at 2022-06-14 18:08:03.132674
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil
    from .compat import get_filesystem_encoding
    from .downloader.common import FileDownloader

    def _mtime(*args):
        return int(round(time.mktime(args)))
    ML = 24 * 60 * 60  # Arbitrary number of milliseconds in a day

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp(prefix='youtube-dl-utime-test-')
    os.environ['TZ'] = 'GMT'
    time.tzset()


# Generated at 2022-06-14 18:08:11.267186
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import get_suitable_downloader
    from ..extractor import gen_extractors
    from ..utils import SameFileError
    pp = PostProcessor(downloader=get_suitable_downloader(None))
    ff = gen_extractors()[0]
    tfn = ff.test_file
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), tfn)
    info = {
        'filepath': filepath,
        'fulltitle': tfn,
        'ext': tfn.split('.')[-1],
        'title': tfn.split('.')[0],
    }
    assert info['filepath'] == filepath
    _, info = pp.run(info)
    os.remove(filepath)


# Generated at 2022-06-14 18:08:21.075786
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import PostProcessor

    class TestPostProcessor(PostProcessor):
        def run(self, information):
            self.try_utime(encodeFilename(information['filepath']), 1, 1)
            return [], information
    import tempfile
    import shutil
    import os
    import os.path
    import time

    fd, fpath = tempfile.mkstemp()
    os.close(fd)
    pp = TestPostProcessor()
    pp.run({'filepath': fpath})
    os.utime(encodeFilename(fpath), (time.time() + 200, time.time() + 200))
    now = time.time()
    pp.run({'filepath': fpath})
    assert os.stat(encodeFilename(fpath)).st_mtime <= now
   

# Generated at 2022-06-14 18:08:24.150907
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    try:
        pp.try_utime('nonexistent file', 1, 1, 'warning message')
    except AudioConversionError:
        print('AudioConversionError raised')
    else:
        print('AudioConversionError not raised')

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:08:34.894224
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FakeDownloader
    from .extractor import FakeInfoExtractor

    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader):
            self._downloader = downloader

    ie = FakeInfoExtractor()
    ie._ies = []

    ie.add_info_extractor(FakeInfoExtractor('foo'))
    ie.add_info_extractor(FakeInfoExtractor('bar'))
    ie._downloader = FakeDownloader({'username': 'ytdl'})
    ie._downloader.add_info_extractor(ie)
    pp = FakePostProcessor(ie._downloader)

    # Test without error
    pp.try_utime('/dev/null', 0, 0)
    assert ie._downloader._msgs == []

    # Test with error
