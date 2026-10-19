

# Generated at 2022-06-14 17:05:57.227170
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Just check that the constructor doesn't throw an error
    TheStarIE ()

# Generated at 2022-06-14 17:06:02.130648
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test the constructor of class TheStarIE
    # Since Bfie is still in development, the constructor is expected
    # to throw an Exception
    try:
        thestar = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
        assert False
    except:
        assert True

# Generated at 2022-06-14 17:06:07.809358
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # test the methods in heapq.
    ie.heapify()
    ie.heappush(ie.heap, -1)
    ie.heappop()
    ie.heappushpop()

# Generated at 2022-06-14 17:06:11.676168
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:06:12.268521
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	TheStarIE()

# Generated at 2022-06-14 17:06:22.035362
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:30.885598
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    info_dict = {
        'id': '4732393888001',
        'ext': 'mp4',
        'title': 'Mankind: Why this woman started a men\'s skin care line',
        'description': 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.',
        'uploader_id': '794267642001',
        'timestamp': 1454353482,
        'upload_date': '20160201',
    }

# Generated at 2022-06-14 17:06:41.288464
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	expected_result = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'
	test_ie = TheStarIE()
	test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
	test_webpage = '<html><body><script>mainartBrightcoveVideoId = 4732393888001</script></body></html>'
	actual_result = test_ie._real_extract(test_url)
	# Checking that the url returned is the same as the one expected
	assert actual_result == expected_result

# Generated at 2022-06-14 17:06:43.602294
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert isinstance(ie, TheStarIE)
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 17:06:44.299604
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info = TheStarIE()
    print(info)

# Generated at 2022-06-14 17:06:56.143371
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html");
    expected_result = "4732393888001"
    assert ie._match_id("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html") == expected_result

# Generated at 2022-06-14 17:07:05.525190
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    #ie._download_webpage('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', '4732393888001')
    #ie._search_regex(r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)', 'https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', 'brightcove id')

# Generated at 2022-06-14 17:07:07.585583
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    #doctest.testmod()
    IE = TheStarIE(TheStarIE._VALID_URL)
    IE.IE(IE._VALID_URL)

# Generated at 2022-06-14 17:07:11.385270
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    IE = TheStarIE()
    assert IE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:17.538841
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Module info
    # mod.mod_type = 'module'
    # mod.name = 'TheStar'
    # mod.display_name = 'TheStar'
    # mod.ie_key = 'thestar'
    # mod.geo_countries = ['CA']

    # Info Extrator info
    # ie.ie_key = 'thestar'
    # ie.name = '__name__'
    # ie.display_name = 'thestar'
    # ie.add_ie('thestar', 'TheStarIE')

    # constructor test
    # ie = TheStarIE()
    assert True

# Generated at 2022-06-14 17:07:27.019393
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:30.841398
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    star = TheStarIE()
    # TheStarIE unit test
    assert star.get_url()
    assert star.get_md5()
    assert star.get_info_dicts()

# Generated at 2022-06-14 17:07:31.532721
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
        TheStarIE()

# Generated at 2022-06-14 17:07:32.623283
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    result = TheStarIE()
    print(result)

