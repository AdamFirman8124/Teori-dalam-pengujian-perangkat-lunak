

# Generated at 2022-06-14 17:58:40.882641
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    class FakeDownloader(object):
        def report_warning(self, msg):
            self.msg = msg

    class FakeFileSystem(object):
        def __getitem__(self, filename):
            raise Exception("Boom!")

        def utime(self, filename, times):
            pass

    class FakePostprocessor(PostProcessor):
        def __init__(self, downloader=None, file_system=None, filename_encoding=None):
            self.fs = file_system
            PostProcessor.__init__(self, downloader)

        def try_utime(self, path, atime, mtime):
            PostProcessor.try_utime(self, path, atime, mtime)

    fs = FakeFileSystem()
    d = FakeDownloader()

# Generated at 2022-06-14 17:58:50.084280
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Test the method try_utime of class PostProcessor."""
    import os
    from ..utils import encodeFilename, tmp_filename
    from .common import FileDownloader
    from .compat import compat_makedirs
    path = encodeFilename(tmp_filename('PostProcessor_try_utime.txt'))
    compat_makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write('test')
    try:
        ydl = FileDownloader()
        ydl.add_post_processor(PostProcessor())
        ydl._do_post_process({'filepath': path}, None)
    finally:
        os.remove(path)

# Generated at 2022-06-14 17:58:58.625817
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import subprocess
    import shutil

    # Try delete non-existent file
    p = PostProcessor()
    path = os.path.join(tempfile.gettempdir(), 'non-existent')
    p.try_utime(path, 0, 0)
    assert not os.path.exists(path)

    # Create a file and update its access time
    path = os.path.join(tempfile.gettempdir(), 'existent')
    subprocess.check_call(['touch', path])
    atime = os.path.getatime(path)
    p.try_utime(path, atime + 1, 0)
    assert os.path.getatime(path) != atime
    shutil.rmtree(path)

# Generated at 2022-06-14 17:59:06.304135
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class test_PostProcessor(PostProcessor):
        def run(self, information):
            os.utime(information['filepath'], (10, 20))
            return [], information
    test_downloader = DummyYDL()
    pp = test_PostProcessor(test_downloader)
    pp.run({'filepath': 'file'})
    assert test_downloader.warnings['Cannot update utime of file'] == 1
    pp.try_utime('file', 10, 20)
    assert test_downloader.warnings['Cannot update utime of file'] == 2



# Generated at 2022-06-14 17:59:13.923895
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    class TestPostProcessor(PostProcessor):
        def run(self, information):
            if information['filepath'] == 'file1.mp4':
                # change creation time to the past
                self.try_utime('file1.mp4', 100000, 100000, 'Cannot change creation time')
            elif information['filepath'] == 'file2.mp4':
                # change modification time to the future
                self.try_utime('file2.mp4', 200000000, 200000000, 'Cannot change modification time')
            else:
                raise ValueError('unknown information %r' % information)
            return [], information
    class TestDownloader(FileDownloader):
        def __init__(self, params):
            self.params = params
            self.to_st

# Generated at 2022-06-14 17:59:23.327562
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MyPostProcessor(PostProcessor):
        pass
    mypostprocessor = MyPostProcessor()
    try:
        mypostprocessor.try_utime('./test_PostProcessor_try_utime.txt', 100, 200)
        assert False  # Exception is expected to be raised
    except PostProcessingError:
        pass
    filename = './test_PostProcessor_try_utime.txt'
    myfile = open(filename, 'w')
    myfile.close()
    mypostprocessor.try_utime(filename, 100, 200)
    os.remove(filename)

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 17:59:24.898505
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    # TODO: how to test Try_utime?
    return True



# Generated at 2022-06-14 17:59:30.061621
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    post_processor = PostProcessor()
    try:
        post_processor.try_utime('/some/path', 1, 2, 'error')
        raise AssertionError('unexpected success')
    except PostProcessingError as e:
        assert str(e) == 'error'

# Generated at 2022-06-14 17:59:37.389633
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import DateRange

    class DummyDownloader(object):
        def __init__(self):
            self.params = {
                'date': DateRange.day(2016, 8, 27),
                'ignoreerrors': True,
            }

        def report_warning(self, message):
            print('Warning: %s' % message)

    pp = PostProcessor(downloader=DummyDownloader())
    pp.try_utime('test.txt', 1472123090, 1472123091, errnote='Cannot update utime of test.txt')

# Generated at 2022-06-14 17:59:39.114606
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Unit test not possible because this method calls to external code
    pass

# Generated at 2022-06-14 17:59:49.541113
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # A small test, without mocking of time, since that seems to be hard.
    # Since we're testing a method that involves time and time.time() is
    # a poor choice for testing, this uses time.clock() instead,
    # which is a simple wall clock timer.
    import time

    # time.clock() schedules a process to be executed upon exit
    # http://docs.python.org/2/library/time.html#time.clock
    # This is a problem for unit tests, and so we remove it here.
    if hasattr(time, '_exit_function'):
        del time._exit_function

    # Simulate a few seconds later for the atime and mtime.
    start = time.clock()
    temp_file = open('a', 'w')
    temp_file.close()
    pp = PostProcessor

# Generated at 2022-06-14 17:59:56.582875
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import DateRange

    from .common import PostProcessorTestCase
    from .mocks.file_io import File
    from .mocks.test_utils_read_json import JsonTestParser

    class MockFileDownloader(FileDownloader):
        def report_warning(self, msg):
            pass

        def to_screen(self, msg):
            pass

    class MockPostProcessor(PostProcessor):
        def run(self, information):
            return [['file_name.mkv']], information

        def try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
            os.utime(encodeFilename(path), (atime, mtime))


# Generated at 2022-06-14 18:00:03.212516
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile, sys
    tmpfd, tmpfname = tempfile.mkstemp()
    tmpf = os.fdopen(tmpfd, 'w')
    tmpf.close()

    class DummyDownloader():
        params = {}
        def report_warning(self, errnote):
            sys.stderr.write('%s\n' % errnote)

    pp = PostProcessor(DummyDownloader())

    pp.try_utime(tmpfname, 0, 0, 'Cannot update utime of file: %s' % tmpfname)
    os.remove(encodeFilename(tmpfname))



# Generated at 2022-06-14 18:00:12.329213
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader

    fd_test = FileDownloader('http://www.youtube.com/watch?v=BaW_jenozKc', params={})
    test_file = os.path.abspath(__file__)
    pp = PostProcessor(fd_test)

    # Test regular case
    utime_before, stat_before = os.path.getmtime(test_file), os.stat(test_file)
    pp.try_utime(test_file, utime_before + 1, utime_before + 1)
    utime_after, stat_after = os.path.getmtime(test_file), os.stat(test_file)
    assert utime_after > utime_before and stat_after.st_atime > stat_before.st_at

# Generated at 2022-06-14 18:00:14.286894
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time

    t = time.time()
    path = 'ffmpeg'
    p = PostProcessor()
    p.try_utime(path, t, t, 'Cannot update time')

# Generated at 2022-06-14 18:00:26.107619
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    try:
        os.remove("test.txt")
    except:
        pass
    os.utime("test.txt", None)  # raises error as file does not exist
    pp.try_utime("test.txt", 1234567, 89101112)  # should fail silently
    open("test.txt", "w").close()  # create file
    assert os.path.getatime("test.txt") == 0 and os.path.getmtime("test.txt") == 0
    os.utime("test.txt", (1234567, 89101112))  # set time of file
    pp.try_utime("test.txt", 1234567, 89101112)  # should set time to same value

# Generated at 2022-06-14 18:00:28.572131
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime("test.notexists", 0, 0)
    pp.try_utime("test.notexists", 0, 0, 'test')

# Generated at 2022-06-14 18:00:37.694050
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import os
    import unittest
    import shutil
    import tempfile

    class Test(unittest.TestCase):
        def setUp(self):
            self.tempdir = tempfile.mkdtemp()
            self.tempfile = os.path.join(self.tempdir, 'temp.txt')
            open(self.tempfile, 'a').close()
            self.pp = PostProcessor(None) # mock downloader

        def tearDown(self):
            if os.path.exists(self.tempdir):
                shutil.rmtree(self.tempdir)

        def test_normal(self):
            # Call the tested method and save the file timestamp for later comparison
            original_timestamp = os.stat(self.tempfile).st_mtime

            # Call the tested method

# Generated at 2022-06-14 18:00:41.817510
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .. import YoutubeDL
    from .test_utils import FakeYDL
    ydl = FakeYDL()
    pp = PostProcessor(ydl)
    pp.try_utime('test', 1, 2)
    assert ydl.has_message('Cannot update utime of file')

# Generated at 2022-06-14 18:00:53.202003
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..__main__ import YoutubeDL
    from tempfile import TemporaryDirectory
    from datetime import datetime, timedelta
    import time
    import os

    with TemporaryDirectory() as tmp_path:
        test_file = os.path.join(tmp_path, 'testfile')
        open(test_file, 'w').close()

        ydl = YoutubeDL()
        ydl.params['quiet'] = True
        pp = PostProcessor(ydl)

        assert os.path.exists(test_file), 'postprocessor_test.py: File does not exist.'

        # Get current modification and access time
        old_atime = os.path.getatime(encodeFilename(test_file))
        old_mtime = os.path.getmtime(encodeFilename(test_file))

        # Delta to add to

# Generated at 2022-06-14 18:01:05.896568
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    pp = PostProcessor(ydl)
    # Create a nex file
    with open('nex.tmp', 'w') as f:
        f.write('nex')
    # Test if utime works
    pp.try_utime('nex.tmp', 0, 0)
    # Test if try_utime catchs ValueError exception
    pp.try_utime('nex.tmp', 0, os.stat('nex.tmp').st_mtime)
    # Delete nex.tmp
    os.remove('nex.tmp')

# Generated at 2022-06-14 18:01:17.262938
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Mocking all needed objects
    import unittest
    import os
    import errno
    from collections import namedtuple
    from ..downloader import FileDownloader
    from ..utils import DateRange, encodeFilename
    FakeInfo = namedtuple('FakeInfo', ['filename', 'url', 'http_headers'])
    class FakeFD(unittest.TestCase):
        def __init__(self, testcase):
            self.testcase = testcase
            self.path = FakePath()
        def report_warning(self, warning):
            self.testcase.assertTrue(warning == 'Cannot update utime of file')
        def to_screen(self, message, skip_eol=False):
            pass
        def to_stdout(self, message):
            pass

# Generated at 2022-06-14 18:01:28.162834
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange
    import os
    import shutil
    import tempfile
    import unittest
    import urllib2

    class MockIE(InfoExtractor):
        def _real_extract(self, url):
            return {
                'id': 'mock_id',
                'upload_date': '20101010',
                'title': 'mock_title',
                'ext': 'mock_ext',
            }

    loop_counter = 0

    class MockYDL(YoutubeDL):
        def to_screen(self, s, skip_eol=False):
            pass

        def download(self, info_dict):
            global loop_counter
            loop_counter += 1

# Generated at 2022-06-14 18:01:35.094916
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from ..utils import sanitize_open
    import time
    import shutil
    import tempfile

    with tempfile.NamedTemporaryFile(dir=os.getcwd()) as f:
        f.write('test')

    pp = PostProcessor(Downloader({}))
    pp.try_utime(f.name, time.time(), time.time())
    # If no exceptions raised, then test is successful
    shutil.rmtree(f.name)

# Generated at 2022-06-14 18:01:43.666129
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .test_utils import FakeYDL
    import tempfile

    def utime(path, atime, mtime):
        raise IOError("Can't set utime")

    with tempfile.NamedTemporaryFile() as t:
        pp = PostProcessor(FakeYDL())
        pp.try_utime(t.name, 100, 200)
        pp._downloader.report_warning = lambda x: None
        pp.try_utime = utime
        pp.try_utime(t.name, 100, 200)
        pp._downloader.report_warning = lambda x: None



# Generated at 2022-06-14 18:01:55.905968
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .common import FakeDownloader
    from .postprocessor import PostProcessor
    import tempfile
    import os
    import time

    with tempfile.NamedTemporaryFile(suffix='.tmp') as tmp:
        pp = PostProcessor(None)
        pp.set_downloader(FakeDownloader({}))
        # pick a time about a minute ago
        # to make sure that time.time() isn't the same as the file system time
        # (which can be the case when e.g. mocking time.time() in unit tests)
        a_minute_ago = time.time() - 60
        pp.try_utime(tmp.name, a_minute_ago, a_minute_ago)
        atime, mtime = os.stat(tmp.name).st_atime

# Generated at 2022-06-14 18:02:03.807284
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # After creating the instance of PostProcessor, try_utime method of PostProcessor class can be called.
    # In the test case, we use open to create a new file on the disk, after that, set a different atime and mtime
    # to the file by using time.time, then we call the try_utime method in the PostProcessor class to update the 
    # utime of the file. If the utime of the file is updated successfully, the atime and mtime of the file will be
    # changed to be the same as the value we set.
    from datetime import timedelta
    import time
    import tempfile

    with tempfile.NamedTemporaryFile() as f:
        atime = time.time() - timedelta(days=1).total_seconds()

# Generated at 2022-06-14 18:02:15.142295
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import _common
    downloader = _common.FakeYDL({})
    pp = PostProcessor(downloader)
    import tempfile
    with tempfile.NamedTemporaryFile() as tmpf:
        path = tmpf.name
        import time
        import os
        atime = time.time() - 100
        mtime = atime - 100
        os.utime(path, (atime, mtime))
        assert os.stat(path).st_atime - atime < 1000
        assert os.stat(path).st_mtime - mtime < 1000
        pp.try_utime(path, atime + 10, mtime + 10)
        assert os.stat(path).st_atime - atime < 10
        assert os.stat(path).st_mtime - mtime < 10
        #reset!

# Generated at 2022-06-14 18:02:18.468204
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # This method is tested in test_utils module
    # test_utils.test_do_utime()
    pass

# Generated at 2022-06-14 18:02:28.808833
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import shutil
    import os.path
    import os

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp(prefix="yt-postprocessor-test-")

    # Create a file and check that is accessible for writing
    tmppath = os.path.join(tmpdir, "file.bin")
    f = open(tmppath, "wb")
    f.close()
    assert os.path.isfile(tmppath)

    # Add a permission to test that try_utime works
    os.chmod(tmppath, 0o444)
    assert not os.access(tmppath, os.W_OK)

    # Create a post processor with a fake downloader
    pp = PostProcessor(downloader=None)

    # Execute try_ut

# Generated at 2022-06-14 18:02:40.400120
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # 1) An object of PostProcessor
    pp = PostProcessor()
    path = __name__
    # 2) test of the method try_utime of the class PostProcessor
    pp.try_utime(path, 1, 2)
    # 3) AssertionError: the method try_utime should return None
    assert pp.try_utime(path, 1, 2) == None

# Generated at 2022-06-14 18:02:41.905288
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert PostProcessor().try_utime(__file__, 1, 2) is None

# Generated at 2022-06-14 18:02:54.139897
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from io import StringIO
    from types import ModuleType

    from .FakeYDL import FakeYDL

    # Create fake downloader object
    class FakeFileModule(object):
        def __init__(self):
            pass
        def utime(self, path, times):
            self._path = path
            self._times = times
    fake_file_module = FakeFileModule()
    fake_modules = {'file' : fake_file_module}

    class FakeModuleType(object):
        def __init__(self):
            pass
        def __getattr__(self, name):
            return fake_modules[name]
    fake_sys = FakeModuleType()
    class FakeModuleSpec(object):
        def __init__(self):
            self.name = 'sys'
            self.loader = FakeModuleType()

   

# Generated at 2022-06-14 18:03:04.333338
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import os
    import shutil
    import tempfile

    from .compat import TemporaryDirectory

    from ..utils import match_filter_func

    from .postprocessor import PostProcessor
    pp = PostProcessor()

    tmppath = tempfile.mkdtemp()
    testtmp = TemporaryDirectory(dir=tmppath)
    testdir = testtmp.name


# Generated at 2022-06-14 18:03:12.515251
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import os
    import shutil
    import tempfile
    if os.name == 'nt':
        import win32file
        import pywintypes
        from win32com.shell import shell
        from win32com.shell import shellcon
        # Force deletion on reboot
        FILE_FLAG_DELETE_ON_CLOSE = win32file.FILE_FLAG_DELETE_ON_CLOSE
        FILE_ATTRIBUTE_HIDDEN = win32file.FILE_ATTRIBUTE_HIDDEN
        INVALID_HANDLE_VALUE = win32file.INVALID_HANDLE_VALUE
        SHGFP_TYPE_CURRENT = shellcon.SHGFP_TYPE_CURRENT
        CSIDL_DESKTOPDIRECTORY = shellcon.CSIDL_DESKTOPDIRECTORY
       

# Generated at 2022-06-14 18:03:24.469297
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """ Checks if PostProcessor will not throw OSError while trying to update utime of file.
        In addition, checks if PostProcessor will throw a PostProcessingError exception
        if trying to update utime of directory.
    """
    from io import BytesIO
    from ..extractor import YoutubeIE
    from ..downloader import _Downloader
    from ..utils import (
        compat_urllib_parse,
        compat_urllib_request,
    )

    pp_true_path = os.path.join(os.path.dirname(__file__), 'post_processor_test_true')
    pp_false_path = os.path.join(os.path.dirname(__file__), 'post_processor_test_false')


# Generated at 2022-06-14 18:03:25.035354
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    return True

# Generated at 2022-06-14 18:03:36.673447
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil

    class FakeFile(file):
        def __init__(self, filename, mode):
            file.__init__(self, filename, mode)
            self._filename = filename

        def __del__(self):
            if self.closed:
                return
            self.close()

        def close(self):
            file.close(self)
            os.unlink(self._filename)


# Generated at 2022-06-14 18:03:47.186088
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile
    from youtube_dl.utils import DateRange
    from .downloader import FileDownloader
    from .extractor import get_info_extractor
    from .postprocessor import PostProcessor
    from .compat import urlopen, urlretrieve, url2pathname
    from .extractor.common import InfoExtractor
    from .compat import PY3
    from collections import namedtuple

    # Use a dummy downloader

# Generated at 2022-06-14 18:03:58.275934
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .YoutubeDL import YoutubeDL
    from .extractor.youtube import YoutubeIE
    from .postprocessor import FFmpegMetadataPP
    from .compat import compat_setenv

    # Mock FFmpegMetadataPP for unit test
    class Test_FFmpegMetadataPP(FFmpegMetadataPP):
        def _configuration_args(self, default=[]):
            return ['--no-post-overwrites']

    outtmpl = 'test_%(id)s.%(ext)s'
    youtube_dl = YoutubeDL({'outtmpl': outtmpl})
    info = YoutubeIE().extract('https://www.youtube.com/watch?v=BaW_jenozKc')
    info['filepath'] = outtmpl % info

# Generated at 2022-06-14 18:04:17.142374
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import compat_os_name
    from ..utils import DateRange
    
    pp = PostProcessor(None)
    atime = mtime = None
    errnote = 'No error'
    if compat_os_name == 'nt':
        atime = mtime = DateRange(timestamp_from=1.0).start
    pp.try_utime(__file__, atime, mtime, errnote)

# Generated at 2022-06-14 18:04:25.349519
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Unit test for method try_utime of class PostProcessor
    """
    import time
    import shutil
    # Currently, we test for the function in the following simple way:
    #
    # 1. Create a directory for testing.
    # 2. Create a file in the dir.
    # 3. Change utime of the file.
    # 4. Get utime of the file.
    # 5. Change the utime of the file using try_utime.
    # 6. Get utime of the file again to ensure it has been changed.
    test_dir = 'test_dir'
    test_file = 'test_file'
    errnote = 'Cannot update utime of file'
    # Create a directory for testing.
    os.mkdir(test_dir)
    # Create a file in the testing directory.

