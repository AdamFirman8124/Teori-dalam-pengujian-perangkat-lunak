

# Generated at 2022-06-14 17:58:35.298469
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import shutil
    from ..extractor.common import InfoExtractor

    tempdir = tempfile.mkdtemp()
    infopath = os.path.join(tempdir, 'info.json')


# Generated at 2022-06-14 17:58:43.217278
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import sys
    if sys.version_info[0] == 2:
        from tempfile import mkstemp
    else:
        from tempfile import TemporaryFile
        mkstemp = TemporaryFile
    from .common import FileDownloader
    from .extractor import gen_extractor

    t1 = time.time() - 60
    file_desc, file_path = mkstemp(prefix='youtubedl_test_utime')
    file_handle = os.fdopen(file_desc, 'wb')
    file_handle.write(b'hello')
    file_handle.close()

    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            PostProcessor.__init__(self, downloader)
            self.test_result = True

# Generated at 2022-06-14 17:58:48.618833
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    PostProcessor().try_utime(
        'PostProcessorTest.test_try_utime.txt',
        1244428453, 1244981253,
        errnote='PostProcessorTest should use custom errnote'
    )
    try:
        PostProcessor().try_utime(
            'PostProcessorTest.test_try_utime.non-existent.txt',
            1244428453, 1244981253,
            errnote='PostProcessorTest should use custom errnote'
        )
        raise AssertionError('Expected OSError')
    except OSError:
        pass
    # Restore the state on disk
    os.remove('PostProcessorTest.test_try_utime.txt')

# Generated at 2022-06-14 17:58:57.449105
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time

    path = 'test_utime.txt'
    with open(path, 'wb') as f:
        f.write(b'test')
    try:
        os.utime(path, (time.time() - 500, time.time() - 500))
        pp = PostProcessor(None)
        pp.try_utime(path, time.time() + 500, time.time() + 500)
    finally:
        os.remove(path)

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 17:59:07.169657
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import YoutubeDL
    dl = YoutubeDL()
    try:
        os.unlink('test_file')
    except OSError:
        pass
    f = open('test_file', 'w')
    f.write('test')
    f.close()
    os.utime('test_file', (2, 3))
    import time
    pp = PostProcessor(dl)
    pp.try_utime('test_file', 1, 2)
    f = os.stat('test_file')
    assert f.st_atime == 1
    assert f.st_mtime == 2

    pp.try_utime('no_file', 1, 2, 'Nothing wrong with that')
    f = os.stat('test_file')
    assert f.st_atime == 1

# Generated at 2022-06-14 17:59:19.117652
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from .common import FilePostProcessor
    from .xattrpp import XAttrMetadataPP

    # Create an instance of PostProcessor
    pp = XAttrMetadataPP()
    # For method try_utime we need a downloader
    downloader = FileDownloader({})
    pp.set_downloader(downloader)

    # Create a valid file
    fd, path = tempfile.mkstemp(prefix='youtubedl-test_PostProcessor-')
    # File needs to be closed
    os.close(fd)

    # For testing method try_utime we need to know the atime
    # and the mtime of the just created file
    file_stat = os.stat(path)
    atime = file_stat.st_atime
   

# Generated at 2022-06-14 17:59:20.122413
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # TODO
    pass

# Generated at 2022-06-14 17:59:23.333034
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader
    fd = FileDownloader(None)
    pp = PostProcessor(downloader=fd)
    pp.try_utime('/fake/path', 1000, 2000)

# Generated at 2022-06-14 17:59:34.082450
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import time
    import tempfile
    import shutil
    import contextlib

    @contextlib.contextmanager
    def tmpfile(data):
        tmpdir = tempfile.mkdtemp()
        tmpfn = os.path.join(tmpdir, 'test_utime')
        with open(tmpfn, 'wb') as filetest:
            filetest.write(data)
        yield tmpfn
        shutil.rmtree(tmpdir)

    # Create a simple file to test time conversion
    data = b'hello'
    with tmpfile(data) as fn:
        p = PostProcessor(None)
        # Set the modification time to seconds since Epoch
        atime = mtime = int(time.time())
        p.try_utime(fn, atime, mtime)
        # Get the

# Generated at 2022-06-14 17:59:38.003779
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FakeYDL
    p = PostProcessor(FakeYDL())
    p.try_utime(__file__, 1, 1)



