

# Generated at 2022-06-14 15:37:59.298529
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.youtube import YoutubeIE
    from ..utils import DateRange


# Generated at 2022-06-14 15:38:09.846911
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    # Live streams heuristic does not always work (e.g. geo restricted to Germany
    # http://hls-geo.daserste.de/i/videoportal/Film/c_620000/622873/format,716451,716457,716450,716458,716459,.mp4.csmil/index_4_av.m3u8?null=0)
    # This heuristic also is not correct since segments may not be appended as well.
    # Twitch vods of finished streams have EXT-X-PLAYLIST-TYPE:EVENT despite
    # no segments will definitely be appended to the end of the playlist.

    # Empty manifest
    assert HlsFD.can_download('', {}) is True

    # Live stream heuristic

# Generated at 2022-06-14 15:38:10.994430
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD(None, None)

# Generated at 2022-06-14 15:38:24.561306
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..utils import create_result_set
    from ..compat import compat_urlparse

    # Create a fake YoutubeDL object with a fake params attribute
    class FakeYDL:
        def __init__(self, params):
            self.params = params

        def urlopen(self, url):
            if url.startswith('http://dash.example.com'):
                # A test that splitted byte ranges and key URL come together.
                return compat_urlparse.ParseResult(scheme='http', netloc='dash.example.com', path='/key1').geturl(), b'key1'

# Generated at 2022-06-14 15:38:36.089605
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    def download_fragment(_ctx, frag_url, _info_dict, _headers):
        if frag_url == 'http://cdn.video.com/frag1.ts':
            return True, b'this is frag 1 content'
        elif frag_url == 'http://cdn.video.com/frag2.ts':
            return True, b'this is frag 2 content'
        raise Exception('Invalid fragment URL %s' % frag_url)
    hls_fd = HlsFD(None, {})
    hls_fd._download_fragment = download_fragment
    hls_fd._append_fragment = lambda ctx, frag_content: None
    hls_fd._finish_frag_download = lambda ctx: None
    hls_fd._prepare_and_start_fr

# Generated at 2022-06-14 15:38:49.010108
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import Downloader
    from ..extractor import YoutubeIE, GenericIE, OptionsRequestExtractor
    d = Downloader()
    url = 'https://www.youtube.com/watch?v=EiCzwg0B_As&feature=push-sd&attr_tag=KxFx4x4x4M4CT4c%253A614824271413259319&playnext=1'
    yie = YoutubeIE(d)
    gie = GenericIE()
    yie.extract(url)
    video_info = list(yie._parse_video_data(url, yie._download_webpage(url, url, None)))[0]
    video_url = video_info['formats'][3]['url']
    gie.extract(video_url)
   

# Generated at 2022-06-14 15:38:51.668310
# Unit test for constructor of class HlsFD
def test_HlsFD():
    params = {'verbose': True, 'dump_intermediate_pages': False, 'extract_flat': True}
    ydl = object()
    hlsfd = HlsFD(ydl, params)
    assert hlsfd.params == params
    assert hlsfd._progress_hooks == []
    assert hlsfd.ydl == ydl


if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:38:55.747510
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .testimporthacks import test_download_for_real_download_test
    test_download_for_real_download_test(HlsFD, 'test', 'hls', 'firstfixture.m3u8', 'firstfixture_frag.dat')

# Generated at 2022-06-14 15:39:05.793806
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import re
    import pytest
    from .test_common import BaseTest

    # Test can_download
    BASE_TEST = BaseTest()

    # Test with a media file
    manifest = '''#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10,
fileSequence0.ts
#EXTINF:10,
fileSequence1.ts
#EXTINF:10,
fileSequence2.ts
#EXTINF:10,
fileSequence3.ts
#EXTINF:10,
fileSequence4.ts
#EXTINF:10,
fileSequence5.ts
#EXTINF:10,
fileSequence6.ts
#EXT-X-ENDLIST
'''
   

