

# Generated at 2022-06-14 16:13:37.888754
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    test_PornerBrosIE = PornerBrosIE()

# Generated at 2022-06-14 16:13:39.630806
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerBrosIE = PornerBrosIE()
    assert pornerBrosIE.IE_NAME == "pornerbros"

# Generated at 2022-06-14 16:13:42.268816
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie_class = PornerBrosIE()
    ie_instance = ie_class(PornerBrosIE.ie_key())
    assert isinstance(ie_instance, PornerBrosIE)

# Generated at 2022-06-14 16:13:55.562338
# Unit test for constructor of class FourTubeIE

# Generated at 2022-06-14 16:14:00.813530
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE._VALID_URL = r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    PornTubeIE._URL_TEMPLATE = 'https://www.porntube.com/videos/video_%s'
    PornTubeIE._TKN_HOST = 'tkn.porntube.com'


# Generated at 2022-06-14 16:14:05.584489
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        FourTubeBaseIE('4tube')
        FourTubeBaseIE('fux')
        FourTubeBaseIE('porntube')
    except:
        assert False, 'Constructor of class FourTubeBaseIE failed'
    else:
        assert True

# Generated at 2022-06-14 16:14:07.109640
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()



# Generated at 2022-06-14 16:14:12.081782
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE()._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'


# Generated at 2022-06-14 16:14:15.909029
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    ie._URL_TEMPLATE

# Generated at 2022-06-14 16:14:20.233527
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert hasattr(ie, '_download_webpage')
    assert hasattr(ie, '_extract_formats')
    assert hasattr(ie, '_real_extract')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, '_VALID_URL')


# Generated at 2022-06-14 16:14:35.645708
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE()


# Generated at 2022-06-14 16:14:37.089099
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    assert issubclass(FourTubeBaseIE, InfoExtractor)

# Generated at 2022-06-14 16:14:45.726993
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    test_url1 = 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    test_url2 = 'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert FourTubeIE._VALID_URL == FourTubeIE()._VALID_URL
    assert FourTubeIE._TESTS[0]['url'] == test_url1
    assert FourTubeIE._TESTS[1]['url'] == test_url2

# Generated at 2022-06-14 16:14:52.328199
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie.IE_NAME == 'PornerBros'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2022-06-14 16:14:55.086519
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:15:01.980822
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    item = FourTubeBaseIE()
    assert item._TKN_HOST == 'token.4tube.com'
    item = PornTubeIE()
    assert item._TKN_HOST == 'tkn.porntube.com'
    item = PornerBrosIE()
    assert item._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:15:03.096239
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE(None, '')


# Generated at 2022-06-14 16:15:06.717016
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE('4tube')
    FourTubeBaseIE('fux')
    FourTubeBaseIE('porntube')
    FourTubeBaseIE('pornerbros')

# Generated at 2022-06-14 16:15:11.487243
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
	test_url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
	test_object = FourTubeIE()
	test_object.extract(test_url)

# Generated at 2022-06-14 16:15:12.167320
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()._extract_formats('url','vid','media','sources')

# Generated at 2022-06-14 16:15:41.345995
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    m = PornerBrosIE(None)
    assert m != None

# Generated at 2022-06-14 16:15:41.870701
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:15:44.598680
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # This test fails because IE is not registered.
    ie = PornTubeIE()
    assert ie.ie_key() == 'PornTube'
    assert ie.ie_key() == ie.IE_NAME
    # Retrieve url from ie_key
    url = ie._WORKING_URL

# Generated at 2022-06-14 16:15:55.065311
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fuxIE = FuxIE(InfoExtractor())
    assert fuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fuxIE._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:16:02.815822
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from .test import get_testcases
    for testcase in get_testcases(FourTubeIE, FourTubeIE.IE_NAME):
        yield testcase
    for testcase in get_testcases(FuxIE, FuxIE.IE_NAME):
        yield testcase
    for testcase in get_testcases(PornTubeIE, PornTubeIE.IE_NAME):
        yield testcase
    for testcase in get_testcases(PornerBrosIE, PornerBrosIE.IE_NAME):
        yield testcase

