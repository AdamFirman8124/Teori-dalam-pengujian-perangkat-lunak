

# Generated at 2022-06-14 16:13:29.630677
# Unit test for constructor of class GlideIE
def test_GlideIE():
	glide = GlideIE()
	glide.extract()

# Generated at 2022-06-14 16:13:30.409250
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:13:31.546356
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:13:38.851798
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # The parameters of the constructor of class InfoExtractor are:
    # downloader, ie_key, ie_name, ie_id, ie_desc
    ie = GlideIE(None, None, None, None, None)
    # The regular expression is identical to the one in the _TEST dict
    # in this test module
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'



# Generated at 2022-06-14 16:13:40.810999
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert 'glide.me' in GlideIE.ie_keywords()

# Generated at 2022-06-14 16:13:41.731424
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert instance is not None

# Generated at 2022-06-14 16:13:42.315960
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:13:46.304695
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Unit test for constructor of class GlideIE
    :return: None
    """
    assert GlideIE(InfoExtractor)._WORKING

# Generated at 2022-06-14 16:13:48.293063
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # just check if GlideIE constructor is working
    assert isinstance(GlideIE(''), InfoExtractor)

# Generated at 2022-06-14 16:13:59.134273
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert ie._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:14:04.004733
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None).IE_NAME == 'glide'


# Generated at 2022-06-14 16:14:11.448804
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF9zlmuQbe4mr+7dCiQ0w==")
    assert ie._VALID_URL == "http://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)"
    assert ie.IE_DESC == "Glide mobile video messages (glide.me)"

# Generated at 2022-06-14 16:14:17.830635
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Call the constructor of class GlideIE
    This function do not invoke any function of class GlideIE,
    thus it will not affect the function of class GlideIE.
    """
    GlideIE('test', ('None', 'None'), 'None')

# Generated at 2022-06-14 16:14:27.023318
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # First test: constructor and "extract" method
    from .common import GlideIE
    assert isinstance(GlideIE, type)
    assert issubclass(GlideIE, InfoExtractor)
    ie = GlideIE()
    assert isinstance(ie, InfoExtractor)
    assert hasattr(ie, '_WORKING')
    assert hasattr(ie, '_downloader')
    assert hasattr(ie, '_download_webpage_handle')
    assert hasattr(ie, '_download_webpage_handle')
    assert hasattr(ie, 'report_warning')
    assert hasattr(ie, 'report_error')
    assert hasattr(ie, 'report_extraction')
    assert hasattr(ie, '_HEADERS')
    assert hasattr(ie, '_html_search_regex')


# Generated at 2022-06-14 16:14:38.136753
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_GlideIE = GlideIE(None)
    assert test_GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:40.663848
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:43.493109
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info_extractor = GlideIE()

    assert info_extractor.IE_NAME == 'glide'
    assert info_extractor.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:14:46.139448
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # check for exceptions
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:14:49.071477
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_GlideIE = GlideIE()
    assert isinstance(test_GlideIE, InfoExtractor)

# Code to test if instance of class GlideIE is created and verifying its validity

# Generated at 2022-06-14 16:14:51.180364
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # assert that GlideIE() is an instance of the class InfoExtractor.
    assert isinstance(GlideIE(), InfoExtractor)


# Generated at 2022-06-14 16:15:00.665896
# Unit test for constructor of class GlideIE
def test_GlideIE():
    global GlideIE
    ie = GlideIE()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:13.643601
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert instance.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert instance._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:15.167019
# Unit test for constructor of class GlideIE
def test_GlideIE():
    infoExtractor = GlideIE()
    print(infoExtractor)

# Generated at 2022-06-14 16:15:15.731480
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:18.735115
# Unit test for constructor of class GlideIE
def test_GlideIE():
	url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
	result = GlideIE._real_extract(url)
	print(result)


# Generated at 2022-06-14 16:15:19.268191
# Unit test for constructor of class GlideIE
def test_GlideIE():
    pass

