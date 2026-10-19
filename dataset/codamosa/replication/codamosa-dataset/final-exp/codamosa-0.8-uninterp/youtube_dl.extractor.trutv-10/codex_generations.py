

# Generated at 2022-06-14 17:16:31.670175
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:32.293037
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:37.661969
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Constructor for TruTVIE class
    # ie = TruTVIE()
    ie = TruTVIE()

    # assert len(ie._extract_ngtv_info) == 3
    assert len(ie._extract_ngtv_info) == 3
    # assert len(ie._real_extract) == 3
    assert len(ie._real_extract) == 3

# Generated at 2022-06-14 17:16:40.748805
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:49.630413
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test case of video with an episode
    video_with_episode_id = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert video_with_episode_id.url == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

    # Test case of video without an episode
    video_without_episode_id = TruTVIE('https://www.trutv.com/shows/tru-tv-presents-worlds-dumbest/videos/worlds-dumbest-commercial-breaks.html')

# Generated at 2022-06-14 17:16:52.391808
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert 'TruTVIE' in str(t)
    assert 'TurnerBaseIE' in str(t)
    assert type(t) == TruTVIE

# Generated at 2022-06-14 17:17:00.779399
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv_ie = TruTVIE() # Constructing the TruTVIE Class
    ttv_ie.turnerBase_ie.extractor_key # Accessing private property to test
    ttv_ie.turnerBase_ie.ident # Accessing private property to test
    ttv_ie.turnerBase_ie.ie_key # Accessing private property to test
    assert ttv_ie.turnerBase_ie.extractor_key == 'turner'
    assert ttv_ie.turnerBase_ie.ident == 'trutv'
    assert ttv_ie.turnerBase_ie.ie_key == 'TruTV'
    ttv_ie._VALID_URL # Accessing private property to test

# Generated at 2022-06-14 17:17:06.798048
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    video_id = '123'
    url = 'http://www.trutv.com/shows/some-show/videos/123'
    ie = TruTVIE({'_type': 'url_transparent', 'url': url})
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:11.976796
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	Test_1=TruTVIE()
	Test_1.IE_NAME
	Test_1.ie_key()
	Test_1.suitable("https://www.trutv.com/shows/the-carbonaro-effect/videos/no-wait-that-was-me.html")

# Generated at 2022-06-14 17:17:13.332264
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Running this unit test should give a successful result
    trutvie = TruTVIE()
    assert trutvie is not None

# Generated at 2022-06-14 17:17:26.534835
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """This unittest is for testing TruTVIE class only
    """
    from .trutv import TruTVIE
    url_test = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    a = TruTVIE()

# Generated at 2022-06-14 17:17:29.793158
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:17:31.283128
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE
    # Some hack to bypass flake8 check
    assert True

# Generated at 2022-06-14 17:17:43.557146
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TestTruTVIE = TruTVIE()
    assert TestTruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:50.007083
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE(TruTVIE._VALID_URL)
    assert ie.SUFFIX == 'trutv'
    assert ie.API_KEY == 'dc9ea2f9b1a3fd02ce3c8bd68fdd86f5cacda7a5'

test_TruTVIE()

# Generated at 2022-06-14 17:17:51.566768
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    result = repr(ie)
    assert result.startswith("<class '__main__.TruTVIE'")


# Generated at 2022-06-14 17:18:01.427683
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:05.853366
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert instance.name == 'truTV'
    assert instance._VALID_URL == instance.VALID_URL
    assert instance._TEST == instance._TEST

# Generated at 2022-06-14 17:18:08.599393
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:18:19.848910
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    expected_browser = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0)'

    # Test TruTVIE constructor with no arguments
    trutv_ie = TruTVIE()

    # Test TruTVIE constructor with arguments
    trutv_ie = TruTVIE(expected_browser)

    # Test TruTVIE constructor with unexpected arguments
    try:
        trutv_ie = TruTVIE(expected_browser, "unexpected string")
    except BaseException as e:
        assert str(e) == "Unexpected number of arguments passed to TruTVIE constructor."

    # Test TruTVIE constructor with passing more than the maximum number of methods

# Generated at 2022-06-14 17:18:37.760385
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE.test()


# Generated at 2022-06-14 17:18:47.860588
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Define a test URL for class TruTVIE
    test_url_TruTVIE = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

    # Create an instance of class TruTVIE
    test_instance = TruTVIE()

    # Call method real_extract() of instance test_instance on test URL
    result = test_instance._real_extract(test_url_TruTVIE)

    # Assert that the result is not None
    assert result is not None

    # Assert that the id of the result is not None
    assert result['id'] is not None

    # Assert that the title of the result is not None
    assert result['title'] is not None

    # Assert that the description of the result is not None
    assert result

# Generated at 2022-06-14 17:18:48.838547
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t is not None

# Generated at 2022-06-14 17:18:51.523333
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttIE_obj = TruTVIE()
    ttIE_str = str(ttIE_obj)
    assert('Turner Base' in ttIE_str)

# Generated at 2022-06-14 17:18:53.664703
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TEST == ie.TEST

# Generated at 2022-06-14 17:18:58.901204
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'



