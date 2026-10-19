

# Generated at 2022-06-14 18:09:04.878160
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
     metadata_pp = XAttrMetadataPP('--yt-download')
     assert isinstance(metadata_pp, XAttrMetadataPP)

# Generated at 2022-06-14 18:09:13.454602
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import pytest

    from .common import test_pp_expected_results

    from ..compat import compat_os_name

    from ..extractor.common import InfoExtractor
    from ..utils import XAttrMetadataError

    ie = InfoExtractor()
    ie.extract = lambda url: InfoExtractor.suitable(lambda: {'url': url})

    class FakeFile:

        def __init__(self, name, xattrs):
            self.name = name
            self.xattrs = xattrs

        def __repr__(self):
            return 'FakeFile(%r)' % self.name


# Generated at 2022-06-14 18:09:15.121454
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """Unit test for constructor of class XAttrMetadataPP"""
    from ..downloader import FakeYDL
    ydl = FakeYDL()
    XAttrMetadataPP(ydl)

# Generated at 2022-06-14 18:09:26.108981
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """
    Test if XAttrMetadataPP can set extended attributes on downloaded file.

    Expected extended attributes:
        * user.xdg.referrer.url -> 'webpage_url'
        * user.xdg.comment -> 'description'
        * user.dublincore.title -> 'title'
        * user.dublincore.date -> 'upload_date'
        * user.dublincore.description -> 'description'
        * user.dublincore.contributor -> 'uploader'
        * user.dublincore.format -> 'format'
    """

    import os
    import tempfile

    from ..compat import unittest

    from .common import FakeInfoExtractor

    # Create the temporary file to be downloaded

# Generated at 2022-06-14 18:09:36.752276
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import tempfile
    from .common import FileDownloader
    from .common import FakeInfoExtractor


    class FakeFileDownloader(FileDownloader):
        def __init__(self, *args, **kargs):
            super(FakeFileDownloader, self).__init__(*args, **kargs)
            self.to_screen_calls = []

        def to_screen(self, *args, **kargs):
            self.to_screen_calls.append({
                'args' : args,
                'kargs': kargs,
            })

        def report_error(self, *args, **kargs):
            self.report_error_calls = []
            self.report_error_calls.append({
                'args' : args,
                'kargs': kargs,
            })


# Generated at 2022-06-14 18:09:37.672278
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP({})

