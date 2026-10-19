

# Generated at 2022-06-14 16:13:29.011153
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:13:29.474742
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:13:32.229880
# Unit test for constructor of class GlideIE
def test_GlideIE():
    res = GlideIE(_TEST["url"])
    res.extract()

if __name__ == '__main__':
    test_GlideIE()

# Generated at 2022-06-14 16:13:34.141362
# Unit test for constructor of class GlideIE
def test_GlideIE():
	print("In test_GlideIE. Not running any test.")
	pass

# Generated at 2022-06-14 16:13:35.577252
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:13:44.234629
# Unit test for constructor of class GlideIE
def test_GlideIE():
    i = GlideIE()
    assert i._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert i.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert i.ie_key() == 'glide'
    assert i.thumbnail() == 'https://i1.ytimg.com/vi/tNuTtEwfNcY/0.jpg'
    assert i.title() == 'Damon on Glide - Hello darling I want to send you a video message'
    assert i.description() == 'Damon on Glide - Hello darling I want to send you a video message'

# Generated at 2022-06-14 16:13:47.129943
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie  = GlideIE()
    assert ie != None


# Generated at 2022-06-14 16:13:50.032056
# Unit test for constructor of class GlideIE
def test_GlideIE():
  try:
    # Test that GlideIE is initialized with the proper name
    GlideIE()
  except:
    assert False, "GlideIE failed to initialize"


# Generated at 2022-06-14 16:13:55.113610
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    GlideIE()._real_initialize()
    GlideIE().suitable(url)
    GlideIE().extract(url).get('url')

# Generated at 2022-06-14 16:14:02.549606
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:09.175264
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """ Unit test for constructor of class GlideIE"""
    GlideIE(InfoExtractor())

if __name__ == '__main__':
    test_GlideIE()

# Generated at 2022-06-14 16:14:12.027315
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert len(ie.IE_DESC) > 0
    assert len(ie._VALID_URL) > 0
    assert ie._TEST is not None

# Generated at 2022-06-14 16:14:15.266317
# Unit test for constructor of class GlideIE
def test_GlideIE():
   GlideIE(object)

# Generated at 2022-06-14 16:14:19.432333
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # 1.
    obj = GlideIE()
    assert isinstance(obj, GlideIE)
    assert obj._VALID_URL == _VALID_URL
    assert obj._TEST == _TEST


# Generated at 2022-06-14 16:14:20.018896
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:22.649102
# Unit test for constructor of class GlideIE
def test_GlideIE():
	g_ie=GlideIE()
	video_id=g_ie._match_id(g_ie._TEST['url'])
	print (video_id)

# Generated at 2022-06-14 16:14:26.681253
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:14:27.269397
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert GlideIE()

# Generated at 2022-06-14 16:14:32.334118
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None)
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:33.732368
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glideIE = GlideIE(GlideIE.ie_key())
    return glideIE

# Generated at 2022-06-14 16:14:49.015004
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_ie = GlideIE()
    test_info = {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'md5': '4466372687352851af2d131cfaa8a4c7',
        'info_dict': {
            'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
            'ext': 'mp4',
            'title': "Damon's Glide message",
            'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
        }
    }
    video_info = video_ie._real_extract(test_info['url'])

# Generated at 2022-06-14 16:14:53.275043
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test"""
    test_object = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert test_object.url == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:14:55.118241
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    The constructor is used to create an instance of the class.
    """
    glide_ie = GlideIE()


# Generated at 2022-06-14 16:15:00.339068
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie.ie_key() == 'Glide'
    assert ie.ie_desc() == 'Glide mobile video messages (glide.me)'
    assert ie.fix_url('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie.working() is True
    print(ie)

# Generated at 2022-06-14 16:15:01.041185
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:03.768750
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test = GlideIE()
    test_GlideIE.IE_DESC == test.IE_DESC

# Generated at 2022-06-14 16:15:05.345147
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(object())


# Generated at 2022-06-14 16:15:05.778143
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:15:07.484005
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE(), InfoExtractor)


# Generated at 2022-06-14 16:15:08.952345
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None) # Doesn't raise an exception
    assert 1 == 1

# Generated at 2022-06-14 16:15:23.423614
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('foo.com')._VALID_URL == r'https?://foo\.com/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:29.760806
# Unit test for constructor of class GlideIE
def test_GlideIE():
    global GlideIE
    from .common import GlideIE
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    print (ie._match_id("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="))

if __name__ == '__main__':
    test_GlideIE()

# Generated at 2022-06-14 16:15:39.235332
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    test_url1 = ie._TEST['url']
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:41.990185
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()._VALID_URL == GlideIE._VALID_URL
    assert GlideIE().IE_DESC == GlideIE._TEST['info_dict']['title']
    assert GlideIE()._TEST == GlideIE._TEST

# Generated at 2022-06-14 16:15:42.600394
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE

# Generated at 2022-06-14 16:15:43.211081
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:44.403299
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie is not None


