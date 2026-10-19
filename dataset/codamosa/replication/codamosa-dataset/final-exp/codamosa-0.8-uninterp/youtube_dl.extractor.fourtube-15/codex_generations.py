

# Generated at 2022-06-14 16:13:39.674921
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        info_extractor = FourTubeBaseIE()
        info_extractor = FuxIE()
        info_extractor = PornTubeIE()
        info_extractor = PornerBrosIE()
    except Exception:
        pass

# Generated at 2022-06-14 16:13:41.631062
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        FourTubeBaseIE()
    except TypeError:
        assert False, 'class FourTubeBaseIE should not be abstract'

# Generated at 2022-06-14 16:13:42.563318
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    l = FourTubeIE()

# Generated at 2022-06-14 16:13:43.562571
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    assert FourTubeBaseIE(None) is not None

# Generated at 2022-06-14 16:13:50.362375
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    obj = PornerBrosIE()
    assert (obj._VALID_URL) == 'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'


# Generated at 2022-06-14 16:13:52.560902
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie_class = FourTubeBaseIE
    ie_class()

# Generated at 2022-06-14 16:13:54.950296
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    class TestIE(FourTubeBaseIE):
        pass
    assert TestIE.__name__ == "TestIE"
    assert TestIE.__doc__.split("\n")[0] == "TestIE()"

# Generated at 2022-06-14 16:13:59.171425
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerBros_IE = PornerBrosIE()
    assert pornerBros_IE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'

# Generated at 2022-06-14 16:14:04.006200
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369');
    assert ie.IE_NAME == 'pornerbros';

# Generated at 2022-06-14 16:14:11.029696
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from . import _download_json
    downloader = _download_json()
    ie = FourTubeBaseIE(downloader)
    assert ie._download_json == downloader._download_webpage
    assert ie._html_search_meta == downloader._html_search_regex
    assert ie._html_search_regex == downloader._html_search_regex

# Generated at 2022-06-14 16:14:48.525561
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Tests a URL of video with a channel
    PornTubeIE()._real_extract('https://www.porntube.com/videos/squirting-teen-ballerina-ecg_1331406')
    # Tests a URL of video without a channel
    PornTubeIE()._real_extract('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    # Tests a URL of embedded video with a channel
    PornTubeIE()._real_extract('https://www.porntube.com/embed/1331406')
    # Tests a URL of embedded video without a channel
    PornTubeIE()._real_extract('https://www.porntube.com/embed/7089759')
    # Tests a URL of mobile video with a channel
    PornTubeIE()._real

# Generated at 2022-06-14 16:14:55.705517
# Unit test for constructor of class FuxIE
def test_FuxIE():

    # ------------------------------------------------
    # test with url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    # ------------------------------------------------
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    ie = FuxIE()
    mobj = re.match(ie._VALID_URL, url)
    video_id, display_id = mobj.group('id', 'display_id')

    # FuxIE._search_regex:
    #   tests:
    #       input:
    #           - pattern = r'INITIALSTATE\s*=\s*(["\'])(?P<value>(?:(?!\1).)+)\1'
    #           -

# Generated at 2022-06-14 16:15:05.596593
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    t = FourTubeIE()
    assert t._TKN_HOST == 'token.4tube.com'
    assert t._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert t._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'


test_FourTubeIE()

# Generated at 2022-06-14 16:15:06.953639
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    test_video = FourTubeIE()

# Generated at 2022-06-14 16:15:08.545800
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    p = PornTubeIE(None)
    assert p is not None


# Generated at 2022-06-14 16:15:09.923417
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    n = FourTubeBaseIE()
    print (n)

# Generated at 2022-06-14 16:15:16.173132
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestPornTubeIE(unittest.TestCase):
        def setUp(self):
            self.ie = PornTubeIE()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPornTubeIE)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-14 16:15:17.071762
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    _PornTubeIE()

# Generated at 2022-06-14 16:15:21.947049
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'


# Generated at 2022-06-14 16:15:22.703503
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)

# Generated at 2022-06-14 16:16:19.590274
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE("url")
    assert(ie!=None)

# Generated at 2022-06-14 16:16:23.754232
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    podnerbros = PornerBrosIE()
    if podnerbros.IE_NAME != 'pornerbros':
        raise ValueError('Expected "pornerbros" but got %s as IE_NAME' % podnerbros.IE_NAME)

# Generated at 2022-06-14 16:16:29.226124
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Constructor of class FourTubeBaseIE
    assert(FourTubeBaseIE is not None)

    # Constructor of class PornHubIE
    assert(PornHubIE is not None)

    # Constructor of class PornHubPlaylistIE
    assert(PornHubPlaylistIE is not None)

    # Constructor of class PornHubUserVideosIE
    assert(PornHubUserVideosIE is not None)

# Generated at 2022-06-14 16:16:30.385981
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Verifies that PornTubeIE constructor is working
    PornTubeIE()

