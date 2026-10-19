

# Generated at 2022-06-14 15:37:49.215014
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os.path
    import tempfile
    import unittest
    import zipfile
    import shutil
    from youtube_dl.utils import make_HTTPServer

    # Example playlist
    # See https://github.com/ytdl-org/youtube-dl/issues/24556

# Generated at 2022-06-14 15:38:02.276476
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U\n#EXTINF:10,\nhttp://example.org/a.ts', {'url': 'http://example.org/m3u8', 'is_live': False})
    assert not HlsFD.can_download('#EXTM3U\n#EXTINF:10,\nhttp://example.org/a.ts', {'url': 'http://example.org/m3u8', 'is_live': True})

# Generated at 2022-06-14 15:38:11.517441
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..extractor.generic import GenericIE

    class MockYDL(object):
        def __init__(self):
            self.info_extractors = [InfoExtractor()]
            self.params = {}
            self.ie = GenericIE(self)

        def urlopen(self, url):
            try:
                b = type(b'')
            except NameError:
                b = bytes
            content = url

# Generated at 2022-06-14 15:38:24.956822
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    class InfoDict():
        def __init__(self, url):
            self.get = self._get
            self.url = url

        def _get(self, key):
            if key == 'is_live':
                return bool('live' in self.url)


# Generated at 2022-06-14 15:38:33.376042
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import YoutubeIE
    from ..downloader import YoutubeDL
    ie = YoutubeIE()
    ydl = YoutubeDL()
    ydl.add_info_extractor(ie)

    fd = HlsFD(ydl, {'simulate': True})
    ie.extract('https://www.youtube.com/watch?v=iAkH0v4cWO4&t=0s')
    assert fd.real_download(None, ie._cache[0])
    assert ydl._downloader.active is False

# Generated at 2022-06-14 15:38:45.861283
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class YDL:
        params = {}
        def to_screen(self, msg):
            print(msg)
        def problem(self, msg):
            print(msg)
        def add_progress_hook(self, _):
            pass
        def urlopen(self, url):
            if 'segment' in url and 'fake-fragment-1.ts' in url:
                with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                       'resources', 'hls', 'fake-fragment-1.ts'), 'rb') as f:
                    return compat_urllib_request.addinfourl(f, {}, url)
            return compat_urllib_request.urlopen(url)


# Generated at 2022-06-14 15:38:57.633940
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import json
    import time
    import unittest

    from ..utils import DateRange
    from ..compat import (
        compat_http_client,
        is_py2
    )
    from ..downloader import BaseDownloader
    from .fragment import FragmentFD
    from .external import FFmpegFD

    from .test_fragment import TestFragmentFD

    class _FakeYDL(object):
        def __init__(self, response):
            self.cache = {}
            self.urlopen_handlers = {
                'http://example.com/test/manifest': self._fake_urlopen_handler(response),
            }

        def urlopen(self, url):
            if url in self.cache:
                return self.cache[url]

# Generated at 2022-06-14 15:39:06.550430
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import mock_server
    from ..extractor import gen_extractors
    import tempfile
    import shutil

    def run_test(port, manifest_content, frag_content, url='', info_dict=None, err=None):
        with mock_server(port, manifest_content) as server:
            with tempfile.NamedTemporaryFile() as f:
                ie = gen_extractors(url or server.url, {}, 0)
                ie[0]._downloader.params.update({
                    'test': True,
                    'fragment_retries': 0,
                    'skip_unavailable_fragments': True,
                })

# Generated at 2022-06-14 15:39:14.406030
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """ Test a real download of HlsFD class. """

    # Test with regular m3u8 file
    info_dict = {
        'url': 'https://tungsten-wallaby.globecast.tv/hls/france24_en/fra/index.m3u8',
        'title': 'France 24',
    }
    ydl = FakeYDL()
    fd = HlsFD(ydl, {})
    fname = ydl.prepare_filename('1MB')
    fd.real_download(fname, info_dict)
    fpath = ydl.prepare_filename('1MB')
    assert os.path.exists(fpath)

    # Test with m3u8 file with byte ranges

# Generated at 2022-06-14 15:39:16.021848
# Unit test for constructor of class HlsFD
def test_HlsFD():
    hlsFD = HlsFD(None, None)
    assert hlsFD is not None

# Generated at 2022-06-14 15:39:31.970272
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """
    Create instance of class HlsFD without any exception.
    """
    HlsFD({}, {})


