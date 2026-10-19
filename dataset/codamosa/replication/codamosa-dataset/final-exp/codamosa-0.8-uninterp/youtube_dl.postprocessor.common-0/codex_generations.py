

# Generated at 2022-06-14 17:58:39.740564
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import os

    f = tempfile.NamedTemporaryFile()
    f.close()

    # Redefine PostProcessor in order to use only constructor
    class MockPostProcessor(PostProcessor):
        def __init__(self):
            PostProcessor.__init__(self)

    p = MockPostProcessor()
    atime = time.time()
    p.try_utime(f.name, atime, atime)
    assert os.path.getatime(f.name) == atime

    fake_atime = atime + 100
    p.try_utime(f.name, fake_atime, fake_atime)
    assert os.path.getatime(f.name) != fake_atime

    os.remove(f.name)

# Generated at 2022-06-14 17:58:42.115907
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert False

# Generated at 2022-06-14 17:58:49.701894
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time

    import pytest

    from ..downloader.common import FileDownloader

    tmpdir = tempfile.mkdtemp(prefix='youtube-dl-test-')

    try:
        fd = open(os.path.join(tmpdir, 'foo'), 'wb')
        fd.write(b'foo')
        fd.close()

        pp = PostProcessor(FileDownloader())
        pp.try_utime(os.path.join(tmpdir, 'foo'), time.time() + 10000, time.time() - 1234)
    finally:
        shutil.rmtree(tmpdir)

# Generated at 2022-06-14 17:58:55.001339
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    try:
        os.utime(None, None)
        assert False
    except TypeError as e:
        pp.throw_utime_error = lambda: e

    try:
        pp.try_utime(None, None, None)
        assert False
    except TypeError as e:
        #  raise if os.utime() fails, in this case with None parameters
        assert True

# Generated at 2022-06-14 17:59:04.950934
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    p = PostProcessor(None)
    class Dummy:
        def report_warning(self, note):
            assert note == 'Cannot update utime of file'
    p._downloader = Dummy()
    # test try_utime for a non-existent file
    p.try_utime('non-existent', 0, 0)
    # test try_utime for an existing file
    # we create a dummy file
    import tempfile
    fd, fp = tempfile.mkstemp()
    os.close(fd)
    # change time
    import time
    p.try_utime(fp, 0, time.time())  # shouldn't raise an exception
    # remove the dummy file
    os.remove(fp)

# Generated at 2022-06-14 17:59:09.885091
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import unittest
    from ..utils import FakeYDL

    class TestPostProcessor(PostProcessor):
        def run(self, information):
            self.try_utime(__file__, 0, 0)
            return [], information

    ydl = FakeYDL()
    pp = TestPostProcessor(ydl)
    pp.run({})
    assert ydl.has_message('Cannot update utime')



# Generated at 2022-06-14 17:59:22.113608
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import stat
    import tempfile
    import time
    import unittest

    class PP(PostProcessor):
        pass
    pp = PP()

    def time():
        return int(time.time())
    def zone():
        return time.strftime('%z')

    with tempfile.NamedTemporaryFile(delete=False) as thefile:
        print(thefile.name)
        filename = thefile.name
        oldmtime = os.stat(filename).st_mtime
        # Test: set to current time
        pp.try_utime(filename, time(), time())
        newmtime = os.stat(filename).st_mtime

# Generated at 2022-06-14 17:59:30.584920
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import filecmp
    import tempfile
    import time
    post_processor = PostProcessor()
    dummy_file_1 = tempfile.NamedTemporaryFile()
    dummy_file_2 = tempfile.NamedTemporaryFile()
    # Write to both the temporary file and copy it
    dummy_file_1.write(u'\x00')
    dummy_file_1.flush()
    dummy_file_2.write(u'\x00')
    dummy_file_2.flush()
    # Get the current time
    curr_time = time.time()
    # Modify the time of the copy of file and then set the time of the original
    # file to the time of the copy
    dummy_file_2.seek(0)

# Generated at 2022-06-14 17:59:38.273641
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def __init__(self):
            self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '__test__.tmp')
            if os.path.exists(self.path):
                os.remove(self.path)
            open(self.path, 'w')

        def run(self, info):
            self.try_utime(self.path, 1, 0)
            self.try_utime(self.path, 0, 1)
            return [], info

    p = TestPostProcessor()
    p.run({})

