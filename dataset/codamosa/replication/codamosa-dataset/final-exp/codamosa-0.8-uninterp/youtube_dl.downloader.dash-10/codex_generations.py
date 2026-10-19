

# Generated at 2022-06-14 15:22:29.314266
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .http import HttpFD
    file_test_id = 'bziEIoLITqU' # i.e. https://www.youtube.com/watch?v=bziEIoLITqU

# Generated at 2022-06-14 15:22:31.290275
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD(None, None, None)

# vim:sw=4:sts=4:et

# Generated at 2022-06-14 15:22:41.428533
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    from ..downloader import get_suitable_downloader
    from ..utils import match_filter_func
    import pytest
    assert match_filter_func(get_suitable_downloader(YoutubeIE()._extract_info('https://www.youtube.com/watch?v=gETI-YXEiDA')), DashSegmentsFD)
    assert not match_filter_func(get_suitable_downloader(YoutubeIE()._extract_info('https://www.youtube.com/watch?v=3D1VuOlErOo')), DashSegmentsFD)
    # Channels

# Generated at 2022-06-14 15:22:41.985994
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    assert True

# Generated at 2022-06-14 15:22:43.274509
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:22:44.151293
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD({})

# Generated at 2022-06-14 15:22:54.581318
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    manifest_url = "http://www.example.com/manifest"
    manifest_content = "<MPD><Period><AdaptationSet><Representation><SegmentList><SegmentURL media=\"example.com:0000/test(format=m3u8-aapl-v3)\"></SegmentURL></SegmentList></Representation></AdaptationSet></Period></MPD>"

    fragment_base_url = "http://example.com:0000/"
    fragment_urls = ["test(format=m3u8-aapl-v3)"]
    fragments = [
        {
            'url': fragment_base_url + fragment_urls[0],
        }
    ]


# Generated at 2022-06-14 15:23:00.712147
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader import get_suitable_downloader
    from ..compat import compat_urllib_request
    from ..utils import sanitize_open
    from ..extractor import YoutubeIE
    import json
    import random
    import os
    import codecs
    import shutil
    import time

# Generated at 2022-06-14 15:23:10.454548
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader.common import FileDownloader
    from .dash import parse_mpd_formats
    from ..utils import parse_filesize, DEFAULT_OUTTMPL
    from ..compat import compat_urlparse
    import os

    def _run_test(path, formats, test_params, expected_num_fragments=None, expected_file_size=None):
        opts = {
            'test': True,
            'quiet': True,
            'outtmpl': DEFAULT_OUTTMPL
        }
        opts.update(test_params)

# Generated at 2022-06-14 15:23:19.311026
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # The method already has a very high coverage
    # since it is very similar to method real_download in class FragmentFD
    # which is well tested.
    # We only do a simple test of downloading the first segment here
    class FakeDashSegmentsFD(DashSegmentsFD):
        def __init__(self, downloader):
            self.downloader = downloader

        def report_retry_fragment(self, err, frag_index, count, retries):
            pass

        def report_skip_fragment(self, frag_index):
            pass

        def check_filesize(self, info_dict, file_size, record_warning=False):
            pass

        def _prepare_and_start_frag_download(self, ctx):
            pass


# Generated at 2022-06-14 15:23:34.303750
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    """Test DashSegmentsFD.real_download"""
    import os.path
    from .fragment import FragmentFD
    from .dash import DashFD
    import sys
    import tempfile
    import urllib.request
    import urllib.error
    import youtube_dl.YoutubeDL
    import youtube_dl.extractor
    import youtube_dl.downloader
    test_tdir = tempfile.mkdtemp()
    # Setup a dummy youtube-dl extractor
    class DummyYoutubeDLExtractor(youtube_dl.extractor.YoutubeBaseInfoExtractor):
        IE_NAME = 'testytdl'
        _VALID_URL = r'https?://testytdl\.com/video/(?P<id>[\w-]+)'

# Generated at 2022-06-14 15:23:46.065165
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..youtube_dl.YoutubeDL import YoutubeDL
    dashsegmentsfd_inst = DashSegmentsFD(YoutubeDL())
    # Initialize YoutubeDL instance with your preferred settings

# Generated at 2022-06-14 15:23:57.374588
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader import Downloader
    from ..extractor import youtube_dl

    import os
    import shutil
    import tempfile

    def _download_playlist(playlist, filename):
        out_file = os.path.join(temp_dir, filename)
        params = {
            'quiet': True,
            'format': 'best',
            'playlistend': 1,
        }
        d = Downloader(ydl_opts=params)
        info_dict = d.extract_info(
            'http://example.org/%s' % playlist, download=False)
        assert info_dict.get('_type', 'video') == 'multi_video'
        info_dict['fragment_base_url'] = 'http://example.org/'
        info_dict['fragments'] = info

