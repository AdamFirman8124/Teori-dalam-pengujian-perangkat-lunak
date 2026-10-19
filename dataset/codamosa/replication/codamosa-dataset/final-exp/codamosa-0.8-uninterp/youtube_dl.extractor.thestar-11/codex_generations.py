

# Generated at 2022-06-14 17:05:54.301549
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	return TheStarIE()

# Generated at 2022-06-14 17:05:55.481183
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    # Test for class inheritance
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:06:03.968940
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for the constructor of class TheStarIE"""
    print("Testing the constructor of class TheStarIE")
    # Testing without an URL
    test_object = TheStarIE()
    assert test_object.ie_key() == 'thestar'
    assert test_object.ie_url() == 'http://www.thestar.com'
    assert test_object._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:07.655400
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:06:10.340473
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .brightcove import BrightcoveNewIE
    b = BrightcoveNewIE
    assert b

# Generated at 2022-06-14 17:06:20.562255
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    title = 'Mankind: Why this woman started a men\'s skin care line'
    description = 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.'
    timestamp = 1454353482
    display_id = '4732393888001'
    brightcove_id = '4733472473001'
    uploader_id = '794267642001'
    upload_date = '20160201'
    
    valid_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    thestar = TheStarIE(TheStarIE.BRIGHTCOVE_URL_TEMPLATE % brightcove_id, TheStarIE._TEST)

    assert thestar

# Generated at 2022-06-14 17:06:23.048725
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(None)
    ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:28.732902
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar = TheStarIE({})
    assert thestar.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert thestar._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:37.117007
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    myclass = TheStarIE()
    myclass._downloader.cache.store('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html',
                                    b'<script>mainartBrightcoveVideoId: "4732393888001"</script>')
    print(myclass._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'))
    assert 0


# Generated at 2022-06-14 17:06:39.882651
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()
    TheStarIE()
    TheStarIE()
    TheStarIE()
    # to check that there were no errors when creating these instances
    assert True

# Generated at 2022-06-14 17:06:46.332556
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie is not None

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:06:56.637781
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie_obj = TheStarIE()
    obj_str = str(ie_obj)
    assert obj_str.startswith('<TheStar')
    assert ie_obj.ie_key().startswith('TheStar')
    assert ie_obj.ie_key() == 'TheStar'
    assert ie_obj.AVAILABLE_FORMATS == ['hls', 'http_dash_segments']
    assert ie_obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie_obj._VALID_URL == 'https?://(?:www\\.)?thestar\\.com/(?:[^/]+/)*(?P<id>.+)\\.html'
    assert ie_obj

# Generated at 2022-06-14 17:07:03.811244
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert obj._VALID_URL == 'https?://(?:www\\.)?thestar\\.com/(?:[^/]+/)*(?P<id>.+)\\.html'

# Generated at 2022-06-14 17:07:06.659302
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:07:12.859868
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:15.839994
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE()
    except:
        assert False


# Generated at 2022-06-14 17:07:25.885320
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = r'https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    # should raise an Exception if it cannot find the required attributes
    instance = TheStarIE(TheStarIE._create_get_url_instance(url))
    assert instance.url == url
    assert instance._VALID_URL == TheStarIE._VALID_URL
    assert instance._TEST == TheStarIE._TEST
    assert instance.BRIGHTCOVE_URL_TEMPLATE == TheStarIE.BRIGHTCOVE_URL_TEMPLATE
    # should not raise an exception if it can find the required attributes
    TheStarIE(TheStarIE._create_get_url_instance(url))

# Generated at 2022-06-14 17:07:33.699129
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_file = open("test.txt","w")
    ie = TheStarIE()
    ie._downloader.params.update({'verbose': True})
    #ie._downloader.params.update({'verbose': True, 'dump_intermediate_pages': True})
    ie._print_debug = test_file.write
    ie._real_extract(ie._TEST['url'])
    test_file.close()

# Unit test of class TheStarIE

# Generated at 2022-06-14 17:07:39.429184
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	# thestar_ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
	thestar_ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:07:40.303443
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    x = TheStarIE()
    assert True

# Generated at 2022-06-14 17:07:52.397215
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	info = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
	assert info.id == '4732393888001'
	assert info.title == 'Mankind: Why this woman started a men\'s skin care line'

# Generated at 2022-06-14 17:07:53.029740
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:08:01.450960
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie = TheStarIE()
    ie.extract(url)
    assert(ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:08:09.816656
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  ie = TheStarIE()
  ie.url = 'https://www.thestar.com/news/canada/2016/02/02/toronto-police-name-man-accused-of-valentines-day-murder-suicide-in-don-mills.html'
  assert ie.url == 'https://www.thestar.com/news/canada/2016/02/02/toronto-police-name-man-accused-of-valentines-day-murder-suicide-in-don-mills.html'
  assert ie.display_id == 'toronto-police-name-man-accused-of-valentines-day-murder-suicide-in-don-mills'

# Generated at 2022-06-14 17:08:11.393565
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        ietester = TheStarIE()
        print ('Failed to raise an exception!')
        assert (False)
    except:
        assert (True)

# Generated at 2022-06-14 17:08:12.787281
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL



# Generated at 2022-06-14 17:08:24.318126
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Please do not use IE as a class variable in future
    ie = TheStarIE()
    video = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    the_star_ie = ie._real_extract(video)

    assert the_star_ie['id'] == '4732393888001'
    assert the_star_ie['ext'] == 'mp4'
    assert the_star_ie['title'] == "Mankind: Why this woman started a men's skin care line"
    assert the_star_ie['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.'
    assert the_star_ie['uploader_id'] == '794267642001'

# Generated at 2022-06-14 17:08:24.967170
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	return TheStarIE()

# Generated at 2022-06-14 17:08:26.051957
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()



# Generated at 2022-06-14 17:08:36.087965
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    a = TheStarIE('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # Do some assertions for the class
    assert a.display_id == 'mankind-why-this-woman-started-a-men-s-skincare-line'
    assert a.url == 'https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert a.true_url == 'https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert a.ext

# Generated at 2022-06-14 17:08:48.613168
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	"""
	TheStarIE unit test stub
	"""
	t = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
	assert t

# Generated at 2022-06-14 17:08:52.137117
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert unicode(ie.BRIGHTCOVE_URL_TEMPLATE) == u'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:59.909548
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Self-testing code
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') == 'mankind-why-this-woman-started-a-men-s-skincare-line'

# Generated at 2022-06-14 17:09:10.006989
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert(ie._VALID_URL == "https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html")
    assert(ie._TEST['url'] == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert(ie._TEST['md5'] == "2c62dd4db2027e35579fefb97a8b6554")

# Generated at 2022-06-14 17:09:21.380152
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar_ie = TheStarIE()
    assert thestar_ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert thestar_ie._VALID_URL == 'https?://(?:www\\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\\.html'
    assert thestar_ie.url_result('http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001', 'BrightcoveNew', '4732393888001')

# Generated at 2022-06-14 17:09:31.168631
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:39.589352
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
   # 
   assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') 
   # test with url that does not match regex
   #assert URL(r'http://www.example.com/foo/bar.html')
   #assert URL(r'http://www.example.com/foo/bar.html')
   #assert URL(r'http://www.example.com/foo/bar.html')
   #assert URL(r'http://www.example.com/foo/bar.html')
   #assert URL(r'http://www.example.com/foo/bar.html')
   #assert URL(r'http://www.example.com/foo/bar.html')
   #

# Generated at 2022-06-14 17:09:50.765514
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    info = ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert info['id'] == '4732393888001'
    assert info['title'] == 'Mankind: Why this woman started a men\'s skin care line'
    assert info['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.'
    assert info['upload_date'] == '20160201'
    # Check for exception if url is invalid

# Generated at 2022-06-14 17:09:51.684865
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    _ = TheStarIE(InfoExtractor())

# Generated at 2022-06-14 17:09:52.322534
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:10:13.858844
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test for youtube video
    youtube_video = TheStarIE(TheStarIE.ie_key())
    youtube_video.url = "https://www.thestar.com/news/world/2016/02/02/manitoba-rescuer-who-saved-woman-from-burning-quebec-train-receives-bronze-medal.html"


# Generated at 2022-06-14 17:10:18.362360
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('https://www.thestar.com/news/gta/2016/08/23/james-durham-former-toronto-detective-convicted-of-robbery-wins-his-fight-against-deportation.html')

# Generated at 2022-06-14 17:10:20.521182
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    TheStarIE(True)._real_initialize()

# Generated at 2022-06-14 17:10:23.460759
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:10:25.311109
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE()
    assert isinstance(instance, TheStarIE)


# Generated at 2022-06-14 17:10:35.576737
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    theStarIE = TheStarIE(url)
    assert theStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert theStarIE.regex == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert theStarIE.display_id == 'mankind-why-this-woman-started-a-men-s-skincare-line'

# Generated at 2022-06-14 17:10:37.078771
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:10:44.076181
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.name == 'TheStar'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:10:52.272685
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_TheStarIE = TheStarIE("TheStarIE.test_TheStarIE", "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html", [], None)
    assert test_TheStarIE.name == "TheStarIE.test_TheStarIE"
    assert test_TheStarIE._TEST['url'] == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    assert test_TheStarIE._TEST['md5'] == "2c62dd4db2027e35579fefb97a8b6554"

# Generated at 2022-06-14 17:10:57.867219
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Unit test - execute test if executed as a standalone program
if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:11:39.850367
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    x = TheStarIE('test')
    print(x.BRIGHTCOVE_URL_TEMPLATE)

# Generated at 2022-06-14 17:11:42.927411
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    c = TheStarIE()
    # Test the metadata of an object of class TheStarIE,
    assert c.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:54.439213
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Arrange
    YouTubeIE.__name__ = 'TestYouTubeIE'
    YouTubeIE._VALID_URL = r'testurl'

    # Act
    print("Created {}".format(TheStarIE(
        'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')))

    # Assert
    assert TheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert hasattr(TheStarIE, '_VALID_URL')
    assert hasattr(TheStarIE, '_TEST')

# Generated at 2022-06-14 17:11:58.029403
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.url == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"


# Generated at 2022-06-14 17:12:03.715069
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:12:06.365556
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar_ie = TheStarIE()

    assert thestar_ie is not None, 'TheStarIE instantiation failed'
    assert thestar_ie.extractor_id == 'thestar'

# Generated at 2022-06-14 17:12:14.794704
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('sdfsdfsdfsdfsdfsdf','http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie.video_id == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:12:16.194362
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:12:22.163501
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Arrange
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    # Act
    extractor = TheStarIE()
    # Assert
    assert extractor.suitable(url)
    assert extractor.__class__ == TheStarIE

# Generated at 2022-06-14 17:12:24.204396
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	TheStarIE()


# Generated at 2022-06-14 17:13:50.955257
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"
    assert ie.VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:13:52.921067
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE



# Generated at 2022-06-14 17:13:57.642921
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    temp = ie.BRIGHTCOVE_URL_TEMPLATE(ie, "4732393888001")
    url = ie._real_extract(temp)
    assert url == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001"
    print ("Passed Test1")


# Generated at 2022-06-14 17:14:00.337515
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.get_id() == 'TheStar'

# Generated at 2022-06-14 17:14:02.337997
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    Video_Extractor_Tester = TheStarIE()
    assert Video_Extractor_Tester


# Generated at 2022-06-14 17:14:03.852762
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:14:05.817121
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_TheStarIE = TheStarIE()
    assert test_TheStarIE != None

# Generated at 2022-06-14 17:14:08.064892
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'Mankind: Why this woman started a men\'s skin care line'
    obj = TheStarIE(url)
    assert '<TheStarIE(%s)>' % url == repr(obj)
    # No assert for __str__ for this complex object; just make it sure that it
    # generates a string
    str(obj)

# Generated at 2022-06-14 17:14:08.744136
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:14:16.002763
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    url = 'http://www.thestar.com/sports/bluejays/2017/07/06/toronto-blue-jays-lose-to-boston-red-sox-to-end-five-game-winning-streak.html'
    ie = TheStarIE()
    info = ie.extract(url)
    assert ie.ie_key() == 'TheStar'

