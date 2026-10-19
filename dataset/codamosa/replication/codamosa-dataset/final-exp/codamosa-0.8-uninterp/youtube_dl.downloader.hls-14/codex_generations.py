

# Generated at 2022-06-14 15:38:01.999292
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    '''
    Test of method real_download() of class FragmentFD.

    This test verifies that HlsFD method real_download() downloads the correct
    data for a known input (see in-line comments below for description of the
    test input).
    '''

    from .external import ExternalFD
    from .fragment import _parse_m3u8_attribs
    from ..utils import _set_file_descriptor_size

    # The input URL to the test (the play list of an m3u8 format file with
    # video fragments).
    URL_INPUT = 'https://example.com/video.m3u8'

    # The first line of the m3u8 input file.
    PLAY_LIST_FIRST_LINE = (
        '#EXTM3U'
    )

    # The second

# Generated at 2022-06-14 15:38:11.323782
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..extractor.youtube import YoutubeIE
    from ..extractor.plussport import PlusSportIE
    from ..extractor.tv2 import TV2IE
    from ..extractor.common import InfoExtractor
    from ..downloader import Downloader
    from ..utils import AdblockIE
    from ..cache import FileCache

    """
    The following test case is disabled because it downloads videos and takes time to run.
    However it can be enabled for testing the code in this file
    """
    # youtube_test_url = 'https://www.youtube.com/watch?v=Ngoj_aYDUcI'
    # TV2_test_url = 'https://tv2.dk/samfund/2019-01-28/ny-tv2-chef-har-skudt-skurke-i-skabet'
    # Plus

# Generated at 2022-06-14 15:38:24.845634
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import sys
    from .http import HttpFD
    class DummyYdl(object):
        def __init__(self):
            self.params = {'noprogress': True}
            self.to_screen = sys.stderr.write
        def urlopen(self, *args, **kargs):
            return HttpFD(self, {'noprogress': True}).urlopen(*args, **kargs)
        def report_warning(self, *args, **kargs):
            pass
        def report_error(self, *args, **kargs):
            raise Exception(args[0])
        def to_stdout(self, s):
            sys.stdout.write(s)
            sys.stdout.flush()
    # test exception of class constructor
    ydl = DummyYdl()


# Generated at 2022-06-14 15:38:36.303536
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_test_handler

    hdlr = get_test_handler('hlsnative')
    hdlr.urlopener.addheaders = [('User-Agent', 'Mozilla/5.0')]

# Generated at 2022-06-14 15:38:49.427744
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import pytest
    from .testutils import FakeYDL, FakeHttpserver
    from ..extractor import YoutubeDL

    ydl = YoutubeDL(FakeYDL({'quiet': True, 'simulate': True}))
    ydl.params['test'] = True
    ydl.add_progress_hook(lambda d: None)
    server = FakeHttpserver()

# Generated at 2022-06-14 15:39:00.763655
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    import sys
    import os.path

    youtube_dl_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(youtube_dl_path)

    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor import get_info_extractor

    info_dict = {}
    class FakeInfoExtractor(object):
        IE_NAME = 'test_ie'
    info_extractor = FakeInfoExtractor()
    info_extractor.ydl = YoutubeDL({})
    info_extractor._downloader = YoutubeDL({})
    info_extractor._match_id = lambda _: True
    get_info_extractor(info_extractor.IE_NAME)(info_extractor)


# Generated at 2022-06-14 15:39:06.326256
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import pytest

    from ..extractor.common import InfoExtractor
    from ..utils import encodeFilename

    from . import (
        MockYDL,
        MockHttpDl,
        Retry,
        test_playlist_base,
        test_playlist_entry_base,
    )
    from .test_fragment import test_fragment_base

    class TestInfoExtractor(InfoExtractor):
        def __init__(self, extractor):
            self.ie = extractor
            self.DEFAULT_OUTTMPL = '%(id)s'

        def _real_extract(self, url):
            return self.ie._real_extract(url)


# Generated at 2022-06-14 15:39:14.278903
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:39:16.393885
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """ Test if HlsFD class can be created """
    HlsFD(None, {})