# Generated at 2022-06-14 15:39:40.841323
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from . import FileDownloader
    from ..extractor import YoutubeIE
    ydl = FileDownloader()
    ydl.add_info_extractor(YoutubeIE())
    ydl.params['hls_prefer_native'] = True
    ydl.params['noprogress'] = True
    ydl.params['logtostderr'] = False
    ydl.params['prefer_insecure'] = True
    ydl.params['format'] = '141/bestaudio'
    ydl.params['usenetrc'] = False
    info = ydl.extract_info(
        'https://www.youtube.com/watch?v=JnfyjwChuNU')
    ydl.download(info)

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:39:45.877461
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import YoutubeDL
    ydl = YoutubeDL({'logger': DummyLogger(), 'nooverwrites': True})
    hlsFD = HlsFD(ydl, {'fragment_retries': 5})
    assert hlsFD is not None
    return hlsFD


# Generated at 2022-06-14 15:39:55.092811
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.youtube import YoutubeIE
    class DummyYDL(object):
        def __init__(self):
            self.params = {
                'verbose': True,
                'skip_download': True,
            }
        def report_warning(self, msg):
            print(msg)
        def download(self, info_dicts):
            return info_dicts
    ydl = DummyYDL()
    ie = YoutubeIE(ydl)

# Generated at 2022-06-14 15:40:04.798240
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .tests import get_testdata_file
    from .common import AllowedFormats
    filename = get_testdata_file(os.path.join(
        'hls-vod', 'manifest.m3u8'))
    ydl = YoutubeDL({
        'verbose': False,
        'format': AllowedFormats.HLS,
        'hls_prefer_native': True,
        'test': True,
    })
    info_dict = {'url': 'test', 'protocol': 'm3u8', 'extractor': 'hlsnative', 'player_url': None, 'id': 'test'}
    fd = HlsFD(ydl, {})
    fd.real_download(filename, info_dict)
    assert os.path.exists(filename)

# Generated at 2022-06-14 15:40:18.105347
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .utils import _ExtractorTest

    # Tests for different features of HLS

# Generated at 2022-06-14 15:40:28.894568
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from . import YoutubeDL
    from .extractor.youtube import YoutubeIE

    def _hook_progress(d):
        print('%s: %s\n' % (d['status'], d['filename']))
        # pretend to report back that we finished
        return True

    def _hook_finished(d):
        print('finished: %s' % (d['filename']))
        # pretend to report back that we finished
        return True

    url = 'https://github.com/'
    ydl = YoutubeDL({})
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(YoutubeIE.ie_key())
    ydl.params['forcejson'] = True
    ydl.params['simulate'] = True
    ydl.params['noprogress'] = True

# Generated at 2022-06-14 15:40:35.162733
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # In this test, a small file is downloaded with the fragment headers set up in such a way that
    # a full file without decryption should be downloaded. The expected value is the plain unencrypted
    # content of the file and the expected total file size (after decryption).
    from .common import fake_urlopen


# Generated at 2022-06-14 15:40:40.429662
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Create HlsFD object.
    from .extractor import gen_extractors
    ydl = gen_extractors()[0]
    HlsFD(ydl, {})

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:40:49.941359
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import encodeArgument
    ydl = __Ydl()
    ydl.params.update({
        'cachedir': False,
        'noprogress': True,
        'logger': ydl.get_logger(),
        'test': True,
        'quiet': True,
        'writedescription':True,
        'outtmpl': encodeArgument('%(epoch)s.%(ext)s'),
    })

    # Test data from http://video-dev.github.io/hls.js/demo/, we don't want to rely on it for a real unit test
    url = 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8'
   

# Generated at 2022-06-14 15:41:25.076429
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import youtube_dl.YoutubeDL
    import youtube_dl
    import youtube_dl.postprocessor.ffmpeg
    import youtube_dl.downloader.common
    import youtube_dl.downloader.hls
    import youtube_dl.downloader.http
    import youtube_dl.extractor.common
    import youtube_dl.extractor.youtube
    import xml.etree.ElementTree

    # Temporary directory
    test_dir = tempfile.mkdtemp()

    # YoutubeDL options

# Generated at 2022-06-14 15:41:26.001305
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD(YDL(), {})

# Generated at 2022-06-14 15:41:33.619000
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .external import ExternalFD
    from .dash import DashSegmentsFD
    from ..compat import compat_str
    from ..utils import (
        encode_compat_str,
        FindFDClass,
    )

    ydl = object()

