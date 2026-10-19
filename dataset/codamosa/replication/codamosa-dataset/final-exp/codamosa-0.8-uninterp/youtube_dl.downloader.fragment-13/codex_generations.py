

# Generated at 2022-06-14 15:37:54.770837
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor.common import InfoExtractor
    class TestIE(InfoExtractor):
        def _real_extract(self, url):
            self.to_screen('Test IE: This is just a test')
            return {
                'id': 'test_id',
                'ext': 'mp4',
                'url': 'http://www.youtube.com/watch?v=BaW_jenozKc',
                'title': 'test_title',
            }
    ie = TestIE(HttpQuietDownloader())
    ie.download('http://www.youtube.com/watch?v=BaW_jenozKc')

# Generated at 2022-06-14 15:38:02.216843
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    hqd = HttpQuietDownloader(None, {})
    assert hqd.ydl is None
    assert hqd.params == {}
    hqd = HttpQuietDownloader(1, {'continuedl': True, 'noprogress': True})
    assert hqd.ydl == 1
    assert hqd.params == {'continuedl': True, 'noprogress': True}

# Generated at 2022-06-14 15:38:08.717250
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader

    # Let's assume that HttpQuietDownloader is inherited from FileDownloader
    assert issubclass(HttpQuietDownloader, FileDownloader)

    # Let's assume that HttpQuietDownloader is inherited from FileDownloader
    assert issubclass(HttpQuietDownloader, FileDownloader)
    # Now we can check the constructor of FileDownloader.
    # If we do not use super() it will fall
    assert issubclass(HttpQuietDownloader, FileDownloader)

# Generated at 2022-06-14 15:38:16.381737
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .common import FileDownloader

    dl = HttpQuietDownloader(None, {'continuedl': True, 'quiet': True, 'noprogress': True})
    try:
        assert isinstance(dl, HttpFD)
        assert isinstance(dl, FileDownloader)
    except AssertionError:
        return False

    return True

# Generated at 2022-06-14 15:38:20.613221
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD.__bases__[0] == FileDownloader
    fd = FragmentFD(None, {})
    assert fd.FD_NAME == 'fragment'



# Generated at 2022-06-14 15:38:22.816969
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    HttpQuietDownloader({}, {'quiet': True, 'noprogress': True})


# Generated at 2022-06-14 15:38:26.083917
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class DummyYDL:
        params = {}
    d = HttpQuietDownloader(DummyYDL(), {})
    assert d.ydl is DummyYDL

# Generated at 2022-06-14 15:38:32.124409
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class MockYDL(object):
        def __init__(self):
            self._progress_hooks = []

        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)

    ydl = MockYDL()
    HttpQuietDownloader(ydl, {})
    assert len(ydl._progress_hooks) == 1

# Generated at 2022-06-14 15:38:33.148840
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:38:39.737928
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor.common import InfoExtractor

    ies = [u'dummy']
    params = {u'quiet': True}
    ie = InfoExtractor('test', ies)
    ie._setup_opener()
    ie.add_info_extractor(ies[0])
    ie.params = params
    dl = HttpQuietDownloader(ie, params)
    assert dl._opener is not None

# Generated at 2022-06-14 15:39:07.823674
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=W0212
    fd = FragmentFD()
    fd.add_default_extra_info({'http_headers': {'User-Agent': 'Test'}})
    info_dict = {}
    assert fd._prepare_url(info_dict, 'http://localhost/') == 'http://localhost/'
    info_dict['http_headers'] = {'Test': 'Header'}
    assert (
        fd._prepare_url(info_dict, 'http://localhost/').get_full_url()
        == 'http://localhost/')
    assert dict(
        fd._prepare_url(info_dict, 'http://localhost/').header_items()
    ) == {'User-Agent': 'Test', 'Test': 'Header'}

# Generated at 2022-06-14 15:39:20.546156
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import datetime
    from .common import FileDownloader
    from .http import HttpFD
    from ..utils import DateRange
    from ..compat import is_py2

    from .common import FakeYDL
    ydl = FakeYDL()
    fd = FragmentFD(ydl)

    # Test the constructor
    assert fd.params == {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'retries': 0,
        'nopart': False,
        'test': False
    }
    assert fd.ydl is ydl
    assert fd.max_fragment_retries == 10

    # Test realtime() method
    assert isinstance(fd.realtime(), float)

    # Test calc_eta() method

