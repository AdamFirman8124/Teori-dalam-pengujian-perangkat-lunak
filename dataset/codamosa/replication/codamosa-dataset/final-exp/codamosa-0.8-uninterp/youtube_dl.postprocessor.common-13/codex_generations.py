

# Generated at 2022-06-14 17:58:31.225097
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert True

# Generated at 2022-06-14 17:58:41.022794
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    if os.name == 'nt':
        import time
        import py
        py.test.skip("mtimes not supported on windows.")

    import tempfile
    testfn = tempfile.mkstemp()[1]

    pp = PostProcessor(None)
    # Test utime with same mtime and atime
    time_start = time.time()
    time_end = time_start + 5
    pp.try_utime(testfn, time_start, time_end)
    atime, mtime = os.stat(testfn).st_atime, os.stat(testfn).st_mtime
    # Time on filesystems not supporting subsecond resolution
    # is floored to full seconds.
    assert ((atime - time_start) < 2)
    assert ((mtime - time_end) < 2)

   

# Generated at 2022-06-14 17:58:51.082429
# Unit test for method try_utime of class PostProcessor

# Generated at 2022-06-14 17:58:53.441161
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    assert pp.try_utime('file_not_exists.mp3', 1, 2) == None

# Generated at 2022-06-14 17:58:54.401866
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    assert True

# Generated at 2022-06-14 17:59:02.235872
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    from ..PostProcessor import PostProcessor
    import tempfile
    import sys

    if sys.version_info[:2] < (2, 7):
        return

    # Create temp file
    temp_f = tempfile.NamedTemporaryFile()
    temp_f.close()

    # Create a PostProcessor
    post_processor = PostProcessor(YoutubeDL())

    # modify utime of temp file
    post_processor.try_utime(temp_f.name, 0, 0)

    # remove temp file
    temp_f.close()



# Generated at 2022-06-14 17:59:07.040493
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile

    # Writing a binary file
    stat = os.fstat(tempfile.mkstemp()[0])
    # PostProcessor.try_utime should handle the binary files
    try:
        os.utime('/tmp', (stat.st_atime, stat.st_mtime))
    except OSError:
        pass

# Generated at 2022-06-14 17:59:14.382441
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import file_size
    from .testcases import PostProcessorTestCase

    pp = PostProcessorTestCase()
    pp.test_dir = os.path.join(os.path.dirname(__file__), 'test_files')
    pp.test_filename = 'test_file.ts'
    pp.test_filepath = os.path.join(pp.test_dir, pp.test_filename)
    size = file_size(pp.test_filepath)
    atime = os.path.getatime(pp.test_filepath)
    mtime = os.path.getmtime(pp.test_filepath)

    pp.assertFalse(os.path.getmtime(pp.test_filepath) != mtime)

# Generated at 2022-06-14 17:59:24.034247
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyFile(object):
        """Dummy File-like object"""
        _contents = None

        def __init__(self, contents):
            self._contents = contents

        def read(self):
            return self._contents

    class DummyDownloader(object):
        """Dummy Downloader"""
        def report_warning(self, warning):
            pass

    dummy_contents = b'hello'
    dummy_file = DummyFile(dummy_contents)
    p = PostProcessor(DummyDownloader())
    filename = 'dummy'
    with open(filename, 'wb') as f:
        f.write(dummy_contents)
    p.try_utime(filename, 1, 1)

# Generated at 2022-06-14 17:59:27.468065
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    path = tempfile.mkstemp()[1]
    atime = time.time()
    mtime = time.time()
    pp = PostProcessor(None)
    pp.try_utime(path, atime, mtime)

# Generated at 2022-06-14 17:59:38.501641
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil
    import stat
    import os

    def safe_utime(path, atime, mtime):
        try:
            os.utime(encodeFilename(path), (atime, mtime))
        except Exception:
            pass

    temp_dir = tempfile.mkdtemp(prefix='youtube-dl-utime')

# Generated at 2022-06-14 17:59:41.153333
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # i.e. it does not raise an exception
    PostProcessor().try_utime('/doesnotexist', 0, 0)

