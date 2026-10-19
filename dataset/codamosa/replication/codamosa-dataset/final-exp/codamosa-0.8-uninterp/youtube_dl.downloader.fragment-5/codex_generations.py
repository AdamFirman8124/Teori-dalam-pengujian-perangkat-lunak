

# Generated at 2022-06-14 15:37:58.164733
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    from .downloader.rtmp import RTMPFD
    ydl = InfoExtractor()
    dl = HttpQuietDownloader(ydl, {'quiet': True})
    dl.report_warning(u'foo')
    assert not dl.report
    dl.report_warning(u'foo', u'bar')
    assert not dl.report
    dl.report_error(u'foo')
    assert not dl.report
    dl.report_error(u'foo', u'bar')
    assert not dl.report
    dl.report_file_already_downloaded(u'foo')
    assert not dl.report
    dl.report_file_already_downloaded(u'foo', u'bar')

# Generated at 2022-06-14 15:38:09.069627
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def sanitize(s):
        return s.replace("\\", "/")
    fd = FragmentFD(None, {"format": "mp4"})

    assert fd.ytdl_filename("abc") == "abc.ytdl"
    assert fd.ytdl_filename("/a/b/c") == "/a/b/c.ytdl"
    # The following test may fail on Windows
    # TODO: Fix this test on Windows
    assert fd.ytdl_filename("a\u2014b.mp4") == "a\u2014b.mp4.ytdl"
    # Ditto
    # assert fd.ytdl_filename("/a/b/\u2014") == "/a/b/\u2014.ytdl"

# Generated at 2022-06-14 15:38:14.410826
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = FileDownloader(params={'noprogress': True})
    dl = HttpQuietDownloader(
        ydl, {'quiet': True, 'noprogress': True, 'retries': 0})
    assert dl.params['quiet'] is True

# Generated at 2022-06-14 15:38:16.194543
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import youtube_dl.YoutubeDL
    ydl = youtube_dl.YoutubeDL({'quiet': True})
    fd = FragmentFD(ydl)
    assert isinstance(fd, FragmentFD)
    assert isinstance(fd, FileDownloader)

# Generated at 2022-06-14 15:38:21.902077
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # TODO
    # This test doesn't work as ydl is not a mock.
    #    # Create an instance of FragmentFD
    #    fd = FragmentFD(mock.Mock())
    #    # Check that the constructor did not fail
    #    assert fd is not None
    pass

# Generated at 2022-06-14 15:38:27.215341
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=W0212
    assert len(FragmentFD.__bases__) == 1
    assert FragmentFD.__bases__[0] is FileDownloader
    fd = FragmentFD(None, None)
    assert fd.params is None
    assert fd.ydl is None

# Generated at 2022-06-14 15:38:33.094736
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Use youtube-dl's testing facility to invoke constructor of class
    # HttpQuietDownloader (see http://git.io/vV8MA for details).
    from . import YoutubeDL
    ydl = YoutubeDL({'quiet': False, 'simulate': True})
    HttpQuietDownloader(ydl, {'quiet': True, 'foobar': 'spam'})

# Generated at 2022-06-14 15:38:40.915877
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from ..downloader.common import FileDownloader
    assert issubclass(HttpQuietDownloader, FileDownloader)

    # check that HttpQuietDownloader doesn't write to stdout
    quiet_fd = HttpQuietDownloader(object(), {'noprogress': False, 'quiet': True})
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    quiet_fd.to_screen('Test')
    assert sys.stdout.getvalue() == ''
    sys.stdout = old_stdout

    # check that HttpQuietDownloader doesn't write to stderr
    quiet_fd = HttpQuietDownloader(object(), {'noprogress': False, 'quiet': False})
    old_stderr = sys.stderr

# Generated at 2022-06-14 15:38:48.511931
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    from collections import namedtuple
    Options = namedtuple('Options', ['nopart'])
    params = {
        'format': 'best',
        'noplaylist': True,
        'quiet': False,
    }
    ydl = YoutubeDL(params)
    ydl.add_info_extractor(FragmentFD(ydl, params, Options(nopart=params.get('nopart', False))))

