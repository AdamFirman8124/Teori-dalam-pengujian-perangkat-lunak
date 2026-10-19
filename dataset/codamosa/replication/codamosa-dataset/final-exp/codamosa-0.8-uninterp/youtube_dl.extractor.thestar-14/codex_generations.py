

# Generated at 2022-06-14 17:06:03.815148
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    for url in ['http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html']:
        ie.url = url
        assert ie.url_result(ie.BRIGHTCOVE_URL_TEMPLATE % '4732393888001', 'BrightcoveNew', '4732393888001')

# Generated at 2022-06-14 17:06:07.554166
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('TheStarIE', 'thestar.com', 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:06:09.718443
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    assert isinstance(t, TheStarIE)

# Generated at 2022-06-14 17:06:20.062853
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	the_star_ie = TheStarIE()
	assert the_star_ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:29.776375
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    expected_url = ie.BRIGHTCOVE_URL_TEMPLATE % '4732393888001'

# Generated at 2022-06-14 17:06:38.993648
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert ie._TEST['info_dict']['id'] == '4732393888001'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
    assert ie._TEST['info_dict']['title'] == 'Mankind: Why this woman started a men\'s skin care line'
    assert ie._TEST['info_dict']['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.'
    assert ie._TEST['info_dict']['uploader_id'] == '794267642001'

# Generated at 2022-06-14 17:06:41.577803
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	instance = InfoExtractor()
	assert instance.get_info_extractor(
		TheStarIE._VALID_URL) is TheStarIE



# Generated at 2022-06-14 17:06:46.370465
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert isinstance(
        TheStarIE().extract_from_url(
            'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'),
        TheStarIE._TEST['url'])

# Generated at 2022-06-14 17:06:48.564490
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	try:
		ie = TheStarIE(None)
	except BaseException as e:
		print(str(e))
		assert False

# Generated at 2022-06-14 17:06:53.827419
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE()
    assert the_star_ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:01.556327
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for constructor of class TheStarIE"""

    # check correct initialization
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:03.203167
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ''' Ensure that class constructor of class TheStarIE is created '''
    ie = TheStarIE()
    assert ie != None

# Generated at 2022-06-14 17:07:11.186573
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:16.104573
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:21.438259
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE()
    assert instance._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert instance.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:22.038273
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:07:25.318522
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._TEST['url'] == TheStarIE._VALID_URL
    assert TheStarIE._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'

# Generated at 2022-06-14 17:07:30.841166
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    #Initialize TheStarIE with test url
    TheStarIE()._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

test_TheStarIE()

# Generated at 2022-06-14 17:07:36.941340
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert_equal("https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html", ie.url)

# Generated at 2022-06-14 17:07:40.139637
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:49.023716
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    actual = obj._VALID_URL
    expected = 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert actual==expected


# Generated at 2022-06-14 17:07:54.493725
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for constructor of class TheStarIE"""
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:07:59.666242
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie._VALID_URL
    ie._TEST
    ie._real_extract
test_TheStarIE()

# Generated at 2022-06-14 17:08:00.716423
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Simple unit test for constructor of class TheStarIE"""
    TheStarIE()

# Generated at 2022-06-14 17:08:11.442145
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .common import InfoExtractor
    from .test import make_test_data_path

    video_url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

    ie = InfoExtractor(TheStarIE.IE_NAME, TheStarIE.VALID_URL).new_instance()
    assert ie.is_suitable(video_url)

    test_data_path = make_test_data_path()
    TEST_FILE_OUTPUT = test_data_path + '/TheStarIE.test'

    ie = InfoExtractor(TheStarIE.IE_NAME, TheStarIE.VALID_URL).new_instance(TheStarIE._TEST)

# Generated at 2022-06-14 17:08:15.286578
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.display_id == 'mankind-why-this-woman-started-a-men-s-skincare-line'

# Generated at 2022-06-14 17:08:16.664055
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # constructor of TheStarIe class
    TheStarIE()


# Generated at 2022-06-14 17:08:17.228421
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE()

# Generated at 2022-06-14 17:08:24.674857
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    x = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert( isinstance(x, InfoExtractor) and
            x.get_id() == '4732393888001' and
            x.get_ext() == 'mp4' and
            x.get_description() == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.' and
            x.get_timestamp() == 1454353482 and
            x.get_upload_date() == '20160201')


# Generated at 2022-06-14 17:08:27.972446
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIEShow(
        TheStarIE(),
        'http://www.thestar.com/news/world/2016/01/29/china-sentences-rights-lawyers-to-prison.html',
    )


# Generated at 2022-06-14 17:08:46.016281
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    Test constructor of TheStarIE.
    """
    instance = TheStarIE('www.thestar.com', 'thestar.com', 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', 'Mankind: Why this woman started a men\'s skin care line', 'mp4')
    assert instance.name == 'www.thestar.com'
    assert instance.ie_key == 'thestar'
    assert instance.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

# Generated at 2022-06-14 17:08:54.733403
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html').__class__.__name__ == 'TheStarIE'
    assert TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')._TEST.get('info_dict').get('title') == 'Mankind: Why this woman started a men\'s skin care line'

# Generated at 2022-06-14 17:08:57.240009
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:09:05.729009
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # to test a constructor of class TheStarIE
    instance = TheStarIE()
    # to test a _VALID_URL of class TheStarIE
    validURL = 'https://www.thestar.com/entertainment/television/2016/02/02/cbc-tapped-to-air-2017-ioc-meeting-in-switzerland.html'
    match = instance._match_id(validURL)
    t = instance._download_webpage(validURL,match)
    s = instance._real_extract(validURL)

# Generated at 2022-06-14 17:09:11.878066
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info_extractor = TheStarIE()
    assert info_extractor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert info_extractor.BRIGHTOCVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert info_extractor.brightcove_url_template == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'



# Generated at 2022-06-14 17:09:18.089516
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # This test is  run with the --download-archive option set, which creates a
    # file "archive.txt" in the current directory. This test is made to ensure
    # that this file doesn't contain the video files downloaded.
    with open("archive.txt") as archive:
        assert r"tmpXfKjId.mp4" not in archive.read()

# Generated at 2022-06-14 17:09:25.596209
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE('http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001')
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert obj._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:26.730038
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    theStar = TheStarIE()

# Generated at 2022-06-14 17:09:28.709153
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.get_url() == ie._VALID_URL

# Generated at 2022-06-14 17:09:35.782561
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Constructor test for the class"""
    result = True
    ie = TheStarIE()
    video_url = ie.BRIGHTCOVE_URL_TEMPLATE % ie._TEST["info_dict"]['id']
    expected_video_url = ie._TEST["info_dict"]['url']

    result = result and (video_url == expected_video_url)
    assert result


# Generated at 2022-06-14 17:10:05.433666
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie == 'thestar', "name is not thestar"
    assert ie.ie_key() == 'thestar', "ie_key is not thestar"
    assert ie.valid_url('http://www.thestar.com'), "url should be valid"
    assert ie.valid_url('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'), "url should be valid"
    assert ie.valid_url('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') == True, "TheStarIE.valid_url() False neg"
    assert ie.valid

# Generated at 2022-06-14 17:10:14.238286
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    tsi = TheStarIE()
    assert tsi._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:10:17.928275
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()._real_extract("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:10:18.837415
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie

# Generated at 2022-06-14 17:10:30.158031
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    theStar = TheStarIE()
    assert theStar._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert theStar._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert theStar._TEST['md5'] == '2c62dd4db2027e35579fefb97a8b6554'
    assert theStar._TEST['info_dict']['id'] == '4732393888001'
    assert theStar._TEST['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:10:39.574585
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:10:44.483677
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    return TheStarIE(TheStarIE._downloader, {})._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:10:52.555076
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    # Arrange
    testURL = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    theStar = TheStarIE()
    expected = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'
    expected2 = 'Mankind: Why this woman started a men\'s skin care line'

    # Act
    actual = theStar._real_extract(testURL)

    # Assert
    assert actual['webpage_url'] == expected
    assert actual['entries'][0]['title'] == expected2

# Generated at 2022-06-14 17:10:56.105846
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:11:02.861979
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """ Unit test for constructor of class TheStarIE """
    # Test to create TheStarIE object:
    TheStarIE = TheStarIE(TheStarIE._VALID_URL)
    # Test to get the name of TheStarIE
    assert TheStarIE.ie_key() == 'TheStar'
    # Test to get the expected declaration of URL
    assert TheStarIE._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    # Test to get the expected declaration of TestCase

# Generated at 2022-06-14 17:11:55.210072
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    MyTheStarIE = TheStarIE()
    assert MyTheStarIE._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:11:55.634726
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:56.273275
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Verify if the constructor presently works
    TheStarIE()

# Generated at 2022-06-14 17:11:56.698244
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:11:59.706858
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    # Use pdb module to pause the execution and then use c, n and s to explore the object
    import pdb; pdb.set_trace()

# Generated at 2022-06-14 17:12:02.095780
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE(None)._VALID_URL == TheStarIE._VALID_URL

# Generated at 2022-06-14 17:12:09.220017
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	test_obj = TheStarIE('https://www.thestar.com/entertainment/television/2016/02/01/the-x-files-reboot-should-have-been-wonderful.html')
	expected_id = '4732393888001'
	assert test_obj.BRIGHTCOVE_URL_TEMPLATE % expected_id == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'


# Generated at 2022-06-14 17:12:16.952123
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .brightcove import BrightcoveNewIE
    from .bases import CompatStr
    from .common import InfoExtractor

    # Create instance of class TheStarIE
    thestar = TheStarIE()

    assert thestar.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

    assert thestar.BRIGHTCOVE_URL_TEMPLATE == CompatStr('http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')


# Generated at 2022-06-14 17:12:20.736880
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE.suitable('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') == True

# Generated at 2022-06-14 17:12:21.990472
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:13:54.158061
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.extract("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    ie.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 17:13:55.163479
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj_TheStarIE = TheStarIE()

# Generated at 2022-06-14 17:14:00.541216
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert(ie._VALID_URL==r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')
    assert(ie.BRIGHTCOVE_URL_TEMPLATE=='http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:14:08.007740
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:14:12.403914
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE('TheStar')
    with open('test.html') as f:
        page = f.read()
    t._download_webpage('http://www.thestar.com', '73853723546')
    t._real_extract('http://www.thestar.com')


# Generated at 2022-06-14 17:14:15.193265
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')


# Generated at 2022-06-14 17:14:22.103484
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(
        TheStarIE.BRIGHTCOVE_URL_TEMPLATE % "12345")
    assert ie.url == ("http://players.brightcove.net/794267642001/"
                      "default_default/index.html?videoId=12345")
    assert ie.video_id == "12345"
    assert ie.ie_key() == "brightcove:12345"

# Generated at 2022-06-14 17:14:22.907808
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:14:26.451519
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info_extractor = TheStarIE()
    print('Testing URL: ' + info_extractor._TEST['url'])
    info_extractor.extract(info_extractor._TEST['url'])

# Generated at 2022-06-14 17:14:37.223883
# Unit test for constructor of class TheStarIE