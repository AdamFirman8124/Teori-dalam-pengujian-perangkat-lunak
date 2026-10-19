

# Generated at 2022-06-14 15:37:47.290144
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)
    ydl = object()
    params = {}
    fd = FragmentFD(ydl, params)
    assert fd.ydl is ydl
    assert fd.params == params

# Generated at 2022-06-14 15:37:58.456954
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = object()
    expected_params = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'nopart': False,
        'ratelimit': None,
        'retries': 0,
        'test': False,
        'fragsize': None,
    }
    hqd = HttpQuietDownloader(ydl, expected_params)
    assert hqd.ydl is ydl
    assert hqd.params == expected_params

    hqd = HttpQuietDownloader(ydl, {})
    assert hqd.params == expected_params


# Generated at 2022-06-14 15:38:00.879857
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD(None, {})
    assert fd.params == {}

# Generated at 2022-06-14 15:38:02.965259
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    assert issubclass(HttpQuietDownloader, HttpFD)

# Generated at 2022-06-14 15:38:04.049039
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        def __init__(self):
            pass
    TestFD()

# Generated at 2022-06-14 15:38:07.001330
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader
    from .http import HttpFD
    assert issubclass(HttpQuietDownloader, FileDownloader)
    assert issubclass(HttpQuietDownloader, HttpFD)

# Generated at 2022-06-14 15:38:12.337038
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .common import FileDownloader
    fd = FileDownloader({})
    dl = HttpQuietDownloader(fd, {'noprogress': True})
    assert dl.params['noprogress'] == True

if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:38:25.920777
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    sys.modules['__main__'].params = {
        'continue_dl': True,
        'quiet': True,
        'noprogress': True,
        'ratelimit': '1M',
        'retries': 0,
        'nopart': False,
        'test': False,
    }
    sys.modules['__main__'].to_screen = lambda x: x
    dl = HttpQuietDownloader(
        sys.modules['__main__'],
        sys.modules['__main__'].params
    )
    assert dl.params['continuedl'] is True
    assert dl.params['quiet'] is True
    assert dl.params['noprogress'] is True
    assert dl.params['ratelimit'] == '1M'
    assert dl

# Generated at 2022-06-14 15:38:27.273334
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # TODO
    pass

# Generated at 2022-06-14 15:38:31.755632
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from ..downloader.external import ExternalFD

    def test_download(fd):
        assert isinstance(fd, FragmentFD)
        assert isinstance(fd, FileDownloader)
        assert isinstance(fd, ExternalFD)

    class MyFD(FragmentFD):
        FD_NAME = 'my_fd'

    fd = MyFD()
    fd.params = {
        'usenetrc': False,
        'username': None,
        'password': None,
        'quiet': True,
        'no_warnings': True,
        'forget_it': None,
        'ratelimit': None,
    }
    fd.add_info_extractor(None)

# Generated at 2022-06-14 15:38:52.369456
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD.__name__ == 'FragmentFD'

# Generated at 2022-06-14 15:38:56.050944
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = FileDownloader(params={})
    dl = HttpQuietDownloader(ydl, {'continuedl': True})
    assert dl.params['continuedl']
    assert dl.ydl is ydl



# Generated at 2022-06-14 15:39:02.838738
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    assert HttpQuietDownloader is not HttpFD
    assert issubclass(HttpQuietDownloader, HttpFD)
    assert HttpQuietDownloader.to_screen == HttpFD.to_screen
    assert HttpQuietDownloader.to_screen.__func__ is HttpFD.to_screen.__func__


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 15:39:03.805510
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert FragmentFD(None, None)

