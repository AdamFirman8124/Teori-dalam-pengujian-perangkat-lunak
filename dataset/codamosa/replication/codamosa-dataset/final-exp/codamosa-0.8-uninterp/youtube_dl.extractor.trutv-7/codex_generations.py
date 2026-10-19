

# Generated at 2022-06-14 17:16:33.333928
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Verify that the URL video can be downloaded

# Generated at 2022-06-14 17:16:33.803536
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()

# Generated at 2022-06-14 17:16:34.894011
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:40.708857
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE._TEST = {
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
    TruTVIE()

# Generated at 2022-06-14 17:16:43.227257
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_TruTVIE = TruTVIE()
    # case: test_TruTVIE is a instance of TruTVIE class
    assert isinstance(test_TruTVIE, TruTVIE)

# Generated at 2022-06-14 17:16:44.334311
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvIE = TruTVIE()

# Generated at 2022-06-14 17:16:46.888025
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from . import TruTVIE

    # Test constructor.
    t1 = TruTVIE(True)
    assert t1 is not None
    assert t1.test_suite() == True

# Generated at 2022-06-14 17:16:50.513941
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE("id", "title", "description", "upload_date", "url", "thumbnail")

# Generated at 2022-06-14 17:16:53.652954
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	print('Unit tests for TruTVIE')
	# Constructor
	ie = TruTVIE()
	assert type(ie) == TruTVIE
	assert ie.sdk == None
	assert ie.service == None

# Generated at 2022-06-14 17:17:01.564192
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # test for url https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html
    TruTVIE_test_values = [(
        'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
        # expected output
        {
            'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1',
            'ext': 'mp4',
            'title': 'Sunlight-Activated Flower',
            'description': "A customer is stunned when he sees Michael's sunlight-activated flower.",
        })]
    # call constructor with test data
    t = TruTVIE()
    # check results

# Generated at 2022-06-14 17:17:13.902221
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test extract
    TruTVIE().extract(TruTVIE._TEST['url'])
    TruTVIE().extract(TruTVIE._TEST['url'])

# Generated at 2022-06-14 17:17:14.482040
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:26.262728
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie._downloader = None
    ie._download_webpage = None
    ie._download_json = None
    ie._extract_ngtv_info = None
    ie.IE_NAME = 'TruTV'
    ie.IE_DESC = 'truTV'
    ie.VALID_URL = r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:34.524377
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test TruTVIE
    trutv_ie = TruTVIE('TruTV')._real_extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    if 'mp4' != trutv_ie['ext']:
        raise AssertionError("Extension error")
    if 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1' != trutv_ie['id']:
        raise AssertionError("Id error")

# Generated at 2022-06-14 17:17:36.657557
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert trutv is not None

# Generated at 2022-06-14 17:17:42.729053
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert str(type(TruTVIE)) == "<class '__main__.TruTVIE'>"
    assert type(TruTVIE._VALID_URL) is re._pattern_type
    assert TruTVIE._VALID_URL.match('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert TruTVIE._VALID_URL.match('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html').groups() == ('the-carbonaro-effect', 'sunlight-activated-flower', None)

# Generated at 2022-06-14 17:17:54.830774
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvIE = TruTVIE()
    assert trutvIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:02.894584
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    if not isinstance(instance, TruTVIE):
        raise Exception("Not a class instance!")
    if not re.match(instance._VALID_URL, "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"):
        raise Exception("Invalid URL!")
    if not re.match(instance._VALID_URL, "https://www.trutv.com/shows/the-carbonaro-effect/1234"):
        raise Exception("Invalid URL!")

# Generated at 2022-06-14 17:18:06.303906
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Make sure that the constructor of the TruTVIE class does not thrown an exception
    test_obj = TruTVIE()
    print('Completed testing TruTVIE()')


# Generated at 2022-06-14 17:18:09.792039
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # positive cases
    url = r'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    parser = TruTVIE(url)


# Generated at 2022-06-14 17:18:29.773994
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttvie = TruTVIE()

# Generated at 2022-06-14 17:18:32.125589
# Unit test for constructor of class TruTVIE

# Generated at 2022-06-14 17:18:33.148376
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE(None, None) is not None

# Generated at 2022-06-14 17:18:34.209570
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    dott = TruTVIE()
    assert dott == TruTVIE()

test_TruTVIE()

# Generated at 2022-06-14 17:18:35.403629
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	assert 'TruTVIE' in globals()

# Generated at 2022-06-14 17:18:36.588538
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:44.017717
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Assign
    video = TruTVIE()
    video_url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    # Act
    info = video.extract(video_url)
    # Assert
    assert info.get("id") == "f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1"

# Generated at 2022-06-14 17:18:46.437949
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    # Try creating an instance of TruTVIE
    trutv_ie_instance = TruTVIE()
    print(trutv_ie_instance)


# Generated at 2022-06-14 17:18:48.016317
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:50.714189
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tv = TruTVIE()
    assert tv.ie_key() == 'TruTV'
    assert tv.ie_key() == TruTVIE.ie_key()


# Generated at 2022-06-14 17:19:41.777410
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Valid URL
    yield (
        'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
        'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
        'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
    )
    # Valid URL with series slug and episode ID

# Generated at 2022-06-14 17:19:53.266873
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert(trutv._VALID_URL == "https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))")

# Generated at 2022-06-14 17:20:05.015795
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:20:07.283704
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    TruTVIE(url)

# Generated at 2022-06-14 17:20:07.826044
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:15.820770
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    # Create a TruTVIE class object
    test_class_object = TruTVIE()

    # Test the actual URL
    assert test_class_object._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Test video extraction

# Generated at 2022-06-14 17:20:17.018173
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == TruTVIE._VALID_URL

# Generated at 2022-06-14 17:20:19.381271
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from unitest import UnitTestCase

    class TruTVIETest(UnitTestCase):
        def test_test(self):
            self.test_test(TruTVIE)

# Generated at 2022-06-14 17:20:23.618369
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tt = TruTVIE()
    assert(tt.get_pattern_re().pattern == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')
    return

# Generated at 2022-06-14 17:20:24.066131
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:03.433493
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:05.215956
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE is not None


# Generated at 2022-06-14 17:21:09.564909
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = TruTVIE._TEST['url']
    # Create an instance of class TruTVIE
    trutv_ie = TruTVIE()
    # Unit test for _real_extract()
    trutv_ie._real_extract(url)


# Generated at 2022-06-14 17:21:14.057299
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # A test for TruTVIE
    # Turn on verbose using:
    #     youtube_dl --verbose TruTVIE
    # Use the following to run it:
    #     youtube-dl -v --dump-json --dump-pages --write-info-json --no-progress TruTVIE
    # TODO: test TruTVIE
    TruTVIE()

# Generated at 2022-06-14 17:21:15.390326
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:17.302601
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    global ie_test
    ie_test = obj


test_TruTVIE()

# Generated at 2022-06-14 17:21:18.830447
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    truTV_IE = TruTVIE()
    # assert truTV_IE.valid()

test_TruTVIE()

# Generated at 2022-06-14 17:21:22.430991
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    x = TruTVIE("http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    x._extract_ngtv_info("http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html",{},{})
    assert(True)

# Generated at 2022-06-14 17:21:30.420750
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tt = TruTVIE()
    assert tt._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:21:37.832633
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    ie = TruTVIE()
    ie._download_json(
            'https://api.trutv.com/v2/web/series/clip/the-carbonaro-effect/sunlight-activated-flower',
            'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1')

# Generated at 2022-06-14 17:23:15.915619
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()

# Generated at 2022-06-14 17:23:22.544179
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    print("Constructor of class TruTVIE\n")
    test = TruTVIE()
    test._VALID_URL = r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:23.390389
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:24.369823
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:35.998634
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    truTV = TruTVIE()
    assert truTV._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:36.919815
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:39.513706
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(None)


# Generated at 2022-06-14 17:23:39.825840
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:40.457272
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    pass

# Generated at 2022-06-14 17:23:43.480761
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    TruTVIE(url)
