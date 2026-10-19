

# Generated at 2022-06-14 17:58:36.036700
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time, os, stat
    temp_dir, temp_filename = tempfile.mkstemp('youtube-dl-test-file')
    os.close(temp_dir)
    temp_dir = tempfile.mkdtemp('youtube-dl-test-dir')
    temp_filepath = os.path.join(temp_dir, temp_filename)
    open(temp_filepath, 'w').close() # create file

# Generated at 2022-06-14 17:58:43.623459
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil
    import tempfile
    import os.path
    from ..downloader.common import FileDownloader


    f = tempfile.NamedTemporaryFile()
    path = f.name
    f.close()
    atime = mtime = time.time()
    pp = FileDownloader(None, {}).postProcessor
    pp.try_utime(path, atime, mtime)
    assert os.path.getatime(path) == atime
    assert os.path.getmtime(path) == mtime

    pp.try_utime(path, None, None)
    assert os.path.getatime(path) != atime
    assert os.path.getmtime(path) != mtime

    shutil.rmtree(os.path.dirname(path))

# Generated at 2022-06-14 17:58:49.279837
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import time
    import utils
    import shutil
    import tempfile

    class MockDownloader(object):
        def report_warning(self, message):
            self.warning = message
            raise Warning('test_PostProcessor_try_utime')

    tempdir = tempfile.mkdtemp('youtube-dl-test')
    orig = os.path.join(tempdir, 'orig')
    with open(orig, 'wb') as f:
        f.write(b'asdf')
    os.utime(orig, (1000000000, 1000000000))  # Sat, 13 Sep 2031 00:46:40 GMT


# Generated at 2022-06-14 17:59:00.441717
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil

    dir_temp = tempfile.mkdtemp()

# Generated at 2022-06-14 17:59:10.083010
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    # Create a temporary directory to save the downloaded file
    temp_dir = tempfile.mkdtemp(prefix='test_youtube-dl_')
    # Create a file in the temporary directory
    filepath = temp_dir + os.sep + "temporary_file.txt"
    f = open(filepath, 'w')
    f.close()
    # Get atime and mtime of the file
    (atime, mtime) = os.stat(filepath)[7:9]
    # Create PostProcessor object
    pp = PostProcessor(None)
    # Call try_utime method to update the timestamp
    pp.try_utime(filepath, time.time(), time.time())
    # Get the updated atime, mtime of the file

# Generated at 2022-06-14 17:59:11.976735
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # tests.PostProcessor_test.test_try_utime
    pass

# Generated at 2022-06-14 17:59:21.935159
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ytdl.YoutubeDL import YoutubeDL
    class TestPostProcessor(PostProcessor):
        def run(self, information):
            import time
            import os
            self.try_utime(information['filepath'], time.time(), time.time())
            os.utime(information['filepath'], (0, 0))
            return [], information

    info = {
        'id': 'test_id',
        'title': 'test video'
    }
    dl = YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    pp = TestPostProcessor(dl)
    pp.run(info)

# Generated at 2022-06-14 17:59:30.461476
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def test_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
        self.path = path
        self.atime = atime
        self.mtime = mtime
        self.errnote = errnote

    pp = PostProcessor(None)
    pp.try_utime = test_utime

    assert 'path' not in pp.__dict__
    assert 'atime' not in pp.__dict__
    assert 'mtime' not in pp.__dict__
    assert 'errnote' not in pp.__dict__

    pp.try_utime('the path', 1, 2)
    assert pp.path == 'the path'
    assert pp.atime == 1
    assert pp.mtime == 2

# Generated at 2022-06-14 17:59:39.242647
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import datetime
    import youtube_dl
    import pytest
    import pytest_catchlog
    import tempfile

    @pytest.fixture
    def pytestconfig(pytestconfig):
        """
        pytest-catchlog uses the warning module which prints
        to stdout by default. This overrides that behaviour.
        """
        from ..utils import ErrorPrinter
        import logging
        logger = logging.getLogger('youtube_dl')
        logger.setLevel(logging.DEBUG)
        logger.addHandler(ErrorPrinter())
        return pytestconfig

    @pytest.fixture
    def tempf():
        with tempfile.NamedTemporaryFile() as f:
            yield f

    @pytest.fixture
    def pp(tempf):
        import os
        pp = PostProcess

