

# Generated at 2022-06-14 16:34:41.649781
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	assert KonserthusetPlayIE

# Generated at 2022-06-14 16:34:46.562947
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE(_initialize_gevent=False, _print=False)
    # pylint: disable=broad-except
    except Exception:
        raise AssertionError("Failed to construct KonserthusetPlayIE object.")

# Generated at 2022-06-14 16:34:52.120207
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    url = "https://www.rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw"
    video = ie.url_result(url)
    data = ie.extract(video.url)
    print(data)
    return data

#test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:34:54.142776
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE()

    assert instance._DOWNLOAD_VIDEO_TEMPLATE

# Generated at 2022-06-14 16:34:55.107890
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert(KonserthusetPlayIE)

# Generated at 2022-06-14 16:34:59.875501
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE()
    # Check if the constructor has been called properly:
    assert instance._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:04.686088
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('/')
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:17.253994
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE(url)

    # Test if all needed variables are initialized
    assert ie.url == url
    assert ie.extractor_key == 'konserthusetplay'
    assert ie.video_id == 'CKDDnlCY-dhWAAqiMERd-A'
    assert ie.name == 'konserthusetplay.se'
    assert ie.artist == 'konserthusetplay.se'
    assert ie.title == None
    assert ie.description == None
    assert ie.thumbnail == None
    assert ie.duration == None
    assert ie.timestamp == None
    assert ie.formats == []

# Generated at 2022-06-14 16:35:24.001356
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Create an object of class KonserthusetPlayIE
    ie = KonserthusetPlayIE()

    # test _VALID_URL
    test_url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    expected_url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert ie._VALID_URL.match(test_url)
    assert ie._VALID_URL.match(test_url).group('id') == 'CKDDnlCY-dhWAAqiMERd-A'
    assert ie._VALID_URL.match(test_url).group('url') == expected_url

# Generated at 2022-06-14 16:35:34.575326
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Initialize KonserthusetPlayIE
    # class KonserthusetPlayIE(InfoExtractor):
    #     _VALID_URL = r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    KonserthusetPlayIE = KonserthusetPlayIE()

    # Call _real_extract()
    # def _real_extract(self, url)

# Generated at 2022-06-14 16:35:51.788131
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    #test_KonserthusetPlayIE()
    assert KonserthusetPlayIE

# Generated at 2022-06-14 16:35:52.844571
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:03.132453
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    url = instance._VALID_URL
    assert url == "https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)", "Incorrect url"
    url2 = instance._TESTS[0]['url']
    assert url2 == "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    url3 = instance._TESTS[1]['url']

# Generated at 2022-06-14 16:36:04.278441
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	video = KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:07.209288
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    _VALID_URL = r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie._VALID_URL == _VALID_URL

# Generated at 2022-06-14 16:36:08.105565
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:12.413131
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert isinstance(KonserthusetPlayIE(),
                      KonserthusetPlayIE)
    assert KonserthusetPlayIE().IE_NAME == 'konserthusetplay'
    assert KonserthusetPlayIE().IE_DESC == ''



# Generated at 2022-06-14 16:36:13.543425
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:21.139259
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # This test does not have any return value and is only for unit testing
    # the constructor of the class KonserthusetPlayIE only

    # This is to test the constructor of the class KonserthusetPlayIE
    # ie = KonserthusetPlayIE(downloader=None)
    ie = KonserthusetPlayIE()

    # This is to indicate the test succeeds

# Generated at 2022-06-14 16:36:23.551209
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie != None, 'Failed to create an instance of KonserthusetPlayIE'

