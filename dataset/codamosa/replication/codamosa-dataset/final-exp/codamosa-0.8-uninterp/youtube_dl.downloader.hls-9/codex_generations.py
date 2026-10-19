

# Generated at 2022-06-14 15:37:54.218684
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import shutil
    import json
    import youtube_dl.utils
    import youtube_dl.YoutubeDL
    filename = None

# Generated at 2022-06-14 15:38:06.256079
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import sys
    import unittest

    sys.modules['pycrypto'] = None


# Generated at 2022-06-14 15:38:13.558987
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .downloader import Downloader
    from .extractor import gen_extractors
    from .extractor.common import InfoExtractor
    from .postprocessor.ffmpeg import FFmpegMergerPP
    from .postprocessor import PostProcessor

    # Introduce a class that overrides the constructor of InfoExtractor
    # and inherits the constructors of Downloader, FFmpegMergerPP, PostProcessor
    class MyIE(InfoExtractor):
        def __init__(self, ydl):
            super(MyIE, self).__init__(ydl)
            super(Downloader, self).__init__()
            super(FFmpegMergerPP, self).__init__()
            super(PostProcessor, self).__init__()

    # Retrieve the original _download_fragment method
    original_download_fragment

# Generated at 2022-06-14 15:38:15.426564
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD(None, {'test': True})



# Generated at 2022-06-14 15:38:28.565570
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from testing.test_utils import FakeYDL
    from testing.test_utils import FakeHttpServer
    import tempfile
    # Create temporary directory to store files
    temp_dir = tempfile.mkdtemp()
    test_enc_data = b'\xd0\xe8\xe4\xfd\x0e\xc4\x8c\xf2\x88\xbe\xe1\x8c\x05\xdf\xe9\xab'
    # Create a http server
    http_server = FakeHttpServer(temp_dir)
    # Generate test chunklist
    man_url = 'http://127.0.0.1:9999/chunklist.m3u8'
    with open(temp_dir + '/chunklist.m3u8', 'wb') as f:
        f.write

# Generated at 2022-06-14 15:38:38.605151
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..utils import HEADRequest
    my_ie = InfoExtractor()
    my_fd = HlsFD(my_ie, {'username': 'user', 'password': 'pass', 'noprogress':True})

    def my_urlopen(request):
        return {
            HEADRequest(u'http://localhost:8080/baz.m3u8'): {
                'status': 200,
                'location': u'localhost:8080/baz2.m3u8'
            },
            HEADRequest(u'http://localhost:8080/baz2.m3u8'): {
                'status': 200
            }
        }[request]

# Generated at 2022-06-14 15:38:51.199637
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .utils import FakeYDL
    ydl = FakeYDL()
    params = {
        'noprogress': True,
        'format': '135',
        'test': True,
        'simulate': True,
    }
    fd = HlsFD(ydl, params)
    info_dict = {
        'url': 'https://example.com/man.m3u8',
    }
    # No fragments
    assert fd.real_download('filename', info_dict)
    assert not ydl.download_retcode
    # Fake data
    fd.ctx['frags_total'] = 3
    fd.ctx['frag_index'] = 0
    fd.ctx['frag_content'] = b'abc'

# Generated at 2022-06-14 15:39:02.323603
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .extractor.common import InfoExtractor

    url = 'http://zdf1615.live.cdn.bitgravity.com/ondemand/mp4:zdf/de/130722_3sat_poparound/de/133370_3sat_poparound_1200.mp4'
    assert HlsFD.can_download(url, InfoExtractor()) is True

    videopassword = 'http://daserste.hls.adaptive.level3.net/i/videoportal/Film/c_620000/622873/format,716451,716457,716450,716458,716459,.mp4.csmil/master_video_for_smarttv.m3u8?null=0'

# Generated at 2022-06-14 15:39:12.020080
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest
    import os.path
    import sys
    import json
    import io
    import shutil
    import tempfile

    # test url is the url of fragment 6, in the media m3u8 list of
    # https://devimages.apple.com.edgekey.net/streaming/examples/bipbop_4x3/gear2/prog_index.m3u8
    TEST_URL = 'https://devimages.apple.com.edgekey.net/streaming/examples/bipbop_4x3/gear2/fileSequence6.ts'
    TEST_KEY_URL = 'https://devimages.apple.com.edgekey.net/streaming/examples/bipbop_4x3/gear2/fileSequence6.key'
    TEST_MANIFEST

