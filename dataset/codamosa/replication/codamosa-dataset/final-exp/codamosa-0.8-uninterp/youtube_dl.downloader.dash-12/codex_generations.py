

# Generated at 2022-06-14 15:22:33.660800
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dash_manifest import DashManifestFD
    from ..extractor import gen_extractors
    from ..utils import determine_extractor

    extractors = gen_extractors()
    dash_extractor = determine_extractor('https://stupidedia.org/video/test/test.mpd', extractors)
    assert dash_extractor.__class__ is DashManifestFD

# Generated at 2022-06-14 15:22:34.179117
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD()

# Generated at 2022-06-14 15:22:43.651098
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import json
    import time
    import shutil
    from tempfile import mkdtemp

    from .dash import parse_mpd_formats, dash_extract_cdns
    from .http import HttpFD
    from .utils import sanitize_open
    from ..utils import (
        # ensure_dir,
        prepend_extension,
        # unescapeHTML,
        # write_json_file
        )

    mpd_base = 'https://dash.akamaized.net'
    mpd_url = mpd_base + '/envivio/EnvivioDash3/manifest.mpd'

    with HttpFD() as http_fd:
        dash_doc, manifest_url, manifest_type = http_fd.get_dash_manifest(mpd_url)
        formats

# Generated at 2022-06-14 15:22:54.184329
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..utils import tests_dir
    from ..downloader.common import FileDownloader
    from ..downloader.http import HttpFD

    info_dict = {
        'id': 'test',
        'fragment_base_url': '',
        'fragments': [
            {'path': 'test_data/test.mp4'},
            {'path': 'test_data/test.mp4'}
        ],
        'protocol': 'm3u8_native',
        'format': 'mp4'
    }
    test_downloader = FileDownloader({'nopart': True, 'continuedl': False, 'nocheckcertificate': True, 'test': True})
    test_downloader.add_info_extractor(HtmlIE())
    test_downloader.add_info_

# Generated at 2022-06-14 15:23:00.492174
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import YoutubeDL
    from ..downloader import FileDownloader
    from .dash import DashManifestFD
    url = 'http://example.com/dash.mpd'
    ydl = YoutubeDL()

    ydl.params['test'] = True
    ydl.params['outtmpl'] = '%(id)s'

    info_dict = {
        'id': 'testid',
        'title': 'abc',
        'alt_title': 'abc',
        'duration': 10,
        'formats': [],
        'fragments': [{'url': 'http://example.com/dash.mpd'}],
        'fragment_base_url': None
    }
    d = FileDownloader(ydl, info_dict)


# Generated at 2022-06-14 15:23:03.531389
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    """
    Simple unit test for DashSegmentsFD.
    """
    DashSegmentsFD(None, None, {})

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:23:14.413316
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .dash import parse_mpd_formats
    import xml.etree.ElementTree as ET


# Generated at 2022-06-14 15:23:16.226827
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(params={})
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:23:28.463741
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..downloader import FileDownloader
    from ..extractor import YoutubeIE
    from ..utils import match_filter_func
    from .fragment import FragmentsFD
    info_dict = YoutubeIE().extract('https://www.youtube.com/watch?v=_HSylqgVYQI')

# Generated at 2022-06-14 15:23:37.434895
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import re,os
    from ..extractor import YoutubeIE
    from ..utils import ytdl_url_hook
    from ..downloader import YoutubeDL
    from ..compat import compat_urllib_request

    url = 'https://www.youtube.com/watch?v=M8CT1DfQ2eY'
    ie = YoutubeIE()
    ydl = YoutubeDL({'quiet': True})
    compat_urllib_request.urlopen = ytdl_url_hook
    # from here, you can perform unit tests with the 'ydl' object as a YoutubeDL instance
    # Return the relevant information from the URL
    info = ie._real_extract(url)
    # TODO: Write a test to check if all segments were downloaded successfully



# Generated at 2022-06-14 15:23:44.701327
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # TODO
    pass

# Generated at 2022-06-14 15:23:46.596805
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    dash_fd = DashSegmentsFD()
    assert dash_fd.FD_NAME == 'dashsegments'