# Generated at 2022-06-14 17:59:51.684119
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """
    This test is a bit hacky, but it works.
    """
    import tempfile
    import time

    # Prepare a file (create and write)
    fd, temppath = tempfile.mkstemp()
    os.write(fd, b'foobarbaz')
    os.close(fd)

    # Get the current time
    starttime = time.time()

    # Create a PostProcessor object
    pp = PostProcessor()

    # Update the time
    pp.try_utime(temppath, time.time(), time.time())

    # Check if the time has been updated (one second resolution is enough)
    endtime = os.path.getmtime(temppath)
    os.unlink(temppath)
    del pp

    assert starttime <= endtime

# Generated at 2022-06-14 18:00:02.449361
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import shutil
    import os
    tempdir = tempfile.gettempdir()
    tempfile = os.path.join(tempdir, "postprocessor_test_tempfile.test")
    postprocessor = PostProcessor()
    with open(tempfile, 'w') as f:
        f.write("1")
    postprocessor.try_utime(tempfile, 0, 0)
    assert(os.path.exists(tempfile))
    os.remove(tempfile)

    # test that the file is not deleted when an exception is raised
    with open(tempfile, 'w') as f:
        f.write("1")

# Generated at 2022-06-14 18:00:10.345958
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    from .mock import MockYDL

    ydl = MockYDL()
    now = time.time()
    pp = PostProcessor(ydl)
    pp.try_utime('filename', now, now + 10)

    assert 'Cannot update utime of file' in ydl.warned

    ydl.warned = []
    pp.try_utime('filename', 0, 0, '')
    assert len(ydl.warned) == 0

# Generated at 2022-06-14 18:00:13.435447
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class TestDownloader:
        def report_warning(self, msg):
            raise PostProcessingError(msg)
    class TestPostProcessor(PostProcessor):
        pass
    tpp = TestPostProcessor(downloader=TestDownloader())
    tpp.try_utime("", 0, 0)

# Generated at 2022-06-14 18:00:25.968408
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    from pytube import Downloader, PostProcessor
    from .testsupport import TstBasic

    class FakeDownloader(Downloader):  # pylint:disable=too-few-public-methods
        """FakeDownloader that just saves the parameters it was called with
        for later inspection."""
        def __init__(self):
            self.was_called_with = None  # pylint:disable=attribute-defined-outside-init
        def to_screen(self, msg):
            pass
        def report_warning(self, msg):
            self.was_called_with = msg

    class FakePostProcessor(PostProcessor):
        """FakePostProcessor that just delegates the utime call to the
        instance of FakeDownloader that was given in the constructor."""

# Generated at 2022-06-14 18:00:29.325214
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class FakeDownloader():
        def report_warning(self, note):
            self.called = note
    pp = PostProcessor(downloader=FakeDownloader())
    pp.try_utime(__file__, None, None)
    assert pp._downloader.called == 'Cannot update utime of file'

# Generated at 2022-06-14 18:00:37.757297
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    from ..compat import compat_os_name

    class FileUtimesError(IOError):
        def __init__(self, filepath):
            self.strerror = 'No access to {}'.format(filepath)
            self.filename = filepath

    class PostProcessorTest(PostProcessor):
        _downloader = None
        _filepath = ''
        _atime = 0
        _mtime = 0

        def __init__(self, downloader=None, filepath='', atime=0, mtime=0):
            self._downloader = downloader
            self._filepath = filepath
            self._atime = atime
            self._mtime = mtime


# Generated at 2022-06-14 18:00:38.988957
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # ToDo: write unit test
    pass

# Generated at 2022-06-14 18:00:45.649069
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class Mock_downloader(object):
        def report_warning(self, errnote='Cannot update utime of file'):
            pass
    class Mock_PostProcessor(PostProcessor):
        def __init__(self, downloader=None):
            super(Mock_PostProcessor, self).__init__(downloader)
    pp = Mock_PostProcessor(Mock_downloader())
    pp.try_utime('', 0, 0)

