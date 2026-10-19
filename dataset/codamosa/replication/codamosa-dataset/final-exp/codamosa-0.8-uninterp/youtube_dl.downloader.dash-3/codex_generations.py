

# Generated at 2022-06-14 15:22:28.741679
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import sys
    import os
    import tempfile
    import io
    import json
    import os
    import re
    import shutil
    import subprocess
    import tempfile
    import xml.etree.ElementTree
    import youtube_dl.utils

    import youtube_dl.downloader.dash

    class FakeYDL(object):
        def __init__(self):
            self.error = []
            self.to_screen = []
            self.download_retcode = 0

        def to_stderr(self, message):
            self.error.append(message)

        def to_stdout(self, message):
            self.to_screen.append(message)


# Generated at 2022-06-14 15:22:32.288135
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YoutubeDL import YoutubeDL
    from .fragment import _download_fragment as download_fragment
    import os
    import shutil
    import tempfile

    fragment_filename = 'fragment.mp4'
    expected_fragment = open(os.path.join(os.path.dirname(__file__), 'test', fragment_filename), 'rb').read()
    tmp_dir = tempfile.mkdtemp()


# Generated at 2022-06-14 15:22:42.045425
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import re
    import sys
    import tempfile

    from ..utils import (
        encodeFilename,
        get_data_files,
    )
    from .common import FileDownloader
    from .http import HttpFD
    from .http_dashsegments import setup_http_dashsegments_test
    from .f4m import F4mFD
    from .fragment import FragmentFD

    def fix_data_files(files):
        for test, data in files.items():
            if 'expected_fragments' in data:
                del data['expected_fragments']
            if 'expected_warnings' in data:
                del data['expected_warnings']

# Generated at 2022-06-14 15:22:52.294228
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:23:03.482697
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # Usage of this test is: python -m __main__
    # The test case is arranged so that the resulting file will have a length
    # of 23 seconds
    from ..compat import compat_urllib_parse
    from ..extractor import YoutubeIE
    from ..downloader import FileDownloader
    from ..postprocessor.ffmpeg import FFmpegPostProcessor

    class MockInfoDict(dict):
        def __init__(self, *args, **kwargs):
            super(MockInfoDict, self).__init__(*args, **kwargs)
            self['ext'] = 'mp4'  # Fake ext
            self['url'] = 'http://example.com'

        def __getattr__(self, name):
            return self[name]

    # Test video: "The Call Of Cthulhu"

# Generated at 2022-06-14 15:23:14.289948
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    from .f4m import F4mFD
    from .dash import (
        DashManifestFD,
        make_fake_info_dict,
    )
    from .hls import (
        HlsFD,
        HlsSegmentsFD,
    )

    assert DashSegmentsFD.is_usable(YoutubeIE()) is True

    for fd_class in (F4mFD, DashManifestFD, DashSegmentsFD, HlsFD, HlsSegmentsFD):
        assert DashSegmentsFD.is_usable(fd_class()) is False

    dash_fd = DashSegmentsFD(
        make_fake_info_dict(YoutubeIE()),
        params={'youtube_include_dash_manifest': True},
    )
    assert dash_fd

# Generated at 2022-06-14 15:23:14.858456
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    pass

# Generated at 2022-06-14 15:23:27.182915
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():

    # Here we test the basic functioning of the downloader.
    # We do not test edge cases, as this would require a too
    # big mock structure that would be hard to maintain.
    # Here we just check that the calls are being made in the
    # correct order.

    # Note that the order of the calls is important, be careful
    # when refactoring

    fd_name = 'dashsegments'

    class PseudoDashSegmentsFD(DashSegmentsFD):
        def real_download(self, filename, info_dict):
            self.assertEqual(fd_name, self.FD_NAME)
            self.assertEqual(filename, 'a filename')
            self.assertEqual(info_dict, 'a info dict')
            return True


# Generated at 2022-06-14 15:23:37.913897
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..extractor import YoutubeIE
    from ..utils import determine_ext
    from .common import FakeYDL
    from .test_fragment_downloader import BaseTestFragmentFD, get_fake_info_dict

    class FakeYTIE(YoutubeIE):

        def __init__(self, ydl, manifest, id_num):
            super(FakeYTIE, self).__init__(ydl)
            self._manifest = manifest
            self._id_num = id_num


