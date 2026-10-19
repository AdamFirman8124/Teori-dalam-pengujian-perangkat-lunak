

# Generated at 2022-06-14 17:16:39.347777
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .ttv_shows.ttv_test import TTvshowsIE

    ie = TTvshowsIE()
    assert ie.IE_NAME == 'trutv:shows'
    assert ie.IE_DESC == 'TruTV shows'
    assert ie._VALID_URL == 'https?://(?:www\.)?trutv\.com/shows/(?P<show_id>[^/]+)/?(?:[?#&]|$)'
    assert ie._PAGE_SIZE == 100
    assert ie._API_URL == 'https://api.trutv.com/v3/shows/%s/episodes?page=%s&pageSize=%s'
    assert ie._JSON_FODDER == 'items'

# Generated at 2022-06-14 17:16:42.518813
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:16:43.161985
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:50.412797
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    match = re.match(TruTVIE._VALID_URL, TruTVIE._TEST['url'])
    series_slug = match.group('series_slug')
    clip_slug = match.group('clip_slug')
    video_id = match.group('id')
    path = 'episode' if video_id else 'series/clip'
    display_id = video_id if video_id else clip_slug
    # assert TruTVIE._download_json(path, series_slug, display_id) == TruTVIE._TEST['info_dict']

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:16:51.454489
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    testTruTVIE = TruTVIE()

# Generated at 2022-06-14 17:16:52.081106
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:59.255487
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()
    assert trutv_ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:05.475389
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Simple test of TruTVIE._real_extract
    """
    TruTVIE._real_extract("http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    TruTVIE._real_extract("http://www.trutv.com/shows/the-carbonaro-effect/1312/")


# Generated at 2022-06-14 17:17:13.710022
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from unittest import TestCase
    class_ = TruTVIE

# Generated at 2022-06-14 17:17:21.407700
# Unit test for constructor of class TruTVIE

# Generated at 2022-06-14 17:17:38.790578
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvIE = TruTVIE()
    assert trutvIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    # Assert whether the test case is valid or invalid

# Generated at 2022-06-14 17:17:47.956669
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
  
  trutv = TruTVIE()
  assert trutv._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
  assert trutv._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
  assert trutv._TEST['info_dict']['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
  assert tr

# Generated at 2022-06-14 17:17:52.744230
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.constructor == TruTVIE
    assert ie.site_name == "truTV"
    assert ie.ie_key == 'trutv'
    assert ie.domain == 'www.trutv.com'

# Unit tests for functions of class TruTVIE

# Generated at 2022-06-14 17:17:56.646819
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """This testcase tests if the TruTVIE class can be constructed
    """
    TruTVIE()

# Generated at 2022-06-14 17:17:57.468212
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:58.459617
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:03.102370
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert(obj.SUFFIX == '%(provider)s')
    assert(obj.login_url() == 'https://api.trutv.com/v2/web/login')



# Generated at 2022-06-14 17:18:13.782658
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv_extractor = TruTVIE()
    assert ttv_extractor._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:21.214019
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Access to class
    trutv_class = TruTVIE()
    # Test method
    # Constructor of class TruTVIE should be able to verify existance of m3u8_url
    result = trutv_class._extract_ngtv_info('37d5151c-5a71-4b68-a0c1-ae81e8fe7a5c', {}, {})
    assert(result['formats'][0]['protocol'] == 'm3u8'), "Unexpected result on TruTVIE"
test_TruTVIE()

# Generated at 2022-06-14 17:18:22.126496
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
  assert TruTVIE()

# Generated at 2022-06-14 17:18:45.710138
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE("http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    except assert_raises as e:
        print(e)

# Test extraction of valid URL

# Generated at 2022-06-14 17:18:47.919119
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:49.169377
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()
    assert not trutv_ie is  None

# Generated at 2022-06-14 17:18:50.198882
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(None)

# Generated at 2022-06-14 17:18:56.010417
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:56.699912
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:58.579517
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._TEST is not None
    x = TruTVIE()
    assert x._VALID_URL is not None

# Generated at 2022-06-14 17:18:59.140149
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:01.729414
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvie = TruTVIE()
    """
    Test to make sure TruTVIE is a class in the TruTVIE module
    """
    assert isinstance(trutvie, TruTVIE)

# Generated at 2022-06-14 17:19:02.685636
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE_obj = TruTVIE()

# Generated at 2022-06-14 17:19:42.714989
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:44.577608
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


# Generated at 2022-06-14 17:19:54.555608
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
  test_item = TruTVIE()
  assert isinstance (test_item, TurnerBaseIE)
  #Assigning test_params with valid URL
  test_url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
  test_series_slug, test_clip_slug, test_video_id = TruTVIE._VALID_URL, re.match(TruTVIE._VALID_URL, test_url).groups()
  #Test assert 1
  #Checking test_series_slug

# Generated at 2022-06-14 17:19:55.948411
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:00.319798
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	try:
		TruTVIE()
	except Exception as e:
		print("Problem in TruTVIE() --> " + str(e) )
	else:
		print("TruTVIE() works fine.")
	finally:
		print("\n")


# Generated at 2022-06-14 17:20:00.912455
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:10.904839
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._VALID_URL == 'http://(?:www\\.)?trutv\\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\\d+))'
    assert TruTVIE._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

# Generated at 2022-06-14 17:20:11.693405
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:15.433077
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Testing valid TruTV video URL
    trutv_video_url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE._VALID_URL == "(" + trutv_video_url + ")"

# Generated at 2022-06-14 17:20:15.972679
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()


# Generated at 2022-06-14 17:20:58.662120
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


# Generated at 2022-06-14 17:20:59.399583
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:59.971565
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:01.596674
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
    except Exception as e:
        assert False, str(e)

# Generated at 2022-06-14 17:21:11.331684
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Unit test for TruTVIE."""
    url_input = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    expected_cls = TruTVIE
    instance = TruTVIE()
    assert isinstance(instance, expected_cls)
    assert hasattr(instance,'_VALID_URL')
    assert hasattr(instance,'_TEST')
    assert expected_cls._TEST == instance._TEST
    assert expected_cls._VALID_URL is instance._VALID_URL
    assert instance._real_extract(url_input)