# Generated at 2022-06-14 18:04:33.322874
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    # We need a downloader
    class Downloader():
        def __init__(self):
            self.report_warning = lambda x: None
            self.params = {}
    downloader = Downloader()

    # We need a post-processor
    class PostProcessor(object):
        def __init__(self, downloader=None):
            self._downloader = downloader

    # We need a file
    import tempfile
    with tempfile.NamedTemporaryFile() as tf:
        post_processor = PostProcessor(downloader)
        post_processor.try_utime(tf.name, 0, 0) # Should not raise a error nor warning


# Test for retrieve_info method of PostProcessor class

# Generated at 2022-06-14 18:04:38.765140
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time

    pp = PostProcessor()
    path = 'utime_test_file'
    f = open(path, 'w')
    f.close()
    atime, mtime = time.time() - 100, time.time() + 100
    pp.try_utime(path, atime, mtime)
    os.remove(path)

# Generated at 2022-06-14 18:04:49.716451
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile

    class TestDownloader:
        def report_warning(self, message):
            self.message = message

    tmpfile = tempfile.NamedTemporaryFile()
    atime = os.stat(tmpfile.name).st_atime

    # Test try_utime with a read-only file
    os.chmod(tmpfile.name, 0o400)
    pp = PostProcessor(TestDownloader())
    pp.try_utime(tmpfile.name, atime, 0)
    os.chmod(tmpfile.name, 0o600)

    # Test try_utime with a file of which we have no read and write access
    os.chmod(tmpfile.name, 0o000)
    pp = PostProcessor(TestDownloader())