# Generated at 2022-06-14 15:39:23.456506
# Unit test for constructor of class HlsFD

# Generated at 2022-06-14 15:39:40.178264
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .abc import FD_NAME, real_download
    assert HlsFD.FD_NAME == FD_NAME
    assert HlsFD.real_download == real_download


# Generated at 2022-06-14 15:39:48.216332
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # Create a fake YoutubeDL object
    class FakeYDL:
        def __init__(self):
            self.params = {'fragment_retries': 0}
            self.urlopen_calls_left = 2
        def urlopen(self, url):
            if self.urlopen_calls_left == 0:
                raise Exception('urlopen called more times than expected')
            self.urlopen_calls_left -= 1
            if self.urlopen_calls_left == 1:
                return open('tests/testdata/hls_test1-frag1', 'rb')
            else:
                return open('tests/testdata/hls_test1-manifest', 'rb')
    # Create a FakeLogger object
    class FakeLogger:
        def __init__(self):
            self.info

# Generated at 2022-06-14 15:39:49.202975
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert can_decrypt_frag

# Generated at 2022-06-14 15:39:56.894828
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_test_data
    from .utils import encodeFilename
    from .extractor.common import InfoExtractor
    from .extractor.generic import GenericIE
    import tempfile

    # First, download the media
    ie = InfoExtractor(params={'noplaylist': True, 'test': True}, downloader=None, youtube_dl=None)
    ie.add_info_extractor(GenericIE())
    url = 'https://d3e2bxwvkx7zhr.cloudfront.net/video/92932/high.m3u8?f=sample'
    manifest = get_test_data('hls/manifest.m3u8', False)

# Generated at 2022-06-14 15:40:01.736281
# Unit test for constructor of class HlsFD
def test_HlsFD():
    '''Class HlsFD is created'''
    import sys
    sys.modules['youtube_dl.downloader.hls'] = sys.modules['__main__']
    from youtube_dl.downloader.hls import HlsFD
    HlsFD(object(), object())
    assert True

# Generated at 2022-06-14 15:40:14.811031
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class FakeYDL:
        def __init__(self, test_data):
            self.test_data = test_data
            self.urlopen_result = None
            self._open = None

        def urlopen(self, url):
            class FakeUrlHandle:
                def __init__(self, url, content):
                    self.url = url
                    self.content = content

                def geturl(self):
                    return self.url

                def read(self, *args):
                    return self.content
            return FakeUrlHandle(url, self.test_data[url])

    # Test all functionality except extra_param_to_segment_url and _decryption_key_url
    # since they require extra package dependency to run the test

