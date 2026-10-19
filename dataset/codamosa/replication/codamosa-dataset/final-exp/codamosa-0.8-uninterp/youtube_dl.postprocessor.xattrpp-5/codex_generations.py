

# Generated at 2022-06-14 18:09:13.763105
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    def setup_module():
        global temp_filename, temp_dir
        import tempfile
        temp_dir = tempfile.mkdtemp()

    def teardown_module():
        import os
        os.rmdir(temp_dir)

    import os
    import xml.etree.ElementTree as ET
    from .common import FileDownloader
    from .extractor import gen_extractors
    from ..utils import platform_module
    from .format import Extractor

    setup_module()

    class TestDownloader(FileDownloader):
        _xattr = platform_module.XAttrMetadataPP()

        def __init__(self, ydl, params):
            self.params = params
            self.ydl = ydl
            self.extractor = Extractor()


# Generated at 2022-06-14 18:09:15.120771
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    xattrMetadataPP = XAttrMetadataPP(None)
    assert xattrMetadataPP.run({}) == ([], {})


# Generated at 2022-06-14 18:09:26.107815
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import PreparedFFmpegPCMAudioPP
    # Create a file for test
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(prefix='test_XAttrMetadataPP_', suffix='.mp4')
    temp_file.close()


# Generated at 2022-06-14 18:09:27.536623
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Testing class
    XAttrMetadataPP({})

# Generated at 2022-06-14 18:09:36.974339
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FileDownloader
    from ..compat import compat_os_name

    if compat_os_name == 'nt':
        return # xattr is not available on NTFS as of 2018-11-08

    testcases = [
        {
            'filepath': '/path/to/video.ext',
            'webpage_url': 'https://www.youtube.com/watch?v=VIDEOID',
            'title': 'Foo Bar',
            'upload_date': '20190228',
            'description': 'Great video',
            'uploader': 'author',
            'format': 'mp4',
        },
    ]

    for testcase in testcases:
        downloader = FileDownloader({})
        downloa

# Generated at 2022-06-14 18:09:39.780257
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert pp is not None

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:09:41.969019
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO
    #   Implement this unit test.
    pass

# Generated at 2022-06-14 18:09:44.585716
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_pp = XAttrMetadataPP()
    assert xattr_pp is not None

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:09:48.225595
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    youtube_downloader = YoutubeDL()
    youtube_downloader.add_post_processor(XAttrMetadataPP())

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:09:49.145239
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP({})

# Generated at 2022-06-14 18:10:03.977705
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import tempfile
    import xattr
    import os
    import errno


# Generated at 2022-06-14 18:10:16.434053
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os

    from ..utils import xattr_get, xattr_set


    # Start with empty xattrs
    filename = 'video.mp4'
    xattr_set(filename, 'user.xdg.test.test0', b'0')
    xattr_set(filename, 'user.xdg.test.test1', b'1')
    xattr_names = xattr_get(filename)
    assert xattr_names == ['user.xdg.test.test0', 'user.xdg.test.test1']
    os.remove(filename)


# Generated at 2022-06-14 18:10:26.479902
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import tempfile

    # Create a temp file
    temp_filename = tempfile.mkstemp()[1]
    # ... and delete it
    os.remove(temp_filename)

    class FakeInfo(dict):
        def __init__(self, metadata):
            dict.__init__(self, metadata)
            self['filepath'] = temp_filename

    class FakeYDL(object):
        def __init__(self):
            self.params = {
                'writethumbnail': False,
                'writesubtitles': False,
                'writeautomaticsub': False,
                'simulate': True
            }

        def to_screen(self, msg):
            print(msg)

        def report_warning(self, msg):
            print(msg)


# Generated at 2022-06-14 18:10:27.441340
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP({})

