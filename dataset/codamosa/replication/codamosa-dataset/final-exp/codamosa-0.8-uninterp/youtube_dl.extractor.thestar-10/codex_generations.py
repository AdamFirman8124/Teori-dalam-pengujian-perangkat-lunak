

# Generated at 2022-06-14 17:06:04.169951
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert True == TheStarIE.suitable("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert True == TheStarIE.suitable("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert True == TheStarIE.suitable("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:06:06.228657
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info_extractor = InfoExtractor()
    assert isinstance(info_extractor, InfoExtractor)

# Generated at 2022-06-14 17:06:15.255935
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # construct object with good link
    thestar = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # retrieve video id
    videoId = thestar._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html').videoId
    assert videoId == '4732393888001'



# Generated at 2022-06-14 17:06:18.299687
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """TheStarIE constructor needs to be tested."""
    brightcove_id = '4732393888001'
    StarIE(brightcove_id)

# Generated at 2022-06-14 17:06:19.096139
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:06:19.899236
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert TheStarIE


# Generated at 2022-06-14 17:06:20.906186
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:06:21.590645
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    theStarIE = TheStarIE()

# Generated at 2022-06-14 17:06:22.868588
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    Unit test for constructor of class TheStarIE
    """

    ie = TheStarIE()
    ie.extract(TheStarIE._TEST['url'])

# Generated at 2022-06-14 17:06:26.397667
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:29.775378
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	"""
	Test TheStarIE constructor
	"""
	
	ie = TheStarIE()



# Generated at 2022-06-14 17:06:31.339985
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Setup
    TheStarIE()
    # Teardown

# Generated at 2022-06-14 17:06:33.332304
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(u'www.thestar.com') == TheStarIE(u'www.thestar.com')

# Generated at 2022-06-14 17:06:33.782891
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:34.570001
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:46.929218
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert thestar.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert thestar._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:48.130484
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:06:57.053317
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    Description:
        Tests to make sure that the TheStarIE module is functioning as
        intended by using the _call_brightcove_API method from the InfoExtractor
        class.

    Output:
        True if the function is working as intended
    """
    ie = TheStarIE(TheStarIE._downloader) # Create instance of module
    ie._call_brightcove_API({'partnerId': 794267642001, 'videoId': 4732393888001}) # Run method
    return True # Method ran without errors


# Generated at 2022-06-14 17:07:06.433268
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    constructor_args = {
        'video_id': '4732393888001',
        '_type': 'BrightcoveNew',
        '_video_id': '4732393888001',
        'url': 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001',
        'ext': 'mp4',
        'title': 'Mankind: Why this woman started a men\'s skin care line',
        '_downloader': None,
        '_parse_html5_media_entries': True
    }
    ie = TheStarIE(**constructor_args)
    assert ie.ie_key() == 'TheStar'
    assert ie.video_id == '4732393888001'

# Generated at 2022-06-14 17:07:11.700875
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert(ie is not None)


# Generated at 2022-06-14 17:07:19.321712
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extract('http://www.thestar.com/news/canada/2016/01/26/university-of-montreal-prof-joins-fight-for-freedom-of-expression.html')

# Generated at 2022-06-14 17:07:21.910876
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # This test only checks if the code doesn't crash and that the
    # InfoExtractor is created without problems
    TheStarIE()

# Generated at 2022-06-14 17:07:25.236889
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    print (ie)

# Generated at 2022-06-14 17:07:26.588975
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(None)
    assert ie.brighcove_id is None

# Generated at 2022-06-14 17:07:32.137470
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	TheStarIE.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
	TheStarIE.BRIGHTCOVE_URL_TEMPLATE


# Generated at 2022-06-14 17:07:33.228451
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar_ie = TheStarIE()

# Generated at 2022-06-14 17:07:42.675233
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
	ie = TheStarIE()
	info = ie.extract(url)
	assert(info['id'] == '4732393888001')
	assert(info['ext'] == 'mp4')
	assert(info['title'] == 'Mankind: Why this woman started a men\'s skin care line')
	assert(info['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.')
	assert(info['uploader_id'] == '794267642001')
	assert(info['timestamp'] == 1454353482)
	assert(info['upload_date'] == '20160201')

# Generated at 2022-06-14 17:07:52.126931
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_cases = {
        'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html':
            '4732393888001',
        'http://www.thestar.com/business/personal_finance/2016/03/03/rrsp-reminder-contribute-by-monday.html':
            '4740977455001'
    }

    for url, expected_id in test_cases.items():
        url_obj = TheStarIE._build_url_result(url, TheStarIE.ie_key())
        brightcove_id = TheStarIE._match_id(url_obj.url)
        actual_url = TheStarIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:07:53.241893
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE() == TheStarIE

# Generated at 2022-06-14 17:07:59.028730
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    Unit test code for TheStarIE
    """
    ie = InfoExtractor(TheStarIE.BRIGHTCOVE_URL_TEMPLATE % '4732393888001')
    assert ie.SUCCESS == ie.extract()


# Generated at 2022-06-14 17:08:12.600463
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test object instantiation
    t = TheStarIE()
    # Test instance of InfoExtractor
    assert( isinstance(t, InfoExtractor) )
    # Test if URL matches expected pattern
    assert( t._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html' )

# Generated at 2022-06-14 17:08:24.047621
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE(True)
    assert the_star_ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:08:26.341572
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_TheStarIE = TheStarIE(1 ,2)
    test_TheStarIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:08:36.312596
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # To test TheStarIE class in isolation (requires a mock class)
    import mock
    from .common import url_basename
    from .brightcove import BrightcoveNewIE

    mock_brightcove_result = mock.Mock()
    mock_brightcove_result.id = '4732393888001'
    mock_brightcove_result.title = 'Mankind: Why this woman started a men\'s skin care line'
    mock_brightcove_result.ie = BrightcoveNewIE
    mock_brightcove_result.url_basename = url_basename

    TheStarIE_instance = TheStarIE()
    TheStarIE_instance.url_result = mock.Mock()
    TheStarIE_instance._search_regex = mock.Mock(return_value='4732393888001')


# Generated at 2022-06-14 17:08:45.798522
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie
    assert ie.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"
    assert ie._TEST['url'] == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    assert ie._TEST['md5'] == "2c62dd4db2027e35579fefb97a8b6554"
    assert ie._TEST['info_dict']['id'] == "4732393888001"
    assert ie._TEST['info_dict']['ext'] == "mp4"
    assert ie._TEST

# Generated at 2022-06-14 17:08:56.880099
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:08:59.470397
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Create an object of TheStarIE
    thestar_ie = TheStarIE()
    thestar_ie.test_cases()

# Generated at 2022-06-14 17:09:03.172748
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:09:07.667805
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_class = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:09:16.776519
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    youtube_dash_manifest = {
        "url": "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html",
        "params": {
        },
        "info_dict": {
            "id": "4732393888001",
            "ext": "mp4",
            "title": "Mankind: Why this woman started a men's skin care line",
            "description": "Robert Cribb talks to Young Lee, the founder of Uncle Peter's MAN.",
            "uploader_id": "794267642001",
            "timestamp": 1454353482,
            "upload_date": "20160201",
        },
    }

# Generated at 2022-06-14 17:09:35.994636
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    global test_TheStarIE
    test_TheStarIE = TheStarIE()


# Generated at 2022-06-14 17:09:37.486858
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestarIE=TheStarIE()
    thestarIE._search_regex
#test_TheStarIE()

# Generated at 2022-06-14 17:09:47.678864
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    inst = TheStarIE()
    assert inst._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:53.428425
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test TheStarIE constructor."""
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    obj = TheStarIE()
    result = obj._match_id(url)

    assert result == 'mankind-why-this-woman-started-a-men-s-skincare-line'

# Generated at 2022-06-14 17:09:56.029658
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()


# Generated at 2022-06-14 17:09:59.956909
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:10:05.409061
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert instance.name() == 'thestar:default'

# Generated at 2022-06-14 17:10:10.225306
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.md5 == '2c62dd4db2027e35579fefb97a8b6554'


# Generated at 2022-06-14 17:10:12.954279
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert(ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:10:13.904720
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert isinstance(ie, TheStarIE)

# Generated at 2022-06-14 17:11:00.710950
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    pre_check = r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)'
    check_url = r'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'
    assert ie._TEST['url'] == url
    assert ie._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert ie._TEST['info_dict']['id'] == '4732393888001'

# Generated at 2022-06-14 17:11:01.719220
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    i = TheStarIE()

# Generated at 2022-06-14 17:11:05.229710
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:11:10.708404
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
	info = TheStarIE().extract(url)
	assert info['id'] == '4732393888001'

# Generated at 2022-06-14 17:11:18.615882
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:11:20.156258
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:11:23.136883
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:34.389959
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:35.176873
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert issubclass(TheStarIE, InfoExtractor)

# Generated at 2022-06-14 17:11:36.262972
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        return TheStarIE()
    except Exception:
        return False

# Generated at 2022-06-14 17:13:18.062629
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:13:19.188459
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE()
    assert the_star_ie is not None

# Generated at 2022-06-14 17:13:25.175269
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        info_extract = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
        return True
    except:
        return False


# Generated at 2022-06-14 17:13:27.768039
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie=TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:13:28.618159
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE != InfoExtractor

# Generated at 2022-06-14 17:13:39.883742
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('test', "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie.IE_NAME == 'TheStar'



# Generated at 2022-06-14 17:13:43.371942
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', {}, {}, {'skip_download': True})

# Generated at 2022-06-14 17:13:44.522747
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(None)

# Generated at 2022-06-14 17:13:47.615494
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert obj.BRIGHT

# Generated at 2022-06-14 17:13:58.475319
# Unit test for constructor of class TheStarIE