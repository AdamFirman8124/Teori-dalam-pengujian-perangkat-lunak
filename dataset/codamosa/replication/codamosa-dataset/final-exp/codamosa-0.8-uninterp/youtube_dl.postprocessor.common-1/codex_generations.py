

# Generated at 2022-06-14 17:58:40.844257
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import time
    import tempfile
    import shutil
    import stat
    import os

    class _DummyPlaylistPP(PostProcessor):
        def run(self, information):
            imported = information['filepath']
            target = imported + '.target'
            shutil.move(imported, target)
            self.try_utime(target, atime=0, mtime=0)
            st = os.stat(target)

# Generated at 2022-06-14 17:58:46.515962
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    try:
        pp.try_utime('nonexistingfile', 0, 0, errnote='Cannot test')
    except PostProcessingError:
        pass
    else:
        raise AssertionError('PostProcessingError not raised')

    # Test for exception-less case
    pp.try_utime('/dev/null', 0, 0)

# Generated at 2022-06-14 17:58:57.566745
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Make fake class that has method report_warning
    class FakeDownloader:
        def report_warning(self, msg):
            self.msg = msg

    # Make fake class that has a _downloader member and that inherits class PostProcessor
    class FakeProcessor(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)

    # Create fake instance of downloader
    downloader = FakeDownloader()

    # Create fake instance of postprocessor
    postprocessor = FakeProcessor(downloader)

    # Call method try_utime of postprocessor
    postprocessor.try_utime('/some/file', 12, 22, errnote='Cannot update utime of file')

    # Check if the fake downloader got a warning message

# Generated at 2022-06-14 17:59:06.608756
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader(object):
        def report_warning(self, msg):
            self.msg = msg

    class FakePostProcessor(PostProcessor):
        pass

    fake_downloader = FakeDownloader()
    fake_post_processor = FakePostProcessor(fake_downloader)

    # Create a fake file
    fake_filename = 'FakeFileForUnitTest'
    fake_file = open(fake_filename, 'w')
    fake_file.close()

    # Try to update mtime of an unexisting file
    os.remove(fake_filename)
    fake_post_processor.try_utime(fake_filename, 1000, 2000)
    assert fake_downloader.msg == 'Cannot update utime of file'

# Generated at 2022-06-14 17:59:14.117430
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time
    import sys
    from ..compat import unittest

    class DummyDownloader(object):
        def __init__(self):
            self.params = {}
            self.dummy_file = None

        def report_warning(self, msg):
            pass

    class DummyPostProcessor(PostProcessor):
        def run(self, information):
            self._downloader.dummy_file = tempfile.NamedTemporaryFile(delete=False)
            self._downloader.dummy_file.close()
            return [], information

    class TestPostProcessor(unittest.TestCase):
        def setUp(self):
            self.pp = DummyPostProcessor()
            self.dd = DummyDownloader()
            self.pp.set_download

# Generated at 2022-06-14 17:59:24.508703
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    # The following two lines is just to simulate the real utime function
    def utime_mock(filename, times):
        utime_mock.filename = filename
        utime_mock.times = times
    setattr(os, 'utime', utime_mock)
    
    # The following two lines is just to simulate the real report_warning
    # function to avoid the printing of warning messages in the real console
    def report_warning_mock(message):
        report_warning_mock.message = message
    setattr(pp._downloader, 'report_warning', report_warning_mock)

    # Test for the normal case
    pp.try_utime('filename', 1549658931, 1549658931)

# Generated at 2022-06-14 17:59:33.608409
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    post_process = PostProcessor()
    # Create test file named 'test'
    with open('test', 'w') as testFile:
        testFile.write("test")
    # Get current timestamp and set the new mtime to 1 day before current time
    import time
    t = time.time()
    newMtime = int(t-86400)
    post_process.try_utime('test', newMtime, newMtime)
    # Check if the change is success
    st = os.stat('test')
    assert st.st_mtime == newMtime
    # Clean up test file
    os.remove('test')

