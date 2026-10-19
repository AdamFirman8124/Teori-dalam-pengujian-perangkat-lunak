

# Generated at 2022-06-14 15:37:54.060149
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:38:01.999209
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors, list_extractors
    gen_extractors()
    info_dict = {}
    for ie in list_extractors(True):
        if ie.suitable(info_dict) and ie.IE_NAME == 'hls':
            info_dict['extractor'] = ie.IE_NAME
            ie.extract(ie.url)
            break

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:38:10.683272
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .hls_fd import HlsFD
    from .external import FFmpegFD
    from .http_fd import HttpFD
    from .dash_fd import DashFD
    from .common import FileDownloader
    from .extractor.common import InfoExtractor
    from ..utils import prepare_filename

    import os

    url = 'http://hls-geo.daserste.de/i/videoportal/Film/c_620000/622873/format,716451,716457,716450,716458,716459,.mp4.csmil/index_4_av.m3u8?null=0'

# Generated at 2022-06-14 15:38:22.761393
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    hls_fd = HlsFD(None, {})
    assert not hls_fd.can_download('#EXT-X-PLAYLIST-TYPE:EVENT', {})
    assert hls_fd.can_download('#EXT-X-PLAYLIST-TYPE:VOD', {})
    assert not hls_fd.can_download('#EXT-X-KEY:METHOD=AES-128', {})
    assert hls_fd.can_download(
        '#EXT-X-KEY:METHOD=AES-128\n#EXT-X-KEY:METHOD=NONE', {})
    assert hls_fd.can_download('#EXT-X-KEY:METHOD=NONE', {})

# Generated at 2022-06-14 15:38:34.008419
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.name() != ""
    assert HlsFD.can_download(None, None)
    fd = HlsFD('youtube-dl', None)
    assert fd.real_download(None, None) is False
    assert fd._download_fragment(None, None, None, None) == (False, None)
    assert fd._prepare_and_start_frag_download(None) is None
    assert fd._append_fragment(None, None) is None
    assert fd._finish_frag_download(None) is None
    assert fd._prepare_url(None, None) != ""

if __name__ == "__main__":
    test_HlsFD()

# Generated at 2022-06-14 15:38:40.307782
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import youtube_dl
    ydl = youtube_dl.YoutubeDL({})
    HlsFD.can_download('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1,RESOLUTION=1280x720\nfoo.m3u8',
        {'url': 'foo.m3u8', 'http_headers': {}})

# Generated at 2022-06-14 15:38:52.477787
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_testdata_server_handler
    from ..utils import prepare_url
    from .utils import FakeYDL

    assert can_decrypt_frag, 'pycrypto not found'

    test_server_handler = get_testdata_server_handler()
    ydl = FakeYDL()
    ydl.urlopen = test_server_handler.urlopen

    url = prepare_url('http://localhost:8080/hls/plaintext_key.m3u8')

# Generated at 2022-06-14 15:38:58.086474
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Create object without argument
    hls = HlsFD()

    # Create object with argument
    argument = dict(params=dict(verbose=True, quiet=True))
    hls_with_argument = HlsFD(argument)

    # Do not delete; let unit test find out memory leak
    assert (hls and hls_with_argument)

# Generated at 2022-06-14 15:39:06.797629
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:39:18.753308
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U', {})
    assert HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {})
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {'is_live': True})
    assert HlsFD.can_download('#EXT-X-KEY:METHOD=AES-128', {'_decryption_key_url': 'http://localhost'})
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=AES-128', {})
    assert not HlsFD.can_download('#EXT-X-BYTERANGE', {})

# Generated at 2022-06-14 15:39:39.817049
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import sys
    import tempfile

    from ..utils import (
        encodeFilename,
    )
    from ..extractor import YoutubeIE


# Generated at 2022-06-14 15:39:51.216765
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import tempfile
    import json
    from ..utils import DownloadError

    def test(info_dict, expected_result = True):
        print('Test case: ' + json.dumps(info_dict))
        # Create a temporary file to write data to
        temp = tempfile.NamedTemporaryFile('w', delete=False)
        file_name = temp.name
        temp.close()


# Generated at 2022-06-14 15:39:57.973259
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..compat import compat_HTTPError
    from ..extractor.common import InfoExtractor
    from ..utils import prepend_extension
    from ..compat import compat_urlparse

    cmd = {
        'url': 'https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/film-4002312263-2._CB547027891_.png',
        'playliststart': 1,
        'playlistend': 2
    }

    def _http_error(request, **kwargs):
        raise compat_HTTPError(request, 403, 'Forbidden', None, None)