# Generated at 2022-06-14 15:38:52.314304
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader(
        {},
        {'noprogress': True, 'quiet': True})
    assert dl._opts['noprogress']
    assert dl._opts['quiet']

# Generated at 2022-06-14 15:39:22.142072
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from ..compat import compat_basestring
    ydl = {'params':{}}
    dl = HttpQuietDownloader(ydl, ydl['params'])
    assert dl.report_warning('warning') is None
    assert dl.trouble('error') == 1
    assert dl.to_screen('message') is None
    assert dl.to_stderr('error') is None
    assert dl.to_console_title('title') is None
    assert isinstance(dl.to_stdout('data'), compat_basestring)
    assert dl.to_stdout('data') == 'data'
    assert dl.add_progress_hook(lambda x: None) is None

# Generated at 2022-06-14 15:39:27.417759
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def build_ydl(ydl_kwargs):
        params = {
            'ratelimit': 10 * 1024,
            'extract_flat': 'in_ext' in ydl_kwargs,
            'skip_download': True,
        }
        params.update(ydl_kwargs)
        from ..YoutubeDL import YoutubeDL
        return YoutubeDL(params)
    import unittest
    class CustomTestCase(unittest.TestCase):
        def __init__(self, *args, **kwargs):
            # Python 2.6 does not have the assertDictContainsSubset method of 3.2
            if not hasattr(self, 'assertDictContainsSubset'):
                self.assertDictContainsSubset = self._assertDictContainsSubset
            unittest.TestCase.__

# Generated at 2022-06-14 15:39:29.829352
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    hqd = HttpQuietDownloader(None, None)
    assert hqd is not None


# Generated at 2022-06-14 15:39:32.938308
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fragment_fd = FragmentFD(None, {'quiet': True})
    assert fragment_fd.params['quiet'] is True
    assert 'skip_unavailable_fragments' not in fragment_fd.params

# Generated at 2022-06-14 15:39:36.057936
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    inst = HttpQuietDownloader('youtube-dl', {'ratelimit': None, 'retries': 2})
    assert inst.params['retries'] == 2
    inst.report_warning('warning')
    assert inst.to_stderr_called == 0

# Generated at 2022-06-14 15:39:45.131184
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import youtube

    tests = [
        (youtube.YoutubeIE(), {
            'live': False,
            'total_frags': 10,
            'filename': 'video.mp4'
        }),
        (youtube.YoutubeIE(), {
            'live': True,
            'filename': 'video.mp4'
        }),
    ]

    for ie, test_data in tests:
        test_data.update({
            'fragment_duration': 10.0,
            'fragment_retries': 10,
            'skip_unavailable_fragments': True,
            'keep_fragments': False
        })
        fd = FragmentFD(ie, test_data)
        assert fd.ie == ie

# Generated at 2022-06-14 15:39:52.813404
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from . import YoutubeDL
    ydl = YoutubeDL()
    ydl.params['nooverwrites'] = True
    hqd = HttpQuietDownloader(ydl, {'continuedl': True, 'quiet': True, 'noprogress': True})
    assert hqd
    assert hqd.ydl is ydl
    assert hqd.params['continuedl']
    assert hqd.params['quiet']
    assert hqd.params['noprogress']
    assert hqd._opener is ydl._opener
    assert hqd._http_retries == 10

# Generated at 2022-06-14 15:40:01.269481
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # A FD class with empty params
    class MyFD(FragmentFD):
        FD_NAME = 'test'
    fd = MyFD({})
    assert fd.params == {}
    # A FD class with non-empty params
    class MyFD(FragmentFD):
        FD_NAME = 'test'
        def real_extract(self, url):
            assert self.params['a'] == '1'
            assert self.params['b'] == '2'
    fd = MyFD({'a': '1', 'b': '2'})
    fd.real_extract('fake url')