# Generated at 2022-06-14 15:23:49.556995
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    '''
    Test DashSegmentsFD.real_download
    '''
    from .http import HttpFD
    from .rtmp import RtmpFD
    from .fragment import FragmentFD
    from ..extractor import YouTubeIE
    from ..compat import compat_urllib_error

    def _real_extract(self, url):
        # Simulate a YouTubeIE instance and extractor
        ie = YouTubeIE(self.ydl)
        ie.report_download_page = lambda *args: None
        ied = self.ying_class()
        ied.extractor = ie
        ied._setup_rtmp_download = lambda *args: None
        ied._do_download = lambda *args: True
        ied._downloader = self.ydl
        return ied._real_extract(url)

# Generated at 2022-06-14 15:23:57.628476
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import youtube_dl.downloader.http
    instance_vs_constant_test(
        youtube_dl.downloader.http.DashSegmentsFD, "real_download",
        lambda x: x.real_download("filename.mp4", {}),
        "filename.mp4",
    )

# Generated at 2022-06-14 15:24:09.471774
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import subprocess
    import tempfile
    import shutil
    import os
    import re

    # Get current directory
    d = os.path.dirname(os.path.abspath(__file__))
    os.chdir(d)

    # Get DashSegmentsFD class
    from ..extractor.common import DashSegmentsFD as _DashSegmentsFD

    # Create temporary directory
    tmpd = tempfile.mkdtemp()

    # Copy test file to temporary folder
    fd, name = tempfile.mkstemp(dir=tmpd)
    shutil.copy('files/dash_manifest.mpd', name)

    # Create test class
    params = {
        'dash_fragments': True,
        'outtmpl': 'files/outtmpl.mp4'
    }
    testclass

# Generated at 2022-06-14 15:24:11.519768
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert(DashSegmentsFD.FD_NAME in FragmentFD.available_fragment_downloaders)

# Generated at 2022-06-14 15:24:12.084401
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:24:19.620207
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import sys
    import json
    import pytest
    import youtube_dl.YoutubeDL
    import youtube_dl.extractor.youtube
    import inspect
    import tempfile
    from youtube_dl.extractor import get_info_extractor

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Change to temporary directory
    olddir = os.getcwd()
    os.chdir(tmpdir)

    edl_url = None

    # Retrieve an active ELD URL for testing
    def _test_real_download(url):
        global edl_url

        # Create a YoutubeDL Object

# Generated at 2022-06-14 15:24:21.549140
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD()
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:24:27.510100
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # Setup
    file_name = 'TEST.mpd'
    info_dict = {
        'id': 'file_id',
    }
    dash_segments_fd = DashSegmentsFD(
        ydl=None, params={},
        downloader=None, filename=file_name, info_dict=info_dict,
    )

    # Test
    dash_segments_fd.real_download(file_name, info_dict)

# Generated at 2022-06-14 15:24:29.470160
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD()
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:24:31.835921
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    print(__name__)
    print(DashSegmentsFD.FD_NAME) # dashsegments
    print(DashSegmentsFD.__doc__) # Download segments in a DASH manifest

# Generated at 2022-06-14 15:24:42.221080
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import sys
    # Override module attributes that are changed by test framework
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    # Execute test code

# Generated at 2022-06-14 15:24:56.246586
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    def _test_frag_download(fragment, fragment_url):
        assert youtube_dl.downloader.fragment.FragmentFD().real_download('.mp4',
           {'fragments': [fragment],
            'info_dict': {},
            'params': {},
           }) == True

    youtube_dl.downloader.fragment.FragmentFD.download = download
    youtube_dl.downloader.fragment.FragmentFD._finish_frag_download = finish_frag_download

    # Valid URL
    fragment = {'url': 'https://example.com/video-title.mp4'}
    _test_frag_download(fragment, fragment['url'])

    # Valid URL with query arguments

# Generated at 2022-06-14 15:25:04.492947
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    try:
        import dbm.gnu
        import dbm
    except ImportError:
        return

    import os
    import shutil
    import tempfile
    import urllib.request
    try:
        from urllib.parse import urlparse
    except ImportError:
        # Python 2
        from urlparse import urlparse

    import hashlib
    import json
    import unittest

    from ..utils import dash_identify_streams, dash_get_representation_type, dash_get_codecs

    TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_FILE = os.path.join(TEST_DIR, 'test.mp4')

    def calc_md5(file):
        md5 = hashlib.md5()