# Generated at 2022-06-14 18:04:56.709656
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import atexit
    import shutil
    class DummyPostProcessor(PostProcessor):
        pass
    dpp = DummyPostProcessor()
    tmpdir = tempfile.mkdtemp(prefix='youtubedl_utime_test_')
    atexit.register(lambda: shutil.rmtree(encodeFilename(tmpdir)))
    for path in ['foo', 'bar', 'bak/baz']:
        fullpath = os.path.join(tmpdir, path)
        dpp.try_utime(fullpath, 1149952271, 1149952272)
        assert os.path.exists(encodeFilename(fullpath)), 'The file %s not exist' % fullpath
        assert os.path.getatime(encodeFilename(fullpath)) == 114

# Generated at 2022-06-14 18:05:07.952741
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..compat import unittest

    class MockDownloader(FileDownloader):

        def __init__(self):
            pass

        def report_warning(self, msg):
            self.warning = msg

    class MockPostprocessor(PostProcessor):

        def __init__(self, downloader=None):
            self._downloader = downloader

    class PostprocessorTest(unittest.TestCase):
        def setUp(self):
            # Create some files
            self.temp_file = tempfile.mkstemp(suffix='.txt')[1]
            self.new_temp_file = tempfile.mkstemp(suffix='.txt')[1]
            self.downloader = MockDownloader()

