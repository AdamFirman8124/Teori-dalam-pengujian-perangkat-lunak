

# Generated at 2022-06-14 15:37:52.687126
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():

    def create_info_dict(url, **kwargs):
        info_dict = dict()
        info_dict['url'] = url
        for key, value in kwargs.items():
            info_dict[key] = value
        return info_dict

    # An invalid manifest will be rejected on the spot
    assert not HlsFD.can_download('invalid manifest', create_info_dict(''))

    # If a method is not supported, extraction will be delegated to FFmpegFD
    assert not HlsFD.can_download(
        '#EXT-X-KEY:METHOD=AES-128', create_info_dict(''))
    assert not HlsFD.can_download(
        '#EXT-X-MAP', create_info_dict(''))

    # Check that supported variants are succesfully handled
    assert Hls

# Generated at 2022-06-14 15:37:53.987997
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD()

# Generated at 2022-06-14 15:38:06.049163
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import io
    from .testutils import FakeYDL

    ydl = FakeYDL()

    class FakeHlsFD(HlsFD):
        def _prepare_url(self, info_dict, url):
            return url

        def _download_fragment(self, ctx, frag_url, info_dict, headers):
            frag_content = b'Test'
            return True, frag_content

    content = b'#EXTM3U\n#EXT-X-TARGETDURATION:12\n#EXT-X-KEY:METHOD=AES-128,URI="http://example.com/AES-128"\n#EXTINF:5,\nhttp://example.com/0\nhttp://example.com/1\n'
    content_io = io.BytesIO(content)

    info_

# Generated at 2022-06-14 15:38:13.456853
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import unittest

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.hfd = HlsFD(None, None)


# Generated at 2022-06-14 15:38:26.818751
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Test download of a manifest and its fragments using HlsFD"""
    class InfoDict():
        """ A fake InfoDict class for testing """
        def __init__(self, url):
            self.url = url

    # Define a fake manifest that contains 2 fragments
    manifest = """\
    #EXTM3U
    #EXT-X-TARGETDURATION:10
    #EXTINF:9.009,
    http://media.example.com/first.ts
    #EXTINF:9.009,
    http://media.example.com/second.ts
    #EXT-X-ENDLIST
    """

    url = 'http://media.example.com/sample.m3u8'
    info_dict = InfoDict(url)


# Generated at 2022-06-14 15:38:32.709544
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .downloader import YoutubeDL
    ydl = YoutubeDL({'quiet': True})
    ydl.process_ie_result({
        'url': '',
        'extractor': 'hls',
        'ie_key': 'Hls',
        'hls_skip_download': True
    })

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:38:40.710172
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    assert HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-VERSION:3\n'
        '#EXT-X-PLAYLIST-TYPE:VOD\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXTINF:9.99,\n'
        'segment1.ts\n'
        '#EXTINF:9.99,\n'
        'segment2.ts\n'
        '#EXTINF:1.99,\n'
        'segment3.ts\n'
        '#EXT-X-ENDLIST\n',
        {'url': 'https://test'}
    )


# Generated at 2022-06-14 15:38:52.314528
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import youtube_dl

    class MyYDL(youtube_dl.YoutubeDL):
        def __init__(self, *args, **kwargs):
            self.cache = {}
            super(MyYDL, self).__init__(*args, **kwargs)

        def urlopen(self, url):
            if url not in self.cache:
                self.cache[url] = super(MyYDL, self).urlopen(url)
            return self.cache[url]
    ydl = MyYDL({'skip_download': True, 'simulate': True})
    ie = HlsFD(ydl, {'simulate': True})
    i = youtube_dl.extractor.common.InfoExtractor(ydl, ie)
    ie.set_downloader(i)

# Generated at 2022-06-14 15:39:03.223219
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # Checks HlsFD can download the given video_id.
    # Returns:
    #   string  the video filename.
    #   string  the video downloaded content.
    #   boolean true if the file is encrypted.
    def real_download(video_id):
        from youtube_dl.YoutubeDL import YoutubeDL
        class FakeFile(object):
            def __init__(self):
                self.name = 'test_video.mp4'
                self.buffer = b''
                self.closed = False
                self.enc = False
            def write(self, buf):
                self.buffer += buf
                if not self.enc and buf[:3] == b'\x00\x00\x01':
                    self.enc = True
            def close(self):
                self.closed = True
                self.buffer = b

# Generated at 2022-06-14 15:39:12.248783
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    Test method real_download of class HlsFD
    """

