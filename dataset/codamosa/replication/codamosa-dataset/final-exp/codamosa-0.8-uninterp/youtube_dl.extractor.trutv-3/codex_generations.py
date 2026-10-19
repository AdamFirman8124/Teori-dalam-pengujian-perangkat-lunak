

# Generated at 2022-06-14 17:16:32.146888
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Test the actual functions of TruTVIE

# Generated at 2022-06-14 17:16:35.848106
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert(ie.IE_NAME == ie.ie_key())
    assert(isinstance(ie, TurnerBaseIE))
    assert(ie.IE_NAME.find('truTV') > -1)

# Generated at 2022-06-14 17:16:36.910131
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(None)

# Generated at 2022-06-14 17:16:37.886210
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:42.743420
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:16:46.963871
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    print("Testing TruTVIE constructor")
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    trutv = TruTVIE(url)
    return trutv, trutv.get_download_url()


# Generated at 2022-06-14 17:16:58.476092
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    if __name__ == '__main__':
        test = TruTVIE()
        test_url = 'https://www.trutv.com/shows/impractical-jokers/videos/jokers-royale-the-purse-drop.html'
        result = test._real_extract(test_url)
        print(result)
        print(result['id'])
        print(result['display_id'])
        print(result['title'])
        print(result['series'])
        print(result['season_number'])
        print(result['episode_number'])
        print(result['auth_required'])
        print(result['format'])
        if result['auth_required']:
            print("%s Needs Authentication" % result['title'])

# Generated at 2022-06-14 17:17:03.803698
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # This test is for TruTVIE constructor
    # Testcase:
    #    Test the constructor of class TruTVIE
    #    
    # Expected Results:
    #    Make sure TruTVIE object is not None
    #
    trutvIE = TruTVIE()
    assert trutvIE is not None


# Generated at 2022-06-14 17:17:09.978508
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'


# Generated at 2022-06-14 17:17:11.552993
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.ie_key() == 'TurnerBase'

# Generated at 2022-06-14 17:17:23.116928
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:17:29.904677
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

    # Check TruTVIE._real_extract() function
    ie = TruTVIE()
    ie._real_extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert ie._real_extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:17:31.385223
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

	TruTv = TruTVIE()
	assert TruTv

# Generated at 2022-06-14 17:17:38.897066
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	trutv = TruTVIE()
	assert trutv._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:39.941246
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert isinstance(instance, TruTVIE)

# Generated at 2022-06-14 17:17:41.494701
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE("init")._real_extract("init")

