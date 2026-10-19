

# Generated at 2022-06-14 17:58:32.552569
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def test_utime(path, atime, mtime):
        class TestDownloader(object):
            def report_warning(self, msg):
                pass
        postprocessor = PostProcessor(TestDownloader())
        postprocessor.try_utime('/tmp/ada', atime, mtime)
        return path
    assert '/tmp/ada' == test_utime('/tmp/ada', 1234567890, 1234567890)

# Generated at 2022-06-14 17:58:42.108970
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    if sys.version_info >= (3, 0):
        import unittest
        import tempfile
        import time
        import os

        test_file_1 = tempfile.NamedTemporaryFile(delete=False)
        test_file_1.close()
        test_file_2 = tempfile.NamedTemporaryFile(delete=False)
        test_file_2.close()

        class TestPostProcessor(PostProcessor):
            def __init__(self, *args):
                pass

        test_pp = TestPostProcessor()

        test_pp.try_utime(test_file_1.name, 0, 0)
        assert os.stat(test_file_1.name).st_atime == os.stat(test_file_1.name).st_mtime == 0

       

# Generated at 2022-06-14 17:58:52.137124
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Run unit test for PostProcessor.try_utime method."""
    # NOTE: This unit test is not meant to be run as part of a test suite.
    #       It should be run the following way:
    #
    #       python -c "from .postprocessor import test_PostProcessor_try_utime as test; test()"

    from ..downloader.common import FileDownloader

    downloader = FileDownloader({})
    postprocessor = PostProcessor(downloader)
    postprocessor._downloader.report_warning = lambda msg: print(msg)

    postprocessor.try_utime('absent_file.txt', 0, 0)
    postprocessor.try_utime('absent_file.txt', 0, 0, 'ignored')


# Generated at 2022-06-14 17:59:01.727135
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    _filename = 'testfile.txt'
    open(_filename, 'wb').close()
    fstat = os.stat(_filename)
    assert fstat.st_atime != 0 and fstat.st_mtime != 0
    fpp = PostProcessor()
    fpp.try_utime(_filename, 0, 0)
    fstat = os.stat(_filename)
    assert fstat.st_atime == 0 and fstat.st_mtime == 0
    fpp.try_utime(_filename, fstat.st_atime, fstat.st_mtime)
    fstat = os.stat(_filename)
    assert fstat.st_atime != 0 and fstat.st_mtime != 0
    os.unlink(_filename)

# Generated at 2022-06-14 17:59:06.922465
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import time
    from ..utils import PostProcessor
    tfile = tempfile.NamedTemporaryFile(delete=True)
    tfile.write('hello')
    tfile.flush()
    pp = PostProcessor(None)
    pp.try_utime(tfile.name, int(time.time()), int(time.time()))

# Generated at 2022-06-14 17:59:14.309735
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import os.path
    from ..downloader import Downloader
    from .common import FileDownloader
    from .xattrpp import XAttrMetadataPP
    from .execafterdownload import ExecAfterDownloadPP
    from .metadatafromtitle import MetadataFromTitlePP
    from .ffmpegmetadata import FFmpegMetadataPP
    from .embedthumbnail import EmbedThumbnailPP
    from .xattrmpp import XAttrMetadataPP as XAttrMPP

    # prepare test files
    mediafile = tempfile.NamedTemporaryFile()
    mediafile_length = 541
    mediafile.write(''.join(['A' for a in range(0, mediafile_length)]).encode('UTF-8'))
    mediafile.flush()

# Generated at 2022-06-14 17:59:16.137961
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime('/', None, None)

# Generated at 2022-06-14 17:59:17.417970
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # TODO: Implement this unit tests
    pass

# Generated at 2022-06-14 17:59:28.815527
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import DateRange
    from ..compat import compat_str
    from .tests.test_utils import TestsFilenameComparison
    from .tests.test_postprocessor_common import make_postprocessor

    postprocessor_test1 = make_postprocessor(None)
    assert isinstance(postprocessor_test1, PostProcessor)


# Generated at 2022-06-14 17:59:29.366018
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 17:59:38.831583
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import unittest

    class Test(unittest.TestCase):
        def test_utime(self):
            from ..utils import encodeFilename

            class MockDl(object):
                def report_warning(self, note):
                    pass
            dl = MockDl()
            pp = PostProcessor(downloader=dl)
            pp.try_utime(encodeFilename('/fake_file'), 1, 1)

    test = Test()
    test.test_utime()

# Generated at 2022-06-14 17:59:42.242941
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Importing here to avoid circular import
    from ..downloader.downloader import FileDownloader
    downloader = FileDownloader(params={})
    pp = PostProcessor(downloader)
    pp.try_utime('somepath', 0, 0)

# Generated at 2022-06-14 17:59:47.355222
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Create a PostProcessor object
    Check that method try_utime doesn't throw exceptions
    """
    os.utime = lambda x, y: None
    pp = PostProcessor(None)
    pp.try_utime("path", -1, -2)