# Generated at 2022-06-14 15:41:43.927160
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_testdata
    manifest_url = get_testdata('npo_out/subdir/subsubdir/manifest.m3u8')
    info_dict = {
        'url': manifest_url,
        'is_live': False,
        'ext': 'mp4',
        'http_headers': {
            'User-Agent': 'test_ua',
            'Cookie': 'test_cookie',
        },
        '_decryption_key_url': 'https://test.nl/decryption_key',
    }

    import io
    with io.open(get_testdata('npo_out/seg-5-v1-a1.ts'), 'rb') as f:
        expected_content = f.read()

    from youtube_dl.YoutubeDL import YoutubeDL
   

# Generated at 2022-06-14 15:41:57.120426
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .http import HttpFD
    import io
    import itertools
    import random
    import struct
    import subprocess
    import tempfile
    import unittest

    # Construct a temporary directory.
    _, temporary_directory = tempfile.mkstemp()
    # Create a temporary directory by prefixing the constructed temporary
    # directory with _ and removing the created file.
    temporary_directory = temporary_directory + '_'
    os.remove(temporary_directory)
    os.mkdir(temporary_directory)

    # Generate a random 128-bits key and initialization vector.
    random_generator = random.SystemRandom()
    key = random_generator.getrandbits(128).to_bytes(16, 'big')

# Generated at 2022-06-14 15:42:05.278165
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import encodeFilename
    from ..extractor import youtube
    from . import FragmentFD_test

    # This test depends on these methods and attributes
    #   of class YoutubeDL

    def urlopen(self, url):
        assert url == 'http://test.server/test.m3u8', "Unexpected url"
        class http_response:
            @staticmethod
            def read():
                return '''#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="http://test.server/test.key"
#EXTINF:2.833,
http://test.server/test.ts
#EXT-X-ENDLIST
'''
        return http_response()

    def to_screen(self, *args, **kwargs):
        pass


# Generated at 2022-06-14 15:42:16.710548
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from datetime import datetime
    from io import BytesIO

    import pytest

    from youtube_dl.downloader import HLSDownloader
    from youtube_dl.utils import encode_base_n
    from tests.test_downloader_hls import FakeYDL

    AD_START = '#ANVATO-SEGMENT-INFO:type=ad,start_time=0'
    AD_END = '#ANVATO-SEGMENT-INFO:type=master'
    UPLYNK_AD_START = '#UPLYNK-SEGMENT:start=0,end=10,ad'
    UPLYNK_AD_END = '#UPLYNK-SEGMENT:start=0,end=10,segment'
    EXT_X_BYTERANGE1_WITH_HASH

# Generated at 2022-06-14 15:42:25.238050
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})

    HlsFD.real_download(
        ydl, None,
        {
            'url': 'https://test.com/test.m3u8',
            'info_dict': {
                'is_live': False,
                '_decryption_key_url': 'https://test.com/test.key',
                'url': 'https://test.com/test.m3u8',
                'id': 'test',
            },
        }
    )

# Generated at 2022-06-14 15:42:36.064520
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile

    from .http import FakeHttpTestFD
    from ..extractor import setup

    ydl = setup()

    # Test the functionality of HlsFD with the real_download method.

    # Test a simple stream
    info_dict = {
        'url': 'https://test.com/test1.m3u8',
        'playlist_mincount': 1,
        'playlist': [
            {'url': 'https://test.com/test1.m3u8', 'title': 'Test 1', 'duration': 1},
        ]
    }

    def test1(fd):
        assert fd.real_download('/test', info_dict)
        return True


# Generated at 2022-06-14 15:42:45.350968
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import gen_extractors
    from ..utils import sanitize_open
    from ..compat import compat_urlretrieve

    import os
    import shutil
    import tempfile
    import textwrap

    extractors = gen_extractors()

# Generated at 2022-06-14 15:43:54.350759
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import get_suitable_downloader
    from ..YoutubeDL import YoutubeDL
    from ..extractor.generic import YoutubeIE

    url = 'http://m1.joker.nixcdn.com/f652a2e1759f1815a9cb4a40c1b4b6ac/5aff0c0f/radio/song/2017/11/10/6/a/6/a6c4b14758b63ed201b05eee7b0ccee3.mp3'

# Generated at 2022-06-14 15:44:05.134628
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    can_download_results = [None] * 1000
    can_download_results[0] = False
    can_download_results[1] = True
    can_download_results[2] = False
    can_download_results[3] = False
    can_download_results[4] = True
    can_download_results[5] = False
    can_download_results[6] = False
    can_download_results[7] = False
    can_download_results[8] = False
    can_download_results[9] = True
    can_download_results[10] = True
    can_download_results[11] = False
    can_download_results[12] = False
    can_download_results[13] = True
    can_download_results[14] = False
    can_download_results

