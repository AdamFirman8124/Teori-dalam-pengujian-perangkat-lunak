

# Generated at 2022-06-14 17:58:41.093520
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractors
    from ..utils import FakeYDL
    from ..compat import compat_urllib_request
    downloader = FakeYDL()
    downloader.params['outtmpl'] = '%(id)s'
    downloader.add_info_extractor(gen_extractors()[0])
    downloader.params['quiet'] = True
    ie = gen_extractors()[0](downloader)
    ie.report_warning = downloader.report_warning
    compat_urllib_request.urlopen(ie._request_webpage('https://www.youtube.com/watch?v=BaW_jenozKc', ie.video_id)).close()
    # Download a file

# Generated at 2022-06-14 17:58:51.090382
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Using some dummy method to replace the report_warning of the PostProcessor
    class DummyDownloader(object):
        def report_warning(self, message):
            pass

    # Testing with a dummy file, first a regular one and then a symlink
    test_filename = 'test_filename'
    test_symlink = 'test_symlink'
    # Creating a dummy file
    f = open(test_filename, 'w')
    f.close()
    # Creating a symlink to the dummy file
    os.symlink(test_filename, test_symlink)

    # Testing regular file
    pp = PostProcessor(DummyDownloader())
    pp.try_utime(test_filename, 0, 0)
    # Testing symlink
    pp = PostProcessor(DummyDownloader())


# Generated at 2022-06-14 17:58:57.571415
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # PostProcessor.try_utime should be called with an argument
    # errnote: 'Cannot update utime of file'  FileNotFoundError
    # is raised in this case.
    import pytest
    with pytest.raises(FileNotFoundError):
        pp = PostProcessor(downloader=None)
        pp.try_utime('any_filename',0,0)


# Generated at 2022-06-14 17:59:01.686655
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    fake_downloader = type('FakeDownloader', (object,),
                           {'report_warning': lambda x: x})()
    fake_pp = type('FakePostProcessor', (PostProcessor,),
                    {'_downloader': fake_downloader})(fake_downloader)
    fake_pp.try_utime('file', 1, 2)

# Generated at 2022-06-14 17:59:08.532678
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import tempfile
    (fd, filename) = tempfile.mkstemp()
    os.close(fd)
    try:
        pp = PostProcessor(None)
        before = datetime.datetime.utcnow()
        after = before + datetime.timedelta(seconds=10)
        pp.try_utime(filename, after.timestamp(), after.timestamp())
        assert os.stat(filename).st_mtime >= after.timestamp()
    finally:
        os.remove(filename)

# Generated at 2022-06-14 17:59:10.003342
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    f = PostProcessor()
    f.try_utime(__file__, 0, 0)
    assert True

# Generated at 2022-06-14 17:59:22.109223
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import time
    import os.path

    import pytest
    from .test_utils import TemporaryDirectory

    # Test file creation
    with TemporaryDirectory() as test_dir:
        file_path = os.path.join(test_dir, 'test_file')
        open(file_path, 'w').close()

        # Get atime and mtime
        atime = os.stat(file_path).st_atime
        mtime = os.stat(file_path).st_mtime

        # Change atime and mtime
        PP = PostProcessor(downloader=None)
        PP.try_utime(file_path, atime + datetime.timedelta(days=1).total_seconds(), mtime + datetime.timedelta(days=1).total_seconds())

# Generated at 2022-06-14 17:59:30.583611
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import unittest
    from .test_utils import DEFAULT_OUTTMPL
    from tempfile import mkstemp
    from sys import getfilesystemencoding
    from shutil import copyfile
    from os.path import basename
    import time
    import os

    def reset_temp_file(filename, a_time, m_time):
        time.sleep(1)
        os.utime(filename, (a_time, m_time))

    class PostProcessorTest(unittest.TestCase):
        def test_try_utime(self):
            _, tmp_filename = mkstemp(prefix='%s' % os.getpid())
            copyfile('test/test.mp4', tmp_filename)
            downloader = object()

