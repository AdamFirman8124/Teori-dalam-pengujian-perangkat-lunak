

# Generated at 2022-06-14 17:16:32.632785
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:32.983480
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()

# Generated at 2022-06-14 17:16:36.641841
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE
    obj = ie()
    assert hasattr(obj, '_VALID_URL')
    assert hasattr(obj, '_TEST')
    assert hasattr(obj, '_real_extract')


# Generated at 2022-06-14 17:16:38.352627
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert trutv
    assert TruTVIE._TEST == trutv._real_extract(TruTVIE._TEST['url'])

# Generated at 2022-06-14 17:16:42.280131
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    inst = TruTVIE(url)
    assert inst.url == url
    assert inst.id == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
    assert inst.title == 'Sunlight-Activated Flower'
    assert inst.description == "A customer is stunned when he sees Michael's sunlight-activated flower."

# Generated at 2022-06-14 17:16:43.304396
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
    exit(1)

# Generated at 2022-06-14 17:16:43.681984
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTV()

# Generated at 2022-06-14 17:16:46.321091
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    #create instance of TruTVIE class
    trutv_ie = TruTVIE()
    #assert class object
    assert isinstance(trutv_ie, TruTVIE)

# Generated at 2022-06-14 17:16:57.780054
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    # Test if _VALID_URL works
    match = ie._VALID_URL.match('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert match
    assert match.group('series_slug') == 'the-carbonaro-effect'
    assert match.group('clip_slug') == 'sunlight-activated-flower'
    assert match.group('id') == None
    match = ie._VALID_URL.match('https://www.trutv.com/full-episodes/1015113/the-carbonaro-effect-snl-surprise.html')
    assert match
    assert match.group('series_slug') == 'the-carbonaro-effect'
    assert match.group('id')

# Generated at 2022-06-14 17:17:09.313596
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_TruTVIE = TruTVIE()
    assert TruTVIE._VALID_URL == "https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/([0-9A-Za-z-]+)/(?:videos/([0-9A-Za-z-]+)|(\d+))"
    assert TruTVIE._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE._TEST['info_dict']['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
    assert TruTVIE._TEST['info_dict']['ext'] == 'mp4'


# Generated at 2022-06-14 17:17:20.201114
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	v = TruTVIE()
	assert 'TruTV' in v._SITE_NAME

# Generated at 2022-06-14 17:17:26.208609
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z\-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z\-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:27.569430
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    a = TruTVIE()

# Generated at 2022-06-14 17:17:36.615905
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Data for testing
    test_data = {
        'url': 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
        'info_dict': {
            'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1',
            'ext': 'mp4',
            'title': 'Sunlight-Activated Flower',
            'description': "A customer is stunned when he sees Michael's sunlight-activated flower.",
        },
        'params': {
            # m3u8 download
            'skip_download': True,
        },
    }

    # Test TruTVIE constructor
    TruTVIE.test_return_value(test_data)

# Generated at 2022-06-14 17:17:37.340507
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:38.447542
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t is not None

# Generated at 2022-06-14 17:17:46.235866
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.ie_key() == 'TruTV'
    assert ie.ie_name() == 'TruTV'
    assert ie.ie_downloadable() == True
    assert ie.ie_filename() == 'trutv.com'
    assert ie._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:51.603981
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    #  Check if the class has the attributes of its super class TurnerBaseIE
    assert hasattr(t, '_VALID_URL') and hasattr(t, '_TEST') and hasattr(t, '_download_json') and hasattr(t, '_extract_ngtv_info')


# Generated at 2022-06-14 17:17:52.426809
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:56.645401
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:18:17.953664
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    youtube = TruTVIE()
    youtube.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:18:20.156687
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from tests.test_extractor import test_TruTVIE

    test_TruTVIE('TheCarbonaroEffect') # type: ignore

# Generated at 2022-06-14 17:18:21.520595
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test = TruTVIE()

# Generated at 2022-06-14 17:18:22.302329
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()

# Generated at 2022-06-14 17:18:23.240677
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert obj

# Generated at 2022-06-14 17:18:23.734076
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:24.203184
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE()

# Generated at 2022-06-14 17:18:36.249132
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv = TruTVIE()
    # test for method _download_json
    ttv._download_json("https://api.trutv.com/v2/web/episode/the-carbonaro-effect/116262", "116262")
    # test for method _extract_ngtv_info
    ttv._extract_ngtv_info("f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1", {}, {"url": "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html", "site_name": "truTV", "auth_required": False})

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:18:46.187299
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE.suitable(url) == True

    trutv_instance = TruTVIE(url)
    assert trutv_instance.suitable(url) == True

    url = 'http://www.trutv.com/full-episodes/4/4/2/index.html'
    assert TruTVIE.suitable(url) == True

    trutv_instance = TruTVIE(url)
    assert trutv_instance.suitable(url) == True

# Generated at 2022-06-14 17:18:49.587825
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .common import _test_constructor_exists
    _test_constructor_exists(TruTVIE)


# Generated at 2022-06-14 17:19:13.075582
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._TEST == TruTVIE._TEST

# Generated at 2022-06-14 17:19:14.356384
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """This is a test for the TruTVIE class"""
    True

# Generated at 2022-06-14 17:19:15.277850
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv = TruTVIE()



# Generated at 2022-06-14 17:19:22.759717
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:19:31.653866
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    global TruTVIE

    TruTVIE = TruTVIE()
    TruTVIE._download_json = lambda self, url, video_id: ""
    TruTVIE._extract_ngtv_info = lambda self, media_id, series_data, video_info: ""
    TruTVIE = TruTVIE()
    TruTVIE._download_json = lambda self, url, video_id: ""
    TruTVIE._extract_ngtv_info = lambda self, media_id, series_data, video_info: ""
    TruTVIE = TruTVIE()
    TruTVIE._download_json = lambda self, url, video_id: ""
    TruTVIE._extract_ngtv_info = lambda self, media_id, series_data, video_info: ""

# Generated at 2022-06-14 17:19:43.228398
# Unit test for constructor of class TruTVIE

# Generated at 2022-06-14 17:19:47.159152
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try: 
        TruTVIE()
    except:
        assert False, "Construction of class TruTVIE should be successful"


# Generated at 2022-06-14 17:19:54.673717
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE._TEST = {
    'info_dict': {
        'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1',
        'ext': 'mp4',
        'title': 'Sunlight-Activated Flower',
        'description': "A customer is stunned when he sees Michael's sunlight-activated flower.",
    },
    'params': {
        # m3u8 download
        'skip_download': True,
    },
}
    TruTVIE._VALID_URL = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    return TruTVIE

# Generated at 2022-06-14 17:19:58.022417
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.suitable("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")

# Generated at 2022-06-14 17:20:01.098077
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
  '''
    Test TruTVIE creation
  '''

  TruTVIE().extract("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")

# Generated at 2022-06-14 17:20:52.736300
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    # Arrange
    valid_url = r'http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    expected_series_slug = 'the-carbonaro-effect'
    expected_clip_slug = 'sunlight-activated-flower'
    expected_id = ''
    
    # Act
    TruTVIE(valid_url)
    
    # Assert
    if (TruTVIE._VALID_URL != valid_url) :
        raise Exception('_VALID_URL should be equal to valid_url')
    
    if (TruTVIE._TEST[ 'url' ] != valid_url) :
        raise Exception('_TEST[ \'url\' ] should be equal to valid_url')
    

# Generated at 2022-06-14 17:21:02.996094
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	assert TruTVIE._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
	assert TruTVIE.turner_guid == 'urn:ngc:video:tbs'
	assert TruTVIE.turner_channel_id == 4

# Generated at 2022-06-14 17:21:09.645140
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	ie = TruTVIE()
	assert (ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')

# Generated at 2022-06-14 17:21:19.912052
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Unit test for constructor of class TruTVIE.

    This is to test that the constructor for the truTVIE class
    is working as expected.
    """
    tru = TruTVIE()

    # Test if the regex in the constructor is properly set up
    assert(tru._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')
    # Test if _TEST object is properly set up
    assert(tru._TEST[0] == 'url')

# Generated at 2022-06-14 17:21:28.917080
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test = TruTVIE();
    test._real_extract("https://www.trutv.com/shows/tru-tv-top-funniest/videos/crazy-confrontations-and-nasty-fights.html");
    test._download_json("https://api.trutv.com/v2/web/series/clip/tru-tv-top-funniest/crazy-confrontations-and-nasty-fights", "crazy-confrontations-and-nasty-fights");

# Generated at 2022-06-14 17:21:40.125732
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .test import TestIE
    from .common import InfoExtractor

    class TestTruTVIE(TestIE):
        IE = InfoExtractor

        def __init__(self, *args, **kwargs):
            super(TestTruTVIE, self).__init__(*args, **kwargs)

        def _run_test(self, args):
            return super(TestTruTVIE, self)._run_test(args)

        def test_constructor(self):
            assert TruTVIE.__name__ == 'TruTVIE'
            assert TruTVIE.__bases__ == (TurnerBaseIE,)
            assert hasattr(TruTVIE, '_VALID_URL')

# Generated at 2022-06-14 17:21:41.007904
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:42.942728
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Unit test constructor class TruTVIE"""
    euro = TruTVIE()
    assert isinstance(euro, TurnerBaseIE)

# Generated at 2022-06-14 17:21:48.644356
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Check if TruTVIE correctly handles malformed URL
    malformed_url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/doesntexist.html'
    truTVIE = TruTVIE()
    # If an exception is raised, the test has passed
    try:
        truTVIE._real_extract(malformed_url)
    except:
        pass



# Generated at 2022-06-14 17:21:49.483770
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
    assert True

# Generated at 2022-06-14 17:22:47.923449
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE is not None

# Generated at 2022-06-14 17:22:51.390068
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvie = TruTVIE('id', 'title', 'description', 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert type(trutvie) == TruTVIE


# Generated at 2022-06-14 17:22:53.761343
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    xbmcgui.Dialog().ok('TruTVIE Unit Test', 'Test Succeeded!')

# Generated at 2022-06-14 17:22:56.845918
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:23:03.038007
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv = TruTVIE()
    assert ttv == TruTVIE()
    assert ttv._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'


# Generated at 2022-06-14 17:23:13.409114
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:15.049135
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:15.630530
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:17.681812
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('https://api.trutv.com/v2/web/episode/the-carbonaro-effect/551870/551870')

# Generated at 2022-06-14 17:23:20.473844
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test extraction from https://github.com/rg3/youtube-dl/issues/14597
    TruTVIE('https://www.trutv.com/shows/impractical-jokers/videos/murr-is-wired-to-a-lie-detector.html')

# Generated at 2022-06-14 17:25:19.173452
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:25:20.816422
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    content = "Importing module for TruTV"
    print(content)
    return

# Generated at 2022-06-14 17:25:22.698145
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert TruTVIE.__doc__ is not None



# Generated at 2022-06-14 17:25:30.378657
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tt = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert tt.valid_url == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert tt.extractor_key == 'TruTV'
    assert tt.display_id == 'sunlight-activated-flower'
    assert tt.video_id ==  'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
    assert tt.entries == []

# Generated at 2022-06-14 17:25:39.524431
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert(trutv._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')

# Generated at 2022-06-14 17:25:46.402839
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE(None)._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:25:47.677331
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._TEST

# Generated at 2022-06-14 17:25:48.278834
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:25:57.777208
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test 1: URL https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html
    # will extract info out of the URL
    extract_TruTVIE = TruTVIE().extract_info(
        'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    with open('test_TruTVIE.json', 'w') as f:
        json.dump(extract_TruTVIE, f)
    assert extract_TruTVIE['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'

    # Test 2: URL https://www.trutv.com/shows/the-carbonaro-effect

# Generated at 2022-06-14 17:25:58.335198
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()