# Generated at 2022-06-14 17:59:50.794707
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import io
    import os
    from tempfile import NamedTemporaryFile
    from .extractor import gen_extractor
    from .downloader import gen_extractor, YoutubeDL

    class MyPostProcessor(PostProcessor):

        def run(self, info):
            f = NamedTemporaryFile(delete=False)
            path = f.name
            f.close()
            os.utime(path, (info['timestamp'], info['timestamp']))
            self.try_utime(path, info['timestamp'] + 1, info['timestamp'] + 1)
            return [path]
    # Test with normal file
    url = 'http://www.youtube.com/watch?v=BaW_jenozKc'

# Generated at 2022-06-14 18:00:02.419134
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..utils import FakeYDL
    from pytube.exceptions import PostProcessingError
    ydl = FakeYDL()
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(VideoExtractor)
    ydl.add_info_extractor(AudioExtractor)
    ydl.add_post_processor(FakePostProcessor)
    ydl.params['format'] = 'bestaudio'
    ydl.parse_options(['test.com/testvideo'])
    ydl.download(ydl.get_entries()[0])
    assert ydl.download_returncode == 1
    assert ydl.extractor.suitable(ydl.get_entries()[0])
    assert ydl.pp.ran
    assert ydl.pp.files_to_

# Generated at 2022-06-14 18:00:10.870629
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time

    class DummyPostProcessor(PostProcessor):

        def test_method(self):
            test_dir = tempfile.mkdtemp()
            path = os.path.join(test_dir, 'file')
            open(path, 'wb').close()
            self.try_utime(path, 0, 0)
            assert os.path.exists(path)
            shutil.rmtree(test_dir)

    DummyPostProcessor().test_method()

# Generated at 2022-06-14 18:00:16.630198
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import pytest
    import os
    import sys
    import stat
    import datetime

    # testing
    import test_utils

    # file to test with
    tests_path = os.path.dirname(os.path.realpath(__file__))
    utime_test_path = os.path.join(tests_path, 'utils', 'utime_test')

    # Make sure file exists
    if not os.path.isfile(utime_test_path):
        pytest.skip('A certain test file is missing, cannot run this test.')

    # Get current time stamp from the file
    file_stat = os.stat(utime_test_path)
    current_mtime = file_stat.st_mtime
    current_atime = file_stat.st_atime

    # Get post processor class

# Generated at 2022-06-14 18:00:21.389864
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Fake class for testing
    class DummyPostProcessor(PostProcessor):
        _downloader = None

    pp = DummyPostProcessor()
    pp.try_utime("test_file", 1000, 1000)


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:00:30.278634
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    # Patch os.utime
    saved_utime = os.utime

    def test_utime(path, times):
        return saved_utime(path, times)

    os.utime = test_utime

    # PostProcessor instantiation
    from youtube_dl.YoutubeDL import YoutubeDL
    downloader = YoutubeDL()

    postprocessor = PostProcessor(downloader)

    # os.utime is working
    assert postprocessor.try_utime('/tmp/foo', 0, 0) == None

    # os.utime is raising an exception
    def test_utime(path, times):
        raise OSError(13, 'Permission denied')

    os.utime = test_utime

    postprocessor.try_utime('/tmp/foo', 0, 0)

    # os.ut

# Generated at 2022-06-14 18:00:35.412204
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        os.utime(encodeFilename('DUMMY_FILE_DOES_NOT_EXIST'), (0, 0))
        assert False, "Utime should raise Exception if file does not exist"
    except:
        pass

# Generated at 2022-06-14 18:00:45.530739
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest
    import os
    import shutil

    class TestPostProcessor(PostProcessor):
        def run(self, information):
            return [], information

    class TmpFile(object):

        def __init__(self, content=b''):
            self.content = content

        def fileno(self):
            return 0

        def read(self):
            return self.content

        def readinto(self, buf):
            size = len(self.content)
            self.content = self.content[size - len(buf):]
            buf[:size] = self.content
            return size

        def close(self):
            pass

    class TestPostProcessor_try_utime(unittest.TestCase):

        def setUp(self):
            self.tmp_dir = './'
           

# Generated at 2022-06-14 18:00:54.666361
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """ test if atime, mtime updated successfully """
    # Create dummy PostProcessor
    pp = PostProcessor(None)
    # Create dummy test.txt file
    with open('test.txt', 'w+') as f:
        f.write('')
    # Set atime, mtime
    atime = 100000000
    mtime = 100000000
    # Update atime, mtime
    pp.try_utime('test.txt', atime, mtime, None)
    # Get atime, mtime
    atime_after = os.path.getatime('test.txt')
    mtime_after = os.path.getmtime('test.txt')
    # Test
    assert atime == atime_after
    assert mtime == mtime_after
    # Cleanup

# Generated at 2022-06-14 18:01:06.942145
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test whether PostProcessor.try_utime behaves correctly
    """
    import time
    import tempfile
    import unittest


    class DownloaderStub:

        def __init__(self):
            self.reported_warnings = []

        def report_warning(self, msg):
            self.reported_warnings.append(msg)

    class PostProcessorSub(PostProcessor):

        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)


    class TestPostProcessor(unittest.TestCase):

        def setUp(self):
            self.downloader = DownloaderStub()
            self.pp = PostProcessorSub(self.downloader)
            self.temp_file = tempfile.NamedTemporaryFile()


# Generated at 2022-06-14 18:01:21.187095
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import filecmp
    import time
    import shutil
    pp = PostProcessor(None)
    fd, fname = tempfile.mkstemp(text=True)
    file = os.fdopen(fd, "w")
    file.write("Hello world")
    file.close()
    t = int(time.time()-100000)
    pp.try_utime(fname, t, t)
    assert os.path.getatime(fname) == t
    os.remove(fname)
    # test_PostProcessor_try_utime2
    pp = PostProcessor(None)
    fd, fname = tempfile.mkstemp(text=True)
    file = os.fdopen(fd, "w")
    file.write("Hello world")
   

# Generated at 2022-06-14 18:01:32.993062
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import time
    import tempfile

    tmpfn = tempfile.mkstemp()[1]

    f = open(tmpfn, 'w')
    f.write('test')
    f.close()

    # Get the timestamp
    timestamp = os.stat(tmpfn).st_mtime

    pp = PostProcessor(None)

    # Confirm that the timestamp is updated
    pp.try_utime(tmpfn, 0, int(time.time()) + 100)
    assert(os.stat(tmpfn).st_mtime != timestamp)

    # Confirm that the timestamp is not updated
    pp.try_utime(tmpfn, 0, 42)
    assert(os.stat(tmpfn).st_mtime == timestamp)

    os.remove(tmpfn)

    # Rename a file, try to

# Generated at 2022-06-14 18:01:44.901467
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL

    ydl = YoutubeDL(params={'postprocessor_args': ['--ignore-errors']})
    pp = PostProcessor(ydl)
    import os
    import tempfile
    tmpdir = tempfile.mkdtemp()
    tmpfile = os.path.join(tmpdir, 'tmpfile')
    tmpfile2 = os.path.join(tmpdir, 'tmpfile2')
    tmpfile3 = os.path.join(tmpdir, 'tmpfile3')
    with open(tmpfile, 'w') as f:
        f.write('hello')
    with open(tmpfile2, 'w') as f:
        f.write('hello')
    with open(tmpfile3, 'w') as f:
        f.write('hello')
    import time
    t = int

# Generated at 2022-06-14 18:01:49.642159
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import shutil
    from .utils import UnavailableVideoError
    from .downloader import Downloader
    from .extractor import GenRequestOnlyIE

    class DummyInfoExtractor(GenRequestOnlyIE):
        IE_DESC = 'Dummy IE'

        def get_info(self, url):
            info = super(DummyInfoExtractor, self).get_info(url)
            info['ext'] = 'tmp'
            return info

    def try_utime_test(tmp_dir):
        tmp_file = tempfile.NamedTemporaryFile(dir=tmp_dir, delete=False)
        tmp_file.close()
        tmp_file = tmp_file.name

        # old utime
        old_utime = os.stat(tmp_file).st_atime
       

# Generated at 2022-06-14 18:02:00.344920
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    tmp_file, file_path = tempfile.mkstemp()
    import time
    import os
    p = PostProcessor()

    atime = time.time()
    mtime = time.time()
    time.sleep(1)
    p.try_utime(file_path, atime, mtime)
    new_atime, new_mtime = os.path.getatime(file_path), os.path.getmtime(file_path)
    assert not (new_atime <= atime and new_mtime <= mtime)
    atime = new_atime
    mtime = new_mtime
    p.try_utime(file_path, atime, mtime, errnote=None)
    new_atime, new_mtime = os.path.getat

# Generated at 2022-06-14 18:02:12.742395
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class PP(PostProcessor):
        def __init__(self):
            class DummyDownloader():
                def report_warning(self, msg):
                    self.msg = msg
            self.downloader = DummyDownloader()

    # Test if success case passes through
    pp = PP()
    pp.try_utime('/path/file', 1298043497, 1298042097)

    # Test if exception is properly handled
    pp = PP()
    pp.try_utime(b'\x93\x89\x90\x9A\x9C\x93\x8A\xAA', 1298043497, 1298042097)
    assert pp.downloader.msg == 'Cannot update utime of file'

    # Test if exception is properly handled, with custom msg
    pp = PP()
    pp

# Generated at 2022-06-14 18:02:18.960679
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkstemp
    from time import time, sleep
    from os import utime, remove, stat

    # Create a temporary file
    unused_fd, filename = mkstemp(prefix='', suffix='.tmp')

    # Record its initial modification timestamp
    initial_modification_timestamp = stat(filename).st_mtime

    # Wait a second
    sleep(1)

    # Change its timestamp with try_utime (record the timestamp before)
    pp = PostProcessor(None)
    pp.try_utime(filename, time(), time()-1)

    # Check that the file's timestamp has actually changed
    assert stat(filename).st_mtime < initial_modification_timestamp

    # Cleanup
    remove(filename)

# Generated at 2022-06-14 18:02:23.656132
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    downloader = FileDownloader({})
    pp = PostProcessor(downloader)
    pp.try_utime('file', 0, 0)

# Generated at 2022-06-14 18:02:33.313605
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    import shutil
    import tempfile
    import time

    try:
        with tempfile.NamedTemporaryFile(suffix='_test_file') as temp:
            temp.write('SOME CONTENT')
            temp.flush()
            os.utime(temp.name, (1, 1)) # 1 second of epoch
            pp = PostProcessor(None)
            pp.try_utime(temp.name, 2, 2) # 2 seconds of epoch
            assert os.stat(temp.name).st_atime == 2
            assert os.stat(temp.name).st_mtime == 2
    finally:
        pass

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:02:37.209923
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os

    # Create a dummy file for test
    test_filename = encodeFilename('PostProcessor_try_utime.test')
    if os.path.exists(test_filename):
        os.unlink(test_filename)
    open(test_filename, 'wb').close()

    # Get the timestamp of the dummy file
    timestamp = os.stat(test_filename).st_mtime

    # Prepare a PostProcessor object for test
    from ..downloader import Downloader
    from ..compat import is_py2
    if is_py2:
        from io import BytesIO as DataIO
    else:
        from io import BytesIO as DataIO
    def fake_report_warning(self, msg):
        print(msg)
    Downloader.report_warning = fake_report_warning
    fake_PP

# Generated at 2022-06-14 18:02:49.625085
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    return {
        'input': {
            'path': 'filename.txt',
            'atime': 1,
            'mtime': 2,
            'errnote': 'errnote test',
        },
        'output': None,
        'exception': None,
        'call_count': {
            'os.utime': 0
        }
    }

# Generated at 2022-06-14 18:02:57.299833
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time

    ff, path = tempfile.mkstemp()
    os.close(ff)

    try:
        os.stat(path)

        pp = PostProcessor(None)
        pp.try_utime(path, 0, 0)
        st = os.stat(path)
        assert st.st_atime == 0
        assert st.st_mtime == 0

    finally:
        os.remove(path)

# Generated at 2022-06-14 18:03:04.455034
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakePostProcessor(PostProcessor):
        pass

    class FakeDownloader:
        def __init__(self):
            self.warning_shown = False

        def report_warning(self, warning):
            self.warning_shown = True

    fpp = FakePostProcessor()
    fd = FakeDownloader()
    fpp.set_downloader(fd)

    file = 'test.mp3'
    fpp.try_utime(file, 0, 0)

    assert fd.warning_shown == False
    os.remove(file)

# Generated at 2022-06-14 18:03:12.589513
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..extractor.common import InfoExtractor
    from .rtmp import _get_fsize
    from ..compat import compat_urllib_request
    from ..utils import encodeFilename

    # Use case 1: change access and modification time of file
    # Precondition: file exists
    # Success: access and modification time of file has been changed
    # Failure1: access or modification time of file has not been changed
    # Failure2: file concurs problems of access
    # Postcondition: file exists
    def test1():
        file_path = './file_test_postprocessor_try_utime.test'
        file = open(file_path, 'w')
        file.close()

        pp = PostProcessor(None)

# Generated at 2022-06-14 18:03:21.119012
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import parse_iso8601

    pp = PostProcessor(None)
    myfile = 'myfile'
    ts = parse_iso8601('2011-01-01T01:01:01.000000Z')  # "utime not allowed" date

    open(encodeFilename(myfile), 'w').close()

    pp.try_utime(myfile, ts, ts)
    assert os.stat(myfile).st_atime == ts
    assert os.stat(myfile).st_mtime == ts

    os.unlink(encodeFilename(myfile))

# Generated at 2022-06-14 18:03:26.546469
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import shutil
    import tempfile
    import time
    import os

    class TmpPP(PostProcessor):
        def __init__(self):
            pass

    (fd, tmpfile) = tempfile.mkstemp()
    tmpfile = encodeFilename(tmpfile)

    pp = TmpPP()
    pp.try_utime(tmpfile, time.time(), time.time())
    os.close(fd)
    os.remove(tmpfile)

# Generated at 2022-06-14 18:03:37.526700
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import os
    import shutil
    from ..utils import PostProcessor
    from ..compat import (
        compat_isfile,
        compat_utime,
        compat_os_name,
    )

    tmp_dir = tempfile.mkdtemp(prefix="ytdl_test_PostProcessor_try_utime_")


# Generated at 2022-06-14 18:03:47.002762
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time

    from . import FakeYDL, EmbedThumbnailPP

    tpath = tempfile.mkdtemp('utime')
    tempdir = os.path.join(tpath, 'tempdir')
    os.mkdir(tempdir)
    temppath = os.path.join(tempdir, 'temppath')
    with open(temppath, 'w') as f:
        f.write('a')
    atime = int(time.time()) - 30
    mtime = int(time.time()) - 60
    with open(temppath, 'a') as f:
        f.write('b')
    shutil.rmtree(tpath)



# Generated at 2022-06-14 18:03:58.127705
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import mock
    import time
    import os
    class MockDownloader(object):
        def report_warning(self, *args, **kwargs):
            pass
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_name = temp_file.name

# Generated at 2022-06-14 18:03:59.123773
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert False, "Not implemented"

# Generated at 2022-06-14 18:04:15.353658
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os.path
    import tempfile
    import time

    path = tempfile.mkstemp()[1]
    now = time.time()
    pp = PostProcessor(None)
    pp.try_utime(path, now + 200, now + 200, 'Cannot update utime')
    assert os.path.getmtime(path) == now + 200

    os.remove(path)



# Generated at 2022-06-14 18:04:24.611015
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    dl = YoutubeDL()

    pp = PostProcessor(dl)

    class FakeFile:
        def __init__(self):
            self.path = 'test.mp4'
            self.atime = None
            self.mtime = None
            self.errnote = None

        def utime(self, atime, mtime):
            self.atime = atime
            self.mtime = mtime

    mp3_file = FakeFile()

    pp.try_utime(mp3_file.path, 1, 2)
    assert mp3_file.atime == 1
    assert mp3_file.mtime == 2
    assert mp3_file.errnote is None

    mp3_file.errnote = 'Cannot update utime of file'
    mp3

# Generated at 2022-06-14 18:04:33.602652
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .. import YoutubeDL
    from .common import FakeYDL
    from .common import FakePostProcessor
    from .extractor.youtube import YoutubeIE

    def test_try_utime(downloader, filename, expected_exception):
        # Set up a PostProcessor object
        pp = PostProcessor(downloader)
        # Set up a FakeFile object
        file_obj = FakeFile({'title': 'mytitle'})
        # Set up an output template to get the filename
        downloader.params['outtmpl'] = '%(title)s_%(id)s_%(ext)s'
        # Set up a FakeInfoExtractor to get the file info
        ie = YoutubeIE(downloader)

# Generated at 2022-06-14 18:04:44.975772
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.common import InfoExtractor
    from ..downloader.common import FileDownloader
    from os import utime
    from time import time
    from tempfile import NamedTemporaryFile
    from collections import namedtuple

    File = namedtuple('File', ['filename'])
    TempFile = namedtuple('TempFile', ['name'])

    class MockInfoExtractor(InfoExtractor):
        def __init__(self, downloader):
            self._downloader = downloader
            self._temp_files = []

        def _make_temp_file(self, suffix):
            tf = TempFile(NamedTemporaryFile(prefix='__yt_dl_test_', suffix=suffix).name)
            self._temp_files.append(tf)
            return tf


# Generated at 2022-06-14 18:04:55.068627
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.youtube import YoutubeIE
    from ..utils import DateRange

    from .common import FakeYDL

    ie = YoutubeIE(FakeYDL())
    postprocessor = PostProcessor(ie)

    # test DirEntry
    mock_entry = ie.ytdl.FileDownloader._download_retrieve_http_headers.mock_entry

    # test with mock_entry
    mock_entry.stat().st_atime = mock_entry.stat().st_mtime = 0
    postprocessor.try_utime(mock_entry.path, 15, 12, 'failed')
    assert mock_entry.stat().st_atime == 15
    assert mock_entry.stat().st_mtime == 12

    # test that utime fails silently with DirEntry
    mock_entry.stat().st_atime = 0
   

# Generated at 2022-06-14 18:05:07.002607
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile
    from datetime import datetime
    from time import sleep

    def count_dif(date_before, date_after):
        date_before = datetime.fromtimestamp(date_before)
        date_after = datetime.fromtimestamp(date_after)
        return (date_after - date_before).total_seconds()

    def sleep_dif(date_before, date_after, max_sleep=1):
        dif = count_dif(date_before, date_after)
        if dif > max_sleep:
            raise PostProcessingError('utime update too slow')

    pp = PostProcessor(None)
    with NamedTemporaryFile() as f:
        file_path = f.name
        sleep(1)
        before = datetime.now()


# Generated at 2022-06-14 18:05:18.297337
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    import time
    import tempfile
    import shutil
    import os

    def touch(fname, times=None):
        with open(fname, 'a'):
            os.utime(fname, times)

    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:05:29.038310
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import io
    import sys
    import tempfile
    from mock import patch

    class DummyDownloader(object):
        params = {'outtmpl': 'dummy'}

        def report_warning(self, message):
            print(message, file=sys.stderr)

    p = PostProcessor(DummyDownloader())

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:05:41.170986
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import platform, sys
    import tempfile
    import time
    import unittest

    def touch(fname, times=None):
        with open(encodeFilename(fname), 'a'):
            os.utime(encodeFilename(fname), times)

    class MockDownloader():
        def report_warning(self, message):
            print >> sys.stderr, message

    class MockPostProcessor(PostProcessor):
        def __init__(self):
            # if you want to specify your own downloader
            # the constructor should accept it as a parameter
            pass

    class TestTryUtimeMethods(unittest.TestCase):
        """
        Tests for PostProcessor.try_utime(path, atime, mtime, errnote)
        """

        def setUp(self):
            self.pp

# Generated at 2022-06-14 18:05:48.337020
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyFile(object):
        def __init__(self, name, times):
            self.name = name
            self.times = times

    class DummyDownloader(object):
        def __init__(self):
            self.downloader_dir = '.'
            self.params = {}

        def report_warning(self, errnote):
            pass
    downloader = DummyDownloader()
    p = PostProcessor(downloader)
    f = DummyFile('foo', [1, 2])
    p.try_utime(f, f.times[0], f.times[1])



# Generated at 2022-06-14 18:06:22.850089
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    from ..extractor import get_suitable_extractor

    class DummyPostProcessor(PostProcessor):
        def run(self, information):
            with tempfile.NamedTemporaryFile() as t:
                os.utime(t.name, (1, 1))
                time.sleep(0.2)
                self.try_utime(t.name, 1, 2, 'FAIL')
                with open(t.name) as s:
                    res = os.fstat(s.fileno())
                # utime is changed successfully
                assert res.st_mtime == 2
            return [], information

    class DummyInfoExtractor(object):
        def __init__(self, downloader):
            pass


# Generated at 2022-06-14 18:06:31.427801
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ytdl.downloader import YoutubeDL
    from ytdl.postprocessor import PostProcessor
    import datetime
    import time
    import os
    import sys

    # create test file and non-ASCII test filename
    fn = u'\u2603 - abc'
    if sys.platform == 'win32':
        fn = fn.encode('utf-8')
    f = open(fn, 'wb')
    f.close()

    # get the current modification time
    mtime = os.stat(fn).st_mtime

    # create the postprocessor instance
    ydl = YoutubeDL()
    pp = PostProcessor(ydl)

    # check that modification time does not change
    pp.try_utime(fn, 0, mtime)
    assert mtime == os.stat(fn).st_

# Generated at 2022-06-14 18:06:42.876073
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import time
    import unittest


# Generated at 2022-06-14 18:06:52.031228
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import compat_get_modified_time
    from ..utils import PostProcessor
    import tempfile
    import os
    import shutil
    import time

    def _create_tmp_file(size=1024):
        fd, path = tempfile.mkstemp()
        os.fdopen(fd).write(b'\x00' * size)
        return path

    def _create_tmp_dir():
        return tempfile.mkdtemp()

    class _FakeDownloader(object):
        def __init__(self, params):
            self.params = params

        def report_warning(self, message):
            pass

    def _test_try_utime_helper(size):
        temp_path = _create_tmp_file(size)
        dir_path = _create_tmp_dir()


# Generated at 2022-06-14 18:07:03.465749
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.common import InfoExtractor
    from ..utils import prepend_extension
    import tempfile
    import shutil
    import os
    cwd = tempfile.mkdtemp()
    DEVNULL = open(os.devnull, 'wb')
    ie = InfoExtractor()
    ie.params['outtmpl'] = os.path.join(cwd, '%(title)s')
    ie.add_info_extractor(_FakeInfoExtractor({'title': 'foo'}))

# Generated at 2022-06-14 18:07:15.592106
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from ..Extractor import GenYoutubeIE
    from ..utils import DateRange

    params = {
        'outtmpl': 'test.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessor_args': ['ffmpeg', '-vn'],
        'nooverwrites': True,
        'quiet': True
    }

    params_without_quiet = dict(params)
    params_without_quiet['quiet'] = False

    # It is expected to raise PostProcessingError in case of
    # the URL is not correctly handled by the downloader

# Generated at 2022-06-14 18:07:22.037273
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from tempfile import NamedTemporaryFile
    f = NamedTemporaryFile()
    dl = YoutubeDL({'outtmpl': f.name})
    post_processor = PostProcessor(None)
    post_processor.set_downloader(dl)
    post_processor.try_utime(f.name, 10, 10) # should not raise any error

# Generated at 2022-06-14 18:07:22.717462
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:07:34.118781
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    # Test it through the subclass FFmpegPostProcessor
    from .ffmpeg import FFmpegPostProcessor
    from ..YoutubeDL import YoutubeDL
    pp = FFmpegPostProcessor(YoutubeDL())

    import tempfile
    import os.path

    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(b"foo")
    f.close()
    try:
        atime, mtime = os.path.getatime(f.name), os.path.getmtime(f.name)
        pp.try_utime(f.name, atime, mtime)
        assert os.path.getatime(f.name) == atime
        assert os.path.getmtime(f.name) == mtime
    finally:
        os.remove(f.name)

# Generated at 2022-06-14 18:07:39.450819
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Test PostProcessor.try_utime
    """
    from ..postprocessor import PostProcessor
    from .common import FakeYDL

    downloader = FakeYDL()
    pp = PostProcessor(downloader)
    try:
        pp.try_utime('/dir/nonexistfile.mp3', 1, 1)
    except PostProcessingError:
        pass
    #do nothing
    else:
        raise AssertionError()

# Generated at 2022-06-14 18:08:22.220776
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # We do not need to test it, because the method just
    # wraps os.utime and we have test for os.utime
    # in module utils.py
    assert True

# Generated at 2022-06-14 18:08:32.366355
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    tmppath = tempfile.mkdtemp(prefix='youtubedownloader-unittest-')
    try:
        fpath = os.path.join(tmppath, 'file')
        f = open(fpath, 'w')
        f.close()
        pp = PostProcessor(None)
        pp.try_utime(fpath, 12345, 0)
        assert os.path.getatime(fpath) == 12345
        pp.try_utime(fpath, 0, 0, '')
        assert os.path.getatime(fpath) != 12345
    finally:
        shutil.rmtree(tmppath)