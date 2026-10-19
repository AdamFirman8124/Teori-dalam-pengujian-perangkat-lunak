

# Generated at 2022-06-14 15:37:47.141349
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD(None, None)

# Generated at 2022-06-14 15:38:00.397338
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert(HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {}))
    assert(HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {'extra_param_to_segment_url': ''}))
    assert(HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {'_decryption_key_url': ''}))

    assert(not HlsFD.can_download('', {}))
    assert(not HlsFD.can_download('', {'is_live': True}))
    assert(not HlsFD.can_download('#EXT-X-KEY:METHOD=SOME', {}))

# Generated at 2022-06-14 15:38:10.423281
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """
    Run a test for the constructor of class HlsFD
    """
    from .extractor.common import InfoExtractor
    from .downloader.common import FileDownloader
    from .postprocessor.common import PostProcessor
    from .utils import DateRange
    from .compat import compat_str
    from .extractor import gen_extractors

    class DummyPostProcessor(PostProcessor):
        def run(self, information):
            return information

    class DummyInfoExtractor(InfoExtractor):
        IE_NAME = 'Dummy'
        IE_DESC = False  # Do not list
        _VALID_URL = r'.*'


# Generated at 2022-06-14 15:38:23.968465
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import youtube_dl.FileDownloader
    import youtube_dl.utils
    outtmpl = '%(epoch)s.%(format_id)s.mp4'
    params = {'format': 'mp4_dash_manifest', 'test': True}
    ydl = youtube_dl.FileDownloader.FileDownloader(params)
    fd = HlsFD(ydl, params)
    assert fd.can_download('#EXTM3U', {'url': 'http://example.com/'})

# Generated at 2022-06-14 15:38:35.648416
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    import io
    import os
    import tempfile
    from .downloader import YoutubeDL
    from .cache import Cache
    from .extractor.common import InfoExtractor
    from .extractor.youtube import YoutubeIE

    try:
        from .utils import _encodeFilename
    except ImportError:
        from .compat import _encodeFilename

# Encode path to utf-8 if necessary
    def fsencode(s):
        if isinstance(s, bytes):
            return s
        return _encodeFilename(s)


# Generated at 2022-06-14 15:38:42.055481
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import YoutubeIE
    from ..downloader import YoutubeDL
    ydl = YoutubeDL({
        'noplaylist': True,
        'format': 'bestvideo[protocol^=m3u8_native]+bestaudio[protocol^=m3u8_native]/best',
    })
    ie = YoutubeIE(ydl)
    fd = HlsFD(ydl, ydl.params)
    assert not fd.can_download(
        'https://example.com/',
        {'url': 'https://example.com/', '_type': 'hls'})

# Generated at 2022-06-14 15:38:53.825914
# Unit test for constructor of class HlsFD

# Generated at 2022-06-14 15:39:02.093661
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import YoutubeIE, get_info_extractor

    extractor = get_info_extractor(YoutubeIE.ie_key())
    ie = extractor._real_extract(
        r'https://www.youtube.com/watch?v=DZWnM1eU6gI')

    fd = HlsFD(None)
    if not fd.can_download(ie['url']):
        return False

    import tempfile
    filename = tempfile.mktemp()
    fd.real_download(filename, ie)
    return True

# Generated at 2022-06-14 15:39:08.964598
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import MockYDL
    from .test import get_test_data_file

    def verify_fragments_downloaded(content):
        import json
        # Verify that the content is the same as the test data
        with open(get_test_data_file('hls.txt')) as f:
            test_data = f.read()
        assert content == test_data
        # Verify that the correct media fragments have been downloaded
        assert ydl.download_frag_count == 3

# Generated at 2022-06-14 15:39:13.841108
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert (HlsFD.can_download("#EXT-X-DISCONTINUITY", "") == True)

