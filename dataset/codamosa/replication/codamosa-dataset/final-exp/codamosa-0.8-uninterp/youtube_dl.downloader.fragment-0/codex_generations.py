

# Generated at 2022-06-14 15:37:48.227688
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    http_fd = HttpFD(None, {})
    assert isinstance(http_fd, HttpFD)



# Generated at 2022-06-14 15:37:56.311073
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import tempfile
    import shutil
    import youtube_dl

    _id = 'test'
    _manifest = 'http://example.com/manifest.f4m'

    class TestFD(FragmentFD):
        pass

    tmpdir = tempfile.mkdtemp(prefix='youtubedl-test-')

# Generated at 2022-06-14 15:37:58.158798
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({}, None)
    assert fd.params == {}

# Generated at 2022-06-14 15:38:02.781739
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MyFD(FragmentFD):
        def __init__(self):
            self.ydl = {
                'params': {
                    'test': True,
                    'outtmpl': 'test.mp4',
                }
            }
            self.temp_name = lambda x: x
            self.ytdl_filename = lambda x: x + '.ytdl'
            self.report_warning = lambda x: None
            FragmentFD.__init__(self)

    # No ytdl file
    fd = MyFD()
    ctx = {
        'filename': 'test.mp4',
        'total_frags': 4,
    }
    fd._prepare_frag_download(ctx)
    assert ctx['fragment_index'] == 0

    # Valid ytdl file
   

# Generated at 2022-06-14 15:38:03.206252
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    pass

# Generated at 2022-06-14 15:38:14.364768
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor import YoutubeIE

    # This is a dummy YTIE for testing purposes
    class DummyYTIE(YoutubeIE):
        def _real_extract(self, url):
            return {}

    # This is a dummy FileDownloader for testing purposes
    class DummyFD(FileDownloader):
        def _prepare_and_start_frag_download(self, ctx):
            return ctx

    # This is a dummy HttpFD for testing purposes
    class DummyHttpFD(HttpFD):
        def _prepare_and_start_frag_download(self, ctx):
            return ctx

    # This is a dummy HttpQuietDownloader for testing purposes

# Generated at 2022-06-14 15:38:27.648221
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys


    class TestFD(FragmentFD):
        def __init__(self, params):
            FragmentFD.__init__(self, params)

        @staticmethod
        def calc_eta(start, now, total, downloaded):
            return 0

        @staticmethod
        def format_retries(retries):
            return str(retries)

        def to_screen(self, *args, **kargs):
            pass

        def report_warning(self, warning):
            pass

        def report_destination(self, filename):
            pass

    try:
        TestFD({}).report_retry_fragment(
            Exception('foo'),
            0,
            1,
            [None])
    except Exception:
        print('Unexpected exception', file=sys.stderr)



# Generated at 2022-06-14 15:38:29.763046
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = FileDownloader({})
    dl = HttpQuietDownloader(ydl, {})

# Generated at 2022-06-14 15:38:33.318768
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = { 'noprogress': True, 'quiet': True, 'retries': 1, 'ratelimit': 1, 'nopart': True }
    assert HttpQuietDownloader(ydl, {})

# Generated at 2022-06-14 15:38:38.674215
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..compat import compat_urllib_request

    fd = HttpQuietDownloader(
        None, {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
        })
    req = compat_urllib_request.Request('http://localhost/')
    fd.download(req, None, None)
    assert fd.ydl is None
    assert fd.params['quiet'] is True

# Generated at 2022-06-14 15:39:02.839457
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=W0613
    class ConcreteFragmentFD(FragmentFD):
        def prepare_frag_download(self, ctx):
            pass
        def start_frag_download(self, ctx):
            pass
        def finish_frag_download(self, ctx):
            pass

    ConcreteFragmentFD(None, {})

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:39:09.352110
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import StringIO
    from .common import FileDownloader
    from ..compat import ytdl_is_updateable, compat_struct_pack
    from ..utils import DateRange, DateRangeValueError
    from .f4m import F4mFD
    from .hls import HlsFD


# Generated at 2022-06-14 15:39:21.344589
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    """Check that HttpQuietDownloader parameters are propagated correctly."""
    dl = HttpQuietDownloader(None, {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'ratelimit': 10,
        'retries': 5,
        'nopart': True,
        'test': True,
    })
    assert dl.params['continuedl'] == True
    assert dl.params['quiet'] == True
    assert dl.params['noprogress'] == True
    assert dl.params['ratelimit'] == 10
    assert dl.params['retries'] == 5
    assert dl.params['nopart'] == True
    assert dl.params['test'] == True

# Generated at 2022-06-14 15:39:22.312363
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD(None, {})

# Generated at 2022-06-14 15:39:27.248730
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    from .extractor.generic import YoutubeIE

    # Constructor should not fail
    assert HttpQuietDownloader(YoutubeIE(), {'continuedl': True, 'quiet': True, 'noprogress': True})

    # Constructor should not fail when creating object for all registered
    # extractors
    for ie in gen_extractors():
        assert HttpQuietDownloader(ie(), {'continuedl': True, 'quiet': True, 'noprogress': True})