# Generated at 2022-06-14 15:24:06.072720
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YoutubeDL import YoutubeDL
    from .extractor import YoutubePlaylistIE
    from .dash import (DashIE,
                       DashSegmentsIE)
    from .generic import YoutubeIE


# Generated at 2022-06-14 15:24:07.434333
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD()



# Generated at 2022-06-14 15:24:13.087538
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD({})
    assert fd._prepare_and_start_frag_download == FragmentFD._prepare_and_start_frag_download
    assert fd._download_fragment == FragmentFD._download_fragment
    assert fd._finish_frag_download == FragmentFD._finish_frag_download
    assert fd.real_download

# Generated at 2022-06-14 15:24:25.443523
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import io
    import sys
    from .downloader import FakeYDL
    from .extractor import get_info_extractor

    class MyFD(DashSegmentsFD):
        def __init__(self, ydl, params):
            super(MyFD, self).__init__(ydl, params)
            self._out_buffer = io.BytesIO()
            self._fail = False
            self._download_count = 0
            self._fail_count = 0
            self._skip_count = 0

        def _prepare_and_start_frag_download(self, ctx):
            return

        def _download_fragment(self, ctx, fragment_url, info_dict):
            if self._download_count == 0:
                assert fragment_url == 'http://example.com/segment1'
                self

# Generated at 2022-06-14 15:24:35.524634
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import youtube_dl
    from .http import HttpFD

    ctx = youtube_dl.YoutubeDL({})._prepare_context('Never Gonna Give You Up')

    # Downloading an MPD file (which is not necessarily a DASH video)
    # with DashSegmentsFD should succeed (as a test)
    dash_fd = DashSegmentsFD(ctx)
    fd = HttpFD(ctx, {'url': 'http://archive.org/download/ksnn_compilation_master_the_internet/ksnn_compilation_master_the_internet_512kb.mp4'})

# Generated at 2022-06-14 15:24:38.089523
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    dashFD = DashSegmentsFD()
    assert dashFD.FD_NAME == 'dashsegments', "FD_NAME is a wrong value"

# Generated at 2022-06-14 15:24:42.193780
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import youtube
    from ..downloader import FileDownloader
    downloader = FileDownloader('', youtube.YoutubeIE(), 'http://rdio.com/')
    dashsegments = DashSegmentsFD(downloader, 'test', {})
    assert dashsegments.params == {
            'skip_unavailable_fragments': True
    }

# Generated at 2022-06-14 15:25:03.758452
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor.youtube import YoutubeIE
    from ..downloader.common import FileDownloader
    from ..downloader import FileDownloader
    from ..utils import WARNING
    from ..compat import match_filter
    import os
    import random
    import sys

    ie = YoutubeIE()

    dl = FileDownloader({
        'usenetrc': False,
        'username': 'test',
        'password': 'test',
        'quiet': True,
        'simulate': True,
        'format': '137+140',
        'outtmpl': '%(id)s.f%(format_id)s.%(ext)s',
    }, {'ytdl_hook': False, 'extractors': [ie], 'extractor_opts': {'youtube': {}}})


# Generated at 2022-06-14 15:25:06.286445
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    dashfd = DashSegmentsFD({}, None)
    assert dashfd is not None

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:25:08.299694
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    print("dashsegments.real_download()")
    DashSegmentsFD().real_download()

# Generated at 2022-06-14 15:25:08.922676
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    assert True

# Generated at 2022-06-14 15:25:13.738783
# Unit test for constructor of class DashSegmentsFD

# Generated at 2022-06-14 15:25:15.542042
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import sys
    sys.stderr = open('test.log','w')
    test = DashSegmentsFD(params={'skip_unavailable_fragments':True})
    assert test.params['skip_unavailable_fragments'] == True

# Generated at 2022-06-14 15:25:24.490880
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    #Pretend we're a youtube-dl command-line program
    import sys
    import os
    from ..utils import YOUTUBE_DL_PATH as __YOUTUBE_DL_PATH
    __dir = (os.path.dirname(__YOUTUBE_DL_PATH) or '.')
    sys.path.insert(0, __dir)
    sys.path.insert(0, os.path.join(__dir, '..'))
    import youtube_dl.YoutubeDL as __YoutubeDL
    del sys.path[0]
    del sys.path[0]

    import youtube_dl.downloader.http as http

    from .common import FakeYDL

    ydl = FakeYDL()
    ydl.params['test'] = True
    ydl.params['progress_hooks'] = []

