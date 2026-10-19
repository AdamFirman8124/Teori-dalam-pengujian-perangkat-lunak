

# Generated at 2022-06-14 15:37:50.205615
# Unit test for constructor of class HlsFD
def test_HlsFD():
    test_url = 'https://www.youtube.com/watch?v=pMxOmHV7p8g'
    entry = {'id': 'pMxOmHV7p8g', 'url': test_url, 'http_headers': {}}
    mdl = HlsFD(None, None)
    assert mdl.can_download(entry)
    assert mdl.real_download(None, entry) != False


# Generated at 2022-06-14 15:38:03.219686
# Unit test for constructor of class HlsFD
def test_HlsFD():

    # Create object
    hls_fd = HlsFD({})

    # Set members
    hls_fd.params = []
    hls_fd.test = True
    hls_fd.max_fragment_size = 524288
    hls_fd.progress_hooks = []
    hls_fd.frag_filename = 'fragment'

    # Test methods
    hls_fd.to_screen()
    hls_fd.report_error()
    hls_fd.report_warning()
    hls_fd.report_retry_fragment()
    hls_fd.report_skip_fragment()
    hls_fd.real_download()

    # Test inner classes
    class InnerError(Exception):
        pass
    hls_fd.report_error('Message')

# Generated at 2022-06-14 15:38:14.352882
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import tempfile
    import os
    from .utils import FakeYDL
    from .downloader import ExternalFD

    # Test: no ffmpeg
    ExternalFD._available = False
    hls_fd = HlsFD(FakeYDL(), {})
    hls_fd.params = {'test': True}

# Generated at 2022-06-14 15:38:27.571515
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import youtube_dl.extractor.common
    import os
    import sys
    import random
    import tempfile
    import shutil
    import time
    import filecmp
    import atexit
    import youtube_dl.utils
    import youtube_dl.downloader.multi_fragment
    import youtube_dl.downloader.fragment
    import youtube_dl.downloader.http
    import youtube_dl.FileDownloader
    import youtube_dl.cache
    import youtube_dl.postprocessor.ffmpeg

    test_dir = tempfile.mkdtemp()
    atexit.register(lambda: shutil.rmtree(test_dir))

    extractor = youtube_dl.extractor.common.KalturaIE('test')
    ext = youtube_dl.extractor.common.InfoExtractor(extractor)

   

# Generated at 2022-06-14 15:38:37.990054
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE\n#EXTINF:10,\nfoo.ts\n#EXTINF:10,\nbar.ts\n', {'url': 'http://example.com/foo.m3u8'})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128\n#EXTINF:10,\nfoo.ts\n#EXTINF:10,\nbar.ts\n', {'url': 'http://example.com/foo.m3u8'})

# Generated at 2022-06-14 15:38:50.825644
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..utils import CommandExecutionError

    import sys
    import os.path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from YoutubeDL import YoutubeDL

    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    info = ydl.extract_info(
        'https://www.youtube.com/watch?v=smv5nQ2zIcw', download=False)
    x = HlsFD()
    assert x.can_download(info['formats'][-1]['manifest_url'], info)

    ydl = YoutubeDL()
    ydl.add_default_info_extractors()

# Generated at 2022-06-14 15:39:02.049547
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import re

    from .external import ExternalFD
    from .utils import urlopen
    from .fragment import FragmentFD
    from .geo_restricted_video import GeoRestrictedVideoFD
    from .dash import DashSegmentsFD
    from .hds import HdsFD

    from ..extractor import YoutubeIE

    from ..utils import (
        remove_start,
        decode_packed_codes,
        orderedSet,
        float_or_none,
        int_or_none,
        url_basename,
    )
    from ..compat import (
        compat_struct_pack,
        compat_urlparse,
    )


# Generated at 2022-06-14 15:39:08.941866
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..__main__ import YoutubeDL
    ydl = YoutubeDL({})

    # Good m3u8 file
    test = r"""
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:5
#EXT-X-STREAM-INF:BANDWIDTH=100
http://www.example.com/low.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=200
http://www.example.com/mid.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=300
http://www.example.com/hi.m3u8
#EXT-X-ENDLIST
"""

