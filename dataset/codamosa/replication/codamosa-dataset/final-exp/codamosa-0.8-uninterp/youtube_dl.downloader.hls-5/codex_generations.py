

# Generated at 2022-06-14 15:37:55.531815
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:37:56.401980
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD

# Generated at 2022-06-14 15:38:07.820632
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import YoutubeIE
    from ..downloader import YoutubeDL
    from ..utils import DateRange

    dl = YoutubeDL({
        'simulate': True,
        'format': 'bestvideo+bestaudio/best',
        'writesubtitles': True,
        'subtitleslangs': 'en',
        'noplaylist': True,
        'subtitlesformat': 'best',
        'dump_intermediate_pages': True,
    })
    inf_url = 'http://127.0.0.1:8888/test_url'


# Generated at 2022-06-14 15:38:21.262827
# Unit test for constructor of class HlsFD
def test_HlsFD():
    test_data = {
        'url': 'http://example/url.m3u8',
        'frag_index': 0,
        'total_frags': 4,
        'filename': 'filename.mp4'
    }
    test_HlsFD = HlsFD(None, None)
    test_HlsFD._prepare_and_start_frag_download(test_data)
    return (test_HlsFD.total_frags == test_data['total_frags'] and
        test_HlsFD.frag_index == test_data['frag_index'] and
        test_HlsFD.filename == test_data['filename'])

if __name__ == '__main__':
    print(test_HlsFD())

# Generated at 2022-06-14 15:38:33.544116
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import json
    import os
    import tempfile

    from ..extractor.common import InfoExtractor
    from ..utils import sanitize_open
    from .external import FFmpegFD

    _TEST_FILES_PATH = os.path.join(os.getcwd(), 'test', 'files')


# Generated at 2022-06-14 15:38:46.143557
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import os
    import tempfile
    test_data_dir = os.path.join(os.path.dirname(__file__), 'test_data')
    fragment_filename = os.path.join(test_data_dir, 'hls_fragment.ts')
    playlist_filename = os.path.join(test_data_dir, 'hls_playlist.m3u8')
    with tempfile.NamedTemporaryFile(suffix='.ts') as fh:
        fd = HlsFD(None, {'test': True})
        fd.real_download(fh.name, {'url': playlist_filename})

    with open(fragment_filename, 'rb') as fh:
        expected_content = fh.read()

# Generated at 2022-06-14 15:38:57.872764
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    import os
    import sys
    import tempfile
    import shutil

    def progress_hook_test(d):
        if d['status'] == 'finished':
            sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            sys.stdout.write('.')
            sys.stdout.flush()


# Generated at 2022-06-14 15:39:06.645532
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..extractor.common import InfoExtractor
    from ..utils import HEADRequest
    from ..compat import json

    # This function must be called when the main YouTube URL is requested.
    def _mock_ydl_urlopen(self, url):
        qs = compat_urlparse.parse_qs(compat_urlparse.urlparse(url).query)
        video_id = qs['v'][0]
        video_info = json.loads(
            InfoExtractor._download_webpage(
                self,
                'https://www.youtube.com/get_video_info?video_id=%s&el=info&ps=default&eurl=&gl=US&hl=en' % video_id,
                video_id))
        dash_manifest = video_info['dashmpd']

        #

# Generated at 2022-06-14 15:39:07.864938
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert isinstance(FdFactory.get_fd_by_name('hlsnative')(), HlsFD)

# Generated at 2022-06-14 15:39:15.130207
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_test_handler
    from .http import HttpFD
    from ..extractor import YoutubeIE


# Generated at 2022-06-14 15:39:46.032813
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import shutil
    import http.server
    import socketserver
    import threading

    os.environ['YOUTUBEDL_HLSNATIVE'] = '1'


# Generated at 2022-06-14 15:39:55.205150
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest

    from .conftest import get_test_data_file
    from ..downloader.common import FileDownloader

    class TestHlsFD(unittest.TestCase):

        @staticmethod
        def test():
            ydl = FileDownloader({
                'quiet': True,
                'outtmpl': '%(id)s.%(ext)s',
                'test': True,
            })

            url = get_test_data_file('hls/index-live.m3u8')
            url += '?extra_query=test'


