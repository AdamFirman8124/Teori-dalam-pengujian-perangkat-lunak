

# Generated at 2022-06-14 15:37:47.415614
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # HlsFD.can_download = lambda self, url: True
    # HlsFD.real_download = lambda self, url, filename: True
    return HlsFD(None, None)

# Generated at 2022-06-14 15:38:00.635033
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({'quiet': True})

    hls_fd = HlsFD(ydl, {'quiet': True})

# Generated at 2022-06-14 15:38:10.566926
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import mock
    import os

# Generated at 2022-06-14 15:38:24.224274
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import youtube_dl
    url = 'https://example.com/man.m3u8?Pram=Value#EXT-X-test'
    ydl_opts = {
        'hls_prefer_native': True,
        'debug_printtraffic': True,
        'simulate': True,
        'dump_single_json': True,
        'writeinfojson': True,
        'extract_flat': True,
        'noplaylist': True,
        'skip_download': True,
        'no_warnings': True,
        'forceurl': True,
        'skip_unavailable_fragments': True,
        'hls_prefer_ffmpeg': True,
        'format': 'best',
    }

# Generated at 2022-06-14 15:38:35.836979
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # basic
    assert HlsFD.FD_NAME == 'hlsnative'

    # can_download
    # no match #1

# Generated at 2022-06-14 15:38:39.340230
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors
    for ie in gen_extractors():
        if ie.IE_NAME == 'hls':
            ie.suitable('https://example.com/test') # This calls HlsFD.can_download
            break


if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:38:51.625583
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import unittest
    import sys
    import os
    import urllib
    from .extractor.common import InfoExtractor

    class DummyInfoExtractor(InfoExtractor):
        def _download_webpage(self, *args, **kwargs):
            return '', None

    class HlsFDTests(unittest.TestCase):
        def setUp(self):
            from .downloader import YoutubeDL
            self.ydl = YoutubeDL({
                'verbose': True,
                'forcejson': True,
                'dump_intermediate_pages': False,
                'skip_download': True,
                'simulate': True,
                'forcetitle': True,
                'forcethumbnail': True,
                'forceid': True,
                'forceduration': True,
            })

# Generated at 2022-06-14 15:39:02.668121
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U', {'is_live': False}) is True
    assert HlsFD.can_download('#EXT-X-KEY:METHOD=AES-128', {'is_live': False}) is True
    assert HlsFD.can_download('#EXT-X-BYTERANGE', {'is_live': False}) is True
    assert HlsFD.can_download('#EXT-X-MEDIA-SEQUENCE:1', {'is_live': False}) is True
    assert HlsFD.can_download('#EXT-X-PLAYLIST-TYPE:EVENT', {'is_live': False}) is True
    assert HlsFD.can_download('#EXT-X-MAP', {'is_live': False}) is True


# Generated at 2022-06-14 15:39:10.011415
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..utils import (
        DateRange,
        HEADRequest,
        sanitize_open,
    )

    class FakeInfoDict(dict):
        def __init__(self):
            super(FakeInfoDict, self).__init__()
            self.populate()


# Generated at 2022-06-14 15:39:22.141568
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import unittest

    def _get_manifest_file_path(url):
        try:
            os.remove('test.m3u8')
        except OSError:
            pass
        os.symlink(url, 'test.m3u8')
        return 'test.m3u8'

    class HlsFD_real_download(unittest.TestCase):
        def setUp(self):
            self.fs = tempfile.NamedTemporaryFile()
            self.tempname = self.fs.name

        def tearDown(self):
            self.fs.close()

        def test_HlsFD_01(self):
            # Test if a new fragment will be appended to the end of the file.
            url = _get_manifest_file_

# Generated at 2022-06-14 15:39:43.457269
# Unit test for constructor of class HlsFD
def test_HlsFD():
    url = 'https://example.org/video.m3u8'
    info_dict = {
        'url': url,
        'title': 'Example Video',
        'thumbnail': 'http://example.org/thumbnail.jpg',
    }
    hls_downloader = HlsFD(YoutubeDL(), {}, info_dict)
    assert hls_downloader.info_dict is not None
    assert hls_downloader.info_dict['url'] == url
    assert hls_downloader.info_dict['title'] == info_dict['title']
    assert hls_downloader.info_dict['thumbnail'] == info_dict['thumbnail']

# Generated at 2022-06-14 15:39:50.221714
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import subprocess
    import sys
    import traceback
    from os import path
    if sys.platform == 'win32':
        python_name = 'pythonw.exe'
    else:
        python_name = 'python3'
    this_file_abspath = path.abspath(__file__)
    ydl = path.abspath(path.join(path.dirname(this_file_abspath), '..', 'youtube_dl'))
    args = [python_name, ydl, '--downloader-args', '--test', '--', 'm3u8testv3']

# Generated at 2022-06-14 15:39:51.474795
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD(None, None)

# Generated at 2022-06-14 15:40:02.364671
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXT-X-VERSION:3\n'
        '#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXT-X-PLAYLIST-TYPE:VOD\n'
        '#EXTINF:10,\n'
        'http://media.example.com/segment1.ts\n'
        '#EXT-X-ENDLIST\n',
        {'format_id': '251', 'url': 'http://example.com'})

