

# Generated at 2022-06-14 15:37:59.186668
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """ Only test for download prepared for tests specially. """
    from ..extractor import get_info_extractor

    def extractor_download(extractor, url, params):
        ie = get_info_extractor(extractor)
        params['outtmpl'] = '%(id)s.mp4'
        params['noplaylist'] = True
        ie.download([url], params)

    def set_up_extractor_params(params):
        params['format'] = 'hls'
        params['test'] = True
        params['quiet'] = True

    def tear_down_extractor_params(params):
        params.pop('test', None)
        params.pop('quiet', None)

    # Test for correct download with and without decryption

# Generated at 2022-06-14 15:38:07.636901
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from tests.helper import FakeYDL
    ydl = FakeYDL()
    fd = HlsFD(ydl, {'prefer_insecure': False})
    info_dict = {
        'url': 'https://example.com/video.m3u8',
        'fragment_base_url': 'https://example.com/videoSeg',
        'fragments': [
            'videoSeg1.ts',
            'videoSeg2.ts',
            'videoSeg3.ts',
        ],
    }
    assert fd.real_download('test.mp4', info_dict)

# Generated at 2022-06-14 15:38:21.558277
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import youtube_dl.YoutubeDL
    from youtube_dl.compat import compat_tempfile

    # Tested HLS stream: http://jell.yfish.us/
    real_hls_url = 'http://jell.yfish.us/hls/bipbop_4x3/bipbop_4x3_variant.m3u8'
    stream_url = lambda i: 'http://jell.yfish.us/hls/bipbop_4x3/gear2/prog_index.m3u8' if i == 0 else real_hls_url

    def _download_hook(d):
        d['info_dict']['url'] = stream_url(d.get('fragment_index', 0))
        # d['fragment_index'] will be

# Generated at 2022-06-14 15:38:33.800559
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # Test for method real_download of class HlsFD. This test needs
    # the YouTube video at http://www.youtube.com/watch?v=R7yfISlGLNU in
    # order to be run.

    import os
    import tempfile
    import shutil

    fd = HlsFD('http://www.youtube.com/watch?v=R7yfISlGLNU')

    (fd_in, temp_filename) = tempfile.mkstemp()
    fd_out = os.fdopen(fd_in, 'w')
    fd_out.close()

    fd.params = {}
    fd.params['test'] = True
    fd.real_download(temp_filename, {})


# Generated at 2022-06-14 15:38:41.014949
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..ytdl import YoutubeDL
    from ..extractor.common import UrlDescriptor
    def tail_hook(d):
        d['filename'] = 'test.tmp'
    ydl = YoutubeDL({'verbose': True, 'quiet': True})
    ydl.add_info_extractor(UrlDescriptor(
        'hlsnative', ['https?://www.domain.com/.+']))
    ydl.add_progress_hook(tail_hook)
    ydl.process_ie_result({
        'url': 'http://example.com/playlist.m3u8',
        '_type': 'url_transparent',
        'ie_key': 'HlsFD',
        'title': 'test'
    })
    return True

# Generated at 2022-06-14 15:38:52.947534
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..test import get_testdata_video

    def _test_HlsFD(
            manifest,
            test_name,
            fragment_total,
            expected_result,
            expected_warning):
        """ Helper function for test to call with different args """
        cls = HlsFD.__class__
        fd_name = 'hlsnative'
        test_data = get_testdata_video('min-' + test_name + '.mp4')
        test_data_url = test_data.http_url
        should_download_frag_count = fragment_total
        test_is_live = False

        test_hlsfd = cls(None, {'outtmpl': 'min.mp4'})

        with open(test_data.name, 'rb') as f:
            test_hlsfd

# Generated at 2022-06-14 15:39:03.430791
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.__bases__[0].__name__ == 'FragmentFD'
    filename = 'test_HlsFD'
    info_dict = {
        'url': 'http://example.com',
        'http_headers': {},
    }
    hlsfd = HlsFD({}, {'test': True})
    hlsfd.to_screen = lambda x: None
    hlsfd.report_warning = lambda x: None
    hlsfd.report_error = lambda x: None
    hlsfd.report_retry_fragment = lambda err, frag_num, count, retries: None
    hlsfd.report_skip_fragment = lambda x: None
    hlsfd.real_download(filename, info_dict)



# Generated at 2022-06-14 15:39:12.433420
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .downloader import YoutubeDL
    from .extractor import get_info_extractor
    import os.path

    youtube_ie = get_info_extractor('youtube')
    ydl = YoutubeDL()
    ydl._ies = [youtube_ie]