# Generated at 2022-06-14 15:39:25.930715
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD


# Generated at 2022-06-14 15:39:26.881114
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    assert HlsFD.real_download(filename, manifest) is True

# Generated at 2022-06-14 15:39:37.616330
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download("""
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:8
#EXT-X-MEDIA-SEQUENCE:2680
#EXTINF:7.975,
https://priv.example.com/fileSequence2680.ts
#EXTINF:7.941,
https://priv.example.com/fileSequence2681.ts
#EXTINF:7.975,
https://priv.example.com/fileSequence2682.ts
""", {})


# Generated at 2022-06-14 15:39:46.426455
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import tempfile
    # This test only verifies that HlsFD.real_download method does not throw exceptions
    # so we only pass minimal arguments to the method.
    hlsfd = HlsFD()
    info_dict = {
        'url': 'https://devimages.apple.com.edgekey.net/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8'
    }
    tmp_fd, tmp_filename = tempfile.mkstemp(prefix='youtubedl-test_')
    try:
        hlsfd.params = {'test': True}
        hlsfd.real_download(tmp_filename, info_dict)
    finally:
        import os
        os.close(tmp_fd)

# Generated at 2022-06-14 15:39:58.047837
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os
    import tempfile
    import shutil
    import json
    import traceback
    import subprocess
    import platform
    import xml.etree.ElementTree as ET
    video_metadata = {
        '_type': 'url',
        'ie_key': 'HlsNative',
        'id': '6gH_oFhjK8g',
        'url': 'http://manifest.googlevideo.com/api/manifest/hls_playlist/source/yt_lang_no_apiary/key/yt_live_broadcast/upn/4v4R-RZ0m-k/playlist/index.m3u8'
    }
    ydl_options = {}
    ydl_options['format'] = 'bestaudio'
    ydl_options['quiet']

# Generated at 2022-06-14 15:40:06.439176
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import FakeYDL
    from .test_external import download_file_test, is_test_fd_fd

    class FakeHlsFD(HlsFD):
        def __init__(self, ydl, params):
            self._download_retval = 'test_HlsFD_real_download'
            super(FakeHlsFD, self).__init__(ydl, params)

        def _prepare_and_start_frag_download(self, ctx):
            return super(FakeHlsFD, self)._prepare_and_start_frag_download(ctx)

        def _append_fragment(self, ctx, frag_content):
            return super(FakeHlsFD, self)._append_fragment(ctx, frag_content)


# Generated at 2022-06-14 15:40:08.452712
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('', {})


# Unit tests for can_download()

# Generated at 2022-06-14 15:40:11.481420
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .http import HttpFD
    from .fragment import _http_test
    return _http_test(HlsFD, HttpFD)

# Generated at 2022-06-14 15:40:24.160328
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .f4mtest import FakeFD
    fake_fd = FakeFD()
    info_dict = {'url': 'hls://live-hls.facebook.com/rtmp/live/liveevent/mcat.scte35/playlist.m3u8?v=7&p=1'}

# Generated at 2022-06-14 15:40:32.303562
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import FileDownloader
    params = {
        'format': 'mp4',
        'test': True,
    }
    with FileDownloader(params) as fd:
        assert(fd.fd._prepare_url({'url': 'https://example.com/video.m3u8?accessToken=foobar', 'http_headers': {}}, 'https://example.com/video.m3u8?accessToken=foobar') == 'https://example.com/video.m3u8?accessToken=foobar')

