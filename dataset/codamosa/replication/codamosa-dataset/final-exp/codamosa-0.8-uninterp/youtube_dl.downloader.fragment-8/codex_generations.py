

# Generated at 2022-06-14 15:37:46.629889
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .http import HttpQuietDownloader
    assert issubclass(HttpQuietDownloader, HttpFD)

# Generated at 2022-06-14 15:37:59.769830
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys

    class FakeInfoDict(object):
        http_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Range': 'bytes=0-',
            'Referer': 'https://www.youtube.com/watch?v=9bZkp7q19f0',
            'Connection': 'keep-alive',
        }

    class FakeYDL(FragmentFD):
        params = {}

# Generated at 2022-06-14 15:38:05.256594
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import platform
    from .extractor.common import InfoExtractor

    class MockFD(FragmentFD):
        def real_download(self, filename, info_dict):
            return True

    class MockIE(InfoExtractor):
        _VALID_URL = r'^unimportant$'
        _TEST = {
            'url': 'unimportant',
            'info_dict': {
                'id': '1337',
                'ext': 'mp4',
            },
        }


# Generated at 2022-06-14 15:38:11.536572
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class MockYoutubeDL:
        params = {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'nopart': False,
            'test': False,
            'retries': 0,
            'ratelimit': 'N/A',
        }
        params = HttpFD.add_default_info_extractors(params)

    http = HttpQuietDownloader(MockYoutubeDL(), {})
    assert http.ydl == MockYoutubeDL()
    assert http.params == MockYoutubeDL().params

# Generated at 2022-06-14 15:38:25.028167
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({'quiet': 0})
    fd = HttpQuietDownloader(
        ydl,
        {
            'continuedl': True,
            'quiet': False,
            'noprogress': False,
            'ratelimit': 100,
            'retries': 0,
            'nopart': False,
            'test': False,
        })
    assert isinstance(fd, HttpQuietDownloader)
    assert fd.ydl is ydl

# Generated at 2022-06-14 15:38:34.303838
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .http import HttpFD
    from .f4m import F4mFD
    from .hls import HlsFD
    from .hlsnative import HlsFD as HlsNativeFD
    from .dash import DashFD
    assert issubclass(FragmentFD, FileDownloader)
    assert issubclass(HttpFD, FragmentFD)
    assert issubclass(F4mFD, FragmentFD)
    assert issubclass(HlsFD, FragmentFD)
    assert issubclass(HlsNativeFD, FragmentFD)
    assert issubclass(DashFD, FragmentFD)

# Generated at 2022-06-14 15:38:40.194454
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import youtube_dl.YoutubeDL
    import youtube_dl.FileDownloader
    params = {
        'noprogress': True,
        'quiet': True,
    }
    dl = youtube_dl.FileDownloader(youtube_dl.YoutubeDL(params), {})
    assert isinstance(HttpQuietDownloader(dl, params), HttpQuietDownloader)

# Generated at 2022-06-14 15:38:44.867310
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..EXT_YOUTUBEDL import YoutubeDL

    class MockInfoDict(dict):
        def __init__(self, d):
            self.update(d)

        def __setitem__(self, key, value):
            self.__dict__[key] = value

        def __getitem__(self, key):
            try:
                return self.__dict__[key]
            except KeyError:
                return self.__dict__.__getitem__(key)

    class FragmentFD(FragmentFD):
        def __init__(self, *args, **kargs):
            pass

        def to_screen(self, message, skip_eol=False):
            pass

    ydl = YoutubeDL({})
    fragfd = FragmentFD(ydl)


# Generated at 2022-06-14 15:38:48.676427
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    """
    Invoke constructor of class FragmentFD

    YoutubeDL object is created and passed to constructor.
    """
    ydl = object()
    fd = FragmentFD(ydl, {})
    assert fd.ydl is ydl

# Generated at 2022-06-14 15:38:55.894084
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys

    ydl = HttpQuietDownloader({'quiet': True, 'noprogress': True}, {'format': 'best'})

    class FakeInfo(object):
        pass

    info = FakeInfo()
    info.filename = sys.executable

    def test_hook(*args):
        raise Exception('test_hook should not be called')

    ydl.add_info_hook(test_hook)
    ydl.add_progress_hook(test_hook)
    ydl.download(info)

