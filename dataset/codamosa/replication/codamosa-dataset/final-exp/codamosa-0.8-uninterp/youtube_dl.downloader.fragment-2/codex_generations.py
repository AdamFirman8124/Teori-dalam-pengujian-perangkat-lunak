

# Generated at 2022-06-14 15:37:49.452599
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader(object(), {
        'noprogress': False,
        'format': 'mp4',
    })
    assert dl.params['noprogress'] is True
    assert dl.params['format'] == 'mp4'


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:37:52.686527
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .http import HttpFD
    assert HttpFD is not None  # silence pyflakes
    from .http import urlopen
    assert urlopen is not None  # silence pyflakes
    from ..compat import compat_urllib_error
    assert compat_urllib_error is not None  # silence pyflakes

# Generated at 2022-06-14 15:37:57.386154
# Unit test for constructor of class FragmentFD
def test_FragmentFD():

    filename = 'test'
    params = {
        'quiet': True,
        'noprogress': True,
        'skip_unavailable_fragments': False,
        'keep_fragments': True,
    }

    # Test
    fragment_fd = FragmentFD(None, {'outtmpl': filename}, params)

    # Assertion
    # Assert that instance of `FileDownloader` is created
    assert isinstance(fragment_fd, FileDownloader)

# Generated at 2022-06-14 15:37:59.217600
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    p = dict(continuedl=False, quiet=True, noprogress=True, nopart=False, ratelimit=None)
    assert HttpQuietDownloader(None, p) == HttpFD(None, p)

# Generated at 2022-06-14 15:38:09.804685
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    try:
        from ..extractor import youtube
    except ImportError:
        # Test only aspect of constructing FragmentFD, not of
        # _prepare_and_start_frag_download method
        return
    ydl = youtube.YoutubeDL({})
    fd = FragmentFD(
        ydl,
        {
            'format': '18',
            'outtmpl': '%(id)s.%(ext)s',
            'noprogress': False,
        })
    info = {
        'format_id': '18',
        'ext': 'mp4',
        'id': '6v2L2UGZJAM',
        'title': 'Sintel',
        'alt_title': 'Sintel Trailer',
        'upload_date': '20101012',
    }
    f

# Generated at 2022-06-14 15:38:13.126416
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert hasattr(HttpQuietDownloader({}, {}), 'to_screen')


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:38:22.069711
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class YDL(object):
        params = {}

    class DummyLogger(object):
        def debug(self, msg):
            pass

    ydl = YDL()
    ydl.logger = DummyLogger()
    from .http import HttpFD
    http_dl = HttpQuietDownloader(ydl, ydl.params)
    assert isinstance(http_dl, HttpFD)

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:38:34.257104
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import unittest
    import tempfile
    import json

    class MockYDL(object):
        def __init__(self):
            self.params = dict()

        def to_screen(self, *args, **kargs):
            pass

        def add_progress_hook(self, callback):
            self.progress_hook = callback

        def temp_name(self, filename):
            return filename + '.tmp'

        def ytdl_filename(self, filename):
            return filename + '.ytdl'

        def calc_eta(self, start, now, total_bytes, downloaded_bytes):
            return now - start

        def report_warning(self, message):
            pass

        def report_destination(self, filename):
            pass

        def try_rename(self, fromname, toname):
            pass



# Generated at 2022-06-14 15:38:41.753192
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..utils import std_headers
    from ..extractor.common import InfoExtractor
    IE_NAME = 'Test'
    ie = None
    ie = InfoExtractor(IE_NAME, {})
    dl = HttpQuietDownloader(ie, {})
    assert isinstance(dl, HttpQuietDownloader)
    assert dl._ies is ie
    assert dl._download_retcode == 0


test_HttpQuietDownloader.test = 'develop'

# Generated at 2022-06-14 15:38:46.595720
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = None
    params = {}
    fd = HttpQuietDownloader(ydl, params)
    assert not hasattr(fd, 'to_screen')