# Generated at 2022-06-14 15:40:14.353461
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # Mock up the YoutubeDL class
    class MockYDL():
        params = {}

    ydl = MockYDL()
    fd = FragmentFD(ydl)
    url = 'http://example.com/video.ext'
    info = {'id': 'video_id'}

    # Test without handler
    fd.params['fragment_retries'] = 1
    fd.params['skip_unavailable_fragments'] = False
    fd.params['keep_fragments'] = False
    fd.add_info_dict(info, True)
    fd.report_destination(url)
    assert fd.downloaded_info_dicts == [info]
    assert fd.params['fragment_retries'] == 3

# Generated at 2022-06-14 15:40:23.816304
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFragmentFD(FragmentFD):
        FD_NAME = 'testfd'
        def real_initialize(self):
            pass

    ydl = {}
    params = {
        'file_id': 1,
        'outtmpl': '%(file_id)s',
        'keep_fragments': True,
    }
    inst = TestFragmentFD(ydl, params)
    assert inst.params['file_id'] == 1
    assert inst.temp_name('1') == '1.part'
    assert inst.ytdl_filename('1') == '1.ytdl'

# Generated at 2022-06-14 15:41:12.020154
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys

    class Opts(object):
        def __init__(self, **kwargs):
            self.__dict__ = kwargs

    class YDL(object):
        def __init__(self, opts):
            self.params = opts

    opt = Opts(noprogress=True)
    ydl = YDL(opt)
    frag = FragmentFD(ydl, opt)
    dl = HttpQuietDownloader(ydl, opt)

    # Test if the constructor of HttpQuietDownloader is called
    assert isinstance(frag, FragmentFD)
    assert frag.params == opt.__dict__
    assert isinstance(dl, HttpQuietDownloader)
    assert dl.params == opt.__dict__

    # Test if the to_screen signature and function are

# Generated at 2022-06-14 15:41:13.869305
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    fd = HttpQuietDownloader(None, {})
    assert(isinstance(fd, HttpFD))

# Generated at 2022-06-14 15:41:22.850519
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import os
    from .common import FileDownloader

    try:
        os.mkdir('test_tmp')
    except OSError:
        pass

    test_cases = (
        ('-', True),
        ('test.mp4', False),
    )

    for tmpfilename, use_tmp_filename in test_cases:
        params = {
            'noprogress': True,
            'logger': None,
        }
        if use_tmp_filename:
            params['tmpfilename'] = tmpfilename
        d = FragmentFD(params, None)
        if use_tmp_filename:
            assert d.tmpfilename == '-', 'Unexpected tmpfilename'
        else:
            assert d.tmpfilename == '.test.mp4.part', 'Unexpected tmpfilename'

# Generated at 2022-06-14 15:41:31.397009
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFragFD(FragmentFD):
        def __init__(self):
            # This is a simplified version of constructor of class YoutubeDL
            self.params = {}
            self.params['noprogress'] = False
            self.logger = self
            self._progress_hooks = []
        def to_screen(self, *args, **kargs):
            pass
    ffd = TestFragFD()
    ctx = {
        'filename': 'filename.f4m',
        'url': 'url',
        'total_frags': 5,
    }
    ffd._prepare_frag_download(ctx)

    assert os.path.isfile(ffd.ytdl_filename('filename.f4m'))

# Generated at 2022-06-14 15:41:37.390644
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..utils import UnsupportedError
    from .http import HttpFD

    class MockYDL(object):
        def __init__(self):
            self.param = {}

    def mock_report_warning(msg):
        pass

    ydl = MockYDL()
    ydl.report_warning = mock_report_warning
    params = dict(
        noprogress=True,
        ratelimit=None,
        retries=1,
        nopart=True,
        test=False,
    )
    ydl = HttpQuietDownloader(
        ydl,
        params,
    )

    info_dict = dict(
        url='https://example.com/index.html',
        http_headers=None,
    )
    filename = 'index.html'
    success = ydl.download

# Generated at 2022-06-14 15:41:44.390610
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FakeInfoDict(dict):
        def __init__(self, *args, **kwargs):
            super(FakeInfoDict, self).__init__(*args, **kwargs)
            self.__dict__ = self


# Generated at 2022-06-14 15:41:48.007839
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..YoutubeDL import YoutubeDL
    assert HttpQuietDownloader(YoutubeDL(), {})