# Generated at 2022-06-14 17:59:48.525433
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test whether try_utime method of PostProcessor class works.
    """
    import pytest
    import datetime
    fd, fname = tempfile.mkstemp()
    # open the file in write mode to change access and modification time
    with os.fdopen(fd, 'w') as f:
        f.write('hello wrld')
    p = PostProcessor(None)
    try:
        p.try_utime(fname, 100, 120)
    except Exception as e:
        pytest.fail(str(e))
    # pytest.fail('fail me')

# Generated at 2022-06-14 18:00:02.035972
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import FileDownloader
    from .postprocessor import PostProcessor
    from .compat import compat_os_name

    # Windows: skip test in case the server runs on a non-windows system
    if compat_os_name == 'nt':
        return

    # Create a test file and set it old access and modification time
    tmpfile_path = 'youtubedl-test-file'
    orig_mtime = 1100000000
    orig_atime = 1200000000

    with open(tmpfile_path, 'wb') as f:
        f.write(b'a')
    os.utime(tmpfile_path, (orig_atime, orig_mtime))

    with FileDownloader({}) as ydl:
        pp = PostProcessor(ydl)

        # Try to set file access and modification time to certain

# Generated at 2022-06-14 18:00:12.911176
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import DateRange
    from .common import FakeYDL
    from .test_downloader import RecordingHooks
    from .test_postprocessor import PostProcessorTestCase

    class FakePostProcessor(PostProcessor):
        _downloader = None
        def __init__(self, downloader):
            self._downloader = downloader

    class TestPostProcessor(PostProcessorTestCase):
        def test_try_utime(self):
            downloaded_file = self.make_file(as_filename=True)
            modified_time = downloaded_file.setmtime(100)
            postprocessor = FakePostProcessor(FakeYDL(params={'no_warnings': True}))
            postprocessor.try_utime(downloaded_file, 0, 0)

# Generated at 2022-06-14 18:00:14.102496
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    # no exception should be raised
    pp.try_utime(None, None, None)

# Generated at 2022-06-14 18:00:26.070837
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # available only on posix systems
    if os.name == 'posix':
        from datetime import datetime
        import time
        import tempfile

        # Create a file, write some content to it, and get access/modify times
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(b'foo')
        tfile.close()
        atime_orig = os.path.getatime(tfile.name)
        mtime_orig = os.path.getmtime(tfile.name)

        # Call try_utime() to set access/modify times to arbitrary values
        pp = PostProcessor(None)
        atime = time.mktime(datetime(2001, 1, 1).timetuple())

# Generated at 2022-06-14 18:00:30.020617
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        # Import the module only if this test is requested
        import youtube_dl.postprocessor.common
        youtube_dl.postprocessor.common.PostProcessor._downloader = None
        youtube_dl.postprocessor.common.PostProcessor.try_utime('foo.mp4', 0, 0)
    except youtube_dl.postprocessor.common.PostProcessingError:
        pass

# Generated at 2022-06-14 18:00:40.892380
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        import tempfile

        dummy_file = tempfile.NamedTemporaryFile()
        dummy_file.close()

        PP = PostProcessor(None)
        PP.try_utime(dummy_file.name, 100, 200)
        assert os.stat(dummy_file.name).st_atime == 100
        assert os.stat(dummy_file.name).st_mtime == 200
    finally:
        if os.path.exists(dummy_file.name):
            os.remove(dummy_file.name)


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:00:53.164601
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    class DummyDownloader(object):
        def __init__(self):
            self.warning_count = 0
        def report_warning(self, errnote):
            self.warning_count = self.warning_count + 1

    from ..compat import file

    # We need to create a dummy file
    file_name = 't1'
    with open(file_name, 'wb') as outf:
        pass

    # We need to know the access and modification times of the file
    stat_obj = os.stat(file_name)
    atime, mtime = stat_obj.st_atime, stat_obj.st_mtime

    # We need to create an instance of PostProcessor
    pp = PostProcessor(None)
    pp.set_downloader(DummyDownloader())

    # Save the value of

# Generated at 2022-06-14 18:01:06.190107
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import stat
    import time
    import os

    class MockDownloader:
        def report_warning(self, message):
            self.reported_warning = message

    class MockPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            self._downloader = downloader

    path = tempfile.mktemp()
    with open(path, 'w') as f:
        f.write("I am a test file")

    with open(path, 'r') as f:
        st = os.fstat(f.fileno())
    atime = st.st_atime
    mtime = st.st_mtime
    tm = time.mktime((2013, 4, 5, 0, 0, 0, 4, 95, 0))

    post_processor = MockPostProcess

# Generated at 2022-06-14 18:01:15.057941
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import time
    import tempfile
    import shutil
    import unittest

    class TestPostProcessor(PostProcessor):
        pass

    class TestDownloader(object):
        def __init__(self, params):
            self.params = params

        def report_warning(self, errnote):
            print(errnote)

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.test_dir = tempfile.mkdtemp(suffix=ESC_TEST_DIR_SUFFIX)

        def tearDown(self):
            shutil.rmtree(self.test_dir)


# Generated at 2022-06-14 18:01:17.272329
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    import doctest
    #doctest.testmod()  # run all tests
    failures, tests = doctest.testmod()

# Generated at 2022-06-14 18:01:30.321773
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    # Just let the exception which is raised in PostProcessor.try_utime
    # to be rendered to exception message.
    if sys.version_info >= (3, 0):
        # On Python 3, must be a TextIOWrapper instance,
        # but on Python 2, must be a file instance.
        f = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False)
    else:
        f = tempfile.NamedTemporaryFile(mode='w', delete=False)
    f.close()
    fname = f.name
    try:
        pp = PostProcessor(None)
        pp.try_utime(f.name, 0, 0)
    finally:
        os.remove(fname)

# Generated at 2022-06-14 18:01:33.427758
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    postprocessor = PostProcessor()
    postprocessor.try_utime('test',1000,2000)
    # TODO: test if os.utime was really called

# Generated at 2022-06-14 18:01:44.891109
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Use a fake file 'ascii.txt' with content 'abc' to test method try_utime of PostProcessor
    """
    import time
    import shutil
    import os
    import tempfile
    import pytest
    from ..YoutubeDL import YoutubeDL
    from ..extractor.common import InfoExtractor
    from ..utils import encodeFilename

    # Create a fake file ascii.txt and open it
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    filename = temp_file.name
    with temp_file as file:
        file.write('abc')
    # Get current timestamp of file ascii.txt
    stat_info = os.stat(filename)
    assert isinstance(stat_info.st_atime, int)

