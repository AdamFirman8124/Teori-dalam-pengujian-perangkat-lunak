

# Generated at 2022-06-14 15:37:55.725465
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Mocking
    import types, youtube_dl.YoutubeDL
    orig_debug = youtube_dl.YoutubeDL.debug
    orig_error = youtube_dl.YoutubeDL.error
    orig_report_error = youtube_dl.YoutubeDL.report_error
    orig_to_screen = youtube_dl.YoutubeDL.to_screen
    youtube_dl.YoutubeDL.debug = dummy_debug
    youtube_dl.YoutubeDL.error = dummy_error
    youtube_dl.YoutubeDL.report_error = dummy_report_error
    youtube_dl.YoutubeDL.to_screen = dummy_to_screen
    dl = HttpQuietDownloader(youtube_dl.YoutubeDL({}), {})
    # Test
    assert type(dl.debug) == types.MethodType
    assert dl

# Generated at 2022-06-14 15:38:04.343602
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    import sys
    import textwrap
    dl = HttpQuietDownloader({}, {'quiet': True, 'noprogress': True})
    assert dl.params == HttpFD.params
    assert dl.ydl == {'quiet': True, 'noprogress': True}
    out = textwrap.dedent('''\
        [download] Downloading video 1 of 2
        [download] Downloading video 2 of 2
    ''')
    assert sys.stdout.getvalue() == out

# Generated at 2022-06-14 15:38:12.580310
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    import sys

    class FakeYDL(object):
        def __init__(self, params):
            self.params = params

        @staticmethod
        def to_screen(msg, skip_eol=False):
            return

    class FakeIE(InfoExtractor):
        def _download_webpage(self, *args, **kwargs):
            return 'webpage', 'webpage_url'

        def _real_extract(self, *args, **kwargs):
            return {
                'id': 'videoid',
                'title': 'videotitle'
            }

    ie = FakeIE({})

# Generated at 2022-06-14 15:38:19.567318
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import get_info_extractor
    ie = get_info_extractor('YoutubeBaseInfoExtractor')
    dl = HttpQuietDownloader(ie, {'quiet': True, 'noprogress': True})
    assert dl._downloader.params['quiet']
    assert dl._downloader.params['noprogress']

# Generated at 2022-06-14 15:38:32.189243
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor


# Generated at 2022-06-14 15:38:43.059039
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .dash import DashFD
    from .hls import HlsFD
    from .http import YoutubeDLHandler

    dl1 = HttpQuietDownloader(None, {'continuedl': True})
    assert dl1.params['continuedl'] == True

    dl2 = HttpQuietDownloader(None, {'noprogress': True})
    assert dl2.params['noprogress'] == True

    dl3 = HttpQuietDownloader(None, {'logger': DashFD()})
    assert isinstance(dl3.params['logger'], YoutubeDLHandler)

    dl4 = HttpQuietDownloader(None, {'external_downloader': 'ffmpeg'})

# Generated at 2022-06-14 15:38:45.178338
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Test for constructor of class HttpQuietDownloader
    assert HttpQuietDownloader

# Generated at 2022-06-14 15:38:51.678420
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD('.', None)
    assert fd._prepare_url(
        {'http_headers': {'User-Agent': 'Foo'}},
        'http://example.com/') == sanitized_Request(
        'http://example.com/', headers={'User-Agent': 'Foo'})
    assert fd._prepare_url({}, 'http://example.com/') == 'http://example.com/'

# Generated at 2022-06-14 15:38:55.788949
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .youtube import YoutubeDL
    ydl = YoutubeDL({})
    fragment_fd = FragmentFD(ydl)
    assert fragment_fd.FD_NAME == 'fragment'
    assert fragment_fd.params.get('keep_fragments', False) is False

# Generated at 2022-06-14 15:39:05.829395
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # A dummy constructor with the minimum required args
    class Constructor(FragmentFD):
        def __init__(self, ydl, *args, **kwargs):
            super(Constructor, self).__init__(ydl, *args, **kwargs)

    # A dummy constructor with the minimum required args
    # and the params specific to FragmentFD
    class ConstructorF(FragmentFD):
        def __init__(self, ydl, *args, **kwargs):
            super(ConstructorF, self).__init__(ydl, *args, **kwargs)

    # A 'real' constructor for a particular protocol
    class ConstructorR(FragmentFD):
        def __init__(self, ydl, *args, **kwargs):
            assert kwargs['protocol'] == 'protocol_name'
           

# Generated at 2022-06-14 15:39:27.210709
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # youtube_dl.FileDowloader is an abstract class hence we can't perform
    # unit test on it.
    pass

# Generated at 2022-06-14 15:39:37.892151
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import gen_extractors
    gen_extractors()
    from ..extractor.common import InfoExtractor

    class FragmentTestIE(InfoExtractor):
        IE_NAME = 'unittest'
        IE_DESC = 'Unit test'

        def __init__(self, downloader=None):
            InfoExtractor.__init__(self, downloader)

        def _real_initialize(self):
            pass

        def _real_extract(self, url):
            self.to_screen('Test output')
            return {
                '_type': 'video',
                'id': 'testid',
                'title': 'testttitle',
                'formats': [],
            }

    class FragmentFDTest(FragmentFD):
        FD_NAME = 'unittest'