# Generated at 2022-06-14 17:07:37.323025
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Tests for constructor of class TheStarIE
    res = TheStarIE("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert(res.__class__.__name__ == "TheStarIE")



# Generated at 2022-06-14 17:07:46.087829
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:48.050406
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE({})


# Generated at 2022-06-14 17:07:49.162862
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    v = TheStarIE()
    assert v is not None

# Generated at 2022-06-14 17:07:53.070610
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_obj = TheStarIE(InfoExtractor)
    assert hasattr(test_obj, '_VALID_URL')
    assert hasattr(test_obj, '_TEST')
    assert hasattr(test_obj, 'BRIGHTCOVE_URL_TEMPLATE')

# Generated at 2022-06-14 17:07:58.714407
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') is not None

# Generated at 2022-06-14 17:08:03.779586
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.display_id == 'mankind-why-this-woman-started-a-men-s-skincare-line'

# Generated at 2022-06-14 17:08:08.126222
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # object instantiation
    thestar_ie = TheStarIE()
    # unit test for instance creation
    assert isinstance(thestar_ie, InfoExtractor)


# Generated at 2022-06-14 17:08:09.201060
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	x = TheStarIE()

# Generated at 2022-06-14 17:08:17.752112
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    VideoExtractorTest = TheStarIE(url ="http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert VideoExtractorTest.url == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    assert VideoExtractorTest.md5 == "2c62dd4db2027e35579fefb97a8b6554"

# Generated at 2022-06-14 17:08:26.816093
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    display_id = 'mankind-why-this-woman-started-a-men-s-skincare-line'
    webpage = 'This is webpage.'
    brightcove_id = '4732393888001'

    the_star_ie = TheStarIE()
    the_star_ie._download_webpage = lambda url, display_id: webpage
    the_star_ie._search_regex = lambda regex, webpage, name: brightcove_id

    tst_ie = test_TheStarIE()

# Generated at 2022-06-14 17:08:45.328878
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Unit test for constructor of class TheStarIE
    video_url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    date = "20160201"
    thestar = TheStarIE()
    thestar.test()

# Generated at 2022-06-14 17:08:52.841531
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    actual_result = ie.BRIGHTCOVE_URL_TEMPLATE
    expected_result = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert actual_result == expected_result

# Generated at 2022-06-14 17:08:58.531443
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test constructor of TheStarIE
    # TODO: add more tests
    assert TheStarIE._VALID_URL == "https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html"
    assert TheStarIE._TEST['url'] == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    pass

# Generated at 2022-06-14 17:09:01.060541
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Check that it can construct an instance of TheStarIE
    instance = TheStarIE('thestar.com')
    assert instance is not None

# Generated at 2022-06-14 17:09:08.975900
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    test_url2 = 'http://thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    TheStarIE.test_url = test_url
    TheStarIE._TEST['url'] = test_url2
    i = TheStarIE()
    assert i.test_url == test_url

# Generated at 2022-06-14 17:09:11.681708
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('https://www.thestar.com/entertainment/opinion/2016/01/31/rethink-your-recollection-of-the-1984-orwell-film.html')

# Generated at 2022-06-14 17:09:19.370261
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print (TheStarIE().extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'))
    print (TheStarIE().extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'))

# Generated at 2022-06-14 17:09:19.965758
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:09:22.674346
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_class = TheStarIE()
    assert test_class.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:25.090463
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_obj = TheStarIE()
    assert test_obj
    assert test_obj.__class__.__name__ == 'TheStarIE'

# Generated at 2022-06-14 17:09:49.573061
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://localhost'  # ignore original test, see below
    s = ie.BRIGHTCOVE_URL_TEMPLATE % '12345'  # see class-level test, below
    assert s == 'http://localhost'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://localhost'

# Test cases from TheStarIE._TEST

# Generated at 2022-06-14 17:09:51.834610
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:09:53.589318
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:10:04.088576
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test the constructor, which is supposed to set the class's _VALID_URL and other attributes
    ie = TheStarIE()
    valid_url = ie._VALID_URL
    assert("www.thestar.com" in valid_url)
    assert("html" in valid_url)
    assert("(?P<id>.+)" in valid_url)
    assert("_VALID_URL" in dir(ie))
    assert("_TEST" in dir(ie))
    assert("BRIGHTCOVE_URL_TEMPLATE" in dir(ie))
    assert("_download_webpage" in dir(ie))
    assert("_real_extract" in dir(ie))

# Generated at 2022-06-14 17:10:07.057048
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for class TheStarIE"""
    extractor = TheStarIE()
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:10:14.710369
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_cases = [
        (False, 'http://video.thestar.com/thesocial/thesocial/thesocial-episode-1.html'),
        (False, 'http://www.thestar.com/yourtoronto/summer-of-festivals.html'),
        (False, 'http://www.thestar.com/news/canada/2016/02/02/north-korea-detained-canadian-korean-missionary-park-chul-hwan.html'),
        (True, 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'),
    ]

# Generated at 2022-06-14 17:10:20.187358
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    expected_attributes = ['BRIGHTCOVE_URL_TEMPLATE', '_TEST', '_VALID_URL']
    for key in expected_attributes:
        assert key in ie.__dict__, ('Attribute "%s" not found in %s' % (key, ie.__dict__))


# Generated at 2022-06-14 17:10:31.863004
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test for constructor of class TheStarIE"""
    # initialize a subclass of TheStarIE
    test_instance = TheStarIE()
    # test if all attributes of test_instance are as expected
    assert test_instance.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert test_instance._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:10:33.400189
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE



# Generated at 2022-06-14 17:10:36.081647
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    TheStarIE()._real_extract(url)

# Generated at 2022-06-14 17:11:18.852608
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    assert t.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:21.878982
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:24.277670
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test the constructor of class TheStarIE"""
    my_obj = TheStarIE(TheStarIE._VALID_URL, TheStarIE._TEST)
    my_obj._real_extract(TheStarIE._VALID_URL)

# Generated at 2022-06-14 17:11:26.216448
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:28.441917
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE(None, None, True)
    except Exception:
        print("Constructor of class TheStarIE throws exception")
        assert(False)
    assert(True)

# Generated at 2022-06-14 17:11:36.625227
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:37.392595
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert TheStarIE(InfoExtractor())

# Generated at 2022-06-14 17:11:38.343399
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:11:44.650087
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:50.987456
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert 'TheStarIE' == ie.ie_key()
    assert 'thestar.com' == ie.host()
    assert ie._VALID_URL == ie.url_re()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == ie.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:13:27.095765
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    thestar.init()



# Generated at 2022-06-14 17:13:30.721660
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Tests for class TheStarIE
    # Unit test for constructor of class TheStarIE
    # Instantiation namespace contains only strings
    assert isinstance(TheStarIE._VALID_URL, str)
    assert isinstance(TheStarIE._TEST, dictionary)
    assert isinstance(TheStarIE.BRIGHTCOVE_URL_TEMPLATE, str)


# Generated at 2022-06-14 17:13:36.297517
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert (TheStarIE.__name__ == 'TheStarIE')
    ie = TheStarIE()
    ie._download_webpage(TheStarIE._TEST['url'], '4732393888001')
    assert (ie._match_id(TheStarIE._VALID_URL) == '4732393888001.html')

# Generated at 2022-06-14 17:13:37.120991
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:13:41.702698
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html');

# Generated at 2022-06-14 17:13:42.685051
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE.__name__ == 'TheStar'

# Generated at 2022-06-14 17:13:48.113742
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Unit test begins
    test_TheStarIE_instance = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    # Testing instance (if exist) of class TheStarIE
    assert isinstance(test_TheStarIE_instance, TheStarIE)
    # Unit test ends


# Generated at 2022-06-14 17:13:58.501277
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    temp_obj = TheStarIE(InfoExtractor)
    assert temp_obj.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"
    assert temp_obj._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert temp_obj._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:13:59.974758
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie

# Generated at 2022-06-14 17:14:05.028630
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'