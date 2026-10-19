

# Generated at 2022-06-14 15:37:51.046292
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from . import YoutubeDL

    def raiseError(self, *args, **kargs):
        raise Exception('error_to_compat_str')

    HttpFD.error_to_compat_str = raiseError

    ydl = YoutubeDL()
    assert isinstance(HttpQuietDownloader(ydl), HttpFD)
    assert HttpQuietDownloader(ydl).params['quiet'] is True
    assert HttpQuietDownloader(ydl).params['noprogress'] is True

# Generated at 2022-06-14 15:38:03.908434
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert(issubclass(FragmentFD, FileDownloader))
    assert(hasattr(FragmentFD, '_prepare_url'))
    assert(hasattr(FragmentFD, '_prepare_and_start_frag_download'))
    assert(hasattr(FragmentFD, '_download_fragment'))
    assert(hasattr(FragmentFD, '_append_fragment'))
    assert(hasattr(FragmentFD, '_prepare_frag_download'))
    assert(hasattr(FragmentFD, '_start_frag_download'))
    assert(hasattr(FragmentFD, '_finish_frag_download'))
    fd = FragmentFD(True, None)
    assert(isinstance(FragmentFD, object))

# Generated at 2022-06-14 15:38:08.014353
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    # pylint: disable=W0612,W0613
    fd = FragmentFD({
        'params': {},
        'ydl': None,
        'tmpfilename': None,
        'filename': 'test',
        'total_frags': 1,
        'frag_index': 0,
    })
    fd.to_screen = sys.stdout.write
    fd.report_retry_fragment(ValueError('Test error'), 0, 1, 2)
    assert fd.format_retries(2) == '2 times'
    fd.report_skip_fragment(0)

# Generated at 2022-06-14 15:38:12.688444
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import gen_extractors
    class FakeInfoExtractor(object):
        IE_NAME = 'test'

    ie = FakeInfoExtractor()
    gen_extractors()
    ie.add_info_extractor(FragmentFD)

# Generated at 2022-06-14 15:38:26.143969
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FakeYDL:
        def __init__(self):
            self.tmpfilename = 'tmpfilename'
        def to_screen(self, *args):
            # Just fake output for now
            pass
        def report_destination(self, *args):
            pass
        def report_warning(self, *args):
            pass
        def calc_eta(self, *args):
            pass

    class FakeDl:
        def download(self, *args):
            pass
        def add_progress_hook(self, *args):
            pass

    ydl = FakeYDL()
    ffd = FragmentFD(ydl, {'ratelimit': 1})
    ffd.to_screen = ydl.to_screen
    ffd.report_destination = ydl.report_destination
    ffd.report_

# Generated at 2022-06-14 15:38:37.170979
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DownloadError

    class BrokenFD:
        def __init__(self, ydl, params):
            raise DownloadError(params['error'] + ' (on constructor)')

    class BrokenPFD(FragmentFD):
        def __init__(self, ydl, params):
            raise DownloadError(params['error'] + ' (on constructor)')


# Generated at 2022-06-14 15:38:41.934776
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    assert 'fragment_retries' in fd.params
    assert 'keep_fragments' in fd.params
    assert 'skip_unavailable_fragments' in fd.params

# Generated at 2022-06-14 15:38:46.822110
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    from tests.test_utils import FakeYDL

    fd = FragmentFD(FakeYDL(), {})
    assert isinstance(fd, FragmentFD)
    assert isinstance(fd.ydl, YoutubeDL)

# Generated at 2022-06-14 15:38:54.491017
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import YoutubeIE
    ydl = YoutubeIE()
    ydl.add_info_extractor(YoutubeIE())

    ydl.params.update({
        'logger': ydl._download_retry,
        'outtmpl': '%(id)s-%(tbr)s.%(ext)s',
        'continuedl': True,
        'error_catcher': lambda *args, **kargs: True,
    })

    assert isinstance(ydl, FileDownloader)
    return ydl

# Generated at 2022-06-14 15:38:57.155127
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    assert issubclass(HttpQuietDownloader, HttpFD)