# Generated at 2022-06-14 15:39:41.114480
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..cache import Cache
    from .http import HttpFD
    cache = Cache("/tmp/")
    qd = HttpQuietDownloader(None, {}, cache)
    assert isinstance(qd, HttpFD)

# Generated at 2022-06-14 15:39:42.917173
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    FileDownloader(FragmentFD.params)

# Generated at 2022-06-14 15:39:45.070606
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    result = HttpQuietDownloader({}, {}).to_screen('test')
    assert result is None

# Generated at 2022-06-14 15:39:52.089697
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from . import YoutubeDL
    ydl = YoutubeDL({'quiet': True, 'format': 'bestaudio/best', 'outtmpl': '%(id)s.%(ext)s'})
    ydl.add_default_info_extractors()
    d = FragmentFD(ydl, {'itag': 140})
    assert d.params['quiet']
    assert d.add_meta
    assert d.FD_NAME == 'audio'

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:40:02.777435
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .retry import RetryFD

    class FragmentFDSubclass(FragmentFD):
        FD_NAME = 'fragmentfd'

        def _prepare_frag_download(self, ctx):
            ctx.update({
                'tmpfilename': 'tmpfilename',
                'filename': 'filename',
                'fragment_index': 0,
                'total_frags': 10,
            })

        def _start_frag_download(self, ctx):
            return 1234

        def report_destination(self, filename):
            pass

        def ytdl_filename(self, filename):
            return filename + '.ytdl'

        def _hook_progress(self, state):
            pass

    dummy_ydl = object()

# Generated at 2022-06-14 15:40:07.971751
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader
    from .http import HttpDownloader
    from .rtmp import RtmpDownloader
    from .f4m import F4mFD

    fd1 = FileDownloader(None, {})
    assert not isinstance(fd1.httpDL, HttpQuietDownloader)
    assert not isinstance(fd1.rtmpDL, HttpQuietDownloader)

    fd2 = F4mFD(None, {})
    assert isinstance(fd2.httpDL, HttpQuietDownloader)
    assert isinstance(fd2.rtmpDL, RtmpDownloader)

# Generated at 2022-06-14 15:40:11.710288
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFragmentFD(FragmentFD):
        FD_NAME = 'testfd'

    dl = TestFragmentFD({})
    assert dl.FD_NAME == 'testfd'

# Generated at 2022-06-14 15:40:22.477679
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractors
    from .extractor.http import HttpIE
    class ie(HttpIE):
        IE_NAME = 'ie'
        def _real_extract(self, url):
            return {'id': 'test'}
    gen_extractors()
    fd = FragmentFD(gen_extractors(), ie(), {},
        'test-video.f4m', {
            'fragment_base_url': 'http://example.com/',
            'fragments': ['abc.ts', 'def.ts']
        }, 'video'
    )
    assert fd.params.get('nopart') is False

# Generated at 2022-06-14 15:41:03.238941
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    fd = HttpQuietDownloader(None, {})
    assert isinstance(fd, HttpFD)

# Generated at 2022-06-14 15:41:08.413761
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..utils import FakeYDL
    from ..extractor.common import InfoExtractor

    ydl = FakeYDL()
    ie = InfoExtractor()
    url = 'http://example.org/video.f4m'
    ie.set_downloader(FragmentFD(ydl, ie, url))

# Generated at 2022-06-14 15:41:10.578096
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert HttpQuietDownloader.__name__ == 'HttpQuietDownloader'


# Generated at 2022-06-14 15:41:12.120283
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FakeYDL
    ydl = FakeYDL()
    fd = FragmentFD(ydl)

# Generated at 2022-06-14 15:41:13.138933
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd_test_case(FragmentFD)

# Generated at 2022-06-14 15:41:21.917413
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import collections
    import types

    fd_name = 'dummy_fd'
    # Use "from downloader import Downloader" instead of "from __main__ import
    # FileDownloader" to avoid shadowing the latter with the former in globals
    from .downloader import Downloader
    fd_class = FragmentFD(Downloader({}), {'outtmpl': '-'})

    # Check that the class has the right name
    assert fd_class.FD_NAME == fd_name

    # Check that the class has the right constructor
    assert fd_class.__name__ == fd_name
    assert fd_class.__module__ == __name__

    # Check that the class has the right methods

# Generated at 2022-06-14 15:41:25.164985
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader
    # Basic test, only attributes
    ydl = FileDownloader({})
    test = HttpQuietDownloader(ydl, {})
    assert(isinstance(test, HttpQuietDownloader))

# Generated at 2022-06-14 15:41:30.221555
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import YoutubeDL
    from .http import HttpFD

    class DummyFragmentFD(FragmentFD):
        FD_NAME = 'dummy'

        def real_extract(self, *args, **kwargs):
            pass

    ydl = YoutubeDL(params={'noprogress': True})
    assert isinstance(DummyFragmentFD(ydl)._prepare_and_start_frag_download({
        'filename': 'dummy-filename',
        'fragment_index': 1,
        'total_frags': 5,
    }), HttpFD)