# Generated at 2022-06-14 15:39:25.501065
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():

    from .external import FFmpegFD

    import unittest
    from unittest.mock import Mock, patch

    import codecs
    import tempfile

    import os

    import youtube_dl.YoutubeDL

    class TestHlsFDRealDownload(unittest.TestCase):

        def setUp(self):

            self.old_FFmpegFD_can_download = FFmpegFD.can_download
            FFmpegFD.can_download = Mock(return_value=False)

            self.old_HlsFD_can_download = HlsFD.can_download
            HlsFD.can_download = Mock(wraps=HlsFD.can_download)

            self.old_HlsFD_real_download = HlsFD.real_download

# Generated at 2022-06-14 15:39:45.464875
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .test import get_testdata
    from .test import TmpBaseFD
    from .test import make_fake_info_dict
    from .test import make_fake_extractor

    with open(get_testdata('hls_test.m3u8'), 'rb') as f:
        test_m3u8 = f.read().decode()

    with open(get_testdata('hls_test_frag.ts'), 'rb') as f:
        test_frag = f.read()

    with open(get_testdata('hls_test_decrypt_frag.ts'), 'rb') as f:
        test_decrypt_frag = f.read()

    with open(get_testdata('hls_test_decrypt_key'), 'rb') as f:
        test_decrypt_

# Generated at 2022-06-14 15:39:54.848959
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import sys
    import pytest

    if sys.version_info.major == 2:
        pytest.exit('HlsFD method real_download unit test requires Python 3', allow_module_level=True)

    # This is not a real unit test, it just checks that the expected output is equal to the actual output.
    # The output needs to be updated if anything changes in the tested function.
    # This is mainly here to prevent regressions.
    # In order to actually run this unit test, the file test/test.txt.frag should exist.
    # For example it can be a fragment from one of the dash streams on youtube

# Generated at 2022-06-14 15:40:00.999893
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from . import YoutubeDL

    ydl = YoutubeDL(FakerYDL())
    hlsfd = HlsFD(ydl, FakerParams())

    fd = hlsfd
    assert fd.name == 'hlsnative'
    assert fd.params is not None
    assert fd.ydl is not None
    assert not fd.finished
    assert not fd.started
    assert fd.total_frags == 0

# Generated at 2022-06-14 15:40:12.124613
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    from .utils import test_download_utils, FakeYDL
    from .test_fragment import test_min_read_size

    dl = FakeYDL()
    filename = 'hlsnative_test'
    url = 'https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8'
    file_base = os.path.join(os.getcwd(), 'test_file_base')
    test_download_utils(
        HlsFD, dl, [url, '-o', filename, '--test', '--min-read-size', test_min_read_size, '--file-base', file_base])

# Generated at 2022-06-14 15:40:15.244770
# Unit test for constructor of class HlsFD
def test_HlsFD():
    hlsfd = HlsFD('dummy_ydl', 'dummy_params')
    return hlsfd.name == 'hlsnative'

# Generated at 2022-06-14 15:40:27.230057
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import os
    import tempfile
    import random
    import string

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'test')
        for i in range(4):
            seg = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
            info_dict = {'url': 'https://video-dev.github.io/streams/x36xhzz/x36xhzz.m3u8?t=%d' % i,
                         '_decryption_key_url': 'https://video-dev.github.io/streams/x36xhzz/x36xhzz_aes/key.bin'}
            hlsfd = HlsFD(None, {})
            hlsfd

# Generated at 2022-06-14 15:40:37.098275
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from ..downloader import YoutubeDL
    from ..extractor import YoutubeIE
    from ..utils import match_filter_func
    from .fragment import FragmentFD
    from .external import FFmpegFD

    ydl = YoutubeDL({'verbose': True, 'match_filter': match_filter_func('any')})

# Generated at 2022-06-14 15:40:38.205051
# Unit test for constructor of class HlsFD
def test_HlsFD():
    HlsFD({}, {})


# Generated at 2022-06-14 15:40:48.393126
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import sys
    sys.stderr = open(os.devnull, 'w')
    # if test fails change the manifest url to a working manifest url
    manifest = 'http://s1.pdl.stream.av.it.pt/hls/live_1.m3u8?u=d1d02ebb&token=1a6a959d-4bab-4a3e-b6bb-ef5c5f6d6ccc'
    hls_fd = HlsFD(None, {'test': True})
    assert hls_fd.can_download(hls_fd.ydl.urlopen(manifest).read().decode('utf-8', 'ignore'), {'test': True})

# Generated at 2022-06-14 15:40:59.181952
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..extractor import gen_extractors
    for ie in gen_extractors():
        manifest = test_HlsFD_manifests.get(ie.IE_NAME)
        if manifest is not None:
            assert ie.suitable(manifest) == HlsFD.can_download(manifest, {'ie_key': ie.ie_key(), 'format': ''})