# Generated at 2022-06-14 15:39:23.124285
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader
    class FakeYDL(object):
        params = {
            'noprogress': True,
            'logger': 'fake_logger',
        }
    fd = HttpQuietDownloader(FakeYDL(), {})
    assert isinstance(fd, FileDownloader)
    assert fd.params['noprogress']
    assert fd.params['logger'] == 'fake_logger'
    assert fd.ydl is FakeYDL()


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:39:27.097866
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Instantiate
    ydl = HttpQuietDownloader(None, {})
    # Check for expected methods
    for m in ('report_warning', 'to_screen', 'report_error', 'trouble'):
        assert hasattr(ydl, m)
    # Check for unexpected methods
    assert not hasattr(ydl, 'to_stdout')

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:39:29.161462
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD('test')
    assert fd.params is not None

# Generated at 2022-06-14 15:39:39.355799
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import tempfile
    import youtube_dl
    fd = FragmentFD(
        youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s', 'quiet': True}),
        {'url': 'http://fake', 'format': 'm3u8'},
        '',
        {
            'skip_unavailable_fragments': True,
            'keep_fragments': True
        })
    ctx = {
        'tmpfilename': 'tmpname.tmp',
        'dl': None,
        'filename': 'outname',
        'total_frags': 1,
        'live': False,
    }
    fd._prepare_frag_download(ctx)
    assert ctx['dl']
    assert ctx['dest_stream']

# Generated at 2022-06-14 15:39:47.814252
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FragmentFD1(FragmentFD):
        # Override this method to enable checking of values of constructor
        # parameters
        def __init__(self, ydl, params):
            super(FragmentFD1, self).__init__(ydl, params)
            self.params = params

    test_params = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
    ffd = FragmentFD1(None, test_params)
    assert ffd.params == test_params

# Generated at 2022-06-14 15:39:51.873034
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MockYDL(object):
        def __init__(self):
            self.params = {}

    fragment_fd = FragmentFD(MockYDL())
    assert fragment_fd.FD_NAME == 'fragment'
    assert fragment_fd.ydl is not None
    assert fragment_fd.params is not None

# Generated at 2022-06-14 15:40:02.659429
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from .extractor import get_info_extractor
    from .extractor.common import InfoExtractor
    from .postprocessor import PostProcessor

    class MockInfoExtractor(InfoExtractor):
        def _real_extract(self, url):
            return {
                'id': 'myid',
                'ext': 'mp4',
                'title': 'mytitle',
                'formats': [{
                    'url': 'http://example.com/myvideo.mp4',
                    'format_id': 'myformat',
                }],
            }

    class MockPostProcessor(PostProcessor):
        def run(self, info):
            pass

    sys.modules['youtube_dl.extractor.test'] = MockInfoExtractor
    sys.modules['youtube_dl.postprocessor.test'] = Mock

# Generated at 2022-06-14 15:40:07.234601
# Unit test for constructor of class FragmentFD
def test_FragmentFD():

    fd = FragmentFD(None, {'noprogress': True})
    assert isinstance(fd, FileDownloader)
    assert not hasattr(fd, 'ydl')

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:40:12.327693
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    '''
    Unit test for constructor of class FragmentFD
    '''
    import sys
    from .common import FileDownloader
    from .options import Options
    from ..compat import compat_urllib_request
    from ..utils import get_cachedir

    FD = FragmentFD

    fd = FD(
        Options({'verbose': True, 'format': 'bestvideo', 'skip_download': True, 'nooverwrites': True, 'forcejson': True}),
        sys.stdout,
        get_cachedir(),
        compat_urllib_request,
        FileDownloader,
        None)

    opts = fd.params

    assert opts.get('format') == 'bestvideo'
    assert opts.get('verbose') is True

# Generated at 2022-06-14 15:40:25.145368
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import tempfile
    def test_frag_hook(status):
        print(status)

    class FakeYDL:
        params = {}
        def __init__(self):
            self._progress_hooks = [test_frag_hook]
            self.to_screen = sys.stdout.write
            self.to_stderr = sys.stderr.write
        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)

    ydl = FakeYDL()
    tmpdir = tempfile.mkdtemp(suffix='-ydl-test')

