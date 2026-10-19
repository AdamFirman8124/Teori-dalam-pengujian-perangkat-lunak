

# Generated at 2022-06-14 17:58:40.618752
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile

    # Create a test file
    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.write(b"Testing time update")
    tf.close()

    # Mock class to test method try_utime
    class PP(PostProcessor):
        def run(self, info):
            self.try_utime(tf.name, 1537332600, 1537332700)

    pp = PP()
    pp.run(None)

    # Check times are updated correctly
    import time
    assert time.ctime(os.path.getatime(tf.name)) == 'Wed Sep 26 14:10:00 2018'
    assert time.ctime(os.path.getmtime(tf.name)) == 'Wed Sep 26 14:11:40 2018'

    # Clean up
    os

# Generated at 2022-06-14 17:58:44.356403
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    import time
    now = time.time()
    file_path = 'file.flv'
    pp.try_utime(file_path, now, now)

# Generated at 2022-06-14 17:58:49.780813
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os

    # create a test file
    tmpfile = open('tmp', 'w')
    tmpfile.close()
    # get the modification time of the file
    orig_atime = os.stat('tmp').st_atime
    orig_mtime = os.stat('tmp').st_mtime

    # get a PostProcessor instance
    pp = PostProcessor(None)

    # We need to sleep a little in order to ensure that the times are different.
    import time
    time.sleep(0.1)
    # Call the method
    pp.try_utime('tmp', orig_atime, orig_mtime)

    # the method should change the file's modification time
    new_atime = os.stat('tmp').st_atime
    new_mtime = os.stat('tmp').st_mtime


# Generated at 2022-06-14 17:58:58.685513
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():  # pylint: disable=invalid-name
    import tempfile
    import datetime
    import shutil

    from ..utils import DateRange, DateTimeRange

    # 1. Configure and prepare variables
    PP_TEST_DIR = tempfile.mkdtemp(prefix='youtube-dl_PostProcessor_try_utime')
    PP_TEST_FILE = os.path.join(PP_TEST_DIR, 'FileForTest')

    PP_TEST_DATE_AFTER = datetime.datetime.now() + datetime.timedelta(days=1)  # Tomorrow
    PP_TEST_DATE_BEFORE = PP_TEST_DATE_AFTER - datetime.timedelta(days=2)  # Yesterday
    PP_TEST_DATE_IN_RANGE_START = PP

# Generated at 2022-06-14 17:59:08.816264
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import shutil
    import datetime
    import time


# Generated at 2022-06-14 17:59:21.517204
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    import shutil
    from tempfile import mkdtemp
    from .utils import DateRange

    ranges = (DateRange(0, 120000000), DateRange(120000000, 0))

    for (atime, mtime) in ranges:
        try:
            tmpdir = mkdtemp()
            path = os.path.join(tmpdir, "test_file")
            f = open(path, "wb")
            f.close()
            pp = PostProcessor(None)

            pp.try_utime(path, atime, mtime)

            stats = os.stat(path)
            assert stats.st_atime == atime
            assert stats.st_mtime == mtime
        except Exception as e:
            raise AssertionError("Couldn't call try_utime: %s" % e)

# Generated at 2022-06-14 17:59:30.399050
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time
    dirname = tempfile.mkdtemp(prefix='youtube-dl-post-processor-utime')

# Generated at 2022-06-14 17:59:42.332433
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    test_file = "/tmp/youtube_dl_utime_test"

# Generated at 2022-06-14 17:59:52.634089
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def try_utime(path, atime, mtime):
        try:
            os.utime(encodeFilename(path), (atime, mtime))
        except Exception:
            pass

    # Create temporal file
    fd, path = tempfile.mkstemp()
    os.close(fd)

    # Get mtime and atime for this file
    stat = os.stat(path)
    mtime = stat.st_mtime
    atime = stat.st_atime

    # Change mtime and atime of this file
    try_utime(path, atime + 100, mtime + 100)
    new_stat = os.stat(path)

    # Test try_utime
    assert new_stat.st_mtime == mtime + 100
    assert new_stat.st_atime == at

