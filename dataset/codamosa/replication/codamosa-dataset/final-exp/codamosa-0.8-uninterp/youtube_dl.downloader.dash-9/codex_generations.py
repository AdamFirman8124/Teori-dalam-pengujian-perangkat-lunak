

# Generated at 2022-06-14 15:22:29.566105
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    print("test_DashSegmentsFD!")
    from .http import HttpFD
    from .m3u8 import M3U8FD
    from ..downloader import Downloader
    dl = Downloader()

    for url in [
            'https://github.com/ytdl-org/youtube-dl/issues/15171',
            'https://github.com/ytdl-org/youtube-dl/issues/15242']:
        http_fd = HttpFD(dl, url)
        m3u8_fd = M3U8FD(dl, http_fd, url)
        dash_fd = DashSegmentsFD(dl, m3u8_fd, url)

if __name__ == "__main__":
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:22:36.411547
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # Function test_DashSegmentsFD_real_download is adapted from test_FragmentsFD_real_download
    # in test_fragment.py.
    # This unit test test that the code of DashSegmentsFD_real_download
    # executes without an exception.
    # This function does not test thatDashSegmentsFD_real_download works as intended.
    # At this moment there is no way to test this method without input from a manifest
    # file (see lines 46-50 in dash.py).
    from ..downloader.common import file_transport_available
    from ..downloader.http import HttpFD
    from ..extractor import (
        get_info_extractor,
        gen_extractors,
    )
    from ..utils import (
        sanitize_open,
        sanitized_Request,
    )

# Generated at 2022-06-14 15:22:38.373893
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-14 15:22:49.140303
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .test.test_downloader import FakeYDL
    from .test.test_downloader import content_filename
    from .test.test_downloader import DummyHttpServer
    from .test.test_downloader import fragment_retries
    from ..extractor import YoutubeIE
    from ..utils import compat_urlparse
    from ..downloader.common import FileDownloader

    url = 'http://127.0.0.1:8791/manifest/dash_fragments'
    manifest_url = url
    fragments = [
        {'path': 'frag1'},
        {'path': 'frag2'},
        {'path': 'frag3'},
    ]

    retries = fragment_retries()


# Generated at 2022-06-14 15:22:50.310884
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # I don't know how to test this yet
    return False

# Generated at 2022-06-14 15:22:57.805503
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dash import (
        parse_dash_manifest,
        get_dash_manifest
    )

    from ..YoutubeDL import YoutubeDL
    from ..downloader.common import FileDownloader
    from ..extractor.youtube import YoutubeIE

    def get_yt_dl(downloader, params=None):
        if params is None:
            params = {}
        params.update({
            'youtube_include_dash_manifest': True
        })
        return YoutubeDL({
            'logger': YoutubeDL.null_logger(),
            'params': params
        }).add_default_info_extractors()

    def get_fd(downloader, ie, params=None):
        if params is None:
            params = {}

# Generated at 2022-06-14 15:23:07.953668
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor.common import extensions_to_list
    from ..downloader import FileDownloader
    from ..extractor import YoutubeIE
    from ..utils import match_filter_func

    dl = FileDownloader({
        'format': 'bestvideo+bestaudio/best',
        'noprogress': True,
        'nooverwrites': True,
        'force_generic_extractor': True,
        'min_filesize': 1,
        'max_filesize': 10,
        'test': True,
        'skip_unavailable_fragments': False,
        'outtmpl': '%(id)s-%(format)s.%(ext)s',
    }, YoutubeIE(), lambda *a, **k: None)
    dl.add_info_extractor(YoutubeIE())
   

# Generated at 2022-06-14 15:23:17.407581
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    youtube_ie = YoutubeIE()
    # "url" is passed to test the `_download_fragment()` method
    res = youtube_ie.extract(url="https://www.youtube.com/watch?v=UxxajLWwzqY")
    dash_segments_fd = DashSegmentsFD()

