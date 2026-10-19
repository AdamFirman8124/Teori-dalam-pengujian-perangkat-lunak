

# Generated at 2022-06-14 17:05:57.615062
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:06:00.402360
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	expected_object = TheStarIE(None)
	assert expected_object._VALID_URL == TheStarIE._VALID_URL
	assert expected_object._TEST == TheStarIE._TEST


# Generated at 2022-06-14 17:06:02.463091
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE();

# Generated at 2022-06-14 17:06:05.593992
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:11.256405
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
        Encapsulates test cases of TheStarIE class.
    """
    import sys

    # Test input parameters
    sys.argv = ["TheStarIE.py", "--url='http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"]
    # Create instance of class
    TheStarIE()

# Generated at 2022-06-14 17:06:21.331731
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
  ie = TheStarIE()
  # Test normal case
  
  # Test to see if the video ID is extracted correctly
  url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
  ie.url_result(url, 'TheStar')

  # Test to see if the url is not supported
  url = 'http://www.thestar.com/careers'
  ie.url_result(url, None)

  # Test to see if the video ID is not found
  url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:06:24.713522
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t1 = TheStarIE()
    t2 = TheStarIE()
    assert t1.BRIGHTCOVE_URL_TEMPLATE == t2.BRIGHTCOVE_URL_TEMPLATE
    assert t1.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:26.091336
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE()
    assert type(instance) is TheStarIE

# Generated at 2022-06-14 17:06:28.489965
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	pass

# Generated at 2022-06-14 17:06:31.424520
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html').BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:06:40.866621
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    test_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    test_id = '4732393888001'
    test_brightcove_template = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    test_brightcove_video_id = '4732393888001'

    assert ie._VALID_URL == ie._VALID_URL
    assert ie._TEST == ie._TEST
    assert ie.BRIGHTCOVE_URL_TEMPLATE == ie.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:06:44.268138
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test initiating an instance of TheStarIE
    ie = TheStarIE()
    assert ie is not None
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not ''

# Generated at 2022-06-14 17:06:44.955665
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()
    True

# Generated at 2022-06-14 17:06:52.211609
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    print(obj.BRIGHTCOVE_URL_TEMPLATE)
    print(obj.extract_video_info('4732393888001'))
    print(obj.extract_video_info('4734894093001'))
    print(obj.extract_video_info('4734490873001'))
    print(obj.extract_video_info('4734385930001'))
    print(obj.extract_video_info('4731827176001'))


# Generated at 2022-06-14 17:07:02.979447
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    return type('TheStarIE', (), {
        '_download_json': lambda *a, **k: {
            'id': '1',
            'title': '<TITLE>',
            'description': '<DESCRIPTION>',
        },
        '_download_webpage': lambda *a, **k: '<WEBPAGE>',
        '_search_regex': lambda *a, **k: '2',
        'url_result': lambda *a, **k: type('UrlResult', (object,), {'__getitem__': lambda x, y: x})(),
    })

# Unit test

# Generated at 2022-06-14 17:07:03.896459
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:07:16.073200
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_TheStarIE = TheStarIE()
    assert test_TheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:17.589802
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    new_TheStarIE = TheStarIE()
    return True

# Generated at 2022-06-14 17:07:19.458575
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	info_extractor = TheStarIE()
	assert info_extractor
	assert isinstance(info_extractor, InfoExtractor)

# Generated at 2022-06-14 17:07:21.108705
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	test = TheStarIE()

# Generated at 2022-06-14 17:07:29.644870
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    TheStarIE(TheStarIE._VALID_URL % 'www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:31.919219
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	assert TheStarIE(TheStarIE._VALID_URL)


# Generated at 2022-06-14 17:07:41.658296
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie.BRIGHTCOVE_URL_TEMPLATE_TEST = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    webpage = """
    <html>
        <head></head>
        <body>
            <script type="text/javascript">
                mainartBrightcoveVideoId = "4732393888001";
            </script>
        </body>
    </html>
    """

    brightcove_id = "4732393888001"

# Generated at 2022-06-14 17:07:47.300324
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Ensure the vars are defined
    assert TheStarIE.__name__ is not None

    # Make sure the class can be instantiated
    instance = TheStarIE()
    assert instance is not None

    # Make sure the constructor initlializes correctly
    assert instance._downloader is not None
    assert instance._working_dir is not None

# Generated at 2022-06-14 17:07:55.978847
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # As this test is to test the class constructor
    # Inherited class methods should not be used for testing
    # Therefore, the following methods are implemented directly
    # to test the class constructor TheStarIE()
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    display_id = '4732393888001'
    TheStarIE._download_webpage = lambda self, x, y: ''
    TheStarIE._search_regex = lambda self, x, y, z: ''
    TheStarIE.url_result = lambda self, x, y, z: ''
    assert TheStarIE._real_extract(TheStarIE, url)

# Generated at 2022-06-14 17:07:56.614214
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:08:03.609648
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert('TheStarIE' in globals())
    TheStarIE_instance = TheStarIE()
    assert(TheStarIE_instance is not None)
    assert(TheStarIE_instance.ie_key() == 'thestar')
    assert(TheStarIE_instance.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')


# Generated at 2022-06-14 17:08:09.793695
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj.__class__.__name__ == 'TheStarIE'
    #assert obj.BRIGHT_COVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"

# Generated at 2022-06-14 17:08:11.155018
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test the constructor of class TheStarIE
    assert TheStarIE(the_star_ie = TheStarIE).the_star_ie == TheStarIE

# Generated at 2022-06-14 17:08:18.628284
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()._VALID_URL == TheStarIE._VALID_URL
    assert TheStarIE()._TEST == TheStarIE._TEST
    assert TheStarIE().BRIGHTCOVE_URL_TEMPLATE == TheStarIE._TEST['url']
    assert TheStarIE().BRIGHTCOVE_URL_TEMPLATE == TheStarIE._TEST['md5']
    assert TheStarIE().BRIGHTCOVE_URL_TEMPLATE == TheStarIE._TEST['info_dict']
    assert TheStarIE().BRIGHTCOVE_URL_TEMPLATE == TheStarIE._TEST['params']
    assert TheStarIE().BRIGHTCOVE_URL_TEMPLATE == TheStarIE._TEST['ext']

# Test for what the real_extract method returns


# Generated at 2022-06-14 17:08:30.127274
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:08:31.094789
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE(None)

# Generated at 2022-06-14 17:08:36.489424
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.__name__ == 'TheStarIE'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:08:41.508065
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.__name__ == 'TheStar'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:44.117602
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test if `__init__` of `TheStarIE` class will work properly
    i = TheStarIE()



# Generated at 2022-06-14 17:08:48.729924
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("default_default")
    assert ie.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"

# Generated at 2022-06-14 17:08:49.757392
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    pass


# Generated at 2022-06-14 17:08:55.626447
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:09:07.851935
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    file_path="../test_data/thestar_response.html"
    with open(file_path) as temp_file:
        response_content = temp_file.read()
    extractor = TheStarIE()
    assert(extractor._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') is not None)
    # Unit test for method used in _real_extract

# Generated at 2022-06-14 17:09:16.976396
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:35.445296
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        TheStarIE()
    except Exception as e:
        raise AssertionError(e)

# Generated at 2022-06-14 17:09:39.512776
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    BrightcoveNew = ie.BRIGHTCOVE_URL_TEMPLATE
    assert BrightcoveNew == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:50.287686
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj is not None
    assert hasattr(obj, "thestar_url_template")
    assert obj.thestar_url_template == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert hasattr(obj, "brightcove_new_id")
    assert obj.brightcove_new_id == 'BrightcoveNew'
    assert hasattr(obj, "BASE_URL")
    assert obj.BASE_URL == 'http://www.thestar.com'
    assert hasattr(obj, "VIDEO_URL_TEMPLATE")
    assert obj.VIDEO_URL_TEMPLATE == 'http://www.thestar.com/%s'

# Generated at 2022-06-14 17:09:54.578649
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    u = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    TheStarIE(TheStarIE._downloader).suitable(u)
    TheStarIE(TheStarIE._downloader).extract(u)

# Generated at 2022-06-14 17:10:05.470514
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """ This function tests class TheStarIE
    """
    from ..utils import _download_webpage, _search_regex
    from ..compat import (compat_urllib_request, compat_parse_qs,
                          compat_str)

    class Dummy:
        """ This is a dummy class for testing purposes
        """
        def __init__(self, display_id):
            self.display_id = display_id
            self.url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
            self.webpage = compat_urllib_request.urlopen(self.url)
            self.webpage = compat_str(self.webpage.read())


# Generated at 2022-06-14 17:10:11.521183
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Unit test for constructor of class TheStarIE
    # Valid URL
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # Invalid URL
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line')

# Generated at 2022-06-14 17:10:20.103283
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    YoutubeURL = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    url = TheStarIE._match_id(YoutubeURL)
    # check that the expected display_id is returned
    assert url == '4732393888001'
    # check that the right URL is extracted
    assert TheStarIE._real_extract(url) == 'TheStar'

# Generated at 2022-06-14 17:10:31.752362
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    x = TheStarIE()
    assert x.class_name() == "TheStarIE"
    assert x._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:10:36.373392
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie.url == "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"


# Generated at 2022-06-14 17:10:40.241384
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    #  Following two lines are the test case of the constructor
    assert TheStarIE._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert TheStarIE._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'



# Generated at 2022-06-14 17:11:22.283347
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    # Tests constructor
    # Also tests:
    # * TheStarIE._real_extract()
    # * brightcove.BrightcoveIE._real_extract
    # * brightcove.BrightcoveNewIE._real_extract
    assert TheStarIE._test()[0].startswith('http://players.brightcove.net/794267642001/default_default/index.html?videoId=')



# Generated at 2022-06-14 17:11:24.564848
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # test: constructor of class TheStarIE
    assert TheStarIE._VALID_URL
    assert TheStarIE._TEST
    assert TheStarIE.BRIGHTCOVE_URL_TEMPLATE


# Generated at 2022-06-14 17:11:33.017741
# Unit test for constructor of class TheStarIE
def test_TheStarIE():    
    the_star_ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert the_star_ie.display_id == 'mankind-why-this-woman-started-a-men-s-skincare-line'
    assert the_star_ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert the_star_ie.valid_url()


# Generated at 2022-06-14 17:11:34.459612
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.overridden_url_pattern == TheStarIE._VALID_URL

# Generated at 2022-06-14 17:11:35.689166
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:11:36.196770
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:39.631326
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	# one test case for each function and the returned result should not be None
	assert TheStarIE(0)._real_extract(0) != None
	assert TheStarIE(0).BRIGHTCOVE_URL_TEMPLATE != None
	assert TheStarIE(0)._url_basename(0) != None


# Generated at 2022-06-14 17:11:40.182567
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:42.326051
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert (TheStarIE._URL_TEMPLATE
            == "https://link.brightcove.com/services/player/bcpid%s?bctid=%s")

# Generated at 2022-06-14 17:11:48.907583
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    ie_test = ie._TEST
    assert ie_test['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie_test['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    ie_test

# Generated at 2022-06-14 17:13:29.345976
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj_TheStarIE = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert obj_TheStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert obj_TheStarIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:31.665923
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()

# Generated at 2022-06-14 17:13:36.342968
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

    # test the BRIGHTCOVE_URL_TEMPLATE in the constructor
    assert(ie.BRIGHTCOVE_URL_TEMPLATE) == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"

# Generated at 2022-06-14 17:13:41.500093
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info = TheStarIE()
    assert(info.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:13:50.610320
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = "https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    thestarIE = TheStarIE()
    assert thestarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:13:56.532537
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:13:59.798446
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:14:00.846150
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    print(TheStarIE())

# Generated at 2022-06-14 17:14:03.460588
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:14:08.898898
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')