

# Generated at 2022-06-14 15:37:57.348374
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor

    fd = FragmentFD({}, {},
        get_info_extractor('test'),
        'http://localhost:8080/test.f4m')
    assert fd.params['fragment_retries'] == 10
    assert not fd.params['skip_unavailable_fragments']
    assert not fd.params['keep_fragments']

    fd = FragmentFD({}, {},
        get_info_extractor('test'),
        'http://localhost:8080/test.f4m',
        fragment_retries=2)
    assert fd.params['fragment_retries'] == 2


# Generated at 2022-06-14 15:38:02.918686
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import unittest
    from types import ModuleType
    from ..compat import compatibility_str

    m = ModuleType(__name__)
    # silence pyflakes
    m.FileDownloader = FileDownloader
    sys.modules[__name__] = m

    from . import _FragmentFD

    class FragmentFDTest(unittest.TestCase):
        def setUp(self):
            self.test_fd = _FragmentFD.FragmentFD(None)

        def test_ytdl_filename(self):
            self.assertEqual(self.test_fd.ytdl_filename('foo'), 'foo.ytdl')
            self.assertEqual(self.test_fd.ytdl_filename('foo.bar'), 'foo.bar.ytdl')
            self.assertE

# Generated at 2022-06-14 15:38:11.802569
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from .common import FileDownloader
    from .extractor import gen_extractors
    print('Testing FileDownloader with HttpQuietDownloader')

# Generated at 2022-06-14 15:38:25.311315
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert hasattr(FragmentFD(None, None), 'report_retry_fragment')
    assert hasattr(FragmentFD(None, None), 'report_skip_fragment')
    assert hasattr(FragmentFD(None, None), '_prepare_url')
    assert hasattr(FragmentFD(None, None), '_prepare_and_start_frag_download')
    assert hasattr(FragmentFD(None, None), '_download_fragment')
    assert hasattr(FragmentFD(None, None), '_append_fragment')
    assert hasattr(FragmentFD(None, None), '_prepare_frag_download')
    assert hasattr(FragmentFD(None, None), '_start_frag_download')

# Generated at 2022-06-14 15:38:35.913417
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    fd = HttpQuietDownloader(
        None,
        {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'ratelimit': 0,
            'retries': 0,
            'nopart': True,
            'test': True,
        })
    assert fd.params['continuedl'] is True
    assert fd.params['quiet'] is True
    assert fd.params['noprogress'] is True
    assert fd.params['ratelimit'] == 0
    assert fd.params['retries'] == 0
    assert fd.params['nopart'] is True
    assert fd.params['test'] is True

# Generated at 2022-06-14 15:38:42.473501
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    dl = HttpQuietDownloader(
        None, {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'ratelimit': None,
            'retries': 0,
            'nopart': False,
            'test': False,
        }
    )
    assert dl.params['noprogress']

# Generated at 2022-06-14 15:38:43.183064
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    pass

# Generated at 2022-06-14 15:38:54.926158
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import unittest
    from .common import FileDownloader
    from .http import HttpFD

    class MyFileDownloader(HttpQuietDownloader):
        def __init__(self, ydl, params):
            super(MyFileDownloader, self).__init__(ydl, params)
            self.to_screen_count = 0
            self.to_stderr_count = 0

        def to_screen(self, *args, **kargs):
            self.to_screen_count += 1

        def to_stderr(self, *args, **kargs):
            self.to_stderr_count += 1


# Generated at 2022-06-14 15:39:05.232589
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    sys.stderr = sys.stdout
    fd = FragmentFD()
    assert fd.FD_NAME == 'fragment'
    assert fd.params.get('retries') is not None
    assert fd.params.get('skip_unavailable_fragments') is not None
    assert fd.params.get('fragment_retries') is not None
    assert fd.temp_name('abc') == 'abc.part'

    assert fd.ytdl_filename('abc') == 'abc.ytdl'
    assert os.path.splitext(fd.ytdl_filename('abc.mp4'))[0] == 'abc.mp4.ytdl'

    assert fd.calc_eta(1, 1.5, 60, 30) == 30

# Generated at 2022-06-14 15:39:05.757410
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert True