# Generated at 2022-06-14 18:09:48.508659
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader import FileDownloader
    from ..YoutubeDL import YoutubeDL
    from .common import FileDownloaderTest
    from .test_postprocessor import downloader_test
    from .test_extractors import download_test_file_mock

    def test_result(self):
        """ Test if the JSON file is being generated correctly. """

        self.assertIn('filepath', self.ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc']))

    # Mock the downloader to use our test-downloader instead
    YoutubeDL.__bases__ = (download_test_file_mock, FileDownloaderTest) + YoutubeDL.__bases__
    FileDownloader.__bases__ = (download_test_file_mock,) + FileDownloader.__bases

# Generated at 2022-06-14 18:09:50.899942
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:09:52.806652
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    constructor = XAttrMetadataPP('test', 'test')
    assert constructor.__str__() == 'XAttrMetadataPP'

# Generated at 2022-06-14 18:10:01.909905
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .test_postprocessor_exec import _run_pp_test
    _run_pp_test(XAttrMetadataPP,
                 ['webpage_url', 'title', 'upload_date', 'uploader', 'format', 'description'],
                 {'format': 'format #0',
                  'webpage_url': 'webpage_url #0',
                  'title': 'title #0',
                  'upload_date': 'upload_date #0',
                  'uploader': 'uploader #0',
                  'description': 'description #0'},
                 output_count = 0,
                 skip_msg = 'xattr not supported')

# Generated at 2022-06-14 18:10:17.741505
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from unittest import TestCase
    from .common import FakeYDL

    class FakeFile(object):
        pass

    class Dummy(object):
        def __init__(self):
            return

    def fake_write_xattr(filename, xattrname, byte_value):
        global fake_write_xattr_called_count
        fake_write_xattr_called_count += 1

        assert filename is not None
        assert xattrname is not None
        assert byte_value is not None

        return

    fake_write_xattr_called_count = 0
    file = FakeFile()
    downloader = FakeYDL()
    pp = XAttrMetadataPP(downloader)


# Generated at 2022-06-14 18:10:27.392270
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .test import PostProcessorTestCase
    from io import BytesIO
    from ..utils import encodeFilename

    class XAttrMetadataPP_runTestCase(PostProcessorTestCase):

        pp = XAttrMetadataPP()

        def setUp(self):
            self.filepath = encodeFilename('test.mp3')
            # Creating fake file
            self.fd = open(self.filepath, 'wb' , 0)
            self.fd.write(b'test')
            self.fd.close()


# Generated at 2022-06-14 18:10:29.064521
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_metadata = XAttrMetadataPP()
    assert xattr_metadata is not None


# Generated at 2022-06-14 18:10:37.837150
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile
    from .f4m import F4mPP
    from .hls import HlsPP

    # Test with f4m manifest
    manifest_url = 'http://playertest.longtailvideo.com/adaptive/oceans_aes/oceans_aes.f4m'
    filepath = tempfile.mkstemp()[1]
    info = {
        'filepath': filepath,
        'webpage_url': 'http://www.youtube.com/watch?v=yif5R5W5bck'
    }
    f4m_pp = F4mPP(None)
    _, info = f4m_pp.run(info)
    _, info = XAttrMetadataPP(None).run(info)

# Generated at 2022-06-14 18:10:41.073610
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    try:
        m = XAttrMetadataPP(None)
        m.run(None)
    except BaseException:
        assert False, 'Failed to initialize XAttrMetadataPP'

# Generated at 2022-06-14 18:10:42.925422
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    postProcessor = XAttrMetadataPP()
    assert postProcessor.name == 'xattrs'

# Generated at 2022-06-14 18:10:45.133177
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()

    # test no xattr support
    assert pp._supports_xattrs() == False

# Generated at 2022-06-14 18:10:56.201388
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from collections import namedtuple
    from tempfile import NamedTemporaryFile
    from ..utils import (
        XAttrMetadataError,
        XAttrUnavailableError,
        get_filesystem_encoding,
        read_xattr,
    )

    def run_test(filename, use_tempfile=False, xattr_mapping=None):
        if use_tempfile:
            if filename is None:
                file_obj = NamedTemporaryFile(delete=False)
            else:
                file_obj = NamedTemporaryFile(delete=False, suffix=filename)
            filename = file_obj.name
            file_obj.close()

        info = namedtuple('Info', 'filepath webpag_url title upload_date uploader format description')
        info.filepath = filename
        info.webpage_url

# Generated at 2022-06-14 18:11:08.038927
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import GenYoutubeIE
    from ..downloader import YoutubeDL
    from ..compat import compat_os_name

    # Test constructor
    if compat_os_name == 'nt':
        pp = XAttrMetadataPP()
        assert pp is None, 'This class should not be used on Windows !'

    else:
        test_url = 'https://www.youtube.com/watch?v=BaW_jenozKc'

        youtube_dl_opts = {
            'logger': YoutubeDL.basic_config(),
            'progress_hooks': [],
        }

        try:
            XAttrMetadataPP(youtube_dl_opts)
        except:
            assert False, 'The constructor failed !'

    # Test run method
    # - with no metadata

# Generated at 2022-06-14 18:11:09.267603
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO: Add test to method run of class XAttrMetadataPP
    pass

# Generated at 2022-06-14 18:11:19.931925
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:11:24.809404
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattrs_pp = XAttrMetadataPP(object())
    assert xattrs_pp.last_download["entries"][0]["url"] == "https://github.com/ytdl-org/youtube-dl/issues/new"
    assert xattrs_pp.last_download["entries"][0]["title"] == "report xattr bugs"

# Generated at 2022-06-14 18:11:28.008433
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Test XAttrMetadataPP.__init__()
    """
    # Test empty constructor
    v = XAttrMetadataPP(None)
    assert isinstance(v, XAttrMetadataPP)

# Generated at 2022-06-14 18:11:29.320384
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    metadata_pp = XAttrMetadataPP()

# Generated at 2022-06-14 18:11:40.984319
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import sys
    import os
    import io
    import tempfile
    from ..utils import (
        xattr_available,
    )

    def get_info_from_file(filename):
        info = {
            'webpage_url': 'http://webpage_url',
            'title':       'title',
            'upload_date': '20150115T120000',
            'description': 'description',
            'uploader':    'uploader',
            'format':      'format',
        }

        filepath = os.path.abspath(filename)
        info['filepath'] = filepath
        old_stdout = sys.stdout
        sys.stdout = tempstdout = io.BytesIO()

        pp = XAttrMetadataPP()
        pp.run(info)

        sys.stdout

# Generated at 2022-06-14 18:11:42.372144
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    return pp is not None

# Generated at 2022-06-14 18:11:51.892324
# Unit test for method run of class XAttrMetadataPP

# Generated at 2022-06-14 18:12:02.567734
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import unittest
    import sys
    import os
    import tempfile
    import xattr
    from .common import FileDownloader

    class TestXAttrMetadataPP(unittest.TestCase):

        def setUp(self):
            self.downloader = FileDownloader({})

        def get_temp_filepath(self, filename):
            tempdir = tempfile.gettempdir()
            return os.path.join(tempdir, filename)

        def get_xattr_value(self, filepath, xattrname):
            return xattr.getxattr(filepath, xattrname)

        def has_xattr(self, filepath, xattrname):
            try:
                self.get_xattr_value(filepath, xattrname)
            except IOError:
                return False

# Generated at 2022-06-14 18:12:15.113589
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FFmpegPostProcessor
    from ..downloader.common import FileDownloader
    from ..extractor import YoutubeIE
    from .xattr import XAttrMetadataPP
    from ..utils import query_xattr

    # Get the video info
    # TODO: make it work with live streams too
    info_dict = YoutubeIE()._real_extract('https://www.youtube.com/watch?v=BaW_jenozKc')

    # Get the downloaded filepath

# Generated at 2022-06-14 18:12:15.589158
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:12:43.285799
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..downloader import YoutubeDL
    import tempfile
    import os
    from .common import FileDownloader

    # Create test file for XAttrMetadataPP
    fd, temp_filename = tempfile.mkstemp()
    os.close(fd)

    test_dl = YoutubeDL({'writeinfojson', 'writethumbnail'})
    test_dl.params['outtmpl'] = temp_filename
    test_dl.add_post_processor(XAttrMetadataPP())

    # Run test

# Generated at 2022-06-14 18:12:56.051367
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import prepend_extension

    pp = XAttrMetadataPP()
    pp.set_downloader(None) # hack to pass the PostProcessor.__init__ function


# Generated at 2022-06-14 18:13:04.639596
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from ..utils import DateRange
    from datetime import datetime

    # no xattrs support
    info = {
        'filepath': 'filepath',
        'webpage_url': 'webpage_url',
        # 'description':            'description',
        'title': 'title',
        'upload_date': datetime(2016, 4, 8),
        'description': 'description',
        'uploader': 'uploader',
        'format': 'format',
    }
    pp = XAttrMetadataPP()
    assert pp.run(info)[1] == info

    # no disk space left, disk quota exceeded or filesystem xattr limit exceeded

# Generated at 2022-06-14 18:13:05.208224
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

# Generated at 2022-06-14 18:13:16.383681
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import shutil
    from tempfile import mkdtemp
    from .test_kodion_helper import Test_YDL

    # Set up a temporary directory
    tmpdir = mkdtemp(prefix='ytdl_test_')

    # Create a fake file and fill it with contents
    filename = tmpdir + '/file.txt'
    testfile = open(filename, 'w')
    testfile_content = 'test\n'
    testfile.write(testfile_content)
    testfile.close()

    # Set up a test downloader and a fake set of options
    ydl = Test_YDL({'outtmpl': tmpdir + '/%(title)s-%(id)s.%(ext)s'})

    # Create a fake info dict

# Generated at 2022-06-14 18:13:17.276460
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

# Generated at 2022-06-14 18:13:20.641392
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_metadata_pp = XAttrMetadataPP()

    assert xattr_metadata_pp is not None


# Generated at 2022-06-14 18:13:25.897678
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Check if an instance of class XAttrMetadataPP can be created.
    """

    # Create an instance of XAttrMetadataPP
    xattr_metadata_pp = XAttrMetadataPP('youtube-dl', [], {}, None)

    xattr_metadata_pp.run({})


# Generated at 2022-06-14 18:13:27.081132
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    #TODO
    raise NotImplementedError



# Generated at 2022-06-14 18:13:39.258461
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import gen_extractors
    from ..utils import prepend_extractor
    import os

    ############
    # Prepare. #
    ############
    xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        'user.xdg.comment': 'description',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }

    # Tests for extended attributes on files.