# Generated at 2022-06-14 18:05:15.258746
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    _ = lambda x: x
    pp = PostProcessor()
    pp._downloader = type('FakeYTDL', (object,), {
        'report_warning': lambda *args: None,
    })()
    path = 'foo/bar'
    atime, mtime = 123, 456
    pp.try_utime(path, atime, mtime)
    # nothing raises, so it's OK


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:05:26.331245
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import time
    try:
        from unittest import mock
    except ImportError:
        import mock
    from . import fake_filesystem_unittest
    from .fake_filesystem_unittest import Patcher

    fs = fake_filesystem_unittest.FakeFilesystem()
    fake_os = fake_filesystem_unittest.FakeOsModule(fs)
    temp_cwd = tempfile.mkdtemp()
    fake_os.chdir(temp_cwd)
    patcher = Patcher(fs=fs, os_module=fake_os)
    patcher.setUp()
    print("Testing in nt")
    fake_os.name = 'nt'

# Generated at 2022-06-14 18:05:33.361196
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockPostProcessor(PostProcessor):
        def __init__(self):
            self.warning_message = None

        def report_warning(self, message):
            self.warning_message = message

    # Simulate os.utime raises exception and report warning message.
    mock_pp = MockPostProcessor()
    mock_pp.try_utime('/tmp/no-such-file', 1, 1)
    assert 'Cannot update utime of file' in mock_pp.warning_message
    mock_pp.try_utime('/tmp/no-such-file', 1, 1, 'Custom warning message')
    assert 'Custom warning message' in mock_pp.warning_message