# Generated at 2022-06-14 15:39:34.914319
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MockYDL():
        params = {}
        def __init__(self):
            self.my_dir = os.path.dirname(os.path.abspath(__file__))
        def temp_name(self, *args):
            return os.path.join(self.my_dir, *args)
    ydl = MockYDL()
    fd = FragmentFD(ydl, {'continuedl': True})
    fd.add_progress_hook(lambda d: None)
    # temp_name is not used in _prepare_frag_download
    fd._prepare_frag_download({
        'filename': 'test.ts',
        'tmpfilename': '-'
    })

# Generated at 2022-06-14 15:39:41.520968
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(None)
    assert fd.ydl is None
    assert fd.params == {}
    assert fd.info_dicts == []
    assert fd.outtmpl == ''
    assert fd.percent_str() == '0.0%'
    assert fd.FD_NAME == 'generic'
    assert fd.ytdl_filename('abc') == 'abc.ytdl'
    assert fd.temp_name('abc') == 'abc.part'


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:39:48.610979
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ydl = object()
    params = {
        'keep_fragments': True,
        'retries': 2,
        'socket_timeout': 30,
    }
    fd = FragmentFD(ydl, params)
    assert fd.params == params
    assert fd.ydl == ydl
    assert fd.retries == params['retries']
    assert fd.troubleshooting == False
    assert fd.done == False

# Generated at 2022-06-14 15:39:52.396347
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD('youtube-dl', {})
    init_dict = {}
    fd._prepare_frag_download(init_dict)
    assert init_dict
    fd.to_screen('FragmentFD init test finished')

# Generated at 2022-06-14 15:39:58.250697
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor
    ydl = gen_extractor({'logger': None})
    qd = HttpQuietDownloader(ydl, {'continuedl': True})
    assert qd.ydl is ydl
    assert qd.params['continuedl']


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:40:03.910505
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def unit_test(self, *args, **kargs):
        pass
    instance = HttpQuietDownloader(None, {'continuedl': True, 'retries': 1})
    assert instance.params['continuedl']
    assert instance.params['retries'] == 1
    assert instance.to_screen == unit_test

# Generated at 2022-06-14 15:40:17.265627
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import unittest
    import tempfile
    import shutil
    import sys

    class TestFragmentFD(unittest.TestCase):
        SNAME = 'youtube-dl'
        TDIR = tempfile.mkdtemp(prefix='%s-' % SNAME)
        SFILE = os.path.join(TDIR, '%s.sock' % SNAME)

        def setUp(self):
            self.filedl = FragmentFD({}, {}, {})

        def tearDown(self):
            if os.path.exists(self.SFILE):
                os.remove(self.SFILE)
            shutil.rmtree(self.TDIR)

        def test_temp_name(self):
            f = self.filedl.temp_name(self.SNAME)
            self.assertE

# Generated at 2022-06-14 15:40:28.399076
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    """
    This function tests if the HttpQuietDownloader constructor
    throws an exception for invalid URLs and for valid URLs
    it checks if the created object is of type HttpQuietDownloader
    """
    from .http import HttpFD

    invalid_urls = [
        '', None, 'sftp://www.example.com/', 'ftp://ftp.example.com/']
    valid_urls = [
        'http://www.example.com/', 'https://www.example.com/',
        'https://www.example.com/test.mp4',
        'http://user:password@www.example.com/']
    ydl = object()
    dl_opts = {'quiet': True}

# Generated at 2022-06-14 15:40:34.809600
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .downloader import YoutubeDL
    from .extractor import get_info_extractor
    from .extractor.common import InfoExtractor

    class TestIE(InfoExtractor):
        IE_NAME = 'test1'
        _VALID_URL = r'https?://.+'

        def _real_extract(self, url):
            return {
                'id': 'test',
                'url': url,
            }

    ie = get_info_extractor(TestIE.IE_NAME)
    ie.add_info_extractor(TestIE)
    ydl = YoutubeDL({'quiet': True, 'noprogress': True})