# Generated at 2022-06-14 17:59:45.300372
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time
    import unittest

    from ..compat import file_open

    class PostProcessorTester(PostProcessor):
        def run(self, information):
            path = os.path.join(tempdir, 'foo')
            file_open(path, 'wb').write(b'hello world')
            self.try_utime(path, 0, 0, errnote='Cannot update utime of file')
            self.try_utime(path, time.time()+3600, time.time()+3600, errnote='Cannot update utime of file')
            return [path], information

    class TestPostProcessorModule(unittest.TestCase):
        def test_PostProcessor_try_utime(self):
            pp = PostProcessorTester()


# Generated at 2022-06-14 17:59:52.715434
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .test_utils import FakeYDL
    import sys
    import time
    import tempfile
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 17:59:57.841819
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    def _dummy_report_warning(self,msg):
        pass

    ydl = YoutubeDL()
    ydl.report_warning = _dummy_report_warning

    # test for success
    filepath = "test_file"
    open(filepath, 'a').close()
    pp = PostProcessor(ydl)
    pp.try_utime(filepath, mtime=12345, atime=67890)
    os.unlink(filepath)

    # test for failure
    pp.try_utime("asdfasdf", mtime=12345, atime=67890)

# Generated at 2022-06-14 18:00:09.302407
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import sys

    from .compat import (
        compat_path_exists,
        compat_setenv,
        compat_time_sleep,
    )

    from ..downloader.common import PostProcessingError

    tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:00:20.585890
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    from . import FakeYDL
    from .extractor.common import InfoExtractor
    from .utils import mark_downloaded_files

    paths = [
        os.path.abspath(__file__),
        os.path.abspath(sys.executable),
    ]
    downloader = FakeYDL()
    

# Generated at 2022-06-14 18:00:29.696593
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import __builtin__
    fake_os = None
    fake_os_module = None
    fake_encodeFilename = None
    fake_utime = None
    fake_report_warning = None
    OSError_caught = False

    def fake_import(name, *args):
        if name == 'os':
            return fake_os_module

    def fake_encodeFilename(filename):
        return 'encode' + filename

    def fake_utime(filename, times):
        if filename == 'encode/root/to/file':
            fake_utime.called += 1
        else:
            raise Exception('Unexpected filename for utime')

    def fake_report_warning(message):
        if message != 'Cannot update utime of file':
            raise Exception('Unexpected warning message')


# Generated at 2022-06-14 18:00:37.795983
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from nose.tools import assert_raises, assert_equal
    from ..utils import DownloadContext, FileDownloader
    from .common import FakeYDL

    class MyPostProcessor(PostProcessor):
        def __init__(self, downloader):
            super(MyPostProcessor, self).__init__(downloader)
            self.counter = 0

        def run(self, information):
            self.counter += 1
            self.try_utime(information['filepath'], 0, 0, 'some error message')
            return ([], information)

    d = FileDownloader(FakeYDL({'outtmpl': '%(id)s'}))
    d.add_info_extractor(None)
    d.add_post_processor(MyPostProcessor, True, 1)

    # Test for utime with non-

# Generated at 2022-06-14 18:00:48.006088
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    test_file = os.path.join(os.path.dirname(__file__), 'test.mp3')
    atime = os.stat(test_file).st_atime
    mtime = os.stat(test_file).st_mtime

    pp = PostProcessor(None)

    pp.try_utime(test_file, atime, mtime)
    pp.try_utime(test_file, None, mtime)
    pp.try_utime(test_file, atime, None)

    if os.name == 'nt' or os.name == 'mac':
        # Some OSes do not support utime on directories
        test_file = os.path.dirname(__file__)
        atime = os.stat(test_file).st_atime

# Generated at 2022-06-14 18:00:58.423712
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # create a class (DummyDownloader) that behaves like a downloader, with a report_warning method
    class DummyDownloader:
        def __init__(self):
            self.warning_text = None

        def report_warning(self, text):
            self.warning_text = text

    # create an instance of PostProcessor and set its _downloader attribute to our dummy downloader
    pp = PostProcessor(DummyDownloader())
    pp.set_downloader(DummyDownloader())
    # create a file to process
    with open('test_file', 'w') as f:
        f.write('a')
    # set the access and modification times of the file to a known value
    os.utime('test_file', (1400000000.0, 1400000000.0))
    # change the access and modification times of the