# Generated at 2022-06-14 17:59:58.123631
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Subclass PostProcessor and override report_warning to catch the error
    class PP_Test(PostProcessor):
        def report_warning(self, errnote):
            self.reported_warning = errnote
    pp = PP_Test()
    # Create a dummy file name
    fname = 'a_filename'
    # Time is in seconds since the epoch
    atime = 12345678.0
    mtime = 98765432.0
    # Call try_utime
    pp.try_utime(fname, atime, mtime, errnote='Dummy Error')
    # Check that the error message was caught
    assert pp.reported_warning == 'Cannot update utime of file'

# Generated at 2022-06-14 18:00:03.950622
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    post_processor = PostProcessor()
    # Create a dummy file
    tmp_file = './test.txt'
    open(tmp_file, 'a').close()
    # Set utime of file to now
    post_processor.try_utime(tmp_file, 0, 0)
    # Remove dummy file
    os.remove(tmp_file)

# Generated at 2022-06-14 18:00:12.980923
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    if not os.path.exists("/bin/touch"):
        print("/bin/touch not found")
        return True
    elif not os.path.exists("/bin/bash"):
        print("/bin/bash not found")
        return True
    import shutil
    import tempfile
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:00:25.671845
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import external_downloader
    from .extractor import gen_extractor

    class DummyPP(PostProcessor):
        """Dummy PostProcessor for unit test."""
        def __init__(self, dl):
            PostProcessor.__init__(self, dl)

        def run(self, information):
            self.try_utime(information['filepath'], 1, 1)
            return [], information

    # Create dummy InfoExtractor, Downloader and PostProcessor
    dl = external_downloader({})
    ie = gen_extractor(dl)

    # Download dummy file
    test_path = os.path.join(dl.get_temp_dir(), 'test')
    test_url = 'http://localhost:8080/test_file'
    ie.url = test_url

# Generated at 2022-06-14 18:00:36.528836
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from . import YoutubeDL
    from datetime import date
    import os.path
    import tempfile
    ydl = YoutubeDL()
    ydl.params['verbose'] = True
    # Check that existing file can be set to 1970
    today = date.today()
    tmp_testfile = tempfile.NamedTemporaryFile(mode='wb', suffix='.ts')
    tmp_testfile.write(b'Test file, remove me')
    tmp_testfile.seek(0)
    assert os.path.getmtime(tmp_testfile.name) >= today.year
    post_processor = PostProcessor(ydl)
    post_processor.try_utime(tmp_testfile.name, 0, 0, 'Cannot test utime')
    assert os.path.getmtime(tmp_testfile.name)

# Generated at 2022-06-14 18:00:46.638211
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.common import InfoExtractor
    from ..extractor import gen_extractors

    gen_extractors()

    class DummyIE(InfoExtractor):
        IE_NAME = 'dummy'
        IE_DESC = False  # do not list
        _TEST = {
            'url': 'http://example.com/file.mp3',
            'md5': '5a7f5e1d74d724ef830a9922310a21b0',
            'info_dict': {
                'id': '90x0LrVnYmY',
                'ext': 'mp3',
                'title': 'Morcheeba - Strange Cousins From The West',
                'thumbnail': 're:^https?://.*\.jpg'
            },
        }

    ie = Dummy

# Generated at 2022-06-14 18:00:55.447272
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractors
    from ..downloader import Downloader
    test_downloader = Downloader(params={'outtmpl': '%(epoch)s.%(ext)s'})
    for ie in gen_extractors():
        ie.set_downloader(test_downloader)
        for ie_result in ie.extract_info(url='', download=False):
            ie_result.add_extra_info({'epoch': '1498551555'})
            pp = PostProcessor(test_downloader)
            pp.run(ie_result)
            break

# Generated at 2022-06-14 18:01:07.880882
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from .common import FakeFile
    from ..utils import encodeFilename

    class XPostProcessor(PostProcessor):
        def run(self, info):
            return [], info

    ff = FakeFile(encodeFilename('xyz'), size=90000)
    fd = open(ff.name, "wb")
    fd.write(b"foo")
    fd.close()

    # test utime
    import time
    orig_utime = os.utime
    orig_utime_warn_err = os.utime.__name__
    os.utime = lambda *args, **kwargs: (1, 2)

    dl = YoutubeDL()
    dl.params['simulate'] = True
    pp = XPostProcessor(dl)


