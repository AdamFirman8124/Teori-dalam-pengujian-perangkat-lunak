

# Generated at 2022-06-14 17:58:38.011480
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FakeYDL

    class FakePP(PostProcessor):
        def __init__(self, downloader):
            self._downloader = downloader
            self._downloaded_info = None

        def run(self, information):
            self._downloaded_info = information
            self.try_utime(information['filepath'], 1, 1234)

    fd, filepath = tempfile.mkstemp('.bin')
    os.fdopen(fd, 'wb').write(b'foo')
    try:
        pp = FakePP(FakeYDL())
        pp.run({'filepath': filepath})
    finally:
        os.remove(filepath)
    assert os.path.getatime(pp._downloaded_info['filepath']) == 1
    assert os.path.getmtime

# Generated at 2022-06-14 17:58:45.653254
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time
    import sys

    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 17:58:57.499161
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    PostProcessor.try_utime() raises a PostProcessingError exception.
    """
    import unittest
    from ytdl.downloader import FakeYDL
    from ytdl.postprocessor import PostProcessor

    class TestPostProcessor(PostProcessor):
        def run(self, info):
            return [], info

    downloader = FakeYDL()
    pp = TestPostProcessor(downloader)
    downloader.params['simulate'] = True
    downloader.report_warning = lambda msg: None
    downloader.report_error = lambda msg: None
    with unittest.TestCase() as test:
        try:
            pp.try_utime('test',0,0)
        except PostProcessingError:
            test.assertTrue(False)
        except Exception:
            test

# Generated at 2022-06-14 17:59:07.210522
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    from ..compat import temporary_named_temporary_file

    # Create a PostProcessor object
    pp = PostProcessor()

    # Create a temporary file
    temp_file = temporary_named_temporary_file()

    # Get the filename of the temporary file
    temp_file_name = temp_file.name

    # Modify the name of the temporary file to insert a unicode character
    # This is done to test that this method handles correctly unicode strings
    temp_file_name = temp_file_name.replace('tmp', u'\u2603')

    # Get the current time
    current_time = time.time()

    # Change the atime and mtime of the temporary file
    pp.try_utime(temp_file_name, current_time, current_time)

    # Check that the at

# Generated at 2022-06-14 17:59:19.210874
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # This can be copy and pasted in a unit test file
    # Create a BasePostProcessor instance
    from ..extractor import gen_extractors
    from ..downloader import gen_ydl

    _DOWNLOADER = gen_ydl()
    pp = PostProcessor(downloader=_DOWNLOADER)

    # Create a temporary file and files that links to it
    import tempfile
    import os


# Generated at 2022-06-14 17:59:30.659692
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import DateRange

    import tempfile

    # Create a temporary directory
    tmpd = tempfile.mkdtemp()

    # Create a temporary file
    tmpf = tempfile.NamedTemporaryFile(dir=tmpd, delete=False)
    tmpf.close()

    # Get file modification time
    st = os.stat(tmpf.name)
    orig_mtime = st.st_mtime

    # Create the downloader
    ydl = FileDownloader({'outtmpl': '%(id)s%(ext)s'})

# Generated at 2022-06-14 17:59:42.378869
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    from ..compat import compat_tempfile_gettempprefix
    from ..downloader.common import FileDownloader
    from ..utils import DateRange

    temp_prefix = compat_tempfile_gettempprefix()
    temp_dir = tempfile.mkdtemp(prefix=temp_prefix)


# Generated at 2022-06-14 17:59:52.634668
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ytdl.downloader import Downloader
    from ytdl.extractor import YoutubeIE
    def dummy_download(url, filename, info_dict, params):
        return {'filename': filename, 'tmpfilename': filename, 'status': 'finished'}
    downloader = Downloader()
    downloader.add_info_extractor(YoutubeIE())
    downloader.add_default_info_extractor(YoutubeIE())
    downloader.to_screen = lambda *_args: None
    downloader.post_processors = []
    downloader.result_store = []
    downloader.add_post_processor(PostProcessor())
    downloader.set_downloader(dummy_download)

# Generated at 2022-06-14 17:59:58.592206
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import datetime
    from ..downloader import get_suitable_downloader
    from .execafterdownload import ExecAfterDownloadPP
    from .xattrpp import XAttrMetadataPP

    def _test_function(downloader, path, atime, mtime):
        pp = XAttrMetadataPP()
        pp.set_downloader(downloader)
        pp.run({'filepath': path})
        pp = ExecAfterDownloadPP()
        pp.set_downloader(downloader)
        pp.run({'filepath': path})
        assert pp.try_utime(path, atime, mtime) is None


# Generated at 2022-06-14 18:00:08.173849
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    try:
        os.utime
        pass_test = True
    except AttributeError:
        pass_test = False
    try:
        os.utime('/')
        pass_test = False
    except Exception as e:
        if str(e)!='[Errno 13] Permission denied: \'/\'':
            pass_test = False
    pp.try_utime('/', 1000, 1000000)
    pp.try_utime('/', 1000, 999999, errnote='Fail')
    if pass_test:
        print('test_PostProcessor_try_utime test pass')
    else:
        print('test_PostProcessor_try_utime test fail')


# Generated at 2022-06-14 18:00:16.084152
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil
    # we need to make up a time that has already passed
    access_time = time.time() - 86400
    modify_time = access_time + 86400
    # get a temporary directory
    temp_dir = tempfile.mkdtemp()
    # make up a file in that directory
    temp_file = os.path.join(temp_dir, 'temp_file')
    with open(temp_file, 'w'):
        pass
    # create a PostProcessor object
    pp = PostProcessor(None)
    # set last access and modify times
    pp.try_utime(temp_file, access_time, modify_time)
    # reset access and modify times
    access_time = modify_time = 0
    # get access and modify times
   

# Generated at 2022-06-14 18:00:26.780948
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import time
    from .compat import (
        compat_makedirs,
        compat_open,
    )
    from .downloader import Downloader

    tempdir = tempfile.mkdtemp()
    fd, path = tempfile.mkstemp(dir=tempdir)
    os.close(fd)

# Generated at 2022-06-14 18:00:35.656848
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    if sys.version_info < (2, 6, 0):
        # os.utime() is unsupported in Python 2.5
        print('Skipping test_PostProcessor_try_utime() because its requirements are not met')
        return

    from types import MethodType
    from tempfile import NamedTemporaryFile
    from time import time

    # Create a mock downloader object with a mock report_warning method
    class MockDownloader(object):
        pass
    MockDownloader.report_warning = MethodType(lambda self, message: None, None, MockDownloader)
    mock_downloader = MockDownloader()

    # Create a temporary file
    temp_file = NamedTemporaryFile(delete=False)

# Generated at 2022-06-14 18:00:45.866159
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import codecs
    import tempfile

    # Mock _downloader
    class Mock_downloader(object):
        def __init__(self):
            self._warn_messages = []
        def report_warning(self, message):
            self._warn_messages.append(message)

    # Mock file
    temp_file = tempfile.NamedTemporaryFile()
    atime = 10000
    mtime = 20000

    # Run test
    downloader = Mock_downloader()
    post_processor = PostProcessor(downloader)
    post_processor.try_utime(temp_file, atime, mtime)
    assert downloader._warn_messages == [] # At this point should not raise any warning

    # Run test
    temp_file = tempfile.NamedTemporaryFile()

# Generated at 2022-06-14 18:00:54.887511
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys

# Generated at 2022-06-14 18:01:07.539192
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import unittest

    from youtube_dl.utils import DateRange

    class DummyObject(object):
        def __init__(self):
            self.params = {}
            self.to_stdout = lambda x: x
            self._downloader = self

        def to_screen(self, s):
            print(s)
            self.to_stdout(s)

        def report_warning(self, s):
            self.to_screen(s)

    class DummyPostProcessor(PostProcessor):
        def __init__(self):
            super(DummyPostProcessor, self).__init__(DummyObject())

        def run(self, info):
            self.try_utime(info["filepath"], int(time.time()-30), int(time.time()-30))


# Generated at 2022-06-14 18:01:19.403778
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader
    from ..extractor import YoutubeIE

    class MockPP(PostProcessor):
        # It is a mock class just to test a method of class PostProcessor.
        def __init__(self, downloader=None):
            super(MockPP, self).__init__(downloader)
            self.called = False
        def run(self, info):
            self.try_utime("path", 1, 2)
            self.called = True

    downloader = FileDownloader({'outtmpl': '%(id)s.%(ext)s'})
    mock = MockPP(downloader)

    downloader.add_info_extractor(YoutubeIE())
    downloader.add_post_processor(mock)

    id = "BaW_jenozKc"
   

# Generated at 2022-06-14 18:01:26.215145
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    class DummyPostProcessor(PostProcessor): pass
    class DummyDownloader(FileDownloader):
        def report_warning(self, message):
            raise ValueError(message)
    dl = DummyDownloader({})
    pp = DummyPostProcessor(dl)
    try:
        pp.try_utime('test.file', 1, 2)
    except ValueError:
        assert False

# Generated at 2022-06-14 18:01:34.450752
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def run(self, information):
            return [], information

    import tempfile

    tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:01:39.973901
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    os.utime = None

    def utime(path, times):
        return times

    os.utime = utime
    assert pp.try_utime('dummy', 0, 1) is None

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:01:44.080445
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        raise PostProcessor('this is a test of PostProcessor_try_utime')
    except PostProcessor as e:
        assert(e.args[0] == 'this is a test of PostProcessor_try_utime')
    except Exception as e:
        assert(False)

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:01:56.174081
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import FakeYDL
    class FakePostProcessor(PostProcessor):
        def __init__(self, *args, **kwargs):
            super(FakePostProcessor, self).__init__(*args, **kwargs)
            self._warning_message = []

        def report_warning(self, msg):
            self._warning_message.append(msg)

    pp = FakePostProcessor()
    pp.set_downloader(FakeYDL())

    try:
        os.unlink(encodeFilename('test_PostProcessor_try_utime'))
    except:
        pass
    # Create a file that can not be modified
    with open('test_PostProcessor_try_utime', 'wb'):
        pass

# Generated at 2022-06-14 18:02:03.979029
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .common import TempFileName

    def raise_utime_error(*args, **kwargs):
        raise OSError('Permission denied')

    # Create post-processor with a dummy downloader
    postprocessor = PostProcessor(downloader=YoutubeDL(params={}))

    # Create test file name
    f = TempFileName(suffix='.tmp')

    # Test if try_utime works
    with open(f, 'w'):
        pass
    mtime = os.path.getmtime(f)
    postprocessor.try_utime(f, mtime, mtime)
    assert os.path.getmtime(f) == mtime

    # Test if try_utime logs error message
    with open(f, 'w'):
        pass


# Generated at 2022-06-14 18:02:13.727439
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import shutil

    class _Dummy_downloader(object):
        def report_warning(self, msg):
            raise AudioConversionError(msg)

    temp_dir = tempfile.mkdtemp()
    f = open(os.path.join(temp_dir, 'test.txt'), 'w')
    f.write('abc')
    f.close()
    downloader = _Dummy_downloader()
    pp = PostProcessor(downloader)
    pp.try_utime(os.path.join(temp_dir, 'test.txt'), 0, 0)
    shutil.rmtree(temp_dir)

# Generated at 2022-06-14 18:02:25.703917
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import filecmp
    import os
    import stat
    import shutil
    import sys
    import tempfile
    import time
    import unittest

    sys.path += ['.', '..']
    from postprocessor import PostProcessor  # noqa: E402

    class TestPostProcessor(PostProcessor):
        def __init__(self, params):
            self._downloader = params

    def createTestFile(name, mtime):
        f = open(name, 'wt')
        f.write('This is a test file')
        f.close()
        os.utime(name, (mtime, mtime))

    # Set up parameters for test
    temp_dir = tempfile.mkdtemp(prefix='yt-test_yt-postprocessor_')

# Generated at 2022-06-14 18:02:35.701736
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader(object):
        def report_warning(self, msg):
            self.msg = msg

    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(FakePostProcessor, self).__init__(downloader)
            self.origin = os.path.join(os.path.sep, 'tmp', 'origin')

        def run(self, information):
            return [], information

    # Create a fake file
    _, path = tempfile.mkstemp()
    path = encodeFilename(path)
    # Get atime and mtime of the file
    stat = os.stat(path)
    atime = stat.st_atime
    mtime = stat.st_mtime
    # Initialize fake downloader
    downloader = FakeDownloader

# Generated at 2022-06-14 18:02:41.491032
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Test class definition
    class TestPostProcessor(PostProcessor):
        pass
    # Test class instantiation
    test_pp = TestPostProcessor()
    # Test method try_utime
    try:
        test_pp.try_utime('',0,0,'')
    except AttributeError:
        # if we get an AttributeError, it means that the _downloader instance is not defined
        # this is the correct behavior
        return

# Generated at 2022-06-14 18:02:54.102032
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import stat
    import shutil
    import time

    from .YoutubeDL import YoutubeDL

    tmpdir = tempfile.gettempdir()

    mtime = time.time()

    org_time = time.time()
    file_info = {
        'id': 'test_video_id',
        'title': 'test_video_title',
        'ext': 'mp4',
        'filesize': 12345,
        'filepath': os.path.join(tmpdir, 'test_filepath'),
        'format': 'fakeformat',
        'format_note': 'fakeformatnote',
        'url': 'http://example.com/testvideo',
        'requested_formats': [],
    }

# Generated at 2022-06-14 18:03:02.624897
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    class MockDownloader(object):
        def __init__(self):
            self.report_warning_count = 0

        def report_warning(self, msg):
            self.report_warning_count += 1

    class MockPostProcessor(PostProcessor):
        pass

    pp = MockPostProcessor(MockDownloader())
    # Test if try_utime does not raise an exception
    pp.try_utime("tests/test_postprocessor.py", 100, 100)
    assert pp._downloader.report_warning_count == 0


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:03:11.460427
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    '''
    test_PostProcessor_try_utime unit test for method try_utime of class PostProcessor
    '''
    from ..utils import DateRange

    from .common import FakeYDL

    post = PostProcessor(FakeYDL())

    # Create a file
    try:
        with open('test_try_utime', 'w'):
            pass
    except IOError:
        assert False

    # Get atime and mtime of the file
    old_stat = os.stat('test_try_utime')

    # Set future date
    date = DateRange(start='2030-01-01').get_upper_limit()

    # Call try_utime method
    post.try_utime('test_try_utime', date, date)

    # Get new atime and mtime of the file

# Generated at 2022-06-14 18:03:22.348168
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    path = encodeFilename('test')
    try:
        os.utime(path, (0, 1))
    except OSError:
        pass

# Generated at 2022-06-14 18:03:29.866920
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    upload_date = '20120101'
    from ..extractor import gen_extractors
    gen_extractors()
    from .. YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl._ies = []

# Generated at 2022-06-14 18:03:37.296598
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    fd, filename = tempfile.mkstemp()

    # Create file and set modification time to zero
    os.write(fd, 'test')
    os.close(fd)
    os.utime(filename, (0, 0))
    assert(os.stat(filename).st_mtime == 0)

    # Update modification time
    test_postprocessor = PostProcessor(None)
    test_postprocessor.try_utime(filename, None, 1)
    assert(os.stat(filename).st_mtime == 1)

    # Cleanup
    os.remove(filename)

# Generated at 2022-06-14 18:03:47.431190
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Very simple unit test for method try_utime."""
    import sys
    import os
    import time
    import shutil
    import tempfile

    # Create a temp directory to store temporary files
    tmpdir = tempfile.mkdtemp()

    # Name of the file to test method try_utime
    filename = 'file.txt'
    # Path of the file to test method try_utime
    filepath = os.path.join(tmpdir, filename)

    # Create the file to test method try_utime
    with open(filepath, 'w') as tmp_file:
        tmp_file.write('abcdef')

    # Set the modification and access times of the created file
    atime = mtime = time.time() - 100

    # Call method try_utime to print its traceback

