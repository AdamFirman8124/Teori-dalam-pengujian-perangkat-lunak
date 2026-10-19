

# Generated at 2022-06-14 15:37:54.965972
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractor_classes
    gen_extractor_classes()
    from .extractor import get_info_extractor as gen_ie
    from .extractor import YoutubeIE
    ie = gen_ie(YoutubeIE.ie_key())
    ie.url = lambda *_: 'http://example.com'
    fd = FragmentFD(ie, {})
    assert fd.params == {'continuedl': True, 'quiet': True, 'noprogress': True}
    assert fd.ie == ie
    assert fd.num == 0


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:38:06.827907
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from collections import namedtuple
    from types import MethodType

    class MockYDL(object):
        params = dict()
        to_screen = False
        _screen_file = None
        _err_file = None

        def __init__(self):
            self._screen_file = open('/dev/null', 'w')
            self._err_file = open('/dev/null', 'w')

        def to_stdout(self, message, skip_eol=False):
            if self.to_screen:
                self._screen_file.write(message + ('\n' if not skip_eol else ''))
                self._screen_file.flush()

        def to_stderr(self, message):
            self._err_file.write(message + '\n')
            self._err_file.flush()

# Generated at 2022-06-14 15:38:09.602368
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(
        {'params': {
            'fragment_retries': 1,
        }}, None)
    assert fd.params['fragment_retries'] == 1

# Generated at 2022-06-14 15:38:14.092940
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    test_http_dl = HttpQuietDownloader(None, {})
    assert test_http_dl.params['noprogress']


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:38:18.098605
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    dl = FragmentFD(None)
    assert isinstance(dl, FileDownloader)
    assert hasattr(dl, 'report_destination')
    assert hasattr(dl, 'try_rename')

# Generated at 2022-06-14 15:38:21.618443
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:38:27.442783
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # pylint: disable=C0111
    from .extractor.common import InfoExtractor
    ie = InfoExtractor()
    ie.params = {}
    dl = HttpQuietDownloader(ie, {})
    assert dl

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:38:31.910792
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor_classes

    ydl_opts = {
        'usenetrc': False,
        'username': 'uname',
        'password': 'pword',
        'twofactor': 'tf',
        'videopassword': 'videopassword',
    }
    ie = gen_extractor_classes()['youtube']('testid', ydl_opts)
    h = HttpQuietDownloader(ie, ydl_opts)
    assert h.params['usenetrc'] is False
    assert h.params['username'] == 'uname'
    assert h.params['password'] == 'pword'
    assert h.params['videopassword'] == 'videopassword'
    assert h.params['twofactor'] == 'tf'

# Generated at 2022-06-14 15:38:35.468255
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    ydl = InfoExtractor()
    dl = HttpQuietDownloader(ydl, {})
    assert isinstance(dl, HttpQuietDownloader)

# Generated at 2022-06-14 15:38:39.123181
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    xdl = HttpQuietDownloader(
        {}, {'quiet': True, 'noprogress': True, 'retries': 0})
    assert xdl.params['quiet']
    assert xdl.params['noprogress']
    assert xdl.params['retries'] == 0, xdl.params['retries']

# Generated at 2022-06-14 15:39:02.931236
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import types

    class HttpQuietDownloaderTest(HttpQuietDownloader):
        def __init__(self):
            HttpQuietDownloader.__init__(self, None, 'http://example.com/')
            self.__progress_hooks = {
                'test': self.test_hook,
            }

        def test_hook(self, status):
            assert isinstance(status, dict)
            assert status['url'] == 'http://example.com/'

    is_py2 = sys.version_info[0] == 2
    is_py3 = sys.version_info[0] == 3 or sys.version_info[1] >= 5
    if is_py2:
        HttpQuietDownloaderTest.__check_py2__()

# Generated at 2022-06-14 15:39:10.611468
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import get_info_extractor
    from .downloader.external import ExternalFD
    from .compat import compat_urllib_request

    youtube_ie = get_info_extractor('youtube')
    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    req = compat_urllib_request.Request(url, headers={'User-Agent': youtube_ie.IE_NAME})
    info_dict = youtube_ie._real_extract(req)
    fd = ExternalFD(youtube_ie.ydl, {'outtmpl': '%(title)s-%(id)s.%(ext)s'}, info_dict)
    assert isinstance(fd.ydl.fd, HttpQuietDownloader)

