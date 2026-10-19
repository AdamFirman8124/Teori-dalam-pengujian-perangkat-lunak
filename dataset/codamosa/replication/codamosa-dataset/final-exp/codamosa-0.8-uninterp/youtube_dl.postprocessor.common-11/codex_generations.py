

# Generated at 2022-06-14 17:58:37.721452
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakePostProcessor:
        def __init__(self):
            pass

        def try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
            return os.utime(encodeFilename(path), (atime, mtime))

    pp = FakePostProcessor()
    import time
    filepath = './tests/test.mp4'
    test_stamp = int(time.time())
    pp.try_utime(filepath, test_stamp, test_stamp, '')
    utime_stamp = int(os.stat(filepath).st_mtime)
    assert utime_stamp == test_stamp



# Generated at 2022-06-14 17:58:44.525362
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time

    vfile = tempfile.mkstemp(suffix='.flv')[1]
    shutil.copyfile(os.path.join('tests', 'test.flv'), vfile)

    ctime = os.stat(vfile).st_ctime
    mtime = os.path.getmtime(vfile)

    pp = PostProcessor(None)

    pp.try_utime(vfile, ctime + 300, mtime)
    assert abs(mtime - os.path.getmtime(vfile)) < 1
    assert abs(ctime - os.stat(vfile).st_ctime) > 300

# Generated at 2022-06-14 17:58:50.586763
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyDownloader:
        def report_warning(self, msg, **kwargs):
            pass

    pp = PostProcessor(downloader=DummyDownloader())
    assert pp.try_utime('', 1, 1) is None

# Generated at 2022-06-14 17:58:57.942855
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Initialize PostProcessor
    pp = PostProcessor(None)
    # Create test file
    import tempfile
    fd, path = tempfile.mkstemp(prefix="ya-dl-test-pp-")
    os.close(fd)
    try:
        # Current time
        import time
        ctime = time.time()
        # Force file modification time
        pp.try_utime(path, ctime, ctime)
        # Check file modification time
        assert(int(os.stat(path).st_mtime + 0.5) == int(ctime + 0.5))
    finally:
        os.remove(path)

# Generated at 2022-06-14 17:59:06.652863
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FakeYDL
    from .downloader import FakeFD

    class TestablePostProcessor(PostProcessor):
        def run(self, info):
            return [], info

    fd = FakeFD()
    ydl = FakeYDL()
    pp = TestablePostProcessor(ydl)
    origname = 'somefilename'
    errnote = 'Cannot update utime of file'
    res = pp.try_utime(origname, -1, -1, errnote)
    assert None == res
    assert errnote in ydl.mock_warning

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 17:59:12.095533
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import datetime
    import tempfile
    class FakeDownloader:
        def __init__(self):
            self.reported_warnings = []
        def report_warning(self, msg):
            self.reported_warnings.append(msg)
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    with tempfile.NamedTemporaryFile() as f:
        name = f.name
    pp.try_utime(name, 0, 0)
    assert len(downloader.reported_warnings) == 0
    s = os.stat(name)
    now = time.time()
    pp.try_utime(name, now - 24 * 3600, now - 24 * 3600)
    s2 = os.stat(name)

# Generated at 2022-06-14 17:59:23.407011
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FileDownloader
    from .extractor.common import InfoExtractor

    class MockInfoExtractor(InfoExtractor):
        def __init__(self, downloader):
            InfoExtractor.__init__(self, downloader)
        
        def _real_extract(self, url):
            return {'id': url,
                    'title': url,
                    'ext': 'm4a',
                    'format_id': 'audio_format',
                    }

    class MockDownloader(FileDownloader):
        def __init__(self):
            FileDownloader.__init__(self)
            self.params['outtmpl'] = os.path.join(os.getcwd(), '%(id)s.%(ext)s')
            self.ie = MockInfoExtractor(self)


# Generated at 2022-06-14 17:59:34.192624
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time

    # Create a temporary directory & file
    _, fileName = tempfile.mkstemp(prefix='youtubedl-test',suffix='.tmp')
    dirName = tempfile.mkdtemp(prefix='youtubedl-test')

    # Remove all files in temporary directory
    def removeTempDir():
        shutil.rmtree(dirName)
        os.remove(fileName)

    # Catch & print possible exceptions
    try:
        # Create the PostProcessor object
        # and call the method try_utime
        post_processor = PostProcessor()
        atime = time.time()
        mtime = time.time()
        post_processor.try_utime(fileName, atime, mtime)

    except Exception as exception:
        print

