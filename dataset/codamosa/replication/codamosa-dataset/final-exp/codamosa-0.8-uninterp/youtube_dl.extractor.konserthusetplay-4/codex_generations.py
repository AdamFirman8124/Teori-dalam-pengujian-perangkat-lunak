

# Generated at 2022-06-14 16:34:43.752384
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:34:55.533344
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Variable initialisation
    KonserthusetPlayIE = KonserthusetPlayIE()
    # Test that the mediaId of a video can be extracted
    value = 'CKDDnlCY-dhWAAqiMERd-A'
    url = 'https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    # Assert that the mediaId is extracted correctly
    assert(KonserthusetPlayIE._match_id(url) == value)
    # Test that the mediaId of a video with query parameters can be extracted
    value = 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:34:56.926796
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie

# Generated at 2022-06-14 16:34:59.927817
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj._VALID_URL is not None
    assert obj._TESTS is not None


# Generated at 2022-06-14 16:35:01.148245
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    a = KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:13.266842
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.SUFFIX == 'se'
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_type() == 'konserthusetplay'
    assert ie.host() == 'www.konserthusetplay.se'

# Generated at 2022-06-14 16:35:17.548077
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Simple test case to test constructor of class KonserthusetPlayIE.
    """
    ie = KonserthusetPlayIE()
    assert ie.IE_NAME == 'KonserthusetPlay'

# Generated at 2022-06-14 16:35:21.308016
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()

    assert(obj._VALID_URL.endswith("m=(?P<id>[^&]+)"))
    assert(len(obj._TESTS) == 2)

# Generated at 2022-06-14 16:35:22.320287
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:23.495592
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE(None)

# Generated at 2022-06-14 16:35:51.011846
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()


# Generated at 2022-06-14 16:35:54.631013
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('konserthusetplay.se')
    assert ie.subdomain == 'www'
    assert ie.hostname == 'www.konserthusetplay.se'


# Generated at 2022-06-14 16:35:56.199903
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None

# Generated at 2022-06-14 16:35:58.450225
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Test KonserthusetPlayIE constructor"""
    assert(isinstance(KonserthusetPlayIE(), KonserthusetPlayIE))

# Generated at 2022-06-14 16:36:08.370371
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    KonserthusetPlayIE('KonserthusetPlay')
    KonserthusetPlayIE('KonserthusetPlayIE')
    KonserthusetPlayIE('konserthusetplay')
    KonserthusetPlayIE('konserthusetplayie')
    KonserthusetPlayIE('RspoPlay')
    KonserthusetPlayIE('RspoPlayIE')
    KonserthusetPlayIE('rspoplay')
    KonserthusetPlayIE('rspoplayie')

# Generated at 2022-06-14 16:36:14.846147
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE(url)
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:19.866523
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        from konserthusetplay_tests import test_KonserthusetPlayIE
        test_KonserthusetPlayIE()
    except Exception as e:
        print(str(e))
        assert False, 'Unit test of class KonserthusetPlayIE has failed'


# Generated at 2022-06-14 16:36:20.991368
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:22.533645
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    constructor_test(KonserthusetPlayIE, {})

# Generated at 2022-06-14 16:36:23.830787
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert True

# Generated at 2022-06-14 16:36:46.579959
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    print("Testing KonserthusetPlayIE")


# Generated at 2022-06-14 16:36:47.518923
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    constructor_test(KonserthusetPlayIE)

# Generated at 2022-06-14 16:36:51.602069
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")

# Generated at 2022-06-14 16:36:52.155541
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE

# Generated at 2022-06-14 16:36:56.496089
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj.SUCCESS == 'SUCCESS'
    assert obj.FAILURE == 'FAILURE'
    assert obj.RETRY == 'RETRY'
    assert len(obj.IE_NAME) > 0
    assert len(obj.IE_DESC) > 0
    assert len(obj._VALID_URL) > 0
    assert len(obj._TEST) > 0
    assert len(obj._TESTS) > 0