# Generated at 2022-06-14 15:39:36.256277
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class FakeYDL:
        def __init__(self, params):
            self.params = params
        def to_screen(self, *args, **kargs):
            pass
    FakeFD = HttpQuietDownloader.factory(FakeYDL)
    # simple test
    assert FakeFD(FakeYDL({})).params == {}
    # copy params
    assert FakeFD(FakeYDL({'foo': 'bar'})).params['foo'] == 'bar'
    # unicode
    assert FakeFD(FakeYDL({'foo': b'\xc3\xa1'.decode('utf-8')})).params['foo'] == 'á'

# Generated at 2022-06-14 15:39:45.354120
# Unit test for constructor of class FragmentFD

# Generated at 2022-06-14 15:39:49.362061
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpDownloader
    quiet_dl = HttpQuietDownloader(None)
    assert quiet_dl.__class__ == HttpDownloader

# Compatibilty test for _prepare_url() and _download_fragment()

# Generated at 2022-06-14 15:39:51.475006
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fragment_fd = FragmentFD(None, {}, None, None)
    assert fragment_fd is not None

# Generated at 2022-06-14 15:40:01.355097
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..utils import get_cachedir
    from ..extractor import youtube_dl

    my_ydl = youtube_dl.YoutubeDL({
        'outtmpl': get_cachedir() + '/test-%(id)s.%(ext)s',
        'noprogress': True,
        'quiet': True,
    })

    dl = HttpQuietDownloader(
        my_ydl,
        {
            'continuedl': False,
            'quiet': True,
            'noprogress': True,
            'outtmpl': get_cachedir() + '/test-%(id)s.%(ext)s',
        }
    )

# Generated at 2022-06-14 15:40:49.010857
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from ..compat import is_py2

    if is_py2:
        from StringIO import StringIO
        from urlparse import urlparse
    else:
        from io import StringIO
        from urllib.parse import urlparse

    class FakeYDL:
        def __init__(self):
            self.params = {
                'continuedl': True,
                'quiet': True,
                'noprogress': True,
                'ratelimit': None,
                'retries': 0,
                'nopart': False,
                'test': False,
            }
            self.to_screen = sys.stdout.write

    class FakeFD:
        def __init__(self):
            self.ydl = FakeYDL()


# Generated at 2022-06-14 15:40:52.853411
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import youtube_dl.YoutubeDL
    downloader = HttpQuietDownloader(youtube_dl.YoutubeDL({}), {'quiet': True})
    assert not downloader.params['quiet']

# Generated at 2022-06-14 15:41:01.220930
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..compat import compat_urlopen
    import youtube_dl.YoutubeDL
    import youtube_dl.extractor
    d = youtube_dl.YoutubeDL({'quiet': True})
    ydl = youtube_dl.extractor.common.YoutubeDL(d)
    ydl.add_info_extractor(
        youtube_dl.extractor.common.FakeIE(ydl, 'fake'))
    urlopen_mock = lambda x, y, z=None: compat_urlopen(x, y)
    hqd = HttpQuietDownloader(ydl, {'continuedl': True}, urlopen_mock)
    hqd.download('fake', {'ie_key': 'fake'})

# Generated at 2022-06-14 15:41:13.184747
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractor

    ydl = type('MockYDL', (object,), {})()
    ydl.params = {}

    class FakeOutFile(object):
        def write(self, s):
            pass

    ydl.outtmpl = '%(id)s.f4m'
    ydl.to_screen = FakeOutFile()
    ydl.to_stderr = FakeOutFile()
    ydl.post_processors = {
        'postprocessors': [],
        'playlist_result': None,
    }
    ydl.progress_hooks = []

    class MockIE(object):
        def __init__(self, ie_desc):
            self.ie_desc = ie_desc

        def _extract_info(self, *args):
            return

# Generated at 2022-06-14 15:41:16.325327
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = object()
    params = {'continuedl': True, 'quiet': True, 'noprogress': True}
    dl = HttpQuietDownloader(ydl, params)
    assert dl.params == params
    assert dl.ydl is ydl

# Generated at 2022-06-14 15:41:21.446437
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from ..compat import compat_basestring

    HttpQuietDownloader(
        '__main__',
        {
            'continuedl': True,
            'noprogress': True,
            'quiet': True,
        })
    assert sys.stdin.isatty()
    assert sys.stdout.isatty()
    assert sys.stderr.isatty()



# Generated at 2022-06-14 15:41:25.696409
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Check that HttpQuietDownloader arguments are propagated to FileDownloader.__init__
    # via HttpFD.__init__
    ydl = object()
    params = {'test': True, 'ratelimit': 1}

    dl = HttpQuietDownloader(ydl, params)

    assert dl.params['test'] == params['test']
    assert dl.params['ratelimit'] == params['ratelimit']