# Generated at 2022-06-14 15:39:09.802769
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from ..compat import compat_HTTPError
    def dummy(*args, **kargs):
        pass
    dummy.report_destination = dummy
    dummy.to_screen = dummy
    dummy.report_progress = dummy
    dummy.report_error = dummy
    dummy.trouble = dummy
    dummy.temp_name = dummy
    dummy.try_rename = dummy
    dummy.try_utime = dummy
    dummy.report_warning = dummy
    dummy.report_resuming_byte = dummy
    dummy.report_retry = dummy
    tmp = HttpQuietDownloader({'quiet': True}, dummy)
    assert tmp._opener.addheaders == []
    tmp = HttpQuietDownloader({'quiet': False}, dummy)
    assert tmp._opener.addheaders != []

# Generated at 2022-06-14 15:39:22.098382
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    try:
        from ytdl_is_update import ytdl_is_update
    except ImportError:
        return

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    from .common import YoutubeDL
    from .extractor.common import InfoExtractor

    ie = InfoExtractor()
    ie._downloader = YoutubeDL()
    ie.params = {
        'skip_download': True,
    }
    ie._ies = []
    ie._ies_inst = {}
    ie._progress_hooks = []
    ie._screen_file = None
    ie.to_screen = lambda *args, **kargs: None
    ie._downloader.to_screen = lambda *args, **kargs: None
    ie.report_warning = lambda msg: None


# Generated at 2022-06-14 15:39:28.930787
# Unit test for constructor of class FragmentFD
def test_FragmentFD():

    # Dummy info_dict
    info_dict = {
        'extractor': 'Common extractor',
    }

    # Constructor FragmentFD
    fd = FragmentFD({}, None, None)

    # Set the private key of FragmentFD to enable the test
    fd.ydl = None  # Dummy youtube-dl instance
    fd.to_screen = lambda *args, **kargs: None
    fd.report_error = lambda *args, **kargs: None
    try:
        fd.__dict__['params']
    except KeyError:
        fd.__dict__['params'] = {}

    # Test _prepare_frag_download

# Generated at 2022-06-14 15:39:39.320006
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    """ Test for constructor of class HttpQuietDownloader """
    import unittest
    from .f4mdownloader import F4mFD
    from .smoothstreams import SmoothStreamsFD
    from .dash import (DashFragmentsFD, DashSegmentsFD,
                       make_dest_pair_names)

    class HttpQuietDownloaderTest(unittest.TestCase):

        def test_HttpQuietDownloader(self):
            ydl = F4mFD()
            dl = HttpQuietDownloader(ydl)
            self.assertEqual(dl.ydl, ydl)

# Generated at 2022-06-14 15:39:47.716150
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor.common import InfoExtractor
    from ..downloader.http import HttpFD
    from .common import FakeYDL

    FakeYDL.params['logger'] = None
    ie = InfoExtractor()
    ie.params['logger'] = None
    ie.to_screen = lambda *a, **k: None

    hqd = HttpQuietDownloader(FakeYDL(), {})

    u_dumps = lambda u: '%s (%s)' % (repr(u), type(u))
    assert u_dumps(hqd.ydl) == u_dumps(FakeYDL())
    assert hqd.params is FakeYDL.params
    assert hqd.to_screen is FakeYDL.to_screen
    assert hqd.report_warning is ie.report_warning

# Generated at 2022-06-14 15:39:52.810127
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..utils import FakeYDL
    ydl = FakeYDL()
    hqd = HttpQuietDownloader(ydl, {'continuedl': True})
    assert hqd.params['noprogress'] is True
    assert hqd.params['quiet'] is True
    assert hqd.params['continuedl'] is True
    assert hqd.params['noprogress'] is True

# Generated at 2022-06-14 15:40:32.880692
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    from .common import FileDownloader
    from .options import _fix_opts

    opts = _fix_opts({})
    gen_extractors()
    for name, ie in FileDownloader.gen_extractor_classes():
        ie = ie(opts)
        dl = ie.get_downloader(opts)
        assert isinstance(dl, HttpQuietDownloader)

