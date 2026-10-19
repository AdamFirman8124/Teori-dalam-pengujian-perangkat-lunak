

# Generated at 2022-06-14 17:05:57.819965
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert TheStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:02.574816
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE({},{'url':'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'})
    assert ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:06:05.492956
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE.__name__ == 'TheStarIE'
    assert hasattr(TheStarIE, 'BRIGHTCOVE_URL_TEMPLATE')

# Generated at 2022-06-14 17:06:07.346900
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.__class__.__name__ == 'TheStarIE'

# Generated at 2022-06-14 17:06:18.948422
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    #test for correct attributes for constructor of class TheStarIE
    test_obj = TheStarIE(None)
    assert test_obj._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:23.228532
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:06:27.356780
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ies = [TheStarIE()]
    for ie in ies:
        assert ie.ie_key() == 'TheStar'
        assert ie.ie_name() == 'TheStar'
        assert isinstance(ie.BRIGHTCOVE_URL_TEMPLATE, basestring)

# Generated at 2022-06-14 17:06:31.664020
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:35.182260
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:06:36.270287
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie != None

# Generated at 2022-06-14 17:06:38.835487
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:39.882312
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE({}, {})

# Generated at 2022-06-14 17:06:41.625817
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  ie = TheStarIE()
  ie.extract(TheStarIE._TEST['url'])

# Generated at 2022-06-14 17:06:49.914613
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # test with no url parameter
    inst =TheStarIE()
    # Assert that the url field is empty
    assert inst.BRIGHTCOVE_URL_TEMPLATE is None
    # test url parameter
    url='http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'
    inst = TheStarIE(url)
    # Assert url is correct
    assert inst.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    return

# Generated at 2022-06-14 17:06:51.341138
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	TheStarIE(None)


# Generated at 2022-06-14 17:06:53.827277
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    tsi = TheStarIE()
# Unit test to verify if an instance of TheStarIE can be properly created