# Generated at 2022-06-14 18:01:49.315013
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    If this test fails, check your filesystem for casesensitivity.
    """
    import os.path
    from .downloader import FileDownloader
    from .extractor.common import InfoExtractor
    from .postprocessor.info import FileInfoPP
    import time

    # Prepare
    downloader = FileDownloader(params={})
    downloader.add_info_extractor(InfoExtractor())
    downloader.add_post_processor(FileInfoPP())

    # Create some files
    file_main = "test_PostProcessor_try_utime"
    file_path = file_main + ".m4a"

    with open(file_path, 'wb') as f:
        f.write("\x00" * 1000)


# Generated at 2022-06-14 18:02:00.277604
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil
    import tempfile
    import unittest

    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(TestPostProcessor, self).__init__(downloader)
            self.errnote = ''

        def run(self, information):
            self.try_utime(information['filepath'], int(time.time()), int(time.time()), self.errnote)

    class TestDownloader(object):
        def __init__(self, params):
            self.params = params

        def report_warning(self, errnote):
            print(errnote)

    class TestPostProcessorTest(unittest.TestCase):
        def test_try_utime(self):
            # Create a temporary directory
            temp_

# Generated at 2022-06-14 18:02:05.849853
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class _DummyPostProcessor(PostProcessor):
        def __init__(self, test_case, mtime):
            super(_DummyPostProcessor, self).__init__()
            self.test_case = test_case
            self.mtime = mtime
            self.applied = False

        @staticmethod
        def makedirs(path):
            if isinstance(path, basestring):
                return os.makedirs(path)
            else:
                return os.makedirs(encodeFilename(path))

        def run(self, info):
            self.try_utime(info['filepath'], 9999999999, self.mtime)
            self.applied = True
            return [], info
    from tempfile import mkdtemp
    from shutil import rmtree

# Generated at 2022-06-14 18:02:16.603248
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    pp = PostProcessor(ydl)

    # create test_file
    import datetime
    import time
    import tempfile
    temp_fd, temp_path = tempfile.mkstemp(prefix='ytdl_test_postprocessor_')
    temp_file_handle = os.fdopen(temp_fd, 'wb+')
    temp_file_handle.write(b'abcefg')
    temp_file_handle.close()

    # get atime and mtime of test_file
    test_file_stat = os.stat(temp_path)
    test_file_atime = test_file_stat.st_atime
    test_file_mtime = test_file_stat.st_mtime

    # check that atime

# Generated at 2022-06-14 18:02:25.584894
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    import time
    import tempfile

    fd, filename = tempfile.mkstemp(prefix='youtubedl-test-utime')
    os.close(fd)
    try:
        atime = time.time() - 40000
        os.utime(filename, (atime, atime))
        mtime = atime + 40000
        pp.try_utime(filename, mtime, mtime)
        assert(mtime == os.stat(filename).st_mtime)
    finally:
        os.remove(filename)

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:02:35.425483
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    try:
        from test_utils import remove_file
    except ImportError:
        from . import remove_file

    # Create an empty file
    fd, filename = tempfile.mkstemp(prefix='youtube-dl-test-')
    os.close(fd)

    # Set the access and modification time to the past
    atime = mtime = time.time() - 100

    # Create a PostProcessor object
    pp = PostProcessor(None)

    # Try to utime a file that does not exist
    remove_file(filename)
    pp.try_utime(filename, atime, mtime, errnote='Something went wrong')

    # Create a file and try to utime it; it should work

# Generated at 2022-06-14 18:02:43.136333
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import _TEST_FILE_CONTENTS

    from tempfile import NamedTemporaryFile
    from .f4m import F4mPP
    from .common import PostProcessorTest
    import os

    with NamedTemporaryFile(prefix='ytdl_test_') as tfile:
        tfile.write(_TEST_FILE_CONTENTS)
        tfile.flush()

        assert os.path.exists(tfile.name)
        p = F4mPP(PostProcessorTest.downloader)
        p.try_utime(tfile.name, 1, 2)
        assert os.path.exists(tfile.name)

# Generated at 2022-06-14 18:02:55.365001
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test utime, atime, and mtime
    """
    import os
    import time
    import pytest

    # Need to define a class because pytest.raises wants a class object
    class MyTestClass(object):
        def __init__(self):
            self.params = {}
        def report_warning(self, warn):
            pass

    postprocessor = PostProcessor(MyTestClass())

    # Check that utime works
    dest_dir = encodeFilename(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dest_dir'))
    dest_file_name = 'dest_file.txt'
    dest_file = os.path.join(dest_dir, dest_file_name)


# Generated at 2022-06-14 18:03:05.273854
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader(object):
        def report_warning(self, string):
            pass

    class MockPostProcessor(PostProcessor):
        def __init__(self):
            super(MockPostProcessor, self).__init__()
            self._downloader = MockDownloader()

    import time

    import sys

    # Test with a valid file
    valid_file = 'valid_file'
    open(valid_file, 'w').close()
    pp = MockPostProcessor()
    pp.try_utime(valid_file, 1, 2)
    assert os.path.getmtime(valid_file) == 2
    assert os.path.getatime(valid_file) == 1
    os.remove(valid_file)
    # Test with a non-existent file
    pp = MockPostProcessor()

# Generated at 2022-06-14 18:03:14.832326
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # First test that we don't fail in case the file or path does not exist
    # or we cannot change the timestamp
    class FakeDownloader(object):
        def report_warning(self, errnote):
            pass

    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader):
            super(FakePostProcessor, self).__init__(downloader)

    downloader = FakeDownloader()
    pp = FakePostProcessor(downloader)
    pp.try_utime('/does/not/exist', 1, 2)
    pp.try_utime('/does/not/exist/foo.txt', 1, 2)

