

# Generated at 2022-06-14 15:37:51.256715
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import io

    class _YDL(object):
        def __init__(self, params):
            self.params = params
            self.to_stderr = lambda *a, **ka: None
            self.to_screen = self.to_stderr

    params = {
        'ratelimit': 1,
        'retries': 2,
        'nopart': True,
        'test': True,
    }
    ydl = _YDL(params)
    dl = HttpQuietDownloader(ydl, params)

    buf = io.BytesIO()
    sys.stdout = buf
    dl.to_screen('test')
    assert buf.getvalue() == b''
    buf.close()

    buf = io.BytesIO()
    sys.stdout = buf
   

# Generated at 2022-06-14 15:38:03.715127
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from . import YoutubeDL
    ydl = YoutubeDL()
    fd = FragmentFD(ydl)
    assert fd.ydl is ydl
    assert not fd.params['continuedl']
    assert not fd.params['quiet']
    assert not fd.params['noprogress']
    assert fd.params['nopart']
    assert fd.params['retries'] == 10
    assert not fd.params['ratelimit']
    assert not fd.params['noresizebuffer']
    assert fd.params['test'] == False
    assert fd.params['fragment_retries'] == 10
    assert not fd.params['skip_unavailable_fragments']
    assert not fd.params['keep_fragments']

# Generated at 2022-06-14 15:38:12.224195
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import hashlib
    from ..compat import compat_urllib_request
    if sys.version_info < (3, 0):
        import urlparse
    else:
        from urllib import parse as urlparse

    urlh = compat_urllib_request.urlopen(test_url)
    info = urlh.info()
    clen = int(info.get('Content-Length'))
    CHUNK = 16 * 1024
    data = compat_urllib_request.urlopen(test_url).read(CHUNK)

# Generated at 2022-06-14 15:38:25.806200
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import tempfile
    tmp_dir = tempfile.mkdtemp()
    os.chdir(tmp_dir)

    def _run_test(cmd, exp_output):
        # Testing FragmentFD constructor
        import youtube_dl.FileDownloader
        res_stream = youtube_dl.FileDownloader.open_file(cmd)

        # Compare output
        data = res_stream.read()
        lines = data.split()
        assert lines == exp_output

        # Cleanup
        res_stream.close()
        os.chdir(tmp_dir)
        for f in os.listdir('.'):
            os.remove(f)
        os.rmdir('.')


# Generated at 2022-06-14 15:38:36.979057
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor

    class DummyIE(object):
        def __init__(self, params):
            self.ydl = params['ydl']

    params = {
        'ydl': {
            'progress_hooks': [],
        }
    }
    d1 = DummyIE(params)
    fd1 = FragmentFD(d1, params)
    fd2 = FragmentFD(d1, params)
    assert fd2.ydl is fd1.ydl

    real_IE = get_info_extractor('youtube')
    params['ydl']['username'] = 'foo'
    params['ydl']['password'] = 'bar'
    yt_IE = real_IE(params)

# Generated at 2022-06-14 15:38:44.080077
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert(FragmentFD.__doc__ is not None)
    assert('FragmentFD' in repr(FragmentFD))

    ydl = object()
    params = {'y': 'yt', 'z': 'z'}
    test_inst = FragmentFD(ydl, params)
    assert(test_inst.ydl is ydl)
    assert(test_inst.params == params)

# Generated at 2022-06-14 15:38:55.683535
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .options import OptParseError
    import shutil
    import tempfile
    import stat

    opts = {
        'ignoreerrors': True,
        'continuedl': True,
        'ratelimit': '10240',
        'retries': '10',
        'fragment_retries': '10',
        'skip_unavailable_fragments': False,
        'keep_fragments': True,
        'noprogress': True,
        'quiet': True,
        'test': True,
    }

    fd = FragmentFD(None, opts)

    assert set(fd.params.keys()) == set(opts.keys())

    for k, v in opts.items():
        assert fd.params[k] == opts[k]

    tmp = tempfile.mk

# Generated at 2022-06-14 15:38:59.955525
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from youtube_dl.YoutubeDL import YoutubeDL
    h = HttpQuietDownloader(YoutubeDL(), {'continuedl': True})
    assert h.ydl is not None
    assert h.params['continuedl']