# Generated at 2022-06-14 16:15:20.991483
# Unit test for constructor of class GlideIE
def test_GlideIE():
    gl = GlideIE("test")
    assert gl.IE_DESC == "Glide mobile video messages (glide.me)"

# Generated at 2022-06-14 16:15:24.350481
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert instance.IE_NAME == 'glide'
    assert instance.IE_DESC == 'Glide mobile video messages (glide.me)'



# Generated at 2022-06-14 16:15:26.909119
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test for proper object construction
    ie = GlideIE()
    assert ie.IE_DESC == "Glide mobile video messages (glide.me)"


# Generated at 2022-06-14 16:15:28.620735
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    print(instance)


# Generated at 2022-06-14 16:15:35.790488
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:38.053003
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    GlideIE().url_result(url)

# Generated at 2022-06-14 16:15:47.605879
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:50.451863
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Assert that the class is successfully created with a valid url
    glideIE = GlideIE()
    assert glideIE is not None, "Creation of GlideIE object failed"
    assert glideIE._VALID_URL is not None, "Creation object has no valid URL"

# Unit tests for class GlideIE

# Generated at 2022-06-14 16:15:51.420519
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(InfoExtractor())

# Generated at 2022-06-14 16:15:52.299626
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()

# Generated at 2022-06-14 16:15:53.521237
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:16:05.700952
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # test supported urls
    assert GlideIE._VALID_URL == GlideIE._TEST['url']
    assert GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert GlideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert GlideIE._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert GlideIE._TEST['info_dict']['ext'] == 'mp4'
    assert GlideIE._TEST['info_dict']['title'] == "Damon's Glide message"
    assert Gl

# Generated at 2022-06-14 16:16:06.726061
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(dict())


