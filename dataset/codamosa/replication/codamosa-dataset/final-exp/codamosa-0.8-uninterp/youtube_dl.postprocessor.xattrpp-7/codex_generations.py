

# Generated at 2022-06-14 18:09:12.081805
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile
    import shutil
    import atexit
    import os
    from .common import PostProcessor
    from ..utils import write_xattr

    # class MockInfo:
    #     def __init__(self, filename, webpage_url, title, upload_date, description, uploader, format, filepath=None):
    #         self.webpage_url = webpage_url
    #         self.title = title
    #         self.upload_date = upload_date
    #         self.description = description
    #         self.uploader = uploader
    #         self.format = format
    #         self.filepath = filepath if filepath else filename

    class MockDownloader:
        def to_screen(self, text): print(text)

# Generated at 2022-06-14 18:09:20.973166
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..utils import sanitize_open
    from ..downloader import Downloader
    import tempfile
    import os
    from ..compat import compat_os_name

    #
    # Generic tests
    #
    filename = "file.txt"

    (fd, filepath) = tempfile.mkstemp()
    os.close(fd)
    os.unlink(filepath)

    # Create a dummy file
    with sanitize_open(filepath, 'wb') as f:
        f.write(b'foo' * 1024)

    # Test if we have xattr support on this system
    try:
        write_xattr(filepath, 'user.foo', b'bar')
    except XAttrUnavailableError:
        # No xattr support on this system
        return

    #
    # Extended attributes

# Generated at 2022-06-14 18:09:22.429031
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 18:09:28.972015
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    assert isinstance(pp, PostProcessor)
    expected_xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }
    assert pp._xattr_mapping == expected_xattr_mapping

# Generated at 2022-06-14 18:09:41.411189
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import PostProcessorTest
    from ..compat import compat_os_name

    filename = 'file.mkv'
    if compat_os_name == 'nt':
        filename = 'file.mp4'

    pp_test = PostProcessorTest(filename)
    pp = XAttrMetadataPP(pp_test.ydl)
    info = {
        'filepath': filename,
        'format': 'MPEG-4 (DASH video)',
        'webpage_url': 'http://example.com',
        'description': 'some description',
        'title': 'Some title',
        'format': 'video/webm',
        'upload_date': '20010101',
        'uploader': 'Somebody',
    }
    # TODO:
    # should return `True` on success,

# Generated at 2022-06-14 18:09:50.655934
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader import FileDownloader
    from .common import PhonyYDL
    dummy_down = FileDownloader({})
    dummy_down.postprocessors = {'dummy_pp_name': 'dummy_pp_class'}
    ydl = PhonyYDL()
    ydl.params = {}

# Generated at 2022-06-14 18:09:52.152189
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None, {}, None)
    assert pp != None



# Generated at 2022-06-14 18:10:02.848146
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile

    xattr_loader = XAttrMetadataPP(None)
    test_file_path = tempfile.mkstemp()[1]

    # Try to write xattrs on file that doesn't exist
    # This should raise a XAttrError, that's ok
    os.remove(test_file_path)

    try:
        xattr_loader.run({'filepath': test_file_path})
    except XAttrMetadataError:
        pass  # This is what we expect

    # Try to write xattrs on file that exists and has no extended attributes

    test_file = open(test_file_path, 'w')
    test_file.write("The quick brown fox jumps over the lazy dog")
    test_file.close()


# Generated at 2022-06-14 18:10:14.566308
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import unittest
    from ..utils import xattr

    from .pp_common import PPTester

    class XAttrMetadataPPTester(PPTester):
        def _mock_write_xattr(self, filename, xattrname, byte_value):
            self.mock_write_xattr_filename = filename
            self.mock_write_xattr_xattrname = xattrname
            self.mock_write_xattr_byte_value = byte_value
            return super(XAttrMetadataPPTester, self)._mock_write_xattr(filename, xattrname, byte_value)