# Generated at 2022-06-14 15:39:04.093370
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    import types
    assert isinstance(HttpQuietDownloader('a', 'b', 'c'), HttpFD)
    assert HttpQuietDownloader.to_screen.im_self is None
    assert isinstance(HttpQuietDownloader.to_screen, types.UnboundMethodType)



# Generated at 2022-06-14 15:39:06.640957
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(None, {'noprogress': True})
    assert fd.params['noprogress'] is True
    assert fd.params.get('keepfragments', False) is False

# Generated at 2022-06-14 15:39:28.740613
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFragmentFD(FragmentFD):
        def report_retry_fragment(self, err, frag_index, count, retries):
            print('Test report_retry_fragment: %s %d %d %d' % (
                err, frag_index, count, retries))

        def report_skip_fragment(self, frag_index):
            print('Test report_skip_fragment: %d' % frag_index)

        def report_destination(self, filename):
            print('Test report_destination: %s' % filename)

        def temp_name(self, filename):
            return 'Test output'

        def try_rename(self, fromname, toname):
            print('Test try_rename: %s %s' % (fromname, toname))

       

# Generated at 2022-06-14 15:39:39.177582
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import io
    import sys

    from .http import HttpFD

    ydl = object()
    params = {'noprogress': True, 'quiet': True, 'logger': None}

    dl = HttpQuietDownloader(ydl, params)

    assert dl.ydl is ydl
    assert dl.params == params

    # Test quiet
    params['quiet'] = False
    dl = HttpQuietDownloader(ydl, params)
    assert dl.to_screen == HttpFD.to_screen

    # Test logger
    params['logger'] = object()
    # Make sure that logger's file is present
    logger = params['logger']
    logger.file = sys.stderr
    dl = HttpQuietDownloader(ydl, params)
    assert dl

# Generated at 2022-06-14 15:39:46.250310
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .common import FileDownloader
    fd = HttpFD({})
    assert isinstance(fd.ydl, FileDownloader)
    hqd = HttpQuietDownloader(fd, {})
    assert isinstance(hqd, HttpFD)
    assert isinstance(hqd.ydl, FileDownloader)
    assert hqd.ydl is fd.ydl

# Generated at 2022-06-14 15:39:52.304471
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    sys.path = sys.path[1:]
    from ytdl_core import YoutubeDL

    ydl = YoutubeDL()
    d = HttpQuietDownloader(ydl, {'quiet': False})
    assert not d.params['quiet']
    d = HttpQuietDownloader(ydl, {'quiet': True})
    assert d.params['quiet']

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:39:57.782245
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # pylint: disable=protected-access
    ydl = HttpQuietDownloader(None, None)
    assert ydl._progress_hooks == []
    HttpQuietDownloader(None, None, {'progress_hooks': []})

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:40:06.642778
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class DummyYDL:
        params = {}
    fd = FragmentFD(DummyYDL())
    assert fd.params == {
        'keep_fragments': False,
        'nopart': False,
        'retries': 0,
    }
    fd = FragmentFD(DummyYDL(), {'fragment_retries': 5})
    assert fd.params == {
        'keep_fragments': False,
        'nopart': False,
        'retries': 5,
    }

# Generated at 2022-06-14 15:40:19.777743
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import random

    class TestFD(FragmentFD):
        def __init__(self):
            self._hooks_progress = []
            self._retries = 0

        def add_progress_hook(self, hook):
            self._hooks_progress.append(hook)

        def download(self, filename, info_dict):
            while self._retries:
                self._retries -= 1
                return False
            self.report_destination(filename)
            return True

        def _hook_progress(self, state):
            for hook in self._hooks_progress:
                hook(state)

        def format_retries(self, retries):
            self._retries = retries
            return str(retries)

        def to_screen(self, message, skip_eol=False):
            pass


# Generated at 2022-06-14 15:40:27.046653
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class YDL(object):
        def __init__(self):
            self.params = {}
            self.to_screen = lambda s: None

    ydl = YDL()
    dl = HttpQuietDownloader(ydl, {'noprogress': True})
    assert dl.ydl is ydl
    assert dl.params == {'noprogress': True}
    assert dl.to_screen == ydl.to_screen