# Generated at 2022-06-14 15:25:33.498101
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import unittest
    import os
    import sys
    import argparse
    import tempfile
    import shutil
    import re
    import gzip
    import base64
    import datetime
    import hashlib
    import json
    import time
    from .common import FileDownloader
    from .http import HttpFD
    from .dash import DashSegmentsFD
    from .fragment import _set_url_query_parameter
    from .fragment import _get_query_parameter
    from .fragment import _replace_extension
    from .fragment import _make_fragment_url
    from .fragment import _parse_fragment_url
    from .fragment import _regularize_fragment_url
    from .dash import _parse_mpd_formats

# Generated at 2022-06-14 15:25:44.294142
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from . import dash

    class DummyYDL(object):
        params = {
            'outtmpl': '',
            'keepvideo': True,
            'nooverwrites': True,
            'cachedir': False,
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'simulate': True,
            'forceurl': True,
            'forcetitle': True,
            'forceid': True,
            'forceduration': True,
            'forcefilename': True,
            'forcethumbnail': True,
            'dump_single_json': True,
            'force_generic_extractor': True,
            'nocheckcertificate': True,
            'verbose': False,
            'skip_download': True,
        }



# Generated at 2022-06-14 15:25:53.718612
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YouTubeIE
    from ..downloader import FFmpegDownloader
    from ..downloader.pptd_downloader import PPTDDownloader
    import ytdl_y4m_test
    import ytdl_test_videos
    import os
    import shutil
    import sys
    import tempfile

    WIDTH, HEIGHT = 1920, 1080
    framerate = '24/1'
    preset = 'libx264-lossless_ultrafast'

    big_buck_bunny = ytdl_test_videos.TestVideo(ytdl_y4m_test.TEST_URL_BIG_BUCK_BUNNY, ytdl_y4m_test.TEST_FILENAMES[0])
    # Download YouTube video in multiple resolutions

# Generated at 2022-06-14 15:26:18.683393
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD.can_download({"protocol":"dash"})

# Generated at 2022-06-14 15:26:20.459578
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dashsegments import DashSegmentsFD
    d = DashSegmentsFD({})
    assert d.params['test'] == False

# Generated at 2022-06-14 15:26:22.228268
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    """
    Class DashSegmentsFD(FragmentFD):
        def real_download(self, filename, info_dict):
    """
    pass

# Generated at 2022-06-14 15:26:34.209586
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # Loading iafd as a library module
    import sys
    from os.path import join, dirname

    iafd_path = join(dirname(__file__), '..', '..')
    if iafd_path not in sys.path:
        sys.path.append(iafd_path)

    # Testing DashSegmentsFD
    from iafd.extractor import DashSegmentsFD
    from iafd.compat import compat_urllib_error
    from iafd.utils import (
        DownloadError,
        urljoin,
    )

    ef = DashSegmentsFD()
    test_filename = 'test_DashSegmentsFD_real_download.mp4'
    ef.params['test'] = True

# Generated at 2022-06-14 15:26:43.802564
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YoutubeDL import YoutubeDL
    from ..extractor.youtube import YoutubeIE
    from ..extractor.generic import YoutubePlaylistIE

    # Test for video Q1R4_4j8lJ4 on YouTube
    video_url = 'https://www.youtube.com/watch?v=Q1R4_4j8lJ4'
    output_path = '-'.join(['%(id)s', '%(title)s.%(ext)s'])
    ydl_opts = {
        'format': '136/137/mp4',
        'outtmpl': output_path,
        'fragment_retries': 10,
        'simulate': True,
    }


# Generated at 2022-06-14 15:26:50.818870
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..downloader import FakeYDL
    ydl = FakeYDL()

    # Test with a single file fragment

# Generated at 2022-06-14 15:26:55.569093
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    downloader_test_call('https://www.youtube.com/watch?v=a1Y73sPHKxw',
        '-f 22/18/17/best -i',
        DashSegmentsFD
    )



# Generated at 2022-06-14 15:26:56.591426
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD



# Generated at 2022-06-14 15:27:01.948630
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor.youtube import YoutubeIE
    ydl = YoutubeIE()
    ydl.add_default_info_extractors()
    url = 'https://www.youtube.com/watch?v=4g4smguYi8k'
    info = ydl._do_extract_info(url, False)
    assert info['formats'][1].get_filesize() == 21557238

# Generated at 2022-06-14 15:27:07.383701
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dash import DashFD
    from .http import HttpFD
    from .http import HlsFD
    dash_fd = DashFD()
    http_fd = HttpFD()
    hls_fd = HlsFD()
    assert DashSegmentsFD in dash_fd.handles
    assert not DashSegmentsFD in http_fd.handles
    assert not DashSegmentsFD in hls_fd.handles

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:28:06.099510
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD()

