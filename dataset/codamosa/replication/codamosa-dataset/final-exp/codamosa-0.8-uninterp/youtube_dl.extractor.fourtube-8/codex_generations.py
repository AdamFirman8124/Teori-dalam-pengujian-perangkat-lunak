

# Generated at 2022-06-14 16:13:41.845081
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE._URL_TEMPLATE == "https://www.pornerbros.com/videos/video_%s"
    assert PornerBrosIE._TKN_HOST == "token.pornerbros.com"
    test_obj = PornerBrosIE("PornerBrosIE")
    assert test_obj._TKN_HOST == "token.pornerbros.com"
    assert test_obj._URL_TEMPLATE == "https://www.pornerbros.com/videos/video_%s"

# Generated at 2022-06-14 16:13:43.561046
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    obj = PornerBrosIE()
    assert obj.IE_NAME == 'pornerbros'

# Generated at 2022-06-14 16:13:48.026571
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE("test", {}, {}, {})
    assert ie._TKN_HOST == "token.4tube.com"

# Generated at 2022-06-14 16:13:50.085791
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        pornTube = PornTubeIE()
    except NameError as e:
        rai

# Generated at 2022-06-14 16:13:51.168412
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():

    assert PornerBrosIE is not None

# Generated at 2022-06-14 16:13:55.879252
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    constructor_test({
        'url': 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'only_matching': True,
    })

# Generated at 2022-06-14 16:13:58.010377
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    class_name = 'FourTubeIE'
    instance = globals()[class_name]()
    assert instance.IE_NAME == class_name

# Generated at 2022-06-14 16:13:59.908363
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:14:03.281582
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    porn_tube = PornTubeIE()

    # Tests if constructor of PornTubeIE instantiates a valid object
    assert porn_tube.__class__.__name__ is 'PornTubeIE'

# Generated at 2022-06-14 16:14:05.339498
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
	a = FourTubeBaseIE()
	assert a != None

# Generated at 2022-06-14 16:14:20.886668
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    t = FourTubeIE()

# Generated at 2022-06-14 16:14:24.432841
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Not actually logging in
    FourTubeBaseIE('4tube', 'waps')
    FourTubeBaseIE('fux', 'waps')
    FourTubeBaseIE('porntube', 'waps')
    FourTubeBaseIE('pornerbros', 'waps')

# Generated at 2022-06-14 16:14:36.152203
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    youtube_url = 'https://www.4tube.com/videos/411750/gorgeous-petite-blonde-jessie-rogers-gets-fuck'
    fux_url = 'https://www.fux.com/video/564878/elephant-tube/porn/dazzling-pornstar-in-crazy-fetish-sex-video'
    porntube_url = 'https://www.porntube.com/videos/fucking-the-tiny-teen-amateur-thai-cucumber-chick_7685124'
    pornerbros_url = 'https://www.pornerbros.com/videos/amateur-porn-fucking-my-teens-best-friend_438568'

# Generated at 2022-06-14 16:14:37.188438
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    four_tube = FourTubeIE()

# Generated at 2022-06-14 16:14:41.411233
# Unit test for constructor of class FuxIE
def test_FuxIE():
    """ constructor of class FuxIE"""
    obj = FuxIE()
    assert obj._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert obj._URL_TEMPLATE == r'https://www.fux.com/video/%s/video'
    assert obj._TKN_HOST == "token.fux.com"

# Generated at 2022-06-14 16:14:43.636974
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        FourTubeBaseIE('FourTubeBaseIE')
    except NameError as e:
        assert False
    assert True

# Generated at 2022-06-14 16:14:45.636880
# Unit test for constructor of class FuxIE
def test_FuxIE():
    test_url = "https://www.fux.com/embed/195359"
    FuxIE()._real_initialize(test_url)

# Generated at 2022-06-14 16:14:47.237403
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.__class__.__name__ == 'PornTubeIE'

# Generated at 2022-06-14 16:14:48.484087
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    from . import PornerBrosIE
    PornerBrosIE

# Generated at 2022-06-14 16:14:55.671429
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    class TestFourTubeIE(FourTubeBaseIE):
        _VALID_URL = r'https?://(?:(?P<kind>www|m)\.)?testtube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
        _URL_TEMPLATE = 'https://www.testtube.com/videos/%s/video'
        _TKN_HOST = 'token.testtube.com'
    assert issubclass(TestFourTubeIE, FourTubeBaseIE)

# Generated at 2022-06-14 16:15:27.129818
# Unit test for constructor of class FuxIE
def test_FuxIE():
    Fux = FuxIE()
    assert Fux._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert Fux._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert Fux._TKN_HOST == 'token.fux.com'
    assert Fux.IE_NAME == '4tube'
    assert Fux.IE_DESC == '4Tube and Fux'

# Generated at 2022-06-14 16:15:28.045128
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        FourTubeBaseIE.suitable("")
    except:
        assert False