# Generated at 2022-06-14 18:06:02.124209
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .test_utils import DownloaderMock

    class PostProcessorMock(PostProcessor):
        pass

    pp = PostProcessorMock(downloader=DownloaderMock())
    pp.try_utime('/dev/null', 0, 0)

# vim: expandtab sw=4 ts=4

# Generated at 2022-06-14 18:06:04.812841
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    args = ['a']
    pp.try_utime(*[None]*(len(args) + 1), errnote='a')

# Generated at 2022-06-14 18:06:13.308060
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import os
    import shutil

    # Create a directory and a file to test.
    temp_dir = tempfile.mkdtemp(prefix='youtubedl_test_utime')
    temp_name = os.path.join(temp_dir, 'testfile')
    with open(temp_name, 'w') as temp_file:
        temp_file.write('test')

    # Get original time and modify the time of the file to test.
    original_time = os.stat(temp_name).st_mtime
    os.utime(temp_name, (original_time, original_time-1000))
    assert abs(os.stat(temp_name).st_mtime-original_time) < 10, 'Test file was not created.'

    # Create a PostProcessor instance to

# Generated at 2022-06-14 18:06:13.977861
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass



# Generated at 2022-06-14 18:06:14.703619
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:06:25.357416
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    from ..downloader.common import FileDownloader

    def bn(n):
        return os.path.join(tempfile.gettempdir(), n)

    dl = FileDownloader(None)
    filepath = bn('file')
    open(filepath, 'wb').write(b'foo')
    atime = os.stat(filepath).st_atime
    mtime = os.stat(filepath).st_mtime
    time.sleep(1)
    pp = PostProcessor(dl)
    pp.try_utime(filepath, atime, mtime)
    assert os.stat(filepath).st_atime == atime
    assert os.stat(filepath).st_mtime == mtime

