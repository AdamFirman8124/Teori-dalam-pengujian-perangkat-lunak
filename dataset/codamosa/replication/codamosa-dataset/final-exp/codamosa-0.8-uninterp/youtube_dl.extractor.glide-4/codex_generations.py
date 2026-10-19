

# Generated at 2022-06-14 16:13:28.381250
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    url = 'http://share.glide.me/{}'.format(video_id)
    glide = GlideIE(None)
    assert glide._match_id(url) == video_id

# Generated at 2022-06-14 16:13:33.670512
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:13:36.201317
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert 'GlideIE' in ie.__class__.__name__


# Generated at 2022-06-14 16:13:37.389135
# Unit test for constructor of class GlideIE
def test_GlideIE():
    import inspect
    assert inspect.isclass(GlideIE)

# Generated at 2022-06-14 16:13:39.729601
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:13:46.657815
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_glide_url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    video_glide_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    video_glide_md5 = '4466372687352851af2d131cfaa8a4c7'
    video_glide_title = "Damon's Glide message"
    video_glide_thumb_url = 'http://d2o906d8ln7ui1.cloudfront.net/photo/ae55fc_620x0_0-0-0.jpg'

# Generated at 2022-06-14 16:13:48.187922
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.ie_key() == "glide"

# Generated at 2022-06-14 16:13:48.913208
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:13:49.553527
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:13:52.560722
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("https://share.glide.me/7xlNdGpw7Dq8Nq3KjX9Q2Q==")

# Generated at 2022-06-14 16:13:56.556925
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()

# Generated at 2022-06-14 16:13:57.368226
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:13:59.573632
# Unit test for constructor of class GlideIE
def test_GlideIE():
    i = GlideIE()
    return i.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:02.086515
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_obj = GlideIE()
    assert test_obj is not None


# Generated at 2022-06-14 16:14:02.768941
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:15.247429
# Unit test for constructor of class GlideIE
def test_GlideIE():
	g = GlideIE("<unittest>", "")
	assert g.IE_DESC == "Glide mobile video messages (glide.me)"
	assert g._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
	assert g._TEST['url'] == "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
	assert g._TEST['md5'] == "4466372687352851af2d131cfaa8a4c7"

# Generated at 2022-06-14 16:14:23.322418
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:14:30.575099
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Simple testcase for GlideIE class
    """
    ie = GlideIE()

    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:41.098518
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None)

    # Test regular expression matching
    assert  ie._match_id('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert  ie._match_id('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert  ie._match_id('http://share.glide.me/UZF8zlmuQbe4mr-7dCiQ0w==') == 'UZF8zlmuQbe4mr-7dCiQ0w=='

# Generated at 2022-06-14 16:14:46.466066
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.IE_NAME == 'glide'

# Generated at 2022-06-14 16:14:54.671925
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:14:56.130542
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Constructor test
    """
    glide_ie = GlideIE()
    assert glide_ie

# Generated at 2022-06-14 16:14:57.718780
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print('Testing GlideIE constructor')
    instance = GlideIE('')
    assert(isinstance(instance, GlideIE))
    

# Generated at 2022-06-14 16:15:01.099986
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    ie = GlideIE()
    assert ie.expected_format() == 'mp4'
    assert ie.expected_type() == 'video'

# Generated at 2022-06-14 16:15:04.173697
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:15:07.809203
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_obj = GlideIE({})
    assert test_obj.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:15:10.794499
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:20.255419
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:24.926158
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert(GlideIE()._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
	assert(GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)')

# Test case for _real_extract()

# Generated at 2022-06-14 16:15:25.912877
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None, None)

# Generated at 2022-06-14 16:15:39.957011
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:15:41.783840
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video = GlideIE(None)
    video.constructor_test()


