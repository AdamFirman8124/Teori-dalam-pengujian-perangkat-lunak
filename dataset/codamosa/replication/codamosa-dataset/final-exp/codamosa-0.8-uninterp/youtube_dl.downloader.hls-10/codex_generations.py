

# Generated at 2022-06-14 15:37:49.112372
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Test initialization of HlsFD with url
    url = 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8'
    try:
        HlsFD(None, None, url)
    except Exception as e:
        print('Failed to initialize HlsFD with url: ' + str(e))
        return False
    if not HlsFD.can_download(None, {'url': url}):
        print('Failed to initialize HlsFD can_download with url')
        return False
    return True

if __name__ == '__main__':
    if not test_HlsFD():
        print('Failed to pass unit test')
        exit(1)

# Generated at 2022-06-14 15:38:02.163444
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os
    import tempfile
    import http.server
    import socketserver
    import threading

    class HTTPServerV6(socketserver.TCPServer):
        address_family = socket.AF_INET6

    class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_HEAD(s):
            s.send_response(200)
            s.end_headers()

        def do_GET(s):
            path = s.path[1:]
            if path == 'index.m3u8':
                s.send_response(200)
                s.send_header('Content-type', 'application/vnd.apple.mpegurl')
                s.end_headers()

# Generated at 2022-06-14 15:38:11.421332
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import re
    import unittest
    from ..downloader.common import FileDownloader
    from ..extractor.common import InfoExtractor
    from ..utils import *
    from .test_utils import *
    from .test_fragment import *

    # These two test_cases must be the same for both hls and hls-native.

# Generated at 2022-06-14 15:38:24.901261
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """ Not an actual unit test to be able to run on all platform """
    from .test import get_test_data
    from ..utils import encode_data_uri, sanitize_open
    from ..extractor import get_info_extractor

    ie = get_info_extractor('hls')
    info = ie._real_extract({
        'url': 'http://devimages.apple.com/iphone/samples/bipbop/gear4/prog_index.m3u8',
        'http_headers': {'Cookie': 'cookie'},
    })
    fd = HlsFD(ie.ydl, ie.params)
    success = fd.real_download(
        'test.3gp', info['formats'][0])

# Generated at 2022-06-14 15:38:36.346420
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .compat import bytes_to_intlist
    import os
    import tempfile

    from ..extractor.common import InfoExtractor
    from ..utils import encode_compat_str
    from ..extractor import gen_extractors

    ie = gen_extractors()['generic']()

    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as tmp_fd:
        tmp_fd.close()

# Generated at 2022-06-14 15:38:38.778837
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .utils import real_download_test
    real_download_test(HlsFD, 'hls')

# Generated at 2022-06-14 15:38:51.362312
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    sys.path.append('..')

    import youtube_dl
    import unittest

    from .common import FakeYDL

    from .fragment_test import download_file_with_fragments, FakeManifest

    # test_HlsFD_realdownload_Fatal
    class test_HlsFD_realdownload_Fatal(unittest.TestCase):
        def runTest(self):
            self.assertFalse(download_file_with_fragments(
                FakeManifest(
                    {
                        'url': 'this is not a url',
                        '_decryption_key_url': 'https://example.com/key',
                    },
                    ['']),
                FakeYDL(),
                HlsFD,
                is_fatal_error=True
            ))

    #

# Generated at 2022-06-14 15:39:02.497299
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:13\n#EXT-X-MEDIA-SEQUENCE:0\n#EXTINF:10,\nhttp://www.yandex.ru/0.ts\n#EXTINF:10,\nhttp://www.yandex.ru/1.ts\n#EXTINF:10,\nhttp://www.yandex.ru/2.ts\n#EXTINF:10,\nhttp://www.yandex.ru/3.ts\n#EXT-X-ENDLIST\n', None)

# Generated at 2022-06-14 15:39:12.059312
# Unit test for constructor of class HlsFD

# Generated at 2022-06-14 15:39:23.497176
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import make_HTTPServer

    from .fragment import TestFragmentFD
    from .external import TestFFmpegFD

    def test_fragment_downloader(download_fragment, *args, **kwargs):
        return True, b'foobar'

    def test_real_download(url, *args, **kwargs):
        base_url = 'http://127.0.0.1:%d/' % server.server_port