# Generated at 2022-06-14 17:06:58.404017
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

    assert ie.brigthcove_url == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie.url_re == 'http://www.thestar.com/(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:02.634603
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert(TheStarIE._VALID_URL ==
        r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')


# Generated at 2022-06-14 17:07:09.798531
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Constructor of class TheStarIE
    ie = TheStarIE()
    # Assert url_result
    url_result = ie.url_result('players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001','BrightcoveNew','4732393888001')
    assert url_result.get('id') == '4732393888001'

# Generated at 2022-06-14 17:07:21.388635
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    IE = TheStarIE()
    assert IE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:28.177389
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_TheStari = TheStarIE()
    assert test_TheStari._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:32.573659
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:07:36.094321
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .common import TheStarIE
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:40.132046
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Unit test for constructor of TheStarIE
    
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:45.757507
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(TheStarIE.BRIGHTCOVE_URL_TEMPLATE % TheStarIE._TEST['info_dict']['id'])
    assert isinstance(ie, TheStarIE)

# Generated at 2022-06-14 17:07:51.881866
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    Test.assertEquals(
		ThestarIE('life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html').display_id,
		'mankind-why-this-woman-started-a-men-s-skincare-line'
		)

# Generated at 2022-06-14 17:08:04.316622
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert(ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')
    assert(ie._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert(ie._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554')

# Generated at 2022-06-14 17:08:11.841131
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # Unit test for Brightcove ID extraction
    assert(ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:08:12.750548
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # TheStarIE()
    pass

# Generated at 2022-06-14 17:08:24.317406
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    extractor = TheStarIE()
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert extractor._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert extractor._downloader is None
    assert extractor._WORKING is True # Py3

# Generated at 2022-06-14 17:08:34.181973
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:08:36.274159
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert(TheStarIE._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')

# Generated at 2022-06-14 17:08:40.904460
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:08:44.982604
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert obj != None

# Generated at 2022-06-14 17:08:49.652925
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', lambda x, y: None)
    return obj

# Generated at 2022-06-14 17:08:53.148619
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	ie = TheStarIE()
	assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:01.188851
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Initialize TheStarIE and set constuctor variables
    thestar_ie = TheStarIE()
    thestar_ie['_downloader'] = 'data'
    thestar_ie['_match_id'] = 'data2'
    thestar_ie['_search_regex'] = 'data3'
    thestar_ie['BRIGHTCOVE_URL_TEMPLATE'] = 'data4'

    # Test that download_webpage returns html
    webpage1 = thestar_ie._download_webpage('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', 'data')
    assert webpage1.find('<html') != -1
    # Test that download_webpage returns false

# Generated at 2022-06-14 17:09:08.108028
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    '''
    run python -m unittest -v test_TheStarIE
    '''
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:09:09.423934
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie != None

# Generated at 2022-06-14 17:09:13.435838
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()._download_webpage

# Generated at 2022-06-14 17:09:34.688656
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    tester = TheStarIE();
    assert tester.name() == "TheStar"
    assert tester.get_info(url="www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html") is not None

# Generated at 2022-06-14 17:09:38.132031
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test for constructor of class TheStarIE
    x = TheStarIE()
    assert x.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s', 'Did not initialize correctly'



# Generated at 2022-06-14 17:09:47.678521
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # test constructor with one url
    info_extractor = TheStarIE(TheStarIE.BRIGHTCOVE_URL_TEMPLATE)
    assert info_extractor.timestamp == None
    assert info_extractor.description == None
    assert info_extractor.formats == []
    assert info_extractor.urls == []
    assert info_extractor.brighcove_id == ""

    # test constructor with another url
    info_extractor = TheStarIE("http://www.thestar.com/entertainment/music/2014/04/12/drake_marries_exgirlfriend_at_beach_wedding_in_miami_moment_4_life.html")
    assert info_extractor.timestamp == None
    assert info_extractor.description == None
    assert info_ext

# Generated at 2022-06-14 17:09:48.606855
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:09:55.586141
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test constructor with simple url
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie = TheStarIE(url)
    assert ie.url == url
    # Test constructor with url that has subpage
    url = 'http://www.thestar.com/life/recipes/2016/02/01/chicken-and-rice-with-mushrooms-and-peas.html'
    ie = TheStarIE(url)
    assert ie.url == url


# Generated at 2022-06-14 17:10:03.933787
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId='
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:10:05.509518
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    assert t is not None

# Generated at 2022-06-14 17:10:14.267167
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert obj._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert obj._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert obj._TEST['info_dict']['id'] == '4732393888001'
    assert obj._TEST['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:10:15.278373
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert True


# Generated at 2022-06-14 17:10:16.027107
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	TheStarIE()

# Generated at 2022-06-14 17:10:53.141061
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:10:54.580984
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    return TheStarIE({})._test_extract({})

# Generated at 2022-06-14 17:10:58.295552
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Example of creating object with TheStarIE class
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:11:09.467036
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test TheStarIE"""

    # Make sure you call the class constructor with the correct paramaters

# Generated at 2022-06-14 17:11:14.529409
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie = TheStarIE(url)
    self.assertTrue(isinstance(ie, TheStarIE))

# Generated at 2022-06-14 17:11:24.410219
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie._VALID_URL == "https?://(?:www\\.)?thestar\\.com/(?:[^/]+/)*(?P<id>.+)\\.html"

# Generated at 2022-06-14 17:11:30.460211
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:32.226711
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    '''
    Invoke constructor to test the returns of class TheStarIE
    '''
    TheStarIE("https://www.thestar.com")

# Generated at 2022-06-14 17:11:39.866092
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:43.548972
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.url == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    #ie._real_extract("MyUnitTest")

# Generated at 2022-06-14 17:13:16.340752
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:13:19.445168
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE().extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    except:
        assert False, 'TheStarIE failed to initialize'


# Generated at 2022-06-14 17:13:23.817885
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Create a TheStarIE object
    TheStarIE_object = TheStarIE()
    assert TheStarIE_object != "null"

# Generated at 2022-06-14 17:13:26.883320
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html','4732393888001',False);

# Generated at 2022-06-14 17:13:31.644070
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie._match_id("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html") == "mankind-why-this-woman-started-a-men-s-skincare-line.html"

# Generated at 2022-06-14 17:13:32.306843
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:13:34.827860
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:13:43.478785
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Creating object of class TheStarIE
    ie = TheStarIE()
    # Asserting that URL is valid
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    # Asserting that URL is invalid

# Generated at 2022-06-14 17:13:44.199783
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info = TheStarIE()
    assert info.ie_key() == 'TheStar'

# Generated at 2022-06-14 17:13:45.314599
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	Test = TheStarIE()
	Test.test()

if __name__ == '__main__':
	test_TheStarIE()