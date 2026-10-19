

# Generated at 2022-06-14 15:22:25.897018
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass
# test_DashSegmentsFD_real_download()

# Generated at 2022-06-14 15:22:34.397488
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import io
    from .http import HttpFD
    from ..extractor.common import InfoExtractor
    from ..compat import urlparse

    # First of all we need to test the method _get_live_fragment_retries of class
    # FragmentFD since it is used in method real_download of class DashSegmentsFD
    # as the parameter fragment_retries
    assert FragmentFD._get_live_fragment_retries(None) == 0
    assert FragmentFD._get_live_fragment_retries({}) == 0
    assert FragmentFD._get_live_fragment_retries({'live_fragment_retries': 0}) == 0
    assert FragmentFD._get_live_fragment_retries({'live_fragment_retries': 1}) == 1

# Generated at 2022-06-14 15:22:35.974080
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    DashSegmentsFD(ydl)

# Generated at 2022-06-14 15:22:37.991212
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..extractor import gen_extractors
    from ..downloader import FileDownloader



# Generated at 2022-06-14 15:22:48.780178
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import pytest
    from .gen_tests import generate_test
    from .extractors.youtube import YoutubeDL
    from .extractors import (
        _parse_mpd_formats,
        _extract_mpd_formats,
        _extract_mpd_segments,
        _process_mpd_formats_extract,
    )
    from ..utils import (
        HEADRequest,
    )
    from ..extractor import (
        gen_extractors,
        list_extractors,
    )
    from ..cache import (
        urlcache,
    )
    from ..compat import (
        compat_cookielib,
        compat_urllib_request,
    )
    from ..extractor.common import (
        InfoExtractor,
    )
    # Load builtin

# Generated at 2022-06-14 15:22:57.000221
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import inspect # Used to get source code of method real_download in class DashSegmentsFD
    import os
    import types

    test_dir = os.path.dirname(os.path.abspath(__file__))
    # Get source code of method real_download in class DashSegmentsFD
    source_code = inspect.getsource(DashSegmentsFD.real_download)
    # Add a dummy class to source code
    source_code = 'class DummyClass: ' + source_code
    # Add the name of the dummy class to source code
    source_code = source_code.replace('FragmentFD', 'DummyClass')
    # Create a new module from the source code
    module_code = types.ModuleType('DummyModule')
    exec(source_code, module_code.__dict__)

# Generated at 2022-06-14 15:22:59.600527
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd=DashSegmentsFD()
    assert(fd.real_download("filename","info_dict")==          True)

# Generated at 2022-06-14 15:23:09.799790
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader.common import FileDownloader
    from ..YoutubeDL import YoutubeDL

    class MockDashSegmentsFD(DashSegmentsFD):
        def _download_fragment(self, ctx, url, info_dict):
            return url
        def _append_fragment(self, ctx, frag_content):
            self.last_fragment_content = frag_content

    class MockFD(object):
        dash_segments_fd_class = MockDashSegmentsFD
        params = None
    ydl = YoutubeDL({'quiet': True})
    fd = MockFD()
    fd.ydl = ydl
    fd.downloader = FileDownloader(ydl)

# Generated at 2022-06-14 15:23:18.953792
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import shutil
    import tempfile
    import urllib.request
    import urllib.response

    def request(url, *args, **kwargs):
        return urllib.response.addinfourl(b'a', '', url)

    # Save original function and replace it

# Generated at 2022-06-14 15:23:30.787187
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader.common import FileDownloader
    from ..extractor import YoutubeIE
    from ..post import FFmpegPostProcessor

    ydl = FileDownloader({
        'usenetrc': 'True',
        'username': '',
        'password': '',
        'fragment_retries': '0',
        'skip_unavailable_fragments': 'True',
    })

    ie = YoutubeIE(ydl=ydl)
    postprocessor = FFmpegPostProcessor(ydl=ydl)


# Generated at 2022-06-14 15:23:48.404081
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dashsegments import DashSegmentsFD
    from .downloader import Downloader
    from .extractor import YoutubeIE
    from .http import HttpFD
    extractor = YoutubeIE('http://www.youtube.com/watch?v=BaW_jenozKc')
    extractor.params.update({'usenetrc': '', 'username': '', 'password': '', 'video_password': '', 'simulate': True, 'format': 'dash-flv'})
    dl = Downloader(extractor)