# Generated at 2022-06-14 15:39:53.098648
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ytdl.YoutubeDL import YoutubeDL
    import tempfile
    import os
    import shutil
    import requests

    # Setup the temp directory to hold fragment files
    temp_dir = tempfile.TemporaryDirectory()

    # Download the manifest file set the output directory to temp_dir

# Generated at 2022-06-14 15:39:58.050522
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_test_data
    HlsFD().real_download(get_test_data('HlsFD_real_download1.m3u8'), {'url': 'https://127.0.0.1/HlsFD_real_download1.m3u8'})


# Generated at 2022-06-14 15:40:10.938380
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import pytest
    from ..extractor.common import InfoExtractor, SearchInfoExtractor
    from ..utils import FakeYDL

    class TestIE(InfoExtractor):
        IE_NAME = 'test'

        def _real_extract(self, url):
            return {
                'id': '1',
                'url': url,
            }

    class HlsIETest(InfoExtractor):
        IE_NAME = 'hlsietest'
        _VALID_URL = r'https?://(?:www\.)?test\.com/(?P<id>\d+).m3u8'

        def _real_extract(self, url):
            video_id = self._match_id(url)
            manifest_url = 'http://test.com/' + video_id + '.m3u8'


# Generated at 2022-06-14 15:40:23.650904
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import MockYDL, _common_ctx
    from ..extractor.generic import GenericIE

    fake_url = 'http://test.com/hls.m3u8'
    fake_url_w_query = 'http://test.com/hls.m3u8?query=key1=val1&key2=val2&'
    fake_url_w_extra_param = 'http://test.com/hls.m3u8?param=val'
    hls_info_dict = {'protocol': 'm3u8_native', 'url': fake_url, 'is_live': False}
    hls_info_dict_w_query = {'protocol': 'm3u8_native', 'url': fake_url_w_query, 'is_live': False}
    h

# Generated at 2022-06-14 15:40:25.844588
# Unit test for constructor of class HlsFD
def test_HlsFD():
    fd = HlsFD(None, None)
    assert fd.FD_NAME == 'hlsnative'

# Generated at 2022-06-14 15:40:33.083605
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import re
    import os
    import subprocess
    from .external import FFmpegFD
    # The tests of HlsFD are based on the ones of FFmpegFD
    test_FFmpegFD_real_download()
    # Basic test with test file
    ffmpeg_test_file = 'http://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_1mb.mp4'
    hls_test_file = ffmpeg_test_file.replace('.mp4', '.m3u8')

# Generated at 2022-06-14 15:40:46.179674
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import io
    import unittest
    import tempfile
    from .test_download.common import FakeYDL
    from .common import FakeFileDownloader

    class HlsFDTest(unittest.TestCase):
        def setUp(self):
            self.tempdir = tempfile.mkdtemp()

        def tearDown(self):
            for fname in os.listdir(self.tempdir):
                os.remove(os.path.join(self.tempdir, fname))
            os.rmdir(self.tempdir)


# Generated at 2022-06-14 15:40:47.942297
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD(None, {})

# Generated at 2022-06-14 15:40:58.815059
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download("""#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-PLAYLIST-TYPE:VOD
#EXTINF:10,
media_0.ts
#EXTINF:10,
media_1.ts
#EXTINF:10,
media_2.ts
#EXT-X-ENDLIST
    """, {"url": "", "http_headers": {}})


# Generated at 2022-06-14 15:41:11.564643
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import YoutubeIE
    import pytest
    from .test_fragment import FakeYDL
    ydl = FakeYDL()
    ydl.add_info_extractor(YoutubeIE(ydl))
    ydl.params['noplaylist'] = True

    test_urls = (
        ('https://www.youtube.com/watch?v=WROI5WQmQyQ', 'test_HlsFD_real_download_0.mp4'),
        ('https://www.youtube.com/watch?v=vr9jOuIpR0g', 'test_HlsFD_real_download_1.mp4'),
    )


# Generated at 2022-06-14 15:41:44.011140
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    opts = {
        'format': 'bestvideo+bestaudio',  # For tests, force bestvideo+bestaudio
        'no_color': True
    }

    # Media fragment download tests
    assert(HlsFD.can_download('#EXTM3U\n#EXTINF:5, index0\nmedia0.ts\n#EXTINF:3, index1\nmedia1.ts\n', {'extractor': HlsFD.FD_NAME, 'is_live': False}))