# Generated at 2022-06-14 15:23:51.148353
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    d = DashSegmentsFD(None, None, {'fragments': [{'url': 'https://fragment_url'}]}, None, None)
    d.real_download('test_filename', {})

test = test_DashSegmentsFD_real_download

if __name__ == '__main__':
    test()

# Generated at 2022-06-14 15:24:02.550781
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..downloader import YoutubeDL
    from .dashmanifest import DashManifestFD
    from .http import HttpFD

    ydl = YoutubeDL({'skip_download': True, 'simulate': True, 'quiet': True, 'format': 'bestvideo[protocol^=http]'})
    ydl.add_info_extractor(DashManifestFD())
    # Make sure HttpFD will not be tested
    ydl.add_info_extractor(DashSegmentsFD())
    ydl.prepare_filename()
    ie = ydl.ies[0]

    segments = []
    ie.params['test'] = True
    def test_download_seg(filename, info_dict):
        segments.append(getattr(filename, 'url', filename))
    ie.to_screen = test_download_seg
   

# Generated at 2022-06-14 15:24:13.656418
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    """
    Usage:
    $ python -m youtube_dl.downloader.dash --test "https://link.to.dash.manifest"
    """
    from ..extractor import gen_extractors
    from ..downloader.http import HttpFD
    from ..utils import encode_data_uri
    from ..postprocessor import run_postprocessors
    from ..compat import compat_urllib_request
    from .dash import DASHDownloader
    from .http import HLSFD
    from .ism import ISMFD
    from .fragment import FragmentFD
    from .common import FileDownloader
    from .external import ExternalFD

    gen_extractors()
    FileDownloader.debug = True
    HttpFD.close_connection = False

    # TODO: Use legacy FFmpegPostProcessor
    # TOD

# Generated at 2022-06-14 15:24:25.591947
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..utils import determine_ext

    from .fragment import FragmentFD
    from .http import HttpFD
    from .file import FileFD
    from .executive import Executive
    from .f4m import F4mFD
    from .hls import HlsFD
    from .smoothstreams import SmoothStreamsFD
    from .m3u8 import M3U8_FORMATS, M3u8FD

    class DummyFD(object):
        def __init__(self, downloader):
            self.downloader = downloader

    class DummyError(Exception):
        pass

    class DummyInfoDict(object):
        def __init__(self):
            pass

    class DummyFragment(object):
        def __init__(self, content):
            self.content = content


# Generated at 2022-06-14 15:24:27.547737
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # TODO: Provide unittest for method real_download of class DashSegmentsFD
    assert False

# Generated at 2022-06-14 15:24:36.646560
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import io
    from .mock import MockHttpServer, MockHttpRequestHandler, MockSocketFileObject

    from requests.exceptions import HTTPError
    # DASH manifest

# Generated at 2022-06-14 15:24:40.019608
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from .fragment import get_fragment_retries

    fd = DashSegmentsFD(downloader=None, params=dict(fragment_retries=7))
    assert get_fragment_retries(fd) == 7

# Generated at 2022-06-14 15:24:46.689023
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    filename = 'hello_world.mp4'
    url = 'http://dash-manifest.test.com/test.mpd'
    base_url = 'http://dash-manifest.test.com/'
    fragment_url = 'fragment.mp4'
    info_dict = {
        'manifest_url': url,
        'fragment_base_url': base_url,
        'fragments': [
            {
                'url': fragment_url
            },
        ],
    }
    fd = DashSegmentsFD(filename, info_dict)
    assert fd.fd_name == 'dashsegments'
    assert fd.filename == filename
    assert fd.info_dict == info_dict
# ---------------------

# Generated at 2022-06-14 15:25:06.798978
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    import tempfile
    temp_file=tempfile.NamedTemporaryFile()
    print(temp_file.name)
    temp_file.close()
    d={u'_type': u'url', u'protocol': u'https', u'title': u'Just a test', u'encrypted': False, u'url': u'https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd', u'ext': u'mpd', 'format':{}}
    ff=DashSegmentsFD({"outtmpl":temp_file.name},d)
    ff.real_download(temp_file.name, d)

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:25:15.077381
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    """
    Test that Dash request works
    """

    result = DashSegmentsFD().real_download('test_filename', {
        'fragment_base_url': 'https://test_base.com',
        'fragments': [
            {
                'path': 'segment1',
                'duration': 1,
            },
            {
                'path': 'segment2',
                'duration': 2,
            }
        ]
    })

    assert result is True, 'DashSegmentsFD.real_download returned unexpected value'

