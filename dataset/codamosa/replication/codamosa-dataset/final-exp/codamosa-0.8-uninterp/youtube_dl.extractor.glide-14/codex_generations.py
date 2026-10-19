

# Generated at 2022-06-14 16:13:29.011451
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None)

# Generated at 2022-06-14 16:13:40.377302
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:43.254306
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Without this check, a change in GlideIE will break unit tests in other
    # directories, which you might not expect.
    import sys
    if 'glide' in sys.modules:
        raise ImportError('Failed to import glide module')
    import glide

# Generated at 2022-06-14 16:13:52.453608
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    glide_IE = GlideIE()
    video_info_dict = glide_IE._real_extract(url)
    assert video_info_dict['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert video_info_dict['title'] == "Damon's Glide message"

# Generated at 2022-06-14 16:13:56.865993
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.url == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='


# Generated at 2022-06-14 16:13:58.068991
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Create instance of class GlideIE
    GlideIE()

# Generated at 2022-06-14 16:13:59.908717
# Unit test for constructor of class GlideIE
def test_GlideIE():
    objTest = GlideIE()
    assert isinstance(objTest, GlideIE)


# Generated at 2022-06-14 16:14:13.172722
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test creation of a GlideIE instance
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:23.921729
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert ie._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['info_dict']['ext'] == 'mp4'
    assert ie._TEST['info_dict']['title']

# Generated at 2022-06-14 16:14:24.589561
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:33.446200
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract(u'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    pass

# Generated at 2022-06-14 16:14:36.839229
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj.IE_NAME == 'Glide'
    assert obj.IE_DESC == GlideIE.IE_DESC
    assert obj.VALID_URL == GlideIE._VALID_URL


# Generated at 2022-06-14 16:14:37.616688
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE
    assert True

# Generated at 2022-06-14 16:14:39.048522
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj
    assert isinstance(obj, GlideIE)
    assert obj.__dict__


# Generated at 2022-06-14 16:14:43.863403
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(InfoExtractor())
    assert ie is not None
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:46.181422
# Unit test for constructor of class GlideIE
def test_GlideIE():
    'Test constructor of GlideIE'
    ie = GlideIE()
    # Check
    assert ie.ie_key() == 'Glide'

# Generated at 2022-06-14 16:14:47.458044
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None)

# Generated at 2022-06-14 16:14:48.040005
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE

# Generated at 2022-06-14 16:14:52.951664
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    obj1 = ie.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    obj2 = ie.suitable('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert obj1 is True
    assert obj2 is True

# Generated at 2022-06-14 16:14:56.386550
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Unit test to check if constructor of class GlideIE works
    glide = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert glide.initialize(), 'Unable to initialize GlideIE'

# Generated at 2022-06-14 16:15:10.409106
# Unit test for constructor of class GlideIE
def test_GlideIE():
    v = GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert v.IE_NAME == "Glide"
    assert v.IE_ID == "glide"
    assert v.IE_DESC == "Glide mobile video messages (glide.me)"


# Generated at 2022-06-14 16:15:20.019500
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:15:22.848498
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.ie_key() == 'Glide'
    assert ie.ie_desc() == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:15:28.384582
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:15:33.078280
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE('http://share.glide.me/VjZ2SzZUQ7qdOzj+p7y4/g==')
    assert instance.VIDEO_URL == 'http://share.glide.me/VjZ2SzZUQ7qdOzj+p7y4/g=='

# Generated at 2022-06-14 16:15:37.456075
# Unit test for constructor of class GlideIE
def test_GlideIE():

    glide_test = GlideIE()
    glide_test._match_id("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    glide_test._real_extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")


# Generated at 2022-06-14 16:15:41.831662
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE()
    assert glide.IE_NAME == 'Glide'
    assert glide.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:45.576485
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:15:50.199248
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie._VALID_URL == GlideIE._VALID_URL
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.test() == GlideIE._TEST


# Generated at 2022-06-14 16:16:00.520953
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    title = "Damon's Glide message"
    thumbnail = r're:^https?://.*?\.cloudfront\.net/.*\.jpg$'
    vid = ie._real_extract(url)
    ie.to_screen(vid)
    assert vid['id'] == video_id
    assert vid['title'] == title
    assert vid['thumbnail'] == thumbnail

# Generated at 2022-06-14 16:16:25.935335
# Unit test for constructor of class GlideIE
def test_GlideIE():
    e = GlideIE()
    assert 'Glide mobile video messages (glide.me)' == e.IE_DESC

# Generated at 2022-06-14 16:16:34.221686
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE()
    assert glide_ie.ie_key() == 'Glide'
    assert glide_ie.ie_desc() == 'Glide mobile video messages (glide.me)'
    assert glide_ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert glide_ie._downloader == None
    assert glide_ie.params == None
    assert glide_ie._ies == []
    assert glide_ie.FD_NAME == 'proxyservice'
    assert glide_ie._downloader_params == None
    assert glide_ie._WORKING == True
    assert glide_ie._download_retry == 4
    assert glide_ie._geo_verification_headers == []

#

# Generated at 2022-06-14 16:16:38.137767
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    GlideIE("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:16:40.745093
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_instance = GlideIE()
    assert isinstance(test_instance, InfoExtractor)

    expected_object_type = 'GlideIE'
    assert test_instance.__class__.__name__ == expected_object_type


# Generated at 2022-06-14 16:16:44.906105
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print("Testing GlideIE...")
    ie = GlideIE()
    # Testing
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    print("OK")


# Generated at 2022-06-14 16:16:46.114454
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(object)._VALID_URL == GlideIE._VALID_URL

# Generated at 2022-06-14 16:16:46.697283
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:48.020406
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Test whether constructor of class GlideIE executes."""
    GlideIE("_")

# Generated at 2022-06-14 16:16:51.227839
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.IE_NAME == 'glide'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:55.508620
# Unit test for constructor of class GlideIE
def test_GlideIE():
    t = GlideIE()
    assert hasattr(t, "_VALID_URL"), "_VALID_URL is missing from object"
    assert t._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)', "_VALID_URL is incorrect"
    assert t.IE_DESC == "Glide mobile video messages (glide.me)"


# Generated at 2022-06-14 16:17:51.488946
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC

# Generated at 2022-06-14 16:17:57.013643
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:17:59.861190
# Unit test for constructor of class GlideIE
def test_GlideIE():
	glide_ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
	assert 'Glide' in glide_ie.IE_DESC

# Generated at 2022-06-14 16:18:04.337260
# Unit test for constructor of class GlideIE
def test_GlideIE():
  constructor_test([
      (
        'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
      , {
        'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
        'ext': 'mp4',
        'title': "Damon's Glide message",
        'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
      }
      )
    ])

# Generated at 2022-06-14 16:18:14.647817
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert ie._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['info_dict']['ext']

# Generated at 2022-06-14 16:18:25.164073
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    assert(GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(GlideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7')
    assert(GlideIE._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(GlideIE._TEST['info_dict']['ext'] == 'mp4')

# Generated at 2022-06-14 16:18:27.404005
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:18:34.112981
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC = 'Glide mobile video messages (glide.me)'
    ie._VALID_URL = r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:36.486308
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:18:39.271176
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:19:54.283834
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # test constructor
    # positive test
    valid_url = " http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w== "
    glide_ie = GlideIE(url=valid_url)
    assert glide_ie.video_id == "UZF8zlmuQbe4mr+7dCiQ0w=="

    # negative test
    invalid_url = " http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==1 "
    glide_ie = GlideIE(url=invalid_url)
    assert glide_ie.video_id == ""



# Generated at 2022-06-14 16:20:04.202411
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:20:09.994043
# Unit test for constructor of class GlideIE
def test_GlideIE():
    #url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    url = "http://share.glide.me/S5c5YbYkRwG6xzLlRcOtwg=="
    ie = GlideIE(url)
    url = ie._TEST["url"]
    #print(ie.__dict__)
    extractor_class = ie._TESTS[url]["extractor_class"]
    ie = extractor_class(url)
    #ie = GlideIE(url)
    #ie_test = ie._TEST
    #ie = ie._TEST["extractor_class"](url)
    m = ie.extract()
    print(m)

#test_GlideIE()

# Generated at 2022-06-14 16:20:18.852218
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.suitable(url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert GlideIE.suitable(url = "http://share.glide.me/rJtCiVfFGq8=")
    assert GlideIE.suitable(url = "http://share.glide.me/dog1")
    assert not GlideIE.suitable(url = "http://share.glide.com/")
    assert not GlideIE.suitable(url = "http://share.glide.me")
    assert GlideIE.suitable(url = "https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:20:19.984798
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test = GlideIE()
    test.suite()


# Generated at 2022-06-14 16:20:22.030134
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE()
    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:20:27.502822
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide.me'
    # Should raise an AssertionError, if it doesn't work
    ie._build_url_result(
        0, ie._search_regex(
            '^\s+<source[^>]+src=(["\'])(?P<url>.+?)\1',
            '<source>', 'video URL', default=None,
            group='url'))

# Generated at 2022-06-14 16:20:28.488939
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert "GlideIE" == GlideIE()._type

# Generated at 2022-06-14 16:20:29.899301
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie


# Generated at 2022-06-14 16:20:31.089077
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC

# Generated at 2022-06-14 16:22:53.036657
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:22:53.862651
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:22:56.638010
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)";
    assert GlideIE.IE_DESC == "Glide mobile video messages (glide.me)";

# Generated at 2022-06-14 16:22:58.940111
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    # a regular expression matching a valid Glide URL
    assert ie._VALID_URL is not None


# Generated at 2022-06-14 16:22:59.797631
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE() is not None

# Generated at 2022-06-14 16:23:02.549286
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == "Glide mobile video messages"
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    

# Generated at 2022-06-14 16:23:06.107470
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert(GlideIE(test_url)._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')

# Generated at 2022-06-14 16:23:09.626473
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Basic unit test for GlideIE module.
    """
    return GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:23:11.325279
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None, {})
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:23:12.508259
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()