# Generated at 2022-06-14 15:39:56.630729
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD(None, {'test': True})

# Generated at 2022-06-14 15:40:05.565245
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors
    from ..utils import FakeYDL
    from ..downloader.common import FileDownloader
    from ..downloader.f4m import F4mFD
    from ..downloader.hls import HlsFD

    extractors = gen_extractors()
    for e in extractors:
        if e.IE_NAME == 'Youtube':
            break

    # Download a DASH video
    dl = FileDownloader(FakeYDL(), {'simulate': True})
    dl.add_info_extractor(e)
    ie = e.extractors['Youtube'](dl)
    ie.extract('https://www.youtube.com/watch?v=Ik-RsDGPI5Y')
    assert dl.ydl.params['test']

# Generated at 2022-06-14 15:40:12.341808
# Unit test for constructor of class HlsFD
def test_HlsFD():
    print('HlsFD unit test')
    # Run tests using a mock ydl object
    ydl = YouTubeDL({})
    url = 'https://example.com/video.m3u8'
    hlsfd = HlsFD(ydl, {'url': url})
    assert hlsfd._url == url

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:40:15.494641
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.get_option_names() == {
        'keep_fragments'
    }


# Generated at 2022-06-14 15:40:27.399242
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import unittest
    from .http import HttpFD
    from ..utils import encodeFilename

    # Helper to create a HlsFD
    def create_HlsFD(url, filename, info_dict, http_headers={}):
        params = {
            'noprogress': True,
            'outtmpl': filename,
            'http_headers': http_headers,
        }
        ydl = None
        return HlsFD(ydl, params, info_dict, url)

    # Parse m3u8 manifest
    def parse_m3u8_manifest(manifest):
        m3u8_io = io.StringIO(manifest)
        return m3u8.load(m3u8_io)

    # Helper to obtain a fragment url
   

# Generated at 2022-06-14 15:40:37.181182
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import pytest
    from ..extractor.common import InfoExtractor
    from ..utils import determine_ext

    class FakeIE(InfoExtractor):
        IE_DESC = 'fake'

        def _real_extract(self, url):
            return {
                'id': 'fake',
                'url': 'http://fake.example.com/',
                'title': 'Fake Title',
                'thumbnail': 'http://fake.example.com/thumbnail.jpg',
                'description': 'Fake Description',
            }

    fake_ie = FakeIE('http://fake.example.com/')
    fake_ie._downloader = pytest.DummyYDL()  # use a dummy downloader so we don't download anything
    fake_ie.params = {'test': True}
    info = fake_ie._real_ext

# Generated at 2022-06-14 15:40:48.238600
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download(): # pragma: no cover
    import os
    from ..utils import urlopen

    from .common import FakeYDL

    ydl = FakeYDL()
    url = 'http://mocked.link/'
    query = 'id=jK7cJ8k-9Y0'

    # Test default case (unencrypted, not live)
    part_sizes = [1024]
    contents = [b'some data']

    def mocked_urlopen(url, data=None, headers=None):
        nonlocal part_sizes, contents
        if not part_sizes:
            raise AssertionError('Unexpected URL opened: ' + url)
        size = part_sizes.pop(0)
        content = contents.pop(0)

# Generated at 2022-06-14 15:40:52.900205
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_testdata_stream
    fd = HlsFD(get_testdata_stream('hls', '161041.m3u8'))
    assert fd.real_download('test.ts', {}) == True


# Generated at 2022-06-14 15:41:20.338680
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD('http://dummyurl/file.mp4')


# Generated at 2022-06-14 15:41:29.842529
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import tempfile
    import os
    import os.path
    import json
    import random
    import calendar
    import sys
    import datetime
    # we don't want to use youtube_dl.YoutubeDL as base class
    # because that would create a new downloader instance and
    # override configuration of this class
    from .downloader import Downloader

    class TestHlsFD(HlsFD):
        def __init__(self, downloader):
            super(TestHlsFD, self).__init__(downloader, {})

        def _download_fragment(self, ctx, frag_url, info_dict, headers):
            count = ctx['frag_download_count']
            ctx['frag_download_count'] += 1

            # Corrupt the first and the last fragment to test retries

# Generated at 2022-06-14 15:41:40.360694
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.generic import GenericIE
    from ..utils import determine_ext
    from .http import HttpFD

    # Test single-file HLS download
    instance = HlsFD(GenericIE(), {'format': 'best'})
    out_filename = 'test' + determine_ext(instance)

# Generated at 2022-06-14 15:41:49.348188
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import ytdl_hook
    import sys
    import json
    import os

    import unittest

    sys.modules['youtube_dl.extractor'] = ytdl_hook

    class TestHlsFdRealDownload(unittest.TestCase):

        TEST_DATA_DIR = '_test_data'

        def setUp(self):
            if not os.path.isdir(TestHlsFdRealDownload.TEST_DATA_DIR):
                os.mkdir(TestHlsFdRealDownload.TEST_DATA_DIR)

        def tearDown(self):
            for filename in os.listdir(TestHlsFdRealDownload.TEST_DATA_DIR):
                os.remove(os.path.join(TestHlsFdRealDownload.TEST_DATA_DIR, filename))


# Generated at 2022-06-14 15:42:00.195017
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    sys.path.append('tests')
    from unit_test_fragment_FD import write_test_file
    import tempfile

    url = 'http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8'
    ydl = MockYDL()
    ydl.params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': True,
        'test': True
    }

    tmpdir = tempfile.mkdtemp()
    test_filename = os.path.join(tmpdir, 'test.ts')
    write_test_file(url, test_filename, 'hlsnative')

    fd = HlsFD(ydl, {})

# Generated at 2022-06-14 15:42:07.198251
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    sys.path.append('tests/')

    from .test_utils import FakeYDL
    from .test_download import _test_download_url

    _test_download_url(
        HlsFD, 'Download URL',
        'https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8',
        '41026175911d4467f6a27c43a46bf6f8c6b9d6a2', False,
        params={'test': True, 'format': '0'},
        ydl_opts={'hls_prefer_native': True})


# Generated at 2022-06-14 15:42:15.668581
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    _res = HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-VERSION:3\n'
        '#EXT-X-TARGETDURATION:5220\n'
        '#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXTINF:5220,\n'
        'https://priv.example.com/fileSequence5219.ts\n'
        '#EXT-X-ENDLIST\n',
        {}
    )
    assert _res == True


# Generated at 2022-06-14 15:42:27.054677
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import re
    import tempfile
    import unittest
    from time import time
    from .test_download import DownloadUtilsMixin
    from .test_download import get_testcases_list

    format_id = 'hlsnative'

    class HlsFDTest(unittest.TestCase, DownloadUtilsMixin):
        def test_all_testcases_hlsnative(self):
            self.download_all_known_formats_for_test(format_id)

        def test_all_testcases_hlsnative_quality(self):
            self.download_all_known_formats_for_test(format_id, modify_url_query={'quality': '720p'})

        def test_all_testcases_hlsnative_limited_retries(self):
            self.download

# Generated at 2022-06-14 15:42:36.825736
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import Downloader
    from ..extractor import YoutubeIE
    from ..utils import std_headers
    dl = Downloader()
    dl.add_info_extractor(YoutubeIE(dl))
    ie = dl._ies[0]
    url = 'https://www.youtube.com/watch?v=WOtj9XZOaT0'
    ie.url = url
    info_dict = ie._real_extract(url)
    fd = HlsFD(dl, ie, {}, std_headers)
    assert fd.can_download(info_dict['formats'][0]['manifest_url'], info_dict)
    assert fd.FD_NAME == 'hlsnative'

