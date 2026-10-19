

# Generated at 2022-06-14 16:13:30.059160
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:32.900992
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from test_suite import assert_equals

    # GlideIE(InfoExtractor) constructor
    assert_equals('GlideIE', GlideIE.__name__)

# Generated at 2022-06-14 16:13:43.590177
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._TEST['url'] == "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    assert GlideIE._TEST['md5'] == "4466372687352851af2d131cfaa8a4c7"
    # info dict
    assert GlideIE._TEST['info_dict']['id'] == "UZF8zlmuQbe4mr+7dCiQ0w=="
    assert GlideIE._TEST['info_dict']['ext'] == "mp4"
    assert GlideIE._TEST['info_dict']['title'] == "Damon's Glide message"

# Generated at 2022-06-14 16:13:47.241686
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.constructor_test_for_type(GlideIE)

# Generated at 2022-06-14 16:13:58.429444
# Unit test for constructor of class GlideIE
def test_GlideIE():
	ie = GlideIE()
	assert ie.IE_NAME == 'GlideIE' 
	assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
	assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:11.815822
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:19.715706
# Unit test for constructor of class GlideIE
def test_GlideIE():
  # pylint: disable=C0103
  class Output:
    ie_desc = GlideIE.IE_DESC
    valid_url = GlideIE._VALID_URL
    _TEST = GlideIE._TEST
  assert(isinstance(Output(), Output))
  print("PASSED: Unit test for constructor of class GlideIE")

if __name__ == '__main__':
    test_GlideIE()

# Generated at 2022-06-14 16:14:20.698252
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(False)

# Generated at 2022-06-14 16:14:25.253098
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == "Glide"
    assert ie.IE_DESC == "Glide mobile video messages (glide.me)"
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:14:26.373909
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(True)

# Generated at 2022-06-14 16:14:30.883595
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:31.968231
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None)

# Generated at 2022-06-14 16:14:40.031539
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("GlideIE", "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==", {'json': {'auto': 'False', 'background': '#FFFFFF'}, 'title': 'Damon', 'ext': 'mp4', 'id': 'UZF8zlmuQbe4mr+7dCiQ0w==', 'thumbnail': 're:^https?://.*?\.cloudfront\.net/.*\.jpg$'}, '4466372687352851af2d131cfaa8a4c7')

