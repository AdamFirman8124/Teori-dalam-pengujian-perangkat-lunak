

# Generated at 2022-06-14 18:09:08.899904
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xp = XAttrMetadataPP({})
    assert xp._downloader is None

# Generated at 2022-06-14 18:09:09.429193
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass  # TODO

# Generated at 2022-06-14 18:09:16.460483
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # initialize the module and its dependencies
    from .tests.test_postprocessor import module_init, module_run
    from .tests import get_testcases_input_output

    postprocessor = module_init(XAttrMetadataPP)

    for (testcase_input, testcase_output) in get_testcases_input_output(test_name=test_XAttrMetadataPP.__name__):

        # update post-processor properties
        postprocessor.exec_key = testcase_input.get('options', {}).get('exec_key', None)

        # execute the post-processor
        actual_output = module_run(postprocessor, testcase_input)

        # verify that the post-processor returns the expected output
        assert(actual_output == testcase_output)

# Test of run()

# Generated at 2022-06-14 18:09:25.987732
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    web_page_url = 'http://example.com/'
    title = 'test title'
    upload_date = '20140520'
    description = 'test description'
    uploader = 'test uploader'
    format = 'test format'

    info = {
        'webpage_url': web_page_url,
        'title': title,
        'upload_date': upload_date,
        'description': description,
        'uploader': uploader,
        'format': format,
    }

    filename = 'test_file'
    pp = XAttrMetadataPP()
    warnings, results = pp.run(info)

    assert(filename == results['filepath'])
    # FIXME: Check if all xattrs are set


# Generated at 2022-06-14 18:09:29.089913
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    ydl = FakeYDL()
    pp = XAttrMetadataPP(ydl)
    assert pp.get_youtube_dl_init() is ydl

# Generated at 2022-06-14 18:09:32.606476
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():

    from ..extractor import gen_extractors
    gen_extractors()

    postprocessor = XAttrMetadataPP(None, None)

    assert isinstance(postprocessor, PostProcessor)
    assert hasattr(postprocessor, 'run')

# Generated at 2022-06-14 18:09:33.518596
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO: implement test
    pass

# Generated at 2022-06-14 18:09:34.099407
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

# Generated at 2022-06-14 18:09:34.804789
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
	pass

# Generated at 2022-06-14 18:09:35.432112
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:09:50.251409
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import sys
    import mock
    from ..utils import FakeYDL
    xattrs_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }
    xattrname = 'user.dublincore.format'
    infoname = 'format'

# Generated at 2022-06-14 18:09:51.380751
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pp = XAttrMetadataPP()

if __name__ == '__main__':
    test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:10:00.306084
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import xattr
    import tempfile
    class FakeInfo(object):
        def __init__(self):
            self.filename = 'some_filename'
            self.title = 'some title'
            self.description = 'some description'
            self.format = 'some format'
            self.uploader_id = 'some uploader_id'
            self.uploader = 'some uploader'
            self.webpage_url = 'some webpage_url'
            self.upload_date = 'some upload date'
            self.ext = 'avi'
        def get(self, name):
            return getattr(self, name, None)

    info = FakeInfo()
    filename = os.path.join(tempfile.gettempdir(), 'ytdl_' + info.filename, info.ext)
    print

# Generated at 2022-06-14 18:10:00.910545
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:10:03.426016
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:10:16.394095
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..compat import compat_etree_ElementTree
    from ..downloader.common import FileDownloader
    from ..utils import encodeFilename, encodeArgument

    kwargs = {
        'format': 'webm',
        'title': 'test',
        'description': 'test_desc',
    }

    downloader = FileDownloader({
        'format': 'bestaudio/best',
        'verbose': True,
        'outtmpl': encodeFilename(encodeArgument('%(id)s.%(ext)s')),
        'nooverwrites': True,
        'nocheckcertificate': True,
        'simulate': True,
    })


# Generated at 2022-06-14 18:10:18.104299
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    x = XAttrMetadataPP()
    assert x is not None