# Generated at 2022-06-14 17:59:50.678172
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        os.utime('c:\\non existent',(0,0))
    except OSError:
        pass

    p = PostProcessor(None)
    p.try_utime('c:\\non existent', 0, 0)

# Generated at 2022-06-14 18:00:02.420719
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil
    from ..compat import PY2
    from ..utils import get_temp_dir, get_temp_file
    from .common import PostProcessorTestCase

    class PP(PostProcessor):
        def run(self, path):
            return []

    class TempdirPP(PP):
        def run(self, path):
            tmpdir = get_temp_dir()
            with open(os.path.join(tmpdir, 'test.txt'), 'w') as f:
                f.write('Hello')
            self.try_utime(tmpdir, 0, 0)
            return [], {}

    class TempfilePP(PP):
        def run(self, path):
            tmpfile = get_temp_file()

# Generated at 2022-06-14 18:00:13.244433
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time
    import os

    import pytest
    from .test_postprocessor import PostProcessor_test

    # Create a test directory and a dummy file to test
    temp_dir = tempfile.mkdtemp()
    test_file = os.path.join(temp_dir, 'test.txt')
    shutil.copy('LICENSE', test_file)

    # Get the last modified time and the last accessed time of test file
    # before making changes to the file.
    statinfo = os.stat(test_file)

    time.sleep(2)
    pp = PostProcessor_test(None)

    # Test if the method try_utime is able to update the last accessed time and the last modified time
    # of the test file

# Generated at 2022-06-14 18:00:20.929425
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Should raise nothing
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL(params={'writedescription': True})
    ydl.add_post_processor(PostProcessor)
    ydl.prepare_filename('1.mp3')
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])

# Generated at 2022-06-14 18:00:25.081826
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import FileDownloader
    from .YoutubeDL import YoutubeDL

    downloader = FileDownloader(params={})
    downloader.add_info_extractor(YoutubeDL())
    pp = PostProcessor(downloader)
    assert pp.try_utime('', 1, 1) == None

# Generated at 2022-06-14 18:00:35.836895
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .f4m_downloader import _process_f4m
    from .http_equiv_downloader import _process_http_equiv
    from .rtmp_downloader import _process_rtmp
    from .xattrs_adapter import _process_xattrs

    class FakePostProcessor(PostProcessor):
        def run(self, information):
            return [], information

    class FakeDownloader:
        @property
        def params(self):
            return {}

        def report_warning(self, errnote):
            pass

    downloader = FakeDownloader()
    p = FakePostProcessor(downloader)


# Generated at 2022-06-14 18:00:46.119322
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader
    from ..compat import PY2
    from .debug_pp import DebugPP


# Generated at 2022-06-14 18:00:56.001244
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import datetime
    import time

    # Create a test file
    fname = 'test_file.txt'
    with open(fname, 'w') as f:
        f.write('Hello World!')
    # Create a datetime.timedelta object a day before the next day
    d = datetime.datetime.today() + datetime.timedelta(days=1)
    # Create post processor object
    pp = PostProcessor(None, None)
    # Define variables for testing
    access_time = time.mktime(d.timetuple())
    modif_time = time.mktime(d.timetuple())
    errnote = 'Cannot update utime of file'
    # Test try_utime method