# Generated at 2022-06-14 18:01:04.719110
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(TestPostProcessor, self).__init__(downloader)
            self.path = None
            self.atime = None
            self.mtime = None
            self.errnote = None


# Generated at 2022-06-14 18:01:09.535891
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import FakeYDL
    from .tests.test_utils import FakeFile

    fl = FakeFile()
    ydl = FakeYDL()
    pp = PostProcessor(ydl)
    pp.try_utime(fl, 0, 0)
    assert fl.content == b'utime'
    pp.try_utime(fl, 0, 0, errnote='err')
    assert fl.content == b'utimeerr'


# Generated at 2022-06-14 18:01:20.848076
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import stat
    import time
    import tempfile

    from ..utils import encodeFilename
    tmppath = None

# Generated at 2022-06-14 18:01:32.738365
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class Downloader():
        def __init__(self):
            self._warned = False

        def report_warning(self, msg):
            self._warned = True

    downloader = Downloader()
    pp = PostProcessor(downloader)
    path = '/path/to/file.mp4'
    atime = 10
    mtime = 20

    # utime success
    os.path.exists = lambda x: True
    os.utime = lambda x, y: True
    pp.try_utime(path, atime, mtime)

    # utime failed
    os.path.exists = lambda x: True
    os.utime = lambda x, y: False
    pp.try_utime(path, atime, mtime)
    assert downloader._warned

    # file not exist


# Generated at 2022-06-14 18:01:44.771892
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile

    class FakeDownloader(object):
        def report_warning(self, msg):
            pass

    temp_file_fd, temp_file_path = tempfile.mkstemp(suffix='.part')
    atime, mtime = time.time(), time.time()
    pp = PostProcessor(FakeDownloader())
    pp.try_utime(temp_file_path, atime, mtime)
    assert os.stat(temp_file_path).st_atime == atime
    assert os.stat(temp_file_path).st_mtime == mtime
    os.close(temp_file_fd)
    os.remove(temp_file_path)

# Generated at 2022-06-14 18:01:56.960919
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .get_testcases import get_testcases
    from .download_playlist import test_playlist

    for t in get_testcases():
        filepath = os.path.join(t['temp'] + "_try_utime", 'video')
        ydl = YoutubeDL(t['params'])
        ydl.params['outtmpl'] = filepath
        ydl.add_default_info_extractors()
        if 'playlist' in t:
            test_playlist(t, ydl)
        else:
            ydl.download([t['url']])
        pp = PostProcessor(ydl)
        # Set utime
        path = pp.run([{'filepath': filepath}])[1][0]['filepath']

# Generated at 2022-06-14 18:02:03.891901
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import FakeYDL
    from .common import fake_sys_argv
    from ..utils import prepend_extension
    from tempfile import mkdtemp
    from shutil import rmtree
    import os.path
    import time

    tmpdir = mkdtemp()


# Generated at 2022-06-14 18:02:11.293393
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL

    def test_utime_dummy(path, atime, mtime, errnote):
        assert path == 'path'
        assert atime == 10
        assert mtime == 8
        assert errnote == 'Cannot update utime of file'

    ydl = YoutubeDL()
    pp = PostProcessor(ydl)
    pp.try_utime = test_utime_dummy
    pp.try_utime('path', 10, 8)

# Generated at 2022-06-14 18:02:17.168912
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    (file_handle, file_path) = tempfile.mkstemp()
    os.close(file_handle)
    try:
        pp = PostProcessor()
        pp.try_utime(file_path, 0, 0)
        os.remove(file_path)
        pp.try_utime(file_path, 1, 1)
    except:
        os.remove(file_path)
        raise
    os.remove(file_path)

# Generated at 2022-06-14 18:02:22.385211
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    _, file_path = tempfile.mkstemp()
    atime = time.time()
    mtime = atime + 30
    downloader = type('DummyDownloader', (object,), {'params': {}})()
    postprocessor = PostProcessor(downloader)
    postprocessor.try_utime(file_path, atime, mtime)