# Generated at 2022-06-14 15:39:23.575950
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import FakeYDL
    from .test_external import OneByOneFDTest

    class HlsTestFD(OneByOneFDTest):
        FD_NAME = 'hlsnative'

        def __init__(self, test, options, fragment_index=None):
            super(HlsTestFD, self).__init__(test, options, fragment_index)
            self.test_manifest = None
            self.test_file_handle = None
            self.test_frag_data = {}

        def _download_fragment(self, ctx, url, info_dict, headers):
            frag_url = re.sub(r'(?<=[^=])[\d]+', '{frag_index}', url)

# Generated at 2022-06-14 15:39:26.644513
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U', {})


# Generated at 2022-06-14 15:39:42.470963
# Unit test for constructor of class HlsFD
def test_HlsFD():

    from ..utils import _gen_extractors

    _gen_extractors()

# Generated at 2022-06-14 15:39:52.864404
# Unit test for constructor of class HlsFD
def test_HlsFD():
    url = 'https://www.example.com/manifest.m3u8'
    ydl = FakeYDL()
    hfd = HlsFD(ydl, {})
    if not isinstance(hfd, object):
        return 'Expected object from class HlsFD'
    if hfd.params != {}:
        return 'Expected empty dictionary'
    if hfd.ydl != ydl:
        return 'Expected ydl to be the same'
    params = {
        'extra_param_to_segment_url': 'test=1',
        '_decryption_key_url': 'https://example.com/key',
        'is_live': True
    }
    hfd = HlsFD(ydl, params)

# Generated at 2022-06-14 15:39:58.764237
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .http_fd import HttpFD
    from .f4mfd import F4mFD
    from ..extractor import get_info_extractor

    from io import BytesIO
    from zipfile import ZipFile
    from unittest import TestCase

    def assert_contents_equal(fname, expected_content):
        actual_content = ZipFile(fname).read('0.ts')
        assert actual_content == expected_content

    class HlsNativeFDTestCase(TestCase):
        def setUp(self):
            self.test_content = BytesIO()
            self.zip_content = BytesIO()
            self.zip_file = ZipFile(self.zip_content, 'w')
            self.zip_file.writestr('0.ts', '\x00' * 0x400)

       

# Generated at 2022-06-14 15:40:11.319226
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .extractor.common import InfoExtractor
    from .extractor.generic import GenericIE
    from .downloader.http import HttpFD
    from .compat import compat_urllib_request, compat_http_client, compat_HTTPError
    from .utils import FakeYDL

    # Simulate the behavior of YoutubeDL in real_download method.

# Generated at 2022-06-14 15:40:24.017871
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import collections
    import http.server
    import os
    import re
    import socketserver
    import threading
    import tempfile
    import urllib.request
    import urllib.error
    import urllib.parse
    import zipfile

    def serve_file_in_background(request_handler, filename):
        request = request_handler.rfile.readline().decode(
            'ascii').strip()
        request_handler.send_response(200)
        request_handler.end_headers()
        content = open(filename, 'rb').read()
        request_handler.wfile.write(content)
        return request

    def serve_manifest_in_background(request_handler, manifest, expected_request=None):
        manifest_dir, manifest_name = os.path.split(manifest)

# Generated at 2022-06-14 15:40:32.207972
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import testutils

    expect_output = """\
[hlsnative] Downloading m3u8 manifest
[download] Downloading fragment 0 of 5
[download] Downloading just-in-case fragment 1 of 5
[download] Downloaded fragment 0 of 5
[download] Downloaded fragment 1 of 5
[download] Downloading fragment 2 of 5
[download] Downloading just-in-case fragment 3 of 5
[download] Downloading just-in-case fragment 4 of 5
[download] Downloaded fragment 2 of 5
[download] Downloaded fragment 3 of 5
[download] Downloaded fragment 4 of 5
"""


# Generated at 2022-06-14 15:40:45.457588
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import _download_json

    download_path = 'download_dir/download_dir/%(height)s-%(ext)s'

# Generated at 2022-06-14 15:40:56.857246
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .http import HttpFD
    from .test import ydl_exe
    from ..YoutubeDL import YoutubeDL


# Generated at 2022-06-14 15:41:03.762305
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    assert HlsFD.can_download('''
#EXTM3U
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-TARGETDURATION:10
#EXTINF:10,
http://media.example.com/first.ts
#EXTINF:10,
http://media.example.com/second.ts
#EXTINF:10,
http://media.example.com/third.ts
#EXT-X-ENDLIST
    ''', {})


# Generated at 2022-06-14 15:41:15.658040
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U', {'url': ''})

    # These features should not be supported.
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=sampling reels', {'url': ''})
    assert not HlsFD.can_download('#EXT-X-BYTERANGE', {'url': ''})
    assert not HlsFD.can_download('#EXT-X-MEDIA-SEQUENCE:1', {'url': ''})
    assert not HlsFD.can_download('#EXT-X-PLAYLIST-TYPE:EVENT', {'url': ''})
    assert not HlsFD.can_download('#EXT-X-MAP:', {'url': ''})

    # These features should not be supported, even if pycrypto is installed.