# Generated at 2022-06-14 15:39:19.430635
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor
    from .extractor.common import InfoExtractor
    from .extractor.youtube import YoutubeIE

    for ie in InfoExtractor._ies:
        if ie.IE_NAME == 'Youtube' and ie is not YoutubeIE:
            raise TypeError('YoutubeIE is not unique')

    YoutubeIE._WORKING = False
    ie = gen_extractor(YoutubeIE.ie_key())()
    if ie is YoutubeIE:
        raise TypeError('YoutubeIE is used while it is known to fail')

# Generated at 2022-06-14 15:39:25.565358
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def dummy_report_warning(msg):
        warnings.append(msg)
    ydl = MockYoutubeDl({})
    ydl.report_warning = dummy_report_warning
    HttpQuietDownloader(
        ydl,
        {
            'continuedl': False,
            'quiet': False,
            'noprogress': True,
            'ratelimit': None,
            'retries': 10,
            'nopart': False,
            'test': False,
        }
    )
    assert not warnings  # 'quiet' is True by default

# Generated at 2022-06-14 15:39:28.024361
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader({}, {})
    assert isinstance(dl, HttpFD)


# Generated at 2022-06-14 15:39:31.036706
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import youtube_dl.extractor.fragment
    youtube_dl.extractor.fragment.FragmentFD('foo')

# Generated at 2022-06-14 15:39:35.210676
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # pylint: disable=W0212
    from .http import HttpDownloader
    fd = HttpQuietDownloader(None, {'continuedl': True, 'quiet': True})
    assert isinstance(fd, HttpDownloader)
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# Generated at 2022-06-14 15:39:46.142852
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import io
    import tempfile
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock
    from .extractor import YoutubeIE

    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'

    ydl = Mock()
    ydl.params = {}
    ydl.add_info_extractor.return_value = {'_type': 'url', 'ie_key': YoutubeIE.ie_key()}

    FD = FragmentFD(ydl)
    filename = tempfile.mkstemp()[1]
    info = {'url': url, 'title': 'test', 'ext': 'flv'}
    FD.download(filename, info)


# Generated at 2022-06-14 15:39:49.700609
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FakeYDL(object):
        def __init__(self):
            self.params = {}

    fragmentfd = FragmentFD(FakeYDL(), {})
    assert fragmentfd.fd is None

test_FragmentFD()

# Generated at 2022-06-14 15:39:52.431701
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpDownloader

    assert issubclass(HttpQuietDownloader, HttpFD)
    assert issubclass(HttpQuietDownloader, HttpDownloader)

test_HttpQuietDownloader()

# Generated at 2022-06-14 15:40:31.014977
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    FragmentFD(None)

# Generated at 2022-06-14 15:40:32.567192
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    assert issubclass(HttpQuietDownloader, HttpFD)

# Generated at 2022-06-14 15:40:39.263821
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    return HttpQuietDownloader(None, {
        'continuedl': True,
        'quiet': False,
        'noprogress': True,
        'retries': 0,
    })


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:40:49.337892
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        @classmethod
        def suitable(cls, *args):
            return True
    fd = TestFD(None, None)
    assert fd.format_retries(0) == 'infinite'
    assert fd.format_retries(1) == '1'
    assert fd.format_retries(3) == '3'
    fd.to_screen('1', '2', key='value')
    fd.to_stderr('1', '2', key='value')
    fd.report_warning('1', '2', key='value')
    fd.report_error('1', '2', key='value')
    fd.report_destination('1', '2', key='value')
    assert fd.ydl_filename('1')

# Generated at 2022-06-14 15:40:59.784344
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor import DummyIE
    from ..post import PostProcessor
    d = HttpQuietDownloader(DummyIE(), {'noprogress': True})
    assert d.params['noprogress']

    d = HttpQuietDownloader(DummyIE(), {'noprogress': False})
    assert not d.params.get('noprogress')

    d = HttpQuietDownloader(DummyIE(), {})
    assert not d.params.get('noprogress')

    d = HttpQuietDownloader(DummyIE(), {'progress_with_newline': False})
    assert d.params['noprogress']

    d = HttpQuietDownloader(DummyIE(), {'progress_with_newline': True})

