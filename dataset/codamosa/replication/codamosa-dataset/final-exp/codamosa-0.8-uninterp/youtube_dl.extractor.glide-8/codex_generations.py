

# Generated at 2022-06-14 16:13:30.361850
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:13:33.236045
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE
    obj = ie(None)
    assert(isinstance(obj.IE_DESC, unicode))
    assert(obj.ie_key() == 'Glide')

# Generated at 2022-06-14 16:13:43.656311
# Unit test for constructor of class GlideIE
def test_GlideIE():
    s = GlideIE()
    assert s.IE_NAME == "glide"
    assert s.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert s._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:56.975724
# Unit test for constructor of class GlideIE
def test_GlideIE():
    g  = GlideIE()
    assert g.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert g._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:13:59.101455
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None).IE_DESC == 'Glide mobile video messages (glide.me)'
    

# Generated at 2022-06-14 16:14:04.940985
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Tests that GlideIE constructor doesn't crash
    """
    # pylint: disable=W0612
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr-7dCiQ0w==")
    # pylint: enable=W0612

# Generated at 2022-06-14 16:14:16.486958
# Unit test for constructor of class GlideIE
def test_GlideIE():
    extractor = GlideIE()
    assert extractor.IE_NAME == 'Glide'
    assert extractor.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert extractor._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:19.064142
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj.IE_NAME == 'glide'


# Generated at 2022-06-14 16:14:21.649231
# Unit test for constructor of class GlideIE
def test_GlideIE():
    i = GlideIE();
    assert i.IE_NAME == 'glide';
    assert i.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:14:22.287262
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()

# Generated at 2022-06-14 16:14:27.426204
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE(), InfoExtractor)


# Generated at 2022-06-14 16:14:33.284401
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.ie_key() == 'Glide'
    assert ie.ie_desc == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:14:34.319348
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None)._VALID_URL

# Generated at 2022-06-14 16:14:36.085605
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .test_match import ensure_test_uris
    ensure_test_uris(GlideIE)

# Generated at 2022-06-14 16:14:46.210868
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert_true(ie.get_test() != None)
    assert_equal(ie.get_test()['md5'], '4466372687352851af2d131cfaa8a4c7')
    assert_equal(ie.get_test()['info_dict']['title'], "Damon's Glide message")
    assert_regex(ie.get_test()['info_dict']['thumbnail'], '^https?://.*?\.cloudfront\.net/.*\.jpg$')
    assert_equal(ie.get_test()['info_dict']['id'], 'UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:14:55.451169
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:14:56.567629
# Unit test for constructor of class GlideIE
def test_GlideIE():
	glide = GlideIE()
	test = glide.test()
	print(test)

# Generated at 2022-06-14 16:14:59.681060
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().IE_NAME == 'Glide'
    assert GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE()._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert GlideIE()._TEST

# Generated at 2022-06-14 16:15:00.512557
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:02.721704
# Unit test for constructor of class GlideIE
def test_GlideIE():
    tester = GlideIE()
    assert tester is not None

# Generated at 2022-06-14 16:15:19.346351
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Check if the class is constructable
    ie = GlideIE()

    # Check if the IE name is correct
    assert ie.IE_NAME == 'Glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:23.562513
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # This test is to verify that the constructor of GlideIE class behaves properly when invoked as follow:
    # GlideIE()
    # The constructor is expected to throw an exception as no site name is provided
    try:
        # Call the constructor explicitly without a site name
        GlideIE()
    except Exception:
        # Make sure that the exception is raised as expected
        assert True
    finally:
        assert True

# Generated at 2022-06-14 16:15:26.546570
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE()
    assert (glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')

# Generated at 2022-06-14 16:15:36.740835
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glideIE = GlideIE()
    assert glideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:37.973030
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().ie_key() == 'Glide'

# Generated at 2022-06-14 16:15:47.529134
# Unit test for constructor of class GlideIE
def test_GlideIE():
    d = GlideIE()
    assert d._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert d._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert d._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert d._TEST['info_dict']['ext'] == 'mp4'
    assert d._TEST['info_dict']['title'] == "Damon's Glide message"

# Generated at 2022-06-14 16:15:48.348678
# Unit test for constructor of class GlideIE
def test_GlideIE():
	GlideIE(None, None)


# Generated at 2022-06-14 16:16:00.661722
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    obj = ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert obj['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert obj['url'] == 'https://d1x7u8b1z8ul7d.cloudfront.net/message/UZF8zlmuQbe4mr+7dCiQ0w==/0.mp4'
    assert obj['thumbnail'] == 'https://d1x7u8b1z8ul7d.cloudfront.net/message/UZF8zlmuQbe4mr+7dCiQ0w==/profile.jpg'

# Generated at 2022-06-14 16:16:02.207794
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:16:03.644238
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE() == GlideIE(InfoExtractor)


# Generated at 2022-06-14 16:16:18.586495
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:16:20.666693
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract(GlideIE._TEST['url'])

# Generated at 2022-06-14 16:16:23.694678
# Unit test for constructor of class GlideIE
def test_GlideIE():
    '''
    Test for constructor of class GlideIE
    :return: None
    '''

    glideIE = GlideIE()
    assert (glideIE.extractor_key == 'glide')

# Generated at 2022-06-14 16:16:26.208066
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:32.329053
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

    # Valid URL
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

    # Valid list of formats
    assert ie._formats == ['HD', 'SD']

    # Valid age limit for Glide website
    assert ie._GEO_BYPASS == False

    # Valid list of extractors
    assert ie._ies == ['Glide', 'GlideMobile', 'GlideMobileIOS', 'GlideMobileAndroid']

# Generated at 2022-06-14 16:16:34.558931
# Unit test for constructor of class GlideIE
def test_GlideIE():
    return GlideIE()._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:37.408999
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_class = GlideIE(0)
    assert test_class.__class__ is GlideIE

test_class = GlideIE(0)
assert test_class.__class__ is GlideIE

# Generated at 2022-06-14 16:16:38.676681
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:16:44.907036
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test GlideIE for constructor with valid url
    glide_ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert glide_ie.url_result() == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='

    # Test GlideIE for constructor with invalid url
    try:
        GlideIE('http://www.youtube.com/watch?v=BaW_jenozKc')
    except TypeError as e:
        assert isinstance(e, TypeError)

# Generated at 2022-06-14 16:16:46.280619
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert(ie.IE_DESC == 'Glide mobile video messages (glide.me)')


# Generated at 2022-06-14 16:17:15.244482
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert('GlideIE' in globals())

# Generated at 2022-06-14 16:17:27.135638
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:27.747235
# Unit test for constructor of class GlideIE
def test_GlideIE():
	GlideIE()

# Generated at 2022-06-14 16:17:30.056047
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:17:32.204683
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor for class GlideIE."""
    GlideIE(None)._real_extract(None)