# Generated at 2022-06-14 15:41:51.033204
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import FakeYDL
    from ..utils import make_HTTPServer
    import tempfile
    import shutil
    import os
    from .fragment import FragmentFD

    port = 5566
    cert = 'cert.pem'
    key = 'key.pem'
    temp_dir = tempfile.mkdtemp()

    # Create the certificate and key files
    # Too lazy to write them in the test
    open(os.path.join(temp_dir, cert), 'w').close()
    open(os.path.join(temp_dir, key), 'w').close()
    server = make_HTTPServer(port, temp_dir, cert, key)
    server_thread = server.start()


# Generated at 2022-06-14 15:42:01.265705
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import unittest
    import sys
    import os

    class HlsFDTest(unittest.TestCase):
        def setUp(self):
            self.test_manifest = os.path.join(os.getcwd(), 'test_manifest.m3u8')
            self.test_info = {'url': 'http://example.com'}
            self.test_params = {}

        def test_can_download(self):
            # should can_download return True if the manifest does not contain features that
            # are unsupported
            # (1) encrypted streams with a KEY METHOD other than NONE or AES-128
            file = open(self.test_manifest, 'w')

# Generated at 2022-06-14 15:42:13.125570
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import io
    import sys
    import unittest

    sys.modules['Crypto'] = None

    class FakeYDL(object):
        class FakeUrlopen(object):
            def __init__(self, url):
                self._url = url

            def read(self):
                if self._url == 'manifest_url':
                    return b'#EXTM3U\n\n'
                elif self._url == '/first_frag_url':
                    return b'first_frag_content'
                elif self._url == '/second_frag_url':
                    return b'second_frag_content'

        def __init__(self, *args, **kwargs):
            pass

        def urlopen(self, url):
            return self.FakeUrlopen(url)


# Generated at 2022-06-14 15:42:24.939966
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    import tempfile
    from .extractor import gen_extractors
    from ..downloader.common import FileDownloader

    # Method can_download of class HlsFD will return false when
    #   1. encryption method is not NONE, AES-128
    #   2. the m3u8 manifest contains the keyword EXT-X-BYTERANGE
    #   3. the keyword EXT-X-PLAYLIST-TYPE:EVENT is in the m3u8 manifest
    #   4. the keyword EXT-X-MAP is in the m3u8 manifest
    #   5. the m3u8 manifest is live playlist
    InfoRedirect = collections.namedtuple('InfoRedirect', ['url', 'query'])

# Generated at 2022-06-14 15:42:32.832591
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..downloader import Downloader
    from ..postprocessor.ffmpeg import FFmpegPostProcessor
    from .fragment import FragmentFD
    from .external import FFmpegFD
    from .dash import DASHFD
    from ..utils import prepend_extension

    count = 0
    def _hook(status):
        print(repr(status))
        nonlocal count
        count += 1

    class FakeIE(InfoExtractor):
        def __init__(self, downloader, ie_url):
            super(FakeIE, self).__init__(downloader, ie_url)

        def _real_initialize(self):
            pass


# Generated at 2022-06-14 15:42:43.514514
# Unit test for constructor of class HlsFD
def test_HlsFD():
    res = HlsFD.can_download("#EXTM3U\n#EXT-X-TARGETDURATION:12\n#EXT-X-VERSION:2\n#EXT-X-MEDIA-SEQUENCE:0\n#EXT-X-PLAYLIST-TYPE:VOD\n#EXTINF:4.007,\n0.ts\n#EXTINF:4.007,\n1.ts\n#EXTINF:4.007,\n2.ts\n#EXTINF:4.007,\n3.ts\n#EXT-X-ENDLIST\n", {})
    assert res

# Generated at 2022-06-14 15:42:50.324086
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor import gen_extractor_classes
    (YoutubeIE, _) = gen_extractor_classes()

    downloader = YoutubeIE().downloader
    downloader.params.update({'ignoreerrors': True, 'nooverwrites': True, 'format': '134'})
    downloader.add_info_extractor(YoutubeIE())

# Generated at 2022-06-14 15:42:57.586655
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    func_name = 'HlsFD_real_download'
    from .test_fragment import test_FragmentFD_real_download
    test_FragmentFD_real_download(func_name, HlsFD.FD_NAME, HlsFD.real_download, verify_data=False)
    try:
        from Crypto.Cipher import AES
        # Test decryption
        test_FragmentFD_real_download(func_name, HlsFD.FD_NAME, HlsFD.real_download, verify_data=True)
    except ImportError:
        pass

# Generated at 2022-06-14 15:43:04.795028
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import os
    import copy
    import json

    from .downloader import FakeYDL
    from .http import HttpFD
    from .http import HeadRequest

    from ..utils import (
        encode_data_uri,
        sanitize_open,
    )