# Generated at 2022-06-14 15:41:12.174682
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # TODO: use mock to test method _append_fragment and _download_fragment
    from . import YoutubeDL
    from .extractor.generic import GenericIE
    from .postprocessor import FFmpegExtractAudioPP
    from .postprocessor import FFmpegMetadataPP

    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test', 'data')
    test_file = lambda f: os.path.join(data_dir, f)
    try:
        os.unlink(test_file('output'))
    except (IOError, OSError):
        pass

    dl = YoutubeDL({'noplaylist': True, 'quiet': True, 'no_warnings': True})
    dl.add_default_info_extract

# Generated at 2022-06-14 15:41:20.563062
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # pylint: disable=unused-argument, missing-docstring
    # pylint: disable=attribute-defined-outside-init,no-self-use
    # pylint: disable=no-member
    class MockYDL(object):
        @staticmethod
        def to_screen(*args, **kargs):
            pass

    ydl = MockYDL()
    # pylint: disable=protected-access
    dl = HttpQuietDownloader(ydl, {'continuedl': True, 'quiet': True})
    assert dl.ydl is ydl
    assert dl._opts['quiet']
    assert dl._opts['continuedl']

# Generated at 2022-06-14 15:41:22.458828
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    fd = HttpQuietDownloader({}, {'quiet': True})
    assert fd.params['quiet']

# Generated at 2022-06-14 15:41:24.945701
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert hasattr(HttpQuietDownloader, 'report_retry_fragment')
    assert not hasattr(HttpQuietDownloader, 'to_screen')

# Generated at 2022-06-14 15:41:25.528681
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    pass

# Generated at 2022-06-14 15:42:11.268816
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import copy
    import youtube_dl.FileDownloader

    def test(args):
        opts = copy.copy(youtube_dl.FileDownloader.default_params)
        opts.update(args)
        return HttpQuietDownloader(None, opts)

    assert test({})
    assert test({'quiet': False})
    assert test({'noprogress': False})
    assert test({'quiet': False, 'noprogress': False})

# Generated at 2022-06-14 15:42:16.910780
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class MyLogger(object):
        def debug(self, *args):
            pass

        def warning(self, *args):
            pass

        def error(self, *args):
            pass

    ydl = {'params': {}, 'logger': MyLogger()}
    dl = HttpQuietDownloader(ydl, {'noprogress': True})
    assert dl.params['quiet'] is True

# Generated at 2022-06-14 15:42:26.222616
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    try:
        import __main__
        __main__.params = {}
        __main__.ydl = None
    except Exception:
        class MockYTDLSession():
            def __init__(self):
                self.params = {}
        ydl = MockYTDLSession()
    ret = HttpQuietDownloader(ydl, {'continuedl': True, 'quiet': True, 'noprogress': True})
    assert isinstance(ret, HttpQuietDownloader)
    assert ret.params['continuedl'] == True
    assert ret.params['quiet'] == True
    assert ret.params['noprogress'] == True

# Generated at 2022-06-14 15:42:33.847177
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import unittest

    class TestFragmentFD(unittest.TestCase):
        def setUp(self):
            self.fd = FragmentFD({})

        def test_constructor(self):
            self.assertEqual(self.fd.params, {})
            self.assertEqual(self.fd.url, None)
            self.assertEqual(self.fd.outtmpl, None)
            self.assertEqual(self.fd.ydl, None)

    return unittest.main()

# Generated at 2022-06-14 15:42:39.048820
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Test that it can be constructed
    options = {
        'continuedl': 1,
    }
    HttpQuietDownloader(None, options)

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:42:43.503013
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # self, ydl, params={}
    ydl = object()
    params = {'param': 'value'}
    result = HttpQuietDownloader(ydl, params)
    assert result.ydl is ydl
    assert result.params == params


# Generated at 2022-06-14 15:42:54.205002
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpQuietDownloader
    from ..extractor import YoutubeIE

    class MyDummyYoutubeIE(YoutubeIE):
        def _real_initialize(self):
            pass

    class MyDummyFD(FragmentFD):
        FD_NAME = 'testfd'

    # Test number 1
    fd = MyDummyFD({})
    fd.params['noprogress'] = False
    fd._prepare_frag_download({'filename': 'dummy'})
    assert isinstance(fd.ctx['dl'], HttpQuietDownloader) is False

    # Test number 2
    fd = MyDummyFD({})
    fd.params['noprogress'] = True
    fd._prepare_frag_download({'filename': 'dummy'})

# Generated at 2022-06-14 15:42:58.972564
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ydl = object()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
        'keep_fragments': True,
    }
    fd = FragmentFD(ydl, params)
    for p in params:
        assert fd.params[p] == params[p]

