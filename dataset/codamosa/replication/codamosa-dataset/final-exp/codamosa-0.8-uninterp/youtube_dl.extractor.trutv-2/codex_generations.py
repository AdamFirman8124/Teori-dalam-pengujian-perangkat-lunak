

# Generated at 2022-06-14 17:16:34.358248
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
    return

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:16:38.257154
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert TruTVIE._VALID_URL == instance._VALID_URL
    assert TruTVIE._TEST == instance._TEST
    assert TruTVIE.name == 'Turner:truTV'
    assert TruTVIE.ie_key() == 'Turner:truTV'
    assert TruTVIE.ie_key() == TruTVIE.ie_key(instance)


# Generated at 2022-06-14 17:16:49.289311
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    x = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    # Test the three types of URLs parsed by extractor
    assert x.get_series('https://www.trutv.com/shows/moonshiners.html') == 'moonshiners'
    assert x.get_season('https://www.trutv.com/shows/impractical-jokers/season-03/index.html') == 'season-03'
    assert x.get_episode('https://www.trutv.com/shows/adam-ruins-everything/videos/adam-ruins-everything-adam-ruins-everything.html') == 'adam-ruins-everything-adam-ruins-everything'

# Generated at 2022-06-14 17:16:52.613527
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    class_ = TruTVIE
    print("Testing class %s" % class_.__name__)
    assert callable(class_)
    if not class_ is object:
        instance = class_()
        assert isinstance(instance, class_)
        assert callable(instance)