# Generated at 2022-06-14 17:59:33.250170
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from youtube_dl.YoutubeDL import YoutubeDL
    postprocessor = PostProcessor(downloader=YoutubeDL())
    # TODO
    assert postprocessor.try_utime('', 0, 0) == None

# Generated at 2022-06-14 17:59:44.928812
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from tempfile import mkstemp

    def dummy_report_warning(msg):
        report_warning(msg)

    report_warning = None

    def setUp():
        global report_warning
        report_warning = dummy_report_warning
        self._temp_file = open(mkstemp()[1], "w")

    def tearDown():
        self._temp_file.close()

    def test_should_report_warning_on_failure(self):
        pp = PostProcessor(YoutubeDL())
        pp.set_downloader(self)

        assert report_warning is not None

        report_warning(None)  # reset

        pp.try_utime(self._temp_file.name, 123, 456, 'test message')

        assert report_warning.call_

# Generated at 2022-06-14 17:59:47.957840
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime(__file__, None, None, None)

# Generated at 2022-06-14 17:59:51.296326
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .http import FileDownloader

    class FakePost(PostProcessor):
        def run(self, info):
            self.try_utime('filepath', 0, 0)
            return [], info

    downloader = FileDownloader({})
    pp = FakePost(downloader)
    pp.run({'filepath': 'filepath'})

# Generated at 2022-06-14 18:00:02.419630
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile

    import test as _test

    class _FakeDownloader(object):

        def report_warning(self, msg):
            self.msg = msg


    my_file = tempfile.NamedTemporaryFile(delete=False)
    my_file.close()
    my_pp = PostProcessor(_FakeDownloader())
    my_pp.run({'filepath': my_file.name})


# Generated at 2022-06-14 18:00:12.424821
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil

    try:
        os.makedirs('temp')
        fp = open('temp/file', 'w')
        fp.write('video file')
        fp.close()
        time.sleep(1)
        pp = PostProcessor(None)
        pp.try_utime('temp/file', 0, 0)
        assert os.stat('temp/file').st_mtime == 0
        pp.try_utime('temp/file', 0, None)
        assert os.stat('temp/file').st_atime == 0
        assert os.stat('temp/file').st_mtime != 0
    finally:
        shutil.rmtree('temp')

# Generated at 2022-06-14 18:00:21.981456
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import time
    import stat
    import tempfile
    import unittest

    class TestPostProcessor(PostProcessor):
        def test_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
            self.try_utime(path, atime, mtime, errnote)

    class TestDownloader:
        def __init__(self):
            self.params = {}

        def report_warning(self, msg):
            self.warning_msg = msg

    class TestTime(object):
        def __init__(self, test_object, name):
            self._test_object = test_object
            self._name = name
            self.called = False

        def __call__(self, *args):
            assert not self.called

# Generated at 2022-06-14 18:00:22.584025
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:00:34.036160
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import datetime
    import os
    import os.path

    pp = PostProcessor(None)
    tmpfd, tmpfname = tempfile.mkstemp()
    os.close(tmpfd)

    atime = datetime.datetime.now()
    mtime = atime - datetime.timedelta(seconds=10)
    pp.try_utime(tmpfname, atime.timestamp(), mtime.timestamp())

    stat = os.stat(tmpfname)
    assert stat.st_atime == atime.timestamp()
    assert stat.st_mtime == mtime.timestamp()
    os.remove(tmpfname)

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:00:44.555407
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    if sys.hexversion < 0x02060000:
        # None of the operating systems support utime() in timezone before Python 2.6
        import pytest
        pytest.skip("Incompatible Python version")
    import os
    from time import time, sleep
    import pytz
    from ..utils import (
        encodeFilename,
        DateRange,
    )

    p = PostProcessor(None)
    # Note that the times are valid for 2014/01/01 in US/Pacific timezone
    p.try_utime(__file__, 1388640800, 1388640800)
    assert pytz.timezone('US/Pacific').localize(DateRange(1388640800)).timetuple() == os.path.getmtime(encodeFilename(__file__))

