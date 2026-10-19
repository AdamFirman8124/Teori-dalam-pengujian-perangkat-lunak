

# Generated at 2022-06-14 15:38:01.001096
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Basic unit tests for HlsFD """
    import sys
    import os
    import unittest

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    import youtube_dl

    # Fake class that supports the context manager protocol
    class FakeFileObject(object):
        def __init__(self):
            self.is_test_valid = False

        def write(self, data):
            self.is_test_valid = True

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    class HlsNativeTest(unittest.TestCase):
        def test_HlsFD_basic(self):
            ydl_opts = {}
            ydl = youtube_dl

# Generated at 2022-06-14 15:38:10.776238
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os, json
    import subprocess
    import youtube_dl
    from youtube_dl.utils import encodeFilename, ReadFileChunked
    from jsonschema import validate
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from threading import Thread, Event
    from time import sleep

    with open('hlsfd.schema.json', 'r', encoding='utf-8') as hlsfdSchema:
        schema = json.load(hlsfdSchema)

    def get_filesize(filename):
        return os.stat(filename).st_size

    def get_download_size(download):
        return get_filesize(download['filename'])

    def get_m3u8_info(filename):
        info = {}
        with open(filename, 'r') as m3u8:
            line

# Generated at 2022-06-14 15:38:24.337860
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """Unit test for method real_download of class HlsFD."""
    from ..extractor import gen_extractors
    from ..downloader.common import FileDownloader


# Generated at 2022-06-14 15:38:35.913002
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:38:48.730535
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import youtube_dl
    import youtube_dl.extractor
    import os
    # Reloading module is needed because we have changed constructor of class HlsFD
    # (otherwise we would have to use super() in HlsFD.__init__)
    reload(youtube_dl.downloader.fragment)
    reload(youtube_dl.downloader.external)
    reload(youtube_dl.downloader.hls)
    fd = youtube_dl.downloader.hls.HlsFD(
        youtube_dl.YoutubeDL({'hls_use_ffmpeg': 'n'}),
        {'test': True})
    if 'pycrypto' in sys.modules:
        del sys.modules['pycrypto']
    if 'Crypto' in sys.modules:
        del sys.modules['Crypto']

   

# Generated at 2022-06-14 15:38:53.245407
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:39:04.011324
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .dashsegments import DashSegmentsFD
    from .fragment import test_FragmentFD_download
    from .external import _downloader_classes
    from ..utils import update_url_query
    from ..compat import bytes_str

    class TestHlsFD(HlsFD):
        """ A mock HlsFD class used by test_HlsFD_real_download """

        def _prepare_url(self, info_dict, url):
            # Modifies the manifest url
            manifest_url_query = url + '?mocked_query'
            # Stores the manifest url in info_dict
            info_dict['manifest_url'] = manifest_url_query
            return manifest_url_query


# Generated at 2022-06-14 15:39:12.901225
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    os.chdir('ytdl')
    print('Testing YoutubeDL._real_download(HlsFD)')
    from .extractor.generic import GenericIE
    from .postprocessor import FFmpegPostProcessor
    from .compat import compat_urlparse
    from .compat import urlopen

    class FakeYDL:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.postprocessors = []
            # self.params = { 'prefix': '', 'outtmpl': '%(id)s%(ext)s', 'nooverwrites': False, 'noprogress': True, 'quiet': True, 'simulate': True, 'writedescription': False, 'writeinfojson': False, 'writeannotations

# Generated at 2022-06-14 15:39:23.691490
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import YoutubeDL

    ydl = YoutubeDL()
    ydl.params['quiet'] = True

    #https://github.com/ytdl-org/youtube-dl/issues/12696
    ydl.add_default_info_extractors()

    #https://github.com/ytdl-org/youtube-dl/issues/12584
    info_dict = ydl._extract_info(
        'http://www.nhk.or.jp/news/web_tokushu/20150202/index.html',
        download=False,
        process=False
    )

    #https://github.com/ytdl-org/youtube-dl/issues/12694
    fd = HlsFD(ydl, ydl.params)

# Generated at 2022-06-14 15:39:35.931490
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import subprocess
    import sys

    def _get_test_cmd(self):
        return ['python', '-m', __name__, '--test-hlsfd', __file__]

    HlsFD.get_test_cmd = _get_test_cmd

    if len(sys.argv) == 1 or sys.argv[1] != '--test-hlsfd':
        return

    def run_test(self, filename, hls_url):
        from .utils import DateRange
        from ..extractor import YoutubeIE
        from .external import ExternalFD

        class MockInfoDict(dict):
            pass

        self._fix_url(MockInfoDict({'url': hls_url}))


# Generated at 2022-06-14 15:40:01.444691
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import YouTube
    from ..downloader.common import FileDownloader
    import tempfile

    def test_download(self):
        with tempfile.NamedTemporaryFile(prefix='test_youtube_dl_') as temp_test_file:
            expected_data = b'Expected Data'

            info = {
                'url': 'http://example.com/index.m3u8',
                '_type': 'hls',
                '_test': self.test,
            }

# Generated at 2022-06-14 15:40:14.519246
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from .dashsegments import DashSegmentsFD
    class YDL(object):
        def report_warning(self, *args, **kargs): pass
    ydl = YDL()

    info_dict = {'url': 'http://www.example.com/playlist.m3u8', '_type': 'hls'}

    playlist_1 = '''
#EXTM3U
#EXTINF:10
http://media.example.com/segment-1.ts
#EXTINF:10,
http://media.example.com/segment-2.ts
#EXT-X-ENDLIST
'''
    assert HlsFD._can_download(playlist_1, info_dict)

    # live stream, HLS-native does not support it
    info_dict['is_live'] = True

# Generated at 2022-06-14 15:40:26.674851
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .external import FFmpegFD
    from .test import MockYDL
    from ..utils import unescapeHTML
    import os

    def _test(dl, dest, expected_name):
        filename = dl.prepare_filename(dest)
        assert os.path.basename(filename) == expected_name
        dl.download(dest)
        with open(filename, 'rb') as f:
            contents = f.read()
        assert contents == b'content\n'
        os.remove(filename)

    ydl = MockYDL()
    ydl.add_info_extractor(FFmpegFD)
    ydl.add_info_extractor(HlsFD)


# Generated at 2022-06-14 15:40:32.224126
# Unit test for constructor of class HlsFD
def test_HlsFD():
    fd = HlsFD({}, {'params': {'outtmpl': '%(id)s.%(ext)s'}})
    # Check if class HlsFD is initialized correctly
    assert fd.FD_NAME == 'hlsnative'

# Generated at 2022-06-14 15:40:38.094542
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Simple unit tests for constructor of the HlsFD class. """
    ydl = None
    params = {'test': True}

    fd = HlsFD(ydl, params)
    assert fd.params is not None
    assert fd.add_progress_hook is not None

