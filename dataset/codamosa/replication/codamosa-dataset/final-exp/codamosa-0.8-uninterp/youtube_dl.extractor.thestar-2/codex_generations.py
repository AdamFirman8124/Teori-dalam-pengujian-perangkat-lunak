

# Generated at 2022-06-14 17:06:03.689298
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    unit_test = TheStarIE()
    assert unit_test._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:13.863871
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for constructor of class TheStarIE."""
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:06:26.004172
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:28.489543
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    pass

# Generated at 2022-06-14 17:06:34.389389
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    video = TheStarIE()
    # Test for real video
    video.url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert video._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    # Test for fake video
    video.url = 'This is not a url.'
    assert not video._VALID_URL == r'This is not a url.'

# Generated at 2022-06-14 17:06:37.273782
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Instance of class TheStarIE
    TheStarIE()

# Generated at 2022-06-14 17:06:40.820288
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE(InfoExtractor('TheStarIE'))._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:06:43.980336
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:54.734624
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Create a test instance of class TheStarIE
    myInstance = TheStarIE()

    # Test the _VALID_URL regex
    matchObject = re.match(myInstance._VALID_URL, "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert(matchObject)

    # Test the _TEST block
    test_block = myInstance._TEST
    assert(test_block['url'] == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:06:58.512423
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:08.909501
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE({})
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:09.509889
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:07:12.429432
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:16.358875
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE()
    the_star_ie.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:07:17.849823
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    t = TheStarIE("TheStarIE")

# Generated at 2022-06-14 17:07:23.451603
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:24.754262
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	the_star_ie = TheStarIE()


# Generated at 2022-06-14 17:07:34.464550
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test constructor of class TheStarIE
    ie_obj = TheStarIE()
    # Check for expected attributes
    assert ie_obj.yuletide_test
    assert ie_obj.BRIGHTCOVE_URL_TEMPLATE
    assert ie_obj._VALID_URL

    # Test video extraction from the given url
    # Currently skips m3u8 download test due to https://github.com/rg3/youtube-dl/issues/8819
    # TODO: Remove 'skip_download' once the above test is fixed
    youtube_dl_arguments = {
        'format': 'best',
        'skip_download': True,
    }
    ie_obj._downloader.cache.remove('4732393888001')

# Generated at 2022-06-14 17:07:35.099412
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()

# Generated at 2022-06-14 17:07:36.169125
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.constructor()


# Generated at 2022-06-14 17:07:46.729863
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    video_id = '4732393888001'
    info = TheStarIE._build_brigthcove_url('4732393888001')
    info_expected = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'

# Generated at 2022-06-14 17:07:50.844824
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_item = TheStarIE(TheStarIE)
    assert test_item._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:51.831871
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:07:53.981860
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test = TheStarIE()
    test.BRIGHTCOVE_URL_TEMPLATE
    test._VALID_URL
    test._TEST

# Generated at 2022-06-14 17:07:59.659597
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test constructor of TheStarIE
    assert TheStarIE()._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:08:01.683522
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.IE_NAME == 'TheStar'


# Generated at 2022-06-14 17:08:03.905684
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE()
    except ValueError as e:
        assert e.message == 'BrightcoveNew module not installed'

# Generated at 2022-06-14 17:08:07.241739
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE(None)
    assert obj.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:08:11.993756
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    example = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert example.__class__.__name__ == 'TheStarIE'
    assert example.test() == True

# Generated at 2022-06-14 17:08:18.983218
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    obj.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    obj.url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    obj.display_id = 'mankind-why-this-woman-started-a-men-s-skincare-line'

    return obj.BRIGHTCOVE_URL_TEMPLATE, obj.url,

# Generated at 2022-06-14 17:08:31.949657
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    cls = TheStarIE
    print(cls.__name__)
    instance = cls()
    if instance.__class__.__name__ != cls.__name__:
        raise Exception('Class %s inheritance error' % cls.__name__)


# Generated at 2022-06-14 17:08:39.690305
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from constructs import TheStarIE
    obj = TheStarIE(id = "4732393888001", ext = "mp4", title = "Mankind: Why this woman started a men's skin care line", description = "Robert Cribb talks to Young Lee, the founder of Uncle Peter's MAN.", uploader_id = "794267642001", timestamp = 1454353482, upload_date = "20160201")
    assert isinstance(obj, TheStarIE)


# Generated at 2022-06-14 17:08:47.856321
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"
    assert ie._TEST.get('url') == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    assert ie._TEST.get('md5') == "2c62dd4db2027e35579fefb97a8b6554"
    assert ie._TEST.get('params') == {'skip_download': True}

# Generated at 2022-06-14 17:08:48.670248
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie != None

# Generated at 2022-06-14 17:08:54.354584
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        # Check is class TheStarIE is already created
        TheStarIE()
    except NameError:
        # Check and save constructor of class TheStarIE
        TheStarIE = type('TheStarIE',
                         (object,),
                         {'_html_search_regex': lambda self, *args: None,
                          '_real_extract': lambda self, *args: {}})
    return True

# Generated at 2022-06-14 17:08:57.082930
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    extractor = TheStarIE()
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId={}'

# Generated at 2022-06-14 17:09:01.528439
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	# Test for invalid URLs
	assert TheStarIE()._match_id(TheStarIE()._VALID_URL) != None
	# Test for valid URLs
	assert TheStarIE()._match_id(TheStarIE()._VALID_URL) != None
	

# Generated at 2022-06-14 17:09:02.151753
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:09:07.154532
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    # when url is not None
    url = "https://www.youtube.com/watch?v=u8W4uv_7kHQ"
    the_star_ie = TheStarIE(url)
    assert the_star_ie.url == url
    assert the_star_ie.name == "The Star"


# Generated at 2022-06-14 17:09:13.024071
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for constructor of class TheStarIE"""
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html' 

