

# Generated at 2022-06-14 16:13:33.758351
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Tests whether the class constructor works correctly
    # Test: Video URL
    video_url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    test_url = GlideIE(video_url)
    assert test_url.video_url == video_url
    assert test_url._TEST['url'] == test_url.video_url

test_GlideIE()


# Generated at 2022-06-14 16:13:43.984849
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:47.479888
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    GlideIE(None)._downloader.troubleshoot()

# Generated at 2022-06-14 16:13:58.579343
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE()
    assert glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:08.395859
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # This is a test to see if GlideIE is constructed correctly
    glide_ie1 = GlideIE()

    # Assert that glide_ie1 has the correct properties
    assert glide_ie1._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert glide_ie1.IE_NAME == 'glide'
    assert glide_ie1.IE_DESC == 'Glide mobile video messages (glide.me)'



# Generated at 2022-06-14 16:14:08.943505
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE()
    assert glide_ie

# Generated at 2022-06-14 16:14:11.815391
# Unit test for constructor of class GlideIE
def test_GlideIE():
	info = {
		'IE_DESC': 'Glide mobile video messages (glide.me)',
	}
	assert isinstance(info, GlideIE)

# Generated at 2022-06-14 16:14:15.765269
# Unit test for constructor of class GlideIE
def test_GlideIE():
	t = GlideIE()
	assert isinstance(t, object)

# Generated at 2022-06-14 16:14:18.038049
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print("test_GlideIE")
    ie = GlideIE()
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 16:14:23.192091
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == "Glide"
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:14:32.477365
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()._VALID_URL == GlideIE._VALID_URL
    assert GlideIE().IE_DESC == GlideIE._TEST['info_dict']['title']
    assert GlideIE()._TEST['url'] == GlideIE._TEST['url']

# Generated at 2022-06-14 16:14:40.594971
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Unit test for constructor of class GlideIE
    """
    glide = GlideIE()
    assert glide.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:41.681870
# Unit test for constructor of class GlideIE
def test_GlideIE():
    object = GlideIE()
    assert object.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:42.800185
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert instance.IE_NAME == 'Glide'

# Generated at 2022-06-14 16:14:52.699654
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:53.171480
# Unit test for constructor of class GlideIE
def test_GlideIE():
    return GlideIE()

# Generated at 2022-06-14 16:14:54.389054
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    return ie.IE_DESC

# Generated at 2022-06-14 16:14:56.748114
# Unit test for constructor of class GlideIE
def test_GlideIE():
    class_ = GlideIE
    instance = class_()
    instance.ie_key() == 'Glide'
    instance.ie_desc() == 'Glide mobile video messages (glide.me)'



# Generated at 2022-06-14 16:15:09.878522
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test a valid GlideIE link
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    GlideIE('http://www.share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    GlideIE('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    GlideIE('https://www.share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    GlideIE('https://share.glide.me/keep-it-up')
    GlideIE('https://share.glide.me/keep-it-up?foo=bar')

# Generated at 2022-06-14 16:15:12.558444
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert hasattr(ie, '_VALID_URL'), 'GlideIE._VALID_URL must be set'

# Generated at 2022-06-14 16:15:26.111120
# Unit test for constructor of class GlideIE
def test_GlideIE():
	ie = GlideIE()
	assert ie is not None


# Generated at 2022-06-14 16:15:33.077790
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._TEST["info_dict"]["title"] == "Damon's Glide message"
    assert GlideIE._TEST["info_dict"]["url"] == 'https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==.mp4'
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:36.458139
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """ Testing GlideIE constructor """

    info_extractor = GlideIE()
    assert info_extractor._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:37.341194
# Unit test for constructor of class GlideIE
def test_GlideIE():
    tst = GlideIE()
    assert tst

# Generated at 2022-06-14 16:15:39.153175
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor())._download_webpage("http://share.glide.me")



# Generated at 2022-06-14 16:15:41.925220
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Selected unit test for constructor of class GlideIE
    """
    ie = GlideIE()
    ie.extract(r'https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:45.694477
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert isinstance(ie, GlideIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:46.498372
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()

# Generated at 2022-06-14 16:15:48.204079
# Unit test for constructor of class GlideIE
def test_GlideIE():
    x = GlideIE()

    # check if the class GlideIE is instantiated properly
    assert(x.IE_NAME)

# Generated at 2022-06-14 16:15:49.150934
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor)


# Generated at 2022-06-14 16:16:10.044443
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info = GlideIE()._get_info( "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==" )
    assert( info['title'] == "Damon's Glide message" )
    assert( info['duration'] == 9 )
    assert( info['url'] == 'http://g.glide.me/media/UZF8zlmuQbe4mr+7dCiQ0w==' )
    assert( info['thumbnail'] == 'http://d.glide.me/thumbs/UZF8zlmuQbe4mr+7dCiQ0w==.jpg' )
    # TODO add more tests

# Generated at 2022-06-14 16:16:10.887257
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:16:12.849035
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:16:13.998745
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor(None))