# Generated at 2022-06-14 15:40:48.844387
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from tests.test_downloader import get_testdata_dir
    import os
    import shutil
    import tempfile
    import contextlib
    from .utils import (
        prepare_manifest,
        prepare_decryption_key,
    )
    from .m3u8 import (
        parse_playlist,
    )

    @contextlib.contextmanager
    def make_test_dir():
        tdir = tempfile.mkdtemp()
        try:
            yield tdir
        finally:
            shutil.rmtree(tdir, ignore_errors=True)


# Generated at 2022-06-14 15:40:59.501727
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import gen_extractors
    from ..utils import ExtractorError
    from .common import FakeYDL
    ydl = FakeYDL()
    info_dict = {
        'id': 'HlsFD',
        'url': 'http://playertest.longtailvideo.com/adaptive/bipbop/gear4/prog_index.m3u8',
        'http_headers': {
            'X-Test': 'foo; bar',
            'Cookie': 'TestCookie=1',
        },
    }
    ext = gen_extractors(ydl, [info_dict['url']])[0]
    hls_fd = ext._workflow[-1]
    assert hls_fd.FD_NAME == 'hlsnative'
    assert not hls_fd.real

# Generated at 2022-06-14 15:41:04.513656
# Unit test for constructor of class HlsFD
def test_HlsFD():
	ydl=Downloader()
	params={}
	url="https://github.com/ytdl-org/youtube-dl"
	ctx={"ydl":ydl,"params":params}
	fd=HlsFD(ctx,url)
	assert fd

# Generated at 2022-06-14 15:41:16.167711
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import _TEST_FILES_TEMPLATE
    from ..downloader import Downloader

    def check(manifest):
        dl = Downloader(params={})
        return HlsFD.can_download(manifest, {})

    assert check(None)
    assert check(_TEST_FILES_TEMPLATE % 'hls_variant_playlist.m3u8')
    assert check(_TEST_FILES_TEMPLATE % 'hls_aed_playlist.m3u8')
    assert check(_TEST_FILES_TEMPLATE % 'hls_ded_playlist.m3u8')
    assert check(_TEST_FILES_TEMPLATE % 'hls_vod_playlist.m3u8')