# Generated at 2022-06-14 15:41:06.323980
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os
    import tempfile
    import shutil

    # Prepare a fake youtube-dl object
    ydl = object()
    ydl.report_warning = lambda x: sys.stderr.write(x + '\n')
    ydl.report_error = lambda x: sys.stderr.write(x + '\n')
    ydl.trouble = lambda x, y: sys.stderr.write('%s: %s\n' % (x, y))
    ydl.report_retry_fragment = lambda x, y, z, a: sys.stderr.write('%s (attempt #%s)\n' % (x, z))

# Generated at 2022-06-14 15:41:14.435832
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from . import YoutubeDL
    from .extractor.common import InfoExtractor
    from .postprocessor.ffmpeg import FFmpegExtractAudioPP
    from .downloader import Downloader
    from .utils import SearchInfoExtractor, fake_http_headers
    from .compat import urlparse, urlunparse


# Generated at 2022-06-14 15:41:19.447229
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:41:29.077523
# Unit test for constructor of class HlsFD
def test_HlsFD():
    try:
        from Crypto.Cipher import AES
    except ImportError:
        print('pycrypto not found. Please install it.')
        return False

# Generated at 2022-06-14 15:41:35.595683
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import os
    import tempfile

    info_dict = {
        'id': 'testing',
        'url': 'http://127.0.0.1:12345/manifest.m3u8',
        'title': 'test hls',
    }

    class TestYDL:
        def __init__(self):
            self.tmpfilename = tempfile.mkstemp()

        def to_screen(self, _):
            pass

        def report_error(self, err):
            print(err)

        def urlopen(self, url):
            return url

        def download(self, fd):
            fd.download(self.tmpfilename)


# Generated at 2022-06-14 15:41:43.537006
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import shutil
    import tempfile
    from .common import FakeYDL
    from .test_common import get_testdata_file

    with tempfile.NamedTemporaryFile(delete=False) as t:
        t.write(b'M3U8 playlist downloaded by youtube-dl\n')

    info_dict = {
        'id': 'Yt8km2Qj5X0',
        'url': get_testdata_file('test.m3u8'),
        'ext': 'mp4',
        'title': 'test',
        'http_headers': {
            'Authorization': 'Basic dGVzdDokbXlzZWNyZXQ=',
        },
        'is_live': False,
    }

    fake_ydl = FakeYDL()
    fake_

# Generated at 2022-06-14 15:41:52.182541
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    HlsFD.can_download('', {
        'is_live': False,
        'url': '',
    })
    HlsFD.can_download('#EXT-X-MEDIA-SEQUENCE:0', {
        'is_live': False,
        'url': '',
    })
    assert not HlsFD.can_download('#EXT-X-MEDIA-SEQUENCE:1', {
        'is_live': False,
        'url': '',
    })
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {
        'is_live': False,
        'url': '',
    })

# Generated at 2022-06-14 15:42:01.906821
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import FakeYDL
    import tempfile

    ydl = FakeYDL()


# Generated at 2022-06-14 15:42:14.004801
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:42:21.039948
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import json
    from .test_utils import FakeYDL

    ydl = FakeYDL()
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(FFmpegFD)
    ydl.params.update( {
        'noprogress' : True,
        'quiet' : True,
        'writeinfojson' : True,
        'skip_download': True,
        'test': True
    })