# Generated at 2022-06-14 15:43:16.708033
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    HlsFD_instance = HlsFD(
        None,
        {},
    )

    # 1. Manifest of encrypted Hls stream

# Generated at 2022-06-14 15:44:20.797788
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import re
    from .downloader import YoutubeDL
    from .extractor import YoutubeIE
    ydl = YoutubeDL({'outtmpl': '/tmp/foo%(playlist_index)s.%(ext)s'})
    ydl.add_info_extractor(YoutubeIE())
    ydl.download(['https://www.youtube.com/watch?v=wNwCey4YxNo'])
    assert(len(re.findall(r'foo\d+\.', open('/tmp/playlist.m3u8', 'r').read())) == 12)

# Generated at 2022-06-14 15:44:22.040697
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('', {}) == True


# Generated at 2022-06-14 15:44:30.230064
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .info import InfoExtractor
    from .extractor import YoutubeIE
    from .downloader import YoutubeDL
    from .common import FileDownloader
    from .utils import match_filter_func
    InfoExtractor.extract = lambda self, url: YoutubeIE().extract(url)
    # Ensure that the constructor of HlsFD is called
    fd = FileDownloader({
        'format': 'bestvideo+bestaudio',
        'noplaylist': True,
        'outtmpl': '%(id)s.%(ext)s',
        'format_filter': match_filter_func('best[ext=mp4]'),
        'logger': YoutubeDL(YoutubeDL.params),
        'progress_hooks': [lambda s: None],
    })
    # Assert that the constructor of HlsFD was called

# Generated at 2022-06-14 15:44:42.212458
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ytdl.extractor import url_or_none, try_get
    from .test_utils import MockYDL
    from .extractor import FakeExtractor
    import unittest
    import platform
    import os

    class Test(unittest.TestCase):
        def setUp(self):
            self.os = platform.system()

        def test_youtube_live_stream(self):
            self.assertIsNone(url_or_none('https://www.youtube.com/channel/UCBi2mrWuNuyYy4gbM6fU18Q'))
            ydl = MockYDL()
            ydl.add_info_extractor(FakeExtractor())
            ydl.params['test'] = True
            ydl.params['forcejson'] = True

# Generated at 2022-06-14 15:44:50.576622
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import youtube_dl.YoutubeDL
    # A malicious playlist can contain invalid characters that would make the regex in the first line of HlsFD.can_download()
    # raise an exception in case the playlist is a byte string, so always ensure it's a utf-8 string.
    ydl = youtube_dl.YoutubeDL({'hls_prefer_native': True})

# Generated at 2022-06-14 15:44:56.347790
# Unit test for constructor of class HlsFD
def test_HlsFD():
    class _DummyYDL():
        def __init__(self):
            self.params = {}
        def prepare_filename(self, info_dict):
            return info_dict['id']
        def to_screen(self, *args, **kwargs):
            pass
        def report_error(self, *args, **kwargs):
            raise RuntimeError()
        def trouble(self, *args, **kwargs):
            pass
        def report_warning(self, *args, **kwargs):
            pass
        def urlopen(self, *args, **kwargs):
            return _DummyUrlOpener()
        def to_stdout(self, s):
            pass

    class _DummyUrlOpener():
        def __init__(self):
            self.data = b''

# Generated at 2022-06-14 15:45:01.576498
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors
    extractors = gen_extractors()
    hd_manifest = None
    for i in range(0, len(extractors)):
        if extractors[i].IE_NAME == 'hlsnative':
            hd_manifest = extractors[i].ie._build_url_result(
                'http://d222l8ho7vhhap.cloudfront.net/content/sintel/hls/playlist.m3u8', {})
            break
    assert hd_manifest

# Generated at 2022-06-14 15:45:12.942244
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..test import get_test_data

    test_frag_name = 'aHR0cDovL2EuY2RuLmZ0Yy52LmNmL3BpL25ld3MvMjAxNjA3L3NvdW5kc3JjLzE1LzI0LzQ2NjQvbWVkaWEvZmFrZV8tdF85NDUxNjMxX1ItMTI5Lm1wNA=='
    test_frag_name = binascii.a2b_base64(test_frag_name)


# Generated at 2022-06-14 15:45:20.541729
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:45:31.696342
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import FakeYDL
    ydl = FakeYDL()
    ydl.params['hls_use_mpegts'] = False
    hls_fd = HlsFD(ydl, {})

    info = {
        'url': 'http://manifest.com/man.m3u8',
        'player_url': 'http://player.com/player.swf',
        'http_headers': {},
        '_decryption_key_url': 'https://decrypt.com/key',
        'extra_param_to_segment_url': '',
        'is_live': False,
    }
