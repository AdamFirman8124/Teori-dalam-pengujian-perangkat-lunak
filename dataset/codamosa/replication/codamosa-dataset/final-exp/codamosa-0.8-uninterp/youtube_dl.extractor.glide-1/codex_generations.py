

# Generated at 2022-06-14 16:13:32.153625
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_dict = {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'md5': '4466372687352851af2d131cfaa8a4c7',
        'info_dict': {
        	'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
        	'ext': 'mp4',
        	'title': "Damon's Glide message",
        	'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
        }
    }
    test_glideIE = GlideIE(test_dict)

# Generated at 2022-06-14 16:13:35.342149
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC
    ie._VALID_URL
    ie._TEST


# Generated at 2022-06-14 16:13:36.415396
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor())


# Generated at 2022-06-14 16:13:38.379457
# Unit test for constructor of class GlideIE
def test_GlideIE():
    o = GlideIE()
    assert o.IE_DESC is not None
    assert o._VALID_URL is not None

# Generated at 2022-06-14 16:13:46.231199
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:57.734745
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="

# Generated at 2022-06-14 16:14:01.930688
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie.VALID_URL == _VALID_URL
    assert ie.TEST == _TEST

# Generated at 2022-06-14 16:14:09.110889
# Unit test for constructor of class GlideIE
def test_GlideIE():
	glide_ie = GlideIE()
	glide_ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
	glide_ie.extract('http://share.glide.me/4b4OiK2H__1Rlk1SxIk_qA==')

# Generated at 2022-06-14 16:14:10.599979
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Tests that an instance of the class can be created
    GlideIE()

# Generated at 2022-06-14 16:14:21.696425
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .common import TestVideoIE
    from .common import mock


# Generated at 2022-06-14 16:14:27.118013
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Unit test for constructor
    assert GlideIE(None).IE_NAME == 'glide'

# Generated at 2022-06-14 16:14:32.231634
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE("", "", "")._real_extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:14:32.890069
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:43.344494
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert ie._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:14:53.100952
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(GlideIE.ie_key(), GlideIE._VALID_URL)
    assert ie.ie_key() == 'Glide'
    assert ie._VALID_URL == r'https?://[^/]+/[A-Za-z0-9\-=_+]+'

# Generated at 2022-06-14 16:14:54.022448
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor())

# Generated at 2022-06-14 16:14:54.860512
# Unit test for constructor of class GlideIE
def test_GlideIE():
	GlideIE()


# Generated at 2022-06-14 16:14:56.018042
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None).IE_NAME == "Glide"


# Generated at 2022-06-14 16:14:59.162586
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC
    ie.IE_NAME
    ie._VALID_URL
    ie.__class__
    ie.test()

# Generated at 2022-06-14 16:15:03.041534
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.template

