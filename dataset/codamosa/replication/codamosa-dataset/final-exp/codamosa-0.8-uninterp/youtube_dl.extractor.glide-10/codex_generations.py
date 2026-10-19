

# Generated at 2022-06-14 16:13:29.662401
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:13:34.992202
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:13:36.455269
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE(), InfoExtractor)

# Generated at 2022-06-14 16:13:41.684749
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:13:47.410916
# Unit test for constructor of class GlideIE
def test_GlideIE():
    inst = GlideIE()
    assert inst.IE_NAME == 'glide'
    assert inst.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert inst._VALID_URL == "https?://share.glide.me/(?P<id>[A-Za-z0-9\-=_+]+)"

# Generated at 2022-06-14 16:13:49.870519
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.IE_DESC != None
    assert GlideIE._VALID_URL != None
    assert GlideIE._TEST != None

# Generated at 2022-06-14 16:13:52.507057
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == ie.IE_DESC

# Generated at 2022-06-14 16:13:53.974590
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = GlideIE.IE_DESC
    ie = GlideIE(url)
    assert ie.extract(url) == None

# Generated at 2022-06-14 16:13:55.415610
# Unit test for constructor of class GlideIE
def test_GlideIE():
    tester = GlideIE()
    tester.initialize()

# Generated at 2022-06-14 16:13:56.915595
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Unit tests for public functions of class GlideIE

# Generated at 2022-06-14 16:14:02.349741
# Unit test for constructor of class GlideIE
def test_GlideIE():
    an_obj = GlideIE()
    assert isinstance(an_obj, InfoExtractor)

# Generated at 2022-06-14 16:14:14.878478
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Test of GlideIE
    """
    glide_extractor = GlideIE()
    assert glide_extractor.IE_NAME == "glide"
    assert glide_extractor.IE_DESC == "Glide mobile video messages (glide.me)"
    assert glide_extractor._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:23.211126
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:24.877183
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor())

# Generated at 2022-06-14 16:14:36.441144
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None)

    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:14:44.083849
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE(None)
    assert obj.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert obj._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert obj._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert obj._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:14:45.682466
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == GlideIE._VALID_URL

# Generated at 2022-06-14 16:14:54.972577
# Unit test for constructor of class GlideIE
def test_GlideIE():
	# Mock a GlideIE instance
	ie = GlideIE()

	# Assertions
	assert repr(ie) == '<GlideIE: glide.me>'
	assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:55.859508
# Unit test for constructor of class GlideIE
def test_GlideIE():
    x = GlideIE()
    assert x != None

# Generated at 2022-06-14 16:15:09.544840
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == (r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')

# Generated at 2022-06-14 16:15:19.537958
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    # Check that _VALID_URL is valid for _VALID_URL
    assert ie._check_valid_url(ie._VALID_URL)
    # Check that _TEST is valid for _TEST
    assert ie._check_valid_url(ie._TEST['url'])

# Generated at 2022-06-14 16:15:26.683406
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_obj = GlideIE()
    assert test_obj._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert test_obj._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert test_obj._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert test_obj._TEST['info_dict']['ext'] == 'mp4'
    assert test_obj._TEST['info_dict']['title'] == "Damon's Glide message"

# Generated at 2022-06-14 16:15:28.857925
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:15:38.555613
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert ie._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:15:40.693272
# Unit test for constructor of class GlideIE
def test_GlideIE():
	# Test constructor with different inputs
	c = GlideIE(None, None, None)
	assert c.__class__.__name__ == 'GlideIE'

# Generated at 2022-06-14 16:15:43.460094
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC
    ie._VALID_URL
    ie._TEST
    ie._real_extract(ie._TEST['url'])

# Generated at 2022-06-14 16:15:44.674397
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE
    ie = GlideIE()
    assert ie


# Generated at 2022-06-14 16:15:46.929939
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    ie = GlideIE()
    ie.extract(GlideIE._TEST['url'])

# Generated at 2022-06-14 16:15:49.183739
# Unit test for constructor of class GlideIE
def test_GlideIE():
    de  = GlideIE()
    assert_equal(de._VALID_URL, r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')

# Generated at 2022-06-14 16:15:51.191542
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(GlideIE().IE_NAME == "Glide")

# Generated at 2022-06-14 16:16:11.718705
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    webpage = 'http://share.glide.me/' + video_id

    ie = GlideIE()
    ie.url = webpage

    title = ie._html_search_regex(
        r'<title>(.+?)</title>', ie._download_webpage(ie.url, video_id),
        'title', default=None) or ie._og_search_title(ie._download_webpage(ie.url, video_id))

# Generated at 2022-06-14 16:16:23.341435
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie=GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    download_webpage=ie._download_webpage("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==","UZF8zlmuQbe4mr+7dCiQ0w==")
    assert download_webpage!=None
    webInfo=ie._real_extract("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:16:23.986489
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:25.237443
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:27.513364
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:35.014675
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Utility function to test the constructor of class GlideIE."""
    ie = GlideIE()
    ie.IE_DESC = 'Glide mobile video messages (glide.me)'
    ie._VALID_URL = r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:35.633860
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:36.388456
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:38.973380
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') != None