# Generated at 2022-06-14 15:39:16.971517
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = None
    params = {}
    dl = HttpQuietDownloader(ydl, params)
    assert dl


# Generated at 2022-06-14 15:39:19.756441
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import youtube_dl.YoutubeDL
    downloader = HttpQuietDownloader({})
    assert isinstance(downloader, youtube_dl.YoutubeDL)

# Generated at 2022-06-14 15:39:22.165877
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import youtube_dl
    ydl = youtube_dl.YoutubeDL({'nooverwrites': True, 'quiet': True, 'simulate': True})
    hqd = HttpQuietDownloader(ydl, {})
    assert hqd.params == {'continuedl': True, 'noprogress': True, 'quiet': True, 'simulate': True}

# Generated at 2022-06-14 15:39:27.418267
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .http import HttpFD
    from .dashsegments import DASHFragmentsFD

    # Basic stuff
    assert FragmentFD.FD_NAME == 'generic'
    assert issubclass(DASHFragmentsFD, FragmentFD)

    # FragmentFD constructor
    fd = FragmentFD('youtube-dl')
    assert isinstance(fd.dl, HttpFD)
    assert not fd.params.get('noprogress')
    assert not fd.params.get('logtostderr')
    assert not fd.params.get('quiet')
    assert fd.params.get('forcetitle')
    assert not fd.params.get('continuedl')
    assert fd.params.get('nopart')
    assert not fd.params.get('updatetime')

# Generated at 2022-06-14 15:39:38.043959
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    from ..extractor.dash import DashIE
    from ..extractor.http import HttpIE

    class TestIE(InfoExtractor):
        IE_DESC = 'Test IE'
        _VALID_URL = r'https?://(?:www\.)?test\.com/video\.html'

        def _real_extract(self, url):
            return {
                '_type': 'url',
                'url': 'http://example.org/video.mp4',
                'ie_key': 'Http',
            }

    class TestFD(FragmentFD):
        FD_NAME = 'testfd'

    test_fd = TestFD()

    assert HttpIE.suitable(test_fd)
    assert not DashIE.suitable(test_fd)
    assert Test

# Generated at 2022-06-14 15:39:47.942055
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class YDL:
        params = {'verbose': False, 'format': 'best'}

    class DummyIE(object):
        def __init__(self, downloader):
            self.downloader = downloader

    ydl = YDL()
    ie = DummyIE(ydl)
    ie.params = {}
    http_dl = HttpQuietDownloader(ydl, ie)

    ydl = YDL()
    ydl.params = {'verbose': True}
    ie = DummyIE(ydl)
    ie.params = {'verbose': False}
    http_dl = HttpQuietDownloader(ydl, ie)

# Generated at 2022-06-14 15:39:56.252723
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import tempfile
    from ..extractor import gen_extractors, list_extractors
    from ..utils import encodeOption

    extractors = [e for e in gen_extractors() if e.IE_NAME in ('youtube', 'generic')]

    (dummyfd, eqfname) = tempfile.mkstemp(prefix='ytdl-test', suffix='.eqf')
    os.close(dummyfd)
    os.remove(eqfname)

    for e in extractors:
        eqfname_e = encodeOption(eqfname, e.IE_NAME)
        if os.sep in eqfname_e:
            continue


# Generated at 2022-06-14 15:39:59.444430
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)
    fd = FragmentFD('youtube-dl', {}, {'skip_download': False})
    assert fd.params == {'skip_download': False}

# Generated at 2022-06-14 15:40:03.516481
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    options = {
        'quiet': True,
        'noprogress': True,
        'continuedl': True,
        'retries': 0,
    }
    ud = HttpQuietDownloader(None, options)

