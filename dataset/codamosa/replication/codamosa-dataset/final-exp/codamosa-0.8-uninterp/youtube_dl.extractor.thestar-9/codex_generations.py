

# Generated at 2022-06-14 17:06:00.698192
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert "TheStarIE" == ie.IE_NAME
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._BRIGHTCOVE_URL_TEMPLATE == ie.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:06:13.592254
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:15.643411
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	ic = TheStarIE()
	assert ic._VALID_URL is not None

# Generated at 2022-06-14 17:06:16.873433
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    print(ie)



# Generated at 2022-06-14 17:06:28.390755
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie._VALID_URL = r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:31.653960
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:06:35.182097
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:43.281712
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print("Unit test of class TheStarIE")
    # test a normal video link
    tester = TheStarIE()
    test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    extractor = tester._download_webpage(test_url, '4732393888001')
    assert extractor == True
    print("Pass the test.\n")

# Generated at 2022-06-14 17:06:45.556484
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:48.798809
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test"""
    assert TheStarIE(InfoExtractor())._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:56.671587
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .test_brightcove import test_BrightcoveIE
    assert issubclass(TheStarIE, InfoExtractor)
    assert issubclass(TheStarIE, test_BrightcoveIE)

# Generated at 2022-06-14 17:06:57.207953
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:07:03.203666
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_TheStarIE = TheStarIE()
    assert test_TheStarIE._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert test_TheStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:07:04.111634
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    #TODO: Add unit test
    assert True

# Generated at 2022-06-14 17:07:05.007682
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie is not None

# Generated at 2022-06-14 17:07:13.992487
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	obj = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', '')
	assert obj._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') == 'mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:07:15.783357
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert True

# Generated at 2022-06-14 17:07:23.337182
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	"""
	Unit test for constructor of class TheStarIE
	"""
	thestarie = TheStarIE()
	assert thestarie.IE_NAME == 'thestar'
	assert thestarie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
	assert thestarie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:24.299245
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:07:30.859813
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    print()

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:07:38.538790
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:46.074154
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    class_ = TheStarIE
    # Constructor test
    the_star_ie = class_("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert the_star_ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:48.537552
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert isinstance(ie, TheStarIE)

# Generated at 2022-06-14 17:07:53.921248
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    i = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert i._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:08:01.148211
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:04.475969
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("https://www.youtube.com/watch?v=2KmG1lDxctA")
    assert ie.url == "https://www.youtube.com/watch?v=2KmG1lDxctA"

# Generated at 2022-06-14 17:08:05.499374
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert TheStarIE()


# Generated at 2022-06-14 17:08:07.805781
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:08:16.914111
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    tester = TheStarIE()
    #    TheStarIE._TEST = {
    #         'url': 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html',
    #         'md5': '2c62dd4db2027e35579fefb97a8b6554',
    #         'info_dict': {
    #             'id': '4732393888001',
    #             'ext': 'mp4',
    #             'title': 'Mankind: Why this woman started a men\'s skin care line',
    #             'description': 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.',
    #             'uploader_id': '79426764

# Generated at 2022-06-14 17:08:20.559911
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:30.912811
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()._VALID_URL == TheStarIE._VALID_URL

# Generated at 2022-06-14 17:08:37.164301
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    c = TheStarIE()
    c._match_id = lambda x: 'x'
    c._search_regex = lambda x,y,z: '4732393888001'
    c._download_webpage = lambda x,y: '<div></div>'

    # Testing the constructor of TheStarIE
    assert isinstance(c, InfoExtractor)
    assert c.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:37.772439
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:08:41.200368
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("")
    assert ie.__class__.__name__ == "TheStarIE"
    

# Generated at 2022-06-14 17:08:45.651604
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    parser_obj = TheStarIE()
    assert parser_obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:08:56.783398
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_TheStarIE = TheStarIE()
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    display_id = 'mankind-why-this-woman-started-a-men-s-skincare-line'
    webpage = test_TheStarIE._download_webpage(url, display_id)
    brightcove_id = test_TheStarIE._search_regex(r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',
            webpage, 'brightcove id')

# Generated at 2022-06-14 17:08:57.444807
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:09:00.004917
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE()
    assert the_star_ie != None
    #print(the_star_ie)


# Generated at 2022-06-14 17:09:04.903727
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(test_TheStarIE.test, extractor_options=None)
    obj = object()
    test_TheStarIE.test = obj
    assert ie.test == obj

test_TheStarIE.test = "Vddvdsv"
test_TheStarIE()

# Generated at 2022-06-14 17:09:12.204554
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    result = TheStarIE()._real_extract("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert result['id'] == '4732393888001'
    assert result['title'] == 'Mankind: Why this woman started a men\'s skin care line'
    assert result['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.'
    assert result['uploader_id'] == '794267642001'
    assert result['timestamp'] == 1454353482
    assert result['upload_date'] == '20160201'
    assert result['uploader'] == 'TheStarTV'

# Generated at 2022-06-14 17:09:30.802746
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    pass

# Generated at 2022-06-14 17:09:37.489082
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    IE = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert IE.BRIGHTCOVE_URL_TEMPLATE != None
    assert IE._VALID_URL != None
    assert IE._TEST != None
    assert IE._TEST['url'] != None
    assert IE._TEST['md5'] != None
    assert IE._TEST['info_dict'] != None

# Generated at 2022-06-14 17:09:38.433123
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE()
    assert isinstance(instance, TheStarIE)

# Generated at 2022-06-14 17:09:40.883750
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:09:41.814815
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()


# Generated at 2022-06-14 17:09:44.413168
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE().BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:54.983809
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:59.904655
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    inst = TheStarIE()
    the_star_ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
print(inst)

# Generated at 2022-06-14 17:10:11.553179
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE()
    assert instance._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:10:23.498837
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    display_id = 'mankind-why-this-woman-started-a-men-s-skincare-line'
    brightcove_id = '4732393888001'
    brightcove_url = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s' % brightcove_id

    result = TheStarIE()._real_extract(url)
    assert result.get('id') == brightcove_id
    assert result.get('url') == TheStarIE.BRIGHTCOVE_URL_TEMPLATE % brightcove_id


# Generated at 2022-06-14 17:11:03.993868
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    IE = TheStarIE()
    assert IE.__name__ == 'thestar'


# Generated at 2022-06-14 17:11:07.697398
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	thestar = TheStarIE()
	assert thestar._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

if __name__ == '__main__':
	test_TheStarIE()

# Generated at 2022-06-14 17:11:19.648270
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    webpage = ie._download_webpage(ie._TEST['url'], ie._TEST['info_dict']['id'])
    brightcove_id = ie._search_regex(r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',
            webpage, 'brightcove id')
    url = ie.BRIGHTCOVE_URL_TEMPLATE % brightcove_id
    info = ie.url_result(url, 'BrightcoveNew', brightcove_id)
    assert ie._is_valid_url(ie.BRIGHTCOVE_URL_TEMPLATE % 4732393888001, info)

# Generated at 2022-06-14 17:11:27.025777
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # test constructor
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    # test url
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie._real_extract(url)['_type'] == 'BrightcoveNew'

# Generated at 2022-06-14 17:11:35.364178
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:11:37.695458
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    TheStarIE(url)

# Generated at 2022-06-14 17:11:40.767736
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test the constructor for the class TheStarIE"""
    ie = TheStarIE()
    assert isinstance(ie, TheStarIE)