# Generated at 2022-06-14 16:36:47.475350
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('http://konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:36:55.751156
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from unittest import mock
    mock_urlopen = mock.MagicMock()

# Generated at 2022-06-14 16:37:01.746219
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay'
    assert ie.ie_name() == 'konserthusetplay'
    assert ie.video_id() == 'CKDDnlCY-dhWAAqiMERd-A'


# Generated at 2022-06-14 16:37:04.795294
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie
    instance = ie._real_extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert instance

# Generated at 2022-06-14 16:37:16.254862
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	# Test for https://github.com/rg3/youtube-dl/issues/14865
	# This fails if the constructor is not reimplemented
	ie = KonserthusetPlayIE("https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
	assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:18.828927
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    t = KonserthusetPlayIE('https://rspoplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    t

# Generated at 2022-06-14 16:37:24.714937
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'KonserthusetPlay'
    assert ie.test()[1][:10] == 'CKDDnlCY-dh'
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:32.534444
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    # Initialize an instance of the KonserthusetPlayIE
    kp_ie = KonserthusetPlayIE()

    # Verify that the instance creation is successful
    assert kp_ie is not None, "Failed to instantiate an instance of KonserthusetPlayIE"

    # The url should be valid
    assert kp_ie._VALID_URL == "https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)", "Invalid url: " + kp_ie._VALID_URL

    # The test video should have a video id
    assert len(kp_ie._TESTS) == 2, "Invalid number of tests"
    test_video = kp_ie._TESTS[0]


# Generated at 2022-06-14 16:37:34.546312
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:37.663693
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from .konserthuset_play import KonserthusetPlayIE
    # Create object of class
    konserthuset_play_ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:32.345862
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    print("Testing constructor of class KonserthusetPlayIE")
    print("==============================================")
    obj = KonserthusetPlayIE()

    assert(isinstance(obj, InfoExtractor))

    print("TEST PASSED")


# Generated at 2022-06-14 16:38:36.828469
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")

    assert ie._match_id("https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A") == "CKDDnlCY-dhWAAqiMERd-A"

# Generated at 2022-06-14 16:38:37.720352
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE({}) is not None

# Generated at 2022-06-14 16:38:50.127458
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie_url = ie._VALID_URL
    ie_id = ie._match_id(ie_url)
    ie_webpage = ie._download_webpage(ie_url, ie_id)
    ie_e = ie._search_regex(ie._VALID_URL, ie_webpage, 'e')
    ie_rest = ie._download_json(
        'http://csp.picsearch.com/rest?e=%s&containerId=mediaplayer&i=object' % ie_e,
        ie_id, transform_source=lambda s: s[s.index('{'):s.rindex('}') + 1])
    ie_media = ie_rest['media']
    ie_player_config = ie_media['playerconfig']
    ie_

# Generated at 2022-06-14 16:38:59.568447
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.get_settings() == {
        'youtube': {
            'age_limit': 0,
            'include_dash_manifest': True,
        },
        'hls': {
            'prefer_native': True,
        },
    }
    assert ie.extract_formats('https://m.youtube.com/watch?v=vn9mMeWcgoM') == []
    assert ie.extract_formats('https://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw') == []
    assert ie.extract_formats('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A') == []

# Generated at 2022-06-14 16:39:02.697407
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    args = [
        {'url': 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'},
        {'url': 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'}
    ]
    for test in args:
        KonserthusetPlayIE(test)._real_extract(test)

# Generated at 2022-06-14 16:39:12.426973
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:18.069025
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    global KonserthusetPlayIE
    url = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    konserthusetplayIE = KonserthusetPlayIE()
    konserthusetplayIE._match_id(url)

# Generated at 2022-06-14 16:39:22.765024
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Checks if constructor of class KonserthusetPlayIE works
    """
    # Checks if constructor of class KonserthusetPlayIE works
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    KonserthusetPlayIE(url)

# Generated at 2022-06-14 16:39:29.129396
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert ie._TESTS[0]['md5'] == 'e3fd47bf44e864bd23c08e487abe1967'

# Generated at 2022-06-14 16:41:49.229914
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Constructor test of class KonserthusetPlayIE"""
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'KonserthusetPlay'
    assert ie.http_headers() is None
    assert ie.query.get('m') is None
    assert ie.query.get('m') is None
    assert ie.video_id is None


# Generated at 2022-06-14 16:41:51.028259
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:42:01.453245
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE()
    instance._download_webpage("https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A", "7c8dd538-b00e-4e90-8cb7-8f75b4ff4b3c")

# Generated at 2022-06-14 16:42:04.134851
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:42:07.065734
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserhuset_play_ie = KonserthusetPlayIE()
    konserhuset_play_ie.extract('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

# Generated at 2022-06-14 16:42:08.269095
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE(None)

# Generated at 2022-06-14 16:42:10.414777
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    # For coverage purpose
    ie.to_screen('TEST_SCREEN')
    assert ie._TEST == 'test'

# Generated at 2022-06-14 16:42:14.082585
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'


# Generated at 2022-06-14 16:42:15.902871
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()._real_extract(None)

# Generated at 2022-06-14 16:42:23.584876
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE()
    info = ie.extract(url)
    assert info['id'] == 'CKDDnlCY-dhWAAqiMERd-A'
    assert info['ext'] == 'mp4'
    assert info['title'] == 'Orkesterns instrument: Valthornen'
    assert info['thumbnail'] is not None


# Use the KonserthusetPlayIE class only for these domains,
# use generic YoutubeIE for other domains.
# The YoutubeIE class is still used for links like this:
# http://www.konserthusetplay.se/video/675