# Generated at 2022-06-14 16:14:49.281002
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    assert(GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(GlideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7')
    assert(GlideIE._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(GlideIE._TEST['info_dict']['ext'] == 'mp4')

# Generated at 2022-06-14 16:14:53.240246
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:15:00.202885
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert GlideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert GlideIE._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert GlideIE._TEST['info_dict']['ext'] == 'mp4'
    assert GlideIE._TEST['info_dict']['title'] == "Damon's Glide message"

# Generated at 2022-06-14 16:15:13.283319
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:16.265835
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    GlideIE().suitable(video_url)

# Generated at 2022-06-14 16:15:21.174296
# Unit test for constructor of class GlideIE
def test_GlideIE():
  # Tests the constructor of GlideIE class
  #       _VALID_URL = r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
  assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:15:24.216471
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor)._real_extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:15:33.553020
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract(
    'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    )
    print(ie.title)

# Generated at 2022-06-14 16:15:41.208694
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE("share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert glide.ie_key() == "Glide", "Name of IE instance is not correct"
    assert glide.ie_desc() == "Glide mobile video messages (glide.me)",  "IE description is not correct"
    assert glide.valid_url("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="), "URL is not valid"
    assert not glide.valid_url("https://share.glide.me/"), "URL is valid, but should not be"
    assert glide._match_id("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:15:45.928236
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().IE_NAME == 'glide'
    assert GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE()._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:15:48.546342
# Unit test for constructor of class GlideIE
def test_GlideIE():
    gl = GlideIE(None)
    assert gl.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')


# Generated at 2022-06-14 16:15:59.349080
# Unit test for constructor of class GlideIE
def test_GlideIE():
    import unittest

    # Constructor of class GlideIE
    class TestGlideIE(unittest.TestCase):
        def setUp(self):
            self.glide = GlideIE('GlideIE')

        def test_sucess(self):
            self.assertEqual(self.glide.IE_NAME, 'GlideIE')
            self.assertEqual(self.glide.IE_DESC, 'Glide mobile video messages (glide.me)')

    suite = unittest.TestLoader().loadTestsFromTestCase(TestGlideIE)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-14 16:16:09.141919
# Unit test for constructor of class GlideIE
def test_GlideIE():
	print("Testing constructor of class GlideIE")
	url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
	assert(GlideIE().suitable(url))
	url = 'http://share.glide.me'
	assert(not GlideIE().suitable(url))
	url = 'https://share.glide.me/hello'
	assert(GlideIE().suitable(url))
	url = 'http://notshare.glide.me/hello'
	assert(not GlideIE().suitable(url))
	url = 'https://glide.me'
	assert(not GlideIE().suitable(url))
	print("Class constructor passed all cases")


# Generated at 2022-06-14 16:16:10.690373
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    # The GlideIE object can't be constructed with an invalid URL
    assert ie.working

# Generated at 2022-06-14 16:16:11.209217
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:17.416915
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')._match_id('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:16:19.767601
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(False)
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:16:41.813330
# Unit test for constructor of class GlideIE
def test_GlideIE():

    from yt_dl_api.yt_dl_api.youtube_dl.extractor import GlideIE
    class OptFunctions(object):
        def __init__(self, **kwargs):
            for k in kwargs:
                setattr(self,k,kwargs[k])
    o1 = OptFunctions(noplaylist=True)
    o2 = OptFunctions(noplaylist=False)
    g1 = GlideIE(o1)
    g2 = GlideIE(o2)
    assert g1.ie_key() == 'glide'
    assert g2.ie_key() == 'glide:playlist'

# Generated at 2022-06-14 16:16:51.596751
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Unit test for constructor of class GlideIE
    glide = GlideIE()
    assert glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:58.174613
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("share.glide.me")
    # Test for basic url match
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    assert(ie._match_id(url) == "UZF8zlmuQbe4mr+7dCiQ0w==")
    # Test for bad url
    url = "http://notGlide.com"
    assert(ie._match_id(url) == None)

# Generated at 2022-06-14 16:17:00.747911
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_extractor = GlideIE()
    assert glide_extractor._VALID_URL == GlideIE._VALID_URL
    assert glide_extractor._TEST == GlideIE._TEST

# Generated at 2022-06-14 16:17:05.131601
# Unit test for constructor of class GlideIE
def test_GlideIE():
    import sys,os.path
    common_path=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'common'))
    sys.path.append(common_path)
    from test_resolver import TestResolver
    return TestResolver().resolve('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:17:06.243760
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(GlideIE._downloader)

# Generated at 2022-06-14 16:17:09.265911
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == GlideIE._VALID_URL
    assert ie.IE_NAME == 'glide'
    asser

# Generated at 2022-06-14 16:17:12.050598
# Unit test for constructor of class GlideIE
def test_GlideIE():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_GlideIE))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# Generated at 2022-06-14 16:17:13.632536
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:17:17.626083
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Test constructor of class GlideIE"""
    glide_ie = GlideIE()
    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide_ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# unit test for function _real_extract of class GlideIE

# Generated at 2022-06-14 16:17:51.653553
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert isinstance(instance, InfoExtractor)
    assert isinstance(instance.IE_NAME, unicode)
    assert instance.IE_NAME == 'glide'

# Generated at 2022-06-14 16:17:52.669042
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:17:56.977344
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:17:59.825045
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    # test with extracted information of a Glide video
    ie.extract({'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='})

# Generated at 2022-06-14 16:18:05.738755
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie_Glide = GlideIE()

# Generated at 2022-06-14 16:18:12.910969
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    ie.extract('http://share.glide.me/KiZkHp9zf-kOUkVg1_Sb1w==')
    ie.extract('http://share.glide.me/gd42Rn1nV7Q2Ik3seG7DwA==')

# Generated at 2022-06-14 16:18:17.413659
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    url = GlideIE(GlideIE.ie_key())
    assert url.suitable(test_url)

# Generated at 2022-06-14 16:18:27.178883
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    # assert ie._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"
    # assert ie._TEST["url"] == "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    # assert ie._TEST["md5"] == "4466372687352851af2d131cfaa8a4c7"
    # assert ie._TEST["info_dict"] == {'id': 'UZF8zlmuQbe4mr+7dCiQ0w==', 'ext': 'mp4', 'title': "Damon's Glide message", 'thumbnail': r're:^https?://.*?\.cloudfront\.

# Generated at 2022-06-14 16:18:33.942824
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:44.065601
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from unittest import TestCase
    from .common import InfoExtractor
    from .glide import GlideIE

    class ConstructorTest(TestCase):
        def test(self):
            ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

            self.assertEqual(ie.__class__.__name__, "GlideIE")
            self.assertEqual(ie.ie_key(), "Glide")
            self.assertEqual(ie.IE_DESC, "Glide mobile video messages (glide.me)")
            self.assertEqual(ie.url_re.pattern, "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)")



# Generated at 2022-06-14 16:19:57.765122
# Unit test for constructor of class GlideIE
def test_GlideIE():

    if __name__ == "__main__":
        url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
        #url = "https://share.glide.me/TPB58mUBmEgf8Wzs3iV1fA=="
        extractor = GlideIE()
        extractor.extract(url)

# Generated at 2022-06-14 16:20:00.896914
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print("Running unit tests for GlideIE")
    glide_instance = GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:20:05.183027
# Unit test for constructor of class GlideIE
def test_GlideIE():

	glide_ie = GlideIE()

	x = glide_ie._VALID_URL
	y = 'https://share.glide.me/(?P<id>[a-zA-Z0-9=_+-]+)'
	z = x == y
	assert z == True, "Unexpected _VALID_URL"

	x = glide_ie.IE_DESC
	y = 'Glide mobile video messages (glide.me)'
	z = x == y
	assert z == True, "Unexpected IE_DESC"

# Generated at 2022-06-14 16:20:06.317835
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    return ie.extract(test_GlideIE._TEST['url'])

# Generated at 2022-06-14 16:20:07.397952
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()


# Generated at 2022-06-14 16:20:08.602674
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(GlideIE.suitable)

# Generated at 2022-06-14 16:20:12.844590
# Unit test for constructor of class GlideIE
def test_GlideIE():
    answer = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==').title()
    correct = 'Damon\'s Glide message'
    assert answer == correct


# Generated at 2022-06-14 16:20:14.038375
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert type(GlideIE().IE_NAME) == str
    assert type(GlideIE().IE_DESC) == str


# Generated at 2022-06-14 16:20:16.363603
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Download a Glide video, burn the link
    # If a new video link is found, change this code
    video_url = 'UZF8zlmuQbe4mr+7dCiQ0w==' # video link
    GlideIE().download(video_url)


# Generated at 2022-06-14 16:20:26.690865
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    webpage = ie._download_webpage(url, video_id)
    title = ie._html_search_regex(r'<title>(.+?)</title>', webpage, 'title', default=None) or ie._og_search_title(webpage)
    video_url = ie._proto_relative_url(ie._search_regex(r'<source[^>]+src=(["\'])(?P<url>.+?)\1', webpage, 'video URL', default=None, group='url')) or ie._og_search_

# Generated at 2022-06-14 16:23:01.539438
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = InfoExtractor(GlideIE)
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:23:08.709033
# Unit test for constructor of class GlideIE
def test_GlideIE():
    g = GlideIE()
    assert g.IE_NAME == 'glide'
    assert g.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert g._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:23:10.739910
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Constructor of class test"""
    GlideIE()

if __name__ == '__main__':
    test_GlideIE()

# Generated at 2022-06-14 16:23:20.290178
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Problem with IPython3
    globals()['InfoExtractor'] = InfoExtractor

    IE=GlideIE()
    assert IE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:23:22.640387
# Unit test for constructor of class GlideIE
def test_GlideIE():
	GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')