# Generated at 2022-06-14 16:15:31.175607
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # This line is to test the correct instantiation of class object
    # The following lines are commented only to avoid the error
    # AttributeError: type object 'FourTubeIE' has no attribute '_VALID_URL'
    # ie = FourTubeBaseIE(FourTubeBaseIE._VALID_URL, FourTubeBaseIE._URL_TEMPLATE)
    return;

# Generated at 2022-06-14 16:15:32.101849
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert issubclass(PornerBrosIE, FourTubeBaseIE)

# Generated at 2022-06-14 16:15:32.578917
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:15:40.016280
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from .common import InfoExtractor
    m = FourTubeBaseIE._VALID_URL.match('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m

    ie = InfoExtractor()
    ie.add_info_extractor(FourTubeIE)
    ie.add_info_extractor(FuxIE)
    ie.add_info_extractor(PornTubeIE)
    ie.add_info_extractor(PornerBrosIE)

    info_dict = ie.extract('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

    # Only verifies

# Generated at 2022-06-14 16:15:44.523091
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert fux._VALID_URL == r'^https?://(?:www|m)\.(?P<host>fux|4tube|porntube)\.com/(?:(?:video|embed)/(?P<display_id>.*)|videos/(?P<display_id>[^/]+))$'

# Generated at 2022-06-14 16:15:45.272268
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    temp = FourTubeIE()
    print(temp)

# Generated at 2022-06-14 16:15:46.478571
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE(FuxIE.ie_key(), FuxIE._VALID_URL)

# Generated at 2022-06-14 16:15:47.191004
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    video = FourTubeIE()

# Generated at 2022-06-14 16:16:47.975728
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE()._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:16:49.415911
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    assert PornTubeIE.__name__ == 'PornTubeIE'

# Generated at 2022-06-14 16:16:53.176992
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    out = PornerBrosIE._download_webpage(PornerBrosIE, 'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert out is not None

# Generated at 2022-06-14 16:16:55.939481
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, FourTubeBaseIE)

# Generated at 2022-06-14 16:17:01.311788
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Source: https://www.youtube.com/watch?v=UaHlPfXZzrY
    url = 'https://www.porntube.com/videos/the-philosophy-of-the-bonglord_1163007'
    youtube_video = FourTubeBaseIE()._real_extract(url)
    assert youtube_video['id'] == '1163007'

# Generated at 2022-06-14 16:17:03.375289
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from .test_porn import TestPornIE
    TestPornIE.test_porn(PornTubeIE, 'PornTube')


# Generated at 2022-06-14 16:17:04.274596
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()._downloader = None



# Generated at 2022-06-14 16:17:06.968299
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        FourTubeBaseIE()
    except TypeError as e:
        assert "abstract class" in str(e)

# Generated at 2022-06-14 16:17:10.599518
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    from .common import InfoExtractor
    import mpy_cross
    assert issubclass(PornerBrosIE, InfoExtractor)
    assert issubclass(PornerBrosIE, mpy_cross.Mp4Dl)

# Generated at 2022-06-14 16:17:12.902397
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE()._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'

# Generated at 2022-06-14 16:19:53.644751
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
	url = 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
	i = PornerBrosIE()
	print(i._real_extract(url))

# Generated at 2022-06-14 16:19:57.983178
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    ie = FourTubeIE()
    ie.extract(url)


# Generated at 2022-06-14 16:20:00.330661
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        import fourtube
        fourtube.FourTubeBaseIE()
    except:
        raise AssertionError('FourTubeBaseIE constructor failed.')

# Generated at 2022-06-14 16:20:02.360702
# Unit test for constructor of class FuxIE
def test_FuxIE():
    """Check that FuxIE does not have any constructor errors"""
    try:
        FuxIE()
    except TypeError as e:
        assert False

# Generated at 2022-06-14 16:20:13.418523
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    import unittest
    class TestPornerBrosIE(unittest.TestCase):
        def test_urls(self):
            self.assertEqual(PornerBrosIE._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
            self.assertEqual(PornerBrosIE._URL_TEMPLATE, 'https://www.pornerbros.com/videos/video_%s')
            self.assertEqual(PornerBrosIE._TKN_HOST, 'token.pornerbros.com');
    unittest.main()

# Generated at 2022-06-14 16:20:16.327889
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    """
    Test if class FourTubeBaseIE is constructed right.
    """
    instance = FourTubeBaseIE()
    assert instance._TKN_HOST is not None
    assert 'FourTubeBaseIE' in instance.IE_NAME

# Generated at 2022-06-14 16:20:20.283045
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE()._TESTS[0]['url'] == 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

# Generated at 2022-06-14 16:20:21.257238
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()._real_initialize()

# Generated at 2022-06-14 16:20:27.622243
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()   # no crash, please
    assert ie.IE_NAME == 'PornTube'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2022-06-14 16:20:28.607462
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    mode = FourTubeIE()