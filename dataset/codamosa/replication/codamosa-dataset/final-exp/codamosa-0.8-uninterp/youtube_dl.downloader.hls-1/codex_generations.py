

# Generated at 2022-06-14 15:37:48.891836
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import encodeFilename

    from .hls import HlsFD

    from .fragment import FragmentFD
    from .external import FFmpegFD

    import tempfile
    import os
    import shutil
    from .common import FakeYdl

    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    url = 'https://video-dev.github.io/streams/x36xhzz/x36xhzz.m3u8'
    tmpdir = tempfile.mkdtemp()
    test_file = os.path.join(tmpdir, 'test.ts')

# Generated at 2022-06-14 15:38:01.943768
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..downloader.common import FileDownloader
    from ..extractor.common import InfoExtractor
    from ..utils import SearchInfoExtractor
    from .common import (
        BaseTest,
        BaseTestDownload,
        MockYDL,
        PAGES,
        NO_DEFAULT,
        mock_get_content
    )

    class MockHlsFD(HlsFD):
        """
        A mock version of HlsFD class used for unit testing
        """
        def _download_fragment(self, ctx, frag_url, info_dict, headers):
            """
            Returns a tuple of whether the download was success and the data
            downloaded
            """

# Generated at 2022-06-14 15:38:11.292841
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    import tempfile
    import shutil
    import os
    import sys
    from ..compat import (
        compat_cookiejar,
        compat_urlopen,
        compat_urllib_parse_urlparse,
    )
    from ..YoutubeDL import YoutubeDL
    from ..utils import (
        encodeFilename
    )

    def _make_ydl(*args, **kwargs):
        options = dict(
            quiet=True,
            no_warnings=True,
            forceurl=True,
            forcetitle=True,
            forceid=True,
            force_generic_extractor=True,
            simulate=True,
            skip_download=True
        )
        options.update(kwargs)
        ydl = YoutubeDL(options)
        ydl.add_default_info_extractors()


# Generated at 2022-06-14 15:38:24.845595
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .test import get_testdata_files_path

    # Test HlsFD constructor
    hlsfd = HlsFD(None, None)

    # Test can_download method
    manifest = open(get_testdata_files_path(
        'hls/hls_manifest_multiple_bitrates.m3u8')).read().decode('utf-8', 'ignore')
    info_dict = {'url': 'http://example.com/example.m3u8'}
    assert hlsfd.can_download(manifest, info_dict) == True

    manifest = open(get_testdata_files_path(
        'hls/hls_bcast_enc.m3u8')).read().decode('utf-8', 'ignore')

# Generated at 2022-06-14 15:38:36.304026
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .external import ExternalFD
    from ..__main__ import parseOpts
    from ..utils import encode_compat_str
    url = 'https://m.youtube.com/watch?v=5pJJu5R1YHg'
    opts = [
      '--hls-use-mpegts',
      '--hls-prefer-native',
      '--hls-prefer-ffmpeg',
      '--rm-cache-dir',
      '--write-info-json',
      '--continue-percent', '0',
      '--ignore-errors',
      '--verbose',
      '--test',
      '--output', '%(id)s.%(ext)s',
    ]
    opts.append(url)
    opts = parseOpts(opts)

# Generated at 2022-06-14 15:38:49.416374
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors
    from ..utils import choose_extractor
    from ..YoutubeDL import YoutubeDL
    from subprocess import Popen, PIPE
    from tempfile import mkstemp

    url = 'http://devimages.apple.com/iphone/samples/bipbop/gear1/prog_index.m3u8'
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    ext = choose_extractor(ydl, url)

    assert isinstance(ext, HlsFD)
    assert ext.get_real_url(url) == url

    # Test download with HLSNative
    tmp_file = mkstemp()[1]
    with ydl:
        ydl.download([url])

# Generated at 2022-06-14 15:38:53.891324
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .dashsegments import DashSegmentsFD
    from .http import HttpFD

    ydl = DummyYDL()
    ydl.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': False,
        'test': True,
    }
    fd = HlsFD(ydl, ydl.params)
    kwargs = {
        'url': 'url',
        'player_url': 'player_url',
        'protocol': 'hls_native',
        'ext': 'mp4',
    }


# Generated at 2022-06-14 15:39:04.508857
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:39:09.303611
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.youtube import YoutubeIE
    ydl = YoutubeIE()
    fd = HlsFD(ydl, {'fragment_base_url': 'http://example.com/'})
    assert fd.ydl is ydl
    assert fd.params['fragment_base_url'] == 'http://example.com/'



