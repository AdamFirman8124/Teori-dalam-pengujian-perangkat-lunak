

# Generated at 2022-06-14 17:58:37.082090
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader(object):
        def __init__(self):
            self.count = 0

        def report_warning(self, errnote):
            self.count += 1

    post_processor = PostProcessor()
    post_processor._downloader = MockDownloader()
    path = 'aaa'  # file that doesn't exist, if exist, test will change the time of file
    atime = mtime = 1

    # normal
    post_processor.try_utime(path, atime, mtime)
    assert post_processor._downloader.count == 0

    # abnormal
    path = ''
    post_processor.try_utime(path, atime, mtime)
    assert post_processor._downloader.count == 1

# Generated at 2022-06-14 17:58:44.201287
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            self.err_note = []
            self.utime = []

        def report_warning(self, errnote):
            self.err_note.append(errnote)

        def try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
            self.utime.append((path, atime, mtime, errnote))
            super(TestPostProcessor, self).try_utime(path, atime, mtime, errnote)

    p = TestPostProcessor()
    p.try_utime("1", 1, 2, 'warning')
    p.try_utime("2", 3, 4, 'warning')
    assert p.utime[0]

# Generated at 2022-06-14 17:58:48.345545
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from ..YoutubeDL import YoutubeDL
    from .common import FileDownloader
    class TestPostProcessor(PostProcessor):
        def run(self, info):
            self.try_utime(info['filepath'], 100, 100)
            return [], info

    # Initialize and run downloader
    downloader = Downloader(ydl=YoutubeDL({}))
    downloader.add_info_extractor(FileDownloader({'outtmpl': '%(id)s.%(ext)s'}))
    downloader.add_post_processor(TestPostProcessor())
    urls = ['http://127.0.0.1:9127/%s.%s' % (i, 'txt') for i in range(0, 10)]

# Generated at 2022-06-14 17:58:58.293377
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile
    from time import sleep

    with NamedTemporaryFile(delete=False) as f:
        name = f.name


# Generated at 2022-06-14 17:59:08.438572
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import subprocess
    import tempfile

    TEST_FILE = os.path.join(tempfile.gettempdir(), 'test_file')
    subprocess.check_call('touch ' + TEST_FILE, shell=True)

    pp = PostProcessor()

    # test for correct arguments
    assert os.stat(TEST_FILE).st_mtime == os.stat(TEST_FILE).st_atime
    pp.try_utime(TEST_FILE, 0, 1)
    assert os.stat(TEST_FILE).st_mtime == 1
    assert os.stat(TEST_FILE).st_atime == 0

    # test for wrong arguments
    pp.try_utime(TEST_FILE, -1, -1)
    assert os.stat(TEST_FILE).st_mtime

# Generated at 2022-06-14 17:59:15.153789
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader(object):
        def __init__(self):
            self.warning_count = 0
            self.warning_templates = []

        def report_warning(self, message):
            self.warning_count += 1
            self.warning_templates.append(message)

    class MockPostProcessor(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)

        def run(self, information):
            return self.try_utime(information, 0, 0)

    downloader = MockDownloader()
    post_processor = MockPostProcessor(downloader)

    information = {'filepath': os.path.join("test", "file", "path")}
    post_processor.run(information)

    assert downloader.warning_count

# Generated at 2022-06-14 17:59:25.421967
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    import time
    import os
    import shutil
    import tempfile

    tempdir = tempfile.mkdtemp(prefix="test-youtubedl-")