# Generated at 2022-06-14 17:59:45.889324
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    class TestPostProcessor(PostProcessor):
        def run(self, info):
            self.try_utime('non-existent', 0, 0)
            self.try_utime(None, 0, 0)
            return [], info
    ydl = YoutubeDL()
    ydl.add_post_processor(TestPostProcessor())
    ydl.download(['http://example.org'])

# Generated at 2022-06-14 17:59:49.046472
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    assert pp.try_utime('nowhere', 0, 0) is None


# Generated at 2022-06-14 17:59:56.137809
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from .ffmpeg import FFmpegExtractAudioPP

    # No need to test on Windows because Windows can't set time in this way.
    if os.name == 'nt':
        return

    # We can't test using tempfiles because the test should change the time of
    # file and tempfiles are deleted immediately after creation.
    testfile = 'postprocessor_test_file'

    downloader = FileDownloader(params={})
    downloader.add_info_extractor(None)

    pp = FFmpegExtractAudioPP(downloader)

# Generated at 2022-06-14 17:59:57.168003
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass


# Test case for class PostProcessor

# Generated at 2022-06-14 18:00:04.276876
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Important: if this unit test fails and the exception is an OSError, it is
    # probably because the user running the tests doesn't have the rights
    # to set the atime and mtime of the test file.
    # Note that the atime and mtime values are not important here,
    # only their type.
    from ..downloader.common import FileDownloader
    from ..utils import json_dict
    test_file = 'test'
    try:
        os.remove(test_file)
    except OSError:
        pass
    with open(test_file, 'a'):
        pass
    params = json_dict()

# Generated at 2022-06-14 18:00:14.044962
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import encodeFilename
    import os
    import shutil
    import tempfile
    import time
    import textwrap
    import unittest

    tempdir = tempfile.mkdtemp()


# Generated at 2022-06-14 18:00:26.068490
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil
    import platform

    if platform.system() == 'Windows':
        import errno
        from .utils import (
            compat_shutil_get_terminal_size,
            compat_shutil_which,
            compat_shutil_which,
            preferredencoding,
            copyfileobj,
            compat_urllib_request,
            compat_html_entities,
            )
        from pytube.exceptions import RegexNotFoundError
        from pytube.playlist import Playlist
        from pytube.streams import Stream
        from pytube.cli import YouTubeDLHandler


# Generated at 2022-06-14 18:00:36.949911
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import YoutubeDL
    from .compat import PY2

    class TestPostProcessor(PostProcessor):
        pass

    TestPostProcessor._downloader = YoutubeDL({
        'outtmpl': 'test',
        'postprocessor_args': ['--exec', ':']
    })
    proc = TestPostProcessor()
    assert proc._configuration_args() == ['--exec', ':']
    assert proc._configuration_args(['--exec', ':']) == ['--exec', ':']

    # in TempTestDir:
    # $ mkdir test
    # $ touch test/file
    # $ touch -d '2012-01-01 00:00:00 UTC' test/file
    # $ touch test/dir
    # $ mkdir -p test/dir/subdir
    # $ touch

# Generated at 2022-06-14 18:00:46.918965
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import time
    from .YoutubeDL import YoutubeDL
    from .downloader.common import FileDownloader
    from .PostProcessor import PostProcessor

    def file_write(path, data):
        with open(path, 'wb') as f:
            f.write(data)

    def get_mtime(path):
        return os.path.getmtime(encodeFilename(path))

    tempdir_path = tempfile.gettempdir()
    tempdir_path_encoded = encodeFilename(tempdir_path)
    filename = 'test_postprocessor_utime'
    filename_encoded = encodeFilename(filename)
    filename_path = os.path.join(tempdir_path_encoded, filename_encoded)

# Generated at 2022-06-14 18:00:57.922412
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..__main__ import YoutubeDL
    from ..YoutubeDL import YoutubeDL
    from ..utils import prepare_filename
    from .common import FakeYDL
    from .test_downloader import MockFD
    from .test_extractor import TestSearchInfoExtractor

    prepare_filename.to_screen = lambda x: x