# Generated at 2022-06-14 15:39:21.612422
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..utils.re import match_re
    from ..extractor import YoutubeDL

    assert match_re(HlsFD.can_download('', {
        'url': '',
        'http_headers': {},
        'ext': 'mp4',
        'start_time': 0,
    }), r'^The following m3u8 features are not supported: ')


# Generated at 2022-06-14 15:39:46.243867
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import shutil
    import tempfile
    import unittest.mock as mock

    from .downloader import MockYoutubeDL

    with tempfile.NamedTemporaryFile(mode='w+t', encoding='utf-8') as f:
        dl = MockYoutubeDL({
            'outtmpl': f.name,
            'hls_prefer_native': True,
            'test': True,
        })

        def _download_fragment(*args, **kwargs):
            return True, args[0]['filename'].encode('utf-8')

        def _report_warning(*args, **kwargs):
            raise AssertionError()


# Generated at 2022-06-14 15:39:55.297410
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    import tempfile
    import os
    import shutil
    import youtube_dl.utils

    class HlsFDTest(unittest.TestCase):
        def get_content_of_file(self, file_name):
            with open(file_name, 'rb') as f:
                content = f.read()
            return content

        def test_case_1(self):
            temp_dir = tempfile.mkdtemp(prefix='ytdl_test_')
            temp_file_name = os.path.join(temp_dir, 'temp.ts')

# Generated at 2022-06-14 15:40:07.797885
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:40:11.962208
# Unit test for constructor of class HlsFD
def test_HlsFD():

    hlsfd = HlsFD(None, None)
    assert hlsfd.FD_NAME == "hlsnative"

    print ("Successfully passed all test cases for constructor of class HlsFD")