# Generated at 2022-06-14 15:41:33.533835
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractor
    fd = FragmentFD(gen_extractor({'name': 'test'}), {})
    assert fd.FD_NAME == 'test'

# Generated at 2022-06-14 15:41:37.024113
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ydl = FileDownloader({})
    fd = FragmentFD(ydl)
    assert fd
    assert fd.FD_NAME == 'fragment'

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:42:58.360433
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:43:01.232520
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    http_quiet_downloader = HttpQuietDownloader({}, {})
    assert not hasattr(http_quiet_downloader, 'to_screen')
    assert hasattr(http_quiet_downloader, 'report_progress')

# Generated at 2022-06-14 15:43:07.845812
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import StringIO
    global out
    out = StringIO.StringIO()
    old_stderr = sys.stderr
    sys.stderr = out
    try:
        HttpQuietDownloader(None, None)
    except Exception as e:
        assert e.message == 'YoutubeDL not available.'
    finally:
        sys.stderr = old_stderr

# Generated at 2022-06-14 15:43:08.583763
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    pass

# Generated at 2022-06-14 15:43:19.572040
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        def __init__(self, ydl=None, params={}):
            self.logger = {}
            self.params = params
            self.ydl = ydl
            self.finished = False
            self.to_screen = self._screen_writer('Destination: ')
            self.report_destination = self._screen_writer('Destination: ')
            self.report_progress = self._screen_writer('Progress: ')
            self.report_warning = self._screen_writer('Warning: ')
            self.report_error = self._screen_writer('Error: ')

        def _screen_writer(self, prefix):
            def screen_writer(msg):
                self.logger[prefix] = msg
            return screen_writer


# Generated at 2022-06-14 15:43:27.283044
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class DummyInfoDict(object):
        def __init__(self):
            self.http_headers = {'Range': 'bytes=0-'}
    class DummyYDL(object):
        def __init__(self):
            self.params = {'continuedl': True}
    class DummyDl(object):
        def __init__(self):
            self.add_progress_hook = lambda x: None
            self.report_destination = lambda x: None
            self.download = lambda x, y: True
    fd = FragmentFD(DummyYDL())

# Generated at 2022-06-14 15:43:28.523019
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    HttpQuietDownloader(None, None)

# Generated at 2022-06-14 15:43:33.251108
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor

    # Testing only the constructor for now
    class DummyIE(InfoExtractor):
        def _real_extract(self, url):
            pass

    ie = DummyIE(None)
    assert isinstance(ie.fd, HttpQuietDownloader)

# Generated at 2022-06-14 15:43:38.112695
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FakeYDL:
        def prepare_filename(self, info_dict):
            return info_dict['url']

        def to_screen(self, *args, **kargs):
            pass

    ydl = FakeYDL()

    fd = FragmentFD(ydl)
    assert fd.ydl == ydl
    assert len(fd.params) == 5

# Generated at 2022-06-14 15:43:44.062592
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    try:
        import __main__
        __main__.params = {}
        __main__.ydl = {}
    except ImportError:
        import sys
        sys.modules['__main__'] = type('', (), {
            'params': {},
            'ydl': {},
        })
    assert FragmentFD({}).params == {}

# Generated at 2022-06-14 15:46:58.928668
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import YoutubeIE
    extractor = YoutubeIE()
    fd = FragmentFD('https://www.youtube.com/watch?v=BaW_jenozKc', {})
    fd = FragmentFD('https://www.youtube.com/watch?v=BaW_jenozKc', {}, extractor)
    assert fd.params['fragment_retries'] == 10, 'Unexpected default value of fragment_retries'

# Generated at 2022-06-14 15:46:59.942155
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    res = FragmentFD('youtube-dl', {'simulate': True})
    assert res

# Generated at 2022-06-14 15:47:02.289960
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()

    assert fd.params['retries'] == 0
    assert fd.params['nopart'] is False
    assert fd.params['test'] is False


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:47:04.513861
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({'logger': None})
    assert fd.params.get('skip_unavailable_fragments') is False
    assert fd.params.get('fragment_retries') == 10
    assert fd.params.get('keep_fragments') is False

# Generated at 2022-06-14 15:47:08.882346
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class DummyYDL(object):
        params = {}
    fd = HttpQuietDownloader(DummyYDL(), {'retries': -1})
    assert fd.params['retries'] == 0
    fd = HttpQuietDownloader(DummyYDL(), {'quiet': False})
    assert fd.params['quiet']

# Generated at 2022-06-14 15:47:19.482949
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import gen_extractors
    import tempfile
    import shutil

    class FragmentFDTest(FragmentFD):
        def _prepare_and_start_frag_download(self, ctx):
            self._prepare_frag_download(ctx)
            self._start_frag_download(ctx)
            ctx['tmpfilename'] = '-'
            ctx['dest_stream'] = open(os.devnull, 'wb')
            ctx['fragment_count'] = 10
            ctx['fragment_index'] = 0
            ctx['started'] = time.time()
            ctx.update({
                'complete_frags_downloaded_bytes': 0,
                'prev_frag_downloaded_bytes': 0,
            })