# Generated at 2022-06-14 18:00:53.811928
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    try:
        from unittest import mock
    except ImportError:
        import mock

    from .mocks import FakeYDL
    from .test_utils import FakeDownloader

    postprocessor = PostProcessor(FakeDownloader())

    # Patch os.utime
    with mock.patch('os.utime') as utime:
        # Patch report warning
        with mock.patch.object(FakeYDL, 'report_warning') as report_warning:
            # Pretend that utime fails
            utime.side_effect = Exception('Cannot update utime of file')
            # Run the method
            postprocessor.try_utime('filepath', 100, 100)
            # Check that report_warning was called
            report_warning.assert_called_with('Cannot update utime of file')

# Generated at 2022-06-14 18:01:06.503067
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import stat
    import shutil
    import tempfile
    from .compat import TemporaryFile

    # Create temporary directory for testing
    tmp_dir = tempfile.mkdtemp()

    # Create temporary file in that directory
    file_path = tmp_dir + '/test_file'
    with open(file_path, 'wb'):
        pass
    assert os.path.exists(file_path)

    # Create temporary PostProcessor
    postprocessor = PostProcessor(None)

    # Test with file that exists
    # Get current time
    t = time.time()
    # Modify current time
    postprocessor.try_utime(file_path, t - 100, t - 100)
    # Check whether utime has been modified
    st = os.stat(file_path)

# Generated at 2022-06-14 18:01:11.296943
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime('/tmp/yt-dl-test/utime-test-file', 1, 2)

# Generated at 2022-06-14 18:01:20.145449
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    utimes = []  # Save atime, mtime used by os.utime
    def _utime_mock(path, times):
        utimes.append(times)
    import __builtin__
    if not hasattr(__builtin__, '_utime'):
        __builtin__._utime = __builtin__.utime
    __builtin__.utime = _utime_mock
    try:
        pp.try_utime('/path/to/file', 1, 2)
        assert utimes == [(1, 2)]
    finally:
        __builtin__.utime = __builtin__._utime

# Generated at 2022-06-14 18:01:32.250007
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    from ..compat import compat_getenv
    from .common import FileDownloader

    (fd, filename) = tempfile.mkstemp()
    os.close(fd)


# Generated at 2022-06-14 18:01:39.531524
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        import _winreg
    except ImportError:
        return

    old_read_string = _winreg.ExpandEnvironmentStrings
    old_key = _winreg.HKEY_CURRENT_USER
    old_sub_key = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders'

    old_utime = os.utime
    def dummy_utime(*args, **kargs):
        raise Exception

    def dummy_read_string(path):
        return 'd:\\'

    _winreg.ExpandEnvironmentStrings = dummy_read_string


# Generated at 2022-06-14 18:01:43.403851
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import platform
    import time

    if platform.system().lower() != 'linux':
        return # No need to run this test on Linux

    import subprocess

    time.sleep(1) # To make mdate sure

    path = '/tmp/toto'
    mdate_before = subprocess.check_output('date -r %s +%%s' % path, shell=True)

    p = PostProcessor(None)
    p.try_utime(path, None, None)

    mdate_after = subprocess.check_output('date -r %s +%%s' % path, shell=True)

    assert mdate_before == mdate_after

# Generated at 2022-06-14 18:01:55.862252
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import FakeDownloader

    class MockOsModule(object):
        def utime(self, path, timestamp):
            self.path = path
            self.timestamp = timestamp
            raise Exception()

    class MockOsModule_2(object):
        def utime(self, path, timestamp):
            self.path = path
            self.timestamp = timestamp

    mock_os_module_1 = MockOsModule()
    mock_os_module_2 = MockOsModule_2()

    old_os_module = os.__dict__.get('os')
    os.os = mock_os_module_1

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    filename = 'video.mp4'
    path = os.path.join('/', filename)
    os.os = mock_