# Generated at 2022-06-14 18:01:08.088120
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import PY2
    from ..utils import DateRange
    from .common import FakeYDL
    from .testcommon import TestPostProcessor

    # Test to check if try_utime function calls the report_warning on an error.
    # This is done by creating a PostProcessor class, passing a FakeYDL
    # object to it and calling the try_utime method on it. The try_utime
    # method calls report_warning method of FakeYDL object, which will
    # change the value of the attribute 'called' of FakeYDL object.
    #
    # If report_warning is called, the value of 'called' will be 1 else 0

    f = FakeYDL({})
    pp = TestPostProcessor(f)
    pp.try_utime('foo', 1, 1)
    assert f.called

# Generated at 2022-06-14 18:01:19.487695
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import DateRange
    import sys
    import tempfile
    import shutil
    import os
    import stat
    import time

    class PostProcessorMock(PostProcessor):

        def __init__(self, downloader=None):
            PostProcessor.__init__(self, downloader)

        def run(self, information):
            # Record information for testing purposes
            self.information = information
            return super(PostProcessorMock, self).run(information)

    # Create temporary directories
    tempdir = tempfile.mkdtemp()
    outtmpl = os.path.join(tempdir, '%(id)s')


# Generated at 2022-06-14 18:01:22.571532
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    errnote = 'Cannot update utime of file'
    pp.try_utime('path', 1, 2, errnote)

# Generated at 2022-06-14 18:01:32.671040
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkstemp
    from .downloader import FileDownloader

    try:
        os.utime
    except:
        print('Cannot run test_PostProcessor_try_utime because os.utime does not exist.')
        return

    (tf, filepath) = mkstemp()

    # Test skipping utime on existing files
    downloader = FileDownloader({})
    pp = PostProcessor(downloader)
    pp.try_utime(filepath, 0, 0)

    # Test skipping utime on deleted files
    os.unlink(filepath)
    pp.try_utime(filepath, 0, 0)


# we want these to be global so that we don't create an infinite amount of
# copies with every download
# We want the pp to be on _downloader and not self in

# Generated at 2022-06-14 18:01:44.890998
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import time
    from ..extractor import get_info_extractor

    # Ensure that we a have a souphttpsrc downloader
    IE = get_info_extractor('youtube', downloader=None)
    assert IE._downloader.params.get('writedescription', False)

    Filename = 'test_postprocessor_try_utime.tmp'

    def get_N_last_lines(n):
        with open(Filename) as f:
            last_lines = f.readlines()[-n:]
        return last_lines

    temp_dir = tempfile.mkdtemp()
    Filename = os.path.join(temp_dir, Filename)

    # Test that the method ignores successfully the permission error

# Generated at 2022-06-14 18:01:57.006301
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import re
    import os
    import random

    # Skip test if python 2.x because "io.StringIO" is not available
    try:
        import io
    except ImportError:
        return

    import tempfile
    import unittest
    import warnings

    downloader = MockYoutubeDl()

    # Test utime with access denied
    tmpdir = tempfile.mkdtemp()
    file_path = os.path.join(tmpdir, 'temp')
    with open(file_path, 'w') as file:
        file.write('Temporary file')

    utime = int(random.random() * 10000)

    pp = PostProcessor(downloader)

    # Make file unalterable
    os.chmod(file_path, 0o444)
    pp.try_utime

# Generated at 2022-06-14 18:01:57.560269
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:02:04.167765
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import time
    import tempfile
    from ..utils import DateRange

    class FakeDownloader():
        def __init__(self, params):
            self.params = params

        def to_screen(self, message):
            if not isinstance(message, basestring):
                message = message.encode(sys.getfilesystemencoding(), 'ignore')
            print(message)

        def report_warning(self, message):
            self.to_screen(message)

    class FakePP(PostProcessor):
        def __init__(self, params, *args, **kwargs):
            super(FakePP, self).__init__(*args, **kwargs)
            self.params = params
            self.tmp_filename = tempfile.mkstemp()[1]
            self.tmp_filename_not_exist

# Generated at 2022-06-14 18:02:15.346158
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time

    assert os.path

    def set_utime(path, atime, mtime):
        os.utime(path, (atime, mtime))

    def get_utime(path):
        return os.stat(path).st_atime, os.stat(path).st_mtime

    old_set_utime = set_utime
    old_get_utime = get_utime