# Generated at 2022-06-14 15:41:33.396267
# Unit test for constructor of class FragmentFD
def test_FragmentFD():

    class DummyYDL(object):
        def __init__(self, params):
            self.params = params
    ydl = DummyYDL({'format': 'best', 'outtmpl': 'test.%(ext)s', 'ignoreerrors': False})

    # No resuming
    fd = FragmentFD(ydl, {'url': '', 'id': 'test-id', 'http_headers': {'User-Agent': 'test-agent'}})
    assert(fd.params['noprogress'] == False)  # noprogress is off for the main downloader
    assert(fd.params['nopart'] == True)  # nopart is on for the main downloader
    assert(fd.params['nopart'] == False)  # For fragment downloaders nopart is off

    # Res

# Generated at 2022-06-14 15:41:39.226210
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor import get_info_extractor
    ydl = get_info_extractor('YoutubeIE')
    hqd = HttpQuietDownloader(
        ydl, {'continuedl': True, 'quiet': True, 'noprogress': True})
    assert hqd.params['continuedl']
    assert hqd.params['quiet']
    assert hqd.params['noprogress']



# Generated at 2022-06-14 15:41:46.212524
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def my_hook(d):
        pass
    params = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'ratelimit': 1,
        'retries': 2,
    }
    ydl = object()
    hqd = HttpQuietDownloader(ydl, params)
    assert hqd.params == params
    assert hqd.add_progress_hook(my_hook) is None


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:43:06.527896
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD('dummy', {'ydl': object()})
    assert fd.ydl is not None

# Generated at 2022-06-14 15:43:13.030196
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor
    class MyFragmentFD(FragmentFD):
        FD_NAME = 'fragment'
    ie = get_info_extractor('youtube', 'YoutubeBaseInfoExtractor')
    myfd = MyFragmentFD(ie._downloader, {'nopart': True, 'quiet': True})
    assert myfd.params['quiet'] is True
    assert myfd.params['nopart'] is True

# Generated at 2022-06-14 15:43:13.752351
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    pass

# Generated at 2022-06-14 15:43:23.860782
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    """Test the HttpQuietDownloader"""
    from .extractor.common import InfoExtractor
    ie = InfoExtractor()
    dl = HttpQuietDownloader(ie, {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'ratelimit': 5000000,
        'retries': 5,
        'nopart': False,
        'test': False,
    })
    from .http import HEADRequest, FIXED_TEMPDIR
    head_request = HEADRequest(
        'http://releases.ubuntu.com/14.04/ubuntu-14.04.2-desktop-amd64.iso'
    )
    urlh = ie._request_webpage(head_request, 'Unused video id')
    # Tell ffmpeg to keep in its

# Generated at 2022-06-14 15:43:25.398604
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    assert fd

# Generated at 2022-06-14 15:43:36.433844
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class TestYdl(object):
        def __init__(self):
            self.params = {}

    ydl = TestYdl()
    frag_dl = HttpQuietDownloader(ydl, {})
    assert isinstance(frag_dl, HttpFD)
    assert frag_dl.ydl is ydl
    assert frag_dl.params == {}
    assert frag_dl.to_screen_enabled() is False

    frag_dl = HttpQuietDownloader(ydl, {'continuedl': True, 'quiet': True})
    assert isinstance(frag_dl, HttpFD)
    assert frag_dl.ydl is ydl
    assert frag_dl.params == {'continuedl': True, 'quiet': True}
    assert frag_dl.to_screen_enabled() is False

# Generated at 2022-06-14 15:43:43.493792
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = object()
    params = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'ratelimit': None,
        'retries': 0,
        'nopart': None,
        'test': None,
    }
    assert HttpQuietDownloader(ydl, params).ydl is ydl
    assert HttpQuietDownloader(ydl, {}).ydl is ydl



# Generated at 2022-06-14 15:43:44.936683
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert isinstance(FragmentFD(None), object)


# Generated at 2022-06-14 15:43:47.316101
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from youtube_dl.downloader.common import FileDownloader
    fd = FragmentFD({})
    assert isinstance(fd, FileDownloader)

# Generated at 2022-06-14 15:43:51.244716
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import params
    from .http import HttpFD
    assert issubclass(FragmentFD, FileDownloader)
    assert issubclass(FragmentFD, HttpFD)
    fragment_fd = FragmentFD(params)
    assert isinstance(fragment_fd, FragmentFD)
    assert isinstance(fragment_fd, HttpFD)

# Generated at 2022-06-14 15:47:09.187717
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor
    from ..utils import match_filter_func

    ie = get_info_extractor('youtube')
    ie.extract('http://www.youtube.com/watch?v=BaW_jenozKc')
    ie.report_warning = match_filter_func(['(?i)Unsupported URL'])
    ie._real_initialize()
    ie._extract_info(ie._download_webpage(
        'http://www.youtube.com/get_video_info?video_id=BaW_jenozKc',
        video_id='XBaW_jenozKc'))

# Generated at 2022-06-14 15:47:18.889045
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=missing-docstring
    def f1(d):
        d.to_screen('f1')

    def f2(d):
        d.to_screen('f2')

    d = FragmentFD(None, {'outtmpl': '%(id)s.%(ext)s'})
    d.add_progress_hook(f1)
    d.add_progress_hook(f2)
    assert d.params['outtmpl'] == '%(id)s.%(ext)s'
    d.report_destination('foo.bar')
    d._hook_progress({'filename': 'foo.bar', 'status': 'finished'})