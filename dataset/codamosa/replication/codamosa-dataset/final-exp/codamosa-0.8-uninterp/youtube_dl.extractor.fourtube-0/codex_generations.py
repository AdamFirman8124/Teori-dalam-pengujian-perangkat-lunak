

# Generated at 2022-06-14 16:13:41.252587
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()._extract_formats('https://www.porntube.com/videos/xxx', 'xxx', 'xxx', ['720'])

# Generated at 2022-06-14 16:13:43.742570
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    import Bootstrap # import Bootstrapt
    Bootstrap.YT_SERVICE_API_URL = 'https://www.4tube.com/api/'
    obj = FourTubeIE()
    assert obj

# Generated at 2022-06-14 16:13:56.661589
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    url = 'https://www.porntube.com/embed/7089759'
    PornTubeIE()._real_extract(url)
    url = 'https://m.porntube.com/embed/7089759'
    PornTubeIE()._real_extract(url)
    url = 'https://www.porntube.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    PornTubeIE()._real_extract(url)
    url = 'https://m.porntube.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    PornTubeIE()._real_extract(url)

# Generated at 2022-06-14 16:14:00.947084
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
  assertion_status = True

  try:
    FourTubeIE('FourTubeIE')
  except AssertionError:
    assertion_status = False

  if assertion_status is False:
    raise AssertionError("Unit test of class FourTubeIE: Assertion Error")

# Generated at 2022-06-14 16:14:13.264782
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from ..utils import (
        uniqify_list,
    )
    ftb = FourTubeBaseIE()
    assert ftb.IE_NAME == '4tube'
    assert ftb._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ftb._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ftb._TKN_HOST == 'token.4tube.com'

    # uniqify_list
    assert uniqify_list([1, 2, 1]) == [1, 2]

# Generated at 2022-06-14 16:14:17.197237
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros = PornerBrosIE()
    pornerbros._TESTS
    pornerbros._VALID_URL
    pornerbros._URL_TEMPLATE
    pornerbros._TKN_HOST

# Generated at 2022-06-14 16:14:18.468763
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # todo: implement test_FuxIE
    pass


# Generated at 2022-06-14 16:14:20.445897
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        PornTubeIE
    except NameError:
        assert False, "PornTubeIE not defined"


# Unit tests for class PornHubIE

# Generated at 2022-06-14 16:14:23.457030
# Unit test for constructor of class FuxIE
def test_FuxIE():
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    FuxIE()._real_extract(url)

# Generated at 2022-06-14 16:14:25.338954
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE({})
    # test adding value to upload_date



# Generated at 2022-06-14 16:14:46.437510
# Unit test for constructor of class FuxIE
def test_FuxIE():
    import unittest
    class TestFuxIE(unittest.TestCase):
        def setUp(self):
            self.ie = FuxIE()

# Generated at 2022-06-14 16:14:48.209440
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # TODO: set these arguments
    url = ''
    ie = FourTubeBaseIE(url)
    # Test _real_extract method
    ie.extract(url)



# Generated at 2022-06-14 16:14:49.062513
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE() is not None


# Generated at 2022-06-14 16:14:50.043879
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    assert PornTubeIE._TKN_HOST == 'tkn.porntube.com'

# Generated at 2022-06-14 16:14:51.645959
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from pornhub.extractor import PornTubeIE
    from pornhub.extractor import PornHubIE
    from pornhub.extractor import PornHubEmbedIE

# Generated at 2022-06-14 16:14:52.170770
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    assert PornTubeIE

# Generated at 2022-06-14 16:14:53.282759
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .. import FuxIE
    assert FuxIE


# Generated at 2022-06-14 16:14:53.840312
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()

# Generated at 2022-06-14 16:14:55.152533
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE('http://www.pornerbros.com/videos/video_181369')

# Generated at 2022-06-14 16:15:06.716554
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    porner_bros_ie = PornerBrosIE()
    porner_bros_ie.IE_NAME = 'pornerbros'
    porner_bros_ie._VALID_URL = r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    porner_bros_ie._URL_TEMPLATE = 'https://www.pornerbros.com/videos/video_%s'
    porner_bros_ie._TKN_HOST = 'token.pornerbros.com'

# Generated at 2022-06-14 16:15:38.333908
# Unit test for constructor of class FuxIE
def test_FuxIE():
    url = 'http://www.fux.com/embed/195359'
    FuxIE()._real_extract(url)

# Generated at 2022-06-14 16:15:39.500206
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE()._VALID_URL == _VALID_URL

# Generated at 2022-06-14 16:15:44.276355
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    testsuite = unittest.TestSuite()
    loader = unittest.TestLoader()
    testsuite.addTest(loader.loadTestsFromTestCase(PornerBrosIE))
    runner = unittest.TextTestRunner()
    runner.run(testsuite)

if __name__ == '__main__':
    test_PornerBrosIE()

# Generated at 2022-06-14 16:15:46.783342
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # constructor test.
    instance = FourTubeIE()

    # check data_regex property.
    assert hasattr(instance, 'data_regex')
    assert not instance.data_regex.match("")
    assert instance.data_regex.match("foo")

# Generated at 2022-06-14 16:15:47.736138
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ZJDFWG=FourTubeIE()


# Generated at 2022-06-14 16:15:50.808704
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    for ie in [FourTubeIE(), FuxIE(), PornTubeIE(), PornerBrosIE()]:
        assert isinstance(ie, FourTubeBaseIE)

# Generated at 2022-06-14 16:15:53.050390
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try:
        FourTubeIE()
    except NameError as e:
        print(e)

# Generated at 2022-06-14 16:16:00.179257
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from .test_suites import Youtube_1
    import __main__
    import sys
    try:
        module = __main__
    except NameError:
        module = sys.modules[__name__]
    if (
        'test_suites/' in module.__file__ and not isinstance(PornTubeIE, Youtube_1)
    ):
        raise Exception('Wrong constructor: not directly inherit from object')

# Generated at 2022-06-14 16:16:01.029286
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:16:02.585601
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert 'PornerBrosIE' in globals()



# Generated at 2022-06-14 16:17:06.438833
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE('FourTubeBaseIE')
    assert ie._VALID_URL is not None

# Generated at 2022-06-14 16:17:10.683788
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    import requests
    fourtube = FourTubeBaseIE()
    url = 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    try:
        webpage, urlh = fourtube._download_webpage_handle(url, 'test_video')
    except requests.exceptions.HTTPError:
        webpage = ''

# Generated at 2022-06-14 16:17:14.839461
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    fail = True
    try:
        PornerBrosIE('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    except:
        fail = False
    assert(fail) # If the constructor fails, the test has passed.

# Generated at 2022-06-14 16:17:16.824955
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    p = PornerBrosIE()
    assert "PornerBrosIE" in str(p)

# Generated at 2022-06-14 16:17:24.571952
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2022-06-14 16:17:26.025507
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE(FourTubeBaseIE())

# Generated at 2022-06-14 16:17:33.887191
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # Create the class
    video = FuxIE()

    # Check that the URL is well formed
    url = "https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow"

    # Fetch the webpage
    webpage = video._download_webpage(url)
    print(webpage)

    # Parse the webpage
    data = video._parse_json(video._search_regex(
            r'INITIALSTATE\s*=\s*(["\'])(?P<value>(?:(?!\1).)+)\1',
            webpage, 'data', group='value')
        )
    print(data)

# Generated at 2022-06-14 16:17:40.680804
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    url_1 = 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    url_2 = 'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    regex_1 = r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

# Generated at 2022-06-14 16:17:44.830793
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    class test(FourTubeBaseIE):
        pass
    assert test._URL_TEMPLATE == FourTubeBaseIE._URL_TEMPLATE
    assert test._VALID_URL == FourTubeBaseIE._VALID_URL
    assert test._TESTS == FourTubeBaseIE._TESTS
    assert test._TKN_HOST == FourTubeBaseIE._TKN_HOST

# Generated at 2022-06-14 16:17:46.681567
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    IE = PornTubeIE()
    assert IE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'

# Generated at 2022-06-14 16:20:55.937974
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    class TestIE(FourTubeBaseIE):
        IE_NAME = 'Example'
        _TKN_HOST = 'example.com'
        _URL_TEMPLATE = 'https://example.com/%s'
        _VALID_URL = r'https://example\.com/(?P<id>\d+)'

    ie = TestIE()
    assert ie._TKN_HOST == 'example.com'
    assert ie._URL_TEMPLATE == 'https://example.com/%s'
    assert ie._VALID_URL == r'https://example\.com/(?P<id>\d+)'

# Generated at 2022-06-14 16:21:05.574176
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    video_data = {
        'id': '209733',
        'ext': 'mp4',
        'title': 'Hot Babe Holly Michaels gets her ass stuffed by black',
        'uploader': 'WCP Club',
        'uploader_id': 'wcp-club',
        'upload_date': '20131031',
        'timestamp': 1383263892,
        'duration': 583,
        'view_count': None,
        'like_count': None,
        'categories': None,
        'age_limit': 18,
    }
    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    obj = FourTubeBaseIE()
    obj._extract_

# Generated at 2022-06-14 16:21:16.204679
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    assert FourTubeBaseIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert FourTubeBaseIE._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert FourTubeBaseIE._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:21:17.092191
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()


# Generated at 2022-06-14 16:21:19.037714
# Unit test for constructor of class FuxIE
def test_FuxIE():
    for ie in [FuxIE, FourTubeIE, FourTubeBaseIE]:
        instance = ie()
        assert isinstance(instance, FourTubeBaseIE)

# Generated at 2022-06-14 16:21:20.102156
# Unit test for constructor of class FuxIE
def test_FuxIE():
    f = FuxIE('Fux')
    assert f


# Generated at 2022-06-14 16:21:22.631505
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    # Check that token.pornerbros.com actually exists
    import requests
    hostname = 'token.pornerbros.com'
    r = requests.get('https://'+hostname)
    assert(r.status_code == 200)



# Generated at 2022-06-14 16:21:25.127970
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
	FourTubeIE()._real_extract("https://www.4tube.com/embed/209733")


# Generated at 2022-06-14 16:21:26.817138
# Unit test for constructor of class FuxIE
def test_FuxIE():
    obj = FuxIE("a")
    assert obj


# Generated at 2022-06-14 16:21:31.677091
# Unit test for constructor of class FuxIE
def test_FuxIE():
    class_ = FuxIE
    #FuxIE.__init__(class_)
    assert '_TKN_HOST' in dir(class_)
    assert '_URL_TEMPLATE' in dir(class_)
    assert '_VALID_URL' in dir(class_)

