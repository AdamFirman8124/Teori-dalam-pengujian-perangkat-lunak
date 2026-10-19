

# Generated at 2022-06-14 16:13:45.674594
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros = PornerBrosIE()
    assert pornerbros.IE_NAME == 'pornerbros'

# Generated at 2022-06-14 16:13:51.100457
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # invalid http code
    assert FourTubeIE._VALID_URL.match(
        "http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")
    
    # invalid id
    assert FourTubeIE._VALID_URL.match(
        "http://www.4tube.com/videos/-1/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")
    
    # invalid id
    assert FourTubeIE._VALID_URL.match(
        "http://www.4tube.com/videos/XXXXXX/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")
    
    # invalid id
   

# Generated at 2022-06-14 16:13:51.742529
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()


# Generated at 2022-06-14 16:13:52.558458
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    globals()['FourTubeBaseIE'](None)

# Generated at 2022-06-14 16:13:59.501777
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    url = 'https://www.porntube.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    mobj = re.match(FourTubeBaseIE._VALID_URL, url)
    assert mobj
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

# Generated at 2022-06-14 16:14:12.894992
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    parse_duration('PT5M57S')

# Generated at 2022-06-14 16:14:22.895872
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Test case in which no argument is passed
    with pytest.raises(TypeError):
        FourTubeIE()
    # Test case in which wrong number of arguments is passed
    with pytest.raises(TypeError):
        FourTubeIE('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black', 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    # Test case in which wrong type of argument is passed
    with pytest.raises(TypeError):
        FourTubeIE(1)
    # Test case in which an invalid argument is passed

# Generated at 2022-06-14 16:14:35.403612
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    import unittest, os
    from youtube_dl.utils import DownloadError
    from youtube_dl.tests import FakeYDL

    class TestFourTubeBaseIE(unittest.TestCase):
        def setUp(self):
            self.ydl = FakeYDL()
            self.url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

# Generated at 2022-06-14 16:14:43.105261
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():

    ie = FourTubeIE()
    assert ie.IE_NAME == "4tube"
    assert ie._VALID_URL == "https?://(?:(?P<kind>www|m)\\.)?4tube\\.com/(?:videos|embed)/(?P<id>\\d+)(?:/(?P<display_id>[^/?#&]+))?"
    assert ie._URL_TEMPLATE == "https://www.4tube.com/videos/%s/video"
    assert ie._TKN_HOST == "token.4tube.com"

# Generated at 2022-06-14 16:14:44.090752
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()._TESTS

# Generated at 2022-06-14 16:15:02.409215
# Unit test for constructor of class FuxIE
def test_FuxIE():
    test_object = FuxIE('http://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2022-06-14 16:15:03.110318
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:15:15.383300
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    with FourTubeBaseIE as ie:
        assert ie.IE_NAME == '4tube'
        assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
        assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
        assert ie._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:15:16.744207
# Unit test for constructor of class FuxIE
def test_FuxIE():
    try:
        FuxIE()
        return True
    except Exception:
        return False

# Generated at 2022-06-14 16:15:19.345974
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try:
        assert FourTubeIE._TKN_HOST == "token.4tube.com"
    except:
        assert False, "Constructor of class FourTubeIE could not be tested"


# Generated at 2022-06-14 16:15:22.135639
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    a=PornerBrosIE()
    a._TESTS
    a._VALID_URL
    a._URL_TEMPLATE
    a._TKN_HOST
    a.test_PornerBrosIE

# Generated at 2022-06-14 16:15:23.246342
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.ie_key() == '4tube'

# Generated at 2022-06-14 16:15:25.059968
# Unit test for constructor of class FuxIE
def test_FuxIE():
    """
    Construye una instancia de la clase FuxIE, para verificar 
    que el constructor funciona correctamente.
    """
    FuxIE()

# Generated at 2022-06-14 16:15:26.264124
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE('https://www.porntube.com/embed/7089759')


# Generated at 2022-06-14 16:15:26.925372
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE().IE_NAME == '4tube'

# Generated at 2022-06-14 16:15:56.891583
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE(FuxIE.IE_NAME)



# Generated at 2022-06-14 16:16:07.533033
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ConstructorTest(FourTubeIE, default_fatal=True, wrong_args=['http://www.4tube.com/teens/'])()
    ConstructorTest(FourTubeIE, default_fatal=True, wrong_args=['http://www.4tube.com/channels/wcp-club/'])()
    ConstructorTest(PornerBrosIE, default_fatal=True, wrong_args=['http://www.pornerbros.com/channels/pornerbros-hd/'])()
    ConstructorTest(PornerBrosIE, default_fatal=True, wrong_args=['http://www.pornerbros.com/channels/'])()

# Generated at 2022-06-14 16:16:09.411429
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Test construction and superclass getter.
    fourtube_ie = FourTubeBaseIE()
    assert fourtube_ie.name == '4tube'

# Generated at 2022-06-14 16:16:14.002528
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.TEST_BASE_URL == 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    assert ie.TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:16:17.604596
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    input_url = "http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black"
    result = FourTubeBaseIE(input_url)

# Generated at 2022-06-14 16:16:21.060349
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
	# Constructor of class FourTubeIE
	instance = FourTubeIE()
	instance = PornTubeIE()
	instance = FuxIE()


# Test for method _extract_formats of class FourTubeIE

# Generated at 2022-06-14 16:16:25.237911
# Unit test for constructor of class FuxIE
def test_FuxIE():
    video_url = 'https://www.fux.com/videos/195359/awesome-fucking-kitchen-ends-cum-swallow'
    ie = FuxIE().get_info_extractor(url=video_url)
    assert ie.IE_NAME == '4tube'

# Generated at 2022-06-14 16:16:26.955800
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.IE_NAME == 'fux'


# Generated at 2022-06-14 16:16:28.357860
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    _constructor_test(PornTubeIE, True, True)


# Generated at 2022-06-14 16:16:30.292125
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Just to make sure that the constructor is not crashed unexpectedly,
    # no expection will be triggered since there is no 'args' dictionary passed.
    fourTubeIE = FourTubeIE(FourTubeIE.IE_NAME, {})
    assert(fourTubeIE.ie_key() == FourTubeIE.IE_NAME)

# Generated at 2022-06-14 16:17:30.407770
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE();

# Generated at 2022-06-14 16:17:32.618882
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Test the constructor.
    ft = FourTubeIE()
    assert ft is not None


# Generated at 2022-06-14 16:17:33.446082
# Unit test for constructor of class FuxIE
def test_FuxIE():
    testObj = FuxIE()

# Generated at 2022-06-14 16:17:34.355393
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from . import FourTubeBaseIE
    assert(FourTubeBaseIE == FourTubeBaseIE)

# Generated at 2022-06-14 16:17:37.126654
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    assert issubclass(FourTubeIE, FourTubeBaseIE)
    assert issubclass(FuxIE, FourTubeBaseIE)
    assert issubclass(PornTubeIE, FourTubeBaseIE)
    assert issubclass(PornerBrosIE, FourTubeBaseIE)

# Generated at 2022-06-14 16:17:37.667987
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE

# Generated at 2022-06-14 16:17:40.762815
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # test the constructor
    fux_obj = FuxIE('test_fux_obj')
    assert fux_obj.IE_NAME == '4tube'

# Generated at 2022-06-14 16:17:43.814571
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Test basic functionality
    obj = FourTubeBaseIE()
    assert isinstance(obj._TESTS, list)
    # Check if tests are updated conditionally
    if not obj._TEST_CASES:
        assert not obj._TESTS

# Generated at 2022-06-14 16:17:44.590002
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    f = FourTubeIE()

# Generated at 2022-06-14 16:17:45.891533
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
	ie = FourTubeBaseIE()
	print("==> Constructor for %s -- OK" % ie.IE_NAME)

# Generated at 2022-06-14 16:20:24.872372
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:20:26.766616
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._TESTS[0]['url'] == ie._VALID_URL

# Generated at 2022-06-14 16:20:36.396496
# Unit test for constructor of class FuxIE

# Generated at 2022-06-14 16:20:40.747554
# Unit test for constructor of class FuxIE
def test_FuxIE():
    x = FuxIE()
    i = 0
    for name in dir(x):
        t = type(getattr(x, name))
        if t == str or t == int or t == list or t == dict or t == tuple or t == unicode:
            i += 1
    assert i == 10


# Generated at 2022-06-14 16:20:46.298249
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE("http://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369")
    assert ie._VALID_URL == "https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)"
    assert ie._URL_TEMPLATE == "https://www.pornerbros.com/videos/video_%s"
    assert ie._TKN_HOST == "token.pornerbros.com"

# Generated at 2022-06-14 16:20:48.341683
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE("https://www.fux.com/embed/195359")

# Generated at 2022-06-14 16:20:53.150239
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert not hasattr(FourTubeIE, '_get_token')
    assert issubclass(FuxIE, FourTubeIE)
    assert hasattr(FuxIE, '_get_token')
    assert hasattr(PornTubeIE, '_get_token')
    assert hasattr(PornerBrosIE, '_get_token')
 

# Generated at 2022-06-14 16:21:00.422739
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

# Generated at 2022-06-14 16:21:03.850766
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert(PornerBrosIE.__name__ is 'PornerBrosIE')
    assert(PornerBrosIE.__doc__ is PornerBrosIE.__init__.__doc__)
    assert('pornerbros.com/videos' in PornerBrosIE._VALID_URL)

# Generated at 2022-06-14 16:21:15.608701
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    print(ie)
    assert ie.IE_NAME == '4tube'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._TESTS[0]['url'] == 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
   