# Generated at 2022-06-14 18:14:21.217533
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP({})

# Generated at 2022-06-14 18:14:30.780166
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FFmpegPostProcessor
    from ..downloader import FakeYDL
    from ..utils import FileDownloader
    from .get_filename import GetFileNamePP

    video_info = {
        "title": "Sintel",
        "id": "Sintel",
        "description": "By Blender Foundation",
        "upload_date": 20120101,
        "webpage_url": "http://www.youtube.com/watch?v=eRsGyueVLvQ",
        "uploader": "durian",
        "format": "720p",
        "filepath": "Sintel.mp4",
    }


# Generated at 2022-06-14 18:14:32.562911
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    res = XAttrMetadataPP()
    assert res

# Invoke test
test_XAttrMetadataPP()

# Generated at 2022-06-14 18:14:43.976542
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor.common import InfoExtractor


# Generated at 2022-06-14 18:14:55.555191
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    import youtube_dl.postprocessor
    from youtube_dl.utils import prepend_extension

    def get_xattr(attrname):
        import xattr
        return xattr.getxattr(test_filename, attrname).decode('utf-8')

    def get_xattr_len(attrname):
        import xattr
        attr = xattr.xattr(test_filename)
        return attr.get_size(attrname)

    # Prepare a temporary directory for this test
    tempdirname = tempfile.mkdtemp(prefix='ydl-unittest-')
    # Create a test file
    test_file = os.path.join(tempdirname, 'test.mp3')
    open(test_file, 'wb').close()
    # Prepend with

