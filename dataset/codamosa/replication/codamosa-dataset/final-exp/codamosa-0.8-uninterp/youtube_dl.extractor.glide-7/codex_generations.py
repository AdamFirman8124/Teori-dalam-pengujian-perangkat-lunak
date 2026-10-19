

# Generated at 2022-06-14 16:13:30.620549
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:13:34.564109
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert isinstance(glide_ie, GlideIE)


# Generated at 2022-06-14 16:13:38.089811
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Constructor is needed, since class GlideIE inherits from class InfoExtractor
    constructor = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')



# Generated at 2022-06-14 16:13:46.062625
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info = GlideIE()._download_json(
        'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'UZF8zlmuQbe4mr+7dCiQ0w==')
    assert info['title'] == "Damon's Glide message"
    assert info['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert info['url'] == 'https://d2l6uygi1pgnys.cloudfront.net/UZF8zlmuQbe4mr+7dCiQ0w==/UZF8zlmuQbe4mr+7dCiQ0w==.mp4'

# Generated at 2022-06-14 16:13:57.606226
# Unit test for constructor of class GlideIE
def test_GlideIE():

    exp_GLIDE_URL = r'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    exp_MD5 = '4466372687352851af2d131cfaa8a4c7'
    exp_VIDEO_ID = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    exp_TITLE = "Damon's Glide message"
    exp_THUMBNAIL = r'https?://.+?\.cloudfront\.net/.*\.jpg'
    exp_EXT = 'mp4'

    glide_ie = GlideIE()

    # Assert _VALID_URL
    assert(glide_ie._VALID_URL == GlideIE._VALID_URL)

    # Assert _T

# Generated at 2022-06-14 16:13:59.485833
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video = GlideIE()

    assert video.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:00.706496
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:10.444331
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert GlideIE().suitable('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert not GlideIE().suitable('https://www.glide.me/')
    assert not GlideIE().suitable('http://glide.me/')
    assert not GlideIE().suitable('https://glide.me/')

# Generated at 2022-06-14 16:14:13.601516
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Make sure the description of the class is set correctly
    """
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:16.941192
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC
    assert hasattr(ie, '_VALID_URL')

# Generated at 2022-06-14 16:14:25.349296
# Unit test for constructor of class GlideIE
def test_GlideIE():
    a = GlideIE()
    assert isinstance(a, GlideIE)

# Generated at 2022-06-14 16:14:34.521925
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._TEST['url'] == GlideIE._TEST['url'].decode('utf-8')
    assert GlideIE._TEST['md5'] == GlideIE._TEST['md5'].decode('utf-8')
    assert GlideIE._TEST['info_dict'] == GlideIE._TEST['info_dict'].decode('utf-8')
    assert GlideIE._TEST['info_dict']['title'] == GlideIE._TEST['info_dict']['title'].decode('utf-8')
    return True


# Generated at 2022-06-14 16:14:35.127007
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:36.139827
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:14:36.742835
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:38.973381
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Test case for constructor of class GlideIE.
    """

    assert GlideIE().IE_NAME == 'Glide'

# Generated at 2022-06-14 16:14:40.186492
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('glide')

# Generated at 2022-06-14 16:14:42.005759
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test instantiation
    extractor = GlideIE()
    assert isinstance(extractor, GlideIE)

# Generated at 2022-06-14 16:14:45.594474
# Unit test for constructor of class GlideIE
def test_GlideIE():
	print("Inside function test_GlideIE")
	assert GlideIE(None)._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:14:46.465171
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None) # Just init the class

# Generated at 2022-06-14 16:15:05.917118
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    video_url = 'http://glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='

    GlideIE(video_id, video_url)

# Generated at 2022-06-14 16:15:11.675774
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.set_test('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:15.771352
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ''' Test GlideIE constructor '''
    ie = GlideIE()
    print(ie.IE_NAME)
    print(ie.IE_DESC)
    print(ie._VALID_URL)
    print(ie._TEST)
    #print(ie.__dict__)

test_GlideIE()

# Generated at 2022-06-14 16:15:16.748957
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None)

# Generated at 2022-06-14 16:15:17.611018
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE();
    assert ie

# Generated at 2022-06-14 16:15:18.690633
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:15:24.896268
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie._download_webpage = lambda url, video_id: url
    ie._search_regex = lambda pattern, string, name, default, group: pattern
    ie._html_search_regex = lambda pattern, string, name, default: pattern
    ie._proto_relative_url = lambda url: url
    ie._og_search_thumbnail = lambda webpage: webpage
    ie._og_search_video_url = lambda webpage: webpage
    ie._og_search_title = lambda webpage: webpage
    ie._match_id = lambda url: url
    ie._real_extract(ie._TEST.get('url'))

# Generated at 2022-06-14 16:15:26.285835
# Unit test for constructor of class GlideIE
def test_GlideIE():
    x = GlideIE([])
    assert x is not None

# Generated at 2022-06-14 16:15:28.384595
# Unit test for constructor of class GlideIE
def test_GlideIE():
    g = GlideIE()
    assert g.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:15:30.998043
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert(ie.IE_DESC == 'Glide mobile video messages (glide.me)')

# Generated at 2022-06-14 16:16:02.680126
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    expected = 'share\.glide\.me'
    assert ie._VALID_URL == 'https?://%s/(?P<id>[A-Za-z0-9\-=_+]+)' % expected


# Generated at 2022-06-14 16:16:05.699882
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert GlideIE(GlideIE._downloader)._downloader is GlideIE._downloader
	
if(__name__ == '__main__'):
	test_GlideIE()

# Generated at 2022-06-14 16:16:06.608280
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE

# Generated at 2022-06-14 16:16:08.500287
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE()
    assert glide.IE_NAME == "glide", "Testcase for testing constructor of class GlideIE failed!"


# Generated at 2022-06-14 16:16:10.887697
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test1 = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    print(test1)

# Generated at 2022-06-14 16:16:13.759819
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = InfoExtractor('Glide')
    assert ie is not None
    print("Test Successful")

# Generated at 2022-06-14 16:16:19.495840
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)', ie._VALID_URL


# Generated at 2022-06-14 16:16:25.049704
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_instance = GlideIE()
    assert test_instance.IE_NAME == 'glide'
    assert test_instance.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert test_instance._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:28.356391
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:16:29.817017
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # just a simple sanity check: the class can be instantiated
    ie = GlideIE()
    assert ie is not None

# Generated at 2022-06-14 16:17:12.211374
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:18.986856
# Unit test for constructor of class GlideIE
def test_GlideIE():
    IE = GlideIE()
    assert IE.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert IE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:29.784791
# Unit test for constructor of class GlideIE
def test_GlideIE():
	class_name = GlideIE.__name__
	# Create a new instance
	instance = GlideIE()
	# Check if the `GlideIE` is of type object
	assert isinstance(instance, object)
	# Check if the created instance is of type `GlideIE`
	assert isinstance(instance, GlideIE)
	# Check if the `GlideIE` is a subclass of InfoExtractor
	assert issubclass(GlideIE, InfoExtractor)
	# Check if the constructed `GlideIE` instance is an instance of `InfoExtractor`
	assert isinstance(instance, InfoExtractor)
	# Check if the `GlideIE` instance has at least one attribute
	assert len(dir(instance)) > 0
	# Check if the instances of `GlideIE` have the attribute `_VALID_URL`


# Generated at 2022-06-14 16:17:31.637890
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Returns an instance of class GlideIE
    GlideIE()
    pass

# Generated at 2022-06-14 16:17:33.957638
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(GlideIE.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='))
    return ie

# Generated at 2022-06-14 16:17:35.452804
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Unit test checks the basic functionality to construct the GlideIE object
    GlideIE()

test_GlideIE()

# Generated at 2022-06-14 16:17:36.721229
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:17:37.825619
# Unit test for constructor of class GlideIE
def test_GlideIE():  # basic sanity
    # (check if implementation is up to date with specification)
    pass

# Generated at 2022-06-14 16:17:39.780361
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print ("type of GlideIE: ", type(GlideIE))


# Generated at 2022-06-14 16:17:42.104499
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"



# Generated at 2022-06-14 16:18:58.802381
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor)


# Generated at 2022-06-14 16:18:59.279137
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:00.343251
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print('Testing GlideIE class constructor')
    assert GlideIE()

# Generated at 2022-06-14 16:19:03.282944
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Constructor test the class GlideIE
    """
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:19:03.813606
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:05.567572
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:19:08.522393
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('/share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert hasattr(ie, '_download_webpage')

# Generated at 2022-06-14 16:19:09.685769
# Unit test for constructor of class GlideIE
def test_GlideIE():
    infoExtractor = GlideIE()
    assert (infoExtractor is not None)

# Generated at 2022-06-14 16:19:14.502429
# Unit test for constructor of class GlideIE
def test_GlideIE():
  response_mock = '<source src="http://videos.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==.mp4">'
  assert GlideIE()._search_regex(r'<source[^>]+src=(["\'])(?P<url>.+?)\1', response_mock, 'video URL', default=None, group='url')

# Generated at 2022-06-14 16:19:18.393665
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print (GlideIE()._VALID_URL)
    GlideIE()._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')


# Generated at 2022-06-14 16:22:00.212452
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()
     #print _VALID_URL
    #print _TEST
    #print _TEST1



if __name__ == "__main__":
    test_GlideIE()

# Generated at 2022-06-14 16:22:00.726695
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()

# Generated at 2022-06-14 16:22:01.961932
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:22:03.883929
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("GlideIE")
    ie.IE_DESC
    ie._VALID_URL
    ie._TEST

# Generated at 2022-06-14 16:22:14.703351
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC = 'Glide mobile video messages (glide.me)'
    ie._VALID_URL = r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:16.816067
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:22:18.080837
# Unit test for constructor of class GlideIE
def test_GlideIE():
	video = GlideIE()
	video.download("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:22:18.558268
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:22:29.195457
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide_ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert glide_ie._TEST.get('url') == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert glide_ie._TEST.get('md5') == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:22:31.428514
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert(ie != None)