# Generated at 2022-06-14 15:41:04.725312
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def dummy_callback(state):
        pass
    fd = FragmentFD('url', {'params': {'outtmpl': '%(id)s'}}, dummy_callback)
    assert fd


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:41:07.928720
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractors
    gen_extractors()  # Load extractors
    # Test without optional arguments without raising any exception
    fd = FragmentFD({})

# Generated at 2022-06-14 15:41:13.797790
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    expected = {
        'skip_unavailable_fragments': False,
        'continuedl': True,
        'noprogress': False,
        'retries': 10,
        'ratelimit': None,
        'nopart': False,
        'test': False
    }
    assert fd._ydl_opts == expected


# Generated at 2022-06-14 15:41:22.594717
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def qprint(obj):
        assert isinstance(obj, dict)
        assert obj['status'] == 'finished'
        assert obj['_total_bytes_estimate'] == 0
    from .extractor import gen_extractors
    gen_extractors()
    from .extractor.youtube import YoutubeIE
    from .extractor.generic import UrlIE
    from .utils import ExtractorError

    ie = UrlIE(YoutubeIE(), 'http://example.org/')

# Generated at 2022-06-14 15:41:26.478609
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from . import YoutubeDL
    ydl = YoutubeDL()
    http_dl = HttpFD(ydl, {'noprogress': True, 'quiet': True})
    http_dl = HttpQuietDownloader(ydl, {'noprogress': True})