# Generated at 2022-06-14 15:25:18.541673
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    d = DashSegmentsFD(None)
    assert d.FD_NAME == 'dashsegments'
    assert d.logger.name == '.'.join(['youtube_dl', 'downloader', 'dashsegments', ''])

# Generated at 2022-06-14 15:25:29.759001
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    class DummyInfoDict:
        def __init__(self):
            self.fragment_base_url = 'https://manifest_base.com/'

# Generated at 2022-06-14 15:25:31.075961
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # Constructor of class DashSegmentsFD
    DashSegmentsFD(params)

# Generated at 2022-06-14 15:25:31.666287
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:25:42.117250
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor.youtube import YoutubeIE
    from ..compat import compat_urllib_request
    from ..utils import sanitize_open
    from .dashmanifest import DashManifestFD
    from .utils import DownloadContext, enc_json_loads


# Generated at 2022-06-14 15:25:51.483061
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # In order to run this test it's needed to put 'dash_manifest' file in the same directory
    # with the test and it is also needed to be called dash_manifest.mpd
    # as it's specified in test_manifest_file
    test_manifest_file = 'dash_manifest'

    import os
    from .common import FakeYDL
    from ..utils import encodeFilename

    file_name = encodeFilename('dash_segments')

    # Create a fake info_dict for the test
    test_fake_ydl = FakeYDL()
    test_file_path = os.path.join(
        os.getcwd(), test_manifest_file + '.mpd')

    # Capture the string with the manifest from real_download
    cap_manifest_str = ''

# Generated at 2022-06-14 15:25:54.265527
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert hasattr(DashSegmentsFD(), "__init__")
    assert hasattr(DashSegmentsFD(), "real_download")

# Generated at 2022-06-14 15:26:03.197589
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .http import HttpFD
    from .m3u8 import M3U8FD
    from .dash import DASHFD
    from .f4m import F4MFD

    # Create a fake DASH manifest that can be used to test DashSegmentsFD.real_download()

# Generated at 2022-06-14 15:26:40.065946
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .fragment import DummyFragmentFD, DummyYTIE
    from ..extractor import YoutubeIE
    from ..compat import compat_http_client
    from .fragment import download
    from urllib.parse import parse_qs
    from .download import YoutubeDLHandler

    # Handling of YoutubeDLHandler in real_download, no HTTPError is occurred
    def real_download_test(self, filename, info_dict):
        # _download_fragment should be called once
        with test_self.assertRaises(StopIteration):
            next(test_self.http_dll)
        # _append_fragment should be called once
        test_self.assertTrue(self._append_fragment.called)
        # _finish_frag_download should be called once
        test_self.assertTrue

# Generated at 2022-06-14 15:26:48.431600
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from ..YtdlHooks import YtdlHooks
    from ..extractor.common import InfoExtractor
    from ..utils import cached_property, encode_data_uri
    from ..compat import compat_urllib_parse_urlparse

    class TestIE(InfoExtractor):
        @cached_property
        def _yt_api_data(self):
            return {
                'display_id': 'DUMMYID',
                'title': 'DUMMY TITLE',
                'formats': [{
                    'url': encode_data_uri(b'DUMMY DATA URI'),
                    'format_id': 'DUMMY FORMAT'
                }]
            }

    hooks = YtdlHooks()
    ie = TestIE(hooks)

    # test with expected data

# Generated at 2022-06-14 15:26:59.699150
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    DashSegmentsFD(params = {}, ydl = None)
    DashSegmentsFD(params = {'test' : True}, ydl = None)
    DashSegmentsFD(params = {'fragment_retries' : 3}, ydl = None)
    DashSegmentsFD(params = {'skip_unavailable_fragments' : True}, ydl = None)
    DashSegmentsFD(params = {'skip_unavailable_fragments' : False}, ydl = None)
    DashSegmentsFD(params = {'quiet' : True}, ydl = None)
    DashSegmentsFD(params = {'test' : True, 'fragment_retries' : 3, 'skip_unavailable_fragments' : True, 'quiet' : True}, ydl = None)

