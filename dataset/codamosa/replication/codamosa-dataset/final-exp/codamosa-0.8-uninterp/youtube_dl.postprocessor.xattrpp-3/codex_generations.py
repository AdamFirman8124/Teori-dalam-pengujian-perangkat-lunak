

# Generated at 2022-06-14 18:09:09.971193
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    p = XAttrMetadataPP()
    assert p.run({}) == ([], {})
    assert p.run({'filepath': 'filename'}) == ([], {'filepath': 'filename'})

# Generated at 2022-06-14 18:09:12.818460
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    filename = "hdsg.mp4"
    info = {'filepath': filename}
    p = XAttrMetadataPP()
    assert p.run(info) == ([], info)


if __name__ == "__main__":
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:09:14.270305
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP().run({}) == ([], {})

# Generated at 2022-06-14 18:09:17.279496
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert pp

# Generated at 2022-06-14 18:09:18.069172
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:09:22.900882
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Unit test for constructor of class XAttrMetadataPP
    """
    from ..YoutubeDL import YoutubeDL
    postprocessor = XAttrMetadataPP(YoutubeDL())
    assert isinstance(postprocessor, XAttrMetadataPP)

# Generated at 2022-06-14 18:09:25.484767
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    def run(self, info):
        return [], info
    instance = XAttrMetadataPP()
    instance.run = run
    assert instance.run(instance, {}) == ([], {})

# Generated at 2022-06-14 18:09:27.314117
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert isinstance(XAttrMetadataPP('_downloader'), PostProcessor)

# Generated at 2022-06-14 18:09:37.455173
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import encodeFilename
    from .common import FileDownloader

    #
    # The way to test the 'write_xattr' method would be to either fake it
    # or to create a dummy file and give it permissions.
    # For now we test that the method is called with the right arguments.
    #

    class MockXAttrMetadataPP(XAttrMetadataPP):

        def __init__(self, downloader):
            super(MockXAttrMetadataPP, self).__init__(downloader)
            self.xattr_calls = []

        def write_xattr(self, filename, attribute, value):
            self.xattr_calls.append((filename, attribute, value))

    ydl_opts = {'format': 'bestvideo+bestaudio'}
    ydl = FileDownloader

# Generated at 2022-06-14 18:09:39.118054
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP('youtube-dl').run is not None

# Generated at 2022-06-14 18:09:53.397647
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import io
    import os
    import platform
    import shutil
    import tempfile
    import xattr

    # Skip this test if xattr is not available in this Python version
    if not hasattr(xattr, 'setxattr'):
        return

    filename = 'test_filename'
    content = b'test content'

    def xattr_assert(*args):
        raise AssertionError('xattr %s should not have been called' % (args,))

    # Save the original functions and replace them with a mockup one
    original_write_xattr = XAttrMetadataPP._write_xattrs
    original_is_writable = XAttrMetadataPP._is_writable
    XAttrMetadataPP._write_xattrs = xattr_assert
    XAttrMetadataPP._is_writ

# Generated at 2022-06-14 18:09:55.361039
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert pp is not None

# Generated at 2022-06-14 18:10:04.969565
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Unit test for constructor of class XAttrMetadataPP
    """
    #
    info = {
        'webpage_url': 'https://www.youtube.com/watch?v=PIh2xe4jnpk',
        'title': 'Big Buck Bunny Full Movie',
        'upload_date': '20081202',
        'description': 'Big Buck Bunny is a short animated film by the Blender Institute. '
                       + 'It has made use of open source software for its creation.',
        'uploader': 'Big Buck Bunny',
        'format': 'best'
    }
    #
    assert info['webpage_url'] == 'https://www.youtube.com/watch?v=PIh2xe4jnpk'
    assert info['title'] == 'Big Buck Bunny Full Movie'

# Generated at 2022-06-14 18:10:07.736384
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:10:17.917162
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        # 'user.xdg.comment':            'description',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }


# Generated at 2022-06-14 18:10:19.538890
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    # TODO:
    # * Implement this unit test!!
    assert 0 == 0