# Generated at 2022-06-14 15:40:26.863387
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Unit test for class HlsFD """
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.compat import html_to_unescape as unescape

    hls_test_data = unescape(
        r'''#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
media-01.ts
#EXT-X-ENDLIST''')

    # test for method can_download
    def can_download_test(manifest, info_dict):
        """ Test method can_download """
        return HlsFD.can_download(manifest, info_dict)

    assert can_download_test(hls_test_data, {'url': 'http://test.com/test.m3u8'})

# Generated at 2022-06-14 15:40:36.950909
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_testdata


# Generated at 2022-06-14 15:40:48.085670
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:40:58.939711
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    sys.modules['youtube_dl.extractor.utils'] = sys.modules['youtube_dl.extractor.utils.mock']
    sys.modules['youtube_dl.YoutubeDL'] = sys.modules['youtube_dl.YoutubeDL.mock']
    sys.modules['youtube_dl.aes'] = sys.modules['youtube_dl.aes.mock']

    from .mock import MockYDL
    from .mock import MockFragmentFD
    from .mock import _real_download_mock as _real_download
    from .mock import _download_fragment_mock as _download_fragment
    from .mock import _download_fragments_mock as _download_fragments

    import youtube_dl.extractor.utils.mock

# Generated at 2022-06-14 15:41:19.068879
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import shutil
    import tempfile
    import subprocess
    import os
    import sys

    TEST_OUT_FILENAME = 'HlsFD_real_download.m4s'
    TEST_OUT_FILENAME_UNFINISHED = 'HlsFD_real_download.unfinished.m4s'


# Generated at 2022-06-14 15:41:28.642259
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():

    from .testutils import FakeYDL
    from .extractor.common import InfoExtractor
    from .compat import compat_struct_pack
    from .utils import write_json_file
    from .extractor import HLSDownloader
    from .downloader.common import FileDownloader
    from .downloader.external import ExternalFD
    import hashlib
    import os

    #Compute a fragment download using method _download_fragment
    class HlsFD_real_download_test(HlsFD):

        def __init__(self, ydl, info_dict):
            #Instance of class YDL
            self.ydl = ydl
            #Instance of class InfoDict
            self.info_dict = info_dict
            #Instance of class HLSDownloader

# Generated at 2022-06-14 15:41:39.063885
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import shutil
    from .test import get_test_data_file
    from .downloader import YoutubeDL
    test_manifest = get_test_data_file('hls-manifest.m3u8')
    ydl = YoutubeDL()
    ydl.params.update({
        'skip_download': True,
        'nooverwrites': True,
        'quiet': True,
        'logger': ydl,
        'test': True,
        'frag_index': 1,
    })
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(HlsFD())

    import tempfile
    filename = next(tempfile._get_candidate_names())
    filename = os.path.join(tempfile.gettempdir(), filename)

    #

# Generated at 2022-06-14 15:41:44.919330
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Unit test for constructor of class HlsFD """
    print('Testing HlsFD constructor...')
    adict = {'url': 'https://test_url'}
    assert HlsFD.can_download(adict) == True
    adict = {'url': 'https://test_url', '_decryption_key_url': 'https://test_key_url'}
    assert HlsFD.can_download(adict, adict) == False
    print('Tested')

# Generated at 2022-06-14 15:41:57.855198
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..extractor.common import InfoExtractor
    def can_download_helper(manifest, info_dict):
        ie = InfoExtractor(None)
        ie._sort_formats(info_dict['formats'], lambda x: x)
        ie.params = info_dict.get('params', {})
        ie.params['noplaylist'] = True
        return HlsFD.can_download(manifest, info_dict)
    assert can_download_helper(
        '#EXTM3U\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=50\npageUrl://low.m3u8\n#EXT-X-ENDLIST\n',
        {'formats': [{'format_id': 'low'}]}
    )


# Generated at 2022-06-14 15:42:06.712677
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .common import SOURCE_VIDEO
    from ..extractor import gen_extractors
    for ie in list(gen_extractors(SOURCES_HLS)):
        if isinstance(ie, HlsFD):
            url = SOURCES_HLS[ie.ie_key()]
            break

    info = {
        'url': url,
        # Remove the query parameter to prevent downloading
        'http_headers': {'Range': 'bytes=0-%d' % (SOURCE_VIDEO.size - 1)},
        'playlist_mincount': 1
    }
    ie = HlsFD(None, {})
    ie._prepare_url = lambda info_dict, url: url
    ie.real_download('test.mp4', info)


# Generated at 2022-06-14 15:42:08.457632
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD(None, {}).FD_NAME == 'hlsnative'

# Generated at 2022-06-14 15:42:18.530413
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..compat import compat_urllib_request

    req = compat_urllib_request.Request('https://gist.githubusercontent.com/rg3/77c729a5a7493ce65d6e/raw/d3b6c9c3ac3f6f24b6d57a6de003e2c8b1283e6e/gistfile1.txt')
    req.add_header('Accept', 'application/vnd.apple.mpegurl')
    response = compat_urllib_request.urlopen(req)
    manifest = response.read().decode()


# Generated at 2022-06-14 15:42:19.694305
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD(None, None)

# Generated at 2022-06-14 15:42:27.424835
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('', {'is_live': False})
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=AES-128', {'is_live': False})
    assert HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {'is_live': False})
    assert not HlsFD.can_download('#EXT-X-MEDIA-SEQUENCE:1', {'is_live': False})

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:43:10.364815
# Unit test for constructor of class HlsFD
def test_HlsFD():
    if __name__ != "__main__":
        return
    print("=============================================================")
    url = 'http://nitro.bbc.co.uk/content/hds/test/test1_video_only.f4m'
    FD_Hls = HlsFD(None, {'noprogress': True})
    print("FD_Hls.can_download(%s, {})" % url)
    print(FD_Hls.can_download(url, {}))
    print("FD_Hls.real_download(%s, {})" % url)
    print(FD_Hls.real_download(url, {}))