if __name__ == "__main__":
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:39:07.583683
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert HttpQuietDownloader.__name__ == 'HttpQuietDownloader'
    assert HttpQuietDownloader.__module__ == 'youtube_dl.downloader.fragment'

# Generated at 2022-06-14 15:39:20.162546
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    import tempfile

    ydl = YoutubeDL({
        'outtmpl': tempfile.mkstemp()[1] + '-%(id)s.%(ext)s',
        'quiet': True,
        'skip_download': True,
    })
    fd = FragmentFD(ydl, {'test': False}, {'live': True}, {'test': False})
    assert fd.params.get('test') is False
    assert fd.params.get('live') is True
    ydl.params.update({'test': True})
    assert fd.params.get('test') is True
    ydl.params.update({'test': False})

    ydl.params.update({'quiet': False})

# Generated at 2022-06-14 15:39:25.400544
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from .common import FileDownloader
    from .http import HttpFD
    class DummyYoutubeDL(object):
        params = {}
    dl = HttpQuietDownloader(DummyYoutubeDL(), {'key': 'val'})
    assert isinstance(dl, HttpFD)
    assert dl.ydl is DummyYoutubeDL()
    assert dl.params == {'continuedl': True, 'quiet': True, 'noprogress': True, 'key': 'val'}
    dl = HttpQuietDownloader(DummyYoutubeDL(), {'key': 'val'}, 'dummyname')
    assert dl.name == 'dummyname'

# Generated at 2022-06-14 15:39:34.071331
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = {
        'params': {
            'noprogress': True,
            'ratelimit': 1048576,
            'retries': 10,
            'nopart': True,
            'continuedl': True,
        },
        'to_screen': lambda *args, **kargs: None,
    }
    dl_opts = {
        'test': True,
    }
    dl = HttpQuietDownloader(ydl, dl_opts)
    assert dl._ydl is ydl
    assert dl._opts == dl_opts

# Generated at 2022-06-14 15:39:42.926374
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FragmentFDTest(FragmentFD):
        def __init__(self, ydl):
            super(FragmentFDTest, self).__init__(ydl)
            self.FD_NAME = 'test'

        def real_download(self, filename, info_dict):
            pass

    from .extractor import YoutubeIE
    ydl = YoutubeIE()
    ydl.add_info_extractor(FragmentFDTest(ydl))
    ydl.params['skip_download'] = True
    # Should not fail
    ydl.process_ie_result({
        '_type': 'url',
        'url': 'http://example.com',
    }, download=False)
    ydl.params.clear()

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:39:45.166749
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import YoutubeIE
    ydl = YoutubeIE()
    qd = HttpQuietDownloader(ydl, {'noprogress': True})
    assert qd

# Generated at 2022-06-14 15:39:51.263380
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        def __init__(self, ydl):
            FragmentFD.__init__(self, ydl)

        @staticmethod
        def calc_eta(start, now, total, downloaded):
            return None

        @staticmethod
        def temp_name(filename):
            return filename + '.part'

        @staticmethod
        def ytdl_filename(filename):
            return filename + '.ytdl'

        def try_rename(self, fromname, toname):
            pass

    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.compat import is_py2
    from io import BufferedWriter


# Generated at 2022-06-14 15:39:53.472811
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader

    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:39:57.130583
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpDownloader
    assert issubclass(HttpQuietDownloader, HttpDownloader)
    assert HttpQuietDownloader.to_screen == FragmentFD.to_screen

# Generated at 2022-06-14 15:40:10.166322
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from .extractor import gen_extractor_classes
    from .extractor.common import InfoExtractor

    class DummyIE(InfoExtractor):
        IE_NAME = 'dummy'
        IE_DESC = 'Dummy IE'
        _VALID_URL = r'(?:https?://)?(?:\w+\.)?youtube\.com/(?:watch|playlist)'