# Generated at 2022-06-14 15:40:44.468353
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    try:
        from collections import OrderedDict
    except ImportError:
        OrderedDict = dict

    params = OrderedDict([
        ('continuedl', True),
        ('quiet', True),
        ('noprogress', True),
        ('ratelimit', 1024),
        ('retries', 16),
        ('nopart', True),
        ('test', True),
    ])
    http_dl = HttpQuietDownloader(None, params)
    assert http_dl.params == params

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:41:28.964128
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from . import YoutubeDL
    from .extractor.common import InfoExtractor

    ydl = YoutubeDL(params={'noplaylist': True})
    ydl.add_info_extractor(InfoExtractor('test'))
    dl = HttpQuietDownloader(ydl, {'continuedl': True, 'quiet': True, 'noprogress': True})
    s = dict()
    dl.to_screen('TEST', s)
    assert (s['_total_bytes_str'] == 'TEST'), 'Test failed!'


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:41:30.881848
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ydl = {}
    params = {}
    fd = FragmentFD(ydl, params)
    assert fd.params == params
    assert fd.ydl == ydl

# Generated at 2022-06-14 15:41:32.486778
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader
    FileDownloader(None, None)

# Generated at 2022-06-14 15:41:36.476200
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    downloader = FragmentFD({})
    assert downloader.params == {
        'keep_fragments': False,
        'fragment_retries': 10,
        'skip_unavailable_fragments': False,
    }
    assert downloader.ydl is None

# Generated at 2022-06-14 15:41:41.153149
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert (
        HttpQuietDownloader(
            None,
            {
                'continuedl': True,
                'quiet': True,
                'noprogress': True,
                'ratelimit': 1,
                'retries': 0,
                'nopart': False,
                'test': False,
            }
        )
        is not None
    )

# Generated at 2022-06-14 15:41:46.301039
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'retries': 10,
        'ratelimit': None,
    }
    dl = HttpQuietDownloader(ydl, {'continuedl': True})
    assert isinstance(dl, HttpFD)
    assert dl.params == ydl

# Generated at 2022-06-14 15:41:54.335140
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def _test_assert_ytdl_file(fname, ytdl_file, state):
        if not ytdl_file:
            assert not os.path.isfile(encodeFilename(fname + '.ytdl'))
            return
        assert os.path.isfile(encodeFilename(fname + '.ytdl'))
        stream, _ = sanitize_open(fname + '.ytdl', 'r')
        try:
            ytdl_state = json.loads(stream.read())['downloader']
            assert ytdl_state['current_fragment']['index'] == state['fragment_index']
            assert ytdl_state['fragment_count'] == state['fragment_count']
        except Exception:
            assert False
        finally:
            stream

# Generated at 2022-06-14 15:42:02.910673
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    from collections import defaultdict
    result = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
    fd = FragmentFD(None, defaultdict(str), defaultdict(str))
    fd.to_screen = lambda *args, **kargs: result['to_screen'][args[0]][args[1]]
    fd.report_retry_fragment(
        'error', 10, 2, 1)
    assert (
        'Got server HTTP error: error. Retrying fragment 10 (attempt 2 of 1)...'
        == result['to_screen']['prefix']['status'])
    fd.report_retry_fragment(
        'error', 10, 2, 2)

# Generated at 2022-06-14 15:42:14.709573
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor import gen_extractors
    from ..postprocessor import gen_pp

    # Test downloader option
    ydl_opts = {
        'quiet': True,
    }
    ydl = YoutubeDL(ydl_opts)

    # Test extractor option
    info_dict = {}
    info_dict['extractor_key'] = 'test_extractor'
    info_dict['url'] = 'http://example.com'
    info_dict['http_headers'].update({'test_header': '123'})
    extractors = list(gen_extractors(ydl, info_dict=info_dict))

    # Test postprocessor option
    info_dict['duration'] = 1
    postprocessors = list(gen_pp(ydl, info_dict=info_dict))

    assert len

# Generated at 2022-06-14 15:42:26.689780
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import compat_urllib_request
    import youtube_dl

    def _download(ydl, url, filename, info_dict):
        dl = HttpQuietDownloader(ydl, {'quiet': True, 'noprogress': True})
        req = compat_urllib_request.Request(url, None)
        return dl.retrieve(req, filename, info_dict)

    # Real use case of HttpQuietDownloader
    class TestDownloader(FragmentFD):
        FD_NAME = 'testfrag'

        def real_download(self, filename, info_dict):
            data = info_dict['url']
            start = time.time()
            filepath = self.temp_name(filename)