# Generated at 2022-06-14 15:25:15.734470
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:25:16.883905
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    assert False, "Not implemented"

# Generated at 2022-06-14 15:25:18.272647
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    pass


# Generated at 2022-06-14 15:25:29.459985
# Unit test for constructor of class DashSegmentsFD

# Generated at 2022-06-14 15:25:37.366692
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..downloader import YoutubeDL
    from ..extractor import YoutubeIE
    assert DashSegmentsFD.can_download({'extractor': YoutubeIE.ie_key(), 'protocol': 'm3u8_native', 'fragments': [{'url': 'http://example.com/0', 'path': '0'}, {'url': 'http://example.com/1', 'path': '1'}]})
    assert not DashSegmentsFD.can_download({'extractor': YoutubeIE.ie_key(), 'protocol': 'm3u8_native'})

# Generated at 2022-06-14 15:25:40.028439
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    from ..extractor import get_info_extractor
    ydl = YoutubeDL({})
    ie = get_info_extractor(ydl, 'youtube')
    assert DashSegmentsFD._is_available(ie)

    ydl = YoutubeDL({})
    ie = get_info_extractor(ydl, 'youtube')
    assert DashSegmentsFD._is_available(ie)

# Generated at 2022-06-14 15:25:49.681593
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import sys
    import os
    import tempfile
    import youtube_dl
    url = "http://dashdemo.edgesuite.net/envivio/dashpr/clear/Manifest.mpd"
    temp_dir = tempfile.mkdtemp(prefix = "ytdl_test_DashSegmentsFD_")
    test_fd = DashSegmentsFD(dict(params = dict(dash_fragment_base_url = "http://dashdemo.edgesuite.net/envivio/dashpr/clear/",
                                                dash_manifest_file = "Manifest.mpd",
                                                dash_fragments_prefix = "Seg1-Frag")))

# Generated at 2022-06-14 15:25:52.191054
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    t = DashSegmentsFD({})
    assert t.params['nopart'] == True
    assert t.params['test'] == False
    assert t.params['continuedl'] == True


# Generated at 2022-06-14 15:26:13.672064
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    info_dict = {}
    info_dict['fragments'] = []
    info_dict['fragments'].append({'url': 'http://a.co/abc'})
    info_dict['fragments'].append({'url': 'http://a.co/cde'})
    info_dict['fragments'].append({'url': 'http://a.co/efg'})
    info_dict['fragments'].append({'url': 'http://a.co/hij'})
    from ..utils import dashsegments
    with dashsegments.test_DashSegmentsFD() as fd:
        fd.real_download('test_DashSegmentsFD_real_download', info_dict)


# Generated at 2022-06-14 15:26:15.386288
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    pass



# Generated at 2022-06-14 15:26:27.395847
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader import Downloader
    from ..postprocessor import FFmpegMergerPP
    from ..compat import compat_urllib_request
    from ..extractor import youtube_dl
    import os

    def _test_download(downloader, ie, i, ie_result, expected_format, expected_file_size, expected_fragments_num):
        expected_file_size = expected_file_size
        def get_size(size):
            return size
        def test_result(result):
            assert result['format'] == expected_format
            assert result['file_size'] == expected_file_size

            for f in ie_result['fragments']:
                assert f.get('url') is not None

            file_count = 0

# Generated at 2022-06-14 15:26:37.609104
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """Test class DashSegmentsFD."""

# Generated at 2022-06-14 15:26:46.891505
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import sys
    import filecmp
    import platform
    from ..extractor import generate_extractors, list_extractors
    from ..utils import (
        trim_json_dumps,
        parse_m3u8_master_playlist,
        parse_m3u8_vod_playlist,
        DownloadError,
    )
    from ..downloader import FileDownloader

    # TODO: refactor test to not use code copy-pasted from __main__
    youtube_ie = None
    for ie in generate_extractors():
        if ie.IE_NAME == 'youtube':
            youtube_ie = ie
            break
    if youtube_ie is None:
        sys.exit('Error: youtube-dl not found')


# Generated at 2022-06-14 15:26:58.503113
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import json
    from ..compat import compat_urllib_error
    from .common import FakeYDL

    ydl = FakeYDL()

    info_dict = json.loads('{"fragments": [{"path": "testpath1", "duration": 1}, {"path": "testpath2", "duration": 1}, {"path": "testpath3", "duration": 1}], "fragment_base_url": "http://example.com/"}')

    def _download_fragment(self, ctx, url, info_dict):
        return True, 'HTTPBodyContent'.encode('utf-8')

    def _report_error(self, msg, tb=None):
        raise DownloadError(msg, tb)

    def _report_skip_fragment(self, frag_index):
        ydl.log