# Generated at 2022-06-14 18:00:54.762192
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader.common import FileDownloader
    from ..utils import DateRange
    from .embedthumbnail import EmbedThumbNailPP
    from .xattrpp import XAttrMetadataPP

    fd = FileDownloader({
        'outtmpl': '%(id)s',
        'check_date_range': DateRange(),
        'writethumbnail': True,
        'writeinfojson': True,
        'writedescription': True,
        'writeannotations': True,
        'writeinfojson': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'allsubtitles': True,
        'embedsubtitles': True,
        'embedthumbnail': True,
        'simulate': True
    })

    # Add some pp
    fd

# Generated at 2022-06-14 18:01:07.027776
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockPostProcessor(PostProcessor):
        def __init__(self):
            self.errnote = None

        def report_warning(self, errnote):
            self.errnote = errnote

    post_processor = MockPostProcessor()
    with open('./test_PostProcessor_try_utime', 'w') as f:
        f.write('')

    post_processor.try_utime('./test_PostProcessor_try_utime', 10, 20)
    assert post_processor.errnote is None

    post_processor.try_utime('./test_PostProcessor_try_utime', 10, 20, 'This is a warning message')
    assert post_processor.errnote == 'This is a warning message'


# Generated at 2022-06-14 18:01:19.402122
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ytdl import YoutubeDL
    from ..compat import compat_os_rename

    class TestPostProcessor(PostProcessor):
        _path = None
        def __init__(self, *args, **kwargs):
            self._path = os.path.join(kwargs.get('tmp_dir'), "test_file.tmp")
            with open(self._path, "wb") as f:
                f.write(b"dummy")
            super(TestPostProcessor, self).__init__(*args, **kwargs)

        def run(self, information):
            os.utime(self._path, (0, 0))
            self.try_utime(self._path, 0, 0)
            return [], information


# Generated at 2022-06-14 18:01:31.660081
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # A mock downloader class with a counter for the number of times
    # the method 'report_warning' has been called.
    class MockDownloader(object):
        counter = 0
        def report_warning(self, msg):
            MockDownloader.counter += 1

    # A mock PostProcessor class with the method try_utime
    class MockPostProcessor(PostProcessor):
        pass

    # Validate that the class PostProcessor has the method try_utime
    assert hasattr(PostProcessor, 'try_utime')
    assert callable(getattr(PostProcessor, 'try_utime', None))

    # Create a mock downloader and a mock postprocessor object
    downloader = MockDownloader()
    postprocessor = MockPostProcessor(downloader=downloader)

    # Validate that the mock postprocessor object

# Generated at 2022-06-14 18:01:33.198335
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    assert pp.try_utime(__file__, 0, 0) is None

# Generated at 2022-06-14 18:01:38.131968
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    fp = tempfile.NamedTemporaryFile(delete=False)
    pp = PostProcessor(None)
    pp.try_utime(fp.name, 0, 0, errnote=None)

# Generated at 2022-06-14 18:01:46.802433
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import shutil
    import subprocess
    import sys
    import tempfile

    if sys.platform.startswith('win'):
        import winsound
    else:
        import sounddevice as sd

    # Create a source file
    source_path = tempfile.NamedTemporaryFile('wb', suffix='.wav', delete=False).name
    if sys.platform.startswith('win'):
        winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
    else:
        sd.play(data=sd.chirp(200.0, f0=440.0, f1=1000.0, duration=1.0), samplerate=44100)
        sd.wait()

    # Create a target file

# Generated at 2022-06-14 18:01:58.616641
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import tempfile
    import os
    import shutil
    import stat
    import errno

    class MyPostProcessor(PostProcessor):
        def __init__(self):
            pass

    pp = MyPostProcessor()

    temp_dir = tempfile.mkdtemp()

    # utime can only be applied to files, so we try create a directory with
    # the same name as a file and try to apply utime on that directory.
    testfile = os.path.join(temp_dir, 'testfile')
    testdir = os.path.join(temp_dir, 'testfile')