# Generated at 2022-06-14 18:06:28.883433
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    class Dummy(object):
        def report_warning(self, msg):
            assert msg == 'Cannot update utime of file'

    pp._downloader = Dummy()
    pp.try_utime('foo', 0, 0)

# Generated at 2022-06-14 18:06:32.138462
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime('/dev/null', 1, 2)

# Generated at 2022-06-14 18:06:43.069053
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from tempfile import mkstemp
    import time
    import os
    import shutil
    import sys

    fd, tmpfile = mkstemp(prefix='youtubedl_test_file_', suffix='.tmp')
    os.close(fd)
    fd, tmpdir = mkstemp(prefix='youtubedl_test_dir_', suffix='.tmp')
    os.close(fd)

    pp = PostProcessor(Downloader({'outtmpl': tmpdir}))

    # non existent file
    path = 'non_existent_file'
    pp.try_utime(path, 0, 1)
    assert not os.path.exists(encodeFilename(path))

    # valid file
    path = tmpfile

# Generated at 2022-06-14 18:06:52.190737
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # This method is not intended to be executed, but to be called by
    # unittest.
    # To make it work, replace the following line:
    raise AssertionError('This method is not intended to be executed.')
    # with something like:
    # import os
    # class FakeDownloader(object):
    #     def __init__(self):
    #         self.params = { }
    #     def to_screen(self, line):
    #         print line
    #     def report_warning(self, line):
    #         print 'WARNING: %s' % (line,)
    # dl = FakeDownloader()
    # pp = PostProcessor(dl)
    # pp.try_utime('/tmp/x', 0, 0)
    # os.unlink('/tmp/x')