# Generated at 2022-06-14 18:01:08.268501
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL

    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(TestPostProcessor, self).__init__(downloader)
            self.utime_called = False

        def run(self, info):
            self.try_utime(info['filepath'], 0, 0, errnote='Test')
            return [], info

    # Test the error "note" message
    ydl = YoutubeDL({'logger': TestLogger()})
    pp = TestPostProcessor(ydl)
    pp.run({'filepath': 'foo'})
    ydl.to_screen.assert_called_once_with('[generic] Test')


# Generated at 2022-06-14 18:01:22.079598
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import datetime
    import shutil
    import os

    fd, temp_filename = tempfile.mkstemp()

    atime = datetime.datetime.now() - datetime.timedelta(hours=1)
    mtime = datetime.datetime.now() - datetime.timedelta(days=1)

    os.close(fd)
    try:
        os.remove(encodeFilename(temp_filename))
    except:
        pass

    p = PostProcessor({})

    try:
        p.try_utime(temp_filename, atime, mtime)
        raise AssertionError('No exception raised')
    except PostProcessingError:
        pass


# Generated at 2022-06-14 18:01:33.311258
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from test.helper import capture_output
    from .testutils import TestDownloader

    # Run try_utime in a dry run mode and check the warning
    downloader = TestDownloader(params={'simulate': True})
    pp = PostProcessor(downloader)
    with capture_output() as (_, err):
        pp.try_utime('test', 1, 2)
    assert 'test: Cannot update utime of file' in err.getvalue()

    # Run try_utime in a regular mode and check that there is no warning
    downloader = TestDownloader()
    pp = PostProcessor(downloader)
    with capture_output() as (_, err):
        pp.try_utime('test', 1, 2)
    assert len(err.getvalue()) == 0

# Generated at 2022-06-14 18:01:44.898070
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import sys
    import unittest
    from ..compat import compat_mock
    from ..utils import PostProcessor, encodeFilename

    class DummyFile(object):
        pass

    class DummyPP(PostProcessor):
        def __init__(self, *args, **kwargs):
            super(DummyPP, self).__init__(*args, **kwargs)
            self._validate_args()

        def _validate_args(self):
            self._downloader = None
            self._downloader_lock = None
            self._progress_hooks = None
            self._params = None
            self._filename = None
            self._tmpfilename = None
            self._outtmpl = None
            self._do_progress = None
            self._simulate = None
            self._keepvideo = None

# Generated at 2022-06-14 18:01:49.316242
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile

    f = NamedTemporaryFile(mode='w', delete=False)
    f.close()
    filename = f.name

    import time

    # In case the file is new, we need to wait a bit to see updates
    time.sleep(1)


# Generated at 2022-06-14 18:01:50.833490
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    print('TODO')

# Generated at 2022-06-14 18:02:00.941062
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil

    temp_np = os.path.join(os.getcwd(), 'temp_np.txt')
    f = open(temp_np, 'w')
    f.close()
    shutil.copyfile(temp_np, 'temp.txt')

    pp = PostProcessor(None)
    pp.try_utime('temp.txt', 1234, 1235, errnote=None)

    assert time.time() - os.stat('temp.txt').st_mtime < 1
    assert time.time() - os.stat(temp_np).st_mtime < 1

    os.remove('temp.txt')
    os.remove(temp_np)


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:02:13.538510
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    from ..compat import PY2
    from ..utils import write_json_file

    # Cannot use @mock.patch.object because in python 2 mock.patch.object
    # would be applied on the class rather than on the instance.
    def test_method(self, path, atime, mtime, errnote='Cannot update utime of file'):
        PostProcessor_try_utime_original(self, path, atime, mtime, errnote)

    orig_method = PostProcessor.try_utime

