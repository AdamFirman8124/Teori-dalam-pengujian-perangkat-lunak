

# Generated at 2022-06-14 18:09:11.359594
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_metadata_pp = XAttrMetadataPP(None)

    assert type(xattr_metadata_pp) == XAttrMetadataPP
    assert type(xattr_metadata_pp.run) == types.MethodType

# Generated at 2022-06-14 18:09:14.820778
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    assert False, 'Not yet implemented'

# Generated at 2022-06-14 18:09:18.267606
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP('id')
    assert pp.downloader == 'id'


# Generated at 2022-06-14 18:09:21.746101
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """Test the functionality of the method XAttrMetadataPP.run."""

    return None


# Generated at 2022-06-14 18:09:23.157620
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert(XAttrMetadataPP.__name__ == 'XAttrMetadataPP')



# Generated at 2022-06-14 18:09:26.124480
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


# Generated at 2022-06-14 18:09:27.140655
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

# Generated at 2022-06-14 18:09:28.955465
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP.name == 'xattr_metadata'

# Generated at 2022-06-14 18:09:31.761594
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    pp.run(None)


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:09:42.321437
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FileDownloader
    from .common import PostProcessor
    from ..compat import compat_os_name
    from filecmp import cmp
    import os
    import shutil
    import sys
    import tempfile
    import unittest

    class MockInfo:
        def __init__(self, value_dict):
            self.__value_dict = value_dict

        def __getattr__(self, attr):
            return self.__value_dict.get(attr)

        def get(self, attr):
            return self.__value_dict.get(attr)

    class XAttrMetadataPP_run(unittest.TestCase):
        def setUp(self):
            self.to_delete = []
            self.test_fnames = ['test1', 'test2']
            self

# Generated at 2022-06-14 18:09:50.851076
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:10:00.520916
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    assert pp.xattr_mapping == {
        'user.xdg.referrer.url': 'webpage_url',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }
    assert pp.unsupported_reasons == {'NO_SPACE', 'VALUE_TOO_LONG'}

# Generated at 2022-06-14 18:10:11.739727
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .XAttrMetadataPP import XAttrMetadataPP
    from ..YoutubeDL import YoutubeDL
    from ..extractor.youtube import YoutubeIE

    YoutubeDL.params = {}
    # YoutubeDL.params['logger'] = YoutubeDL.create_stdout_logger('unit test')
    ydl = YoutubeDL({})

    ie = YoutubeIE(ydl)

# Generated at 2022-06-14 18:10:23.474518
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os

    import pytest
    from ..compat import xattr

    class FakeInfoDict(object):
        def __init__(self):
            self.info = dict()

        def __getitem__(self, item):
            return self.info[item]

        def get(self, item):
            return self.info.get(item)

        def __setitem__(self, key, value):
            self.info[key] = value

    class FakeYDL(object):
        def to_screen(self, message):
            print(message)

        def report_error(self, message):
            print(message)

        def report_warning(self, message):
            print(message)


# Generated at 2022-06-14 18:10:24.309845
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP()
    assert pp

# Generated at 2022-06-14 18:10:35.337398
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    original_getenv = os.getenv
    class InfoDict(dict):
        def __init__(self, filepath, title):
            self['filepath'] = filepath
            self['title'] = title


# Generated at 2022-06-14 18:10:38.124401
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP is not None

# Generated at 2022-06-14 18:10:40.407816
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # No unit tests for this module, there is no easy way to test it automatically
    # (too much platform specific stuff)
    pass

# Generated at 2022-06-14 18:10:52.144404
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import os.path
    x = XAttrMetadataPP()
    x._downloader = None # TODO: dummy downloader object instead of None

    xattr_mapping = {'user.xdg.referrer.url': 'webpage_url',
                     'user.xdg.comment': 'description',
                     'user.dublincore.title': 'title',
                     'user.dublincore.date': 'upload_date',
                     'user.dublincore.description': 'description',
                     'user.dublincore.contributor': 'uploader',
                     'user.dublincore.format': 'format'}

    # Test if XAttrMetadataPP's instance has xattr_mapping attribute
    assert hasattr(x, 'xattr_mapping')

    #