# Generated at 2022-06-14 16:16:16.883346
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Test for constructor of class GlideIE
    Also run a unit test for methods: _extract_video_id, _extract_video_info, _extract_video_url
    """
    import unittest
    import doctest
    try:
        from urlparse import urlparse
        from urlparse import parse_qs
        from urlparse import parse_qsl # pylint: disable=E0611
    except ImportError:
        from urllib.parse import urlparse
        from urllib.parse import parse_qs
        from urllib.parse import parse_qsl # pylint: disable=E0611

    GlideIE.IE_DESC = 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:16:32.988619
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # ie = GlideIE()
    ie = InfoExtractor(GlideIE())
    ie.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:33.509193
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:16:35.393388
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE(InfoExtractor())
    except:
        raise AssertionError("Failed to create instance of GlideIE")

# Generated at 2022-06-14 16:16:38.637589
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.get_format({'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='})

# Generated at 2022-06-14 16:16:43.371751
# Unit test for constructor of class GlideIE
def test_GlideIE():
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    ie_obj = GlideIE(url)
    ie_obj.extract(url)

# Generated at 2022-06-14 16:16:51.284192
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC = 'Glide mobile video messages (glide.me)'
    ie._VALID_URL = ie.IE_DESC

# Generated at 2022-06-14 16:16:52.972860
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert(ie.IE_DESC == 'Glide mobile video messages (glide.me)')

# Generated at 2022-06-14 16:17:02.419191
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('asd','123')
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:09.449950
# Unit test for constructor of class GlideIE
def test_GlideIE():
    i = GlideIE()
    assert i.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert i._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert i._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert i._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:17:11.054586
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert hasattr(GlideIE, "_download_webpage")
    assert hasattr(GlideIE, "_match_id")
    assert hasattr(GlideIE, "_real_extract")

# Generated at 2022-06-14 16:17:43.847971
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    GlideIE()._real_extract(url)

test_GlideIE()

# Generated at 2022-06-14 16:17:48.536847
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .helper import _assert_valid_url
    _assert_valid_url(GlideIE, 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    _assert_valid_url(GlideIE, 'http://share.glide.me/dDtTj79tVuFxm9Ep7Vk-Yw==')


# Generated at 2022-06-14 16:17:50.883094
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:17:57.787608
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    assert(GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(GlideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7')

# Generated at 2022-06-14 16:17:59.376257
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor())._VALID_URL == GlideIE._VALID_URL

# Generated at 2022-06-14 16:18:05.030659
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    # TODO: Test _TEST
    # assert ie._TEST == 'TODO'


# Generated at 2022-06-14 16:18:15.165873
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert (GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    assert (GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)')
    assert (GlideIE._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert (GlideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7')
    assert (GlideIE._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:18:18.223825
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:18:19.172975
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:18:21.905396
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie._downloader = object()
    ie.url = ''
    ie.ie_key = 'GlideIE'
    ie.suitable = lambda x: True
    ie.initialize()

# Generated at 2022-06-14 16:19:40.697856
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test = {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'md5': '4466372687352851af2d131cfaa8a4c7',
        'info_dict': {
            'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
            'ext': 'mp4',
            'title': "Damon's Glide message",
            'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
        }
    }
    return GlideIE()._real_extract(test['url'])

# Generated at 2022-06-14 16:19:41.242486
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:46.260793
# Unit test for constructor of class GlideIE
def test_GlideIE():
	assert GlideIE().IE_DESC == 'Glide mobile video messages (glide.me)'
	assert GlideIE()._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:19:49.073953
# Unit test for constructor of class GlideIE
def test_GlideIE():
    IE = GlideIE()
    assert IE._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:19:59.921442
# Unit test for constructor of class GlideIE
def test_GlideIE():
    #Arrange
    from glide import GlideIE
    from .common import InfoExtractor
    from .common import InfoExtractor
    from .common import InfoExtractor
    from .common import InfoExtractor
    from .common import InfoExtractor

    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    url = 'http://share.glide.me/' + video_id
    webpage = '<source src="https://share.glide.me/v1/videos/' + video_id + '" type="video/mp4"></source>'
    expected_video_url = 'https://share.glide.me/v1/videos/' + video_id

    #Act
    result = GlideIE()

    #Assert
    assert result is not None

# Generated at 2022-06-14 16:20:06.903513
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert obj._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:20:10.334466
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE().extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')


# Generated at 2022-06-14 16:20:13.507948
# Unit test for constructor of class GlideIE
def test_GlideIE():
    print("Testing GlideIE constructor")
    try:
        GlideIE()._download_webpage("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==", "UZF8zlmuQbe4mr+7dCiQ0w==")
        print("Constructor GlideIE passed.")
    except:
        print("Constructor GlideIE failed.")


# Generated at 2022-06-14 16:20:18.192895
# Unit test for constructor of class GlideIE
def test_GlideIE():
    for url in ["http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==", "http://share.glide.me/R_N5cAjNQq3-4L-DSP7eOA=="]:
        ie = GlideIE(u"http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
        ie.extract(url)

# Generated at 2022-06-14 16:20:19.200386
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:22:56.433652
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:23:00.430153
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # To test with a self-made Glide message, replace the following link with your own Glide file
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    GlideIE().extract(url)
    return

# Generated at 2022-06-14 16:23:01.244630
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:23:02.066459
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()

# Generated at 2022-06-14 16:23:02.896938
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:23:08.942918
# Unit test for constructor of class GlideIE
def test_GlideIE():
	ie = GlideIE()
	#assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
	assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
	return ie

# Generated at 2022-06-14 16:23:19.097505
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ie.IE_NAME == 'glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:23:22.877124
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Tests constructor of class GlideIE to see if object is correctly constructed.
    """
    instance = GlideIE({})
    assert isinstance(instance, GlideIE)


# Generated at 2022-06-14 16:23:25.838392
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Simple test case to verify that Glide constructor is working
    """
    # Construct an object to test
    glideIE = GlideIE()
    # Make sure that it is working
    assert glideIE