# Generated at 2022-06-14 18:02:19.858500
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time

    def test_attributes(f):
        atime = int(time.time()) + 100
        mtime = int(time.time()) + 200
        pp = PostProcessor(None)
        pp.try_utime(f, atime, mtime)
        assert os.stat(f).st_atime < atime
        assert os.stat(f).st_mtime < mtime

    with tempfile.NamedTemporaryFile() as tf:
        test_attributes(tf.name)
        temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:02:31.802918
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    from subprocess import Popen, PIPE, STDOUT
    from ..compat import compat_subprocess_get_DEVNULL

    DEVNULL = compat_subprocess_get_DEVNULL()
    assert DEVNULL is not None, 'DEVNULL is None'

    class MockDownloader():
        def __init__(self, params=None):
            if params is None:
                self.params = {}
            else:
                self.params = params

        def report_warning(self, errnote):
            print(errnote)

    # create dummy file
    fd, path = tempfile.mkstemp(prefix='youtube-dl_test_try_utime_', text=False)
    # get file stat
    stat = os.fstat(fd)

    # init PostProcessor
   

# Generated at 2022-06-14 18:02:43.240264
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FakeYDL
    ydl_opts = {
        'keepvideo': True,
        'writethumbnail': True,
        'skip_download': True,
        'nooverwrites': True,
        'writeinfojson': True,
        'outtmpl': '%(id)s%(ext)s'
    }
    ydl = FakeYDL(ydl_opts)
    try_utime_meth = PostProcessor(ydl).try_utime
    try:
        try_utime_meth('nonexistent', 0, 0, None)
        assert False  # try_utime should raise a PostProcessingError exception
    except PostProcessingError:
        pass
    open('test.txt', 'w').close()

# Generated at 2022-06-14 18:02:56.817564
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from ..utils import DateRange, DateRangeInfoExtractor

    # Dummy file, don't need to be exist
    filename = 'test.FLV'
    # Dummy downloader, don't need to download anything, mimick a fake file
    downloader = Downloader({
        'nopart': True,
        'quiet': True,
        'forcefilename': filename,
        'forcetitle': 'test',
        'forcethumbnail': 'http://i.ytimg.com/vi/9bZkp7q19f0/hqdefault.jpg',
    })
    # Dummy extractor
    ie = DateRange((1, 1, 2), (1, 1, 3))
    # Dummy downloader will call ie.extract()
    downloader.add_info_ext

# Generated at 2022-06-14 18:03:06.280098
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Let downloader be None
    pp = PostProcessor(None)
    if os.path.exists('./nonexistent_file'):
        os.remove('./nonexistent_file')
    if os.path.exists('./postprocessor_test.py'):
        # Change the attribute of file postprocessor_test.py
        os.utime(encodeFilename('./postprocessor_test.py'), (1426808429, 1426808430))
        # Test try_utime method
        pp.try_utime('./nonexistent_file', 1426808429, 1426808430)
        pp.try_utime('./postprocessor_test.py', 1426808430, 1426808431)
        # Compare the changed attribute

# Generated at 2022-06-14 18:03:16.331947
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    downloader = FileDownloader({})
    pp = PostProcessor(downloader)

    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test_utils.py')

    atime_pre = os.path.getatime(file_path)
    mtime_pre = os.path.getmtime(file_path)

    pp.try_utime(file_path, atime_pre, mtime_pre, errnote='foo')

    assert os.path.getatime(file_path) == atime_pre
    assert os.path.getmtime(file_path) == mtime_pre

    # TODO: Test a case of failure of utime.

