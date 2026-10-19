

# Generated at 2022-06-14 16:13:28.180614
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert(obj.IE_DESC == "Glide mobile video messages (glide.me)")


# Generated at 2022-06-14 16:13:32.356693
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Unit tests for constructor of GlideIE class.
    """
    print("Running GlideIE unit tests")
    glide_ie = GlideIE(None)
    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    glide_ie = GlideIE('Glide mobile video messages (glide.me)')
    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    print("All unit tests passed!")

# Generated at 2022-06-14 16:13:33.668394
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:13:35.704833
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE('GlideIE').IE_NAME == 'Glide'

# Generated at 2022-06-14 16:13:38.984815
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        _ = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    except Exception:
        raise AssertionError('Failed to instantiate GlideIE')

# Generated at 2022-06-14 16:13:39.736509
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:13:50.314532
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info = GlideIE().extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert info['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert info['url'] == 'https://s3.amazonaws.com/share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==.mp4', info['url']
    assert info['thumbnail'] == 'https://s3.amazonaws.com/s.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==.jpg', info['thumbnail']
    assert info['title'] == "Damon's Glide message"

# Generated at 2022-06-14 16:13:55.367275
# Unit test for constructor of class GlideIE
def test_GlideIE():
  #pylint: disable=redefined-outer-name
  url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
  glideIE = GlideIE()
  #pylint: enable=redefined-outer-name

# Generated at 2022-06-14 16:13:57.605896
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        GlideIE()
    except:
        assert False, 'GlideIE() constructor raises exception'


# Generated at 2022-06-14 16:14:10.868569
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://www.example.com')
    assert isinstance(ie, InfoExtractor)
    ae = assert_equal
    ae(ie.IE_NAME, 'GlideIE')
    ae(ie.IE_DESC, 'Glide mobile video messages')
    ae(ie._VALID_URL, 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    ae(ie._TEST['url'], 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    ae(ie._TEST['md5'], '4466372687352851af2d131cfaa8a4c7')

# Generated at 2022-06-14 16:14:20.327477
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract(GlideIE._TEST['url'])
    assert(ie.extract(GlideIE._TEST['url']) == GlideIE._TEST)

# Generated at 2022-06-14 16:14:21.317521
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:14:22.745533
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    assert GlideIE

# Generated at 2022-06-14 16:14:27.167513
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:14:31.427875
# Unit test for constructor of class GlideIE
def test_GlideIE():    
    from unit import Unit
    glide_ie = GlideIE()
    unit = Unit('glide')
    unit.add('instantiate', glide_ie is not None)
    glide_ie.close()
    unit.report()

# Generated at 2022-06-14 16:14:32.835400
# Unit test for constructor of class GlideIE
def test_GlideIE():
    gl = GlideIE()
    assert(gl == GlideIE)

# Generated at 2022-06-14 16:14:34.806640
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE()
    assert isinstance(glide, InfoExtractor)


# Generated at 2022-06-14 16:14:40.963228
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Object creation
    ie = GlideIE()
    # Tests
    ie.extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    ie.extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    ie.extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    ie.extract("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:14:49.759582
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_ie = GlideIE()
    assert test_ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert test_ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:52.546635
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==", {}) is not None

# Generated at 2022-06-14 16:15:00.504795
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE(), InfoExtractor)


# Generated at 2022-06-14 16:15:08.344739
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glideIE = GlideIE()
    assert glideIE._VALID_URL == "https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)", "Invalid url pattern"
    assert glideIE.IE_DESC == "Glide mobile video messages (glide.me)", "Invalid IE description"

# Constructor of class GlideIE is already tested
# Testing extract

# Generated at 2022-06-14 16:15:17.491503
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    # The extractor does not accept URLs with the http protocol
    assert ie.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') is False
    # The extractor accepts only URLs with the https protocol
    assert ie.suitable('https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') is True
    # The extractor does not accept URLs with a different host
    assert ie.suitable('https://glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') is False

# Generated at 2022-06-14 16:15:19.068008
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:15:22.506959
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Test constructor of GlideIE"""

    glide_ie = GlideIE()

    expected_result = "Glide mobile video messages (glide.me)"
    result = glide_ie.IE_DESC

    assert result == expected_result

