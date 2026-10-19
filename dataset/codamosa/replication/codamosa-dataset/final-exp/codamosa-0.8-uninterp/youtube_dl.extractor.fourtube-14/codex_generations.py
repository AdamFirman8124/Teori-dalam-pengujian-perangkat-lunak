

# Generated at 2022-06-14 16:13:37.768348
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    pass

# Generated at 2022-06-14 16:13:45.965954
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .common import InfoExtractor
    from ..utils import parse_duration
    from .common import HEADRequest
    from six.moves import urllib
    from six.moves.urllib.parse import urlparse, parse_qs

    ie = InfoExtractor()
    ie._downloader = lambda _: ie
    ie.http_HEAD = lambda url: HEADRequest(url, {}, {'Location': url})
    ie.add_info_extractor(FourTubeIE.ie_key())

    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    mobj = re.match(FourTubeIE._VALID_URL, url)
    video_id = mobj.group('id')

   

# Generated at 2022-06-14 16:13:53.879851
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    f = FourTubeIE()
    assert f._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert f._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert f._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:13:56.234849
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    ie = FuxIE()
    ie = PornTubeIE()
    ie = PornerBrosIE()

# Generated at 2022-06-14 16:13:57.587063
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert isinstance(PornerBrosIE(), PornTubeIE)



# Generated at 2022-06-14 16:14:02.197288
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
  assert PornerBrosIE._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'

# Generated at 2022-06-14 16:14:12.081071
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE(None)
    assert ie.IE_NAME == '4tube'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:14:17.196544
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert (
        PornerBrosIE(None, {}).
        _VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )

# Generated at 2022-06-14 16:14:20.428194
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    object_1 = FourTubeBaseIE(FourTubeBaseIE._downloader)
    assert object_1._downloader == FourTubeBaseIE._downloader
    assert object_1._WORKING == True
    

# Generated at 2022-06-14 16:14:21.917222
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert isinstance(FourTubeIE(), FourTubeIE)