# Generated at 2022-06-14 18:02:02.425923
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    os.utime('', (0, 0))

# vim: expandtab:sw=4:ts=4

# Generated at 2022-06-14 18:02:10.871849
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class Downloader():
        class FileDownloader():
            def report_error(self, message):
                raise PostProcessingError(message)
        def report_warning(self, message):
            pass
    class MetadataFromTitlePP(PostProcessor):
        pass
    filer = MetadataFromTitlePP(Downloader())
    filer.try_utime('fakepath', 2, 1)

# Generated at 2022-06-14 18:02:18.939695
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class Options(object):
        def __init__(self):
            self.forcejson = None
    class Downloader(object):
        def __init__(self):
            self._config = Options()
            self.params = {'verbose': True}

        def report_warning(self, msg):
            pass
    d = Downloader()
    p = PostProcessor(d)

    d.params['forcejson'] = 'forcejson'
    p.try_utime('.', 1, 2)

    d.params['forcejson'] = None
    p.try_utime('non-exist-file', 1, 2)

# Generated at 2022-06-14 18:02:31.433159
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..compat import get_user_agent
    from ..compat import get_user_agent_platform
    from ..compat import matches_user_agent
    from ..compat import USER_AGENT_FORMAT
    from ..compat import USER_AGENT_PLATFORM_VERSION_REGEX
    from ..compat import USER_AGENT_PLATFORM_REGEX
    from ..downloader import Downloader
    from ..utils import get_cachedir
    from ..utils import get_platform
    from ..utils import prepend_extension
    from ..utils import prepend_extension_if_not_present

    import os
    import tempfile
    import shutil

    td = tempfile.mkdtemp()
    downloader = Downloader()
    postprocessor = PostProcessor(downloader)

    # Create a

# Generated at 2022-06-14 18:02:42.342124
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..downloader import Downloader

    class MockDownloader(Downloader):
        def report_warning(self, msg):
            self.msg = msg

    d = MockDownloader(params={'outtmpl': '%(id)s_%(extractor)s_%(title)s_%(format_id)s.%(ext)s', 'restrictfilenames': True, 'nooverwrites': True})
    p = PostProcessor(d)

    p.try_utime('a_b_c.d', 1, 2)
    assert(d.msg == "Cannot update utime of file")
    assert(d.msg == "Cannot update utime of file")

# Generated at 2022-06-14 18:02:54.141508
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.PostProcessor import PostProcessor
    import tempfile
    import time
    import os
    import stat
    import sys

    # Skip the test on Windows where we can't set file timestamp
    if sys.platform == 'win32':
        return

    with tempfile.TemporaryFile() as tf:
        tfname = tf.name
    p = PostProcessor(downloader=FileDownloader(params={}))
    fname = encodeFilename(tfname + '.test')
    open(fname, 'w').close()

    if os.name == 'nt':
        # it's impossible to set the time to a value in the past on windows
        p.try_utime(fname, 1, 15)
    else:
        p.try_ut

# Generated at 2022-06-14 18:03:03.742148
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from tempfile import TemporaryFile
    from ..compat import PY2

    class DummyDownloader(object):
        def report_warning(self, errnote):
            assert errnote == 'Cannot update utime of file', errnote

    if PY2:
        # os.utime on Python2 expects a filename of the type 'str' (bytes)
        f = TemporaryFile(mode='wb')
    else:
        # os.utime on Python3 expects a filename of the type 'str' (unicode)
        f = TemporaryFile(mode='w', encoding='utf-8')
    # Avoid 'BrokenPipeError: [Errno 32] Broken pipe' traceback on Python3
    f.close()
    fname = f.name
    pp = PostProcessor(DummyDownloader())
    pp.try_ut

# Generated at 2022-06-14 18:03:12.168790
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import os
    import time
    import shutil

    class DummyDownloader:
        def report_warning(self, note):
            pass

    def _test_try_utime_helper(path):
        assert os.path.exists(path)
        postprocessor = PostProcessor(DummyDownloader())
        postprocessor.try_utime(path, int(time.time()) + 1000, int(time.time() + 2000))
        assert os.stat(path).st_atime == int(time.time()) + 1000
        assert os.stat(path).st_mtime == int(time.time()) + 2000

    # Create a dummy file and do a test with it.
    dummy_file_path = tempfile.mkstemp()[1]

