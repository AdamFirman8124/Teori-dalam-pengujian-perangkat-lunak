

# Generated at 2022-06-14 15:37:55.179163
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor.common import InfoExtractor
    from .postprocessor import FFmpegPostProcessor
    from .postprocessor.embedthumbnail import EmbedThumbnailPP
    ydl = InfoExtractor()
    ydl.add_default_info_extractors()
    ydl.add_post_processor(FFmpegPostProcessor())
    ydl.add_post_processor(EmbedThumbnailPP())
    quiet_http_dl = HttpQuietDownloader(ydl, {'nooverwrites': True})
    assert isinstance(quiet_http_dl, FileDownloader)
    assert isinstance(quiet_http_dl, HttpFD)
    assert isinstance(quiet_http_dl, HttpQuietDownloader)

# Generated at 2022-06-14 15:37:59.648080
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import youtube_dl.YoutubeDL

    ydl = youtube_dl.YoutubeDL(params={})
    HttpQuietDownloader(ydl, params={})


# vim:set shiftwidth=4 softtabstop=4 expandtab:

# Generated at 2022-06-14 15:38:10.094272
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from ..extractor import all_extractors
    extractors = [x for x in all_extractors.values() if x.IE_NAME != 'generic']

    for ie in extractors:
        ie = ie(downloader=HttpQuietDownloader)
        info_dict = {}
        ie.add_default_info_extractors(info_dict)

        assert 'formats' in info_dict

        for f in info_dict['formats']:
            assert f.get('url') or f.get('manifest_url')

        assert info_dict.get('extractor') == ie.IE_NAME

        assert info_dict.get('webpage_url', '').startswith('http')

        assert 'title' in info_dict['extractor_key']

# Generated at 2022-06-14 15:38:19.042489
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import gen_extractors
    extractors = gen_extractors()
    for ie in extractors:
        if hasattr(ie, '_WORKING'):
            continue
        FD = type(ie.IE_NAME, (FragmentFD,), {})
        inst = FD(
            {'params': {}}, ie, {}, 'http://example.com/video.f4m')
        assert inst

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:38:25.368686
# Unit test for constructor of class FragmentFD

# Generated at 2022-06-14 15:38:27.704747
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD('youtube-dl', {})
    assert isinstance(fd, FragmentFD)

# Generated at 2022-06-14 15:38:33.956935
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    fd = HttpQuietDownloader(None, {'continuedl': True, 'quiet': True, 'noprogress': True})
    assert fd.params['continuedl']
    assert fd.params['noprogress']
    assert fd.params['quiet']
    assert not fd.params.get('logger')
    assert not fd.params.get('progress_hooks')

# Generated at 2022-06-14 15:38:36.753657
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor

# Generated at 2022-06-14 15:38:43.396016
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    from .http import HttpFD
    ydl = YoutubeDL()
    ydl.add_progress_hook(lambda x: None)  # Don't print output
    df = FragmentFD(ydl, {})
    df.to_screen = lambda x: None
    assert df.__class__.__base__ == HttpFD

# Generated at 2022-06-14 15:38:55.142152
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    params = {
        'skip_unavailable_fragments': True,
        'keep_fragments': False,
        'retries': 10,
        'fragment_retries': 10,
        'an_option': 'test',
    }
    fd.add_info_extractor(params)
    fd.add_params(params)
    assert fd.params['keep_fragments'] is False
    assert fd.params['skip_unavailable_fragments'] is True
    assert fd.params['retries'] == 10
    assert fd.params['fragment_retries'] == 10
    assert fd.params['an_option'] == 'test'

    # Now test new options with new defaults

# Generated at 2022-06-14 15:39:15.964806
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({}, {})
    assert fd


if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:39:22.656401
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    params = {
        'continuedl': True,
        'quiet': True,
        'noprogress': True,
        'retries': 0,
        'nopart': False,
        'test': False,
    }
    downloader = HttpQuietDownloader(None, params)
    for k, v in params.items():
        assert getattr(downloader, k) == v


