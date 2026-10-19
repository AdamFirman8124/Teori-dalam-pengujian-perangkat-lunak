

# Generated at 2022-06-14 17:06:00.018840
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # test for constructor of class TheStarIE
    return TheStarIE()

# Generated at 2022-06-14 17:06:03.847000
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:06:16.047997
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL == "https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html"

# Generated at 2022-06-14 17:06:16.952617
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    assert t != None

# Generated at 2022-06-14 17:06:18.405756
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    theStarIE = TheStarIE()
    assert not theStarIE == None

# Generated at 2022-06-14 17:06:21.102758
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert(ie != None)

# Generated at 2022-06-14 17:06:25.000108
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .test_ThePlatform import test_ThePlatformIE
    return test_ThePlatformIE.test_construcor(TheStarIE, {'url': 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'}, {'display_id': 'mankind-why-this-woman-started-a-men-s-skincare-line'})

# Generated at 2022-06-14 17:06:31.866132
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    #Define url to get unit test
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    #Define extractor to get video
    ie = TheStarIE()
    #Define video id to get video
    video_id = ie._match_id(url)
    #Define webpage to get video
    webpage = ie._download_webpage(url, video_id)
    #Define brightcove_id to get video
    brightcove_id = ie._search_regex(
        r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',
        webpage, 'brightcove id')
    #Define result of unit

# Generated at 2022-06-14 17:06:37.157423
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    obj = TheStarIE()

# Generated at 2022-06-14 17:06:38.597385
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	b = TheStarIE();
	assert (b != None)

# Generated at 2022-06-14 17:06:50.518894
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Init object
    object = TheStarIE()
    object.BRIGHTCOVE_URL_TEMPLATE
    object._download_webpage('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', '4732393888001')
    object._match_id('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    object._real_extract('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:02.050366
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star = TheStarIE()
    the_star.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

    assert the_star._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert the_star._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert the_star._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert the

# Generated at 2022-06-14 17:07:02.979767
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Basic init test
    TheStarIE()

# Generated at 2022-06-14 17:07:08.127375
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('4732393888001')
    TheStarIE(
        'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:11.447731
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None
    assert ie.BRIGHTCOVE_URL_TEMPLATE != ''


# Generated at 2022-06-14 17:07:14.405733
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(InfoExtractor())._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:15.897247
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:07:17.798403
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE()
    assert isinstance(instance, TheStarIE)


# Generated at 2022-06-14 17:07:19.617172
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	from TheStarIE import TheStarIE
	ie = TheStarIE()
	assert(ie is not None)

# Generated at 2022-06-14 17:07:25.623247
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    assert t.__class__.__name__ == 'TheStarIE'
    assert t.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'	
    assert t._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:34.048973
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  ie = TheStarIE()
  assert ie.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"

# Generated at 2022-06-14 17:07:37.041932
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:41.784906
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie = TheStarIE(url)
    assert ie is not None

# Generated at 2022-06-14 17:07:46.491611
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:49.878711
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    video = TheStarIE("test")
    assert(video.VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')
    assert(video.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')
    
# Test if the test object is as expected

# Generated at 2022-06-14 17:07:53.369285
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:07:55.674684
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()



# Generated at 2022-06-14 17:07:59.785888
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert (thestarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')


# Generated at 2022-06-14 17:08:03.478834
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    print(thestar)

# Generated at 2022-06-14 17:08:07.736923
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert isinstance(ie, TheStarIE)
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:08:19.321746
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:23.943768
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE('www.thestar.com', 'https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert instance._VALID_URL is not None
    assert instance.BRIGHTCOVE_URL_TEMPLATE is not None
    assert instance._TEST is not None

# Generated at 2022-06-14 17:08:31.932025
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	ie = TheStarIE()
	ie.url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
	ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
	ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:36.765671
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    brightcove_id = ie.BRIGHTCOVE_URL_TEMPLATE % '5472692624001'
    assert unicode(ie) == 'TheStarIE'
    assert ie._extract_video_id(brightcove_id) == '4732393888001'
    assert ie.BRIGHTCOVE_URL_TEMPLATE.endswith('index.html?videoId=%s')

# Generated at 2022-06-14 17:08:42.721173
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    IE = TheStarIE({})
    obj = IE._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert obj is not None
    assert len(obj.keys()) > 0
    assert type(obj) is dict

# Generated at 2022-06-14 17:08:54.132970
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    url = 'http://www.thestar.com/life'
    # remeber TheStarIE.BRIGHTCOVE_URL_TEMPLATE to test
    TheStarIE.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    # temp
    TheStarIE._TEST = {}

    TheStarIE(url)

if __name__ == "__main__":
    test_TheStarIE()

# Generated at 2022-06-14 17:08:55.751488
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        assert TheStarIE is not None
    except AssertionError:
        print("TheStarIE test failure")

# Generated at 2022-06-14 17:09:03.594614
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Check if it can extract and download videos from thestar.com"""

    # Instantiate the Unit Test class
    ie_instantiation_test = TheStarIE(None)

    # Check that it sucessfully instantiated by testing one of its properties
    assert ie_instantiation_test.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:09:11.809432
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info_dict = {
    "id": "4732393888001",
    "ext": "mp4",
    "title": "Mankind: Why this woman started a men\'s skin care line",
    "description": "Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.",
    "uploader_id": "794267642001",
    "timestamp": 1454353482,
    "upload_date": "20160201",
    }
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    inst = TheStarIE()

# Generated at 2022-06-14 17:09:22.952295
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    # Test URL parsing
    # It should match because id contains only digits
    assert ie._VALID_URL == ie._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # It should match because id contains alphanumeric characters
    assert ie._VALID_URL == ie._match_id('http://www.thestar.com/life/2016/02/01/a-man-s-skincare-line.html')
    # It should match because id contains a trailing slash

# Generated at 2022-06-14 17:09:47.262374
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(TheStarIE)
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:50.677677
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj=TheStarIE()
    obj._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:09:51.600938
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    extractor = TheStarIE()

# Generated at 2022-06-14 17:09:52.241356
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()

# Generated at 2022-06-14 17:09:55.426221
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.__class__.__name__ == 'TheStarIE'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:10:05.701701
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:10:12.618601
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie._downloader
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie._match_id(ie)
    ie._real_extract(ie)
    ie._download_webpage(ie)
    ie._search_regex(ie)
    ie.url_result(ie)

# Generated at 2022-06-14 17:10:14.651226
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Create an instance of TheStarIE
    # Check if the instance is an instance of TheStarIE
    # Check if the instance is an instance of InfoExtractor
    assert isinstance(TheStarIE, InfoExtractor)

# Generated at 2022-06-14 17:10:15.817950
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    src = TheStarIE()

# Generated at 2022-06-14 17:10:25.046157
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
   assert TheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:04.357123
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert isinstance(TheStarIE, InfoExtractor)


# Generated at 2022-06-14 17:11:10.642336
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test case for constructor to have brightcove_url_template and URL_REGEX
    test_object = TheStarIE()
    assert test_object.BRIGHTCOVE_URL_TEMPLATE == \
           'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert test_object._VALID_URL == \
           r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:17.349584
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """ Unit test for testing the constructor of class TheStarIE """
    
    TEST_URL = 'https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    TheStarIE(TEST_URL)
    pass

# Generated at 2022-06-14 17:11:19.861792
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._TEST['url']
    assert TheStarIE._TEST['info_dict']
    assert TheStarIE._TEST['params']


# Generated at 2022-06-14 17:11:22.958299
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extract("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:11:25.470236
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # a non-existing object
    obj = TheStarIE()
    assert obj is not None

# Generated at 2022-06-14 17:11:27.066747
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    name = "TheStarIE"
    
    TheStarIE(name)

# Generated at 2022-06-14 17:11:27.596402
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	TheStarIE()

# Generated at 2022-06-14 17:11:33.167023
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    print(info)
    info = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', params = {'skip_download': True})
    print(info)

# Generated at 2022-06-14 17:11:33.966404
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    temp = TheStarIE()
    assert temp!=None

# Generated at 2022-06-14 17:13:09.302103
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie != None

# Generated at 2022-06-14 17:13:14.550857
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print("\nUnit test for TheStarIE")
    ie = TheStarIE()
    test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    test_result = ie.suitable(test_url)
    print("Test Result: %s", test_result)
    return

# Generated at 2022-06-14 17:13:17.253005
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = TheStarIE.BRIGHTCOVE_URL_TEMPLATE
    ie.extract(TheStarIE._TEST['url'])
    assert ie.BRIGHTCOVE_URL_TEMPLATE == TheStarIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:13:25.950224
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=99999'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=99999'

# Generated at 2022-06-14 17:13:32.663076
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:37.977936
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    Test for constructor of class TheStarIE
    """
    obj = TheStarIE('http://www.thestar.com/videonetwork/index.html?bcpid=1886276297001&bctid=4556624150001')
    assert('videonetwork' in obj)
    assert('thestarIE' in obj)
    assert('thestar' in obj)

# Generated at 2022-06-14 17:13:40.368710
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE();

# Generated at 2022-06-14 17:13:45.166603
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # TheStarIE.__init__
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie._downloader == None
    assert ie._WORKING == True


# Generated at 2022-06-14 17:13:48.752504
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s', 'Value of variable BRIGHTCOVE_URL_TEMPLATE is not correct'

# Generated at 2022-06-14 17:13:50.583652
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()  # Should not raise