# Generated at 2022-06-14 15:39:17.290155
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import MockYtdl
    youtube_dl = MockYtdl()
    hls_fd = HlsFD(youtube_dl, {'test': True})
    return hls_fd.real_download(
        'filename.mp4',
        {
            'url': 'url_of_manifest',
            'http_headers': {
                'foo': 'bar',
                'range': 'bytes=0-10',
            },
        }
    )



# Generated at 2022-06-14 15:39:26.098902
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    if sys.version_info < (3, 6):
        return
    from .test import get_test_data
    from ..utils import determine_protocol
    from ..extractor.common import InfoExtractor
    from ..compat import compat_HTTPError
    from .HttpFD import _test_read_content
    from .external import FFmpegFD

    ie = InfoExtractor(
        downloader=None,
        params={
            'test': True,
            'format': 'bestaudio',
            'skip_download': True,
            'noplaylist': True,
        },
    )
    ie._downloader = None

    def _test_download_content(content):
        def test_hook(status):
            pass


# Generated at 2022-06-14 15:39:47.560464
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    # Test encrypted streams
    def can_download_enc(method):
        s = '#EXT-X-KEY:METHOD=%s' % method
        return HlsFD.can_download(s, {})

    assert not can_download_enc('AES-128')
    assert can_download_enc('NONE')

    # Test media initialization
    def can_download_map(map_url):
        s = '#EXT-X-MAP:URI="%s"' % map_url
        return HlsFD.can_download(s, {})

    assert not can_download_map(None)

    # Test live streams
    def can_download_live(seq):
        s = '#EXT-X-MEDIA-SEQUENCE:%s' % seq
        return HlsFD.can_download(s, {})



# Generated at 2022-06-14 15:39:51.916086
# Unit test for constructor of class HlsFD
def test_HlsFD():
    print(HlsFD.can_download('#EXTM3U\n#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=836280,RESOLUTION=640x360', {'url': '#EXTM3U'}))

# test_HlsFD()

# Generated at 2022-06-14 15:39:58.345670
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from urllib.request import urlopen
    import tempfile

    # Download a m3u8 file that contains a segment encrypted with AES-128
    # and another segment in byte range form
    # Also, the hlsnative extractor doesn't support live streams.
    # Let's check the live stream detection.
    url = 'https://devstreaming-cdn.apple.com/videos/wwdc/2015/502rzrj3q2nb/502/hls_vod_mvp.m3u8'

    # Get the manifest file
    manifest = urlopen(url).read().decode('utf-8', 'ignore')

    # Verify the real_download method can appropriately handle this manifest
    info_dict = {
        'url': url,
        'http_headers': {},
    }
    assert HlsFD.can_

# Generated at 2022-06-14 15:40:06.596279
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest

    from . import FakeYDL
    from .extractor.common import InfoExtractor

    class HlsFDFakeYDL(FakeYDL):
        def urlopen(self, url):
            url_h = super(HlsFDFakeYDL, self).urlopen(url)
            if re.match(r'.*\.ts', url):
                return self.filehandle('test.ts', urlh=url_h)
            return url_h

    class MockIE(InfoExtractor):
        def _get_info_from_url(self, url):
            return {'id': 'foo', 'ext': 'ts', 'url': url}


# Generated at 2022-06-14 15:40:19.674254
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    from .test_fragment import _download_fragment
    from .test_fragment import _append_fragment

    class DummyYDL(object):
        def __init__(self):
            self.prefer_free_formats = False

        def urlopen(self, url):
            class MockUrlOpen(object):
                def __init__(self, url):
                    self.url = url
            return MockUrlOpen(url)

    class HlsFDTest(unittest.TestCase):
        class DummyParam(object):
            def __init__(self, test=False, fragment_retries=0):
                self.test = test
                self.fragment_retries = fragment_retries


# Generated at 2022-06-14 15:40:29.816485
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..compat import compat_str
    from ..downloader import Downloader
    from .common import FileDownloader
    from .http import HttpFD
    from .external import FFmpegFD
    from .dash import DashSegmentsFD
    from .f4m import F4mFD
    from .fragment import FragmentFD

    class FakeHlsIE(InfoExtractor):

        IE_NAME = 'hlsnative'
        _VALID_URL = r'https?://hls-media-server.com/.+?\.m3u8'

        def _download_webpage(self, url, video_id, note, errnote):
            return 'id="%s"' % video_id

        def _real_extract(self, url):
            return self.url_result

