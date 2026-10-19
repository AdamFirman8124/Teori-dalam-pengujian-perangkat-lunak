

# Generated at 2022-06-14 17:16:33.701858
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE("123")

# Generated at 2022-06-14 17:16:34.359820
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:42.941555
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    import unittest
    import sys
    import ytdl.extractor

    # Inherit from TestCase class from unittest module
    class ConstructorTestCase(unittest.TestCase):

        # Set up variables to test
        def setUp(self):

            # Set up extractor for class to test (YoutubeIE)
            self.ie = ytdl.extractor.get_info_extractor('trutv')

            # Set up constant values for testing
            self.url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
            self.path = 'episode'
            self.series_slug = 'the-carbonaro-effect'
            self.clip_slug = 'sunlight-activated-flower'

# Generated at 2022-06-14 17:16:46.813198
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	test_TruTVIE = TruTVIE();
	print(test_TruTVIE.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'));

test_TruTVIE();

# Generated at 2022-06-14 17:16:49.999159
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    m = TruTVIE(object())
    m.test()

# Generated at 2022-06-14 17:16:50.622695
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:51.660998
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    x = TruTVIE()
    assert x

# Generated at 2022-06-14 17:16:58.757255
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    video_url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    video_id = "f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1"
    title = "Sunlight-Activated Flower"
    description = "A customer is stunned when he sees Michael's sunlight-activated flower."
    y = TruTVIE()._real_extract(video_url)
    assert y['id'] == video_id
    assert y['title'] == title
    assert y['description'] == description

# Generated at 2022-06-14 17:16:59.446851
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:02.046340
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tru_tv_ie = TruTVIE()
    assert(tru_tv_ie.ie_key() == 'TruTV')

# Generated at 2022-06-14 17:17:08.267461
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Simple test case to check if the constructor works
    """
    TruTVIE()

# Generated at 2022-06-14 17:17:11.904468
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Create an instance of class TruTVIE
    trutvIE = TruTVIE()

    # Check if the instance of TruTVIE class is valid
    assert isinstance(trutvIE, TruTVIE)

    # Check if the instance of TruTVIE class is a subclass of TurnerBaseIE
    assert issubclass(TurnerBaseIE, TruTVIE)

# Generated at 2022-06-14 17:17:12.827261
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE


# Generated at 2022-06-14 17:17:13.532442
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:17.705979
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:27.376916
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    # Constructor of TurnerBaseIE
    assert trutv._TEST == trutv._TEST_TURNER
    assert trutv._TURNER_BASE_URL == 'https://ws.ngtv.com'
    assert trutv._TURNER_API_KEY == 'MnYzYTdkODNlMmMyNDRkMmU5MTA1ODY1ZDFkMzU5YTI='
    # Constructor of TruTVIE

# Generated at 2022-06-14 17:17:28.492876
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
  tru = TruTVIE()
  return

# Generated at 2022-06-14 17:17:30.188572
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv = TruTVIE();
    assert ttv is not None

# Generated at 2022-06-14 17:17:31.227454
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:32.856754
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # TruTVIE is a subclass of TurnerBaseIE, so test this class only when necessary
    TruTVIE();

# Generated at 2022-06-14 17:17:49.591198
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._BUILD_VHOST({'pi': 'prod', 'e': 'pc'}) == 'pc.prod.turner.com'
    assert TruTVIE._DOMAIN_TO_REGION['.de'] == 'eu'
    assert TruTVIE._DOMAIN_TO_REGION['.es'] == 'la'
    assert TruTVIE._DOMAIN_TO_REGION['.mx'] == 'la'
    assert TruTVIE._DOMAIN_TO_REGION['.nl'] == 'eu'
    assert TruTVIE._DOMAIN_TO_REGION['.pl'] == 'eu'
    assert TruTVIE._DOMAIN_TO_REGION['.pt'] == 'la'
    assert TruTVIE._DOMAIN_TO_REGION['.tv'] == 'la'
    assert TruTVIE

# Generated at 2022-06-14 17:17:50.262353
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE()

# Generated at 2022-06-14 17:17:50.904179
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:56.838744
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
        Unit test for TruTVIE constructor
    """
    trutv = TruTVIE()
    assert(trutv._VALID_URL ==
           r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')

# Generated at 2022-06-14 17:18:05.894744
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test with example given in the assignment
    t = TruTVIE()
    # Testing the TruTVIE constructor
    assert isinstance(t, TruTVIE)
    assert type(t) == TruTVIE
    # Testing the video_id
    assert t._TEST['info_dict']['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
    # Test with the example from the assignment
    assert t._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    # Testing the video title
    assert t._TEST['info_dict']['title'] == 'Sunlight-Activated Flower'
    # Testing the video description
    assert t._

# Generated at 2022-06-14 17:18:10.358278
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:16.499481
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url1 = 'https://www.trutv.com/full-episodes/218060-episode-3.html'
    assert TruTVIE._VALID_URL == re.match(TruTVIE._VALID_URL, url1).re.pattern
    assert TruTVIE._download_json(url1, None)


# Generated at 2022-06-14 17:18:22.644368
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # create a unit test for TruTVIE constructor
    # TruTVIE is inherited from class TurnerBaseIE
    # this unit test case will test constructor of class TurnerBaseIE
    # it only tests whether the instance is created successfully
    # it will not test the functionality
    ie = TruTVIE()
    # check whether the instance is created successfully
    assert ie is not None


# Generated at 2022-06-14 17:18:23.124699
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()

# Generated at 2022-06-14 17:18:31.047214
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from re import compile, match
    from .common import InfoExtractor
    from .turner import TurnerBaseInfoExtractor
    from .trutv import TruTVIE
    from .theplatform import ThePlatformIE

    # Test for the creation of class TruTVIE
    print("Testing for the creation of class TruTVIE")
    assert(isinstance(TruTVIE(), InfoExtractor))
    assert(isinstance(TruTVIE(), TurnerBaseInfoExtractor))
    assert(isinstance(TruTVIE(), ThePlatformIE))
    print("Tested for the creation of class TruTVIE")

    # Test for the __init__ method of class TruTVIE
    print("Testing for the __init__ method of class TruTVIE")

# Generated at 2022-06-14 17:18:54.317247
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	assert(TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')

# Generated at 2022-06-14 17:18:57.921632
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    '''
    Unit test for TruTVIE
    '''
    trutv_ie = TruTVIE()
    assert trutv_ie.test()

# Generated at 2022-06-14 17:19:03.392157
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Simple unit test for TruTVIE for the link
    https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html
    """
    # Constructor for TruTVIE class
    ttvie = TruTVIE()

    # Compare the result with the expected result from the test in TruTVIE.py
    # If the comparison is True, the test is OK, otherwise: Error
    assert ttvie._TEST == ttvie._real_extract(ttvie._TEST['url'])

# Generated at 2022-06-14 17:19:08.825476
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvIE = TruTVIE()
    # Asserting the value for _VALID_URL
    assert trutvIE._VALID_URL == "https?://(?:www\\.)?trutv\\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\\d+))"
    # Asserting the value for _TEST

# Generated at 2022-06-14 17:19:12.249003
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert not TruTVIE.suitable(object)
    assert TruTVIE.suitable(TruTVIE)

# Generated at 2022-06-14 17:19:13.070218
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    x = TruTVIE()



# Generated at 2022-06-14 17:19:15.066086
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    construction1 = TruTVIE()
    construction2 = TruTVIE()
    assert construction1 == construction2
    assert TruTVIE is construction1.__class__

# Generated at 2022-06-14 17:19:15.737374
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:24.103464
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    print('Testing TruTVIE')
    # Any video id should do
    video_id='f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
    
    TruTVIE()._extract_ngtv_info(
            video_id, {}, {
                'url': 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
                'site_name': 'truTV',
                'auth_required': True,
            })
            
    print('Tested TruTVIE')

# Generated at 2022-06-14 17:19:32.527596
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:20:15.643021
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:23.679367
# Unit test for constructor of class TruTVIE
def test_TruTVIE():  
    # Test constructor with URL of known video
    trutv_ie = TruTVIE(TruTVIE._TEST['url'])
    assert trutv_ie is not None
    # Test that the extract() method is working as expected
    test_video_info = TruTVIE._TEST['info_dict']
    url = TruTVIE._TEST['url']

    # Test constructor with URL of unknown video
    unknown_trutv_ie = TruTVIE("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    assert unknown_trutv_ie is None
    # Test that the extract() method will return None if the URL is unknown
    unknown_test_video_info = None
    
    # Test that the extract() method will return None if the

# Generated at 2022-06-14 17:20:24.597369
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:25.813974
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.__name__ == 'TruTVIE'

# Generated at 2022-06-14 17:20:28.382840
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
    except:
        return False
    return True

# Generated at 2022-06-14 17:20:32.818545
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == TruTVIE._VALID_URL
    assert TruTVIE()._TEST == TruTVIE._TEST
    assert TruTVIE()._real_extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:20:42.994485
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    assert TruTVIE("https://www.trutv.com/full-episodes/12775369/truTV/truTV-premieres.html?linkId=29844815")
    assert TruTVIE("https://www.trutv.com/shows/hacksaw-ridge/videos/the-battle-of-okehazama.html")
    assert TruTVIE("https://www.trutv.com/full-episodes/12775369/truTV/truTV-premieres.html")

# Generated at 2022-06-14 17:20:44.987405
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTV_obj = TruTVIE()

# Generated at 2022-06-14 17:20:46.331597
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
    except NameError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 17:20:52.583931
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:22:30.132710
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:22:32.551839
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
        assert True
    except AssertionError:
        assert False


# Generated at 2022-06-14 17:22:34.846737
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # check TruTVIE processing
    TruTVIE()._real_extract(TruTVIE._TEST['url'])



# Generated at 2022-06-14 17:22:45.147578
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    # Test for TruTVIE.suitable()
    print("\n[INFO]\tUnit-test: TruTVIE.suitable()")
    assert(TruTVIE.suitable(test_url))
    # Test for TruTVIE._real_extract()
    print("\n[INFO]\tUnit-test: TruTVIE._real_extract()")
    print(TruTVIE._real_extract(TruTVIE, test_url))

# Generated at 2022-06-14 17:22:52.158076
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .test_youtube import _download_json

    class TruTVIESim(TruTVIE):
        def _download_json(self, url, video_id, *args, **kwargs):
            return _download_json(url)

    # # Series
    # # Example of Series
    # # https://www.trutv.com/shows/harry-loves-lisa/index.html
    # # https://www.trutv.com/shows/harry-and-lisa/videos/cheeky-meerkats.html
    # # https://www.trutv.com/shows/harry-and-lisa/videos/harrys-date-night.html
    # # https://www.trutv.com/shows/harry-and-lisa/videos/the-hairy-b

# Generated at 2022-06-14 17:22:56.568741
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    TruTVIE()._real_extract(url)

# Generated at 2022-06-14 17:23:07.046727
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert obj._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

# Generated at 2022-06-14 17:23:15.261010
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:15.871048
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:17.830829
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test with an instance of class TruTVIE
    trutv_ie = TruTVIE()
    print(trutv_ie)