# Generated at 2022-06-14 18:10:23.554257
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Tests that calling the constructor of XAttrMetadataPP only invokes super()
    pp = XAttrMetadataPP(None)
    assert pp.run({'filepath': '/tmp/foo.txt', 'title': 'bar'}) == ([], {'filepath': '/tmp/foo.txt', 'title': 'bar'})

# Generated at 2022-06-14 18:10:28.614393
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    #
    #TODO: test XAttrMetadataPP
    #
    assert True == True

test_XAttrMetadataPP_run()  # Run the test

# Helper Functions

#
#TODO: add more helper functions for extended attributes
#

# Generated at 2022-06-14 18:10:37.499599
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os, sys
    if compat_os_name == 'nt':
        import ctypes
        ctypes.windll.kernel32.SetConsoleCP(65001)
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

    from ..utils import get_xattr_file_size_limit, get_xattr_file_count_limit
    from .xattrpp import xattr_write, xattr_read

    filename = 'test.mp4'
    extattr_value = 'This is a test for extended attribute'

    pp = XAttrMetadataPP(None)


# Generated at 2022-06-14 18:10:50.218582
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_metadata_pp = XAttrMetadataPP()


# Generated at 2022-06-14 18:10:52.845605
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    fake_downloader = object()
    postprocessor = XAttrMetadataPP(fake_downloader)

    assert(postprocessor._downloader == fake_downloader)

# Generated at 2022-06-14 18:11:05.843733
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    xattrpp = XAttrMetadataPP()

    xattrpp.run({'filepath': 'test', 'webpage_url': 'webpage_url', 'format': 'format', 'upload_date': 'upload_date'})

    def run_fail(info):
        try:
            xattrpp.run(info)
        except XAttrMetadataError as e:
            return e.reason

    # no filepath
    assert run_fail({'upload_date': 'upload_date'}) == 'NO_FILE'
    # no xattr support
    assert run_fail({'filepath': 'test', 'webpage_url': 'webpage_url', 'format': 'format', 'upload_date': 'upload_date'}) == 'NO_XATTR_SUPPORT'



# Generated at 2022-06-14 18:11:15.170551
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    test_data = {
        'webpage_url': 'http://example.com/video.html',
        'description': 'A video about something',
        'title': 'The title',
        'upload_date': '20121115',
        'uploader': 'someone',
        'format': 'webm'
    }

    pp = XAttrMetadataPP(None)
    # Wrap postprocessor around our test data
    pp.run(test_data)
    # Test if the output is correct

# Generated at 2022-06-14 18:11:25.209310
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..extractor.common import InfoExtractor
    filename = 'test.mp4'
    info = {
        'webpage_url': u'https://www.youtube.com',
        'title': u'My Title',
        'description': u'My description',
        'upload_date': u'2014-04',
        'uploader': u'My Uploader',
        'format': u'17 - 3gp small',
        'filepath': filename,
    }

    # Mock xattr module for the duration of the test
    import sys
    sys.modules['xattr'] = lambda: None
    sys.modules['xattr'].setxattr = lambda path, xattrname, value: None

    pp = XAttrMetadataPP(InfoExtractor())
    pp.run(info)

    import xattr
    assert x

# Generated at 2022-06-14 18:11:26.381171
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO
    pass


# Generated at 2022-06-14 18:11:30.961089
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .test_utils import FakeYDL
    from .video_type_test import test_video_type_file
    x = test_video_type_file()

    ydl = FakeYDL()
    ydl.add_post_processor(XAttrMetadataPP(ydl))
    d = ydl.process_ie_result(x, download=True)
    assert d[0]['xattrs']

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:11:36.366094
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import mock
    import sys

    # TODO: get_test_data_file_path(path)
    import os

    if os.path.exists('/tmp/myfile'):
        os.remove('/tmp/myfile')
    f = open('/tmp/myfile', 'a')
    f.write('test')
    f.close()

    class InfoDict(dict):
        def __init__(self, *args, **kwargs):
            dict.__init__(self, *args, **kwargs)
            self['filepath'] = '/tmp/myfile'

    class FakeYDL(object):
        @staticmethod
        def to_screen(msg):
            print('[XAttrMetadataPP] ' + msg)

    # Test 1: Test with xattr support, no extended attributes
   