# Generated at 2022-06-14 15:23:52.657415
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    (fd, info) = DashSegmentsFD.downloader_classes['dashsegments'](None, None, {})
    assert fd.FD_NAME is None
    assert fd.params is None
    assert fd.ydl is None
    assert fd.ie is None
    assert fd.info is None
    assert fd._tmpfilename is None

# Generated at 2022-06-14 15:24:03.450826
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YoutubeDL import YoutubeDL
    import os
    import tempfile
    import shutil
    import contextlib
    import sys
    import time

    @contextlib.contextmanager
    def temp_file(**kwargs):
        """
        Context manager to use a temporary file like an open file.
        """
        fp = tempfile.NamedTemporaryFile(mode='w+b', delete=False, **kwargs)
        fp.close()
        try:
            yield fp.name
        finally:
            os.remove(fp.name)

    with tempfile.TemporaryDirectory() as temp_dir:
        # Set of all file names created by the downloader
        created_file_names = set()

        # A YoutubeDL object that is used to perform the download

# Generated at 2022-06-14 15:24:14.368826
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import re
    import sys
    import traceback
    import unittest
    import ytdl_core_downloader as ytdl_core

    class FakeInfoDict(dict):
        def __init__(self, d, **kw):
            # TODO: proper deepcopy and inheritance from dict
            super(FakeInfoDict, self).__init__(**kw)
            self.update(d)
            for k, v in self.items():
                if isinstance(v, dict):
                    self[k] = FakeInfoDict(v)

    class DashSegmentsFDTests(unittest.TestCase):
        def setUp(self):
            self._dashfd = DashSegmentsFD({})


# Generated at 2022-06-14 15:24:16.462853
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD('foo').FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:24:17.101004
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    return True

# Generated at 2022-06-14 15:24:28.002826
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YoutubeDL import YoutubeDL
    from ..extractor.fragment import FragmentFD_Test
    import shutil
    import tempfile
    import os

    def get_temporary_file_path(suffix=""):
        fd, file_path = tempfile.mkstemp(suffix)
        os.close(fd)
        return file_path

    def get_temporary_directory():
        return tempfile.TemporaryDirectory()

    # Tests
    temp_dir = get_temporary_directory()
    t_mp4_file_path = get_temporary_file_path(suffix='.mp4')
    t_mpd_file_path = os.path.join(temp_dir.name, "media.mpd")

# Generated at 2022-06-14 15:24:36.827735
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """
    Just run the DashSegmentsFD constructor to test if it executes correctly
    This is just a sanity check, not a real test of its functionality
    """

    # Test without info_dict since it's optional
    fd = DashSegmentsFD(None, None)
    assert fd.params == {}
    assert fd.frag_index == 0
    assert fd.total_frags == -1
    assert fd.filename is None
    assert fd.tmpfilename is None
    assert fd.info is None
    assert fd.fatal_error is None
    assert fd.reported == 0
    assert fd.frag_num is None
    assert fd.frag_content is None
    assert fd.success is None
    assert fd.retries == 0

# Generated at 2022-06-14 15:24:42.800879
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # import youtube_dl
    try:
        import youtube_dl
    except ImportError:
        print('Please check if youtube_dl is installed')
        raise ImportError('youtube_dl not found')
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader.dashsegments import DashSegmentsFD
    from youtube_dl.downloader.fragment import FragmentFD
    # Initialize the downloader
    ydl_opts = {
        'outtmpl': '%(id)s.%(ext)s',
        'format': '134+140',
    }
    ydl = YoutubeDL(ydl_opts)
    ydl.add_default_info_extractors()

# Generated at 2022-06-14 15:24:48.726928
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    try:
        import youtube_dl
        from unittest import SkipTest
        raise SkipTest("The test for 'real_download' is part of test_extractor.py and can't be tested in isolation. Use '--extractor-tests' option to run it.")
    except ImportError:
        pass

    # TODO: Implement unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:25:02.694812
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """
    Test
    """
    pass


# Unit test the method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:25:13.694323
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader.common import FileDownloader
    from ..extractor import get_info_extractor
    import os
    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 15:25:19.691082
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    d = {'fragment_base_url': "http://furl", 'fragments': [{'path': "fpath"}, {'path': "fpath2"}]}
    f = DashSegmentsFD(d)
    assert not f.params.get('test', False)
    f = DashSegmentsFD(d, params={'test': True})
    assert f.params.get('test', False)
    assert f.params.get('noprogress', False)