# Generated at 2022-06-14 17:59:45.656609
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import mock

    class DummyPostProcessor(PostProcessor):
        pass

    downloader = mock.Mock()
    pp = DummyPostProcessor(downloader)
    # Ensure that a warning is reported if utime throws an exception
    with mock.patch('os.utime', side_effect=Exception) as mock_utime:
        pp.try_utime('path', 'atime', 'mtime')
        mock_utime.assert_called_once_with(encodeFilename('path'), ('atime', 'mtime'))
        downloader.report_warning.assert_called_once_with('Cannot update utime of file')
    # Ensure that a warning isn't reported if utime doesn't throw an exception

# Generated at 2022-06-14 17:59:52.301130
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    class DummyPostProcessor(PostProcessor):

        def __init__(self):
            PostProcessor.__init__(self)
            self.warnings = 0

        def try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
            PostProcessor.try_utime(self, path, atime, mtime, errnote)

        def report_warning(self, msg):
            self.warnings += 1

    pp = DummyPostProcessor()
    pp.try_utime('file.txt', 11, 22)
    assert pp.warnings == 1

# Generated at 2022-06-14 18:00:02.911418
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockReportWarning(object):
        def __call__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
    mock = MockReportWarning()

    pp = PostProcessor(downloader={'report_warning': mock})
    result = pp.try_utime('/a/path/to/file', 100, 50, 'Warning message')
    assert result is None
    assert mock.args[0] == 'Cannot update utime of file'
    assert mock.kwargs == {'exc_info': True}

    # Check if it raises error too
    pp = PostProcessor(downloader={'report_warning': mock})

# Generated at 2022-06-14 18:00:09.828579
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..utils import DateRange

    class FakeInfo(dict):
        def __init__(self, **kwargs):
            dict.__init__(self, **kwargs)
            self['upload_date'] = DateRange.day(self['upload_date'])
            self['uploader'] = 'Test'

    info = FakeInfo(id='ID', upload_date='20140101', filename='temp.tmp')
    ydl = YoutubeDL({})
    pp = PostProcessor(ydl)
    pp.run(info)



# Generated at 2022-06-14 18:00:20.585822
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Test utime with a non-existing file and a file without permission to read and write
    from ..YoutubeDL import YoutubeDL
    from tempfile import NamedTemporaryFile
    from shutil import chmod
    import os
    import stat

    dummy_downloader = YoutubeDL({})
    dummy_postprocessor = PostProcessor(dummy_downloader)

    # Create a file in temp dir that we can change to chmod later
    temp_file = NamedTemporaryFile()

    # Create a file that we don't have permission to chmod
    with open('/boot/file_cannot_chmod', 'w'):
        pass
    chmod_mode = os.stat('/boot/file_cannot_chmod').st_mode

# Generated at 2022-06-14 18:00:25.496124
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    d = YoutubeDL({'writedescription': True, 'writethumbnail': True})
    pp = PostProcessor(d)
    with open('temp_file', 'wb') as f:
        pass
    with open('temp_file', 'wb') as f:
        pp.try_utime(f.name, 10, 20)

# Generated at 2022-06-14 18:00:36.374153
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil
    from ..downloader.common import FileDownloader

    tmpdir = tempfile.mkdtemp()
    file_path = os.path.join(tmpdir, 'test_file.tmp')
    with open(file_path, 'w') as f:
        f.write('Test')
    os.utime(file_path, (time.time() - 3600, time.time() - 3600))
    file_path_symlink = os.path.join(tmpdir, 'test_file_symlink.tmp')
    os.symlink(file_path, file_path_symlink)
    os.utime(file_path_symlink, (time.time() - 3600, time.time() - 3600))

    downloader = FileDownload

# Generated at 2022-06-14 18:00:43.643548
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Create temporary file
    import tempfile
    with tempfile.TemporaryFile() as f:
        # Set current time
        import time
        atime = mtime = time.time()
        # Create new instance of PostProcessor
        from .extractor import YoutubeDL
        ydl = YoutubeDL()
        ydl.dump_intermediate_pages = False
        pp = PostProcessor(ydl)
        # Try to set current time on file
        pp.try_utime(f, atime, mtime)

    # Should not fail

