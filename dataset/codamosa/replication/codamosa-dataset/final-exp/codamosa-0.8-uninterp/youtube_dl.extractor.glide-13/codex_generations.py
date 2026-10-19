

# Generated at 2022-06-14 16:13:29.504888
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie != None

test_GlideIE()


# Generated at 2022-06-14 16:13:31.591375
# Unit test for constructor of class GlideIE
def test_GlideIE():
	# Return value is of type GlideIE
	assert GlideIE.__name__ == 'GlideIE'

# Generated at 2022-06-14 16:13:33.232772
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('Glide')


# Generated at 2022-06-14 16:13:36.781600
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print("Testing GlideIE constructor")
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:13:38.898618
# Unit test for constructor of class GlideIE
def test_GlideIE():
    Glide_IE = GlideIE()
    Glide_IE.ie_key()
    Glide_IE.extractor()

# Generated at 2022-06-14 16:13:42.616617
# Unit test for constructor of class GlideIE
def test_GlideIE():
    t = GlideIE()
    assert t._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    

# Generated at 2022-06-14 16:13:44.379673
# Unit test for constructor of class GlideIE
def test_GlideIE():
    x = GlideIE()
    assert x.IE_DESC



# Generated at 2022-06-14 16:13:57.297020
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC = "Glide mobile video messages (glide.me)"
    ie.validateURL = r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:59.100184
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert(ie.IE_NAME == 'glide')



# Generated at 2022-06-14 16:14:00.702738
# Unit test for constructor of class GlideIE
def test_GlideIE():
    return GlideIE()._test_extraction()

# Generated at 2022-06-14 16:14:16.240514
# Unit test for constructor of class GlideIE
def test_GlideIE():
    #test GlideIE constructor
    test_video_url = "https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    glide_ie = GlideIE()
    assert glide_ie._VALID_URL == GlideIE._VALID_URL
    assert glide_ie._TEST == GlideIE._TEST
    assert glide_ie.IE_DESC == GlideIE.IE_DESC
    assert glide_ie.suitable(test_video_url) == True
    #test for '_real_extract' function
    video_url = "https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    video_id = glide_ie._match_id(video_url)
    webpage

# Generated at 2022-06-14 16:14:18.463186
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()._download_webpage('mock', 'mock')

# Generated at 2022-06-14 16:14:27.254945
# Unit test for constructor of class GlideIE
def test_GlideIE():
    class_ = GlideIE()
    assert class_
    assert class_.IE_NAME == 'Glide'
    assert class_.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert class_._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:28.828099
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:14:32.141803
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == GlideIE.IE_NAME
    assert ie.IE_DESC == GlideIE.IE_DESC
    assert ie._VALID_URL == GlideIE._VALID_URL
    assert ie._TEST == GlideIE._TEST

# Generated at 2022-06-14 16:14:33.835983
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_test = GlideIE()
    
# Test for _real_extract method of class GlideIE