# Generated at 2022-06-14 18:10:23.475096
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    ydl = FakeYDL()
    ydl.add_post_processor(XAttrMetadataPP(ydl))
    ydl.set_options(writeinfojson=True)
    ydl.download(['http://example.com/foo'])
    assert ydl.files is not None
    assert len(ydl.files) == 1
    f = ydl.files[0]
    assert f['format'] == 'fake'
    assert f['ext'] == 'mp4'
    assert f['title'] == 'foobar'


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:10:29.417449
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

# Generated at 2022-06-14 18:10:37.062571
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    filename = 'filename'
    info_dict = {
        'webpage_url': 'webpage_url',
        'title': 'title',
        'upload_date': 'upload_date',
        'description': 'description',
        'uploader': 'uploader',
        'format': 'format',
    }

    postprocess = XAttrMetadataPP()
    postprocess._downloader = lambda x: None
    postprocess._downloader.params = {
        'writethumbnail': True,
        'writeinfojson': True,
    }
    postprocess.run(info_dict)


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:10:49.217076
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..extractor.common import InfoExtractor
    from .xattrpptest import (
        XAttrPPTester,
        OnDiskTestXAttrContainer,
        OnDiskTestXAttrContainerEmpty,
    )

    #
    # Create test file, set XAttrs, run method and compare
    #

    # Test data
    test_filepath = 'some.file.mp4'
    test_info = {
        'id': 'some_id',
        'ext': 'mp4',
        'title': '"Hello, world!"',
        'webpage_url': 'http://some.url',
        'uploader': 'Some Uploader',
        'upload_date': '20131312',
        'format': 'best',
    }

    # Result

# Generated at 2022-06-14 18:10:49.827053
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:10:58.919977
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    #
    # Construct an object to test method run of class XAttrMetadataPP
    #
    # The constructor of XAttrMetadataPP receives a YDL object,
    # then it is ready to use method run
    #
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader.external.ffmpeg import FFmpegPostProcessor
    from youtube_dl.downloader.http import HttpDownloader

    ydl_opts = {}
    ydl = YoutubeDL(ydl_opts)
    ydl.params['logger'] = ydl
    ydl.params['nooverwrites'] = True
    ydl.add_post_processor(FFmpegPostProcessor(ydl))
    ydl.add_post_processor(XAttrMetadataPP(ydl))
    y

# Generated at 2022-06-14 18:11:09.794506
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .common import FileDownloader
    from .xattr import XAttrPP
    from .xattr_metadata import XAttrMetadataPP
    from .exec_cmd import ExecCmdPP
    from .ffmpeg import FFmpegExtractAudioPP
    from ..extractor.common import InfoExtractor
    from ..extractor.youtube import YoutubeIE
    from ..utils import FakeYDL
    ydl_opts = {
        'continuedl': True,
        'outtmpl': '%(id)s'
    }
    ydl = FakeYDL()
    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    with ydl:
        ie = InfoExtractor(ydl, {})
        result = ie.extract(url)
    ffmpeg = FFmpegExtractAudio

# Generated at 2022-06-14 18:11:18.683478
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import sys
    import os
    import tempfile
    from .common import PostProcessor
    from .xattr import XAttrMetadataPP

    def test_init():
        if not sys.platform.startswith('linux') and not sys.platform.startswith('freebsd'):
            return
        if os.name != 'posix':
            return
        try:
            tempfile.NamedTemporaryFile().close()
        except (IOError, OSError):
            return

        pp = XAttrMetadataPP(PostProcessor({}))

# Generated at 2022-06-14 18:11:19.299325
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:11:27.662721
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    try:
        from . import get_testdata_video_url
    except ImportError as e:
        from ..utils import get_testdata_video_url

    #import youtube_dl.FileDownloader
    from youtube_dl.downloader.external import ExternalFD

    ydl = ExternalFD({'format': 'bestaudio/best', 'progress_hooks': [], 'outtmpl': u'unit tests/%(id)s.%(ext)s'})
    ydl.add_info_extractor(get_testdata_video_url())
    ydl.add_post_processor(XAttrMetadataPP)

    ydl.download([get_testdata_video_url()])

    return True