# Generated at 2022-06-14 15:40:16.558506
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FD(FragmentFD):
        FD_NAME = 'testfd'

        @staticmethod
        def format_retries(retries):
            return '%d' % retries

        def report_destination(self, filename):
            pass

        def report_warning(self, warning):
            pass

        def to_screen(self, message, skip_eol=False):
            pass

        def calc_eta(self, start, now, total, downloaded):
            return 0

        @staticmethod
        def ytdl_filename(filename):
            return filename + '.ytdl'

        @staticmethod
        def temp_name(filename):
            return filename + '.part'

        @staticmethod
        def try_rename(fromname, toname):
            os.rename(fromname, toname)

    fd

# Generated at 2022-06-14 15:40:44.361904
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import config
    import extractor

    # We do not want to require 'fake' module in actual use
    import sys
    sys.modules['fake_modules'] = extractor

    ydl = config.YoutubeDL({
        'quiet': False,
        'logger': False,
    })

    # Fails if HttpQuietDownloader constructor raises exception
    HttpQuietDownloader(ydl, {})

# Generated at 2022-06-14 15:40:47.336972
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from . import YoutubeDL
    ydl = YoutubeDL()
    fd = HttpQuietDownloader(ydl, {'noprogress': True})
    assert isinstance(fd, HttpQuietDownloader)

# Generated at 2022-06-14 15:40:51.805591
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..downloader.common import FileDownloader
    class TestFD(FragmentFD, FileDownloader):
        FD_NAME = 'testfd'
    fd = TestFD()
    assert fd.FD_NAME == 'testfd'

# Generated at 2022-06-14 15:40:54.218556
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor

    for ie in get_info_extractor(None):
        if ie.__class__.__name__ == 'FragmentFD':
            return

    assert False, 'FragmentFD not found'

# Generated at 2022-06-14 15:40:55.308222
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD.__name__ == 'FragmentFD'

# Generated at 2022-06-14 15:40:56.321392
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:41:03.544373
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import io
    import unittest
    import tempfile
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'youtube_dl')))
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor

    # Base test class
    class _TestFD(FragmentFD):
        def __init__(self, ydl):
            self.ydl = ydl
            self.params = {
                'noprogress': True,
                'quiet': True,
            }
        def _prepare_frag_download(self, ctx):
            FragmentFD._prepare_frag_download(self, ctx)
            ctx

# Generated at 2022-06-14 15:41:06.430665
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert HttpQuietDownloader((None, None, None), {'continuedl': True}).params['continuedl'] == True

# Generated at 2022-06-14 15:41:08.704046
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .downloader import FileDownloader
    from .http import HttpFD
    assert issubclass(FragmentFD, FileDownloader)
    assert issubclass(FragmentFD, HttpFD)

# Generated at 2022-06-14 15:41:12.265257
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    import youtube_dl.YoutubeDL
    HttpQuietDownloader(HttpFD(youtube_dl.YoutubeDL({})), {'continuedl': True, 'quiet': True})

# Generated at 2022-06-14 15:41:41.692520
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    params = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'nopart': False,
        'ratelimit': None,
        'retries': 0,
        'test': False,
        'progress_hooks': []
    }
    ydl = HttpQuietDownloader({}, params)
    assert ydl.params == params
    assert ydl.ydl == {}
    params['continuedl'] = False
    ydl = HttpQuietDownloader({}, params)
    assert ydl.params == params

# Generated at 2022-06-14 15:41:42.710496
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:41:49.793250
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from . import YoutubeDL
    from .extractor.common import InfoExtractor

    class DummyYoutubeDL(YoutubeDL):
        def __init__(self, *args, **kwargs):
            super(DummyYoutubeDL, self).__init__(*args, **kwargs)
            self.params['skip_download'] = True
            self.extractor = InfoExtractor()

    ydl = DummyYoutubeDL()
    dl = HttpQuietDownloader(ydl, {})
    assert dl._ydl is ydl
    assert dl.params == ydl.params
    assert dl._ie is ydl.extractor

# Generated at 2022-06-14 15:41:52.216601
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    d = HttpQuietDownloader({}, {})
    assert d.ydl is not None
    assert d.params == {}

