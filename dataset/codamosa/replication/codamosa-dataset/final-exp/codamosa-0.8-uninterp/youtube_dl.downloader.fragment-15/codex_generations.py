

# Generated at 2022-06-14 15:37:50.398679
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import DownloadError
    from .http import HttpFD
    from .http import ytdl
    from .http import download_json
    from .http import std_headers

    class DummyYoutubeDL(object):
        def __init__(self):
            self.params = {}

        def to_screen(self, *args, **kargs):
            pass

        def trouble(self, *args, **kargs):
            pass

        def report_warning(self, *args, **kargs):
            pass

        def report_error(self, *args, **kargs):
            pass

    class DummyFD(object):
        def __init__(self):
            self.ydl = DummyYoutubeDL()

        def report_error(self, *args, **kargs):
            pass


# Generated at 2022-06-14 15:37:54.104288
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = {'noprogress': True, 'postprocessors': [],
           'progress_hooks': [], 'params': {}}
    hd = HttpQuietDownloader(ydl, {'quiet': True, 'noprogress': True})
    assert hd.params['quiet']
    assert 'quiet' in hd.params

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:38:02.964639
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    try:
        from collections import OrderedDict
    except ImportError:
        OrderedDict = dict

    class YDL:
        def __init__(self):
            self.params = OrderedDict()

    class Dummy:
        def __init__(self):
            self.ydl = YDL()

    Dummy().ydl.params['continuedl'] = True
    Dummy().ydl.params['quiet'] = True
    Dummy().ydl.params['noprogress'] = True

    assert True

# Generated at 2022-06-14 15:38:13.757944
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from youtube_dl.YoutubeDL import YoutubeDL
    from .http import HttpFD
    from .common import FileDownloader
    ydl = YoutubeDL({
        'quiet': False,
        'verbose': False,
        'outtmpl': '%(id)s.part',
    })
    assert isinstance(ydl, YoutubeDL)
    assert isinstance(ydl.params, dict)
    assert ydl.params['outtmpl'] == '%(id)s.part'
    assert isinstance(ydl.fd, FileDownloader)
    assert isinstance(ydl.fd, HttpFD)
    assert ydl.fd.params == ydl.params
    assert ydl.fd.ydl == ydl
    assert isinstance(ydl.fd.report_destination, object)


# Generated at 2022-06-14 15:38:18.302108
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Check that HttpQuietDownloader has all attributes of HttpFD
    assert hasattr(HttpQuietDownloader, 'report_error')
    assert hasattr(HttpQuietDownloader, 'trouble')



# Generated at 2022-06-14 15:38:19.595717
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    FD = FragmentFD({'format': 'mp4'})
    assert type(FD) == FragmentFD

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:38:20.929543
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    # It should not raise any exception
    FragmentFD(InfoExtractor(), {}).report_warning('Warning message')

# Generated at 2022-06-14 15:38:22.701539
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    assert fd is not None

# Generated at 2022-06-14 15:38:34.727677
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .downloader import Downloader
    from .http import HttpFD
    from .rtmp import RtmpFD

    # dummy methods
    def report_destination(self, filename, *args, **kargs):
        pass

    def to_screen(self, *args, **kargs):
        pass

    def hooked_to_screen(self, *args, **kargs):
        pass

    # monkey patching
    Downloader.report_destination = report_destination
    Downloader.to_screen = to_screen
    Downloader.hooked_to_screen = hooked_to_screen
    HttpFD._real_download = lambda self, filename, info_dict: True
    RtmpFD._real_download = lambda self, filename, info_dict: True


# Generated at 2022-06-14 15:38:39.140926
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = HttpQuietDownloader({'quiet': True, 'noprogress': True})
    assert not (ydl.params.get('quiet') and ydl.params.get('progress_with_newline') and ydl.params.get('noprogress'))

# Generated at 2022-06-14 15:38:59.092212
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    assert fd is not None

# Generated at 2022-06-14 15:39:06.644771
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor.common import InfoExtractor
    class TestIE(InfoExtractor):
        _VALID_URL = r'^https?://.+'
        _TEST = {
            'url': 'http://example.com/video.mp4',
        }
        def _real_extract(self, url):
            return self.playlist_result([{
                'url': 'http://example.com/video.mp4',
            }], playlist_title=None)

    ydl = YoutubeDL({'quiet': True, 'simulate': True})
    ydl.add_info_extractor(TestIE())
    ydl.download(['http://example.com/video.mp4'])