if __name__ == '__main__':
    # Run all tests
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 15:39:37.290330
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import re
    import shutil
    from .common import FakeYDL, FakeFD
    from .extractor import get_info_extractor
    from .compat import compat_HTTPError

    def test_real_download_helper(
            ie, url, *query, **kwargs):
        out_filename = kwargs.get('out_filename')
        fragment_retries = kwargs.get('fragment_retries', 3)
        expected_fragment_count = kwargs.get('expected_fragment_count', None)
        expected_fragment_retries = kwargs.get('expected_fragment_retries', None)

        def _mocked_urlopen(url, extra_info=None):
            assert extra_info is None


# Generated at 2022-06-14 15:39:44.331297
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import os
    import ydl_opts
    opts = ydl_opts.YDL_OPTS
    hls_url = 'https://example.com/manifest/master.m3u8'
    hls_info = {'url': hls_url, 'format_id': 'hls'}
    hls_filename = os.path.join('test_out', hls_info['format_id'], hls_url.split('/')[-1])
    hls_fd = HlsFD(opts, hls_info)

# Generated at 2022-06-14 15:39:54.344320
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    from ..utils import FakeYDL
    from ..extractor import YoutubeIE
    """
    A test case to test the real_download method of HlsFD
    :return: a test suite of the test case
    """

    class TestHlsFD(unittest.TestCase):
        def setUp(self):
            """
            Set up for the test case
            :return: None
            """
            self.ydl = FakeYDL()
            self.params = {'noprogress': True, 'quiet': True, 'simulate': True}

# Generated at 2022-06-14 15:40:04.269135
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..utils import unescapeHTML
    import sys
    import os

    class MockYDL(object):
        def __init__(self, params):
            self.params = params
            self.to_screen = lambda x: None
            self.report_warning = lambda x: None
        def urlopen(self, s):
            return compat_urllib_error.HTTPError(s, 200, 'OK', None, None)

    class DummyIE(InfoExtractor):
        def __init__(self, ydl):
            self.ydl = ydl

    class DummyIE2(InfoExtractor):
        def __init__(self, ydl):
            self.ydl = ydl


# Generated at 2022-06-14 15:40:17.597434
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import pytest
    hls_fd = HlsFD(None, None)
    assert hls_fd.FD_NAME == 'hlsnative'
    assert not HlsFD.can_download("#EXT-X-KEY:METHOD=blah", {})
    assert HlsFD.can_download("", {})
    assert not HlsFD.can_download("#EXT-KEY:METHOD=NONE", {})
    assert HlsFD.can_download(
        "#EXT-X-KEY:METHOD=AES-128",
        {'_decryption_key_url': "Key_url"})
    assert not HlsFD.can_download(
        "#EXT-X-KEY:METHOD=AES-128",
        {'extra_param_to_segment_url': "blah"})
    assert not Hls

# Generated at 2022-06-14 15:40:28.567436
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:40:34.918137
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    HlsFD = HlsFD(None)
    errors = 0
    def error(s):
        r = HlsFD.can_download(s, {})
        global errors
        if r:
            print('ERROR: can_download() returned True for:')
            print('  ' + s.replace('\n', '\n  '))
            errors += 1
            return False
        return True
    # Note: We just test for non false return value since
    # HlsFD.can_download() does not return true for some
    # cases it should (see the comment describing UNSUPPORTED_FEATURES).
    assert error('#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:7794\n#EXTINF:10,\n')

# Generated at 2022-06-14 15:40:46.916014
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import youtube
    # test that HlsFD can be instanciated if youtube-dl is called on a HLS live stream

# Generated at 2022-06-14 15:40:58.520715
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..cache import Cache
    from ..extractor import YoutubeIE
    from ..downloader import FakeYDL
    from ..compat import compat_str
    import unittest
    import shutil
    import os.path

    # Setup
    tempdir = os.path.join(os.path.dirname(__file__), 'HlsFD_real_download_test')
    if not os.path.isdir(tempdir):
        os.mkdir(tempdir)
    info = YoutubeIE._real_extract('https://www.youtube.com/watch?v=PpR7ZG9XkdQ', None)
    ydl = FakeYDL()
    ydl.cache = Cache(tempdir)
    file = tempdir + '/out.mp4'