# Generated at 2022-06-14 16:16:41.320612
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")


# Generated at 2022-06-14 16:17:12.498197
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of GlideIE."""
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    glide_ie = GlideIE(url)
    expected_video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert glide_ie.video_id == expected_video_id


# Generated at 2022-06-14 16:17:14.686706
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:17:17.135058
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:17:20.344903
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")



# Generated at 2022-06-14 16:17:30.571446
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Test the constructor of class GlideIE."""
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:17:39.110973
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:39.959723
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('Glide')

# Generated at 2022-06-14 16:17:45.268812
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Validation test for the class constructor of 'GlideIE'"""
    glide = GlideIE()
    assert glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert glide.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide.IE_NAME == 'glide'
    assert glide.BR_DESC == 'Glide'


# Generated at 2022-06-14 16:17:48.938801
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Create instance of class GlideIE
    glide_ie = GlideIE()

    # Verify that the created instance has the expected attributes
    assert(glide_ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')


# Generated at 2022-06-14 16:17:52.951434
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test the Glide mobile video messages (glide.me) IE
    ie = GlideIE()
    assert ie._VALID_URL == GlideIE._VALID_URL
    assert ie._TEST == GlideIE._TEST


# Generated at 2022-06-14 16:19:01.370386
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor)

# Generated at 2022-06-14 16:19:10.463682
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Construction
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

    # Attributes and methods
    assert ie.__class__.__name__ == 'GlideIE'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:19:19.260653
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:19:20.121777
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:19:23.928529
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('glide.glide.me', 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.domain == 'glide.glide.me'
    assert ie.url == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:19:27.601920
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Constructor for GlideIE class
    ie = GlideIE("www.example.com")
    # Unit test for all the methods in the class
    assert ie._real_extract("www.example.com") == "url = www.example.com, id = None"
    assert ie._real_extract("www.example.com/id") == "url = www.example.com, id = id"

test_GlideIE()

# Generated at 2022-06-14 16:19:32.680442
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == "GlideIE"
    assert ie.IE_DESC == "Glide mobile video messages (glide.me)"
    assert ie._VALID_URL == r"https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"


# Generated at 2022-06-14 16:19:40.703374
# Unit test for constructor of class GlideIE
def test_GlideIE():
    import unittest
    class TestGlideIE(unittest.TestCase):
        def setUp(self):
            self.ie = GlideIE()
        def test_object_creation(self):
            self.assertEqual(self.ie.__name__, 'GlideIE')
        def test_ie_key(self):
            self.assertEqual(self.ie.ie_key(), 'Glide')
        def test_info_url(self):
            self.assertEqual(
                self.ie._info_url(''),
                'http://api.glide.me/v1.1/video/url/%s'
            )

# Generated at 2022-06-14 16:19:50.974400
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # url of website to extract information from
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    glide = GlideIE(url)
    # checks if url is valid for glideIE
    assert glide._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"
    # checks if extractor extracts video id as UZF8zlmuQbe4mr+7dCiQ0w==
    assert glide._match_id(url) == "UZF8zlmuQbe4mr+7dCiQ0w=="
    # checks if extractor returns title as Damon's Glide Message
    assert glide._TEST['info_dict']['title']

# Generated at 2022-06-14 16:19:52.438396
# Unit test for constructor of class GlideIE
def test_GlideIE():
	obj = GlideIE()
	print("Constructor of class GlideIE")

# Generated at 2022-06-14 16:22:20.648260
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert (GlideIE._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)")
    assert (GlideIE.IE_DESC == "Glide mobile video messages (glide.me)")
    assert (GlideIE.__name__ == "GlideIE")
    assert (GlideIE.__doc__ == "Glide mobile video messages (glide.me)")

# Generated at 2022-06-14 16:22:21.711869
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert(obj.ie_key() == 'glide')

# Generated at 2022-06-14 16:22:22.837973
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()



# Generated at 2022-06-14 16:22:28.455678
# Unit test for constructor of class GlideIE
def test_GlideIE():
    testClass = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert testClass._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    #print(testClass)


# Generated at 2022-06-14 16:22:32.014905
# Unit test for constructor of class GlideIE
def test_GlideIE():

    # Test constructor of class GlideIE
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:33.149071
# Unit test for constructor of class GlideIE
def test_GlideIE():
    t = GlideIE()
    assert t.IE_NAME == 'Glide'

# Generated at 2022-06-14 16:22:33.687934
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:22:34.609563
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:22:42.697899
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:44.728130
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print(GlideIE)
    # check if the class is defined
    assert (GlideIE is not None)