# Generated at 2022-06-14 18:01:19.442952
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    def run_test(mocker, errnote):
        pp = PostProcessor(None)
        os_utime_mock = mocker.patch('os.utime')
        encodeFilename_mock = mocker.patch('youtube_dl.postprocessor.encodeFilename')
        pp.report_warning = mocker.MagicMock()
        os_utime_mock.side_effect = Exception(errnote)
        pp.try_utime('path', 1, 2)
        encodeFilename_mock.assert_called_once_with('path')
        os_utime_mock.assert_called_once_with(encodeFilename_mock.return_value, (1, 2))
        pp.report_warning.assert_called_once_with(errnote)


# Generated at 2022-06-14 18:01:31.701960
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..extractor.common import InfoExtractor

    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            PostProcessor.__init__(self, downloader)

    class TestInfoExtractor(InfoExtractor):
        def __init__(self, downloader=None):
            InfoExtractor.__init__(self, downloader)
            self.test_info_dict = {}

        def _real_extract(self, url):
            return self.test_info_dict

    test_ie = TestInfoExtractor()
    test_ie.test_info_dict = {'id': 'anId', 'title': 'aTitle', 'ext': 'aExt'}

    my_test_pp = TestPostProcessor()
    my

# Generated at 2022-06-14 18:01:33.073881
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime('path', 10, 15)

# Generated at 2022-06-14 18:01:45.202993
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import datetime
    import time
    import subprocess
    from ..compat import compat_tempfile

    class DummyDownloader:
        @staticmethod
        def report_warning(msg):
            print(msg)

    pp = PostProcessor(DummyDownloader())

    # check if we can set both atime and mtime with try_utime
    with compat_tempfile.NamedTemporaryFile() as tf:
        timestamp_0 = int(time.time())
        timestamp_1 = timestamp_0 - 1000
        pp.try_utime(tf.name, timestamp_0, timestamp_0, errnote='Cannot update both utime of file')
        stat_0 = os.stat(tf.name)
        assert datetime.datetime.fromtimestamp(stat_0.st_atime) == dat

# Generated at 2022-06-14 18:01:53.227820
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.params['outtmpl'] = '%(title)s'
    pp = PostProcessor(ydl)
    pp.try_utime('./test_try_utime.txt', 3, 3)
    pp.try_utime('./test_try_utime_not_exist.txt', 3, 3)
    os.remove(os.path.join('.', 'test_try_utime.txt'))

# Generated at 2022-06-14 18:02:00.795134
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    # Case 1: normal case

# Generated at 2022-06-14 18:02:08.550301
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import pytest
    pp = PostProcessor()
    def test(a,b,c,d,e,f):
        print("Test")
    pp.report_warning = test
    print(pp.try_utime(1,1,1))
    #assert pp.try_utime(1,1,1) is None
    #assert pp.try_utime(1,1,1,1) is None


# Generated at 2022-06-14 18:02:10.665166
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # should not raise any exception
    pp.try_utime('foo', 0, 0)

# Generated at 2022-06-14 18:02:20.239380
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil, tempfile
    import time
    # create temporary directory
    dirpath = tempfile.mkdtemp()
    # create temporary file
    fd, filepath = tempfile.mkstemp(dir=dirpath)
    with open(fd, 'wb') as fo:
        fo.write(b"test")
    os.close(fd)
    # change file modification time
    mtime = time.gmtime(time.time() - 86400)
    os.utime(filepath, (os.path.getatime(filepath), time.mktime(mtime)))
    # test try_utime with same modification time
    test_PP = PostProcessor(downloader=None)
    mtime = time.gmtime(time.time() - 86400)

# Generated at 2022-06-14 18:02:30.099867
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    from ..utils import encodeFilename
    from .downloader import getFakeYDL
    from .extractor import get_info_extractor
    from .common import InfoExtractor
    from .compat import compat_basestring
    import os
    import time
    import shutil

    # We need a custom InfoExtractor class to override some methods
    class MockInfoExtractor(InfoExtractor):
        def __init__(self, downloader):
            super(MockInfoExtractor, self).__init__(downloader)