# Generated at 2022-06-14 16:14:37.499575
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glideIE = GlideIE()
    assert(glideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    assert(glideIE.IE_DESC == 'Glide mobile video messages (glide.me)')

# Generated at 2022-06-14 16:14:38.568371
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE == type(GlideIE({}))

# Generated at 2022-06-14 16:14:41.400782
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.download("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:14:51.147103
# Unit test for constructor of class GlideIE
def test_GlideIE():
  print ("Testing GlideIE class")
  
  #Constructor with URL as first argument
  url = "http://share.glide.me/UZF8zlmuQbe4mr%2B7dCiQ0w==";
  glideIE = GlideIE(url)
  print ("GlideIE object created")
  
  #constructor with URL as first argument
  glideIE = GlideIE(url)
  print ("GlideIE object created")
  
  #constructor with URL as second argument
  glideIE = GlideIE(url_package={'url':url})
  print ("GlideIE object created")
  
  #constructor with both arguments
  glideIE = GlideIE(url, url_package={'url':url})
  print ("GlideIE object created")

# Generated at 2022-06-14 16:15:00.094457
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:10.740278
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Unit test for the file not found error
    globals()['GlideIE']._download_webpage = \
        lambda self, url, video_id: self._downloader.http_HEAD(url)
    globals()['GlideIE']._download_webpage.__name__ = \
        lambda self, url, video_id: self._downloader.http_HEAD.__name__
    ie = globals()['GlideIE'](None)
    ie._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:16.827192
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_Obj = GlideIE("url")
    assert test_Obj.ie_key() == 'Glide'
    expected_obj = GlideIE("url")
    assert test_Obj._downloader==expected_obj._downloader
    assert test_Obj._match_id("https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==") == "UZF8zlmuQbe4mr+7dCiQ0w=="

# Generated at 2022-06-14 16:15:18.734799
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert('GlideIE' == type(GlideIE({'test': 'test'})).__name__)


# Generated at 2022-06-14 16:15:20.552543
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:15:23.593671
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:15:25.605799
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        assert(GlideIE)
    except NameError:
        raise AssertionError("Class 'GlideIE' not found")
    assert(isinstance(GlideIE, type))


# Generated at 2022-06-14 16:15:28.488330
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:32.545407
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE(None) # test constructor of class GlideIE
    except Exception as e:
        assert True == False, "Error raised unexpected: %s"%(str(e))
    assert True == True, "Error not raised"


# Generated at 2022-06-14 16:15:41.829355
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:16:06.269783
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert video.download() == "4466372687352851af2d131cfaa8a4c7"
    video = GlideIE("share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert video.download() == "4466372687352851af2d131cfaa8a4c7"
    video = GlideIE("share.glide.me/5f7VuS5NxIRLd+WQ9J4mkQ")
    assert video.download() == "8f0f719f5e5c262ab7a937ac07fde732"

# Generated at 2022-06-14 16:16:09.453076
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None, 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    title = ie.extract_info()['title']
    assert title == "Damon's Glide message"

# Generated at 2022-06-14 16:16:13.606455
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.initialize_test_info()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:14.288770
# Unit test for constructor of class GlideIE
def test_GlideIE():
    return GlideIE()

# Generated at 2022-06-14 16:16:25.438433
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.IE_NAME == 'Glide'
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:28.368606
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:28.890707
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:30.927533
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:16:34.601522
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    try:
        GlideIE(url)
    except Exception as e:
        print("Unit test for GlideIE failed: " % (e))
        return False
    return True

# Generated at 2022-06-14 16:16:36.762407
# Unit test for constructor of class GlideIE
def test_GlideIE():
    yt = GlideIE()
    assert(yt.IE_DESC == 'Glide mobile video messages (glide.me)')

# Generated at 2022-06-14 16:17:07.702577
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:17:09.472759
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()._test_extractor(GlideIE._TEST)

# Generated at 2022-06-14 16:17:17.487969
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info_extractor = GlideIE()
    assert info_extractor.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert info_extractor._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:28.782888
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:37.358138
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:40.314473
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert instance.ie_key() == 'Glide'
    assert instance.ie_desc() == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:17:44.219025
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    webpage = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    result = ie._download_webpage(webpage, 'UZF8zlmuQbe4mr+7dCiQ0w==')
    assert result == None

# Generated at 2022-06-14 16:17:49.170101
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None)
    params = {'extractor_key': 'GlideIE', 'IE_DESC': 'Glide mobile video messages (glide.me)', '_VALID_URL': 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'}
    for key, value in params.items():
        assert ie.__getattribute__(key) == value

# Generated at 2022-06-14 16:17:52.851534
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for the constructor of class GlideIE"""
    # TODO: improve the unit test
    glide_ie = GlideIE()
    assert isinstance(glide_ie, InfoExtractor)

# Generated at 2022-06-14 16:17:54.161640
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    GlideIE()
    return

# Generated at 2022-06-14 16:19:09.290354
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Check that only registered IEs can be used
    GlideIE(InfoExtractor)

    # Check that only a single IE can be registered for a class
    GlideIE(InfoExtractor)

# Generated at 2022-06-14 16:19:11.958324
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    from . import GlideIE
    glide_ie = GlideIE(None)
    assert isinstance(glide_ie, GlideIE)

# Generated at 2022-06-14 16:19:18.340758
# Unit test for constructor of class GlideIE
def test_GlideIE():

    # pylint: disable=maybe-no-member
    assert isinstance(GlideIE, type), 'Class instantiated.'

    # pylint: disable=maybe-no-member
    assert isinstance(GlideIE.__name__, str), 'String returned.'
    assert isinstance(GlideIE.IE_NAME, unicode), 'Unicode string returned.'
    assert isinstance(GlideIE.IE_DESC, unicode), 'Unicode string returned.'
    assert isinstance(GlideIE._VALID_URL, unicode), 'Unicode string returned.'

# Generated at 2022-06-14 16:19:19.148327
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(GlideIE({}) is not None)

# Generated at 2022-06-14 16:19:20.837479
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:19:26.560606
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        from youtube_dl.extractor.glide import GlideIE
    except:
        print("Failed to import GlideIE from glide")
        return
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie.IE_DESC == "Glide mobile video messages (glide.me)"
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_NAME == "glide"

# Generated at 2022-06-14 16:19:27.864035
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("GlideIE", "Glide mobile video messages")

# Generated at 2022-06-14 16:19:28.426479
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:29.744987
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:19:32.762323
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = GlideIE.IE_DESC
    e = GlideIE(url)
    #print e.IE_DESC
    assert e.IE_DESC == GlideIE.IE_DESC

# Generated at 2022-06-14 16:22:18.001036
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    # test properties
    assert obj.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:22:19.105838
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:22:25.958361
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    ie = GlideIE()

# Generated at 2022-06-14 16:22:36.397313
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert obj.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:22:45.796844
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE(1)
    # Test of method '_real_extract'

# Generated at 2022-06-14 16:22:47.106811
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie != None, "Object creation failed"

# Generated at 2022-06-14 16:22:48.284923
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj != None

# Generated at 2022-06-14 16:22:50.768878
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Creates GlideIE object to be used for testing other functions"""       
    ie = GlideIE()
    assert isinstance(ie, GlideIE)


# Generated at 2022-06-14 16:22:53.823515
# Unit test for constructor of class GlideIE
def test_GlideIE():
	# test an invalid URL
	invalidURL = 'http://share.glide.me/'
	try:
		GlideIE()._real_extract(invalidURL)
	except Exception as e:
		assert isinstance(e, AssertionError)

# Generated at 2022-06-14 16:22:57.444267
# Unit test for constructor of class GlideIE
def test_GlideIE():
    IEC = GlideIE()
    assert IEC.IE_NAME == "Glide"
    assert IEC.IE_DESC == "Glide mobile video messages (glide.me)"
    assert IEC._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
