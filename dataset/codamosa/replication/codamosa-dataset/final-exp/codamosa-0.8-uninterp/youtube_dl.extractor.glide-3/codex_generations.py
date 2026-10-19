

# Generated at 2022-06-14 16:13:37.107535
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.IE_DESC == "Glide mobile video messages (glide.me)"
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:38.901692
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:13:46.420673
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"
    assert GlideIE._TEST["url"] == "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    assert GlideIE._TEST["md5"] == "4466372687352851af2d131cfaa8a4c7"
    assert GlideIE._TEST["info_dict"]["id"] == "UZF8zlmuQbe4mr+7dCiQ0w=="
    assert GlideIE._TEST["info_dict"]["ext"] == "mp4"

# Generated at 2022-06-14 16:13:47.754807
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == "glide"
    assert ie.IE_DESC == "Glide mobile video messages (glide.me)"



# Generated at 2022-06-14 16:13:51.705065
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    glide_ie = GlideIE()
    data = glide_ie._real_extract(url)
    assert data["title"] == "Damon's Glide message"
    assert data["url"] == "https://d2zhsg4ak20lrp.cloudfront.net/UZF8zlmuQbe4mr+7dCiQ0w==_20140829_085325_0-0-0-0.mp4"

# Generated at 2022-06-14 16:14:00.878691
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE()._TEST == {'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='}
    assert GlideIE()._TEST == {'md5': '4466372687352851af2d131cfaa8a4c7'}

# Generated at 2022-06-14 16:14:01.977438
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()


# Generated at 2022-06-14 16:14:04.063608
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE()
    except Exception as e:
        assert(0 == 1)

# Generated at 2022-06-14 16:14:08.903511
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.ie_key() == 'Glide'

# Generated at 2022-06-14 16:14:11.067472
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test = GlideIE._TEST
    assert GlideIE._VALID_URL.match(test['url'])
    ie = GlideIE(test['url'])
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.IE_NAME == 'glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:17.616469
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie._real_extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:14:21.207973
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert hasattr(ie, '_VALID_URL')

# Generated at 2022-06-14 16:14:23.710600
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:24.930494
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:14:30.300009
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:14:35.021689
# Unit test for constructor of class GlideIE
def test_GlideIE():
    result = GlideIE()
    assert result.IE_NAME == 'glide'
    assert result.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert result._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:14:36.803886
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Test for class GlideIE"""
    GlideIE(None)



# Generated at 2022-06-14 16:14:46.855610
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.__class__ == GlideIE
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:48.852213
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:14:50.335624
# Unit test for constructor of class GlideIE
def test_GlideIE():
    A = GlideIE(None)
    B = InfoExtractor(None)
    assert(A == B)

# Generated at 2022-06-14 16:14:59.386169
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Unit tests for GlideIE.extract

# Generated at 2022-06-14 16:15:02.033309
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE(InfoExtractor()), InfoExtractor)

# Generated at 2022-06-14 16:15:09.112821
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Unit test for constructor of class GlideIE
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    instance = GlideIE(url)
    assert instance._VALID_URL == url
    assert instance.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert instance._TEST is not None


# Generated at 2022-06-14 16:15:15.281244
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:15:16.620961
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None)._VALID_URL == GlideIE._VALID_URL

# Generated at 2022-06-14 16:15:21.481182
# Unit test for constructor of class GlideIE
def test_GlideIE():
    expected_GlideIE = GlideIE(None)
    assert expected_GlideIE.IE_NAME == 'glide'
    assert expected_GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert expected_GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:15:22.371802
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:25.960544
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Here I test if it is possible to create an instance of GlideIE
    # without errors
    ie = GlideIE()
    assert(ie is not None)
    
#Unit test for method _real_extract of class GlideIE

# Generated at 2022-06-14 16:15:28.914208
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:33.124787
# Unit test for constructor of class GlideIE
def test_GlideIE():
    infoExtractor = GlideIE()
    assert infoExtractor.getInformation( 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==' )['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:15:46.851344
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert True

test_GlideIE()

# Generated at 2022-06-14 16:15:48.235982
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor())._VALID_URL == GlideIE._VALID_URL

# Generated at 2022-06-14 16:15:55.357880
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.ie_key() == 'Glide'
    assert ie.ie_flags() == 0


# Generated at 2022-06-14 16:15:58.304933
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None)._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:00.570710
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try: 
        GlideIE()
    except:
        assert False
    else:
        assert True



# Generated at 2022-06-14 16:16:06.226570
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.ie_key() == 'Glide'
    assert ie.ie_desc() == 'Glide mobile video messages (glide.me)'
    assert ie.VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:16:08.109430
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:11.820649
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie is not None
    assert ie.name == 'Glide'
    assert ie.ie_key() == 'Glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Test case for extract method of class GlideIE

# Generated at 2022-06-14 16:16:14.275087
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    ie = GlideIE()
    assert ie.IE_DESC

# Generated at 2022-06-14 16:16:14.661714
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:45.259115
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Call the constructor
    yt = GlideIE()
    assert yt is not None


# Generated at 2022-06-14 16:16:48.642571
# Unit test for constructor of class GlideIE
def test_GlideIE():
    a = GlideIE()
    # Test the function _real_extract() in class GlideIE
    GlideIE._real_extract(a, a._TEST['url'])

if __name__ == '__main__':
    test_GlideIE()

# Generated at 2022-06-14 16:16:50.636959
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Constructor should not throw an exception
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:17:00.546016
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert obj._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert obj._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert obj._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert obj._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:17:08.237056
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie_obj=GlideIE()
    obj=ie_obj._real_extract(ie_obj._VALID_URL)
    assert str(type(obj['id']))=="<type 'unicode'>"
    assert str(type(obj['title']))=="<type 'unicode'>"
    assert str(type(obj['url']))=="<type 'unicode'>"
    assert str(type(obj['thumbnail']))=="<type 'unicode'>"

# Generated at 2022-06-14 16:17:09.445750
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    This test checks if GlideIE can be created without any error
    """
    GlideIE()