# Generated at 2022-06-14 15:41:20.874587
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import gen_extractors
    Extractor = gen_extractors()[24]
    m3u8_url = 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8'
    extractor = Extractor({'url': m3u8_url, 'http_chunk_size': 1, 'test': True})
    extractor.test()

# Generated at 2022-06-14 15:41:58.057426
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..extractor.youtube import YoutubeIE
    from ..extractor.generic import GenericIE
    from .external import FFmpegFD

    params = {
        'format': 'bestvideo[height<720]+bestaudio/best',
        'youtube_include_dash_manifest': False,
    }
    extractor = YoutubeIE(InfoExtractor('test', {}))

# Generated at 2022-06-14 15:42:05.894354
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():

    from .smil import _build_smil_formats
    from ..extractor.common import InfoExtractor
    from ..compat import StringIO

    # unit test to make sure HLS downloader is working correctly
    test_url = 'https://vodhls-akc.mediahub.sky.com/vod/smil:video/HLS/SkyMovies/StandardDefinition/MGS_DF_PC_AAC_Stereo_HLS/MGS_DF_PC_AAC_Stereo_HLS.smil/manifest-m3u8-aapl.m3u8'

# Generated at 2022-06-14 15:42:16.144798
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """Test for constructor of class HlsFd"""
    # Dummy downloader instance
    class Dummy(object):
        def urlopen(self, url):
            return url

    ydl = Dummy()
    ydl.params = {}
    hls_fd = HlsFD(ydl, ydl.params)
    # Check all inherited attributes are gettable
    expected_keys = [
        "ydl", "params", "name", "progress_hooks", "fragment_retries",
        "fragment_retry_sleep", "test", "skip_unavailable_fragments",
    ]
    for key in expected_keys:
        assert hasattr(hls_fd, key)

# Generated at 2022-06-14 15:42:27.271548
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..utils import SearchInfoExtractor
    ie = InfoExtractor(
        {'url': 'https://example.com', 'params': {'test': True}})
    assert ie.test_HlsFD_can_download(
        '#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXTINF:10,\n'
        'http://media.example.com/first.ts\n',
        {'url': 'https://example.com/index.m3u8'})

# Generated at 2022-06-14 15:42:32.823541
# Unit test for constructor of class HlsFD
def test_HlsFD():
    print("Testing constructor of HlsFD")
    try:
        hls_config = {
            'key': 'value'
        }
        ydl = None
        params = None
        hls = HlsFD(ydl, params)
    except IOError:
        print("Constructor of HlsFD is tested")
        pass
    else:
        raise


# Generated at 2022-06-14 15:42:43.514402
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    Unit test for method real_download of class HlsFD.
    """
    # Download test files (if not already downloaded) and store the content for comparison.
    data_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'tests',
        'testdata')
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)


# Generated at 2022-06-14 15:42:54.157346
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os
    import argparse
    import json
    import tempfile
    import shutil
    import random

    try:
        import requests
    except ImportError:
        print('requests is required for unit tests to run')
        return

    import youtube_dl.postprocessor

    tmp_dir = tempfile.mkdtemp(prefix='youtube-dl-hls-test-')
    tmp_file = os.path.join(tmp_dir, 'test.ts')
    tmp_config = os.path.join(tmp_dir, 'config.json')
    tmp_log = os.path.join(tmp_dir, 'test.log')
    tmp_test_file = os.path.join(tmp_dir, 'test')

    sys.setrecursionlimit(100000)


# Generated at 2022-06-14 15:43:02.583730
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .downloader import YoutubeDL
    from .extractor.http import HttpIE
    from .compat import urlparse, parse_qs

    def downloader_simulator(url, *args, **kwargs):
        assert len(args) == 0
        assert len(kwargs) == 0

        body = '' # content of downloaded fragment
        headers = {}
        TestCase = r'[a-zA-Z0-9]+'

# Generated at 2022-06-14 15:43:14.795809
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    import os
    import tempfile
    import filecmp
    import shutil
    from .downloader import YoutubeDL
    from .extractor import gen_extractors

    def get_streams_of_comparison_manifest(path):
        ydl = YoutubeDL({'forceurl': True, 'forceduration': True, 'forcetitle': True, 'ignoreerrors': True, 'quiet': True})
        ydl.add_default_info_extractors()
        gen_extractors()
        result = ydl.extract_info(path, download=False)
        return result['requested_formats']

    def get_expected_size(streams):
        return sum([stream['filesize'] for stream in streams])

    def get_final_size(path):
        return os.stat(path).st_size

# Generated at 2022-06-14 15:43:17.177895
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.FD_NAME == 'hlsnative'

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:44:22.353982
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    Tests the functionality of the real_download method of HlsFD class.
    """