if __name__ == '__main__':
    test_HttpQuietDownloader()

# Generated at 2022-06-14 15:39:27.306198
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    # prepare test params
    params = {
           'continuedl': True,
           'quiet': True,
           'noprogress': True,
           'nopart': False,
           'test': False
    }

    # prepare test system arguments
    args = ['youtube-dl', '--no-check-certificate', 'http://www.youtube.com/watch?v=BaW_jenozKc']

    # test instance creation
    testHttpQuietDownloader = HttpQuietDownloader(None, params)

    assert isinstance(testHttpQuietDownloader, FileDownloader)

    assert testHttpQuietDownloader.params == params
    assert testHttpQuietDownloader._args == args

# Generated at 2022-06-14 15:39:37.980427
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class TestFD(FragmentFD):
        def __init__(self, ydl, params):
            super(TestFD, self).__init__(ydl, params)
        def real_download(self, *args, **kwargs):
            pass
        def _prepare_frag_download(self, *args, **kwargs):
            pass
        def _start_frag_download(self, *args, **kwargs):
            pass
        def _finish_frag_download(self, *args, **kwargs):
            pass
        def ytdl_filename(self, *args, **kwargs):
            pass
    from ..extractor import YoutubeIE
    from ..YoutubeDL import YoutubeDL

# Generated at 2022-06-14 15:39:46.573606
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    from .extractor import gen_extractors

    class FakeYDL:
        def __init__(self):
            self.params = {
                'noprogress': False,
            }

        def to_screen(self, *args, **kargs):
            pass

        def trouble(self, *args, **kargs):
            pass

    ydl = FakeYDL()
    gen_extractors()
    hqd = HttpQuietDownloader(ydl, {})
    assert hqd.params['noprogress']

# Generated at 2022-06-14 15:39:55.502106
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    import os.path
    # Test downloader methods
    assert HttpQuietDownloader.real_download(
        HttpQuietDownloader(),
        {
            'url': 'http://www.youtube.com/',
            'http_headers': {
                'Content-Type': 'text/plain; charset=utf-8',
            }
        },
        {
            'continuedl': True,
            'noprogress': True,
            'ratelimit': None,
            'retries': 0,
            'nopart': False,
            'test': False,
        },
        '-'
    ) == (True, {'status': 'finished'})

    if sys.version_info < (2, 7):
        return

    # Test _match_entry()
    downloader = Http

# Generated at 2022-06-14 15:39:56.746452
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    HttpQuietDownloader(None, None)

# Generated at 2022-06-14 15:40:09.754496
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..compat import compat_urllib_request
    youtube_dl = None

    fd = FragmentFD(youtube_dl, {})
    info_dict = {'http_headers': {'Range': 'bytes=0-'}}
    url = 'http://example.com/video.mp4'

    req = fd._prepare_url(info_dict, url)
    assert isinstance(req, compat_urllib_request.Request)
    assert req.get_full_url() == url
    assert req.get_header('Range') == 'bytes=0-'

    info_dict = {}
    req = fd._prepare_url(info_dict, url)
    assert isinstance(req, basestring)
    assert req == url


if __name__ == '__main__':
    test_Frag

# Generated at 2022-06-14 15:40:13.745544
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    assert sys.version_info >= (2, 6)

    # Just make sure the FragmentFD class can be instantiated
    fd = FragmentFD({})
    assert fd is not None

# Generated at 2022-06-14 15:40:17.597309
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..downloader import Downloader
    ydl = Downloader()
    fd = FragmentFD(ydl, {})
    assert fd.params == {}
    assert fd.ydl == ydl