# Generated at 2022-06-14 15:40:36.765446
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import youtube_dl
    import os.path
    this_dir = os.path.dirname(os.path.realpath(__file__))
    manifest_file = os.path.join(this_dir, "hls_manifest.m3u8")
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    info_dict = {}
    fd = HlsFD(ydl, {})
    with open(manifest_file, 'r') as f:
        s = f.read()
        fd.download(s, info_dict)

# Generated at 2022-06-14 15:40:47.912894
# Unit test for constructor of class HlsFD
def test_HlsFD():
    '''
    Test case for constructor of class HlsFD.
    '''
    ydl = DummyYdl()
    params = DummyParams()

    video_url = 'http://www.youtube.com/watch?v=PGNiXGX2nLU&feature=g-high-rec'

# Generated at 2022-06-14 15:40:53.332913
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import ydl_test_support
    ydl_test_support.create_and_cleanup_downloader('https://developer.apple.com/streaming/examples/advanced.m3u8?r=1528128637289')


if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:41:01.980213
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import json
    import os
    import unittest
    import youtube_dl.extractor.common as common

    from .test_downloader import (
        FakeYDL,
        FakeHttpResponse,
        FakeFile,
        get_testdata_file)

    segment_data = b'This is a segment of the test video'
    segment_data_len = len(segment_data)
    segment_data_half = segment_data[:segment_data_len // 2]
    segment_data_partial_len = len(segment_data_half)

    def get_segment_url(segment_num):
        return 'http://example.com/segment_%d.ts' % segment_num


# Generated at 2022-06-14 15:41:38.938161
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('EXT-X-BYTERANGE', {
        'url': 'http://example.com', 'is_live': False})
    assert HlsFD.can_download('#EXT-X-BYTERANGE', {
        'url': 'http://example.com', 'is_live': False})
    assert HlsFD.can_download('#EXT-X-KEY', {
        'url': 'http://example.com', 'is_live': False})
    assert HlsFD.can_download('#EXT-X-STREAM-INF', {
        'url': 'http://example.com', 'is_live': False})


# Generated at 2022-06-14 15:41:41.450419
# Unit test for constructor of class HlsFD
def test_HlsFD():
    hf = HlsFD({}, {})
    assert hf.FD_NAME == "hlsnative"


if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:41:50.278415
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .hls import HlsFD

# Generated at 2022-06-14 15:42:00.822633
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os.path
    import tempfile
    import sys
    from .external import ExternalFD
    from ..extractor import gen_extractors
    from ..cache import Cache
    from compat import compat_etree_fromstring

    with tempfile.NamedTemporaryFile(suffix='.m3u8') as f:
        test_url = 'https://raw.githubusercontent.com/ytdl-org/youtube-dl/master/youtube_dl/extractor/test_files/test.m3u8'
        test_filename = 'test.mp4'
        test_file_size = 1512

# Generated at 2022-06-14 15:42:12.638793
# Unit test for constructor of class HlsFD
def test_HlsFD():
    params = {
        '-f':'18',
        'skip_download':True,
        'format':'mp4',
        'noplaylist':True,
    }
    ydl = YoutubeDL(params)

# Generated at 2022-06-14 15:42:24.223839
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    assert HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:1\n'
        '#EXTINF:1,some-title\n'
        'http://some-url/playlist.m3u8',
        {'url': 'foo', 'is_live': False})
    # Not live

# Generated at 2022-06-14 15:42:32.393729
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import unittest
    from . import FakeYDL
    from .test_downloader import TDownloaderTest
    from .test_downloader import TDownloaderUnitTest, TDownloaderIntegrationTest
    from .test_downloader import gettestcases_HlsFD

    class TestHlsFD(unittest.TestCase):

        HLS_URL = 'https://example.com/hls/'

        def test_real_download(self):
            # pylint: disable=no-member
            # gettestcases_HlsFD sets self.HLS_URL
            test_cases = gettestcases_HlsFD(self.HLS_URL)


# Generated at 2022-06-14 15:42:33.445784
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD(None, "unit test")