# Generated at 2022-06-14 18:00:50.075492
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader
    from ..utils import DateRange
    post_processor = PostProcessor(downloader=FileDownloader({'outtmpl': '%(id)s.%(ext)s', 'daterange': DateRange(), 'verbose': True}))
    post_processor.try_utime('debug.txt', 0, 0)

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:00:52.681220
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime('this_is_a_file', 0, 0)
    pp.try_utime('this_is_a_dir/', 0, 0)

# Generated at 2022-06-14 18:01:06.140343
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import random
    import shutil
    import tempfile
    from ..compat import (
        compat_open,
    )

    now = time.time()
    atime = random.randint(1, now - 1)
    mtime = random.randint(atime + 1, now)

    tempdir = tempfile.mkdtemp()
    tempfilepath = os.path.join(tempdir, 'tempfile')
    with compat_open(encodeFilename(tempfilepath), 'w') as _:
        pass
    os.utime(encodeFilename(tempfilepath), (atime, mtime))
    post_processor = PostProcessor()
    assert os.path.getmtime(encodeFilename(tempfilepath)) != mtime

# Generated at 2022-06-14 18:01:10.094921
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def mock_utime(filepath, atime, mtime):
        mock_utime.calls.append((filepath, atime, mtime))
        raise OSError()

    pp = PostProcessor(None)
    mock_utime.calls = []
    pp.try_utime('testfile', 1, 2)
    assert mock_utime.calls == [('testfile', 1, 2)]



# Generated at 2022-06-14 18:01:20.237801
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import defs
    defs.reset()
    import youtube_dl.YoutubeDL
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s'})
    p = PostProcessor(ydl)
    p.try_utime('blabla', 1.23, 4.56)
    assert defs.warning.count("Cannot update utime of file") > 0
    assert defs.warning.count("blabla") > 0
    defs.reset()

# Generated at 2022-06-14 18:01:32.375688
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import time
    # We can't set a function as a value of the attribute, so we will use a variable
    # to store the original time.time() to restore it later
    time_original = time.time
    # A dummy time.time() function that always returns the same value
    time_fixed = lambda : 0

    with tempfile.NamedTemporaryFile(delete=False) as tf:
        postprocessor = PostProcessor()
        filename = tf.name
        # We don't want our temporary file to be deleted after closing
        postprocessor.try_utime(filename, 5, 4, 'Could not update file %s' % filename)
        # In a perfect world, we should now have a file with atime and mtime set to 5 and 4
        # respectively.
        # Now we compare the real at

# Generated at 2022-06-14 18:01:33.937912
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime('test.txt', 0, 0)

