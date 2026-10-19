

# Generated at 2022-06-14 16:13:29.420166
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """
    Tests GlideIE constructor.
    """

    GlideIE(None)._TEST = _TEST
    GlideIE(None)._VALID_URL = _VALID_URL
    GlideIE(None).IE_DESC = IE_DESC

_TEST = GlideIE.IE_DESC
_VALID_URL = GlideIE._VALID_URL
IE_DESC = GlideIE.IE_DESC

# Generated at 2022-06-14 16:13:32.148718
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:13:43.187724
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert GlideIE.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w')
    assert GlideIE.suitable('http://share.glide.me/UZF8zlmuQbe4mr-7dCiQ0w')
    assert GlideIE.suitable('http://share.glide.me/UZF8zlmuQbe4mr_7dCiQ0w')
    assert GlideIE.suitable('http://share.glide.me/UZF8zlmuQbe4mr=7dCiQ0w')
    assert GlideIE.suitable

# Generated at 2022-06-14 16:13:46.472879
# Unit test for constructor of class GlideIE
def test_GlideIE():
	test_GlideIE = GlideIE()
	test_GlideIE

# Generated at 2022-06-14 16:13:57.894954
# Unit test for constructor of class GlideIE
def test_GlideIE():
    yield (
        GlideIE.suitable, "http://share.glide.me/Np7HYnbGQcKjpnV/RY2YzQ==/jF2l4J3tQaWtXeXtRZ29jSg==", True
        )
    yield (
        GlideIE.suitable, "http://share.glide.me/Np7HYnbGQcKjpnV/RY2YzQ==/jF2l4J3tQaWtXeXtRZ29jSg==/s/", True
        )

# Generated at 2022-06-14 16:14:02.988144
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:09.720266
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE().IE_NAME == "Glide"
    assert GlideIE().IE_DESC == "Glide mobile video messages (glide.me)"
    assert "https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==" in GlideIE()._TEST["url"]


# Generated at 2022-06-14 16:14:11.594950
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor())._VALID_URL == GlideIE._VALID_URL

# Generated at 2022-06-14 16:14:22.833901
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie_Glide = GlideIE()
    assert ie_Glide._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:14:29.348297
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie.IE_NAME == 'Glide'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:14:39.673458
# Unit test for constructor of class GlideIE
def test_GlideIE():

    # Create instance of GlideIE
    glideIE = GlideIE()

    # Test correct URL
    match = glideIE._VALID_URL.match("http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==")
    assert match

    # Test incorrect URL
    match = glideIE._VALID_URL.match("http://share.glide.me/")
    assert not match



# unit tests for GlideIE.py

# Generated at 2022-06-14 16:14:41.014421
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor()).IE_NAME == 'Glide'


# Generated at 2022-06-14 16:14:42.735593
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==');

# Generated at 2022-06-14 16:14:52.699732
# Unit test for constructor of class GlideIE
def test_GlideIE():
    p = GlideIE()
    assert p.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert p._TEST == {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'md5': '4466372687352851af2d131cfaa8a4c7',
        'info_dict': {
            'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
            'ext': 'mp4',
            'title': "Damon's Glide message",
            'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
        }
    }
    assert p._VALID_URL == r

# Generated at 2022-06-14 16:14:54.174515
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == ie.IE_DESC

# Generated at 2022-06-14 16:14:58.171598
# Unit test for constructor of class GlideIE
def test_GlideIE():
    test_cases = [('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==', 'UZF8zlmuQbe4mr+7dCiQ0w==')]
    for test_case in test_cases:
        assert test_case[1] == GlideIE._match_id(test_case[0])


# Generated at 2022-06-14 16:15:00.783788
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj == GlideIE()
    assert obj.IE_DESC == "Glide mobile video messages (glide.me)"