# Generated at 2022-06-14 18:11:48.223937
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    class FakeInfo:
        filename = 'Nothing to see here'
        duration = 210.0
        format = 'mp4'
        filesize = 87380
        width = 1920
        height = 1080
        webpag_url = 'test_url'
        title = 'Test Title'
        upload_date = '20160501'
        description = 'Test description'
        uploader = 'Test uploader'
        fps = 30

    def assert_xattr(fd, xattrname, value):
        from ..utils import get_xattr
        assert get_xattr(fd, xattrname) == value

    # Create test file and check that all xattrs are set properly
    with tempfile.TemporaryFile() as fd:
        pp = XAttrMetadataPP()

# Generated at 2022-06-14 18:11:56.841171
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    #
    # Test XAttrMetadataPP method run with a file system supporting XAttr feature
    #

    # Precondition: filesystem supporting XAttr feature
    if compat_os_name != 'nt':
        import os
        import xattr

        # TODO: Read file system and check if it supports XAttr feature
        filepath = '.'
        res = xattr.xattr(filepath)

    from .test_common_xattr_metadata import test_XAttrMetadataPP_run
    test_XAttrMetadataPP_run(XAttrMetadataPP)


# Generated at 2022-06-14 18:12:28.641409
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader import get_suitable_downloader
    from ..extractor import gen_extractors
    from .common import FileDownloader
    from .get_filename import GetFileNamePP
    from .metadata_from_title import MetadataFromTitlePP
    from .embedthumbnail import EmbedThumbnailPP
    from .ffmpegmetadata import FFmpegMetadataPP
    from ..utils import xattr_available

    if xattr_available():
        def test(filename, expected_xattrs):
            dl = get_suitable_downloader(
                {'format': 'worst', 'noplaylist': True, 'quiet': True},
                [],
                gen_extractors(),
                {},
                FileDownloader,
            )

            dl.add_post_processor(XAttrMetadataPP())


# Generated at 2022-06-14 18:12:29.312332
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:12:37.442060
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import unittest
    import tempfile
    from .common import FileDownloader
    from ..utils import xattr_supported

    try:
        from ..compat import compat_xattr
    except ImportError:
        if compat_os_name == 'nt':
            raise unittest.SkipTest('extended attributes are not available on Windows')
        else:
            raise unittest.SkipTest('pyxattr module is not available')

    # Note: The unit test uses a dummy downloader to avoid calling sys.exit()
    class DummyLogger(object):
        errors = []
        warnings = []
        def debug(self, msg):
            pass
        def warning(self, msg):
            self.warnings.append(msg)
        def error(self, msg):
            self.errors.append(msg)


# Generated at 2022-06-14 18:12:38.480566
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