# Generated at 2022-06-14 15:23:29.501051
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import sys
    import os
    import tempfile
    from subprocess import Popen, PIPE
    from ..downloader import dash_fd_constructor, FileDownloader

    n_fragments=20
    if len(sys.argv) < 3:
        print('usage: %s <URL> <FILENAME> [<TEMPFILENAME>]' % sys.argv[0])
        sys.exit(1)
    url = sys.argv[1]
    filename = sys.argv[2]
    if len(sys.argv) >= 4:
        tempfilename = sys.argv[3]
    else:
        tempfile.tempdir = os.path.dirname(filename)
        tempfilename = tempfile.mkstemp(prefix='pytube_dashing_')[1]
    f

# Generated at 2022-06-14 15:23:38.583953
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import shutil
    import tempfile

    directory = tempfile.mkdtemp()
    filename = "test.mpd"
    path = os.path.join(directory, filename)
    open(path, "w").close()

# Generated at 2022-06-14 15:23:54.462687
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.params['fragment_retries'] = 3
    ydl.params['skip_unavailable_fragments'] = False
    ydl.params['test'] = True
    # Test a non-existent video (the fragments should not be downloaded, but the retry logic should work)
    filename = '/tmp/ytdl_frag_dash.mp4'

# Generated at 2022-06-14 15:23:56.859237
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    try:
        assert(DashSegmentsFD)
    except:
        raise AssertionError("Class DashSegmentsFD is not defined")


# Generated at 2022-06-14 15:23:59.973823
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD('', {'fragments':[{'path':'path1', 'url':'url1'},{'path':'path2', 'url':'url2'}] })

# Generated at 2022-06-14 15:24:11.896265
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    """
    Purpose of this test is to check whether a broken manifest can be downloaded
    """
    import sys
    import os
    import shutil
    import tempfile
    import subprocess
    from ..utils import prepend_extension
    from ..downloader.common import FileDownloader
    filename = "test_DashSegmentsFD_real_download"

# Generated at 2022-06-14 15:24:24.335620
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import pytest

    # Test --skip-unavailable-fragments download
    with pytest.raises(DownloadError):
        DashSegmentsFD().real_download("", {
            "fragment_base_url": "https://manifest_baseurl.com",
            "fragments": [
                {"path": "https://manifest_baseurl.com/dummy_path", "duration": 1},
                {"path": "https://manifest_baseurl.com/dummy_path2", "duration": 1},
                {"path": "https://manifest_baseurl.com/dummy_path3", "duration": 1},
                {"path": "https://manifest_baseurl.com/dummy_path4", "duration": 1},
            ],
        })

    # Test --skip-unavailable-fragments

# Generated at 2022-06-14 15:24:29.941496
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dash import dash_segments_from_xml, DashSegmentsFD
    # Test the constructor of DashSegmentsFD class
    dash_segments_from_xml('a', 'b', 'c')
    # Test the constructor of FragmentFD class
    DashSegmentsFD('a', 'b', 'c')

# Generated at 2022-06-14 15:24:33.359071
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dash import DashSegmentsFD as DashSegmentsFD_module

    DashSegmentsFD_module.FragmentFD = FragmentFD
    try:
        DashSegmentsFD_module(None, None, None, None, None)
    except:
        assert False

