

# Generated at 2022-06-14 15:37:53.811431
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import datetime
    import tempfile
    import os

    temp_dir = tempfile.mkdtemp(prefix=datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S'))+'/'
    HlsFD._test_base_dir = temp_dir
    manifest_url = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourfm.m3u8'
    manifest_file_path = os.path.join(temp_dir, 'bbc_radio_fourfm.m3u8')

# Generated at 2022-06-14 15:38:05.914934
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .ytdl import YoutubeDL
    params = {
        'format': '141/140',
        'skip_download': True,
    }
    ydl = YoutubeDL(params)
    hlsfd = HlsFD(ydl, params)
    if hlsfd.can_download(None, None):
        assert False, 'constructor of class HlsFD should check parameters, not passed'
    assert hlsfd.get_filename(None) == 'ydl-%(id)s-%(format_id)s.tmp'

    info_dict = {}
    assert HlsFD.can_download(None, info_dict)
    info_dict['is_live'] = True

# Generated at 2022-06-14 15:38:08.404740
# Unit test for constructor of class HlsFD
def test_HlsFD():
    info_dict = {}
    hlsFD = HlsFD(None, info_dict)
    assert(isinstance(hlsFD, HlsFD))


# Generated at 2022-06-14 15:38:22.515011
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import pytest
    from decimal import Decimal

    from .test_fragment import TestFragmentFD
    if not HlsFD.can_download:
        pytest.skip("HlsFD requires Crypto (pycryptodome)")

    info_dict = {
        'id': 'id',
        'ext': 'mp4',
        'title': 'title',
        'url': 'https://example.org/hls/manifest.m3u8',
    }
    hl = HlsFD(TestFragmentFD.ydl, TestFragmentFD.params)


# Generated at 2022-06-14 15:38:34.590844
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_test_data
    from .common import prepend_extension

    def _mocked_urlopen(url):
        filename = url.split('/')[-1]
        return get_test_data([filename, filename.replace('.m3u8', '_frag.ts')])

    def _test_download(test, manifest_name, expected_data):
        manifest = get_test_data([manifest_name])

        class MockedYDL:
            def __init__(self):
                self.urlopen = _mocked_urlopen

        fd = HlsFD(MockedYDL(), {'test': True})
        test.assertTrue(
            fd.real_download(prepend_extension(manifest_name, 'test_'), {'url': manifest.name}))

# Generated at 2022-06-14 15:38:43.622791
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader.common import FileDownloader

    # unit test for non-ffmpeg downloader
    ydl = FileDownloader({'hls_prefer_native': True})
    ydl.add_info_extractor(HlsFD)
    ydl.add_info_extractor(FFmpegFD)
    res = ydl.extract_info(
        'http://www.nasa.gov/multimedia/nasatv/NTV-Public-IPS.m3u8',
        download=False
    )
    assert res['extractor'] == 'hlsnative'

# Generated at 2022-06-14 15:38:45.689697
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('', {'is_live': False})

# Generated at 2022-06-14 15:38:57.489394
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # For tests we stub _download_fragment, _prepare_url, _append_fragment
    # and _finish_frag_download methods

    class fake_HlsFD(HlsFD):
        def _download_fragment(self, ctx, url, info_dict, headers):
            frag_index = ctx['fragment_index']
            # Mock the amount of data for the test
            if frag_index == 1:
                ctx['total_frags'] = 1
                ctx['frag_content_length'] = 1000
            elif frag_index == 2:
                ctx['frag_content_length'] = 100

# Generated at 2022-06-14 15:39:06.452415
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .tests.test_HlsFD import _mocked_urlopen
    from .tests.test_HlsFD import HlsFDCase
    from .tests.test_HlsFD import run_downloader
    from .extractor import gen_extractors
    from .downloader import gen_ydl

    # Prepare the testcase object
    testcase = HlsFDCase()

    def mocked_downloader_init(self, ydl):
        return
    def mocked_add_progress_hook(self, ph):
        return
    def mocked_download(self, filename, info_dict):
        testcase.extra_config({'url': 'http://example.com/hls.m3u8', 'hls_use_mpegts': True})
        ydl = gen_ydl(testcase.config)
        return

# Generated at 2022-06-14 15:39:08.148654
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .tests.test_downloader import get_testcases_for_all_FDs
    for t in get_testcases_for_all_FDs(HlsFD):
        yield t

# Generated at 2022-06-14 15:39:21.803582
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert can_decrypt_frag or not HlsFD.can_download('#EXT-X-KEY:METHOD=AES-128', {})

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:39:25.759691
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..downloader.common import FileDownloader
    from ..extractor import gen_extractors

    # generate a FileDownloader instance
    ydl = FileDownloader(params={'logger': None, 'nopart': True, 'quiet': True})
    ydl.add_default_info_extractors()

    # get HlsFD instance
    hls = [x for x in gen_extractors(ydl) if x.IE_NAME == 'hlsnative'][0]

    # test method can_download()

# Generated at 2022-06-14 15:39:36.811508
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from . import Options
    from .extractor import YoutubeIE
    from .downloader import common as dl_common
    from ..compat import compat_str
    from ..utils import read_batch_urls
    opts = Options()
    opts.format = 'best'
    opts.forcejson = 'false'
    opts.simulate = 'true'
    opts.outtmpl = 'test'
    opts.retries = '0'
    opts.test = 'true'
    opts.skip_download = 'false'

    urls_batch = read_batch_urls('test/test_urls/urls.txt')
    output_batch = read_batch_urls('test/test_urls/output.txt')
    dl = YoutubeIE(opts)

# Generated at 2022-06-14 15:39:41.476838
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # TODO: remove this when we have a better testing infrastructure
    def report(msg):
        pass

    ydl = {'params': {}, 'report_error': report}
    hls_fd = HlsFD(ydl, {}, True)
    assert hls_fd.download_fragment.__module__ == 'youtube_dl.downloader.hls'

# Generated at 2022-06-14 15:39:52.263179
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import get_info_extractor
    ie = get_info_extractor(HlsFD.IE_NAME)
    assert ie.suitable('https://example.com/manifest.m3u8')
    assert ie.suitable('https://example.com/video.m3u8')
    assert ie.suitable('https://example.com/hls.m3u8')
    assert ie.suitable('https://example.com/variant.m3u8')
    assert ie.suitable('https://example.com/master.m3u8')
    assert ie.suitable('https://example.com/index.m3u8')
    assert ie.suitable('https://example.com/video.mpd')
    assert ie.suitable('https://example.com/hls.mpd')

# Generated at 2022-06-14 15:39:54.667654
# Unit test for constructor of class HlsFD
def test_HlsFD():
    ydl = FakeYDL()
    params = FakeParams()
    fd = HlsFD(ydl, params)
    assert fd.ydl is ydl and fd.params is params


# Generated at 2022-06-14 15:40:04.517381
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import io
    import json
    import shutil
    import tempfile
    import os
    import time
    import warnings
    import re
    import subprocess
    import hashlib
    import datetime
    from .external import find_executable

    from ..compat import (
        compat_urllib_error,
        compat_urllib_request,
        compat_urlparse,
    )
    from ..utils import (
        clean_html,
        encodeFilename,
        encodeArgument,
        std_headers,
    )
    from ..extractor import gen_extractors

    from .test_utils import (
        FakeYDL,
        FakeInfoExtractor,
        DownloadContextManager,
        TemporaryFile,
    )

    ffmpeg_path = find_executable('ffmpeg')

    failure_count = 0

# Generated at 2022-06-14 15:40:17.760022
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..downloader import FileDownloader

    def run_test(downloader_params, download_method_params):
        ydl_opts = {
            'verbose': True,
            'forceurl': True,
            'forcetitle': True,
            'forcedescription': True,
            'quiet': True,
            'outtmpl': '%(id)s.f4m',
            'format': '36/37/96',
        }

        if downloader_params is not None:
            ydl_opts.update(downloader_params)
        ydl = FileDownloader(ydl_opts)

        class MockInfoDict(dict):
            pass


# Generated at 2022-06-14 15:40:28.665984
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .fragment import FragmentFDTest
    import io
    import os
    import shutil
    import tempfile
    import unittest

    class TestHlsFD_real_download(FragmentFDTest):
        def setUp(self):
            self.temp_dir = tempfile.mkdtemp()
            filename = os.path.join(self.temp_dir, 'video')
            def get_test_cases(test_case_file, end_at=None):
                with io.open(test_case_file, 'r', encoding='utf-8') as f:
                    test_cases = f.readlines()
                if end_at:
                    test_cases = test_cases[:end_at]
                return test_cases

# Generated at 2022-06-14 15:40:31.075000
# Unit test for constructor of class HlsFD
def test_HlsFD():
    fd = HlsFD({}, {}, {})



# Generated at 2022-06-14 15:41:02.947892
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from .extractor.common import InfoExtractor


# Generated at 2022-06-14 15:41:14.976856
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert not HlsFD.can_download('', {})
    assert HlsFD.can_download('', {'ext': 'm3u8'})
    assert HlsFD.can_download('#EXTM3U', {'ext': 'm3u8'})
    assert HlsFD.can_download('#EXTM3U\n#EXTINF:1\nhttp://', {'ext': 'm3u8'})
    assert not HlsFD.can_download('#EXTM3U\n#EXTINF:1\nhttp://\n#EXT-X-KEY:METHOD=NONE', {'ext': 'm3u8'})

# Generated at 2022-06-14 15:41:16.447857
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Just instantiate HlsFD """
    HlsFD(None, None)

# Generated at 2022-06-14 15:41:18.668539
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test_HlsFD_real_download()

# Generated at 2022-06-14 15:41:28.255757
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import get_info_extractor, gen_extractors
    ie = get_info_extractor('twitch:live')
    stream_url = 'https://www.twitch.tv/tommyinnit'
    info_dict = ie._real_extract(stream_url)
    hls_url = info_dict.get('url')
    hls_url_test = HlsFD.can_download(hls_url, info_dict = info_dict)
    print('HlsFD.can_download test:', hls_url_test)
    #if hls_url_test:
    hls_download_test = HlsFD()
    hls_download_test.download(hls_url, info_dict = info_dict)
    #else:
    #    hls_url_ff

# Generated at 2022-06-14 15:41:39.022204
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import json
    import re
    import os
    import shutil
    import subprocess
    import tempfile
    from time import time
    import youtube_dl
    import youtube_dl.extractor.common
    from ..utils import prepare_url
    from ..compat import compat_urllib_error

    # Set up the test environment
    test_dir = os.path.join(tempfile.gettempdir(), '%s' % int(time()))
    os.makedirs(test_dir)
    videos = json.loads(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              '..', '..', 'tests', 'test_data', 'videos.json'), 'rb').read().decode('utf-8'))

# Generated at 2022-06-14 15:41:48.274340
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os
    import tempfile
    from .utils import (
        FakeYDL,
        FakeFile,
        make_fake_info_dict,
    )
    from .extractor.m3u8 import downloaded as m3u8

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # test 1, stream without encryption

# Generated at 2022-06-14 15:41:59.759710
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import sys
    import os
    import tempfile

    def test(name, man_url, info_dict, ext = 'mp4'):
        sys.stderr.write('Testing %s...\n' % name)
        with tempfile.NamedTemporaryFile(suffix='.' + ext, delete=False) as tf:
            filename = tf.name
        try:
            fd = HlsFD(params)
            fd.real_download(filename, info_dict)
        except:
            os.remove(filename)
            raise
        os.remove(filename)
        sys.stderr.write('%s test passed\n' % name)

    params = {
        'mode': 'any',
        'noplaylist': True,
    }


# Generated at 2022-06-14 15:42:02.428609
# Unit test for constructor of class HlsFD
def test_HlsFD():
    ydl = YoutubeDL(dict(forceurl=True))
    info = dict()
    test = HlsFD(ydl, info)
    assert test.info is info
    assert test.ydl is ydl

# Generated at 2022-06-14 15:42:14.382322
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .downloader import common

    info_dict = {
        'url': 'http://test_url_taken_from_info_dict',
        'http_headers': {'test_header': 'test_header_value'},
    }
    hlsfd = HlsFD(common.FileDownloader({}), {}, {'test': True})
    assert hlsfd.urlh == None
    assert hlsfd.manifest_url == 'http://test_url_taken_from_info_dict'
    assert hlsfd.headers == {'test_header': 'test_header_value'}
    assert hlsfd.params == {'test': True}
    assert hlsfd.manifest_type == None
    assert hlsfd.live_segment_index == None
    assert hlsfd.media_

# Generated at 2022-06-14 15:43:21.230966
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert(HlsFD.can_download('#EXTM3U\n#EXT-X-TARGETDURATION:10\n#EXT-X-MEDIA-SEQUENCE:1\n#EXTINF:10,\n#EXT-X-KEY:METHOD=AES-128,URI="https://key_url"\nsegment1.ts\n#EXTINF:10,\nsegment2.ts\n#EXTINF:10,\nsegment3.ts\n#EXTINF:10,\nsegment4.ts\n#EXTINF:10,\nsegment5.ts\n#EXTINF:10,\nsegment6.ts\n#EXT-X-ENDLIST\n', {'is_live':False}))

# Generated at 2022-06-14 15:43:32.749041
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    '''
    Unit test for method real_download of class HlsFD
    '''
    from .f4mfd import F4mFD
    from .externalfd import ExternalFD
    for fd in (F4mFD, ExternalFD):
        fd.available = False
    from .http import HttpFD
    HttpFD._DOWNLOAD_RETcode_RETRYABLE = (
        lambda self, count, retcode, cause, res_sz_err, retries:
        count == 3 and retcode == 399 and isinstance(cause, (compat_urllib_error.HTTPError, OSError, IOError))  # pylint: disable=line-too-long
    )
    HttpFD.real_download = lambda self, filename, info_dict: False  # pylint: disable=line-

# Generated at 2022-06-14 15:43:37.525407
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Test inheritance
    assert issubclass(HlsFD, FragmentFD)

    # Test return values of class methods
    hlsfd = HlsFD(None, {})
    assert hlsfd.can_download('', {})

    # Test return values of instance methods
    hlsfd = HlsFD(None, {})
    assert hlsfd.real_download('', {})

# Generated at 2022-06-14 15:43:48.555047
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor import gen_extractors
    from ..downloader import gen_downloader

    ydl = gen_downloader()
    for ie in gen_extractors():
        if ie.IE_NAME == 'hlsnative':
            ie = ie()
            break

    # Test:
    # * Loading of an m3u8 playlist can be done
    # * Can download a single fragment
    # * Can download and decrypt a single fragment

# Generated at 2022-06-14 15:44:01.150866
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    hlstest_video_id = 'tlG9rO1jqZU'
    hlstest_initial_data_id = 'b5a6f5e6-9a6a-41e1-8f8c-30b5e2ab0d90'
    hlstest_initial_data_url = (
        'https://hlstest.com/%s/%s.bin' % (hlstest_video_id, hlstest_initial_data_id))
    hlstest_video_url = ('https://hlstest.com/%s/master.m3u8?a=1&b=2' % hlstest_video_id)
    hlstest_extra_param_to_segment_url = 'a=2&b=5'


# Generated at 2022-06-14 15:44:10.848211
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .external import ExternalFD
    from .http import HttpFD
    from .http import HlsFD as HlsFD_http
    from ..utils import fake_urlopen
    # Test HlsFD constructor with youtube-dl.org/download.py input
    # "url"

# Generated at 2022-06-14 15:44:22.777076
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.FD_NAME == 'hlsnative'
    assert HlsFD.can_download('#EXTM3U', {})
    assert not HlsFD.can_download('#EXTM3U' + '\n' + '#EXT-X-KEY:METHOD=AES-128', {})
    assert not HlsFD.can_download('#EXTM3U' + '\n' + '#EXT-X-BYTERANGE', {})
    assert HlsFD.can_download('#EXTM3U' + '\n' + '#EXT-X-BYTERANGE', {'_decryption_key_url': 'https://example.com'})

# Generated at 2022-06-14 15:44:30.701334
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..extractor.common import InfoExtractor
    from .fragment import FragmentFD
    from .external import FFmpegFD

    # Test for encrypted stream
    def test_encrypted_stream(FdClass):
        if FdClass == HlsFD:
            assert not FdClass.can_download(manifest, {})
        else:
            assert FdClass.can_download(manifest, {})
        return True

    manifest = '#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI="https://priv.example.com/key.php?r=52"\n'
    manifest += '#EXTINF:2.833,\nhttp://example.com/00001.ts\n'

# Generated at 2022-06-14 15:44:42.258408
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .old_extractor import YoutubeDL
    ydl = YoutubeDL({
        'simulate': True,
        'skip_download': True,
        'quiet': True,
        'video_id': 'BQ0mxQXmLsk',
        'writeinfojson': True,
    })
    ydl.download(['https://www.youtube.com/watch?v=BQ0mxQXmLsk&list=PLX6ozaUYRrhtF6TBlT-LFx7VkHpzKi7gC'])
    with open('BQ0mxQXmLsk.info.json') as f:
        info_dict = json.load(f)
    hls_fd = HlsFD(ydl, {})
    for ph in range(4):
        ydl.report_progress

# Generated at 2022-06-14 15:44:50.597318
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .url import Url
    from .utils import fake_urlopen
    from .downloader import FakeYDL
    from .extractor import gen_extractor
    from .embedthumbnail import ThumbnailExtractor
    from .extractor import youtube_dl
    from .compat import compat_struct_pack
    import os
    import shutil
    # hlsnative has detected features it does not support, extraction will be delegated to ffmpeg
    url = "https://www.youtube.com/watch?v=I8bzWYBArGE"
    ydl = FakeYDL()
    ie = gen_extractor(ydl, url)
    info = ie.extract(url)
    filename = ydl.prepare_filename(info)
    hlsnative = HlsFD(ydl, {'quiet': True})
    file