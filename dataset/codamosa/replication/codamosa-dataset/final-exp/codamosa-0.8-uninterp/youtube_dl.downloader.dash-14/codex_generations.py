

# Generated at 2022-06-14 15:22:33.305205
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import youtube_dl.YoutubeDL
    YoutubeDL().params['youtube_include_dash_manifest'] = True
    url = 'https://example.com/vod.mpd'

# Generated at 2022-06-14 15:22:36.568558
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    d = YoutubeDL({'fragment_retries': 5})
    fd = DashSegmentsFD(d, {})
    assert isinstance(fd, DashSegmentsFD)
    assert fd.ytdl is d
    assert fd.params == {'fragment_retries': 5}
    assert fd.info_dict == {}
    assert fd.grabbed == {}



# Generated at 2022-06-14 15:22:38.504788
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD()
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:22:49.259986
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    url = 'https://example.com/manifest.mpd'
    info_dict = {
        'id': 'example',
        'ext': 'mp4',
        'title': 'Example Video Title',
        'fragment_base_url': url,
        'fragments': [
            {'url': url, 'duration': 2.0, 'length': 1024, 'path': '/example.mp4'},
            {'duration': 2.0, 'length': 1024, 'path': '/example.mp4'},
        ],
    }
    dashsegsfd = DashSegmentsFD(url, info_dict)
    assert dashsegsfd.url == url
    assert dashsegsfd.info_dict == info_dict

if __name__ == "__main__":
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:22:53.930228
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    mdict = {"url": "http://example.com",
             "fragments": [{"duration": 1}, {"duration": 1}, {"duration": 1}]}

    # Simple test that it does not raise any exceptions
    dash = DashSegmentsFD(mdict)
    dash.real_download("test_dash", mdict)

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:23:00.374948
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:23:09.854890
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .common import FakeYDL
    from ..extractor.dash import DashIE, parse_segment_template
    from ..extractor.common import InfoExtractor
    from ..compat import compat_urlparse

    ie = InfoExtractor(FakeYDL(), {})
    ie.add_info_extractor(DashIE)
    ie.add_info_extractor(DashSegmentsFD)
    ie.add_info_extractor(FragmentFD)

    def seg_test(test):
        url = 'http://127.0.0.1:15000/%s' % test['url']
        _, params = compat_urlparse.urlparse(url).path[1:].split('/', 1)
        params = dict(compat_urlparse.parse_qsl(params))
        fragments = parse_segment_

# Generated at 2022-06-14 15:23:11.358861
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    d = DashSegmentsFD({}, {}, {})
    return d

# Generated at 2022-06-14 15:23:19.922685
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dash_test_data import (
        mock_dash_manifest,
        mock_dash_segment,
        text_dash_manifest
    )
    from ..extractor import get_info_extractor
    from ..utils import (
        compat_urllib_error,
        compat_urllib_request,
    )

    # set up a test video, fragments and video info extractor
    video_id = 'YOLO'
    fragments = [mock_dash_segment('.f%s' % i, num=i) for i in range(1, 4)]
    fragment_base_url = 'http://example.com/dash/'
    manifest = mock_dash_manifest(
        video_id, fragments, fragment_base_url, 'mp4', text_dash_manifest)
    ie

# Generated at 2022-06-14 15:23:20.673382
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:23:38.111720
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """
    This function tests if DashSegmentsFD works as expected
    """
    # First test case : test with dashsegments
    ydl_opts = {'dash_fragments': True, 'quiet': False, 'playlistend':1, 'skip_unavailable_fragments':True}
    ydl_opts_sim = {'simulate': True, 'quiet': False}
    dash_frag_url = 'https://dash.akamaized.net/envivio/EnvivioDash3/manifest.mpd'
    seg_frag_url = 'https://dash.akamaized.net/dash264/TestCasesHD/hamburger_10s/1_DASH_2/2M_4s/Manifest.mpd'