# Generated at 2022-06-14 15:25:20.859390
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # TODO
    pass

# Generated at 2022-06-14 15:25:32.024108
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .common import FakeYDL
    from .http import RetryFD
    from ..extractor import YoutubeIE
    from ..downloader import FileDownloader
    from ..utils import prepend_extension
    from ..compat import compat_str

    MOCK_FRAGMENTS = list(range(10))
    MOCK_FRAGMENT_BASE_URL = 'http://example.com/'
    MOCK_FRAGMENT_CONTENT_TEMPLATE = ('-' * 20).encode('ascii')

    class FakeFragmentsFD(RetryFD):
        def _download_fragment(self, ctx, fragment_url, info_dict):
            frag_index = ctx['fragment_index']

# Generated at 2022-06-14 15:25:42.537836
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    try:
        from ..YoutubeDL import YoutubeDL
        from ..extractor.youtube import YoutubeIE
        from ..utils import encode_data_uri
    except:
        print("ERROR: cannot import YouTubeDL and/or YoutubeIE")
        return False
    from .common import FakeYDL
    import tempfile
    import os.path

    if not YoutubeIE.suitable(encode_data_uri('http://example.org/test.mpd')):
        print("ERROR: YoutubeIE is not suitable for this test")
        return False

    # Set up a fake YDL object
    class _YDL(FakeYDL):
        def report_warning(self, msg):
            pass

        def report_error(self, msg):
            raise Exception(msg)

        def to_stdout(self, msg):
            pass


# Generated at 2022-06-14 15:25:52.122968
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    try:
        import json
    except ImportError:
        import simplejson as json
    from ytdl_server.cmdline import parseCmdLine
    from ytdl_server.common import post_text
    from ytdl_server.server import Server

    # Create table containing fake data of one downloaded video (from YouTube)

# Generated at 2022-06-14 15:25:53.543415
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass # Test is implemented in test_download

# Generated at 2022-06-14 15:26:02.064888
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    test_video_id = '3MteSlpxCpo'

# Generated at 2022-06-14 15:26:11.011971
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    from ..extractor.common import InfoExtractor
    InfoExtractor.IE_NAME['Youtube'] = YoutubeIE

    from . import dashextractor
    from .dashextractor import DashManifestIE
    InfoExtractor._ALL_CLASSES.append(DashManifestIE)
    InfoExtractor.IE_NAME['DashManifest'] = DashManifestIE

    DashManifestIE.ie_key = 'DashManifest'
    DashManifestIE._TYPE = 'dash'
    DashManifestIE._WORKING = True
    YoutubeIE.ie_key = 'Youtube'
    YoutubeIE._WORKING = True
    YoutubeIE.working = True


# Generated at 2022-06-14 15:26:39.407365
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import sys
    sys.argv = ['you-get', 'http://www.viki.com/videos/1116766v-goblin-episode-7']
    from ..extractors import viki
    viki.playlist = viki.viki_download_by_id
    viki.download_playlist()

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:26:40.950577
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    return DashSegmentsFD.real_download(DashSegmentsFD, 'filename', 'info_dict')

# Generated at 2022-06-14 15:26:48.965955
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YoutubeDL import YoutubeDL
    from .dash import DASHIE
    ydl = YoutubeDL(params={
        'outtmpl': '%(id)s-%(playlist_id)s-%(playlist_title)s.%(ext)s',
        'quiet': True,
    })
    ydl.add_info_extractor(DASHIE)
    opts = {'playlistend': 1}
    fd = DashSegmentsFD(ydl, ydl.params, 'youtube:3oLdXrjDqVU', opts)

# Generated at 2022-06-14 15:27:00.546944
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():

    from .dash_manifest import DashManifestFD

    try:
        import xmltodict
    except ImportError:
        return

    def _write(fn, *args, **kwargs):
        with open(fn, *args, **kwargs) as f:
            f.write('a')

    # Note: this test uses the same manifest file as the test
    #       test_DashManifestFD_real_download() in dash_manifest.py
    manifest_file = 'test.dash'

# Generated at 2022-06-14 15:27:03.641226
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # Test for checking if the constructor of DashSegmentsFD
    # returns an instance of DashSegmentsFD.
    dashsegm_fd = DashSegmentsFD()
    assert isinstance(dashsegm_fd, DashSegmentsFD)

# Generated at 2022-06-14 15:27:04.145049
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass



# Generated at 2022-06-14 15:27:09.205876
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    info_dict = {'fragments': [{'url': 'http://127.0.0.1/1.ts'}], 'fragment_base_url': 'http://127.0.0.1/', 'url': 'http://127.0.0.1/manifest'}
    t = DashSegmentsFD(info_dict)
    assert t.get_method() == 'GET'
    assert t.get_name() == 'dashsegments'

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:27:11.188626
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # TODO
    assert False

# Generated at 2022-06-14 15:27:21.823444
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import sys
    sys.path.append("../youtube_dl")
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor import YoutubeIE
    from youtube_dl.utils import DownloadError
    from dashsegments import DashSegmentsFD

    ydl = YoutubeDL()
    ydl_opts = {'format': 'mp4', 'logger': ydl}

    # test for successful download of dash segments
    url = "https://www.youtube.com/watch?v=tHGz0C_Yt2Q"
    ie = YoutubeIE()
    info = ie._real_extract(url, ydl_opts)
    fd = DashSegmentsFD(url, ydl_opts)
    fd.download(info)

# Generated at 2022-06-14 15:27:31.670488
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import shutil
    import tempfile
    import json
    import re
    import subprocess
    import sys

    if sys.version_info[0] > 2:
        from io import StringIO, BytesIO
    else:
        from StringIO import StringIO
        from cStringIO import StringIO as BytesIO

    from ..extractor import YoutubeIE, determine_ext
    from ..post import ytdl_post_processor
    from ..utils import (
        encode_compat_str,
        ExtractorError,
        compat_urllib_parse_urlencode,
        compat_urllib_request,
        compat_urlparse,
        compat_urlretrieve,
        compat_xml_parse_error,
    )

# Generated at 2022-06-14 15:28:29.692649
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..compat import compat_urllib_request
    from ..extractor.common import InfoExtractor
    from ..utils import compat_urllib_parse

    class CustomInfoExtractor(InfoExtractor):
        def _real_extract(self, url):
            self.report_extraction(None)

# Generated at 2022-06-14 15:28:31.421249
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    d = DashSegmentsFD()
    assert d.FD_NAME == 'dashsegments'
    assert d.params == {}

# Generated at 2022-06-14 15:28:41.177837
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    from ..extractor.dash import DashSegmentsFD
    from ..postprocessor import FFmpegMergerPP
    ydl = YoutubeDL({})
    d = DashSegmentsFD(ydl=ydl)
    assert isinstance(d, FragmentFD)

    # Test class methods
    d.add_post_processor(FFmpegMergerPP(ydl))
    d.add_post_processor(FFmpegMergerPP(ydl))
    d.remove_post_processor(FFmpegMergerPP)
    assert len(d.get_postprocessors()) == 0
    d.remove_post_processor(FFmpegMergerPP)

    # Test params dict
    # Note: FFmpegMergerPP uses "ffmpeg_location"
    # so to not have to mock it, avoid adding it


# Generated at 2022-06-14 15:28:53.156723
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    print('test_DashSegmentsFD_real_download start')
    import youtube_dl.YoutubeDL
    import youtube_dl.extractor.youtube
    ydl = youtube_dl.YoutubeDL({'quiet': False, 'writedescription': False, 'writeinfojson': False, 'writesubtitles': False, 'writeannotations': False, 'subtitleslangs': [], 'skip_download': False, 'format': 'bestvideo+bestaudio', 'ignoreerrors': False, 'forceurl': False, 'forcethumbnail': False, 'forceduration': False, 'forcefilename': True, 'simulate': False, 'outtmpl': u'/home/nils/tmp/out/tmp.mp4'})
    func_name = 'youtube_dl.extractor.youtube.YoutubeIE.extract'

# Generated at 2022-06-14 15:29:02.730903
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dash import DashSegmentsFD
    from .http import HttpFD

    print()
    print('test for method real_download of class DashSegmentsFD')

    #testing for a mp4 file

# Generated at 2022-06-14 15:29:13.934846
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import sys
    import os
    import youtube_dl.extractor.youtube
    # This will fail if not running unit test
    # This is to prevent import dependency on module in unit tests of other modules
    extractor = youtube_dl.extractor.youtube.YoutubeIE()
    info_dict = extractor.url_result('http://test.com/test', 'url')
    # Note: You may have to run multiple times to have fragments
    # to test if fragments are downloaded or not
    # You may also try on another video to make sure extractor is not hardcoded
    info_dict['manifest_url'] = 'http://test.com/manifest'
    info_dict['fragments'] = [{'url': 'http://test.com/test', 'path': 'test_path'}]