# Generated at 2022-06-14 16:16:25.124932
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test = {'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
            'match': 'GlideIE'}
    url, match = test['url'], test['match']
    ie = eval("{0}('{1}')".format(match, url))
    video_id = ie._match_id(ie.url)
    webpage = ie._download_webpage(ie.url, video_id)
    title = ie._html_search_regex(
        r'<title>(.+?)</title>', webpage,
        'title', default=None) or ie._og_search_title(webpage)

# Generated at 2022-06-14 16:16:28.796473
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Test to verify that the GlideIE constructor behaves correctly.
    """
    # Check that GlideIE is a subclass of InfoExtractor
    assert issubclass(GlideIE, InfoExtractor), \
        'GlideIE is not a subclass of InfoExtractor.'


# Generated at 2022-06-14 16:16:35.242531
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("https://example.com/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie._get_id("https://example.com/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie._real_extract("https://example.com/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie._match_id("https://example.com/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:16:43.789989
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:16:51.533949
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie.IE_NAME == 'glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:16:55.175452
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert instance.IE_NAME == "Glide"
    assert instance.IE_DESC
    assert instance._VALID_URL
    assert instance.__name__ == "GlideIE"
    assert instance.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:17:31.283429
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("")
    assert ie.IE_DESC == "Glide mobile video messages (glide.me)"
    assert ie._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"

# Generated at 2022-06-14 16:17:31.832390
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:17:34.727184
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(GlideIE.IE_DESC, GlideIE._VALID_URL)
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:41.275849
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print('Test constructor of GlideIE')
    glide_ie = GlideIE()
    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide_ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:48.585511
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Testing constructor of class GlideIE"""
    # Pexpect uses many print statements, so disable them temporarily
    import sys
    #reload(sys)
    #sys.setdefaultencoding("utf-8")
    sys.stdout = open("/dev/null", 'w')
    
    from .common import InfoExtractor
    from .glide import GlideIE
    import youtube_dl.extractor.common
    import pexpect
    import os
    import os.path
    import urllib.request

    ydl = youtube_dl.YoutubeDL({'outtmpl': os.path.join(os.getcwd(), '%(id)s.%(ext)s')})
    
    
    # Create instance of InfoExtractor class
    # Expect it to be instance of GlideIE class
    info_

# Generated at 2022-06-14 16:17:59.001090
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:17:59.534805
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:18:05.588367
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE._TEST == {'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'md5': '4466372687352851af2d131cfaa8a4c7', 'info_dict': {'id': 'UZF8zlmuQbe4mr+7dCiQ0w==', 'ext': 'mp4', 'title': "Damon's Glide message", 'thumbnail': 're:^https?://.*?\\.cloudfront\\.net/.*\\.jpg$'}}


# Generated at 2022-06-14 16:18:10.622788
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.ie_key()
    ie.ie_desc()
    ie.valid_url()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:18:11.979469
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'


# Generated at 2022-06-14 16:19:21.431144
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:19:24.130305
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_url ='http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    glide_ie = GlideIE(InfoExtractor())
    glide_ie._real_extract(video_url)

# Generated at 2022-06-14 16:19:24.585747
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:25.576883
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # unit test for class GlideIE
    assert GlideIE is not None

# Generated at 2022-06-14 16:19:27.663192
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['title'] == "Damon's Glide message"

# Generated at 2022-06-14 16:19:28.257478
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:31.759966
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert not GlideIE.suitable('http://fanart.tv')

# Generated at 2022-06-14 16:19:33.757765
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE(None, None)
    except Exception:
        print >> sys.stderr, "Couldn't instance object GlideIE"

# Generated at 2022-06-14 16:19:34.576314
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None) is not None

# Generated at 2022-06-14 16:19:42.398584
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:13.268580
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_url = GlideIE._TEST.get('url')
    assert test_url, 'url should not be empty'
    assert GlideIE._TEST.get('md5') == GlideIE()._real_extract(test_url).get('md5'), 'md5 of video should be same'

# Generated at 2022-06-14 16:22:16.034640
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract("http://www.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:22:18.190128
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:20.354520
# Unit test for constructor of class GlideIE
def test_GlideIE():
    global ie
    try:
        ie = GlideIE()
    except:
        assert False, 'Cannot instantiate GlideIE'
    assert ie



# Generated at 2022-06-14 16:22:21.164714
# Unit test for constructor of class GlideIE
def test_GlideIE():
    i = GlideIE()

# Generated at 2022-06-14 16:22:32.572394
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    info = GlideIE().extract(url)

    assert info['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert info['title'] == "Damon's Glide message"
    assert info['url'] == 'https://s3-us-west-2.amazonaws.com/video.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==/video.mp4'

# Generated at 2022-06-14 16:22:35.065872
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC
    assert ie._VALID_URL
    assert ie._TEST

# Generated at 2022-06-14 16:22:39.205206
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:39.762862
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:22:44.533699
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        # Create instance of class GlideIE
        GlideIE()
    except Exception as e:
        print('test_GlideIE failed:')
        print(e)
# #################################################################
# ################### Unit tests ################################
# #################################################################