# Generated at 2022-06-14 18:12:41.576472
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Test the XAttrMetadataPP class constructor.
    """

    ydl = None
    pp = XAttrMetadataPP(ydl)

    assert isinstance(pp, XAttrMetadataPP)
    assert pp.ydl == ydl

# Generated at 2022-06-14 18:12:51.262652
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import xattr


# Generated at 2022-06-14 18:13:03.141041
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import io

    # Create some io.BytesIO objects
    info = {
        'webpage_url': 'http://example.com/webpage_url',
        'upload_date': '2001-02-03',
        'title': 'title',
        'description': 'description',
        'uploader': 'uploader',
        'format': 'format',
    }
    byte_io = io.BytesIO()

    pp = XAttrMetadataPP(None)
    pp._downloader = DummyYDL()
    pp._downloader.to_screen = lambda s: s

    # Create the test file
    fd = open('test.txt', 'wb')

# Generated at 2022-06-14 18:13:14.880452
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import PostProcessorTest
    from .test_extractors import MockYoutubeIE

    class XAttrMetadataPPTest(PostProcessorTest):

        def create_post_processor(self):
            return XAttrMetadataPP()

        def test_no_xattr(self):
            # (tested with '--xattr-write-filesystem rootfs')
            try:
                write_xattr('/dev/null', 'user.dublincore.contributor', b'foo')
            except XAttrUnavailableError:
                return True
            else:
                self.fail('Expected XAttrUnavailableError')


# Generated at 2022-06-14 18:13:23.101380
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # xattr_mapping test
    pp = XAttrMetadataPP()
    xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        # 'user.xdg.comment':            'description',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }
    assert pp.xattr_mapping == xattr_mapping

# Generated at 2022-06-14 18:13:25.490064
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert isinstance(pp, XAttrMetadataPP)
    assert isinstance(pp, PostProcessor)

# Generated at 2022-06-14 18:14:14.043418
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    # Mock youtube_dl
    class MockInfo:
        def get(self, key, default=None):
            return {
                'webpage_url': 'https://www.youtube.com/watch?v=1234567890',
                'title': 'mock title',
                'upload_date': '20170131',
                'description': 'mock description',
                'uploader': 'mock uploader',
                'format': 'mock format',
            }.get(key, default)

    class MockYoutubeDL:
        def to_screen(self, msg):
            assert msg == '[metadata] Writing metadata to file\'s xattrs'


# Generated at 2022-06-14 18:14:16.068473
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xmp = XAttrMetadataPP()
    assert xmp

if __name__ == "__main__":
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:14:21.527169
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .common import FileDownloader
    from .http import HttpFD

    class FakeInfo:
        pass

    ydl = FileDownloader(HttpFD())
    ydl.params = {'writethumbnail': True}
    pp = XAttrMetadataPP(ydl)

    info = FakeInfo()
    info.title = 'video title'
    info.upload_date = '20110101'
    info.description = 'video description'
    info.uploader = 'uploader'
    info.format = 'format'
    info.thumbnail = 'http://thumbnail/url'
    info.webpage_url = 'http://webpage/url'
    info.duration = 600.0
    info.tags = ['tag1', 'tag2']
    info.categories = ['cat1', 'cat2']
   

# Generated at 2022-06-14 18:14:30.931751
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import io
    import os
    import tempfile

    # xattr writing functionality is not supported on Windows
    if os.name == 'nt':
        return


# Generated at 2022-06-14 18:14:34.039626
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    return None
    # TODO Implement unit test for method run of class XAttrMetadataPP
    #      Raise an exception if the test fails
    raise NotImplementedError()

# Generated at 2022-06-14 18:14:44.611537
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    filename = 'name.mp4'
    metadata = {
        'title': 'Test video title',
        'description': 'Test video description',
        'webpage_url': 'http://example.com',
        'uploader': 'Example uploader',
        'upload_date': '20110101',
    }

    xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        'user.dublincore.title': 'title',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.date': 'upload_date',
    }

    xattr_values = {}

# Generated at 2022-06-14 18:14:47.344886
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:14:57.902107
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    class Info:
        # Notice: the attributes must match the dictionary keys below
        #         to ensure that the method 'run' works correctly
        def get(self, name):
            return info_simulation_dict.get(name)

    ppro = XAttrMetadataPP()

    info_simulation_dict = {
        'webpage_url': 'webpage_url_value',
        'description': 'description_value',
        'title': 'title_value',
        'upload_date': 'upload_date_value',
        'uploader': 'uploader_value',
        'format': 'format_value',
    }
    info = Info()

    # Extend attributes are currently disabled
    XAttrMetadataPP.write_xattr = lambda filename, xattrname, byte_value: False

# Generated at 2022-06-14 18:15:07.746534
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import unittest
    import sys
    from .common import DummyYDL
    from ..utils import XAttrMetadataError

    class DummyFile(object):
        """Dummy file with no xattr support"""
        def __init__(self, filenames=None, filenames_with_no_space_left=None, filenames_with_value_too_long=None):
            self.filenames = filenames if filenames else []
            self.filenames_with_no_space_left = filenames_with_no_space_left if filenames_with_no_space_left else []
            self.filenames_with_value_too_long = filenames_with_value_too_long if filenames_with_value_too_long else []


# Generated at 2022-06-14 18:15:19.175047
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FFmpegPostProcessor, PostProcessor
    from ..compat import compat_os_name
    from ..utils import XAttrMetadataError, XAttrUnavailableError
    from ..extractor.youtube import YoutubeIE
    import tempfile
    import subprocess
    import os
    import pytest
    import shutil

    class DummyYoutubeIE(YoutubeIE):
        def _real_initialize(self):
            pass

    # Create temporary directory
    temp_dir_fd, temp_dir_path = tempfile.mkstemp(prefix='youtube-dl-test-xattr-metadata-')
    os.close(temp_dir_fd)
    os.mkdir(temp_dir_path)

    # Create temporary file
    temp_file_fd, temp_file_path = tempfile.mkstemp

# Generated at 2022-06-14 18:16:57.183377
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import PostProcessorTest

    class DummyYDL(object):
        def __init__(self):
            self.params = {}

        def to_screen(self, text):
            pass

        def report_error(self, text):
            self.error_text = text

        def report_warning(self, text):
            self.warning_text = text

    class DummyFile(object):
        def __init__(self, filename):
            self.filename = filename


# Generated at 2022-06-14 18:16:58.827001
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # TODO: write a test for this class
    assert False

# Generated at 2022-06-14 18:17:00.264441
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(None, None, None)

# Generated at 2022-06-14 18:17:10.640977
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Postprocessor should run only when xattr support is found
    from .common import FileDownloader
    from  ..utils import has_xattr
    try:
        # Test with xattr available
        assert has_xattr()
        fd = FileDownloader({})  # errors here
        pp = XAttrMetadataPP(fd)
        assert pp.run({})[0] == []
    except XAttrUnavailableError:
        # Test with xattr unavailable
        assert not has_xattr()
        fd = FileDownloader({})  # errors here
        pp = XAttrMetadataPP(fd)
        assert pp.run({})[0] == []

# Generated at 2022-06-14 18:17:12.999501
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Unit test for constructor of class XAttrMetadataPP
    """
    # TODO
    return