# Generated at 2022-06-14 15:40:56.859126
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD({'ydl_params': {'format': 'mp4'}}, None, None)
    assert fd._allow_resume


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 15:41:05.092741
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class MockYDL(object):
        def __init__(self):
            self.params = {}
        def to_screen(self, txt):
            print(txt)
    ydl = MockYDL()
    ydl.params.update({
        'format': 'best',
        'outtmpl': '%(id)s.%(ext)s',
        'continuedl': False,
        'quiet': True,
        'noprogress': True,
        'ratelimit': None,
        'retries': 10,
        'nopart': False,
        'test': False,
        'fragment_retries': 10,
        'skip_unavailable_fragments': False,
    })
    fd = FragmentFD(ydl, {})
    assert fd.params == ydl

# Generated at 2022-06-14 15:41:06.983592
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    return HttpQuietDownloader({}, {'quiet': True})

# Generated at 2022-06-14 15:41:08.840696
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:41:14.331501
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..extractor import gen_extractors
    from ..downloader.common import FileDownloader
    gen_extractors()

    def hook(status):
        pass

    fd = FileDownloader({'progress_hooks': [hook]}, {})
    type(fd).add_info_extractor(FragmentFD)

# Generated at 2022-06-14 15:41:19.945940
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ydl = FileDownloader({'continuedl': True, 'quiet': True})
    fd = FragmentFD(ydl, {'keep_fragments': True})
    assert fd._prepare_url({}, 'url') == 'url'
    assert fd._prepare_url({'http_headers': {'a': 'b'}}, 'url') == sanitized_Request('url', None, {'a': 'b'})

# Generated at 2022-06-14 15:41:27.078464
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    # Parameters:
    #        params: Parameters to be passed to the FileDownloader constructor.
    #         ydl: an instance of YoutubeDL.
    params = {'m4a_id': '123'}
    ydl = {'verbose': False, 'params': params}

    # Expected result:
    #        The instance of the class FragmentFD
    result = FragmentFD(ydl, params)

    # Comparing attributes of the instance created with those of the instance
    # expected
    assert result.params == params
    assert result.ydl == ydl

# Generated at 2022-06-14 15:41:38.979614
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from ..compat import compat_urllib_request

    class MockFD(FragmentFD):
        params = {}
        ydl = None

        def real_download(self, filename, info_dict):
            pass

        def temp_name(self, filename):
            return '%s.part' % filename

        def ytdl_filename(self, filename):
            return '%s.ytdl' % filename

        def try_rename(self, old_filename, new_filename):
            os.rename(encodeFilename(old_filename), encodeFilename(new_filename))

        def report_destination(self, filename):
            pass

        def report_warning(self, msg):
            pass

        def calc_eta(self, start_time, time_now, total_bytes, downloaded_bytes):
            total_sec

# Generated at 2022-06-14 15:41:47.369642
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    http_downloader = HttpQuietDownloader(
        None,
        {
            'continuedl': True,
            'quiet': True,
            'noprogress': True,
            'ratelimit': 0,
            'retries': 0,
            'nopart': False,
            'test': False,
        }
    )
    assert (http_downloader.ydl is None
            and http_downloader.params == {
                'continuedl': True,
                'quiet': True,
                'noprogress': True,
                'ratelimit': 0,
                'retries': 0,
                'nopart': False,
                'test': False,
            })

# Generated at 2022-06-14 15:41:59.044865
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractor_classes
    from .fragment import FragmentFD
    # pylint: disable=W0612
    from .extractor.common import InfoExtractor
    for ieclass in gen_extractor_classes():
        if not issubclass(ieclass, InfoExtractor):
            continue
        if ieclass.ie_key() in ('generic', 'googledrive'):
            continue
        ie = ieclass()
        # pylint: disable=W0212
        fd = ie._downloader
        if not isinstance(fd, FragmentFD):
            continue
        assert isinstance(fd._http_fd_impl, HttpQuietDownloader)
        assert fd._http_fd_impl._ydl == ie._ydl
        assert fd._http_fd_impl._params

# Generated at 2022-06-14 15:43:21.531666
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    dl = FragmentFD(FakeYDL())
    assert dl.params == {
        'noprogress': True,
        'quiet': True,
        'continuedl': True,
        'nopart': False,
        'retries': 0,
        'fragment_retries': 10,
        'skip_unavailable_fragments': True,
        'keep_fragments': False,
    }
    assert dl.ydl is not None
    assert dl.name() == 'fragment'



