

# Generated at 2022-06-14 18:09:13.626836
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import tempfile

    from ..compat import compat_os_name, compat_path

    # Test the case where extended attributes are supported
    if compat_os_name == 'nt':
        # NTFS supports extended attributes (user.NAME)
        filepath = os.path.join(tempfile.gettempdir(), 'xattr')
        try:
            os.remove(filepath)
        except OSError:
            pass

        info = {
            'title': 'title',
            'webpage_url': 'webpage_url',
            'description': 'description',
            'uploader': 'uploader',
            'upload_date': 'upload_date',
            'format': 'format',
            'filepath': filepath,
        }


# Generated at 2022-06-14 18:09:18.590798
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    filename = 'tests/files/xattr_metadata.txt'
    import tempfile
    with tempfile.NamedTemporaryFile() as tf:
        from ..downloader import Downloader
        dl = Downloader(None)
        pp = XAttrMetadataPP(dl, {})
        # pp._downloader.fd.write(open(filename, 'rb').read())
        # pp._downloader.fd.flush()
        pp.run({'filepath': filename})

# Generated at 2022-06-14 18:09:28.028655
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    assert XAttrMetadataPP.run({}) == ([], {})
    assert XAttrMetadataPP.run({
        'format': 'best',
        'title': 'xattr test',
        'webpage_url': 'http://example.com',
        'upload_date': '20010101',  # date uses dashes
        'description': 'xattr test description',
        'uploader': 'xattr test uploader',
    }) == ([], {
        'format': 'best',
        'title': 'xattr test',
        'webpage_url': 'http://example.com',
        'upload_date': '20010101',
        'description': 'xattr test description',
        'uploader': 'xattr test uploader',
    })

# Generated at 2022-06-14 18:09:32.992896
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():

    def download(params):
        pass

    pp = XAttrMetadataPP({}, download)

    assert pp.run({}) == ([], {})

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:09:34.042956
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO: Implement this unit test
    pass

# Generated at 2022-06-14 18:09:35.284537
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert (XAttrMetadataPP({}, {}, {}, {}))


# Generated at 2022-06-14 18:09:44.730060
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """Here we test method run of class XAttrMetadataPP
    """
    class Info(dict):
        def __getattr__(self, name):
            return self[name]

        def __setattr__(self, name, value):
            self[name] = value
    pp = XAttrMetadataPP()
    #Now this should fail, as we cannot write to a non-existing file.
    info = Info()
    info.filepath = "/this/file/does/not/exist"
    # TODO: here, catch the exception...
    pp.run(info)

if __name__ == '__main__':
    test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:09:52.504949
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ Tests constructor of XAttrMetadataPP. """

# Generated at 2022-06-14 18:10:01.619744
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor.common import InfoExtractor

    class FakeInfoExtractor(InfoExtractor):

        def _real_extract(self, url):
            return {
                'id': 'testid',
                'ext': 'mp3',
                'title': 'test title',
                'description': 'test description',
                'upload_date': '20131224',
                'uploader': 'nobody',
                'webpage_url': 'http://example.com/index.html',
                'format': 'bestaudio/best',
            }

    class FakeDownloader(object):

        def __init__(self):
            self.params = {
                'writedescription': True,
                'writeinfojson': True,
            }

        def to_screen(self, msg):
            print(msg)


# Generated at 2022-06-14 18:10:03.282780
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    x = XAttrMetadataPP(None)
    assert x is not None

# Generated at 2022-06-14 18:10:10.340964
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """Constructor tests for class XAttrMetadataPP."""
    xattr = XAttrMetadataPP(downloader=None)
    # print xattr.get_supported_protocols()

# Generated at 2022-06-14 18:10:10.941305
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert True

# Generated at 2022-06-14 18:10:12.878853
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP('youtube-dl')
    assert pp.name == 'xattrs'

# Generated at 2022-06-14 18:10:16.647023
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Test that default constructor of class XAttrMetadataPP works
    return XAttrMetadataPP(None)


if __name__ == "__main__":
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:10:18.345340
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert pp is not None

# Generated at 2022-06-14 18:10:24.811482
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import sys
    from .common import PostProcessorTest
    from ..utils import (
        encodeArgument,
        get_filesystem_encoding,
    )

    class Args(object):
        metadata_commands = None
        nocheckcertificate = False
        no_color = False
        simulator = False
        verbose = True
        dump_intermediate_pages = False

    class YDL(object):
        params = Args()
        verbose = 2
        to_screen = sys.stdout.write

    ydl = YDL()

    class Downloader(object):
        def __init__(self, ydl):
            self.ydl = ydl

        def to_screen(self, message):
            # Forwards to ydl.
            self.ydl.to_screen(message)


# Generated at 2022-06-14 18:10:30.036666
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Test empty constructor
    x = XAttrMetadataPP()

    # Test constructor with parameters
    obj = 'fake'
    downloader = 'fake'
    x2 = XAttrMetadataPP(obj, downloader)
    assert x2 == obj
    assert x2._downloader == downloader



# Generated at 2022-06-14 18:10:33.500828
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert isinstance(pp, PostProcessor)

if __name__ == '__main__':
    # Unit test for constructor of class XAttrMetadataPP
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:10:34.709557
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ """
    pp = XAttrMetadataPP()
    assert pp is not None

