

# Generated at 2022-06-14 15:37:49.005561
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    assert 'fragment_retries' in fd.params
    assert 'skip_unavailable_fragments' in fd.params

# Generated at 2022-06-14 15:37:57.552495
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MockYDL(object):
        def __init__(self):
            self.params = {}
    class MockFragmentFD(FragmentFD):
        def __init__(self):
            self.ydl = MockYDL()
    assert not hasattr(MockFragmentFD(), 'dl')
    assert FragmentFD(MockYDL(), {}).dl is not None
    assert isinstance(FragmentFD(MockYDL(), {}).dl, HttpQuietDownloader)


# Generated at 2022-06-14 15:38:03.719204
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from .extractor import gen_extractors
    gen_extractors()
    downloader = HttpQuietDownloader({}, {})
    assert (downloader.params['format'] in downloader._default_format) == \
        (sys.version_info[0] == 2)  # Default format is webm for py2, mp4 for py3

# Generated at 2022-06-14 15:38:05.521931
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(None, None)
    assert fd

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:38:12.632519
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .youtube import YoutubeDL
    y = YoutubeDL({'quiet': True})
    y.add_default_info_extractors()
    h = HttpQuietDownloader(y, {'noprogress': True, 'quiet': True})
    assert isinstance(h, HttpFD)
    assert h.params['quiet']
    assert h.params['noprogress']


# Generated at 2022-06-14 15:38:15.819372
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert FragmentFD is FileDownloader

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:38:18.230946
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    assert fd.to_screen == fd.ydl.to_screen

# Generated at 2022-06-14 15:38:22.644963
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange
    class FakeInfoExtractor(InfoExtractor):
        def __init__(self):
            InfoExtractor.__init__(self)

# Generated at 2022-06-14 15:38:31.143854
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(None, {'fragment_retries': '10'})
    assert fd.params['fragment_retries'] == 10
    fd = FragmentFD(None, {'fragment_retries': 'inf'})
    assert fd.params['fragment_retries'] == float('inf')
    fd = FragmentFD(None, {'fragment_retries': '-1'})
    assert fd.params['fragment_retries'] == float('inf')


# Generated at 2022-06-14 15:38:40.019278
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import YoutubeDL
    ydl = YoutubeDL.YoutubeDL({'quiet': True})
    fd = FragmentFD(ydl)
    assert fd.params == {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'keep_fragments': False,
    }
    ydl = YoutubeDL.YoutubeDL({
        'quiet': True,
        'fragment_retries': 5,
        'skip_unavailable_fragments': False,
        'keep_fragments': True,
    })
    fd = FragmentFD(ydl)

# Generated at 2022-06-14 15:39:02.615948
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    from ..extractor import gen_extractors

    # Initialize DASH and hlsnative extractors
    gen_extractors()

    for ie in InfoExtractor._ies:
        if ie.ie_key() in [
                'dash',
                'hlsnative',
        ]:
            frag_filename = 'test.mp4'
            params = {
                'noprogress': True,
                'outtmpl': frag_filename,
                'format': 'best',
            }
            ie = ie.ie
            # Test constructor
            fd = ie(
                downloader=None,
                params=params,
                filename=frag_filename,
                info_dict={})
            assert fd.FD_NAME == ie.ie_key()



# Generated at 2022-06-14 15:39:05.321037
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    hqd = HttpQuietDownloader({}, {'continuedl': True, 'quiet': True, 'noprogress': True})
    assert hqd.ydl is not None
    assert hqd.params['continuedl'] is True
    assert hqd.params['noprogress'] is True



# Generated at 2022-06-14 15:39:07.190432
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader(None, None)
    assert dl.params['quiet']
    assert dl.params.get('noprogress')

# Generated at 2022-06-14 15:39:16.021786
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # https://github.com/rg3/youtube-dl/issues/6931
    # https://github.com/rg3/youtube-dl/pull/6936
    from .http import HttpDownloader as HttpFD
    from .fragment import FragmentFD
    fd = FragmentFD(HttpFD(HttpQuietDownloader(), None, None))
    # this is the only important thing, if this passes it means the constructor
    # call is correct
    fd.report_skip_fragment(None)

# Generated at 2022-06-14 15:39:23.986135
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys

    class FakeYTDLSettings():
        params = {}
    class FakeYTDLInfoDict():
        def __init__(self):
            self.ydl_opts = FakeYTDLSettings()
        def __del__(self):
            pass
    # This should call the constructor of HttpQuietDownloader
    FakeYTDLSettings.params['noprogress'] = True
    # No need to call the constructor, the test will be done by superclass
    FileDownloader(FakeYTDLInfoDict(), params={})


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:39:35.976274
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from .extractor import get_info_extractor

    def _stderr_write():
        sys.stderr.write('\n')

    # Create a FragmentFD for a DASH manifest
    ies = get_info_extractor(
        'http://127.0.0.1/dash.youtube.com/get_video_info/'
        '?video_id=JQhGQZVuY2Y')
    info = ies.extract('JQhGQZVuY2Y')

# Generated at 2022-06-14 15:39:37.258343
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    tester = FragmentFD({})
    assert isinstance(tester, FragmentFD)