# Generated at 2022-06-14 15:40:10.940021
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import re
    from .urlfetch import URLFetchError, URLSizeLimitExceededError
    from .http import HTTPDownloader

    class FakeHLSInfo(dict):
        def __init__(self, dict_):
            dict.__init__(dict_)

    # Real example
    # https://manifest.googlevideo.com/api/manifest/hls_playlist/source/m3u8?ipbits=0&clen=8570148&itag=137&expire=1536993882&ei=P3MqW4GvM8Ls8wS6m724BA&sparams=clen,ei,expire,gir,id,ip,ipbits,ipbypass,itag,lmt,mime,mm,mn,ms,mv,pl,

# Generated at 2022-06-14 15:40:23.651818
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import pytest
    from .extractor.generic import GenericIE

    # The test should be run with this command:
    # pytest -k HlsFD --extractor GenericIE --video-id <video-id> --playlist-id <playlist-id> --fragment-index <fragment-index>

    class TestHlsFD:
        def __init__(self, video_id, playlist_id, fragment_index):
            self.extractor = GenericIE({})

# Generated at 2022-06-14 15:40:25.873239
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """Build a HlsFD object and test its attributes"""
    from .extractor import gen_extractors

    ydl = gen_extractors()['youtube']
    fd = HlsFD(ydl, {})
    assert fd.ydl == ydl
    assert fd.AUTO_ADAPT == True

# Generated at 2022-06-14 15:40:36.384188
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import YoutubeIE
    from ..utils import youtube_dl_extractor
    import os

    test_url = 'https://youtu.be/dAiOvc-YhBE'
    temp_file = 'temp_HlsFD_real_download_file.mp4'

    ydl = youtube_dl_extractor(YoutubeIE)
    ydl.params.update({
        'hls_use_mpegts': True,  # For testing, force downloading of a hls-mpegts manifest
        'test': True,
    })
    with ydl:
        result = ydl.extract_info(test_url, download=False)

    hlsfd = HlsFD(ydl, ydl.params)
    success = hlsfd.real_download(temp_file, result)
    os.remove