# Generated at 2022-06-14 18:03:25.863583
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FileDownloader

    import tempfile
    from ..utils import DateRange, prepend_extension

    tempdir = tempfile.mkdtemp()

    dl = FileDownloader({})
    dl.params['outtmpl'] = os.path.join(tempdir, '%(title)s-%(id)s.%(ext)s')
    pp = PostProcessor(dl)

    test_file = os.path.join(tempdir, 'test.mp4')
    open(test_file, 'wb').close()
    modified = os.path.getmtime(test_file)

    # Test with a DateRange
    test_file = os.path.join(tempdir, 'test.mp4')
    pp.try_utime(test_file, modified, modified)

# Generated at 2022-06-14 18:03:37.170130
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import time
    import tempfile
    import unittest

    # This is a class that mocks a downloader, since the real one
    # needs a lot of stuff that we don't need for testing (like
    # an event loop) but the PostProcessor objects need it
    class MockYDL(object):
        def report_error(self, msg):
            raise

        def report_warning(self, msg):
            raise

    # This is a minimal test case for the try_utime method. We
    # create a file, write to it, set its time, and then we
    # check that the time is set.
    class TestTryUtime(unittest.TestCase):
        def setUp(self):
            fd, self.name = tempfile.mkstemp()
            os.close(fd)