# Generated at 2022-06-14 16:17:14.560935
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    This function tests function GlideIE
    """
    # Test for GlideIE
    # This tests for GlideIE
    import GlideIE
    # Test for GlideIE
    glide_test = GlideIE.GlideIE()
    # This tests for GlideIE
    glide_test._match_id("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:17:19.669657
# Unit test for constructor of class GlideIE
def test_GlideIE():
	ie = GlideIE(None)
	assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
	assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:20.264484
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()

# Generated at 2022-06-14 16:17:21.563310
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_GlideIE.ie = GlideIE()

# Generated at 2022-06-14 16:18:30.890186
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:32.796397
# Unit test for constructor of class GlideIE
def test_GlideIE():
    c = GlideIE()
    assert c.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:18:43.356703
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for GlideIE
    """
    from . import GlideIE
    from .test_common import assertEqual
    from .test_common import assertIE

    assertIE(GlideIE.name, GlideIE.__module__)
    assertEqual(GlideIE.IE_DESC, "Glide mobile video messages (glide.me)")
    assertEqual(GlideIE._VALID_URL, r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')

# Generated at 2022-06-14 16:18:52.747544
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE()
    print (glide_ie.IE_DESC)
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    video_id = glide_ie._match_id(url)
    webpage = glide_ie._download_webpage(url, video_id)
    title = glide_ie._html_search_regex(r'<title>(.+?)</title>', webpage, 'title', default=None)
    print ("title: ", title)

# Generated at 2022-06-14 16:18:55.773528
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for GlideIE().
    """
    # This test will check that GlideIE could extract an URL.
    assert isinstance(GlideIE().extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='), dict)

# Generated at 2022-06-14 16:19:04.085789
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Constructor test
    ie = GlideIE()
    # Extra check
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.IE_NAME == 'glide'
    assert ie.http_headers == {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0 (Chrome)'}

    # Unit test for getting file id from url
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='


# Generated at 2022-06-14 16:19:11.263430
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert("GlideIE" == ie.IE_NAME)
    assert("Glide mobile video messages (glide.me)" == ie.IE_DESC)
    assert("https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)" == ie._VALID_URL)
    assert(ie._TEST['url'] == "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:19:19.977977
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert obj._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert obj._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert obj._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert obj._TEST['info_dict']['ext'] == 'mp4'
    assert obj._TEST['info_dict']['title']

# Generated at 2022-06-14 16:19:27.802140
# Unit test for constructor of class GlideIE
def test_GlideIE():
	ie = GlideIE()
	assert ie.IE_NAME == "Glide"
	assert ie.IE_DESC == "Glide mobile video messages (glide.me)"
	assert ie.VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"

# Generated at 2022-06-14 16:19:31.607949
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE = __import__('youtube_dl.extractor.glide').GlideIE
    ie = GlideIE()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:22:02.553139
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert isinstance(obj, InfoExtractor)

# Generated at 2022-06-14 16:22:13.152236
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie._real_extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    #assert ie._real_extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==") == 'http://cdn.glideo.com/clips/UZF8zlmuQbe4mr+7dCiQ0w==/146428ef2e6/clip.mp4?Expires=1464337790&Signature=YnsYFgLT7VuwfOZH7VQ8WlkJ9rCx-TUybIsH8I6Uy7FQw1Qq3BB6~Izf-B9X

# Generated at 2022-06-14 16:22:21.918756
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .common import GlideIE
    from .common import InfoExtractor
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    from .common import InfoExtractorUnitTestCase
    # Test constructor of class GlideIE
    # Test attributes of class GlideIE
    # Test method extract of class GlideIE
    # Test method _real_extract of class GlideIE

# Generated at 2022-06-14 16:22:23.975332
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None)
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:27.706384
# Unit test for constructor of class GlideIE
def test_GlideIE():

    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    ie = GlideIE()
    ie.extract(url, {'download': False})

# Generated at 2022-06-14 16:22:28.337799
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None)

# Generated at 2022-06-14 16:22:29.569291
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """ Test construction of GlideIE object """
    ie = GlideIE()

# Generated at 2022-06-14 16:22:34.223801
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE_instance = GlideIE(InfoExtractor())
    assert GlideIE_instance.ie_key() == 'Glide'
    assert GlideIE_instance.ie_desc() == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:22:35.305621
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:22:43.148658
# Unit test for constructor of class GlideIE
def test_GlideIE():
    import unittest
    try:
        from unittest import mock
    except ImportError:
        import mock

    class TestGlideIE(unittest.TestCase):
        def setUp(self):
            from ..ytdl_data import SAMPLE_GLIDE
            self.SampleGlide = SAMPLE_GLIDE

        def test_GlideIE_constructor(self):
            def _get_webpage(url, *args, **kwargs):
                return self.SampleGlide

            GlideIE.IE_NAME = 'Glide'
            ie = GlideIE(GlideIE.ie_key())
            ie.http = mock.Mock()
            ie.http.get = mock.Mock(side_effect=_get_webpage)