# Generated at 2022-06-14 15:40:49.973792
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD.__name__ is 'FragmentFD'

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:41:00.179294
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from .common import FileDownloader

    class MyFD(FileDownloader):
        def __init__(self, ydl, params):
            super(MyFD, self).__init__(ydl, params)
            self.info = dict()

        def to_screen(self, *args, **kargs):
            self.info['to_screen'] = args

        def report_progress(self, *args, **kargs):
            self.info['report_progress'] = args

        def report_error(self, *args, **kargs):
            self.info['report_error'] = args


# Generated at 2022-06-14 15:41:07.144384
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = object()
    mock_http_downloader_params = {'noprogress': True}
    http_quiet_downloader = HttpQuietDownloader(ydl, mock_http_downloader_params)
    assert http_quiet_downloader
    assert http_quiet_downloader.ydl is ydl
    assert http_quiet_downloader.params is mock_http_downloader_params

# Generated at 2022-06-14 15:41:12.310061
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    h = HttpQuietDownloader(None, {})
    assert isinstance(h, HttpQuietDownloader)
    assert hasattr(h, 'ydl')
    assert h.params == {}
    assert hasattr(h, 'to_screen')
    assert callable(h.to_screen)


# Generated at 2022-06-14 15:41:21.656027
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor import get_info_extractor
    from ..extractor.youtube import YoutubeIE

    ytdl = YoutubeIE()
    ytdl.add_progress_hook(lambda s: None)

# Generated at 2022-06-14 15:41:27.478729
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .cache import CacheClass
    extractor_names = ['youtube', 'test']
    fd = FragmentFD(CacheClass(None, None, None), None, None, extractor_names, False)
    assert fd.FD_NAME == 'test'
    assert fd.extractor_names == extractor_names
    assert fd.params == {}

    extractor_names = ['test', 'youtube']
    fd = FragmentFD(CacheClass(None, None, None), None, None, extractor_names, False)
    assert fd.FD_NAME == 'test'
    assert fd.extractor_names == extractor_names
    assert fd.params == {}

# Generated at 2022-06-14 15:41:36.190422
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .youtube_dl.extractor.common import InfoExtractor
    from .youtube_dl.YoutubeDL import YoutubeDL

    class DummyIE(InfoExtractor):
        pass

    ie = DummyIE('http://www.youtube.com/watch?v=BaW_jenozKc')
    ie.add_info_extractor(lambda i: i.setdefault('fragment_count', 100))
    ydl = YoutubeDL({'writedescription': True, 'writeinfojson': True})
    fd = FragmentFD(ydl, ie, {})

# Generated at 2022-06-14 15:41:43.849046
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor
    from ..downloader.http import HttpFD
    from ..downloader.external import ExternalFD

    class MockInfoExtractor(object):
        IE_NAME = 'mock'
        IE_DESC = 'mock info extractor'

        def __init__(self, downloader):
            assert downloader is not None

    ie = get_info_extractor(MockInfoExtractor.IE_NAME)
    ie.__class__ = MockInfoExtractor
    ie.suitable = lambda *args: True
    ie.extract = lambda *args: None
    ie.downloader = HttpFD(None)

    fd = FragmentFD(ie.downloader, ie)
    assert fd.ied is ie
    assert fd.downloader is ie.downloader
   

# Generated at 2022-06-14 15:41:47.375269
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # pylint: disable=protected-access
    assert HttpQuietDownloader._FD_NAME == 'HttpQuiet'

# Generated at 2022-06-14 15:41:47.908245
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    pass

# Generated at 2022-06-14 15:43:10.483304
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import youtube_dl.YoutubeDL
    import youtube_dl.FileDownloader
    ydl = youtube_dl.YoutubeDL({})
    fd = youtube_dl.FileDownloader(ydl)
    qdl = HttpQuietDownloader(fd, {})
    assert qdl.ydl == ydl
    assert qdl.params == {}

