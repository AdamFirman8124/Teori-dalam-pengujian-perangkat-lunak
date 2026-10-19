

# Generated at 2022-06-14 16:34:44.495975
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE()
    assert k.ie_key() == 'KonserthusetPlay'
    assert k.ie_url() == 'konserthusetplay.se'


# Generated at 2022-06-14 16:34:56.119342
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE("https://www.konserthusetplay.se/?m=L5Txop0a-dhWAAqiMERd-A&u=http%3A%2F%2Fwww.konserthusetplay.se%2F&app=www.konserthusetplay.se&rev=2.0.2-270.73&ct=8&c=SMART_WEB&v=4.4.1-3.3.4.4&f=iPhone%2CiPod%2CTouch&t=Safari%2C2.0.1&os=9.3.1&p=SMART_WEB&h=smartweb&pt=SMARTWEB_APP&jsonp=picsearch&_=1459297054274")

# Constructor test
test

# Generated at 2022-06-14 16:34:58.758272
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kp = KonserthusetPlayIE('')
    assert isinstance(kp, KonserthusetPlayIE)

# Generated at 2022-06-14 16:35:03.521277
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.get_id() == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:35:05.715205
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()._VALID_URL == KonserthusetPlayIE._VALID_URL

# Generated at 2022-06-14 16:35:10.180820
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    testTeardown = setup_test_download_dir()
    try:
        KonserthusetPlayIE()
    except NameError as e:
        assert False, 'Could not construct KonserthusetPlayIE'
    finally:
        testTeardown()

# Generated at 2022-06-14 16:35:12.628622
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
        assert(False)
    except NotImplementedError:
        assert(True)

# Generated at 2022-06-14 16:35:15.525546
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Assert instance of class
    assert isinstance(KonserthusetPlayIE, InfoExtractor)