# Generated at 2022-06-14 15:42:45.625561
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..utils import prepend_extension

    def create_m3u8_downloader(info_dict, params=None):
        ie = InfoExtractor(params)
        params = params or {}
        params.update(info_dict)
        return HlsFD(ie, params)

    def get_info_dict(url, ie=None, ie_key=None):
        ie = ie or InfoExtractor()
        ie.params = {}
        ie.url = url
        ie.report_warning = lambda msg: None
        ie.report_error = lambda msg: None
        ie_key = ie_key or ie.ie_key()
        if ie_key:
            ie._downloader = create_m3u8_downloader(ie.extract(url))
       

# Generated at 2022-06-14 15:43:52.594506
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .extractor.common import InfoExtractor
    from .extractor.youtube import YoutubeIE
    from .downloader.common import FileDownloader

    url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    ie = InfoExtractor(YoutubeIE.ie_key())
    manifest_url = ie._get_video_info(url)['url']
    info_dict = {
        'url': manifest_url,
        'http_headers': {
            'User-Agent': 'FakeUserAgent',
        },
    }
    fd = HlsFD(FileDownloader({'test': True}), {})

# Generated at 2022-06-14 15:44:04.145852
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.common import InfoExtractor
    from ..extractor.generic import GenericIE
    ie = InfoExtractor(GenericIE(), None)

    # Non-live stream
    ie._downloader.params['noprogress'] = True
    ie._downloader.params['test'] = True

# Generated at 2022-06-14 15:44:13.492375
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .tests.mocks.test_HlsFD_real_download import (
        result_video,
        result_audio,
        result_mux,
        audio_only_playlist,
        video_only_playlist,
        muxed_playlist,
        audio_only_playlist_with_key,
        video_only_playlist_with_key,
        muxed_playlist_with_key,
    )
    from .tests import YoutubeDL

    test_audio_only = lambda: test_HlsFD(
        audio_only_playlist, '',
        test=True, download=False, expected_fragments=result_audio)


# Generated at 2022-06-14 15:44:21.593137
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    sys.path += ['.', '..']
    from youtube_dl.YoutubeDL import YoutubeDL, YoutubeDLHandler
    from youtube_dl.utils import DownloadError
    from youtube_dl.extractor.common import InfoExtractor
    class MockIE(InfoExtractor):
        def __init__(self, ie_dir, ie_name, ie_id):
            super(MockIE, self).__init__({})
            self._type = 'Mock'
            self._downloader = YoutubeDL({'cachedir': False})
            self._ie_dir = ie_dir
            self._ie_name = ie_name
            self._ie_id = ie_id

        def report_warning(self, msg):
            pass

        def _real_initialize(self):
            pass


# Generated at 2022-06-14 15:44:23.439022
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .utils import real_download
    return real_download('hlsnative', HlsFD)

# Generated at 2022-06-14 15:44:31.055724
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000\nurl_0/index.m3u8', {})
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000\n#EXT-X-KEY:METHOD=AES-128\nurl_0/index.m3u8', {})

# Generated at 2022-06-14 15:44:33.370035
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    assert HlsFD.real_download('filename', {'url': 'test_url', 'http_headers': {}}) is True

# Generated at 2022-06-14 15:44:38.195460
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Test HlsFD constructor """
    import youtube_dl
    ydl = youtube_dl.YoutubeDL()
    fd = HlsFD(params=ydl.params, ydl=ydl)

    return fd

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:44:48.285689
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .http import HttpFD
    from .fragment import FragmentFD
    from .external import FFmpegFD
    from ..utils import compat_struct_pack as struct_pack


# Generated at 2022-06-14 15:44:57.593483
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import youtube_dl

    # Download first 5 fragments of playlist found in main/test/test.m3u8
    # For quick test use following command:
    # $ youtube-dl -v --test --fragment-retries 0 --no-progress
    #     --hls-prefer-native https://github.com/ytdl-org/youtube-dl/blob/83105b4/test/test.m3u8
    #
    # The test will fail on purpose if the downloaded fragments are not decrypted
    # and verified.

    # This is the encrypted fragments payload.
    # The decrypted fragments payload is 'real' in main/test/test_HlsFD_real_download.py
    # which is not included in the repository.