# Generated at 2022-06-14 15:41:49.565463
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert HttpQuietDownloader({}, {})

# Generated at 2022-06-14 15:41:56.437851
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    ie = InfoExtractor()

    # This is an example from HttpFD._real_initialize
    ie._downloader = HttpQuietDownloader(ie, {'continuedl': True, 'quiet': True, 'noprogress': True, 'ratelimit': None, 'retries': 0, 'nopart': False, 'test': False})

    assert isinstance(ie._downloader, HttpQuietDownloader)

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:42:01.519895
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    from ..utils import ExtractorError
    try:
        FragmentFD(InfoExtractor(), {})
        assert False, 'Expected TypeError'
    except TypeError as e:
        pass
    try:
        FragmentFD(InfoExtractor(), {'format': 'a'})
        assert False, 'Expected ExtractorError'
    except ExtractorError as e:
        pass

# Generated at 2022-06-14 15:43:20.232096
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import YoutubeIE

    class TestFD(FragmentFD):
        NAME = 'TestFD'
        IE_NAME = 'youtube'

    # First test: no problems, successful download
    test_fd = TestFD({})
    test_fd.to_screen = lambda *_: None
    test_fd.report_warning = lambda *_: None
    test_fd.report_error = lambda *_: None
    test_fd.report_destination = lambda *_: None


# Generated at 2022-06-14 15:43:21.764593
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader(None, {'noprogress': False})
    assert not dl._params.get('noprogress')

# Generated at 2022-06-14 15:43:26.753553
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    """Test if the constructor of FragmentFD class works"""

    ydl = FileDownloader({})
    test_fd = FragmentFD(ydl)
    assert ydl == test_fd.ydl
    assert test_fd.FD_NAME


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:43:37.530466
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    hqd = HttpQuietDownloader(
        {
            'usenetrc': False,
            'username': 'u',
            'password': 'p',
            'videopassword': 'vp',
        },
        {
            'quiet': True,
            'noprogress': True,
            'retries': 0,
            'continuedl': True,
            'nopart': False,
            'test': False,
        }
    )
    assert not hqd.params['quiet']
    assert not hqd.params['noprogress']
    assert len(hqd.http_headers)


# Generated at 2022-06-14 15:43:39.026810
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:43:42.181427
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    assert isinstance(fd, FragmentFD)

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:43:44.757119
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .downloader import YoutubeDL
    ydl = YoutubeDL()
    ydl.prepare_filename = lambda f: f
    fd = FragmentFD(ydl)

# Generated at 2022-06-14 15:43:48.843615
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractors

    gen_extractors()
    from ..extractor.common import InfoExtractor

    ie = InfoExtractor()
    ie.add_default_info_extractors()


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:44:01.486614
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    class FakeInfoDict(object):
        pass
    filename = 'test.flv'
    info_dict = FakeInfoDict()
    info_dict.filename = filename
    info_dict.http_headers = False
    fd = FragmentFD(FakeYDL(), info_dict)
    fd.to_screen = lambda *x: sys.stdout.write(x[0] + '\n')
    fd.report_warning = lambda *x: sys.stderr.write(x[0] + '\n')
    fd.try_rename = lambda x, y: None
    fd.params = {
        'noprogress': False,
        'updatetime': True,
    }

# Generated at 2022-06-14 15:44:04.530550
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        FD_NAME = 'testfd'
    assert TestFD.FD_NAME == 'testfd'
    fd = TestFD(None, {}, None)
    assert fd.FD_NAME == 'testfd'

# Generated at 2022-06-14 15:47:22.305869
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    info_dict = {
        'fragments': [None],
        'http_headers': {},
    }
    params = {}
    ydl = object()
    fd = FragmentFD(ydl, info_dict, params)
    assert fd.FD_NAME == 'generic'
    assert fd.ydl is ydl
    assert fd.info_dict is info_dict
    assert fd.params is params

    fd.add_info_dict(
        {
            'http_headers': {
                'Cookie': 'foo=bar',
            }
        },
        override=False)

    fd.add_info_dict(
        {
            'http_headers': {
                'Referer': 'ref',
            }
        },
        override=True)

    info_dict = f