# Generated at 2022-06-14 15:40:37.010292
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import tempfile
    import shutil

    from .extractor import gen_extractors

    # Create temporary directory and save the old one for
    # restoring later
    temp_dir = tempfile.mkdtemp()
    old_dir = os.getcwd()
    os.chdir(temp_dir)

    # Output handler
    out = sys.stdout

    # Extractors for testing
    extractors = gen_extractors()
    extractors_names = set(list(extractors.keys()))
    extractors_names.add('generic')

    # Test extractors
    good_exts = []
    good_exts.append('youtube')
    good_exts.append('youtube:user')
    good_exts.append('youtube:playlist')

# Generated at 2022-06-14 15:40:40.817134
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    def test(ydl):
        assert isinstance(ydl, HttpQuietDownloader)

    downloader = FileDownloader({}, test)
    downloader.report_destination('dest')

# Generated at 2022-06-14 15:41:11.564305
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    fd.params['retries'] = 2
    fd.params['fragment_retries'] = 3
    assert fd.params['retries'] == 2
    assert fd.params['fragment_retries'] == 3

    fd = FragmentFD({'retries': 4})
    fd.params['fragment_retries'] = 3
    assert fd.params['retries'] == 4
    assert fd.params['fragment_retries'] == 3

    fd = FragmentFD({'fragment_retries': 4})
    fd.params['retries'] = 3
    assert fd.params['retries'] == 3
    assert fd.params['fragment_retries'] == 4


# Generated at 2022-06-14 15:41:16.135374
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .downloader import Downloader

    class FakeInfo:
        pass

    class FragmentFD_test(FragmentFD):
        def __init__(self, ydl, params):
            self.params = params
            self.ydl = ydl
            self.info = FakeInfo()
            self.info.url = 'http://foo.bar/'
            self.info.title = 'title'
            self.to_screen = lambda *args, **kargs: None
            FragmentFD.__init__(self, ydl, params)

    d = Downloader({})
    t = FragmentFD_test(d, {})
    t.report_error('foobar')
    assert d.params['outtmpl'] == '%(title)s-%(id)s.%(ext)s'

# Generated at 2022-06-14 15:41:24.288818
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor import gen_extractors
    from ..postprocessor import gen_pp
    from ..utils import DEFAULT_OUTTMPL
    valid_urls = [
        'https://github.com/rg3/youtube-dl/raw/master/LICENSE',
        'rtmp://blabla',
    ]
    invalid_urls = [
        'htttps://github.com/rg3/youtube-dl/raw/master/LICENSE',
        'https://www.youtube.com/watch?v=W8_KfJO3VjU'
    ]

# Generated at 2022-06-14 15:41:30.755521
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys

    class MyFragmentFD(FragmentFD):
        FD_NAME = 'myfragfd'

    class MyFragmentFD2(FragmentFD):
        FD_NAME = 'myfragfd2'

        def _prepare_frag_download(self, ctx):
            pass

        def _start_frag_download(self, ctx):
            pass

        def _finish_frag_download(self, ctx):
            pass

    assert MyFragmentFD().FD_NAME == 'myfragfd'
    assert MyFragmentFD2().FD_NAME == 'myfragfd2'
    assert FragmentFD().FD_NAME == 'fragment'
    fd = MyFragmentFD()
    fd.to_screen('foo')
    fd.report_warning('bar')


# Generated at 2022-06-14 15:41:41.058517
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import os
    import urllib
    import tempfile

    if sys.version_info < (2, 6):
        import unittest2 as unittest
    else:
        import unittest

    from .common import FileDownloader

    def urlopen(req):
        return urllib.urlopen(req)

    from .fragment import FragmentFD

    class TestInfoDict(dict):
        pass

    class TestDownloader(FileDownloader):
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params

        def to_stdout(self, s):
            pass

    class TestFragmentFD(FragmentFD):
        def __init__(self, ydl, params):
            self.ydl = ydl
           

# Generated at 2022-06-14 15:41:47.438474
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    params = {'test': True, 'quiet': True, 'retries': 5}
    ydl = object()
    dl = HttpQuietDownloader(ydl, params)
    assert dl.ydl is ydl
    assert dl.params is params
    assert dl.params['quiet'] is True
    assert dl.params['retries'] == 5
    assert dl.params['noprogress'] is True

# Generated at 2022-06-14 15:41:56.545772
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # pylint: disable=W0212
    test_params = {
        'continuedl': True,
        'noprogress': True,
        'retries': 10,
    }
    dl = HttpQuietDownloader(None, test_params)
    assert dl.params == test_params
    assert dl.ydl is None
    assert dl._progress_hooks == []
    assert dl._progress_hooks_descs == []
    for _, func in dl.progress_hooks.items():
        assert func == dl._generic_hook