# Generated at 2022-06-14 18:03:26.496488
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def utime(path, atime=None, mtime=None):
        if path == 'a' and mtime == 'b':
            raise OSError("can't touch this")

    import __builtin__
    _utime = __builtin__.utime
    __builtin__.utime = utime
    pp = PostProcessor()
    pp.try_utime('a', 'b', 'c')
    pp.try_utime('a', 'b', 'b')
    __builtin__.utime = _utime
    import sys
    if sys.version_info[:2] >= (3, 0):
        __builtin__.utime = None

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:03:37.488464
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Downloader (interface/FileDownloader.py) calls PostProcessor.try_utime.
    PostProcessor.try_utime calls os.utime.
    FileDownloader calls PostProcessor.try_utime when it fails to download
    audio with ffmpeg.
    So if we can't update utime of file, we raise AudioConversionError.
    """

    from .common import FileDownloader
    from .utils import DateRange

    downloader = FileDownloader({})
    pp = PostProcessor(downloader=downloader)
    date_range = DateRange(None, None)
    fake_path = 'fake_path'

    def _fake_u_time(path, atime, mtime):
        pass

    old_u_time = os.utime
    os.utime = _fake_u

# Generated at 2022-06-14 18:03:47.533358
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import stat

    try:
        os.remove('test_utime.txt')
    except OSError:
        pass
    with open('test_utime.txt', 'w') as f:
        f.write('test file')
    pp = PostProcessor(None)

    # File atime and mtime are too old
    os.utime('test_utime.txt', (0, 0))
    pp.try_utime('test_utime.txt', 10**9, 10**9)
    assert int(os.stat('test_utime.txt').st_atime) != 0  # atime must be updated
    assert int(os.stat('test_utime.txt').st_mtime) != 0  # mtime must be updated

    # File atime too old and mtime too new
    os

# Generated at 2022-06-14 18:03:50.331552
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    try:
        pp.try_utime('.', 1, 2)
    except Exception:
        return False
    else:
        return True

# Generated at 2022-06-14 18:04:01.674873
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkdtemp
    from shutil import rmtree
    from time import time
    from os import path, utime

    tmp_dir = mkdtemp()
    tmp_file = path.join(tmp_dir, 'tmp_file')
    with open(tmp_file, 'w'):
        pass
    cur_time = time()
    utime(tmp_file, (cur_time, cur_time))
    file_stat = os.stat(tmp_file)
    postprocessor = PostProcessor(None)
    postprocessor.try_utime(tmp_file, cur_time + 3600, cur_time + 7200, 'test')
    assert cur_time + 3600 == os.stat(tmp_file).st_atime

# Generated at 2022-06-14 18:04:10.812990
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            self.is_time_set = False
            PostProcessor.__init__(self, downloader)

        def try_utime(self, path, atime, mtime, errnote=None):
            self.is_time_set = True
            self.path = path
            self.atime = atime
            self.mtime = mtime
            self.errnote = errnote

    post_processor = FakePostProcessor()
    post_processor.try_utime('/test', 1, 1, 'Cannot update utime of file')
    assertPostProcessorTimeSet(post_processor)



# Generated at 2022-06-14 18:04:21.630194
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange

    class FakePostProcessor(PostProcessor):
        def run(self, information):
            self.try_utime(information['filepath'],
                           information['filepath'].stat().st_atime,
                           information['filepath'].stat().st_mtime)
            return [], information  # by default, keep file and do nothing

    class FakeDownloader(object):
        params = None


# Generated at 2022-06-14 18:04:39.355915
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class _Downloader(object):
        def report_warning(self, only_for_test):
            pass

    downloader = _Downloader()
    postprocessor = PostProcessor()
    postprocessor.set_downloader(downloader)
    temp = os.tempnam()
    try:
        postprocessor.try_utime(temp, 0, 0)
    finally:
        os.remove(temp)

# Generated at 2022-06-14 18:04:50.265749
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractors
    from ..downloader import gen_ydl
    from ..utils import DateRange

    class MyExtractor(object):
        IE_NAME = 'TestExtractor'
        def __init__(self, ydl):
            self.ydl = ydl

        def _real_extract(self, info, *args):
            def _get_file_id(ext):
                return '__%s__' % ext
            info['ext'] = 'mp4'
            info['title'] = 'test_video'
            info['formats'] = [_get_file_id(info['ext'])]
            info['upload_date'] = '20180807'
            info['categories'] = []
            info['tags'] = []
            info['thumbnails'] = []

# Generated at 2022-06-14 18:04:57.000114
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import sys
    import tempfile
    import shutil
    import subprocess

    # This method needs to be executed in a system with a working
    # 'touch' command.
    try:
        subprocess.check_call(['touch', '--help'])
    except (subprocess.CalledProcessError, OSError):
        print('Skipping "test_PostProcessor_try_utime"')
        return

    # A simple but effective way to create a temporary directory for
    # the test is to use the system's tmp directory and add our
    # component at the end of the path.
    tmp_dir = os.path.join(tempfile.gettempdir(), 'youtube_dl_test')
    # We don't use mkdtemp for compatibility reasons, since the code
    # needs to run on Python 2

# Generated at 2022-06-14 18:05:08.292831
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import shutil
    import datetime

    tmpdir = tempfile.mkdtemp()
    testpath = os.path.join(tmpdir, "foo.bar")

    f = open(testpath, 'wb')
    f.write(b"foobar")
    f.close()

    pp = PostProcessor(None)
    pp.try_utime(testpath, 0, 0)

    # On some filesystems utime can only be set with second precision.
    # See http://bugs.python.org/issue24658
    mtime = os.stat(testpath).st_mtime
    mtime_within_one_second = mtime + datetime.timedelta(seconds=1).total_seconds()
    assert mtime <= mtime_within_one_second

    shutil

# Generated at 2022-06-14 18:05:19.199201
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import sys
    from ..compat import which
    from .common import BINARIES

    # Check if ffmpeg is installed
    try:
        which(u'ffmpeg')
        bin_ffmpeg = which('ffmpeg') + ['-i']
    except Exception:
        if sys.platform == 'win32':
            raise unittest.SkipTest('ffmpeg not installed')
        else:
            raise unittest.SkipTest('ffmpeg not found')

    def _test_utime_audio(path, expected_errnote):
        path_tempdir = tempfile.mkdtemp()

        pp = PostProcessor(None)  # downloader=None
        pp.try_utime(path, 0, 0, errnote=expected_errnote)

# Generated at 2022-06-14 18:05:29.733341
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import YoutubeDL

    import shutil
    from tempfile import mkdtemp

    from .utils import OnDemandPopen

    old_popen = OnDemandPopen.__init__
    OnDemandPopen.__init__ = lambda self, *args, **kwargs: None

    with YoutubeDL(params={'logger': 'test'}) as ydl:
        tempdir = mkdtemp()

# Generated at 2022-06-14 18:05:42.028573
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import YoutubeDL
    from .extractor.youtube import YoutubeIE
    from .extractor.common import InfoExtractor
    import os
    import tempfile
    import time

    class DummyPostProcessor(PostProcessor):
        def __init__(self, downloader=None, ie=None):
            PostProcessor.__init__(self, downloader)
            self._ie = ie

        def run(self, info):
            if self._ie:
                ie = self._ie
            else:
                ie = info['extractor']
            ie_key = ie.IE_NAME
            test_output_dir = os.path.join(tempfile.gettempdir(), 'youtubedl_test_%s' % ie_key)
            if not os.path.exists(test_output_dir):
                os

# Generated at 2022-06-14 18:05:48.991551
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..PostProcessor import PostProcessor
    with open('test.txt', 'w') as f:
        f.write('test')
    ydl = YoutubeDL()
    pp = PostProcessor(ydl)
    # The file is then deleted
    pp.try_utime('test.txt', 2, 3, 'testing the truthing of truth')
    print('Testing the PostProcessor.try_utime() method ...')
    if os.path.exists('test.txt'):
        print('Error: the file was not deleted properly')

# Generated at 2022-06-14 18:05:57.377581
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def fake_os_utime(path, time):
        if os.path.basename(path) != "ok.file":
            raise ValueError("test: I can't change time of %s" % path)
    import sys
    import __builtin__
    old_os_utime = os.utime
    old_report_warning = PostProcessor._downloader.report_warning
    old_stderr = sys.stderr
    sys.stderr = open("/dev/null", "w")
    os.utime = fake_os_utime
    PostProcessor._downloader.report_warning = lambda msg: sys.stderr.write("test: warning: %s\n" % msg)
    # No exception
    PostProcessor().try_utime("ok.file", None, None)
   

# Generated at 2022-06-14 18:06:05.507749
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange
    from .common import PostProcessorTestCase
    from .test_downloader import (
        MockYDL, MockFileDownloaderHandler,
        match_str, FakeHttpServer,
        override_getaddrinfo,
    )

    class MockInfoExtractor(InfoExtractor):
        IE_NAME = 'Mock'

    class MockPostProcessor(PostProcessor):
        pass

    class TestDownloader(FileDownloader):
        def __init__(self):
            FileDownloader.__init__(self, MockYDL())
            self.add_info_extractor(MockInfoExtractor())
            self.add_post_processor(MockPostProcessor())


# Generated at 2022-06-14 18:06:34.743551
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Unit test for method try_utime of class PostProcessor."""

    try:
        os.utime('test', (0, 0))
    except:
        raise Exception('test_PostProcessor_try_utime failed. '
                        'os.utime() is not implemented or works incorrectly')