# Generated at 2022-06-14 15:39:46.170526
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from . import YoutubeDL
    from .extractor.common import InfoExtractor
    from .extractor.youtube import YoutubeIE

    class MockExtractor(InfoExtractor):
        def __init__(self, *args, **kwargs):
            InfoExtractor.__init__(self)
            self._entries = kwargs.pop('entries', [])

        def _real_extract(self, url):
            return self._entries.pop(0)

    class MockFD(FragmentFD):
        def __init__(self, ydl, *args, **kwargs):
            self.__ydl = ydl
            FragmentFD.__init__(self, ydl, *args, **kwargs)

        @property
        def ydl(self):
            return self.__ydl

    ydl = YoutubeDL

# Generated at 2022-06-14 15:39:52.397086
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader

    class MyFragFD(FragmentFD):
        def __init__(self, ydl, params):
            super(MyFragFD, self).__init__(ydl, params)
            assert self.params is params
            assert self.ydl is ydl

    ydl = FileDownloader({})
    params = {'a': 3}
    MyFragFD(ydl, params)

# Generated at 2022-06-14 15:39:54.995268
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    """
    >>> from youtube_dl.downloader.http import FragmentFD
    >>> FragmentFD(None, None).FD_NAME
    'fragment'
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 15:40:37.694209
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractor_classes, list_extractors
    from .extractor.common import InfoExtractor
    from ..compat import compat_str

    for ie in gen_extractor_classes():
        class TestIE(ie):
            IE_NAME = 'Test_' + ie.IE_NAME

            def _real_initialize(self):
                pass

            def _real_extract(self, url):
                pass

            def _download_webpage(self, *args, **kargs):
                pass

            def _download_xml(self, *args, **kargs):
                pass

            def _download_json(self, *args, **kargs):
                pass

        ie = TestIE(InfoExtractor())

# Generated at 2022-06-14 15:40:42.379028
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .smoothstreams import SmoothStreamsFD
    from .dash import DASHFD

    assert issubclass(DASHFD, FragmentFD)
    assert issubclass(SmoothStreamsFD, FragmentFD)
    assert not issubclass(FileDownloader, FragmentFD)

# Generated at 2022-06-14 15:40:43.955044
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert 'noprogress' in HttpQuietDownloader(None, None).params

# Generated at 2022-06-14 15:40:49.970952
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class FakeYDL:
        def __init__(self):
            self.params = {
                'outtmpl': '%(id)s',
                'continuedl': True,
                'noprogress': False,
                'logger': None,
                'progress_hooks': [],
            }
    ydl = FakeYDL()
    qdl = HttpQuietDownloader(ydl, {'continuedl': True, 'noprogress': True})
    assert isinstance(qdl, HttpQuietDownloader)

# Generated at 2022-06-14 15:40:59.106110
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class Opts(object):
        def __init__(self):
            self.noprogress = False
            self.retries = 0
            self.fragment_retries = 0
            self.skip_unavailable_fragments = True

    ydl = object()
    hqd = HttpQuietDownloader(ydl, Opts())
    assert (hqd
            and not hqd.params['noprogress']
            and hqd.params['retries'] == 0
            and hqd.params['fragment_retries'] == 0
            and hqd.params['skip_unavailable_fragments'] is True)



# Generated at 2022-06-14 15:41:11.701880
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    from .http import HttpFD
    from .extractor.common import InfoExtractor

    class TestIE(InfoExtractor):
        def _real_extract(self, url):
            return {
                'id': 'test_id',
                'title': 'test_title',
                'url': 'http://dummyurl.com',
            }

    gen_extractors()
    ie = TestIE(downloader=HttpQuietDownloader(
        downloader=HttpFD().downloader, ydl=None))
    info_dict = ie.extract('http://dummyurl.com')

    assert info_dict['id'] == 'test_id'
    assert info_dict['title'] == 'test_title'

# Generated at 2022-06-14 15:41:17.047923
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = {}
    params = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'ratelimit': None,
        'retries': 0,
        'nopart': False,
        'test': False
    }
    assert HttpQuietDownloader(ydl, params).params == params

# Generated at 2022-06-14 15:41:21.475276
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import youtube_dl.FileDownloader
    inst = youtube_dl.FileDownloader({
        'noprogress': True,
        'quiet': True,
        'format': 'webm',
        'restrictfilenames': True,
        'nooverwrites': False,
    })
    FragmentFD(inst, {'fragment_retries': 5, 'restrictfilenames': False})

# Generated at 2022-06-14 15:41:25.630845
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MyFragmentFD(FragmentFD):
        FD_NAME = 'test'
        def ytdl_filename(self, name):
            return name + '.ytdl'
        def temp_name(self, name):
            return name + '.part'
        def try_rename(self, old_filename, new_filename):
            return
        def calc_eta(self, start_time, end_time, total_bytes, downloaded_bytes):
            return 1
        def report_destination(self, *args, **kargs):
            return
        def report_warning(self, *args, **kargs):
            return

    fd = MyFragmentFD(None)
    ctx = {
        'filename': 'filename',
        'total_frags': 5,
    }
    fd._prepare_fr

# Generated at 2022-06-14 15:41:32.383570
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def _dummy_write_ytdl_file(ctx):
        pass

    def _dummy_download(filename, info_dict):
        return True

    fd = FragmentFD(
        {
            'params': {
                'noprogress': True,
            },
            'to_screen': lambda *args, **kwargs: None,
            '_hook_progress': lambda x: None,
        },
    )
    fd.write_ytdl_file = _dummy_write_ytdl_file
    fd.dl.download = _dummy_download
    fd._prepare_url = lambda info_dict, url: url
    fd._append_fragment = lambda ctx, frag_content: None

# Generated at 2022-06-14 15:42:55.401647
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .downloader import YoutubeDL
    ydl = YoutubeDL()
    ydl.params['fragment_retries'] = 10
    ydl.params['skip_unavailable_fragments'] = True
    ydl.params['keep_fragments'] = True
    ydl.params['noprogress'] = True
    fd = FragmentFD(ydl)
    assert fd.params['fragment_retries'] == 10
    assert fd.params['skip_unavailable_fragments'] == True
    assert fd.params['keep_fragments'] == True
    assert fd.params['noprogress'] == True

# Generated at 2022-06-14 15:43:02.884919
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader

    class TestHttpQuietDownloader(HttpQuietDownloader):
        def to_screen(self, *args, **kargs):
            pass

    # FIXME remove this (see https://github.com/rg3/youtube-dl/issues/11694)
    FileDownloader.params = {}

    # Check __init__
    params = {'ratelimit': 10240}
    info_dict = {'url': 'foo'}
    ydl = type('YoutubeDL', (object,), {'params': params})()
    fd = TestHttpQuietDownloader(ydl, info_dict)
    assert fd.ydl is ydl
    assert fd.params['ratelimit'] == 10240

# Generated at 2022-06-14 15:43:08.520525
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    from .common import FileDownloader
    from .http import HttpFD
    assert FragmentFD(None, None)
    assert FragmentFD(FileDownloader(None), None)
    assert FragmentFD(HttpFD(None, None), None)

# Generated at 2022-06-14 15:43:18.815671
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=W0212
    from .youtube import YoutubeFD
    from .dash import DASHFD
    from .hls import HLSFD

    def do_test(fd_cls):
        assert issubclass(fd_cls, FragmentFD)
        fd = fd_cls(None)
        assert fd.params == {}
        fd = fd_cls(None, params={'noprogress': True})
        assert fd.params == {'noprogress': True}

    do_test(YoutubeFD)
    do_test(DASHFD)
    do_test(HLSFD)

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:43:24.280275
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .youtube_dl.YoutubeDL import YoutubeDL
    from .extractor.common import InfoExtractor

    class FakeInfoExtractor(InfoExtractor):
        def __init__(self, ydl):
            self.ydl = ydl

    ydl = YoutubeDL()
    FakeInfoExtractor(ydl)._downloader = HttpQuietDownloader(ydl, {'quiet': True})
    assert ydl.params['quiet'] is True


# Generated at 2022-06-14 15:43:35.870109
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    import tempfile
    import shutil

    class MyFD(FragmentFD):

        def __init__(self, params, ydl):
            self.params = params
            self.ydl = ydl
            self.tmpfilename = self.temp_name(ydl.prepare_filename('video'))
            assert self.tmpfilename

        def download(self, video_filename, video_info):
            return True

        def calc_eta(self, start, end, total_bytes, downloaded_bytes):
            return (downloaded_bytes / total_bytes) * (end - start)

        def temp_name(self, *args, **kwargs):
            return FragmentFD.temp_name(self, *args, **kwargs)


# Generated at 2022-06-14 15:43:46.966811
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    from .extractor.youtube import YoutubeIE
    from .extractor.youtube import YoutubePlaylistIE
    from .extractor.youtube import YoutubeChannelIE
    from .utils import match_filter_func
    from .utils import orderedSet
    from .postprocessor.ffmpeg import FFmpegPostProcessor


# Generated at 2022-06-14 15:43:51.339820
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import youtube_dl.FileDownloader
    ydl = youtube_dl.FileDownloader.FileDownloader()
    dl = HttpQuietDownloader(ydl, {'quiet': True})
    assert dl.params['quiet']

# Generated at 2022-06-14 15:43:56.713974
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def test(**kwargs):
        dl = HttpQuietDownloader(None, kwargs)
        for key in kwargs:
            assert dl.params[key] == kwargs[key]
    test(ratelimit='10k', retries=10, nopart=True, test=True)

# Generated at 2022-06-14 15:44:06.832888
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..YoutubeDL import YoutubeDL
    hd = HttpQuietDownloader(YoutubeDL({
        'quiet': False,
        'noprogress': False,
        'nopart': False,
        'logger': None
    }), {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'nopart': True,
        'logger': None
    })
    assert 'quiet' in hd.params
    assert 'noprogress' in hd.params
    assert 'continuedl' in hd.params
    assert 'nopart' in hd.params
    assert hd.params['quiet']
    assert hd.params['noprogress']
    assert hd.params['continuedl']
    assert hd