# Generated at 2022-06-14 18:10:38.757125
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile, os
    from .test_postprocessor import PostProcessorTestCase

    xattrdata = {'webpage_url': 'http://example.com', 'title': 'some title', 'upload_date': '2010', 'description': 'some description',
                 'uploader': 'uploader', 'format': 'some_format'}

    class MockYdl(object):
        def __init__(self):
            self.to_screen_calls = []
            self.report_warning_calls = []

        def to_screen(self, msg):
            self.to_screen_calls.append(msg)

        def report_warning(self, msg):
            self.report_warning_calls.append(msg)

        def report_error(self, msg):
            self.report_warning_calls.append

# Generated at 2022-06-14 18:10:50.758761
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader import FileDownloader
    from ..extractor import gen_extractors
    from ..utils import dict_keys_to_lower

    info = dict_keys_to_lower({
        'webpage_url': 'https://www.youtube.com/watch?v=BaW_jenozKc',
        'title': "Yogscast Lewis & Simon - Minecraft - Dusty's Crazy Craft",
        'upload_date': '20120804',
        'description': '...',
        'uploader': 'Yogscast Lewis & Simon',
        'format': 'mp4',
    })

    dl = FileDownloader({})
    gen_extractors()

    pp = XAttrMetadataPP(dl)
    pp.run(info)

# Generated at 2022-06-14 18:10:59.578312
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..extractor.common import InfoExtractor
    from ..utils import encode_dict, encode_data_uri
    from ..compat import compat_urllib_parse_unquote

    class FakeInfoExtractor(InfoExtractor):
        def __init__(self, origin_ie, video_id):
            self.origin_ie = origin_ie
            self.video_id = video_id
            self.title = 'FooBar Baz'
            self.description = 'Foo Bar Baz'
            self.uploader = 'Baz'
            self.upload_date = '20150102'
            self.webpage_url = 'http://example.com/watch?v=%s' % video_id

# Generated at 2022-06-14 18:11:02.369298
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    def _check_run(self):
        pass

    XAttrMetadataPP.run = _check_run
    XAttrMetadataPP(None)

# Generated at 2022-06-14 18:11:04.580205
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-14 18:11:14.672494
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import filecmp
    import os
    import tempfile

    filename = tempfile.mkstemp()

# Generated at 2022-06-14 18:11:36.279479
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..downloader import Downloader
    from ..compat import compat_str

    # init
    d = Downloader(params={})
    d.add_info_extractor(None)
    pp = XAttrMetadataPP(d)
    d.postprocessors.append(pp)

    # run

# Generated at 2022-06-14 18:11:37.641391
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(None).run({})[0] == []

# Generated at 2022-06-14 18:11:46.222422
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    filename = 'somefilename'
    info = {
        'title': 'sometitle',
        'description': 'somedescription',
        'uploader': 'someuploader',
        'upload_date': 'someuploaddate',
        'format': 'someformat',
        'webpage_url': 'somewebpageurl',
    }
    pp = XAttrMetadataPP(None)
    (exit_code, result_info) = pp.run(info)
    assert exit_code == []
    assert info == result_info

# Generated at 2022-06-14 18:11:52.374395
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import sys

    try:
        # Initialize the config
        from .. import YoutubeDL
        ydl = YoutubeDL({})
        pp = XAttrMetadataPP(ydl)
        assert pp.get_name() == 'xattrmovie'
    except Exception as e:
        print('Error in XAttrMetadataPP: ' + str(e))
        print('  on line ' + str(sys.exc_info()[-1].tb_lineno))
        raise e # Re-raise exception if something went wrong
        assert False



# Generated at 2022-06-14 18:11:55.047000
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # pylint: disable=E0102
    # pylint: disable=W0613


    # XAttrMetadataPP.run is tested when XAttrWriteTestCase is run
    pass

# Generated at 2022-06-14 18:12:06.282747
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    msg_template = 'Unexpected result with file{}: {}'
    pp = XAttrMetadataPP()

    #
    #  Testing user.xdg.referrer.url xattr writing
    #

    file1 = {
        'title': 'Webpage URL',
        'webpage_url': 'http://www.webpage-url.com',
        'format': 'video/mp4',
        'filepath': 'file1.mp4'
    }

    file2 = {
        'title': 'Webpage URL',
        'format': 'video/mp4',
        'filepath': 'file2.mp4'
    }

    expected_file1 = os.path.splitext(file1['filepath'])[0]
    expected_file1 += '.mp4'