# Generated at 2022-06-14 15:39:09.314453
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    fd.to_screen = lambda *args: None
    fd._prepare_frag_download({'filename': 'x', 'total_frags': 1})

# Generated at 2022-06-14 15:39:21.660889
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import copy

    class MyFragFD(FragmentFD):
        def __init__(self, ydl, params):
            super(MyFragFD, self).__init__(ydl, params)
            self.orig_params = copy.deepcopy(params)
            self.Parameters = {}
            self.Parameters['live'] = False
            self.Parameters['fragment_index'] = 0
            self.Parameters['total_frags'] = 5
            self.Parameters['complete_frags_downloaded_bytes'] = 0
            self.Parameters['tmpfilename'] = '/tmp/file.ts'
            self.Parameters['filename'] = '/home/user/file.ts'

        def to_screen(self, *args, **kargs):
            print(args, kargs)


# Generated at 2022-06-14 15:39:28.656994
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from collections import namedtuple
    from io import BytesIO

    FakeYdl = namedtuple('FakeYdl', ['params'])
    ydl = FakeYdl({'outtmpl': 'filename'})
    dl = HttpQuietDownloader(ydl, {})

    assert dl.ydl is ydl
    assert dl.params == ydl.params
    assert dl.req == {}

    dl = HttpQuietDownloader(ydl, {'cookiefile': 'x'})

    assert dl.req == {}

    dl = HttpQuietDownloader(ydl, {'cookies': {'x': 'y'}})

    assert dl.req == {'cookies': {'x': 'y'}}


# Generated at 2022-06-14 15:39:36.642315
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import StringIO

    from .http import HttpFD

    # Python 2.6 doesn't support assigning to sys.stdout from a class
    # constructor, so we need to monkey-patch it here.

    sys.stdout = StringIO.StringIO()
    dl = HttpQuietDownloader(None, {'noprogress': True})
    assert sys.stdout.getvalue() == ''
    dl = HttpFD(None, {'progress_with_newline': True})
    assert sys.stdout.getvalue() == ''

# Generated at 2022-06-14 15:39:45.691764
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import gen_extractors
    youtube_dl = gen_extractors()
    # For this test we need the 'youtube' extractor
    youtube_dl.add_info_extractor(youtube_dl.get_info_extractor('Youtube'))
    try:
        youtube_dl.download(['ytsearch:test'])
        # This should raise an exception since we didn't setup anything
        raise AssertionError
    except SystemExit:
        pass

# Generated at 2022-06-14 15:39:55.014815
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    """Ensure that FragmentFD always gets the required params in opts"""
    import inspect
    import copy

    # The constructor of the super class FileDownloader accepts only these params
    super_constructor_params = inspect.getargspec(FileDownloader.__init__).args

    def create_downloader(opts):
        class DummyFragmentFD(FragmentFD):
            def __init__(self, ydl, params):
                super(DummyFragmentFD, self).__init__(ydl, params)

        params = copy.deepcopy(opts)

# Generated at 2022-06-14 15:40:04.797857
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        def report_retry_fragment(self, *args, **kargs):
            pass
        def _download_fragment(self, *args, **kargs):
            return True, 'content'

    def get_info_dict(*args, **kargs):
        return {'http_headers': {}}

    class TestYDL():
        def __init__(self):
            self.params = {}
        def to_screen(self, *args, **_kargs):
            pass

    test_ydl = TestYDL()
    test_fd = TestFD(test_ydl, {'outtmpl': '%(id)s.%(ext)s', 'restrictfilenames': True})

# Generated at 2022-06-14 15:40:18.099840
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import unittest
    import tempfile
    import shutil
    import sys
    import warnings
    from io import BytesIO

    class MockYDL(object):
        def __init__(self, *args, **kwargs):
            pass

        def to_screen(self, msg):
            pass

        def to_stdout(self, msg):
            pass

        def trouble(self, msg, tb=None):
            pass

        def report_warning(self, msg):
            warnings.warn(msg)

    class MockFD(FileDownloader):
        FD_NAME = 'test'

        def temp_name(self, filename):
            return filename + '.tmp'


# Generated at 2022-06-14 15:41:02.635566
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..compat import compat_urllib_error
    from ..extractor import YoutubeIE
    from ..downloader import HttpFD

    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    content = b'foobar'
    ie = YoutubeIE()
    info = ie.extract(url)
    dl = HttpQuietDownloader(None, {'noprogress': True})
    filename = dl.temp_name(info['id'])

    class MyHttpFD(HttpFD):
        def real_download(self, filename, info_dict):
            f, _ = sanitize_open(filename, 'wb')
            try:
                f.write(content)
            finally:
                f.close()