# Generated at 2022-06-14 18:02:03.775973
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import time
    import tempfile

    from .testcases import TestCase
    from ..downloader import Downloader
    from ..utils import DateRange

    class TestDownloader(Downloader):
        def post_process(self, *args, **kwargs):
            pass

        def report_warning(self, *args, **kwargs):
            pass

    def assertUTimeError(video_id):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            filename = os.path.basename(temp_file.name)

# Generated at 2022-06-14 18:02:15.144638
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest
    import tempfile
    import os
    import shutil, time
    from ..compat import compat_str

    class TestPP(PostProcessor):
        pass

    test_dir = tempfile.mkdtemp()
    filename = 'utime_test.txt'
    test_path = os.path.join(test_dir, filename)


# Generated at 2022-06-14 18:02:25.664956
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    # Create a PostProcessor
    pp = PostProcessor()

    # Create a file to test
    import tempfile
    tf = tempfile.NamedTemporaryFile()

    # Test the method using non-existing files should do nothing
    pp.try_utime('non-existing-file.mp3', 1, 1, 'error non-existing-file.mp3')
    # Test the method using existing file should change the utime to (1, 1)
    pp.try_utime(tf.name, 1, 1, 'error ' + tf.name)

    assert os.path.getatime(tf.name) == 1
    assert os.path.getmtime(tf.name) == 1

    # Cleanup
    tf.close()

# Generated at 2022-06-14 18:02:35.425859
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    from .utils import prepend_extension
    from .common import FileDownloader
    from .compat import (
        compat_urllib_request,
        compat_urllib_error,
    )

    # Create an empty temporary directory
    dl = FileDownloader({'outtmpl': os.path.join(os.path.dirname(__file__), 'test.%(ext)s')})
    temp_dir = dl.params['outtmpl'] % {'ext': ''}
    if not os.path.isdir(temp_dir):
        os.mkdir(temp_dir)


# Generated at 2022-06-14 18:02:44.277774
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyPostProcessor(PostProcessor):
        pass

    class DummyYoutubeDL():
        def report_warning(self, errnote):
            self.errnote = errnote

    dpp = DummyPostProcessor()
    dl = DummyYoutubeDL()
    dpp.set_downloader(dl)
    try:
        dpp.try_utime('', '', '')
    except Exception:
        assert False, 'try_utime failed'
    assert dl.errnote == 'Cannot update utime of file'

# Generated at 2022-06-14 18:02:54.307361
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import os
    import time

    from subprocess import call, PIPE


# Generated at 2022-06-14 18:03:01.371605
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from pytube import Playlist
    from pytube.downloader import FileDownloader
    from pytube.compat import parse_qs
    from pytube.exceptions import RegexMatchError
    from pytube.exceptions import LiveStreamError