# Generated at 2022-06-14 18:12:07.354961
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP(None)

# Generated at 2022-06-14 18:12:07.947233
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:12:11.899208
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    # We don't test the extended attributes functionality because a working xattr implementation
    # is needed to execute the test and this is not always the case. Anyway, the implementation of
    # the xattr metadata post-processor does not change anymore.
    pass

# Generated at 2022-06-14 18:12:13.488537
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
	assert XAttrMetadataPP(None).get_type() == 'xattrs'

# Generated at 2022-06-14 18:12:41.930919
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Import json library that Qt can't import
    import json
    # We are using this kind of imports because we can't use an external library
    from ..compat import compat_basestring
    from ..utils import XAttrUnavailableError

    # We are using this kind of imports because we can't use an external library
    from .common import PostProcessorTest
    from .pp_json import PP_jsonTest
    from .pp_xattr import PP_xattrTest
    import os

    # Get the path of a test JSON file
    json_path = PP_jsonTest.get_file_path()

    # Get the path of a test video file
    video_path = PP_xattrTest.get_file_path()

    # Copy the test video file
    video_path_copy = video_path + '.copy'
    os.system

# Generated at 2022-06-14 18:12:53.996056
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    from io import BytesIO
    from ..downloader import Downloader
    import tempfile

    info = {
        'webpage_url': 'https://example.com',
        'description': 'A video about stuff.',
        'title': 'A video about stuff',
        'upload_date': '20170608',
        'uploader': 'Example User',
        'format': 'webm'
    }

    tmpdir = tempfile.mkdtemp()
    tmpfile = os.path.join(tmpdir, 'test.mp4')

    with open(tmpfile, 'wb') as f:
        f.write(b' ' * 1024 * 1024 * 1024)


# Generated at 2022-06-14 18:13:04.790225
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """
    Unit test for method run of class XAttrMetadataPP.
    """
    downloader = None # How to mock this?
    pp = XAttrMetadataPP(downloader)

    # Failure due to nonexisting file
    info = {'filepath': 'nonexisting_file'}
    res, info = pp.run(info)
    assert res == []
    assert info == info

    # Failure due to not supporting xattrs
    # TODO: How to mock XAttrUnavailableError?
    # info = {'filepath': 'fake_file'}
    # res, info = pp.run(info)
    # assert res == []
    # assert info == info

# Generated at 2022-06-14 18:13:08.222441
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # test1:
    # Test if post processor is initialized correctly

    post_processor = XAttrMetadataPP()

    assert post_processor != None


# Generated at 2022-06-14 18:13:10.432416
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


#
# Extra metadata for archives (e.g. description, tags)
#