# Generated at 2022-06-14 16:15:06.860201
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Unit test for the constructor of class GlideIE.
    """
    glide_obj = GlideIE()
    assert glide_obj.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:15:12.331891
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    # Test accessing the URL
    ie.download("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    

# Generated at 2022-06-14 16:15:13.729706
# Unit test for constructor of class GlideIE
def test_GlideIE():
    my_video = GlideIE()
    assert my_video is not None

# Generated at 2022-06-14 16:15:14.912750
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None)


# Generated at 2022-06-14 16:15:23.349657
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:15:28.738295
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:38.250692
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE();

# Generated at 2022-06-14 16:15:40.555297
# Unit test for constructor of class GlideIE
def test_GlideIE():
	"""
	Used to test the constructor of class GlideIE
	"""
	assert(GlideIE(GlideIE._TEST).extract_urls() == GlideIE._TEST)

# Generated at 2022-06-14 16:15:49.610085
# Unit test for constructor of class GlideIE
def test_GlideIE():
    '''
    Create an extractor unit test for GlideIE
    '''

    # Create a fake test video
    import uuid
    video_id = str(uuid.uuid4())
    title = "Damon's Glide Message"

    # Create the test url
    url = "http://share.glide.me/" + video_id

    # Add the test video to the test video dictionary
    test_video = GlideIE._TEST
    test_video['url'] = url
    test_video['md5'] = str(uuid.uuid4())
    test_video['info_dict']['id'] = video_id
    test_video['info_dict']['title'] = title

    # Create an extractor for the test video
    extractor = GlideIE(test_video)

    # Test

# Generated at 2022-06-14 16:15:50.908371
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:15:56.832901
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:57.444918
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:58.104246
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert GlideIE()

# Generated at 2022-06-14 16:16:08.546654
# Unit test for constructor of class GlideIE
def test_GlideIE():
	glide = GlideIE()
	assert_equal(glide.ie_key(), 'Glide')
	assert_equal(glide.ie_desc(), 'Glide mobile video messages (glide.me)')
	#assert_equal(glide.valid_url(), 'https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
	assert_equal(glide.working, True)
	assert_equal(glide.extractor_key(), 'Glide')
	assert_equal(glide.__getattribute__('IE_DESC'), 'Glide mobile video messages (glide.me)')

# Generated at 2022-06-14 16:16:14.750326
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Checks constructor of GlideIE class
    """
    _ = GlideIE()
    # Check that this class is available
    info_extractor = _.suitable([{'url': 'https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'only_matching': True}])
    assert info_extractor is not None

# Generated at 2022-06-14 16:16:25.546687
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE._TEST == {'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'md5': '4466372687352851af2d131cfaa8a4c7', 'info_dict': {'id': 'UZF8zlmuQbe4mr+7dCiQ0w==', 'ext': 'mp4', 'title': "Damon's Glide message", 'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$'}}


# Generated at 2022-06-14 16:16:27.258609
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie


# Generated at 2022-06-14 16:16:28.836456
# Unit test for constructor of class GlideIE
def test_GlideIE():
    return GlideIE("GlideIE", "Glide mobile video messages (glide.me)")

# Generated at 2022-06-14 16:16:31.615890
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Constructor test
    """
    ie = GlideIE(GlideIE.ie_key())
    assert ie.ie_key() == 'Glide'
    assert ie.IE_NAME == 'glide'

# Generated at 2022-06-14 16:16:36.575287
# Unit test for constructor of class GlideIE
def test_GlideIE():
	ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
	assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
	assert type(ie) == GlideIE


# Generated at 2022-06-14 16:16:54.999874
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test 1
    test1 = [
        # input
        "‪http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==‬",
        # expected output
        "UZF8zlmuQbe4mr+7dCiQ0w=="
        ]
    # Initialize instance of class GlideIE
    glideIE = GlideIE()
    # Test _match_id() method.
    assert glideIE._match_id(test1[0]) == test1[1]



# Generated at 2022-06-14 16:16:56.065766
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    pass

# Generated at 2022-06-14 16:16:57.645340
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert ctor_GlideIE()

# Generated at 2022-06-14 16:16:59.414745
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:17:07.055177
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:15.697649
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    This test shows the correct behavior in cases that
    the constructor returns None (nothing is returned)
    and cases that an instance is returned.
    """

    # Testing that the constructor return None
    # when the video_id is not found.
    assert(None == GlideIE.suitable(None))
    assert(None == GlideIE.suitable("https://www.youtube.com/watch?v=bvL-_Dxy2ts"))

    # Testing that the constructor return an instance
    # of class GlideIE.
    res = GlideIE.suitable("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert(isinstance(res, GlideIE))

# Generated at 2022-06-14 16:17:23.461253
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE('Glide', 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert obj.name == 'Glide'
    assert obj._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert obj.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:17:25.116985
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE(InfoExtractor())
    assert obj != None


# Generated at 2022-06-14 16:17:34.170327
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'http://www.youtube.com/watch?v=BaW_jenozKc')
    assert ie is not None
    print (ie.IE_DESC)
    #assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.IE_NAME == 'glide'
    assert ie.ie_key() == 'Glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.ie_key() == 'Glide'
    ie.ie_key()
    ie.ie_key()


# Generated at 2022-06-14 16:17:34.653582
# Unit test for constructor of class GlideIE
def test_GlideIE():
	GlideIE()

# Generated at 2022-06-14 16:18:13.682549
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE()
    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide_ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:17.299590
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test = GlideIE()
    test_str = "Unit test for GlideIE"
    assert not(test is None), test_str + ": Did not create object"

# Generated at 2022-06-14 16:18:18.519605
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Create a new instance of the class
    GlideIE()


# Generated at 2022-06-14 16:18:19.088348
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:18:25.406617
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ieUrl = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    html = urlopen(ieUrl).read().decode('utf-8')
    video = ie.extract(ieUrl)
    assert video.keys() == ['id', 'uploader', 'ext', 'title', 'thumbnail', 'url', 'timestamp', 'upload_date', 'view_count']

# Generated at 2022-06-14 16:18:31.019417
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

    # This is a sample URL.
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    instance = ie.url_result(url)
    id = ie._match_id(url)
    assert id == 'UZF8zlmuQbe4mr+7dCiQ0w=='

    # This is a sample URL.
    url = "http://ab.cd"
    id = ie._match_id(url)
    assert id == ''

# Generated at 2022-06-14 16:18:42.057515
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:43.715174
# Unit test for constructor of class GlideIE
def test_GlideIE():
    s = GlideIE()
    assert(s.IE_DESC == 'Glide mobile video messages (glide.me)')

# Generated at 2022-06-14 16:18:53.159680
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert(ie.IE_NAME == "Glide.me")
    assert(ie.IE_DESC == "Glide mobile video messages")
    assert(ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')

# Generated at 2022-06-14 16:18:57.000496
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:19:57.718723
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().IE_NAME == 'glide'
    assert GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE()._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:19:59.197923
# Unit test for constructor of class GlideIE
def test_GlideIE(): 
    GlideIE(InfoExtractor())

# Generated at 2022-06-14 16:20:04.398876
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(False)
    info = ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert info['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert info['ext'] == 'mp4'
    assert info['title'] == "Damon's Glide message"
    assert info['thumbnail'].startswith('https://')


# Generated at 2022-06-14 16:20:05.545814
# Unit test for constructor of class GlideIE
def test_GlideIE():
    this_ie = GlideIE()
    assert isinstance(this_ie, InfoExtractor)

# Generated at 2022-06-14 16:20:09.014546
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('Glide Mobile Video Messages (glide.me)',
        'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:20:10.238985
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("Test")


# Generated at 2022-06-14 16:20:18.980924
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("GlideIE")
    print(repr(ie))
    assert ie.IE_NAME == "GlideIE"
    assert ie.IE_DESC == "Glide mobile video messages (glide.me)"
    assert ie._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"
    assert ie._TEST.get("url") == "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    assert ie._TEST.get("md5") == "4466372687352851af2d131cfaa8a4c7"

# Generated at 2022-06-14 16:20:19.809866
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor())

# Generated at 2022-06-14 16:20:22.830899
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie.IE_NAME == 'Glide'

# Generated at 2022-06-14 16:20:31.978005
# Unit test for constructor of class GlideIE
def test_GlideIE():
	print('Test constructor of class GlideIE')
	assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
	assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:35.792981
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:22:41.793143
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

    # There is not a unit test for each of these test cases.
    # Instead, the overall unit test is integrated. Thankful to that,
    # this GlideIE test is not longer than 4 lines.
    assert ie.IE_NAME in ie._FAILED_URL_PATTERN
    assert ie._VALID_URL in ie._TEST
    assert ie._TEST['url'] in ie._VALID_URL
    assert ie._TEST['md5'] == ie._real_extract(ie._TEST['url'])['md5']

# Generated at 2022-06-14 16:22:43.029524
# Unit test for constructor of class GlideIE
def test_GlideIE():
	info_extractor = GlideIE(None)

# Generated at 2022-06-14 16:22:45.795981
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert GlideIE(GlideIE.ie_key(), GlideIE._TEST['url']).result['md5'] == GlideIE._TEST['md5']

test_GlideIE()

# Generated at 2022-06-14 16:22:54.768036
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info_extractor = GlideIE()
    assert info_extractor.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert info_extractor._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert info_extractor._downloader is None
    assert info_extractor.params is None
    assert info_extractor._connection is None
    assert info_extractor._available_formats == []
    assert info_extractor._formats == []
    assert info_extractor._sort_formats is None

# Generated at 2022-06-14 16:23:00.702753
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert isinstance(ie, InfoExtractor)
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:23:08.154428
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(GlideIE(None).IE_NAME == 'glide')
    assert(GlideIE(None).IE_DESC == 'Glide mobile video messages (glide.me)')
    assert(GlideIE(None)._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')

# Generated at 2022-06-14 16:23:11.788258
# Unit test for constructor of class GlideIE
def test_GlideIE():
	try:
		global tester
		tester = GlideIE()
		print("Unit test for GlideIE.py is complete!")
	except:
		print("Error in unit test for GlideIE.py!")


# Generated at 2022-06-14 16:23:12.936034
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('test', True).test()

# Generated at 2022-06-14 16:23:21.306737
# Unit test for constructor of class GlideIE
def test_GlideIE():
	import os
	from .common import test_glide
	from .common import InfoExtractor

	GlideIE = test_glide.GlideIE()
	assert(GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)')
	assert(GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
	assert(GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
	assert(GlideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7')