# Generated at 2022-06-14 18:03:10.769743
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test PostProcessor.try_utime
    """
    import mock
    import tempfile
    import shutil
    from .compat import os


# Generated at 2022-06-14 18:03:15.590042
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime(__file__, 0, 0)
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile() as f:
        pp.try_utime(f.name, 0, 0, errnote='testing postprocessor.try_utime')

# Generated at 2022-06-14 18:03:20.854746
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader():

        def __init__(self):
            self.warning_count = 0

        def report_warning(self, message):
            self.warning_count += 1

    pp = PostProcessor(FakeDownloader())

    try:
        os.utime('/nonexistentfile', (1,1))
    except Exception:
        pass

# Generated at 2022-06-14 18:03:28.989818
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import time
    import filecmp
    import unittest
    class TestPostProcessor(PostProcessor):
        def run(self, information):
            return [], information
    class FileDownloader():
        def __init__(self):
            self.params = {}
        def to_screen(self, message):
            pass
        def report_warning(self, message):
            pass
    def compare_files(file_name_1, file_name_2):
        return (filecmp.cmp(encodeFilename(file_name_1), encodeFilename(file_name_2)))


# Generated at 2022-06-14 18:03:39.095062
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from sys import platform
    from tempfile import mkdtemp
    from shutil import copyfile
    from os import makedirs, stat, utime, unlink, remove

    class TestPostProcessor(PostProcessor):
        def run(self, information):
            self.try_utime(information['filepath'], 1, 2)
            return [], information


    os.environ["TMP"] = "/tmp"
    ydl_opts = {'writethumbnail': True, 'continuedl': True, 'quiet': True}

    ydl = YoutubeDL(ydl_opts)
    pp = TestPostProcessor(ydl)


# Generated at 2022-06-14 18:03:48.436092
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ytdl_postprocessor import PostProcessor
    from ytdl_downloader import Downloader, MaxDownloadsReached
    from ytdl_info_extractor import YoutubeIE, YoutubeSearchIE
    from ytdl_extractor import InfoExtractor
    from unittest import TestCase
    import tempfile
    import os
    import time

    class PostProcessorTest(TestCase):
        def setUp(self):
            self.test_file = tempfile.NamedTemporaryFile()
            self.pp = PostProcessor(None)
            self.pp._downloader = Downloader({'forcejson': True})
            self.pp._downloader.add_info_extractor(YoutubeIE())
            self.pp._downloader.add_info_extractor(YoutubeSearchIE())


# Generated at 2022-06-14 18:03:54.171247
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader

    d = FileDownloader({})
    pp = PostProcessor(d)
    path = 'dummy_path'
    atime = 1234.0
    mtime = 1234.0
    errnote = 'Cannot update utime of file'
    pp.try_utime(path, atime, mtime, errnote)

# Generated at 2022-06-14 18:04:10.347475
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import pytest

    from ..extractor import YouTubeIE

    # Create a file with a known timestamp
    t = time.time()
    tmp_path = tempfile.mktemp()
    with open(tmp_path, 'w') as tmp_file:
        tmp_file.write('foo')
    os.utime(tmp_path, (t, t))

    # Test try_utime
    info = {}
    info['filepath'] = tmp_path
    post_processor = PostProcessor()
    post_processor._downloader = YouTubeIE()
    post_processor.run(info)

    # Check utime was not modified
    assert abs(os.stat(tmp_path).st_mtime - t) < 1

# Generated at 2022-06-14 18:04:15.897971
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import time
    from ..compat import PY2, parse_timezone


# Generated at 2022-06-14 18:04:24.851609
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time

    import pytest

    from ..utils import DateRange

    from .common import FakeYDL
    from .test_downloader import MockFD

    tmp = tempfile.mkdtemp()


# Generated at 2022-06-14 18:04:33.748710
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    from subprocess import Popen, PIPE

    class DummyDownloader():
        def report_warning(self, msg):
            print(msg)

    def get_utime(path):
        stat_cmd = ['stat', '-c', '%Y', encodeFilename(path)]
        utime = Popen(stat_cmd, stdout=PIPE, stderr=PIPE)
        utime = utime.communicate()[0]
        return float(utime)

    # Create a test file
    fd, path = tempfile.mkstemp()
    print('Test file path: %s' % path)
    # File created without utime
    print('Initial utime: %f' % get_utime(path))

# Generated at 2022-06-14 18:04:34.342396
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:04:45.722630
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import errno
    import os
    import shutil
    import sys
    import tempfile
    import unittest
    import datetime
    import time
    import mock

    # print('Test %s being run' % __name__)  # For manual testing purposes

    class TestPostProcessor(PostProcessor):
        def run(self, information):
            local_path = information['filepath']
            self.try_utime(local_path, int(time.time()) + 10, int(time.time()))
            return [], information

    class MockDownloader(object):
        def report_warning(self, str):
            pass

        def params(self):
            return {}

    def _fake_time():
        return 10

    def _fake_time_mock(self):
        return _fake_time()

   

# Generated at 2022-06-14 18:04:47.821413
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime('/foo/bar', 1, 2)

# Generated at 2022-06-14 18:04:57.020417
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyFile(object):
        def __init__(self, path, mtime):
            self.path = path
            self.mtime = mtime

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def utime(self, *args):
            raise OSError()

    class DummyDownloader(object):
        def __init__(self):
            self.params = {
                'verbose': False
            }
            self.pp = PostProcessor(self)

    class DummyInfo(dict):
        def __init__(self, *args, **kwargs):
            super(DummyInfo, self).__init__(*args, **kwargs)
            self.filepath = encodeFilename(self['path'])


# Generated at 2022-06-14 18:05:08.377165
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Unit test for method try_utime of class PostProcessor"""
    import platform
    import datetime
    import time
    import tempfile
    import os

    pp = PostProcessor()
    with tempfile.NamedTemporaryFile() as f:
        filename = f.name
        # Mac OS X uses POSIX file timestamps with 1-second precision.
        # This test may fail on these platforms, especially around midnight.
        pp.try_utime(filename, 1000, 2000)
        pp.try_utime(filename, 3000, 4000)
    stat = os.stat(filename)
    if platform.system() == 'Windows':
        # Windows stores file timestamps with a 2-second precision.
        assert abs(stat.st_mtime - 3) < 2, 'mtime not updated correctly'