# Generated at 2022-06-14 18:13:13.094386
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    This function performs black-box unit testing for class XAttrMetadataPP.
    """

    # TODO: Change 'pass' to the tests you want to perform.
    pass

# Generated at 2022-06-14 18:13:23.389810
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    # This test tries to write xattrs to a temporary file,
    # and then checks if the xattrs are correctly written

    from .utils import InTemporaryDirectory
    from ..utils import encodeFilename

    with InTemporaryDirectory() as tmpdir:

        postprocessors = [XAttrMetadataPP()]

        # Create a temporary file
        import tempfile
        tmpfile = tempfile.NamedTemporaryFile(prefix='ytdl-test_', suffix='.webm', delete=False)
        tmpfile.write(b'content')
        tmpfile.close()


# Generated at 2022-06-14 18:13:31.355189
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FileDownloader
    from .common import FakeYDL
    from ..extractor import youtube_dl as youtube_dl_module

    pp = XAttrMetadataPP()
    pp.set_downloader(FileDownloader(FakeYDL()))

    # No xattr support

# Generated at 2022-06-14 18:13:41.857707
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from ..extractor import gen_extractors
    from ..utils import DateRange, parse_resolution

    # Create an instance of YoutubeIE (calling _real_extract causes the extraction of the url)
    ie = gen_extractors(['youtube'])[0]

    # Create a FakeYDL object
    ydl = FakeYDL()

    # Create a downloader (from downloader.py)
    dl = Downloader(ydl)

    # Create a PostProcessor (from postprocessor.py)
    pp = XAttrMetadataPP(dl)

    # Define a video information

# Generated at 2022-06-14 18:13:49.920183
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..compat import compat_HTTPError
    import tempfile
    import os

    class FakeInfoDict(dict):
        def __init__(self, *args, **kwargs):
            self['filepath'] = tempfile.mkstemp()[1]
            self.update(*args, **kwargs)

        def __del__(self):
            try:
                os.remove(self['filepath'])
            except KeyError:
                pass

    class FakeYDL(object):
        def __init__(self):
            self._progress_hooks = []

        def add_progress_hook(self, f):
            self._progress_hooks.append(f)

        def to_screen(self, message):
            pass

        def report_warning(self, message):
            raise compat_HTTPError(message)



# Generated at 2022-06-14 18:14:41.056935
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..compat import compat_xattr

    import time
    import tempfile

    # use a temporary file
    tmpfile = tempfile.NamedTemporaryFile()
    filename = tmpfile.name

    # add some xattrs
    dummy_xattrs = {
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
    }
    byte_value = 'value'.encode('utf-8')
    for xattrname, infoname in dummy_xattrs.items():
        write_xattr(filename, xattrname, byte_value)

    # add some info

# Generated at 2022-06-14 18:14:48.299670
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor.youtube import YoutubeIE
    # import the PostProcessor class
    from ..postprocessor.common import PostProcessor
    # Create an instance of XAttrMetadataPP class
    x= XAttrMetadataPP()
    # Test if the instance variable downloader is empty or not
    assert isinstance(x._downloader, PostProcessor) is False
    # Test if the instance variable downloader is a YoutubeIE object
    assert isinstance(x._downloader, YoutubeIE) is False

# Generated at 2022-06-14 18:14:56.057895
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """ Unit test for method run of class XAttrMetadataPP """

    from ..compat import compat_os_name
    from ..utils import DownloadInfo

    if compat_os_name == 'nt':
        return

    import tempfile

    tempfile.tempdir = '/tmp'
    filepath = tempfile.mkstemp()[1]

    info = DownloadInfo(
        {'filepath': filepath, 'webpage_url': 'http://example.org', 'title': 'Test title',
         'upload_date': '20170129', 'uploader': 'Test uploader', 'format': 'ext'})

    pp = XAttrMetadataPP()
    retcode, newinfo = pp.run(info)
    assert retcode == []
    assert newinfo is info

# Generated at 2022-06-14 18:15:06.184375
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile, os
    from ..extractor.common import InfoExtractor

    def get_temp_filename(suffix=None):
        if suffix is None:
            return tempfile.mktemp(prefix='ytdl-test_XAttrMetadataPP')
        else:
            return tempfile.mktemp(suffix=suffix, prefix='ytdl-test_XAttrMetadataPP')

    def make_xattr_unavailable_error(filename, attr):
        # Mock
        class XAttrUnavailableError(Exception): pass
        e = XAttrUnavailableError()
        e.filename = filename
        e.attr = attr
        return e


# Generated at 2022-06-14 18:15:15.463793
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FileDownloader
    downloader = FileDownloader(None, None)


# Generated at 2022-06-14 18:15:19.463799
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattrs = XAttrMetadataPP(None)
    assert xattrs is not None

# With this test we can invoke the constructor of the Post Processor
# as a standalone program
if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:15:30.893949
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    """ test 1:
        if self.run(info) returns ([], info), it's ok
    """

    from .common import PostProcessor
    from ..extractor import YoutubeIE, YoutubePlaylistIE
    from ..downloader import FileDownloader

    from .common import unknown_error
    from .xattr import XAttrMetadataError

    # Fake instance of the InfoExtractor class
    class FakeInfoExtractor:
        def __init__(self, ie_name):
            self.ie_name = ie_name
            self.params = {
                'username': 'Man',
                'playlist_id': 'PL4B4C89E558EEE881',
            }

    # Fake instance of the FileDownloader class
    class FakeFileDownloader(FileDownloader):
        ie = FakeInfoExtractor('FakeIE')

       

# Generated at 2022-06-14 18:15:33.224934
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr = XAttrMetadataPP(PostProcessor())
    assert xattr


# Generated at 2022-06-14 18:15:41.271033
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import re

    if compat_os_name == 'nt':
        # XXX: xattrs won't work on windows. :(
        return
    from .common import FileDownloader
    from .common import calc_filesize
    from .common import prepare_extractor
    from .common import prepare_args
    from .common import YOUTUBE_IE_NAME
    from .common import YOUTUBE_URL_TEMPLATE
    from .common import sanitize_open

    from ..utils import get_xattr
    from ..utils import remove_xattr

    args = prepare_args()
    args.simulate = True
    args.writeinfojson = True
    args.writethumbnail = True
    args.writesubtitles = True
    args.writeautomaticsub = True


# Generated at 2022-06-14 18:15:49.723623
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # See https://github.com/ytdl-org/youtube-dl/pull/15347
    # for a motivation of this test

    import os
    import xattr
    import tempfile

    from .common import FileDownloader
    from .extractor import YoutubeIE
    from .downloader.common import FFmpegExtractAudioPP
    from .downloader.http import HttpFD
    from .downloader.http.external_downloader import WgetFD
    from .downloader.youtube import YoutubeDL
    from .utils import dispatch_event
    from .jsinterp import JSInterpreter


# Generated at 2022-06-14 18:17:24.423832
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    from ..utils import xattr_set
    from ..compat import compat_os_name

    #
    # This will only work on Linux with xattr support (usually only on recent extfs)
    # and xattr python bindings available.
    #
    if compat_os_name != 'posix' or not xattr_set:
        return


# Generated at 2022-06-14 18:17:25.024160
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:17:37.266864
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """
    This method tests the method run of class XAttrMetadataPP.
    It tries to set extended attributes on a fake downloaded file.
    """
    import os
    import tempfile
    from ..downloader import Downloader
    from ..utils import xattr_supported

    # Define a fake Downloader object
    class FakeDownloader(Downloader):
        def to_screen(self, text):
            """
            Print the message to stdout.
            :param text: message to print
            """
            print(text)

        def report_warning(self, text):
            """
            Report the message by printing it to stdout.
            :param text: message to print
            """
            print(text)


# Generated at 2022-06-14 18:17:47.138921
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile
    import os
    import shutil

    class PostProcessorTester(PostProcessorTester):

        def __init__(self):
            self.has_xattr_support = True
            self.values_to_write = {}
            self.written_values = []
            self._temp_file_descriptor, self._temp_file_path = tempfile.mkstemp(prefix='yt-dl-test_', suffix='.mp4')
            self._temp_dir_path = tempfile.mkdtemp(prefix='yt-dl-test_')


# Generated at 2022-06-14 18:17:49.684527
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Create an instance of XAttrMetadataPP
    """
    test_downloader = object()

    pp = XAttrMetadataPP(test_downloader)

    assert pp._downloader is test_downloader

# Generated at 2022-06-14 18:17:51.733278
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """Test XAttrMetadataPP constructor and name property."""

    pp = XAttrMetadataPP(None)
    assert pp.name == 'xattrs'

# Generated at 2022-06-14 18:17:55.437117
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    obj = XAttrMetadataPP('/tmp/dummy-file')

    assert obj is not None


# Generated at 2022-06-14 18:17:56.117670
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:17:57.146236
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    x = XAttrMetadataPP(None)

# Generated at 2022-06-14 18:18:08.996388
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    codecs_old = sys.stdout.encoding