# Generated at 2022-06-14 18:10:27.906614
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Necessary imports
    import sys
    import os
    from tempfile import mkstemp
    from typing import List, Dict

    from pytube._compat import PY2, UnicodeMixin, xattr
    from pytube.exceptions import XAttrMetadataError
    from pytube.postprocessor import XAttrMetadataPP

    class DownloaderFake(UnicodeMixin):
        def report_error(self, msg):
            pass

        def report_warning(self, msg):
            pass

        def to_screen(self, msg):
            pass

    class FakeYDL(object):
        def __init__(self):
            self.params = {'outtmpl': '%(title)s-%(id)s.%(ext)s'}
            self.downloader = DownloaderFake()

   

# Generated at 2022-06-14 18:10:28.882016
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert isinstance(XAttrMetadataPP, object)

# Generated at 2022-06-14 18:10:29.471327
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:10:32.296551
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    x = XAttrMetadataPP(None)
    assert x

# Generated at 2022-06-14 18:10:42.323758
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass



# Generated at 2022-06-14 18:10:43.380564
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass


# Generated at 2022-06-14 18:10:54.726011
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .test_utils import FakeYDL
    from .extractor import YoutubeIE

    import os
    import tempfile

    ydl = FakeYDL()
    ydl.params['writedescription'] = True
    ydl.params['writeinfojson'] = True
    ydl.params['writeannotations'] = True
    ydl.params['writeautomaticsub'] = True
    ydl.params['writethumbnail'] = True
    ydl.params['writesubtitles'] = True
    ydl.params['write_xattrs'] = True


# Generated at 2022-06-14 18:10:57.711755
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    obj = XAttrMetadataPP()
    assert obj is not None

# Generated at 2022-06-14 18:11:07.929532
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    try:
        # Video info
        info = {}
        info['webpage_url'] = 'http://www.example.com/foo.html'
        info['title'] = 'Foo title'
        info['upload_date'] = '20131201'
        info['description'] = 'Foo description'
        info['uploader'] = 'Foo uploader'
        info['format'] = 'Foo format'
        info['filepath'] = '/path/to/foo.flv'

        # PostProcessor initialization
        pp = XAttrMetadataPP()

        # Call run method
        pp.run(info)

    except (XAttrMetadataError, XAttrUnavailableError):
        # xattr is not supported on the current filesystem
        pass

# Generated at 2022-06-14 18:11:14.250410
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert repr(pp) == '<XAttrMetadataPP>'

# The following tests assume that the external library 'xattr' is available.
# In py2exe distribution this is not the case.
# TODO: Implement fallbacks for these unit tests for py2exe distribution.
#       See for example https://stackoverflow.com/questions/8748507/python-unit-testing-that-a-method-throws-a-specific-exception


# Generated at 2022-06-14 18:11:25.187452
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from unittest import TestCase
    from ytdl_extractor.ytdl_extractor import YoutubeDL
    from ytdl_extractor.compat import compat_os_name


    youtube_dl = YoutubeDL()
    info = {
        'filepath': '/tmp/test.mp4',
        'webpage_url': 'https://www.youtube.com/watch?v=XvLnZn_4ZJ4',
        # 'description': 'My cool video',
        'title': 'My cool video',
        'upload_date': '20180222',
        'description': 'My cool video',
        'uploader': 'My cool uploader',
        'format': 'pseudo-format',
    }

    xattrMetadataPP = XAttrMetadataPP(youtube_dl.params)
   

# Generated at 2022-06-14 18:11:26.381487
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(None)

# Generated at 2022-06-14 18:11:31.784661
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    info = {
        'title' : 'the title',
        'uploader' : 'the uploader',
        'webpage_url' : 'the webpage url',
        'upload_date' : 'the upload date',
        'description' : 'the description',
        'format' : 'the format',
        'filepath' : 'the filepath'
    }
    PP = XAttrMetadataPP(None)
    assert PP.run(info) == ([], info)

# Generated at 2022-06-14 18:11:42.599891
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from ..YoutubeDL import YoutubeDL
    from ..extractor.common import InfoExtractor

    class DummyIE(InfoExtractor):

        def _real_extract(self, url):
            return {
                'id': '1234',
                'title': 'Dummy video title',
                'description': 'Video description',
                'upload_date': '20121002',
                'uploader': 'John Smith',
                'url': 'http://example.com/watch?v=1234',
                'webpage_url': 'http://example.com/watch?v=1234',
                'ext': 'mp4',
                'format': 'MP4',
                'format_id': 'MP4',
                'duration': 10,
                'width': 100,
                'height': 100,
            }