# Generated at 2022-06-14 16:16:05.001140
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    """Try to initiate an instance of class FourTubeBaseIE"""
    FourTubeBaseIE()


# Generated at 2022-06-14 16:16:05.758389
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pass

# Generated at 2022-06-14 16:16:07.368925
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    '''
    Test that PornTubeIE can be instantiated
    '''
    PornTubeIE()

# Generated at 2022-06-14 16:16:10.151452
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
     FourTubeIE()._real_extract("http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")

# Generated at 2022-06-14 16:16:11.008243
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE()

# Generated at 2022-06-14 16:16:44.463773
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    _ = PornTubeIE('https://www.porntube.com/')

# Generated at 2022-06-14 16:16:48.193155
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        # get IE
        IE = FourTubeBaseIE("", "", "")
    except:
        # if exception is raised (likely because of 
        # invalid parameters) then the test failed
        assert False

    # if no exception is raised, the test passed
    assert True


# Generated at 2022-06-14 16:16:52.005988
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    url = 'https://www.porntube.com/videos/squirting-teen-ballerina-ecg_1331406'
    ie = PornTubeIE()
    ie._real_extract(url)
    assert ie.IE_NAME == 'PornTube'


# Generated at 2022-06-14 16:16:54.995465
# Unit test for constructor of class FuxIE
def test_FuxIE():
    test_url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    ie = FuxIE()
    ie.extract(test_url)

# Generated at 2022-06-14 16:16:56.066491
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()


# Generated at 2022-06-14 16:17:01.029621
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    addon = PornTubeIE('PornTube', 'http://www.porntube.com/embed/181369', '181369')
    addon.extract()
    assert(addon.url != 'http://www.porntube.com/videos/video_181369')
    assert(addon.url == 'https://www.porntube.com/videos/video_181369')

# Generated at 2022-06-14 16:17:02.534610
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Fails to construct the PornTubeIE in python 2.7.14 and 3.7.3
    PornTubeIE()

# Generated at 2022-06-14 16:17:10.051175
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from youtube_dl import YoutubeDL
    from youtube_dl.extractor.fux import FuxIE
    from youtube_dl.utils import parse_duration
    import json

    time_stamp = "1489530038"
    duration = "585"
    title = "Hot Babe Holly Michaels gets her ass stuffed by black"
    media_id = "195359"
    sources = ["240", "480", "720", "1080"]

    ydl = YoutubeDL({
        'debug': True
    })
    # The best result is the first one
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(FuxIE())

    # Note that the last portion of the unit test is an assertion
    # to see that the expected duration is 585:
    # https://github.com/rg3

# Generated at 2022-06-14 16:17:13.249709
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    try:
        PornerBrosIE()
        print("Unit test for constructor of class PornerBrosIE is successful")
    except Exception as e:
        print("Unit test for constructor of class PornerBrosIE is failed\n{}".format(e))

# Generated at 2022-06-14 16:17:24.478630
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from .test import get_testcases
    from .test import list_testcases
    from .test import run_testcases
    from .test import print_testcases
    from .test import get_testcase_output_text
    from .test import fail_on_testcases_output_differences
    list_testcases(PornTubeIE, sys.modules[__name__], True)
    testCases = get_testcases(PornTubeIE, sys.modules[__name__])
    run_testcases(testCases)
    if fail_on_testcases_output_differences:
        print_testcases(testCases)
        for test_case in testCases:
            assert test_case.expected_output == test_case.output, 'Unexpected output:\n%s' % get_testcase_output_text

# Generated at 2022-06-14 16:18:44.821880
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Test extractor with empty class to run instance construction
    # and ensure no errors are thrown
    FourTubeBaseIE()


