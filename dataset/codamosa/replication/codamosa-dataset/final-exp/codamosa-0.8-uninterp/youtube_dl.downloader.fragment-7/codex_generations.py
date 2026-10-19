

# Generated at 2022-06-14 15:37:50.199791
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def test_download(filename, info_dict):
        return True
    ydl = {}
    hqd = HttpQuietDownloader(ydl, {})
    assert hqd.ydl is ydl
    hqd.download = test_download
    hqd.download('test', {})

# Generated at 2022-06-14 15:38:02.798360
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader(
        None,
        {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'ratelimit': '5',
            'nopart': True,
            'test': True,
            'retries': 5,
        }
    )

    assert dl.ydl is None
    assert dl.params['continuedl'] is True
    assert dl.params['quiet'] is True
    assert dl.params['noprogress'] is True
    assert dl.params['ratelimit'] == 5
    assert dl.params['nopart'] is True
    assert dl.params['test'] is True
    assert dl.params['retries'] == 5

# Generated at 2022-06-14 15:38:07.971311
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor
    fd = FragmentFD(None, None, {'noprogress': True})
    assert fd.FD_NAME == 'generic'
    fd = FragmentFD(None, None, {
        'fragment_base_url': 'base_url',
        'fragments': ['a', 'b', 'c'],
        'noprogress': True,
    })
    assert fd.FD_NAME == 'generic'
    fd = FragmentFD(None, None, {
        'fragment_base_url': 'base_url',
        'fragments': ['a', 'b', 'c'],
        'noprogress': True,
    })
    assert fd.FD_NAME == 'generic'
    f4m_

# Generated at 2022-06-14 15:38:10.191280
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # No arguments
    HttpQuietDownloader(None, {})

# Generated at 2022-06-14 15:38:14.862930
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..__main__ import YoutubeDL
    inst = YoutubeDL({})
    FileDownloader = FragmentFD
    fd = FileDownloader(inst, {'fragment_retries': 10, 'noprogress': True})



# Generated at 2022-06-14 15:38:18.297800
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import youtube_dl
    ydl = youtube_dl.YoutubeDL(dict(logger=None))
    assert ydl is not None


# Generated at 2022-06-14 15:38:28.734382
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FileDownloaderSubclass(FragmentFD):
        pass

    ydl = object()
    params = {
        'noprogress': True,
        'ratelimit': None,
        'retries': 0,
        'nopart': False,
        'test': False,
    }

    fd = FileDownloaderSubclass(ydl, params)
    assert fd.retries == 0
    assert fd.continuedl
    assert fd.quiet
    assert fd.noprogress
    assert fd.ratelimit is None
    assert not fd.nopart
    assert not fd.test

# Generated at 2022-06-14 15:38:38.743393
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.youtube import YoutubeIE
    from youtube_dl.utils import parse_filesize

    ydl = YoutubeDL({
        'forcetitle': True,
        'simulate': True,
        'skip_download': True,
        'quiet': True,
    })

    fd = FragmentFD(ydl, { 'skip_download': True })


# Generated at 2022-06-14 15:38:51.371703
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import pytest
    from ..compat import compat_urllib_parse_urlparse, compat_urllib_parse_unquote
    names = ['http', 'https', 'rtsp', 'mms', 'rtmp']
    schemes = {'mms': 'mmsh'}
    netlocs = ['www.example.com', '127.0.0.1', 'localhost', 'user:pass@localhost']
    paths = ['/', '/example.mp4', '/path/to/example.mp4', '/path/to/file%20with%20spaces']
    query_strings = ['', '?param=val', '?%s' % '&'.join(('param%d=val%d' % (d, d) for d in range(10)))]
    fragments = ['', '#fragment']

# Generated at 2022-06-14 15:39:02.540296
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import tempfile

    # Preparing temp files and directories
    tempdir = encodeFilename(tempfile.mkdtemp())
    tmp = ['', '', '']
    tmp[0] = encodeFilename(tempfile.NamedTemporaryFile(mode='w+b', suffix='.tmp', dir=tempdir).name)
    tmp[1] = encodeFilename(tempfile.NamedTemporaryFile(mode='w+b', suffix='.tmp', dir=tempdir).name)
    tmp[2] = encodeFilename(tempfile.NamedTemporaryFile(mode='w+b', suffix='.ytdl', dir=tempdir).name)

    # Writing ytdl file

# Generated at 2022-06-14 15:39:25.813418
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import io
    import types

    params = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'nopart': False,
        'test': False,
        'retries': 0,
        'ratelimit': None,
        'outtmpl': None,
    }
    outtmpl = '%(id)s.%(ext)s'
    ydl = object()
    fd = HttpQuietDownloader(ydl, params)
    assert isinstance(fd, HttpQuietDownloader)
    assert isinstance(fd._opener, types.NoneType)
    assert fd.ydl is ydl
    assert fd._progress_hooks[0] is fd.report_progress

