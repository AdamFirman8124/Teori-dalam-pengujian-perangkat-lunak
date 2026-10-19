

# Generated at 2022-06-14 17:58:32.351572
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)  # skip the downloader set, utime not called
    import time
    import tempfile
    temp_file = tempfile.NamedTemporaryFile()
    pp.try_utime(temp_file.name, time.time(), time.time(), 'Cannot update utime of file')

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 17:58:39.328323
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import FakeDownloader
    from tempfile import mkstemp
    from time import time

    _, filepath = mkstemp()

    p = PostProcessor(FakeDownloader())
    p.try_utime(filepath, 0, 0)

    # Check if time actually changed, so we know if try_utime works
    assert time() > 0
    assert os.stat(filepath).st_atime + os.stat(filepath).st_mtime > 0

    os.remove(filepath)

# Generated at 2022-06-14 17:58:41.597291
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        os.utime(__file__, None)
    except TypeError:
        pass
    else:
        raise TypeError('os.utime without tuple argument should raise a TypeError')

# Generated at 2022-06-14 17:58:45.621810
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MyPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            PostProcessor.__init__(self)
            self._downloader = downloader
    post_processor = MyPostProcessor()
    post_processor.try_utime('', 1, 2)

# Generated at 2022-06-14 17:58:46.205133
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 17:58:57.325708
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import pytest
    from ..utils import PostProcessor
    from ..downloader.common import _ANY_DOWNLOADER

    def recwarn(record):
        """
        Get the text of the warning message from a warnings.WarningMessage.
        https://docs.python.org/3.5/library/warnings.html#warnings.record.message
        """
        return record.message.args[0]

    testfile = 'testfile'
    p=PostProcessor(_ANY_DOWNLOADER)

    # Create a test file
    fd = open(testfile, 'w+')
    fd.close()

    # Get the current time
    atime_prev = time.time() - 60
    mtime_prev = time.time() - 120

# Generated at 2022-06-14 17:59:02.436162
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    try:
        os.remove(encodeFilename('tmp_file'))
    except OSError:
        pass
    with open(encodeFilename('tmp_file'), 'w') as tmp_file:
        tmp_file.write('a')
    from ..YoutubeDL import YoutubeDL
    pp = PostProcessor(YoutubeDL())
    pp.try_utime(encodeFilename('tmp_file'), 0, 0)

# Generated at 2022-06-14 17:59:10.497441
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile
    from time import sleep

    video = NamedTemporaryFile()
    info = {'title': 'test', 'ext': 'webm', 'filepath': video.name}
    postprocessor = PostProcessor(None)
    before_sleep = os.path.getmtime(video.name)
    sleep(1) # Sleep to ensure that the system clock is updated.
    postprocessor.try_utime(video.name, 0, 0)
    after_sleep = os.path.getmtime(video.name)

    assert before_sleep <= after_sleep, \
           "utime() not working properly, otherwise the test is broken"

# Generated at 2022-06-14 17:59:22.149554
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    from ..downloader import get_suitable_downloader

    params = {'postprocessor_args': []}
    downloader = get_suitable_downloader(params)
    pp = PostProcessor(downloader)
    mtime = os.path.getctime(__file__)
    atime = mtime + 10
    pp.try_utime(__file__, atime, mtime, errnote='could not update atime and mtime')

    assert abs(os.path.getmtime(__file__) - mtime) < 3
    assert abs(os.path.getatime(__file__) - atime) < 3

    pp.try_utime('nonExistentFile', mtime, atime, errnote='could not update atime and mtime')

# Generated at 2022-06-14 17:59:32.917805
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader(object):
        def __init__(self):
            self.params = {'verbose': true}
            self.trouble = []
            self.to_stderr_fn = self.to_stderr

        def to_stderr(self, message):
            self.trouble.append(message)

    import tempfile
    import os
    import time
    import shutil
    from ..utils import encodeFilename

    pp = PostProcessor(FakeDownloader())
    target_dir = tempfile.mkdtemp()
    target = os.path.join(target_dir, 'test.file')

