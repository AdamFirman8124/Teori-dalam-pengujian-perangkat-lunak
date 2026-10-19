

# Generated at 2022-06-14 17:06:00.525944
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    import sys
    import os.path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', ".."))
    from xtester.xtester import Xt
    xt = Xt()
    xt._register_module(__name__, sys.modules[__name__])



# Generated at 2022-06-14 17:06:05.923129
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    inst = TheStarIE('TheStarIE', 'thestar.com', 'star')
    assert inst.name == 'TheStarIE'
    assert inst.ie_key == 'thestar.com'
    assert inst.ie_key == 'thestar.com'
    assert inst.host == 'thestar.com'

# Generated at 2022-06-14 17:06:10.245869
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:15.539574
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    if __name__ == '__main__':
        inputURL = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
        extractor = TheStarIE()
        extractor.url = inputURL
        extractor.download()

# Generated at 2022-06-14 17:06:21.622979
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.url == 'https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie.display_id == 'mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:06:28.488103
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    ie = TheStarIE()
    display_id = ie._match_id(url)
    webpage = ie._download_webpage(url, display_id)
    brightcove_id = ie._search_regex(
            r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',
            webpage, 'brightcove id')
    result = ie.url_result(ie.BRIGHTCOVE_URL_TEMPLATE % brightcove_id,
            'BrightcoveNew', brightcove_id)
#    print(result)


# Generated at 2022-06-14 17:06:29.592702
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    a = TheStarIE()
    assert a

# Generated at 2022-06-14 17:06:39.980518
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:41.721132
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(InfoExtractor())._VALID_URL == TheStarIE._VALID_URL

# Generated at 2022-06-14 17:06:45.766508
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:06:55.569572
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj._VALID_URL == "https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html"
    # Check test case
    # assert obj._TEST == {...}


# Generated at 2022-06-14 17:07:01.648220
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	obj = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
	assert(obj._VALID_URL.match('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'))


# Generated at 2022-06-14 17:07:03.635857
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    print(ie.BRIGHTCOVE_URL_TEMPLATE)


# Generated at 2022-06-14 17:07:10.961642
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for constructor of class TheStarIE"""
    # call constructor of TheStarIE
    testTheStarIE = TheStarIE()
    # check if URL is correct
    assert testTheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    # check if test cases are correct

# Generated at 2022-06-14 17:07:13.609977
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.search(""+ie._VALID_URL)
    ie.download(""+ie._VALID_URL)

# Generated at 2022-06-14 17:07:14.756987
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE

# Generated at 2022-06-14 17:07:21.835852
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    temp = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert temp._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') == '4732393888001'


# Generated at 2022-06-14 17:07:27.938534
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie._real_extract('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001' \
           == ie.BRIGHTCOVE_URL_TEMPLATE % '4732393888001'

# Generated at 2022-06-14 17:07:32.852163
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:39.134171
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    test = ie.extract("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert test == ie._TEST
    assert type(test) == dict

# Generated at 2022-06-14 17:07:54.020458
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE();
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html');

# Generated at 2022-06-14 17:07:58.661122
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ins = TheStarIE()
    assert ins.BRIGHTCOVE_URL_TEMPLATE == TheStarIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:08:08.243301
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

    assert ie.extractor_key == "TheStarIE"
    assert ie.display_id == 'mankind-why-this-woman-started-a-men-s-skincare-line'
    assert ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Unit

# Generated at 2022-06-14 17:08:09.743394
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(TheStarIE._downloader) is not None

# Generated at 2022-06-14 17:08:18.075573
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Create an object for the video.
    video_class = TheStarIE()

    # Create an object for the video and get information of the video.
    video_info = video_class._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert (video_info['id'] == '4732393888001')
    assert (video_info['title'] == 'Mankind: Why this woman started a men\'s skin care line')
    assert (video_info['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.')
    assert (video_info['timestamp'] == 1454353482)

# Generated at 2022-06-14 17:08:18.576493
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()

# Generated at 2022-06-14 17:08:19.717031
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	print("Testing class TheStarIE")
	assert True

# Generated at 2022-06-14 17:08:21.879470
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie= TheStarIE()
    ie.extract(ie._VALID_URL, ie._TEST)


# Generated at 2022-06-14 17:08:25.805889
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie =TheStarIE()

# Generated at 2022-06-14 17:08:26.804550
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie

# Generated at 2022-06-14 17:08:52.443164
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Constructor of TheStarIE needs to be tested before class TheStarIE!
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:08:56.406209
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    a = TheStarIE({}, {})
    assert a.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:08:58.933487
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
        theStarIE = TheStarIE()
        assert isinstance(theStarIE, InfoExtractor)

# Generated at 2022-06-14 17:08:59.577926
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:09:00.644594
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print(TheStarIE())

# Generated at 2022-06-14 17:09:06.579723
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert obj._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:08.129083
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extractor_key = 'TheStar'


# Generated at 2022-06-14 17:09:09.424436
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  ie =TheStarIE()
  ie.constructor()

# Generated at 2022-06-14 17:09:18.522712
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	"""
	Test for constructor of class TheStarIE.
	Class TheStarIE does not inherit from any other class and does not have any class initializer.
	Only thing to check is whether an object of the class is properly initialized.
	"""
	obj = TheStarIE()
	assert(isinstance(obj, TheStarIE) and isinstance(obj, InfoExtractor))
	print("Unit test for constructor of class TheStarIE is succesful.")


# Generated at 2022-06-14 17:09:26.879637
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	from youtube_dl.YoutubeDL import YoutubeDL
	from youtube_dl.extractor.common import ExtractorError
	from itertools import chain
	from tests.test_htmlparser import Mock_html_entities

	# Mock _download_webpage

# Generated at 2022-06-14 17:09:48.265470
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie_obj = TheStarIE()

# Generated at 2022-06-14 17:09:53.883773
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test for valid URL
    thestarie = TheStarIE(TheStarIE._VALID_URL)
    thestarie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # Test for invalid URL
    thestarie = TheStarIE(TheStarIE._VALID_URL)
    thestarie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.php')

# Generated at 2022-06-14 17:10:05.435608
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    u = TheStarIE("")
    assert u._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert u._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert u._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert u._TEST['info_dict']['id'] == '4732393888001'
    assert u._TEST['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:10:14.240173
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:10:18.748363
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Test class TheStarIE"""
    theStarIE = TheStarIE()
    assert theStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:10:30.043704
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	# test for URL.
	assert TheStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:10:32.133618
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:10:32.610629
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:10:40.030632
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    assert t._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    # Below test will pass only for 1st second of each day