# Maps extractor name to its manifest

# Generated at 2022-06-14 15:41:40.360012
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from .utils import FakeYDL
    from .external import FFmpegFD
    from .fragment import TestFragmentFD

    ydl = FakeYDL()
    # Make sure that we can actually download playlist from the server.
    # The file will not be written
    fd = FFmpegFD(ydl, {'outtmpl': '-'})
    info = fd.download(
        'https://devimages.apple.com.edgekey.net/streaming/examples/bipbop_4x3/'
        'bipbop_4x3_variant.m3u8')[0]
    # Now test HlsFD
    # Do not modify the dict - it is reused in other tests
    info['hlsnative_m3u8_url'] = info.pop('url')
    hfd = H

# Generated at 2022-06-14 15:41:46.310636
# Unit test for constructor of class HlsFD
def test_HlsFD():

    import os
    import re
    import sys
    import unittest

    if sys.version_info[0] >= 3:
        from unittest import mock
    else:
        import mock
    from unittest.mock import Mock

    from ..extractor.common import InfoExtractor
    from ..downloader import FileDownloader
    from .fragment import FragmentFD

    from ..utils import urlopen
    from .http_fd import HttpFD

    class MockExtractor(InfoExtractor):

        def __init__(self, downloader):
            self.downloader = downloader

        def extract(self, url, *args, **kwargs):
            return {
                '_type': 'url',
                'url': url,
            }
    extractor = MockExtractor(None)

    # check HlsFD

# Generated at 2022-06-14 15:41:56.754350
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .common import FakeYDL
    import json

    test_cases = json.load(open('test/test_hlsnative_constructor.json'))

    for test_case in test_cases:
        can_download = HlsFD.can_download(
            test_case['s'],
            test_case['info_dict'],
        )
        assert can_download == test_case['expected']

    # Test download method
    info_dict = test_cases[0]['info_dict']
    ydl = FakeYDL()
    hlsfd = HlsFD(ydl, {'test': True})
    hlsfd.real_download('test.out', info_dict)

# Generated at 2022-06-14 15:42:04.957743
# Unit test for constructor of class HlsFD

# Generated at 2022-06-14 15:42:05.653596
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    pass

# Generated at 2022-06-14 15:42:16.944996
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from . import YoutubeDL
    import tempfile

    # Test downloading incomplete (unavailable) fragments
    # https://github.com/ytdl-org/youtube-dl/issues/10165
    # https://github.com/ytdl-org/youtube-dl/issues/10448
    ydl = YoutubeDL({'skip_unavailable_fragments': True})

# Generated at 2022-06-14 15:42:24.398578
# Unit test for constructor of class HlsFD
def test_HlsFD():
    assert HlsFD.can_download('#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0\n#EXT-X-KEY:METHOD=NONE\n#EXTINF:2.008,\nhttps://priv.example.com/fileSequence2680.ts\n#EXT-X-ENDLIST\n', {'id': '_'}) is True
    return True

if __name__ == '__main__':
    test_HlsFD()

# Generated at 2022-06-14 15:42:32.506187
# Unit test for constructor of class HlsFD
def test_HlsFD():
    import sys
    import unittest

    class DownloaderMockup:
        def __init__(self):
            self.to_screen_called_with = []
            self.cache = {}
            self.retval = None

        def to_screen(self, what, *args):
            self.to_screen_called_with.append((what, args))

        def urlopen(self, url, *args, **kwargs):
            class Result:
                def __init__(self, data, url=None):
                    self.data = data
                    self.url = data

                def read(self):
                    return self.data

                def geturl(self):
                    return self.url
            ret = Result(self.retval)
            self.retval = None
            return ret


# Generated at 2022-06-14 15:42:43.288492
# Unit test for method can_download of class HlsFD

# Generated at 2022-06-14 15:42:50.151624
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import tempfile
    import os

    def _prepare_url(info_dict, url):
        return url

    def _download_fragment(ctx, url, info_dict, headers):
        return False, b''

    def _append_fragment(ctx, fragment):
        pass

    def _report_progress(ctx, fragment_index, num_fragments):
        pass

    def _finish_frag_download(ctx):
        pass


# Generated at 2022-06-14 15:44:07.649069
# Unit test for method real_download of class HlsFD

# Generated at 2022-06-14 15:44:16.509103
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    import os
    import glob
    import youtube_dl.utils

    def test_download(capsys, ydl, url, options, expected_output=None, expected_retcode=0, expected_exception=None, expected_filename=None, expected_return=False):
        if not expected_output:
            expected_output = []
        # Remove old files if needed
        for f in glob.glob("*_HlsFD_real_download"):
            os.remove(f)
        try:
            # Download a file
            retcode = ydl.download([url])
        except Exception as e:
            print(e)
            assert isinstance(e, expected_exception)
            return
        # Compare captured output from stderr and stdout
        captured = capsys.readouterr()

# Generated at 2022-06-14 15:44:18.981002
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Test: First test to see if the HlsFD class is being loaded by checking that the following is not None
    assert HlsFD is not None

# Generated at 2022-06-14 15:44:27.962339
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..downloader import YoutubeDL

    ydl = YoutubeDL()
    assert HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-PLAYLIST-TYPE:VOD\n'
        '#EXT-X-TARGETDURATION:3\n'
        '#EXT-X-VERSION:3\n'
        '#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXT-X-KEY:METHOD=NONE\n'
        '#EXTINF:3, no desc\n'
        'https://example.com\n'
        '#EXT-X-ENDLIST',
        {'is_live': None}
    )

# Generated at 2022-06-14 15:44:33.481641
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    from ..extractor import get_info_extractor
    from .fragment import FragmentFD
    from .external import FFmpegFD
    from ..utils import orderedSet

    ydl = FakeYDL()

    ie = get_info_extractor(ydl, 'youtube')
    info_dict = ie.extract('https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ')
    assert HlsFD.can_download(info_dict['formats'][0]['manifest_url'], info_dict)
    assert not FFmpegFD.can_download(info_dict['formats'][0]['manifest_url'], info_dict)

# Generated at 2022-06-14 15:44:34.405185
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # TODO: add unit test
    pass

# Generated at 2022-06-14 15:44:45.977624
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from .test_downloader import MockYDL
    ydl = MockYDL()
    ydl.params['hls_use_mpegts'] = False
    fd = HlsFD(ydl, ydl.params)
    fd.add_progress_hook(ydl.hooks['progress'])

    # Get a test video
    GOOGLE_HLS_TEST = 'http://devimages.apple.com/iphone/samples/bipbop/gear1/prog_index.m3u8'
    # Using the same test video as ytdl uses
    # TODO: get a video that has some of the features defined in HlsFD.can_download
    TEST_URL = GOOGLE_HLS_TEST

# Generated at 2022-06-14 15:44:55.187759
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import unittest

    import sys

    if sys.version_info[0] < 3:
        raise unittest.SkipTest('Test ported from Python 3 only')

    import pathlib

    from ..compat import compat_urllib_error, compat_urllib_robotparser

    from . import FakeYDL
    from .external import FFmpegFD

    from ..extractor import gen_extractors
    from ..utils import (
        prepend_extension,
        encodeArgument,
    )

    from .test_robot_parser import RobotFileParserTest

    class Hlsfound(object):
        def __init__(self, manifest):
            self.manifest = manifest

        def read(self):
            return self.manifest

    class HlsNotfound(object):
        def read(self):
            raise

# Generated at 2022-06-14 15:45:03.238704
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    # Stubs
    def _prepare_url(ignore1, ignore2):
        # This function is called after test_file is loaded so the Id is equal to 1
        return 'http://127.0.0.1:9999/test'
    def _download_fragment(ignore1, ignore2, info_dict, headers):
        urlh = compat_urllib_request.urlopen(info_dict['url'], headers = headers)
        response = urlh.read()
        success = True if b'#EXTM3U' in response else False
        return (success, response)
    def add_progress_hook(ignore):
        pass
    def report_warning(ignore):
        pass
    # Injecting stubs
    params = {}

# Generated at 2022-06-14 15:45:15.531088
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from ..YoutubeDL import YoutubeDL, DEFAULT_OUTTMPL
    import os
    import tempfile
    import shutil
    def download_test_m3u8(url):
        ydl = YoutubeDL({'outtmpl': DEFAULT_OUTTMPL, 'quiet': True, 'format': 'best', 'nooverwrites': True})
        ydl.add_default_info_extractors()
        info_dict = ydl.extract_info(url, download=False)
        temp_dir = tempfile.mkdtemp()
        os.chdir(temp_dir)