# Generated at 2022-06-14 18:17:24.292663
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..extractor import gen_extractors
    from ..utils import *
    from .common import PostProcessor

    # Initialize stuff that might be used by PostProcessor methods
    info = {
        'id': 'A_VIDEO_ID',
        'ext': 'mp4',
        'title': 'A video title',
        'upload_date': '20161011',
        'uploader': 'An uploader',
        'webpage_url': 'https://www.youtube.com/watch?v=A_VIDEO_ID',
        'description': 'A description',
        'format': '5 - 480x360 (H.264)'
    }

    extractors = gen_extractors()
    pp = XAttrMetadataPP(None, None, {}, extractors)


# Generated at 2022-06-14 18:17:36.691501
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pp = XAttrMetadataPP()

# Generated at 2022-06-14 18:17:42.558565
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor.common import InfoExtractor
    from ..utils import ExtractorError
    from .common import FileDownloader
    from .xattr import get_xattr_mapping
    import os
    import tempfile


# Generated at 2022-06-14 18:17:45.057189
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    metadata_pp = XAttrMetadataPP(None)
    assert metadata_pp

if __name__ == "__main__":
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:17:53.878736
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    xattrpp = XAttrMetadataPP()

    # Test NO_SPACE (NO_SPACE is raised by xattr)
    info = {
        'title': 'foo',
        'filepath': '/path/to'
    }
    xattrpp.run(info)

    # Test VALUE_TOO_LONG (VALUE_TOO_LONG is raised by xattr)
    info = {
        'title': 'foo' * 2**16,
        'filepath': '/path/to'
    }
    xattrpp.run(info)

    # Test NO_SUPPORT (NO_SUPPORT is raised by xattr)
    info = {
        'title': 'foo',
        'filepath': '/path/to'
    }
    xattrpp.run(info)