# Generated at 2022-06-14 18:03:49.848400
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # We don't set _downloader attribute for tests
    pp = PostProcessor()
    assert pp.try_utime('f', 1, 2) is None

# Generated at 2022-06-14 18:04:01.207811
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import errno
    import os
    import tempfile

    path = tempfile.mktemp()
    open(path, 'w').close()

    class Downloader():
        def report_warning(self, errnote):
            self.errnote = errnote

    pp = PostProcessor(Downloader())
    errnote = 'Cannot update utime of file'
    pp.try_utime(path, 1, 2, errnote)

    assert pp._downloader.errnote == errnote, 'PostProcessor.try_utime() failed'

    os.unlink(path)

# Generated at 2022-06-14 18:04:10.740377
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    pp = PostProcessor()
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test", "try_utime")
    # Check that filepath exists and that it is not a directory
    assert(os.path.exists(filepath) and not os.path.isdir(filepath))
    # Check that the last modification timestamp differs from the last access timestamp
    assert(os.path.getmtime(filepath) != os.path.getatime(filepath))
    # Check that the last modification timestamp is closer to the current time than the last access timestamp

# Generated at 2022-06-14 18:04:21.590466
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class PP(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)
            self.file_to_test = ''
            self.original_utime = None

        def run(self, information):
            self.original_utime = os.path.getatime(self.file_to_test), os.path.getmtime(self.file_to_test)
            self.try_utime(self.file_to_test, 0, 0)
            return [], information

    import tempfile
    import shutil
    import sys

    class DummyDownloader():
        def __init__(self):
            self.params = {'postprocessor_args': []}

        def report_warning(self, msg):
            print(msg)

    directory