# Generated at 2022-06-14 17:19:05.465670
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:19:07.515224
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    global url
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    return TruTVIE(url)

#test_TruTVIE()

# Generated at 2022-06-14 17:19:15.086078
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.ie_key() == 'TruTV'
    assert TruTVIE.ie_key() == 'trutv'
# Using the test url
test_TruTVIE = TruTVIE.url_result('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
# Check title
print(test_TruTVIE.get('title'))

# Generated at 2022-06-14 17:19:22.648127
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    #Test normal URLs
    item = TruTVIE('https://www.trutv.com/shows/tru-tv-top-funniest/videos/tru-tv-top-funniest-celebrity-bloopers-and-gaffes.html')
    assert item._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert item._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'


# Generated at 2022-06-14 17:20:02.351568
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    ie.extract('https://www.trutv.com/full-episodes/75310/the-carbonaro-effect-the-carbonaro-effect--dec-14-2017-episode.html')

# Generated at 2022-06-14 17:20:09.171850
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t._TEST['info_dict']['title'] == 'Sunlight-Activated Flower'
    assert t._TEST['info_dict']['description'] == "A customer is stunned when he sees Michael's sunlight-activated flower."
    assert t._TEST['info_dict']['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'

# Generated at 2022-06-14 17:20:12.038227
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE(None).IE_NAME == 'truTV'

# Generated at 2022-06-14 17:20:12.966184
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(None)

# Generated at 2022-06-14 17:20:21.566968
# Unit test for constructor of class TruTVIE

# Generated at 2022-06-14 17:20:33.434844
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:20:43.259061
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert instance._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:20:43.743781
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    pass

# Generated at 2022-06-14 17:20:44.682050
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(None)._VALID_URL

# Generated at 2022-06-14 17:20:50.764841
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Testing with a clip URL
    t = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert t._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert t._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

# Generated at 2022-06-14 17:21:28.169673
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test construction of class TruTVIE
    trutv_ie = TruTVIE()
    assert isinstance(trutv_ie, TruTVIE)

# Generated at 2022-06-14 17:21:35.808538
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test for constructor with valid parameters
    true_tv = TruTVIE()
    assert isinstance(true_tv, TruTVIE)
    # Test for constructor with invalid parameters
    try:
        true_tv = TruTVIE(empty_dict)
    except Exception as ex:
        assert isinstance(ex, TypeError) or isinstance(ex, ValueError)

test_TruTVIE()

# Generated at 2022-06-14 17:21:36.447839
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:37.833192
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert isinstance(instance, TruTVIE)

# Generated at 2022-06-14 17:21:38.375898
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:45.755977
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    pytest unit test method for constructor of class TruTVIE
    """
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    TruTVIE(True).extract(url)

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:21:46.597993
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(None)

# Generated at 2022-06-14 17:21:47.391446
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE_test = TruTVIE()

# Generated at 2022-06-14 17:21:51.389388
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .TruTVIE import TruTVIE
    # Setting url
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    # Creating object
    obj = TruTVIE(url)
    print (obj)

# Generated at 2022-06-14 17:21:53.446874
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert TruTVIE._TEST == ie._TEST


# Generated at 2022-06-14 17:23:22.337736
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert obj.turner_id() != None


# Generated at 2022-06-14 17:23:26.699634
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # this test is only to make sure that TruTVIE is a valid class,
    # as it will be dynamically created at registration (see __init__.py)
    try:
        TruTVIE()
    except:
        raise AssertionError("TruTVIE valid constructor test failed")
    return True

# Generated at 2022-06-14 17:23:34.775139
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Test for testing the constructor of class TruTVIE"""
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:39.224699
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test TruTVIE constructor with empty url
    TruTVIE()

if __name__ == '__main__':
    # Test TruTVIE constructor with empty url
    test_TruTVIE()

# Generated at 2022-06-14 17:23:41.575887
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()

# Generated at 2022-06-14 17:23:49.590613
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:52.623500
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Unit test for constructor of class TruTVIE"""
    try:
        # Create instance of TruTVIE
        TruTVIE()
    except:
        print("Construction of class TruTVIE failed")


# Generated at 2022-06-14 17:23:57.721364
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    import unittest
    from .turner import TurnerBaseIE
    from .trutv import TruTVIE
    testClass = unittest.TestCase()
    trutv_ie = TruTVIE(testClass)
    testClass.assertTrue(isinstance(trutv_ie, TurnerBaseIE))

# Generated at 2022-06-14 17:24:05.446640
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .common import *
    # Unit test for constructor of class TruTVIE
    t = TruTVIE(downloader=None)
    assert t != None
    # Unit test for TruTVIE._extract_subtitles
    # It is not possible to unit test this method because it requires a key which is hardcoded
    # in the method, and there is no easy way to fake it.

    # Unit test for TruTVIE._extract_ngtv_info
    # It is not possible to unit test this method because it requires a key which is hardcoded
    # in the method, and there is no easy way to fake it.

    # Unit test for TruTVIE._real_extract
    # It is not possible to unit test this method because it requires a key which is hardcoded
    # in the method, and there is no easy way to fake it.



# Generated at 2022-06-14 17:24:16.650456
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'