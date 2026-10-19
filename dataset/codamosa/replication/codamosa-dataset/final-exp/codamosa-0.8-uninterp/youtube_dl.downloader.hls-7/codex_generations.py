

# Generated at 2022-06-14 15:37:56.657717
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import unittest
    class TestHlsFD(unittest.TestCase):
        def setUp(self):
            from ..YoutubeDL import YoutubeDL
            self.manifest_url = ''
            self.ydl = YoutubeDL({'noprogress': True})


# Generated at 2022-06-14 15:37:57.420452
# Unit test for constructor of class HlsFD
def test_HlsFD():
    pass

# Generated at 2022-06-14 15:38:02.011937
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    ydl = FakeYDL()
    params = {}
    hls_params = {}
    if __name__ == '__main__':
        hls_params['test'] = True
        ydl.params['nooverwrites'] = True
    hls_params['fragment_retries'] = 0
    hls_params['skip_unavailable_fragments'] = True

    hls_params['fragment_retries'] = 0
    hls_params['skip_unavailable_fragments'] = True
    url = 'http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8'
    info_dict = {'url': url}
    hls_fd = HlsFD(ydl, params)

# Generated at 2022-06-14 15:38:10.750492
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..postprocessor.ffmpeg import FFmpegPostProcessor
    hlsFD = HlsFD(None, {})
    assert hlsFD.params == {}
    assert hlsFD.url is None
    assert hlsFD.ydl is None
    assert not hlsFD.finished
    assert not hlsFD.available
    assert len(hlsFD.fragment_retries) == 0
    assert hlsFD.complete_frags_downloaded == 0
    assert hlsFD.postprocessors == [FFmpegPostProcessor(hlsFD)]
    assert isinstance(hlsFD.pp, FFmpegPostProcessor)

    test_url = 'test_url'
    test_params = {'test_param': 'test_param_val'}