# Generated at 2022-06-14 18:11:39.872399
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    from ..utils import xattr_supported

    # If xattr is not supported, the test is useless, so just return
    if not xattr_supported():
        return

    # Create a random file with 644 permissions
    fd, fpath = tempfile.mkstemp()
    os.close(fd)
    os.chmod(fpath, 0o644)

    # Test the method run with a stupid video_info

# Generated at 2022-06-14 18:12:01.791427
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    filename = 'http://debug/foo.avi'
    info = {
        'webpage_url': 'http://debug/web/page.html',
        'title': 'title - foo bar',
        'upload_date': 'today',
        'description': 'description - foo bar',
        'tags': 'tags - foo bar',
        'uploader': 'uploader - foo bar',
        'ext': '.avi',
        'format': 'avi video - foo bar',
        'thumbnail': 'thumbnail url',
        'filepath': filename,
        'resolution': '720x480',
    }

# Generated at 2022-06-14 18:12:14.501455
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import sys
    import unittest

    class XAttrMetadataPP_run_TestCase(unittest.TestCase):

        def setUp(self):
            self.prepare_environment()
            self.make_dummy_video_info()
            self.make_dummy_extractor()
            self.make_dummy_downloader()
            self.make_dummy_xattrmetadatapp()

        def tearDown(self):
            self.delete_dummy_files()

        def prepare_environment(self):
            """
            Remove environment variables that may be set from
            previous tests.
            """


# Generated at 2022-06-14 18:12:20.470911
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..extractor import YoutubeIE
    from ..downloader import Downloader
    from .test.test_filesystem import make_tempdir
    from .test.test_downloader import MockYDL
    from .test.test_videos import mock_info_dict

    with make_tempdir() as tmpdir:
        downloader = Downloader(MockYDL())
        ie = YoutubeIE(downloader)

        info = mock_info_dict(downloader, {'upload_date': '20121004', 'format': 'webm'})
        xattr_pp = XAttrMetadataPP(downloader)

        try:
            xattr_pp.run(info)
        except XAttrUnavailableError:
            pass
        except XAttrMetadataError as e:
            assert e.reason == 'NO_SUPPORT'


# Generated at 2022-06-14 18:12:23.915611
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    return pp

if __name__ == '__main__':
    print(test_XAttrMetadataPP())

# Generated at 2022-06-14 18:12:25.917722
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    #
    # TODO: write tests for XAttrMetadataPP
    #
    pass

# Generated at 2022-06-14 18:12:34.855097
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..utils import get_exe_version
    from ..extractor.common import InfoExtractor

    assert XAttrMetadataPP.supported()

    downloader = InfoExtractor()
    downloader.add_info_extractor(InfoExtractor())

    #
    # Test
    #

    # test_run_empty
    info = {}
    pp = XAttrMetadataPP(downloader)
    # TODO: fix this test so that it actually checks if it is writing the xattr
    res = pp.run(info)
    assert res == ([], info)

    # test_run

# Generated at 2022-06-14 18:12:47.102669
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """Run the unittest for method run of class XAttrMetadataPP."""

    import os
    from .common import FileDownloader

    # Prepare objects for test:

# Generated at 2022-06-14 18:12:48.357363
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    return XAttrMetadataPP(None)

# Generated at 2022-06-14 18:12:58.888924
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FileDownloader
    from ..extractor import YoutubeIE
    from ..utils import DateRange
    from ..compat import is_py2

    class FakeYDL(FileDownloader):

        def __init__(self, *args, **kwargs):
            FileDownloader.__init__(self, *args, **kwargs)
            self.to_screen = lambda x: x
            self.report_error = lambda x: x

        @staticmethod
        def to_screen(s):
            return s

        @staticmethod
        def report_error(s):
            return s

    ydl = FakeYDL({'writedescription': True, 'writeinfojson': True, 'writethumbnail': True})