# Generated at 2022-06-14 15:43:00.291252
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    Unit test for method real_download of class HlsFD
    """
    import os
    import tempfile
    import shutil
    from .test_fragment import MockYDL
    from .test_fragment import MockFD

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    # Create a temporary file in that directory
    temp_file = tempfile.NamedTemporaryFile(dir = temp_dir, prefix = 'ydl-test_', suffix = '.tmp')
    temp_file_path = os.path.join(temp_dir, temp_file.name[len(temp_dir)+1:])

    # Create a mock YouTubeDL object
    mock_ydl = MockYDL()

    # Create a mock FragmentFD object

# Generated at 2022-06-14 15:43:11.835504
# Unit test for constructor of class HlsFD
def test_HlsFD():
    url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    info_dict = {'url': url}

    #Download with pycrypto absent
    HlsFD.can_download('#EXT-X-KEY:METHOD=AES-128', info_dict)

    #Download with supported features only

# Generated at 2022-06-14 15:43:22.477930
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from .m3u8 import M3U8FD
    from .external import FFmpegFD
    from .dash import DashFD
    ydl = object()

# Generated at 2022-06-14 15:43:34.291826
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..extractor.common import InfoExtractor


# Generated at 2022-06-14 15:43:45.111703
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert(HlsFD.can_download("#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0\n#EXTINF:2.008,\nhttps://priv.example.com/fileSequence0.ts\n#EXT-X-ENDLIST\n", {})) == False #encrypted
    assert(HlsFD.can_download("#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0\n#EXTINF:2.008,\nhttps://priv.example.com/fileSequence0.ts\n#EXT-X-ENDLIST\n", {'is_live' : True})) == False #live

# Generated at 2022-06-14 15:43:53.113023
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI="https://foo.bar/key.bin"\n#EXT-X-BYTERANGE:16@0\nfragment.ts\n#EXT-X-ENDLIST',
        {'url': 'http://foo.bar/stream.m3u8'}) is False

# Generated at 2022-06-14 15:44:00.488863
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import encode_data_uri
    from .fragment import test_FragmentFD_real_download_impl

# Generated at 2022-06-14 15:44:09.381045
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..downloader.common import FileDownloader
    from . import frag_downloader

    class FakeInfoExtractor(InfoExtractor):
        def _real_initialize(self):
            self._available_formats = ['http']

    class FakeFD(HlsFD):
        def _download_fragment(self, *args, **kwargs):
            return 'downloaded content', None

        def _append_fragment(self, *args, **kwargs):
            pass

    ie = FakeInfoExtractor({'_type': 'fake', 'id': 'fakeid'})
    ie.http_headers = {}
    ie.add_info_extractor(ie)
    fd = FileDownloader({'hls_use_native': True}, ie)
    info_dict

# Generated at 2022-06-14 15:44:17.780992
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test_downloads import download_url
    from .test_downloads import parse_options

    # This is the output of `youtube-dl --simulate --format hls-251 --match-filter 'is_def' 'https://www.youtube.com/watch?v=n1qlpNMBW8E'`
    # The video is a cooking video but it has a lot of ads, including pre- and mid-roll.
    result = download_url(
        'https://www.youtube.com/watch?v=n1qlpNMBW8E',
        downloader_options={
            'simulate': True,
            'format': 'hls-251',
            'match_filter': 'is_def',
            'test': True
        }
    )
    # The URL of the first fragment is this
    url

# Generated at 2022-06-14 15:44:24.058211
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .test_utils import TestDownloader, FakeYDL
    class HlsFDTest(HlsFD, TestDownloader):
        def __init__(self, ydl):
            TestDownloader.__init__(self, ydl)
            HlsFD.__init__(self, ydl, {}, {})
    ydl = FakeYDL()
    HlsFDTest(ydl)


if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:45:33.095520
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    import os

    # We don't want any output to the command line
    import logging
    logger = logging.getLogger('youtube_dl')
    logger.disabled = True

    # Use a stub version of YoutubeDL to avoid dependency on the real version
    class YoutubeDLStub:
        def __init__(self, test_case):
            self.test_case = test_case

        def urlopen(self, url):
            return urllib.request.urlopen(url)

        def to_screen(self, text):
            pass

        def report_warning(self, text):
            pass

        def report_error(self, text):
            self.test_case.assertTrue(False, text)


# Generated at 2022-06-14 15:45:39.837264
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import requests
    import tempfile
    import os
    # Create a temporary file for testing
    fd, path = tempfile.mkstemp()
    os.close(fd)

    # Download a playlist
    ydl_opts = {
        'test':True,
        'logtostderr':True,
        'hls_prefer_native':True,
    }
    ctx = {
        'infos': [{
            'id': 'jq3qDBhTTZQ',
            'title': 'VIDEO TEST',
            'url': 'https://example.com/jq3qDBhTTZQ.m3u8'
        }],
        'params': ydl_opts,
    }
    req = requests.get(ydl_opts['url'])
    req.raise_

# Generated at 2022-06-14 15:45:44.670527
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import get_info_extractor
    from ..downloader.common import FileDownloader

    def test_download(outfd, manifest, info_dict=None):
        if info_dict is None:
            info_dict = get_info_extractor('generic').suitable(manifest)
        if info_dict is None:
            return False
        # Create a FileDownloader instance
        fd = FileDownloader(params={'nopart': True, 'quiet': True, 'outtmpl': '-'})
        # Create a FileDownloaderProcessor
        fdp = fd.get_postprocessor(filename=None)
        # Create an HlsFD instance
        hls_fd = HlsFD(fd, params={'nopart': True, 'quiet': True})

# Generated at 2022-06-14 15:45:54.381090
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .extractor.common import InfoExtractor
    from .youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    class HlsMockIE(InfoExtractor):
        def _real_initialize(self):
            self.playlist_id = '267836174'

        def _real_extract(self, url):
            try:
                self.url = url
                return {'_type': 'url', 'url': url, 'ie_key': 'HlsMock'}
            except NameError:
                print('FFmpegFD is not installed')

    ie = HlsMockIE(ydl, {})

# Generated at 2022-06-14 15:46:03.178463
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import sys
    import shutil
    import tempfile
    import unittest
    from .common import FakeYDL
    from .test_downloader import MockHttpServerRule
    from .extractor.generic import GenericIE
    from .compat import is_py2

    class HlsManifestTest(unittest.TestCase):
        def setUp(self):
            self.test_dir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.test_dir)

        def assertExistsAndHasSize(self, path, size):
            self.assertExists(path)
            self.assertEqual(os.path.getsize(path), size)


# Generated at 2022-06-14 15:46:06.430085
# Unit test for constructor of class HlsFD
def test_HlsFD():
    ydl = downloader.YoutubeDL()
    ydl.params = {'format': '270+137'}
    with HlsFD(ydl, {}) as fd:
        assert fd.format == '270+137'

# Generated at 2022-06-14 15:46:14.650512
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import unittest
    import os.path
    import warnings

    warnings.filterwarnings('ignore', category=ResourceWarning, message='unclosed.*<ssl.SSLSocket.*>')
    warnings.filterwarnings('ignore', category=PendingDeprecationWarning, module=r'urllib3\.contrib\.pyopenssl')

    class HlsFDRealDownloadTests(unittest.TestCase):
        def setUp(self):
            sys.modules['__main__'].params = {
                'test': True,
                'quiet': True,
            }
            self.HlsFD = HlsFD
            self.HlsFD_can_download = self.HlsFD.can_download
            self.HlsFD.can_download = lambda *args: True


# Generated at 2022-06-14 15:46:23.533628
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    from .test import get_testcases_api_urls
    from .common import fake_urlopen
    from .external import FFmpegFD
    from ..utils import (
        encodeFilename,
    )
    from ..compat import (
        compat_urllib_error,
    )

    fake_urlopen_instance = fake_urlopen()
    fake_urlopen_instance.register_handler('http://www.yt-dl.org/api/get_video_info', get_testcases_api_urls)

# Generated at 2022-06-14 15:46:29.926729
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..utils import get_cachedir
    from .external import FFmpegFD
    class Ydl:
        def __init__(self):
            self.params = {
                'cachedir': get_cachedir(),

                'fragment_retries': 3,
                'skip_unavailable_fragments': True,
                'test': False,

                'hls_use_mpegts': True,
            }
            self.cache = {}
        def to_screen(self, *args, **kwargs):
            pass
        def trouble(self, *args, **kwargs):
            pass
        def report_warning(self, *args, **kwargs):
            pass
        def report_error(self, *args, **kwargs):
            pass

# Generated at 2022-06-14 15:46:35.303451
# Unit test for constructor of class HlsFD
def test_HlsFD():
    url = 'http://localhost:8081/hls/index.m3u8'
    ydl = YoutubeDL({})
    frag_fd = HlsFD(ydl, {'test': True})
    info_dict = {
        'id': 'test',
        'extractor': 'test',
        'url': url,
        'title': 'test'
    }
    frag_fd.real_download('test.mp4', info_dict)