# Generated at 2022-06-14 17:16:59.785005
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    A unit test for class TruTVIE.
    """
    # Test with a TruTV specified url
    _TEST_TruTVIE_URL = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    TruTVIE()._real_extract(_TEST_TruTVIE_URL)
    _TEST_TruTVIE_URL = 'https://www.trutv.com/full-episodes/23119/the-carbonaro-effect-season-1-episode-7-flip-out/videos/sunlight-activated-flower.html'
    TruTVIE()._real_extract(_TEST_TruTVIE_URL)

# Generated at 2022-06-14 17:17:02.749011
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    '''
    Test that the constructor of the class TruTVIE is working
    '''
    trutv = TruTVIE()
    assert(trutv is not None)

# Generated at 2022-06-14 17:17:03.881719
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert isinstance(ie, TruTVIE)


# Generated at 2022-06-14 17:17:04.515699
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:05.057706
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE()

# Generated at 2022-06-14 17:17:07.416555
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_url = TruTVIE._TEST['url']
    TruTVIE(test_url)

# Generated at 2022-06-14 17:17:18.420623
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:18.930738
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:21.907937
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
	TruTVIE(url)

# Generated at 2022-06-14 17:17:23.878453
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
    return True

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:17:27.209739
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.__name__ == "TruTVIE"

# Generated at 2022-06-14 17:17:36.650761
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_test = TruTVIE()
    assert trutv_test._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:38.284353
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.ie_key() == 'TruTV'

# Generated at 2022-06-14 17:17:43.924774
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    trutvie = TruTVIE()

# Generated at 2022-06-14 17:17:45.750652
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


# Generated at 2022-06-14 17:17:47.168524
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    print(trutv)

# Generated at 2022-06-14 17:17:57.916906
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:59.851784
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE._VALID_URL
    TruTVIE._TEST
    TruTVIE()._real_extract

# Generated at 2022-06-14 17:18:02.081238
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.IE_NAME == 'trutv'
    assert ie.IE_DESC == 'truTV'

# Generated at 2022-06-14 17:18:13.742296
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    # Constructor with valid URL
    obj = TruTVIE("http://www.trutv.com/shows/full-episodes/2/videos/an-american-in-chechnya.html")

    # Correct class type
    assert isinstance(obj, TruTVIE)

    # Correct IE name
    assert obj.ie_key() == "TruTV"

    # Correct ID
    assert obj.video_id == "an-american-in-chechnya"

    # Incorrect URL
    obj = TruTVIE("http://www.truTV.com/shows/full-episodes/x/videos/an-american-in-chechnya.html")

    # Correct IE name
    assert obj.ie_key() == "TruTV"

    # Correct ID

# Generated at 2022-06-14 17:18:21.764907
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # This test checks TruTVIE instance is created
    # with valid _VALID_URL as its attribute
    obj = TruTVIE("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    assert obj._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:26.764384
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    testInput = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    expectOutput = None

    realOutput = TruTVIE().suitable(testInput)
    assert realOutput == expectOutput, 'Test Fail: expectOutput = %s, realOutput = %s' % (expectOutput, realOutput)
    print('Test Pass')


# Generated at 2022-06-14 17:18:27.550720
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()


# Generated at 2022-06-14 17:18:29.674564
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    mr = TruTVIE()
    assert mr

# Generated at 2022-06-14 17:18:37.136283
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from youtube_dl.utils import DateRange
    # assert TruTVIE.__doc__
    assert TruTVIE._TEST
    assert TruTVIE.__name__
    assert TruTVIE._VALID_URL
    assert TruTVIE._download_webpage
    assert TruTVIE._search_regex
    assert TruTVIE._html_search_regex
    assert TruTVIE._extract_ngtv_formats
    assert TruTVIE._real_extract
    assert TruTVIE._TYPE
    assert TruTVIE._TESTS
    assert DateRange


# Generated at 2022-06-14 17:18:44.627131
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test for constructor of class TruTVIE
    trutv_url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    ie = TruTVIE()
    ie.url = trutv_url
    expected_result = {
        'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1',
        'ext': 'mp4',
        'title': 'Sunlight-Activated Flower',
        'description': "A customer is stunned when he sees Michael's sunlight-activated flower.",
    }
    assert expected_result == ie._TEST


# Generated at 2022-06-14 17:19:05.384774
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    pass

# Generated at 2022-06-14 17:19:11.260593
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	# Test 1:
	TruTVIE._VALID_URL = 'https://www.trutv.com/shows/the-carlton-dance/videos/the-carlton-dance.html'
	assert TruTVIE._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
	assert TruTVIE._TEST['info_dict'] == {'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1', 'ext': 'mp4', 'title': 'Sunlight-Activated Flower', 'description': "A customer is stunned when he sees Michael's sunlight-activated flower."}

# Generated at 2022-06-14 17:19:22.610843
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    trutv_ie = TruTVIE()
    video_info = trutv_ie._real_extract(url)

    assert video_info['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
    assert video_info['display_id'] == 'sunlight-activated-flower'
    assert video_info['title'] == 'Sunlight-Activated Flower'
    assert video_info['description'] == 'A customer is stunned when he sees Michael\'s sunlight-activated flower.'
    assert video_info['url'] == url
    assert video_info['site_name'] == 'truTV'

# Generated at 2022-06-14 17:19:25.047606
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE().extract("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")

# Generated at 2022-06-14 17:19:30.438434
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    constructor_test_class = TruTVIE('TruTV', 'http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert constructor_test_class.name == 'TruTV'
    assert constructor_test_class.url == 'http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'


# Generated at 2022-06-14 17:19:32.168775
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    urls = TruTVIE()._TEST['url']
    TruTVIE()._real_extract(urls)

# Generated at 2022-06-14 17:19:34.597255
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # create object of class TruTVIE
    obj = TruTVIE()
    # assert object is created
    assert obj != None

# Generated at 2022-06-14 17:19:42.533928
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Valid url
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    t = TruTVIE(TruTVIE.extractor)
    t.extract(url)
    # Invalid url
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower'
    t = TruTVIE(TruTVIE.extractor)
    t.extract(url)

# Generated at 2022-06-14 17:19:48.296692
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_TruTVIE = TruTVIE()
    test_TruTVIE.extract(test_TruTVIE._TEST.get('url'))
    #test_TruTVIE.download()

#test_TruTVIE()

# Generated at 2022-06-14 17:19:50.818762
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:20:43.470107
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    # Test with a valid link
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    # Test with an invalid link
    with pytest.raises(ExtractorError):
        ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/')

# Generated at 2022-06-14 17:20:50.411982
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test with valid link
    assert TruTVIE.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert TruTVIE.suitable('https://www.trutv.com/shows/impractical-jokers/videos/the-worst-challenge-ever.html')
    assert TruTVIE.suitable('https://www.trutv.com/shows/the-carbonaro-effect/full-episodes/11859-the-carbonaro-effect-the-useless-box.html')
    assert TruTVIE.suitable('https://www.trutv.com/shows/impractical-jokers/full-episodes/11860-impractical-jokers-charity-case.html')
    # Test with non valid link
   

# Generated at 2022-06-14 17:20:57.782534
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	# Test regular video
	TruTVIE()._real_extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
	# Test episode
	TruTVIE()._real_extract('https://www.trutv.com/full-episodes/1433024/the-carbonaro-effect-s02e03/1433233/to-the-rescue/')

# Generated at 2022-06-14 17:21:02.417310
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    TruTVIE()
    # assert TruTVIE(url, True).extract_info(url,True)
#    assert TruTVIE(url, True).extract_info(url,False)


# Generated at 2022-06-14 17:21:13.679437
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    url_str = "https://www.trutv.com/shows/the-carbonaro-effect/videos/" + \
              "sunlight-activated-flower.html"
    test_video_dict = {'url': url_str, 'info_dict': {'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1', 
        'ext': 'mp4', 'title': 'Sunlight-Activated Flower', 
        'description': "A customer is stunned when he sees Michael's sunlight-activated flower."}, 
        'params': {'skip_download': True}}
    test_video_str = str(test_video_dict)

# Generated at 2022-06-14 17:21:16.037170
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.__name__ == 'TruTVIE'

# Generated at 2022-06-14 17:21:20.479987
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	instance = TruTVIE()
	instance._extract_ngtv_info('f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1', {}, {'auth_required': True})
	instance._extract_ngtv_info('f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1', {}, {})

# Generated at 2022-06-14 17:21:25.412781
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Legacy link
    assert TruTVIE.suitable("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    # New link with the ID
    assert TruTVIE.suitable("https://www.trutv.com/shows/tacoma-fd/full-episodes/453864")

# Generated at 2022-06-14 17:21:25.898486
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE

# Generated at 2022-06-14 17:21:26.702340
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    (TruTVIE())


# Generated at 2022-06-14 17:23:16.048827
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    video_extractor_inst = TruTVIE()
    assert type(video_extractor_inst) == TruTVIE


# Generated at 2022-06-14 17:23:20.555975
# Unit test for constructor of class TruTVIE
def test_TruTVIE():  
    print()
    print("Testing TruTVIE:")
    print()
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    trutv_ie = TruTVIE()
    fetched_information = trutv_ie._real_extract(url)
    print(fetched_information)
    
test_TruTVIE()

# Generated at 2022-06-14 17:23:27.746675
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

		# Test for valid TruTV Url
		assert TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'


# Generated at 2022-06-14 17:23:29.272899
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:23:33.124744
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Try with the initializer
    try:
        TruTVIE()
    except:
        raise AssertionError("Initializer is not working as expected.")


# Generated at 2022-06-14 17:23:44.763132
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .test_utils import TestSearchParser
    from . import main as yt_main
    from .extractor.common import InfoExtractor
    try:
        InfoExtractor.IE_NAME.index('TruTVIE')
        print('Found TruTVIE class in list of IEs.  OK.')
    except ValueError:
        print('FAIL: Could not find TruTVIE class in list of IEs.')

    ie = yt_main.get_info_extractor('TruTVIE')
    assert ie is not None, 'Could not get TruTVIE instance.'


# Generated at 2022-06-14 17:23:49.316950
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test creating instance of class
    print("Testing TruTVIE class")
    tru_tv = TruTVIE()
    assert tru_tv is not None
    print("TruTVIE class test passed")

# Generated at 2022-06-14 17:23:56.524625
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html').url == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE('Sunlight-Activated Flower').title == 'Sunlight-Activated Flower'
    return TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html').title == 'Sunlight-Activated Flower'

test_TruTVIE()

# Generated at 2022-06-14 17:23:59.588517
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == TruTVIE._VALID_URL
    assert TruTVIE()._TEST == TruTVIE._TEST

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:24:00.460206
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
