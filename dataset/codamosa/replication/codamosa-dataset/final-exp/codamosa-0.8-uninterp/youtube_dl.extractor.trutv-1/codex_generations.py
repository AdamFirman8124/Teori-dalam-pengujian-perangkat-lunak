

# Generated at 2022-06-14 17:16:34.734368
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test an invalid URL
    with pytest.raises(Exception) as excinfo:
        TruTVIE('http://www.trutv.com/series')
    assert(excinfo.typename == 'ExtractorError')

# Generated at 2022-06-14 17:16:35.368351
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:42.336871
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    IE_TruTVIE = TruTVIE()
    assert(IE_TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')
    assert(IE_TruTVIE.ie_key() == 'TruTV')
    assert(IE_TruTVIE.ie_name() == 'TruTV')

# Generated at 2022-06-14 17:16:44.623709
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:16:45.232983
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE is not None

# Generated at 2022-06-14 17:16:47.783172
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
        print("test_TruTVIE passed")
    except:
        print("test_TruTVIE failed")
# unit test call
test_TruTVIE()

# Generated at 2022-06-14 17:16:49.291578
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:55.569389
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE_test = TruTVIE()
    assert TruTVIE_test._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:02.575916
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:12.319401
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    ie.extract('https://www.trutv.com/shows/hacking-the-system/videos/how-to-steal-a-car.html')
    ie.extract('https://www.trutv.com/shows/in-session/videos/a-jealous-love-in-tulsa.html')
    ie.extract('https://www.trutv.com/shows/hacking-the-system/videos/how-to-steal-a-car.html')

# Generated at 2022-06-14 17:17:20.098184
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .common import TestCommon
    TestCommon.test_IE_class(TruTVIE)

# Generated at 2022-06-14 17:17:26.940069
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    #Create object of class TruTVIE
    t = TruTVIE(None)
    # Chect if it has right embed URL
    assert t._embed_url == 'http://www.trutv.com/embeds/%s.html'
    # Check if test dict is defined correctly
    assert t._TEST['info_dict']['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
    assert t._TEST['info_dict']['title'] == 'Sunlight-Activated Flower'



# Generated at 2022-06-14 17:17:28.955418
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert isinstance(trutv, TruTVIE)

# Generated at 2022-06-14 17:17:31.432893
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:17:37.209451
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Initializes an object of class TruTVIE
    truTV = TruTVIE()

    # Tests the function _real_extract of the class TruTVIE
    truTV._real_extract("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")

    # Tests the function _extract_ngtv_info of the class TruTVIE
    truTV._extract_ngtv_info("f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1", {})

# Generated at 2022-06-14 17:17:41.546240
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert True == ie.IE_NAME in TruTVIE.ie_key()

# Generated at 2022-06-14 17:17:42.926298
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t.ie_key() == 'TruTV'

# Generated at 2022-06-14 17:17:43.224031
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:45.699350
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


# Generated at 2022-06-14 17:17:47.112962
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Constructor of class TruTVIE should not fail on invocation."""
    TruTVIE()

# Generated at 2022-06-14 17:18:04.994981
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test with video URL
    test_video_url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    TruTVIE_URL = TruTVIE(test_video_url)
    # Verify that the TruTVIE object was created
    assert TruTVIE_URL != None

# Test for function _real_extract for class TruTVIE

# Generated at 2022-06-14 17:18:14.671267
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    print("Testing TruTVIE")
    info = TruTVIE()._real_extract({
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
    })
    print(info)

if __name__ == '__main__':
    test_TruTV

# Generated at 2022-06-14 17:18:17.306821
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Constructor is invoked
    ie = TruTVIE()
    # Assertions
    assert len(ie._VALID_URL) > 0
    assert len(ie._TEST) > 0


# Generated at 2022-06-14 17:18:21.339060
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    # Check if parse_url method of TruTVIE class returns a tuple
    assert isinstance(ie.parse_url(ie._TEST['url']), tuple)

# Generated at 2022-06-14 17:18:29.816029
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Here we get the number of test cases that the class will be used to test.
    num = TruTVIE._TEST.get('num', 0)
    if TruTVIE._TEST.get('error') is not None:
        print('\nTest ' + str(num) + ' is bad due to error (' + TruTVIE._TEST.get('error') + ').')
        return
    print('\nTest ' + str(num) + 'is good.')
    print('\tURL:', TruTVIE._TEST.get('url'))
    print('\tParams:', TruTVIE._TEST.get('params'))
    print('\tInfo dict:', TruTVIE._TEST.get('info_dict'))

# Generated at 2022-06-14 17:18:31.987437
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Test TruTVIE constructor"""
    #assert TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    print("Constructor testing completed")

# Generated at 2022-06-14 17:18:39.721421
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Check the validity of TruTVIE class constructor
    TruTVIE_class = TruTVIE()
    assert TruTVIE_class.IE_NAME == 'trutv:shows:videos'
    assert TruTVIE_class._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    TruTVIE_class_test = TruTVIE_class._TEST

# Generated at 2022-06-14 17:18:40.364815
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()

# Generated at 2022-06-14 17:18:41.994652
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._TEST == TruTVIE._TEST

# Generated at 2022-06-14 17:18:50.079061
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE(None)._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert TruTVIE(None)._TEST.get('url') == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE(None)._TEST.get('params') == {'skip_download': True}

# Generated at 2022-06-14 17:19:13.317093
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	t = TruTVIE()

# Generated at 2022-06-14 17:19:21.029227
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Unit test for constructor of class TruTVIE"""
    # In this unit test, we will test the constructor of TruTVIE
    # First we need to import the class
    from .trutv import TruTVIE

    # This is a valid url
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    # Test if the url is valid
    assert TruTVIE()._match_id(url)

    # This is an invalid url
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower'
    # Test if the url is invalid
    assert not TruTVIE()._match_id(url)

# Generated at 2022-06-14 17:19:30.911365
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    def test_TruTVIE(url, expected_title):
        trutv = TruTVIE()
        trutv._TEST['url'] = url
        trutv._TEST['expected_title'] = expected_title
        trutv._TEST = trutv._TEST
    test_TruTVIE("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html", "Sunlight-Activated Flower")
    test_TruTVIE("https://www.trutv.com/shows/impractical-jokers/full-episodes/crossover.html", "Impractical Jokers S02E17 – Crossover")

# Generated at 2022-06-14 17:19:31.877532
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t1 = TruTVIE()


# Generated at 2022-06-14 17:19:36.253796
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = TruTVIE._VALID_URL
    if url.find('/full-episodes/') != -1:
        TruTVIE(url)
        return 'Success'
    else:
        return 'Failure'


# Generated at 2022-06-14 17:19:37.772619
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:40.279130
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(_download_webpage=lambda url: "", _download_json=lambda url, video_id: {'episode': {}})._real_extract(url)

# Generated at 2022-06-14 17:19:52.170982
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:19:56.975639
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')


# Generated at 2022-06-14 17:20:01.307780
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"; #sample url
    contructor = TruTVIE(url)
    print(contructor)

# Unit tests for _real_extract of TruTVIE

# Generated at 2022-06-14 17:20:58.569072
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    x = TruTVIE()
    assert x.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert not x.suitable('https://www.amctv.com/shows/the-walking-dead/full-episodes/season-3/episode-02-sick')
    assert not x.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')



# Generated at 2022-06-14 17:21:06.183355
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Set up test constants 
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    series_slug = "the-carbonaro-effect"
    clip_slug = "sunlight-activated-flower" 
    video_id = None
    path = "series/clip"
    display_id = clip_slug
    media_id = "f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1"
    title = "Sunlight-Activated Flower"
    description = "A customer is stunned when he sees Michael's sunlight-activated flower."
    isAuthRequired = False

    # Create TruTVIE object 
    constructor_TruTVIE = TruTVIE()

    # Use _

# Generated at 2022-06-14 17:21:06.813382
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:10.806495
# Unit test for constructor of class TruTVIE

# Generated at 2022-06-14 17:21:11.488479
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:15.424631
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Make sure that there are no errors when instantiating the TruTVIE class
    browser = TruTVIE()
    assert isinstance(browser, TruTVIE), "Error: object is not an instance of TruTVIE class"



# Generated at 2022-06-14 17:21:22.213265
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tt = TruTVIE()
    assert tt._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'


# Generated at 2022-06-14 17:21:22.853229
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:30.662695
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Description:
        Unit tests for constructor of class TruTVIE.
    Returns:
    Exceptions:
    """
    trutvIE = TruTVIE()
    assert trutvIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:21:32.892118
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tru_tv_ie = TruTVIE()
    assert tru_tv_ie

# Generated at 2022-06-14 17:23:23.592459
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:25.585717
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert(instance)

# Generated at 2022-06-14 17:23:34.195710
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t is not None
    # Test TruTVIE
    assert t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    data = {
        'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1',
        'ext': 'mp4',
        'title': 'Sunlight-Activated Flower',
        'description': "A customer is stunned when he sees Michael's sunlight-activated flower.",
    }

# Generated at 2022-06-14 17:23:45.663024
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test case 1: https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html
    truTV1 = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert truTV1.ie_key() == 'TruTV', 'Fails to instance class TruTVIE'
    assert truTV1.display_id() == 'sunlight-activated-flower', 'Fails to extract display_id'
    # Test case 2: https://www.trutv.com/shows/greatest-ever/episodes/greatest-ever-t-shirts.html

# Generated at 2022-06-14 17:23:52.003252
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.__dict__ is not None
    assert TruTVIE._VALID_URL is not None
    assert TruTVIE._TEST is not None
    assert TruTVIE._real_extract is not None

# Unit test to check the excution of TruTVIE()._real_extract

# Generated at 2022-06-14 17:24:02.241499
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvIE = TruTVIE()
    assert trutvIE._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:24:05.527368
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(TurnerBaseIE(),"https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")

# Generated at 2022-06-14 17:24:06.886953
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie_instance = TruTVIE()

# Generated at 2022-06-14 17:24:09.148931
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()._real_extract(
        'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:24:10.027501
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