# Generated at 2022-06-14 18:04:24.466824
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Create a PostProcessor instance for testing purpose
    from ..YoutubeDL import YoutubeDL

# Generated at 2022-06-14 18:04:27.530582
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        pp = PostProcessor()
        pp.try_utime(None, None, None)
    except PostProcessingError:
        pass
    else:
        assert False, 'Expected exception'

# Generated at 2022-06-14 18:04:45.461763
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import sys
    import errno

    if sys.platform == 'win32':
        import ctypes
        if ctypes.windll.kernel32.SetFileTime(
                0, None, None, (1, 1)) == 0:
            # Not supported on this version of Windows
            return

    # Create a zero byte file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        path = temp_file.name
        temp_file.write(b'')

    # Test to see if utime can be set on a file
    errnote = "Cannot set utime on file"
    pp = PostProcessor(None)


# Generated at 2022-06-14 18:04:55.479669
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakePostProcessor(PostProcessor):
        def run(self, information):
            if 'created_date' in information:
                return self.try_utime(information['filepath'],
                                      information['created_date'],
                                      information['created_date'])
            else:
                return self.try_utime(information['filepath'], 0, 0)

    # Create a fake file
    import tempfile
    FILE_NAME = tempfile.NamedTemporaryFile().name

    # Get the current utime of the file
    from os.path import getatime, getmtime
    FILE_ATIME = getatime(FILE_NAME)
    FILE_MTIME = getmtime(FILE_NAME)

    # Change the file utime
    import time
    NEW_UTIME = time.time()

   