# Generated at 2022-06-14 15:28:16.351781
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import io
    import os
    import tempfile
    import unittest
    from .http import HttpFD
    from ..extractor import YoutubeDL
    from ..downloader.common import DownloadError

    # This is a test of the real_download method of the DashSegmentsFD class.
    # The structure is as follows:
    #    - test_dash_fragments_basic
    #        - set up a temporary directory
    #        - run a simple download of two videos using the dashsegments protocol
    #        - check that the videos are the same as the originals

    class DummyYoutubeDL(YoutubeDL):
        """
        A class for use in the tests that sets up a temporary directory
        and defines a method for downloading a segmented DASH stream.
        """
        def __init__(self, tmpdir):
            YoutubeDL

# Generated at 2022-06-14 15:28:17.512296
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    print("TEST: DashSegmentsFD.real_download")
    assert True == True

# Generated at 2022-06-14 15:28:28.486042
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    """
    This test asks youtube-dl to download a video that requires
    fragment downloading (that is, AES-128 encryption). This
    should bypass the downloader chain and download directly
    the fragments and concatenate them.

    This is a regression test (see [1]) for
    https://github.com/rg3/youtube-dl/pull/7957

    [1]: https://travis-ci.org/rg3/youtube-dl/jobs/154506934
    """
    from ..extractor.youtube import YoutubeIE
    from ..downloader.common import FileDownloader
    from ..utils import prepare_filename

    url = 'https://www.youtube.com/watch?v=g4Hbz2jLxvQ'
    ie = YoutubeIE(params={'noplaylist': True})
    info = ie.extract

# Generated at 2022-06-14 15:28:38.789362
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    test_filename = 'test_filename'
    fragment_base_url = 'http://dash/'
    fragments = [{
        'url': 'http://dash/1.mp4',
        'path': '1.mp4',
        'duration': 1
    }, {
        'url': 'http://dash/2.mp4',
        'path': '2.mp4',
        'duration': 2
    }, {
        'url': 'http://dash/3.mp4',
        'path': '3.mp4',
        'duration': 3
    }]

    class Downloader:
        def to_screen(self, message):
            print(message)

    class MockContext:
        def __init__(self):
            self.fragment_index = 1
            self.downloaded_bytes = b''



# Generated at 2022-06-14 15:28:40.892564
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    print(DashSegmentsFD)

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:28:42.859345
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import pytest
    assert DashSegmentsFD.real_download({}, {}) == False
test_DashSegmentsFD_real_download()

# Generated at 2022-06-14 15:28:54.883143
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    from ..downloader import FileDownloader
    from ..utils import get_cachedir
    from .fragment import FragmentFD
    import tempfile
    import json
    import os

    # Note: this test needs to be executed within the unit test directory
    OUTPUT_DIR = tempfile.mkdtemp(dir=os.path.dirname(os.path.realpath(__file__)))

# Generated at 2022-06-14 15:29:03.808842
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    # test for dash segments
    assert (isinstance(ydl.build_fragment_downloader(dash_segments_url='https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd', dash_manifest=False), DashSegmentsFD))
    # test for dash manifest
    assert (not isinstance(ydl.build_fragment_downloader(dash_segments_url='https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd', dash_manifest=True), DashSegmentsFD))
    # test for non dash

# Generated at 2022-06-14 15:29:06.183834
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    url = 'https://example.com/video.mpd';
    dashsegmentsfd = DashSegmentsFD(url)

# Generated at 2022-06-14 15:31:49.238960
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    from ..downloader import FileDownloader

# Generated at 2022-06-14 15:31:56.229177
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD.can_download({"fragments": [{'url': 'url', 'path': 'path'}]})
    assert not DashSegmentsFD.can_download({"fragments": [{'path': 'path'}]})
    assert DashSegmentsFD.can_download({"fragments": [{'url': 'url'}]})
    assert not DashSegmentsFD.can_download({"fragments": [{'ur': 'ur'}]})

# Generated at 2022-06-14 15:31:58.595064
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    pass

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:32:00.278323
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    pass


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:32:02.762130
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD(None, 'dashsegments', None, None)



# Generated at 2022-06-14 15:32:06.402728
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD.__name__ == 'DashSegmentsFD'
    assert DashSegmentsFD.FD_NAME == 'dashsegments'
    assert DashSegmentsFD.constructor_handler_class() is not None

# Generated at 2022-06-14 15:32:07.060942
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:32:09.550181
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    dash_fd = DashSegmentsFD({}, {}, {}, {})

    assert dash_fd.FD_NAME == 'dashsegments'