# Generated at 2022-06-14 18:12:14.175315
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    #
    # Test XAttrMetadataPP.run(...)
    #

    from ..extractor.common import InfoExtractor
    from ..downloader.cache import FileCache
    from ..downloader.http import HttpFD
    from ..utils import get_free_space
    from ..compat import compat_xattr_get
    from ..compat import XAttrMetadataError
    from ..compat import compat_os_name

    global xattr_available

    xattr_available = False

    def test_write_xattr(filename, attrname, attrvalue):
        global xattr_available
        xattr_available = True
        return True

    def test_free_space(path):
        import sys
        free_space = int(sys.argv[1])
        return free_space

    #
    #

# Generated at 2022-06-14 18:12:25.824070
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    '''
    Run unit tests for the XAttrMetadataPP constructor.

    Returns:
     0 if unit tests pass
     1 if unit tests fail
    '''
    import unittest
    import sys
    import os
    import errno
    import tempfile

    class XAttrMetadataPPTests(unittest.TestCase):
        def setUp(self):
            self.test_dir = tempfile.mkdtemp()

        def tearDown(self):
            os.rmdir(self.test_dir)

        def test_XAttrUnavailableError_catch(self):
            from ..postprocessor import XAttrMetadataPP
            # pylint: disable=protected-access
            pp = XAttrMetadataPP()


# Generated at 2022-06-14 18:12:33.376667
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():

    # check whether this platform supports xattrs
    from ..utils import _get_xattr_supported
    if not _get_xattr_supported():
        return

    from ..extractor.common import InfoExtractor

    ie = InfoExtractor({})
    info = {'filepath': '', 'title': 'testfile', 'description': 'xattr_test', 'uploader': 'youtubedl_test_user'}
    pp = XAttrMetadataPP(ie)
    pp.run(info)


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:12:34.485039
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass



# Generated at 2022-06-14 18:12:35.906461
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP({}, {}, {})

# Generated at 2022-06-14 18:12:47.729259
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """
    Test cases:
    - Title, description, uploader, format, upload_date available, NO_SPACE
    - Title, description, uploader, format, upload_date available, VALUE_TOO_LONG
    - Title, description, uploader, format, upload_date available, NO_WRITE_PERMISSIONS
    """
    import tempfile
    import shutil

    from ..utils import (
        XAttrMetadataError,
        XAttrUnavailableError,
    )


# Generated at 2022-06-14 18:12:50.097586
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-14 18:12:52.257447
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:12:52.864816
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:12:53.820835
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP({})

# Generated at 2022-06-14 18:13:41.486496
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # import
    from collections import defaultdict
    from ..utils import (
        FakeFile,
        SameFakeFile,
        XAttrMetadataError,
        XAttrUnavailableError,
    )

    # FakeFile for testing the write_xattrs method
    class XAttrFakeFile(FakeFile):

        def __init__(self):
            super(XAttrFakeFile, self).__init__()
            self.xattrs = defaultdict(dict)

        def write_xattr(self, filename, name, value):
            xattrs = self.xattrs
            if not filename in xattrs:
                xattrs[filename] = {}
            xattrs[filename][name] = value


# Generated at 2022-06-14 18:13:49.024006
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        'user.xdg.comment': 'description',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }
    # TODO: Check if 'XAttrMetadataPP' is a singleton or not
    xatt = XAttrMetadataPP()
    assert xatt.xattr_mapping == xattr_mapping

# Generated at 2022-06-14 18:13:50.130835
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO
    assert False

# Generated at 2022-06-14 18:13:59.967376
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    xa_m = XAttrMetadataPP()

    #
    # More info about extended attributes for media:
    #   http://freedesktop.org/wiki/CommonExtendedAttributes/
    #   http://www.freedesktop.org/wiki/PhreedomDraft/
    #   http://dublincore.org/documents/usageguide/elements.shtml
    #
    # TODO:
    #  * capture youtube keywords and put them in 'user.dublincore.subject' (comma-separated)
    #  * figure out which xattrs can be used for 'duration', 'thumbnail', 'resolution'
    #

    # Example input (non-youtube data)