# Generated at 2022-06-14 17:17:41.979905
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:48.760177
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE().to_screen('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    TruTVIE().to_screen('https://www.trutv.com/full-episodes/1896133/the-carbonaro-effect-season-2-sunlight-activated-flower.html')

# Generated at 2022-06-14 17:17:58.995403
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert TruTVIE._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

# Class TruTVIE is the object for extracting information from URL
myTruTVIE = TruTVIE()

# Class TruTVIE has function extract from '_TEST' and prints extracted information

# Generated at 2022-06-14 17:18:00.049660
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('test.test')

# Generated at 2022-06-14 17:18:20.721324
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert obj._downloader.params['skip_download'] == True

# Generated at 2022-06-14 17:18:24.727742
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:25.144767
# Unit test for constructor of class TruTVIE

# Generated at 2022-06-14 17:18:31.522873
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
  url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
  trutvIE = TruTVIE().extract(url)
  assert isinstance(trutvIE, dict), "TruTVIE constructor failed"

# Generated at 2022-06-14 17:18:36.286699
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    video = TruTVIE("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    assert video.video_id == "f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1"
    assert video.series_slug == "the-carbonaro-effect"
    assert video.clip_slug == "sunlight-activated-flower"
    assert video.video_id == None

    video = TruTVIE("https://www.trutv.com/shows/the-carbonaro-effect/168197")
    assert video.video_id == "168197"
    assert video.series_slug == "the-carbonaro-effect"
    assert video.clip_slug == None
    assert video.video

# Generated at 2022-06-14 17:18:40.803510
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    print(obj._VALID_URL)
    print(obj._TEST)

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:18:43.343541
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE().extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:18:50.865996
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    print("Testing constructor of TruTVIE")

    if obj._VALID_URL != "https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))":
        print("Invalid value for TruTVIE._VALID_URL")


# Generated at 2022-06-14 17:18:58.291086
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    print('\n'.join(sorted(ie.IE_NAME for ie in gen_extractors(
        ie, TruTVIE._TEST['url'], []) if ie.IE_NAME)))
    print('\n'.join(sorted(ie.IE_NAME for ie in gen_extractors(
        ie, TruTVIE._TEST['url'], []) if ie.IE_NAME)))
    assert TruTVIE()._VALID_URL == TruTVIE.VALID_URL
    assert TruTVIE()._TEST == TruTVIE.TEST

# Generated at 2022-06-14 17:19:02.440613
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        # Try to run the code
        TruTVIE()
    except Exception as e:
        # If the code fails, print information
        print("TruTVIE()")
        print("TruTVIE constructor")
        print("Traceback information = " + str(e))
        # If the code fails, the test fails
        assert False
    else:
        # If the code runs, the test passes
        assert True


# Generated at 2022-06-14 17:19:22.769174
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Inputs, behaviors and outputs
    TruTVIE()

# Generated at 2022-06-14 17:19:24.702642
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    expected = TruTVIE(TurnerBaseIE())
    TruTVIE(TurnerBaseIE()) == expected

# Generated at 2022-06-14 17:19:25.297645
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE

# Generated at 2022-06-14 17:19:26.935549
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Unit test for constructor of class TruTVIE
    """
    TruTVIE()

# Generated at 2022-06-14 17:19:27.350216
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:27.894590
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:32.553740
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()
    assert trutv_ie.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert not trutv_ie.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/')
    assert not trutv_ie.suitable('https://www.trutv.com/shows/the-carbonaro-effect/')

# Generated at 2022-06-14 17:19:33.674251
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()

# Generated at 2022-06-14 17:19:34.324127
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()

# Generated at 2022-06-14 17:19:38.211013
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert (
        TruTVIE.__name__ == "TruTVIE" and
        TruTVIE.__doc__ == "TruTVIE()"
    )


# Generated at 2022-06-14 17:20:23.655481
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:24.207859
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:34.990311
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Unit test function for TruTVIE."""
    ttvie = TruTVIE()
    assert ttvie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert ttvie._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

# Generated at 2022-06-14 17:20:35.959133
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._VALID_URL

# Generated at 2022-06-14 17:20:36.381827
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:37.152291
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert(True)

# Generated at 2022-06-14 17:20:44.230007
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert trutv.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert trutv.suitable('https://www.trutv.com/shows/the-carbonaro-effect/full-episodes/light-bulb-life-erase-your-age-put-it-in-reverse-and-more-1595772')

# Generated at 2022-06-14 17:20:44.818782
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:46.210513
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    new_TruTVIE = TruTVIE()

# Generated at 2022-06-14 17:20:47.158807
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:22:25.572039
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
    except:
        return False
    return True

# Generated at 2022-06-14 17:22:28.843515
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Constructor test for class TruTVIE
    """
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    TruTVIE('https://www.trutv.com/full-episodes/1384/the-carbonaro-effect-s03e01-ep01/')


# Generated at 2022-06-14 17:22:29.616104
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:22:38.980923
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.suitable(ie.ie_key())
    ie.download_webpage(TruTVIE._TEST['url'], None)
    ie.working()
    ie._real_initialize(TruTVIE._TEST['url'])
    assert TruTVIE._TEST['url'] == ie._match_id(TruTVIE._TEST['url'])
    ie._real_extract(TruTVIE._TEST['url'])
    ie.report_warning(TruTVIE._TEST['url'])
    ie.add_default_headers({})
    ie.to_screen(TruTVIE._TEST['url'])
    ie.try_get(TruTVIE._TEST['url'], list())
    ie.report_extraction({})


# Generated at 2022-06-14 17:22:43.050134
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.suitable(TruTVIE._TEST['url'])
    assert TruTVIE(TruTVIE._TEST['url'])._VALID_URL == TruTVIE._VALID_URL


# Generated at 2022-06-14 17:22:44.105071
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()

# Generated at 2022-06-14 17:22:51.677756
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test valid URLs
    OKAY_URL = ['https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
        'https://www.trutv.com/full-episodes/the-carbonaro-effect/videos/sunlight-activated-flower.html',
        'https://www.trutv.com/shows/the-carbonaro-effect/3/episode/Double-Trouble.html',
        'https://www.trutv.com/shows/tacoma-fd/videos/tacoma-fd-sneak-peek.html',
        'https://www.trutv.com/full-episodes/tacoma-fd/videos/tacoma-fd-sneak-peek.html']

# Generated at 2022-06-14 17:22:52.278792
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:02.459899
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract(r'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert ie.title == 'Sunlight-Activated Flower'
    assert ie.description == "A customer is stunned when he sees Michael's sunlight-activated flower."
    assert ie.series == "The Carbonaro Effect"
    assert ie.episode_number == 14
    assert ie.season_number == 5
    assert ie.timestamp == 1518571162
    assert ie.duration == 615

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:23:03.258214
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