# Generated at 2022-06-14 18:02:42.340558
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    files_to_delete = []

    dummy_downloader = object()

    from ..compat import compat_tempfile
    test_file = compat_tempfile.NamedTemporaryFile(delete=False)
    test_file.write(b"test string")
    test_file.close()

    PP = PostProcessor(dummy_downloader)

    # default errnote
    PP.try_utime(test_file.name, 0, 0)

    # custom errnote
    PP.try_utime(test_file.name, 0, 0, errnote='Custom errnote')

    # custom encoding
    PP.try_utime(test_file.name, 0, 0, errnote='Custom errnote')

    # should print the error message from os.utime, and not the errnote
    test_file.close()

# Generated at 2022-06-14 18:02:54.141260
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest import TestCase
    from tempfile import mkdtemp
    import shutil
    from ..utils import DateRange
    from ..compat import file_open
    from ..downloader import FileDownloader

    class TestDownloader(FileDownloader):
        def report_warning(self, msg, *args):
            raise AudioConversionError(msg % args)

    class PostProcessorTest(TestCase, PostProcessor):
        def setUp(self):
            self.temp_dir = mkdtemp()
            self.configure_downloader(FileDownloader(params={
                'outtmpl': os.path.join(self.temp_dir, '%(title)s-%(id)s.%(ext)s'),
            }))


# Generated at 2022-06-14 18:03:01.308359
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        import posix
        is_posix = True
    except ImportError:
        is_posix = False
    if not is_posix:
        from nose.exc import SkipTest
        raise SkipTest("could not import posix (only testable on *nix)")
    class DummyDownloader():
        def __init__(self, pp):
            self.pp = pp
        def to_screen(self, msg):
            self.msg = msg
        def report_warning(self, msg):
            self.errnote = msg
    class DummyPP(PostProcessor):
        pass
    # Atime and Mtime of this file should be the same
    file_path = __file__
    dummy_pp = DummyPP(DummyDownloader(dummy_pp))
    atime_original = posix

# Generated at 2022-06-14 18:03:08.544674
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile, os
    from ..utils import DateRange

    (fd, fn) = tempfile.mkstemp()
    os.fdopen(fd, 'w').close()
    mtime = os.stat(fn).st_mtime
    pp = PostProcessor(downloader=None)
    # Change mtime:
    pp.try_utime(fn, mtime, mtime + 2)
    # Keep mtime:
    pp.try_utime(fn, -1, -1)
    # Restore mtime:
    pp.try_utime(fn, mtime, mtime)
    os.remove(fn)

# Generated at 2022-06-14 18:03:21.595199
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import shutil
    import sys
    class FakeLogger(object):
        def debug(self, msg):
            print('FakeLogger.debug: %s' % msg)
        def warning(self, msg):
            print('FakeLogger.warning: %s' % msg)
    class FakeYDL(object):
        def __init__(self):
            self.params = {
                'keepvideo': True,
                'outtmpl': '%(title)s.%(ext)s',
            }
            self.logger = FakeLogger()
        def report_warning(self, msg):
            print('FakeYDL.report_warning: %s' % msg)
    class PostProcessor(object):
        def __init__(self):
            self._downloader = FakeY

# Generated at 2022-06-14 18:03:29.480950
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest
    import tempfile
    class TestPostProcessor(PostProcessor):
        def __init__(self, proc_test):
            self.proc_test = proc_test
        def try_utime(self, *args, **kargs):
            self.proc_test.assertEqual(args, (self.proc_test.temp_file, 1, 2))
            self.proc_test.assertEqual(kargs, {'errnote': 'Cannot update utime of file'})
    class TestDownloader(object):
        def __init__(self, proc_test):
            self.proc_test = proc_test
        def report_warning(self, msg):
            self.proc_test.assertEqual(msg, 'Cannot update utime of file')