# Generated at 2022-06-14 15:23:49.742803
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import unittest
    import shutil
    import tempfile
    from .conftest import make_test_downloader
    from .test_download import setup_mock_server

    class TestDashSegmentsFD(unittest.TestCase):

        def setUp(self):
            self.test_dir = tempfile.mkdtemp()
            self.server = setup_mock_server()
            self.server.add_handler('/DASH_fragments.mpd', content_type='text/xml')

        def tearDown(self):
            shutil.rmtree(self.test_dir)


# Generated at 2022-06-14 15:23:57.698219
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """Tests for DashSegmentsFD"""
    from .fragment import FragmentFD
    from .dash import DashFD
    from ..YoutubeDL import YoutubeDL
    from ..extractor.youtube import YoutubeIE

    def _test(ydl, ie, manifest_url, segments_url):
        dashfd = DashFD(ydl, {
            'ie_key': 'Youtube',
            'url': manifest_url,
            'player_url': None,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
            },
            'force_restful': True
        })
        dashfd.add_manifest_url(manifest_url, ie)
       

# Generated at 2022-06-14 15:24:09.523064
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():

    from .dashsegments import DashSegmentsFD
    from ..compat import compat_urllib_error
    from ..downloader import Downloader
    from ..downloader.http import HttpFD
    from .ffmpegmuxer import FFmpegMuxer
    from .hls import HlsFD

    from .fragment import retries as fragment_retries
    from .fragment import skip as skip_unavailable_fragments

    import mock
    import os
    import pprint
    import socket
    import tempfile
    import unittest
    import uuid

    import pytest


# Generated at 2022-06-14 15:24:10.153289
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:24:18.589516
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():

    from .dash import DashFD
    from .http import HttpFD
    from .http import GenericFD
    from ..utils import IncompleteReadError

    # test_1
    import io
    import requests
    import ytdl

    test_data = {'url': 'http://www.youtube.com/watch?v=BaW_jenozKc'}
    dash_data = {'dashmpd': 'http://google.com'}
    dash_data_2 = {'dashmpd': 'http://google.com', 'fragments': 'null'}

    resp = requests.Response()
    resp.status_code = 200
    resp.raw = io.StringIO(u'{"dashmpd": "url"}')
    dash_instance = DashFD(test_data)

# Generated at 2022-06-14 15:24:28.884501
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    import youtube_dl
    import sys
    import os
    from ..utils import make_HTTPServer

    s = DashSegmentsFD()
    url = "https://www.youtube.com/watch?v=b1UiAyYw6Hk"
    ie = youtube_dl.YoutubeDL({}).extract_info(url, download=False)
    filename = 'test.mp4'

    filepath = os.path.join(sys.path[0], filename)

    if os.path.isfile(filepath):
        os.remove(filepath)

    port = make_HTTPServer(ie, s, filepath)
    test_url = 'http://localhost:{0}/{1}'.format(port, filename)

    info_dict = {}
    info_dict

# Generated at 2022-06-14 15:24:30.893082
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    print(DashSegmentsFD)

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:24:35.293572
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor.common import InfoExtractor
    from ..extractor.dash import DashIE
    for ie in (DashIE(), InfoExtractor()):
        try:
            DashSegmentsFD(ie, {}, {}, None, None)
        except TypeError:
            pass
        else:
            raise AssertionError('TypeError expected')

test_DashSegmentsFD()

# Generated at 2022-06-14 15:24:36.098756
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass


# Generated at 2022-06-14 15:24:56.906520
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader import Downloader
    from ..extractor import youtube_dl
    import os
    import shutil
    import tempfile
    import youtube_dl.extractor.common
    import youtube_dl.utils

    class FakeInfoDict(object):

        def __init__(self, fragments_num, fragment_base_url=None, fragments_urls=None):
            self.fragments = list(range(fragments_num))
            self.fragment_base_url = fragment_base_url
            def create_fragment(i):
                if fragments_urls is None:
                    return {
                        'path': 'segment-%d.mp4' % i,
                    }
                else:
                    return {
                        'url': fragments_urls[i],
                    }

# Generated at 2022-06-14 15:25:01.497805
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    
    dl = DashSegmentsFD()
    dl.params['fragment_retries'] = True
    dl.params['skip_unavailable_fragments'] = True

    assert dl.real_download("test.mp4", {})
    assert dl.params['fragment_retries'] == 1
    assert dl.params['skip_unavailable_fragments'] == True