# Generated at 2022-06-14 18:03:47.326170
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import datetime
    import tempfile
    import shutil
    import os

    tmp_dir = tempfile.mkdtemp(prefix="tmp_test_PostProcessor_try_utime_")
    test_file = os.path.join(tmp_dir, "test_file")
    with open(test_file, 'w') as f:
        f.write("TEST FILE\n")

# Generated at 2022-06-14 18:03:58.373046
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import sys
    import time
    import tempfile
    import shutil
    from ..utils import DateRange

    if sys.version_info < (3, 0):
        from cStringIO import StringIO
    else:
        from io import StringIO

    class FakeDownloader:
        def __init__(self):
            self.params = {'verbose': True, 'outtmpl': '%(id)s'}
            self._scroll_messages = []
            self._screen_file = None

        def report_warning(self, msg):
            self._scroll_messages.append(msg)

        def to_stdout(self, msg):
            self._scroll_messages.append(msg)


# Generated at 2022-06-14 18:04:10.156798
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """PostProcessor_try_utime is called in the PostProcessor class,
    but we want to unit test it independent of an PostProcessor instance
    because this method doesn't depend on self and also because
    of the lack of a standard unit test module in Python.

    This unit test should work independently of the machine it runs,
    independently of the umask and independently of the root privileges
    of the user.

    """
    try:
        import tempfile
        tmpdir = tempfile.mkdtemp()
        from ..utils import (
            sanitize_open,
            sanitize_path,
            encodeFilename,
        )
    except ImportError:  # Python 2.4 compatibility
        import tempfile
        tmpdir = tempfile.mktemp()

# Generated at 2022-06-14 18:04:21.028109
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """ Test if method try_utime of class PostProcessor can update utime of file
    """
    import os
    import time
    import unittest

    class TestPostProcessor(PostProcessor):

        def run(self, information):
            utime_file = "{0}/{1}".format(os.path.dirname(os.path.abspath(__file__)),
                                          "utime_file.txt")

            with open(utime_file, 'w') as f:
                f.write("")

            self.try_utime(utime_file, 100, 100)
            self.try_utime(utime_file, 200, 200)
            self.try_utime(utime_file, 300, 300)