# Generated at 2022-06-14 15:39:30.599848
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .dash import DASHFD
    from .hls import HLSFD
    assert issubclass(DASHFD, FragmentFD)
    assert issubclass(HLSFD, FragmentFD)

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:39:36.110016
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    assert not fd._prepare_url(None, None)
    info_dict = {'http_headers': {'test': 'headers'}}
    url = 'http://blah.blah'
    req = fd._prepare_url(info_dict, url)
    assert isinstance(req, sanitized_Request)
    assert req.get_method() == 'HEAD'

# Generated at 2022-06-14 15:39:37.438934
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader(None, {'continuedl': True})

# Generated at 2022-06-14 15:39:46.279996
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = None

    class InfoDict(object):
        def __init__(self, url, headers):
            self.url = url
            self.http_headers = headers

    hqd = HttpQuietDownloader(
        ydl,
        {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'nopart': False,
        }
    )

    assert hqd is not None

    info_dict = InfoDict('http://www.example.com/video.mp4', None)
    assert hqd.real_download('/tmp/video1.mp4', info_dict) is None

    info_dict = InfoDict('http://www.example.com/video.mp4', {'Range': 'bytes=0-'})


# Generated at 2022-06-14 15:39:58.049161
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractors
    from ..utils import match_filter_func
    from .extractor.common import InfoExtractor

    URL = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    FILTER_PARAMS = {
        'simulate': True,
        'skip_download': True,
        'matchtitle': 'testvideo',
    }

    class TestIE(InfoExtractor):
        IE_NAME = 'Test'
        _VALID_URL = ':%s:'

        def __init__(self, downloader):
            super(TestIE, self).__init__(downloader)
            self.test_result = False

        def report_download_webpage(self, *args, **kargs):
            pass


# Generated at 2022-06-14 15:40:06.438877
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    from .http import HttpFD
    from .dash import DASHFD
    from .hls import HLSFD
    from types import MethodType, FunctionType
    attributes = set(dir(DASHFD)) - set(dir(HttpFD))
    attributes.remove('__init__')
    attributes.remove('_start_frag_download')
    attributes.remove('select_format')
    attributes.remove('report_resume_byte')
    attributes.remove('report_retry_fragment')
    attributes.remove('report_skip_fragment')
    attributes.remove('std_headers')
    attributes.remove('params')

# Generated at 2022-06-14 15:40:09.533958
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({'writethumbnail': False, 'noprogress': True}, {})
    fd.to_screen('test')

# Generated at 2022-06-14 15:40:15.878724
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    assert fd.params is not None

    fd = FragmentFD(params={'noprogress': True})
    assert fd.params['noprogress']

    fd = FragmentFD(params={'skip_unavailable_fragments': True})
    assert fd.params['skip_unavailable_fragments']

# Generated at 2022-06-14 15:40:20.538544
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class FakeYDL:
        def __init__(self):
            self.params = {}

    ydl = FakeYDL()
    dl = HttpQuietDownloader(ydl, {'continuedl': True})
    assert dl.ydl == ydl

# Generated at 2022-06-14 15:41:08.432011
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD('youtube-dl', {})
    assert isinstance(fd, FileDownloader)
    assert '_hook_progress' in dir(fd)

# Generated at 2022-06-14 15:41:11.098312
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    hqd = HttpQuietDownloader(None, {'quiet': False})
    assert hqd.params.get('quiet') is True

# Generated at 2022-06-14 15:41:19.336984
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    try:
        import StringIO as io
    except ImportError:
        import io
        # < patch
        def b(string):
            return string.encode('UTF-8')
        io.StringIO.write = io.StringIO.write
        io.StringIO.seek = io.StringIO.seek
    with io.StringIO() as output:
        data = {
            'format': '100',
            'url': 'http://example.com/video.ts',
        }
        for key in ('format', 'url'):
            assert key in data

# Generated at 2022-06-14 15:41:29.000493
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    from ..compat import compat_urllib_parse_urlencode

# Generated at 2022-06-14 15:41:32.975538
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    import ETagger
    assert issubclass(FragmentFD, FileDownloader)
    assert FragmentFD.__bases__[1] is ETagger.ETagger


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:41:37.761502
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import ydl_opts
    ydl = YoutubeDL(ydl_opts.YoutubeDL())
    hd = HttpQuietDownloader(ydl, {'continuedl': True})
    # youtube_dl/downloader/http.py base constructor asserts that opts['quiet']
    # is not True. If it succeeds, so should ours.