# Generated at 2022-06-14 18:15:05.462119
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from ..compat import unittest
    from ..utils import encodeFilename

    class MockYDL(object):

        def __init__(self):
            self.params = {
                'writedescription': True,
                'writeinfojson': True,
                'writethumbnail': True
            }

        def to_screen(self, msg):
            pass

        def report_warning(self, msg):
            pass

        def report_error(self, msg):
            pass

    class MockInfoDict(object):
        def __init__(self):
            self.infoname = 'infoval'

        def get(self, infoname):
            return self.infoname

    class MockTempFile(object):
        def __init__(self):
            self.name = encodeFilename(u'ABCD')

# Generated at 2022-06-14 18:15:15.149181
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile
    from .test_utils import downloader

    video = {
        'webpage_url': 'https://youtu.be/BaW_jenozKc',
        'title': 'youtube-dl test video "\'/\\ä↭𝕐',
        'upload_date': '20121002',
        'description': 'test chars:  "\'/\\ä↭𝕐\n\nxxx',
        'uploader': 'nschoe',
        'format': '17 - tiny',
    }

    postprocessor = XAttrMetadataPP(downloader)
    temp_filename, temp_fd = tempfile.mkstemp(prefix='ytdl_')

# Generated at 2022-06-14 18:15:20.780747
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    assert pp.name == 'xattr'
    assert pp.description == 'Set extended attributes on downloaded file'

    assert pp._accepted_info_keys == {"filepath", "title", "webpage_url", "upload_date", "description", "uploader", "format"}
    assert pp._accept_results == True

# Generated at 2022-06-14 18:15:21.591668
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:15:25.593898
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .test import get_test_info
    testinfo = get_test_info()
    testinfo['filepath'] = 'test1.tmp'

    return XAttrMetadataPP(None).run(testinfo)