# Generated at 2022-06-14 15:41:33.960979
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import unittest
    import sys
    import tempfile

    class TestHttpQuietDownloader(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_HttpQuietDownloader(self):
            output = tempfile.NamedTemporaryFile()
            sys.stdout = output
            retcode = HttpQuietDownloader(None, {'url': 'http://github.com'}).download()
            output.flush()
            self.assertEqual(retcode, 0)
            output.seek(0)
            self.assertEqual(output.read(), "")
            output.close()

    unittest.main()

if __name__ == "__main__":
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:41:41.090189
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HeadRequest
    from .http import HttpFD
    from .common import FileDownloader
    hqd = HttpQuietDownloader(FileDownloader({}), {'noprogress': True})
    assert hqd
    assert isinstance(hqd, HttpFD)
    assert callable(hqd.to_screen)
    assert hqd.params['noprogress']
    assert hqd.params['quiet']
    assert isinstance(hqd.request(HeadRequest('http://localhost')), HeadRequest)

# Generated at 2022-06-14 15:41:46.628153
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # pylint: disable=protected-access
    assert (HttpQuietDownloader._setup_opener.__func__
            is HttpFD._setup_opener.__func__)
    assert (HttpQuietDownloader._real_initialize.__func__
            is HttpFD._real_initialize.__func__)
    assert (HttpQuietDownloader._do_download.__func__
            is HttpFD._do_download.__func__)
    assert (HttpQuietDownloader._do_retry.__func__
            is HttpFD._do_retry.__func__)
    assert (HttpQuietDownloader._finish_download.__func__
            is HttpFD._finish_download.__func__)

# Generated at 2022-06-14 15:41:58.392060
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from ..utils import prepend_extension

    ydl = type(str('FakeYoutubeDL'), (object,), {})()
    hqd = HttpQuietDownloader(ydl, {'restrictfilenames': True})
    assert isinstance(hqd.ydl, type(ydl))

    hqd.params['outtmpl'] = 'test'
    hqd.params['continuedl'] = False
    hqd.params['noprogress'] = False
    assert hqd.prepare_filename('foo') == 'test.part'

    for suffix in ('flv', 'mp4', 'webm'):
        hqd.params['restrictfilenames'] = False

# Generated at 2022-06-14 15:42:06.168716
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpQuietDownloader
    from .extractor import get_info_extractor
    from .downloader.common import FileDownloader

    # Correct initialization of a single instance

# Generated at 2022-06-14 15:43:26.287240
# Unit test for constructor of class FragmentFD
def test_FragmentFD():

    retries = 5
    quiet = False
    skip_unavailable_fragments = False
    params = {
        'fragment_retries': retries,
        'quiet': quiet,
        'keep_fragments': True,
        'skip_unavailable_fragments': skip_unavailable_fragments,
    }
    info_dict = {
        'id': 'test_frag_id',
        'title': 'test title',
    }

    class MockYoutubeDL(object):
        def __init__(self, params):
            self.params = params
            self.to_screen = lambda *x, **xx: None
            self.report_error = lambda msg: None

        @staticmethod
        def temp_name(filename):
            return 'test_temp_name'


# Generated at 2022-06-14 15:43:37.117813
# Unit test for constructor of class FragmentFD

# Generated at 2022-06-14 15:43:48.178440
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from .common import FileDownloader
    from .extractor import gen_extractors

    extractors = gen_extractors()
    for ie in extractors:
        ie.ydl = FileDownloader(params={})

    test_url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    test_ie = [ie for ie in extractors if ie.suitable(test_url)][0]

    dl = HttpQuietDownloader(test_ie.ydl, None)

    def noop(*args, **kargs):
        pass

    dl.report_error = dl.report_warning = dl.report_resuming_byte = noop
    dl.report_retry = dl.report_file_already_downloaded = noop

# Generated at 2022-06-14 15:43:48.710714
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    pass

# Generated at 2022-06-14 15:44:01.392248
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import tempfile
    from .extractor.youtube import YoutubeIE
    from ..compat import compat_urlparse

    video_id = 'BaW_jenozKc'
    youtube_ie = YoutubeIE()

    class FakeYDL:
        params = {}

        def __init__(self):
            self._ies = [youtube_ie]
            self.cache = {}
            self.params = {}
            self.to_screen = sys.stdout.write
            self.to_stderr = sys.stderr.write

        def report_warning(self, msg):
            self.to_stderr('WARNING: ' + msg + '\n')

        def extract_info(self, url, download=False, ie_key=None):
            if ie_key is None:
                ie_key = self

# Generated at 2022-06-14 15:44:07.362332
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class YDL(object):
        def __init__(self, params):
            self.params = params
            self.to_screen = lambda *x: None

    fd = HttpQuietDownloader(YDL(dict()), {'a': 1})
    assert fd.ydl.params == {'a': 1}
    fd = HttpQuietDownloader(YDL(dict(b=2)), {'a': 1})
    assert fd.ydl.params == {'b': 2, 'a': 1}

# Generated at 2022-06-14 15:44:10.970277
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    import sys
    sys.stdout = open(os.devnull, 'w')
    try:
        assert HttpFD().to_screen() is None
    finally:
        sys.stdout = sys.__stdout__

# Generated at 2022-06-14 15:44:19.205553
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    fd = HttpQuietDownloader(None, {
        'continuedl': False,
        'noprogress': True,
        'ratelimit': None,
        'retries': 10,
        'quiet': True,
        'nopart': False,
        'test': False,
    })
    assert not hasattr(fd, 'to_screen')

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:44:28.180474
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys

    class MockYDL(object):
        def __init__(self):
            self.params = {}
            self.cache = {}
            self.progress_hooks = []

        def add_progress_hook(self, ph):
            self.progress_hooks.append(ph)

        def to_screen(self, s, skip_eol=True):
            if isinstance(s, str):
                s = s.decode('ascii', 'ignore')
            sys.stdout.write(s)
            if not skip_eol:
                print('')

    fd = FragmentFD(MockYDL(), {})
    assert fd.params == {}
    assert fd.cache == {}
    assert fd.FD_NAME == 'fragment'

    # Test whether _prepare_

# Generated at 2022-06-14 15:44:33.671500
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    from .downloader.common import FileDownloader
    from .compat import compat_str
    import sys
    import time

    class TestExtractor(InfoExtractor):
        IE_DESC = 'Test'
        IE_NAME = 'test'
        _VALID_URL = r'https?://(?:www\.)?example\.com/'

        def report_warning(self, msg):
            sys.stderr.write('[warning] %s\n' % msg)

        def report_error(self, msg, tb=None):
            if tb:
                raise Exception('TestExtractorError: ' + msg)

    class TestDownloader(FileDownloader):
        FD_NAME = 'test'

        def report_warning(self, msg):
            sys.st