# Generated at 2022-06-14 18:04:31.590605
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class File(object):
        def __init__(self, name, st_atime=-1, st_mtime=-1):
            self.name = name
            self.st_atime = st_atime
            self.st_mtime = st_mtime

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
    class AccessorC(object):
        def __init__(self, files):
            self.files = files

        def open(self, path, mode):
            assert mode == 'r'
            for file in self.files:
                if file.name == path:
                    yield file


# Generated at 2022-06-14 18:04:42.819399
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()
    try:
        f = open(tmpdir + 'myfile', 'w')
        f.close()
        pp = PostProcessor(None)
        pp.try_utime(tmpdir + 'myfile', 2, 3)
    finally:
        shutil.rmtree(tmpdir)

# Generated at 2022-06-14 18:04:52.853877
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # If a PostProcessor is required we can create a subclass with a mock downloader
    class TestPostProcessor(PostProcessor):
        def __init__(self):
            # constructor is required for unit test
            super(TestPostProcessor, self).__init__()

    import tempfile
    tmp_dir = tempfile.mkdtemp()
    file_name = unicode(tmp_dir) + os.path.sep + 'temp_file'

    from datetime import datetime
    import time

    # create a temporary file on file system
    open(encodeFilename(file_name), 'w').close()

    file_time = datetime.now().replace(microsecond=0)

    # retrieve current file time
    file_time_stats = os.stat(encodeFilename(file_name))
    file_time_at

# Generated at 2022-06-14 18:05:01.194438
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import os

    # Create file to test
    f = open('try_utime.tmp', 'w')
    f.close()

    p = PostProcessor(None)

    # Check that file exists
    if not os.path.isfile('try_utime.tmp'):
        raise TypeError('File creation failed')

    # Try utime on file and check that errors are not raised
    p.try_utime('try_utime.tmp', 0, 1)

    # Remove file created
    os.remove('try_utime.tmp')

# Generated at 2022-06-14 18:05:05.803011
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FakeYoutubeDL
    p = PostProcessor(FakeYoutubeDL({}))
    p.try_utime('/file/path', 1, 1)
    p.try_utime('/file/path', '1', '1')

# Generated at 2022-06-14 18:05:17.707059
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def os_utime_mockup(filename, atime, mtime):
        os_utime_mockup.called = True
        os_utime_mockup.filename = filename
        os_utime_mockup.atime = atime
        os_utime_mockup.mtime = mtime

    class MockDownloader(object):
        def report_warning(self, msg):
            report_warning_mockup.msg = msg

    def report_warning_mockup(msg):
        pass

    os_utime_mockup.called = False
    report_warning_mockup.msg = None
    filename = "filename"
    atime = 1
    mtime = 2
    postprocessor = PostProcessor()
    postprocessor._downloader = MockDownloader()
    postprocessor

# Generated at 2022-06-14 18:05:18.346429
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:05:29.082731
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Use a class which inherits PostProcessor
    class MockPP(PostProcessor):
        pass

    import tempfile, os
    # Create temporary directory
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:05:41.219018
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil, tempfile
    from ..downloader import Downloader
    from . import FFmpegPostProcessor

    cwd = os.path.dirname(os.path.abspath(__file__))
    tmp = tempfile.mkdtemp()
    test_file = os.path.join(cwd, 'ffmpeg_test.txt')
    shutil.copy(test_file, tmp)
    test_file = os.path.join(tmp, 'ffmpeg_test.txt')
    params = {'username': 'unittest', 'quiet': True, 'simulate': True, 'skip_download': True,
              'outtmpl': os.path.join(tmp, '%(id)s.%(ext)s')}
    downloader = Downloader(params)