# Generated at 2022-06-14 18:02:32.927965
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Test that method try_utime raises no exception when called with a path to a file whose name
    # contains a non-ASCII character.
    from io import BytesIO
    from pytube import YouTube
    yt = YouTube('https://www.youtube.com/watch?v=BaW_jenozKc', on_progress_callback=lambda x: x)
    obj = yt.streams.first().download(output_path='tests', filename='non_ascii_char_℃_₊.mp4')

    # Downloader does not have a valid params attribute, so it has to be set for method run to be
    # successful.
    class FakeDownloader:
        params = {}
    fake_downloader = FakeDownloader()

    # The file non_ascii_char_℃_₊

# Generated at 2022-06-14 18:02:43.914957
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    # create empty test file
    fn = 'ytdl_test_file'
    if os.path.exists(fn):
        os.remove(fn)
    fh = open(fn, 'w')
    fh.close()
    # get current file time
    st = os.stat(fn)
    # update file time to past
    pp.try_utime(fn, st.st_atime - 1, st.st_mtime - 1)
    # check if time was updated
    st2 = os.stat(fn)
    if st2.st_atime <= st.st_atime or st2.st_mtime <= st.st_mtime:
        raise PostProcessingError('utime not updated')
    # remove test file
    os.remove(fn)

# Generated at 2022-06-14 18:02:54.521063
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import pytest
    import time
    import tempfile

    class TestPP(PostProcessor):
        def try_utime(self, path, atime, mtime, errnote):
            return (path, atime, mtime, errnote)

    with tempfile.NamedTemporaryFile() as tf:
        filename = tf.name
    test = TestPP()
    filepath = encodeFilename(filename)
    atime = time.time()
    mtime = time.time()
    errnote = 'Cannot update utime of file'

    assert test.try_utime(filepath, atime, mtime, errnote) == (filepath, atime, mtime, errnote)

    # Raise a exception when filename is not file

# Generated at 2022-06-14 18:02:55.237350
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # TODO: Missing test
    pass

# Generated at 2022-06-14 18:03:10.837795
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from tempfile import mkstemp
    from time import time
    from os import utime, stat
    from shutil import rmtree
    from sys import version_info
    downloader = Downloader()
    postprocessor = PostProcessor(downloader)
    filepath = mkstemp()[1]
    mtime = stat(filepath).st_mtime
    downloader.params['pretend'] = True
    downloader.params['dump_intermediate_pages'] = True
    downloader.report_warning = lambda *args: None
    # Ensure that pretending not to do anything fixes mtime value
    postprocessor.try_utime(filepath, mtime, mtime + 3600)
    assert stat(filepath).st_mtime == mtime

# Generated at 2022-06-14 18:03:19.572954
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil
    from ..utils import temp_name

    pp = PostProcessor(None)
    file_name = temp_name('.tmp')

    try:
        with open(file_name, 'wb') as f:
            f.write(b'Test')

        atime = time.time() - 3600
        mtime = time.time() - 4200

        pp.try_utime(file_name, atime, mtime)
    finally:
        os.remove(file_name)

    assert os.path.isfile(file_name) is False

# Generated at 2022-06-14 18:03:28.113917
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader:
        def report_warning(self, msg):
            self.msg = msg
    def test_factory(postprocessor_cls, **args):
        test_downloader = MockDownloader()
        test_postprocessor = postprocessor_cls(test_downloader, **args)
        return test_downloader, test_postprocessor
    def test_UTimePossible(postprocessor_cls, **args):
        test_downloader, test_postprocessor = test_factory(postprocessor_cls, **args)
        from time import time
        current_time = time()
        test_postprocessor.try_utime('test', current_time, current_time)
    def test_UTimeNotPossible(postprocessor_cls, **args):
        test_downloader, test_postprocessor = test

# Generated at 2022-06-14 18:03:38.224484
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import sys

    # Set values for tests for windows
    user = 'user'
    group = 'group'
    # Create the test file
    filename = 'test_postprocessor_try_utime.tmp'
    with open(filename, 'w'):
        pass

    # Get the old stats of the file
    old_stat = os.stat(filename)

    # Create a PostProcessor object
    pp = PostProcessor(None)

    # Set the mtime to an old date
    pp.try_utime(filename, 0, 0)

    # Get the new stats of the file
    new_stat = os.stat(filename)

    # Remove the test file
    os.remove(filename)