# Generated at 2022-06-14 18:10:53.231376
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    # TODO: Unit test when xattr support is available.
    pass

# Generated at 2022-06-14 18:11:13.930115
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    class MockYDL:
        def __init__(self):
            self.params = {
                'verbose': True,
            }
            self.to_screen_calls = 0
            self.report_warning_calls = 0
            self.report_error_calls = 0

        def to_screen(self, message):
            self.to_screen_calls += 1

        def report_warning(self, message):
            self.report_warning_calls += 1

        def report_error(self, message):
            self.report_error_calls += 1

    class MockInfo:
        def __init__(self, infodict=dict()):
            self.infodict = infodict

        def get(self, key):
            return self.infodict.get(key)


# Generated at 2022-06-14 18:11:21.470664
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    video_info = {
        'webpage_url': 'https://www.youtube.com/watch?v=BaW_jenozKc',
        'title': 'youtube-dl test video',
        'format': '22 - 720p',
        'uploader': 'Philipp Hagemeister',
        'upload_date': '20071124',
        'description': 'test description',
        'filepath': 'test.filepath',
    }

    pp = XAttrMetadataPP(None)
    pp.run(video_info)

# Generated at 2022-06-14 18:11:34.538740
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..extractor import gen_extractors
    from ..utils import DateRange

    def _test_xattr_write(filepath, xattrs_dict):
        import tempfile
        tmp_file = tempfile.NamedTemporaryFile()
        filename = tmp_file.name
        tmp_file.close()
        for xattr_name, xattr_value in xattrs_dict.items():
            write_xattr(filename, xattr_name, xattr_value.encode('utf-8'))

        xattrs = get_xattrs(filename)
        if xattrs:
            for xattr_name, xattr_value in xattrs_dict.items():
                assert xattr_name in xattrs.keys()
                assert xattr_value in xattrs.values()

    import os


# Generated at 2022-06-14 18:11:44.928416
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from .common import FileDownloader
    from .ffmpeg import FFmpegPostProcessor
    from .xattrpp import XAttrPostProcessor
    from .extractor import YoutubeIE
    from .downloader import Downloader


# Generated at 2022-06-14 18:11:54.864197
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """ Unit testing for XAttrMetadataPP class, method run. """

    # pylint: disable=import-error, no-name-in-module
    from . import common as pp_common
    from ..compat import compat_os_name, compat_os_open, compat_os_write

    # Patching open and glob functions
    compat_os_open_orig = compat_os_open
    def compat_os_open_mock(filename, flags, mode):
        """ mock for compat_os_open method when writing to file's xattrs """

        # Check if filename is correct
        assert filename == 'filename' # pylint: disable=undefined-variable

        return pp_common.MockFD(b'', flags=flags)

    compat_os_open.side_effect = compat_os_open_mock



# Generated at 2022-06-14 18:12:06.099992
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile
    import os
    import pytest
    from ..compat import PY2

    try:
        from ..utils import xattr_supported
        from ..utils import xattr_writable
    except ImportError:
        return

    if not xattr_supported() or not xattr_writable():
        return
    pytest.importorskip('xattr')

    # xattrs don't work on directories in Linux (https://github.com/xattr/xattr/issues/62),
    # so create a file to use as temporary filepath
    fd, filename = tempfile.mkstemp(prefix='ytdl_test_')
    os.close(fd)


# Generated at 2022-06-14 18:12:06.781856
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:12:09.553266
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP.__name__ is 'XAttrMetadataPP'
    assert XAttrMetadataPP.__doc__ is not None

# Generated at 2022-06-14 18:12:18.796763
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import pytest
    from tempfile import NamedTemporaryFile

    fd,path = NamedTemporaryFile(suffix=".tmp").file.get_filename()

    pp = XAttrMetadataPP()
    x,y = pp.run({'filepath':path, 'upload_date':'2012-12-12', 'title':'Test-Title', 'description':'Test-Description', 'uploader':'Test-Uploader', 'format':'MP4', 'webpage_url':'http://www.youtube.com/watch?v=dQw4w9WgXcQ'})

    assert(not x)
    assert(y['filepath'] == path)
    assert(y['upload_date'] == '2012-12-12')
    assert(y['title'] == 'Test-Title')