# Generated at 2022-06-14 16:18:46.964105
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE('www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2022-06-14 16:18:47.746832
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros = PornerBrosIE()

# Generated at 2022-06-14 16:18:49.330571
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE



# Generated at 2022-06-14 16:18:58.014434
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE(): 
    # Test with a completely random URL
    # It shouldnt work as the URL is completely random
    random_url="https://www.youtube.com"
    ie = FourTubeIE(random_url)
    assert ie != random_url
    
    # Test with a random URL which has the same hostname as the original URL
    # It shouldnt work
    random_url="https://www.4tube.com/random/"
    ie = FourTubeIE(random_url)
    assert ie != random_url
    
    # Test with a random URL wich has the same URL template as the original URL
    # It shouldnt work as the id is not valid
    random_url="https://www.4tube.com/videos/random/video"
    ie = FourTubeIE(random_url)
    assert ie != random_url
    
   

# Generated at 2022-06-14 16:19:03.930342
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux_ie = FuxIE()

    assert fux_ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fux_ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fux_ie._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:19:08.806581
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert hasattr(ie, "_VALID_URL")
    assert hasattr(ie, "_URL_TEMPLATE")
    assert hasattr(ie, "_TKN_HOST")
    assert hasattr(ie, "_TESTS")
    assert hasattr(ie, "_real_extract")
    assert hasattr(ie, "_extract_formats")

# Generated at 2022-06-14 16:19:12.957627
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    # Constructor of class PornerBrosIE should contain a parameter _VALID_URL
    pornerBrosIE = PornerBrosIE(PornerBrosIE._VALID_URL, PornerBrosIE._URL_TEMPLATE, PornerBrosIE._TKN_HOST)
    assert pornerBrosIE

# Generated at 2022-06-14 16:19:15.255072
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    try:
        ie._TKN_HOST
        ie._URL_TEMPLATE
    except Exception as e:
        assert False, e.message

# Generated at 2022-06-14 16:19:20.997391
# Unit test for constructor of class FuxIE
def test_FuxIE():
    class_ = FuxIE
    assert hasattr(class_, "_VALID_URL")
    assert hasattr(class_, "_URL_TEMPLATE")
    assert hasattr(class_, "_TKN_HOST")
    assert hasattr(class_, "_TESTS")


# Generated at 2022-06-14 16:22:22.263607
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, FourTubeBaseIE)

# Generated at 2022-06-14 16:22:32.412835
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Test for file:///
    url = 'file:///C:/Users/pavana/Desktop/pytube_video.html'
    ie = FourTubeBaseIE()
    # urllib.urlopen has been deprecated in Python 3.0
    # TODO: Need to remove this import
    from urllib.request import urlopen
    f = urlopen(url)
    webpage = f.read().decode('utf-8')
    assert ie._search_regex(r'<link rel="thumbnailUrl"[^>]+href="([^"]+)"', webpage, 'thumbnail', fatal=False) is not None
    assert ie._html_search_meta('uploadDate', webpage) is not None

# Generated at 2022-06-14 16:22:33.567253
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:22:37.451241
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE("FourTubeIE", "4tube.com")
    FourTubeBaseIE("FuxIE", "fux.com")
    FourTubeBaseIE("PornTubeIE", "porntube.com")
    FourTubeBaseIE("PornerBrosIE", "pornerbros.com")

# Generated at 2022-06-14 16:22:38.236111
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:22:41.592570
# Unit test for constructor of class FuxIE
def test_FuxIE():
    import pickle
    f = FuxIE("https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow")
    s = pickle.dumps(f)
    f1 = pickle.loads(s)


# Generated at 2022-06-14 16:22:42.720980
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:22:50.236367
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Test must fail because this class is abstract
    assert not issubclass(FourTubeIE, InfoExtractor)
    # Test requiring the abstract method to be implemented
    ie = FourTubeIE('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by')
    with pytest.raises(NotImplementedError):
        ie._real_extract("http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by")

# Generated at 2022-06-14 16:22:53.371854
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE('4tube', '4tube.com')
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.ie_key() == 'FourTube'
    assert ie.ie_name() == '4tube'



# Generated at 2022-06-14 16:23:00.603478
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():

    src = r'<script id=playerembed src="https://embed.porntube.com/embed/U2FsdGVkX19b4H4Zc%2BqvDwFx0xE1Mf0jKMbPpV7k9%2FgI7ZuYsTgT7TQjEorIthHr"></script>'
    result = FourTubeIE._parse_json(src = src)

    assert(len(result) is 2)
    assert(result[0] is "asbfasdfasfaefawegawegawegwagag")
    assert(result[1] is "asdfasdfasdfasdfasdfasdf")