# Generated at 2022-06-14 15:40:46.178507
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from .common import FileDownloader
    from .http import HttpFD
    from .dash import DASHFD

    # Class hierarchy
    assert issubclass(FragmentFD, FileDownloader)
    assert issubclass(HttpFD, FragmentFD)
    assert issubclass(DASHFD, HttpFD)

    # Constructor args
    assert DASHFD.__init__.__code__.co_varnames[0] == 'self'
    assert DASHFD.__init__.__code__.co_varnames[1] == 'ydl'
    assert DASHFD.__init__.__code__.co_varnames[2] == 'params'
    assert FileDownloader.__init__.__code__.co_varnames[0] == 'self'
    assert FileDownload

# Generated at 2022-06-14 15:40:52.368556
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    ydl = object()
    opts_dict = {'continuedl': True, 'quiet': True, 'noprogress': True}
    assert HttpQuietDownloader(ydl, opts_dict).ydl is ydl
    assert HttpQuietDownloader(ydl, opts_dict).params == opts_dict

# Generated at 2022-06-14 15:41:01.413163
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    """
    Minimal unit test for class HttpQuietDownloader
    """
    from .common import FileDownloader, IsNotUTF8
    from .http import HttpQuietDownloader
    from ..utils import prepend_extension
    from time import time as unix_time

    try:
        import argparse
    except ImportError:
        argparse = None

    if argparse is None:
        return

    class FakeYDL(FileDownloader):
        def __init__(self, params):
            super(FakeYDL, self).__init__(params)
            self.downloaded_bytes = 0

# Generated at 2022-06-14 15:41:08.071581
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD

    class DummyYDL(object):
        params = {}
        def __init__(self):
            self.params = {}

    ydl = DummyYDL()
    fd = HttpFD(ydl, {'continuedl': True, 'quiet': True, 'noprogress': True})
    assert isinstance(fd, HttpQuietDownloader)

# Generated at 2022-06-14 15:41:19.088210
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import StringIO
    import logging
    import itertools
    import unittest
    import tempfile
    import shutil
    import os.path
    from .fragment import FragmentFD

    class TestInfoDict(dict):
        pass

    test_info = TestInfoDict(
        {
            'http_headers': {
                'user-agent': 'test-user-agent',
                'accept': 'test-accept',
            },
            'live': False,
        }
    )

    class TestFD(FragmentFD):
        FD_NAME = 'test'

        def __init__(self, params):
            super(TestFD, self).__init__(params)

# Generated at 2022-06-14 15:41:25.784766
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    ie = InfoExtractor()
    ie.to_screen = lambda *args, **kargs: None
    # Arguments for FileDownloader.__init__
    params = {
        'nooverwrites': False, 'quiet': True,
        'forcefilename': True, 'forcetitle': True,
    }
    hqd = HttpQuietDownloader(ie, params)
    assert hqd.ydl is ie
    assert hqd.params is params

# Generated at 2022-06-14 15:41:31.352844
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import get_info_extractor
    ie = get_info_extractor('youtube')

    dl = ie.FragmentFD(None, ie)
    dl.report_resuming_byte('x')
    dl.report_retry('x')
    dl.report_destination('x')
    dl.report_progress(1, 2, 3)
    dl.to_screen('x')
    dl.to_stderr('x')
    dl.to_console_title('x')
    dl.try_rename('x', 'y')
    dl.try_utime('x', 'y')


# Generated at 2022-06-14 15:41:41.297535
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ydl = FakeYDL()
    fd = FragmentFD(ydl, {'outtmpl': '%(title)s.%(ext)s'})

    assert fd.params['outtmpl'] == '%(title)s.%(ext)s'
    assert fd.TEMP_NAME_PATTERN == '%(title)s-%(id)s.%(ext)s'

    fd = FragmentFD(ydl, {'outtmpl': '%(title)s-%(format_id)s.%(ext)s'})

    assert fd.params['outtmpl'] == '%(title)s-%(format_id)s.%(ext)s'

# Generated at 2022-06-14 15:41:42.286993
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert HttpQuietDownloader(None, {})

# Generated at 2022-06-14 15:43:00.032027
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # Ensure that it is possible to create HttpQuietDownloader
    HttpQuietDownloader(None, {})


# Generated at 2022-06-14 15:43:05.442837
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    """
    Unit test for constructor of class HttpQuietDownloader.
    """
    ydl = object()
    params = {'continuedl': True, 'quiet': True, 'noprogress': True}
    hd = HttpQuietDownloader(ydl, params)
    assert hd.ydl == ydl
    assert hd.params == params



# Generated at 2022-06-14 15:43:07.295567
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({})
    assert fd is not None

# Generated at 2022-06-14 15:43:18.721721
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    import tempfile
    import shutil
    import os
    import json

    tmp_dir = tempfile.mkdtemp()
    fd = FragmentFD(frag_index=3)
    fd.params = {
        'outtmpl': os.path.join(tmp_dir, '%(id)s.%(ext)s'),
    }
    fd.to_screen = sys.stdout.write
    filename = fd.prepare_filename(
        {'id': 'test', 'ext': 'mp4'})
    filename_sanitized = fd.sanitize_path(filename)
    dl = HttpQuietDownloader(fd.ydl, {'continuedl': True})
    dl.to_screen = sys.stdout.write

# Generated at 2022-06-14 15:43:26.720725
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MyFD(FragmentFD):
        def __init__(self, ydl, params):
            FragmentFD.__init__(self, ydl, params)

        def read_fragment_list(self, *args, **kargs):
            pass

        def _process_info(self, *args, **kargs):
            pass

    params = {
        'fragment_retries': 1,
        'keep_fragments': True,
        'skip_unavailable_fragments': True,
    }
    ydl = {}

    fd = MyFD(ydl, params)

    assert fd.params['skip_unavailable_fragments']
    assert fd.params['keep_fragments']
    assert fd.params['fragment_retries'] == 1


# Generated at 2022-06-14 15:43:30.376319
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    assert issubclass(HttpQuietDownloader, FileDownloader)
    assert HttpQuietDownloader.FILE_DOWNLOADER == True
    assert isinstance(HttpQuietDownloader(None, {}), FileDownloader)

# Generated at 2022-06-14 15:43:41.615172
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    def assert_num_equal(a, b, message=None):
        if a != b:
            message = message or '%s != %s' % (a, b)
            raise AssertionError(message)

    def test_ytdl_file_write(fd):
        filename = fd.ytdl_filename('test-file.mp4')
        stream, _ = sanitize_open(filename, 'w')
        stream.write('{"a": 0}')
        stream.close()
        return filename

    def test_ytdl_file_read(fd, context, filename):
        # Break ytdl_filename's invariant
        context['tmpfilename'] = ''
        context['fragment_index'] = 0

# Generated at 2022-06-14 15:43:50.889165
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .html import HtmlFD
    class MyFragmentFD(FragmentFD):
        def real_download(self, filename, info_dict):
            url = info_dict['url']
            http_dl = HtmlFD()
            return http_dl.download(filename, {'url': url})

    fd = MyFragmentFD({}, None)
    assert fd._download_fragment(
        {}, 'http://localhost', {}, info_dict={}) == (False, None)
    assert fd._download_fragment(
        {}, 'http://localhost', {'url': 'http://example.com'}) == (False, None)
    assert fd._download_fragment(
        {}, 'http://localhost', {'url': 'http://localhost'}) == (True, b'test')

# Generated at 2022-06-14 15:43:53.082017
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    assert issubclass(HttpQuietDownloader, HttpFD)

# Generated at 2022-06-14 15:44:00.774144
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import io

    testout = io.BytesIO()
    sys.stdout = testout
    testfd = HttpQuietDownloader(None, None)
    testfd.to_screen('test')
    testfd.report_retry('test')
    testfd.report_error('test')
    testfd.report_finish()
    sys.stdout = sys.__stdout__
    assert not testout.getvalue()

# Generated at 2022-06-14 15:47:16.187323
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL({'quiet': True})
    dl = HttpQuietDownloader(ydl, {'quiet': True})
    assert dl.params['quiet'] == True