# Generated at 2022-06-14 15:41:14.874973
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # pylint: disable=W0212
    import tempfile
    class MyFD(FragmentFD):
        def __init__(self, ydl, params):
            FragmentFD.__init__(self, ydl, params)
            self.tmpfilename = tempfile.mkstemp()[1]

    params = {
        'keep_fragments': True,
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }
    ydl = object()
    myfd = MyFD(ydl, params)
    # If a constructor doesn't throw exception then we're OK
    # (isn't it?)
    assert myfd.params == params
    assert myfd.ydl is ydl
    assert myfd.tmpfilename != '-'
    assert os.path

# Generated at 2022-06-14 15:41:23.384322
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor
    from ..downloader.f4m import F4mFD
    from ..downloader.hls import HlsFD
    from .dash import DashSegmentsFD
    from .m3u8 import M3u8FD
    from .http import HttpFD
    from .rtmp import RtmpFD
    from .httpserver import Server
    from .ffmpegmux import MuxFD
    from .concat import ConcatFD
    from .external import ExternalFD
    from .fragment import FragmentFD

    IEs = [
        'youtube',
    ]


# Generated at 2022-06-14 15:41:31.780418
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    filename = 'testvideo.flv'
    u = FragmentFD('testvideo.flv', {})
    assert os.path.join(os.getcwd(), filename) == u.filename
    assert 'Frag' in u.temp_name(filename)
    assert 'testvideo.flv.ytdl' == u.ytdl_filename(filename)
    assert isinstance(u.extra_info_dict, dict)

    u = FragmentFD(filename, {})
    assert os.path.join(os.getcwd(), filename) == u.filename
    assert 'Frag' in u.temp_name(filename)
    assert 'testvideo.flv.ytdl' == u.ytdl_filename(filename)
    assert isinstance(u.extra_info_dict, dict)

# Generated at 2022-06-14 15:41:37.671794
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor

    # extractor_key is set to prevent
    # "WARNING: Unable to extract uploader nickname"
    class TestInfoExtractor(get_info_extractor('Test')):
        def real_extract(self, url):
            self.extractor_key = 'test'

            class TestFragmentFD(FragmentFD):
                FD_NAME = 'testfd'
                def process_info(self, info_dict):
                    # All info_dict related code is invoked in the constructor
                    # of FragmentFD.
                    # This method is intended for overriding by
                    # subclasses in order to add extra functionality.
                    pass

# Generated at 2022-06-14 15:41:44.498942
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert hasattr(FragmentFD, 'to_screen')
    assert hasattr(FragmentFD, 'report_retry_fragment')
    assert hasattr(FragmentFD, 'report_skip_fragment')
    assert hasattr(FragmentFD, '_prepare_url')
    assert hasattr(FragmentFD, '_prepare_and_start_frag_download')
    assert hasattr(FragmentFD, '__do_ytdl_file')
    assert hasattr(FragmentFD, '_read_ytdl_file')
    assert hasattr(FragmentFD, '_write_ytdl_file')
    assert hasattr(FragmentFD, '_download_fragment')
    assert hasattr(FragmentFD, '_append_fragment')

# Generated at 2022-06-14 15:41:57.737910
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    from ..postprocessor import FFmpegMergerPP
    from ..compat import compat_str


# Generated at 2022-06-14 15:42:02.020574
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from . import YoutubeDL
    from .extractor.common import InfoExtractor
    class DummyIE(InfoExtractor):
        IE_NAME = 'dummy'
        _VALID_URL = r'.*'
        def _real_extract(self, url):
            return {}
    ie = DummyIE(YoutubeDL({}))
    obj = FragmentFD(ie, {}, 'fake-id')

# Generated at 2022-06-14 15:42:14.147318
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class _FragmentFD(FragmentFD):
        def __init__(self, *args, **kargs):
            self.to_screen_values = []
            self.report_warning_values = []
            FragmentFD.__init__(self, *args, **kargs)

        def to_screen(self, *args, **kargs):
            self.to_screen_values.append((args, kargs))

        def report_warning(self, *args, **kargs):
            self.report_warning_values.append((args, kargs))

        def _hook_progress(self, *args, **kargs):
            pass

        def temp_name(self, *args, **kargs):
            return 'test-filename'

        def ytdl_filename(self, *args, **kargs):
            return