# Generated at 2022-06-14 15:41:47.531474
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MyFragmentFD(FragmentFD):
        FD_NAME = 'MyFragmentFD'

        def __init__(self, ydl):
            super(MyFragmentFD, self).__init__(ydl)

    from ..extractor.common import InfoExtractor
    from ..utils import DateRange
    from .rtmp import RtmpFD

    ie = InfoExtractor('test')
    mkdtemp = lambda: 'tmpdir'
    dl = lambda filename, info_dict: 'download' in info_dict.get('url', '')
    fd = MyFragmentFD(ie)

# Generated at 2022-06-14 15:41:49.986932
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(FileDownloader({}, {}))
    assert fd is not None

# Generated at 2022-06-14 15:42:00.657087
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import unittest
    from .common import FileDownloaderTest
    from ..compat import compat_HTTPError

    class FragmentFDTest(FileDownloaderTest):
        class YDL(object):
            params = {}

        @classmethod
        def setUpClass(cls):
            cls.ydl = cls.YDL()

        def setUp(self):
            self.ctx = {
                'dl': None,
                'filename': 'test.mp4',
                'total_frags': 4,
            }
            self.frag_fd = FragmentFD(self.ydl)

        def test_start_frag_download(self):
            # Test normal flow
            self.frag_fd._prepare_frag_download(self.ctx)
            start = self.frag_fd._start_

# Generated at 2022-06-14 15:42:03.183930
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    class FakeInfoDict():
        url = 'http://someurl/'
    fd = FragmentFD(None, FakeInfoDict(), None)
    assert fd



# Generated at 2022-06-14 15:43:37.761623
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import get_info_extractor
    from .extractor.youtube import YoutubeIE

    ytdl = YoutubeIE()
    # Info extractor's download method returns a result of FileDownloader's
    # constructor call with the right info dict

# Generated at 2022-06-14 15:43:43.728041
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        def __init__(self, ydl, params, report_warning):
            super(TestFD, self).__init__(ydl, params, report_warning)

        def real_extract(self, url):
            return {}

    fd = TestFD({}, {}, lambda _: None)
    assert fd is not None

# Generated at 2022-06-14 15:43:49.656557
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    get_extractor = lambda ie_name: next(e for e in gen_extractors() if e.IE_NAME == ie_name)
    ydl = get_extractor('generic')
    ydl.params = {'socks_proxy': 'localhost:1234', 'usenetrc': False}
    ydl = HttpQuietDownloader(ydl, {'continuedl': True, 'quiet': True})

# Generated at 2022-06-14 15:43:53.796457
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert HttpQuietDownloader.name() == 'http'
    downloader = HttpQuietDownloader(None, {})
    assert not downloader.params.get('forcetitle')


# Generated at 2022-06-14 15:43:59.948644
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = object()
    params = {'continuedl': False, 'quiet': False, 'noprogress': False, 'ratelimit': None, 'retries': None}
    http_quiet_downloader = HttpQuietDownloader(ydl, params)
    assert http_quiet_downloader.ydl == ydl
    assert http_quiet_downloader.params == params

# Generated at 2022-06-14 15:44:09.182571
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import YoutubeDL
    ydl = YoutubeDL({'quiet': True})
    hqd = HttpQuietDownloader(
        ydl, {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'retries': 3,
            'nopart': False,
            'test': False,
        }
    )
    assert hqd.params.get('continuedl', False)
    assert hqd.params.get('quiet', False)
    assert hqd.params.get('noprogress', False)
    assert hqd.params.get('ratelimit') is None
    assert hqd.params.get('retries', 0) == 3
    assert not hqd.params.get('nopart', False)
    assert not h

# Generated at 2022-06-14 15:44:13.304804
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    ydl = None
    info_dict = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'retries': 5,
        'nopart': False,
        'test': False,
    }
    hq = HttpQuietDownloader(ydl, info_dict)
    assert isinstance(hq, HttpFD)
    assert hq.ydl is ydl
    assert hq.params == info_dict



# Generated at 2022-06-14 15:44:16.237245
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpQuietDownloader
    assert HttpQuietDownloader(None, None)

# Generated at 2022-06-14 15:44:17.626556
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert issubclass(HttpQuietDownloader, HttpFD)

# Generated at 2022-06-14 15:44:22.733680
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import YoutubeDL
    try:
        dl1 = HttpQuietDownloader(YoutubeDL(), {'retries': 10})
        assert dl1.params['retries'] == 10
    except:
        raise
    dl2 = HttpQuietDownloader(YoutubeDL(), {})
    assert dl2.params['retries'] == 0