# Generated at 2022-06-14 15:42:01.309773
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class FragmentFDTest(FragmentFD):
        FD_NAME = 'testfd'

    from .url import URL
    fdt = FragmentFDTest(URL('http://example.com/test.m3u8'))
    assert fdt.name == 'testfd'
    assert fdt.params['nopart'] is False


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:42:13.230067
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import io
    import sys
    import unittest

    # Arrange
    class TestFD(FragmentFD):
        def __init__(self):
            self.progress = None
            self.tmpfilenames = []
            self.filenames = []
        def to_screen(self, *args, **kargs):
            pass
        def report_warning(self, *args, **kargs):
            pass
        def report_destination(self, filename):
            self.filenames.append(filename)
        def temp_name(self, filename):
            tmpfilename = '-%d' % len(self.tmpfilenames)
            self.tmpfilenames.append(tmpfilename)
            return tmpfilename
        def _hook_progress(self, progress):
            self.progress = progress

# Generated at 2022-06-14 15:42:25.067029
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .smuggle import smuggle_url

    from .common import FileDownloader
    from .extractor import get_info_extractor
    FileDownloader.write_string = lambda *a: None

    query = smuggle_url(
        'https://www.youtube.com/watch?v=BgfcToAjfdc',
        {'extractor': 'youtube'})
    ie = get_info_extractor(query['extractor'])

    # Test default constructor
    d = HttpQuietDownloader(FileDownloader({}), query)
    assert d.params['quiet']
    assert d.params['noprogress']
    assert d.params['continuedl']

    # Test that quiet set to True overrides noprogress and continuedl

# Generated at 2022-06-14 15:43:20.219258
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from . import _test_downloader
    ydl = _test_downloader.FakeYDL()
    ydl.params['outtmpl'] = u'%(id)s'
    ydl.params['writedescription'] = False
    ydl.params['writeinfojson'] = False
    ydl.params['writesubtitles'] = True
    ydl.params['writeautomaticsub'] = True
    ydl.params['writeannotations'] = True
    ydl.params['writethumbnail'] = True
    ydl.params['writedescription'] = False
    ydl.params['writeinfojson'] = False
    ydl.params['writesubtitles'] = True
    ydl.params['writeautomaticsub'] = True
    ydl.params['writeannotations'] = True
    ydl

# Generated at 2022-06-14 15:43:22.163327
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)
    fd = FragmentFD()

# Generated at 2022-06-14 15:43:25.322662
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:43:36.434483
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import copy
    import re

    class FakeInfoDict(object):
        pass

    class FakeYDL(object):
        def __init__(self):
            self.params = {}

    class FragmentFDUT(FragmentFD):
        def _prepare_and_start_frag_download(self, ctx):
            raise NotImplementedError()

        def _prepare_frag_download(self, ctx):
            raise NotImplementedError()

        def _start_frag_download(self, ctx):
            raise NotImplementedError()

        def _parse_fragment_url(self, info_dict, url, frag_index):
            return url, None

        def _download_fragment(self, ctx, frag_url, info_dict, headers=None):
            return False

# Generated at 2022-06-14 15:43:37.418661
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD(None, {}, {})

# Generated at 2022-06-14 15:43:41.854308
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    args = {'quiet': True}
    ydl = FakeYDL()
    dl = HttpQuietDownloader(ydl, args)
    assert dl.ydl is ydl
    assert dl.params == args



# Generated at 2022-06-14 15:43:51.052663
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    class MockYDL():
        params = {
            'continuedl': True,
            'noprogress': True,
            'nopart': True,
            'updatetime': True,
            'test': True
        }
    def hook(status):
        assert status['status'] == 'finished'
    ydl = MockYDL()
    dl = HttpQuietDownloader(ydl, {'retries': 5})
    dl.add_progress_hook(hook)
    assert dl.params == {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'ratelimit': None,
        'retries': 5,
        'nopart': True,
        'test': True
    }
    assert dl.ydl == ydl

# Generated at 2022-06-14 15:44:02.986316
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor.common import InfoExtractor
    from ..extractor.dash import DASHIE
    ydl = InfoExtractor()
    ydl.add_info_extractor(DASHIE())
    from ..utils import make_HTTPServer
    from ..compat import compat_str

    server = make_HTTPServer()