# Generated at 2022-06-14 18:03:19.573088
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time

    with tempfile.NamedTemporaryFile() as file:
        p = PostProcessor(None)
        p.try_utime(file.name, 0, 0) # should not raise any exception
        p.try_utime(file.name, 1, 1) # should not raise any exception

        time.sleep(1)
        p.try_utime(file.name, time.time(), time.time()) # should not raise any exception

# Generated at 2022-06-14 18:03:28.115289
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime
    from ..downloader.common import FileDownloader
    from ..YoutubeDL import YoutubeDL
    from .embedthumbnail import EmbedThumbnailPP
    from .__main__ import postprocessor_classes, gen_extractors

    # initialization
    ydl_opts = {
        'restrictfilenames': True,  # to set utime
        'writedescription': True,  # to test result
    }
    ydl = YoutubeDL(ydl_opts)
    gen_extractors(ydl)
    dl = FileDownloader(ydl, {'simulate': True, 'skip_download': True})
    post_processor = EmbedThumbnailPP(dl)
    # set downloader
    post_processor.set_downloader(dl)

    # run
    path = 'testfile'


# Generated at 2022-06-14 18:03:38.223790
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader(object):
        def __init__(self):
            self.params = {'outtmpl': '%(title)s'}
        def report_warning(self, message):
            print('warning: %s' % message)

    class MockPostProcessor(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)
            self.file_list = []

        def run(self, info):
            path = info.get('filepath')
            if path is not None:
                self.file_list.append(path)
            return self.file_list, info

    pp = MockPostProcessor(MockDownloader())
    info = {
        'title': 'test.mp4',
    }

# Generated at 2022-06-14 18:03:51.882489
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import time
    import tempfile
    import unittest

    class PostProcessor_try_utime(PostProcessor):
        def report_warning(self, msg):
            self.msg = msg

    class Downloader(object):
        def __init__(self, params):
            self.params = params

    class TestPostProcessor_try_utime(unittest.TestCase):
        def setUp(self):
            (fd, self.path) = tempfile.mkstemp()
            os.close(fd)
            self.atime = time.time()
            self.mtime = time.time()
            self.pp = PostProcessor_try_utime()
            self.params = {'outtmpl': self.path}

# Generated at 2022-06-14 18:04:03.064230
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import time
    from ..downloader.common import FileDownloader

    # Create temporary working directory
    tmpdir = tempfile.mkdtemp()

    # Create a fake downloader
    ydl = FileDownloader({})
    ydl.params['outtmpl'] = tmpdir + '/%(title)s-%(id)s.%(ext)s'

    # Create a fake postprocessor
    pp = PostProcessor(ydl)

    # Create a fake file
    open(tmpdir + '/foo.bar', 'wb').close()

    # Try utime, it should fail silently
    pp.try_utime(tmpdir + '/foo.bar', 1, 2)

    # Check utime of file, it should not be changed as previous operation failed
    timestamp = os.path.getm

# Generated at 2022-06-14 18:04:13.867146
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import shutil
    from .Downloader import FakeDownloader
    from .compat import compat_makedirs

    def _try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
        return os.utime(encodeFilename(path), (atime, mtime))

    def _mkstemp(self):
        return 'tempfile', 'wb', 1

    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test')
    dummy_file = os.path.join(test_dir, 'dummy')
    temp_file = os.path.join(test_dir, 'tempfile')

    PostProcessor_try_utime = PostProcessor.try_utime
    Post

# Generated at 2022-06-14 18:04:23.666308
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Create a PostProcessor instance
    class TestPostProcessor(PostProcessor):
        pass
    pp = TestPostProcessor()
    # create a test file
    import tempfile
    tf = tempfile.mkstemp()[1]
    # test if its time attributes can be changed
    import time
    old_atime = time.time() - 3600
    old_mtime = time.time() - 3600
    pp.try_utime(tf, old_atime, old_mtime)
    assert os.stat(tf).st_atime < old_atime
    assert os.stat(tf).st_mtime < old_mtime
    # clean up
    del pp
    os.remove(tf)

if __name__ == '__main__':
    test_PostProcessor_try_utime

# Generated at 2022-06-14 18:04:33.001671
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # You need to install the following modules to run this test
    # Python modules:
    #     unittest
    #     sys
    #     os
    #     tempfile
    #     atexit
    #     shutil
    #     urllib
    #     stat
    #     subprocess
    #     datetime
    #     time
    #
    # System packages:
    #     ffmpeg
    #     bc
    import unittest
    import sys
    import os
    import tempfile
    import atexit
    import shutil
    import urllib
    import stat
    import subprocess
    import datetime
    import time
    from ..downloader import post_processor

    class PP_try_utime(post_processor.PostProcessor):

        def run(self, information):
            self.try_

# Generated at 2022-06-14 18:04:36.733221
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class MockDownloader():
        def report_warning(self, msg):
            pass
    pp = PostProcessor(MockDownloader())
    pp.try_utime('foo', 0, 0)

# Generated at 2022-06-14 18:04:45.262176
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import shutil
    import tempfile

    filename = os.path.join(tempfile.gettempdir(), 'youtubedl-test-file')
    shutil.copy(__file__, filename)

    pos_processor = PostProcessor(None)

    # Test without utime
    assert os.path.exists(filename)
    assert os.path.isfile(filename)
    os.remove(filename)
    assert not os.path.exists(filename)

    # Test with utime
    assert not os.path.exists(filename)
    pos_processor.try_utime(filename, 12345678, 12345678)
    assert not os.path.exists(filename)

    # Cleanup
    try:
        os.remove(filename)
    except Exception:
        pass

# Generated at 2022-06-14 18:04:52.176947
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(None)
    pp._downloader = object()
    pp._downloader.report_warning = lambda s: True

    os.utime = lambda path, times: None
    pp.try_utime(None, None, None)

    os.utime = lambda path, times: True
    pp.try_utime(None, None, None)

    os.utime = lambda path, times: True
    pp.try_utime(None, None, None, errnote='Some error')

# Generated at 2022-06-14 18:05:03.316593
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import datetime

    import filecmp
    import pytest
    import tempfile
    import os

    class MockDownloader():

        def __init__(self):
            self.reported_warnings = []

        def report_warning(self, msg):
            self.reported_warnings.append(msg)

    class PostProcessorWithTryUtimes(PostProcessor):

        def __init__(self, downloader=None):
            super(PostProcessorWithTryUtimes, self).__init__(downloader)
            self.times_called = 0


# Generated at 2022-06-14 18:05:10.419041
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # pylint: disable=R0915
    class MockFile(object):
        def __init__(self, mtime):
            self.mtime = mtime

        def __enter__(self):  # pylint: disable=R0201
            return self

        def __exit__(self, exc_type, exc_value, traceback):  # pylint: disable=W0613
            pass

    class MockOs(object):
        def __init__(self, mtime):
            self.mtime = mtime
            self.strerror = 'OSError strerror'

        def utime(self, path, times):  # pylint: disable=W0613
            if self.mtime is not None:
                raise OSError(errno.EXDEV, 'OSError message')
            return self

# Generated at 2022-06-14 18:05:32.751558
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyPostProcessor(PostProcessor):
        def run(self, information):
            path = information['filepath']
            atime = mtime = information['upload_date']
            self.try_utime(path, atime, mtime)
            return [], information

        def __init__(self, downloader=None):
            super(DummyPostProcessor, self).__init__(downloader)

    class DummyDownloader(object):
        def __init__(self, params):
            self.params = params
            self.warned = False

        def report_warning(self, note):
            self.warned = True

    downloader = DummyDownloader({})
    pp = DummyPostProcessor(downloader)
    assert not downloader.warned

# Generated at 2022-06-14 18:05:42.081392
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os, shutil
    from ..downloader.common import FileDownloader
    from .common import FileDownloaderTestCase, get_testdata_dir

    DIR = os.path.dirname(os.path.abspath(__file__))

    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)
            self._in_progress_files = []

        def run(self, info):
            return self._in_progress_files, info

        def _add_file(self, filename):
            self._in_progress_files.append(filename)


# Generated at 2022-06-14 18:05:51.244781
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    class DummyPostProcessor(PostProcessor):
        def __init__(self, test):
            self.test = test
    import time
    import tempfile
    import shutil
    test = {'tmp_dir': None, 'atime': -1, 'mtime': -1}
    p = DummyPostProcessor(test)
    tmp_dir = tempfile.mkdtemp()
    test['tmp_dir'] = tmp_dir
    tmp_file = os.path.join(tmp_dir, 'dummy')
    f = open(tmp_file, 'w')
    f.close()
    (test['atime'], test['mtime']) = (os.stat(tmp_file).st_atime, os.stat(tmp_file).st_mtime)

# Generated at 2022-06-14 18:06:02.719844
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time
    import shutil

# Generated at 2022-06-14 18:06:12.025034
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import copy
    import time
    import sys
    class MockDownloader(object):
        def __init__(self):
            self.params = {'postprocessor_args': []}
        def to_stdout_silent(self, message):
            sys.stdout.write(message + '\n')
        def to_stderr(self, message):
            sys.stderr.write(message + '\n')
        def report_warning(self, message):
            self.to_stderr('WARNING: ' + message)
    pp1 = PostProcessor(MockDownloader())
    pp2 = copy.copy(pp1)
    path = 'test.file'

# Generated at 2022-06-14 18:06:23.397289
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import time
    import shutil
    import tempfile
    import unittest
    import stat

    from ..utils import (
        DateRange,
        PostProcessor,
    )

    class MockDownloader(object):
        def __init__(self):
            pass

        def report_warning(self, msg):
            print('MockDownloader report_warning: %s' % msg)

    class TestPostProcessor(PostProcessor):
        def run(self, information):
            print('run information: %s' % information)

            # Configure atime and mtime for file, acording to date_range value
            date_range = self._downloader.params.get('date_range')

            if (date_range != None):
                start_time, end_time = date_range.get_start_