# Generated at 2022-06-14 15:42:01.935785
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import youtube_dl.extractor.common
    from youtube_dl import YoutubeDL
    from youtube_dl.utils import DateRange

    def my_hook(d):
        if d.get('status') == 'finished':
            sys.stderr.write('Done downloading, now converting ...\n')

    # simulating youtube-dl.org server -
    # this is a minimalistic HTTP server that responds to the HTTP requests
    # youtube-dl will send
    class MyServer(object):

        def __init__(self):
            self.headers = {
                'content-type': 'text/html; charset=utf-8',
                'connection': 'close',
                'content-length': '2',
            }
            self.reply_str = 'OK'


# Generated at 2022-06-14 15:42:07.766501
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import YouTubeIE
    h = HttpQuietDownloader(None, {'noprogress': True})
    assert not h.params['noprogress']
    e = YouTubeIE(h)
    h = HttpQuietDownloader(e, {'noprogress': True})
    assert not h.params['noprogress']

# Generated at 2022-06-14 15:42:16.750943
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    class MyLogger(object):
        def debug(self, msg):
            sys.stdout.write('LOG: %s\n' % msg)
    ydl = {
        'params': {
            'verbose': True,
            'quiet': False,
            'no_warnings': False,
            'simulate': True,
            'skip_download': True,
        },
        'logger': MyLogger(),
        '_opener': None,
        '_num_downloads': None,
    }
    dl = HttpQuietDownloader(ydl, {})
    dl.to_screen('hi')

# Generated at 2022-06-14 15:42:22.189427
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    from .http import HttpFD
    assert issubclass(FragmentFD, FileDownloader)
    assert FragmentFD.FD_NAME == 'fragment'

    assert issubclass(HttpQuietDownloader, HttpFD)
    assert HttpQuietDownloader.FD_NAME == 'http_quiet'

# Generated at 2022-06-14 15:42:24.127424
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    pass

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:42:28.930597
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    ydl = {}
    params = {'continuedl': True, 'quiet': True, 'noprogress': True}
    dl = HttpQuietDownloader(ydl, params)
    assert dl.ydl is ydl
    assert dl.params == params
    assert dl.to_screen == sys.stderr.write


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:43:34.699459
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    class TestFD(FragmentFD):
        FD_NAME = 'test'

    import tempfile
    tmpd = tempfile.mkdtemp()

# Generated at 2022-06-14 15:43:44.397778
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class YDL:
        params = {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'ratelimit': '1M',
            'retries': 321,
            'nopart': True,
            'test': False,
        }

    dl = HttpQuietDownloader(YDL(), {})
    params = dl.params
    assert params['quiet']
    assert params['continuedl']
    assert params['noprogress']
    assert params['ratelimit'] == '1M'
    assert params['retries'] == 321
    assert params['nopart']
    assert not params['test']


# Generated at 2022-06-14 15:43:50.684330
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FD(FragmentFD):
        FD_NAME = 'test_downloader'

    fd = FD(None, {})
    assert fd.params == {'fragment_retries': 10,
                         'keep_fragments': False,
                         'noprogress': False,
                         'outtmpl': '%(id)s',
                         'restrictfilenames': False,
                         'skip_unavailable_fragments': False}
# De-comment the line below to run the test.
# run(test_FragmentFD)

# Generated at 2022-06-14 15:43:54.432873
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    fd = HttpQuietDownloader(None, {'continuedl': True, 'quiet': True})
    assert isinstance(fd, HttpQuietDownloader)

# Generated at 2022-06-14 15:43:56.910013
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert HttpQuietDownloader(None, {})

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:44:06.962835
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from ..utils import format_bytes

    def _fake_ydl(*args, **kargs):
        print(args, kargs)
        return HttpQuietDownloader(None, kargs)

    fd = HttpQuietDownloader.best_downloader({}, None, None)
    fd.to_screen('foo')

    dl = _fake_ydl(False, None, {'outtmpl': 'bar'}, {}, None)
    assert dl.params['outtmpl'] == 'bar'

    dl = _fake_ydl(False, None, {'quiet': True}, HttpFD.params, None)
    assert dl.params['quiet'] is True

    dl.report_resuming_byte(123456)
    dl.report_retry