# Generated at 2022-06-14 18:05:07.101654
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkstemp
    from ..YoutubeDL import YoutubeDL
    from ..utils import delete_file
    from time import time

    def get_file_utime(path):
        return os.stat(encodeFilename(path)).st_mtime

    # Create a dummy info dict
    info = {
        'id': 'testpostprocessor',
        'title': 'testpostprocessor',
        'ext': 'mp3',
        'format': '22'
    }

    # Create a dummy downloader
    ydl = YoutubeDL()

    # Create a dummy PostProcessor
    pp = PostProcessor(ydl)

    # Create a new temp file
    handle, path = mkstemp()

    # Set the file mtime
    mtime = time()

# Generated at 2022-06-14 18:05:18.457082
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import pytest
    class StupidDownloader(object):
        def report_warning(self, msg):
            assert msg == 'Cannot update utime of file'
            self.report_warning_called = True
    import os
    import time
    import tempfile
    pp = PostProcessor(StupidDownloader())
    tmpfile = tempfile.NamedTemporaryFile()
    pp.try_utime(tmpfile.name, 1234, 4321)
    assert pp._downloader.report_warning_called
    t = os.stat(encodeFilename(tmpfile.name)).st_mtime
    if t > 4321:
        pytest.fail('unexpected mtime %f, expected 4321' % t)