# Generated at 2022-06-14 16:37:06.922941
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Constructor of KonserthusetPlayIE should throw an error if the URL is not valid
    # Create instance of test class
    konserthuset = KonserthusetPlayIE()

    # Assign regular expression to variable
    regex = konserthuset._VALID_URL

    # Assert that regular expression matches correct URL, and that incorrect URL raises error
    assert re.match(regex, "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert re.match(regex, "http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw")

# Generated at 2022-06-14 16:37:10.571686
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        # IE InfoExtractor
        ie = KonserthusetPlayIE()
    except:
        assert False, "Fail to construct a KonserthusetPlayIE object"



# Generated at 2022-06-14 16:37:13.413537
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    print(ie)
    assert ie.__class__.__name__ == "KonserthusetPlayIE"

# Generated at 2022-06-14 16:37:15.491400
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE()
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:37:20.383390
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.resultType = "create_test"
    result = ie.extract("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert "e3fd47bf44e864bd23c08e487abe1967" in result["id"]

# Generated at 2022-06-14 16:38:07.012637
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	assert KonserthusetPlayIE

# Generated at 2022-06-14 16:38:08.225863
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE

# Generated at 2022-06-14 16:38:12.226225
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from .common import make_extractor

    KonserthusetPlayIE.__bases__ = (make_extractor(None),)
    KonserthusetPlayIE.suitable(None)
    KonserthusetPlayIE._real_extract(None, None)

# Generated at 2022-06-14 16:38:12.873340
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	assert True

# Generated at 2022-06-14 16:38:24.103563
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    test = KonserthusetPlayIE()
    response = test._download_webpage('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A', 'test')
    assert response == None
    assert test._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert test._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert test._TESTS[0]['md5'] == 'e3fd47bf44e864bd23c08e487abe1967'

# Generated at 2022-06-14 16:38:25.600376
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE(None)

# Generated at 2022-06-14 16:38:27.480804
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test initiation of KonserthusetPlayIE
    ie = KonserthusetPlayIE()
    assert ie is not None


# Generated at 2022-06-14 16:38:30.583535
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:38:38.647859
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:43.685660
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert(KonserthusetPlayIE().get_info("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A").get("id") == "CKDDnlCY-dhWAAqiMERd-A")

# Generated at 2022-06-14 16:40:22.726735
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert type(ie) == KonserthusetPlayIE

# Generated at 2022-06-14 16:40:28.888117
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kp_ie = KonserthusetPlayIE()
    assert kp_ie
    assert kp_ie.ie_key() == "konserthusetplay"
    assert kp_ie.ie_key() == KonserthusetPlayIE.ie_key()
    assert kp_ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'


# Generated at 2022-06-14 16:40:29.848214
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:40:30.965414
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie


# Generated at 2022-06-14 16:40:32.730749
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None


# Generated at 2022-06-14 16:40:38.142162
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """This is a test for the constructor of class KonserthusetPlayIE"""
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    # This should be parsed correctly.
    Video = KonserthusetPlayIE()._real_extract(url)
    assert Video['id'] == video_id

# Generated at 2022-06-14 16:40:47.933160
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:40:57.258914
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    def create_konserthusetplay(url, **kwargs):
        return KonserthusetPlayIE(url, **kwargs)
    ie = create_konserthusetplay('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie._match_id('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A') == 'CKDDnlCY-dhWAAqiMERd-A'
    assert ie._match_id('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw') == 'elWuEH34SMKvaO4wO_cHBw'

# Generated at 2022-06-14 16:41:05.276358
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    fixture_url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    data = KonserthusetPlayIE()._real_extract(fixture_url)
    assert data['id'] == 'CKDDnlCY-dhWAAqiMERd-A'
    assert data['ext'] == 'mp4'
    assert 'Orkesterns instrument: Valthornen' in data['title']
    assert 'md5:f10e1f0030202020396a4d712d2fa827' in data['description']

# Generated at 2022-06-14 16:41:06.376355
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()