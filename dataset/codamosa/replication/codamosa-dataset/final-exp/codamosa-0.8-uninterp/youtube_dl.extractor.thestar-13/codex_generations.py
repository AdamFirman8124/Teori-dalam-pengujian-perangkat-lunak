

# Generated at 2022-06-14 17:06:05.331959
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    success = True

    instance = TheStarIE()

# Generated at 2022-06-14 17:06:06.394125
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE({})

# Generated at 2022-06-14 17:06:11.877179
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    print("\nTesting TheStarIE constructor:")
    print("\t- URL = " + TheStarIE._TEST['url'])
    theStarIE = TheStarIE()
    assert theStarIE._TEST['url'] == theStarIE._VALID_URL
    assert theStarIE.__class__.__name__ == 'TheStarIE'

# Generated at 2022-06-14 17:06:21.788533
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._TEST['url'] == \
    'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

    assert TheStarIE._TEST['md5'] == \
    '2c62dd4db2027e35579fefb97a8b6554'

    assert TheStarIE._TEST['info_dict']['id'] == \
    '4732393888001'

    assert TheStarIE._TEST['info_dict']['ext'] == \
    'mp4'

    assert TheStarIE._TEST['info_dict']['title'] == \
    'Mankind: Why this woman started a men\'s skin care line'

    assert TheStarIE._TEST

# Generated at 2022-06-14 17:06:23.690153
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Input is instance of url
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    ie = TheStarIE(url)
    assert ie.url == url


# Generated at 2022-06-14 17:06:26.047092
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    global _extractors
    _extractors = []

    TheStarIE()
    assert len(_extractors) == 1

# Generated at 2022-06-14 17:06:37.929559
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()

# Generated at 2022-06-14 17:06:39.518322
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    """Unit test for constructor of class TheStarIE"""
    assert test_TheStarIE

# Generated at 2022-06-14 17:06:49.806954
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    assert TheStarIE._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:07:01.468710
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # TODO: check if there is a better way to do this
    res = TheStarIE()._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert(res['id'] == '4732393888001')
    assert(res['ext'] == 'mp4')
    assert(res['title'] == 'Mankind: Why this woman started a men\'s skin care line')
    assert(res['description'] == 'Robert Cribb talks to Young Lee, the founder of Uncle Peter\'s MAN.')
    assert(res['uploader_id'] == '794267642001')
    assert(res['timestamp'] == 1454353482)

# Generated at 2022-06-14 17:07:15.676043
# Unit test for constructor of class TheStarIE

# Generated at 2022-06-14 17:07:25.776364
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()
    assert t._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert t._TEST.get('url') == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert t._TEST.get('md5') == '2c62dd4db2027e35579fefb97a8b6554'
    assert t._TEST.get('info_dict').get('id') == '4732393888001'
    assert t._TEST.get('info_dict').get('ext') == 'mp4'

# Generated at 2022-06-14 17:07:31.920733
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = "http://www.thestar.com/sports/2013/10/05/mike_babcock_says_he_could_have_coached_the_leafs_or_the_red_wings.html"
    instance = TheStarIE(url)
    assert isinstance(instance, TheStarIE)


# Generated at 2022-06-14 17:07:35.566223
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE(None)
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:07:36.522577
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    testVid = TheStarIE()


# Generated at 2022-06-14 17:07:37.557862
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    test_TheStarIE = TheStarIE()


# Generated at 2022-06-14 17:07:44.118237
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    #TheStarIE('https://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

# Generated at 2022-06-14 17:07:47.723296
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s', "Constructor testing"


# Generated at 2022-06-14 17:07:50.607798
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Should be able to create an instance of TheStarIE class
    instance = TheStarIE()
    assert hasattr(instance, '_download_webpage')

# Generated at 2022-06-14 17:07:51.639249
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()