# Generated at 2022-06-14 16:15:43.166146
# Unit test for constructor of class GlideIE
def test_GlideIE():
	ie = GlideIE()
	assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:15:47.678911
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE.
    """
    glide = GlideIE()._real_initialize()
    assert glide.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:00.373280
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('glide') == GlideIE('glide')
    assert GlideIE('glide') != GlideIE('youtube')
    assert GlideIE('youtube') != GlideIE('glide')
    assert GlideIE('glide') != GlideIE('glide', 'params')
    assert GlideIE('glide', 'params') != GlideIE('glide', 'params')
    assert GlideIE('glide', 'params') != GlideIE('glide', 'params2')
    assert GlideIE('glide', 'params2') != GlideIE('glide', 'params')
    assert GlideIE('youtube') != GlideIE('youtube', 'params')
    assert GlideIE('youtube', 'params') != GlideIE('youtube', 'params2')

# Generated at 2022-06-14 16:16:05.655525
# Unit test for constructor of class GlideIE
def test_GlideIE():
    testcases = [('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==','UZF8zlmuQbe4mr+7dCiQ0w==')]
    for testcase,expected in testcases:
        assert GlideIE.__init__(url=testcase) == expected

# Generated at 2022-06-14 16:16:12.730573
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.LANG == 'en'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.SITE_NAME == 'glide.me'
    assert ie.SUFFIX == '.glide.me'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:15.012653
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:16:26.254281
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert GlideIE.suitable('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert GlideIE._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:16:26.797644
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:59.501307
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:17:03.666260
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'



# Generated at 2022-06-14 16:17:14.560939
# Unit test for constructor of class GlideIE
def test_GlideIE():

    assert GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==") is not None
    assert GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==") is not None
    assert GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==/") is not None
    assert GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==/ ") is not None
    assert GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==?") is not None


# Generated at 2022-06-14 16:17:26.599951
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert GlideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:17:35.841314
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    # one way to set the information for each instance
    ie._VALID_URL = 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:36.329634
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:17:44.204441
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE()
    assert glide_ie.ie_key() == 'Glide'
    assert glide_ie.ie_desc() == 'Glide mobile video messages (glide.me)'
    assert glide_ie.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert not glide_ie.suitable('http://not-valid-url.com/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert glide_ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:46.282125
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .common import GlideIE
    from .common import InfoExtractor
    # Case: class GlideIE derives from class InfoExtractor
    assert issubclass(GlideIE,InfoExtractor) == True

# Generated at 2022-06-14 16:17:47.481281
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().ie_key() == 'Glide'

# Generated at 2022-06-14 16:17:48.394623
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('glide.me').IE_NAME == 'glide'

# Generated at 2022-06-14 16:19:04.233824
# Unit test for constructor of class GlideIE
def test_GlideIE():
    '''
    This test simply ensures that the constructor of GlideIE works properly
    '''

    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:19:04.742078
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:07.350545
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE()
    except TypeError:
        print("Constructor of class GlideIE throws an TypeError")
        return False
    return True



# Generated at 2022-06-14 16:19:11.134332
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .common import TestCase

    class TestGlideIE(TestCase):
        def assertIdEquals(self, url, expected):
            ie = GlideIE(GlideIE._build_request(url))
            self.assertEqual(ie.result['id'], expected)

    TestGlideIE('test_glide_ie').run()

# Generated at 2022-06-14 16:19:13.289296
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glideIE = GlideIE()
    assert glideIE.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:19:14.143242
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:19:14.975762
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie != None

# Generated at 2022-06-14 16:19:19.960106
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:19:22.601309
# Unit test for constructor of class GlideIE
def test_GlideIE():
    name_for_test = "GlideIE"
    make_test_instance_with_assert(GlideIE, name_for_test)

# Generated at 2022-06-14 16:19:25.421895
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test constructor without video URL
    assert GlideIE() is not None
    # Test constructor with video URL
    assert GlideIE(None, 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') is not None

# Generated at 2022-06-14 16:22:03.576082
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:22:07.674368
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert(obj._VALID_URL == GlideIE._VALID_URL)
    assert(obj.IE_DESC == GlideIE.IE_DESC)
    assert(obj._TEST == GlideIE._TEST)


# Generated at 2022-06-14 16:22:08.556914
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

test_GlideIE()

# Generated at 2022-06-14 16:22:10.314978
# Unit test for constructor of class GlideIE
def test_GlideIE():
    class_obj = GlideIE(None)
    assert isinstance(class_obj, GlideIE)

# Generated at 2022-06-14 16:22:12.639673
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None)
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 16:22:21.499297
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_NAME == 'glide:share'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:22:26.851268
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == ie_Glide._VALID_URL
    assert ie._TEST == ie_Glide._TEST
    assert ie.IE_DESC == ie_Glide.IE_DESC
    assert ie._real_extract == ie_Glide._real_extract

# Generated at 2022-06-14 16:22:29.232814
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Tests constructor without exception
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:22:31.082255
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("www.glide.me")

# Generated at 2022-06-14 16:22:32.609157
# Unit test for constructor of class GlideIE
def test_GlideIE():
    x = GlideIE()
    assert ('share.glide.me' in x.ie_key()) == True