# Generated at 2022-06-14 15:25:11.737770
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:25:21.628082
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..extractor import gen_extractors
    from ..downloader import gen_ydl
    import json

    class DashSegmentsFD_real_download_test_FD(DashSegmentsFD):
        def _download_fragment(self, ctx, fragment_url, info_dict):
            frag_content = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            return True, frag_content

        def _append_fragment(self, ctx, frag_content):
            pass

        def _finish_frag_download(self, ctx):
            pass


# Generated at 2022-06-14 15:25:32.571581
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import shutil
    from .test import get_test_data

    test_dir = get_test_data()
    save_file = os.path.join(test_dir, 'test.mp4')
    manifest_url = 'http://localhost:8080/hls/testv2.mpd'
    info_dict = {
        'id': '1',
        'fragment_base_url': 'http://localhost:8080/hls/',
        'fragments': [
            { 'path': '1.m4s', },
            { 'path': '2.m4s', },
        ],
    }

    fd = DashSegmentsFD(save_file, { 'test': True })
    success = fd.real_download(save_file, info_dict)


# Generated at 2022-06-14 15:25:41.863891
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    reqs = [
        'DashSegmentsFD(http://example.com/index.mpd)',
        {
            'outtmpl': '%(id)s.mp4',
            'write_subtitles_to_stdout': True
        },
    ]
    params = {
        'test': True,
        'format': '',
        'subtitles_lang': 'en',
        'subtitles_format': 'srt',
        'subtitles_output_encoding': 'utf-8',
    }
    res = DashSegmentsFD(*reqs, **params).download()
    assert res['filename'] == 'video_id.mp4'
    assert res['status'] == 'finished'

# Generated at 2022-06-14 15:25:51.132801
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    em = ExtractorManager(json.loads(json_str))
    extractor = em.extractors[0]
    extractor.params['skip_unavailable_fragments'] = False
    extractor.params['fragment_base_url'] = 'http://127.0.0.1:8080'
    extractor.params['test'] = True
    extractor.params['noprogress'] = True
    extractor.params['no_warnings'] = True
    extractor.params['quiet'] = True
    extractor._print_warning = lambda x,y: None
    extractor._make_progress_bar = lambda x: None
    extractor._prepare_and_start_frag_download = lambda x: None
    extractor._finish_frag_download = lambda x: None
    extractor._

# Generated at 2022-06-14 15:26:00.833307
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    with open('test_data/fragments.json') as f:
        d = ydl.process_ie_result({'_type': 'dash_fragments', 'fragments': json.load(f)})
    ydl.params['fragment_retries'] = 0
    ydl.params['skip_unavailable_fragments'] = True
    fd = DashSegmentsFD(ydl, d)
    assert fd.name == 'dashsegments'
    assert fd.tbr is None
    assert fd.tduration is None
    assert not fd.duration
    assert fd.title is None
    assert fd._target_infos is not None
    assert fd._target_infos[1] == d


# Generated at 2022-06-14 15:26:02.561276
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
  assert issubclass(DashSegmentsFD, FragmentFD)

# Generated at 2022-06-14 15:26:14.405727
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    """
    Unit test for method real_download of class DashSegmentsFD.
    """

    from .youtube import YouTubeFD
    from .fragment import FragmentFD

    # Suppress noise from stderr in unit tests
    import logging
    log = logging.getLogger('youtube_dl')
    log.setLevel(logging.ERROR)

    # Test cases
    class TestCase:
        """
        Test case.
        """

        def __init__(self, url, expected_fragment_retries):
            """
            Initialize test case.
            """

            self.url = url
            self.expected_fragment_retries = expected_fragment_retries
            return


# Generated at 2022-06-14 15:26:38.205278
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD()

# Generated at 2022-06-14 15:26:46.095511
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL()
    ydl.add_info_extractor(DummyIE())
    
    filename = ydl.prepare_filename('DASH video')
    
    fd = DashSegmentsFD(ydl, filename, {'fragment_base_url': 'base_url'})
    fd.real_download(filename, {'fragments': [
        {'path': 'first_frag'},
        {'path': 'second_frag'},
    ]})

    assert(ydl.downloaded == [
        ('base_url/first_frag', 1),
        ('base_url/second_frag', 1),
    ])