# Generated at 2022-06-14 17:59:45.874785
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time
    import stat

    dir = tempfile.mkdtemp()
    f = open(os.path.join(dir, 'example'), 'w')
    f.write('test')
    f.close()
    pp = PostProcessor(None)
    pp.try_utime(os.path.join(dir, 'example'), 0, 0)
    assert os.stat(os.path.join(dir, 'example')).st_mtime == 0
    pp.try_utime(os.path.join(dir, 'example'), time.time(), time.time())
    assert os.stat(os.path.join(dir, 'example')).st_mtime == os.stat(os.path.join(dir, 'example')).st_atime
    os.chmod

# Generated at 2022-06-14 17:59:53.232925
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .YoutubeDL import YoutubeDL
    from .utils import DateRange

    import datetime
    import os
    import tempfile

    ydl = YoutubeDL({'quiet': True})

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.close()

    pp = PostProcessor(ydl)

    # Basic usage
    pp.try_utime(f.name, 0, 0)
    stats = os.stat(f.name)
    assert stats.st_atime == stats.st_mtime == 0

    # Test exceptions
    def _raise_os_error(*args):
        raise OSError
    pp.try_utime = _raise_os_error
    pp.try_utime(f.name, 0, 0)

    os.unlink(f.name)

# Generated at 2022-06-14 18:00:02.563587
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import (
        gen_extractors
    )
    from ..downloader import (
        gen_ydl
    )
    from urllib import (
        parse
    )
    from datetime import (
        datetime
    )
    import sys

    p = PostProcessor(gen_ydl())
    gen_extractors.gen_extractors(sys.modules[gen_extractors.__package__])
    gen_extractors.update_default_args(p._configuration_args)
    url = 'http://example.com/'
    atime = mtime = datetime.utcnow().replace(microsecond=0).isoformat()
    ie = gen_extractors.gen_extractor(parse.urlparse(url), p)
    ie.extract(url)


# Generated at 2022-06-14 18:00:13.317035
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import tempfile
    import time
    import unittest
    import sys

    if sys.version_info < (3,):
        from StringIO import StringIO
    else:
        from io import StringIO

    class FakeDownloader():
        def __init__(self):
            self.report_warning_count = 0
            self.params = {
                'updatetime': True
            }

        def report_warning(self, text):
            self.report_warning_count += 1

    class FakeInfo():
        def __init__(self, filename, upload_date=None, creation_date=None):
            self.filename = filename
            self.upload_date = upload_date
            self.creation_date = creation_date


# Generated at 2022-06-14 18:00:23.002342
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # TODO
    #from .. import YoutubeDL
    #def report_warning(...):
    #    assert False, 'report_warning should not be called'
    #def utime(...):
    #    assert False, 'utime should not be called'
    #PostProcessor._downloader = YoutubeDL(dict(verbose=True))
    #PostProcessor._downloader.report_warning = report_warning
    #os.utime = utime
    #PostProcessor().try_utime('', 0, 0)
    pass

# Generated at 2022-06-14 18:00:34.345587
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import calendar
    import time
    import os
    tmpdir = os.path.dirname(os.path.abspath(__file__))
    path_to_testfile = os.path.join(tmpdir, "test.file")

# Generated at 2022-06-14 18:00:39.186917
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(downloader=None)
    filepath = encodeFilename(os.path.abspath('__test.test'), True)
    with open(filepath, 'a'):
        pp.try_utime(filepath, 1, 2)
    os.remove(filepath)

# Generated at 2022-06-14 18:00:47.095927
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # No exception is rasied.
    class MockDownloader():
        def report_warning(self, text):
            assert text == 'Cannot update utime of file'
    pp = PostProcessor(MockDownloader())
    pp.try_utime('/dummy/path', 0, 0)
    pp.try_utime('/dummy/path', 0, 0, 'Cannot update utime of file')
    # Other exception is rasied.
    pp = PostProcessor()
    test = False
    try:
        pp.try_utime('/dummy/path', 0, 0)
    except BaseException:
        test = True
    assert test

# Generated at 2022-06-14 18:00:54.265244
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import mock
    import shutil
    import tempfile
    downloader = mock.Mock()
    pp = PostProcessor(downloader)
    tmpdir = tempfile.mkdtemp()
    open(os.path.join(tmpdir, 'tmpfile'), 'w').close()
    pp.try_utime(os.path.join(tmpdir, 'tmpfile'), 100, 200)
    shutil.rmtree(tmpdir)

# Generated at 2022-06-14 18:01:06.905633
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    from ..downloader import Downloader
    from ..compat import compat_atime, compat_mtime
    filename = None

# Generated at 2022-06-14 18:01:21.853055
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import tempfile
    import time
    import unittest

    from file_utils import sanitize_open
    from postprocessor import PostProcessor
    from ytdl_options import FakeYDL

    class TestPP(PostProcessor):
        def __init__(self, test):
            self.test = test
            PostProcessor.__init__(self, FakeYDL())

    class TestPostProcessor(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()
            self.td1 = os.path.join(self.tmpdir, 'td1')
            self.td2 = os.path.join(self.tmpdir, 'td2')
            self.td3 = os.path.join(self.tmpdir, 'td3')

# Generated at 2022-06-14 18:01:27.985761
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    try:
        pp = PostProcessor()
        pp.try_utime('x', 'y', 'z', 'errnote')
    except:
        assert sys.exc_info() == (None, None, None) #raise UnexpectedException("postprocessor.PostProcessor.try_utime: Expected None")
    else:
        assert False, "postprocessor.PostProcessor.try_utime: Expected Exception"

# Generated at 2022-06-14 18:01:28.601404
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:01:35.419128
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import time
    import unittest

    def dummy_report_warning(warning):
        print(warning, file=sys.stderr)
        warnings.append(warning)

    warnings = []
    p = PostProcessor(None)
    p.set_downloader({'params': {}})
    p._downloader.report_warning = dummy_report_warning


# Generated at 2022-06-14 18:01:39.041468
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import NamedTemporaryFile
    from time import time, sleep
    from os.path import getmtime

    f = NamedTemporaryFile(delete=True)
    name = f.name
    t = time() - 1000  # last access time 1000 seconds ago
    PostProcessor(None).try_utime(name, t, t)

    # Some filesystems have coarse timestamp granularity
    # Allow a 1 second window
    assert abs(getmtime(name) - t) <= 1.0
    os.unlink(name)

# Generated at 2022-06-14 18:01:43.716315
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from ..extractor.common import InfoExtractor

    class DummyIE(InfoExtractor):
        def _real_extract(self, url):
            self.to_screen('DummyIE: ' + url)
            return {'id': 'foo',
                    'url': 'bar',
                    'title': 'foo',
                    'ext': 'ogg',
                    'upload_date': 'today',
                    'uploader': 'me',
                    'duration': 10}

    class DummyPostProcessor(PostProcessor):
        def run(self, info):
            self.try_utime('nonexistent_file', 0, 0, 'Cannot update utime of file')
            return [], info

    dl = Downloader(params={'verbose': True})
    dl.add_

# Generated at 2022-06-14 18:01:55.906671
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    from .downloader import FileDownloader
    from .extractor import YoutubeIE

    # test utime function of class PostProcessor
    #   - create PostProcessor
    #   then call try_utime() with the following arguments:
    #       - path: 'test.txt'
    #       - atime: int(time.time()) - 10
    #       - mtime: int(time.time()) - 10
    #       - errnote: 'Cannot update utime of file'
    test = PostProcessor(downloader=FileDownloader(YoutubeIE()))
    atime = int(time.time()) - 10
    mtime = int(time.time()) - 10
    test.try_utime('test.txt', atime, mtime, errnote='Cannot update utime of file')

# Generated at 2022-06-14 18:02:03.809945
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from tempfile import mkdtemp
    from shutil import rmtree
    from datetime import datetime
    import os

    tempdir = mkdtemp()
    dummy_file = os.path.join(tempdir, 'a file.txt')
    open(dummy_file, 'w').close()

    now = datetime.now()
    yesterday = datetime(now.year, now.month, now.day - 1)
    os.utime(dummy_file, (yesterday.timestamp(), yesterday.timestamp()))
    assert os.path.getmtime(dummy_file) < now.timestamp()


# Generated at 2022-06-14 18:02:15.143751
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # If a file already exists, os.utime should update its access and
    # modified time. Otherwise, os.utime should throw an OSError.
    class PostProcessor_try_utime(PostProcessor):
        # Note: The downloader is not necessary for this test.
        def run(self, information):
            assert information['__type'] == 'file'
            assert information['filepath'] == 'fake_filepath'

            atime, mtime = information['time']
            self.try_utime(information['filepath'], atime, mtime)

            assert os.path.getatime('fake_filepath') == atime
            assert os.path.getmtime('fake_filepath') == mtime


# Generated at 2022-06-14 18:02:27.244180
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import time
    import tempfile
    import shutil

    # Create a temporary directory
    temp_directory = tempfile.mkdtemp()

    # Create a temporary file
    file_path = os.path.join(temp_directory, "temp_file.tmp")

    def touch(fname, times=None):
        with open(fname, 'a'):
            os.utime(fname, times)


# Generated at 2022-06-14 18:02:42.804377
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time, datetime
    from random import randint
    from tempfile import NamedTemporaryFile
    from youtube_dl.utils import DateRange, DateRangeError
    import youtube_dl.postprocessor

    def daterange_to_utime(dr, t):
        return (
            time.mktime(datetime.datetime.combine(dr.start, datetime.time.min).timetuple())
            if dr.start is not None
            else t,
            time.mktime(datetime.datetime.combine(dr.end, datetime.time.max).timetuple())
            if dr.end is not None
            else t,
        )

    pp = youtube_dl.postprocessor.PostProcessor(downloader=None)
    with NamedTemporaryFile() as tf:
        pp.try_utime

# Generated at 2022-06-14 18:02:46.493772
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    pp.try_utime('/doesnotexist', 0, 0)
    # We cannot really test if the utime was successful

# Generated at 2022-06-14 18:02:56.659697
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    from time import time
    from ..utils import temp_filename

    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            self._downloader = downloader

    temp_dir = temp_filename('', '')
    os.mkdir(temp_dir)
    pp = TestPostProcessor()
    try:
        temp_file = temp_filename(os.path.join(temp_dir, 'test'), '.mp4')
        f = open(temp_file, 'w')
        f.close()
        pp.try_utime(temp_file, time(), time() - 2000)
    except:
        raise
    finally:
        shutil.rmtree(temp_dir)

# Generated at 2022-06-14 18:03:06.215433
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    from .fake_filesystem_unittest import Patcher
    from .utils import (
        check_executable,
    )
    import sys

    if not check_executable('ffmpeg', ['-codecs']):
        sys.exit('ffmpeg not found in PATH, skipping ffmpeg PostProcessor unit test')

    import tempfile
    import shutil
    import stat
    import errno
    import os
    import subprocess

    tempdir = tempfile.mkdtemp()

    patcher = Patcher()
    patcher.setUp()

    if hasattr(os, 'chmod'):
        patcher.fs.add_real_directory(tempdir)
    else:
        patcher.fs.add_entity(tempdir, target_entity=None, is_dir=True)


# Generated at 2022-06-14 18:03:08.778474
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    assert(pp.__class__ is PostProcessor)
    pp.try_utime("./test_result/test_file", 1, 1)

# Generated at 2022-06-14 18:03:21.595579
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor.common import InfoExtractor
    from ..downloader import common
    import copy
    import datetime
    import time
    import unittest
    import shutil
    import tempfile

    class TestIE(InfoExtractor):
        def report_warning(self, msg, video_id=None):
            self.msgs.append(msg)
            self.video_ids.append(video_id)
            self.num_warnings += 1

        def _real_extract(self, url):
            raise Exception('should not be called')

        def extract(self, url):
            self.msgs = []
            self.video_ids = []
            self.num_warnings = 0
            return InfoExtractor._real_extract(self, url)


# Generated at 2022-06-14 18:03:29.481210
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime, filecmp, os, shutil, tempfile
    from ..utils import DateRange, str_to_time

    ref_file = 'tests/testdata/test.flv'
    ref_file_stat = os.stat(ref_file)

    tmpdir = tempfile.mkdtemp()
    tmp_file = os.path.join(tmpdir, 'test.flv')


# Generated at 2022-06-14 18:03:39.485823
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL

    class TestPP(PostProcessor):
        def run(self, info):
            # Get the filename
            filename = info['filepath']
            # Try to set the utime of the file
            self.try_utime(filename, 0, 0)
            return [], info

    # Create downloader
    dummy_ydl = YoutubeDL({})
    dummy_ydl.add_post_processor(TestPP(dummy_ydl))
    # Create temporary file
    import tempfile
    (_, fname) = tempfile.mkstemp(prefix='YoutubeDL-test_PostProcessor_try_utime-')
    # Download the file
    dummy_ydl.process_info({
        'id': 'test',
        'filepath': fname,
    })



# Generated at 2022-06-14 18:03:48.516975
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import shutil
    import time
    from ..utils import PostProcessor

    cwd = os.getcwd()
    workdir = tempfile.mkdtemp(prefix=__name__ + '-', suffix='-workdir')


# Generated at 2022-06-14 18:03:51.290221
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    p = PostProcessor(None)
    p._downloader = _FakeDownloader()
    p.try_utime('a/b/c', 0, 0)


# Generated at 2022-06-14 18:04:15.033939
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestPostProcessor(PostProcessor):
        def run(self, information):
            self.try_utime(information['filepath'], information['utime'], information['utime'])
            return [], information

    from .test_downloader import FakeInfoExtractor
    from .extractor import InfoExtractor
    from .downloader import YoutubeDL

    test_downloader = YoutubeDL({'postprocessor_args': '-ar 44100 -ac 2'})
    test_ie = FakeInfoExtractor()
    test_downloader.add_info_extractor(test_ie)
    test_pp = TestPostProcessor(test_downloader)
    test_downloader.add_post_processor(test_pp)

    # Test when file is not exist

# Generated at 2022-06-14 18:04:20.942357
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .downloader import downloader

    def test_postprocessor(downloader):

        from .YoutubeDL import PostProcessor

        pp = PostProcessor(downloader)
        pp.try_utime('file.txt', mtime=0, atime=0)

    try:
        test_postprocessor(downloader)
    except:
        print('test_PostProcessor_try_utime failed')
        return False

    return True

# Generated at 2022-06-14 18:04:31.590452
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil

    from ..downloader.common import FileDownloader
    fd = FileDownloader({})
    fd.params['outtmpl'] = '%(title)s.%(ext)s'
    fd._prepare_and_start_download = lambda *args: None

    def dummy(*args):
        downloaded = args[0][1]
        with open(downloaded, 'w') as f:
            f.write('Hello World')

    fd.to_screen = lambda *args: None
    fd.temp_name = dummy
    fd.report_warning = lambda *args: None

    pp = PostProcessor(fd)

    filename = u'a\ufeffb'
    with open(filename, 'wb') as f:
        f.write(b'hello world')

# Generated at 2022-06-14 18:04:33.622650
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    return True

# Generated at 2022-06-14 18:04:45.023957
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader
    from ..utils import DateRange
    # test for warning

# Generated at 2022-06-14 18:04:55.108949
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import time
    import stat
    import shutil
    import tempfile
    from ..YoutubeDL import YoutubeDL
    # Create a temporary directory
    tempdir = tempfile.mkdtemp()
    pp = PostProcessor(YoutubeDL({}))
    # Create a file
    thefile = os.path.join(tempdir, "toto")
    with open(thefile, "wb") as f:
        f.write(b'foo')
    # Set a modification time 5 secs ago
    f = os.stat(thefile)
    oldmtime = f.st_mtime
    oldatime = f.st_atime
    os.utime(thefile, (f.st_atime, oldmtime - 5))
    f = os.stat(thefile)

# Generated at 2022-06-14 18:05:02.895968
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    t = PostProcessor()
    with open('./test_utime', 'w') as f:
        # create a file, then set its modification time back to the past
        f.write('test')
        t.try_utime('./test_utime', 1, 1)

    os.remove('./test_utime')
    if os.path.exists('./test_utime'):
        raise Exception('test_utime was not created or is not removed')

# Generated at 2022-06-14 18:05:04.774818
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    #TODO
    #https://github.com/rg3/youtube-dl/issues/8020
    pass

# Generated at 2022-06-14 18:05:12.144278
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import stat

    # Prepare a dummy PostProcessor
    pp = PostProcessor(None)

    # Create a dummy file with a specific atime and mtime
    from ..utils import DateRange
    from .common import temp_name
    from .common import DummyYDL
    tmpf = temp_name(suffix='.tmp')
    with open(tmpf, 'wb') as f:
        f.write(b'Hello')
    now = DateRange().start_time()
    atime, mtime = now, now - 10
    os.utime(tmpf, (atime, mtime))

    # Check that the file content is consistent
    assert os.path.getsize(tmpf) == 5
    assert os.stat(tmpf).st_mode & stat.S_IFREG != 0

    # Try

# Generated at 2022-06-14 18:05:16.951583
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyDownloader(object):
        def report_warning(self, *args, **kwargs):
            self.warn = True
    p = PostProcessor(DummyDownloader())
    p.try_utime('file', atime=0, mtime=0, errnote='error')
    assert p._downloader.warn is True

# Generated at 2022-06-14 18:05:51.707622
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():

    # Unit test requires to have a _downloader object
    PostProcessor._downloader = object()

    import tempfile
    import time

    fd, fname = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write('test')
    f.close()

    assert os.stat(fname).st_atime != os.stat(fname).st_mtime

    PostProcessor().try_utime(fname, os.stat(fname).st_mtime, os.stat(fname).st_atime)

    assert os.stat(fname).st_atime == os.stat(fname).st_mtime
    assert os.stat(fname).st_atime != time.time()

    os.remove(fname)


# Generated at 2022-06-14 18:05:59.393104
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import PostProcessingError
    pp = PostProcessor()

    # Make sure that method try_utime of class PostProcessor
    # does not raise an exception, because the file /some_random_file
    # will not exist
    pp.try_utime(path='/some_random_file', atime=10, mtime=10)

if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:06:05.016786
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    """Tests the method try_utime"""
    #Try to set utime of a file
    post_processor = PostProcessor()
    post_processor.try_utime("README.md", 0, 0, errnote="")

    #Try to set utime of a non existing file
    #Post-9.0 versions of youtube-dl raise an exception, we need to catch it
    try:
        post_processor.try_utime("", 0, 0, errnote="")
    except AudioConversionError:
        pass

# Generated at 2022-06-14 18:06:10.950831
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from .common import (
        FakeYDL,
    )

    ydl = FakeYDL(params={'writedescription': False, 'outtmpl': 'test_%(id)s_%(ext)s'})
    fd = FileDownloader(ydl, {})
    pp = PostProcessor(fd)
    pp.try_utime('test_ABC_REQUEST', 1374148701.0, 1374148801.0)



# Generated at 2022-06-14 18:06:22.802892
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import shutil
    import stat

    class TestPP(PostProcessor):
        def run(self, information):
            self.try_utime('nonExistingFile', 1, 1)
            self.try_utime('nonExistingFileDir/nonExistingFile', 1, 1, 'Cannot u')

    temp_path = os.path.realpath(os.path.join(os.getcwd(), 'temp_test_PostProcessor'))


# Generated at 2022-06-14 18:06:24.255816
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp.try_utime('video.jpg', 0, 0)

# Generated at 2022-06-14 18:06:32.845197
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .test_postprocessor import MockYDL
    from ..utils import DateRange

    ydl = MockYDL()

    t2k = DateRange('2000').end_of_day()
    t3k = DateRange('3000').end_of_day()

    pp = PostProcessor(ydl)

    # test with a good file
    pp.try_utime('/tmp/test.tmp', t2k, t2k, 'Cannot update utime of file')

    # test with a not existing file
    pp.try_utime('/tmp/fake.tmp', t3k, t3k, 'Cannot update utime of file')

    # assert that the warning has been reported
    assert ydl.from_test_warning == ['Cannot update utime of file']

# Generated at 2022-06-14 18:06:33.422202
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:06:44.049633
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import mkdtemp
    from shutil import rmtree
    from datetime import datetime
    import time

    import os
    import pytest

    from .common import FileDownloader

    class TestPP(PostProcessor):
        def __init__(self, *args, **kwargs):
            super(TestPP, self).__init__(*args, **kwargs)

    @pytest.fixture
    def test_dir():
        path = mkdtemp()
        yield path
        rmtree(path)

    @pytest.fixture
    def test_fp(test_dir):
        path = os.path.join(test_dir, 'test')

        with open(path, 'w') as f:
            pass

        yield path

    def get_modified_time(path):
        return datetime

# Generated at 2022-06-14 18:06:55.370946
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    '''
    test for method try_utime of class PostProcessor
    '''
    tempfile = __import__('tempfile')
    tempfile.tempdir = None

# Generated at 2022-06-14 18:07:55.947895
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Test PostProcessor method try_utime."""
    pp = PostProcessor(None)
    pp.try_utime('nonexistent-file.xyz')
    try:
        pp.try_utime('nonexistent-file.xyz', errnote=None)
    except Exception:
        pass
    else:
        assert False, 'Exception expected'

# Generated at 2022-06-14 18:08:06.047494
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    # We don't use a standard temporary file (tempfile.NamedTemporaryFile)
    # because it creates an open file descriptor that may not be writable.
    # We'd also have to close the descriptor before calling os.utime, but we
    # wouldn't be able to delete the file then.
    (fd, path) = tempfile.mkstemp(prefix='youtubedl-test_')
    os.close(fd)

# Generated at 2022-06-14 18:08:13.007826
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader:
        def report_warning(self, msg):
            pass

    class FakePostProcessor:
        def __init__(self, downloader):
            self._downloader = downloader


    postprocessor = FakePostProcessor(FakeDownloader())

    path = 'test'
    atime = 1
    mtime = 2
    errnote = 'test'

    try:
        os.utime(path, (atime, mtime))
    except Exception:
        postprocessor.try_utime(path, atime, mtime, errnote)


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:08:20.974230
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    Creates a postprocessor instance, and print out its
    utime error message

    Can be called via the following command:
    youtube-dl --rm-cache-dir --no-post-overwrites -o '%(id)s.%(ext)s' --postprocessor-args '-caption_file' --write-auto-sub --skip-download 'https://www.youtube.com/watch?v=D5b5G5Zt-WI'
    """

    post_processor = PostProcessor()
    post_processor.try_utime('/test/test', 1, 1)


if __name__ == '__main__':
    test_PostProcessor_try_utime()

# Generated at 2022-06-14 18:08:29.494817
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    from ..downloader.common import FileDownloader
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange
    downloader = FileDownloader(params={'verbose': True, 'progress_with_newline': False})
    downloader.add_info_extractor(InfoExtractor)
    pp = PostProcessor(downloader)
    # test_time is the time we will set it to.  It's arbitrary.
    test_time = 1364015165.11
    # test_file just needs to exist, with a null modification time.
    test_file = 'test_file'
    open(test_file, 'a').close()  # make it
    os.utime(encodeFilename(test_file), (0,0))  # set the modification time to 0