# Test _real_extract method of GlideIE

# Generated at 2022-06-14 16:15:24.590085
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(None, None)._VALID_URL == GlideIE._VALID_URL

# Generated at 2022-06-14 16:15:29.073874
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = GlideIE._VALID_URL
    # Regular Expression object
    import re
    m = re.match(url, 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    print(m.group(1))

# Generated at 2022-06-14 16:15:38.729235
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_DESC = 'Glide mobile video messages (glide.me)'
    ie._VALID_URL = 'https://share.glide.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:40.259380
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:41.306090
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()

# Generated at 2022-06-14 16:15:57.441136
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:00.522033
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Unit test for constructor of class GlideIE
    """
    # Check whether constructor of class GlideIE works
    glide_ie = GlideIE()
    assert(glide_ie)


# Generated at 2022-06-14 16:16:03.372512
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:16:10.509377
# Unit test for constructor of class GlideIE
def test_GlideIE():
    result = GlideIE()
    assert result.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert result._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert result._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert result._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'



# Generated at 2022-06-14 16:16:11.821653
# Unit test for constructor of class GlideIE
def test_GlideIE():
    glide = GlideIE()


# Generated at 2022-06-14 16:16:14.275387
# Unit test for constructor of class GlideIE
def test_GlideIE():
    tester = GlideIE()
    tester.assure_working()
# Test the constructor of class GlideIE

# Generated at 2022-06-14 16:16:14.871335
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE is GlideIE

# Generated at 2022-06-14 16:16:21.731086
# Unit test for constructor of class GlideIE
def test_GlideIE():

    # global GlideIE
    # GlideIE = __import__('GlideIE').GlideIE
    glide = GlideIE() #we are not passing the value to 'url' because we already declared it in class

    #url input
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    result = glide.extract(url)


# Generated at 2022-06-14 16:16:22.810865
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE() is not None


# Generated at 2022-06-14 16:16:24.725758
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    # constructor without any argument
    GlideIE()

# Generated at 2022-06-14 16:16:48.152592
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # test for url: http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==
    ogv_test = GlideIE(url="http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert ogv_test.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ogv_test._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ogv_test._TEST['url'] == "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    assert o

# Generated at 2022-06-14 16:16:58.349171
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test for cases in class GlideIE
    # Set up some test inputs and expected outputs
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    glide = GlideIE()
    # Check if the test inputs and outputs are equal to what we expect
    assert glide.suitable(url), 'Suitable returns True'
    assert glide._match_id(url) == 'UZF8zlmuQbe4mr+7dCiQ0w==', 'match_id extracts right id'
    assert glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)', 'VALID_URL is correct'
    assert glide._real_extract(url)

# Generated at 2022-06-14 16:17:06.220668
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:17:12.812140
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info_extractor = GlideIE("GlideIE", "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    
    video_id = info_extractor._match_id("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert video_id == "UZF8zlmuQbe4mr+7dCiQ0w=="


# Generated at 2022-06-14 16:17:13.564157
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(GlideIE._TEST)

# Generated at 2022-06-14 16:17:14.396591
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('GlideIE')

# Generated at 2022-06-14 16:17:18.331085
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE();
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    

# Generated at 2022-06-14 16:17:20.470000
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == ie._VALID_URL

# Generated at 2022-06-14 16:17:27.177634
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Tests for checking if instantiating an object of class GlideIE
    and obtaining the necessary attributes of it works properly"""

    # Test: Test an object of class GlideIE
    glide = GlideIE()
    assert glide is not None
    assert glide.IE_NAME is not None
    assert glide.IE_DESC is not None
    assert glide._VALID_URL is not None
    assert glide._TEST is not None



# Generated at 2022-06-14 16:17:29.588792
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")

# Generated at 2022-06-14 16:18:10.623222
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Unit test creation of an instance of GlideIE
    # 
    # Expected Return Type: none
    # Expected Return Value: none

    # This is not necessary, but it will make the output easier to read
    # between the different unit tests
    print('\n\n')

    glide = GlideIE()

    # expected output: <class '__main__.GlideIE'>
    print(glide.__class__)
    print('\n')


# Generated at 2022-06-14 16:18:17.383255
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from .test import get_testcases
    from .test import list_test_data
    # Obtain a list of test cases from the test module
    testcases = get_testcases(__name__)

    for testcase in testcases:
        # Obtain an instance of GlideIE
        glide = GlideIE()
        # Test whether the constructor raises any error
        try:
            glide = GlideIE()
        except:
            print ("Error: cannot create an instance of class GlideIE, \
                    check the constructor of class GlideIE!")
            return False

    # Obtain an instance of GlideIE
    glide = GlideIE()
    # Obtain a list of data
    data_list = list_test_data(glide)
    # Test whether there are duplicated data

# Generated at 2022-06-14 16:18:18.263727
# Unit test for constructor of class GlideIE
def test_GlideIE():
    d = GlideIE()
    return d

# Generated at 2022-06-14 16:18:27.918902
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:29.285778
# Unit test for constructor of class GlideIE
def test_GlideIE():
	IE_DESC = 'Glide mobile video messages (glide.me)'
	assert(IE_DESC is not None)

# Generated at 2022-06-14 16:18:30.599749
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Constructor of class InfoExtractor
    InfoExtractor.__init__(GlideIE)

# Generated at 2022-06-14 16:18:32.356084
# Unit test for constructor of class GlideIE
def test_GlideIE():
    instance = GlideIE()
    assert type(instance) == GlideIE

# Generated at 2022-06-14 16:18:36.874946
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # This test case will check the constructor of class GlideIE
    test_instance = GlideIE()
    assert test_instance._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:18:39.310533
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:18:46.585582
# Unit test for constructor of class GlideIE
def test_GlideIE():
    func = getattr(GlideIE, "__init__", None)
    assert func
    assert_equal(GlideIE._VALID_URL, r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)')
    assert_equal(GlideIE._TEST['url'], 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert_equal(GlideIE._TEST['md5'], '4466372687352851af2d131cfaa8a4c7')
    assert_equal(GlideIE._TEST['info_dict']['id'], 'UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:19:57.853917
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Basic test
    assert GlideIE()

# Generated at 2022-06-14 16:20:00.657415
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

# Generated at 2022-06-14 16:20:06.889392
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(InfoExtractor()._match_id('/UZF8zlmuQbe4mr+7dCiQ0w==') == 'UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(InfoExtractor()._proto_relative_url('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') == '//share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert(InfoExtractor()._match_id('/UZF8zlmuQbe4mr+7dCiQ0w==') == 'UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:20:16.402267
# Unit test for constructor of class GlideIE
def test_GlideIE():
	
	url = "http://www.dailymotion.com/video/x2fv2hl_coupe-du-monde-de-rugby-finale-nz-vs-australie-20-nouvelle-zelande-17-australie-19-16-novembre-20_sport"
	
	ie = GlideIE(url)
	
	assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
	assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'


# Generated at 2022-06-14 16:20:26.689376
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Constructor of class GlideIE must add an extra element to its
    # _TESTS list, mapping from URL
    # http://share.glide.me/6oYl6UQ2Q9Og6_O1EIUL8g==
    # to the key 'info_dict' of an item of the list
    glide_ie = GlideIE()

# Generated at 2022-06-14 16:20:35.130894
# Unit test for constructor of class GlideIE
def test_GlideIE():
    extractor = GlideIE()
    assert extractor._TEST == {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'md5': '4466372687352851af2d131cfaa8a4c7',
        'info_dict': {
            'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
            'ext': 'mp4',
            'title': "Damon's Glide message",
            'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
        }
    }


# Generated at 2022-06-14 16:20:43.925400
# Unit test for constructor of class GlideIE

# Generated at 2022-06-14 16:20:55.225735
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:20:58.716984
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:21:01.168154
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'