# Generated at 2022-06-14 16:15:13.731111
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:15:21.053357
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Tests for the constructor of GlideIE

    # use default values
    glideIE = GlideIE(InfoExtractor())

    print('name: ' + glideIE.IE_NAME)
    assert glideIE.IE_NAME == 'Glide'
    print('description: ' + glideIE.IE_DESC)
    assert glideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    print('URL: ' + glideIE._VALID_URL)
    assert glideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:15:22.891511
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:15:39.073258
# Unit test for constructor of class GlideIE
def test_GlideIE():
    
    # Instantiate class GlideIE
    glideIE = GlideIE()

    # Following codes should be in __init__
    # Assign variable _VALID_URL
    glideIE._VALID_URL = r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

    # Instantiate class InfoExtractor
    InfoExtractor.__init__(glideIE)

    # Following codes should be in _real_extract
    
    # Obtain group: id from url
    video_id = glideIE._match_id('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

    # Test for function
    # Download webpage from url and return the webpage
    # webpage = glideIE._

# Generated at 2022-06-14 16:15:39.580781
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:42.095148
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie._VALID_URL == GlideIE._VALID_URL
    assert ie._TEST == GlideIE._TEST

# Generated at 2022-06-14 16:15:50.423713
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    glideIE = GlideIE()
    assert glideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert glideIE._TEST['url'] == url
    assert glideIE._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
    assert glideIE._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert glideIE._TEST['info_dict']['ext'] == 'mp4'
    assert glideIE

# Generated at 2022-06-14 16:15:51.054012
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:15:58.102917
# Unit test for constructor of class GlideIE
def test_GlideIE():
    from . import GlideIE
    obj = GlideIE()
    assert(obj._VALID_URL.startswith('https?://'))
    assert(obj.IE_DESC.startswith('Glide mobile video messages'))
    assert(obj._TEST.get('url') == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:08.595148
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    expected = True
    assert ie.suitable('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==') == expected
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'

# Generated at 2022-06-14 16:16:19.856304
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj._VALID_URL == 'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:27.594758
# Unit test for constructor of class GlideIE
def test_GlideIE():
    result = GlideIE()
    assert result.IE_NAME == 'Glide'
    assert result.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert result._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert result._TEST_URL == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    

# Generated at 2022-06-14 16:16:29.453943
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:16:48.599197
# Unit test for constructor of class GlideIE
def test_GlideIE():
    IE = GlideIE()
    assert IE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:16:50.604321
# Unit test for constructor of class GlideIE
def test_GlideIE():
    expected_result = 'Glide mobile video messages (glide.me)'
    Glide = GlideIE()
    assert(expected_result == Glide.IE_DESC)

# Generated at 2022-06-14 16:16:58.481235
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'

    # Test URL
    assert ie._real_extract(ie._TEST['url'])['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='

# Generated at 2022-06-14 16:17:09.981471
# Unit test for constructor of class GlideIE
def test_GlideIE():
    url = "http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=="
    obj = GlideIE(url)
    assert obj.id == "UZF8zlmuQbe4mr+7dCiQ0w=="
    assert obj.title == "Damon's Glide message"
    assert obj.url == "http://video.gli.st/UZF8zlmuQbe4mr+7dCiQ0w==.mp4"

# Generated at 2022-06-14 16:17:12.416515
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE(None)
    # checks if IE_NAME property is set to 'Glide'
    assert (ie.IE_NAME == 'Glide')

# Generated at 2022-06-14 16:17:13.000159
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE()

# Generated at 2022-06-14 16:17:13.780836
# Unit test for constructor of class GlideIE
def test_GlideIE():
    obj = GlideIE()
    assert obj

# Generated at 2022-06-14 16:17:14.329691
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert isinstance(GlideIE(), InfoExtractor)

# Generated at 2022-06-14 16:17:17.790274
# Unit test for constructor of class GlideIE
def test_GlideIE():
    gie = GlideIE(InfoExtractor._downloader, "")
    assert gie.IE_DESC is not None
    assert gie._VALID_URL is not None
    assert gie._TEST is not None

# Generated at 2022-06-14 16:17:20.040675
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # bad type pass to test
    assert not GlideIE(object)
    # just a test
    assert GlideIE()

# Generated at 2022-06-14 16:18:03.017715
# Unit test for constructor of class GlideIE
def test_GlideIE():
	test = GlideIE()
	assert test._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
	assert test._TEST['url'] == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
	assert test._TEST['md5'] == '4466372687352851af2d131cfaa8a4c7'
	assert test._TEST['info_dict']['id'] == 'UZF8zlmuQbe4mr+7dCiQ0w=='
	assert test._TEST['info_dict']['ext'] == 'mp4'
	assert test._TEST['info_dict']['title']

# Generated at 2022-06-14 16:18:04.096923
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()


# Generated at 2022-06-14 16:18:04.721318
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:18:08.238927
# Unit test for constructor of class GlideIE
def test_GlideIE():
    try:
        g = GlideIE()
    except Exception as e:
        print('Caught Exception in test_GlideIE(): {}'.format(e))

# Generated at 2022-06-14 16:18:15.356846
# Unit test for constructor of class GlideIE
def test_GlideIE():
    """Unit test for constructor of class GlideIE"""
    ie = GlideIE('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'
    assert ie.id == 'UZF8zlmuQbe4mr+7dCiQ0w=='
    assert ie.url == 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    return


# Generated at 2022-06-14 16:18:24.311305
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # First we create a new object of the GlideIE class and then we call the method _build_url
    # for which we pass the video_id as the argument
    
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    glide_ie = GlideIE()
    url = glide_ie._build_url(video_id)
    
    # Here we check if the url constructed is correct
    if url == 'https://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==':
        return True
    else:
        return False


# Generated at 2022-06-14 16:18:26.262034
# Unit test for constructor of class GlideIE
def test_GlideIE():
    d = GlideIE(None)
    assert d.ie_key() == 'Glide'

# Generated at 2022-06-14 16:18:27.138735
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(None)._real_initialize()

# Generated at 2022-06-14 16:18:29.671293
# Unit test for constructor of class GlideIE
def test_GlideIE():
    info_extractor = GlideIE()
    info_extractor._downloader = None
    info_extractor._real_extract('http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==')

# Generated at 2022-06-14 16:18:30.431193
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(GlideIE._downloader)

# Generated at 2022-06-14 16:19:47.294023
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:48.674484
# Unit test for constructor of class GlideIE
def test_GlideIE():
  assert GlideIE(InfoExtractor()).IE_NAME == 'Glide'

# Generated at 2022-06-14 16:19:49.528063
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Initialize
    GlideIE()

# Generated at 2022-06-14 16:19:50.033653
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:19:50.934594
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE(GlideIE._TEST)

# Generated at 2022-06-14 16:20:01.798586
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert GlideIE._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:20:07.838774
# Unit test for constructor of class GlideIE
def test_GlideIE():
    mie = GlideIE()
    assert mie.IE_NAME == 'Glide'
    assert mie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert mie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

# Generated at 2022-06-14 16:20:09.239163
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE(InfoExtractor()) is not None

# Generated at 2022-06-14 16:20:10.045554
# Unit test for constructor of class GlideIE
def test_GlideIE():
	GlideIE()

# Generated at 2022-06-14 16:20:11.190798
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert GlideIE.IE_NAME == 'glide'

# Generated at 2022-06-14 16:22:51.321513
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.IE_NAME
    ie._VALID_URL
    ie._TEST

# Generated at 2022-06-14 16:22:54.993278
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE('https://share.glide.me/', {})
    # Test that the class throws an AssertionError when the URL is not
    # a Glide video message
    try:
        GlideIE('https://share.glide.me/', {})
        assert False
    except AssertionError:
        assert True

# Generated at 2022-06-14 16:22:59.151553
# Unit test for constructor of class GlideIE
def test_GlideIE():
	import unittest.mock
	from music_dl.extractor import GlideIE
	m = unittest.mock.MagicMock()
	GlideIE(m)
	m.add_ie.assert_called_once_with(GlideIE.ie_key(), GlideIE)

# Generated at 2022-06-14 16:23:00.347815
# Unit test for constructor of class GlideIE
def test_GlideIE():
    assert(not "No constructor arguments supported." in GlideIE.IE_DESC)

# Generated at 2022-06-14 16:23:00.861208
# Unit test for constructor of class GlideIE
def test_GlideIE():
    GlideIE()

# Generated at 2022-06-14 16:23:08.264423
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    ie.set_cookiejar()
    ie.IE_DESC = 'Glide mobile video messages (glide.me)'
    test_dict = {
        'url': 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w==',
        'md5': '4466372687352851af2d131cfaa8a4c7',
        'info_dict': {
            'id': 'UZF8zlmuQbe4mr+7dCiQ0w==',
            'ext': 'mp4',
            'title': "Damon's Glide message",
            'thumbnail': r're:^https?://.*?\.cloudfront\.net/.*\.jpg$',
        }
    }
    ie.ext

# Generated at 2022-06-14 16:23:13.740257
# Unit test for constructor of class GlideIE
def test_GlideIE():
    ie = GlideIE()
    assert ie.IE_NAME == 'Glide'
    assert ie.IE_DESC == 'Glide mobile video messages (glide.me)'
    assert ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'


# Generated at 2022-06-14 16:23:19.277628
# Unit test for constructor of class GlideIE
def test_GlideIE():
    # Test for creating a GlideIE instance
    glide_ie = GlideIE()

    assert glide_ie._VALID_URL == r'https?://share\.glide\.me/(?P<id>[A-Za-z0-9\-=_+]+)'

    assert glide_ie.IE_DESC == 'Glide mobile video messages (glide.me)'

    glide_ie == InfoExtractor()
    return

