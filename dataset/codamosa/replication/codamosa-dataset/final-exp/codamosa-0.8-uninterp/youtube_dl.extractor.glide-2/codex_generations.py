

# Generated at 2022-06-14 16:13:30.874610
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    instance.constructor_method()

if __name__ == "__main__":
    test_GlideIE()


# Generated at 2022-06-14 16:13:42.119597
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert(ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    assert(ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7')
    assert(ie._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(ie._TEST['info_dict']['ext'] == 'mp4')

# Generated at 2022-06-14 16:13:55.379013
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide mobile video messages'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST["url"] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST["md5"] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:14:02.703051
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE('UZF8zlmuQbe4mr+7dCiQ0w==','http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',True)
    yield (instance, 'GlideIE', 'ext', 'mp4')
    yield (instance, 'GlideIE', 'id', 'UZF8zlmuQbe4mr+7dCiQ0w==')
    yield (instance, 'GlideIE', 'url', 'https://shares-prod-videos.s3.amazonaws.com/video/UZF8zlmuQbe4mr+7dCiQ0w==/UZF8zlmuQbe4mr+7dCiQ0w==.mp4')

# Generated at 2022-06-14 16:14:06.226192
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:14:17.943262
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    ie = GlideIE()
    ie.extract(url)
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:14:20.379409
# Unit test for constructor of class GlideIE
def test_GlideIE():
    myGlideIE = GlideIE()
    assert myGlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:21.378663
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    pass

# Generated at 2022-06-14 16:14:29.595788
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == "glide"
    assert ie.IE_DESC == "Glide Mobile Video Messages"
    assert ie._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)".decode("utf-8")

# Generated at 2022-06-14 16:14:33.280646
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(common.InfoExtractor())._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:42.139240
# Unit test for constructor of class GlideIE
def test_GlideIE():

    # Create an instance of the class GlideIE
    glide_ie = GlideIE()

    # Validate that the instance is not null
    assert glide_ie is not None


# Generated at 2022-06-14 16:14:47.582204
# Unit test for constructor of class GlideIE
def test_GlideIE():
    a_tuple_of_numbers = (2, 3, 5, 7, 11)
    url = 'https://share.glide.me/PZF8zlmuQbe4mr+7dCiQ0w=='
    input_entered = a_tuple_of_numbers, url
    assert input_entered == (a_tuple_of_numbers, url)


# Generated at 2022-06-14 16:14:48.815342
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glideIE = GlideIE()
    assert glideIE != None

# Generated at 2022-06-14 16:14:50.273872
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:14:53.561985
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor())._VALID_URL == GlideIE._VALID_URL
    assert GlideIE(InfoExtractor()).IE_DESC == GlideIE.IE_DESC


# Generated at 2022-06-14 16:14:54.102582
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:00.637474
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # constructor takes one required argument and two optional arguments:
    #
    # 1) Name of the subclass (GlideIE in this case)
    # 2) Regular expression of acceptable URLs: _VALID_URL (from above)
    # 3) Date of the write-up (or last edit) of the module
    ie = GlideIE(GlideIE.ie_key(), GlideIE._VALID_URL)
    # Calling url_result uses one required and one optional argument:
    #
    # 1) canonical URL of the extraction target (from above)
    # 2) A dict of properties to override the properties extracted from the
    #    URL
    info = ie.url_result('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    # The _downloader may be used

# Generated at 2022-06-14 16:15:03.247328
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .common import InfoExtractor

    # Test that GlideIE properly loads
    InfoExtractor('Glide')

# Generated at 2022-06-14 16:15:09.056566
# Unit test for constructor of class GlideIE
def test_GlideIE():
    constructor = GlideIE
    assert constructor.ie_key() == 'Glide'
    assert constructor.ie_desc() == 'Glide mobile video messages (glide.me)'
    assert constructor._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:09.661942
# Unit test for constructor of class GlideIE
def test_GlideIE():
    g = GlideIE()
    assert(g)

# Generated at 2022-06-14 16:15:29.447529
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    # GlideIE constructor sets url and name of IE
    assert ie.url == "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    assert ie.name == "GlideIE" 


# Generated at 2022-06-14 16:15:34.091834
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE();
    assert glide.IE_NAME == 'glide' and glide.IE_DESC == 'Glide mobile video messages (glide.me)';
    assert glide.VALID_URL == GlideIE._VALID_URL;
    assert glide.TEST == GlideIE._TEST;


# Generated at 2022-06-14 16:15:35.004733
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert False


# Generated at 2022-06-14 16:15:37.258005
# Unit test for constructor of class GlideIE
def test_GlideIE():
	info_extractor = GlideIE()
	assert(info_extractor.IE_DESC == "Glide mobile video messages (glide.me)")


# Generated at 2022-06-14 16:15:38.683906
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE.__init__(GlideIE)

# Generated at 2022-06-14 16:15:47.342006
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test 1
    expected = {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
        'title': "Damon's Glide message",
        'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
    }

    ie = GlideIE()
    info_dict = ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

    assert info_dict['url'] == expected['url']
    asse

# Generated at 2022-06-14 16:15:50.666472
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:02.771382
# Unit test for constructor of class GlideIE
def test_GlideIE():
    checker = GlideIE()
    assert checker.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert checker._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert checker._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert checker._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert checker._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:16:04.957435
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC
    ie._VALID_URL
    ie._TEST

# Generated at 2022-06-14 16:16:06.001688
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE() != None

# Generated at 2022-06-14 16:16:24.358696
# Unit test for constructor of class GlideIE
def test_GlideIE():
    _, info_dict = GlideIE()._download_webpage_handle(GlideIE()._TEST['url'])
    _, info_dict_glideie = GlideIE().extract(GlideIE()._TEST['url'])
    assert info_dict == info_dict_glideie

# Generated at 2022-06-14 16:16:26.716149
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:16:28.155365
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_NAME = 'glide'

# Generated at 2022-06-14 16:16:35.500847
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Test constructor of class GlideIE"""
    glideie = GlideIE()
    assert glideie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glideie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:38.334656
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Represents a test for the function _real_extract of GlideIE.
    """
    glide = GlideIE({})
    assert glide.IE_NAME == 'Glide'

# Generated at 2022-06-14 16:16:38.865054
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:39.987531
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(GlideIE == type(GlideIE('temp')))

# Generated at 2022-06-14 16:16:42.396546
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Unit test for constructor of class GlideIE
    :return:
    """
    extractor = GlideIE()
    assert extractor is not None


# Generated at 2022-06-14 16:16:43.412716
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:16:44.167440
# Unit test for constructor of class GlideIE
def test_GlideIE():
    pass

# Generated at 2022-06-14 16:17:24.436171
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Create an instance of class GlideIE
    m = GlideIE()
    assert m._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert m._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert m._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:17:27.443901
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = "https://share.glide.me/-OgtndxkTzT834i7sNQEAQ=="
    GlideIE(url)

# Generated at 2022-06-14 16:17:27.994729
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE

# Generated at 2022-06-14 16:17:29.346879
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None)

# Generated at 2022-06-14 16:17:36.564026
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info = {
        'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
        'title': "Damon's Glide message",
        'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
    }
    glideIE = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    glideIE._real_extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert glideIE.get_info() == info

# Generated at 2022-06-14 16:17:37.293474
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:17:40.230213
# Unit test for constructor of class GlideIE
def test_GlideIE():
    class_ = GlideIE
    instance = class_(None)
    assert(instance.IE_DESC)
    assert(instance._VALID_URL)


# Generated at 2022-06-14 16:17:42.441777
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:17:43.371808
# Unit test for constructor of class GlideIE
def test_GlideIE():
    return GlideIE()

# Generated at 2022-06-14 16:17:43.955979
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:09.250884
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ieIns = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ieIns.IE_DESC == 'Glide mobile video messages (glide.me)'
    # test __init__ method
    assert ieIns._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    # test _real_extract method
    assert ieIns._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    # test _download_webpage method
   

# Generated at 2022-06-14 16:19:10.774293
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(GlideIE.IE_DESC, GlideIE._VALID_URL)

# Generated at 2022-06-14 16:19:11.716971
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test for multiple cases
    GlideIE()

# Generated at 2022-06-14 16:19:14.421366
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor())._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:19:14.937976
# Unit test for constructor of class GlideIE
def test_GlideIE():
	GlideIE()

# Generated at 2022-06-14 16:19:19.152709
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Test for constructor

# Generated at 2022-06-14 16:19:19.625991
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert 1

# Generated at 2022-06-14 16:19:26.792340
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL ==  r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:19:33.578046
# Unit test for constructor of class GlideIE
def test_GlideIE():
	g = GlideIE()
	assert g.suitable(u'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') == True
	assert g.suitable(u'http://share.glide.me/myvideo') == True
	assert g.suitable(u'http://share.glide.me/') == False
	assert g.suitable(u'') == False
	assert g.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:19:41.122316
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from io import StringIO
    from ytdl_server.comparison_tool import CompareTool
    
    expected = {
        'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
        'title': "Damon's Glide message",
        'url': 'https://d1w836my735uqw.cloudfront.net/video/UZF8zlmuQbe4mr+7dCiQ0w==/vod.mp4',
        'thumbnail': 'https://d1w836my735uqw.cloudfront.net/video/UZF8zlmuQbe4mr+7dCiQ0w==/thumbnail.jpg',
    }
    

# Generated at 2022-06-14 16:22:26.399123
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert True

# Generated at 2022-06-14 16:22:27.300459
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE(), InfoExtractor)

# Generated at 2022-06-14 16:22:37.567855
# Unit test for constructor of class GlideIE
def test_GlideIE():
	info_extractor = GlideIE()
	assert info_extractor.IE_DESC == 'Glide mobile video messages (glide.me)'
	assert info_extractor._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:39.492122
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE({'_downloader': {}}), InfoExtractor)


# Generated at 2022-06-14 16:22:40.701631
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract()

# Generated at 2022-06-14 16:22:41.989879
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor())

# Generated at 2022-06-14 16:22:48.920002
# Unit test for constructor of class GlideIE
def test_GlideIE():
    globals()['GlideIE']('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

test_GlideIE.CASES = [
    # ref: https://github.com/rg3/youtube-dl/pull/5143
    [{
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'only_matching': True,
    }]
]

# Generated at 2022-06-14 16:22:50.590276
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:23:00.388177
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    x = ie._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert x['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w==', 'Wrong id returned.'
    assert x['title'] == 'Damon\'s Glide message', 'Wrong title returned.'
    assert x['url'][-3:] == 'mp4', 'mp4 url not extracted.'
    assert x['thumbnail'][-4:] == '.jpg', 'jpg url not extracted.'
    assert 'https://' in x['url'], 'URL is not secure.'
    assert 'https://' in x['thumbnail'], 'Thumbnail URL is not secure.'

# Generated at 2022-06-14 16:23:07.932228
# Unit test for constructor of class GlideIE
def test_GlideIE():
	try:
		from StringIO import StringIO
		from urllib import urlencode
		from urllib2 import HTTPHandler, build_opener, install_opener, urlopen
		from urlparse import urlparse, parse_qsl, urlsplit
	except ImportError:
		from io import StringIO
		from urllib.parse import urlencode, parse_qsl, urlsplit, urlparse
		from urllib.request import HTTPHandler, build_opener, install_opener, urlopen
		from urllib.error import HTTPError
	try:
		from toString import toString
	except ImportError:
		from .toString import toString