# Generated at 2022-06-14 15:44:14.834218
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    assert not HlsFD.can_download(
        "#EXTM3U\n#EXT-X-VERSION:6\n#EXT-X-PLAYLIST-TYPE:VOD\n#EXT-X-KEY:METHOD=AES-128,URI=\"https://priv.example.com/key.php?r=52\",IV=0x9c7db8778570d05c3177c349fd9236aa\n#EXT-X-MAP:URI=\"test.ts\"\n#EXTINF:4.161333,\ntest.ts\n#EXT-X-ENDLIST\n",
        {"url": "test.m3u8"})

# Generated at 2022-06-14 15:44:22.353718
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # Prepare
    import tempfile
    import os
    from ..utils import prepare_mock_download
    from ..extractor import YoutubeIE
    from ..extractor.common import InfoExtractor
    from youtube_dl.downloader.external import FFmpegFD

    def put_m3u8_manifest(manifest_name, manifest_content):
        manifest_file = open(manifest_name, 'w')
        manifest_file.write(manifest_content)
        manifest_file.close()

    manifest_name = 'manifest.m3u8'

# Generated at 2022-06-14 15:44:30.391223
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .test_utils import _parse_m3u8_attributes
    from .test_utils import _append_fragment
    from .test_utils import _prepare_and_start_frag_download
    from .test_utils import _finish_frag_download
    from .test_utils import _download_fragment
    from .test_utils import _prepare_url
    from .test_utils import _get_byte_range
    from .test_utils import _real_extract
    from .test_utils import _real_extract_from_m3u8_formats
    from .test_utils import _remove_bitrates
    # Initialize a fake context

# Generated at 2022-06-14 15:44:42.214744
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import doctest_refactor_util
    from ..postprocessor import FFmpegMergerPP
    from .fragment import FragmentFD
    from .external import FFmpegFD
    import os
    import shutil
    import tempfile

    fake_info_dict = {
        'url': 'https://test.server/test.m3u8',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        },
        'extra_param_to_segment_url': '',
        '_decryption_key_url': '',
        'is_live': False,
    }

    byte_r

# Generated at 2022-06-14 15:44:49.258194
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import re
    import os
    from .test import get_test_data_dir

    def _test_params():
        return {
            'fragment_retries': 0,
            'skip_unavailable_fragments': False,
            'test': True,
            'keepfragments': True,
            'outtmpl': '',
        }

    def _url_open(cls, url, *args, **kwargs):
        if kwargs.get('timeout') is None:
            kwargs['timeout'] = 6
        return super(HlsFD, cls).urlopen(url, *args, **kwargs)

    # Method test for _download_fragment
    # The purpose is to ensure that the method does not throw exceptions.

# Generated at 2022-06-14 15:44:58.412601
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import unittest
    import youtube_dl
    from ytdl_test_server import HTTPServerWsgiFrameworks

    server = HTTPServerWsgiFrameworks(port=0, test_file_list=['test.m3u8'])
    server.start()

    test_url = 'http://localhost:{port}/test.m3u8'.format(port=server.server_port)

    test_file_path = os.path.join(server.files_dir, 'test.m3u8')
    def check_got(should):
        got = open('test.m3u8', 'rb').read()
        server.stop()
        assert got == should, 'got %s expected %s' % (repr(got), repr(should))


# Generated at 2022-06-14 15:45:08.277937
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import _download_json
    from .test import _extract_manifest_url
    from .test import _get_test_data

    class FakeYDL:
        def __init__(self, manifest_url, manifest, fragment_urls):
            self.manifest_url = manifest_url
            self.manifest = manifest
            self.fragment_urls = fragment_urls
            self.fragment_contents = {}

        def urlopen(self, url):
            if url == self.manifest_url:
                return _get_test_data(self.manifest)
            else:
                assert self.fragment_urls[0] == url
                self.fragment_urls = self.fragment_urls[1:]

# Generated at 2022-06-14 15:45:17.974414
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import MagicMock, patch
    except ImportError:
        from mock import MagicMock, patch
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    ydl._downloader = MagicMock()
    with patch('youtube_dl.YoutubeDL.urlopen') as urlopen_mock:
        urlopen_mock = MagicMock()
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b''
        mock_response.geturl.return_value = ''
        urlopen_mock.return_value = mock_response
        HlsFD(ydl, {'test': True}).real_download(None, {'url': None})