# Generated at 2022-06-14 18:17:02.265587
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    import pytest
    import subprocess
    import textwrap
    from xattr import listxattr
    from subprocess import PIPE
    from ytdl.postprocessor.xattrm import XAttrMetadataPP
    #
    # Environment
    #
    # Default list of expected keys
    expected_keys = {
        'user.xdg.referrer.url',
        'user.xdg.comment',
        'user.dublincore.title',
        'user.dublincore.date',
        'user.dublincore.description',
        'user.dublincore.contributor',
        'user.dublincore.format',
    }
    #
    # Test cases
    # ==> usefixture 'mock

# Generated at 2022-06-14 18:17:06.873660
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    try:
        XAttrMetadataPP(None)
    except Exception as e:
        assert False, 'constructor of class XAttrMetadataPP raised an exception'
    else:
        assert True

# Generated at 2022-06-14 18:17:16.658432
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import tempfile

    info = {
        'filepath': tempfile.mkstemp()[1],
        'webpage_url': 'example.com',
        'title': 'Test',
        'upload_date': '20170101',
        'description': 'This is a test',
        'uploader': 'Uploader',
        'format': 'MP4',
    }


# Generated at 2022-06-14 18:17:19.871861
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_metadata_pp = XAttrMetadataPP()
    assert xattr_metadata_pp is not None

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:17:26.928355
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    class MockInfo():
        def __init__(self, info):
            self.info = info
        def get(self, key): # MockInfo.get method
            return self.info[key]

    class MockDownloader():
        def __init__(self):
            self.to_screen_message = None
            self.report_error_message = None
            self.report_warning_message = None

        def to_screen(self, msg):
            self.to_screen_message = msg

        def report_error(self, msg):
            self.report_error_message = msg

        def report_warning(self, msg):
            self.report_warning_message = msg


# Generated at 2022-06-14 18:17:31.013627
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


if __name__ == '__main__':
    print('Testing XAttrMetadataPP.run')
    test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:17:41.431244
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():

    res = {'formats': [{'protocol': 'm3u8_native', 'ext': 'mp4', 'vcodec': 'none'},
                       {'protocol': 'm3u8_native', 'ext': 'mp4', 'vcodec': 'none'},
                       {'protocol': 'm3u8_native', 'ext': 'mp4', 'vcodec': 'none'},
                       {'protocol': 'm3u8_native', 'ext': 'mp4', 'vcodec': 'none'},
                       {'protocol': 'm3u8_native', 'ext': 'mp4', 'vcodec': 'none'}]}

    xattr = XAttrMetadataPP({})
    xattr.run(res)

# Generated at 2022-06-14 18:17:49.283979
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    XAttrMetadataPP constructor test

    This function executes the constructor test of the class XAttrMetadataPP.

    First it creates an object of the class XAttrMetadataPP and then it checks if the object created is valid.
    """
    # Create an object of the class XAttrMetadataPP
    xattr_pp = XAttrMetadataPP()

    if xattr_pp == None:
        raise Exception('The object of the class XAttrMetadataPP is None and it should not be.')

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:18:01.564640
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..compat import compat_os_name
    import tempfile
    import os

    filename = os.path.join(tempfile.gettempdir(), 'youtube-dl_XAttrMetadataPP_test_file')

    # Create a temporary file so that we can populate its xattrs
    with open(filename, 'wb') as f:
        f.write(b'test file contents')

    tester = XAttrMetadataPP('XAttrMetadataPP')

# Generated at 2022-06-14 18:18:12.913773
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    with open('tests/testdata/test.mp4', 'rb') as fd:
        binary = fd.read()

    def download(ydl):
        return ydl.process_ie_result({
            '_type': 'mp4',
            'id': 'abcdefghij0123456789',
            'title': 'test video',
            'description': 'test description',
            'uploader': 'test uploader',
            'upload_date': '20150705',
            'ext': 'mp4',
            'format': '360p',
        }, {}, binary)

    class MockYDL(YoutubeDL):
        def report_warning(self, msg):
            assert False, msg