# Generated at 2022-06-14 15:44:14.529826
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    input_info_dict = {
        'continuedl': True,
        'quiet': True,
        'ratelimit': 1024*1024,
        'retries': 2,
    }
    expected_info_dict = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'ratelimit': 1024*1024,
        'retries': 2,
        'nopart': False,
        'test': False,
    }
    hd = HttpQuietDownloader(None, input_info_dict)
    assert hd.ydl is None
    assert hd.params == expected_info_dict


# Generated at 2022-06-14 15:44:24.648802
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MyFragmentFD(FragmentFD):
        def get_fragment_retries(self, fragment):
            return self.params.get('fragment_retries', 0)

    ffd = MyFragmentFD(
        {
            'fragment_retries': '0',
            'skip_unavailable_fragments': True,
            'test': True,
        },
        lambda s: None)
    assert ffd.params['fragment_retries'] == 0
    try:
        ffd = MyFragmentFD(
            {'fragment_retries': '-1'},
            lambda s: None)
        assert False
    except ValueError:
        pass

# Generated at 2022-06-14 15:44:27.026688
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=W0212
    ydl = {'params': {}}
    fd = FragmentFD(ydl)
    assert fd.params == {}
    assert fd.buffered_bytes == 0
    assert fd.total_bytes == 0
    assert fd.tmpfilename is None
    assert fd.dest_stream is None


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:44:31.655932
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    from ..compat import compat_urllib_request

    ydl = None
    ext_dict = gen_extractors()
    youtube_ie = None
    downloader = None
    for ie in ext_dict.values():
        if ie.IE_NAME == 'youtube':
            youtube_ie = ie
            break
    if youtube_ie:
        ydl = youtube_ie._ydl
        req = compat_urllib_request.Request(youtube_ie._VALID_URL, None)
        youtube_info = youtube_ie._real_extract(youtube_ie._download_webpage(req, 'test-id'))
        video_id = youtube_info.get('id', 'test-id')

# Generated at 2022-06-14 15:46:41.678828
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    hqd = HttpQuietDownloader(None, {'quiet': True})
    assert not hqd.params['quiet']

# Generated at 2022-06-14 15:46:51.212891
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor

    ie = get_info_extractor(
        'fragment',
        {
            'extractor_key': 'value',
        })
    assert ie.params == {'skip_unavailable_fragments': False, 'fragment_retries': 10,
        'keep_fragments': False, 'extractor_key': 'value'}
    ie = get_info_extractor(
        'fragment',
        {
            'extractor_key': 'value',
            'keep_fragments': True,
        })
    assert ie.params == {'skip_unavailable_fragments': False, 'fragment_retries': 10,
        'keep_fragments': True, 'extractor_key': 'value'}
    # The

# Generated at 2022-06-14 15:46:53.448720
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    try:
        from ..YoutubeDL import YoutubeDL
        HttpQuietDownloader(YoutubeDL(), {})
    except Exception as e:
        return str(e)
    return None

# Generated at 2022-06-14 15:47:00.153637
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import ydl_opts
    from ydl_opts import Opts
    from utils import YDL_OUT

    # Silence output of constructor
    old_YDW_OUT = sys.stderr
    sys.stderr = YDL_OUT

    opts = Opts({'format': 'best', 'quiet': True})
    fd = FragmentFD(ydl_opts.YDL({'extractor_opts': {'prefer_ffmpeg': True}}), opts)

    # Silence output of constructor
    sys.stderr = old_YDW_OUT

    assert fd

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:47:02.713648
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .wget import WgetFD
    for dl in (HttpQuietDownloader(HttpFD(), {}), HttpQuietDownloader(WgetFD(), {})):
        assert dl

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:47:14.350014
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import os
    import tempfile
    from .http import HttpFD
    from .common import FileDownloader
    import youtube_dl.YoutubeDL

    # Run test in separate process
    if not hasattr(os, 'fork'):
        return

    ydl = youtube_dl.YoutubeDL({'quiet': True, 'noprogress': True})

    pid = os.fork()
    if pid == 0:
        # child

        # Create temporary file
        tmpfilename = tempfile.mkstemp()[1]

        # Capture stdout
        sys.stdout = open(tmpfilename, 'w')

        # Test
        HttpQuietDownloader(ydl, {'ratelimit': 1, 'retries': 0})

        # Exit
        sys.stdout.close()