# Generated at 2022-06-14 16:35:19.811565
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('https://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

# Generated at 2022-06-14 16:35:31.195507
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
   ie = KonserthusetPlayIE();
   assert(ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')
   assert(ie._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
   assert(ie._TESTS[0]['md5'] == 'e3fd47bf44e864bd23c08e487abe1967')
   assert(ie._TESTS[1]['url'] == 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

# Generated at 2022-06-14 16:35:56.459874
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie

# Generated at 2022-06-14 16:36:06.802776
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("")

    assert(ie.VIDEO_ID_REGEX == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')
    assert(ie.VIDEO_ID_MATCH == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/?.*\bm=(?P<id>[^&]+)')
    assert(ie.compat_str == 'konserthusetplay:rest:csp.picsearch')
    assert(ie.IE_MAIN == 'konserthusetplay')
    assert(ie.IE_NAME == 'konserthusetplay')

# Generated at 2022-06-14 16:36:08.241313
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	# Call the constructor of class KonserthusetPlayIE
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:19.973279
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert(KonserthusetPlayIE._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')
    assert(KonserthusetPlayIE.__name__ == 'KonserthusetPlayIE')
    assert(KonserthusetPlayIE.ie_key() == 'KonserthusetPlay')
    assert(KonserthusetPlayIE.supported_ie() == ['KonserthusetPlay'])
    assert(KonserthusetPlayIE.ie_key() in KonserthusetPlayIE.supported_ie())
    assert(KonserthusetPlayIE.supported_ie() in KonserthusetPlayIE.ie_key())

# Generated at 2022-06-14 16:36:22.024765
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, KonserthusetPlayIE)

# Generated at 2022-06-14 16:36:23.752900
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()



# Generated at 2022-06-14 16:36:29.612026
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Checks constructor of the KonserthusetPlayIE"""
    obj = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert isinstance(obj, KonserthusetPlayIE)

# Unit tests for the function _extract_m3u8_formats

# Generated at 2022-06-14 16:36:37.169326
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from .common import _TEST_INPUT_FILE
    m = KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:42.262536
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    testcases = [None, "", "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"]

    for input in testcases:
        KonserthusetPlayIE(input)

# Generated at 2022-06-14 16:36:52.423303
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE(None)._VALID_URL == "https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)"
    assert KonserthusetPlayIE(None)._TESTS[0]['url'] == "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    assert KonserthusetPlayIE(None)._TESTS[0]['md5'] == "e3fd47bf44e864bd23c08e487abe1967"

# Generated at 2022-06-14 16:37:45.791194
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('www.konserthusetplay.se', 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert not ie.suitable('http://www.konserthusetplay.se/')

# Generated at 2022-06-14 16:37:48.008640
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    test_konserthusetPlayIE = KonserthusetPlayIE()
    assert isinstance(test_konserthusetPlayIE, KonserthusetPlayIE)

# Generated at 2022-06-14 16:38:00.085805
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from .common import InfoExtractor
    from .konserthusetplay import KonserthusetPlayIE
    from .extractors._m3u8_native import m3u8_native as m3u8_native_module
    from .extractors.rtmp import RtmpIE
    from ..utils import url_or_none
    ie = KonserthusetPlayIE.ie_key()
    ie_constructor = InfoExtractor.get_info_extractor(ie)
    ie_instance = ie_constructor()
    assert ie_instance is not None
    assert isinstance(ie_instance, KonserthusetPlayIE)
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    webpage = ie_instance._

# Generated at 2022-06-14 16:38:13.033689
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE_obj = KonserthusetPlayIE()

    assert KonserthusetPlayIE_obj._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:14.080845
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:38:25.744455
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """ """
    test_ie = KonserthusetPlayIE()

    assert test_ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:34.392809
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Test KonserthusetPlayIE."""
    KonserthusetPlayIE = KonserthusetPlayIE("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert KonserthusetPlayIE.VideoId == "CKDDnlCY-dhWAAqiMERd-A"
    KonserthusetPlayIE = KonserthusetPlayIE("http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw")
    assert KonserthusetPlayIE.VideoId == "elWuEH34SMKvaO4wO_cHBw"

# Generated at 2022-06-14 16:38:35.763496
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kp = KonserthusetPlayIE()
    assert kp



# Generated at 2022-06-14 16:38:40.718884
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay'
    assert ie.ie_key() == 'rspoplay'
    assert ie.SUCCESS == ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:38:44.261689
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except TypeError:
        assert False, "No constructor of class KonserthusetPlayIE"


# Generated at 2022-06-14 16:39:26.952575
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # error when giving an invalid url
    assert(KonserthusetPlayIE({})._real_initialize() == False)


# Generated at 2022-06-14 16:39:37.473920
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:40.249396
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    a = KonserthusetPlayIE()
    assert a._match_id(url) == 'elWuEH34SMKvaO4wO_cHBw'

# Generated at 2022-06-14 16:39:40.954622
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:39:50.451867
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:54.288618
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._match_id('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A') == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:39:57.196691
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE(KonserthusetPlayIE.IE_NAME, KonserthusetPlayIE.IE_DESC, KonserthusetPlayIE._VALID_URL,
            KonserthusetPlayIE._TESTS)

# Generated at 2022-06-14 16:39:59.007053
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    global ie_KonserthusetPlay
    ie_KonserthusetPlay = KonserthusetPlayIE()


# Generated at 2022-06-14 16:40:03.666624
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable(
        'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert not ie.suitable(
        'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:40:07.236505
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()._VALID_URL == KonserthusetPlayIE._VALID_URL
    assert KonserthusetPlayIE()._TESTS == KonserthusetPlayIE._TESTS
    assert KonserthusetPlayIE()._real_extract == KonserthusetPlayIE._real_extract

# Generated at 2022-06-14 16:42:17.826333
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 16:42:21.969594
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    # The result of __init__() should be an instance
    assert isinstance(ie, KonserthusetPlayIE)
    # The result of _VALID_URL should be a string
    assert isinstance(ie._VALID_URL, str)
    # The result of get_info should be a dictionary
    assert isinstance(ie.get_info(), dict)

# Generated at 2022-06-14 16:42:30.628761
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    unit tests for the KonserthusetPlayIE constructor class
    """
    ie = KonserthusetPlayIE()
    assert hasattr(ie, '_VALID_URL') == True, "valid URL class attribute not found"
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)', "valid URL class attribute has unexpected value"
    assert hasattr(ie, '_TEST') == True, "TEST class attibute not found"

# Generated at 2022-06-14 16:42:35.090263
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("")
    assert ie.IE_NAME == "KonserthusetPlay"
    assert ie.IE_DESC == "KonserthusetPlay.se"
    assert ie.IE_VERSION == "1.0"
    assert ie.IE_CONFIG == {}
    assert ie.VALID_URL == "http://(?:www\\.)?(?:konserthusetplay|rspoplay)\\.se/(?:\\?.*)?m=(?P<id>[^&]+)"
    assert ie.VALID_URL_SUFFIX == "?m=CKDDnlCY-dhWAAqiMERd-A"
    return True

# Generated at 2022-06-14 16:42:36.118870
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert(ie.__class__.__name__ == 'KonserthusetPlayIE')

# Generated at 2022-06-14 16:42:39.971478
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.url == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:42:40.806552
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:43.975951
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert(ie._VALID_URL, "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert(ie._TESTS)
    
test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:47.355941
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    a = KonserthusetPlayIE()
    assert a.ie_key() == 'KonserthusetPlay' 
    assert a.ie_name() == 'KonserthusetPlay'
    assert a.ie_description() == 'KonserthusetPlay Youtube-dl extractor'

# Generated at 2022-06-14 16:42:58.296880
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """constructor test"""
    ie = KonserthusetPlayIE()
    assert ie.IE_NAME == 'KonserthusetPlay'
    assert ie.IE_DESC == 'KonserthusetPlay and RSPOPlay video services'
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'