# Generated at 2022-06-14 18:05:50.387819
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import fake_downloader
    from .extractor.common import FileDownloader
    from .compat import compat_makedirs

    downloader = fake_downloader(params={'outtmpl': '%(id)s.mp4'})
    FileDownloader._read_functions['test1'] = lambda _: b'file info'
    FileDownloader._read_packages['test1'] = lambda _: b''
    FileDownloader._write_functions['test1'] = lambda _, c: c

# Generated at 2022-06-14 18:05:57.166854
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader():
        def __init__(self):
            self.to_stderr_count = 0
            self.to_stderr_messages = []

        def report_warning(self, msg):
            self.to_stderr_count += 1
            self.to_stderr_messages.append(msg)

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    pp.try_utime('no-such-file.mp4',1,1,'Warning message')
    assert downloader.to_stderr_count == 1
    assert downloader.to_stderr_messages[0] == 'Warning message'

# Generated at 2022-06-14 18:06:21.456610
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import time
    from ..compat import (
        compat_path,
        compat_os_name,
        compat_shutil,
    )

    class FakeDownloader():
        def report_warning(self, errnote):
            pass

    with tempfile.NamedTemporaryFile(delete=False) as tf:
        path = compat_path(tf.name)
        atime = time.time()
        pp = PostProcessor(FakeDownloader())
        if compat_os_name == 'nt':
            compat_shutil.move(path, compat_path(os.path.join(tempfile.gettempdir(), 'a.tmp')))

# Generated at 2022-06-14 18:06:30.859095
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockPostProcessor(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)
            self.warnings = []

        def report_warning(self, message):
            self.warnings.append(message)

    import sys
    import copy
    from collections import namedtuple
    from types import BuiltinFunctionType

    # On Windows, os.utime is a builtin method that can't be replaced
    # by mock.
    if sys.platform.startswith('win') and isinstance(os.utime, BuiltinFunctionType):
        raise Exception('This test can\'t be run on Windows')

    class MockOsModule(object):
        class error(Exception):
            pass


# Generated at 2022-06-14 18:06:42.831245
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time

    downloader = object
    pp = PostProcessor(downloader)

    # Touch a file in a such way that its atime and mtime are different
    os.system('touch example.file')
    if int(time.time()) % 2 == 0:
        time.sleep(1)
    os.system('touch -mt 201901010000 example.file')

    # Retrieve the values of atime and mtime
    stat = os.stat('example.file')
    atime = stat.st_atime
    mtime = stat.st_mtime

    # Modify the file's atime and mtime with try_utime of class PostProcessor
    pp.try_utime('example.file', 1234567890, 1234567890)

    # Retrieve the values of atime and mtime again
    stat

# Generated at 2022-06-14 18:06:47.056347
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.common import InfoExtractor
    from .ffmpeg import FFmpegPostProcessor
    ie = InfoExtractor({'outtmpl': '%(id)s.%(ext)s'})
    pp = FFmpegPostProcessor(ie)
    pp.try_utime('mydir', 1234, 5678)

# Generated at 2022-06-14 18:06:54.743198
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil

    import pytest
    from ..utils import dash_join

    class FakeDownloader():
        class FakeToString():
            pass

        class FakeLock():
            pass

        @property
        def params(self):
            return self.FakeToString()

        @params.setter
        def params(self, value):
            pass

        @staticmethod
        def report_warning(errnote):
            pass

        def to_screen(self, message, percent=None, status=None, error=False):
            pass

# Generated at 2022-06-14 18:07:02.090191
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    temp_file_name = temp_file.name
    try:
        old_time = os.stat(temp_file_name).st_mtime
        pp = PostProcessor(None)
        pp.try_utime(temp_file_name, old_time, old_time)
        assert os.stat(temp_file_name).st_mtime == old_time
    finally:
        os.unlink(temp_file_name)