# Generated at 2022-06-14 15:26:57.781221
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dash import DashFD
    import re
    import os
    from ..utils import prepend_extension, urlopen
    from ..downloader.common import FileDownloader
    from ..downloader.http import HttpFD

    # Download the DASH manifest
    DASH_URL = 'http://ftp.nluug.nl/pub/graphics/blender/demo/movies/Sintel.2010.720p.mkv.mpd'
    http_fd = HttpFD()
    http_fd.real_download(DASH_URL, {
        'continuedl': False,
        'skip_unavailable_fragments': False,
        'noprogress': True,
    })
    dash_manifest = http_fd.get_result()

    # Init the DashFD instance
    dash_fd_

# Generated at 2022-06-14 15:27:00.010756
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    d = DashSegmentsFD()
    assert d is not None


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:27:08.464334
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():

    info_dict = {
        'fragment_base_url': 'http://test.com/fragmentBaseUrl',
        'fragments': [
            {'path': 'fragment/path1'},
            {'path': 'fragment/path2'},
            {'url': 'http://test.com/fragment/path3'},
            {'url': 'http://test.com/fragment/path4'},
        ]
    }

    fd = DashSegmentsFD(None, None, None, False, [], info_dict)
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params == {}
    assert fd.info_dict == info_dict
    assert fd.params.get('test', False) == False

# Generated at 2022-06-14 15:27:20.002055
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import download
    import utils

    ydl = download.YoutubeDL({})
    # Set the working directory to the one where this file is located
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    video_id = '7dPpXDu4vVs'
    # Generate the info dict for the video
    info = ydl.extract_info(video_id, download=False)
    # Create the DashSegmentsFD
    dashsegments_fd = DashSegmentsFD(ydl)
    # Download the video using DashSegmentsFD
    dashsegments_fd.real_download(info['formats'][-1]['fragment_base_url'], info)

    # Check that the generated files are the same as the reference ones
    ref

# Generated at 2022-06-14 15:27:20.936119
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass


# Generated at 2022-06-14 15:27:21.589776
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:27:23.082708
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    obj = DashSegmentsFD()
    assert obj.FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:27:33.146482
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:28:29.978324
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .http import HttpFD
    from .m3u8 import M3u8FD
    from ..YoutubeDL import YoutubeDL
    from ..extractor.youtube import YoutubeIE
    from ..extractor.brightcove import BrightcoveNewIE
    from ..extractor.ooyala import OoyalaIE
    ydl = YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    ydl.add_info_extractor(YoutubeIE())
    ydl.add_info_extractor(OoyalaIE())
    ydl.add_info_extractor(BrightcoveNewIE())
    # Test downloading of segments from the DASH manifest, where the first
    # segment contains headers necessary for joining the segments into a valid
    # MP4 file
    name = '1119012'
    result

# Generated at 2022-06-14 15:28:33.172513
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """Test for DashSegmentsFD."""

    # This is a constructor test.
    # No need to set up a MockYoutubeDL object.
    DashSegmentsFD()


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:28:41.471338
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import argparse
    import json
    import os
    import shutil
    import tempfile
    import youtube_dl.YoutubeDL
    import youtube_dl.FileDownloader

    def get_test_video_url(test_video_ind):
        assert test_video_ind == 1
        return ('https://manifest.googlevideo.com/api/manifest/dash/'
                'source/youtube/video/0nt8Pt2uPQQ')

    args = argparse.Namespace()
    args.output_template = '%(id)s.%(ext)s'
    ydl_opts = {}
    fd = youtube_dl.FileDownloader(ydl_opts, args)
    ie = fd.ies_by_url[get_test_video_url(1)]()
    info

# Generated at 2022-06-14 15:28:53.422958
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():

    from .utils import _download_json
    from .http import HttpFD
    from .dash import parse_dash_manifest


