

# Generated at 2022-06-14 17:06:04.985864
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print("testing TheStarIE")

    homepage = "http://www.thestar.com/"
    video_id = "4732393888001"
    embed_url = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId='
    expected_url = embed_url + video_id

    thestar = TheStarIE(homepage)

    assert(thestar._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')
    assert(thestar._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

    # Test find video

# Generated at 2022-06-14 17:06:08.436295
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert TheStarIE(InfoExtractor())._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:06:10.732270
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie


# Generated at 2022-06-14 17:06:20.867228
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert TheStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert TheStarIE._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert TheStarIE._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert TheStarIE._TEST

# Generated at 2022-06-14 17:06:22.248472
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    if __name__ == "__main__":
        TheStarIE()

# Generated at 2022-06-14 17:06:30.781745
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    obj = ie._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    print(obj)
    assert(obj['id'] == '4732393888001')
    assert(obj['ext'] == 'mp4')
    assert(obj['title'] == 'Mankind: Why this woman started a men\'s skin care line')
    assert(obj['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.')
    assert(obj['upload_date'] == '20160201')
    assert(obj['uploader_id'] == '794267642001')

# Generated at 2022-06-14 17:06:38.117063
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie.BRIGHTCOVE_URL_TEMPLATE != 'http://players.brightcove.net/794267642001/default_default/index.html?videoid=%s'


# Generated at 2022-06-14 17:06:38.836260
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE

# Generated at 2022-06-14 17:06:42.216756
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert(ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:06:46.584893
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie._download_webpage(ie._VALID_URL, ie._TEST['url'])
    ie._real_extract(ie._TEST['url'])
    ie._search_regex(ie._TEST['url'])

# Generated at 2022-06-14 17:06:51.343305
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert True

# Generated at 2022-06-14 17:07:02.447780
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    star_ie = TheStarIE()
    regex = (r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)')
    assert star_ie._search_regex(regex, "mainartBrightcoveVideoId123", "brightcove id") == "123"
    assert star_ie._search_regex(regex, "mainartBrightcoveVideoId : 123", "brightcove id") == "123"
    assert star_ie._search_regex(regex, "mainartBrightcoveVideoId:123", "brightcove id") == "123"
    assert star_ie._search_regex(regex, "mainartBrightcoveVideoId: '123'", "brightcove id") == "123"

# Generated at 2022-06-14 17:07:05.547238
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:16.598607
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie.__class__.__name__ == 'TheStarIE'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:17.581872
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('4732393888001')

# Generated at 2022-06-14 17:07:19.154324
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print(TheStarIE.__name__)
    t = TheStarIE()
    print(t)


# Generated at 2022-06-14 17:07:20.168245
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE(object())

# Generated at 2022-06-14 17:07:24.057589
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie_thestar = TheStarIE()
    ie_thestar._real_extract("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:07:25.028918
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    _ = TheStarIE()

# Generated at 2022-06-14 17:07:26.060682
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj

# Generated at 2022-06-14 17:07:40.580387
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert TheStarIE()._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:42.954721
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE is not None

# Generated at 2022-06-14 17:07:46.584841
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print("test_TheStarIE")
    TheStarIE('test_TheStarIE')
    print("test_TheStarIE end")

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:07:49.676876
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE._download_webpage = lambda _, __, ___: ''

    assert TheStarIE._download_webpage('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', '4732393888001') == ''

# Generated at 2022-06-14 17:07:54.614187
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    testurl = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    TheStarIE_instance = TheStarIE()
    _result = TheStarIE_instance.extract(testurl)
    assert _result['title'] == "Mankind: Why this woman started a men's skin care line"

# Generated at 2022-06-14 17:07:59.223395
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .brightcove_new import BrightcoveNewIE

    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert isinstance(ie, BrightcoveNewIE)
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:08.528531
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE()
    assert the_star_ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert the_star_ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:17.387349
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test for valid url of constructor for TheStarIE class
    t = TheStarIE()
    t._valid_url('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # Test for not valid url of constructor for TheStarIE class
    t = TheStarIE()
    t._valid_url('http://news.yahoo.com/video/queen-called-beijing-people-chinese-111205797.html')
    # Test for valid url of constructor for TheStarIE class
    t = TheStarIE()

# Generated at 2022-06-14 17:08:21.472755
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    s = TheStarIE()
    s2 = TheStarIE()
    assert(s.__dict__.keys() == s2.__dict__.keys())
    s3 = TheStarIE()
    assert(s3.__dict__.keys() == s.__dict__.keys())

# Generated at 2022-06-14 17:08:21.993919
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:08:33.422647
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com')
    assert ie.BRIGHTCOVE_URL_TEMPLATE=='http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:08:35.904985
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:08:36.665054
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie is not None

# Generated at 2022-06-14 17:08:37.133609
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    pass

# Generated at 2022-06-14 17:08:37.578976
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:08:43.604164
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:08:48.302649
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.(?P<ext>html)'


# Generated at 2022-06-14 17:08:57.938966
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    ie = TheStarIE()
    ie.extract(url)
    assert ie.format_id == "4732393888001"
    assert ie.display_id == "4732393888001"
    assert ie.urls == ["http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001"]
    assert ie.br_urls == ["http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001"]
    assert ie.id == "4732393888001"
    assert ie.url

# Generated at 2022-06-14 17:09:04.666656
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    theStarIE = TheStarIE()
    assert theStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert theStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:07.937844
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"

# Generated at 2022-06-14 17:09:25.494531
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    test_obj = TheStarIE()
    result = test_obj.suitable(test_url)
    assert result == True, "suitable() failed with url: " + test_url

# Generated at 2022-06-14 17:09:32.657518
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:33.247197
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:09:37.190251
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/')

# Generated at 2022-06-14 17:09:43.967802
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_instance = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert test_instance._VALID_URL == test_instance._VALID_URL

# Generated at 2022-06-14 17:09:51.558250
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    # Test brightcove video
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:09:54.806071
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  ie = TheStarIE('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

  if (ie is None):
    assert False, "Error: ie is None"

# Generated at 2022-06-14 17:09:57.937482
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    parser_test = TheStarIE()
    url_test = parser_test._VALID_URL
    parser_test._real_extract(url_test)

# Generated at 2022-06-14 17:10:02.728718
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  ie = TheStarIE()
  assert ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
  assert ie.title == 'Mankind: Why this woman started a men\'s skin care line'

# Generated at 2022-06-14 17:10:06.310612
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    inst_TheStarIE = TheStarIE()
    assert inst_TheStarIE is not None


# Generated at 2022-06-14 17:10:37.715506
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:10:41.701265
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	test_obj = TheStarIE()
	test_obj.test()

test_TheStarIE()

# Generated at 2022-06-14 17:10:51.054768
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:10:52.103047
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    constructor = TheStarIE()
    assert constructor

# Generated at 2022-06-14 17:10:52.942017
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:10:53.607719
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:01.955454
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    result = TheStarIE()
    assert result.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert result._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert result._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert result._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:11:04.255140
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('https://www.thestar.com/')
    ie


# Generated at 2022-06-14 17:11:04.893887
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:08.090656
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:12:33.556860
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(None, None)
    assert ie != None

# Generated at 2022-06-14 17:12:44.923806
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test constructor of class TheStarIE"""
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:12:47.076924
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(InfoExtractor)._VALID_URL == TheStarIE._VALID_URL

# Generated at 2022-06-14 17:12:49.353005
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:13:00.034815
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    _TheStarIE = TheStarIE()
    assert isinstance(_TheStarIE, TheStarIE)
    assert hasattr(_TheStarIE, "_downloader")
    assert _TheStarIE._downloader is not None
    assert hasattr(_TheStarIE, "_download_webpage")
    assert _TheStarIE._download_webpage is not None
    assert hasattr(_TheStarIE, "_match_id")
    assert _TheStarIE._match_id is not None
    assert hasattr(_TheStarIE, "_search_regex")
    assert _TheStarIE._search_regex is not None
    assert hasattr(_TheStarIE, "BRIGHTCOVE_URL_TEMPLATE")
    assert _TheStarIE.BRIGHTCOVE_URL_TEMPLATE is not None

# Generated at 2022-06-14 17:13:05.321260
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	theStarIE = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
	print(theStarIE)

# Generated at 2022-06-14 17:13:05.924786
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()

# Generated at 2022-06-14 17:13:06.654785
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:13:07.649180
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:13:15.312565
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar = TheStarIE()
    thestar.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    thestar._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    thestar._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    return thestar