# Generated at 2022-06-14 15:24:43.125782
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import re
    import math
    import random
    import hashlib
    import tempfile

    # import test_downloader
    # import video_utils
    from .fragment import FragmentFD, FragmentFD_data
    from .dashsegments import DashSegmentsFD
    from .youtube_dl import YoutubeDL
    # from .utils import (
    #     encodeFilename,
    #     cleanup
    # )

    def calc_md5(filename):
        with open(filename,"rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    # Temporary directory for testing
    tmp_dir = tempfile.mkdtemp()

    # Prepare params for the downloader

# Generated at 2022-06-14 15:24:53.505653
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dash import parse_representation_base_url
    import re

    # Set mock info_dict
    fragments = []
    fragments.append({'path':'0/00000000/00000001.m4s','url':None})
    fragments.append({'path':'0/00000000/00000002.m4s','url':None})
    fragments.append({'path':'0/00000000/00000003.m4s','url':None})
    fragments.append({'path':'0/00000000/00000004.m4s','url':None})

# Generated at 2022-06-14 15:25:02.025434
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dash import DashFD
    from ..downloader.common import FileDownloader
    from ..extractor.generic import YoutubeIE
    from ..compat import compat_str
    dash_downloader = FileDownloader({
        'usenetrc': False,
        'verbose': False,
        'quiet': True,
        'simulate': True,
        'skip_download': True,
        'nooverwrites': True,
        'format': '140',
    })
    url = 'https://www.youtube.com/watch?v=hcOvbhz9Xn0'
    info = dash_downloader.extract_info(url, download=False)
    dash_downloader.prepare_filename(info)
    dash_fd = DashFD(dash_downloader, YoutubeIE(), url, info)


# Generated at 2022-06-14 15:25:22.984553
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os.path
    from .http import HttpFD
    from .dash import DashFD
    from ..downloader import Downloader
    from ..YoutubeDL import YoutubeDL

    # Get a DASH manifest and extract the fragments
    URL = 'http://dash.edgesuite.net/envivio/EnvivioDash3/manifest.mpd'
    fd = HttpFD(Downloader({}), URL, {})
    dash_doc, dash_info = fd.get_manifest_and_info(URL)
    dash = DashFD(Downloader({}), URL, dash_info)
    segments = dash.get_fragment_urls_and_headers()

    # Get the video title, so that we can name the output file

# Generated at 2022-06-14 15:25:31.546170
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dash import DashFD
    from .http import HttpFD
    import sys
    import os
    import urllib
    import tempfile
    import threading
    import socket
    import re
    # Workaround to remove the dependency on cryptography in pydub
    import pydub.utils
    pydub.utils.PROCESS_NULL = open(os.devnull, 'r')
    class XMLFD(HttpFD):
        def real_download(self, filename, info_dict):
            video_id = info_dict['id']
            url = 'http://localhost:8090/%s.xml' % video_id
            return super(XMLFD, self).real_download(filename, {'id': 'xml', 'url': url, '_filename': filename})

# Generated at 2022-06-14 15:25:32.854228
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD("", {})

test_DashSegmentsFD()

# Generated at 2022-06-14 15:25:43.629673
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    '''
    Unit test for constructor of class DashSegmentsFD
    '''
    import time
    import youtube_dl
    import os
    import re
    import shutil

    # Create a youtube_dl instance
    ydl_opts = {}
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    # Set the DASH manifest URL

# Generated at 2022-06-14 15:25:46.066563
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    _ = DashSegmentsFD()


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:25:54.739024
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dash import DashFD
    from .http import HttpFD
    from .http2 import Http2FD
    from .https import HttpsFD
    from .hls import HlsNativeFD
    from .hls import HdsFD
    from .m3u8 import M3u8FD
    assert DashSegmentsFD is not None
    assert issubclass(DashSegmentsFD, FragmentFD)
    assert not issubclass(DashSegmentsFD, HttpFD)
    assert not issubclass(DashSegmentsFD, Http2FD)
    assert not issubclass(DashSegmentsFD, HttpsFD)
    assert not issubclass(DashSegmentsFD, HlsNativeFD)
    assert not issubclass(DashSegmentsFD, HdsFD)

# Generated at 2022-06-14 15:26:07.276191
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # 1. Test DASH manifest with URL-encoded paths
    #    https://github.com/ytdl-org/youtube-dl/issues/7336

    info_dict = {
        'url': 'http://youtube.com',
        'fragments': [
            {
                'path': 'b%3Dto_mp4%26g%3D3A6o8U6J%252BjQQhog%253D%253D%26f%3Dmp4_hd1080%252Clen_2849',
            },
        ],
    }

    dash_fd = DashSegmentsFD()
    dash_fd._prepare_and_start_frag_download({'filename': 'abc'}, info_dict)
    assert dash_fd.tmpfilename == 'abc.part'

    # 2. Test D

# Generated at 2022-06-14 15:26:17.553840
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    def test_download_and_concatenate_fragments(input_, url, params):
        """
        Assert that input fragments, if downloaded and concatenated, produces the expected output.
        """

        from .http import HttpFD
        from .test import MockYdl, MockInfoDict
        from ..utils import determine_ext

        def mock_download_fragment(ctx, fragment_url, info_dict):
            """
            This is a mock implementation of the _download_fragment method for the DashSegmentsFD
            class, it will return the content of the fragment as is when called.
            """

            import posixpath
            from ..utils import sanitize_open

            # We want the filename to be the name of the fragment, if available,
            # otherwise just the basename of the url.

# Generated at 2022-06-14 15:26:22.655999
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """
    Make sure that constructor of class DashSegmentsFD doesn't fail
    """
    params = {
        'quiet': False,
        'noprogress': False,
    }
    DashSegmentsFD(params)

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:26:34.592785
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeIE
    from ..downloader.common import FileDownloader
    from ..utils import sanitize_open

    # Basic test
    fields = [
        'id', 'upload_date', 'uploader', 'description', 'title',
    ]

    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    dl = FileDownloader(YoutubeIE(), params={'outtmpl': '%(id)s.%(ext)s'})
    info_dict = dl.extract(url)
    info_dict = {field: info_dict[field] for field in fields}

# Generated at 2022-06-14 15:27:00.370865
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fragment_downloader = DashSegmentsFD()
    assert fragment_downloader.params.get("test") == False
    assert fragment_downloader.params.get("fragment_retries") == 0
    assert fragment_downloader.params.get("skip_unavailable_fragments") == True
    
test_DashSegmentsFD()

# Generated at 2022-06-14 15:27:00.983277
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:27:09.189700
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import sys
    import io

    if sys.version_info[0] < 3:
        raise Exception("This test can't run under Python 2.")

    from ..extractor import YoutubeIE
    from ..utils import get_cachedir

    ydl = YoutubeIE("", {})

    dashsegmentsfd = DashSegmentsFD("", {})
    dashsegmentsfd.params = {'noprogress': True}
    dashsegmentsfd.report_destination = io.StringIO()
    dashsegmentsfd.report_progress = lambda frag_index: None
    dashsegmentsfd._make_cmd = lambda _: [sys.executable, __file__]
    dashsegmentsfd.to_screen = lambda _: None


# Generated at 2022-06-14 15:27:12.093485
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert(DashSegmentsFD.FD_NAME == 'dashsegments')

# Unit test

# Generated at 2022-06-14 15:27:22.402666
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    d = DashSegmentsFD({})
    # Use a simple fragment downloader in mock to avoid download real data
    from ..downloader.http import HttpFD
    orig_dashsegments_frag_downloader = d.fragment_downloader
    def mock_fragment_downloader(*args):
        return orig_dashsegments_frag_downloader(HttpFD, *args)
    d.fragment_downloader = mock_fragment_downloader
    # Generate some fake fragments
    info_dict = {'fragments': []}
    import random
    import string
    random_chars = string.ascii_letters + string.digits

# Generated at 2022-06-14 15:27:31.923631
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # Following code is only executed when this file is run as a script
    # We prepare a mock for class FileDownloader
    import sys
    class DummyFD(object):
        def to_screen(self, msg):
            print(msg)

    # Following lines makes sure that the unit test can run alone
    # sys.modules["__main__"].FileDownloader = DummyFD

    # Following code is the unit test itself
    from .common import fake_options, fake_info_dict
    # Create a DashSegmentsFD object
    fd = DashSegmentsFD(DummyFD(), fake_options(), fake_info_dict())
    # Call method real_download of the object with suitable arguments

# Generated at 2022-06-14 15:27:38.343177
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .dashsegments import DashSegmentsFD
    import json
    import os
    import pytest
    from ..extractor.youtube import YoutubeIE
    from ..utils import encodeFilename, strip_jsonp, FileDownloader

    testdata_dir = os.path.join(os.path.dirname(__file__), 'testdata')
    fd = FileDownloader(params={'skip_unavailable_fragments': False, 'test': False})

    # Test video: ttajbnFcjb8
    fd.add_info_extractor(YoutubeIE())
    with open(os.path.join(testdata_dir, 'ttajbnFcjb8_vcodec_dash.json'), 'r', encoding='utf-8') as f:
        fd._ies = []
        fd.add

# Generated at 2022-06-14 15:27:49.960819
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .smoothstreams import SmoothStreamsFD
    from ..downloader import Downloader
    from ..utils import prepend_extension, std_headers

    downloader = Downloader(default_params={
        'fragment_retries': 10,
    })
    info_dict = {
        'url': 'https://host.com/manifest',
        'fragments': [],
        'fulltitle': 'Sample title',
        'title': 'title',
        'id': 'video id',
        'ext': 'mp4',
        'display_id': 'Sample video',
        'http_headers': std_headers,
    }
    assert not DashSegmentsFD(downloader, info_dict).suitable
    info_dict['smoothstreams_manifest'] = 'manifest'
    assert not DashSegments

# Generated at 2022-06-14 15:28:02.305214
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from io import StringIO
    from .http import HttpFD
    from .fragment import SegmentedFragmentFD
    from ..compat import compat_urlparse
    from ..extractor import gen_extractors
    def download_dash_segments():
        for ie in gen_extractors():
            if isinstance(ie, HttpFD) or isinstance(ie, SegmentedFragmentFD):
                return ie

    dash_ie = download_dash_segments()

    # Create a mock http.downloader.http object
    class FakeHTTPDownloadHandler(object):
        def __init__(self, test):
            self._test = test
        def __enter__(self):
            return self
        def __exit__(self, *_):
            pass

# Generated at 2022-06-14 15:28:03.686032
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    pass

# Generated at 2022-06-14 15:28:58.676045
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YoutubeDL import YoutubeDL
    from .dashsegments import DashSegmentsFD
    from .fragment import FragmentFD
    from .hls import HlsFD
    from .http import HttpFD
    from .f4m import F4mFD
    from .__main__ import parseOpts
    import unittest
    import tempfile
    import os
    import shutil
    import time
    import sys
    if sys.version_info < (3, 4):
        from mock import patch
    else:
        from unittest.mock import patch

    class TestDashSegmentsFD(unittest.TestCase):
        # General test for class DashSegmentsFD
        def test_dashsegments(self):
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_file = os.path

# Generated at 2022-06-14 15:29:09.926345
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # Test constructor
    dashsegment = DashSegmentsFD('test-url', { 'testfrag': True }, 'test-dest',
            'test-play-path')
    assert dashsegment.params['fragment_base_url'] == 'test-url'
    assert dashsegment.params['extra_param_to_segment_url'] == { 'testfrag': True }
    assert dashsegment.params['filename'] == 'test-dest'
    assert dashsegment.params['play_path'] == 'test-play-path'
    assert dashsegment.params['test'] == False
    assert dashsegment.params['test_fragments'] == None


# Generated at 2022-06-14 15:29:18.941635
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:29:30.925292
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import time
    import os
    import shutil
    from .helpers import (
        FakeYDL,
        FakeFileDownloader,
        CacheClass,
        mock_dummy_system
    )
    from ..utils import (
        write_json_file,
        read_json_file,
    )
    from ..compat import compat_urllib_error

    # Start of unit test

# Generated at 2022-06-14 15:29:36.330197
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    '''
    Test whether the constructor of class DashSegmentsFD is working
    '''
    try:
        dashsegments_fd = DashSegmentsFD()
    except Exception as e:
        print('Call to constructor of class DashSegmentsFD failed: %s' %type(e))
        return
    print('%s call to constructor of class DashSegmentsFD successful' %type(dashsegments_fd))

# Generated at 2022-06-14 15:29:43.911696
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .http import HttpFD

    url = 'http://example.com/manifest.mpd'
    dash_fd = HttpFD(dict(params={}, ytdl_options={}, downloader=None), url)
    dash_info = dash_fd.real_extract()
    assert dash_info.get('fragments')
    dash_seg_fd = DashSegmentsFD(dict(params={}, ytdl_options={}, downloader=None), dash_info)
    dash_seg_fd.real_download('', dash_info)

# Generated at 2022-06-14 15:29:46.618634
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:29:47.302354
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:29:48.780797
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # No test at the moment
    pass

# Generated at 2022-06-14 15:29:57.982813
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    filename = 'videoplayback.mp4'

# Generated at 2022-06-14 15:32:13.001605
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor.youtube import YoutubeIE
    ydl = YoutubeIE()
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert True