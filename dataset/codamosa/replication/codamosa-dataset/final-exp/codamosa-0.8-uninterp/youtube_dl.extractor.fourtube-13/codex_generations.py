

# Generated at 2022-06-14 16:13:47.302318
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE(None)
    assert ie._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:13:51.070584
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    expected = PornerBrosIE(PornerBrosIE.ie_key())
    assert expected is not None
    assert expected.ie_key() == 'PornerBros'
    assert expected.ie_name() == 'PornerBros'

# Generated at 2022-06-14 16:13:54.737346
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    try:
        assert(PornerBrosIE._TKN_HOST == 'token.pornerbros.com')
        assert(PornerBrosIE._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s')
    except Exception:
        print("Unit test failed for constructor of class PornerBrosIE")



# Generated at 2022-06-14 16:13:57.107179
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    inst = FourTubeBaseIE()
    assert inst._VALID_URL == ''
    assert inst._TKN_HOST == ''

# Generated at 2022-06-14 16:13:59.681644
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    try:
        PornerBrosIE()
        ok = True
    except:
        ok = False
    assert ok, 'Test PornerBrosIE constructor'


# Generated at 2022-06-14 16:14:11.302836
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # test with empty url
    ie = FourTubeBaseIE()
    assert ie.suitable('', True)  # should be suitable
    # test with valid url
    ie = FourTubeBaseIE()
    assert ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    # test with invalid url
    ie = FourTubeBaseIE()
    assert not ie.suitable('https://www.youtube.com/watch?v=8JNrQ6_km5Q')

if __name__ == '__main__':
    test_FourTubeBaseIE()

# Generated at 2022-06-14 16:14:22.381521
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # This test plays with the file FourTubeBaseIE.py
    # and should be updated if the file is modified.
    from .common import InfoExtractor
    
    # Check inheritance:
    assert issubclass(FourTubeIE, InfoExtractor) is True, (
        "unit test expects FourTubeBaseIE class to be a subclass of InfoExtractor"
    )

    # Check initialization:
    extractor = FourTubeIE()
    assert isinstance(extractor, FourTubeIE) is True, (
        "unit test expects FourTubeBaseIE class to instantiate a FourTubeBaseIE object."
    )

    # Check inheritance:
    assert issubclass(FuxIE, InfoExtractor) is True, (
        "unit test expects FourTubeBaseIE class to be a subclass of InfoExtractor"
    )

    # Check initialization:
    extract

# Generated at 2022-06-14 16:14:30.259374
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # test for method get_format_id()
    test_format_id = [
        {'resolution': 240, 'expected_result': '240p'},
        {'resolution': 360, 'expected_result': '360p'},
        {'resolution': 480, 'expected_result': '480p'},
        {'resolution': 720, 'expected_result': '720p'},
        {'resolution': 1080, 'expected_result': '1080p'},
        {'resolution': 1440, 'expected_result': '1440p'},
        {'resolution': 2160, 'expected_result': '2160p'},
        {'resolution': 4320, 'expected_result': '4320p'},
        {'resolution': 546, 'expected_result': '546p'},
    ]


# Generated at 2022-06-14 16:14:31.048094
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE(FourTubeBaseIE)

# Generated at 2022-06-14 16:14:41.609616
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    video_id = "7089759"
    url = PornTubeIE._URL_TEMPLATE % video_id
    webpage = PornTubeIE._download_webpage(url, video_id)
    video = PornTubeIE._parse_json(
        PornTubeIE._search_regex(
            r'INITIALSTATE\s*=\s*(["\'])(?P<value>(?:(?!\1).)+)\1',
            webpage, 'data', group='value'), video_id,
        transform_source=lambda x: compat_urllib_parse_unquote(
            compat_b64decode(x).decode('utf-8')))['page']['video']
    title = video['title']
    media_id = video['mediaId']

# Generated at 2022-06-14 16:14:59.515764
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    ie.extract('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2022-06-14 16:15:12.931245
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    class_FourTubeIE = FourTubeIE(None)
    assert str(class_FourTubeIE) == '<FourTubeIE(FourTube)>'
    assert class_FourTubeIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert class_FourTubeIE._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert class_FourTubeIE._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:15:15.895353
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    # Access to a protected member _TKN_HOST of a client class - pylint: disable=W0212
    assert PornerBrosIE._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:15:17.896162
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    IE4T = FourTubeIE()
    assert(IE4T._TKN_HOST == 'token.4tube.com')


# Generated at 2022-06-14 16:15:22.250510
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .common import update_url_query

    # 1. No argument
    from .common import FuxIE
    assert FuxIE()._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert FuxIE()._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE()._TKN_HOST == 'token.fux.com'

    # 2. With arguments
    from .common import PornTubeIE

# Generated at 2022-06-14 16:15:27.447319
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
        #variables
        url = "https://www.porntube.com/videos/teen-couple-doing-anal_7089759"
        expectedTitle = "Teen couple doing anal"

        #testing
        PornTubeIE._download_webpage = lambda self, url: open('test_data/porntube_response.txt').read()
        PornTubeIE._parse_json = lambda self, *args, **kwargs: json.loads(open('test_data/porntube_response.txt').read())
        PornTubeIE._html_search_meta = lambda self, *args, **kwargs: 'Teen couple doing anal'
        PornTubeIE._search_regex = lambda self, *args, **kwargs: '7089759'

        result = PornTubeIE()._real_extract(url)

# Generated at 2022-06-14 16:15:28.186410
# Unit test for constructor of class FuxIE
def test_FuxIE():
    x = FuxIE()

# Generated at 2022-06-14 16:15:30.274904
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE('PornerBrosIE','http://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',1)

# Generated at 2022-06-14 16:15:32.277187
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    """
    Constructor of class PornerBrosIE
    Tests that the PornerBrosIE object is constructed
    properly, without raising any errors.
    """
    ie = PornerBrosIE()

# Generated at 2022-06-14 16:15:33.655339
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE('http://www.pornerbros.com')
    assert ie.__class__ == PornerBrosIE

# Generated at 2022-06-14 16:16:05.987476
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ins = PornerBrosIE()
    assert ins is not None

# Generated at 2022-06-14 16:16:06.905532
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:16:10.044564
# Unit test for constructor of class FuxIE
def test_FuxIE():
    test_video_url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    FuxIE(FuxIE.ie_key())._real_extract(test_video_url)


# Generated at 2022-06-14 16:16:21.778448
# Unit test for constructor of class FourTubeIE

# Generated at 2022-06-14 16:16:31.404788
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    ie = FuxIE()
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    ie = PornTubeIE()
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    ie = PornerBrosIE()

# Generated at 2022-06-14 16:16:35.880916
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from .common import InfoExtractor
    import unittest


    class Test(unittest.TestCase):
        def test_4tubeIE(self):
            InfoExtractor('4tube')
        def test_FuxIE(self):
            InfoExtractor('Fux')
        def test_PornTubeIE(self):
            InfoExtractor('PornTube')
        def test_PornerBrosIE(self):
            InfoExtractor('PornerBros')


    unittest.main()

# Generated at 2022-06-14 16:16:37.040335
# Unit test for constructor of class PornTubeIE

# Generated at 2022-06-14 16:16:42.718969
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .test_common import BaseTestCase
    from .. import YoutubeIE
    from ..utils import asset

    try:
        from ..jsinterp import JSInterpreter
    except ImportError:
        JSInterpreter = None

    class FourTubeTestCase(BaseTestCase):
        def setUp(self):
            BaseTestCase.setUp(self)
            self.interpreter = JSInterpreter()

        def assert_extract(self, url, expected):
            self.assertEqual(self.interpreter.extract(url), expected)

    ie = FourTubeIE(FourTubeTestCase())
    url = 'https://www.tubegalore.com/embed/777913'
    webpage = asset(compat_urlparse.urlparse(url).path.split('/')[-1])

    info = ie

# Generated at 2022-06-14 16:16:43.336312
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    str_or_none('1')

# Generated at 2022-06-14 16:16:53.132784
# Unit test for constructor of class PornTubeIE

# Generated at 2022-06-14 16:18:05.067008
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from .test_downloads import _get_testcases_1
    for t in _get_testcases_1():
        m = PornTubeIE(t['url'])
        m.extract()

# Generated at 2022-06-14 16:18:07.935633
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE(PornerBrosIE._VALID_URL, None)

# Generated at 2022-06-14 16:18:09.789770
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie.IE_NAME == 'PornerBros'

# Generated at 2022-06-14 16:18:15.355046
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    fourTubeBaseIE = FourTubeBaseIE()
    if(fourTubeBaseIE._TKN_HOST == 'token.4tube.com'):
        print("it's 4tube class")
    elif(fourTubeBaseIE._TKN_HOST == 'token.fux.com'):
        print("it's fux class")
    elif(fourTubeBaseIE._TKN_HOST == 'tkn.porntube.com'):
        print("it's porntube class")
    else:
        print("it's pornerbros class")

# Generated at 2022-06-14 16:18:16.926759
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:18:17.680063
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE('FourTube')
    print (ie._TKN_HOST)

# Generated at 2022-06-14 16:18:27.515022
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        import urllib3
    except ImportError:
        raise ImportError('To run unit-tests at least urllib3 is required.')
    from ..downloadermiddleware import DownloaderMiddlewareManager

    from .common import FakeYDL, FakeDownloader

    # For fixing "MaxRetryError: HTTPConnectionPool(...) has no connection available" errors
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # create FakeDownloader with middleware for PornTubeIE
    FakeDownloader.middleware_manager = DownloaderMiddlewareManager(
        FakeYDL(), [PornTubeIE.ie_key()])

    url = 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    video = PornTubeIE()._

# Generated at 2022-06-14 16:18:28.444333
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # Unit-test to ensure the class can be created
    FuxIE(None)


# Generated at 2022-06-14 16:18:29.401775
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    gutil.assert_fails_with(AssertionError, PornTubeIE, 'xxx')

# Generated at 2022-06-14 16:18:33.539461
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Testing the FourTubeIE class
    # and checking if the constructor is the same as FourTubeBaseIE
    assert FourTubeIE.__name__ == FourTubeBaseIE.__name__

    # Testing the FuxIE class
    # and checking if the constructor is the same as FourTubeBaseIE
    assert FuxIE.__name__ == FourTubeBaseIE.__name__

    # Testing the PornTubeIE class
    # and checking if the constructor is the same as FourTubeBaseIE
    assert PornTubeIE.__name__ == FourTubeBaseIE.__name__

    # Testing the PornerBrosIE class
    # and checking if the constructor is the same as FourTubeBaseIE
    assert PornerBrosIE.__name__ == FourTubeBaseIE.__name__

# Generated at 2022-06-14 16:21:51.161010
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    ie.extract('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')


# Generated at 2022-06-14 16:21:52.832630
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie_instance = PornTubeIE()
    assert isinstance(ie_instance, PornTubeIE)

# Generated at 2022-06-14 16:21:54.103214
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    obj = FourTubeBaseIE()
    assert obj._TKN_HOST != None

# Generated at 2022-06-14 16:21:56.210813
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE(None)._TESTS[0]['url'].startswith('https://www.pornerbros.com/videos/')

# Generated at 2022-06-14 16:22:01.567165
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    x = PornTubeIE()
    assert x.IE_NAME == 'porntube'
    assert x.IE_DESC == 'Pornhub, RedTube, YouPorn, Tube8, Beeg, SpankWire, KeezMovies, PornMD and more'
    assert x._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert x._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert x._TKN_HOST == 'tkn.porntube.com'
    assert len(x._TESTS) == 3

# Generated at 2022-06-14 16:22:02.674099
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE('http://fux.com')

# Generated at 2022-06-14 16:22:12.639913
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    video = FourTubeIE()
    url = 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert video.suitable(url)
    assert video.IE_NAME == '4tube'
    assert video.IE_DESC == '4Tube is a porn tube site with tens of thousands of videos, which stream free to you in high quality.'
    assert video.VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

# Generated at 2022-06-14 16:22:14.587083
# Unit test for constructor of class FuxIE
def test_FuxIE():
    """
    Unit test for instantiation of class FuxIE()
    """
    fux = FuxIE()

# Generated at 2022-06-14 16:22:18.041548
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():

    # Make sure it's instance is not None
    class_FourTubeIE_Instance = FourTubeIE()
    assert class_FourTubeIE_Instance is not None

    # Make sure its name is correct
    assert class_FourTubeIE_Instance.IE_NAME == "4tube"


# Generated at 2022-06-14 16:22:25.313788
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    assert PornTubeIE()._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert PornTubeIE()._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert PornTubeIE()._TKN_HOST == 'tkn.porntube.com'
    assert PornTubeIE()._TESTS
    assert PornTubeIE()._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'