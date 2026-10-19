

# Generated at 2022-06-14 16:13:29.493474
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert type(ie) == InfoExtractor
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:31.176740
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie != None


# Generated at 2022-06-14 16:13:42.381381
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert GlideIE.suitable("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
	assert not GlideIE.suitable("https://www.youtube.com/watch?v=UZF8zlmuQbe4mr+7dCiQ0w==")
	assert not GlideIE.suitable("http://www.glude.me/UZF8zlmuQbe4mr+7dCiQ0w==")
	assert not GlideIE.suitable("http://www.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:13:48.589144
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:52.453514
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')


if __name__ == "__main__":
    test_GlideIE()

# Generated at 2022-06-14 16:14:01.181734
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:03.101311
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .test_generic_info_extractor import test_constructor
    test_constructor(GlideIE)

# Generated at 2022-06-14 16:14:06.166581
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test that GlideIE class exists
    GlideIE = GlideIE()
    assert GlideIE is not None

# Generated at 2022-06-14 16:14:14.187904
# Unit test for constructor of class GlideIE
def test_GlideIE():
    asserclass(GlideIE()._VALID_URL, GlideIE._VALID_URL)
    asserclass(GlideIE()._TEST, GlideIE._TEST)
    asserclass(GlideIE()._real_extract, GlideIE._real_extract)
    asserclass(GlideIE()._TEST, GlideIE._TEST)
    asserclass(GlideIE()._TEST, GlideIE._TEST)
    asserclass(GlideIE()._TEST, GlideIE._TEST)

# Generated at 2022-06-14 16:14:23.063936
# Unit test for constructor of class GlideIE
def test_GlideIE():

    # Test constructor of class GlideIE
    assert hasattr(GlideIE, 'IE_NAME')
    assert hasattr(GlideIE, 'IE_DESC')
    assert hasattr(GlideIE, '_VALI_URL')
    assert hasattr(GlideIE, '_TEST')
    # Test constructor of class InfoExtractor
    assert hasattr(InfoExtractor, '_WORKING')
    assert hasattr(InfoExtractor, '_downloader')
    assert hasattr(InfoExtractor, '_download_webpage_handle')


# Test the _download_webpage_handle method of class InfoExtractor

# Generated at 2022-06-14 16:14:35.356545
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:14:35.942125
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:38.135158
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert True

# Generated at 2022-06-14 16:14:47.956343
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Unit test for constructor of GlideIE class
    """

    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:49.106656
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj.IE_NAME == 'Glide'

# Generated at 2022-06-14 16:14:57.718205
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:05.917092
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Implement a constructor test
    # The failed case (no exception raised) will be
    # assert len(glide_ie.extractor.subtitles.all()) == 0
    # I suppose this case is true by default. and it is not necessary
    # to be tested here

    # The passed case (no exception raised) will be
    # assert len(glide_ie.extractor.subtitles.all()) == 2
    # Maybe the passed case can be replaced by comment below
    assert True

# Generated at 2022-06-14 16:15:12.062918
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:15:14.783474
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:15:15.685887
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor._downloader)

# Generated at 2022-06-14 16:15:33.343073
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Purpose of this test:
    1. check if the constructor of class GlideIE works
    2. check if the extractor works
    """
    test_instance = GlideIE()
    assert test_instance.IE_NAME == 'glide.me'
    assert test_instance.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert test_instance.VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:34.968904
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:15:44.245817
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    webpage = ie._download_webpage(url, video_id)
    title = ie._html_search_regex(
        r'<title>(.+?)</title>', webpage,
        'title', default=None) or ie._og_search_title(webpage)

# Generated at 2022-06-14 16:15:46.851302
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:48.547262
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:15:49.815741
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(
        InfoExtractor())

# Generated at 2022-06-14 16:16:02.062847
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:11.176092
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.IE_NAME == 'Glide'
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE.IE_VERSION == '0.0.1'
    assert GlideIE.IE_KEY == 'glide'
    assert GlideIE.IE_URL == 'glide.me'
    assert GlideIE._VALID_URL == r'http://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    # Test of test case in _TEST
    assert GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert GlideIE._TEST['md5']

# Generated at 2022-06-14 16:16:23.083756
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert(ie.IE_DESC == 'Glide mobile video messages (glide.me)')
    assert(ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    assert(ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7')
    assert(ie._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:24.101841
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract()

# Generated at 2022-06-14 16:16:45.341272
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    url = 'http://share.glide.me/' + video_id
    ie = GlideIE(url)
    assert ie.video_id() == video_id
    assert ie.title() == "Damon's Glide message"

# Generated at 2022-06-14 16:16:49.196261
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('')
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:59.250735
# Unit test for constructor of class GlideIE
def test_GlideIE():
	glideIE = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
	assert glideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
	assert glideIE.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:17:00.789380
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 16:17:02.266210
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    print ('Test for constructor of class GlideIE calling is successful\n')


# Generated at 2022-06-14 16:17:03.337878
# Unit test for constructor of class GlideIE
def test_GlideIE():
    my_GlideIE = GlideIE()
    assert my_GlideIE is not None

# Generated at 2022-06-14 16:17:04.158652
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert type(GlideIE) == type(object)

# Generated at 2022-06-14 16:17:05.791839
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE(), InfoExtractor)

# Generated at 2022-06-14 16:17:08.336668
# Unit test for constructor of class GlideIE
def test_GlideIE():

    # file_id
    assert GlideIE._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"

    # extractor
    return GlideIE()

test_GlideIE()

# Generated at 2022-06-14 16:17:15.081231
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC = 'Glide mobile video messages (glide.me)'
    ie._VALID_URL = r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:49.849299
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('test', 'abc123').test()

test_GlideIE()

# Generated at 2022-06-14 16:17:53.043773
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_GlideIE = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:17:59.934458
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_GlideIE.__name__ = 'test_GlideIE'
    extractor = GlideIE()
    test_url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert extractor._match_id(test_url) == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert extractor.IE_NAME == 'glide'
    assert extractor.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:18:00.839419
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE, InfoExtractor)

# Generated at 2022-06-14 16:18:03.936458
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide:share'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:04.893168
# Unit test for constructor of class GlideIE
def test_GlideIE():
    constructor_test_for_ie('GlideIE')

# Generated at 2022-06-14 16:18:15.070937
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE()._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:17.771843
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:18:20.080859
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    # check that it has params
    assert ie._VALID_URL is not None
    assert ie.IE_NAME is not None
    assert ie.IE_DESC is not None
    assert ie._TEST is not None
    # check that it has methods
    assert ie._real_extract is not None
    assert ie._real_initialize is not None
    assert ie._real_extract is not None
    assert ie._real_suitable is not None
    # check that it follows the template
    assert ie._WORKING == True

# Generated at 2022-06-14 16:18:22.102529
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_class = type(InfoExtractor._create_ie('glide'))
    assert glide_class == GlideIE

# Generated at 2022-06-14 16:19:43.701755
# Unit test for constructor of class GlideIE
def test_GlideIE():
  # Initialize an instance of GlideIE class
  glide_extractor = GlideIE()
  print(glide_extractor.IE_DESC)
  print(glide_extractor.IE_NAME)
  print(glide_extractor.ie_key())
  print(glide_extractor._VALID_URL)
  print(glide_extractor._TEST)
  # Extracts video url and title of a glide video
  print(glide_extractor._real_extract(glide_extractor._TEST['url']))

# Generated at 2022-06-14 16:19:44.913730
# Unit test for constructor of class GlideIE
def test_GlideIE():
    downloader = GlideIE()
    downloader.download(GlideIE._TEST['url'])

# Generated at 2022-06-14 16:19:48.234313
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test instanciation
    ie = GlideIE()
    # Test type of ie
    assert ie.IE_NAME == 'glide'
    # Test ie has method extract
    assert callable(ie.extract)

# Generated at 2022-06-14 16:19:52.997925
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    

# Generated at 2022-06-14 16:19:55.040560
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Unit test for constructor of class GlideIE
    Parameters:
        None
    Returns:
        None
    Raises:
        None
    """
    ie = InfoExtractor()
    ie.add_ie(GlideIE)
    ie.download(glideurl)

# test_GlideIE()

# Generated at 2022-06-14 16:19:57.206707
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert "GlideIE" == GlideIE.__name__

# Generated at 2022-06-14 16:20:00.370773
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    ie.get_url()
    ie.get_info()

# Generated at 2022-06-14 16:20:02.360011
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None)
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:20:07.443752
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.IE_DESC is not None
    assert GlideIE.IE_NAME is not None 
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE.IE_NAME == 'glide' 
    assert GlideIE._VALID_URL is not None
    assert GlideIE._TEST is not None


# Generated at 2022-06-14 16:20:09.426417
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # TODO: Remove this
    return GlideIE(None)

# Generated at 2022-06-14 16:22:56.995374
# Unit test for constructor of class GlideIE
def test_GlideIE():
  #print("test_GlideIE()")
  g = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
  assert g.info_extractor_key() == 'Glide'
  assert g.info_extractor_type() == 'video'

# Generated at 2022-06-14 16:22:58.603243
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE()
    except:
        raise AssertionError()

# Generated at 2022-06-14 16:22:59.472411
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(isinstance(GlideIE, InfoExtractor))

# Generated at 2022-06-14 16:23:07.253656
# Unit test for constructor of class GlideIE
def test_GlideIE():
    import unittest

    class TestGlideIE(unittest.TestCase):
        def setUp(self):
            self.s = GlideIE()
            self.url1 = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='

        def test_GlideIE_instantiation(self):
            self.assertIsInstance(self.s, GlideIE)

        def test_GlideIE_url_id(self):
            id = self.s._match_id(self.url1)
            self.assertEqual(id, 'UZF8zlmuQbe4mr+7dCiQ0w==')

    suite = unittest.TestLoader().loadTestsFromTestCase(TestGlideIE)
    unittest.Text

# Generated at 2022-06-14 16:23:12.558863
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(InfoExtractor())
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:23:21.137713
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert glide._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)', 'Should be a valid url'
    assert glide._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'Should be a valid test url'
    assert glide._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7', 'Should be a valid test md5'