# Generated at 2022-06-14 18:10:47.065942
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Imports required for testing
    import os
    import tempfile
    # Initialising variables
    xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        'user.xdg.comment': 'description',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }

    # Create temporary file
    temp_file_name = tempfile.mkstemp()[1]

# Generated at 2022-06-14 18:10:58.153037
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:11:09.251151
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import PostProcessorTest

    class MockXAttrMetadataPP(PostProcessor, XAttrMetadataPP):
        pass

    config = {'format': 'best', 'outtmpl': os.path.join(os.curdir, '%(id)s.%(ext)s')}
    test = PostProcessorTest(MockXAttrMetadataPP, config=config)

    # test right invocation
    info = {
        'id': 'abcdef',
        'ext': 'mp4',
        'title': 'Title',
        'webpage_url': 'http://www.website.com/video/1234/'
    }
    retval = test.run_pp(info=info)
    assert not retval

    # test wrong invocation

# Generated at 2022-06-14 18:11:10.991837
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    _postprocessor = XAttrMetadataPP()
    pass


# Generated at 2022-06-14 18:11:13.768006
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    if compat_os_name == 'nt':
        # xattr is only available on NTFS
        pass

# Generated at 2022-06-14 18:11:24.787223
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from .common import FileDownloader
    from ..utils import encodeFilename

    # Test values
    test_fname = '/path/to/test/file.ext'
    test_info = {
        'webpage_url':  'http://www.youtube.com/watch?v=BaW_jenozKc',
        'format':       'best',
        'ext':          'mp4',
        'upload_date':  None,
        'uploader':     'testuser',
        'title':        'testtitle',
        'description':  'testdescription',
    }

    # Test initialization of class
    xattr_pp = XAttrMetadataPP(FileDownloader({}))

    # Test run of class
    results, info = xattr_pp.run(test_info)

    # Test results

# Generated at 2022-06-14 18:11:28.402804
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    #
    # TODO: Check whether xattr library is available.
    #       Also check whether xattr is available (and writable) for '/' directory.
    #
    assert pp is not None

# Generated at 2022-06-14 18:11:34.840354
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile

    class FakeYDL():
        def __init__(self):
            self.to_screen_calls = []
            self.report_warning_calls = []
            self.report_error_calls = []
            self.params = {'outtmpl': 'FILE%(autonumber)s.%(ext)s','writedescription': True, 'writethumbnail': True,}

        def to_screen(self, msg):
            self.to_screen_calls.append(msg)

        def report_warning(self, msg):
            self.report_warning_calls.append(msg)

        def report_error(self, msg):
            self.report_error_calls.append(msg)


# Generated at 2022-06-14 18:11:36.323752
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    x = XAttrMetadataPP(None)
    assert(x is not None)

# Generated at 2022-06-14 18:11:41.704361
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .common import FileDownloader
    from .xattr import XAttrMetadataPP
    xattr_metadata = XAttrMetadataPP(FileDownloader({}))
    assert xattr_metadata is not None, 'Problem when creating XAttrMetadataPP instance'

# Generated at 2022-06-14 18:11:45.551684
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .common import PostProcessorTestCase
    test = PostProcessorTestCase.TestPostProcessor(XAttrMetadataPP)
    test.run()



# Generated at 2022-06-14 18:12:15.653360
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import unittest
    import tempfile
    import os
    import xattr

    class XAttrMetadataPPDownloader(object):
        def __init__(self, xattrs_support_enabled=True):
            self.xattrs_support_enabled = xattrs_support_enabled

        def to_screen(self, message):
            print(message)

        def report_warning(self, message):
            print(message)

        def report_error(self, message):
            print(message)

        def xattrs_supported(self):
            return self.xattrs_support_enabled

    class XAttrMetadataPPTest(unittest.TestCase):
        def setUp(self):
            self.downloader = XAttrMetadataPPDownloader()
            self.filename = tempfile.N

# Generated at 2022-06-14 18:12:21.201293
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .test import PostProcessorTestCase
    from ..compat import compat_str
    postProcessor = XAttrMetadataPP(PostProcessorTestCase.downloader, None, None)
    PostProcessorTestCase.checkProcessor(postProcessor)
    postProcessor.run({'filepath': compat_str('foobar'), 'title': compat_str('title'), 'format': compat_str('format')})