# Generated at 2022-06-14 15:27:00.890087
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD(None, None, None, None, None)


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:27:09.128782
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import shutil
    import tempfile
    import urlparse
    # Method real_download requires 'fragments' and 'fragment_base_url' in 'info_dict'
    info_dict = {
        'fragments': [{
            'url': 'http://localhost:8080/video_file_001.mp4',
            'path': 'video_file_001.mp4'
        }]
    }
    # Test real_download method with available and inaccessible HTTP server
    for available_http_server in (True, False):
        fragment_base_url = 'http://localhost:8080'
        # Start HTTP server for available HTTP server
        if available_http_server:
            import BaseHTTPServer
            import SimpleHTTPServer

# Generated at 2022-06-14 15:27:20.848217
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # create a dict for the info of the video
    info = {}
    info['id'] = "abc"
    info['title'] = "def"
    info['thumbnail'] = "ghi"
    info['description'] = "jkl"
    info['upload_date'] = "mno"
    info['uploader_id'] = "pqr"
    info['uploader'] = "stu"
    info['duration'] = 60
    info['webpage_url'] = "vwx"
    info['formats'] = []
    info['fragments'] = [{'url': 'http://a.b.c/00001'}, {'url': 'http://a.b.c/00002'}]
    info['fragment_base_url'] = 'http://a.b.c/'



# Generated at 2022-06-14 15:27:31.042602
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:27:55.905299
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    dash_fd = DashSegmentsFD()

# Generated at 2022-06-14 15:27:58.377577
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    try:
        fd = DashSegmentsFD({"test_mode": False, "fragment_base_url": "http://example.com/", "fragments": []})
        assert fd.FD_NAME == "dashsegments"
    except:
        raise

# Generated at 2022-06-14 15:28:07.220482
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2022-06-14 15:28:17.141311
# Unit test for constructor of class DashSegmentsFD

# Generated at 2022-06-14 15:28:28.044367
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..downloader import FileDownloader
    from ..YoutubeDL import YoutubeDL

    ydl_opts = {
        'simulate': True,
        'quiet': True,
    }
    # check: None is valid for segment_base_url
    ydl = YoutubeDL(ydl_opts)

    url = 'manifest_url_here'
    seg_base_url = None
    fragments = []
    seg_filename = 'segment_filename.mp4'

    info_dict = {
        'url': url,
        'manifest_url': url,
        'fragment_base_url': seg_base_url,
        'title': seg_filename,
        'fragments': fragments,
    }


# Generated at 2022-06-14 15:28:28.647824
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    return True

# Generated at 2022-06-14 15:28:38.924398
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # Tests that DashSegmentsFD downloads files in fragment_base_url/fragment['path']
    # when fragment['url'] is not set
    import os
    import tempfile
    import shutil
    import subprocess
    import test_httpserver
    with test_httpserver.Httpserver() as server:
        server.add_handler("GET", "/manifest", lambda path, query:
            (200, "OK", "application/json", '{"fragments": [{"path": "segment1.m4s", "duration": 4.04}, {"url": "%s/segment2.m4s", "duration": 4.04}]}' % server.url))

# Generated at 2022-06-14 15:28:50.982365
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import json
    import shutil
    import os

    from .http import HttpFD
    from ..extractor import get_info_extractor
    from ..utils import (
        encode_data_uri,
        parse_json,
    )

    # Create test data
    segment_data_template = "#EXTINF:5,\n{segment_data_uri}"
    segment_data_uri = encode_data_uri("TestDashSegmentsFD.real_download", "test data")
    fragments = [
        '',
        '',
        '',
        '',
        '',
        '',
        segment_data_template.format(segment_data_uri=segment_data_uri.decode('ascii')),
        '',
        '',
    ]

