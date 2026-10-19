

# Generated at 2022-06-14 16:34:54.044826
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    valid_inputs = [
        # Valid input types
        'https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A',
        'https://konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A',
        'https://rspoplay.se/?m=CKDDnlCY-dhWAAqiMERd-A&b=1',
    ]

    invalid_inputs = [
        # Invalid input types
        'https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A&b=1',
        'https://youtu.be/9bZkp7q19f0',
    ]


# Generated at 2022-06-14 16:34:55.802333
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:35:03.785745
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    obj = ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert obj['id'] == 'CKDDnlCY-dhWAAqiMERd-A'
    assert obj['title'] == 'Orkesterns instrument: Valthornen'
    assert obj['thumbnail'] == 're:^https?://.*$'
    assert obj['duration'] == 398.76

# Generated at 2022-06-14 16:35:16.457192
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Instantiating testee
    konserthusetplay = KonserthusetPlayIE()
    assert konserthusetplay is not None
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    webpage = konserthusetplay._download_webpage(url, 'CKDDnlCY-dhWAAqiMERd-A')
    e = konserthusetplay._search_regex(
            r'https?://csp\.picsearch\.com/rest\?.*\be=(.+?)[&"\']', webpage,
            'e')


# Generated at 2022-06-14 16:35:19.221352
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Create instance of KonserthusetPlayIE
    KonserthusetPlayIE()

if __name__ == '__main__':
    # Unit test
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:21.649893
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert(ie != None)
    #TODO: Add unit test


# Generated at 2022-06-14 16:35:32.903965
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:35.639754
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

# Generated at 2022-06-14 16:35:37.055346
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj.name == 'konserthuset-play'

# Generated at 2022-06-14 16:35:41.936830
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except:
        assert False

# Testcase for constructor of class KonserthusetPlayIE
# Tested object:       KonserthusetPlayIE(KonserthusetPlayIE)
# Tested method:       __init__(self)
# Input Parameters:    None
# Expected result:     None

# Generated at 2022-06-14 16:35:58.308051
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() in ie.suitable



# Generated at 2022-06-14 16:36:08.299912
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE_instance = KonserthusetPlayIE()
    assert KonserthusetPlayIE_instance._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert KonserthusetPlayIE_instance._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert KonserthusetPlayIE_instance._TESTS[0]['md5'] == 'e3fd47bf44e864bd23c08e487abe1967'
    assert KonserthusetPlayIE_instance._TESTS[1]['url']

# Generated at 2022-06-14 16:36:11.092805
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE.ie_key() == 'konserthusetplay'
    assert KonserthusetPlayIE.ie_key() != 'rspoplay'

# Generated at 2022-06-14 16:36:15.033979
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE._VALID_URL == "https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)"

# Generated at 2022-06-14 16:36:18.085635
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    import doctest
    doctest.testmod()
    # doctest.run_docstring_examples(KonserthusetPlayIE._real_extract, globals())

# Generated at 2022-06-14 16:36:19.290012
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:19.763420
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:27.791129
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL  == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert ie._TESTS[0]['md5'] == 'e3fd47bf44e864bd23c08e487abe1967'
    assert ie._TESTS[0]['info_dict']['id'] == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:36:28.940280
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:30.655495
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE.ie_key() == 'konserthusetplay'



# Generated at 2022-06-14 16:37:06.047579
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert(ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')

# Generated at 2022-06-14 16:37:06.954411
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE();

# Generated at 2022-06-14 16:37:14.922592
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    url_for_test = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    expected_url = 'http://www.konserthusetplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    assert(KonserthusetPlayIE._VALID_URL == KonserthusetPlayIE._real_extract(url_for_test))
    print('test_KonserthusetPlayIE  done!')

# Generated at 2022-06-14 16:37:16.073527
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:25.410171
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:27.296308
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    # Basic unit test of constructor
    obj = KonserthusetPlayIE()
    assert(type(obj) is KonserthusetPlayIE)

# Generated at 2022-06-14 16:37:34.435280
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.IE_NAME == "KonserthusetPlay"
    assert ie.IE_DESC == 'Konserthuset Play'
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:37.541185
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = "http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw"
    KonserthusetPlayIE(url)

# Generated at 2022-06-14 16:37:38.768695
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:42.185188
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE._VALID_URL == r'^(?P<proto>https?)://(?P<url>www\.)?konserthusetplay.se/.*$'

# Generated at 2022-06-14 16:38:53.299150
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:55.455196
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('www.konserthusetplay.se')

# Generated at 2022-06-14 16:39:06.949468
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    test_instance = KonserthusetPlayIE()
    # Check if object was instantiated correctly
    assert test_instance._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:10.751258
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test creating an object of class KonserthusetPlayIE
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    _test = KonserthusetPlayIE()
    assert isinstance(_test, InfoExtractor)

# Generated at 2022-06-14 16:39:13.645421
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:15.972388
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Test for constructor of class KonserthusetPlayIE"""
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:39:17.772813
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None


# Generated at 2022-06-14 16:39:22.091023
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A', 'CKDDnlCY-dhWAAqiMERd-A', 'md5:e3fd47bf44e864bd23c08e487abe1967', 'mp4', 398.76, 'Orkesterns instrument: Valthornen', 'md5:f10e1f0030202020396a4d712d2fa827', 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

# Generated at 2022-06-14 16:39:25.278594
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    IE = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert isinstance(IE.video_id,unicode)
    assert isinstance(IE.url,str)
    assert IE.video_id == 'CKDDnlCY-dhWAAqiMERd-A'
    assert IE.url == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:39:27.001434
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    print(ie)


# Generated at 2022-06-14 16:41:55.048257
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:42:01.668245
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Unit test for constructor of class KonserthusetPlayIE"""
    konserthusetPlayIE = KonserthusetPlayIE()
    assert_equals(konserthusetPlayIE._VALID_URL, r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')
    assert_equals(konserthusetPlayIE._TESTS[0]['url'], 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert_equals(konserthusetPlayIE._TESTS[0]['md5'], 'e3fd47bf44e864bd23c08e487abe1967')

# Generated at 2022-06-14 16:42:03.658484
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    koplayie = KonserthusetPlayIE('http://www.konserthusetplay.se/')
    assert koplayie is not None

# Generated at 2022-06-14 16:42:12.859446
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    video = KonserthusetPlayIE().video("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert repr("http://csp.picsearch.com/rest?e=6UaW6U8wHadgg1S42yS0oQ&containerId=mediaplayer&i=object") in repr(video)
    assert repr("http://csp.picsearch.com/rest?e=6UaW6U8w9ZUaW6U8w6UaW6U8w6UaW6U8w&containerId=mediaplayer&i=object") in repr(video)
    assert repr("Orkesterns instrument: Valthornen") in repr(video)

# Generated at 2022-06-14 16:42:13.787266
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:18.074356
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        ie = KonserthusetPlayIE(None)
        # print ie.__class__.__bases__[0].__name__ # KonserthusetPlayIE is an extension of class InfoExtractor
    except Exception:
        raise AssertionError

if __name__ == '__main__':
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:21.060669
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    lst = ie._VALID_URL.split("=")
    lst[1] = "234567"
    url = "=".join(lst)
    assert ie._match_id(url) == "234567"

# Generated at 2022-06-14 16:42:22.928550
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Simple test to verify that KonserthusetPlayIE can be constructed.
    """
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:23.724780
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:26.629957
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE()
    assert ie._match_id(url) == 'CKDDnlCY-dhWAAqiMERd-A'