# Generated at 2022-06-14 15:28:54.413996
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD(None, None).FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:29:00.188189
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import youtube_dl.YoutubeDL
    dash_segments_fd = DashSegmentsFD(YoutubeDL({}), {})
    assert dash_segments_fd.FD_NAME == 'dashsegments'
    assert dash_segments_fd.params == {}
    assert dash_segments_fd.ydl is not None

    dash_segments_fd2 = DashSegmentsFD(YoutubeDL({}), {})
    assert dash_segments_fd2.FD_NAME == 'dashsegments'
    assert dash_segments_fd2.params == {}
    assert dash_segments_fd2.ydl is not None

# Generated at 2022-06-14 15:29:01.514585
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD(None, None, None)

# Generated at 2022-06-14 15:29:13.303930
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:29:19.287629
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YDL()
    ydl.params['max_downloads'] = 2
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(FragmentsIE())
    ydl.add_info_extractor(YoutubeIE())
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert(ydl.result['fragments'])
    assert(ydl._live_fragment_format)
    assert(ydl.params['max_downloads'])

# Generated at 2022-06-14 15:29:22.196856
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # Expected result: Download OK
    pass


# Generated at 2022-06-14 15:31:21.369462
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import youtube
    ydl = youtube.YoutubeDL({})
    ydl.add_info_extractor(youtube.YoutubeIE(ydl))
    # Check that DASH segments downloader works
    ie = youtube.YoutubeIE(ydl)
    info = ie._fetch_info('https://www.youtube.com/watch?v=dRolcBPgIdo', 'dRolcBPgIdo')
    fd = DashSegmentsFD(ydl, {'skip_unavailable_fragments': True})
    # Check that fetched fragments are different from ones in another video
    frag1 = info['fragments'][0]

# Generated at 2022-06-14 15:31:31.992990
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import argparse
    import os.path
    import sys
    import youtube_dl
    ydl = youtube_dl.YoutubeDL()
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--ytdl-patched', dest='ytdl_patched', action='store_true')
    argparser.add_argument('--test', dest='test', action='store_true')
    argparser.add_argument('--outtmpl', dest='outtmpl', nargs='?', type=str)
    argparser.add_argument('--fragment-retries', dest='fragment_retries', nargs='?', type=int)
    argparser.add_argument('--skip-unavailable-fragments', dest='skip_unavailable_fragments', action='store_true')

# Generated at 2022-06-14 15:31:43.665508
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dash import DASHIE
    from .fragment import FragmentFD
    from .http import HTTPFD
    from ..extractor import YoutubeDL
    from ..postprocessor.ffmpeg import FFmpegMetadataPP
    from ..utils import encode_data_uri
    from sys import stderr
    from ..compat import compat_urllib_error

    dash_manifest = encode_data_uri(
        DASHIE,
        'application/dash+xml')


# Generated at 2022-06-14 15:31:44.269040
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:31:52.257504
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    from .dash import DashFD

    ydl = YoutubeDL({})
    dash = DashSegmentsFD(ydl, {'fragment_base_url': 'http://url.com/'})
    assert dash.fd is None
    dash2 = DashSegmentsFD(ydl, {})
    assert dash2.fd is None
    dash3 = DashSegmentsFD(ydl, {'fragment_base_url': 'http://url.com/'})
    dash3.fd = DashFD(ydl, {'url': 'http://youtube.com/'})
    assert dash3.fd
    assert dash3.fd.ydl is ydl


# Generated at 2022-06-14 15:31:54.576082
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    dash_segments_fd = DashSegmentsFD(None)
    assert isinstance(dash_segments_fd,DashSegmentsFD)


# Generated at 2022-06-14 15:32:00.460633
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    manifest = {u'fragments': [
        {
            'path': 'video-segment-1.m4s',
        },
        {
            'path': 'video-segment-2.m4s'
        }
    ], 'fragment_base_url': 'https://foo/Path'}
    downloader = DashSegmentsFD()
    downloader.real_download('video', manifest)

# Generated at 2022-06-14 15:32:07.237472
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """
    Test for constructor of class DashSegmentsFD
    """
    filename = 'video.mp4'

# Generated at 2022-06-14 15:32:17.232764
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    ie = YoutubeIE(params={'noplaylist': True})