# Generated at 2022-06-14 15:41:11.529102
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .internal import DashSegmentsFD
    from .external import FFmpegFD
    ydl = MockYDL()
    fd = HlsFD()
    fd.params = {'test': True}
    fd.to_screen = lambda *args, **kargs: None
    fd.report_error = lambda *args, **kargs: None
    fd.report_warning = lambda *args, **kargs: None
    fd.report_retry_fragment = lambda *args, **kargs: None
    fd.report_skip_fragment = lambda *args, **kargs: None
    fd.add_progress_hook = lambda ph: None
    fd.ydl = ydl

# Generated at 2022-06-14 15:41:46.208609
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import io

    from ..utils import encode_data_uri

    from .external import FFmpegFD
    from .hls import HlsFD
    from .http import HttpFD
    from .skip import SkipFD

    # In this test we want to

    # 1. test file generated can be opened by ffmpeg
    # 2. test the timestamps of the first fragment (it is hard to test the timestamps of the last fragment
    #    because of the change of timestamps for the last fragment in setuptools 38.4.0)
    # 3. test the size of the downloaded fragment is what is expected (so we can test range headers)
    # 4. test the downloaded fragment is in fact the expected fragment

    # Configuration

# Generated at 2022-06-14 15:41:58.156266
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os
    import shutil
    from .testutils import FakeYDL, FakeFD

    # Remove directory with test file
    def rm_testfile_dir(file_name):
        testfile_dir = os.path.split(file_name)[0]
        temp_output_dir = os.path.split(testfile_dir)[0]
        shutil.rmtree(temp_output_dir)

    # Test with HLS manifest file
    test_file = os.path.join(os.path.dirname(__file__), 'test.m3u8')
    test_data = b''

# Generated at 2022-06-14 15:42:05.980670
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test_downloads import (
        setup_test_downloads,
        teardown_test_downloads,
        set_up_pycrypto,
        tear_down_pycrypto,
    )

    # Skip test if module pycrypto is not present
    set_up_pycrypto()
    setup_test_downloads()

    import os
    import youtube_dl

    # pylint: disable=too-many-locals
    # pylint: disable=too-many-statements


# Generated at 2022-06-14 15:42:17.167370
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .http import HttpFD
    from .external import FFmpegFD

    def _test_method(test_instance, method, *args, **kwargs):
        try:
            method(*args, **kwargs)
        finally:
            test_instance.methods_called.append(method.__name__)

    def make_HlsFD(self, *args, **kwargs):
        res = HlsFD(self, *args, **kwargs)
        res._progress_hooks = []
        res._prepare_url = lambda x, y: y
        res._download_fragment = lambda ctx, _, __, ___: (True, b'frag_content')
        res._append_fragment = lambda x, y: _test_method(self, self.append_fragment, x, y)

# Generated at 2022-06-14 15:42:21.638055
# Unit test for constructor of class HlsFD
def test_HlsFD():
    print('Testing HlsFD')
    try:
        hls = HlsFD(None, None)
    except Exception as e:
        print('Failed to initialize HlsFD: ' + str(e))
        return False
    return True



# Generated at 2022-06-14 15:42:30.560340
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    filename = 'HlsFD-test.out'
    manifest = """#EXTM3U
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10,
http://media.example.com/segment1.ts
#EXTINF:10,
http://media.example.com/segment2.ts
#EXTINF:10,
http://media.example.com/segment3.ts
"""

    # Test downloading a simple manifest (without encryption, initialization segment,
    # playlist composed of byte ranges, live stream, or appended segments)
    info_dict = {
        'url': 'http://manifest.example.com/test.m3u8',
        'http_headers': {},
    }

# Generated at 2022-06-14 15:42:40.934646
# Unit test for constructor of class HlsFD
def test_HlsFD():
    url = 'https://hls-geo.daserste.de' + \
        '/i/videoportal/Film/c_620000/622873/' + \
        'format,716451,716457,716450,716458,716459,.mp4.csmil/' + \
        'master.m3u8?null=0'

# Generated at 2022-06-14 15:42:48.428855
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import tempfile

    from .common import FakeYDL
    from ..utils import limited_stream