# Generated at 2022-06-14 18:05:19.200051
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ydl.downloader import FakeDownloader
    import tempfile
    import os
    import sys

    def _test_PostProcessor_try_utime():
        pp = PostProcessor(FakeDownloader())
        path = tempfile.mktemp()
        open(path, 'w').close()
        pp.try_utime(path, 0, 0)
        pp.try_utime(path, 1, 2)
        os.remove(path)

    def _test_PostProcessor_try_utime_assert():
        assert False, '_test_PostProcessor_try_utime raises exception'

    if sys.platform == 'win32':
        _test_PostProcessor_try_utime()
    else:
        import errno
        from ..utils import sanitize_open

# Generated at 2022-06-14 18:05:43.843089
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import unittest

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    class TestDownloader(object):
        def __init__(self):
            self.warnings = []
            self.tempdir = tempfile.mkdtemp()

        def report_warning(self, msg):
            self.warnings.append(msg)

    class TestPostProcessor(PostProcessor):
        def __init__(self):
            self.set_downloader(TestDownloader())

    test_dir = tempfile.mkdtemp()
    test_file = os.path.join(test_dir, 'test_file')


# Generated at 2022-06-14 18:05:50.900340
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import Downloader
    from .extractor import InfoExtractor
    from .extractor.common import InfoExtractor
    from .compat import compat_HTTPError

    class FakeInfoExtractor(InfoExtractor):
        @staticmethod
        def suitable(info_dict):
            return True

        def extract(self, url):
            self.report_result('video', {})

    class FakePostProcessor(PostProcessor):
        pass

    class FakeYoutubeIE(InfoExtractor):
        @staticmethod
        def suitable(info_dict):
            return False

        def _real_extract(self, url):
            raise compat_HTTPError(None, None, '', None, None)

    ie = FakeInfoExtractor()
    pp = FakePostProcessor()
    yt = FakeYoutubeIE()
    y

# Generated at 2022-06-14 18:05:58.822791
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader(object):
        def __init__(self):
            self.warning_cnt = 0

        def report_warning(self, note):
            self.warning_cnt += 1

    pp = PostProcessor(MockDownloader())
    pp.try_utime("MockPath", 1234, 5678, "Cannot update utime of file")
    assert(pp._downloader.warning_cnt == 1)

# Generated at 2022-06-14 18:06:06.882243
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .FileDownloader import FileDownloader
    from .common import FakeYDL
    from .compat import int_or_none, compat_urllib_error

    class DummyPostProcessor(PostProcessor):
        def __init__(self, *args, **kwargs):
            super(DummyPostProcessor, self).__init__(*args, **kwargs)
            self._errnote = ''

        def try_utime(self, path, atime, mtime, errnote=''):
            path += 'bar'
            atime += 1
            mtime += 1
            self._errnote = errnote

            try:
                os.utime(encodeFilename(path), (atime, mtime))
            except Exception:
                pass

    def _run_downloader(params):
        ydl = FakeY

