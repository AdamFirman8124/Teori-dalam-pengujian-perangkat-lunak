

# Generated at 2022-06-14 17:06:04.674504
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    ie.display_id = ie._match_id(ie.url)
    ie.webpage = ie._download_webpage(url, display_id)
    ie.brightcove_id = ie._search_regex(
        r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',
        webpage, 'brightcove id')
    ie.url_result = ie.url_result(ie.BRIGHTCOVE_URL_TEMPLATE % ie.brightcove_id, 'BrightcoveNew', brightcove_id)

# Generated at 2022-06-14 17:06:05.293320
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:06.739118
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    Unit test for TheStarIE()
    """
    TheStarIE()

# Generated at 2022-06-14 17:06:07.818607
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    x = TheStarIE()



# Generated at 2022-06-14 17:06:19.288959
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:19.786945
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:20.295219
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:21.443967
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    i = TheStarIE()
    assert i.institution_name == 'TheStarIE'

# Generated at 2022-06-14 17:06:22.512744
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.url_result(ie.BRIGHTCOVE_URL_TEMPLATE % 'foo', 'BrightcoveNew', 'foo')

# Generated at 2022-06-14 17:06:26.135595
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('TheStarIE')
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    return ie

# Generated at 2022-06-14 17:06:30.967387
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE() != None

# Generated at 2022-06-14 17:06:34.056028
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE('https://www.thestar.com/news/gta/2015/10/16/scarborough-man-58-shot-to-death-in-backyard.html')
    except:
        raise AssertionError('TheStarIE constructor test failed!')

# Generated at 2022-06-14 17:06:46.545773
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:48.986180
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test initialization of class TheStarIE"""
    assert TheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:06:50.013720
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:56.836121
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE('', {}, False)
    assert t.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert t.BRIGHTCOVE_URL_TEMPLATE == TheStarIE._TEST['info_dict']['player_url']

# Generated at 2022-06-14 17:07:00.684910
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie = TheStarIE()
    assert ie.match(url) == True


# Generated at 2022-06-14 17:07:09.003733
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:12.312646
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:18.940426
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:31.105902
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert str(ie.BRIGHTCOVE_URL_TEMPLATE) == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:34.795596
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info = TheStarIE()._parse_ie_properties()
    assert info['extractor'] == 'TheStar'
    assert info['name'] == 'thestar'
    assert info['description'] == 'Unit test for extractor for thestar.com'

# Generated at 2022-06-14 17:07:40.012582
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(InfoExtractor(), 'TheStarIE', True)
    assert ie.name == 'TheStarIE'
    assert ie.ie_key == 'TheStar' 
    assert ie.working == True
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:42.266635
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:07:46.548346
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:47.299459
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()



# Generated at 2022-06-14 17:07:49.277952
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('www.thestar.com', {}, None)
    assert isinstance(ie, TheStarIE)