# Generated at 2022-06-14 15:40:15.605247
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    fragments_url = 'https://github.com/ytdl-org/youtube-dl/blob/master/test/data/hls/fragments.txt?raw=true'
    manifest_url = 'https://github.com/ytdl-org/youtube-dl/blob/master/test/data/hls/manifest.m3u8?raw=true'
    info_dict = {
        'url': manifest_url,
        'id': 'YOUTUBEID',
        'http_headers': {},
        'fragments': fragments_url
    }

    class FakeYDL():
        def urlopen(self, url, data=None, timeout=None):
            class FakeUrlH():
                def read(self):
                    return 'fake_content'
            return FakeUrlH()


# Generated at 2022-06-14 15:40:27.481466
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .downloader import FakeHttpFD
    from ..utils import encode_data_uri

    def return_true(url, args):
        return True

    def return_false(url, args):
        return False

    def append_fragment(*args):
        return True

    def detect_http_error(url, args):
        raise compat_urllib_error.HTTPError(url, None, None, None, None)

    # Test that it downloads the first fragment
    # Also test that it skips requests for the key if it's already available

# Generated at 2022-06-14 15:40:37.263858
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import gen_extractors
    import os.path
    import time
    import shutil
    import tempfile
    import zipfile
    import json

    TEST_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'tests', 'data', 'download', 'HlsFD')

    def run_test(test_json):
        temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 15:40:48.315147
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .extractor import gen_extractors
    from ..utils import unescapeHTML
    from io import BytesIO

    # Test for catching errors when pycrypto is not found.
    def _download_fragment(self, ctx, frag_url, info_dict, headers):
        raise NotImplementedError

    setattr(HlsFD, '_download_fragment', _download_fragment)
    _downloader = gen_extractors()['youtube']

    url = 'http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8'

# Generated at 2022-06-14 15:40:59.101674
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_testcases, fake_ydl

    for test_param in get_testcases():
        if not test_param.get('youtube_dl_fatal_errors_fatal', True):
            continue
        ydl = fake_ydl(test_param)
        info_dict = test_param.get('info_dict')
        stream_url = info_dict['url']
        fd = HlsFD(ydl, ydl.params)
        fd.real_download(info_dict['_filename'], info_dict)
        assert fd.ydl.calls[0][0] == 'urlopen'
        assert fd.ydl.calls[0][1][0] == stream_url

# Generated at 2022-06-14 15:41:11.701903
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from youtube_dl.YoutubeDL import YoutubeDL

    ydl = YoutubeDL({
        'quiet': True,
        'writedescription': True,
        'nooverwrites': True,
        'format': '140',
        'skip_download': True,
        'hls_prefer_native': True,
        'logger': YoutubeDL.std_logger,
    })

    with open('test/testdata/test.m3u8', 'r') as file:
        m3u8 = file.read()

    if HlsFD.can_download(m3u8, {}):
        print