# Generated at 2022-06-14 16:15:45.620296
# Unit test for constructor of class GlideIE
def test_GlideIE():
    pass

# Test for method _real_extract() of class GlideIE

# Generated at 2022-06-14 16:15:49.483998
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE([GlideIE])
    assert(ie.IE_DESC == 'Glide mobile video messages (glide.me)')
    ie = GlideIE([GlideIE])
    ie._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:57.670911
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    instance._download_webpage("")
    instance._match_id("")
    instance._real_extract("")
    instance._html_search_regex("", "", "")
    instance._og_search_title("")
    instance._search_regex("", "", "")
    instance._proto_relative_url("")
    instance._og_search_video_url("")
    instance._og_search_thumbnail("")

# Generated at 2022-06-14 16:16:24.047307
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:25.691569
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE, InfoExtractor)

# Generated at 2022-06-14 16:16:33.466613
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .common import GlideIE
    ie = GlideIE(False);
    assert ie.IE_NAME == 'Glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'


# Generated at 2022-06-14 16:16:37.371878
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print("Test for constructor of class GlideIE")

    # Test for constructor without argument
    print("Case 1: Test for constructor without argument")
    try:
        GlideIE()
    except TypeError:
        print("Test has passed!")
    else:
        print("Test hasn't passed")


# Generated at 2022-06-14 16:16:38.637004
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:16:47.889090
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:58.087594
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Tests for class GlideIE
    """
    glide_test = GlideIE(None)
    # test _VALID_URL
    assert glide_test._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    # test _TEST['url']
    assert glide_test._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    # test _TEST['md5']
    assert glide_test._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    # test _TEST['info_dict']
    assert glide_test._TEST

# Generated at 2022-06-14 16:17:00.345843
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_GlideIE = GlideIE()
    assert test_GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    

# Generated at 2022-06-14 16:17:03.645418
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:17:09.982245
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:18:14.836329
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = InfoExtractor.for_url('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    print(ie._downloader)
    print(ie._match_id)
    print(ie)

# Generated at 2022-06-14 16:18:18.965361
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Test for object constructor."""
    glide = GlideIE(use_proxy=True, proxy_address='127.0.0.1', proxy_port=8080)
    assert (glide.glide_url == 'https://share.glide.me/')

# Generated at 2022-06-14 16:18:23.909823
# Unit test for constructor of class GlideIE
def test_GlideIE():

    glide = GlideIE('GlideIE')
    print(glide._VALID_URL)
    assert glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)', "The _VALID_URL should be defined in class, but the value is not correct."


# Generated at 2022-06-14 16:18:31.915497
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    info = GlideIE()._real_extract(url)
    assert(info)
    assert(info["id"] == "UZF8zlmuQbe4mr+7dCiQ0w==")
    assert(info["title"] == "Damon's Glide message")
    assert(info["url"] == "http://share.glide.me/v/UZF8zlmuQbe4mr+7dCiQ0w==/0/video.mp4")
    assert(info["thumbnail"] == "http://cf.d.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==/0/thumbnail.jpg")

# Generated at 2022-06-14 16:18:32.946044
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE.from_ie('Default')

# Generated at 2022-06-14 16:18:34.022061
# Unit test for constructor of class GlideIE
def test_GlideIE():
    s = GlideIE()

# Generated at 2022-06-14 16:18:37.089741
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    GlideIE()

# Generated at 2022-06-14 16:18:45.625188
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:50.855987
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:18:58.955578
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"

# Generated at 2022-06-14 16:21:21.147466
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:21:32.732385
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:21:37.189935
# Unit test for constructor of class GlideIE
def test_GlideIE():
    x = GlideIE()
    assert x.IE_DESC == 'Glide mobile video messages (glide.me)'

if __name__ == '__main__':
    test_GlideIE()

# Generated at 2022-06-14 16:21:45.032016
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Initial test for the class GlideIE
    """
    assert GlideIE._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    sample_url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    assert GlideIE._match_id(sample_url) == 'UZF8zlmuQbe4mr+7dCiQ0w=='


# Generated at 2022-06-14 16:21:45.804963
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(object)

# Generated at 2022-06-14 16:21:49.104363
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor(None) )._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:21:51.340423
# Unit test for constructor of class GlideIE
def test_GlideIE():
    pass

if __name__ == '__main__':
    # run_all(argv=['-v'])
    test_GlideIE()

# Generated at 2022-06-14 16:21:55.237110
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj == GlideIE()

if __name__ == "__main__":
    #test_GlideIE()
    obj = GlideIE()
    print(obj._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='))

# Generated at 2022-06-14 16:21:57.133800
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert (ie.IE_DESC) == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:21:59.201514
# Unit test for constructor of class GlideIE
def test_GlideIE():
	print ('Running unit test for class GlideIE')
	GlideIE();

# Test method for this file
if __name__ == '__main__':
    test_GlideIE()