# Generated at 2022-06-14 15:42:26.351677
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import get_info_extractor

    # This function is used to test HttpQuietDownloader only.
    # We don't need it to fail on any errors.
    def fail_hard(self, *args, **kargs):
        assert False, 'Fail hard'

    class MockYoutubeDL(object):
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
            self.to_screen = fail_hard

        def add_default_extra_info(self, *args, **kargs):
            return


# Generated at 2022-06-14 15:43:54.770831
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def my_hook(s):
        assert False, 'my_hook should not be invoked'

    params = {
        'quiet': True,
        'noprogress': True,
        'continuedl': True,
    }
    dl = HttpQuietDownloader(None, params)
    dl.add_progress_hook(my_hook)
    dl.to_screen('some message')


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:44:05.477948
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from . import YoutubeDL
    from .extractor.youtube import YoutubeIE

    def _hook(status):
        print(status)

    ydl = YoutubeDL({
        'quiet': True,
        'logger': YoutubeDL.logger_class('test', True),
    })
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(YoutubeIE.ie_key())
    dl = HttpQuietDownloader(ydl, {
        'continuedl': True,
        'quiet': True,
        'logger': ydl._LoggerClass('test2', True),
        'noprogress': True,
        'ratelimit': 40000,
        'retries': 4,
        'nopart': True,
        'test': True,
    })


# Generated at 2022-06-14 15:44:11.180113
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class DummyYDL(object):
        def __init__(self):
            self.params = {'verbose': True}

    ydl = DummyYDL()
    hd = HttpQuietDownloader(ydl, {'noprogress': True, 'quiet': True})
    assert not hd._opts['verbose']
    assert hd._ydl.params['verbose']

# Generated at 2022-06-14 15:44:16.919572
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = MockYoutubeDL()
    params = {'quiet': True, 'noprogress': True}
    hd = HttpQuietDownloader(ydl, params)
    assert hd.ydl == ydl
    assert hd.params == params


# Generated at 2022-06-14 15:44:20.954703
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ydl = object()
    params = {
        'fragment_retries': 5,
    }
    fragFD = FragmentFD(ydl, params)
    assert fragFD.params == params
    assert fragFD.ydl == ydl

# Generated at 2022-06-14 15:44:26.836903
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    fd = FragmentFD(sys.modules['__main__'])
    assert not fd.params.get('noprogress')
    assert fd.params.get('continuedl')
    assert fd.params.get('nopart')
    assert not fd.params.get('ratelimit')
    assert fd.params.get('retries') is None
    assert fd.params.get('noprogress')
    assert not fd.params.get('keepfragments')

# Generated at 2022-06-14 15:44:29.502850
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    sys.stderr = sys.stdout
    HttpQuietDownloader(
        None,
        {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'retries': 0,
            'nopart': False,
            'test': False,
        }
    )

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:44:34.692248
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor

    class FakeInfoDict(dict):
        def __init__(self, data):
            self.data = data
            dict.__init__(self)
        def __getattr__(self, key):
            return self.data.get(key)

    # extractor_name - name of extractor class or None
    # err_expected - expected error
    # err_msg - error message substring expected in exception
    # extractor_config - custom configuration for an extractor
    TestCase = collections.namedtuple('TestCase',
                                      'extractor_name err_expected err_msg extractor_config')

# Generated at 2022-06-14 15:44:46.072141
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    gen_extractors()
    # First parameter is a youtube-dl object
    # Second parameter is a dictionary of options
    dl = HttpQuietDownloader(None,
                             {
                                 'continuedl': True,
                                 'noprogress': True,
                                 'quiet': True,
                                 'nopart': True,
                                 'ratelimit': 'nolimit',
                                 'retries': 10,
                             })
    assert dl
    # Test if dl has the correct options set
    assert dl.params['continuedl']
    assert dl.params['noprogress']
    assert dl.params['quiet']
    assert dl.params['nopart']

# Generated at 2022-06-14 15:44:52.396770
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def test_param(args, value):
        assert args['quiet']
        assert args['noprogress']
        assert args['params']['key'] == value

    from .http import HttpDownloader
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL({'key': 'value'})
    dl = HttpQuietDownloader(ydl, {'key': 'value'})
    dl._setup_opener(test_param)

if __name__ == '__main__':
    test_HttpQuietDownloader()