# Generated at 2022-06-14 18:07:52.005436
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # We need a class that contains 'try_utime' method
    class Tester(PostProcessor):
        def try_utime(self, path):
            raise AudioConversionError
    ex = Tester()
    # We expect 'AudioConversionError' to be raised
    raised = False
    try:
        ex.try_utime('path')
    except AudioConversionError:
        raised = True
    if not raised:
        raise Exception('AudioConversionError not raised')

# Generated at 2022-06-14 18:08:00.974821
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os

    import shutil
    import tempfile
    TESTFN = tempfile.mktemp(prefix='yt-dl-test_try_utime', suffix='.txt')
    TESTFN2 = tempfile.mktemp(prefix='yt-dl-test_try_utime', suffix='.txt2')

    # Create a file
    with open(TESTFN, 'w') as f:
        f.write('test')

    class Downloader(object):
        params = {'test': '1'}
        def report_warning(self, msg):
            self.msg = msg

    # Get atime and mtime of the file
    lstat = os.lstat(TESTFN)
    creation_time = lstat.st_ctime
    modification_time = lstat.st_mtime

    # Keep them for later

# Generated at 2022-06-14 18:08:09.946434
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest

    # Create the test case
    class TestPostProcessor(unittest.TestCase):
        def setUp(self):
            os.path.exists = TestPostProcessor._fake_os_exists
            os.utime = TestPostProcessor._fake_os_utime

        @staticmethod
        def _fake_os_exists(path):
            return True

        @staticmethod
        def _fake_os_utime(path, atime, mtime):
            raise Exception('Fake exception')

        def test_try_utime(self):
            import sys

            # Create a PostProcessor object
            pp = PostProcessor(None)

            # Redirect stderr
            stderr = sys.stderr
            sys.stderr = open('/dev/null', 'w')

# Generated at 2022-06-14 18:08:20.804333
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time

    import pytest
    from .common import FakeYDL

    class FakePP(PostProcessor):
        def __init__(self):
            super(FakePP, self).__init__(downloader=FakeYDL())

    a_pp = FakePP()

    fn = './temp/test_PostProcessor_try_utime_file'
    with open(fn, 'w') as f:
        f.write('test')

    a_pp.try_utime(fn, 0, 0)
    stat = os.stat(fn)

    assert time.time() - stat.st_mtime < 1, 'time not reverted'

    with pytest.raises(PostProcessingError) as excinfo:
        a_pp.try_utime(fn + 'a', 0, 0)
    assert excinfo

# Generated at 2022-06-14 18:08:28.586950
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    from .common import FakeYDL
    from .downloader.common import ENCODING

    def test_function():
        tmp_fd, tmp_path = tempfile.mkstemp()

# Generated at 2022-06-14 18:08:39.084377
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import DateRange
    from .file import FilePostProcessor