# Generated at 2022-06-14 15:40:24.551594
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    import unittest

    import re
    import math
    import tempfile

    from .fragment import FragmentFD

    from ..utils import (
        encode_data_uri,
        write_json_file,
    )

    class HlsFDTest(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.manifest_fds = []
            cls.manifest_paths = []
            cls.manifest_urls = []

            # Generate random manifests

# Generated at 2022-06-14 15:40:32.547420
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from youtube_dl import YoutubeDL
    from youtube_dl.utils import std_headers
    from youtube_dl.YoutubeDL import YoutubeDL
    class DummyYDL(YoutubeDL):
        def __init__(self, params):
            self.params = params
            self.cache = None
            self.to_screen = None
            self.to_stderr = None
            self.to_console_title = None
            self.debug = None
            self.server_socket = None
            self.download_retcode = None

# Generated at 2022-06-14 15:40:45.842832
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import EDLr
    edlr = EDLr.EDLr()
    assert edlr.set_hls_uri('https://dvhnwjs7jlwj2.cloudfront.net/out/v1/f1b253a11cec4e2d816c6ac77e6efa7a/index.m3u8',
                            'index.m3u8') == 0, 'Did not find HLS media'
    assert edlr.download() == 0, 'Downloading HLS media failed'
    assert edlr.seek(-1000) == 0, 'Seeking to -1000ms failed'
    assert abs(edlr.tell() + 1000) < 2, 'Telling position failed'
    assert edlr.seek(0) == 0, 'Seeking to 0ms failed'

# Generated at 2022-06-14 15:40:57.350042
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .external import FFmpegFD
    from ..youtube_dl.extractor import YoutubeDL
    from ..utils import strip_jsonp, unescapeHTML
    from ..compat import compat_str
    import json
    import os
    import sys

    # Check that the function can_download(manifest, info_dict) of HlsFD class
    # classifies manifests correctly
    def can_download(manifest, info_dict):
        if FFmpegFD.can_download(manifest, info_dict):
            return True
        elif HlsFD.can_download(manifest, info_dict):
            return False
        else:
            assert False, 'Impossible'

    # Check that the manifests are downloaded correctly

# Generated at 2022-06-14 15:41:03.971713
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..utils import _test_proto_relative_urls
    from ..extractor.common import InfoExtractor
    from ..extractor.generic import GenericIE
    from ..compat import is_py2
    import shutil
    import tempfile
    import os
    if is_py2:
        from StringIO import StringIO
    else:
        from io import StringIO
    from .external import ExternalFD

    def _download(url, m3u8_content):
        ie = InfoExtractor(GenericIE())
        ie.params = {'skip_unavailable_fragments': '1'}
        ie._cache = {'manifest': url}
        ie._downloader = DummyYdl()

# Generated at 2022-06-14 15:41:15.942862
# Unit test for constructor of class HlsFD

# Generated at 2022-06-14 15:41:43.661409
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD._can_download('key=val,foo=bar', {'is_live': False})


# Generated at 2022-06-14 15:41:57.114894
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({
        'logger': YoutubeDL.debug_print,
        'fragment_retries': 10,
        'skip_download': True,
    })
    assert HlsFD.can_download('#EXTM3U\nhttps://foo.bar/baz.ts\n#EXT-X-ENDLIST', {})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI=https://foo.bar/baz.key\nhttps://foo.bar/baz.ts\n#EXT-X-ENDLIST', {})

# Generated at 2022-06-14 15:42:05.248467
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .external import ExternalFD
    from .dash import DashSegmentsFD
    from ..extractor import DummyIE
    from ..post import PostProcessor

    # Check for ffmpeg
    info_dict = {'url': 'http://foo.com'}
    assert not HlsFD.can_download('abc', info_dict)
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=FOO', info_dict)
    assert HlsFD.can_download('#EXT-X-KEY:METHOD=AES-128', info_dict)
    assert HlsFD.can_download(
        '#EXT-X-KEY:METHOD=AES-128\n'
        'https://example.com/index.m3u8', info_dict)

# Generated at 2022-06-14 15:42:16.670983
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    # Test method can_download of class HlsFD
    manifest = '''
    #EXTM3U
    #EXT-X-KEY:METHOD=AES-128,URI="https://priv.example.com/key.php?r=52"
    #EXTINF:2.833,
    http://media.example.com/fileSequence52-A.ts
    #EXTINF:15.0,
    http://media.example.com/fileSequence52-B.ts
    #EXTINF:13.333,
    http://media.example.com/fileSequence52-C.ts
    '''
    info_dict = {'url': 'manifest_url', '_decryption_key_url': 'key_url'}
    assert HlsFD.can_download(manifest, info_dict)

# Generated at 2022-06-14 15:42:27.593002
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=FOO', {})
    assert HlsFD.can_download(
        '#EXT-X-KEY:METHOD=AES-128\n'
        'https://something.com/fileSequence1.ts\n'
        'https://something.com/fileSequence2.ts\n'
        'https://something.com/fileSequence3.ts\n',
        {})

    if can_decrypt_frag:
        assert HlsFD.can_download(
            '#EXT-X-KEY:METHOD=AES-128\n'
            '#EXT-X-BYTERANGE:121090@0\n'
            'https://something.com/fileSequence1.ts\n',
            {})

# Generated at 2022-06-14 15:42:38.286351
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import json
    import os
    import tempfile
    import unittest
    from .downloader import YoutubeDL
    from .external import FFmpegPostProcessor
    from .f4m import get_base_url
    from .extractor import get_info_extractor


# Generated at 2022-06-14 15:42:46.440376
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    fd = HlsFD(ydl, ydl.params)
    assert fd.params is fd.ydl.params
    assert ydl.params is not fd.params
    # We do not want to alter the original params object
    fd.params['fragment_retries'] = 3
    assert ydl.params['fragment_retries'] != 3
    fd.params['skip_unavailable_fragments'] = True
    assert ydl.params['skip_unavailable_fragments'] is not True
    assert fd.params['noprogress'] is False
    fd.params['noprogress'] = True
    assert fd.params['noprogress'] is True

# Generated at 2022-06-14 15:42:57.386389
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    Very basic unit test that ensures that the method real_download of class HlsFD is
    at least executed without throwing any exception.
    """
    import youtube_dl
    import os
    import tempfile
    import shutil
    from youtube_dl.utils import encode_compat_str

    ydl_opts = {'restrictfilenames': True, 'noplaylist': True}
    video_url = 'https://videos.com/videoID'
    video_url = encode_compat_str(video_url)

# Generated at 2022-06-14 15:43:04.683734
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download(
        '#EXTM3U\n'
        '#EXTINF:10,\n'
        'http://media.example.com/segment1.ts\n'
        '#EXTINF:10,\n'
        'http://media.example.com/segment2.ts\n'
        '#EXTINF:10,\n'
        'http://media.example.com/segment3.ts\n'
        '#EXT-X-ENDLIST\n',
        {
            'url': 'https://example.com/',
            'http_headers': {'foo': 'bar'},
            'extra_param_to_segment_url': '',
            '_decryption_key_url': '',
        },
    )


# Generated at 2022-06-14 15:43:16.601935
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_test_data
    from .extractor import gen_extractors

    video_id = 'testvideo'
    youtube_ie = gen_extractors()[0]
    ydl_data = {'usenetrc': '', 'username': '', 'password': '', 'quiet': True}
    test_data = get_test_data(['testvideo'], youtube_ie, ydl_data)
    info_dict = test_data['testvideo'][0]
    info_dict.update({'format': 'hls'})
    result = HlsFD(test_data, ydl_data).real_download('testvideo', info_dict)
    assert result is True
    # The first fragment downloaded must be the same as the second fragment

# Generated at 2022-06-14 15:44:24.442643
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('', {})  # pylint: disable=protected-access
    assert HlsFD.can_download('#EXTM3U', {})  # pylint: disable=protected-access
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD="NONE"', {})

    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-BYTERANGE', {})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:1', {})
    assert not HlsFD.can_download('#EXTM3U\n#EXT-X-PLAYLIST-TYPE:EVENT', {})

# Generated at 2022-06-14 15:44:30.502081
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    class test_HlsFD(HlsFD):
        def __init__(self):
            self.manifest = ''
        @staticmethod
        def can_download(manifest, info_dict):
            return super(test_HlsFD, self).can_download(manifest, info_dict)

    hls_test = test_HlsFD()
    # m3u8 manifest with no EXT-X-KEY
    hls_test.manifest = '#EXTM3U\n#EXT-X-VERSION:3\n'
    assert hls_test.can_download(hls_test.manifest, {})

    # m3u8 manifest with no supported KEY METHOD
    hls_test.manifest += '#EXT-X-KEY:METHOD=UNSUPPORTED\n'
    assert not hls_

# Generated at 2022-06-14 15:44:42.213854
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .fragment import FragmentFD
    from .external import FFmpegFD
    from ..utils import (
        encode_base_n,
    )
    import os
    os.umask(0)
    import tempfile
    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.close()

# Generated at 2022-06-14 15:44:50.571996
# Unit test for constructor of class HlsFD
def test_HlsFD():
    hlsfd = HlsFD(None, {'skip_unavailable_fragments': True})

# Generated at 2022-06-14 15:44:59.494222
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import FakeYDL

    # Test HlsFD._download_fragment
    def test_download_fragment(urlh, fragment_downloader, ctx=None, info_dict=None, headers=None):
        assert_equal('https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', urlh.get_full_url())

    HlsFD._download_fragment = test_download_fragment

    # Test HlsFD._finish_frag_download
    def test_finish_frag_download(_):
        assert_equal(1, 1)

    HlsFD._finish_frag_download = test_finish_frag_download

    # Test HlsFD._append_fragment
   

# Generated at 2022-06-14 15:45:06.440961
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download(r'#EXTM3U\n#EXTINF:1\nx\n#EXT-X-ENDLIST', {})
    assert HlsFD.can_download(r'#EXTM3U\n#EXTINF:1\nx\n#EXT-X-ENDLIST', {'extra_param_to_segment_url': 'foo'})
    assert not HlsFD.can_download(r'#EXTM3U\n#EXT-X-KEY:METHOD=AES-128\n#EXTINF:1\nx\n#EXT-X-ENDLIST', {})

# Generated at 2022-06-14 15:45:07.931784
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD({})


# Generated at 2022-06-14 15:45:09.545518
# Unit test for constructor of class HlsFD
def test_HlsFD():
    hls_fd = HlsFD(None, None)
    assert hls_fd

# Generated at 2022-06-14 15:45:16.740833
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import YoutubeDL
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    info_dic = ydl.extract_info('https://www.youtube.com/watch?v=N3vJtt63hW8', download=False)
    hls_fd = HlsFD(ydl, {'fragment_retries': 10})
    hls_fd.real_download('test.mp4', info_dic)

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:45:24.764652
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    youtube_dl_instance = YoutubeDL(params={'test': True})
    youtube_dl_instance.add_default_info_extractors()
    url = 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8'
    info_dict = { 'url': url, '_type': 'hls' }
    fd = HlsFD(youtube_dl_instance, {'test': True})
    assert fd.real_download('test.ts', info_dict)