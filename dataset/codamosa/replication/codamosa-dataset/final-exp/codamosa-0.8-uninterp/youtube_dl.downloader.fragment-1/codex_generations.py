

# Generated at 2022-06-14 15:37:55.362868
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader
    from .http import HttpFD

    class DummyYDL(object):
        def __init__(self):
            self.params = {
                'continuedl': True,
                'quiet': True,
                'noprogress': True,
                'retries': 10,
                'ratelimit': '5',
            }

    dummy_ydl = DummyYDL()
    httpqd = HttpQuietDownloader(dummy_ydl)

    assert isinstance(httpqd, FileDownloader)
    assert isinstance(httpqd, HttpFD)
    assert httpqd.params['continuedl']
    assert httpqd.params['quiet']
    assert httpqd.params['noprogress']

# Generated at 2022-06-14 15:38:07.166154
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from .extractor import gen_extractors, list_extractors

    def print_info(ydl, info):
        print(info)

    ydl_opts = {
        'logger': sys.stdout,
        'nocheckcertificate': True,
        'simulate': True,
        'quiet': True,
        'forcetitle': True,
        'forceurl': True,
        'forcethumbnail': True,
        'forceduration': True,
        'forcefilename': True,
        'forcejson': True,
        'dump_single_json': True,
        'skip_download': True,
    }
    gen_extractors()

# Generated at 2022-06-14 15:38:20.848755
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor
    url = 'https://test.test/test'
    extractor = gen_extractor(url)
    context = {
        'ydl': object(),
        'params': {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'ignoreerrors': True,
            'ratelimit': None,
            'retries': 0,
            'nopart': False,
            'test': False,
        },
    }
    dl = HttpQuietDownloader(context['ydl'], context['params'])
    context['dl'] = dl
    ctx = context['dl'].prepare_and_start_frag_download(context)


# Generated at 2022-06-14 15:38:21.687329
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    pass

# Generated at 2022-06-14 15:38:33.957124
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import StringIO
    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen

    from six.moves import urllib_request
    from six.moves import urllib_parse

    # NOOP class
    class YDL():
        def __init__(self):
            pass

        def trouble(self, *args, **kargs):
            pass

        def to_screen(self, *args, **kargs):
            pass

    # NOOP class
    class FakeInfoDict():
        def __init__(self):
            pass

    url = 'http://httpbin.org/get'

    ydl = YDL()
    info_dict = FakeInfoDict()


# Generated at 2022-06-14 15:38:37.388635
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    assert not fd.params.get('noprogress', False)
    assert not fd.params.get('ratelimit', False)
    assert fd.params.get('retries', 0) == 0

# Generated at 2022-06-14 15:38:44.952337
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..utils import get_cachedir

    class DummyYDL(object):
        params = {'noprogress': False}
        params = {}
        def trouble(self, *args, **kargs):
            return

    dl = HttpQuietDownloader(DummyYDL(), {'noprogress': True})
    dl = HttpQuietDownloader(DummyYDL(), {})

# Generated at 2022-06-14 15:38:47.036760
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert HttpQuietDownloader(None, None).to_screen() == None


# Generated at 2022-06-14 15:38:50.465763
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD('test_FragmentFD')
    # _hook_progress must be a static method of FragmentFD or its subclasses
    assert isinstance(FragmentFD._hook_progress, staticmethod)

# Generated at 2022-06-14 15:38:52.839234
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import downloader
    downloader.quiet = True
    assert HttpQuietDownloader(None, {})
    downloader.quiet = False

# Generated at 2022-06-14 15:39:22.573164
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from .options import opts
    ydl = FileDownloader(opts)
    ydl.params['outtmpl'] = '%(id)s'
    ydl.add_info_extractor(FragmentFD(ydl, {
        'fragment_retries': 10,
        'skip_unavailable_fragments': True,
        'keep_fragments': True,
    }))
    ydl.add_info_extractor(FragmentFD(ydl, {
        'fragment_retries': 10,
        'skip_unavailable_fragments': False,
        'keep_fragments': False,
    }))

# Generated at 2022-06-14 15:39:23.176202
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    pass

# Generated at 2022-06-14 15:39:24.467057
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor import youtube_dl
    ydl = youtube_dl.YoutubeDL()
    HttpQuietDownloader(ydl, {})