# Generated at 2022-06-14 18:02:28.932716
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    class Fake_PP(PostProcessor):
        def __init__(self):
            self._atime = time.time() - 3600
            self._mtime = time.time() - 60 * 60 * 24 * 7

    pp = Fake_PP()
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    pp.set_downloader(ydl)
    pp.try_utime('', pp._atime, pp._mtime)

# Generated at 2022-06-14 18:02:32.779133
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.params['verbose'] = True
    pp = PostProcessor(ydl)
    pp._downloader.report_warning = lambda x: None
    pp.try_utime(__file__, 1, 2)

# Generated at 2022-06-14 18:02:43.914492
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile

    class MockFFmpegPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(MockFFmpegPostProcessor, self).__init__(downloader)

    def get_test_filepath(filename):
        return os.path.join(tempfile.gettempdir(), filename)

    # Create a temporary file, and set its atime, mtime
    filename = 'youtube-dl-test-audio-conversion-atime-mtime-utime.tmp'
    test_filepath = get_test_filepath(filename)
    open(test_filepath, 'w').close()
    # Set atime, mtime
    os.utime(test_filepath, (100000, 200000))

    # Create a PostProcessor object with a

# Generated at 2022-06-14 18:02:54.520920
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .youtube_dl.downloader.common import FileDownloader

    class PostProcessorFake(PostProcessor):
        def __init__(self, downloader=None):
            self.errnote = None
            self.path = None
            self.atime = None
            self.mtime = None

        def run(self, information):
            self.try_utime(self.path, self.atime, self.mtime, self.errnote)

    with open(__file__, 'rb') as f:
        d = FileDownloader({'outtmpl': '%(id)s'}, None, None)
        pp = PostProcessorFake(d)

    pp.path = 'video.mp4'
    pp.atime = 100
    pp.mtime = 100

# Generated at 2022-06-14 18:03:04.611350
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import unittest
    from .common import TestCase

    class _TestPostProcessor(PostProcessor):
        def run(self, info):
            filepath = info['filepath']
            try:
                self.try_utime(filepath, 100, 200)
            except PostProcessingError:
                self.assertFalse(os.path.exists(filepath))
                self.assertRaises(PostProcessingError, self.try_utime, filepath, 100, 200)
            else:
                self.assertTrue(os.path.exists(filepath))
                self.assertEqual(100, os.stat(filepath).st_atime)
                self.assertEqual(200, os.stat(filepath).st_mtime)

# Generated at 2022-06-14 18:03:10.179520
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import time
    import unittest

    from ..compat import compat_os_path

    from ..utils import DateRange

    class FakePostProcessor(PostProcessor):
        pass

    class TestPostProcessor(unittest.TestCase):
        def setUp(self):
            self.pp = FakePostProcessor()
            self.pp.set_downloader(None)

        def test_try_utime_path_none(self):
            'Test try_utime method when path is None'
            path = None
            atime = 0
            mtime = 0

            self.assertRaises(PostProcessingError, self.pp.try_utime, path, atime, mtime)


# Generated at 2022-06-14 18:03:11.024619
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:03:19.722322
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FileDownloader
    class DummyPP(PostProcessor):
        def __init__(self, downloader):
            super(DummyPP, self).__init__(downloader)
        def run(self, info):
            self.try_utime('filename', 1234567, 7654321, 'cannot change utime')
            return info
    fd = FileDownloader({})
    pp = DummyPP(fd)
    pp.run({'id': 'video', 'title': 'video title', 'ext': 'mp4'})

# Generated at 2022-06-14 18:03:27.716106
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from tempfile import mkstemp
    import os

    dummy_data = b"0123456789"
    (fn, fn_path) = mkstemp(suffix='postprocessor-test')
    with open(fn_path, 'wb') as f:
        f.write(dummy_data)
    now = os.stat(fn_path).st_mtime
    ydl_opts = {'logger': YoutubeDL().logger}
    pp = PostProcessor(YoutubeDL(ydl_opts))
    pp.try_utime(fn_path, now+3600, now+3600, 'error')
    assert os.stat(fn_path).st_mtime > now