# Generated at 2022-06-14 15:43:21.491032
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFragmentFD(FragmentFD):
        def __init__(self, params):
            self.params = params

    test_fd = TestFragmentFD({
        'keep_fragments': False,
        'retries': 10,
        'skip_unavailable_fragments': True,
        'test': False,
    })
    assert not test_fd.params.get('keep_fragments')
    assert isinstance(test_fd.params.get('retries', 0), int) and test_fd.params['retries'] == 10
    assert isinstance(test_fd.params.get('skip_unavailable_fragments', False), bool)
    assert test_fd.params['skip_unavailable_fragments']
    assert not test_fd.params['test']

# Generated at 2022-06-14 15:43:25.248052
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # it should throw exception 'AssertionError'
    # because it is not possible to instantiate abstract class
    try:
        FragmentFD('youtube-dl', {})
    except AssertionError:
        pass

# Generated at 2022-06-14 15:43:36.392169
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    ht = HttpQuietDownloader(None)
    assert ht.to_screen == HttpFD.to_screen
    assert ht.report_destination == HttpFD.report_destination
    assert ht.report_progress == HttpFD.report_progress
    assert ht.report_resuming_byte == HttpFD.report_resuming_byte
    assert ht.report_retry == HttpFD.report_retry
    assert ht.report_file_already_downloaded == HttpFD.report_file_already_downloaded
    assert ht.report_unable_to_resume == HttpFD.report_unable_to_resume
    assert ht.report_finish == HttpFD.report_finish
    assert ht

# Generated at 2022-06-14 15:43:44.240477
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def test_instance(params, test_name):
        print('Testing %s' % test_name)
        fd = FragmentFD(params, DummyYDL())
        assert fd.params == params
        assert fd.progress_hooks == []
        assert fd.name == test_name

    params = {
        'continuedl': True,
        'noprogress': True,
        'retries': 10,
        'ratelimit': None,
    }
    test_instance(params, 'HlsFD')


# Generated at 2022-06-14 15:43:48.764720
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    params = {'noprogress': True, 'quiet': True, 'foo': 'bar'}
    dl = HttpQuietDownloader(None, params)
    assert dl.params['noprogress'] == True
    assert 'quiet' not in dl.params
    assert dl.params['foo'] == 'bar'



# Generated at 2022-06-14 15:44:01.441423
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import unittest
    import sys
    from collections import namedtuple
    from io import BytesIO

    from .extractor import get_info_extractor
    from .downloader.rtmp import RtmpFD

    TestCase = namedtuple('TestCase', ['name', 'f4m_entry', 'expectation', 'setup'])


# Generated at 2022-06-14 15:44:10.006019
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable = missing-docstring
    import sys

    class DummyYDL(object):
        def __init__(self):
            self.params = {
                'ratelimit': None,
                'retries': 0,
                'nopart': False,
                'test': False,
            }

        def to_screen(self, msg):
            print(msg)

    ydl = DummyYDL()
    fd = FragmentFD(ydl, {
        'fragment_retries': 10,
        'keep_fragments': True,
        'noprogress': True,
    })

    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from StringIO import StringIO
    out = StringIO()

# Generated at 2022-06-14 15:44:16.319880
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=W0612
    from .fragment import FragmentFD
    from .downloader import YoutubeDL
    ydl = YoutubeDL({})
    fd = FragmentFD(ydl)
    assert not fd._is_running
    assert fd._progress_hooks == []
    assert fd._progress_hooks_lock.locked()
    assert fd._hook_download_lock.locked()

if __name__ == '__main__':
    # pylint: disable=E0602
    import unittest
    unittest.main()

# Generated at 2022-06-14 15:44:26.090111
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    from .extractor import get_info_extractor

    # test no downloader
    ie = InfoExtractor('dummy')
    ie._downloader = None
    ie._downloader_for_fs = None
    ie.http_downloader = None
    ie.http_proxy = None
    ie.http_headers = None
    ie.http_query = None
    ie.http_reason = None
    ie.ext = 'mp3'
    ie._prepare_and_start_frag_download = lambda ctx: None
    ie._finish_frag_download = lambda ctx: None
    ie._download_fragment_retry = lambda ctx, frag_url: (None, None)
    ie.report_warning = lambda message: None
    ie.report