# Generated at 2022-06-14 18:12:19.863966
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass



# Generated at 2022-06-14 18:12:50.550005
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile

# Generated at 2022-06-14 18:13:02.873076
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import tempfile
    import os
    import platform
    from .common import FileDownloader

    if platform.system() == 'Windows':
        return
    else:
        try:
            write_xattr(__file__, 'user.dublincore.title', '1'.encode('utf-8'))
            os.remove(__file__)
        except (OSError, XAttrMetadataError):
            return

    info = {
        'filepath': tempfile.NamedTemporaryFile().name,
        'webpage_url': 'https://www.youtube.com/watch?v=9bZkp7q19f0',
        'title': 'Gangnam style',
        'upload_date': '20120916',
        'description': 'This is a test description',
    }

    downloader

# Generated at 2022-06-14 18:13:04.463608
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP.name == 'xattrs'


# Generated at 2022-06-14 18:13:08.383377
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader.common import FileDownloader
    try:
        fd = FileDownloader({'format': 'best'})
        xd = XAttrMetadataPP(fd)
    except Exception:
        pass

# Generated at 2022-06-14 18:13:12.236673
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    postprocessor = XAttrMetadataPP(
        {
            'filepath': '/dev/null',
            'format': 'webm',
            'title': 'test_title'

        }
    )
    postprocessor.run({})

# Generated at 2022-06-14 18:13:20.538512
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Test for various xattr exceptions
    from .common import FileDownloader
    from ..utils import XAttrUnavailableError, XAttrMetadataError
    from ..extractor.youtube import YoutubeIE
    from tempfile import TemporaryFile


    def raise_XAttrUnavailableError():
        raise XAttrUnavailableError('testing', 'testing')

    def raise_XAttrMetadataError():
        raise XAttrMetadataError('testing', 'testing')

    try:
        with TemporaryFile('w') as f:
            ydl = FileDownloader({'outtmpl': f.name})
            youtube_ie = YoutubeIE(ydl)
            youtube_ie.extract('https://www.youtube.com/watch?v=BaW_jenozKc')
    except XAttrUnavailableError:
        pass
   

# Generated at 2022-06-14 18:13:30.212637
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import sanitize_open

    class TestDownloader(object):
        def __init__(self):
            self.to_screen_messages = []
            self.errors = []
            self.warnings = []

        def to_screen(self, message, skip_eol=False):
            self.to_screen_messages.append(message)

        def report_warning(self, message):
            self.warnings.append(message)

        def report_error(self, message):
            self.errors.append(message)

    downloader = TestDownloader()
    pp = XAttrMetadataPP(downloader)

    #
    # Test normal mode
    #

# Generated at 2022-06-14 18:13:36.589920
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    d = {
        'webpage_url': 'http://example.com',
        'description': 'description',
        'title': 'title',
        'upload_date': '20151215',
        'uploader': 'uploader',
        'format': 'format',
    }
    assert pp.run(d) == ([], d)

# Generated at 2022-06-14 18:13:38.044873
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
  assert XAttrMetadataPP(None, None)._downloader is None

# Generated at 2022-06-14 18:13:48.951372
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader import Downloader

    d = Downloader()

    # manually set the script output template to ensure consistent tests
    d._yt_dl.params['outtmpl'] = '%(id)s%(ext)s'

    # create a video info object and set some properties that should be propagated to the file
    info = {
        'title': 'test title',
        'description': 'description',
        'upload_date': '20130913',
        'uploader': 'uploader',
        'webpage_url': 'url',
        'format': 'format'
    }

    # don't use real filesystem here
    import io
    import sys
    if sys.version_info[:2] > (2, 6):
        # io.FileIO is deprecated since Python 2.6
        from io import FileIO as _

# Generated at 2022-06-14 18:14:40.413427
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pp_test = XAttrMetadataPP()

    filename = '/tmp/test_ydl_xattrs'
    filepath = '/tmp/test_ydl_xattrs'
    info = {
        'filepath': filepath,
        'webpage_url': 'Hello World',
        'description': 'Foobar',
        'title': 'Test',
        'upload_date': '20150801',
        'uploader': 'Barfoo',
        'format': 'mp4',
    }

    with open(filename, 'w') as f:
        f.write('foo')

    # test XAttrUnavailableError exception
    def _os_fgetxattr(filepath, xattrname, *args):
        raise IOError((95, 'Operation not supported'))
    pp_test._os_f