# Generated at 2022-06-14 15:39:25.861872
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import tempfile
    from .fragment import FragmentFD
    from .dash import DASHFD
    from .hls import HLSFD
    from .hlsnative import HLSNativeFD
    from .http import HttpFD
    for fd_class in (FragmentFD, DASHFD, HLSFD, HLSNativeFD, HttpFD):
        fd = fd_class({})
        fd.params['noprogress'] = True
        # Make sure we get an error with non existing file:
        tmpfilename = tempfile.mkstemp()[1]
        try:
            fd.report_destination(tmpfilename)
            assert False
        except Exception:
            pass
        # Make sure we get no error with existing file:
        fd.report_destination(__file__)


# Generated at 2022-06-14 15:39:27.922455
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader(None, {})
    assert dl.ydl is None



# Generated at 2022-06-14 15:39:38.416600
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor

    def _test_constructor(ie_key, params, expected_params):
        ie = get_info_extractor(ie_key)()
        downloader = ie.get_info_extractor(ie.url)()
        downloader.params = params
        downloader._prepare_and_start_frag_download({
            'filename': 'test.flv',
            'total_frags': 100,
        })
        actual_params = downloader.params
        assert actual_params == expected_params

    # Default parameters

# Generated at 2022-06-14 15:39:49.827292
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import gen_extractors
    class MyInfoExtractor(FragmentFD):
        IE_NAME = 'fragmentfd'
        IE_DESC = False
        _VALID_URL = r'(?x)^https?://.+'
        _TEST = {
            'info_dict': {},
            'params': {
                'skip_download': True,
            }
        }
    gen_extractors.add_ie(MyInfoExtractor)
    import sys
    myfd = MyInfoExtractor(sys.argv[0])

# Generated at 2022-06-14 15:39:52.626406
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    http_downloader = HttpQuietDownloader(None, {})
    assert http_downloader.params['logger'] == http_downloader

# Generated at 2022-06-14 15:39:55.202183
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    '''Unit test for constructor of class FragmentFD'''
    return


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:40:07.652746
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor
    from .extractor.common import InfoExtractor
    from .extractor.common import SearchInfoExtractor
    from .downloader.http import HttpFD
    from .downloader.f4m import F4mFD
    from .downloader.hls import HlsFD
    from .downloader.hls import HlsNativeFD
    from .downloader.dash import DashSegmentsFD
    from .compat import compat_str

    ie = InfoExtractor('foo')
    assert isinstance(ie.ydl, HttpQuietDownloader)

    ie = SearchInfoExtractor('foo')
    assert isinstance(ie.ydl, HttpQuietDownloader)

    ie = gen_extractor({'IE_NAME': 'foo'})

# Generated at 2022-06-14 15:40:12.688078
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    assert isinstance(fd, FragmentFD)
    assert fd.params == {
        'fragment_retries': 10,
        'keep_fragments': False,
        'skip_unavailable_fragments': True,
    }

# Generated at 2022-06-14 15:40:43.117802
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ydl = object
    params = {
        'continuedl': True,
        'nopart': True,
        'ratelimit': '1k',
        'retries': 5,
        'test': True,
        'keepfragments': False,
        'skip_unavailable_fragments': True,
        'fragment_retries': 5,
    }
    fd = FragmentFD(ydl, params)
    assert fd

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:40:48.977025
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    from .http import HttpFD
    from .dash import DASHFD
    from .hls import HLSFD
    from .smoothstreams import SmoothstreamsFD
    assert issubclass(FragmentFD, FileDownloader)
    assert issubclass(DASHFD, FragmentFD)
    assert issubclass(HLSFD, FragmentFD)
    assert issubclass(SmoothstreamsFD, FragmentFD)

# Generated at 2022-06-14 15:40:52.084486
# Unit test for constructor of class FragmentFD
def test_FragmentFD(): # pylint:disable=unused-variable
    fd = FragmentFD({}, {}, {})
    assert fd is not None

# Generated at 2022-06-14 15:41:01.188758
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def prepare_frag_download(ctx):
        ctx.update({
            'filename': 'test.mp4',
            'total_frags': 5,
            'fragment_index': 3,
        })
        ff = FragmentFD(
            None, {
                'retries': 3,
            }
        )
        ff._prepare_frag_download(ctx)
        return ff

    class FakeFD(object):
        def download(self, filename, info_dict):
            if filename == 'test.mp4-Frag3':
                return True
            else:
                return False

        def add_progress_hook(self, hook):
            pass

    ff = prepare_frag_download({})
    ff.to_screen = lambda *args, **kargs: None