# Generated at 2022-06-14 17:11:41.283918
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:43.395890
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    url = ie.BRIGHTCOVE_URL_TEMPLATE % 4732393888001
    return ie.url_result(url)

# Generated at 2022-06-14 17:11:54.850053
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	"""Set up and run a unit test for TheStarIE.

	Args:
		None

	Returns:
		None

	Raises:
		AssertionError, if the unit test fails
	"""
	url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:13:38.280498
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:41.558085
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(None)
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None

# Generated at 2022-06-14 17:13:48.152691
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Unit test with a link to a video of class TheStarIE
    TheStarIE_test = TheStarIE(TheStarIE._TEST)
    assert TheStarIE_test._TEST['url'] == TheStarIE_test.url
    assert TheStarIE_test._TEST['md5'] == TheStarIE_test.md5
    assert TheStarIE_test._TEST['info_dict'] == TheStarIE_test.info_dict
    assert TheStarIE_test._TEST['params'] == TheStarIE_test.params

# Generated at 2022-06-14 17:13:58.499421
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for testing constructor of class TheStarIE"""

    # Construct an object of TheStarIE
    the_Star_IE = TheStarIE()

    # Get expected value from TEST object
    expected_URL = the_Star_IE._TEST['url']
    expected_ID = the_Star_IE._TEST['info_dict']['id']

    
    # Get actual value from TheStarIE.extract_brightcove_url(URL)
    actual_URL = the_Star_IE.extract_brightcove_url(expected_URL)

    # Get ID later on used for testing from actual_URL
    actual_ID_using_url = actual_URL.split("=")[1]
       
    # Get actual value from TheStarIE.extract_brightcove_id(URL)
    actual_ID = the_

# Generated at 2022-06-14 17:14:07.295372
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info_dict = {'id': '4732393888001',
                 'ext': 'mp4',
                 'title': 'Mankind: Why this woman started a men\'s skin care line',
                 'description': 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.',
                 'uploader_id': '794267642001',
                 'timestamp': 1454353482,
                 'upload_date': '20160201',
                 '_type': 'url_transparent',
                 'url': 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001',
                 'ie_key': 'BrightcoveNew',
                 'ie': 'BrightcoveNew',
                 'real_id': '4732393888001'}


# Generated at 2022-06-14 17:14:12.295788
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId='
    t = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert t._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:14:14.851314
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    extractor = TheStarIE()
    assert extractor._extract_brightcove_url == TheStarIE._extract_brightcove_url


# Generated at 2022-06-14 17:14:16.405977
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:14:18.382477
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert isinstance(obj, InfoExtractor)

# Generated at 2022-06-14 17:14:27.077251
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.initBaseIE()
    ie.initExtractor()
    ie.extract(test_TheStarIE.TEST['url'])
    assert ie.display_id == test_TheStarIE.TEST['info_dict']['id']
    assert ie.ie_key() == 'BrightcoveNew:' + test_TheStarIE.TEST['info_dict']['id']
    assert ie.title == test_TheStarIE.TEST['info_dict']['title']

if __name__ == '__main__':
    test_TheStarIE()