# Generated at 2022-06-14 17:59:33.481775
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    test_PP = PostProcessor()
    path = '/tmp/foo'
    try:
        os.mknod(encodeFilename(path))
    except:
        raise

    atime = 0.0
    mtime = 0.0
    errnote = 'some error'
    test_PP.try_utime(path, atime, mtime, errnote)
    # TODO: test if try_utime actually does anything

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 17:59:45.198652
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import stat
    import os.path
    import tempfile
    import shutil

    pp = PostProcessor(None)

    # Create test file
    dir = tempfile.mkdtemp()
    fd, fpath = tempfile.mkstemp(dir=dir)
    f = os.fdopen(fd, 'w')
    f.write('X' * 10000)
    f.close()

    # Get the file stat
    stat_info = os.stat(fpath)
    atime = stat_info.st_atime
    mtime = stat_info.st_mtime

    # Try to update utime
    pp.try_utime(fpath, atime + 10, mtime + 10)

    # Verify that the file utime has been updated

# Generated at 2022-06-14 17:59:53.401331
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def utimeFail(path, atime, mtime):
        return False
    import sys
    import io
    import unittest
    import urllib
    import shutil

    class TestPostProcessor(PostProcessor):
        def run(self, info):
            out_file = info['filepath']
            self.try_utime(out_file,0,0)
            return None, info

    class _FileLike(object):
        def __init__(self, buffer):
            self.buffer = buffer
            self.pos = 0

        def read(self, bs):
            to_read = min(bs, len(self.buffer) - self.pos)
            read = self.buffer[self.pos:self.pos + to_read]
            self.pos += to_read
            return read


# Generated at 2022-06-14 18:00:03.480694
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    import datetime
    import time
    import os
    # write a new file and get file creation time
    f = open('foo.txt', 'w')
    f.write('bar')
    f.close()
    ctime = os.path.getctime('foo.txt')
    # set a time in the past
    then = datetime.datetime(2000, 1, 1)
    # the delta between the past and now
    delta = datetime.datetime.now() - then
    # extract the seconds from the delta
    seconds = delta.days * 24 * 3600 + delta.seconds
    # set the file modification time to the past
    pp.try_utime('foo.txt', seconds, seconds)
    # set the file modification time to the present

# Generated at 2022-06-14 18:00:12.568855
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil
    class MockDownloader(object):

        def report_warning(self, warning_message):
            self.warning_message = warning_message

    downloader = MockDownloader()

    pp = PostProcessor(downloader)
    tempdir = tempfile.mkdtemp(prefix='youtubedl-test-utime')
    tempf = os.path.join(tempdir, 'test_utime_file')
    with open(tempf, 'w') as f:
        f.write('test_utime')

    now_time = time.time()
    time.sleep(1)
    # Modify the time of the file so that we can test pp.try_utime() is working
    os.utime(tempf, None)

    pp.try_utime

# Generated at 2022-06-14 18:00:25.039746
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time

    # Create a PostProcessor with a fake downloader
    class Downloader:
        def report_warning(self, msg):
            self.report_warning_msg = msg

    pp = PostProcessor(downloader=Downloader())

    # Prepare a file with a timestamp in the past
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_path = temp_file.name
    temp_file.write('foobar')
    temp_file.close() # close file to set the mtime
    t_ref = time.time() - 1000
    os.utime(temp_file_path, (t_ref, t_ref))

    # Update time of the file
    t = int(time.time())

# Generated at 2022-06-14 18:00:34.804763
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil, tempfile
    import os, os.path

    file_path = os.path.abspath(__file__)
    _, file_name = os.path.split(file_path)
    temp_dir = tempfile.mkdtemp(prefix='youtube-dl.', suffix='.test')
    test_file_path = os.path.join(temp_dir, file_name)
    shutil.copy(file_path, test_file_path)

    p = PostProcessor(None)
    p.try_utime(test_file_path, 0, 0, '')

    os.utime(test_file_path, (0, 0))

    shutil.rmtree(temp_dir)

# Generated at 2022-06-14 18:00:45.252713
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """ Test try_utime method of class PostProcessor """
    from ..YoutubeDL import YoutubeDL
    from .test_utils import FakeDownloader
    ydl = YoutubeDL(params={})
    pp = PostProcessor(FakeDownloader(ydl, {
        'outtmpl': '%(id)s.%(ext)s',
        'postprocessor_args': ['--format', 'mp3']
    }))