# Generated at 2022-06-14 18:14:00.933349
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:14:06.353167
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .. import YoutubeDL
    ydl = YoutubeDL()
    p = XAttrMetadataPP(ydl)
    assert p.supported(), 'XAttrMetadataPP must be supported'
    # TODO: add test for postprocess method

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:14:15.523286
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from ..compat import compat_xattr
    from ..compat import compat_os_name
    from .common import FileDownloader
    from .common import PostProcessor

    class MockXAttrMetadataPP(XAttrMetadataPP):
        def __init__(self, downloader):
            PostProcessor.__init__(self, downloader)
            self.add_thumbnail = False

        def run(self, info):
            num_written = XAttrMetadataPP.run(self, info)
            return num_written

    class MockDownloader(FileDownloader):
        def __init__(self):
            self.to_screen("MockDownloader is being initialized")
            FileDownloader.__init__(self)

    p = MockXAttrMetadataPP(MockDownloader())

    # get dummy

# Generated at 2022-06-14 18:14:21.547596
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import datetime
    from ..utils import (
        calc_xattr_checksum,
        is_xattr_writable,
        xdg_get_cache_home,
        get_xattr_sep,
    )

    sep = get_xattr_sep()
    filename = xdg_get_cache_home() + '/test.flv'
    referrer_url = 'https://www.youtube.com/watch?v=BaW_jenozKc'

    if is_xattr_writable(filename):
        title = 'youtube-dl test video \'BaW_jenozKc\''
        upload_date = datetime.date(2012, 11, 27)
        description = 'Test video for youtube-dl.\nhttps://github.com/rg3/youtube-dl'

# Generated at 2022-06-14 18:14:23.094640
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert isinstance(pp, PostProcessor)

# Generated at 2022-06-14 18:14:24.491445
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP({})

# Generated at 2022-06-14 18:15:40.755472
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:15:51.233614
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import gen_extractors
    from ..downloader import gen_ydl
    ydl = gen_ydl(params={})
    ydl.add_post_processor(XAttrMetadataPP)

    # Sort of integration test
    extractors = gen_extractors()
    for i, ie in enumerate(extractors):
        if i % 10 == 0:
            print('Testing XAttrMetadataPP on ' + ie.IE_NAME)
        ie = ie.ie
        if ie.working:
            ie(ydl=ydl, force_generic_extractor=True)

# Invoke test when script is run
if __name__ == "__main__":
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:16:03.166454
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from types import ModuleType
    from youtube_dl.downloader import common as dl_common
    from youtube_dl.extractor import common as extractor_common
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor.common import PostProcessor
    from youtube_dl.compat import compat_os_name

    ydl = YoutubeDL({'writedescription': True, 'writeinfojson': True, 'outtmpl': '%(id)s%(ext)s'})


# Generated at 2022-06-14 18:16:12.949328
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..extractor import YoutubeIE
    from ..compat import compat_urllib_request

    test_values = {
        'webpage_url': 'http://www.youtube.com/watch?v=BaW_jenozKc',
        'description': 'test-description',
        'title': 'test-title',
        'format': 'test-format',
        'upload_date': '20130101',
        'uploader': 'test-uploader',
        'duration': '60',
        'thumbnail': 'test-thumbnail',
        'resolution': '360x240',
    }


# Generated at 2022-06-14 18:16:14.535174
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP.__name__ == 'XAttrMetadataPP'

# Generated at 2022-06-14 18:16:17.167550
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Basic test for XAttrMetadataPP
    """
    xattr_metadata = XAttrMetadataPP(None)
    assert xattr_metadata

# Generated at 2022-06-14 18:16:18.707426
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    assert pp.run(dict()) == ([], {})

# Generated at 2022-06-14 18:16:29.148201
# Unit test for method run of class XAttrMetadataPP

# Generated at 2022-06-14 18:16:32.609398
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .common import PostProcessor
    from .xattr import XAttrMetadataPP

    instance = XAttrMetadataPP()
    assert isinstance(instance, PostProcessor)


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:16:42.795019
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile
    from .common import FFmpegPostProcessor
    from ..utils import xattr_supported

    if not xattr_supported():
        return False

    ydl = FakeYdl()
    meta_processor = XAttrMetadataPP(ydl)
    info = {
        'filepath': None,
        'title': 'example',
        'webpage_url': 'https://example.org/',
        'upload_date': '20160201',
        'description': 'example description',
        'uploader': 'example uploader',
        'format': '21 - 480p'
    }

    temppath = tempfile.mkstemp()[1]
    info['filepath'] = temppath
    meta_processor.run(info)

    ff_processor = FFmpegPostProcessor(ydl)