# Generated at 2022-06-14 15:29:01.054575
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .fragment import FragmentFD
    from .dash import DashFD
    from ..utils import (
        ExtractorError,
        RegexNotFoundError,
    )
    from ..downloader import YoutubeDL
    from .fragment import DASH_VIDEO_RE
    def get_dash_video_re():
        return DASH_VIDEO_RE

    # test for constructor
    with YoutubeDL(dict()) as ydl:
        dashfd = DashFD(ydl, dict())
        dashfd.extract()
        # test if DashSegmentsFD is returned and if DashSegmentsFD is instance of FragmentFD
        assert isinstance(dashfd, FragmentFD)
        assert isinstance(dashfd, DashFD)
        assert isinstance(dashfd, DashSegmentsFD)

# Generated at 2022-06-14 15:29:13.045686
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import time
    import random
    import os
    from subprocess import check_output
    import ytdl_utils
    from ytdl_utils import (
        DownloadError,
        prepare_filename,
        FileDownloader,
        urlopen,
    )
    from dash_manifest import (
        DashManifest,
        calculate_fragment_size,
    )
    from utils import (
        compat_urlparse,
        get_exe_version,
    )
    from path import path

    def get_frags(path, n):
        return [{'path': os.path.basename(path)} for i in range(n)]

    def generate_static_manifest(fragments, duration):
        manifest = DashManifest()
        manifest['contentType'] = 'video/mp4'
        manifest

# Generated at 2022-06-14 15:30:00.957143
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from . import dashsegments
    assert dashsegments.DashSegmentsFD.__bases__[0] == FragmentFD

# Generated at 2022-06-14 15:30:04.110750
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    dash_segments_fd = DashSegmentsFD(ydl)
    assert dash_segments_fd.FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:30:08.933037
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    try:
        import ytdl
    except ImportError:
        import YoutubeDL as ytdl
    ytdl.main(['--dump-single-json',
              'https://www.youtube.com/watch?v=rzJQeDvV8ps', '-o', '-'])

# Generated at 2022-06-14 15:30:09.441790
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    assert True

# Generated at 2022-06-14 15:30:16.576101
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import sys
    import os
    import re
    import pytest
    from .test_downloader import MockYDL, MockFD

    dashsegmentsfd = DashSegmentsFD(MockYDL(), MockFD(), None)

    assert dashsegmentsfd.params.get('test', False) == False

    dashsegmentsfd = DashSegmentsFD(MockYDL(), MockFD(), {'test': True, 'fragment_retries': 3, 'skip_unavailable_fragments': False})

    assert dashsegmentsfd.params.get('test', False) == True
    assert dashsegmentsfd.params.get('fragment_retries', 0) == 3
    assert dashsegmentsfd.params.get('skip_unavailable_fragments', True) == False

# Generated at 2022-06-14 15:30:17.686115
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass


# Generated at 2022-06-14 15:30:28.542477
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import re
    import os
    import shutil
    from .http import HttpFD
    from .external import ExternalFD
    from .dash import DashFD
    from .fragment import FragmentFD
    from .hls import HlsFD
    from .dash import _parse_mpd_formats
    from ..utils import (
        prepend_extension,
        unescapeHTML,
        ffmpeg_download_with_rtmpdump,
        sane_path,
        extract_attributes,
        encodeArgument,
    )


# Generated at 2022-06-14 15:30:37.710711
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import shutil
    import sys
    import tempfile

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    from .test_fragment import Launcher

    class TestDashSegmentsFD(Launcher):
        def __init__(self):
            super(TestDashSegmentsFD, self).__init__(DashSegmentsFD)

        def test_real_download(self):
            base_url = 'https://example.com/'
            video_id = 'video_id'

# Generated at 2022-06-14 15:30:48.050578
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os.path
    from ..utils import sanitized_Request
    from ..extractor.youtube import YoutubeIE
    from ..compat import compat_urllib_request
    from ..downloader.common import FileDownloader
    from ..downloader.http import HttpFD
    from ..downloader.external import ExternalFD

    try:
        compat_urllib_request.urlopen(sanitized_Request('https://youtube.com'))
    except compat_urllib_error.URLError as compat_urllib_error:
        from ..utils import ExtractorError
        raise ExtractorError(
            'Error downloading youtube video: %s' % compat_urllib_error.reason,
            cause=compat_urllib_error)

# Generated at 2022-06-14 15:30:55.243748
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    test_url = "https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd"
    ydl = YoutubeDL({})
    info = ydl.extract_info(test_url, download=False)
    fd = DashSegmentsFD(ydl, info)
    assert fd.get_info_dict()
    assert fd.get_fragment_retries() == 3
    assert fd.get_skip_fragments() == True