# Generated at 2022-06-14 17:10:42.491696
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE()
        assert True
    except Exception:
        assert False


# Generated at 2022-06-14 17:11:32.542619
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    VIDEO_ID = '4732393888001'
    URL = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    thestar = TheStarIE()
    thestar.extract(URL)
    assert thestar._match_id(URL) == VIDEO_ID
    assert thestar._real_extract(URL) == thestar.url_result(thestar.BRIGHTCOVE_URL_TEMPLATE % VIDEO_ID, 'BrightcoveNew', VIDEO_ID)
#--------------------------------------------------

# Generated at 2022-06-14 17:11:36.975853
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._VALID_URL is not None
    assert ie._TEST is not None
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None
    assert ie._downloader is not None
    # TODO: Unit test for function _real_extract

# Generated at 2022-06-14 17:11:37.730838
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:39.504996
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:43.513742
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:44.562317
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:11:47.675250
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert isinstance(TheStarIE({}), TheStarIE)

# Generated at 2022-06-14 17:11:51.162543
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:51.551986
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:58.539262
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Instantiation of class TheStarIE

    # Instantiating with a string
    assert TheStarIE(TheStarIE._VALID_URL)
    # Instantiating with a string and a string
    assert TheStarIE(TheStarIE._VALID_URL, TheStarIE._TEST['url'])
    # Instantiating with a string and a string and a string
    assert TheStarIE(TheStarIE._VALID_URL, TheStarIE._TEST['url'], TheStarIE._TEST['md5'])
    # Instantiating with a string and a dictionary
    assert TheStarIE(TheStarIE._VALID_URL, TheStarIE._TEST)

    # Instantiating with a wrong string
    try:
        TheStarIE('string')
    except:
        pass

    # Instantiating with a wrong dictionary


# Generated at 2022-06-14 17:13:49.613228
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    URL = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    TheStar_ie = TheStarIE()
    assert TheStar_ie._VALID_URL == (r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')
    assert TheStar_ie._TEST['url'] == URL
    assert TheStar_ie._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert TheStar_ie._TEST['info_dict']['id'] == '4732393888001'

# Generated at 2022-06-14 17:13:58.568016
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    # Check if the object of class TheStarIE is created correctly
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:13:59.694730
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:14:07.649089
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:14:08.743228
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	thestar = TheStarIE('TheStarIE')

# Generated at 2022-06-14 17:14:14.992616
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html' # noqa
    ie = TheStarIE()
    ie.extract(url)
    assert ie.url_result == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'


# Generated at 2022-06-14 17:14:16.988281
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(0)

# Generated at 2022-06-14 17:14:28.305573
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Construct the instance
    ie = TheStarIE()
    # Set the url for testing
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    # Retrieve video information
    video_info = ie._real_extract(url)
    # Assert that the title is 'Mankind: Why this woman started a men\'s skin care line'
    assert video_info['title'] == 'Mankind: Why this woman started a men\'s skin care line'
    # Assert that the duration is None
    assert video_info['duration'] == None
    # Try to download the video
    success = ie.extract(url)
    # Assert that the download is not successful
    assert success == False

# Generated at 2022-06-14 17:14:32.358399
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    '''
    Unit test for constructor of class TheStarIE
    '''
    assert isinstance(TheStarIE(), TheStarIE)


# Generated at 2022-06-14 17:14:33.211057
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert(len(TheStarIE._TEST)) == 5