# Generated at 2022-06-14 15:41:01.906131
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    pass

# Generated at 2022-06-14 15:41:06.875559
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    # Check that the constructor is actually defined
    HttpQuietDownloader()
    # Check that the constructor actually does what it is intended to do
    assert HttpQuietDownloader.to_screen != HttpFD.to_screen

# Generated at 2022-06-14 15:41:17.889443
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpQuietDownloader
    from .extractor import YoutubeIE
    from .downloader.common import FileDownloader
    from .compat import compat_http_client
    from .postprocessor.common import FFmpegPostProcessor
    from .utils import DateRange
    from .extractor import gen_extractors

    def _hook(status):
        if status['status'] == 'finished':
            state['num_frags_downloaded'] += 1

    def _test_HttpQuietDownloader(d, info_dict):
        state['num_frags_downloaded'] = 0
        d.add_progress_hook(_hook)
        success = d.download(info_dict)
        return success, state['num_frags_downloaded']


# Generated at 2022-06-14 15:41:25.423751
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .options import parseOpts
    from .extractor import gen_extractors
    from .extractor.common import InfoExtractor
    from .extractor.common import YoutubeIE

    for ie in gen_extractors():
        if not hasattr(ie, '_TEST') or ie._TEST is None:
            continue
        if issubclass(ie.__class__, InfoExtractor):
            test, result = ie._TEST
        elif issubclass(ie.__class__, YoutubeIE):
            continue  # We do not need to test YoutubeIE
        else:
            raise TypeError('Unexpected base class %r' % ie.__class__)

        opts = parseOpts(test, ['noprogress'])
        ie = ie.suitable(test)
        if ie:
            ie.ext

# Generated at 2022-06-14 15:41:26.392082
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:41:30.552597
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor_classes

    from .common import FileDownloader, YoutubeDL
    from .http import HttpQuietDownloader

    ydl = YoutubeDL()
    hd = HttpQuietDownloader(ydl, {
        'quiet': True,
        'noprogress': False,
    })
    assert isinstance(hd, FileDownloader)

# Generated at 2022-06-14 15:42:21.684639
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from . import YoutubeDL
    from .extractor.common import InfoExtractor
    from .downloader.common import FileDownloader
    from .postprocessor import FFmpegMetadataPP
    from .utils import DateRange
    from .compat import compat_http_client

    class MockInfoExtractor(InfoExtractor):
        _WORKING = False

    class MockHttpDl(FileDownloader):
        def real_download(self, filename, info_dict):
            self.to_screen('[mock] Downloading')
            ctx = self.ydl.ctx
            ctx['tmpfilename'] = '-'
            ctx['filename'] = '-'
            ctx['complete_frags_downloaded_bytes'] = 0
            ctx['started'] = time.time()
            ctx['speed'] = float('inf')

            #

# Generated at 2022-06-14 15:42:30.625588
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import unittest

    class TestFragmentFD(unittest.TestCase):
        def setUp(self):
            self.options = {
                'fragment_retries': 2,
                'skip_unavailable_fragments': False,
                'keep_fragments': False,
            }

        def test_options(self):
            self.assertEqual(self.options['fragment_retries'], 2)
            self.assertEqual(self.options['skip_unavailable_fragments'], False)
            self.assertEqual(self.options['keep_fragments'], False)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFragmentFD)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-14 15:42:41.010005
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import youtube
    from ..downloader import common

    def test_fragment_download(params):
        total_frags = 3
        ctx = {}
        dl = FragmentFD(youtube.YoutubeIE(params), params)


# Generated at 2022-06-14 15:42:48.520722
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    from ..utils import encode_data_uri

    class FakeIE(InfoExtractor):
        def __init__(self, downloader=None, params=None):
            self._downloader = downloader
            self._params = params
            self._ies = []

        def _real_extract(self, url):
            raise NotImplementedError

        def to_screen(self, message):
            pass

        def _download_webpage(self, *args, **kwargs):
            pass

        def _download_webpage_handle(self, *args, **kwargs):
            return None, None

        def _download_json(self, *args, **kwargs):
            raise NotImplementedError


# Generated at 2022-06-14 15:42:52.522630
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import youtube_dl.FileDownloader

    sys.modules.pop('youtube_dl', None)
    fd = youtube_dl.FileDownloader(params={})
    assert isinstance(fd, FragmentFD)