# Generated at 2022-06-14 16:16:37.152007
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # ARRANGE
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    vid_id = '195359'
    expected_vid_id = '195359'
    expected_title = 'Awesome fucking in the kitchen ends with cum swallow'
    expected_uploader = 'alenci2342'
    expected_uploader_id = 'alenci2342'
    expected_upload_date = '20131230'
    expected_timestamp = 1388361660
    expected_duration = 289
    expected_view_count = int
    expected_like_count = int
    expected_categories = list
    expected_age_limit = 18

    # ACT
    fux_ie = FuxIE(url)
    vid_

# Generated at 2022-06-14 16:16:40.102810
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert issubclass(FourTubeIE, InfoExtractor)
    assert hasattr(FourTubeIE, '_VALID_URL')
    assert hasattr(FourTubeIE, '_URL_TEMPLATE')
    assert hasattr(FourTubeIE, '_TKN_HOST')
    assert hasattr(FourTubeIE, '_TESTS')


# Generated at 2022-06-14 16:16:42.176020
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    fourtube_ie = FourTubeIE()
    # constructor of class FourTubeIE should pass
    assert fourtube_ie



# Generated at 2022-06-14 16:16:44.969370
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    class_ = FourTubeIE
    constr = class_('4tube')
    assert constr is not None, "Failed to initialize 4tube"


# Generated at 2022-06-14 16:16:46.805665
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert(FuxIE()._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')

# Generated at 2022-06-14 16:16:53.218615
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
   test_url = 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
   test_display_id = extract_display_id(test_url)
   assert test_display_id == 'skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
   test_id = 181369
   assert test_id == 181369


# Generated at 2022-06-14 16:18:04.980851
# Unit test for constructor of class FuxIE
def test_FuxIE():
    url = 'https://www.fux.com/videos/195359/awesome-fucking-kitchen-ends-cum-swallow'
    ie = FuxIE()
    ie.extract(url)

# Generated at 2022-06-14 16:18:08.188228
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    f = FourTubeIE()
    assert f.__class__.__name__ == 'FourTubeIE'

# Generated at 2022-06-14 16:18:09.622527
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    f = FourTubeBaseIE()
    assert f is not None

# Generated at 2022-06-14 16:18:12.529890
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert ie._VALID_URL is None
    assert ie._URL_TEMPLATE is None
    assert ie._TKN_HOST is None
    assert ie._TESTS is None

# Generated at 2022-06-14 16:18:15.920898
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .test_FuxIE import FuxIE
    from .FuxIE import FuxIE
    from .FuxIE import FuxIE
    from .FuxIE import FuxIE
    from .FuxIE import FuxIE
    from .FuxIE import FuxIE
    from .FuxIE import FuxIE
    from .FuxIE import FuxIE

# Generated at 2022-06-14 16:18:17.653567
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    x = PornerBrosIE()
    assert isinstance(x, FourTubeBaseIE)

# Generated at 2022-06-14 16:18:19.994530
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE({'fetch': {'*': 'nop'}})  # Example of Dict[str, Callable]
    assert fux is not None

# Generated at 2022-06-14 16:18:20.926154
# Unit test for constructor of class FuxIE
def test_FuxIE():
    _FuxIE = FuxIE()

# Generated at 2022-06-14 16:18:21.984524
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    mt_ie = PornTubeIE()

# Generated at 2022-06-14 16:18:23.367897
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    obj = FourTubeIE()
    assert obj

# Generated at 2022-06-14 16:21:32.732155
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fuxIE = FuxIE("http://m.fux.com/videos/195359/awesome-fucking-kitchen-ends-cum-swallow")
    assert fuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fuxIE._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:21:44.917355
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    # Example url
    url = 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    # Result of url.parse_url()
    url_parse = {
        'scheme': 'https',
        'path': '/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',
        'base_path': '/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',
        'netloc': 'www.pornerbros.com',
        'params': '',
        'query': '',
        'fragment': '',
        'url': url
    }

    #

# Generated at 2022-06-14 16:21:45.462251
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:21:46.305479
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:21:47.560426
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

# Generated at 2022-06-14 16:21:52.143862
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    f = FourTubeIE()
    result = f._real_extract(url)
    assert result.get('id') == '209733'

# Generated at 2022-06-14 16:21:53.464680
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    assert PornTubeIE._TKN_HOST == 'tkn.porntube.com'

# Generated at 2022-06-14 16:21:55.274110
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # test class without subclassing
    ie = FourTubeIE()
    assert ie._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:22:01.231973
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    import json

    x = PornTubeIE({})
    x._parse_json('{"a": 1}', 'video_id')
    x._parse_json(b'{"a": 1}', 'video_id')
    str_or_none(None)
    try_get(None, lambda x: x['a'], 'b', compat_str)
    url_or_none(None)
    url_or_none('foo')
    assert json.loads(b'{"a": 1}') == {"a": 1}
    assert json.loads(b'{="a"}') != {"a": 1, "b": 2}

# Generated at 2022-06-14 16:22:12.264867
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    ie = FourTubeBaseIE()
    assert ie._VALID_URL == '(?i)https?://(?:(?P<kind>www|m)\.)?(?P<domain>4tube|fux|porntube|pornerbros)\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'