# Generated at 2022-06-14 15:39:35.292992
# Unit test for constructor of class FragmentFD
def test_FragmentFD():

    class DerivedFragmentFD(FragmentFD):
        def __init__(self, ydl=None):
            super(DerivedFragmentFD, self).__init__(ydl)
            self.FD_NAME = 'derived_fragment_fd'

    fd = DerivedFragmentFD()
    assert fd.FD_NAME == 'derived_fragment_fd'
    assert fd.ydl is None

    class DummyYDL:
        def __init__(self):
            self.params = {'dump_intermediate_pages': False}

    fd = DerivedFragmentFD(ydl=DummyYDL())
    assert fd.ydl.params['dump_intermediate_pages'] is False

# Generated at 2022-06-14 15:39:41.496514
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(None, {
        'noprogress': True,
        'ratelimit': None,
        'nopart': True,
        'continuedl': True,
    })
    assert fd
    assert fd.params == {
        'noprogress': True,
        'ratelimit': None,
        'nopart': True,
        'continuedl': True,
        'retries': 0,
        'test': False,
    }

# Generated at 2022-06-14 15:39:43.773967
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD(None, None, None).__doc__ == FragmentFD.__doc__

# Generated at 2022-06-14 15:39:53.813345
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .downloader import YoutubeDL
    import sys

    class MyLogger:
        def debug(self, msg):
            sys.stdout.write('[debug] %s\n' % msg)
        def warning(self, msg):
            sys.stdout.write('[warning] %s\n' % msg)
        def error(self, msg):
            sys.stdout.write('[error] %s\n' % msg)

    def test(fd):
        assert isinstance(fd, HttpQuietDownloader)
        assert fd.params['quiet']
        assert fd.params['noprogress']
        assert fd.ydl is not None
        assert fd.params['continuedl']


# Generated at 2022-06-14 15:39:56.507180
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:40:00.044688
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=W0212
    # Access to a protected member _FD_NAME of a client class
    assert FragmentFD._FD_NAME == 'generic'


# Test for method report_retry_fragment

# Generated at 2022-06-14 15:40:06.987827
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    from .http import HttpFD
    from .dash import DASHFD
    from .hls import HLSFD
    assert issubclass(FragmentFD, FileDownloader)
    assert issubclass(DASHFD, FragmentFD)
    assert issubclass(HLSFD, FragmentFD)
    assert FragmentFD is not FileDownloader
    assert FragmentFD is not HttpFD

# Generated at 2022-06-14 15:40:42.325378
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:40:50.903527
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    for ie in gen_extractors():
        if ie.IE_NAME == 'generic':
            break

# Generated at 2022-06-14 15:40:59.160668
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    args = ['youtube-dl', '--no-warnings', '--no-playlist', '--verbose', 'http://www.youtube.com/playlist?list=ELjM2-dUQwxwU6xsRU8_dsjg']
    args += ['-o', 'test_%(playlist_index)s.%(ext)s']
    sys.argv = args
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    assert not ydl.params.get('verbose')
    ydl.report_warning('Test warning')
    ydl.report_error('Test error')
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])



# Generated at 2022-06-14 15:41:06.269778
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class YDL:
        def __init__(self):
            self.params = {
                'noprogress': False,
                'logger': None,
            }

    ydl = YDL()
    hqd = HttpQuietDownloader(ydl, {})
    assert hqd.params['noprogress'] or hqd.params['logtostderr']

# Generated at 2022-06-14 15:41:14.397363
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import tempfile
    import youtube_dl

    def _test_HookRelay():
        # This function simulates a FileDownloader object
        # It provides a fake _hook_progress() function that is called
        # from the constructor of FragmentFD
        # It collects the call arguments and provides a function
        # to access them
        progress_hook_args = []
        def _hook_progress(status):
            progress_hook_args.append(status)
        def get_progress_hook_args():
            return progress_hook_args
        return _hook_progress, get_progress_hook_args

    class MyLogger:
        def debug(self, msg):
            pass
        def warning(self, msg):
            pass
        def error(self, msg):
            pass

    ydl = youtube_dl.Y

# Generated at 2022-06-14 15:41:15.942669
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(dict(params={}), dict())
    assert fd.params == {'retries': 0, 'keepfragments': False}



# Generated at 2022-06-14 15:41:19.031034
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Pylint fails to detect that HttpQuietDownloader is properly initialized
    # in the relevant line below (bug or missing feature of pylint?).
    # pylint: disable=E1102
    assert repr(HttpQuietDownloader(None, {'quiet': True}))

# Generated at 2022-06-14 15:41:28.640568
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor_classes
    from .downloader.f4m import F4mFD
    from .downloader.hls import HlsFD
    from .utils import DateRange

    # Global parameter