# Generated at 2022-06-14 18:14:51.857046
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    import unittest

    info = {
        'webpage_url': 'https://www.youtube.com/watch?v=jNQXAC9IVRw',
        'upload_date': '20110127',
        'title': 'Wink Dot Dot Dot',
        'description': 'Wink Dot Dot Dot',
        'format': 'mp4',
        'uploader': 'Justin E. P.',
        'filepath': os.path.join(tempfile.gettempdir(), 'XAttrMetadataPP_test')
    }

    with open(info['filepath'], 'wb') as f:
        f.write(b'foobar\n')

    pp = XAttrMetadataPP()
    pp.run(info)


# Generated at 2022-06-14 18:15:02.948163
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import sys
    import tempfile
    import os
    from ..utils import FileDownloader

    def check_result(md, md_expected):
        for key, value in md_expected.items():
            assert key in md
            assert md[key] == value, 'value for ' + key + ' has changed'

    # Create a temporary file
    filepath = tempfile.mkstemp()[1]
    with open(filepath, 'wb') as f:
        f.write(b'Hello')
        f.flush()

    # Create FileDownloader instance
    downer = FileDownloader({
        'format': 'best',
        'outtmpl': filepath,
        'noprogress': True,
        'quiet': True,
        'writethumbnail': True,
        'writeinfojson': True,
    })

# Generated at 2022-06-14 18:15:04.012936
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # not implemented
    raise NotImplementedError

# Generated at 2022-06-14 18:15:14.146170
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import shutil
    import tempfile
    import unittest

    from .common import FileDownloader

    from ..utils import xattr_unavailable

    def skip_if_unavailable():
        if xattr_unavailable():
            raise unittest.SkipTest

    class TempDir(object):
        def __init__(self, suffix, prefix):
            self.path = tempfile.mkdtemp(suffix, prefix)

        def __enter__(self):
            return self.path

        def __exit__(self, type, value, traceback):
            shutil.rmtree(self.path, ignore_errors=True)

    def get_file_path(dirpath, filename):
        return os.path.join(dirpath, filename)


# Generated at 2022-06-14 18:15:23.116428
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    filename = "testfile.flv"

    # Metadata: title, description, uploader and upload_date
    yt_info = {
        "title": "test",
        "description": "testdesc",
        "uploader": "testuploader",
        "upload_date": "testuploaddate"
    }

    import tempfile

    with tempfile.NamedTemporaryFile() as f:
        pp = XAttrMetadataPP()
        pp.run(yt_info)


if __name__ == "__main__":
    test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:15:33.272223
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import os
    from . import get_testdata_dir
    from ..compat import compat_os
    from ..downloader import FakeYDL
    from ..extractor import gen_extractors

    test_file = os.path.join(get_testdata_dir(), 'test.mp4')
    extractors = gen_extractors()
    ie = extractors[0].ie
    d = FakeYDL({'outtmpl': '%(id)s.%(ext)s'})
    d.add_info_extractor(ie)
    results = d.extract_info(ie.suitable([{'url': 'https://www.youtube.com/watch?v=BaW_jenozKc'}])[0], download=False)