# Generated at 2022-06-14 15:41:40.572243
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Test  HlsFD constructor """
    assert HlsFD(None, None)

# Generated at 2022-06-14 15:41:49.585244
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import io
    import json
    import os
    import re
    import socket
    import sys
    from collections import OrderedDict
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer
    from urllib.parse import urlparse
    from unittest.mock import Mock
    from unittest.mock import patch

    from ..extractor import YoutubeDL
    from ..extractor.common import InfoExtractor

    # Set the test mode for YoutubeDL
    YoutubeDL.params['test'] = True

    # Remove the --test argument from command line arguments if present
    # It would otherwise lurk behind and be treated as an URL.
    sys.argv = [arg for arg in sys.argv if arg != '--test']

    # Silence the youtube_dl logger
    from ..utils import _LOG_LE

# Generated at 2022-06-14 15:42:00.377994
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os
    import unittest
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    from ..utils import FakeYDL
    from ..extractor import get_info_extractor
    from .external import ExternalFD
    from .ffmpeg import FFmpegFD

    ################################################################################
    # patch import
    ################################################################################
    class FakeModule:
        class YTCookieFD:
            can_download = False
            FD_NAME = 'faketcookie'
            def real_download(self, filename, info_dict):
                pass

    import sys
    sys.modules['youtube_dl.downloader.faketcookie'] = FakeModule()

    class FakeModule:
        class ExternalFD:
            can_download = False
            FD_

# Generated at 2022-06-14 15:42:01.147520
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD

# Generated at 2022-06-14 15:42:04.172539
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():  # TODO
    hlsfd = HlsFD()
    hlsfd.params['test'] = True
    hlsfd.real_download('filename', {'url': 'http://example.com'})



# Generated at 2022-06-14 15:42:15.842919
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from . import YoutubeDL
    ydl = YoutubeDL()
    assert HlsFD.can_download('#EXTM3U', {'url': 'foo'})
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0', {'url': 'foo'})
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE', {'url': 'foo'})
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128', {'url': 'foo'})

# Generated at 2022-06-14 15:42:27.091581
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from .http import HttpFD
    from .m3u8 import M3u8FD
    from ..downloader.http import YoutubeDLHandler
    from ..extractor import common as ext_common
    from ..Extractor import gen_extractors
    from ..utils import fake_http_server_handler

    # pylint: disable=unused-argument
    def handler_factory(program):
        def handler(conn, _):
            url = conn.recv(1024)
            conn.send('HTTP/1.1 200 OK\r\n\r\n%s' % program.manifest)
            return url
        return handler


# Generated at 2022-06-14 15:42:27.634744
# Unit test for constructor of class HlsFD
def test_HlsFD():
    pass

# Generated at 2022-06-14 15:42:37.096060
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # testing can_download method
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-VERSION:5\n#EXT-X-MEDIA-SEQUENCE:0\n#EXT-X-TARGETDURATION:10\n#EXT-X-KEY:METHOD=AES-128,URI="",IV=0x00000000000000000000000000000000\n#EXTINF:10.000000,\n#EXT-X-BYTERANGE:15000@0\nindex_0_av.m3u8\n', {'is_live': False})

# Generated at 2022-06-14 15:42:45.731302
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # Since the method is not completely implemented, it's hard to test.
    # But we can test that the playlist reading and skipping fragments
    # upon errors works as intended.
    playlist = '''
#EXTM3U
#EXT-X-ALLOW-CACHE:NO
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-TARGETDURATION:5
#EXTINF:5,
segment.ts
#EXT-X-ENDLIST
'''
    # It's a dummy class but we don't care
    ydl = {'urlopen': lambda url: url}
    # Make HlsFD think only 10 seconds are in the playlist.
    # That way we can test that only the first fragment is downloaded.
    test_params = {'test': True}

# Generated at 2022-06-14 15:43:56.368559
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.FD_NAME == 'hlsnative'

# Generated at 2022-06-14 15:44:06.582510
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .utils import FakeYDL
    from .common import fake_info_dict
    from .external import ExternalFD
    import os
    import tempfile

    # Usage:
    #   python -m youtube_dl.extractor.tests.HlsFD_real_download

    def test_frag_download(ydl, url, urlh, frag_url, frag_content):
        assert ydl.urlopen(url) == urlh
        assert ydl.urlopen(frag_url) == frag_content

    class FakeFragmentFD(FragmentFD):
        # Download the first fragment twice, just to verify we don't download
        # more fragments than we need to during the tests.
        first = True
        def _download_fragment(self, *args, **kwargs):
            if self.first:
                self.first

# Generated at 2022-06-14 15:44:15.829743
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..compat import compat_urlparse
    from ..utils import urlhead

    url = 'https://raw.githubusercontent.com/rg3/youtube-dl/master/test/data/hls/hls.m3u8'
    hls_info_dict = {
        'id': 'hls',
        'extractor': 'generic',
        'url': url,
        'playlist_index': 0,
        'playlist': url,
        'title': 'HLS test',
        '_type': 'hls',
        'is_live': False,
    }

    class HlsTestIE(InfoExtractor):
        IE_NAME = 'hls'
        IE_DESC = False  # Do not list

# Generated at 2022-06-14 15:44:23.060888
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():

    from .test import get_testdata_file

    def _urlopen(ctx, *args, **kwargs):
        self = ctx['self']
        #print(args[0])
        if args[0] in self.test_urls:
            fp = get_testdata_file(self.test_urls[args[0]])
        else:
            raise AssertionError('Unexpected url: %s' % args[0])
        return fp

    def _prepare_url(ctx, *args, **kwargs):
        self = ctx['self']
        return args[0]

    from .test import FakeYDL

    class MockHlsFD(HlsFD):

        def __init__(self, ydl, params):
            self._ydl = ydl
            self._params = params



# Generated at 2022-06-14 15:44:30.821437
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U', {})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONAES', {})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128', {})
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE', {})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128\n#EXT-X-BYTERANGE:121090@803136', {})

# Generated at 2022-06-14 15:44:42.258274
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    def _can_download(s, is_live):
        man_info = {'url': 'http://example.com/file.m3u8', 'is_live': is_live}
        return HlsFD.can_download(s, man_info)

    # Unsupported features test

# Generated at 2022-06-14 15:44:50.597114
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    HlsFD().real_download('lol.mp4', {
        'url': 'https://url/to/m3u8',
        'extra_param_to_segment_url': '',
        'http_headers': {},
        'n_fragments': 2,
        'fragment_base_url': 'https://url/to/fragment/',
        'fragments': ['fragment1', 'fragment2'],
    })


# Generated at 2022-06-14 15:44:51.256387
# Unit test for constructor of class HlsFD
def test_HlsFD():
    pass

# Generated at 2022-06-14 15:44:52.564966
# Unit test for constructor of class HlsFD
def test_HlsFD():
    hlsfd = HlsFD(None, {})
    assert hlsfd is not None

# Generated at 2022-06-14 15:45:01.041170
# Unit test for constructor of class HlsFD