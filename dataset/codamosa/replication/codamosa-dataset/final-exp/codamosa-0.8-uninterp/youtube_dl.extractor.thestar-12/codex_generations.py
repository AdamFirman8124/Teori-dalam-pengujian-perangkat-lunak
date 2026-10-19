

# Generated at 2022-06-14 17:06:02.660045
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert(TheStarIE._VALID_URL == 
		r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')


# Generated at 2022-06-14 17:06:10.960317
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()
#Defines the object of class TheStarIE as yt_ie
yt_ie = TheStarIE()

# The below lines are not neccessary. 
# For demonstration only. 
# The following two lines will print all the list of 
# dictionaries of all attributes in TheStarIE class


# Generated at 2022-06-14 17:06:19.216727
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie.__name__ == 'www.thestar.com'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:06:20.175133
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    infoextractor = TheStarIE()

# Generated at 2022-06-14 17:06:23.634849
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'




# Generated at 2022-06-14 17:06:27.679688
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == TheStarIE._VALID_URL
    assert ie._TEST == TheStarIE._TEST
    assert ie.BRIGHTCOVE_URL_TEMPLATE == TheStarIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:06:33.859366
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert(ie.URL == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:06:34.654023
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:06:46.957837
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    e = TheStarIE()
    assert(e._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')

# Generated at 2022-06-14 17:06:49.670380
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:02.674941
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # This function is used to test the constructor of TheStarIE class
    name = 'TheStarIE'
    ie_inst = TheStarIE()
    # Here, the assertEqual is used to verify that the object of TheStarIE class is created successfully
    assertEqual(ie_inst.name, name)
    # Here, the assertEqual is used to verify that the instance attributes are created successfully
    assertEqual(ie_inst._VALID_URL, r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')

# Generated at 2022-06-14 17:07:03.396557
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:07:08.669267
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    a = TheStarIE()
    assert(a.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:07:10.784700
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    v = TheStarIE()
    assert v.__class__.__name__ == "TheStarIE"

# Generated at 2022-06-14 17:07:13.409452
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Testing an example
    thestar_test = TheStarIE()
    thestar_test.BRIGHTCOVE_URL_TEMPLATE


# Generated at 2022-06-14 17:07:16.204050
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    myInstance = TheStarIE()
    assert isinstance(myInstance, TheStarIE)

# Generated at 2022-06-14 17:07:16.822156
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    pass

# Generated at 2022-06-14 17:07:26.581571
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestarie = TheStarIE()
    assert (thestarie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')
    assert (thestarie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')

# Generated at 2022-06-14 17:07:27.122692
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()

# Generated at 2022-06-14 17:07:31.472571
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.TheStarIE
    ie._TEST
    ie._VALID_URL
    ie._download_webpage

# Generated at 2022-06-14 17:07:40.626651
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .test_utils import MyTestCase
    class construct_test(MyTestCase):
        def test_construct(self):
            inst = TheStarIE()
            self.assertEqual(inst.BRIGHTCOVE_URL_TEMPLATE, 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')
    construct_test('test_construct').run()


# Generated at 2022-06-14 17:07:47.088144
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.url_result('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', 'BrightcoveNew', '4732393888001') == '4732393888001'

# Generated at 2022-06-14 17:07:49.944394
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:52.785538
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s', "TheStarIE.BRIGHTCOVE_URL_TEMPLATE should be 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'"


# Generated at 2022-06-14 17:07:59.785693
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert(ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html' or ie._VALID_URL == r'http://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')

# Generated at 2022-06-14 17:08:03.479397
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    

# Generated at 2022-06-14 17:08:15.360747
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    web_page_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    video_id = '4732393888001'
    the_starIE = TheStarIE()
    # test of instance constructor
    the_starIE.TheStarIE()
    # test of _match_id method
    video_id_test = the_starIE._match_id(web_page_url)
    assert video_id == video_id_test
    # test of _download_webpage method
    web_page_url_test = the_starIE._download_webpage(web_page_url, video_id)

# Generated at 2022-06-14 17:08:15.730031
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    pass

# Generated at 2022-06-14 17:08:17.083787
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert TheStarIE.__name__ == "TheStarIE"


# Generated at 2022-06-14 17:08:26.103555
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'

# Generated at 2022-06-14 17:08:45.009096
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    import TheStarIE
    d = TheStarIE.TheStarIE()
    i = TheStarIE._TEST

# Generated at 2022-06-14 17:08:50.509812
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:08:54.506768
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE({})
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie.extract(url)


# Generated at 2022-06-14 17:09:07.809247
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test 1
    test_1 = TheStarIE()
    test_1.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    test_1._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # Test 2
    test_2 = TheStarIE()
    test_2.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:09.131573
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    video_obj = TheStarIE()


# Generated at 2022-06-14 17:09:17.377779
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info_obj = TheStarIE().get_info_obj(url="https://www.thestar.com/news/queenspark/2016/02/06/ontario-looks-to-identify-where-the-best-syrian-refugees-will-land.html")
    assert(info_obj.id == "4732692843001")
    assert(info_obj.title == "Ontario looks to identify where the best Syrian refugees will land")
    assert(info_obj.author == "Richard J. Brennan")
    assert(info_obj.uploader == "Toronto Star")
    assert(info_obj.url == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732692843001")


# Generated at 2022-06-14 17:09:25.663251
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:09:30.708912
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestarie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    print(thestarie.extract())

# Generated at 2022-06-14 17:09:39.338348
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	m = TheStarIE();
	assert(m.name == 'thestar.com')
	assert(m.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:09:41.934587
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    theStarIE = TheStarIE()
    print (theStarIE._VALID_URL)
    print (theStarIE.BRIGHTCOVE_URL_TEMPLATE)


# Generated at 2022-06-14 17:10:07.819851
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # URL of the page.
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    # ID of the page.
    id = 'mankind-why-this-woman-started-a-men-s-skincare-line'
    # Test if the id of the page is same as the test.
    assert(id == ie._id)
    # Test if the webpage of the page was downloaded.
    webpage = ie._download_webpage(url, id)

# Generated at 2022-06-14 17:10:10.383668
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:10:16.165178
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    inp_url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    i = TheStarIE(inp_url)
    assert i.url == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    assert i._match_id(inp_url) == "mankind-why-this-woman-started-a-men-s-skincare-line"

# Generated at 2022-06-14 17:10:25.243540
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.brightcove_url_template == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._valid_url('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._valid_url('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') == True

# Generated at 2022-06-14 17:10:27.064227
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    inst = TheStarIE

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:10:29.542528
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	a = TheStarIE()

# Generated at 2022-06-14 17:10:32.612777
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    pass

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:10:34.834001
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print('Begin test of class TheStarIE')
    # Test creating an instance of the class.
    TheStarIE()
    print('End test of class TheStarIE')


# Generated at 2022-06-14 17:10:37.063455
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    theStar = TheStarIE() # Do not throw exception
    theStar = TheStarIE(params={'proxy': 'http://user:pass@127.0.0.1:8080'}) # Do not throw exception

# Generated at 2022-06-14 17:10:43.720727
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:30.105749
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie._downloader.login == '7703900'
    assert ie._downloader.password == 'Gm73g5'

test_TheStarIE()

# Generated at 2022-06-14 17:11:34.056232
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=6264669352001' == ie.BRIGHTCOVE_URL_TEMPLATE % '6264669352001'

# Generated at 2022-06-14 17:11:36.952234
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestarIE = TheStarIE()
    assert thestarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:11:39.501763
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None

# Generated at 2022-06-14 17:11:40.504017
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE(TheStarIE.ie_key())


# Generated at 2022-06-14 17:11:41.967388
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()._VALID_URL is not None
    assert TheStarIE()._TEST is not None

# Generated at 2022-06-14 17:11:47.714458
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    ret_dict = {
        'id': '4732393888001',
        'ext': 'mp4',
        'title': 'Mankind: Why this woman started a men\'s skin care line',
        'description': 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.',
        'uploader_id': '794267642001',
        'timestamp': 1454353482,
        'upload_date': '20160201'
    }
    assert ie._TEST == ret_dict


# Generated at 2022-06-14 17:11:49.420654
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	t = TheStarIE()
	assert t != None


# Generated at 2022-06-14 17:11:55.806978
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    t.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    t._download_webpage = lambda url, display_id: open('test.html').read()
    t._search_regex = lambda pat, str, name: '4732393888001'
    t.url_result = lambda url, ie, video_id: [url, ie, video_id]

# Generated at 2022-06-14 17:11:56.443004
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # TheStarIE()
    pass

# Generated at 2022-06-14 17:13:32.881787
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()

# Test the function _real_extract in class TheStarIE

# Generated at 2022-06-14 17:13:41.881914
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    name = 'thestar'
    website = 'thestar.com'
    builder = 'https://players.brightcove.net/794267642001/default_default/index.html?videoId=4732506910001'
    example = 'http://www.thestar.com/life/2016/02/05/toronto-dog-owner-wants-to-help-seniors-with-her-pet-rental-service.html'
    objTheStarIE = TheStarIE()
    # test constructor with assertEquals
    assert objTheStarIE.name == name
    assert objTheStarIE.website == website
    assert objTheStarIE.builder == builder
    assert objTheStarIE._VALID_URL == example

# Generated at 2022-06-14 17:13:42.890183
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    x = TheStarIE()

# Generated at 2022-06-14 17:13:51.483420
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	# Test for unsuccessful initialization of brightcove_url
	info_extractor = InfoExtractor(InfoExtractor.BRIGHTCOVE_URL_TEMPLATE % NULL)
	assert info_extractor.BRIGHTCOVE_URL == NULL, "info_extractor.BRIGHTCOVE_URL is NULL"
	assert (info_extractor.BRIGHTCOVE_URL is NULL)
	# Test for successful initialization of brightcove_url
	info_extractor = InfoExtractor(thestarie.BRIGHTCOVE_URL_TEMPLATE % BRIGHTCOVE_ID)

# Generated at 2022-06-14 17:13:51.844829
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  pass

# Generated at 2022-06-14 17:13:53.964889
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    t.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:13:58.123595
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert(ie.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s")

# Generated at 2022-06-14 17:14:01.145365
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test for class constructor
    obj = TheStarIE()
    assert obj.BRIGHTCOVE_URL_TEMPLATE != None


# Generated at 2022-06-14 17:14:04.085412
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test sample given in the docstring of that class
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.extract(TheStarIE._TEST['url'])

# Generated at 2022-06-14 17:14:09.721366
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Nothing to assert, just a test to see if it can be instantiated:
    ie = TheStarIE()
    ie = TheStarIE('TheStarIE')
    ie = TheStarIE('TheStarIE', 'TheStarIE.test')