# Generated at 2022-06-14 15:43:56.116396
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # Test for https://github.com/rg3/youtube-dl/issues/7722
    # Must not raise an exception when the fragment_retries option is missing
    FragmentFD(None, {})

# Generated at 2022-06-14 15:44:02.250739
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import youtube_dl
    ydl = youtube_dl.YoutubeDL({'quiet': True})
    x = FragmentFD(ydl, {'format': 'm4a', 'noprogress': True})
    assert sys.getrefcount(x) == 2
    del x
    assert sys.getrefcount(ydl) == 1
    del ydl


# Generated at 2022-06-14 15:44:05.980560
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD.__bases__ == (FileDownloader,)
    assert hasattr(FragmentFD, '_prepare_frag_download')
    assert hasattr(FragmentFD, '_start_frag_download')

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:44:08.960007
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = object()
    params = {'continuedl': True}
    HttpQuietDownloader(ydl, params)

# Generated at 2022-06-14 15:44:11.944009
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader
    ydl = FileDownloader({'quiet': True})
    dl = HttpQuietDownloader(ydl, {'continuedl': True})
    assert dl._ydl is ydl

# Generated at 2022-06-14 15:44:24.101145
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class MyFD(FileDownloader):
        def report_destination(self, filename):
            print('Destination: %s' % filename)
        def temp_name(self, filename):
            return '%s.temp' % filename
    ydl = MyFD({})
    # (1) Test basic successful download
    hqd = HttpQuietDownloader(ydl, {'continuedl': True})
    d = hqd.download('http://www.example.com/', {'outtmpl': '/tmp/spam'})
    assert d is True
    assert os.path.isfile('/tmp/spam.temp')
    os.remove('/tmp/spam.temp')
    os.remove('/tmp/spam')
    # (2) Test file location
    hqd = HttpQu

# Generated at 2022-06-14 15:44:31.509410
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import tempfile
    sys.argv = 'youtube-dl -o "-".f4m'.split()
    fd = FragmentFD()
    info = dict(
        id='test',
        display_id='test',
        title='test',
        _filename='test',
        formats=[
            dict(format_id='1', url='url1', frag_index=1),
            dict(format_id='2', url='url2', frag_index=2, preference=1),
            dict(format_id='3', url='url3', preference=2),
        ],
    )
    def _hook(status):
        print(repr(status))
    fd._hooks = dict(progress=_hook)
    fd.params['test'] = True

# Generated at 2022-06-14 15:44:36.019177
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    ydl = object()
    params = {}
    http_fd = HttpQuietDownloader(ydl, params)
    assert http_fd.ydl is ydl
    assert http_fd.params is params
    assert isinstance(http_fd, HttpFD)

# Generated at 2022-06-14 15:44:46.935044
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from .common import FileDownloader
    from .http import HttpFD

    class DummyYDL(object):
        def __init__(self, params):
            self.params = params
            self.to_screen = lambda *args, **kargs: sys.stderr.write(
                ' '.join(map(compat_str, args)) + '\n')
            self.to_stdout = lambda s: sys.stdout.write(s + '\n')
            self.to_stderr = lambda s: sys.stderr.write(s + '\n')
            self.to_console_title = lambda *args: None
            self.process = lambda: None
            self.temp_name = lambda s: s
            self.fix_filename = lambda s: s
            self.report_

# Generated at 2022-06-14 15:44:56.265189
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor.youtube import YoutubeIE
    from ..compat import compat_urllib_error
    from ..compat import compat_urllib_request
    from ..utils import format_bytes

    def report_retry_fragment(self, err, frag_index, count, retries):
        print('Retrying fragment %d (attempt %d of %s)...' % (frag_index, count, self.format_retries(retries)))

    def report_skip_fragment(self, frag_index):
        print('Skipping fragment %d...' % frag_index)

    def __do_ytdl_file(ctx):
        return not ctx['live'] and not ctx['tmpfilename'] == '-'

    def _read_ytdl_file(self, ctx):
        stream,