# Generated at 2022-06-14 15:42:43.960338
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import youtube_dl.YoutubeDL
    import youtube_dl.extractor.http.hls
    # test_hlsnative_extract_functions.py
    # Tests get_formats function by trying to extract formats from HLS streams
    # supported by hlsnative.
    ydl = youtube_dl.YoutubeDL({'hls_prefer_native': True})
    ydl.add_info_extractor(youtube_dl.extractor.http.hls.HlsIE())


# Generated at 2022-06-14 15:42:50.624930
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """Test constructor and basic methods (IE internal) of class HlsFD"""
    from .test import get_test_data_submodule

    test_data = get_test_data_submodule('HlsFD')


# Generated at 2022-06-14 15:43:51.999949
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .testutils import FakeYDL, FakeHttpDl, download_urls
    from .testutils import DummyFD
    from ..downloader.common import FileDownloader
    from ..downloader.external_downloader import YoutubeDL

    ydl = FakeYDL()
    dl = FileDownloader(ydl)
    dl.params['test'] = True
    dl.add_info_extractor(DummyFD(ydl, {'protocol': 'hls'}))
    dl.add_info_extractor(DummyFD(ydl, {'protocol': 'hls'}))
    dl.add_info_extractor(DummyFD(ydl, {'protocol': 'hls'}))

# Generated at 2022-06-14 15:44:03.653056
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .fake_downloader import FakeFD

    progress_hooks = [lambda x: None]
    params = {'test': True, 'fragment_retries': 0, 'skip_unavailable_fragments': True}
    ydl = None
    hls_fd = HlsFD(ydl, params)
    for hook in progress_hooks:
        hls_fd.add_progress_hook(hook)

    assert hls_fd.FD_NAME == 'hlsnative'
    assert hls_fd.can_download == HlsFD.can_download

    assert hls_fd.can_download(b'', {})

    assert hls_fd.can_download(b'#EXT-X-KEY:METHOD=NONE\n', {})

# Generated at 2022-06-14 15:44:06.254318
# Unit test for constructor of class HlsFD
def test_HlsFD():
    hlsfd = HlsFD(None, {})
    assert hlsfd
    assert hlsfd.params == {}
    assert hlsfd.ydl == None
    assert hlsfd._progress_hooks == []

# Generated at 2022-06-14 15:44:13.085356
# Unit test for constructor of class HlsFD

# Generated at 2022-06-14 15:44:24.442255
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import YoutubeDL
    from ..extractor import youtube

    def hooks_wrapper(hooks):
        def _hooks(d):
            if d.get('status', None) == 'finished':
                hooks.append(d)

        return _hooks

    hooks = []
    dl = YoutubeDL({
        'outtmpl': '%(id)s',
        'skip_download': True,
        'format': 'best[protocol=m3u8_native]/best',
        'hls_prefer_native': True,
        'hls_prefer_ffmpeg': False,
        'progress_hooks': [hooks_wrapper(hooks)]
    })

    dl.add_info_extractor(youtube.YoutubeIE())

# Generated at 2022-06-14 15:44:34.795187
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import youtube_dl.FileDownloader
    frag_url = 'http://example.com/frag.ts'
    frag_content = b'content'
    sample_manifest = (
        '#EXTM3U\n'
        '#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXTINF:1.0\n'
        + frag_url + '\n'
        '#EXT-X-ENDLIST\n')
    def urlopen(frag_url):
        assert frag_url == frag_url
        return compat_urllib_request.urlopen(compat_urllib_request.Request(frag_url)).read()

    ydl = youtube_dl.FileDownloader({'format': 'best'})
    ydl.add_progress_

# Generated at 2022-06-14 15:44:46.112234
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # Test download of encrypted HLS with AES-128
    import tempfile


# Generated at 2022-06-14 15:44:55.265961
# Unit test for constructor of class HlsFD
def test_HlsFD():
    info_dict = {
        'url': 'http://test.test/test.m3u8',
        'http_headers': {'User-Agent': 'Test'},
        'fragment_base_url': 'http://test.test/test-fragment.m4s',
        '_decryption_key_url': 'http://test.test/test-decryption-key',
        '_decryption_iv': 'abcdabcdabcdabcdabcdabcdabcdabcd',
        'extra_param_to_segment_url': 'param1=1&param2=2',
        'is_live': True,
        'ytdl_options': {},
    }

# Generated at 2022-06-14 15:45:03.305323
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:45:04.896340
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    pass