# Generated at 2022-06-14 18:03:33.137799
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkstemp
    from os import utime, unlink

    fd, name = mkstemp()
    os.close(fd)

    # Create file
    utime(name, None)

    pp = PostProcessor(None)
    pp.try_utime(name, 0, 0)  # should not throw exception

    # Delete file
    unlink(name)

# Generated at 2022-06-14 18:03:57.378556
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        raise PostProcessor_try_utime
    except TypeError:
        return 'TypeError'
    except Exception:
        return 'Exception'
    return 'No TypeError'

if test_PostProcessor_try_utime() != 'No TypeError':
    import stat
    import shutil
    import time
    import datetime
    import tempfile

    def test_PostProcessor_try_utime_make_file():
        if os.name == 'nt':
            raise ValueError('Windows doesn\'t support the utime command.')

        # create a file
        handle, path = tempfile.mkstemp()
        os.write(handle, 'test')
        os.close(handle)

        # update modified and access times
        now = time.time()

# Generated at 2022-06-14 18:04:09.347999
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .test_utils import FakeDownloader
    from tempfile import mkstemp

    # Create a 'file' with a fake timestamp
    (fd, tmpfilename) = mkstemp(prefix='youtubedl-test-utime-')
    try:
        os.utime(tmpfilename, (0, 0))

        pp = PostProcessor(downloader=FakeDownloader())
        pp._downloader.to_screen = lambda s: s
        pp.try_utime(tmpfilename, 10, 20)

        # Check that the file has been updated
        (atime, mtime) = os.stat(tmpfilename)[7:9]
        assert atime == 10, 'atime updated while it should not'
        assert mtime == 20, 'mtime not updated'
    finally:
        # Remove the file
        os.close

# Generated at 2022-06-14 18:04:15.940611
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from .ffmpeg import FFmpegPostProcessor
    import tempfile

    fd = tempfile.NamedTemporaryFile()
    downloader = FileDownloader({'proxy': '127.0.0.1:8118', 'outtmpl': fd.name})
    pp = FFmpegPostProcessor(downloader)
    pp.try_utime(fd.name, 0, 0)

# Generated at 2022-06-14 18:04:23.699432
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil

    d = tempfile.mkdtemp()
    path = os.path.join(d, 'test')
    open(path, 'w').close()
    mtime = time.time() - 100
    # Default PostProcessor inits self._downloader as None, so the test will fail
    temp = PostProcessor(downloader="test")
    temp.try_utime(path, mtime, mtime)
    stat = os.stat(path)
    assert int(stat.st_mtime) == int(mtime)
    shutil.rmtree(d)

# Generated at 2022-06-14 18:04:30.982887
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    # Successful case of use of the method
    try:
        import tempfile
        tmppath = tempfile.mktemp()
        with open(tmppath, 'wb') as tmpf:
            tmpf.write('qwerty')
        pp.try_utime(tmppath, 0, 0)
    finally:
        os.remove(tmppath)
    # Initial failure of use of the method

# Generated at 2022-06-14 18:04:41.169529
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import MockYDL
    from ..utils import FakeFile

    ydl = MockYDL()
    pp = PostProcessor(ydl)
    # Test for successful execution
    ydl.params['logger'] = ydl.logger
    ydl.params['nooverwrites'] = False
    ff = FakeFile(b'content')
    ff.utime = lambda atime, mtime: None
    ff.name = '/some/path'
    pp.run({'filepath': ff})
    assert ydl.asset_called

    ydl.asset_called = False
    # Test for an exception
    def ex_utime(atime, mtime):
        raise Exception
    ff.utime = ex_utime
    pp.run({'filepath': ff})

    assert ydl.asset

# Generated at 2022-06-14 18:04:42.239623
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass



# Generated at 2022-06-14 18:04:52.332618
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import datetime
    from ..compat import PY2

    # Create a temp file
    import tempfile
    tmp = tempfile.NamedTemporaryFile()
    tmpname = tmp.name
    tmp.close()

    # Save stat of file
    statinfo = os.stat(tmpname)

    # Change the timestamp
    date = datetime.datetime(2001, 1, 1, 1, 1, 1).timetuple()
    newtimes = (time.mktime(date),) * 2
    oldtimes = (statinfo.st_atime, statinfo.st_mtime)