# Generated at 2022-06-14 15:41:48.376605
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import get_suitable_downloader
    downloader = get_suitable_downloader(HlsFD.can_download, HlsFD)
    downloader.url = 'http://example.com/'
    expected = HlsFD
    assert isinstance(downloader, expected)

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:41:57.546665
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_test_data
    import os

    with open(os.path.join(get_test_data, 'hds_manifest.f4m')) as f:
        content = f.read()

    info_dict = {
        'url': 'http://test.test/test.m3u8',
    }

    hlsfd = HlsFD(None, {'test': True})
    ctx = {}
    hlsfd._prepare_and_start_frag_download(ctx)
    hlsfd.can_download(content, info_dict)
    frag_url = 'http://test.test/fragment'
    frag_content = b'Test data'
    hlsfd._download_fragment(ctx, frag_url, info_dict)
    hlsfd._

# Generated at 2022-06-14 15:42:04.188586
# Unit test for constructor of class HlsFD
def test_HlsFD():
    info_dict = {
        'id': '1',
        'ext': 'mp4',
        'url': 'http://example.com/',
        'title': 'A test title',
    }

# Generated at 2022-06-14 15:42:15.843858
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .f4mfd import (
        F4mFD,
        parse_meta,
        _create_token_generator,
        _create_auth_param,
        _create_auth_generator,
    )
    from .dash import (
        DashSegmentsFD,
        _get_decryptor,
        _get_init_data,
    )
    from ..utils import (
        encodeFilename,
        unified_strdate,
        bytes_to_intlist,
    )
    from .m3u8 import (
        M3U8,
    )

    # Test cases:
    #   Case 1: AES-128 encryption with IV in manifest.
    #   Case 2: AES-128 encryption with IV in query (token).
    #   Case 3: AES-128 encryption with IV in query (auth).


# Generated at 2022-06-14 15:42:27.091077
# Unit test for constructor of class HlsFD
def test_HlsFD():
    try:
        import youtube_dl as ytdl
        from youtube_dl.YoutubeDL import YoutubeDL
    except ImportError:
        import sys
        sys.path.append('..')
        import youtube_dl as ytdl
        from youtube_dl.YoutubeDL import YoutubeDL

    class opts:
        pass

    opts.hls_use_mpegts = False
    opts.hls_prefer_native = True
    opts.hls_prefer_ffmpeg = False
    opts.prefer_ffmpeg = None
    opts.ytdl_skip_download = True
    ydl = YoutubeDL(opts)

    class params:
        pass

    params.__dict__ = {}
    params.__dict__['outtmpl'] = '%(id)s'

# Generated at 2022-06-14 15:42:31.451172
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..extractor import YoutubeIE
    from .common import download_org

    # test with a non-live HLS video
    ie = InfoExtractor('test', 'http://www.youtube.com/watch?v=GIQn8pab8Vc')
    try:
        ie._real_initialize()
    except AssertionError:
        # This is OK
        pass
    else:
        assert False, 'Live only video should raise an error'

    # test with a live HLS video
    ie = InfoExtractor('test', 'https://www.youtube.com/watch?v=oLHUoJyTa0Q')
    try:
        ie._real_initialize()
    except AssertionError:
        # This is OK
        pass

# Generated at 2022-06-14 15:42:41.654093
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..downloader import YoutubeDL
    from ..compat import compat_HTTPError
    import io
    import urllib
    import sys
    import io
    import os


# Generated at 2022-06-14 15:42:45.769169
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..extractor import YoutubeIE

    YouTube = InfoExtractor._build_class_by_name(YoutubeIE.ie_key())
    url = 'https://www.youtube.com/watch?v=UxxajLWwzqY'
    ie = YouTube(dict(ydl=dict(default_stdout=True)))
    ie.extract(url)

# Generated at 2022-06-14 15:42:56.849936
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    # Test AES-128 encryption
    manifest = '#EXTM3U\n#EXT-X-TARGETDURATION:1\n#EXT-X-KEY:METHOD=AES-128,URI="/static/crypto/key.bin",IV=0x1234567890abcdef1234567890abcdef\n#EXTINF:1,\n0.ts\n#EXT-X-ENDLIST\n'
    info_dict = {
        'url': 'master.m3u8',
    }
    assert HlsFD.can_download(manifest, info_dict)

    # Test with empty/unsupported encryption method