# Generated at 2022-06-14 15:38:24.337178
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Unit test for constructor of class HlsFD """
    res = HlsFD.can_download('#EXTM3U', {})
    assert res == False

    res = HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128', {})
    assert res == True

    res = HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128\n#EXT-X-BYTERANGE', {})
    assert res == False

    res = HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NON_EXISTENT', {})
    assert res == True


# Generated at 2022-06-14 15:38:35.913737
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """Test that HlsFD._download_fragment returns the correct data."""
    from .testutils import FakeYDL, BASE_URL_HLS_VIDEO, BASE_URL_HLS_AUDIO
    from .testutils import mocked_http_server, mocked_http_downloads

    def create_and_run_hlsfd_fd(url, extra_param_to_segment_url=None, decryption_key_url=None):
        ydl = FakeYDL()
        ydl.add_default_info_extractors()
        ydl.add_info_extractor(HlsFD())
        ydl.params['skip_download'] = True
        ydl.params['format'] = '640x480'

# Generated at 2022-06-14 15:38:38.402282
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from . import YoutubeDL
    ydl = YoutubeDL({'quiet': True})
    fd = HlsFD(ydl, {})

# Generated at 2022-06-14 15:38:51.145758
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .extractor.common import InfoExtractor
    from .downloader import Downloader
    from .utils import HeadRequest

    class DummyIE(InfoExtractor):
        def _real_initialize(self):
            self.test_kwargs = self._downloader.params.get('test_kwargs', {})

        def _real_extract(self, url):
            return {'id': 'test video'}

    args = ['--test', '--test-fragments']
    ie = DummyIE(Downloader(params=dict(nooverwrites=True, test=True)), 'http://dummy/')

    # Unencrypted playlist
    dl = HlsFD(ie._downloader, ie.test_kwargs)

# Generated at 2022-06-14 15:38:58.041105
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """Initialize instance of the HlsFD class"""

    import youtube_dl.YoutubeDL
    import tempfile

    ydl = youtube_dl.YoutubeDL({
        'quiet': True,
        'skip_download': True,
        'outtmpl': tempfile.mkstemp()[1],
    })
    HlsFD(ydl, {})

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:39:06.768640
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:39:29.208957
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    def check_can_download(url, expected):
        manifest = ''.join(open(url, 'r').readlines()).strip()
        print(url, HlsFD.can_download(manifest, {}) == expected)

    check_can_download('./test/manifests/hlsnative/live.m3u8', False)
    check_can_download('./test/manifests/hlsnative/vod.m3u8', True)
    check_can_download('./test/manifests/hlsnative/aes128.m3u8', True)
    check_can_download('./test/manifests/hlsnative/byte-range.m3u8', True)

# Generated at 2022-06-14 15:39:38.079005
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors
    from ..downloader import gen_ydl
    from ..utils import DateRange

    test_manifest_url = 'http://test.com/x.m3u8'
    ydl = gen_ydl()
    xlist = gen_extractors(ydl)
    HlsFD(ydl, {}, xlist[0].ie_key(), test_manifest_url, 'fragment.mp4')

    assert(not HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {}))
    assert(HlsFD.can_download('#EXT-X-KEY:METHOD=AES-128', {}))

# Generated at 2022-06-14 15:39:41.060537
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    HlsFD('https://example.com/manifest.m3u8', ydl)

# Generated at 2022-06-14 15:39:52.003517
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .external import FFmpegFD, FFmpegPostProcessor, FFmpegMetadataPP

    def _downloader_get_info_dict(url, http_headers=None, expected_status=None,
                       status_forcelist=None, query=None, req_checker=None,
                       extra_info_dict=None, extra_processors=None):
        self = HlsFD(FFmpegFD())

# Generated at 2022-06-14 15:39:53.539563
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    return HlsFD.real_download(HlsFD, 'test-filename', {'url': 'test-url'})

# Generated at 2022-06-14 15:40:03.811098
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import io
    import tempfile
    import re
    import functools
    import pytest
    from collections import namedtuple

    from .common import FakeYDL, FakeInfoDict


# Generated at 2022-06-14 15:40:17.025102
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import YoutubeDL
    ydl = YoutubeDL({'simulate': True})

    # Test: invalid download
    class InvalidHlsFD(HlsFD):
        def _prepare_and_start_frag_download(self, ctx):
            assert ctx.get('total_frags') == 4
            assert ctx.get('ad_frags') == 0
            assert ctx.get('filename') != ''

        def _append_fragments(self, ctx, content):
            assert content is None
            assert ctx.get('fragment_index') == 1

            ctx.update({
                'fragment_index': 2,
            })

        def _finish_frag_download(self, ctx):
            assert ctx.get('total_frags') == 4

# Generated at 2022-06-14 15:40:28.252767
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..extractor.generic import GenericIE
    from ..downloader.common import FileDownloader
    from ..utils import encodeFilename, prepend_extension
    url = 'https://tm.video.gqdns.com:7000/Trailers/2012/1080p/avatar-tlr2_h1080p.mov.m3u8?b=1700&id=5025&e=1549677137&h=fff9244e9b8b84d0e2aa678c9edb5e5e'

# Generated at 2022-06-14 15:40:37.521039
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import unittest
    import shutil
    from .test_download import FakeYDL
    from .test_HlsFD_real_download1 import (
        mock_m3u8_urlopen,
        mock_urlopen,
        M3U8_MANIFEST
    )

    @unittest.skipUnless(can_decrypt_frag, 'cannot decrypt HLS fragments')
    class TestHlsFD(unittest.TestCase):
      def setUp(self):
        self.tempdir = tempfile.mkdtemp(suffix='youtube-dl-test')
        self.ydl = FakeYDL()
        self.ydl.params['quiet'] = True
        self.fd = HlsFD(self.ydl, self.ydl.params)


# Generated at 2022-06-14 15:40:40.870410
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..extractor import gen_extractors
    for ie in gen_extractors():
        if ie.ie_key() == 'hlsnative':
            return ie.can_download

# Generated at 2022-06-14 15:41:19.946138
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    class FakeHlsExtractor(InfoExtractor):
        def __init__(self, ie_params, hls_url):
            self._ie_params = ie_params  # Get the video options
            self.hls_url = hls_url

        def extract(self, url):
            ie = HlsFD(self._ie_params, {'url': self.hls_url, 'is_live': False})
            ie.real_download('', {})

    FakeHlsExtractor({}, 'https://example.com/hls').extract('https://example.com/video')

# Generated at 2022-06-14 15:41:29.479897
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..test.test_downloads import fake_info_dict_for_test
    import os
    import shutil
    import tempfile
    filename = None
    try:
        with tempfile.TemporaryDirectory() as tmp_path:
            filename = os.path.join(tmp_path, 'output.ts')
            fd = HlsFD(None, {'outtmpl': filename, 'test': True})
            success = fd.real_download(filename, fake_info_dict_for_test())
            assert success
            assert os.path.getsize(filename) > 0
    finally:
        if filename and os.path.exists(filename):
            shutil.rmtree(os.path.dirname(filename))

if __name__ == '__main__':
    test_HlsFD_real_

# Generated at 2022-06-14 15:41:39.735660
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import re
    import tempfile
    import shutil
    import subprocess
    import sys

    import youtube_dl.extractor
    import youtube_dl.downloader

    def _get_file_size(filename):
        return (
            os.stat(filename).st_size,
            subprocess.check_output(['sha1sum', filename]).split(None, 1)[0]
        )

    def _test_HlsFD_real_download(manifest_content, expected_output_filename, expected_output_size, expected_output_sha1):
        (out_fd, out_tmp_filename) = tempfile.mkstemp(suffix='.ytdl-tmp')

# Generated at 2022-06-14 15:41:44.371616
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors
    ydl = gen_extractors()['youtube']
    hls_fd = HlsFD(ydl, {'quiet': True})
    # @TODO: Implement proper test.
    # Compare expected files to downloaded files
    # @TODO: Write proper unit tests for each feature.
    assert hls_fd

# Generated at 2022-06-14 15:41:52.897709
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors
    from ..youtube_dl.YoutubeDL import YoutubeDL
    from .ts_dl import TsFD
    extractors = gen_extractors()
    ydl = YoutubeDL(extractors=extractors)
    try:
        # Test that HlsFD is in the extractors to be created
        test_class = next(
            x for x in ydl.extractors
            if x.IE_NAME == 'hlsnative'
        )
        # Test that HlsFD's constructor is not TsFD
        assert(test_class.__name__ != TsFD.__name__)
    except Exception as e:
        print(e)
    print('test_HlsFD: passed')

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:41:53.993180
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD

# Generated at 2022-06-14 15:42:02.788402
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import sys
    import unittest
    import unittest.mock as mock
    import tempfile
    import contextlib

    import youtube_dl.downloader.fragment

    # See https://github.com/ytdl-org/youtube-dl/pull/27660
    @contextlib.contextmanager
    def mock_can_decrypt_frag():
        real_can_decrypt_frag = youtube_dl.downloader.fragment.can_decrypt_frag
        try:
            youtube_dl.downloader.fragment.can_decrypt_frag = True
            yield
        finally:
            youtube_dl.downloader.fragment.can_decrypt_frag = real_can_decrypt_frag


# Generated at 2022-06-14 15:42:03.823912
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD(None, None)
    return True

# Generated at 2022-06-14 15:42:15.528820
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader.common import FileDownloader
    from ..extractor import common as extractor

    ydl = FileDownloader({'logger': extractor.get_ytdl_logger()})
    hlsfd = HlsFD(ydl, {'playliststart': 1, 'playlistend': 1})
    assert hlsfd.can_download('#EXTM3U', {'url': 'a'})
    assert not hlsfd.can_download('#START', {'url': 'not_m3u8'})
    assert hlsfd.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128', {'url': 'a'})

# Generated at 2022-06-14 15:42:27.014821
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..ytdl import YoutubeDL
    from .fragment import FragmentFD
    from .external import FFmpegFD

    def fake_prepare_and_start_frag_download(ctx):
        ctx['frag_content'] = []

    def fake_append_fragment(ctx, frag_content):
        ctx['frag_content'].extend(list(frag_content))

    def fake_finish_frag_download(ctx):
        ctx['frag_content'] = b''.join(ctx['frag_content'])

    def fake_report_error(message):
        raise Exception(message)

    def fake_can_download(a, b):
        return True

    ydl = YoutubeDL({})

    # Valid manifest

# Generated at 2022-06-14 15:43:43.825891
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .downloader import Downloader
    from .utils import prepend_extension
    from .extractor import gen_extractors, list_extractors
    from .cache import FileCache
    from .postprocessor import FFmpegMergerPP
    import os
    import tempfile
    import shutil

    # Load supported extractors
    gen_extractors()

    # Get the extractor for the test
    extractors = list_extractors()
    extractor = None
    for e in extractors:
        if e.IE_NAME == 'twitch:vod':
            extractor = e
            break
    assert extractor

    tmpdir = tempfile.mkdtemp(prefix='youtube-dl-hlsnative-test-')

# Generated at 2022-06-14 15:43:55.279552
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class MockYDL(object):
        def __init__(self):
            self.params = {'test': False}

        def urlopen(self, url):
            class MockUrl(object):
                def geturl(self):
                    return url
                def read(self):
                    return mock_manifest
            return MockUrl()

    class MockHlsFD(HlsFD):
        def __init__(self, ydl):
            self.ydl = ydl
            self.params = ydl.params
            self.num_downloads = 0

        def _download_fragment(self, ctx, frag_url, info_dict, headers):
            return True, mock_content

        def _prepare_url(self, info_dict, url):
            return url


# Generated at 2022-06-14 15:44:05.854735
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Test that HlsFD cannot download an encrypted stream when pycrypto is not installed
    info_dict = {
        'url': 'https://example.com',
        'player_url': 'https://example.com',
        'manifest_url': 'https://example.com',
        '_type': 'hls',
        '_decryption_key_url': 'https://example.com',
    }
    from .downloader import external_downloader
    from .downloader import FakeYdl
    ydl = FakeYdl()
    info_dict['_decription_aes_key_gen'] = 'https://example.com'
    fd = HlsFD(ydl, {})

# Generated at 2022-06-14 15:44:15.639356
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import common
    from ..downloader.external import ExternalFD
    from ..downloader.common import FileDownloader
    from ..utils import url_basename
    import os
    url = 'http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8'
    # Regular test
    params = {
        'skip_download': False,
        'skip_unavailable_fragments': True,
        'skip_unavailable_fragments_count': True,
        'outtmpl': '%(id)s.mp4'
    }
    ydl = FileDownloader(common.params)
    ydl.params.update(params)

# Generated at 2022-06-14 15:44:22.600339
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Test constructor of class HlsFD by passing empty set of values
    HlsFD(None, {})
    # Test constructor of class HlsFD by passing invalid ydl
    HlsFD('InvalidYouTubeDL', {})
    # Test constructor of class HlsFD by passing invalid params
    HlsFD(None, {'params': 'InvalidParams'})
    # Test constructor of class HlsFD by passing valid values
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    HlsFD(ydl, {})


# Generated at 2022-06-14 15:44:30.577464
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from .manifest import ManifestFD
    from .utils import get_info_extractor, set_default_opener, compat_urllib_request
    import tempfile
    import os
    import shutil
    from .utils import get_cachedir

    current_dir = os.path.dirname(os.path.abspath(__file__))

    def download_media(media_url, media_file, opener):
        request = compat_urllib_request.Request(media_url)
        with open(media_file, 'wb') as media_fd:
            media_fd.write(opener.open(request).read())

    def download_manifest(manifest_url, manifest_file, opener):
        request = compat_urllib_request.Request(manifest_url)

# Generated at 2022-06-14 15:44:34.987620
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    def can_download(man, is_live):
        info_dict= {'url': 'a', 'is_live': is_live}
        return HlsFD.can_download(man, info_dict)

    # Spotify

# Generated at 2022-06-14 15:44:46.275858
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .utils import _TEST_FILE_DUMP_FD
    from .http import HttpFD
    from .hls_playlist import HlsPlaylistFD
    from .hls_multi_bitrate import HlsMultiBitrateFD
    from .external import FFmpegFD
    from .downloader import YoutubeDL

    hls_playlist_fd = HlsPlaylistFD()
    if not hls_playlist_fd:
        raise Exception('HlsPlaylistFD is None')

    hls_multibitrate_fd = HlsMultiBitrateFD()
    if not hls_multibitrate_fd:
        raise Exception('HlsMultiBitrateFD is None')

    http_fd = HttpFD()
    if not http_fd:
        raise Exception('HttpFD is None')

    ffmpeg_fd = FF

# Generated at 2022-06-14 15:44:55.444544
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import io
    import os
    import sys
    import tempfile
    from .dest_file import temp_name
    from .file import FileFD

    # HlsFD does not support URLs with a query string. So we need to override the download method
    # and prepend a query string to the test URL.
    def _prepare_and_start_frag_download(self, ctx):
        ctx['_tempfiles_set'] = set()
        ctx['tempfiles'] = {}
        ctx['fragment_index'] = 0
        ctx['total_frags'] = 1
        ctx['ad_frags'] = 0
        ctx['frag_counter'] = 0
        ctx['skip_fragments'] = 0
        ctx['retry_fragments'] = 0

# Generated at 2022-06-14 15:45:03.435454
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import httpretty
    import tempfile
    from .test import flv_filename

    url = 'http://example.org/index.m3u8'
    media_url = 'http://example.org/segment.ts'

    def download_url(url):
        if url == url:
            return b'm3u8 data'
        elif url == media_url:
            return b'segment data'
        raise Exception('Unexpected URL %s' % url)