# Generated at 2022-06-14 18:05:28.609516
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import shutil
    import datetime

    from ..utils import date_from_str
    from ..compat import PY2
    pytest = sys.modules['pytest']

    tmp = tempfile.mkdtemp()

    if PY2:
        temp_file = os.path.join(tmp, 'temp.txt')
    else:
        temp_file = os.path.join(tmp, 'temp中文.txt')


# Generated at 2022-06-14 18:05:33.478890
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import common
    from .common import DownloaderTest
    import os
    import time

    class MockDL(object):
        def __init__(self):
            self.to_stderr = self.to_screen = self._err_warning_count = 0
        def report_warning(self, errnote):
            self._err_warning_count += 1
    class MockPP(PostProcessor):
        def __init__(self, dl):
            self.set_downloader(dl)
    filepath='mock_file'
    now = time.time()
    last_modified = now - 10
    last_accessed = now - 20

# Generated at 2022-06-14 18:05:45.109356
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import sys
    import tempfile
    import time
    import unittest

    import youtube_dl.utils

    class FakeYDL(object):
        def __init__(self):
            self.progress_hooks = []
            self.params = {
                'prefer_insecure': False,
                'youtube_include_dash_manifest': False,
                'youtube_skip_dash_manifest': False,
            }

        def add_progress_hook(self, hook):
            self.progress_hooks.append(hook)

        def to_screen(self, *args, **kwargs):
            pass

        def report_warning(self, *args, **kwargs):
            pass

    class FakeOptions(object):
        preference = None

    ydl = FakeYDL()