# Generated at 2022-06-14 15:43:01.752474
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    assert isinstance(fd, FragmentFD)
    assert isinstance(fd, FileDownloader)

# Generated at 2022-06-14 15:43:13.649919
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HTTPDownloader
    from .http import HttpFD
    from .http import HttpQuietDownloader
    from ..compat import compat_urllib_parse_unquote


# Generated at 2022-06-14 15:44:32.531506
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:44:43.984386
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    info_dict = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
        'keep_fragments': False,
    }
    ydl = {}

    def to_screen(msg):
        print(msg)

    def report_warning(msg):
        print('WARNING: ' + msg)

    def report_destination(filename):
        print('Writing video to: %s' % filename)

    def try_rename(tmpname, filename):
        print('Renaming %s to %s' % (tmpname, filename))

    def calc_eta(start, now, total, downloaded):
        return 42

    def format_retries(retries):
        return '%d more' % retries


# Generated at 2022-06-14 15:44:50.197505
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    try:
        from urllib.request import build_opener
    except ImportError:
        from urllib2 import build_opener
    opener = build_opener()
    opener.addheaders = [('X-Test', 'test')]
    ydl = FakeYDL({'http_header_updates': {'X-Foo': 'foo'}})
    d = HttpQuietDownloader(ydl, {}, opener=opener)
    assert d.opener.addheaders == [('X-Test', 'test'), ('X-Foo', 'foo')]



# Generated at 2022-06-14 15:44:59.240089
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import copy
    from collections import defaultdict

    fd = FragmentFD('blah')
    assert fd.FD_NAME == 'blah'
    assert fd.fragment_retries == 10
    assert fd.skip_unavailable_fragments == True
    assert fd.keep_fragments == False
    assert fd.fragment_retry_wait == 5

    fd = FragmentFD('blah', fragment_retries=3, skip_unavailable_fragments=False,
        keep_fragments=True, fragment_retry_wait=1)
    assert fd.fragment_retries == 3
    assert fd.skip_unavailable_fragments == False
    assert fd.keep_fragments == True
    assert fd.fragment_retry

# Generated at 2022-06-14 15:44:59.763393
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    pass

# Generated at 2022-06-14 15:45:06.660798
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def _test_fd_init(fd_factory):
        ydl = {'params': {}, 'to_screen': None}
        fd = fd_factory(ydl, {})
        assert fd.params == {
            'ratelimit': None,
            'retries': 0,
            'nopart': False,
            'test': False,
        }
        assert fd.ydl.params == {}
        assert fd.ydl.to_screen is None
        ydl = {'params': {'retries': 5, 'test': True}, 'to_screen': True}
        fd = fd_factory(ydl, {'retries': '10', 'keep_fragments': True})

# Generated at 2022-06-14 15:45:13.965367
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from . import YoutubeDL
    params = {'quiet': True, 'no_warnings': True, 'simulate': True}
    fd = HttpQuietDownloader(YoutubeDL(params), params)
    assert fd.ydl.params['quiet'] == True
    assert fd.ydl.params['no_warnings'] == True
    assert fd.ydl.params['simulate'] == True
    assert isinstance(fd, HttpFD)


# Generated at 2022-06-14 15:45:18.690987
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..YoutubeDL import YoutubeDL
    from .http import HttpFD

    class HttpQuietDownloaderTest(HttpQuietDownloader):
        def to_screen(self, *args, **kargs):
            self.out.extend(args)

    class TestBase(object):
        out = []

        def __init__(self, *a, **kw):
            self.ydl = YoutubeDL(params=kw.get('params', {}))

    class TestFD(TestBase, FragmentFD):
        FD_NAME = 'test'

    ydl = YoutubeDL()
    params = {'verbose': True, 'ratelimit': '1M'}
    dl = HttpQuietDownloader(ydl, params)
    assert dl.params['continuedl']

# Generated at 2022-06-14 15:45:29.276883
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        FD_NAME = 'test'

    fd = TestFD({})
    assert fd.params == {
        'keepfragments': False,
        'nopart': False,
        'quiet': True,
        'retries': 0,
        'test': False,
    }

    fd = TestFD({'keep_fragments': True})
    assert fd.params == {
        'keepfragments': True,
        'nopart': False,
        'quiet': True,
        'retries': 0,
        'test': False,
    }

    fd = TestFD({'nopart': True})

# Generated at 2022-06-14 15:45:30.828301
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(None, None)
    assert fd.ydl is None