# Generated at 2022-06-14 18:07:14.222480
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import stat
    import time

    import youtube_dl.postprocessor

    def get_mtime_atime(path):
        st = os.stat(path)
        return st[stat.ST_MTIME], st[stat.ST_ATIME]

    tmpdir = tempfile.mkdtemp()
    filename = os.path.join(tmpdir, 'foo.flv')
    with open(filename, 'w') as f:
        f.write('aaaaaaaaa')
    mtime, atime = get_mtime_atime(filename)
    time.sleep(3)
    pp = youtube_dl.postprocessor.PostProcessor(None)
    pp.try_utime(filename, atime, mtime)
    new_mtime, new_atime = get_mtime

# Generated at 2022-06-14 18:07:20.133615
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    s = object()
    pp = PostProcessor(downloader=s)
    class tester(object):
        def __init__(self, o):
            self._o = o
            self.warning_count = 0
        def report_warning(self, msg):
            assert msg == 'Cannot update utime of file'
            self.warning_count += 1
    s = tester(s)
    pp._downloader = s
    pp.try_utime('some path', 1, 2, errnote='Cannot update utime of file')
    assert s.warning_count == 1

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:07:21.284732
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # TODO
    pass

# Generated at 2022-06-14 18:07:27.610855
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader(object):
        def __init__(self):
            self.params = {
                'nooverwrites': False
            }
        def to_screen(self, msg):
            pass
        def report_warning(self, msg):
            pass
    downloader = MockDownloader()
    postprocessor = PostProcessor()
    postprocessor.set_downloader(downloader)
    postprocessor.try_utime('test.txt', 128895928, 128895928)

# Generated at 2022-06-14 18:08:02.531287
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import YoutubeIE
    from ..downloader.common import FileDownloader

    class MockPostProcessor(PostProcessor):
        def run(self, information):
            self.try_utime(information['filepath'], 0, 0)
            return [], information

    ydl = FileDownloader(YoutubeIE())
    ydl.params['postprocessor_args'] = [
        '--audio-format', 'mp3',
    ]
    postprocessor = MockPostProcessor()
    postprocessor.set_downloader(ydl)

    path = os.path.join(ydl.ydl_opts.download_archive, 'mp3', 'abc')
    with open(path, 'w') as f:
        pass
    information = {
        'filepath': path,
    }
    postprocessor.run

# Generated at 2022-06-14 18:08:10.828269
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractor
    from ..downloader import gen_downloader
    extractor = gen_extractor(params={})
    extractor._downloader = gen_downloader(params={})
    pp = PostProcessor(downloader=extractor._downloader)
    import sys
    import platform

    if sys.version_info[0] == 2:
        import errno
        # We need OSError under Python 2, not OSError under Python 3.
        # http://bugs.python.org/issue22416
        # It doesn't really matter which one we test here, as long as it is a subclass of Exception.
        if platform.system() == 'Windows':
            error_to_test = (WindowsError, errno.EACCES)

# Generated at 2022-06-14 18:08:21.040796
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from youtube_dl.utils import FakeYDL, DateRange
    pp = PostProcessor(FakeYDL({}))
    # We assume here that the code is run on a filesystem supporting atime and mtime
    f = open('test_file', 'w')
    f.write('toto')
    f.close()
    pp.try_utime('test_file', 100, 200)
    os.utime('test_file', (0, 0))
    dr = DateRange('1970-01-01T02:00:00Z', '1970-01-01T04:00:00Z')
    pp.try_utime('test_file', dr.start_time, dr.end_time)
    os.utime('test_file', (0, 0))

# Generated at 2022-06-14 18:08:29.574048
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPP(PostProcessor):
        def run(self, info):
            self.try_utime('test_file', 1539580018, 1539580018, errnote='Cannot update utime of file')

    from ..YoutubeDL import YoutubeDL
    import shutil
    import time

    test_file = open('test_file', 'wb')
    test_file.write(b'test')
    test_file.close()

    test_pp = TestPP()
    ydl = YoutubeDL()
    ydl.params['writedescription'] = False
    ydl.params['writeinfojson'] = False
    test_pp.set_downloader(ydl)
    test_pp.run({'id': 'test', 'filepath': 'test_file'})