# Generated at 2022-06-14 17:07:49.894440
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:07:54.734335
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test constructor of TheStarIE"""
    ie = TheStarIE()
    print(ie)
    print(ie._VALID_URL)
    print(ie._TEST)
    print(ie._TEST['url'])
    print(ie._TEST['info_dict'])
    print(ie.BRIGHTCOVE_URL_TEMPLATE)

# Unit test extraction of class TheStarIE

# Generated at 2022-06-14 17:08:01.791405
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	info_extractor = TheStarIE()
	assert info_extractor._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
	assert info_extractor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
	assert info_extractor._downloader == None
	assert info_extractor._download_webpage == None
	assert info_extractor._match_id == None
	assert info_extractor._search_regex == None
	assert info_extractor.url_result == None

test_TheStarIE()


# Generated at 2022-06-14 17:08:26.226587
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    IE = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert IE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert IE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert IE._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert IE._

# Generated at 2022-06-14 17:08:36.238181
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:08:42.599610
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL == r'^https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html$'
    assert TheStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:08:44.516018
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	temp = TheStarIE()

# Generated at 2022-06-14 17:08:45.556896
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj is not None

# Generated at 2022-06-14 17:08:51.075128
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    il = TheStarIE()
    brightcove_id = '4732393888001'
    brightcove_url = il.BRIGHTCOVE_URL_TEMPLATE % brightcove_id
    assert il._real_extract(brightcove_url)['id'] == brightcove_id

# Generated at 2022-06-14 17:08:53.762988
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	info_extractor = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
	return info_extractor

# Generated at 2022-06-14 17:08:54.778801
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE(None)

# Generated at 2022-06-14 17:09:00.487166
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:01.272178
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:09:18.458413
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert TheStarIE._VALID_URL is not None
    assert TheStarIE._TEST is not None

# Generated at 2022-06-14 17:09:22.251029
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    BrightcoveNew(TheStarIE().BRIGHTCOVE_URL_TEMPLATE % '4732393888001')

# Generated at 2022-06-14 17:09:32.804507
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:09:40.257391
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    # valid url
    # url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    # assert (TheStarIE._VALID_URL.match(url) != None)

    # invalid url
    # url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line'
    # assert (TheStarIE._VALID_URL.match(url) == None)

    # test thestar_ie
    thestar_ie = TheStarIE()

# Generated at 2022-06-14 17:09:51.727550
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/entertainment/celebrity/2015/07/23/sandra-bullock-offers-to-surrogate-for-ryan-reynolds-and-blake-lively.html')

# Generated at 2022-06-14 17:09:58.042035
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	# test for url http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html
	theStarIE = TheStarIE(TheStarIE._VALID_URL)
	theStarIE.BRIGHTCOVE_URL_TEMPLATE = "http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001"

# Generated at 2022-06-14 17:10:01.521580
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    info_dict = ie._download_webpage(
        'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html',
            '4732393888001')
    assert info_dict['id'] == '4732393888001'

# Generated at 2022-06-14 17:10:07.427258
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE()
    the_star_ie.BRIGHTCOVE_URL_TEMPLATE % '4732393888001'
    # 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'

# Generated at 2022-06-14 17:10:08.473060
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()



# Generated at 2022-06-14 17:10:15.801644
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    #test 1
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    brightcove_id = ie._search_regex(r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',
            ie._download_webpage(url, 'test'), 'brightcove id')

# Generated at 2022-06-14 17:11:00.207008
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test that the constructor works without error
    ie = TheStarIE()
    # Test that build_url does not raise an exception
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie.BRIGHTCOVE_URL_TEMPLATE = ie._search_regex('(.+)', 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s', 'brightcove_url_template')

# Generated at 2022-06-14 17:11:03.873914
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:11:04.501942
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    return TheStarIE

# Generated at 2022-06-14 17:11:12.603982
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://video.thestar.com/')
    assert ie is not None
    assert ie.params['cookie'] == 'market=toronto; lang=en'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
#
# # Unit test for _real_extract function
# def test_TheStarIE_real_extract():
#     ie = TheStarIE('http://video.thestar.com/')
#     ie._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:11:14.980491
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE({})
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:11:19.468221
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    obj._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:11:21.557423
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:11:23.592046
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj._VALID_URL == TheStarIE._VALID_URL
    assert obj._TEST['url'] == TheStarIE._TEST['url']

# Generated at 2022-06-14 17:11:24.210228
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:33.512756
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:13:07.086630
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:13:12.017474
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie_ = TheStarIE()
    assert ie_.SUFFIX == 'thestar.com'
    assert ie_.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:19.444008
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie != None
    assert ie.SUITABLE_VIDEO_FORMATS == ['application/x-mpegURL']
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:29.651914
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:31.666112
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:13:35.593642
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:13:42.637203
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE({'url': 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'})
    assert(ie.BRIGHTCOVE_URL_TEMPLATE) == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:51.332703
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:53.429077
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:56.655981
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'