

# Generated at 2022-06-14 16:34:37.998236
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE

# Generated at 2022-06-14 16:34:43.963865
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kpIE = KonserthusetPlayIE('test_KonserthusetPlayIE')
    kpIE.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    kpIE.extract('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

# Generated at 2022-06-14 16:34:45.068159
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()


# Generated at 2022-06-14 16:34:50.121226
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test parameters
    url = ''

    # Test constructor of class KonserthusetPlayIE
    instance = KonserthusetPlayIE(url)

    # Test instance of class KonserthusetPlayIE
    assert isinstance(instance, KonserthusetPlayIE)

# Generated at 2022-06-14 16:34:53.488330
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay'
    assert ie.ie_name() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:34:55.763259
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE().extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:34:58.265222
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
  try:
    KonserthusetPlayIE()
  except:
    raise AssertionError("Test failed")
  else:
    assert True

# Generated at 2022-06-14 16:35:10.657378
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    # Test constructor of class KonserthusetPlayIE
    assert(KonserthusetPlayIE._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')

    # Test constructor of class KonserthusetPlayIE
    assert(len(KonserthusetPlayIE._TESTS) == 2)

    # Test constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:35:12.679453
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:35:14.605833
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        ie = InfoExtractor()
        my_ie = KonserthusetPlayIE(ie)
        print(my_ie)
    except Exception as e:
        print(e)


# Generated at 2022-06-14 16:35:29.103725
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    instance = KonserthusetPlayIE()
    instance._real_initialize(url)

# Generated at 2022-06-14 16:35:32.459272
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert isinstance(ie, KonserthusetPlayIE)

# Generated at 2022-06-14 16:35:34.952719
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert 'KonserthusetPlay' in ie.IE_NAME
    # Only one test case
    assert len(ie._TESTS) == 1


# Generated at 2022-06-14 16:35:38.621778
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    KonserthusetPlayIE().suitable(url)
    KonserthusetPlayIE._real_extract(url)

# Generated at 2022-06-14 16:35:40.141965
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:41.896343
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    info = InfoExtractor(KonserthusetPlayIE)
    test = KonserthusetPlayIE(info).test()
    assert test == True

# Generated at 2022-06-14 16:35:42.694189
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:43.472431
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    info_extractor = KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:44.427822
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()
    assert 1 == 1

# Generated at 2022-06-14 16:35:45.807023
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:12.836259
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test the constructror of KonserthusetPlayIE class
    url = KonserthusetPlayIE()._VALID_URL
    # test if it has been created successfully
    assert KonserthusetPlayIE()._VALID_URL == url

# Test for download function

# Generated at 2022-06-14 16:36:15.203612
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except Exception as e:
        assert False, ('KonserthusetPlayIE', e)

# Generated at 2022-06-14 16:36:22.024292
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable(KonserthusetPlayIE._VALID_URL)
    assert ie.IE_NAME == "konserthusetplay"
    assert ie.IE_DESC == "konserthusetplay.se"
    assert "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A" in ie.workingURLs

# Generated at 2022-06-14 16:36:32.497095
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Constructor of class KonserthusetPlayIE
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_key() == "KonserthusetPlay"
    assert ie.video_id is None
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:36:33.691232
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Create object
    KonserthusetPlayIE()



# Generated at 2022-06-14 16:36:41.266799
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # test for KonserthusetPlayIE object
    from .common import InfoExtractor
    from ..utils import (
        determine_ext,
        float_or_none,
        int_or_none,
        url_or_none,
    )

    assert KonserthusetPlayIE._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'


# Generated at 2022-06-14 16:36:42.755965
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    check_ie(ie)

# Generated at 2022-06-14 16:36:43.650120
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Unit test for constructor of class KonserthusetPlayIE"""
    instance = KonserthusetPlayIE()
    assert True

# Generated at 2022-06-14 16:36:47.337131
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kp = KonserthusetPlayIE()
    url = "http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw"
    kp._real_extract(url)


# Generated at 2022-06-14 16:36:52.225620
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Create object
    k_play = KonserthusetPlayIE()
    try:
        k_play.extract('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    except:
        print("error: constructor of class KonserthusetPlayIE failed")
        assert False
    else:
        assert True


# Generated at 2022-06-14 16:37:44.660672
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:47.267900
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie._real_extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:37:49.488838
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    #Tester init av klassen KonserthusetPlayIE
    ie = KonserthusetPlayIE()
    assert(ie != None)

# Generated at 2022-06-14 16:38:01.394338
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    print('Test of KonserthusetPlayIE constructor')

    print(ie.url)
    print(ie._VALID_URL)
    print(ie.video_id)
    print('CKDDnlCY-dhWAAqiMERd-A')
    print(ie._TESTS)
    print(ie._TESTS[0]['url'])
    print(ie._TESTS[0]['md5'])
    # print(ie._TESTS[0]['info_dict'])
    print(ie._TESTS[0]['info_dict']['id'])

# Generated at 2022-06-14 16:38:13.775273
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    import os
    import sys

    # Make sure that environment variable is set, so unit test can run
    os.environ['KONSERTHUSET_API_KEY'] = 'api_key'

    # Create a string with website content to use for unit testing
    videoUrl = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    url = KonserthusetPlayIE._build_url(videoUrl)
    webpage = KonserthusetPlayIE._download_webpage(
    			url, videoUrl)

    # Create a unit test for function _real_extract
    def test_real_extract():
        KonserthusetPlayIE._real_extract(videoUrl)

    # Run unit test and return value (_real_ext

# Generated at 2022-06-14 16:38:17.316703
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthusetPlayIE = KonserthusetPlayIE()
    assert konserthusetPlayIE != None

# Generated at 2022-06-14 16:38:20.194656
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except TypeError:
        assert False, 'constructor of class KonserthusetPlayIE raises TypeError unexpectedly'
    except:
        pass


# Generated at 2022-06-14 16:38:26.673021
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Unit tests for constructor of class KonserthusetPlayIE."""
    from ..utils import get_testcases
    # Test with various inputs
    for testcase in get_testcases(KonserthusetPlayIE.__name__):
        assert KonserthusetPlayIE(testcase).match({}, {}, {})
    # Test with various inputs
    for testcase in get_testcases(KonserthusetPlayIE.__name__):
        assert KonserthusetPlayIE(testcase).match({}, {}, {})



# Generated at 2022-06-14 16:38:27.658038
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:30.726208
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:39:58.726932
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	classname = KonserthusetPlayIE.__name__
	# print(classname)
	assert classname

# Generated at 2022-06-14 16:40:00.410791
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:40:01.826740
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    gen = KonserthusetPlayIE()
    assert isinstance(gen, KonserthusetPlayIE)

# Generated at 2022-06-14 16:40:06.618131
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, KonserthusetPlayIE)
    assert hasattr(ie, '_VALID_URL')
    assert ie._VALID_URL is not None
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:40:11.923943
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    IE=KonserthusetPlayIE()
    assert IE.IE_NAME == 'e-konserthusetplay'
    assert IE.IE_DESC == 'e-konserthusetplay'
    assert IE._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:40:17.617500
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')

# Generated at 2022-06-14 16:40:18.474773
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:40:19.312893
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:40:23.096976
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    global ie
    ie = KonserthusetPlayIE()
    return ie.suitable('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')


# Generated at 2022-06-14 16:40:24.739204
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie is not None