# Generated at 2022-06-14 15:44:11.023405
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MyFragmentFD(FragmentFD):
        def __init__(self, ydl, params):
            super(MyFragmentFD, self).__init__(ydl, params)

        def real_download(self, *a, **k):
            pass

        @staticmethod
        def report_warning(msg):
            pass

        @staticmethod
        def report_destination(filename):
            pass

        @staticmethod
        def report_error(msg):
            pass

        @staticmethod
        def try_utime(filename, last_modified_hdr):
            pass

    ydl = object()


# Generated at 2022-06-14 15:44:14.689020
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:45:43.822478
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .extractor import gen_extractor
    from .downloader.common import FileDownloader

    class SampleFragmentFD(FragmentFD):
        FD_NAME = 'sample'

    class SampleIE(gen_extractor()):
        IE_NAME = 'sample'
        IE_DESC = 'Sample IE'
        _VALID_URL = r'https?://(?:www\.)?sample\.com/video\.html'

        _TESTS = [{
            'url': 'http://www.sample.com/video.html',
            'info_dict': {
                'id': '1337',
                'ext': 'mp4',
                'title': 'Sample video',
            },
            'params': {
                'skip_download': True,
            }
        }]


# Generated at 2022-06-14 15:45:46.800440
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class A(FragmentFD):
        pass
    a = A({
        'params': {
            'keepfragments': True,
            'fragment_retries': 3,
            'skip_unavailable_fragments': False,
        },
        'to_screen': lambda x: True,
    })

    assert a.params['keepfragments'] == True
    assert a.params['fragment_retries'] == 3
    assert a.params['skip_unavailable_fragments'] == False

# Generated at 2022-06-14 15:45:48.528471
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = FileDownloader({})
    assert isinstance(ydl, FileDownloader)
    assert ydl.params.get('quiet', False) is True
    assert ydl.params.get('logger', None) is None

# Generated at 2022-06-14 15:45:55.711453
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..compat import is_py2
    from ..utils import encode_compat_str

    def HttpQuietDownloader_get_handle(self):
        # pylint: disable=no-self-use
        return False
    import types
    HttpQuietDownloader.get_handle = types.MethodType(
        HttpQuietDownloader_get_handle, HttpQuietDownloader)

    def hook(d):
        if is_py2:
            assert isinstance(d['filename'], str)
        else:
            assert isinstance(d['filename'], str)


# Generated at 2022-06-14 15:45:58.158037
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    ydl = InfoExtractor()
    dl = HttpQuietDownloader(ydl, {'retries': 3})
    assert dl._opts['retries'] == 3

# Generated at 2022-06-14 15:46:01.676292
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = object()
    params = {'continuedl': True, 'quiet': True}
    inst = HttpQuietDownloader(ydl, params)
    assert inst._ydl is ydl
    assert inst._params == params


# Generated at 2022-06-14 15:46:09.900145
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..compat import compat_urllib_request
    from ..downloader.http import HttpDownloader

    req = compat_urllib_request.Request('http://www.example.com', headers={'User-Agent': 'foobar'})
    dl = HttpQuietDownloader({}, {'quiet': True})
    assert isinstance(dl, HttpDownloader)
    assert dl.ydl is not None
    assert dl.params['quiet']
    http_req = dl._prepare_request(req, None)
    assert http_req.headers['User-Agent'] == 'foobar'

# TODO: Add unit test for _start_frag_download()

# Generated at 2022-06-14 15:46:18.785339
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD('a', None)
    assert fd.params == {
        'keep_fragments': False,
        'nopart': False,
        'quiet': True,
        'ratelimit': None,
        'retries': 0,
        'skip_unavailable_fragments': False,
    }

    fd = FragmentFD('a', None, {
        'keep_fragments': True,
        'quiet': False,
        'ratelimit': '10.0',
        'skip_unavailable_fragments': True,
    })

# Generated at 2022-06-14 15:46:19.978331
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert (HttpQuietDownloader({}, {}) is not None)

# Generated at 2022-06-14 15:46:24.621865
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..downloader.http.HttpFD import HttpQuietDownloader
    ydl = object()
    params = {'continuedl': True, 'noprogress': True, 'ratelimit': 123, 'retries': 10}
    d = HttpQuietDownloader(ydl, params)
    assert d.ydl is ydl
    assert d.params == params
    assert d._screen_file == None