# Generated at 2022-06-14 16:14:42.471477
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Test invalid URLs
    with pytest.raises(TypeError):
        FourTubeBaseIE()
    with pytest.raises(AssertionError):
        FourTubeBaseIE('http://www.4tube.com/video')
    with pytest.raises(AssertionError):
        FourTubeBaseIE(
            'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    with pytest.raises(AssertionError):
        FourTubeBaseIE(
            'http://www.4tube.com/embed/209733-hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2022-06-14 16:14:42.947158
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()

# Generated at 2022-06-14 16:14:44.343283
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    base = FourTubeBaseIE()
    assert base._TKN_HOST
    assert base._VALID_URL
    assert base._URL_TEMPLATE

# Generated at 2022-06-14 16:14:44.833503
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:14:51.037513
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fuxie = FuxIE()

    assert fuxie.IE_NAME == '4tube'

    assert fuxie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fuxie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fuxie._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:15:00.841940
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # --------------------------
    # Test case 1.
    # --------------------------
    example_url = 'https://www.porntube.com/embed/7089759'

    # Create an instance of class PornTubeIE
    pt_ie = PornTubeIE()

    # Get a dictionary with basic data about the video to extract
    # and test if the matches with what it should be
    # and test if the matches with what it should be
    video_data = pt_ie._real_extract(example_url)

    assert video_data[u'id'] == '7089759'
    assert video_data[u'title'] == 'Teen couple doing anal'
    assert video_data[u'uploader'] == 'Alexy'
    assert video_data[u'uploader_id'] == '91488'
    assert video_data

# Generated at 2022-06-14 16:15:04.693269
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    porner_bros_ie = PornerBrosIE()
    assert porner_bros_ie.IE_NAME == 'PornerBros'

# Generated at 2022-06-14 16:15:06.025527
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert(ie)

# Generated at 2022-06-14 16:15:07.328398
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:15:08.034865
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:15:43.591852
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    class_name = "PornTubeIE"
    # test case 1 - check if class name correctly assigned
    try:
        assert class_name == PornTubeIE.IE_NAME, "1st test fail"
        print("class %s: test case 1 passed" % class_name)
    except AssertionError:
        print("class %s: test case 1 failed" % class_name)
    # test case 2 - check if regex of url validator correctly assigned
    test_url = "https://www.porntube.com/videos/teen-couple-doing-anal_7089759"

# Generated at 2022-06-14 16:15:52.916931
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.utils import DownloadError

    class MyFileDownloader(FileDownloader):
        # The basic idea is to detect whether the desired video is available
        # for all formats or not, and if so, to raise an error.

        def _retrieve_url(self, url_data):
            my_url = url_data['url']
            if 'video1.mp4' in my_url:
                raise DownloadError('This video is not available in all formats.')
            return 'fake_bytes', {}

    fd = MyFileDownloader(
        params={'nopart': True})
    ie = FourTubeBaseIE()

# Generated at 2022-06-14 16:15:55.650047
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE()._TKN_HOST == 'token.fux.com'


# Generated at 2022-06-14 16:15:57.019761
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    x = PornerBrosIE()


# Generated at 2022-06-14 16:15:59.746122
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # testing if constructor throws exception when called
    try:
        PornTubeIE()
        assert False
    except:
        assert True

###################################################################

# Generated at 2022-06-14 16:16:09.790928
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .common import InfoExtractor
    from ..utils import fake_urlopen
    from ..compat import compat_str

    class DummyIE(InfoExtractor):
        IE_NAME = "DummyIE"
        IE_DESC = "Dummy description"
        _VALID_URL = r".*"

        @staticmethod
        def _extract_urls(url, webpage):
            return [url]

        def _real_extract(self, url):
            return self.url_result(url)

    class ProxyFuxIE(FuxIE, DummyIE):
        def _real_extract(self, url):
            return super(ProxyFuxIE, self)._real_extract(url)

    fake_urlopen.side_effect = FakeUrlOpen(content=b'{"hello": "world"}')


# Generated at 2022-06-14 16:16:15.209975
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    url_template = 'https://www.porntube.com/videos/video_%s'
    url_id = 'main'
    url = url_template % url_id
    # The following line will fail if object not initialized properly
    test_object = FourTubeBaseIE()._build_url_result(url, url_id)
    assert test_object

# Generated at 2022-06-14 16:16:26.471366
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    from .kaltura_tests import KalturaIE


# Generated at 2022-06-14 16:16:27.054195
# Unit test for constructor of class FuxIE
def test_FuxIE():
    pass


# Generated at 2022-06-14 16:16:28.019212
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from . import PornTubeIE as TestPornTubeIE
    instance = TestPornTubeIE()

# Generated at 2022-06-14 16:17:33.738372
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    f = FourTubeIE(InfoExtractor())
    assert f.IE_NAME == '4tube'
    assert f._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert f._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert f._TKN_HOST == 'token.4tube.com'
    

# Generated at 2022-06-14 16:17:35.137245
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    f = FourTubeBaseIE()
    pb = PornerBrosIE(f)

# Generated at 2022-06-14 16:17:37.025600
# Unit test for constructor of class FuxIE
def test_FuxIE():
    video_url = 'https://www.fux.com/embed/200952?autoplay=true'
    assert FuxIE().suitable(video_url) is True

# Generated at 2022-06-14 16:17:43.057840
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    info_extractor = PornTubeIE()
    result = info_extractor._parse_json(
            info_extractor._search_regex(
                r'INITIALSTATE\s*=\s*(["\'])(?P<value>(?:(?!\1).)+)\1',
                '<html></html>', 'data', group='value'), '123',
            transform_source=lambda x: compat_urllib_parse_unquote(
                compat_b64decode(x).decode('utf-8')))['page']['video']
    result['user'] = {'username': 'test', 'id': 'test'}
    assert result == {
        'mediaId': 'test',
        'user': {'username': 'test', 'id': 'test'}
        }

# Generated at 2022-06-14 16:17:47.624712
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .utils import (
        FakeWebpage,
        find_test_cases,
        make_test_case,
        skip_unless
    )

    def test_FuxIE_constructor():

        test_case_map = {}

        for test_case_dict in find_test_cases(FuxIE, 'FuxIE'):
            test_case_map.update(
                make_test_case(FuxIE, 'test_FuxIE_constructor', **test_case_dict)
            )

        @skip_unless(test_case_map)
        def test_FuxIE_cases(self):
            for test_case_id, test_case in test_case_map.items():
                self.run_test(
                    test_case_id,
                    test_case
                )

        return test

# Generated at 2022-06-14 16:17:48.368705
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    fourTubeBaseIE = FourTubeBaseIE()

# Generated at 2022-06-14 16:17:48.872309
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:17:52.673359
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    x = FourTubeIE()
    assert x._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert x._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert x._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:17:54.782548
# Unit test for constructor of class FuxIE
def test_FuxIE():
  fux = FuxIE("https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow", False)
  assert fux.IE_NAME == "4tube"


# Generated at 2022-06-14 16:17:55.292215
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:20:48.800961
# Unit test for constructor of class FuxIE
def test_FuxIE():
    m = FuxIE()

# Generated at 2022-06-14 16:20:57.009183
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie.IE_NAME == "FourTube"
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie.IE_DESC == "PornerBros"

# Generated at 2022-06-14 16:20:59.147448
# Unit test for constructor of class FuxIE
def test_FuxIE():
    try:
        FuxIE()
    except Exception as e:
        raise Exception('FuxIE constructor test failed with error: ' + str(e))


# Generated at 2022-06-14 16:21:09.755002
# Unit test for constructor of class FuxIE
def test_FuxIE():
    a = FuxIE()
    assert a.IE_NAME == '4tube'
    assert a._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert a._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert a._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:21:19.460880
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert(FuxIE._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
    assert(FuxIE._TESTS[0]['url'] == 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert(FuxIE._TESTS[1]['url'] == 'https://www.fux.com/embed/195359')
    assert(FuxIE._TESTS[2]['url'] == 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2022-06-14 16:21:20.898651
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE(None)
    assert ie._download_webpage('http://example.com', '1234') is None

# Generated at 2022-06-14 16:21:32.475019
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    P = PornTubeIE()
    assert P._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert P._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert P._TKN_HOST == 'tkn.porntube.com'
    print(P._TESTS)

# Generated at 2022-06-14 16:21:44.768658
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    ie._VALID_URL = FourTubeBaseIE._VALID_URL
    ie._TKN_HOST = FourTubeBaseIE._TKN_HOST
    ie._URL_TEMPLATE = FourTubeBaseIE._URL_TEMPLATE
    ie._search_regex = FourTubeBaseIE._search_regex
    ie._download_webpage = FourTubeBaseIE._download_webpage
    ie._parse_json = FourTubeBaseIE._parse_json
    ie._html_search_meta = FourTubeBaseIE._html_search_meta
    ie._extract_formats = FourTubeBaseIE._extract_formats
    ie._sort_formats = FourTubeBaseIE._sort_formats
    ie._real_extract = FourTubeBaseIE._real_extract
    ie._

# Generated at 2022-06-14 16:21:49.841194
# Unit test for constructor of class FuxIE
def test_FuxIE():
  url_test = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
  fux_ie = FuxIE()
  fux_ie._download_webpage = lambda url, video_id: ''
  fux_ie._parse_json = lambda json, video_id: {}
  fux_ie._real_extract(url_test)

# Generated at 2022-06-14 16:21:51.707487
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Test the fourtube constructor
    obj = FourTubeBaseIE();
    assert obj != None;