# Generated at 2022-06-14 15:44:03.255448
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .test import get_testdata_stream

    assert HlsFD.can_download(get_testdata_stream('hls.m3u8', 'media_playlist.m3u8').read(), {
        'url': 'https://example.com/media_playlist.m3u8', 'http_headers': {}, '_decryption_key_url': 'https://example.org/key.bin',
        'extra_param_to_segment_url': 'abcdef=1', 'is_live': False})

# Generated at 2022-06-14 15:44:11.169239
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import json
    import os
    import tempfile
    import unittest
    import shutil

    from ytdl.utils import (
        encodeFilename,
        sanitize_open,
    )
    from ..YoutubeDL import YoutubeDL
    from .external import ExternalFD

    class HlsFDTest(unittest.TestCase):
        def setUp(self):
            self.temp_dir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.temp_dir)

        def test_HlsFD_real_download(self):
            filename = os.path.join(self.temp_dir, 'test_HlsFD_real_download.mp4')


# Generated at 2022-06-14 15:44:23.352608
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    import os
    from .test_downloader import TestDownloader
    from ..extractor import gen_extractors

    class HlsFDTest(unittest.TestCase):
        def setUp(self):
            def _media_frag_download(self, fragment_url, substitute_url=None, retry_on_error=False,
                                     headers={}, query={}, timeout=None):
                if substitute_url:
                    fragment_url = substitute_url
                if retry_on_error or substitute_url or headers or query or timeout is not None:
                    raise Exception('HlsFD should not use media_frag_download')
                if fragment_url == 'https://test.url/video0.ts':
                    return True, b'\x00' * 8192  # Mock video fragment

# Generated at 2022-06-14 15:44:25.931397
# Unit test for constructor of class HlsFD
def test_HlsFD():
    try:
        #Test the construtor of class HlsFD
        hlsfd = HlsFD(None, None)
    except:
        print("Error constructing HlsFD")


# Generated at 2022-06-14 15:44:32.638282
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..extractor import YoutubeDL
    from ..utils import SearchInfoExtractor

    ydl = YoutubeDL()
    ydl.add_info_extractor(SearchInfoExtractor())

    # test can_download method with samples collected from various sites

# Generated at 2022-06-14 15:44:33.959901
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert FFmpegFD.can_download(None, None) is True

# Generated at 2022-06-14 15:44:45.527999
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test_utils import fake_downloader
    from .test_utils import FakeHtmlParser
    from .test_utils import _assert_download
    from .test_utils import _assert_download_failure
    from .test_utils import _assert_download_info

    dl = fake_downloader({
        'params': {'playlist_items': '1-2', 'skip_unavailable_fragments': True, 'keep_fragments': True, 'fragment_retries': 1},
        'progress_hooks': [],
        'test': True,
    })

    # test playlists

# Generated at 2022-06-14 15:44:54.925949
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import FakeYDL
    from .test_common import get_test_data_file

    class ContextManager(object):
        def __init__(self, obj):
            self.obj = obj

        def __enter__(self):
            return self.obj

        def __exit__(self, exc_type, exc_value, tb):
            pass

    # Open file "fragment.m4s" for reading as binary
    with open(get_test_data_file(__file__, 'fragment.m4s'), 'rb') as test_fragment:
        with ContextManager(test_fragment) as test_fragment:
            test_ydl = FakeYDL()
            hlsfd = HlsFD(test_ydl, {'test': True})


# Generated at 2022-06-14 15:45:02.995197
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .http import HttpFD
    from .dash import DASHFD
    from .external import FFmpegFD

    import io
    import pytest
    from ..compat import compat_urllib_error
    from ..utils import FakeYDL

    class TestHlsFD(HlsFD):
        def __init__(self, ydl, params):
            super(TestHlsFD, self).__init__(ydl, params)
            self._last_url = None
            self._real_download_fragment = self._download_fragment

        def _prepare_url(self, info_dict, url):
            self._last_url = url
            return url


# Generated at 2022-06-14 15:45:08.942693
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    from .extractor.common import InfoExtractor
    from ..compat import mock

    test_url = 'https://manifest_url.m3u8'
    test_playlist = """
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0

#EXTINF:10,
frag_1
#EXTINF:6,
frag_2

#EXT-X-ENDLIST
    """

    def mock_urlopen(req, *args, **kwargs):
        assert req.get_full_url() == test_url
        return mock.Mock(read=lambda: test_playlist, geturl=lambda: req.get_full_url())