# Generated at 2022-06-14 18:03:47.946808
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil, tempfile
    import time
    import os

    # Get valid values for os.utime
    tempdir = tempfile.mkdtemp()
    tempfilepath = os.path.join(tempdir, 'tempfile')
    testfile = open(tempfilepath, 'w')
    testfile.close()
    current_time = time.time()
    # On windows, atime and mtime must be multiplied by 1e7
    if os.name == 'nt':
        atime = mtime = int(current_time * 1e7)
    else:
        atime = mtime = int(current_time)
    test_atime = atime + 60
    test_mtime = mtime + 120

    # Initialize the PostProcessor

# Generated at 2022-06-14 18:03:58.572760
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # create a fake test downloader
    class FakeTestDownloader:
        def report_warning(self, warning):
            pass
    FakeTestDl = FakeTestDownloader()

    # create a fake test file for postprocessing
    class FakeTestFile:
        def __init__(self):
            self.path = 'fake_test_file.opus'
    FakeTestFile = FakeTestFile()

    # create a fake test postprocessor
    class FakeTestPp:
        def __init__(self, downloader):
            self.downloader = downloader
    FakeTestPp = FakeTestPp(FakeTestDl)

    # invoke method try_utime of class PostProcessor
    FakeTestPp.try_utime(FakeTestFile.path, 0, 0)

# Generated at 2022-06-14 18:04:10.350197
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import DateRange
    from ..YoutubeDL import YoutubeDL
    from .common import PostProcessorTest

    class TestPP(PostProcessor):
        def run(self, information):
            filepath = information['filepath']
            self.try_utime(filepath, 1, 2, errnote='Cannot update utime of file')
            return [filepath], information

    def _test_utime(self, expected=(1, 2), mtime_cb=None):
        if mtime_cb is None:
            mtime_cb = lambda *a: expected[1]
        def do_test(result):
            self.assertEqual(result['filepath'], filepath)
            self.assertEqual(os.stat(result['filepath']).st_mtime, expected[1])

# Generated at 2022-06-14 18:04:21.263075
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from pytest import raises
    from ..compat import cmp
    from ..utils import DateRange

    class TestPP(PostProcessor):
        """Shortcut for testing PostProcessor.try_utime"""

        def __init__(self, downloader=None):
            pass

    pp = TestPP()

    with raises(PostProcessingError):
        pp.try_utime('/', 0, 0, errnote='test')

    # can't test real utime because it will update it
    # but we can check if it uses cmp()

# Generated at 2022-06-14 18:04:31.745289
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import tempfile
    import os

    # Create a temporary file and change its atime and mtime
    # to known values
    tmpfile = tempfile.NamedTemporaryFile(delete=False)
    tmpname = tmpfile.name
    tmpfile.close()
    assert os.path.isfile(tmpname)
    assert os.path.exists(tmpname)
    now = datetime.datetime.now()
    atime = now - datetime.timedelta(days=1)
    mtime = now - datetime.timedelta(days=2)
    os.utime(tmpname, (atime.timetuple(), mtime.timetuple()))

    class MockDownloader(object):
        def __init__(self):
            self.msgs = []


# Generated at 2022-06-14 18:04:44.323678
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile
    # the code is only for the purpose of unit test
    # pylint: disable=W0106
    downloader = 'test_downloader'
    pp = PostProcessor(downloader)
    with NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Sample text')
    path = temp_file.name

# Generated at 2022-06-14 18:05:07.052794
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyDownloader:
        def report_warning(self, msg):
            self.warning = msg

    pp = PostProcessor(DummyDownloader())

    path = 'test_file'
    open(path, 'w').close()

    errnote = 'Cannot update utime of file'

    pp.try_utime(path, 1, 1, errnote)

    os.remove(path)

    pp.try_utime(path, 1, 1, errnote)
    assert pp._downloader.warning == errnote

    os.remove(path)

    pp.try_utime(path, 2, 2)
    assert pp._downloader.warning == errnote