# Generated at 2022-06-14 18:12:30.616084
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():

    xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        'user.xdg.comment':      'description',
        'user.dublincore.title': 'title',
        'user.dublincore.date':  'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }

    assert XAttrMetadataPP._xattr_mapping == xattr_mapping

# Generated at 2022-06-14 18:12:31.524938
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP()

# Generated at 2022-06-14 18:12:41.059846
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .testcases import TestCase
    from ..utils import xattr_supported

    test = TestCase(XAttrMetadataPP)
    if not xattr_supported():
        test.accept('[warn] Unable to write extended attributes')
        return
    test.accept('[metadata] Writing metadata to file\'s xattrs')
    test.accept('[metadata] Writing metadata to file\'s xattrs')

# Generated at 2022-06-14 18:12:51.057992
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import gen_extractors
    from ..utils import sanitize_open

    for ie in gen_extractors():
        ie_result = ie.extract('http://www.youtube.com/watch?v=BaW_jenozKc')

        # Test that we're able to get a valid result
        assert(ie_result is not None and len(ie_result['formats']) > 0)

        filepath = u'fakefilename'

        # Create a XAttrMetadataPP object
        pp = XAttrMetadataPP(ie.ydl, {})

        # Fake a file for testing
        with sanitize_open(filepath, 'wb') as f:
            f.write(b'')

        # Test by setting a fake key in the info dict

# Generated at 2022-06-14 18:12:51.859873
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:13:03.245055
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import copy
    import datetime
    test_info = {
        'upload_date': datetime.date(1970, 1, 1),
        'webpage_url': 'test_webpage',
        'description': 'test_description',
        'title': 'test_title',
        'uploader': 'test_uploader',
        'duration': 5.0,
        'format': 'test_format',
    }
    pp = XAttrMetadataPP(None)
    pp.run(test_info)
    expected_result = copy.deepcopy(test_info)
    expected_result['upload_date'] = '1970-01-01'
    assert expected_result == test_info

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:13:04.410374
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP()

# Generated at 2022-06-14 18:13:15.856506
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from tempfile import mkstemp
    from unittest import TestCase, SkipTest
    from .common import test_pp_common_run

    # This test requires xattr package, which doesn't work on Windows
    if compat_os_name == 'nt':
        raise SkipTest('Extended attributes are not available on Windows')

    try:
        from xattr import xattr
    except ImportError:
        raise SkipTest('Extended attributes are not available (xattr is not installed)')

    class TestXAttrMetadataPP(TestCase, object):
        def setUp(self):
            fd, self._filename = mkstemp(prefix='ylc-', suffix='.mp4')
            os.close(fd)


# Generated at 2022-06-14 18:13:58.302206
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP('/tmp/f', {})
    assert pp.xattr_filename == '/tmp/f'
    assert pp.info == {}

# Generated at 2022-06-14 18:14:06.968772
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    test_values = {
        "title": "This is the title",
        "upload_date": "20150218",
        "description": "This is the description",
        "uploader": "This is the uploader",
        "format": "This is the format",
    }

    from .common import FileDownloader
    from .console import ConsolePostProcessor, FileDownloader

    pp = XAttrMetadataPP(FileDownloader())
    assert pp.run(test_values) == ([], test_values)

# Generated at 2022-06-14 18:14:12.163675
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    try:
        import xattr
    except ImportError:
        pytest.skip('Could not import xattr (Python 3), skipping test.')
    if not getattr(xattr, '__version__', None) or xattr.__version__ < '0.6.4':
        pytest.skip('xattr package version is too old, skipping test.')
    pytest.raises(XAttrUnavailableError, lambda: XAttrMetadataPP())

# Generated at 2022-06-14 18:14:14.341436
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP('/test/', 'A test video', '1234')
    assert isinstance(pp, XAttrMetadataPP)

# Generated at 2022-06-14 18:14:18.914203
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """Builds a dummy PostProcessor and run the test."""
    from ..YDL import YDL
    ydl_opts = {
        'writedescription': True,
        'writeinfojson': True,
    }
    ydl = YDL(ydl_opts)
    pp = XAttrMetadataPP(ydl)
    pp.run({'filepath': 'test'})  # should raise exception


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:14:22.149396
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(None, {}).__class__ == XAttrMetadataPP

# Generated at 2022-06-14 18:14:24.803001
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert issubclass(XAttrMetadataPP, PostProcessor)
    assert XAttrMetadataPP.run.__module__ == __name__

# Generated at 2022-06-14 18:14:30.197930
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .test import PostProcessorTest
    pp = XAttrMetadataPP()
    PostProcessorTest(pp, ['http://www.youtube.com/watch?v=BaW_jenozKc'], {'writeinfojson': True, 'writethumbnail': True}).run()