# Generated at 2022-06-14 18:05:55.627012
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .testcommon import FakeYDL
    from datetime import datetime

    d = FakeYDL()
    pp = PostProcessor(d)

    class DummyOSModule:
        def utime(self, path, times):
            self.path = path
            self.atime, self.mtime = times

    class DummyOSModuleFail:
        def utime(self, path, times):
            raise IOError()

    dummy = DummyOSModule()
    dummy_fail = DummyOSModuleFail()

    import sys
    old_os = sys.modules['os']
    old_os_mtime = old_os.mtime
    sys.modules['os'] = dummy

    # Test normal behavior
    pp.try_utime('foo', 1, 2)
    assert dummy.path == encodeFilename('foo')
   

# Generated at 2022-06-14 18:06:04.550978
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import GenericIE
    from ..downloader.common import FileDownloader

    class TestPP(PostProcessor):
        def run(self, info):
            atime, mtime = info['filetime']
            if atime:
                self.try_utime(info['filepath'], atime, mtime)
            return [], info

        def _configuration_args(self, default=[]):
            return []

    dl = FileDownloader(params={
        'format': 'bestaudio/best',
        'postprocessor_args': ['-x', '--audio-format', 'vorbis', '-vn'],
        'proxy': 'localhost:8118',  # tor
    })
    dl.add_info_extractor(GenericIE())