# Generated at 2022-06-14 18:01:44.927836
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test method PostProcessor.try_utime
    """
    import shutil
    import sys
    import tempfile
    import time

    import pytest

    from ..utils import (
        encodeArgument,
        encodeFilename,
    )

    from .common import FakeDownloader

    POST_PROCESSOR_ERRNOTE = 'Cannot update utime of file'


# Generated at 2022-06-14 18:01:51.274796
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Mock a post-processor
    pp = PostProcessor(None)

    # Create a file
    f = open(encodeFilename('_test.txt'), 'wb')
    f.write(b'foo')
    f.close()

    # Fail
    pp.try_utime('_test.txt', 3, 3, 'Cannot update utime of file')

    # Clean up
    os.remove('_test.txt')

# Generated at 2022-06-14 18:01:51.853104
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:02:01.731145
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    from . import FileDownloader
    from ..compat import compat_os_name

    # Create a temp file
    path = os.path.join(os.path.dirname(__file__), 'temp')
    temp = open(path, 'w')
    temp.close()

# Generated at 2022-06-14 18:02:14.657552
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # create a dummy PostProcessor object and assign it to a variable
    dummy_postprocessor = PostProcessor()
    # open a file for testing
    testfile = open('PostProcessor_try_utime_testfile.txt', 'w')
    testfile.close()
    # call try_utime on dummy_postprocessor to change the modification time
    # of the file
    dummy_postprocessor.try_utime('PostProcessor_try_utime_testfile.txt', 200, 100)
    # check the modification time of the file
    assert os.stat('PostProcessor_try_utime_testfile.txt').st_mtime == 100
    # remove the file
    os.remove('PostProcessor_try_utime_testfile.txt')

if __name__ == '__main__':
    test_Post

# Generated at 2022-06-14 18:02:27.197993
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyPostProcessor(PostProcessor):
        """Dummy PostProcessor used for testing try_utime method."""
        def __init__(self, downloader=None, *args, **kwargs):
            super(DummyPostProcessor, self).__init__(downloader, *args, **kwargs)
            self._atime = None
            self._mtime = None
            self._set_utime_called = False

        def set_utime(self, path, atime, mtime):
            """Dummy method for testing try_utime."""
            self._atime = atime
            self._mtime = mtime
            self._set_utime_called = True

    dpp = DummyPostProcessor()

# Generated at 2022-06-14 18:02:33.881638
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .common import FakePostProcessor

    class FakeOsModule:
        def utime(self, _, __):
            raise Exception

    postprocessor = FakePostProcessor()
    postprocessor.set_downloader(YoutubeDL({'verbose': True}))
    postprocessor._downloader.params['outtmpl'] = '%(id)s.%(ext)s'
    postprocessor._downloader.params['usenetrc'] = False
    postprocessor._downloader.params['username'] = None
    postprocessor._downloader.params['password'] = None
    postprocessor._downloader.params['videopassword'] = None
    postprocessor._downloader._downloader.params['temp_filename'] = 'abc.webm'

    import sys

# Generated at 2022-06-14 18:02:47.984613
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time
    import unittest

    class TestPostProcessor(PostProcessor):
        def __init__(self):
            self.downloader = DummyYdl()

    class DummyYdl(object):
        def report_error(self, error, video_id=None):
            pass

        def to_screen(self, msg):
            pass

        def to_stderr(self, msg):
            pass

        def report_warning(self, msg, video_id=None):
            pass

    class PostProcessorTest(unittest.TestCase):
        tmp_file = None
        pp = None

        def setUp(self):
            self.pp = TestPostProcessor()
            self.tmp_dir = tempfile.mkdtemp()
            self.tmp_

# Generated at 2022-06-14 18:02:54.913349
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import pytest
    from tempfile import NamedTemporaryFile
    import time
    import datetime

    with NamedTemporaryFile() as tempfile:
        filename = tempfile.name
        pp = PostProcessor(None)
        a = time.time()
        b = a + datetime.timedelta(days=1)
        pp.try_utime(filename, a, b, errnote='Test')
        # check that time change is within an acceptable range
        assert abs(os.path.getatime(filename) - a) < 10
        assert abs(os.path.getmtime(filename) - b) < 10

# Generated at 2022-06-14 18:03:04.612027
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time
    import os.path

    path1 = tempfile.mktemp()
    with open(path1, 'wb') as f:
        f.write(b'')
    atime = time.time()
    mtime = atime - 60

    # Test with existing file
    pp = PostProcessor(None)
    pp.try_utime(path1, atime, mtime)
    assert os.path.getatime(path1) > mtime
    assert os.path.getmtime(path1) > mtime

    shutil.rmtree(path1)
    # Test with not existing file
    pp.try_utime(path1, atime, mtime)
    # No assertion

# Generated at 2022-06-14 18:03:12.656074
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import os.path
    import time
    import os
    import atexit

    dirname = tempfile.mkdtemp()
    atexit.register(lambda: shutil.rmtree(dirname))

    class FakeDownloader(object):
        def report_warning(self, message):
            print(message)

    def create_temp_file(dirname):
        basename = tempfile.mktemp(dir='.', suffix='.tmp', prefix='postprocessor', dir=dirname)
        tmpfile = open(basename, 'w')
        tmpfile.close()
        return basename

    pp = PostProcessor(FakeDownloader())

    path = create_temp_file(dirname)
    path_bytes = path.encode('utf-8')

# Generated at 2022-06-14 18:03:24.549005
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    from ..YoutubeDL import YoutubeDL
    from .common import gettestcases_general
    from .test_extractor import gettestcases_extractor

    def run_test(testcase, params=None):
        dl = YoutubeDL(params)
        tmpdir = tempfile.mkdtemp(prefix="ytdl_utime_test_")
        filename = os.path.join(tmpdir, 'test.txt')
        with open(filename, 'w') as fh:
            fh.write('testfile\n')
        t = os.path.getmtime(filename)
        dl.params['postprocessor_args'] = ['-no-mtime', '-outtmpl', filename + '.%(ext)s']
        pp = PostProcessor(dl)

# Generated at 2022-06-14 18:03:36.211677
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile

    # FIXME: This test fails if it is not run as root (or not using sudo)
    # because files cannot have mtime set in the future.
    # The test has been marked as "expectedFailure" until this is fixed.
    from nose.plugins.attrib import attr
    from nose.plugins.skip import SkipTest

    if os.geteuid() != 0:
        raise SkipTest('Superuser privilege is required')

    from . import FakeYDL
    ydl = FakeYDL()
    ydl.add_default_info_extractors()
    pp = PostProcessor(ydl)

    utime_fails = []
    utime_fails.append('/ytdl/should/not_exist/')


# Generated at 2022-06-14 18:03:46.931198
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import TemporaryDirectory
    from ..utils import DateRange, DateTime

    class DummyPostProcessor(PostProcessor):
        def __init__(self):
            pass

    class DummyDateRange(DateRange):
        def __init__(self, valid=False):
            super(DummyDateRange, self).__init__()
            self.valid = valid

        def intersects(self, other):
            return self.valid and other.valid

        def __repr__(self):
            return "DateRange({0})".format(self.valid)

    with TemporaryDirectory(
        suffix='-test_postprocessor_try_utime',
        prefix='ytdl_test_'
    ) as temp_dir:
        temp_file = os.path.join(temp_dir, 'testfile')

# Generated at 2022-06-14 18:03:54.259130
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader

    fd = FileDownloader({})
    pp = PostProcessor(fd)
    fd.add_post_processor(pp)
    open('test.file', 'w').close()

    pp.try_utime('test.file', 1, 2)

    if os.stat('test.file').st_mtime != 2:
        raise AssertionError('The mtime of the test.file was not updated')

    os.remove('test.file')

# Generated at 2022-06-14 18:04:04.949964
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import compat_mock

    # Mocking os.utime is not working on Python 2.6 (see #4931)
    if os.name == 'nt' or not hasattr(os.path, 'getatime'):
        raise Exception('Test cannot be performed on this platform')

    filename = os.path.join(os.path.dirname(__file__), 'testid.bin')
    atime = os.path.getatime(filename)
    mtime = os.path.getmtime(filename)

    with compat_mock.patch('os.utime') as mock_utime:
        mock_utime.side_effect = OSError
        postprocessor = PostProcessor()
        postprocessor.try_utime(filename, atime, mtime)


# Generated at 2022-06-14 18:04:15.940215
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.utils import DateRange
    import sys
    import time

    class DummyPostProcessor(PostProcessor):
        def run(self, info):
            atime = time.time() - 1000
            mtime = time.time() - 2000
            filepath = info.get('filepath')
            self.try_utime(filepath, atime, mtime)
            return [], info

    def test_callback(filename, step_name, total_fragments):
        pass


# Generated at 2022-06-14 18:04:35.755082
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkstemp
    from time import time
    from shutil import rmtree
    from pytube.extractor.common import (
        ExtractorError,
    )
    import os
    import pytube.downloader.f4m
    # Create temp dir
    tmp_dir = mkdtemp()
    fd, file_path = mkstemp(prefix=tmp_dir)
    # Create temp file
    with open(file_path, 'w') as f:
        f.write('test')
    # Create PostProcessor instance
    pp = PostProcessor(pytube.downloader.f4m.F4mFD())
    atime = time()
    mtime = time() + 3600
    # Run try_utime method with existing file

# Generated at 2022-06-14 18:04:43.888354
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL

    ydl = YoutubeDL({})

    pp = PostProcessor(ydl)
    try:
        os.remove('./test_PostProcessor_try_utime.tmp')
    except:
        pass
    f = open('./test_PostProcessor_try_utime.tmp', 'w')
    f.close()
    pp.try_utime('./test_PostProcessor_try_utime.tmp', 1, 1)

    os.remove('./test_PostProcessor_try_utime.tmp')

# Generated at 2022-06-14 18:04:54.177465
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from tempfile import mkdtemp
    tmpdir = mkdtemp()

# Generated at 2022-06-14 18:04:55.209136
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # There is no safe way to test this class
    pass

# Generated at 2022-06-14 18:05:04.477971
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import time
    import random
    from shutil import copyfile
    tmp_dir = tempfile.mkdtemp(prefix='yt-unit-tests-post-processor-try_utime-dir')
    tmp_filename = os.path.join(tmp_dir, 'yt-unit-tests-file')
    tmp_file = open(tmp_filename, 'w')
    tmp_file.close()
    
    current_time = int(time.time())
    atime = current_time + random.randint(0, 100)
    mtime = current_time + random.randint(0, 100)

    copyfile(tmp_filename, tmp_filename + '.bak')
    os.utime(tmp_filename, (atime, mtime))
    assert os.path.getatime

# Generated at 2022-06-14 18:05:12.000512
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from types import ModuleType
    from ..downloader import FakeYDL

    class FakePostProcessor(PostProcessor):
        def run(self, information):
            self.try_utime(information['filepath'], 0, 0)
            return [], information

    pp = FakePostProcessor()
    pp.set_downloader(FakeYDL({'outtmpl': "%(stitle)s-%(id)s.%(ext)s"}))
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_dir, 'testfile')

# Generated at 2022-06-14 18:05:22.960877
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from youtube_dl.downloader import FakeInfoExtractor
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.compat import compat_makedirs

    from tempfile import mkdtemp
    from shutil import rmtree
    from os import utime, path, getpid
    from datetime import datetime

    OUTPUT_DIR = None
    OLD_TIME = 10.0

    class FakePostProcessor(PostProcessor):
        def __init__(self, *args, **kwargs):
            super(FakePostProcessor, self).__init__(*args, **kwargs)
            self.utime_was_called = False

        def run(self, *args, **kwargs):
            self.utime_was_called = True
            return ([], {})


# Generated at 2022-06-14 18:05:28.842456
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader(object):
        def report_warning(self, text):
            pass

    class PP(PostProcessor):
        def __init__(self):
            pass # remove downloader dependency

        def run(self, info):
            return self.try_utime(__file__, 0, 0)

    pp = PP()
    pp.set_downloader(MockDownloader())
    pp.run(None)

# Generated at 2022-06-14 18:05:38.047477
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader():
        pass

    class MockPostProcessor(PostProcessor):
        pass

    downloader = MockDownloader()
    p = MockPostProcessor(downloader)

    p.try_utime('/tmp', 0, 0)
    assert not hasattr(downloader, 'report_warning')

    downloader.report_warning = lambda e: e  # lambda needed to avoid "None error" when assert is called

    import errno
    error = OSError()
    error.errno = errno.EPERM
    import os
    import sys
    import __builtin__
    BuiltinIO = __builtin__.io
    class mock_os_utime(object):
        def __init__(self, *args, **kwargs):
            raise error

# Generated at 2022-06-14 18:05:48.299343
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import datetime
    import time
    import os
    import shutil
    tempdir = tempfile.mkdtemp()
    try:
        test_file = os.path.join(tempdir, "testfile.dat")
        with open(test_file, "wb") as f:
            f.write(b"test data")
        a = PostProcessor({})
        a.try_utime(test_file, 0, 0, "test note")
        # time.sleep(1) # TODO: why needed?
        t = datetime.datetime.utcfromtimestamp(time.time())
        a.try_utime(test_file, t.timestamp(), t.timestamp(), "test note")
    finally:
        shutil.rmtree(tempdir)


# Generated at 2022-06-14 18:06:26.401851
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange
    from .helpers import TestTopic

    class DummyPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(DummyPostProcessor, self).__init__(downloader)
            self.times = []
            self.paths = []

        def run(self, info):
            path = info['filepath']
            self.paths.append(path)
            atime, mtime = os.path.getatime(path), os.path.getmtime(path)
            self.try_utime(path, atime-60, mtime-60)
            self.times.append((os.path.getatime(path), os.path.getmtime(path)))

# Generated at 2022-06-14 18:06:34.496510
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import DateRange
    from ..cache import Cache
    from ..extractor import youtube_dl
    from ..compat import compat_urllib_request
    from .test_file_downloader import FakeYDL

    dl = FakeYDL()
    dl.params['cache'] = None
    dl.add_info_extractor(youtube_dl.YoutubeIE())

    # Download a test video
    dl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])

    # Try to set its creation and modification time to current time
    assert dl.downloaded_info_dicts[0]['id'] == 'BaW_jenozKc'


# Generated at 2022-06-14 18:06:45.063132
# Unit test for method try_utime of class PostProcessor

# Generated at 2022-06-14 18:06:55.886252
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractors
    from ..utils import DateRange
    from .embedthumbnailpp import EmbedThumbnailPP
    from .execafterdownload import ExecAfterDownload
    from .metadatafromtitle import MetadataFromTitle
    from .xattrsmetadata import XAttrMetadata
    import sys
    import unittest

    if os.name == 'nt':
        utime_test_file = os.path.join(os.getenv('TEMP') or os.getenv('TMP'), 'utime_test_file')
    else:
        utime_test_file = '/tmp/utime_test_file'

    # Get test downloader
    downloader = gen_downloader({}, {}, {}, {})

    # Check that utime_test_file does not exist

# Generated at 2022-06-14 18:07:05.774755
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import os
    import time

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create a temporary file
    temp_file = os.path.join(temp_dir, 'test_file')
    with open(temp_file, 'w') as fp:
        fp.write('Test')

    postprocessor = PostProcessor()
    postprocessor._downloader = DummyYoutubeDL()

    orig_stat = os.stat(temp_file)
    atime, mtime = orig_stat.st_atime, orig_stat.st_mtime

    # Test that the try_utime method won't update the file times if the
    # specified times are the same as the original

# Generated at 2022-06-14 18:07:08.844952
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        PostProcessor().try_utime('/tmp/aoeu', 0, 0)
    except Exception as e:
        assert isinstance(e, PostProcessingError)

# Generated at 2022-06-14 18:07:18.573261
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .common import FakeYDL

    def test_PostProcessor_try_utime_aux(downloader):
        postprocessor = PostProcessor(downloader)
        fake_path = b'this/is/a/fake/path.mp4'
        postprocessor.try_utime(fake_path, 1000, 1001)
        assert downloader.to_screen_calls == [
            u'[debug] Cannot update utime of file',
        ]
        assert downloader.to_screen_msgs == [
            u'Cannot update utime of file',
        ]
        downloader.to_screen_calls = []
        downloader.to_screen_msgs = []

    downloader = FakeYDL()

# Generated at 2022-06-14 18:07:29.787539
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    from .test import _fake_downloader
    from .common import FileDownloader
    from .test import get_testcases_downloads_dir
    from ..utils import (
        video_extro_dict,
        get_crc32,
    )
    # Create test file
    f = open(os.path.join(get_testcases_downloads_dir(),
                          'testfile.mp4'), 'w')
    f.write('test')
    f.close()
    # Create downloader with test file
    f = open(os.path.join(get_testcases_downloads_dir(),
                          'test.tmp'), 'w')
    f.write('test')
    f.close()
    # Create postprocessor

# Generated at 2022-06-14 18:07:38.262028
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .test_util import FakeYDL
    from .extractor.common import InfoExtractor
    from .downloader.common import FileDownloader
    from .compat import compat_urllib_request
    import tempfile
    import shutil
    import os
    import time

    temp_dir = tempfile.mkdtemp(prefix="youtubedl-")
    dst_path = os.path.join(temp_dir, 'temp_file')

# Generated at 2022-06-14 18:07:45.501553
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    from ..extractor import youtube_dl
    from .common import FakeYDL

    test_path = 'test/expected/file'
    test_atime = 1468926058.0
    test_mtime = 1468926058.0

    class FakeOS:
        def utime(self, path, atime):
            assert path == encodeFilename(test_path)
            assert atime == (test_atime, test_mtime)

    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader):
            self._downloader = downloader

    fake_os = FakeOS()
    post_processor = FakePostProcessor(FakeYDL({}))
    post_processor.try_utime(test_path, test_atime, test_mtime)
    post_processor.try_