# Generated at 2022-06-14 15:40:47.781116
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    The method real_download is tested using dummy_HlsFD class
    """
    class dummy_HlsFD(HlsFD):
        def __init__(self):
            self.fragment_list = []
            self.progress_hooks_list = []
            self.stored_frags = []
            self.line_count = 0
            self.line_index = 0
            self.frag_index = 0

        def test(self, manifest, info_dict, fragment_index=0):
            self.line_count = 0
            for line in manifest.splitlines():
                self.line_count += 1
            self.line_index = 0
            self.frag_index = fragment_index
            return self.real_download('dummy_filename', info_dict)


# Generated at 2022-06-14 15:40:58.648210
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    import os
    import tempfile
    import http.server
    import socket
    import threading
    import shutil
    import json
    import hashlib
    import binascii
    try:
        from Crypto.Cipher import AES  # pylint: disable=unused-variable
    except ImportError:
        AES = None
    from ..extractor import gen_extractors
    from ..downloader import Downloader
    extractors = gen_extractors()

    for ie in extractors:
        if ie.IE_NAME != 'hlsnative':
            continue
        downloader = Downloader(extractors)
        ie = downloader.get_info_extractor(ie.ie_key())
        ie.setDownloader(downloader)


# Generated at 2022-06-14 15:41:11.518257
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..downloader import FileDownloader
    from .external import ExternalFD
    from .fragment import FragmentFD
    from .http import HttpFD

    # Test download of hls streams that can be handled by HlsFD

# Generated at 2022-06-14 15:41:27.317814
# Unit test for constructor of class HlsFD
def test_HlsFD():
    ydl = FakeYDL()
    params = {'format': 'best', 'username': 'test', 'password': 'test'}
    hlsfd = HlsFD(ydl, params)
    assert isinstance(hlsfd, HlsFD)
    assert hlsfd.ydl is ydl
    assert hlsfd.params is params


# Generated at 2022-06-14 15:41:38.980634
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import tempfile
    import os
    import shutil
    from .testutils import FakeYDL
    ydl = FakeYDL()
    hls_fd = HlsFD(ydl, {'skip_unavailable_fragments': False, 'test': True})
    with tempfile.NamedTemporaryFile(delete=False) as test_file:
        shutil.copyfile('test/test_data/hls_test.m3u8', test_file.name)
        assert hls_fd.real_download(test_file.name, {
            'url': test_file.name,
            'name': "A title",
            'playlist': "This is a playlist",
            'playliststart': 1,
            'playlistend': 3,
        })

# Generated at 2022-06-14 15:41:48.241542
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    # method returns True when manifest does not have any unsupported features
    manifest_true_1 = ('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXT-X-TARGETDURATION:10\n#EXTINF:10,\n'
        'http://example.com/fragment1.ts\n#EXTINF:10,\n'
        'http://example.com/fragment2.ts\n#EXT-X-ENDLIST\n')
    info_dict_true_1 = {}
    assert HlsFD.can_download(manifest_true_1, info_dict_true_1)

    # method returns True when manifest has unsupported features but we have
    # extra_param_to_segment_

# Generated at 2022-06-14 15:41:50.609440
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import test_HlsFD_real_download
    test_HlsFD_real_download(HlsFD)

# Generated at 2022-06-14 15:42:01.014177
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import tempfile

    sys.path.append('..')
    from youtube_dl import YoutubeDL
    from youtube_dl.extractor import set_downloader
    from youtube_dl.downloader import set_socks_proxy

    # Downloading with proxy and socks config
    set_socks_proxy('127.0.0.1', 9050)
    set_downloader('HlsFD')
    ydl = YoutubeDL()
    info_dict = {'url': 'https://example.com/video.m3u8',
                 '_decryption_key_url': 'https://example.com/encryption.key',
                 'is_live': True}
    # First test does not work

# Generated at 2022-06-14 15:42:12.754282
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Disable the test when pycrypto is not present
    if can_decrypt_frag:
        import pytest

        # Disable the test when aes_decrypt_binary is not present in the youtube_dl
        from youtube_dl.postprocessor import common

        has_aes = hasattr(common, 'aes_decrypt_binary')
        if has_aes:
            import base64


# Generated at 2022-06-14 15:42:24.399452
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import patch
    from io import BytesIO
    from .test_downloader import FakeYDL
    from .http import HTTPDownloader
    # noinspection PyUnresolvedReferences
    from ..extractor import gen_extractors

    def fake_download_fragment(ctx, frag_url, info_dict, headers=None, test=False):
        frag_content = b'test data'
        if test:
            frag_content = frag_content[:10]
        return True, frag_content

    with patch('youtube_dl.downloader.common.HlsFD._download_fragment') as mock_download_fragment:
        mock_download_fragment.side_effect = fake_download_fragment

# Generated at 2022-06-14 15:42:28.927947
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # These variables are for testing the HLS download only when
    # the downloaded media file is corrupted
    from .external import FFmpegFD
    from ..downloader import DownloadContext
    from ..downloader.common import FileDownloader
    from ..downloader.http import YoutubeDLHandler
    from ..downloader.http.http_requests import ytdl_urlopen
    from ..utils import encode_bytes, encodeFilename
    from ..compat import (
        compat_urllib_request,
        compat_urllib_response,
        compat_urllib_error,
    )
    class HlsFDCorruptTest(HlsFD):
        def _download_fragment(self, ctx, url, info_dict, headers):
            download_context = DownloadContext(url, info_dict, headers)
            download_context.params

# Generated at 2022-06-14 15:42:39.204226
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import ytdl
    d = ytdl({'hlsnative_prefer_native': True, 'prefer_free_formats': True})
    # non-existent url to avoid premature downloading
    # https://github.com/ytdl-org/youtube-dl/blob/master/tests/test_download.py
    d.add_info_extractor(HlsFD.ie_key())
    info = d.extract_info('https://www.example.com/hls.m3u8', download=True)
    assert info['_type'] == 'url_transparent'
    assert info['url'] == 'https://www.example.com/hls.m3u8'
    assert info['protocol'] == 'm3u8'
    assert info['ext'] == 'mp4'

# Generated at 2022-06-14 15:42:46.795397
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    from .test_download import FakeYDL

    class MockResponse(object):
        def __init__(self, content):
            self.content = content
            self.headers = {"content-length": len(content)}


    class TestHlsFD(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            '''
            Setup a FakeYDL object to be used with the tests.
            '''
            cls.ydl = FakeYDL()

        def test_real_download(self):
            '''
            Test real_download() method of class HlsFD.
            '''
            import os
            import tempfile
            import shutil
            import binascii
            import base64
            import hashlib
            import json

            # Set up testing params


# Generated at 2022-06-14 15:43:26.523351
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .http import HttpFD
    from .downloader import Downloader
    from .http import HEADRequest
    from .downloader import FakeYdl
    from .external import ExternalFD
    from .subtitles import SubtitlesFD
    from .fragment import FragmentFD
    from .dash import DashSegmentsFD
    from .dash import IsmaFD
    import youtube_dl

    ydl = youtube_dl.YoutubeDL({'simulate': True, 'quiet': True, 'skip_download': True})

# Generated at 2022-06-14 15:43:37.291978
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .downloader import Downloader
    from .external import ExternalFD
    from .fragment import FragmentFD

    # Test if it is an instance of FragmentFD
    ydl = Downloader({})
    info_dict = {
        'url': 'some_url',
        'is_live': False,
    }
    fd = HlsFD(ydl, {})
    assert isinstance(fd, FragmentFD)
    assert isinstance(fd, ExternalFD)

    # Test if can_download is False when is_live is True
    info_dict['is_live'] = True
    assert not HlsFD.can_download('', info_dict)

    # Test if can_download is False when another unsupported feature is detected
    info_dict['is_live'] = False
    assert not HlsFD.can_download

# Generated at 2022-06-14 15:43:44.061804
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import _common_test_download, ytdl
    from .extractor.common import InfoExtractor
    _common_test_download(
        [], HlsFD, ytdl,
        'https://devimages.apple.com.edgekey.net/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8',
        'HlsFD', InfoExtractor)

# Generated at 2022-06-14 15:43:52.482590
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import youtube_dl.YoutubeDL
    import youtube_dl.extractor.common
    import os.path


# Generated at 2022-06-14 15:44:04.058332
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import YoutubeIE
    from ..utils import match_filter_func

    def test_prepare_url(self, url):
        return url

    YoutubeIE._prepare_url = test_prepare_url

    test_cases = [
        # 'url': url to download
        # 'expected': expected result, True for success and False for failure
        {'url': 'http://www.youtube.com/watch?v=BaW_jenozKc', 'expected': True},
    ]
    for test_case in test_cases:
        test_ie = YoutubeIE(ydl=None, params={})
        with test_ie:
            info = test_ie.extract(test_case['url'])
            result = HlsFD.can_download(info['url'], info)

# Generated at 2022-06-14 15:44:13.401559
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import shutil
    import tempfile
    import unittest
    from .test_utils import download_video
    from . import YoutubeDL

    def _m3u8_to_m3u8(url, data):
        return data, {'noplaylist': False}

    def _m3u8_to_ts(url, data):
        return data.replace('#EXT-X-MEDIA-SEQUENCE:0\n', '')

    def _m3u8_to_key_ts(url, data):
        return data.replace('#EXT-X-KEY:METHOD=NONE\n', '').replace('#EXT-X-KEY:METHOD=AES-128\n', '')


# Generated at 2022-06-14 15:44:21.495297
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import io
    from .test_downloader import TestFD
    from .fragment import FragmentFD
    from .external import FFmpegFD
    from .external import aes128
    from .file import FileFD
    from .dash import DashSegmentsFD
    from .dash import DashManifestFD
    from .rtmp import RtmpSegmentsFD
    from .rtmp import RtmpManifestFD

    assert HlsFD in (HlsFD, FragmentFD, TestFD)
    assert DashSegmentsFD in (DashSegmentsFD, FragmentFD, TestFD)
    assert DashManifestFD in (DashManifestFD, FileFD, TestFD)
    assert RtmpSegmentsFD in (RtmpSegmentsFD, FragmentFD, TestFD)

# Generated at 2022-06-14 15:44:24.060212
# Unit test for constructor of class HlsFD
def test_HlsFD():
    hls = HlsFD(None, {'format': 'test'})
    assert hls.FD_NAME == 'test'

test_HlsFD()

# Generated at 2022-06-14 15:44:24.618092
# Unit test for constructor of class HlsFD
def test_HlsFD():
    pass


# Generated at 2022-06-14 15:44:35.122082
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import shutil
    import tempfile
    import unittest
    from .mock import MockYDL

    def assert_not_raises(self, func, *args, **kwargs):
        def do_assert():
            func(*args, **kwargs)
        return self.assertTrue(do_assert())

    class _HlsFDTestCase(unittest.TestCase):
        _LOCAL_MANIFEST_URI = 'http://localhost/man.m3u8'
        _LOCAL_MANIFEST_URI_WITH_PARAM = 'http://localhost/man.m3u8?param=value'

# Generated at 2022-06-14 15:45:53.673170
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import shutil
    import platform
    from urlparse import urlparse
    from ..YoutubeDL import FileDownloader
    from ..utils import encodeFilename

    def _run_test(video_id, expected_file_contents, expected_file_size=None):
        """ Runs a test on the method that downloads HLS manifests. """
        temp_dir = tempfile.mkdtemp(prefix='ytdl-test-hls-native-')

# Generated at 2022-06-14 15:45:59.457341
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .downloader import YoutubeDL

    def _hook(d):
        if d['status'] == 'finished':
            raise YoutubeDLHandlerExit

    ydl = YoutubeDL({'quiet': True})
    ydl.add_progress_hook(_hook)

    m = HlsFD(ydl, {})
    test_url = 'https://sample-videos.com/hls/hls-frag-aes.m3u8'

    # Test that the class constructor doesn't raise an exception
    m.real_download('test', {'url': test_url})


# Generated at 2022-06-14 15:46:05.779083
# Unit test for constructor of class HlsFD
def test_HlsFD():
    '''
    This function unit tests the constructor of HlsFD
    '''
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor

    ie = InfoExtractor()
    ie.set_downloader(YoutubeDL(dict(hls_prefer_native=True)))
    ie.download = lambda *args, **kargs: None

    try:
        ie.test()
    except AttributeError:
        pass

# Generated at 2022-06-14 15:46:14.001886
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..utils import boost_test_runner

    class MyInfoExtractor(InfoExtractor):
        def _real_extract(self, url):
            pass

    url = ''
    MyInfoExtractor._download_webpage = lambda _, url, *args, **kargs: (url, None)
    ie = MyInfoExtractor({})
    ie.params['test'] = True
    ie._downloader.params['test'] = True

    # Case 1: Basic download
    m3u8_data = (
        '#EXTM3U\n'
        '#EXTINF:2\n'
        'frag1.ts'
        '#EXTINF:2\n'
        'frag2.ts'
    )
    ie._download_webpage

# Generated at 2022-06-14 15:46:22.840064
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..downloader import FakeYDL
    from .fragment import test_FragmentFD_download

    # An m3u8 playlist with only one fragment
    frag_manifest = '''
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:4
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-PLAYLIST-TYPE:VOD
#EXTINF:4.000000,
test_frag.ts
#EXT-X-ENDLIST
'''

    # An m3u8 playlist with only one AES-128 encrypted fragment

# Generated at 2022-06-14 15:46:27.647288
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    HlsFD.can_download('', {})
    HlsFD.can_download(
        '#EXT-X-KEY:METHOD=AES-128',
        {'_decryption_key_url': 'http://example.com/key.bin'},
    )
    HlsFD.can_download(
        '#EXT-X-KEY:METHOD=AES-128\n#EXT-X-BYTERANGE:16@0',
        {'_decryption_key_url': 'http://example.com/key.bin'},
    )

# Generated at 2022-06-14 15:46:33.155764
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import functools, json, os, random, shutil, tempfile, unittest
    import youtube_dl.extractor.common

    _download_fragment = HlsFD._download_fragment
    _decrypt_fragment = HlsFD._decrypt_fragment
    _append_fragment = HlsFD._append_fragment
    _finish_frag_download = HlsFD._finish_frag_download
    _prepare_url = HlsFD._prepare_url

    def _append_fragment(ctx, frag_content):
        self._test_frag_contents += frag_content


# Generated at 2022-06-14 15:46:41.417691
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import pprint
    import sys
    import tempfile
    import subprocess

    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tests'))
    from test_downloads import _do_test_downloads
    from test_download import (
        _download_test_data,
        _pull_test_data,
        _test_download_general,
    )

    def test_hls_fd(data, params, width, height, expected_filesize):
        info_dict = {}
        fd = HlsFD(data['ydl'], params)
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = os.path.join(temp_dir, 'tmpfile.mp4')

# Generated at 2022-06-14 15:46:50.836538
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from .http import HttpFD

    def test_can_download(url, expected, is_live_stream=None, extra_param_to_segment_url=None, _decryption_key_url=None):
        info_dict = dict(url=url)
        if is_live_stream is not None:
            info_dict['is_live'] = is_live_stream
        if extra_param_to_segment_url is not None:
            info_dict['extra_param_to_segment_url'] = extra_param_to_segment_url
        if _decryption_key_url is not None:
            info_dict['_decryption_key_url'] = _decryption_key_url
        # We don't actually use the HlsFD class here but we do want to test
        # the `can

# Generated at 2022-06-14 15:46:58.886796
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    Unit test for method real_download of class HlsFD
    """

    # Import required modules
    import os
    import shutil
    import tempfile
    import threading
    import time

    # Create a temporary directory
    d = tempfile.mkdtemp(prefix='youtube-dl.test.')

    # Unit test for method real_download of class HlsFD
    # Assumptions for this test:
    # - The stream is available in HLS with quality 0 and at least one more quality
    # - The stream is in a constant duration
    def real_download_test_thread(test_url, params):
        """
        Function that runs method real_download of class HlsFD in a separate thread with the provided URL and params
        """

        # Create the HlsFD class