# Generated at 2022-06-14 17:09:35.041508
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    input_url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    output_url = "http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001"
    r = TheStarIE()._real_extract(input_url)
    assert(r.url == output_url)
    assert(r.ie == 'BrightcoveNew')

# Generated at 2022-06-14 17:09:41.200364
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:09:43.844861
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    Instantiate the class, then check whether it's an instance of InfoExtractor
    """
    test = TheStarIE()
    assert isinstance(test, InfoExtractor)


# Generated at 2022-06-14 17:09:51.110574
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:09:54.486511
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    id = '4732393888001'
    TheStarIE(url, id)

# Generated at 2022-06-14 17:09:56.603716
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	ie = TheStarIE()

# Generated at 2022-06-14 17:10:06.395907
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    # Use the constructor of InfoExtractor
    ie = InfoExtractor(True)

    # Use the constructor of TheStarIE
    ts_ie = TheStarIE(ie)

    # Check if the embeded IE has the right id
    assert ts_ie.ie._ies == ['BrightcoveNew']

    # This is the test case.

# Generated at 2022-06-14 17:10:08.548533
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	test_TheStarIE = TheStarIE("test", "test", "test", {}, {})
	assert isinstance(test_TheStarIE, InfoExtractor)

# Generated at 2022-06-14 17:10:10.212892
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	e = TheStarIE()
	assert isinstance(e, InfoExtractor)
	assert isinstance(e,TheStarIE)

# Generated at 2022-06-14 17:10:16.505066
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:01.002909
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    dummy_url = "https://www.thestar.com/news/world/us_election/2016/02/01/username-trumps-twitter-handle-not-so-secret-anymore.html"
    dummy_video_id = "4731620001001"
    res = TheStarIE._real_extract(TheStarIE(), dummy_url)
    assert(res['id'] == dummy_video_id)
    assert('BrightcoveNew' in res['ie_key'])

# Generated at 2022-06-14 17:11:03.491931
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    sut = TheStarIE()
    # Here is where we would actually test something


# Generated at 2022-06-14 17:11:07.192732
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:08.632120
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    pass

# Generated at 2022-06-14 17:11:19.690905
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/content/dam/thestar/life/shopping_style/2016/01/29/the-top-5-beauty-items-to-buy-in-february/the-top-5-beauty-items-to-buy-in-february.jpg')
    assert ie.name == 'thestar'
    assert ie.domain == 'http://www.thestar.com/content/dam/thestar/life/shopping_style/2016/01/29/the-top-5-beauty-items-to-buy-in-february/the-top-5-beauty-items-to-buy-in-february.jpg'

# Generated at 2022-06-14 17:11:20.239627
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:30.026804
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE()
    assert the_star_ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert the_star_ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:35.475840
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
  assert ie._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') == 'mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:11:37.465406
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print("Starting test for constructor of class TheStarIE")
    test_instance = TheStarIE()
    assert isinstance(test_instance, TheStarIE)


# Generated at 2022-06-14 17:11:39.500551
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(None)

# Generated at 2022-06-14 17:13:20.073141
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._TEST.get('url') == TheStarIE.BRIGHTCOVE_URL_TEMPLATE % TheStarIE._TEST.get('info_dict').get('id')

# Generated at 2022-06-14 17:13:25.048941
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test for the constructor of the class
    testobj = TheStarIE()
    assert isinstance(testobj, InfoExtractor)


# Unit tests for _real_extract function of class TheStarIE

# Generated at 2022-06-14 17:13:27.974444
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:13:29.100590
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  new_test = TheStarIE()
  assert new_test

# Generated at 2022-06-14 17:13:41.203335
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # test constructor of TheStarIE
    # create TheStarIE instance using 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html' as url
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # test if url of instance ie is 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:13:42.634928
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.count == 0


# Generated at 2022-06-14 17:13:46.130935
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:52.808897
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    match = TheStarIE._VALID_URL.match(url)
    assert match
    assert match.group('id')

# Generated at 2022-06-14 17:13:57.330681
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    instance = TheStarIE()
    # Check if the URL is valid
    instance.suitable(url)
    # Check if the URL is valid
    instance.suitable(url)

# Generated at 2022-06-14 17:14:07.219426
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

    # Basic instantiation, does not download anything
    theStar_ie = TheStarIE(test_url)

    # Test regular BrightCove video
    brightcoveNew_ie = theStar_ie._real_extract(test_url)
    assert brightcoveNew_ie.display_id == 'mankind-why-this-woman-started-a-men-s-skincare-line'
    assert brightcove