# Generated at 2022-06-14 18:05:03.326732
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import sys

    import subprocess

    if sys.version_info < (3, 0):
        from subprocess import CalledProcessError
    else:
        from subprocess import SubprocessError as CalledProcessError

    if hasattr(sys, 'frozen'):
        # py2exe (and similar)
        # TODO: This path should be made cross-platform
        ffmpeg_location = os.path.join(sys.executable.rsplit(os.path.sep, 1)[0], 'ffmpeg.exe')
    else:
        # normal python
        ffmpeg_location = 'ffmpeg'

    class DummyPostProcessor(PostProcessor):

        def __init__(self, ffmpeg_location):
            PostProcessor.__init__(self)
            self.ffmpeg_location = ffmpeg_

# Generated at 2022-06-14 18:05:10.421247
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import FileDownloader
    from ..utils import prepend_extension
    ydl = FileDownloader({})
    pp = PostProcessor(ydl)
    import sys
    import tempfile
    import time
    import shutil

# Generated at 2022-06-14 18:05:38.072693
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    PostProcessor.try_utime(None, '/path/to/file',-1,-1)

# Generated at 2022-06-14 18:05:43.553244
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        from types import ClassType as python_class
    except ImportError: #python 3
        from types import ClassType
        python_class = type

    assert isinstance(PostProcessor, python_class)


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:05:49.401789
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    from ..downloader import FileDownloader

    fd, fname = tempfile.mkstemp(prefix='youtube-dl-test_', suffix='.tmp')
    time.sleep(.1)
    os.close(fd)
    fd = open(fname, 'w')
    fd.close()
    atime = time.time()
    pp = PostProcessor(FileDownloader())
    try:
        pp.try_utime(fname, atime, atime)
        pass
    finally:
        os.remove(fname)

# Generated at 2022-06-14 18:05:57.603598
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import FakeYDL
    from tempfile import mkdtemp
    import os
    import shutil
    import time

    def test_try_utime(self):
        try:
            file_path = os.path.join(self.temp_dir, 'fake_file')
            open(file_path, 'w').close()
            current_time = os.path.getatime(file_path)
            self.postprocessor.try_utime(file_path, current_time, current_time)
        finally:
            shutil.rmtree(self.temp_dir)


# Generated at 2022-06-14 18:06:05.582240
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    ydl_opts = {
        "logger": YoutubeDL().logger,
        "outtmpl": "out%(ext)s"
    }

    class TestedPostProcessor(PostProcessor):
        # function to be tested
        def __init__(self, ydl_opts):
            PostProcessor.__init__(self, downloader=YoutubeDL(ydl_opts))

        def run(self, info):
            path = os.path.join(encodeFilename(self._downloader.params['outtmpl'] % info), 'some_file.tmp')
            # create the file to start with
            with open(path, 'w') as f:
                f.write('a' * 100)

# Generated at 2022-06-14 18:06:13.736937
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..extractor import gen_extractors

    downloader = FileDownloader({})
    downloader.add_info_extractor(gen_extractors()[0])
    downloader.add_post_processor(PostProcessor())

    assert not os.path.exists('test')
    assert not os.path.exists('test-atime')
    assert not os.path.exists('test-mtime')

    open('test', 'w').close()
    atime = int(os.path.getatime('test'))
    mtime = int(os.path.getmtime('test'))

    downloader.post_processors[0].try_utime('test', atime, mtime)

# Generated at 2022-06-14 18:06:24.966209
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    postProcessor = PostProcessor()

    # Create a stub object of class Downloader
    class Downloader:
        def __init__(self):
            self.report_warning_count = 0

        def report_warning(self, *args):
            self.report_warning_count += 1

    downloader = Downloader()
    postProcessor.set_downloader(downloader)

    # Test negative case
    file_name = 'file'
    try:
        os.remove(file_name)
    except OSError:
        pass
    open(file_name, 'a').close()
    now = datetime.datetime.now()
    postProcessor.try_utime(file_name, now.timestamp(), now.timestamp())
    assert downloader.report_warning_count == 1