# Generated at 2022-06-14 15:27:08.245299
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import urllib
    from .common import get_testdata_files_dir
    from .fake_filesystem_downloader import FakeFsDownloader

    files_dir = get_testdata_files_dir()
    dash = files_dir / 'dash.mpd'

    info = {
        'num': 2,
        'fragments': [
            {'url': 'http://localhost:8333/a.ts'},
            {'url': 'http://localhost:8333/b.ts'}
        ],
    }

    output = 'dash_segment_download.mp4'
    dl = FakeFsDownloader(params={'noprogress': True})

    fragment_downloader = DashSegmentsFD(dl, info, params={'noprogress': True})
    fragment_downloader.real_download

# Generated at 2022-06-14 15:27:09.133214
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD({})

# Generated at 2022-06-14 15:27:10.595131
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    pass

# Generated at 2022-06-14 15:27:12.573445
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD()

if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2022-06-14 15:27:22.685927
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import youtube_dl
    from ..utils import DateRange
    from .http import HttpFD

    input_params = {
        'n_frags': 10,
        'frag_size': 5000000,
        'test': False,
        'frag_index': 0,
        'url_handle': HttpFD('http://www.youtube.com/watch?v=BaW_jenozKc'),
    }

    dash_fd = DashSegmentsFD(input_params)

    # The following raises NotImplementedError since it is a
    # DownloadError
    dash_fd.report_retry_fragment(DownloadError('blah'), 1, 2, 3)

    # The following is just a sanity test, it doesn't check the validity
    # of the data returned
    print('-' * 40)

# Generated at 2022-06-14 15:27:24.549579
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    dfd = DashSegmentsFD({})
    assert dfd.fragment_index == 0

# Generated at 2022-06-14 15:27:25.731802
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD({})

# Generated at 2022-06-14 15:28:35.449451
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from .http import HTTPFD
    from ..extractor.youtube import YoutubeIE
    downloader = YoutubeIE().downloader

    # Test 1: fragment_retries = 0 and skip_unavailable_fragments = False

# Generated at 2022-06-14 15:28:36.145999
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass


# Generated at 2022-06-14 15:28:43.425476
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # Arrange
    import json
    json_string='{\
    "fragment_base_url":"https://test.com",\
    "fragments":[\
        {"path":"filename.mp4",\
        "duration":1.0,\
        "url":"https://test.com/filename.mp4"}]\
    }'
    json_data=json.loads(json_string)
    filename="filename.mp4"

    # Act
    result = DashSegmentsFD.real_download(DashSegmentsFD(), filename, json_data)

    # Assert
    assert result == True

# Generated at 2022-06-14 15:28:44.173143
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    pass

# Generated at 2022-06-14 15:28:56.027625
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():

    # required and optional arguments for method real_download
    filename = 'filename.mp4'
    info_dict = {
        'fragments': [
            {'url': 'http://example.org/segment1.mp4'},
            {'url': 'http://example.org/segment2.mp4'},
            {'url': 'http://example.org/segment3.mp4'}
        ]
    }


# Generated at 2022-06-14 15:29:01.991027
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..extractor import get_info_extractor
    from ..downloader import FileDownloader
    
    downloader = FileDownloader(params={}, info_dict={'url': 'https://example.com'})
    downloader.add_info_extractor(get_info_extractor('GenericIE'))
    d = DashSegmentsFD(downloader, {'noprogress': True, 'quiet': True})
    assert d.get_type() == 'dashsegments'

# Generated at 2022-06-14 15:29:13.432299
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():

    from .fragment import FragmentsFD
    from ..extractor.common import InfoExtractor
    from ..extractor.youtube import YoutubeIE

    testinst = DashSegmentsFD(YoutubeIE(), 'http://localhost/', {'test': True, 'http_chunk_size': 5})
    assert testinst.ie is YoutubeIE
    assert testinst.url == 'http://localhost/'
    assert testinst.params == {'test': True, 'http_chunk_size': 5}
    assert testinst.retries == 10

    testinst = DashSegmentsFD(YoutubeIE(), 'http://localhost/', {'test': True, 'http_chunk_size': 5}, retries=1)
    assert testinst.retries == 1