# Generated at 2022-06-14 18:06:12.204897
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    with YoutubeDL(params={'logger': YoutubeDL.buffer_logger()}) as ydl:
        pp = PostProcessor(ydl)

        import tempfile
        import time
        import atexit
        tmpfd, tmppath = tempfile.mkstemp()
        atexit.register(lambda: os.remove(tmppath))

        t1 = time.time() - 10
        t2 = time.time() - 5
        pp.try_utime(tmppath, t1, t2)
        atime, mtime = os.stat(tmppath)[7:9]
        assert mtime == t2, 'mtime not updated'
        assert atime == t1, 'atime not updated'

# Generated at 2022-06-14 18:06:22.414289
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockOs:
        def __init__(self):
            self.utime_args = []

        def utime(self, path, utime_tuple):
            self.utime_args.append([path, utime_tuple])

    class MockDownloader:
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    pp = PostProcessor(None)
    pp.set_downloader(MockDownloader())
    MockOs().utime(pp, 'path', 'utime_tuple')


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:06:31.170000
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from PyIntoYouTube.compat import IS_WIN32
    import os
    import unittest

    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)
            self.test_atime = None
            self.test_mtime = None

        def run(self, info):
            self.try_utime(info['filepath'], self.test_atime, self.test_mtime)

    def createFile(path):
        f = open(path, 'w')
        f.write('Test Content')
        f.close()

    def getDate(path):
        if IS_WIN32:
            import time
            f = os.stat(path)[-2]
            t = time.localtime(f)

# Generated at 2022-06-14 18:06:38.963056
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class testDownloader():
        def report_warning(self, message):
            self.error = message

    class testPostProcessor(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)

    tp = testPostProcessor(testDownloader())
    tp.try_utime('/', 0, 0)
    assert tp._downloader.error == 'Cannot update utime of file'

# Generated at 2022-06-14 18:06:48.680158
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def run(self, info):
            return 'downloads/', info

    postProcessor = TestPostProcessor()
    from ..downloader import Downloader
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange
    class TestDownloader(Downloader):
        def __init__(self, params):
            self._ies = [TestIE(params)]
            self._params = params

    class TestIE(InfoExtractor):
        def _real_extract(self, url):
            return { 'id': 'test', 'url': url, 'title': 'test', 'ext': 'mp3', 'upload_date': '20100102' }

    dl = TestDownloader({})
    postProcessor.set_downloader(dl)

# Generated at 2022-06-14 18:06:57.840765
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import is_py2
    import stat
    import shutil
    import tempfile
    import time

    # TODO: don't do this.
    import youtube_dl.downloader.common as common
    common.postprocessor = [None]


    # TODO: this is a very crude test
    # TODO: better test with set mtimes of files
    # TODO: merge this method with AudioMergerPP
    class MockDownloader:
        def report_warning(self, msg):
            print('WARNING: %r' % msg)


    def test_utime(pp, f, atime, mtime, errnote):
        oldstat = os.stat(f)
        pp.try_utime(f, atime, mtime, errnote)
        newstat = os.stat(f)
       

# Generated at 2022-06-14 18:07:31.412572
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    class FakeDownloader:
        def __init__(self):
            self.notice = []

        def report_warning(self, warning):
            self.notice.append(warning)

    fake_downloader = FakeDownloader()
    fake_pp = PostProcessor(fake_downloader)

    # Test pass
    fake_pp.try_utime(__file__, 1455878190, 1455878190)

    assert len(fake_downloader.notice) == 0

    # Test error
    fake_pp.try_utime('.', 1455878190, 1455878190)

    assert len(fake_downloader.notice) == 1