# Generated at 2022-06-14 18:05:18.402256
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyPostProcessor(PostProcessor):
        def run(self, info):
            self.try_utime(info['filepath'], 0, 0)
            return [info['filepath']], info

    class MockDownloader(object):
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    d = MockDownloader()
    pp = DummyPostProcessor(downloader=d)

    # utime() can really raise an exception
    assert not hasattr(os, 'utime_works')
    assert not hasattr(os, 'utime_raises_OSError')

# Generated at 2022-06-14 18:05:29.135492
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL

    class PostProcessorMock(PostProcessor):
        def __init__(self, downloader):
            self.downloader = downloader

    class DownloaderMock:
        def __init__(self):
            self.params = {}

        def report_warning(self, msg):
            self.reported_warnings = self.reported_warnings + [msg] if hasattr(self, 'reported_warnings') else [msg]

    def mock_utime(fn, t):
        self.utime_called = True
        if fn == 'raise exception':
            raise Exception

    pp = PostProcessorMock(DownloaderMock())
    pp.utime = mock_utime
    pp.try_utime('raise exception', 0, 0, errnote='Cannot update utime')

# Generated at 2022-06-14 18:05:41.314821
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import pytest
    try:
        os.utime(__file__, None)
    except Exception:
        pytest.skip('Current os.utime does not accept None as time values')

    import tempfile
    from ..compat import PY2
    from ..extractor.common import InfoExtractor

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b'foobar' if PY2 else 'foobar')
        f.seek(0)


# Generated at 2022-06-14 18:05:43.165753
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert PostProcessor().try_utime(None, 0, 0)

# Generated at 2022-06-14 18:05:50.492013
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile
    from datetime import datetime, timedelta
    from ..utils import date_from_str
    import time
    import os

    class DummyDownloader():
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    with NamedTemporaryFile(suffix='.tmp') as tmpfile:
        filepath = tmpfile.name
        assert os.path.exists(filepath)
        # to be sure that tmpfile is not already added in filesystem
        # time.sleep(2)
        # to be sure that system time is not already added
        # time.sleep(1)
        postprocessor = PostProcessor(DummyDownloader())

# Generated at 2022-06-14 18:05:58.094207
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import sys
    import time
    import datetime
    import os

    if sys.version_info[0] >= 3:
        from io import StringIO
    else:
        from StringIO import StringIO

    def get_temp_file_name(suffix=''):
        handle, name = tempfile.mkstemp(suffix=suffix)
        os.close(handle)
        return name

    if not hasattr(sys, "gettotalrefcount"):
        print('Skipping for Python version < 2.7')
        return
    temp_dir = tempfile.mkdtemp()
    errnote = 'Cannot update utime of file'
    postprocessor = PostProcessor(None)
    temp_file = get_temp_file_name('.mp3')

# Generated at 2022-06-14 18:06:05.822474
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class Downloader():
        def __init__(self):
            self.warned = False

        def report_warning(self, note):
            self.warned = True

    class PP(PostProcessor):
        def __init__(self, downloader=None):
            if downloader is None:
                self.downloader = Downloader()
            else:
                self.downloader = downloader

    pp = PP()
    path = 'no-a-file'
    try:
        pp.try_utime(path, 1, 1)
    except Exception as e:
        assert str(e) == 'Cannot update utime of file'
    else:
        assert False, 'Exception should be raised'
    assert pp.downloader.warned
    pp.try_utime(path, 1, 1, 'error')


# Generated at 2022-06-14 18:06:10.606002
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        os.utime('/root', (0, 0))
    except:
        pass
    else:
        assert False, "try_utime must raise exception on inaccessible path"
    try:
        os.utime(encodeFilename('/root'), (0, 0))
    except:
        pass
    else:
        assert False, "try_utime must raise exception on inaccessible path"

# Generated at 2022-06-14 18:06:17.662202
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    with tempfile.NamedTemporaryFile() as test_file:
        pp = PostProcessor(None)
        if hasattr(os, 'utime'):
            assert pp.try_utime(test_file.name, 0, 0) is None
        else:
            assert pp.try_utime(test_file.name, 0, 0) is not None