# Generated at 2022-06-14 18:06:33.558808
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    from datetime import datetime, timedelta
    import tempfile
    import shutil
    import os

    def init_file(dir):
        path = os.path.join(dir, 'test.tmp')
        with open(path, 'w') as fd:
            fd.write('test\n')
        return path

    dir = tempfile.mkdtemp()
    path = init_file(dir)
    atime = time.time() - 100
    atime_dt = datetime.now() - timedelta(hours=3)
    pp = PostProcessor(downloader=None)
    pp.try_utime(path, atime, atime, errnote='')
    atime_new = os.stat(path).st_atime

# Generated at 2022-06-14 18:06:35.506332
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime(__file__, None, None)

# Generated at 2022-06-14 18:06:45.884672
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import shutil

    class FakeYDL(object):
        def __init__(self):
            self.params = {}

        def report_warning(self, *args):
            pass

    ydl = FakeYDL()

    with tempfile.NamedTemporaryFile(suffix='test.dat') as f:
        postproc = PostProcessor(ydl)
        postproc.try_utime(f.name, 1, 2)

        atime, mtime = os.stat(f.name).st_atime, os.stat(f.name).st_mtime
        assert atime == 1
        assert mtime == 2

    # test with directory

# Generated at 2022-06-14 18:07:46.025506
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import os
    import stat
    import time
    import shutil
    import tempfile
    import unittest

    from .common import compat_getenv

    from ..utils import (
        encodeFilename,
    )

    from ..compat import (
        compat_os_path,
        compat_rename,
        compat_urllib_error,
    )

    from .test_utils import FakeDownloader

    downloader = FakeDownloader()

    # We must create a new temp directory here that is used for all tests.
    # If we don't then this test won't work on Windows Vista and above.
    # See issue #2219 for more information.
    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-14 18:07:55.436455
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    import tempfile
    import time
    import sys
    import os
    import stat

    def _real_time_equal(a, b):
        return abs(a - b) < 0.5

    def tmp_file(name, contents, atime, mtime):
        file_path = os.path.join(tmp, name)
        with open(file_path, 'w') as file:
            file.write(contents)
        os.utime(file_path, (atime, mtime))
        return file_path

    tmp = tempfile.mkdtemp()
    original_atime, original_mtime = time.time(), int(time.time()) - 10

# Generated at 2022-06-14 18:08:05.480396
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..downloader import FileDownloader
    from ..extractor import YoutubeIE
    from ..utils import DateRange
    import datetime

    downloader = YoutubeDL(params={'outtmpl': '%(id)s_%(extractor_key)s.%(ext)s'})
    downloader.add_info_extractor(YoutubeIE())

    # Test post processor without initialized downloader
    pp = PostProcessor({})
    try:
        pp.try_utime("", 0, 0)
    except Exception:
        pass
    else:
        assert False
    pp1 = PostProcessor(downloader)
    pp1.try_utime("", 0, 0)

    # Test post processor with initialized downloader
    temp_filename = '__temp_file__'


# Generated at 2022-06-14 18:08:13.584969
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import YtdlDownloader
    from .YoutubeDL import YoutubeDL
    from .extractor import YoutubeIE
    from .postprocessor import FFmpegMetadataPP

    class FakeYoutubeDL(YoutubeDL):
        params = {}

        def to_screen(self, *args, **kargs):
            pass

        def to_stderr(self, *args, **kargs):
            pass

        def report_warning(self, *args, **kargs):
            pass

        def report_error(self, *args, **kargs):
            pass

    class FakeYtdlDownloader(YtdlDownloader):

        @property
        def params(self):
            return self._ydl.params

        def report_warning(self, message):
            print('WARNING: ' + message)


# Generated at 2022-06-14 18:08:22.184165
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import VideoExtractor
    from ..downloader import FileDownloader
    from ..utils import DateRange


# Generated at 2022-06-14 18:08:31.161204
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    class _FakeDownloader(object):
        def report_warning(self, errnote):
            print(errnote)

    class _FakePostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            self._downloader = downloader or _FakeDownloader()

    p = _FakePostProcessor()
    path = 'Fake_utime_path'
    atime = mtime = 0
    p.try_utime(path, atime, mtime)


if __name__ == '__main__':
    test_PostProcessor_try_utime()