# Generated at 2022-06-14 15:29:21.324573
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():

    import json
    import os.path
    import tempfile
    import youtube_dl.FileDownloader
    #from ..YoutubeDL import YoutubeDL as YoutubeDL_Class

    # json_string contains the fragment list generated by
    # YoutubeDL.extract_info( 'https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd', process_info={'skip_download': True} )

# Generated at 2022-06-14 15:29:24.744776
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    DashSegmentsFD().real_download('temp.mp4', {'fragments': [{'url': 'http://link.com/video.mp4'}], 'fragment_base_url':''})

# Generated at 2022-06-14 15:29:33.941601
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # Test constructor of class DashSegmentsFD
    # TODO: Define input arguments for constructor
    assert FragmentFD.__module__ == 'youtube_dl.downloader.dash'
    assert DashSegmentsFD.__module__ == 'youtube_dl.downloader.dash'
    
    from .fragment import FragmentFD
    fragmentfd = FragmentFD()
    dash_segmentsfd = DashSegmentsFD()
    dash_segmentsfd.params.update(fragmentfd.params)
    dash_segmentsfd.report_skip_fragment = lambda x: print('skip_fragment {}'.format(x))
    dash_segmentsfd.report_error = lambda x: print('error {}'.format(x))

# Generated at 2022-06-14 15:31:28.289822
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # unit test for method real_download of class DashSegmentFD

    import sys
    # sys.path.append('..\..')
    if '..\\..' not in sys.path:
        sys.path.append('..\\..')
    import YoutubeDL
    

# Generated at 2022-06-14 15:31:29.932697
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    # TODO: How to unit test download?
    pass


# Generated at 2022-06-14 15:31:41.813570
# Unit test for constructor of class DashSegmentsFD

# Generated at 2022-06-14 15:31:51.547110
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    import os
    import sys
    import json
    import re
    import YouTubeDownloader
    from YouTubeDownloader.extractor import DashSegmentsFD
    from YouTubeDownloader.helpers import prepend_extension
    from YouTubeDownloader.compat import compat_urllib_error
    from YouTubeDownloader.utils import (
        DownloadError,
        urljoin,
    )

    # Get the real_download function
    real_download = DashSegmentsFD.real_download

    # Create some dummy information to send to real_download
    info_dict = {}
    info_dict['fragment_base_url'] = 'https://dash.akamaized.net/akamaized/something.mp4/'

# Generated at 2022-06-14 15:32:01.924077
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():

    from .ytdl_file_fd import YtdlFileFD
    from .http_fd import HttpFD
    from .http_request import fake_http_response, HttpRequest
    from ..downloader import FileDownloader

    import io

    dash_fd = DashSegmentsFD()
    data_url = 'http://localhost/data'
    content = b'foobar'

    # Mock
    def _download_fragment(ctx, fragment_url, info_dict):
        success, frag_content = HttpRequest(fragment_url).download()
        return success, frag_content.read()

    dash_fd._download_fragment = _download_fragment

    # No fragments
    info_dict = {}
    assert not dash_fd.real_download('filename', info_dict)

    # 1 fragment

# Generated at 2022-06-14 15:32:03.992750
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    # This function is intentionally left blank and only provided for
    # the *lazy* tests runner :)
    pass

# Generated at 2022-06-14 15:32:08.582898
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    assert DashSegmentsFD.can_download({}) == False
    assert DashSegmentsFD.can_download({'protocol': 'm3u8'}) == False
    assert DashSegmentsFD.can_download({'protocol': 'dashsegments'}) == True

# Generated at 2022-06-14 15:32:18.026913
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    from ..YoutubeDL import YoutubeDL
    options = {
        'quiet': True,
        #'verbose': True,
        'skip_download': True,
        'format': '[dashsegments]',
        'dash_fragments_inf_limit': 999999999999,
    }
    ydl = YoutubeDL(options)