# Generated at 2022-06-14 18:03:40.055014
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Test PostProcessor.try_utime()"""

# Generated at 2022-06-14 18:03:49.083488
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .FakeDl import FakeDl
    from .compat import compat_str
    from .compat import compat_os_name
    from shutil import rmtree
    from tempfile import mkdtemp
    from time import time

    # Create the temp dir
    temp_dir = mkdtemp(prefix="youtube-dl-test_", suffix="-PostProcessor")

    # Create the FakeDl
    d = FakeDl(params={})

    # Create the PostProcessor
    p = PostProcessor(d)

    # Empty dir
    p.try_utime(temp_dir, 1, 2, 'hello')

    # Only file
    file_path = os.path.join(temp_dir, 'file_1')
    f = open(file_path, 'w')
    f.write('')


# Generated at 2022-06-14 18:04:00.867543
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time
    def t():
        pp = PostProcessor(None)
        tdir = tempfile.mkdtemp()
        try:
            fname = os.path.join(tdir, 'foo')
            with open(fname, 'wb') as f:
                f.write(b'bar')
            os.utime(fname, (1, 2))
            pp.try_utime(fname, 3, 4)
            assert os.stat(fname).st_atime == 3
            assert os.stat(fname).st_mtime == 4
        finally:
            shutil.rmtree(tdir)
    t()
    import os
    # Windows doesn't allow to change the file date of open file
    # so let's use a dummy implementation of os

# Generated at 2022-06-14 18:04:07.424548
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL

    # Create a dummy downloader
    downloader = YoutubeDL()

    # Create a PP object and test `utime` method
    pp = PostProcessor(downloader)
    # First, create a dummy file
    path = 'dummy.tmp'
    open(path, 'wb').close()
    # Test normal successful case
    pp.try_utime(path, 1513773700, 1513900500)
    # Test exception case
    pp.try_utime(path, 'a', 'b', errnote='This is an error')
    # Delete dummy file
    os.remove('dummy.tmp')

# Generated at 2022-06-14 18:04:13.279236
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class _FakePostProcessor(PostProcessor):
        def __init__(self, test):
            self.test = test

    pp = _FakePostProcessor(test=False)
    os.environ['YOU_TUBE_DL_TEST_PPUTIME'] = '1'
    try:
        if pp.try_utime('_', '_', '_', '_'):
            raise AssertionError('try_utime returned True')
    finally:
        del os.environ['YOU_TUBE_DL_TEST_PPUTIME']

# Generated at 2022-06-14 18:04:23.280514
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import copy
    import tempfile
    import os
    import shutil
    import time
    import locale
    import stat

    locale.setlocale(locale.LC_ALL, 'C')

    # Create temp folder
    tmp_folder = tempfile.mkdtemp()

    # Create temp file in tmp folder
    (fd, path) = tempfile.mkstemp(None, None, tmp_folder)
    file = os.fdopen(fd, 'wb')
    file.close()

    # Change time of temp file
    os.utime(path, (100, 200))

    # Create PostProcessor object
    pp = PostProcessor(None)

    # Set time of temp file to default
    pp.try_utime(path, 0, 0)

    # Check if file time was changed

# Generated at 2022-06-14 18:04:32.902849
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import errno
    import time
    import pytest
    from ..PostProcessor import PostProcessor

    def os_utime_mock(path, times):
        if path != 'foo':
            raise Exception('Cannot update utime of file')
    postProcessor = PostProcessor()
    postProcessor.try_utime = os_utime_mock

    try:
        postProcessor.try_utime('foo', time.time(), time.time(), 'Cannot update utime of file')
    except Exception as e:
        pytest.fail(str(e))

    with pytest.raises(PostProcessingError) as excinfo:
        postProcessor.try_utime('', time.time(), time.time(), 'Cannot update utime of file')
    assert 'Cannot update utime of file'

# Generated at 2022-06-14 18:04:47.152786
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    test_dir = 'test_dir'
    test_file = os.path.join(test_dir, 'test_file')
    os.makedirs(test_dir)
    open(test_file, 'wb').close()

    atime = os.path.getatime(test_file)
    mtime = os.path.getmtime(test_file)

    pp = PostProcessor(None)
    pp.try_utime(test_file, atime, mtime)
    assert os.path.getatime(test_file) == atime
    assert os.path.getmtime(test_file) == mtime

    # TODO: find a way to make the following test pass.
    #
    #os.chmod(test_file, 0)
    #pp.try_utime(test

# Generated at 2022-06-14 18:04:56.553385
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import time
    from ..utils import encodeFilename

    # Create temporary file
    fd, tmpfile = tempfile.mkstemp(prefix='youtubedl_test_')
    os.close(fd)

    # Set mtime to the past
    past_time = time.time() - 3600
    os.utime(encodeFilename(tmpfile), (past_time, past_time))

    # Instantiate PostProcessor
    pp = PostProcessor(None)

    # Test
    # Should not raise exception
    pp.try_utime(tmpfile, 0, 0)

    # Should not raise exception, but mtime remains the same
    pp.try_utime(tmpfile, os.utime, 1000000000, 1000000000)

    # Cleanup

# Generated at 2022-06-14 18:05:07.779724
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # pylint: disable=import-error
    import sys
    if sys.version_info < (2, 6):
        return
    from ..utils import DateRange
    pp = PostProcessor(None)
    path = 'this_is_just_a_test'
    # Test that calling while not raising exceptions works
    pp.try_utime(path, 100, 100)
    # Test that raising exceptions are caught
    class MyException(Exception):
        pass
    def utime_exc(*args, **kwargs):
        raise MyException()
    old_utime = os.utime
    try:
        os.utime = utime_exc
        pp.try_utime(path, 200, 200, 'An error note')
        del utime_exc
    finally:
        os.utime = old_utime

# Generated at 2022-06-14 18:05:18.712641
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestDownloader():
        def report_warning(self, msg):
            self.msg = msg

    downloader = TestDownloader()
    pp = PostProcessor(downloader)
    assert downloader.msg is None
    pp.try_utime('/tmp/qzrbgqk/Holiday Island/Adventure/ENU/SFX/SFX_PLAYER_CANT_SHOOT.aac', 1, 2)
    assert downloader.msg is None
    os.mkdir(encodeFilename('/tmp/qzrbgqk/Holiday Island/Adventure/ENU/SFX'))
    pp.try_utime('/tmp/qzrbgqk/Holiday Island/Adventure/ENU/SFX/SFX_PLAYER_CANT_SHOOT.aac', 1, 2)


# Generated at 2022-06-14 18:05:23.481827
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # If the execution of the function os.utime raises an exception, it will be
    # caught and a warning message will be displayed in the log of ytdl.
    pp = PostProcessor()

    class Test:
        def report_warning(self, errnote):
            self.warning = errnote
    t = Test()

    pp._downloader = t
    pp.try_utime(1, 1, 1)
    assert t.warning == 'Cannot update utime of file'

    # If the execution of the function os.utime does not raise an exception,
    # it will not be caught and then the return value of the function is None.
    pp = PostProcessor()

    class Test2:
        def report_warning(self, errnote):
            self.warning = errnote
    t2 = Test2()

    pp

# Generated at 2022-06-14 18:05:31.143205
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.f4m import F4mFD
    from ..utils import DateRange
    from .common import FileDownloader

    fd = F4mFD()
    with open('test.f4m', 'w') as f:
        f.write('''<manifest xmlns="http://ns.adobe.com/f4m/1.0">
                    <id>test</id>
                    <mimeType>video/mp4</mimeType>
                    <streamType>recorded</streamType>
                    <baseURL>http://example.com/video</baseURL>
                </manifest>''')

    fd.add_info_extractor('http://example.com/video',
                          'utils.tests.test_postprocessor.f4m_download_stub')

# Generated at 2022-06-14 18:05:36.184783
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(downloader=None)
    st = os.stat('ffmpeg.py')
    os.remove('ffmpeg.py')
    pp.try_utime('ffmpeg.py', st.st_atime, st.st_mtime)
    os.utime(encodeFilename('ffmpeg.py'), st)

# Generated at 2022-06-14 18:05:47.197612
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    print('[ut] Test PostProcessor.try_utime')
    import datetime
    a = PostProcessor()
    import tempfile
    fpath = tempfile.mktemp()
    with open(fpath, 'a'):
        pass
    import time
    atime = time.time() - 100
    mtime = time.time() - 100
    a.try_utime(fpath, atime, mtime)
    stat = os.stat(encodeFilename(fpath))
    if datetime.datetime.fromtimestamp(stat.st_mtime) > datetime.datetime.now():
        a.try_utime(fpath, atime, mtime, 'Unit test fail: Cannot update utime of file')
    else:
        print('[ut] Success')

# Generated at 2022-06-14 18:05:56.284451
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .test_utils import FakeDownloader
    from . import NullPostProcessor
    from .extractor.common import InfoExtractor
    from .compat import compat_path

    class FakeInfoExtractor(InfoExtractor):
        def _real_extract(self, url):
            return {'id': 'fake', 'filepath': self._TEST_FILEPATH}

    class FakePostProcessor(NullPostProcessor):
        _TEST_FILEPATH = compat_path(os.path.join(os.path.dirname(__file__), '__main__.py'))

        def try_utime(self, path, atime, mtime, errnote=''):
            assert self._TEST_FILEPATH == path
            assert os.path.exists(path)

# Generated at 2022-06-14 18:06:01.803371
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader
    from ..utils import DateRange
    downloader = FileDownloader(params={'dateafter': DateRange('now-2h')})
    pp = PostProcessor(downloader)
    pp.try_utime('', 0, 0)
    pp.try_utime('', 0, 0, errnote='Hello world')

# Generated at 2022-06-14 18:06:13.202958
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    TEST_FILE_PATH = os.path.join(os.path.dirname(__file__), 'test.mp4')
    TEST_UNKNOWN_PATH = os.path.join(os.path.dirname(__file__), 'test_unknown.mp4')
    TEST_UTIME = 1234567890

    def get_utime(path):
        return os.stat(path).st_ctime

    def check_utime(path, utime):
        assert get_utime(path) == utime

    pp = PostProcessor(None)
    pp.try_utime(TEST_FILE_PATH, TEST_UTIME, TEST_UTIME)
    check_utime(TEST_FILE_PATH, TEST_UTIME)

    # Unknown file

# Generated at 2022-06-14 18:06:24.179695
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import datetime
    import tempfile

    def mk_mtime(year=2000, month=1, day=1, hour=0, minute=0, second=0):
        return datetime.datetime(year, month, day, hour, minute, second, tzinfo=datetime.timezone.utc).timestamp()

    def mk_fname():
        return tempfile.mktemp()

    # file does not exist - error report is issued
    fname = mk_fname()
    pp = PostProcessor(None)
    pp.try_utime(fname, mk_mtime(), mk_mtime())

    # file exists - no error report is issued
    with open(fname, 'w') as f:
        pass

# Generated at 2022-06-14 18:06:31.653941
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyDownloader(object):
        def __init__(self):
            self.params = {}

        def report_warning(self, msg):
            self.msg = msg

    pp = PostProcessor(DummyDownloader())

    pp.try_utime('file', 1, 2)

    downloader = DummyDownloader()
    pp = PostProcessor(downloader)

    pp.try_utime('file', 1, 2)
    assert downloader.msg == 'Cannot update utime of file'
    pp.try_utime('file', 1, 2, 'Can not foo')
    assert downloader.msg == 'Can not foo'

# Generated at 2022-06-14 18:06:34.615527
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime('/tmp/1', 1, 2)
    pp.try_utime('/tmp/2', 2, 1)

# Generated at 2022-06-14 18:06:39.526526
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import shutil
    import sys

    orig_time = time.time()
    postprocessor = PostProcessor()
    tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 18:06:49.216442
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader

    from .common import get_testdata_dir
    from .test_common import make_tempdir

    def test_utime_write_fail(self, info, expected_files, expected_result, utime_fail_reason):
        pp = PostProcessor(self)
        outdir = make_tempdir()
        info['filepath'] = os.path.join(outdir, 'test.mp4')
        with open(info['filepath'], 'w') as fh:
            fh.write('test')
        info['title'] = 'test'

        pp.try_utime = MagicMock(side_effect=pp.try_utime)

# Generated at 2022-06-14 18:06:55.793827
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Unit test for method try_utime of class PostProcessor
    """
    # pylint: disable = no-member
    from youtube_dl.YoutubeDL import YoutubeDL
    from tempfile import NamedTemporaryFile
    import atexit
    import time
    import os

    aff = NamedTemporaryFile(delete=False)
    aff.close()
    atexit.register(os.remove, aff.name)

    class DummyYoutubeDL(YoutubeDL):
        def report_warning(self, msg):
            pass

        def to_screen(self, msg):
            pass

    p = PostProcessor(DummyYoutubeDL())

    # Touch file
    with open(aff.name, 'a'):
        os.utime(aff.name, None)

    time.sleep(2)  # make