# Generated at 2022-06-14 16:17:33.596981
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide_ie = GlideIE()
    assert isinstance(glide_ie, InfoExtractor)


# Generated at 2022-06-14 16:17:34.418460
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:17:35.390743
# Unit test for constructor of class GlideIE
def test_GlideIE():
	ie=GlideIE()

# Generated at 2022-06-14 16:17:35.989607
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:17:36.632650
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:18:11.166687
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE().IE_DESC, str)


# Generated at 2022-06-14 16:18:15.179591
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:18:19.290625
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:18:20.199913
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None)


# Generated at 2022-06-14 16:18:24.471198
# Unit test for constructor of class GlideIE
def test_GlideIE():
    '''
    Unit test for constructor of class GlideIE
    '''
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST

# Generated at 2022-06-14 16:18:27.330243
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(GlideIE._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')

# Generated at 2022-06-14 16:18:28.424325
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE().IE_DESC, str)

# Generated at 2022-06-14 16:18:29.731485
# Unit test for constructor of class GlideIE
def test_GlideIE():
	test = GlideIE()
	test.test()



# Generated at 2022-06-14 16:18:32.195882
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE.GlideIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:18:34.731543
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE();
    except Exception:
        return False;
    else:
        return True;

# Generated at 2022-06-14 16:19:14.021452
# Unit test for constructor of class GlideIE
def test_GlideIE():
    return GlideIE()