if __name__ == "__main__":
    test_HlsFD()

# Generated at 2022-06-14 15:43:21.406667
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import youtube_dl.extractor.http as http
    assert HlsFD.can_download("#EXTM3U", {'url': ''})
    assert not HlsFD.can_download("#EXTM3U\n#EXT-X-ALLOW-CACHE:NO", {'url': ''})
    assert not HlsFD.can_download("#EXTM3U\n#EXT-X-KEY:METHOD=AES-128", {'url': ''})
    assert not HlsFD.can_download("#EXTM3U\n#EXT-X-KEY:METHOD=AES-128\n#EXT-X-BYTERANGE:1704@0", {'url': ''})

# Generated at 2022-06-14 15:43:32.990383
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_testdata_file
    from .utils import get_max_filesize
    from .extractor import YoutubeDL
    from .extractor.common import InfoExtractor
    from .common import FileDownloader
    from .common import DownloadError
    from .utils import sanitize_open


# Generated at 2022-06-14 15:43:43.869584
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Set up mock ytdl object
    from ..extractor.common import InfoExtractor
    from ..utils import FakeYDL
    ie = InfoExtractor({})
    ydl = FakeYDL()
    ydl.add_info_extractor(ie)

    ydl_opts = {
        'hls_use_mpegts': True,
    }
    hlsFD = HlsFD(ydl, ydl_opts)
    assert hlsFD.params == {'use_mpegts': True, 'hls_prefer_native': True, 'test': False}
    assert hlsFD.use_mpegts is True

    # Test that we get the correct fragments URLs
    hlsFD = HlsFD(ydl, {})

# Generated at 2022-06-14 15:43:52.369163
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # Import required modules
    import tempfile
    import os
    import shutil
    import unittest
    import youtube_dl
    # Create temp directory for saving downloaded files
    temp_dir_path = tempfile.mkdtemp()
    # Name of file for test
    temp_file_name = 'temp_file.bin'
    # Path of file for test
    temp_file_path = os.path.join(temp_dir_path, temp_file_name)
    # Create test config for youtube-dl
    test_config = {
        'nopart': True,
        'test': True,
        'quiet': True,
        'outtmpl': temp_file_path,
    }
    # Create youtube_dl object
    test_ydl = youtube_dl.YoutubeDL(test_config)
    #

# Generated at 2022-06-14 15:43:59.022505
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U\n',{}) == True
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="https://what.ever.com/"',{}) == False
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-BYTERANGE',{})==False

# Generated at 2022-06-14 15:44:08.454389
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..compat import compat_str
    from ..utils import encode_compat_str
    from .fragment import (
        FragmentFD,
        _encodeFilename,
        _get_filename,
        _is_test,
    )
    from ..compat import md5

    # Create a mock YoutubeDL object
    class MockYoutubeDL(object):
        def __init__(self, params):
            self.params = params

        def prepare_filename(self, info_dict):
            return _encodeFilename(self, info_dict)

        def to_screen(self, s):
            print(s)

        def to_stdout(self, s):
            print(s)


# Generated at 2022-06-14 15:44:12.646138
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Following is needed to set up the fake instance of YoutubeDL
    class FakeYDL():
        def __init__(self):
            pass
        def params(self):
            return {}
    ydl = FakeYDL()

    # Construct an instance of HlsFD
    hlsfd = HlsFD(ydl, {})
    assert hlsfd.ydl == ydl
    assert hlsfd.params == {}

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:44:24.400909
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:44:31.672026
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .http import HttpFD
    from .external import ExternalFD
    from .ffmpeg import FFmpegFD

    def get_media_list(s):
        return [line.strip() for line in s.splitlines() if line.strip() and not line.startswith('#')]
    def show(msg):
        print(msg)
    def download(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, *__):
        pass
    def hook(a, b, c):
        pass

    hls_fd = HlsFD({}, {})

    # Test real_download, test delegated to FFmpegFD
    # Test 1: Test with live stream
   