# Generated at 2022-06-14 18:00:54.504837
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    from .pyquery_compat import PyQuery
    from .external.compat import (
        compat_str,
        compat_urllib_error,
    )
    from .compat import (
        compat_urlparse,
        compat_shlex_split,
        compat_os_name,
        compat_struct_pack,
        compat_winsound,
    )
    from .downloader import (
        HttpFD,
        YoutubeDL,
    )
    from .utils import (
        encodeFilename,
        encodeArgument,
        error_to_compat_str,
    )
    from .compat import (
        compat_shutil_which,
        compat_which,
    )

# Generated at 2022-06-14 18:01:06.908525
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import platform
    if platform.system() == 'Windows':
        import pytest
        pytest.skip("Not available on Windows")
    import tempfile, time
    from ..postprocessor import PostProcessor, encodeFilename
    from ..utils import DateRange

    def build_date_range(delta=None, seconds=0, minutes=0, hours=0, days=0, weeks=0, months=0, years=0):
        from datetime import datetime, timedelta, tzinfo

# Generated at 2022-06-14 18:01:09.292437
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # TODO: add tests

    pass

# Generated at 2022-06-14 18:01:20.410547
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import common as test_common

    def check_utime(path, atime, mtime):
        stat = os.stat(encodeFilename(path))
        return (stat.st_atime == atime), (stat.st_mtime == mtime)

    pp = PostProcessor(test_common.FakeYDL())
    pp.try_utime('/test.mp4', 1000, 2000)
    assert check_utime('/test.mp4', 1000, 2000)
    pp.try_utime('/test.mp4', 404, 1001)
    assert check_utime('/test.mp4', 404, 1001)
    pp.try_utime('/test.mp4', 500, 600)
    assert check_utime('/test.mp4', 500, 600)

# Generated at 2022-06-14 18:01:32.500988
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import mock
    import sys
    import unittest

    class TestPostProcessor(PostProcessor):
        def run(self, information):
            upload_date = information.get('upload_date')
            test_file = os.path.join(self._downloader.ydl.tmpfilename, 'test')
            with open(test_file, 'w'):
                pass
            self.try_utime(test_file, int(upload_date), int(upload_date))
        
            return [], information

    class TestDownloader(object):
        def __init__(self):
            self.params = {}
            self.ydl = mock.Mock()
            self.ydl.tmpfilename = '/tmp'
            self.report_warning = mock.Mock()

# Generated at 2022-06-14 18:01:38.911058
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockPostProcessor(PostProcessor):
        def __init__(self):
            super(MockPostProcessor, self).__init__()
            self.report_warning_called = False

    post_processor = MockPostProcessor()
    post_processor.set_downloader(None)
    post_processor.try_utime('filepath', 123, 456)
    assert not post_processor.report_warning_called