# Generated at 2022-06-14 18:06:13.154231
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class Dummy:
        def report_warning(self, *args, **kwargs):
            print("Warning: %s" % args[0])

    import time, sys
    if sys.version_info[0] == 3:
        from io import StringIO
    else:
        from io import BytesIO as StringIO
    import logging
    import os.path

    fname = os.path.join(os.path.expanduser('~'), 'ytdl_test_file')
    try:
        os.remove(fname)
    except OSError:
        pass
    f = open(fname, 'wb')
    f.write(b'\x01\x02\x03\x04')
    f.close()
    dl = Dummy()

# Generated at 2022-06-14 18:06:34.802987
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import os
    import time

    downloader = object()
    downloader.to_screen = lambda x: x
    downloader.report_warning = lambda x: x
    pp = PostProcessor(downloader)
    tempdir = os.path.abspath(os.path.realpath('pydl_test_tempdir'))
    os.mkdir(tempdir)
    fn1 = os.path.join(tempdir, 'fn1')
    fn2 = os.path.join(tempdir, 'fn2')

# Generated at 2022-06-14 18:06:39.630932
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import common

    def utime_raise_oserror(path, attrs):
        raise OSError(1, 'Operation not permitted')

    def utime_raise_ioerror(path, attrs):
        raise IOError(1, 'Operation not permitted')
    _pp = PostProcessor(downloader=common.FileDownloader(params={'outtmpl': '%(id)s', 'continuedl': False, 'restrictfilenames': True}))
    _pp.try_utime('dummy_path', 0, 0)

    _pp.try_utime = utime_raise_oserror
    _pp.try_utime('dummy_path', 0, 0)

    _pp.try_utime = utime_raise_ioerror

# Generated at 2022-06-14 18:06:49.340664
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time
    import os

    # 1. Create a PostProcessor object without parameters.
    postProcessor = PostProcessor()

    # 2. Create a temporary folder for the test.
    temp_dir = tempfile.mkdtemp(prefix='ytdl_postProcessor')
    # 3. Create an empty file
    file_path = os.path.join(temp_dir, 'file')
    open(file_path, 'a').close()

    # 4. Get current time
    current_time = time.time()
    # 5. Update the time of the file
    postProcessor.try_utime(file_path, current_time, current_time)

    # 6. Get the time of the file
    file_time = os.path.getmtime(file_path)

# Generated at 2022-06-14 18:06:55.245018
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Verifies fix for <https://github.com/rg3/youtube-dl/issues/2489>."""

    pp = PostProcessor(None)
    atime = mtime = 100

    # Pretend the file doesn't exist
    import errno
    def os_utime(path, times):
        # Emulate OSError
        raise OSError(errno.ENOENT, 'File not found')
    pp.os_utime = os_utime

    def report_warning(errnote):
        assert errnote == 'Cannot update utime of file'
    pp._downloader.report_warning = report_warning

    pp.try_utime('foo', atime, mtime)

# Generated at 2022-06-14 18:07:05.142105
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil
    import sys
    import os
    import subprocess
    from ytdl_web.core.extractor import InfoExtractor
    from ytdl_web.postprocessor import PostProcessor
    from ytdl_web.downloader import YoutubeDL
    from ytdl_web.compat import compat_os_name, compat_shlex_split
    from ytdl_web.utils import safe_filename, real_path

    def _run_ytdl_postprocessor(postprocessor, fname='test.mp3'):
        ie = InfoExtractor('test')
        ie._results = [{
            'id': 'test',
            'title': 'test',
            'ext': 'mp3',
            'url': 'http://test.de/test.mp3'
        }]


# Generated at 2022-06-14 18:07:07.353133
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # TODO
    # Implement this unit test for method try_utime of class PostProcessor
    pass