# Generated at 2022-06-14 18:07:40.067502
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Unit test for method try_utime of PostProcessor.
    """
    import pytest
    from .test_utils import make_mock_downloader
    from .test_utils import mock_open_file
    from .test_utils import mock_exists

    def path_exists(path):
        return path == 'testfile'

    def test_utime(path, times):
        assert path == b'testfile'

    def test_no_utime(path, times):
        pytest.fail('test_no_utime should not be called')

    postprocessor = PostProcessor(make_mock_downloader())


# Generated at 2022-06-14 18:07:45.045947
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    try:
        pp.try_utime('test_file', 1337, 1337)
    except PostProcessingError:
        raise Exception('try_utime raised PostProcessingError although test file existing')
    try:
        pp.try_utime('not_existing_file', 1337, 1337)
    except PostProcessingError:
        pass
    else:
        raise Exception('try_utime did not raise PostProcessingError although test file not existing')

# Generated at 2022-06-14 18:07:53.679625
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    def try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
        self._test_file_utime_called = path, atime, mtime, errnote

    import types
    pp = PostProcessor(None)
    pp._test_file_utime_called = None
    pp.try_utime = types.MethodType(try_utime, pp)

    pp.try_utime('path', 'atime', 'mtime')
    assert pp._test_file_utime_called == ('path', 'atime', 'mtime', 'Cannot update utime of file')

    del pp.try_utime
    assert not hasattr(pp, 'try_utime')

# Generated at 2022-06-14 18:08:03.643015
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil

    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            PostProcessor.__init__(self)

    pp = TestPostProcessor()
    tempdir = os.path.realpath(tempfile.mkdtemp())
    filename = os.path.join(tempdir, "test_file")

    with open(filename, "wb") as new_file:
        new_file.write(b"HELLO")
    file_stat = os.stat(filename)
    atime = int(time.time()) - 200
    mtime = int(time.time()) - 200

    pp.try_utime(filename, atime, mtime)
    new_file_stat = os.stat(filename)

    assert new

# Generated at 2022-06-14 18:08:09.347567
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest
    class test_PostProcessor:
        @staticmethod
        def report_warning(errnote):
            print(errnote, 'test')
    class test_utime():
        @staticmethod
        def utime(path, atime, mtime, errnote='Cannot update utime of file'):
            pass
    obj = test_PostProcessor()
    obj.try_utime = test_utime
    obj.try_utime("test.txt", 1, 2)


# Generated at 2022-06-14 18:08:20.701311
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import shutil
    import pytest

    def _get_mtime(path):
        return os.stat(path).st_mtime

    def _create_temp_file():
        return tempfile.mkstemp()[1]

    with tempfile.TemporaryDirectory(prefix='youtube-dl.PostProcessorTest.') as temp_dir:
        pp = PostProcessor(None)

        atime = time.time()
        mtime1 = atime + 10
        mtime2 = atime + 20

        path = _create_temp_file()

        # Test changing the mtime
        pp.try_utime(path, atime, mtime1)
        assert _get_mtime(path) == mtime1

        # Test changing the mtime again
        pp.try_ut

# Generated at 2022-06-14 18:08:25.991412
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    class FakePostProcessor(PostProcessor):
        def __init__(self, *args, **kwargs):
            PostProcessor.__init__(self, *args, **kwargs)
            self.warnings = []

        def report_warning(self, warning):
            self.warnings.append(warning)

    fake = FakePostProcessor()
    fake.try_utime('', '', '', 'Cannot update utime')
    assert len(fake.warnings) == 1

    fake = FakePostProcessor()
    fake.try_utime('', 0, 0, 'Cannot update utime')
    assert len(fake.warnings) == 0

# Generated at 2022-06-14 18:08:36.058377
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import shutil
    import time
    import stat

    tempdir = tempfile.mkdtemp()

    filename = os.path.join(tempdir, 'test_utime')

    pp = PostProcessor(None)