# Generated at 2022-06-14 18:13:00.547983
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP.__name__ == 'XAttrMetadataPP'

# Generated at 2022-06-14 18:13:30.554525
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import encodeFilename
    from .common import FileDownloader
    from ..extractor import YoutubeIE

    # Downloader object used to get filepath and other data
    ydl = FileDownloader({'outtmpl': encodeFilename('%(title)s.%(ext)s')})

# Generated at 2022-06-14 18:13:37.320663
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import sys
    sys.path.append('..')
    from ydl.downloader.common import FileDownloader
    d = FileDownloader({'outtmpl': '/tmp/%(stitle)s.%(ext)s'})
    x = XAttrMetadataPP(d)
    return x

if __name__ == '__main__':
    x = test_XAttrMetadataPP()
    print(x)

# Generated at 2022-06-14 18:13:39.893779
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    filename = 'video.mp4'
    pp = XAttrMetadataPP()
    assert pp._run_hooks({'filepath': filename}) == ([], {"filepath": filename})

# Generated at 2022-06-14 18:13:41.444512
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xamd = XAttrMetadataPP(None)

# Generated at 2022-06-14 18:13:49.237710
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import tempfile
    from ..extractor.common import InfoExtractor
    from ..utils import encodeFilename

    # Use a temporary directory to avoid messing up with current ones
    temp_dir = tempfile.mkdtemp()
    file_path = encodeFilename(os.path.join(temp_dir, "video.mp4"))

    ie = InfoExtractor()
    ie.add_default_info_extractors()

    # Test the XAttrMetadataPP constructor
    pp = XAttrMetadataPP(ie, {'filepath': file_path})

    # Remove the temporary directory
    os.rmdir(temp_dir)


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:13:59.323705
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # 1. Create an object of class XAttrMetadataPP
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    pp = XAttrMetadataPP(ydl)

    # 2. Create an object of class YoutubeDL
    #    Save the metadata in its dict.
    from .test_YoutubeDL import test_YoutubeDL_process_ie_result
    ie_result = test_YoutubeDL_process_ie_result()
    info = {}
    for key, value in ie_result.items():
        info[key] = value

    # 3. Fake the _downloader.to_screen method.
    import sys
    from io import StringIO
    # Save stdout
    old_stdout = sys.stdout
    # Fake stdout
    sys.stdout = mystdout

# Generated at 2022-06-14 18:14:10.601314
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import tempfile

    from ..utils import xattr

    d = {
        'webpage_url': 'http://www.youtube.com/watch?v=BaW_jenozKc',
        'title': 'youtube-dl test video "_ä↭𝕐',
        'upload_date': '20121002',
        'description': 'test chars:  \"\'/\\ä↭𝕐',
        'uploader': 'Philipp Hagemeister',
        'format': '17 - 640x360 (medium)',
    }

    postprocessor = XAttrMetadataPP(None)
    fd, temp_filename = tempfile.mkstemp()
    os.close(fd)
    r, _ = postprocessor.run(dict(d, filepath=temp_filename))

    assert r == []



# Generated at 2022-06-14 18:14:18.334611
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .test_common import FakeYDL
    from .test_PostProcessor import unit_test_run

    ydl = FakeYDL()
    fake_info = {
        'id': '8O-kpPvA_ro',
        'webpage_url': 'https://www.youtube.com/watch?v=8O-kpPvA_ro',
        'title': 'Video title',
        'upload_date': '20150806',
        'description': 'Video description',
        'uploader': 'Author',
        'format': 'format',
    }
    ydl.add_info_extractors()
    ydl.add_post_processors(XAttrMetadataPP())
    unit_test_run(ydl, [], fake_info)
    assert ydl.get_fake_