# Generated at 2022-06-14 18:15:36.236446
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ Test constructor of class XAttrMetadataPP """

    import pytest

    # test invalid downloader
    with pytest.raises(TypeError):
        XAttrMetadataPP(None, {})
    pass

# Generated at 2022-06-14 18:15:46.584403
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FileDownloader

    import pytest
    from unittest.mock import call, patch


# Generated at 2022-06-14 18:15:58.720225
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    class Info(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    # We initialize the field downloader of class XAttrMetadataPP
    class FakeDl(object):
        def to_screen(self, msg):
            pass

        def report_error(self, msg):
            pass

        def report_warning(self, msg):
            pass

    fake_dl = FakeDl()
    xattr_pp = XAttrMetadataPP(fake_dl)

    # We create an info object

# Generated at 2022-06-14 18:17:40.380353
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader import Downloader

    info = {
        'filepath': '/tmp/fakepath',
        'webpage_url': 'Webpage URL',
        'upload_date': '2016',
        'description': 'Description',
        'uploader': 'Uploader name',
        'format': 'Format',
        'title': 'Title'
    }

    # Mock write_xattr
    def mock_write_xattr(filename, xattrname, value):
        if len(xattrname) > len(value):
            raise XAttrMetadataError('VALUE_TOO_LONG',
                                     'Value too long')

        if len(value) > 10:
            raise XAttrMetadataError('NO_SPACE',
                                     'No space left on device')

        return True

    # Error code: VALUE

# Generated at 2022-06-14 18:17:49.361592
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from ..utils import encodeFilename

    #
    # Test for case when xattrs are supported.
    #

    from .common import FileDownloader

    def write_xattr(filename, xattrname, byte_value):
        if byte_value != b'value' or xattrname not in [b'user.xdg.referrer.url', b'user.dublincore.title']:
            raise XAttrMetadataError(XAttrMetadataError.REASON_UNKNOWN)

    def read_xattr(filename, xattrname):
        if xattrname not in [b'user.xdg.referrer.url', b'user.dublincore.title']:
            raise XAttrMetadataError(XAttrMetadataError.REASON_UNKNOWN)
        return b'value'

# Generated at 2022-06-14 18:17:49.884560
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    assert 1==1

# Generated at 2022-06-14 18:17:51.000682
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO: implement
    return

# Generated at 2022-06-14 18:18:01.415295
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import prepare_extractor, SearchInfoExtractor
    mp = XAttrMetadataPP()
    mp.running = True

    # Prepare dl and extractor
    dl = prepare_extractor()
    ie = SearchInfoExtractor()
    dl.add_info_extractor(ie)

    # Set the internal attributes needed for XAttrMetadataPP
    mp.add_default_info({
        'extractor': ie.IE_NAME,
        'filepath': './test_XAttrMetadataPP.run.mp4',
    })

    # Run the postprocessor
    mp.run({})



# Generated at 2022-06-14 18:18:12.755449
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    exc_test = lambda: XAttrMetadataError(XAttrMetadataError.NO_SPACE, 'test')

# Generated at 2022-06-14 18:18:20.390692
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import TORRENT_FILE_EXT
    from .common import FileDownloader
    from .xattrpp import XAttrMetadataPP

    try:
        import xattr

        xattr.listxattr
    except AttributeError:
        #
        # If xattr module is not available, just skip this test
        #
        import nose
        raise nose.SkipTest('xattr module not available')

    def _markers_listxattr(filename):
        #
        # Helper method that returns only xattrs set by the XAttrMetadataPP
        #
        return [attr for attr in xattr.listxattr(filename) if attr.startswith('user.')]


# Generated at 2022-06-14 18:18:23.204623
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """ Unit test for testing the method run of class XAttrMetadataPP """
    pass


# Generated at 2022-06-14 18:18:30.544801
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import os
    import tempfile
    import xattr

    info = {
        'title': 'I\'m a title',
        'webpage_url': 'http://www.mywebpage.com',
        'upload_date': '20151102',
        'description': 'MY DESCRIPTION',
        'uploader': 'MY UPLOADER',
        'ext': 'mp4',
        'format': 'MY FORMAT',
        'format_id': 'MY FORMAT ID',
        'display_id': 'I\'m a display id'
    }

    downloader = None


# Generated at 2022-06-14 18:18:41.129908
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Instantiate the test class
    from ..YtdlHooks import YtdlHooks
    from .common import DeprecatedPostProcessor
    class TestPostProcessor(DeprecatedPostProcessor, XAttrMetadataPP):
        def __init__(self, downloader=None):
            DeprecatedPostProcessor.__init__(self, downloader)
    ytdl_opts = {
        'format': '-',
        'logger': YtdlHooks(),
        'nooverwrites': True,
        'postprocessor_args': [],
    }
    ytdl = TestPostProcessor(ytdl_opts)

    # Values used by ytdl to fill the xattr
    # (a file path is needed to pass the test)