# Generated at 2022-06-14 15:41:36.829175
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractors

    info = {}
    info['extractor'] = 'test'
    info['fragments'] = []

    class TestFD(FragmentFD):
        def real_prepare(self, info):
            return info

    fd = TestFD(
        TestYDL({'fragment_retries': 0}), info, TestFD.fd_name(), TestFD.suitable)
    fd.prepare()
    assert fd.resume_len == 0
    assert fd.frag_index == 0
    assert fd.total_frags == 0

    class TestFD2(FragmentFD):
        def real_prepare(self, info):
            raise Exception('123')


# Generated at 2022-06-14 15:41:39.064019
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = HttpQuietDownloader(None, {})
    ydl.to_screen('test')
    assert ydl.params['quiet']

# Generated at 2022-06-14 15:43:01.981789
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor.generic import GenericIE
    from ..compat import compat_urllib_request

    class MockIE(GenericIE):
        IE_NAME = 'mock'
        IE_DESC = 'Mock test'

        @staticmethod
        def _extract_info(url):
            if url == 'http://www.mock-url.com/mock.mpd':
                return {
                    'id': 'a_fake_id',
                    'title': 'A fake title',
                    'url': url,
                    'ext': 'mp3',
                    'http_headers': {
                        'User-Agent': 'Custom User-Agent',
                    },
                }

        @classmethod
        def _real_extract(cls, url):
            return cls._extract_info(url)

    MockIE

# Generated at 2022-06-14 15:43:08.787025
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    sys.modules['youtube_dl'] = sys.modules['__main__']
    from ..postprocessor import FFmpegPostProcessor
    from ..extractor import YoutubeIE
    fd = FragmentFD(YoutubeIE(), {}, FFmpegPostProcessor(), {})
    assert fd.params['fragment_retries'] == 10
    assert fd.params['keep_fragments'] == False

# Generated at 2022-06-14 15:43:19.794920
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import copy
    class TestFD(FragmentFD):
        FD_NAME = 'testfd'
        """File downloaders for fragmented formats should override this"""
        def fragment_retries(self, fragment_index, retries):
            return 1

    ydl = object()
    params = {
        'fragment_retries': 10,
    }
    test_fd = TestFD(ydl, params)
    assert test_fd.ydl is ydl
    assert test_fd.params == params
    for fatal in [True, False]:
        for force in [True, False]:
            for retries in [0, 1, 10]:
                assert test_fd.fragment_retries(0, retries) == retries
                test_params = copy.copy(params)

# Generated at 2022-06-14 15:43:23.938414
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class DummyYDL(object):
        def __init__(self):
            self.params = {}
    ydl = DummyYDL()
    hqd = HttpQuietDownloader(ydl)
    assert hqd.params['quiet'] is True
    assert hqd.params['noprogress'] is True

# Generated at 2022-06-14 15:43:35.568905
# Unit test for constructor of class HttpQuietDownloader

# Generated at 2022-06-14 15:43:41.272695
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .downloader import (
        gen_extractors,
        gen_extractor_classes,
        get_info_extractor)
    from .extractor import youtube_dl
    from .extractor.common import InfoExtractor

    class FakeIE(InfoExtractor):
        _WORKING = False

    gen_extractors(youtube_dl)
    gen_extractor_classes(get_info_extractor)

    info_dict = {
        'id': 'test_id',
        'extractor': 'test_extractor',
        'title': 'test_title',
        'description': 'test_description',
        'thumbnail': 'test_thumbnail',
        'duration': 'test_duration',
    }

    class YDLSimulator(object):
        def to_screen(self, message):
            print

# Generated at 2022-06-14 15:43:43.824420
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:43:48.382981
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    http_downloader = HttpQuietDownloader(None, {})
    assert hasattr(http_downloader, 'report_warning')
    assert hasattr(http_downloader, 'to_screen')
    assert hasattr(http_downloader, 'extract_info')
    assert hasattr(http_downloader, 'report_destination')

# Generated at 2022-06-14 15:44:00.825180
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import tempfile

    # We don't want to pollute unit test output with youtube-dl downloader messages
    class NullFD:
        softspace = 0

        def isatty(self):
            return False

        def write(self, text):
            pass

    null_fd = NullFD()
    old_stdout, old_stderr = sys.stdout, sys.stderr

# Generated at 2022-06-14 15:44:09.582161
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .http import HeadRequest
    from ..compat import compat_urllib_request

    class MockYDL:
        def __init__(self):
            self.params = {}
        def extract_info(self, url, download):
            info = {
                'url': url,
                'http_headers': {},
            }
            if 'http_headers' in self.params:
                info['http_headers']['Cookie'] = self.params['http_headers']
            return info
        def report_warning(self, msg):
            pass
        def to_screen(self, msg):
            pass

    dl = HttpQuietDownloader(MockYDL(), {'noprogress': True})
    assert dl.params['noprogress'] is True