# Generated at 2022-06-14 18:14:20.635194
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:14:25.059896
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ Test XAttrMetadataPP class, constructor. """
    assert XAttrMetadataPP, 'Failed to load class XAttrMetadataPP'
    # Test constructor
    assert XAttrMetadataPP(None), 'Failed to construct instance of class XAttrMetadataPP'

# Generated at 2022-06-14 18:15:07.116236
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(123)


# Generated at 2022-06-14 18:15:10.350804
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    dl = object()
    pp = XAttrMetadataPP(dl)
    assert pp.downloader is dl

# Generated at 2022-06-14 18:15:21.643247
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    class dummyDL(object):
        def to_screen(self, msg): print(msg)
        def report_warning(self, msg): print('warning: ' + msg)
        def report_error(self, msg): print('error: ' + msg)
    class dummyInfo(object):
        def get(self, key):
            if key == 'upload_date': return '20150101'
            if key == 'title': return 'foo'
            if key == 'description': return 'bar'
            if key == 'uploader': return 'someone'
            if key == 'webpage_url': return 'example.com'
            if key == 'ext': return 'mp4'
            if key == 'format': return 'video/mp4'
        def __getitem__(self, key):
            return self.get(key)
    info

# Generated at 2022-06-14 18:15:22.846554
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    assert isinstance(pp, XAttrMetadataPP)


# Generated at 2022-06-14 18:15:33.067705
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """
    Unit test for method run of class XAttrMetadataPP
    """

    # Test data
    info = {
        '_type': 'video',
        'webpage_url': 'https://www.youtube.com/watch?v=BaW_jenozKc',
        'title': 'youtube-dl test video "\'/\\ä↭𝕐',
        'upload_date': '20121002',
        'description': 'test chars:  "\'/\\ä↭𝕐\ntest URL: https://github.com/rg3/youtube-dl/issues/1892\n\nThis is a test video for youtube-dl.\n\nFor more information, contact phihag@phihag.de .',
        'uploader': 'phihag',
        'format': 'format',
    }



# Generated at 2022-06-14 18:15:34.829482
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

if __name__ == '__main__':
    test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:15:44.737880
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import string
    import tempfile

    tempdirname = tempfile.mkdtemp()
    filename = os.path.join(tempdirname, 'xattr_test')

    with open(filename, 'w') as f:
        f.write(string.ascii_letters)

    def _has_xattr(filename):
        try:
            write_xattr(filename, 'user.testattr', 'test_value')
            return True
        except XAttrUnavailableError:
            return False


# Generated at 2022-06-14 18:15:46.109181
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP("/tmp/fake_filename.mp4")

# Generated at 2022-06-14 18:15:49.511731
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    #
    # TODO:
    #   * find a way to check if metadata is written to xattrs...
    #
    pass

test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:16:01.469431
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    from .common import FileDownloader
    from ..utils import USER_AGENT
    from ..extractor.common import InfoExtractor

    # execute FileDownloader with params
    params_dict = dict()
    params_dict['outtmpl'] = 'outtmpl.%(ext)s'
    params_dict['quiet'] = True
    params_dict['nocheckcertificate'] = True
    params_dict['forcetitle'] = False
    params_dict['noplaylist'] = True
    params_dict['sleep_interval'] = 0
    params_dict['format'] = 'mp4'
    params_dict['verbose'] = True
    params_dict['ignoreerrors'] = False
    params_dict['forceurl'] = False
    params_dict['forcethumbnail'] = False
    params

# Generated at 2022-06-14 18:17:40.244290
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    metadata_PP = XAttrMetadataPP()

    # test infos
    infos = {
        'id': 'test_id',
        'filepath': '/home/user/Downloads/test_file.flv',
        'title': 'test_title',
        'webpage_url': 'http://test_url.com',
        'description': 'test_description',
        'uploader': 'test_uploader',
        'format': 'test_format',
        'upload_date': '20130103'
        }

    # test run
    metadata_PP.run(infos)
    assert infos['id'] == 'test_id'
    assert infos['filepath'] == '/home/user/Downloads/test_file.flv'
    assert infos['title'] == 'test_title'


# Generated at 2022-06-14 18:17:49.251193
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .test_utils import FakeYDL

    # Testing of extended attributes for Python 3.4+
    # Note: extended attributes for Python 2.7 are tested in ext attr module test (TODO: merge those tests)
    if hasattr(__import__('xattr'), 'setxattr'):
        import tempfile
        import shutil

        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()

        # Put a file into the temporary directory
        filename = 'foo'
        filepath = os.path.join(temp_dir, filename)
        with open(filepath, 'w') as f:
            f.write('')

        # Test metadata

# Generated at 2022-06-14 18:17:52.050631
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(object)
    assert pp.name == 'xattrs'
    assert pp.description == 'Writing metadata to file\'s xattrs'

# Generated at 2022-06-14 18:18:03.792026
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # When downloader is initialized with '--no-mtime'
    #   Flag forces the creation of new file with current timestamp
    downloader = FakeYDL(params={'no_mtime': True})
    postprocessor = XAttrMetadataPP(downloader)

    # fake info object
    info = {
        'filepath': '/tmp/a_video.mp4',
        'title': 'A Video',
        'upload_date': '20140101',
        'uploader': 'John Doe',
        'webpage_url': 'https://www.youtube.com/watch?v=example',
        'description': 'Test Video',
        'format': 'Format',
    }

    # Assert that video is processed successfully
    errors, info_returned = postprocessor.run(info)

# Generated at 2022-06-14 18:18:05.633052
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    try:
        XAttrMetadataPP(None)
    except AttributeError as e:
        assert type(e) == AttributeError

# Generated at 2022-06-14 18:18:15.104127
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    def _test(self, info, expected_success, expected_info):
        """
            Test method run of class XAttrMetadataPP.
            Checks if written extended attributes are as expected.
        """
        success, result_info = self.pp.run(info)
        self.assertEqual(success, expected_success)

        for k in result_info:
            self.assertEqual(result_info[k], expected_info[k])

    import unittest
    from .test_utils import FakeYDL

    class XAttrMetadataPPTest(unittest.TestCase):
        """ Test class XAttrMetadataPP. """

        def setUp(self):
            self.pp = XAttrMetadataPP()


# Generated at 2022-06-14 18:18:16.207624
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    inst = XAttrMetadataPP()
    assert inst.name == 'metadata'

# Generated at 2022-06-14 18:18:28.204309
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor.youtube import YoutubeIE
    from ..utils import determine_ext
    import os
    import tempfile
    import xattr

    # Skip this test if xattr is not supported
    if compat_os_name != 'nt' and not xattr.is_enabled(tempfile.mkdtemp()):
        print('xattr not supported (skipping test)')
        return

    # Create temp file
    temp_dir = tempfile.mkdtemp(prefix='ytdl_')
    temp_file_path = os.path.join(temp_dir, 'test_file')
    open(temp_file_path, 'a').close()

    # Test setting xattrs on a simple file

# Generated at 2022-06-14 18:18:29.245041
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert pp is not None

# Generated at 2022-06-14 18:18:40.415521
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import gen_extractors
    for ie in gen_extractors():
        if ie.IE_DESC == 'Test IE':
            break

    info = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'format': 'format',
        'webpage_url': 'webpage_url',
        'thumbnail': 'thumbnail',
        'duration': 'duration',
        'view_count': 'view_count',
        'like_count': 'like_count',
        'dislike_count': 'dislike_count',
        'average_rating': 'average_rating',
        'formats': 'formats',
        'is_live': 'is_live',
    }

    pp = XAttrMetadataPP(ie._downloader)