# Generated at 2022-06-14 16:19:14.857322
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE == type(GlideIE())

# Generated at 2022-06-14 16:19:17.242029
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE()
        # This line is not reached if an error is raised.
        return True
    except:
        return False


# Generated at 2022-06-14 16:19:18.377827
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_obj = GlideIE()
    test_obj.suite()

# Generated at 2022-06-14 16:19:27.328974
# Unit test for constructor of class GlideIE
def test_GlideIE():

    # Testing the initializer
    # Create the GlideIE object
    glide = GlideIE()

    # Make sure the instance of the class is not null
    assert glide != None

    # Make sure the IE name is Glide
    assert glide.IE_NAME == 'Glide'

    # Make sure the IE description is Glide mobile video messages (glide.me)
    assert glide.IE_DESC == 'Glide mobile video messages (glide.me)'

    # Make sure the format is null
    assert glide.format == None

    # Make sure the format ID is null
    assert glide.format_id == None

    # Make sure the video title is null
    assert glide.title == None

    # Make sure the video description is null
    assert glide.description == None

    # Make sure the video URL is null
    assert glide.url == None

# Generated at 2022-06-14 16:19:30.687539
# Unit test for constructor of class GlideIE
def test_GlideIE():
    inst = GlideIE(InfoExtractor)
    assert isinstance(inst, InfoExtractor)
    assert inst._VALID_URL == GlideIE._VALID_URL
    assert inst._TEST == GlideIE._TEST

# Generated at 2022-06-14 16:19:38.622284
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print('Testing GlideIE object')
    ie_obj = GlideIE()
    print('  Testing %s object' % ie_obj)
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    expected_ie = 'Glide mobile video messages (glide.me)'
    print('  Input URL: %s; Expected ie_key: %s' % (url, expected_ie))
    actual_ie = ie_obj.suitable(url)
    print('  Actual ie_key: %s' % actual_ie)
    if actual_ie != expected_ie:
        print('Test FAILED')
    else:
        print('Test PASSED')

# Generated at 2022-06-14 16:19:41.194382
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ''' Unit test for constructor of class GlideIE '''
    glide = GlideIE()
    assert glide.IE_NAME == 'glide'
    assert glide.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:19:47.623422
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .mock import fake
    from .util import mock
    from .util.unittest_ import TestCase

    t = TestCase()

    ie = GlideIE(fake.FakeYDL({}))

    assert not ie.suitable('http://www.glide.me/')
    assert ie.suitable('http://share.glide.me/')
    assert ie.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')


# Generated at 2022-06-14 16:19:57.206236
# Unit test for constructor of class GlideIE
def test_GlideIE():
	glide = GlideIE(None)
	assert(glide._TEST == {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'md5': '4466372687352851af2d131cfaa8a4c7',
        'info_dict': {
            'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
            'ext': 'mp4',
            'title': "Damon's Glide message",
            'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
        }
    }) 
	


# Generated at 2022-06-14 16:21:21.023929
# Unit test for constructor of class GlideIE
def test_GlideIE():
    e = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    e._download_webpage
    assert e._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:21:28.007004
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """ test for the constructor of class GlideIE """
    
    glide_ie = GlideIE()
    assert glide_ie.ie_key() == 'Glide'
    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert glide_ie.ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:21:35.932758
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE('test')
    assert obj.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert obj._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert obj._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert obj._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:21:46.304879
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Basic test for class GlideIE"""
    GlideIE(None)._download_webpage('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'UZF8zlmuQbe4mr+7dCiQ0w==')
    GlideIE(None)._download_webpage('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:21:48.377756
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:21:48.919977
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:21:50.386148
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert isinstance(instance, GlideIE)

# Generated at 2022-06-14 16:21:52.064598
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor)._VALID_URL == GlideIE._VALID_URL

# Generated at 2022-06-14 16:21:53.759935
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:21:54.255350
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE