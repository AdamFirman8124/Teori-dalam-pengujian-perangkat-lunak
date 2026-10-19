

# Generated at 2022-06-14 18:09:05.032507
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert isinstance(pp, XAttrMetadataPP)

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:09:12.446822
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    XAttrMetadataPP(None).run({
        'filepath': 'filename',
        'format': 'format_value',
        'description': 'description_value',
        'uploader': 'uploader_value',
        'title': 'title_value',
        'webpage_url': 'https://www.youtube.com/watch?v=VIDEO_ID',
    })

# Generated at 2022-06-14 18:09:21.000056
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..extractor import YoutubeIE
    from ..utils import DateRange
    from .common import FileDownloader
    from .external import ExternalFD
    import subprocess
    import tempfile
    import os

    # -------------------------------------------------------------------------
    def has_xattr(filename):
        exitcode = subprocess.call(['getfattr', '-n', 'user.dublincore.title', filename])
        return exitcode == 0

    # -------------------------------------------------------------------------
    def get_title(filename):
        p = subprocess.Popen(['getfattr', '-n', 'user.dublincore.title', '--only-values', filename],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return stdout.strip()

# Generated at 2022-06-14 18:09:28.173958
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import PostProcessor

    import pytest
    class MyXAttrMetadataPP(XAttrMetadataPP):
        def run(self, info):
            return info.get('message')

# Generated at 2022-06-14 18:09:34.547599
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ytdl.YtdlPostProcessor import YtdlPostProcessor
    pp = YtdlPostProcessor()
    pp_xattr = pp.get_postprocessor('XAttrMetadataPP')
    pp_xattr.run('')


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:09:35.179586
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:09:35.786080
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:09:37.103435
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xmd = XAttrMetadataPP(None)


# Generated at 2022-06-14 18:09:47.999969
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():

    import tempfile
    import os
    import shutil
    from ..utils import prepend_extension, xattr_supported

    if not xattr_supported():
        return

    fd, tmpfile = tempfile.mkstemp(prefix='yt-dl_', suffix='.tmp')
    f = os.fdopen(fd, 'wb')


# Generated at 2022-06-14 18:09:55.580921
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .common import FileDownloader
    from ..YoutubeDL import YoutubeDL

    ydl = YoutubeDL({'writedescription': 'description', 'writeannotations': 'annotations', 'writeinfojson': 'info.json'})
    d = FileDownloader(ydl, {'outtmpl': '%(title)s-%(id)s.%(ext)s'})

    x = XAttrMetadataPP(d)
    assert isinstance(x, PostProcessor)

# Generated at 2022-06-14 18:10:11.975864
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    import unittest
    from .common import FileDownloader
    from .test_support import FakeYDL

    class TestXAttrMetadataPP(unittest.TestCase):

        def setUp(self):
            self.tempdir = tempfile.mkdtemp()
            self.tempfile = os.path.join(self.tempdir, 'test.mp4')
            self.f = open(self.tempfile, 'w')
            self.f.close()
            self.f = open(self.tempfile, 'rb+')

        def tearDown(self):
            self.f.close()
            os.unlink(self.tempfile)
            os.rmdir(self.tempdir)

        def test_XAttrMetadataPP_run(self):
            y

# Generated at 2022-06-14 18:10:23.701552
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    def _test_run(filename, xattrname, value, expected_xattr_value):
        if compat_os_name == 'nt':
            pytest.skip("Windows doesn't support xattrs.")
        write_xattr(filename, xattrname, expected_xattr_value)
        xattr_mapping = {xattrname: 'xattr'}
        info = {'xattr': value}
        xattrs = XAttrMetadataPP()
        xattrs.run(info)
        assert read_xattr(filename, xattrname) == expected_xattr_value


    _test_run('tmp/test.mp4', 'user.xdg.referrer.url', 'http://youtube.com/foo', b'http://youtube.com/foo')

# Generated at 2022-06-14 18:10:34.747067
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..utils import DateRange
    from ..extractor import every_get

    # Create an info with values that should be written to several xattrs
    info = {
        'webpage_url': 'http://www.example.com/page.html',
        'title': 'The Title',
        'description': 'This is a description.',
        'upload_date': DateRange('20180816'),
        'uploader': 'Mr. Uploader',
        'format': 'video/mp4',
    }

    assert len(info) != 0

    # Instantiate the class that is being tested
    pp = XAttrMetadataPP(None)

    # Run the postprocessor
    info = pp._run(info) # pylint: disable=protected-access

    # Check if the xattrs are correct

# Generated at 2022-06-14 18:10:38.458171
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO: implement test for method run of class XAttrMetadataPP
    pass


# Generated at 2022-06-14 18:10:42.853953
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP({}, None) is not None

# Generated at 2022-06-14 18:10:44.787146
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    assert isinstance(pp, XAttrMetadataPP)

# Generated at 2022-06-14 18:10:53.638662
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..ytdl.YoutubeDL import YoutubeDL
    from ..extractor.common import InfoExtractor
    from .subtitles import SubtitlesPP
    from .ffmpeg import FFmpegMetadataPP

    ydl = YoutubeDL({'writesubtitles': True, 'writeautomaticsub': True, 'subtitleslangs': ['de', 'en'], 'subtitlesformat': 'best'})

    ie = InfoExtractor({})
    ie.extract({'url': 'https://www.youtube.com/watch?v=XjcikHl0JNQ', 'extractor': 'youtube'})

    pp = XAttrMetadataPP(ydl)
    pp1 = SubtitlesPP(ydl)
    pp2 = FFmpegMetadataPP(ydl)


# Generated at 2022-06-14 18:11:06.324789
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from time import time
    from datetime import datetime
    from ..utils import xattr_set_if_exists

    # mock downloader
    class MockDownloader(object):
        def report_warning(self, msg):
            pass
        def report_error(self, msg):
            pass
        def to_screen(self, msg):
            pass

    # mock info dictionary

# Generated at 2022-06-14 18:11:08.190885
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattrmetadatapp = XAttrMetadataPP(None)
    assert xattrmetadatapp.run(None) == ([], None)

# Generated at 2022-06-14 18:11:09.956839
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert PostProcessor.is_enabled('XAttrMetadataPP') is False

# Generated at 2022-06-14 18:11:28.936077
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattrPP = XAttrMetadataPP()
    xattrPP.run( {'filepath': 'test.mp4'} )
    xattrPP.run( {'filepath': 'test.mp4', 'format': 'mp4'} )
    xattrPP.run( {'filepath': 'test.mp4', 'webpage_url': 'https://www.youtube.com'} )
    xattrPP.run( {'filepath': 'test.mp4', 'title': 'test'} )
    xattrPP.run( {'filepath': 'test.mp4', 'upload_date': '20160805'} )
    xattrPP.run( {'filepath': 'test.mp4', 'description': 'test'} )

# Generated at 2022-06-14 18:11:29.965443
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO: see test_metadata.py
    pass

# Generated at 2022-06-14 18:11:35.824358
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .test_postprocessor import TestPostProcessor
    from .common import PostProcessor
    from ..utils import (
        write_xattr,
        read_xattr,
        XAttrUnavailableError,
        XAttrMetadataError,
        xattr_set_available,
    )
    import os
    import shutil
    import tempfile

    xattr_available = xattr_set_available()
    if not xattr_available:
        print('WARNING: Skipping XAttrMetadataPP tests, the system doesn\'t support extended attributes.')
        return

    _downloader = TestPostProcessor('this is a test video', 'filename.mp4')

    TEMP_DIR = tempfile.mkdtemp()


# Generated at 2022-06-14 18:11:41.146254
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    '''
    Run the constructor for class XAttrMetadataPP
    '''
    ydl = YoutubeDL({})
    pp = XAttrMetadataPP(ydl)
    assert isinstance(pp, XAttrMetadataPP)


# Generated at 2022-06-14 18:11:43.389466
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    print(pp)

# Generated at 2022-06-14 18:11:53.557270
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import tempfile

    from .common import FileDownloader

    from ..compat import compat_urlparse, compat_urllib_error

    # Create a temporary file for testing
    handle, filename = tempfile.mkstemp()
    os.close(handle)

    #
    # Test with duplicated xattr values
    #
    url = 'http://youtube.com/watch?v=BaW_jenozKc'
    context = {}
    context['player_url'] = 'https://www.youtube.com/embed/BaW_jenozKc'
    context['f4m_id'] = 'BaW_jenozKc'
    context['age_limit'] = None


# Generated at 2022-06-14 18:11:54.620875
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:11:56.469891
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP(None)

# Generated at 2022-06-14 18:12:01.213723
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from . import get_testcases_for
    for test_case, expected_return in get_testcases_for(XAttrMetadataPP).items():
        obj = XAttrMetadataPP(test_case)
        assert obj.__dict__ == expected_return

# Generated at 2022-06-14 18:12:10.510965
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import tempfile
    import platform
    from .common import FileDownloader
    from .common import prepare_mock_files

    from .test_files import XAttrUnavailableError

    from .test_files.fake_filesystem_unix import fake_filesystem_unix
    from .test_files.fake_filesystem_xattr import fake_filesystem_xattr

    if platform.system() == 'Windows':
        return

    class FakeXAttrMetadataPP(XAttrMetadataPP):
        def __init__(self, ydl, params):
            super(FakeXAttrMetadataPP, self).__init__(ydl, params)

        def run(self, info):
            (retcode, _) = super(FakeXAttrMetadataPP, self).run(info)
            return

# Generated at 2022-06-14 18:12:37.890797
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os.path
    import pytest

    from ..utils import make_temp_dir

    from .common import FileDownloader

    from .test_postprocessor import (
        make_mock_ydl,
        read_xattrs,
        simulate_xattr_support,
    )

    @pytest.fixture
    def ydl(tmpdir):
        ydl = make_mock_ydl(tmpdir)
        ydl.params['writedescription'] = True
        return ydl


# Generated at 2022-06-14 18:12:49.416687
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import encodeFilename

    import os
    import tempfile

    if compat_os_name == 'nt':
        raise unittest.SkipTest('Not available on Windows')

    # Create a temporary file
    fd, temp_filepath = tempfile.mkstemp(text=False)
    os.close(fd)


# Generated at 2022-06-14 18:12:52.790773
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    postprocessor = XAttrMetadataPP(None)
    # is an instance of XAttrMetadataPP
    assert isinstance(postprocessor, XAttrMetadataPP)


# Generated at 2022-06-14 18:13:04.736140
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    import xattr
    import sys

    # TODO: Needs to be ported to Windows

    assert sys.platform == 'linux2'

    # Prepare a file
    path = tempfile.mkstemp()[1]

    # Prepare a downloader object
    class DebugDict(dict):
        def debug(self, msg):
            print(msg)

    class FakeInfo:
        def __init__(self, infos):
            self.infos = infos

        def get(self, key, _=None):
            return self.infos.get(key)

    class FakeYDL:
        def __init__(self, to_screen=None):
            self.to_screen = to_screen
            self.params = {}

        def report_error(self, msg):
            raise Exception

# Generated at 2022-06-14 18:13:07.254973
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert callable(XAttrMetadataPP)

# vim:et:sw=4:ts=4

# Generated at 2022-06-14 18:13:17.531739
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import sys
    import os
    import tempfile
    from ..extractor.common import InfoExtractor
    from ..compat import compat_urllib_request
    from ..compat import compat_os_name
    from ..utils import sanitize_open

    if compat_os_name == 'nt':
        return  # Test doesn't apply on Windows
    if not os.path.exists('/proc/self/fd'):
        return  # Test doesn't apply on OSX
    if not os.path.exists('/sys/fs/xattr/'):
        return  # Test doesn't apply on old Linux versions (before 2.6.19)


# Generated at 2022-06-14 18:13:20.917310
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    '''
    Test the constructor of the class XAttrMetadataPP.
    '''
    XAttrMetadataPP(None)

# Generated at 2022-06-14 18:13:30.415901
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Prepare arguments for the method
    filename = 'test.avi'
    xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        # 'user.xdg.comment':            'description',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }

    class FakeDownloader():
        to_screen = None
        report_warning = None
        report_error = None

        def to_screen(self, msg):
            return msg


# Generated at 2022-06-14 18:13:31.665579
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:13:42.067338
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import unittest
    import sys
    import os
    import shutil
    import tempfile
    from ..utils import (
        encode_compat_str,
        encodeFilename,
        read_xattr,
        verify_xattr_availability,
    )
    from ..version import __version__

    class TestXAttrMetadataPP(unittest.TestCase):
        def setUp(self):

            # First make sure xattrs can be written
            if not verify_xattr_availability():
                raise unittest.SkipTest('XAttrs are not supported in this system')


# Generated at 2022-06-14 18:14:22.150135
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:14:31.150239
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    youtube_url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    yt_video_id = 'BaW_jenozKc'
    info = {}
    expected_output = []

    # The following test verifies that the constructor
    # creates the expected attributes
    pp = XAttrMetadataPP()

    # The following test verifies that the constructor
    # creates the expected attributes
    assert hasattr(pp, '_downloader')
    assert hasattr(pp, 'run')

# Finish test for class XAttrMetadataPP


# Generated at 2022-06-14 18:14:41.465706
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .test_utils import FakeYDL
    from .postprocessor import FFmpegPostProcessor

    # Create a fake info dict

# Generated at 2022-06-14 18:14:43.526523
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ Test constructor of class XAttrMetadataPP. """

    # Test XAttrMetadataPP constructor
    assert XAttrMetadataPP()

# Generated at 2022-06-14 18:14:55.030065
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """
    This function returns the output that class XAttrMetadataPP would return when calling its method run.
    """
    from .common import PostProcessor
    from ..compat import compat_os_name
    from ..utils import (
        hyphenate_date,
        write_xattr,
        XAttrMetadataError,
        XAttrUnavailableError,
    )

    # Create a PostProcessor object
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    pp = XAttrMetadataPP(ydl)

    # Create a DownloadInfo object
    from ..extractor import common
    info = common.DownloadInfo()
    info['filepath'] = 'filepath'

    # Write the metadata to the file's xattrs

# Generated at 2022-06-14 18:14:56.793939
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(None, {}).__class__ is XAttrMetadataPP

# Generated at 2022-06-14 18:15:06.937064
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader.common import FileDownloader
    from ..compat import compat_os_name

    class MockInfo:
        pass

    class MockFileDownloader(FileDownloader):
        def to_screen(self, *args, **kargs):
            pass

        def report_error(self, msg):
            raise RuntimeError(msg)

        def report_warning(self, msg):
            raise RuntimeError(msg)

    info = MockInfo()
    downloader = MockFileDownloader(None)

    if compat_os_name == 'nt':
        info.filepath = 'D:\\TEMP\\test.mp4'
        XAttrMetadataPP(downloader, info).run(info)
    else:
        from ..utils import get_xattr_supported_platforms
        from ..compat import compat_getenv

# Generated at 2022-06-14 18:15:19.023662
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """
    Test if method run of class XAttrMetadataPP
    raises an exception if the value of an extended
    attribute is too long.
    """

    # Create a XAttrMetadataPP to test its method run
    metadata_pp = XAttrMetadataPP(None)

    # Create a fake Info object
    mock_info = {
        'filepath': 'tests/mock_info/filepath',
        'title': 'A test',
        'format': 'a test format',
        'uploader': 'A test uploader',
        'upload_date': '20160101',
        'webpage_url': 'http://example.com',
        'description': 'A test description'
    }

    # Call method run of class XAttrMetadataPP
    # TODO: add test to check if method run


# Generated at 2022-06-14 18:15:23.911572
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import youtube_dl
    ydl = youtube_dl.YoutubeDL({'writethumbnail': True,
                                'writexattrs': True,
                                })
    pp = XAttrMetadataPP(ydl)



# Generated at 2022-06-14 18:15:26.940535
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import gen_extractors
    ie = gen_extractors()['youtube']('http://www.youtube.com/watch?v=BaW_jenozKc&feature=youtu.be')
    ie.extract()
    ie.download()
    assert XAttrMetadataPP().run(ie.get_info('BaW_jenozKc')) == ([], {})


if __name__ == '__main__':
    import sys
    sys.exit(test_XAttrMetadataPP())

# Generated at 2022-06-14 18:16:52.550837
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


# Command line test for method run of class XAttrMetadataPP

# Generated at 2022-06-14 18:17:03.201289
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    from .common import PostProcessorTest, PostProcessor
    from ..utils import (
        xattr,
        XAttrUnavailableError,
        XAttrMetadataError,
    )

    class TestPP(XAttrMetadataPP):
        def _log(self, msg):
            XAttrMetadataPP._log(self, msg)
            self.log_out += msg + '\n'

    class MyDl(object):
        def __init__(self):
            self.log_out = ''

        def to_screen(self, msg):
            pass

        def report_error(self, msg):
            self.log_out += msg + '\n'

        def report_warning(self, msg):
            self.log_out += msg + '\n'


# Generated at 2022-06-14 18:17:06.976502
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(None)


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:17:12.191681
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """
    Unit test for method run of class XAttrMetadataPP

    Test by setting extended attributes on downloaded file (if xattr support is found).
    """
    print("\n--- Start test_XAttrMetadataPP_run ---")


if __name__ == "__main__":
    test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:17:12.737169
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    return True

# Generated at 2022-06-14 18:17:24.287349
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import shutil
    import tempfile

    from ..downloader import FakeYDL
    from ..extractor import YoutubeIE
    from ..utils import encodeFilename

    # Make a temporary directory
    temp_dir = tempfile.mkdtemp(prefix='yt-dl_test_XAttrMetadataPP_run')

    # Create a temporary file in this directory
    (file_fd, file_path) = tempfile.mkstemp(suffix='.f4v', dir=temp_dir)
    os.close(file_fd)

    # Create a downloader instance
    ydl = FakeYDL()
    ydl.params['quiet'] = True
    ydl.params['logger'] = ydl

    # Create a filename
    video_id = 'CXeJqn7yuJo'
    test_filename

# Generated at 2022-06-14 18:17:27.671186
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    info = {}
    pp = XAttrMetadataPP()
    assert pp.run(info) == ([], info)

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:17:39.994682
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import gen_extractors

    def test_gen_extractors():
        import types
        extractors = gen_extractors()
        assert isinstance(extractors, types.GeneratorType)
        assert len(list(extractors)) > 0
    test_gen_extractors()

    xattr_metadata_pp = XAttrMetadataPP(None)


# Generated at 2022-06-14 18:17:49.025005
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile

    class MyDownloader:

        def to_screen(self, *args, **kwargs):
            pass

        def report_error(self, *args, **kwargs):
            pass

        def report_warning(self, *args, **kwargs):
            pass

    tempdir = tempfile.mkdtemp()
    filename = os.path.join(os.path.dirname(__file__), 'test_xattr', 'test.flv')
    tempfilepath = os.path.join(tempdir, 'temp.flv')
    with open(filename, 'rb') as f:
        with open(tempfilepath, 'wb') as f_temp:
            f_temp.write(f.read())


# Generated at 2022-06-14 18:17:55.600861
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader import Downloader
    from .common import FileDownloader
    from ..YoutubeDL import YoutubeDL
    from ..extractor import gen_extractors
    from ..utils import encodeFilename, prepend_extension

    gen_extractors()

    ydl = YoutubeDL({
        'outtmpl': encodeFilename('%(title)s.f%(format_id)s.%(ext)s')
    })
    dl = Downloader(ydl, {})