# Generated at 2022-06-14 18:06:26.444422
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Just calling the try_utime() method as a test."""
    pp = PostProcessor(None)
    pp.try_utime('test', 0, 0)


# Generated at 2022-06-14 18:06:27.021147
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pass

# Generated at 2022-06-14 18:06:34.616826
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import shutil
    from ..YoutubeDL import YoutubeDL

    td = tempfile.mkdtemp()

# Generated at 2022-06-14 18:06:35.633760
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()
    # TODO
    assert True

# Generated at 2022-06-14 18:07:14.174456
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import shutil
    import datetime
    from ..compat import PY2
    from ..utils import PostProcessor

    # Create temp directory to store file
    tmp_dir = tempfile.mkdtemp(prefix='test_youtube_dl_')
    

# Generated at 2022-06-14 18:07:18.979957
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from mock import Mock

    pp = PostProcessor(Mock())
    orig_utime = os.utime

    def test_utime(*args, **kwargs):
        raise OSError('This is test exception')
    os.utime = test_utime

    pp.try_utime('path', 'atime', 'mtime', 'errnote')
    pp._downloader.report_warning.assert_called_with('errnote')
    os.utime = orig_utime



# Generated at 2022-06-14 18:07:30.117846
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import time
    import unittest
    import tempfile
    import shutil
    from ytdl_postprocessor import PostProcessor

    class Test(unittest.TestCase):
        TEMP_DIR = None

        @classmethod
        def setUpClass(cls):
            cls.TEMP_DIR = tempfile.mkdtemp()

        def setUp(self):
            self.filepath = os.path.join(self.TEMP_DIR, 'test')
            with open(self.filepath, 'w') as f:
                f.write('test')

        @classmethod
        def tearDownClass(self):
            shutil.rmtree(cls.TEMP_DIR)


# Generated at 2022-06-14 18:07:34.894772
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Test case for file which doesn't exists
    pp = PostProcessor(None)
    pp.try_utime('sample file', 1, 2)

    # Test case for file which exists
    try:
        f = open('sample file', 'w')
        f.write('Sample file')
        f.close()
        pp.try_utime('sample file', 1, 2)
    finally:
        # Cleanup
        os.remove('sample file')

# Generated at 2022-06-14 18:07:43.362178
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import sys
    import shutil
    import tempfile
    import os

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create 'test.txt' with content 'test' and set last modification time to 'Jan 1 1970 01:00:00'
    filename = os.path.join(tmpdir, 'test.txt')
    with open(filename, 'w') as tmpfile:
        tmpfile.write('test')
    os.utime(filename, (0, 0))

    # Create PostProcessor object
    try:
        from ydl.YoutubeDL import YoutubeDL
    except ImportError:
        sys.exit('ERROR: cannot import YoutubeDL')
    downloader = YoutubeDL({'outtmpl': 'test', 'quiet':True})


# Generated at 2022-06-14 18:07:53.931529
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import time
    import sys
    import shutil
    from ..utils import PostProcessor
    from ..compat import PY2

    if PY2:
        from . import compat_http_client as http_client
        from . import compat_urllib_request as urllib_request
        from . import compat_urllib_error as urllib_error
    else:
        from . import compat_http_client as http_client
        from . import compat_urllib_request as urllib_request
        from . import compat_urllib_error as urllib_error

    class Downloader:

        def report_warning(self, errnote):
            print(errnote)


# Generated at 2022-06-14 18:08:02.145821
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..YoutubeDL import YoutubeDL
    import time

    def test_utime():
        try:
            os.utime(encodeFilename("arschloch"), (time.time(), time.time()))
            return True
        except Exception:
            return False

    assert test_utime()

    ydl = YoutubeDL(params={'logger': YoutubeDL.logger_debug})
    pp = PostProcessor(ydl)
    pp.try_utime("arschloch", time.time(), time.time())

    assert test_utime()

# Generated at 2022-06-14 18:08:10.474254
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from ..extractor import gen_extractors
    for info_dict in gen_extractors():
        downloader = info_dict['ie']._downloader
        pp = PostProcessor(downloader)

        # Generate a dummy time
        import time
        atime = time.time() - (60 * 60 * 24 * 2)  # 2 days ago
        mtime = time.time() - (60 * 60 * 24 * 1)  # 1 day ago

        # Generate a temporary file
        import tempfile
        temp_fd, temp_path = tempfile.mkstemp(prefix='youtube-dl')
        os.close(temp_fd)
        os.utime(temp_path, (atime, mtime))

        # Test try_utime method

# Generated at 2022-06-14 18:08:20.885787
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import unittest
    import tempfile
    import shutil
    import stat

    class TestPostProcessor(PostProcessor):
        def __init__(self, downloader):
            self._downloader = downloader
            self.test_updates = []

        def try_utime(self, path, atime, mtime, errnote='Cannot update utime of file'):
            self.test_updates.append((path, atime, mtime))

    class MockYoutubeDL(object):
        def __init__(self):
            self.params = {}

        def report_warning(self, errnote):
            self.params['errnote'] = errnote

    unittest.TestCase.maxDiff = None  # show full diff error messages


# Generated at 2022-06-14 18:08:25.915812
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import time
    import tempfile
    import shutil

    temp_dir = tempfile.mkdtemp()
    path = os.path.join(temp_dir, 'a.txt')
    try:
        f = open(path, 'w')
        f.write('Hello World!')
        f.close()
        atime = time.time() - 1000
        mtime = time.time() - 2000
        pp = PostProcessor(None)
        pp.try_utime(path, atime, mtime)
    finally:
        shutil.rmtree(temp_dir)


# Extractors for common file formats that can just be copied as-is