# Generated at 2022-06-14 18:07:05.702781
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .youtube_dl.downloader.common import FileDownloader
    from .youtube_dl.utils import DateRange
    from .youtube_dl.postprocessor.common import PostProcessor
    from .youtube_dl.compat import PY2
    from os.path import join

    if PY2:
        # There is no error "File exists" in python2
        expected_error_message = 'Cannot update utime of file'
        open_mode = 'wb'
    else:
        expected_error_message = 'Cannot update utime of file: [Errno 17] File exists'
        open_mode = 'w'


# Generated at 2022-06-14 18:07:09.156923
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    pp = PostProcessor(Downloader({}))
    pp.try_utime('/non/existent/file', 1422809029, 1422809030)  # won't raise an exception

# Generated at 2022-06-14 18:07:10.073273
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """TO DO"""
    pass

# Generated at 2022-06-14 18:07:34.618089
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Create temporary file and directory
    from ..utils import make_tempdir_with_files, remove_tempdir_and_files
    (tmp_dir, tmp_file, _) = make_tempdir_with_files('tmp')

    # Create temporary file for post-processing
    with open(tmp_file, 'wb') as f:
        f.write(b'Test file')

    import datetime
    import time

    # Create PostProcessor
    class FakePostProcessor(PostProcessor):
        pass
    pp = FakePostProcessor()

    # Set downloader of PostProcessor
    class FakeDl():
        def report_warning(self, errnote):
            pass
    pp._downloader = FakeDl()

    # Check modification time of test file

# Generated at 2022-06-14 18:07:39.605913
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FileDownloader

    class FakePostProcessor(PostProcessor):
        def run(self, information):
            return self.try_utime('/dev/null', 0, 0)

    downloader = FileDownloader(None, None)
    downloader.add_post_processor(FakePostProcessor())
    downloader.download([{'url': 'http://127.0.0.1/'}])

# Generated at 2022-06-14 18:07:41.875040
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert 'Cannot update utime of file' in PostProcessor().try_utime('/path/to/file', 0, 0, 'Cannot update utime of file')

# Generated at 2022-06-14 18:07:48.186488
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange
    from ..downloader.f4m import F4mFD
    from ..compat import compat_setenv, compat_urllib_request
    import tempfile
    import os
    import sys
    old_env = compat_setenv('TZ', 'Europe/Madrid')

# Generated at 2022-06-14 18:07:54.190269
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader():
        def report_warning(self, errnote):
            assert errnote == 'Cannot update utime of file'
    fake_downloader = FakeDownloader()
    pp = PostProcessor(fake_downloader)
    pp.try_utime('/path/to/file', 1, 2)

# Generated at 2022-06-14 18:07:59.201739
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractors
    _downloader = gen_extractors()[_0_test]()
    pp = PostProcessor(_downloader)
    # TODO: write unit test (do not use other classes)


# Do not remove this line. It is used by tests/extractor/common.py
# and by tests/postprocessor/common.py
_0_test = 'youtube:_0_test'

# Generated at 2022-06-14 18:07:59.745683
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import t

# Generated at 2022-06-14 18:08:09.103625
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest
    import shutil
    import tempfile
    import os
    import time

    class TestPP1(PostProcessor):
        def run(self, info):
            with tempfile.NamedTemporaryFile() as fd:
                shutil.copyfile(info['filepath'], fd.name)
                self.try_utime(fd.name, 0.0, 0.0)

    class TestPP2(PostProcessor):
        def run(self, info):
            with tempfile.NamedTemporaryFile() as fd:
                shutil.copyfile(info['filepath'], fd.name)
                self.try_utime(fd.name, -1, -1)


# Generated at 2022-06-14 18:08:15.265713
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        # this is actually redundant, since the function is not supposed to fail
        os.utime(__file__, (0, 0))
    except OSError:
        # rewind time
        os.utime(__file__, (0, 0))

# Generated at 2022-06-14 18:08:23.178065
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    import time
    import tempfile
    import os
    import shutil
    import unittest

    # Create a fake file
    f = tempfile.NamedTemporaryFile()

    # Fake downloader
    class FakeDownloader():
        def report_warning(self, message):
            self.last_message = message

    # Fake postprocessor
    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            PostProcessor.__init__(self, downloader)

    pp = FakePostProcessor(FakeDownloader())

    # Store the original time
    orig_atime = time.time()
    
    # Only update the modified time
    new_mtime = orig_atime - 10

    # Do it