# Generated at 2022-06-14 15:42:58.869897
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import sys
    import copy
    import subprocess
    from .extractor.common import InfoExtractor

    class DummyYDL(object):
        """Simple downloader stub."""
        params = {
            'hls_prefer_native': True,
            'prefer_insecure': True,
        }
        def __init__(self):
            pass
        def to_screen(self, msg):
            pass
        def urlopen(self, url):
            return open(url[7:], 'rb')

    def test_HlsFD_real_download_main(url, ydl):
        """Main stub for calling real_download.

        Keyword arguments:
        url   -- URL for which the real_download should be tested
        ydl   -- DummyYDL instance

        """

# Generated at 2022-06-14 15:42:59.759511
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    #TODO
    pass

# Generated at 2022-06-14 15:44:04.319816
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import FakeYDL
    from .extractor.common import InfoExtractor

    import tempfile
    from os.path import join
    from .youtube_dl.YoutubeDL import YoutubeDL
    import youtube_dl

    # generating a fake url (protocol://username:password@host/path)
    url = 'http://127.0.0.1/playlist.m3u8?some=query"'

# Generated at 2022-06-14 15:44:13.681150
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import pytest
    from ..utils import FakeYDL

    mock_urlopen = FakeYDL.urlopen_mock({
        'https://example.com/manifest': b'#EXTM3U\n#EXTINF:1.2,\nsegment-1.ts\n',
        'https://example.com/segment-1.ts': b'abc'
    })

    ydl = FakeYDL()
    ydl.params = {
        'outtmpl': 'test_%(id)s.mp4',
        'skip_download': True,
        'playlist_items': '0',
        'hls_prefer_native': True,
    }
    ydl.add_download_result(False)

    fd = HlsFD(ydl, ydl.params)

    info

# Generated at 2022-06-14 15:44:24.525070
# Unit test for constructor of class HlsFD

# Generated at 2022-06-14 15:44:31.752329
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .downloader_test import MockYdl
    from .downloader_test import MockYdlFsock
    from .downloader_test import MockYdlFd
    import time


# Generated at 2022-06-14 15:44:43.140586
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    from .testutils import FakeYDL
    from .extractor import YoutubeDL
    from .downloader import FileDownloader

    def test(manifest_content, info_dict, expected_result, expected_length):
        def _check_result(result):
            assert result == expected_result

        def _check_length(result):
            assert len(result) == expected_length

        ydl = YoutubeDL({
            'forcejson': True,
            'fragment_retries': 0,
            'skip_unavailable_fragments': True,
            'outtmpl': '%(id)s.%(ext)s',
        })
        ydl.add_progress_hook(_check_result)
        ydl.add_progress_hook(_check_length)
        fd = H

# Generated at 2022-06-14 15:44:46.191709
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.__name__ == 'HlsFD'
    h = HlsFD(None, {})
    assert h.FD_NAME == 'hlsnative'
    assert h.params == {}


# Generated at 2022-06-14 15:44:49.213212
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD(None, None)

# Only run the tests if no other classes use HlsFD
if __name__ == "__main__":
    import sys
    import doctest
    doctest.testmod()
    sys.exit()

# Generated at 2022-06-14 15:44:58.376523
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():

    import unittest

    class HlsFDTestCase(unittest.TestCase):

        def test_can_download(self):
            import re
            import warnings
            from .downloader import Downloader


# Generated at 2022-06-14 15:45:05.564006
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U', {'is_live': False})
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128', {'is_live': False})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128', {'is_live': True})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE', {'is_live': False})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE\n#EXT-X-BYTERANGE:123', {'is_live': False})


# Generated at 2022-06-14 15:45:16.827450
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    import sys
    import os
    import tempfile
    import shutil

    # Python 3 renamed assertRaisesRegexp to assertRaisesRegex,
    # and fires deprecation warnings if a program uses the old name.
    if not hasattr(unittest.TestCase, 'assertRaisesRegex'):
        unittest.TestCase.assertRaisesRegex = unittest.TestCase.assertRaisesRegexp

    # We import youtube_dl inside the tests in order to be able to patch its
    # members more easily
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.compat import compat_urlparse
    from youtube_dl.downloader.common import FileDownloader