# Generated at 2022-06-14 15:43:25.398234
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .common import FileDownloader
    assert issubclass(HttpQuietDownloader, HttpFD)
    assert issubclass(HttpQuietDownloader, FileDownloader)



# Generated at 2022-06-14 15:43:31.355173
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    class DummyFD(FragmentFD):
        def __init__(self):
            self.ydl = {
                'params': {},
                # Stub to make tests pass
                'to_screen': lambda *args, **kargs: None,
            }
            FragmentFD.__init__(self, self.ydl)
    assert DummyFD().params == {}

# Generated at 2022-06-14 15:43:34.157250
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    fd = FragmentFD()
    assert fd.FD_NAME == 'Fragment'

if __name__ == '__main__':
    test_FragmentFD()

# Generated at 2022-06-14 15:43:39.688885
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    import sys
    from ..extractor import get_info_extractor

    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from io import BytesIO as StringIO

    filename = 'filename'
    test_output = StringIO()

    ydl = get_info_extractor('TestIE')
    ydl.params['logger'] = ydl
    ydl.params['outtmpl'] = '%(id)s_output'
    ydl.to_stdout = lambda s: test_output.write(s + '\n')
    ydl.to_stderr = lambda s: test_output.write(s + '\n')
    ydl.report_warning = lambda *args: None


# Generated at 2022-06-14 15:43:43.632847
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    ''' Unit test for constructor of class FragmentFD.

    For testing it is sufficient to have the constructor of the class
    tested to be successfully called.
    '''
    try:
        fd = FragmentFD(None, None, None, None, None, None)
    except Exception as e:
        assert False, 'An unexpected exception occured while calling the constructor of FragmentFD: ' + str(e)
    else:
        assert True

# Generated at 2022-06-14 15:43:52.249199
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .extractor import gen_extractors
    from .extractor.common import InfoExtractor
    from .utils import DateRange

    class DummyIE(InfoExtractor):
        IE_NAME = IE_DESC = 'dummy'
        _VALID_URL = r'(?:https?://)?(?:\w+\.)?example\.org/'

        def report_download_webpage(self, *args, **kargs):
            pass

        def _real_extract(self, url):
            return {
                'id': 'example',
                'ext': 'mp4',
                'title': 'example',
                'duration': 10,
                'upload_date': '19700101',
            }

    ie = DummyIE(gen_extractors())

# Generated at 2022-06-14 15:43:55.178861
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD

    fd = HttpQuietDownloader(None, {})
    assert isinstance(fd, HttpFD)

# Generated at 2022-06-14 15:44:00.284600
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    import sys
    sys.argv = ['none']
    try:
        d = HttpQuietDownloader(None, {'quiet': True, 'noprogress': True})
    except Exception as err:
        return False
    return d.params['quiet'] and d.params['noprogress']

# Generated at 2022-06-14 15:44:02.162434
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    from .common import FileDownloader
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:47:15.348853
# Unit test for constructor of class FragmentFD
def test_FragmentFD():
    assert issubclass(FragmentFD, FileDownloader)

# Generated at 2022-06-14 15:47:21.732532
# Unit test for constructor of class HttpQuietDownloader
def test_HttpQuietDownloader():
    from .http import HttpFD
    from .common import FileDownloader
    assert issubclass(HttpQuietDownloader, HttpFD)
    assert issubclass(HttpQuietDownloader, FileDownloader)
    assert HttpQuietDownloader.__init__ is not HttpFD.__init__
    assert HttpQuietDownloader.__init__ is not FileDownloader.__init__
    assert HttpQuietDownloader.to_screen is HttpQuietDownloader.to_screen.im_func
    assert HttpQuietDownloader.to_screen.func_code is not HttpFD.to_screen.im_func.func_code