# Generated at 2022-06-14 17:08:02.829760
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.get_title('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    ie.get_title('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')


# Generated at 2022-06-14 17:08:10.546890
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()
# test for __init__(self, url)
    TheStarIE("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")
# test for __init__(self, ie, video_id, display_id)
    TheStarIE("TheStarIE", "4732393888001", "4732393888001")
# test for __init__(self, ie, url, video_id, display_id)
    TheStarIE("TheStarIE", "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html", "4732393888001", "4732393888001")

# Generated at 2022-06-14 17:08:13.669057
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    instance = TheStarIE()
    instance.url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    instance._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')


# Generated at 2022-06-14 17:08:15.935547
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE('test')

# Generated at 2022-06-14 17:08:21.522733
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    # Test successful instantiation of TheStarIE
    TheStarIE(None)

    # Test unsuccessful instantiation of TheStarIE
    try:
        TheStarIE('http://example.com/boo')
        assert False, 'An error should have been raised because invalid video URL'
    except AssertionError:
        pass
    else:
        assert True, 'An error should have been raised because invalid video URL'


# Generated at 2022-06-14 17:08:27.888840
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    '''
    Mainly test whether TheStarIE can detect given url is valid or not
    '''
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    obj = TheStarIE()
    assert obj._VALID_URL == obj._TEST['url']
    assert obj._match_id(obj._TEST['url'])
    valid_url = obj._VALID_URL % {'id': '4732393888001'}
    assert valid_url == url

# Generated at 2022-06-14 17:08:35.024370
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    extractor = TheStarIE()
    assert extractor._match_id('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html') == 'mankind-why-this-woman-started-a-men-s-skincare-line'
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:08:40.380291
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.ie_key() == 'thestar'
    assert ie.ie_key() == 'TheStar'
    # Test display name
    assert ie.title() == 'thestar'
    assert ie.title() == 'TheStar'

# Generated at 2022-06-14 17:08:52.544322
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test the constructor of class TheStarIE
    t = TheStarIE()
    assert t._VALID_URL == 'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert t.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    # Test the __call__ method of class TheStarIE
    test = t._call_the_api('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html', '4732393888001')
    assert test['id'] == '4732393888001'


# Generated at 2022-06-14 17:08:57.753983
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    #Test TheStarIE constructor
    url = "http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html"
    thestar_ie = TheStarIE(True)
    output = thestar_ie._match_id("4732393888001")
    assert output == "4732393888001"


# Generated at 2022-06-14 17:09:05.730477
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE("")

# Generated at 2022-06-14 17:09:06.841773
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    print(type(ie))
    print(ie)

# Generated at 2022-06-14 17:09:16.033480
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.br == None
    assert ie.bl == None
    assert ie.ie == None
    assert ie.fixed_video_url == None
    assert ie.fixed_video_ext == None
    assert ie.fixed_video_format == None
    assert ie.fixed_video_certificate == None
    assert ie.fixed_video_certificate_hash == None
    assert ie.fixed_video_extractor_key == None
    assert ie.fixed_video_preference == None
    assert ie.fixed_video_proxy == None
    assert ie.fixed_video_source_url == None
    assert ie.fixed_video_referer == None
    assert ie.fixed_video_reference == None
    assert ie.fixed_video_format_note == None

# Generated at 2022-06-14 17:09:20.975545
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()._real_extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    TheStarIE().BRIGHTCOVE_URL_TEMPLATE
    TheStarIE()._VALID_URL

# Generated at 2022-06-14 17:09:23.648408
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie is not None

# Generated at 2022-06-14 17:09:28.609220
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Execute
    ie = TheStarIE('http://players.brightcove.net/794267642001/default_default/index.html?videoId=4732393888001')

    # Assert
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:09:31.336788
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # TODO: no unittest for this extractor
    pass


# Generated at 2022-06-14 17:09:39.661907
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'

# Generated at 2022-06-14 17:09:40.362475
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE()

# Generated at 2022-06-14 17:09:42.935176
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = (
        TheStarIE()
    )
    print(obj)

if __name__ == "__main__":
    test_TheStarIE()

# Generated at 2022-06-14 17:10:06.031251
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    extractor = TheStarIE()
    assert (extractor.BRIGHTCOVE_URL_TEMPLATE ==
            'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s')

# Generated at 2022-06-14 17:10:06.834404
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    return TheStarIE()

# Generated at 2022-06-14 17:10:10.877635
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    obj = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert obj.__class__.__name__ == 'TheStarIE'

# Generated at 2022-06-14 17:10:11.352861
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:10:14.806698
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()._real_extract(TheStarIE._TEST['url'])

# Generated at 2022-06-14 17:10:17.298520
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    '''
    Test the constructor of TheStarIE
    '''
    t = TheStarIE()

# Generated at 2022-06-14 17:10:17.882711
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()

# Generated at 2022-06-14 17:10:25.607148
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    video = ie.extract('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert video.url == ie.BRIGHTCOVE_URL_TEMPLATE % '4732393888001'
    assert video.id == '4732393888001'
    assert video.title == 'Mankind: Why this woman started a men\'s skin care line'

# Generated at 2022-06-14 17:10:27.823400
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	ie = TheStarIE(None)
	expect_ie = '<TheStarIE none>'
	assert str(ie) == expect_ie

# Generated at 2022-06-14 17:10:31.124434
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    inst=TheStarIE()
    # test __init__()
    assert inst.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s"


# Generated at 2022-06-14 17:11:09.973330
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    print(ie)
    assert ie is not None

# Generated at 2022-06-14 17:11:17.819871
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    url = "http://sometesturl.com"
    ie = TheStarIE(url)
    assert ie._TEST is None, "Test field not empty"
    assert ie._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html', "Invalid Regex for URL"
    assert ie._downloader is not None, "Downloader not defined"

# Generated at 2022-06-14 17:11:19.181422
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE() # should not raise exception



# Generated at 2022-06-14 17:11:20.114418
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    t = TheStarIE()

# Generated at 2022-06-14 17:11:29.903512
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ''' Constructor tests for class TheStarIE
        Input should be a string containing a valid URL
        The return object must have a group attribute and group 'id'
    '''
    instance = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert instance._VALID_URL == r'https?://(?:www\.)?thestar\.com/(?:[^/]+/)*(?P<id>.+)\.html'
    assert instance._TEST
    assert instance._TEST['url'] == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert instance

# Generated at 2022-06-14 17:11:30.830998
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    TheStarIE()


# Generated at 2022-06-14 17:11:33.549673
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    ie.download("http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html")

# Generated at 2022-06-14 17:11:39.133324
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	ie = TheStarIE()
	assert ie.__class__.__name__ == TheStarIE.__class__.__name__
	assert ie.BRIGHTCOVE_URL_TEMPLATE == TheStarIE.BRIGHTCOVE_URL_TEMPLATE
	assert ie._VALID_URL == TheStarIE._VALID_URL
	# assert ie.IE_NAME == TheStarIE.IE_NAME
	# assert ie.IE_DESC == TheStarIE.IE_DESC
	assert ie._TESTS == TheStarIE._TESTS

# Generated at 2022-06-14 17:11:39.980376
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE("TheStarIE")

# Generated at 2022-06-14 17:11:44.465951
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Create an instance of class TheStarIE
    class_ = TheStarIE
    # Verify it is created successfully
    assert(class_ != None)
    # Verify that a version identifier is set
    version = class_.VERSION
    assert(version != None)
    # Verify that appropriate URL patterns are included
    url_patterns = class_.IE_DESC['ie_key']
    assert(url_patterns != None)
    print("TheStarIE test completed.")

# Generated at 2022-06-14 17:13:20.901256
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
	thestar_instance = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
	assert thestar_instance.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:26.290723
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.ie
    assert ie.BRIGHTCOVE_URL_TEMPLATE
    assert ie._VALID_URL
    assert ie._TEST['url']
    assert ie._TEST['md5']
    assert ie._TEST['info_dict']['id']

# Generated at 2022-06-14 17:13:26.849389
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    return TheStarIE()

# Generated at 2022-06-14 17:13:29.550692
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:36.918257
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    # Test passing a valid YouTube URL
    TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')

    # Test passing an invalid YouTube URL
    with pytest.raises(extractor.ExtractorError):
        TheStarIE('fake_url')


# Generated at 2022-06-14 17:13:43.419981
# Unit test for constructor of class TheStarIE
def test_TheStarIE():

    test_url = TheStarIE._TEST['url']
    test_data = TheStarIE._TEST
    ie = TheStarIE()

    ie.extract(test_url)

    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:46.823449
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    s = TheStarIE()
    assert s.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

# Generated at 2022-06-14 17:13:53.406101
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'

import unittest

# Generated at 2022-06-14 17:13:58.152177
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'

test_TheStarIE()

# Generated at 2022-06-14 17:14:07.270480
# Unit test for constructor of class TheStarIE
def test_TheStarIE():
    ie = TheStarIE('http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')
    assert ie.url == 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    assert ie.display_id == '4732393888001'
    assert ie.md5 == '2c62dd4db2027e35579fefb97a8b6554'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/794267642001/default_default/index.html?videoId=%s'
    assert ie.id