# Generated at 2022-06-14 15:42:57.547130
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class YDL(object):
        params = {}

    ydl = YDL()
    dl = HttpQuietDownloader(ydl, {'retries': 0})

    # test that _retry_max_bytes is set to 0
    assert dl._retry.max_bytes == 0

    # test that retries is set to 0
    assert dl._opener.retries == 0

# Generated at 2022-06-14 15:43:08.733156
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    info_dict = {
        'id': 'A',
        'title': 'A',
        'url': 'http://a.com/a',
    }
    params = {
        'prefix': '[prefix] ',
        'fragment_retries': 'infinite',
        'skip_unavailable_fragments': True,
        'keep_fragments': True
    }
    ydl = DummyYDL()
    fragfd = FragmentFD(ydl, info_dict, params)

# Generated at 2022-06-14 15:43:10.707455
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    fd = FragmentFD(None)
    assertFileDownloader(fd)

# Generated at 2022-06-14 15:43:15.870977
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .fragment import FragmentFD
    from .dash import DASHFD
    from .hls import HLSFD
    assert issubclass(FragmentFD, HttpFD)
    assert issubclass(DASHFD, FragmentFD)
    assert issubclass(HLSFD, FragmentFD)

# Generated at 2022-06-14 15:43:17.232647
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    fd = FragmentFD(ydl)
    assert fd.params['retries'] == 10

# Generated at 2022-06-14 15:44:40.046645
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD.__name__ == 'FragmentFD'

# Generated at 2022-06-14 15:44:42.257474
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(None, None, None)
    assert isinstance(fd, FragmentFD)

# Generated at 2022-06-14 15:44:50.622218
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    from ..extractor import gen_extractors
    from .rtmp import RtmpFD
    from .http import HttpFD
    from .hls import HlsFD
    from .dash import DashFD

    fake_params = {
        'test': True,
        'format': 'TestFormat/333',
    }

    # Test http formats
    ie = InfoExtractor(gen_extractors())
    ie.add_info_extractor(gen_extractors()['generic'])
    c = HttpFD(ie)
    c.params = fake_params
    assert isinstance(c, FragmentFD)

    # Test rtmp formats
    ie = InfoExtractor(gen_extractors())

# Generated at 2022-06-14 15:44:55.555178
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # test constructor with no parameters
    dl = HttpQuietDownloader(object(), {})
    assert dl.ydl is not None
    assert dl.params == {}
    # test constructor with parameters
    dl = HttpQuietDownloader(object(), {'key': 'value'})
    assert dl.ydl is not None
    assert dl.params == {'key': 'value'}

# Generated at 2022-06-14 15:45:03.467304
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class Sub(FragmentFD):
        pass
    Sub.FD_NAME = 'Sub'

    # Simulate FFmpegFD
    Sub.params = {
        'keepfragments': True,
    }
    Sub.to_screen = print
    Sub.report_warning = lambda *args, **kwargs: None
    Sub.report_destination = lambda *args, **kwargs: None
    Sub.temp_name = lambda *args, **kwargs: 'out'
    Sub.ytdl_filename = lambda *args, **kwargs: 'out.ytdl'
    Sub.try_rename = lambda *args, **kwargs: None
    Sub.calc_eta = lambda *args, **kwargs: None
    Sub.params = {
        'keepfragments': True,
    }


# Generated at 2022-06-14 15:45:08.276820
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpDownloader
    # Test that HttpQuietDownloader is a subclass of HttpDownloader
    assert issubclass(HttpQuietDownloader, HttpDownloader)

# Generated at 2022-06-14 15:45:10.896689
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD(None, None).FD_NAME

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:45:19.386852
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MockDict(dict):
        pass
    mock_info_dict = MockDict()
    mock_info_dict['http_headers'] = {
        'User-Agent': 'TestUserAgent'
    }

    class MockYDL(object):
        params = MockDict()
        params.update({
            'noprogress': False,
            'ratelimit': None,
            'retries': 10,
            'fragment_retries': 10,
            'skip_unavailable_fragments': True,
            'keep_fragments': True,
            'test': False,
        })
        def download(self, *args, **kwargs):
            pass

    mock_ydl = MockYDL()
    ff = FragmentFD(mock_ydl, mock_info_dict, {})



# Generated at 2022-06-14 15:45:22.364153
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    dummy_fd = FragmentFD(None, {'params': {}}, None, None)
    assert dummy_fd.FD_NAME == 'fragment'
    assert dummy_fd.params.get('keep_fragments') is False

# Generated at 2022-06-14 15:45:33.097226
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    from .downloader.external import ExternalFD
    from .downloader.rtmp import RtmpFD