# Generated at 2022-06-14 15:29:21.698414
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..extractor import DashSegmentsIE
    from .common import gettestcases
    from .test_dash import download_manifest

    for ie in DashSegmentsIE.extractors.values():
        for case in gettestcases(ie, ie.suitable):
            if not case:
                continue
            video_id = case.get('id', case['url'].split('/')[-1])
            # Skip rtmpdump tests, they don't work with this unit test
            if case.get('player_url') is not None:
                continue
            # Skip decryption tests, they don't work with this unit test
            if case.get('key') is not None:
                continue
            # Skip tests without manifest url
            if case.get('_type') != 'url' or not case.get('url'):
                continue


# Generated at 2022-06-14 15:29:31.843093
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import filecmp
    import os
    import shutil
    import tempfile
    import ytdl_pafy
    import youtubedl

    ytdl = youtubedl.YoutubeDL()

    class TestYDL(ytdl_pafy.YtdlPafy):
        def __init__(self, url, basic=False, gdata=False, sig_cache=None,
                     verbose=False, progress_hooks=None):
            self.verbose = verbose
            self.progress_hooks = progress_hooks
            if basic:
                self._pafy = ytdl.extract_info(url, download=False, process=False)
            else:
                self._pafy = ytdl.extract_info(url, download=False)
            self._populate

# Generated at 2022-06-14 15:29:40.702819
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import youtube
    from ..utils import human_bytes
    from ..videoinfo import VideoInfo
    fd = DashSegmentsFD({}, youtube.YoutubeIE(), VideoInfo({'url': ''}))
    assert fd.fd_name == 'dashsegments'
    assert fd.params.get('test', False)
    assert not fd.params.get('fragment_retries', False)
    assert fd.params.get('skip_unavailable_fragments', True)
    fd = DashSegmentsFD({'test': False, 'skip_unavailable_fragments': False, 'fragment_retries': 3}, youtube.YoutubeIE(), VideoInfo({'url': ''}))
    assert not fd.params['test']

# Generated at 2022-06-14 15:29:43.272196
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    s = DashSegmentsFD(None, None, {})
    assert s.FD_NAME == 'dashsegments'
    assert s.downloader is None
    assert s.params is None

# Generated at 2022-06-14 15:31:43.079750
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import ytdl_youtube_dl_test as ytdl_test
    ydl_opts = {
        'format':
            'bestvideo[height<=1080]+bestaudio',
        'restrictfilenames': True,
        'outtmpl':
            '%(id)s-%(height)sp.mp4'
    }
    with ytdl_test.YoutubeDL(ydl_opts) as ydl:
        downloader = 'dashsegments'
        ytdl_test.local_playlist.clear()
        ytdl_test.playlist_result.clear()
        ydl.params['nooverwrites'] = True
        ydl.params['skip_download'] = True
        ydl.params['noplaylist'] = False
        ydl.params['test']

# Generated at 2022-06-14 15:31:52.322363
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dash import DASHIE
    from ..utils import (
        determine_ext,
        encodeFilename,
        get_cachedir
    )

    def _http_error_handler_fake(self, request, err):
        from ..downloader import _HttpErrorProcessor
        _HttpErrorProcessor(self, request, err)

    def test_true(x):
        assert x
        return True


# Generated at 2022-06-14 15:32:02.513773
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YoutubeDL import YoutubeDL
    from ..extractor.generic import YoutubeIE
    from ..postprocessor import FFmpegMetadataPP
    from ..postprocessor.ffmpeg import FFmpegMergerPP
    from ..postprocessor.common import MetadataFromTitlePP
    # Prepare the inputs
    # We are going to use YoutubeDL() in the test method to make
    # sure there is no reference of the instance in the method,
    # which might cause bugs.

# Generated at 2022-06-14 15:32:14.236759
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .common import FakeYDL
    from .test_common import FakeHttpServer
    from .dash import parse_mpd_formats

    def test_dash(formats, test, fragment_base_url, skip_unavailable_fragments, **kwargs):
        httpd = FakeHttpServer()
        with httpd:
            httpd.serve_content(
                b'<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" profiles="urn:mpeg:dash:profile:isoff-live:2011">\r\n',
                headers={'Content-Type': 'text/xml'}
            )