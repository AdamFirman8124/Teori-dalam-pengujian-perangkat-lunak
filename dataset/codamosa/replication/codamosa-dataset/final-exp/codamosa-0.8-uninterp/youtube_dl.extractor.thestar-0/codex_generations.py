

# Generated at 2022-06-14 17:06:00.326092
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE("www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:06:02.463376
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # test TheStarIE object create
    TheStarIE()

# Generated at 2022-06-14 17:06:08.545506
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s', 'Failed to set default template for URL'

# Generated at 2022-06-14 17:06:19.899610
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:21.369667
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
		test_instance = TheStarIE()
		assert isinstance(test_instance, InfoExtractor)

# Generated at 2022-06-14 17:06:24.553933
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert TheStarIE().BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:29.419188
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie._TEST
    ie._VALID_URL
    ie._download_webpage
    ie._match_id
    ie._real_extract
    ie._search_regex
    ie.url_result
    ie.url_result
    ie.url_result
    ie.url_result

# Generated at 2022-06-14 17:06:30.074552
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:06:40.772569
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert 'TheStarIE' in globals()
    ie = TheStarIE()
    test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie._match_id(test_url)
    test_webpage = ie._download_webpage(test_url, '2342342')
    assert ie._search_regex(
        r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',
        test_webpage, 'brightcove id')
    test_download = ie.BRIGHTCOVE_URL_TEMPLATE % '4732393888001'

# Generated at 2022-06-14 17:06:44.815131
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:49.959575
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:51.817534
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """ Unit test for constructor of class TheStarIE. """
    TheStarIE()

# Generated at 2022-06-14 17:07:00.569379
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    # Test that TheStarIE uses the correct test, and that
    # TheStarIE does not initialize to failure
    assert len(ie._TEST) > 1
    assert ie.IE_NAME == 'thestar'
    assert ie._VALID_URL is not None
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None


# Generated at 2022-06-14 17:07:02.274145
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    video = TheStarIE()
    video.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:07:10.069391
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE()
    assert(instance._VALID_URL == "^(?P<protocol>https?://)?(?P<url>.*thestar\.com/.*)\.html")
    assert(instance._TEST['url'] == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert(instance._TEST['md5'] == "2c62dd4db2027e35579fefb97a8b6554")
    assert(instance._TEST['info_dict']['id'] == "4732393888001")
    assert(instance._TEST['info_dict']['ext'] == "mp4")

# Generated at 2022-06-14 17:07:11.039933
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    tester = TheStarIE()
    assert tester is not None

# Generated at 2022-06-14 17:07:18.527199
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:19.458159
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	obj = TheStarIE()

# Generated at 2022-06-14 17:07:24.163325
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie = TheStarIE()
    ie = TheStarIE()
    ie = TheStarIE()
    ie = TheStarIE()
    ie = TheStarIE()
    ie = TheStarIE()
    ie = TheStarIE()
    ie = TheStarIE()
    ie = TheStarIE()


# Generated at 2022-06-14 17:07:25.155766
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    return TheStarIE()


# Generated at 2022-06-14 17:07:36.094335
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:37.453964
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.url_result()

# Generated at 2022-06-14 17:07:38.964320
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(TheStarIE._create_ie()) == TheStarIE

# Generated at 2022-06-14 17:07:39.818711
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:07:44.547492
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # To construct an object of TheStarIE, please pass the params like this:
    # thestar = TheStarIE(url)
    pass

# Generated at 2022-06-14 17:07:49.193786
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE=='http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL==r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:07:57.981990
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE({})
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:00.128608
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    '''
    Unit test for constructor of class TheStarIE
    '''
    my_IE = TheStarIE()

# Generated at 2022-06-14 17:08:03.391588
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    test if the right instance of info extractor is constructed
    """
    t = TheStarIE()
    if not isinstance(t, (InfoExtractor)):
        print("Not the right instance of info extractor")

# Generated at 2022-06-14 17:08:07.744635
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE()
    except:
        assert False, 'Can not construct class TheStarIE'


# Generated at 2022-06-14 17:08:25.263545
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from youtube_dl.utils import ExtractorError
    assert isinstance(TheStarIE, type)
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie = TheStarIE(url)
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie.VALID_URL == ie._VALID_URL
    ie = TheStarIE(ie._VALID_URL)

# Generated at 2022-06-14 17:08:26.103390
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL is not None

# Generated at 2022-06-14 17:08:30.077460
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:31.858271
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    IE = TheStarIE()
    assert IE.__class__ == TheStarIE


# Generated at 2022-06-14 17:08:33.285234
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    # Test for constructor
    # TheStarIE()
    assert True

# Generated at 2022-06-14 17:08:36.050816
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test regular case
    TheStarIE()._real_extract(
        'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:08:40.462946
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:08:45.378897
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	class_ = TheStarIE
	assert_equal(class_.__name__, "TheStarIE")

	instance = class_()
	assert_equal(instance.__class__, class_)
	assert_raises(AttributeError, lambda:instance.__setattr__('foo', 'bar'))

# Generated at 2022-06-14 17:08:54.999353
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert (ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')
    ie._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')


# Generated at 2022-06-14 17:09:00.487757
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(TheStarIE.create_geo_restricted_request('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'))

# Generated at 2022-06-14 17:09:21.233474
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie = TheStarIE(url)
    assert ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:09:23.278966
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE({})

# Generated at 2022-06-14 17:09:27.646960
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert t.suitable(url) == 'true'
    assert t.IE_NAME == 'TheStar'

# Generated at 2022-06-14 17:09:31.914779
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:09:35.783531
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    a = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    print(a.__dict__)
test_TheStarIE()

# Generated at 2022-06-14 17:09:41.470571
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	# Test for empty url
	try:
		TheStarIE(None)
		assert(False)
	except TypeError:
		assert(True)

	# Test for invalid url
	try:
		TheStarIE('http://www.thestar.com')
		assert(False)
	except TypeError:
		assert(True)

	# Test for valid url
	theStar = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
	assert(theStar.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

#

# Generated at 2022-06-14 17:09:47.164125
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    Test creating an instance of the TheStarIE class.
    """
    info_extractor = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert isinstance(info_extractor, TheStarIE)

# Generated at 2022-06-14 17:09:48.974767
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	try:
		TheStarIE("test","test")
	except:
		assert False


# Generated at 2022-06-14 17:09:56.692976
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Create instance of this class
    the_star = TheStarIE()
    # Test instance
    assert isinstance(the_star, TheStarIE)
    # Test values of already instantiated class members
    assert the_star._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert the_star._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert the_star._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'

# Generated at 2022-06-14 17:10:02.812008
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('', 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:10:37.131207
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    i = TheStarIE()
    assert i.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:10:44.474381
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    input_data = "/life/2015/08/17/straight-up-talks-to-the-stars-david-haydn-jones.html"
    expected_data = ['4732393888001']
    assert ie._match_id(input_data) == expected_data

# Generated at 2022-06-14 17:10:48.384657
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    except:
        raise AssertionError('TheStarIE object creation failed.')

# Generated at 2022-06-14 17:10:51.246937
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    p = TheStarIE()
    assert p._extract_brightcove_url('')


# Generated at 2022-06-14 17:10:51.871660
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE

# Generated at 2022-06-14 17:10:56.105393
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	url = TheStarIE._VALID_URL
	i = TheStarIE(url, {})

# Generated at 2022-06-14 17:10:56.975228
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	pass

# Generated at 2022-06-14 17:10:59.134713
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()

# Generated at 2022-06-14 17:11:00.851052
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star = TheStarIE()
    assert the_star != None

# Generated at 2022-06-14 17:11:10.883009
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test = TheStarIE()._TEST
    assert test['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert test['md5'] == '2c62dd4db2027e35579fefb97a8b6554'

# Generated at 2022-06-14 17:12:37.686820
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:12:48.456617
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'

# Generated at 2022-06-14 17:12:52.617307
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:12:55.815803
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extract('http://www.thestar.com/news/world/2015/10/11/gchq-spied-on-wikileaks-and-associated-press.html')

# Generated at 2022-06-14 17:12:59.649560
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert hasattr(ie, 'BRIGHTCOVE_URL_TEMPLATE')
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:07.183773
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	"""
	Whether it can detect an url and extract the video id
	
	test for *_VALID_URL*
	"""
	test1 = TheStarIE
	test = test1._VALID_URL
	assert "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html" \
	== test
	

# Generated at 2022-06-14 17:13:13.211093
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Arrange
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    instance = TheStarIE()

    # Act
    result = instance.extract(url)

    # Assert
    assert isinstance(result, dict)
    assert result['id'] == '4732393888001'

# Generated at 2022-06-14 17:13:22.526201
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info_dict = {
        'id': '4732393888001',
        'ext': 'mp4',
        'title': 'Mankind: Why this woman started a men\'s skin care line',
        'description': 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.',
        'uploader_id': '794267642001',
        'timestamp': 1454353482,
        'upload_date': '20160201',
    }
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    BrightcoveNew = 'BrightcoveNew'
    brightcove_id = '4732393888001'
    BRIGHTCOVE_URL_

# Generated at 2022-06-14 17:13:30.867412
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar_ie = TheStarIE()
    # test extraction of complete URL segment
    assert thestar_ie._match_id("https://www.thestar.com/#thestar_nav") is None
    assert thestar_ie._match_id("https://www.thestar.com/news/gta/2017/11/29/toronto-police-recover-body-of-27-year-old-man-in-etobicoke-creek.html") == 'toronto-police-recover-body-of-27-year-old-man-in-etobicoke-creek'

# Generated at 2022-06-14 17:13:32.296837
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    UnitTest(TheStarIE).test_basic()