# Generated at 2022-06-14 18:07:16.919359
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(TestPostProcessor, self).__init__(downloader)
            self.errnote = ''
            self.atime = ''
            self.mtime = ''
            self.called = False
            self.path = ''

        def run(self, info):
            self.called = True
            self.path = info['filepath']
            self.try_utime(self.path, self.atime, self.mtime, self.errnote)
            return [], info

    class TestDownloader(object):
        def __init__(self, warning=None):
            self.reported = []
            self.warning = warning
        
        def report_warning(self, errnote):
            self.reported.append

# Generated at 2022-06-14 18:07:28.987697
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import FakeYDL
    from .compat import PY2
    from sys import platform

    # Skip utime test for Windows
    if platform.startswith('win'):
        return

    ydl = FakeYDL()

    pp = PostProcessor(ydl)

    # Check for exception when file does not exist
    try:
        pp.try_utime('not_a_file', 1, 1)
    except PostProcessingError:
        pass

    # Check for exception when permissions are bad
    path = encodeFilename('file_with_bad_permissions')
    if not PY2:
        path = path.decode('utf-8')
    with open(path, 'w+') as f:
        f.write('data')
    os.chmod(path, 0o200)

# Generated at 2022-06-14 18:07:35.769635
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import time
    from ..utils import PostProcessor
    from ..compat import compat_makedirs

    def get_test_filepath(filename):
        temp_dir = tempfile.mkdtemp(prefix='test_postprocessor_try_utime_')
        return os.path.join(temp_dir, filename)

    test_filepath = get_test_filepath('test.txt')
    file_time_mtime = time.time()
    file_time_atime = file_time_mtime + 100
    open(test_filepath, 'a').close()
    mtime_old = os.path.getmtime(test_filepath)
    atime_old = os.path.getatime(test_filepath)
    os.utime

# Generated at 2022-06-14 18:07:46.152828
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import time
    from ..utils import PostProcessor

    pp = PostProcessor(None)

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    # Create a file
    tfile = os.path.join(tmpdir, "tfile.txt")
    with open(tfile, 'w') as f:
        f.write('Test file')
    # Get current modification time
    current_mtime = os.path.getmtime(tfile)
    # Change modification time of file
    pp.try_utime(tfile, 0, int(current_mtime) - 10000)
    # Verify that mtime has been changed
    new_mtime = os.path.getmtime(tfile)
    assert new_mtime < current_

# Generated at 2022-06-14 18:08:20.808549
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        os.utime('/notexists', (0, 0))
    except Exception as e:
        assert(isinstance(e, OSError))
        utime_exception = e

    pp = PostProcessor(None)
    assert(pp.try_utime('/notexists', 0, 0) is None)
    assert(pp.try_utime('/notexists', 0, 0, errnote='Errnote') is None)

# Generated at 2022-06-14 18:08:25.663893
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import FakeYDL
    from .testprovider import TestPostProcessor

    test = TestPostProcessor()
    test.set_downloader(FakeYDL())

    info = {
        'id': 'fakeid',
    }

    # Set the path to a non-existing file, so it will fail.
    info['filepath'] = 'thispathdoesnotexist'
    with test:
        empty = test.run(info)

    # Set the path to an existing file, so it will succeed.
    info['filepath'] = 'youtube-dl/__init__.py'
    with test:
        empty = test.run(info)

# Generated at 2022-06-14 18:08:34.035331
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest
    from .test_utils import TestDownloadManager
    from .extractor import JWPlatformIE
    from .utils import sanitize_open

    class FakeDL(object):
        def report_warning(self, msg):
            print(msg)

    class FakeJWIE(JWPlatformIE):
        def _real_extract(self, url):
            return {
                'id': '1234',
                'title': 'Fake title',
                'upload_date': '20150101',
                'creator': 'Fake author',
                'webpage_url': 'http://example.com/video/1234',
                'url': 'http://example.com/video/1234.mp4',
            }
    class FakePostProcessor(PostProcessor):
        def __init__(self):
            Post