# Generated at 2022-06-14 18:14:31.928641
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    x = XAttrMetadataPP()
    assert isinstance(x, XAttrMetadataPP)

# Generated at 2022-06-14 18:14:43.934323
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """Test XAttrMetadataPP object construction"""

    # youtubeie requires an 'ydl' object to be defined
    class YDLDummy(object):
        params = {'quiet': True}
        def to_stderr(self, message):
            pass
        def to_screen(self, message):
            pass
        def report_warning(self, message):
            pass
        def report_error(self, message):
            pass

    ydl = YDLDummy()

    # create a arbitrary dictionary for test purpose
    #   title, upload_date and format  will be used in the test

# Generated at 2022-06-14 18:16:01.421197
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    return 0

# Generated at 2022-06-14 18:16:10.236951
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import TestPostProcessor
    from .metadatafromtitle import MetadataFromTitlePP
    from ..downloader.common import FileDownloader
    from ..extractor import YoutubeIE
    import os

    # Create a fake downloader object
    downloader = FileDownloader(
        YoutubeIE(),
        None,
        '',
        {}
    )
    downloader.params = { 'outtmpl': os.path.join('%(download_dir)s', '%(title)s.%(ext)s') }
    downloader.report_warning = lambda msg: print(msg)
    downloader.report_error = lambda msg: print(msg)
    downloader.to_screen = lambda msg: print(msg)

    # Create a fake info dict

# Generated at 2022-06-14 18:16:14.617140
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ Function test_XAttrMetadataPP to test XAttrMetadataPP constructor
    """
    try:
        XAttrMetadataPP(None)
        return True
    except:
        return False

# Generated at 2022-06-14 18:16:15.839723
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # This method is not directly testable.
    pass

# Generated at 2022-06-14 18:16:19.312943
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Unit test for constructor of class XAttrMetadataPP.
    Call constructor of class XAttrMetadataPP with a valid value and test if it runs without error.
    """
    postprocessor = XAttrMetadataPP(None)
    assert postprocessor is not None

# More unit tests

# Generated at 2022-06-14 18:16:29.680116
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import get_info_extractor
    from .pprint import pprint_json

    ie = get_info_extractor('YoutubePlaylistIE', 'youtube:playlist')

    pl_id = 'PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'
    pl_url = 'https://www.youtube.com/playlist?list=%s' % pl_id
    pl_info = ie._real_extract(pl_url)

    video_id = 'm0LMQioEx94'
    video_url = 'https://www.youtube.com/watch?v=%s&list=%s' % (video_id, pl_id)
    video_info = ie._real_extract(video_url)


# Generated at 2022-06-14 18:16:40.689102
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile

    # Create a temp file
    temp_path = tempfile.mkstemp()
    temp_fd = temp_path[0]
    temp_filename = temp_path[1]

    # Create a class instance
    ydl = FakeYDL()
    pp = XAttrMetadataPP(ydl)

    # Create info dictionary
    info = {
        'filepath': temp_filename,
        'description': 'Description',
        'title': 'Title',
        'resolution': '360p',
        'upload_date': '20080701',
        'uploader': 'Uploader',
    }

    # Run method
    status = pp._run(info)

    # Assert method returns no error and dictionary is untouched
    assert os.path.exists(temp_filename)
    assert status

# Generated at 2022-06-14 18:16:51.041588
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # initialization
    import os
    import tempfile
    import shutil
    import json
    import xattr
    import glob
    import hashlib

    temp_dir = tempfile.mkdtemp()
    filename = 'testfile.mp4'
    filepath = os.path.join(temp_dir, filename)
    filecontent = b'\x00\x00'
    with open(filepath, 'wb') as f:
        f.write(filecontent)


# Generated at 2022-06-14 18:17:02.217052
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import tempfile

    # Extracted metadata on test video
    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    info = {
        'webpage_url': url,
        'title': "YTP - It's a Trap",
        'description': 'youtube-dl test video\n\nThis is a test video for youtube-dl.\n\nvideoplayback',
        'uploader': 'Philipp Hagemeister',
        'upload_date': '20121002',
        'filepath': os.path.join(tempfile.gettempdir(), 'test_video.flv'),
        'format': '18 - 640x360 (medium)',
    }

    # Create test video file

# Generated at 2022-06-14 18:17:14.333414
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from ..downloader.common import FileDownloader
    from ..compat import compat_os_name

    # Create a fake downloader
    dl = FileDownloader({})

    # Create a fake info
    info = {
        'title': 'The video title',
        'format': 'best video format',
        'webpage_url': 'http://www.youtube.com/watch?v=XOXXOeTLGKs',
        'uploader': 'The uploader',
        'upload_date': '20130303',
        'description': 'The video description',
        'filepath': 'Dummy file path',
    }

    # Prepare to run the postprocessor
    pp = XAttrMetadataPP(dl, {})

    # Run the postprocessor