# Generated at 2022-06-14 18:06:54.895994
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import time
    import sys

    class FakeDownloader():
        def __init__(self):
            self.reports = []

        def to_screen(self, msg):
            pass

        def report_warning(self, msg):
            self.reports.append(msg)

    if sys.version_info < (3, 0):
        from types import FileType
        assert isinstance(tempfile.TemporaryFile(), FileType)


# Generated at 2022-06-14 18:07:04.688756
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import compat_mock
    from ..extractor import common

    mock_logger_warning = compat_mock.MagicMock()

    pp = PostProcessor(common.FileDownloader({
        'outtmpl': '%(id)s'
    }))
    pp.set_downloader(common.FileDownloader({
        'outtmpl': '%(id)s'
    }, {
        'logger': compat_mock.MagicMock(warning=mock_logger_warning)
    }))

    pp.try_utime('video.mp4', 1, 2)

    assert mock_logger_warning.call_count == 0

    pp.try_utime('video.mp4', None, None)

    assert mock_logger_warning.call_count == 1

# Generated at 2022-06-14 18:07:11.723531
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import shutil
    import sys

    pp = PostProcessor()
    pp._downloader = type('FakeDl', (object,), {'to_screen': lambda self, msg, skip_eol=False, check_quiet=False: sys.stderr.write(msg)})()

    fd, file_path = tempfile.mkstemp(text=True)
    os.write(fd, b'a' * 10 * 1024 * 1024)  # Write 10 MiB
    os.close(fd)

    try:
        t = time.time() - 100
        pp.try_utime(file_path, t, t)
    finally:
        os.remove(file_path)

    # If a non existing file is given, we should catch the exception and return None

# Generated at 2022-06-14 18:07:19.926583
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    from os.path import getmtime
    from pytube.PostProcessor import PostProcessor
    import shutil
    test_dir = tempfile.mkdtemp()
    try:
        pp = PostProcessor(None)

        f = open(test_dir + '/1', 'w')
        f.write('Hi')
        f.close()
        t = getmtime(test_dir + '/1')
        time.sleep(2)
        pp.try_utime(test_dir + '/1', t, t)
        assert getmtime(test_dir + '/1') == t

        pp.try_utime(test_dir + '/null', t, t)
    finally:
        shutil.rmtree(test_dir)

# Generated at 2022-06-14 18:07:28.379500
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime('abc', 1, 2, 'errnote')
    pp.try_utime(b'abc', 1, 2, 'errnote')
    pp.try_utime('\udce2\udce3', 1, 2, 'errnote')
    pp.try_utime(b'\xee\xee', 1, 2, 'errnote')
    pp.try_utime(None, 1, 2, 'errnote')
    pp.try_utime(b'', 1, 2, 'errnote')

# Generated at 2022-06-14 18:07:35.415535
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    from ..compat import PY2

    def get_utime(path):
        # In Python 3.3, os.utime(path, None) gives a OSError
        # In Python 2.7, os.utime(path, None) gives a TypeError
        try:
            if PY2:
                return os.stat(path).st_atime, os.stat(path).st_mtime
            else:
                return os.utime(path, None)
        except Exception:
            return 0, 0

    # create a temp file
    (temp_handle, temp_file_name) = tempfile.mkstemp()

# Generated at 2022-06-14 18:07:36.018760
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:07:46.246746
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import YoutubeDL
    from ..utils import DateRange

    class DummyPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(DummyPostProcessor, self).__init__(downloader)

    class DummyDownloader(YoutubeDL):
        def __init__(self):
            self.params = {'writedescription':True, 'writethumbnail':True, 'writeannotations':True}
            self.warn_count = 0

        def report_warning(self, msg):
            if self.warn_count == 0:
                assert 'Cannot update utime of file' == msg
            elif self.warn_count == 1:
                assert 'Cannot update utime of file' == msg

# Generated at 2022-06-14 18:07:49.766877
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    pp = PostProcessor(Downloader(params={}))

    pp.try_utime('filename', 1, 2, 'errnote')



# Generated at 2022-06-14 18:07:59.736261
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import time
    import shutil
    from ..utils import DateRange
    from ..compat import is_win32

    # Create temporary directory to perform the test in
    tempDir = tempfile.mkdtemp(prefix="test_PostProcessor_try_utime_")
    origTime = time.time()