# Generated at 2022-06-14 18:06:45.308902
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test the utime logic of the class PostProcessor using a temporary directory.
    """
    import errno
    import stat
    import tempfile

    tmpdir = tempfile.mkdtemp()
    dummy_file_name = 'dummy'
    dummy_file_path = os.path.join(tmpdir, dummy_file_name)
    dummy_file_handle = open(dummy_file_path, 'w')
    dummy_file_handle.close()

    pp = PostProcessor(None)
    original_atime = os.lstat(dummy_file_path).st_atime
    original_mtime = os.stat(dummy_file_path).st_mtime
    pp.try_utime(dummy_file_path, original_atime + 1, original_mtime + 1)

# Generated at 2022-06-14 18:06:51.160075
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader(object):
        def report_warning(self, *args):
            print(args[0])

    pp = PostProcessor(downloader=FakeDownloader())

    class FakeFile(object):
        def __init__(self, mtime):
            self.mtime = mtime

        def utime(self, access, modification):
            pass
    pp.try_utime(FakeFile(mtime=1), atime=0, mtime=0)



# Generated at 2022-06-14 18:07:02.091206
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil
    dirpath = tempfile.mkdtemp('youtube-dl.test.PostProcessor.try_utime')
    try:
        path = dirpath + os.sep + 'test'
        open(path, 'w').close()
        pp = PostProcessor(downloader=None)
        mtime = time.time()
        pp.try_utime(path, mtime, mtime, errnote='ignore')
        assert abs(os.path.getmtime(path) - time.time()) < 1  # within 1 sec
    finally:
        shutil.rmtree(dirpath)

# Generated at 2022-06-14 18:07:02.702188
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:07:05.591498
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    pp = PostProcessor(ydl)
    pp.try_utime('test.txt', 1, 2)
    pp.try_utime('test.txt', None, None)

# Generated at 2022-06-14 18:07:15.863413
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import datetime
    import time
    import stat

    (file_descriptor, file_path) = tempfile.mkstemp(prefix="ytdl-test_")
    os.close(file_descriptor)
    # The date format for the touch command is:
    # [[CC]YY]MMDDhhmm[.ss]
    # This format is also valid for the GNU touch utility
    # To respect this format and not having a year with a value
    # outside of [19,99] we need to pass a year with a value inside
    # this range.
    now_time = datetime.datetime.now()
    now_time_delta = datetime.timedelta(days=21)
    now_time -= now_time_delta

# Generated at 2022-06-14 18:07:24.196539
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mktemp
    from shutil import rmtree
    from time import time

    fname = mktemp()
    try:
        open(fname, 'wb').close()
        pp = PostProcessor(None)
        t = time()
        pp.try_utime(fname, t, t)
        assert os.stat(fname).st_mtime == os.stat(fname).st_atime == t
    finally:
        rmtree(os.path.dirname(fname), ignore_errors=True)

# Generated at 2022-06-14 18:07:35.268655
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .test_downloads import MockYDL
    from .extractor.common import InfoExtractor
    from .compat import str

    class MockInfoExtractor(InfoExtractor):
        IE_NAME = 'mock'

        def __init__(self, downloader=None):
            super(MockInfoExtractor, self).__init__(downloader)

        def _real_extract(self, url):
            return {'id': '1234', 'ext': 'mp4'}

    class MockPostProcessor(PostProcessor):
        pass

    # Create a mock downloader with a proper _real_initialize

# Generated at 2022-06-14 18:07:43.636749
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader
    from ..extractor import YoutubeIE
    import os
    import time

    test_path = 'test_PostProcessor_try_utime.tmp'
    touch_cmd = 'touch %s' % test_path
    if os.name == 'nt':
        touch_cmd = 'echo|set /p="">%s' % test_path

    downloader = FileDownloader(params={'outtmpl': test_path})
    downloader.add_info_extractor(YoutubeIE())
    downloader.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    t1 = os.stat(encodeFilename(test_path)).st_atime
    time.sleep(1)
    pp = PostProcessor(downloader)
   