# Generated at 2022-06-14 18:01:47.234629
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Create a file, then create a PostProcessor object, and finally call
    the method try_utime of the created object and check the result.
    """
    import platform
    import datetime
    import time
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix='youtubedownloader-test_PostProcessor_try_utime-')
    if platform.system() == 'Windows':
        tmpfile = os.path.join(tmpdir, '_test.tmp')
    else:
        tmpfile = os.path.join(tmpdir, '.test.tmp')
    f = open(tmpfile, 'w')
    f.close()
    s = os.stat(tmpfile)
    pp = PostProcessor(None)

# Generated at 2022-06-14 18:01:58.686299
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import FakeDict
    from ..downloader.common import FileDownloader
    from ..utils import DateRange
    from .XAttrMetadataPP import XAttrMetadataPP

    fd = FileDownloader(FakeDict({'noprogress': True,
                                  'quiet': True,
                                  'simulate': True,
                                  'forcetitle': True,
                                  'forceduration': True,
                                  'forcetotalbytes': True,
                                  'forcetotalbitrate': True,
                                  'forcedate': True,
                                  'dump_single_json': True,
                                  'outtmpl': '%(id)s.%(ext)s'}))

    fd._ies = []
    fd._pps = [XAttrMetadataPP()]

   

# Generated at 2022-06-14 18:02:08.666386
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from sys import version_info
    from ..YoutubeDL import YoutubeDL
    from .common import (
        make_temp_dir,
        make_temp_file,
        get_temp_file_path,
        make_temp_path,
    )

    def open_file(path, *args, **kwargs):
        return open(encodeFilename(path), *args, **kwargs)

    def close_file(fileobj):
        return fileobj.close()

    fd, tmp_file = make_temp_file(prefix='YDL-TEST', suffix='.tmp')
    close_file(fd)
    with make_temp_dir(prefix='YDL-TEST') as temp_dir:
        pp = PostProcessor(YoutubeDL())
        # utime(2) only takes seconds

# Generated at 2022-06-14 18:02:19.017482
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # mock downloader
    downloader = type("test", (object,), {
        "params": {
            "no_overwrites":False,
            "continuedl":False,
            "nooverwrites":False,
            "forcetitle":False,
            "forcethumbnail":False,
            "forcedescription":False
        }
    })

    # mock os
    os = type("test", (object,), {
        "utime": lambda x,y: None
    })

    # mock os.path
    os.path = type("test", (object,), {
        "exists": lambda x: True,
        "getsize": lambda x: 10
    })


# Generated at 2022-06-14 18:02:31.529221
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile

    downloader = object()
    pp = PostProcessor(downloader)
    assert pp._downloader == downloader

    # Create temporary directory and file
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, 'test_file')
    with open(temp_file, 'w') as f:
        f.write('testing')
    temp_file_atime = os.stat(temp_file).st_atime
    temp_file_mtime = os.stat(temp_file).st_mtime

    # Test if pp.try_utime() updates the file times
    pp.try_utime(temp_file, temp_file_atime, temp_file_mtime+1)

# Generated at 2022-06-14 18:02:40.647743
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time

    tpath = tempfile.mkdtemp()
    ppath = os.path.join(tpath, 'ff.mp3')
    with open(ppath, 'w') as f:
        f.write('a')
    pp = PostProcessor(None)
    atime = time.time()-1000
    mtime = time.time()-1000
    pp.try_utime(ppath, atime, mtime)
    os.remove(ppath)
    os.rmdir(tpath)

# Generated at 2022-06-14 18:02:48.101301
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os.path
    import shutil
    import tempfile
    import time
    from .test import get_testdata_files_dir

    # create test file for next functions
    tmpd = tempfile.mkdtemp()
    tmpf = os.path.join(tmpd, 'testfile')
    shutil.copy2(os.path.join(get_testdata_files_dir(), 'test.mp3'), tmpf)

    def get_utime(filename):
        """Return a tuple of atime and mtime of a file"""
        return os.stat(filename).st_atime, os.stat(filename).st_mtime

    def set_utime(filename, atime=None, mtime=None):
        """Set atime and mtime of a file"""
        if atime is None:
            atime

# Generated at 2022-06-14 18:02:56.472510
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try_utime_path = os.path.join(os.path.dirname(__file__), 'PostProcessor')
    if not os.path.exists(try_utime_path):
        os.mkdir(try_utime_path)
    open(os.path.join(try_utime_path, 'try_utime_test_1'), 'w').close()
    if not os.path.exists(os.path.join(try_utime_path, 'try_utime_test_2')):
        raise AssertionError('Cannot create file for testing utime')

# Generated at 2022-06-14 18:03:06.082384
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Mock an object of class Downloader and a method report_warning
    class MockDownloader(object):
        def report_warning(self, note):
            print(note)

    import os
    import tempfile
    import hashlib

    # Get a temporary directory with a temporary file
    tmp_dir = tempfile.mkdtemp()
    tmp_file = tempfile.NamedTemporaryFile(dir=tmp_dir, delete=False)
    tmp_file.write(os.urandom(10))
    tmp_file.close()

    # Create a PostProcessor object with the mock object
    pp = PostProcessor(MockDownloader())

    # Get utime of the file before and after trying to update
    before_utime = os.stat(tmp_file.name).st_mtime

# Generated at 2022-06-14 18:03:24.270958
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import unittest
    from tempfile import mkstemp
    from ..utils import DateRange

    # Create a temporary file to test
    temp_fd, temp_file = mkstemp(prefix='youtube-dl_test_PostProcessor_try_utime_')
    os.close(temp_fd)

    # Create a PostProcessor object with a mocked downloader
    class DownloaderMock(object):
        def report_warning(self, msg):
            self.warning_msg = msg

    pp = PostProcessor(downloader=DownloaderMock())
    pp._downloader.params['writedescription'] = False

    # Test time conversion functions
    for time_tuple in [(-1, 0, 0), (2038, 1, 1), (2037, 1, 2)]:
        time_tuple

# Generated at 2022-06-14 18:03:36.029594
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from types import MethodType

    # TODO: Create a real unit test
    # Create a dummy file
    file = open('a_file', 'w')
    file.close()
    # Current utime of the dummy file
    utime = os.stat('a_file').st_atime
    # Create a dummy _downloader and PostProcessor
    _downloader = object()
    pp = PostProcessor(_downloader)
    # Set report_warning as a method of pp
    pp.report_warning = MethodType(lambda self, a: print(a), pp)
    # Try to change the utime of the file
    # This should fail with a warning
    pp.try_utime('a_file', utime - 60, utime - 60)
    # Remove the dummy file
    os.remove('a_file')
   

# Generated at 2022-06-14 18:03:46.858364
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def __init__(self):
            PostProcessor.__init__(self)

    test_pp = TestPostProcessor()
    import os.path
    import time
    try:
        os.remove("./TEST_FILE")
    except:
        pass
    f = open('./TEST_FILE', 'w')
    f.close()
    atime_1 = time.time()
    time.sleep(1)
    test_pp.try_utime('./TEST_FILE', atime_1, time.time())
    atime_2, _ = os.path.getatime('./TEST_FILE'), os.path.getmtime('./TEST_FILE')

# Generated at 2022-06-14 18:03:51.857830
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .YoutubeDL import YoutubeDL
    from .FileDownloader import FileDownloader
    downloader = FileDownloader(YoutubeDL({'outtmpl': '%(id)s.%(ext)s'}))
    post_processor = PostProcessor(downloader)
    post_processor.try_utime('', 1, 1)

# Generated at 2022-06-14 18:04:03.022021
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import shutil
    import time
    import os

    downloader = None
    pp = PostProcessor(downloader)

    tmpdir = tempfile.mkdtemp(prefix='yt-downloader-test_')


# Generated at 2022-06-14 18:04:13.762674
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MyDownloader(object):
        def report_warning(self, msg):
            print(msg)

    class PostProcessorNoException(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)

        def run(self, info):
            self.try_utime(os.getcwd() + '/abc', 0, 0)
            return [], info

    class PostProcessorWithException(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)

        def run(self, info):
            self.try_utime(os.getcwd() + '/abc', 0, 0, 'error note')
            return [], info

    PostProcessorNoException(MyDownloader()).run

# Generated at 2022-06-14 18:04:15.888110
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime("testfile.txt", 0, 0)

# Generated at 2022-06-14 18:04:24.851982
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time, tempfile, random
    import shutil, os # import needed for setup_tempdir_for_utime_test

    from ..downloader import Downloader
    from ..postprocessor import PostProcessor

    def setup_tempdir_for_utime_test(self, dir_name_prefix):
        self.tempdir_for_utime_test = tempfile.mkdtemp(prefix=dir_name_prefix)
        self.addCleanup(shutil.rmtree, self.tempdir_for_utime_test)
        return self.tempdir_for_utime_test

    def create_file_with_timestamp(self, file_name, timestamp):
        filepath = os.path.join(self.tempdir_for_utime_test, file_name)

# Generated at 2022-06-14 18:04:33.748853
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import utils
    import postprocessor
    import fileutils

    p = postprocessor.PostProcessor(downloader=utils.FakeYDL())
    with fileutils.temp_dir() as tmp:
        test_file = os.path.join(tmp, 'test.txt')
        with open(test_file, 'w') as f:
            pass
        stat = os.stat(test_file)
        orig_atime = stat.st_atime
        orig_mtime = stat.st_mtime
        p.try_utime(test_file, orig_atime - 1000, orig_mtime - 1000)
        stat = os.stat(test_file)
        assert stat.st_atime == orig_atime - 1000
        assert stat.st_mtime == orig_mtime - 1000
        # Restore to original

# Generated at 2022-06-14 18:04:45.116102
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import YoutubeIE
    from ..downloader.common import FileDownloader

    ydl = FileDownloader({'writedescription': True,
                          'usetitle': True,
                          'continuedl': True,
                          'nooverwrites': True,
                          'simulate': True,
                          'quiet': True,
                          'outtmpl': '%(id)s%(ext)s'})
    pp = PostProcessor(ydl)
    ie = YoutubeIE(ydl)
    ie.extract('http://www.youtube.com/watch?v=BaW_jenozKc')
    pp.run(ie._downloader.tmpfilename)
    assert ie._downloader._screen_file_title == 'youtube-dl test video \'\'\'"'

# Generated at 2022-06-14 18:04:56.298192
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPP(PostProcessor):
        def test_try_utime(self):
            path = os.path.join('a dir', 'b.file')
            atime = 1.1
            mtime = 2.2
            errnote = 'note'
            self.try_utime(path, atime, mtime, errnote)
    pp = TestPP()
    pp.try_utime = lambda *args: PostProcessor.try_utime(pp, *args)
    pp._downloader = {'report_warning': lambda x: x}
    pp.test_try_utime()

# Generated at 2022-06-14 18:05:07.699274
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyPostProcessor(PostProcessor):
        def run(self, information):
            return [], information
    pp = DummyPostProcessor()

    class DummyDownloader(object):
        def __init__(self):
            self.params = {}
            self.warned = False

        def report_warning(self, note):
            self.warned = True

    dl = DummyDownloader()
    pp.set_downloader(dl)

    # test absence of "utime" attribute
    information={}
    pp.try_utime('', 0, 0, 'error')
    assert dl.warned is False

    # test presence of "utime" and absence of "mtime" attribute
    dl.warned = False
    information={'utime':0}
    pp.try_utime

# Generated at 2022-06-14 18:05:18.662281
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    os.remove('.PostProcessor_test_try_utime') if os.path.exists('.PostProcessor_test_try_utime') else None
    if not os.path.exists('.PostProcessor_test_try_utime'):
        with open('.PostProcessor_test_try_utime', 'w'): pass

# Generated at 2022-06-14 18:05:29.308786
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import os
    import stat
    import tempfile
    import time
    import shutil

    if sys.version_info < (2, 6):
        import unittest2 as unittest
    else:
        import unittest
    from ..downloader import FileDownloader

    @unittest.skipUnless(sys.platform.startswith('linux'), 'Test for Linux only')
    @unittest.skipUnless(os.geteuid() == 0, 'Test for root user only')
    class TestPostProcessor_try_utime(unittest.TestCase):
        def setUp(self):
            self.__test_file = None
            self.__test_file_path = None
            self.__temp_dir = tempfile.mkdtemp()

            # make test file
            fd,

# Generated at 2022-06-14 18:05:37.856628
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    def check_try_utime(value, expected):
        info = {'title': 'test'}
        pp = PostProcessor(None)
        (deletable, info) = pp.run(info)
        assert info == expected

    check_try_utime(None, {'title': 'test'})
    check_try_utime(1, {'title': 'test', 'server_time': 1})
    check_try_utime(['1', '2'], {'title': 'test', 'server_time': ['1', '2']})

# Generated at 2022-06-14 18:05:46.983538
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import shutil
    import tempfile

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create file
    filename = 'foo'
    filepath = os.path.join(tmpdir, filename)
    file = open(encodeFilename(filepath), 'w')
    file.write('test')
    file.close()

    # Check if utime is called successfully
    pp = PostProcessor(None)
    atime = 0
    mtime = 0
    pp.try_utime(filepath, atime, mtime)

    # Clean up
    shutil.rmtree(tmpdir)

    return

# Generated at 2022-06-14 18:05:53.029999
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    is_invalid_utime = False
    try:
        class P(PostProcessor):
            def run(self, info):
                self.try_utime(info.get('filepath'))
                return [], info
        P().run({'filepath': 1})
    except TypeError as e:
        if str(e) == 'utime() argument 1 must be string, not int':
            is_invalid_utime = True
    assert is_invalid_utime

# Generated at 2022-06-14 18:06:02.800684
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Create a dummy PostProcessor instance
    pp = PostProcessor()

    # Create some files
    files = ['foo', 'bar']
    for f in files:
        open(encodeFilename(f), 'w').close()

    # Set their times to a particular time-stamp
    time_stamp = 12345678
    for f in files:
        pp.try_utime(f, time_stamp, time_stamp)
    for f in files:
        assert os.stat(encodeFilename(f)).st_atime == time_stamp
        assert os.stat(encodeFilename(f)).st_mtime == time_stamp

    # Set the time stamp of one of the files using the command line
    f = files[-1]
    new_time_stamp = 98765432

# Generated at 2022-06-14 18:06:12.096938
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import time
    import subprocess
    import tempfile
    import shutil
    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)
    # Create temporary directory and files
    tmp_dir = tempfile.mkdtemp()
    tmp_file = os.path.join(tmp_dir, 'foo') # filename
    tmp_new = os.path.join(tmp_dir, 'bar') # new filename
    touch(tmp_file) # Create a empty file
    # Backup current files
    old_file = os.path.join(tmp_dir, 'old_foo') # backup file
    old_new = os.path.join(tmp_dir, 'old_bar') # backup file
    shutil.copyfile(tmp_file, old_file)


# Generated at 2022-06-14 18:06:23.446260
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakePP(PostProcessor):
        def __init__(self):
            self.call_count = 0

        def try_utime(self, path, atime, mtime, errnote):
            self.call_count += 1
            self.path = path
            self.atime = atime
            self.mtime = mtime
            self.errnote = errnote
            raise Exception

    fakepp = FakePP()
    try:
        fakepp.try_utime('test_path', 123, 456, "test_errnote")
    except Exception:
        pass

    assert fakepp.call_count == 1
    assert fakepp.path == 'test_path'
    assert fakepp.atime == 123
    assert fakepp.mtime == 456

# Generated at 2022-06-14 18:06:44.243807
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime('.', 0, 0)
    pp.try_utime(__file__, 0, 0)
    import tempfile
    tmpfile = tempfile.NamedTemporaryFile(delete=False)
    os.remove(tmpfile.name)
    pp.try_utime(tmpfile.name, 0, 0)
    # Check that file was created
    os.path.exists(tmpfile.name)
    tmpfile.close()

# Generated at 2022-06-14 18:06:55.516874
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import sanitize_open
    from tempfile import mkdtemp
    from shutil import rmtree

    class DummyPostProcessor(PostProcessor):
        def run(self, information):
            return [], information

    tmpdir = mkdtemp()


# Generated at 2022-06-14 18:07:05.419261
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import FakeYDL
    from .extractor.common import InfoExtractor
    from .downloader.common import FileDownloader

    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            PostProcessor.__init__(self, downloader)

    class FakeIE(InfoExtractor):
        def __init__(self, downloader=None):
            InfoExtractor.__init__(self, downloader)

    class FakeFD(FileDownloader):
        def __init__(self, ydl, params):
            FileDownloader.__init__(self, ydl, params)


# Generated at 2022-06-14 18:07:12.293852
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import shutil
    import time
    import unittest

    from ..utils import is_outdated_version, shell_quote
    from .common import PostProcessorTestCase

    def noop(param):
        return param

    def noproc(param):
        """Proc that does nothing
        """
        return (param, None)

    class PostProcessorTryUtime(PostProcessorTestCase):
        def test_PostProcessor_try_utime(self):
            # Ensure the time jumps at least for one second
            if time.time() - self._start_time < 1:
                time.sleep(1)
            # tempdir is a file.
            self.test_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:07:16.765573
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FakeYDL
    from tempfile import NamedTemporaryFile, mkdtemp
    import os
    import time
    import shutil
    import platform

    # Creating the temp file
    temp_file = NamedTemporaryFile(delete=False)
    temp_file.close()
    # Creating the temp dir
    temp_dir = mkdtemp()
    # Adding the temp dir to the path, so we can create non empty directory
    temp_file = os.path.join(temp_dir, temp_file.name)

    # Create the fake downloader, with the tempfile as filename
    fake_dl = FakeYDL()
    fake_dl.params['outtmpl'] = temp_file

    PP = PostProcessor(fake_dl)

    # get the times of our test file

# Generated at 2022-06-14 18:07:18.989311
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractor
    from . import FFmpegExtracto

# Generated at 2022-06-14 18:07:25.871748
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .common import FakeYDL
    from .extractor import gen_extractor

    ydl = FakeYDL()
    ydl.params['ffmpeg_location'] = 'ffmpeg'

    # Test if PostProcessor is able to ignore errors
    # and call report_warning()
    # when updating utime of file
    info = {'id': 'id_'}
    ext = gen_extractor(
        'audio', ydl, info,
        ie='http://ccmixter.org/content/DoKashiteru/DoKashiteru_-_you_(naive_melody).mp3',
        audioformat='mp3',
        _type='url',)
    ex = ext()
    for pp in ex.post_processors:
        pp.set_downloader(ydl)

# Generated at 2022-06-14 18:07:27.077372
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:07:37.027124
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    from time import time, sleep
    test_name = os.path.join(tempfile.gettempdir(), 'test_utime.tmp')
    file(test_name, 'w').close() # Must be regular file
    old_time = time()
    sleep(1)
    new_time = time()
    pp = PostProcessor(None)
    pp.try_utime(test_name, new_time, new_time)
    assert(os.path.getmtime(test_name) == int(new_time))
    assert(os.path.getatime(test_name) == int(new_time))
    pp.try_utime(test_name, old_time, new_time)

# Generated at 2022-06-14 18:07:46.466390
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import filecmp
    import time
    import sys

    # Create a test file with current time
    with open('test_file', 'wb') as outf:
        outf.write(b'I am a test file for youtube-dl')
    # Post-process the test file
    import compat_os_path
    from .common import FileDownloader

    pp = PostProcessor(FileDownloader({}))
    pp.try_utime(
        'test_file', time.time() + 7200, time.time() + 7200,
        errnote='Cannot set utime of file')
    # Check if file has been correctly post-processed
    if not filecmp.cmp('test_file', 'test_file'):
        sys.exit(1)

# Generated at 2022-06-14 18:08:27.125620
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from tempfile import mkstemp
    import shutil
    import os
    import time

    # Creating a test file
    fd, original_path = mkstemp()
    os.close(fd)
    original_atime = int(time.time())
    original_mtime = original_atime
    time.sleep(1)  # Hopefully this should be enough to guarantee that the next atime and mtime values are different

    # Creating a YoutubeDL object
    ydl = YoutubeDL({'simulate': True, 'quiet': True, 'writedescription': True, 'writeinfojson': True, 'noplaylist': True})

    # Creating a post processor
    pp = PostProcessor(ydl)

    # Getting the full filename of the file
    full_filename = ydl.prepare