# Generated at 2022-06-14 15:39:13.953937
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    See https://github.com/ytdl-org/youtube-dl/pull/27660
    """
    from .testcases import YDL_TESTCASES
    from .testcases import YoutubeDLTest
    from ..utils import urlopen

    class HlsFDTest(YoutubeDLTest):
        def __init__(self, test_name, test_case):
            YoutubeDLTest.__init__(self, test_name, test_case)
            self.hlsfd = HlsFD(self.ydl, self.params)
            self._progress_hooks = []

        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)

        def _prepare_url(self, info_dict, *args, **kwargs):
            return YoutubeDLTest._prepare

# Generated at 2022-06-14 15:39:38.118014
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_test_data
    import os.path
    from .external import ExternalFD
    from nose.tools import eq_


# Generated at 2022-06-14 15:39:44.894948
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="https://priv.example.com/key.php?r=52"', {})
    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-MEDIA-SEQUENCE:7794', {})
    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-PLAYLIST-TYPE:EVENT', {})
    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-MAP:URI="main.mp4",BYTERANGE="616@0"', {})

# Generated at 2022-06-14 15:39:45.586876
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD()

# Generated at 2022-06-14 15:39:51.505828
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import tempfile
    import os
    import shutil
    import random
    import string
    import io

    from .http import HttpFD

    class TestHlsFD(HlsFD):

        def _prepare_url(self, info_dict, url):
            return url

        def _prepare_and_start_frag_download(self, ctx):
            ctx['temp_file_handle'] = tempfile.NamedTemporaryFile('w+b', delete=False)
            ctx['temp_filename'] = ctx['temp_file_handle'].name
            ctx['total_frags'] = 3
            ctx['fragment_index'] = random.randint(0, ctx['total_frags'] - 1)


# Generated at 2022-06-14 15:39:58.118097
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .fragment import FragmentFD
    from .external import FFmpegFD
    from ..compat import compat_urllib_error

    class DummyYdl(object):
        def __init__(self, test, can_download_test=True):
            self.test = test
            self.can_download_test = can_download_test

        def urlopen(self, *args, **kwargs):
            return self

        def geturl(self):
            self.test('geturl')
            return ''

        def read(self):
            self.test('read')
            return b''

    class DummyParams(object):
        def __init__(self, test, can_download_test=True):
            self.test = test
            self.can_download_test = can_download_test


# Generated at 2022-06-14 15:40:06.471187
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import check_executable

    if not check_executable('ffmpeg', ['ffmpeg'], True):
        return

    import shlex
    import tempfile
    import os
    import subprocess

    from . import YoutubeDL
    from .fragment import FragmentFD
    from .external import FFmpegFD
    from .common import FileDownloader

    from .extractor.common import InfoExtractor

    def _test_HlsFD_real_download(playlist_url, expected_fragment_counts):
        def _test_HlsFD_real_download_test(test_name, params, expected_fragment_counts):
            test_fd = tempfile.NamedTemporaryFile(suffix='.' + test_name, delete=False)
            tmp_fd_name = test_fd.name



# Generated at 2022-06-14 15:40:19.567322
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.generic import GenericIE

    class FakeInfoDict:
        def __init__(self, url, extra_param_to_segment_url, http_headers):
            self.url = url
            self.extra_param_to_segment_url = extra_param_to_segment_url
            self.http_headers = http_headers

    class FakeYDL:
        def __init__(self, extractor):
            self.extractor = extractor
            self.params = {
                'skip_download': True,
                'test': True,
            }

        def urlopen(self, url):
            class FakeURLH:
                def __init__(self, content):
                    self.content = content

                def read(self):
                    return self.content.encode()

            return FakeURLH

# Generated at 2022-06-14 15:40:29.751539
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..invoke import InvokeYDL

    class Downloader(InvokeYDL):
        def __init__(self):
            self.param = {
                'skip_download': True,
                'noprogress': True,
                'quiet': True,
                'test': True,
                'simulate': True,
            }
            self.options = self.gen_extractor_options()

        def gen_extractor_options(self):
            return {
                'key': 'value',
            }

        def to_screen(self, s):
            pass

    def test_func(url):
        downloader = Downloader()
        result = downloader.extract_info(url, download=False)
        fd = HlsFD(downloader, downloader.param)

# Generated at 2022-06-14 15:40:37.807394
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    from unittest.mock import patch
    from tempfile import TemporaryFile, NamedTemporaryFile
    from ..extractor import YoutubeDL
    import json

    class TestHlsFD(HlsFD, unittest.TestCase):
        def __init__(self, *args, **kwargs):
            super(TestHlsFD, self).__init__(*args, **kwargs)
            self._params = {
                'skip_download': True,
                'test': True,
            }
            self.addCleanup(self._cleanup)

        def _cleanup(self):
            if self._test_file:
                self._test_file.close()
                self._test_file = None
            if self._test_url_file:
                self._test_url_file.close()
               

# Generated at 2022-06-14 15:40:41.141402
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Simple test that checks that the HlsFD class can be constructed
    # The real tests are implemented in test_download.py
    HlsFD({})

# Generated at 2022-06-14 15:41:02.474171
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from . import YoutubeDL
    from .extractor.common import InfoExtractor
    from .compat import (
        compat_etree_fromstring,
        compat_parse_qs,
        compat_urlparse,
    )
    from .extractor.common import InfoExtractor
    from .utils import (
        determine_ext,
        ExtractorError,
        int_or_none,
        remove_end,
        unescapeHTML,
    )

    # Test cases copied from https://github.com/rg3/youtube-dl/blob/master/README.md#readme
    #
    # youtube-dl's unit test framework is not set up to use the python unittest framework, so
    # this is instead set up to be a function that returns true if all the tests have passed, false
    # otherwise.

# Generated at 2022-06-14 15:41:11.468318
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import FakeYDL
    url = 'https://example.com/media.m3u8'
    info_dict = {
        'id': 'abc',
        'ext': 'mp4',
    }
    params = {
        'fragment_retries': 1,
    }
    ydl = FakeYDL()
    fd = HlsFD(ydl, params)
    fd.real_download('test_filename', info_dict)
    assert fd.ydl is ydl
    assert fd.params is params


# Generated at 2022-06-14 15:41:19.598844
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .utils import IsolatedAsyncioTestCase

    class TestHlsFD(IsolatedAsyncioTestCase):
        def setUp(self):
            super(TestHlsFD, self).setUp()
            self.fd = HlsFD(None, None)
            self.fd.to_screen = lambda *args, **kargs: None
            self.fd.report_error = lambda msg: self.fail(msg)
            self.fd._prepare_url = lambda info_dict, url: url
            self.fd._finish_frag_download = lambda ctx: None

        def _download_fragment(self, ctx, url, info_dict, headers={}, bytes_to_read=None):
            from io import BytesIO

            if bytes_to_read is None:
                bytes_to_read = ctx

# Generated at 2022-06-14 15:41:29.222713
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .http import HttpFD
    from .dash import DashFD
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL({
        'noprogress': True,
        'nooverwrites': True,
        'logger': YoutubeDL.std_logger,
    })

    # Use DashFD
    ydl.add_info_extractor(DashFD(ydl))
    # Use HlsFD
    ydl.add_info_extractor(HlsFD(ydl))

    info_dict = {}

# Generated at 2022-06-14 15:41:30.572804
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Constructor of class HlsFD
    HlsFD(1,{})

# Generated at 2022-06-14 15:41:40.902742
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # TODO: currently, it's just calling the method, but it should check
    # it returns True and the file is created.
    from .external import FFmpegFD
    from ..extractor import gen_extractors
    import youtube_dl

    ydl = youtube_dl.YoutubeDL({
        'logger': youtube_dl.FileLogger(None),
        'hls_prefer_native': True,
        'verbose': True,
        'simulate': True,
        'skip_download': True,
        'test': True,
        'fragment_retries': 0,
        'skip_unavailable_fragments': False,
    })

    exts = gen_extractors()
    ext_gen = generate_extractor_tests(exts)

# Generated at 2022-06-14 15:41:46.882283
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import shutil
    import tempfile

    from .test_downloader import TestDownloader
    from ..compat import urlopen

    # Prepare downloader
    test_dir = tempfile.mkdtemp()
    test_dir_path = os.path.join(test_dir, '%(title)s.%(ext)s')
    ydl_opts = {
        'outtmpl': test_dir_path,
        'quiet': True,
        'skip_download': True,
        'noplaylist': True,
        'hls_prefer_native': True,
        'forcejson': True,
    }
    test_downloader = TestDownloader(ydl_opts)

    # Manually extract manifest URL

# Generated at 2022-06-14 15:41:47.546633
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    pass



# Generated at 2022-06-14 15:41:59.181868
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:42:03.443037
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert not HlsFD.can_download('test', {'url': 'whatever'})
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-PLAYLIST-TYPE:VOD\n#EXTINF:10,\ndata.ts\n#EXT-X-ENDLIST',
        {'url': 'whatever'})



# Generated at 2022-06-14 15:42:39.445619
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..YoutubeDL import YoutubeDL
    HlsFD(YoutubeDL(), {}, {'url': 'http://foo/bar'})

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:42:46.795886
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from mediainfo import MediaInfo
    from unittest import TestCase
    from .urllib_utils import FakeFileCacheURLLib
    import os

    class HlsTestCase(TestCase):
        def setUp(self):
            self.outfile = 'test-test.mp4'
            self.url = 'http://test.com/test.m3u8'
            self.file_cache = FakeFileCacheURLLib()

        def tearDown(self):
            if os.path.isfile(self.outfile):
                os.remove(self.outfile)
            if os.path.isdir('test'):
                os.rmdir('test')

        # Download test.m3u8, check that the resulting file is a valid MP4

# Generated at 2022-06-14 15:42:57.425766
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import FakeYDL
    from .testcommon import str_to_test_file

    ydl = FakeYDL()
    params = {
        'simulate': True,
        'quiet': True,
        'outtmpl': '-',
        'test': True,
    }


# Generated at 2022-06-14 15:43:04.707147
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    import requests
    import youtube_dl.downloader
    import youtube_dl.extractor.youtube

    class MockYtdl(object):
        def __init__(self, params):
            self.params = params

        def to_screen(self, s, end=''):
            pass

        def report_error(self, s):
            raise AssertionError(s)

        def report_warning(self, s):
            pass

        def urlopen(self, url):
            return requests.get(url)

    class MockInfoDict(dict):
        def __init__(self, **kwargs):
            super(MockInfoDict, self).__init__(**kwargs)

        def dict(self):
            return self


# Generated at 2022-06-14 15:43:16.604480
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import shutil
    import stat
    import subprocess
    import tempfile
    import uproot
    import uproot_methods

    import youtube_dl.utils

    from .test_download import has_curl_head_or_git
    from .test_dash import test_DashFD_real_download as dash_test_real_download

    filename = tempfile.mktemp()

    class YDL(object):
        params = {"test": True,
                  "outtmpl": filename}
        verbose = False

    ydl = YDL()

    def _download_fragment(ctx, frag_url, info_dict, headers):
        """Stub for the _download_fragment method"""
        return dash_test_real_download(ctx, frag_url, info_dict, headers)


# Generated at 2022-06-14 15:43:25.498385
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    from mockserver import MockServer, Mp4Segment, MockHandler, MockHandlerWithQuery
    test_files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files')
    out_file = tempfile.NamedTemporaryFile()
    server_port = 8090
    query_param = 'key'

    server = MockServer(port=server_port)
    server_url = 'http://localhost:{}'.format(server_port)
    query = {query_param: 'value'}
    query_url = update_url_query(server_url, query)


# Generated at 2022-06-14 15:43:36.499277
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import sys
    import tempfile
    import shutil
    import filecmp
    import mock
    import youtube_dl.downloader.external

    sys.modules['Crypto.Cipher.AES'] = mock.Mock()

    ydl = mock.Mock()
    params = {'format': '135'}

    hls_fd = HlsFD(ydl, params)
    assert not hls_fd.can_download('#EXT-X-PLAYLIST-TYPE:EVENT', {'is_live': False})


# Generated at 2022-06-14 15:43:47.665170
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.FD_NAME == 'hlsnative'

    # Test for staticmethod can_download for class HlsFD.

# Generated at 2022-06-14 15:43:59.947293
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .filesystem import FileFD
    from .utils import encode_data_to_file
    import os


# Generated at 2022-06-14 15:44:07.752914
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..downloader import Downloader
    ydl = Downloader()
    ydl.params.update({
        'hls_use_mpegts': False,
        'outtmpl': '%(id)s.%(ext)s',
        'quiet': True,
        'test': True,
        'skip_download': True
    })
    url = 'https://www.youtube.com/watch?v=OI-_FTHTZTQ'
    ie = ydl._find_info_extractor(url)
    info = ie.extract(url)
    fd = HlsFD(ydl, ydl.params)
    fd.real_download('test.ts', info)

# Generated at 2022-06-14 15:45:35.341669
# Unit test for constructor of class HlsFD
def test_HlsFD():
    class YDL:
        def __init__(self):
            self.params = {}

        def urlopen(self, url):
            class UrlH:
                def geturl(self):
                    return url
                def read(self):
                    return b''
            return UrlH()

    fd = HlsFD(YDL(), {})
    url = 'https://media.example.org/'
    assert (fd, fd._prepare_url(None, url)) == (fd, url)

    fd.ydl.params['http_proxy'] = 'http://localhost'
    assert (fd, fd._prepare_url(None, url)) == (fd, 'http://localhost/%s' % url)

    fd.ydl.params['http_proxy'] = 'http://localhost:8080'
   

# Generated at 2022-06-14 15:45:41.639896
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from datetime import datetime
    from .downloader import Downloader
    from .extractor import gen_extractors
    from .utils import DateRange

    class MyDownloader(Downloader):
        def __init__(self):
            Downloader.__init__(self)

        def report_warning(self, msg):
            pass

        def report_error(self, msg):
            raise Exception(msg)

    # Shorthand method to create the HlsFD
    def create_hlsfd(url, params={}, info_dict={}):
        hlsfd = HlsFD(MyDownloader(), params)
        if 'youtube_include_dash_manifest' not in hlsfd.params:
            hlsfd.params['youtube_include_dash_manifest'] = False

# Generated at 2022-06-14 15:45:45.993014
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # mock parameters of download function
    params = {
        'url': 'https://example.url/playlist.m3u8',
        'test': True,
    }
    # mock manifest contents

# Generated at 2022-06-14 15:45:47.129050
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD()


# Generated at 2022-06-14 15:45:55.977741
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .external import ExternalFD
    from ..downloader import FakeYDL
    import textwrap
    # Test for a basic HLS download
    ydl = FakeYDL()
    ydl.params.update(
        {'verbose': True, 'skip_download': True, 'merge_output_format': 'mp4'}
    )
    test_fd = HlsFD(ydl, {})
    output_url = 'test.mp4'

# Generated at 2022-06-14 15:46:05.585356
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os

    # prevent import error
    sys.modules['Crypto'] = None
    sys.modules['Crypto.Cipher'] = None

    from .test_utils import TestDownloader
    from .extractor.common import FileDownloader

    def _progress_hook(status):
        print('[%s] %s' % (status.get('downloaded_bytes'), status.get('_percent_str')))

    # sut = HlsFD(TestDownloader({'format': 'bestvideo'}, {'simulate': True}), {'format': 'bestvideo'})
    sut = HlsFD(
        FileDownloader({'format': 'bestvideo'}, {'simulate': True}),
        {'format': 'bestvideo'})
    sut.add_progress_hook(_progress_hook)

# Generated at 2022-06-14 15:46:13.819737
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class TestHlsFD(HlsFD):
        def report_skip_fragment(self, frag_index):
            self.skip_frag_index = frag_index
        def report_retry_fragment(self, err, frag_index, count, fragment_retries):
            self.retry_frag_index = frag_index
            self.retry_frag_count = count
            self.fragment_retries = fragment_retries
        def _download_fragment(self, frag_url, info_dict, headers):
            return not frag_url == 'https://fragments.com/fragment-4.ts', 'content'
        def _finish_frag_download(self, ctx):
            self.fragments_content = ctx['fd'].getvalue()


# Generated at 2022-06-14 15:46:22.724304
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .extractor.common import InfoExtractor
    from .compat import compat_urllib_request, compat_http_client
    from .downloader import YoutubeDL
    from .cache import Cache

    class YoutubeDLMock(YoutubeDL):
        def __init__(self, params):
            super(YoutubeDLMock, self).__init__(params)
            self._test_response = [None, None]
            self._test_counter = 0

        def urlopen(self, url):
            test_response = self._test_response[self._test_counter]
            self._test_counter += 1
            if test_response is None:
                return super(YoutubeDLMock, self).urlopen(url)

# Generated at 2022-06-14 15:46:29.341482
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import json
    import os
    import tempfile
    from ..utils import encodeFilename

    man_url = 'https://vodhls-uk-live.akamaized.net/hls/live/2144183/uk/master_audio_eng.m3u8'
    info_dict = {
        'url': man_url,
        'id': '2144183',
        'title': 'HLS-UK',
        'formats': 'master_audio_eng',
        'http_headers': {
            'Origin': 'https://player.twitch.tv',
            'Referer': 'https://player.twitch.tv/js/embed/v1.js',
        },
    }

# Generated at 2022-06-14 15:46:30.734551
# Unit test for constructor of class HlsFD
def test_HlsFD():
    ydl = MockYoutubeDL({})
    assert HlsFD(ydl, {})