# Generated at 2022-06-14 15:45:55.840757
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from youtube_dl.downloader import YoutubeDL
    from youtube_dl.options import Options
    from .fragment import DownloadError

    # Test for unsupported media.
    # 1. encrypted streams
    # 2. live streams
    # 3. media segments may be appended to the end of event media playlists
    opts = Options()
    opts.format('bestvideo[protocol^=http]/bestaudio[protocol^=http]')
    opts.noplaylist = True
    opts.quiet = True

    # 1. encrypted streams

# Generated at 2022-06-14 15:46:05.428692
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nhttp://example.com/seg1.ts\nhttp://example.com/seg2.ts',
    {'url': 'http://example.com/playlist.m3u8'})
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nhttp://example.com/seg1.ts\nhttp://example.com/seg2.ts',
    {'url': 'http://example.com/playlist.m3u8', 'is_live': True})

# Generated at 2022-06-14 15:46:08.408905
# Unit test for constructor of class HlsFD
def test_HlsFD():
    exec ('from youtube_dl.downloader.hls import HlsFD', globals())

    hlsfd_instance = HlsFD(None, None)
    assert hlsfd_instance.FD_NAME == 'hlsnative'

# Generated at 2022-06-14 15:46:16.576828
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import YoutubeDL
    from ..extractor.common import InfoExtractor
    from ..utils import fake_urlopen

    class FakeYdl(YoutubeDL):
        def urlopen(self, url):
            return fake_urlopen(self, url)

    ie = InfoExtractor()
    ie.URL_PATTERN = r'https?://.+'
    ie.add_info_extractor(r'(.*)', [{
        'url': 'https://example.org/index.m3u8',
        'playlist': False,
        'playlist_mincount': 1,
    }])
    ie._real_extract = lambda *args: {}

    ydl = FakeYdl({'hls_prefer_native': True, 'simulate': True})
    ydl.add_info_

# Generated at 2022-06-14 15:46:19.316972
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Unit test helper function """
    assert HlsFD.can_download('http://fakemanifest.com', {'url': 'http://fakemanifest.com'})

# Generated at 2022-06-14 15:46:26.878845
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    downloader = HlsFD(DummyYDL(), {'test': True})
    assert downloader.real_download('test.mp3', {'url': 'test.m3u8'})
    assert downloader.real_download('test.mp3', {
        'url': 'test.m3u8',
        'http_headers': {'User-Agent': 'user-agent'}
    })
    assert not downloader.real_download('test.mp3', {
        'url': 'test.m3u8',
        'extra_param_to_segment_url': 'something'
    })

# Generated at 2022-06-14 15:46:35.656144
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .downloader import Downloader
    from .cache import FileCache
    from .extractor import gen_extractors

    ydl_opts = {
        'hls_prefer_native': True,
        'keepvideo': True,
    }
    ie = gen_extractors(ydl_opts)
    ie[0]._real_initialize()
    ie[0]._downloader = Downloader(ydl_opts, ie[0].ydl, FileCache(ydl_opts), ie[0])
    ie[0].params = ydl_opts
    ie[0]._type = 'hls'

    url = 'https://media.example.com/foo/bar/baz.m3u8'

# Generated at 2022-06-14 15:46:42.558882
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .downloader import HlsFD
    from .extractor import YoutubeIE
    from .ydl import FileDownloader

    class DummyInfoDict:
        pass

    info_dict = DummyInfoDict()

    manifest = """
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:1
#EXTINF:10.00000,
fileSequence1.ts
#EXTINF:10.00000,
fileSequence2.ts
#EXTINF:10.00000,
fileSequence3.ts
#EXTINF:10.00000,
fileSequence4.ts
#EXTINF:10.00000,
fileSequence5.ts
#EXT-X-ENDLIST
    """

    ie = YoutubeIE(FileDownloader())
   

# Generated at 2022-06-14 15:46:51.791946
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('', {'is_live': False})
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {'is_live': False})
    assert not HlsFD.can_download('#EXT-X-KEY:METHOD=NONE', {
        'is_live': True,
    })
    assert not HlsFD.can_download(
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="https://priv.example.com/key.php"',
        {
            'is_live': False,
        })

# Generated at 2022-06-14 15:46:59.628884
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    """
    Test with a hardcoded manifest
    """