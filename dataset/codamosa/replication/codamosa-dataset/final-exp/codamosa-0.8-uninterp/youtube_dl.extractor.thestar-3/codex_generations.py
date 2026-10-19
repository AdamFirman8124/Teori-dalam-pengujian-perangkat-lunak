

# Generated at 2022-06-14 17:06:00.213657
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE in ie_gen.BRIGHTCOVE_IE_LIST


# Generated at 2022-06-14 17:06:05.084242
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    import re
    ans = re.compile(r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html')
    assert ans == TheStarIE._VALID_URL

# Generated at 2022-06-14 17:06:06.126654
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:06:08.353936
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    the_star_ie = TheStarIE()
    assert str(the_star_ie) == '<TheStarIE>'


# Generated at 2022-06-14 17:06:19.709291
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:21.788950
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:25.484467
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    print("-------------------testing constructor--------------------------")
    t = TheStarIE("TheStarIE")
    print("-------------------passed constructor test----------------------")

    print("-------------------testing returns------------------------------")
    print("-------------------passed returns test--------------------------")

    print("-------------------testing results------------------------------")
    print("-------------------passed results test--------------------------")

    print("....................TheStarIE Test Pass.........................")

test_TheStarIE()

# Generated at 2022-06-14 17:06:31.070444
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:06:36.584953
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    if ie.suitable('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'):
        print('Good URL')
    else:
        print('Bad URL')

if __name__ == '__main__':
    test_TheStarIE()

# Generated at 2022-06-14 17:06:38.727146
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    try:
        ie = TheStarIE(None)
    except Exception as e:
        assert(str(e) == 'TheStarIE requires a name parameter')
    return True

# Generated at 2022-06-14 17:06:41.768611
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test = TheStarIE()


# Generated at 2022-06-14 17:06:43.006100
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestar_ie = TheStarIE()

# Generated at 2022-06-14 17:06:45.302416
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    info_extractor = TheStarIE(None)
    assert info_extractor._VALID_URL.pattern == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:06:50.277243
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert(ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert(ie.video_id == '4732393888001')

# Generated at 2022-06-14 17:06:51.688750
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	obj = TheStarIE()
	return


# Generated at 2022-06-14 17:06:53.036349
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:07:02.139128
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    video_url0 = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie.url_result(ie.BRIGHTCOVE_URL_TEMPLATE % '4732393888001',
                'BrightcoveNew', '4732393888001')

    assert(ie._download_webpage(video_url0, 'Mankind: Why this woman started a men\'s skin care line') != None)

    # testing _real_extract
    # assert(ie._real_extract(video_url0) != None)

# Generated at 2022-06-14 17:07:06.114202
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    # Test correct
    assert ie.ie_key() == 'TheStar'
    assert ie.ie_key() == TheStarIE.ie_key()
    assert ie.ie_key() == 'TheStar'
    assert ie.IE_NAME == 'TheStar'
    assert ie.extractor is TheStarIE

# Generated at 2022-06-14 17:07:11.284335
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:15.579996
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    # test for function _real_extract
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    result = TheStarIE().extract(url)
    expected_result = {
        '_type': 'url',
        'url': 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001',
        'ie_key': 'BrightcoveNew',
        'id': '4732393888001'
    }
    assert result == expected_result

# Generated at 2022-06-14 17:07:30.858975
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', display_id='4732393888001')
    assert obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    #assert obj.PLAYER_URL == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:33.287513
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:07:35.846546
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    'Unit test for constructor of class TheStarIE.'

    # Success case
    TheStarIE('')

    # Fail case
    try:
        TheStarIE('x')
    except:
        pass


# Generated at 2022-06-14 17:07:38.695897
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie._download_webpage

# Generated at 2022-06-14 17:07:45.957205
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    info = ie._real_extract("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert info['id'] == '4732393888001'
    assert info['ext'] == 'mp4'
    assert info['title'] == 'Mankind: Why this woman started a men\'s skin care line'
    assert info['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.'
    assert info['uploader_id'] == '794267642001'
    assert info['timestamp'] == 1454353482
    assert info['upload_date'] == '20160201'

# Generated at 2022-06-14 17:07:46.767126
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:07:51.650675
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.video_id is None
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Test url of class TheStarIE

# Generated at 2022-06-14 17:07:52.248947
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:08:01.567969
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

    # Test empty constructor
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None

    # Test missing url
    url = None
    with pytest.raises(TypeError):
        TheStarIE(url)

    # Test empty url
    url = ""
    with pytest.raises(ValueError):
        TheStarIE(url)

    # Test invalid url
    url = "invalid"
    with pytest.raises(ValueError):
        TheStarIE(url)

# Generated at 2022-06-14 17:08:09.878307
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:08:18.377310
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:08:21.842749
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:24.509583
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:08:34.505839
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:08:36.219088
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie != None

# Generated at 2022-06-14 17:08:40.368173
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # test for entering invalid url
    instance = TheStarIE(TheStarIE.ie_key())
    assert_raises(ExtractorError, instance.url_result, 'http://example.com')

    # test for extracting video id from a valid url
    instance = TheStarIE(TheStarIE.ie_key())
    video_id = instance._real_extract(TheStarIE._TEST['url'])
    assert video_id == '4732393888001'

# Generated at 2022-06-14 17:08:45.048858
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    params = { 'url': 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html',
            'mode': 'play',
            'return_data': True}
    result = TheStarIE()._downloader.execute_command(TheStarIE()._downloader._match_id, params)
    assert result is not None
    

# Generated at 2022-06-14 17:08:45.653374
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:08:48.612739
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    # This is a functional test case. Only minimal assertions are further required.

# Generated at 2022-06-14 17:08:54.285756
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """
    The constructor of class InfoExtractor should be able to take a urlstring
    and return a instance of class TheStarIE.
    """
    url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    t = TheStarIE(url)
    assert t != None

# Generated at 2022-06-14 17:09:12.380721
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.name == 'TheStar'
    assert ie._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'


# Generated at 2022-06-14 17:09:15.635243
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ref_object = TheStarIE()
    test_object = TheStarIE()
    assert test_object.BRIGHTCOVE_URL_TEMPLATE == ref_object.BRIGHTCOVE_URL_TEMPLATE, 'Test failed'

# Generated at 2022-06-14 17:09:24.462615
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.url == ''
    assert ie.valid_urls == [r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html']
    assert ie.valid_brightcove_ids == []
    assert ie.valid_url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie.valid_url_id == '4732393888001'
    assert ie.src == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'

# Generated at 2022-06-14 17:09:25.328010
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:09:36.983910
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:40.836916
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    a = TheStarIE()
    assert a != None

# Generated at 2022-06-14 17:09:41.418451
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    return TheStarIE

# Generated at 2022-06-14 17:09:46.995262
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    m = TheStarIE()
    tmp = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert m._match_id(tmp) == 'mankind-why-this-woman-started-a-men-s-skincare-line'
    assert m.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:48.354083
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    assert isinstance(t, InfoExtractor)

# Generated at 2022-06-14 17:09:51.259613
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    thestari = TheStarIE()
    assert thestari.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:10:26.573346
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    theStarIE = TheStarIE()
    # should run without error
    try:
        theStarIE.extract(None, None)
    except Exception as e:
        print(e)
        assert False
    print("test_TheStarIE passed!")

# Generated at 2022-06-14 17:10:29.802367
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    i = TheStarIE()
    assert i.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'


# Generated at 2022-06-14 17:10:35.067845
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ies = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert len(ies._downloader._ies) == 1
    assert ies._downloader._ies[0]._real_extract("http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001")['id'] == "4732393888001"

# Generated at 2022-06-14 17:10:35.580004
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:10:42.064011
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    from .common import InfoExtractor
    from .TheStarIE import TheStarIE
    ie = TheStarIE()
    # test for the url
    url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    assert ie._match_id(url)
    # test for the webpage download
    webpage = ie._download_webpage(url, ie._match_id(url))
    # test for the brightcove id
    brightcove_id = ie._search_regex(r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',webpage, 'brightcove id' )
    # test for the result
    result = ie.BRIGHTC

# Generated at 2022-06-14 17:10:51.187238
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    test = ie.BRIGHTCOVE_URL_TEMPLATE % ie._TEST['info_dict']['id']
    url = ie._TEST['url']

    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie.suitable(url) == True
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:10:51.776473
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	TheStarIE()

# Generated at 2022-06-14 17:10:53.605736
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # assert True
    TheStarIE()


# Generated at 2022-06-14 17:11:01.955258
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert ie._API_URL == None
    assert ie._SUBTITLE == None

# Generated at 2022-06-14 17:11:06.999629
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	theStar = TheStarIE()
	theStar._VALID_URL = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
	theStar._match_id(theStar._VALID_URL)

# Generated at 2022-06-14 17:12:47.698113
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Unit tests are usually constructed using the python standard
    # unittest framework, but this one is constructed using the
    # pytest framework, to be able to construct tests in a more
    # funtional style, without having to construct an instance of
    # a class.
    # 
    # To run this unit test, call 'py.test TheStarIE' from the command
    # line.

    # Create an instance of the TheStarIE class, so that we can
    # access the protected members of that class.
    TheStarIE_instance = TheStarIE()

    # Extract the id from the following url, which should be
    # the string '4732393888001'

# Generated at 2022-06-14 17:12:59.582507
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie._VALID_URL
    ie._TEST
    ie._download_webpage
    ie._match_id
    ie._real_extract
    ie._search_regex
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie.BRIGHTCOVE_URL_TEMPLATE
    ie

# Generated at 2022-06-14 17:13:00.088345
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:13:02.286472
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert(ie.__class__.__name__ == 'TheStarIE')

# Generated at 2022-06-14 17:13:11.563973
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    expected_output = 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001'
    ie = TheStarIE(url)
    result = ie._real_extract(url)
    assert result.url == expected_output, "TheStarIE._real_extract did not produce expected output"

# Generated at 2022-06-14 17:13:22.333197
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:13:29.875616
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE.BRIGHTCOVE_URL_TEMPLATE = 'http://foo.com/%s'
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    url = ie._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert url.startswith(TheStarIE.BRIGHTCOVE_URL_TEMPLATE % '4732393888001')

# Generated at 2022-06-14 17:13:34.021967
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    class_name = ie.__class__.__name__
    assert class_name == 'TheStarIE'


# Generated at 2022-06-14 17:13:35.642312
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert isinstance(ie, TheStarIE)

# Generated at 2022-06-14 17:13:36.262281
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()