# Generated at 2022-06-14 17:21:17.636202
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert not t.suitable('https://www.trutv.com/shows/the-carbonaro-effect/')
    assert t.IE_NAME == 'trutv:episode'
    assert t.IE_DESC == 'truTV'

# Generated at 2022-06-14 17:21:19.156430
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        obj = TruTVIE()
    except:
        return False
    return True

# Generated at 2022-06-14 17:21:27.911080
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert instance.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html') == True
    assert instance.suitable('https://www.trutv.com/full-episodes/1016901/video/test/test') == True
    assert instance.suitable('https://www.trutv.com/full-episodes/episode/45582') == True
    assert instance.suitable('https://www.trutv.com/full-episodes/episode/45582/video/test/test') == False
    assert instance.suitable('https://www.trutv.com') == False


# Generated at 2022-06-14 17:21:39.706304
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    t._VALID_URL
    t._TEST
    t._real_extract
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'
    }
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import requests
    import json
    import re
    season_num = ''
    episode_num = ''
    response = requests.get('https://www.trutv.com/full-episodes/impractical-jokers/videos/the-jokers-strike-back.html', headers=header)
    soup = BeautifulSoup(response.text, "lxml")

# Generated at 2022-06-14 17:21:50.096437
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # test case 1: valid url
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    result = TruTVIE()._real_extract(url)
    assert 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1' == result['id']

    # test case 2: invalid url
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.htm"
    with TruTVIE() as trutv:
        with trutv.assertRaisesRegexp(TurnerBaseIE._TURNERE_REGEX_ERROR, 'Invalid URL'):
            trutv._real_extract(url)

# Generated at 2022-06-14 17:23:32.736681
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert isinstance(obj, TruTVIE)
    
# Unit test to check if the valid url is being parsed  

# Generated at 2022-06-14 17:23:44.515251
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()

    _VALID_URL = r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    t._VALID_URL = _VALID_URL
    # 1st test case
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    series_slug, clip_slug, video_id = re.match(_VALID_URL, url).groups() # clip_slug, video_id
    assert video_id == None


# Generated at 2022-06-14 17:23:48.918515
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert trutv._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'


# Generated at 2022-06-14 17:23:49.886072
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test = TruTVIE()
    test.suite()

# Generated at 2022-06-14 17:23:54.102468
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url="https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    trutv = TruTVIE()
    vidinfo = trutv._real_extract(url)
    print(vidinfo)
    

# Generated at 2022-06-14 17:23:56.540982
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Unit test class TruTVIE
    """
    trutv = TruTVIE()
    assert trutv

# Generated at 2022-06-14 17:24:04.524607
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Arrange
    input_url_1 = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    input_url_2 = 'https://www.trutv.com/full-episodes/12604/the-carbonaro-effect-sunlight-activated-flower.html'
    input_url_3 = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/'
    input_url_4 = 'https://www.trutv.com/full-episodes/12604/'
    input_url_5 = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/leaves-on-a-tree.html'

# Generated at 2022-06-14 17:24:05.230293
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:24:16.404377
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.IE_NAME == 'trutv:v2'
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:24:21.776740
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Unit test for constructor of class TruTVIE
    """
    # with clip url
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    TruTVIE(None)._real_extract(url)

    # without clip url
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/full-episodes/tba)39.html'
    TruTVIE(None)._real_extract(url)