# Generated at 2022-06-14 15:44:28.566825
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import shutil
    from .test_download import create_downloader
    # Create a temporary file to store the downloaded file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    # Download and test
    downloader = create_downloader(HlsFD, {'quiet': True, 'test': True, 'force': True})
    info_dict = {'url': 'https://example.com/playlist.m3u8',
                 'ext': 'mp4',
                 'player_url': 'https://example.com/player.html',
                 'manifest_url': 'https://example.com/playlist.m3u8'}

# Generated at 2022-06-14 15:44:41.090895
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:44:49.951846
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import shutil
    import unittest
    import youtube_dl.YoutubeDL
    from ..utils import UnavailableVideoError

    ydl = youtube_dl.YoutubeDL({'format': 'hls[height<=1080]'})

    class TestHlsFD(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.temp_dir = tempfile.mkdtemp()
            os.chdir(cls.temp_dir)

        @classmethod
        def tearDownClass(cls):
            try:
                shutil.rmtree(cls.temp_dir)
            except (OSError, IOError):
                pass

        def _test_hls_fd(self, manifest_url, manifest, expected_data):
            manifest

# Generated at 2022-06-14 15:44:58.983752
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Test that HlsFD.can_download returns False when pycrypto is not present
    # and the manifest explicitly declares that it is AES-128 encrypted
    manifest = '#EXT-X-KEY:METHOD=AES-128'
    assert not HlsFD.can_download(manifest, '')

    # Test that HlsFD.can_download returns False when pycrypto is not present
    # and the manifest declares that it is AES-128 encrypted and has byte ranges
    manifest = '#EXT-X-KEY:METHOD=AES-128\n#EXT-X-BYTERANGE'
    assert not HlsFD.can_download(manifest, '')

    # Test that HlsFD.can_download returns True when the manifest declares that
    # it is AES-128 encrypted and has no byte ranges

# Generated at 2022-06-14 15:45:06.044760
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import FakeYDL
    from .test_fragment import test_make_temp_file

    ydl = FakeYDL()

    url = 'https://nrk.no/myhaaland-1.0.m3u8'

    for params in [
            {},
            {'test': True}]:
        info_dict = {
            'url': url,
            'http_headers': {'User-Agent': 'Mozilla/5.0'},
        }
        ctx = {
            'filename': test_make_temp_file(),
        }
        fd = HlsFD(ydl, params)
        assert fd.real_download(ctx['filename'], info_dict)


# Generated at 2022-06-14 15:45:12.113610
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .tests import get_testdata_video_url
    from ..extractor.common import InfoExtractor
    ie = InfoExtractor(HlsFD(), {}, {'noplaylist': True})
    ie.add_default_info_extractors()
    ie.extract_from_url(get_testdata_video_url("test_playlist"))

# Generated at 2022-06-14 15:45:20.101050
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .external import FFmpegFD
    from ..extractor import YoutubeIE
    from ..postprocessor import FFmpegMetadataPP
    import os

    def test_real_download(self, test, manifest_url, options, expected_segment_count):
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'socks_proxy': os.environ.get('SOCKS_PROXY'),
            'format': 'http-720p-8000',
            'outtmpl': 'test_data/test_%(format_id)s_%(resolution)s_%(abr)sk.mp4',
            'retries': 0,
        }
        ydl_opts.update(options)
        with YoutubeIE(ydl_opts) as ydl:
            y

# Generated at 2022-06-14 15:45:20.897721
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD(None, {})



# Generated at 2022-06-14 15:45:32.095396
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import youtube_dl
    import json

    # HLS Native
    # Test normal HLS stream
    info_dict = {
        "extractor": "hlshlsnative",
        "id": "XmSdTa9kaiQ",
        "url": "http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
        "title": "HLSNative Sample Video"
        }
    HlsFD.can_download(
        youtube_dl.extractor.common.urlopen(
            info_dict['url']).read().decode('utf-8'), info_dict)

    # Test a high quality HLS stream