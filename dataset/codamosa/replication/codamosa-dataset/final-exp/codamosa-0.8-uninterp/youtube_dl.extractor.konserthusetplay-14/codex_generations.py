

# Generated at 2022-06-14 16:34:44.184520
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Constructor should not raise any exception
    ie = KonserthusetPlayIE('http://konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')


# Generated at 2022-06-14 16:34:55.886256
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Since it's an abstract class, the only way to test it is to test one of its subclasses.
    # This is how we test the abstract class (http://stackoverflow.com/questions/2636691/how-to-unit-test-an-abstract-base-class-in-python
    import unittest
    import sys

    test_cases = (
        KonserthusetPlayIE, )

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

# Generated at 2022-06-14 16:35:00.199002
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test type checking
    assert isinstance(KonserthusetPlayIE, InfoExtractor)
    # Test if instantiation is successful
    konserthusetPlayIE = KonserthusetPlayIE
    assert konserthusetPlayIE


# Generated at 2022-06-14 16:35:12.524503
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from .test_utils import const, TestRequestHandler
    from ..utils import compat_urllib_error
    import json

    class TestHandler(TestRequestHandler, InfoExtractor):
        def do_request(self, req):
            scheme, host, path, qs, _ = req.urlparse()
            if scheme == 'http' and host == 'csp.picsearch.com' and path == '/rest':
                e = dict(compat_urllib_error.parse_qsl(qs))['e']
                filename = e + '.json'
                return const(json.load(open(filename, 'rb')))
            else:
                return super(TestHandler, self).do_request(req)
    ie = TestHandler({}, None, None, None)

# Generated at 2022-06-14 16:35:17.155335
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    
    # Instantiate class KonserthusetPlayIE
    KonserthusetPlayIE(url)

# Generated at 2022-06-14 16:35:18.815148
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert(ie != None)



# Generated at 2022-06-14 16:35:23.646909
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    # a test URL
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

    # calling constructor of class KonserthusetPlayIE with URL
    kie = KonserthusetPlayIE(url)


# Generated at 2022-06-14 16:35:34.317970
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    assert ie.IE_NAME == 'konserthusetplay'
    assert ie.IE_DESC == 'Konserthuset Play'
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:35.678890
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:39.956016
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    x = KonserthusetPlayIE()
    assert isinstance(x, KonserthusetPlayIE)
    assert hasattr(x, '_VALID_URL')
    assert hasattr(x, '_TESTS')
    assert hasattr(x, '_real_extract')

# Generated at 2022-06-14 16:36:01.313678
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj._TEST.get('extractor') == 'KonserthusetPlayIE'
    assert obj._TEST.get('id') == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:36:09.594593
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw")
    assert(ie.ie_key() == "KonserthusetPlayIE")
    assert(ie.url_re.pattern == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')
    assert(ie._VALID_URL == "https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)")

# Generated at 2022-06-14 16:36:14.975921
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.IE_NAME == "konserthusetplay"
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:19.054812
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Description:
        Tests the constructor of class KonserthusetPlayIE
    """ 
    ie = KonserthusetPlayIE()

    assert ie.ie_key() == 'konserthusetplay', ie.ie_key()

# Generated at 2022-06-14 16:36:21.521671
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.name() == "KonserthusetPlayIE"


# Generated at 2022-06-14 16:36:22.639964
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:27.997620
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    titleResult = ie.md5 == 'e3fd47bf44e864bd23c08e487abe1967'
    urlResult = ie.md5 == 'c9c2df37f7b196ee2a2a7cafd0431b7f'

    assert titleResult == True
    assert urlResult == False

# Generated at 2022-06-14 16:36:36.533825
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE()
    assert(k._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')

# Generated at 2022-06-14 16:36:39.666619
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	assert KonserthusetPlayIE()._BUILD_REQUEST(1) == {'ie': 'KonserthusetPlay'}

# Generated at 2022-06-14 16:36:43.337060
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except Exception as inst:
        assert False, str(type(inst)) + ' ' + str(inst)


# Generated at 2022-06-14 16:37:13.367325
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj is not None


# Generated at 2022-06-14 16:37:19.421711
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie= KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay' #Test the ie_key function
    assert ie.working #Test the working function
    assert 'konserthusetplay' in ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')['id'] #Test the extract function

# Generated at 2022-06-14 16:37:22.233270
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url_test = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    KonserthusetPlayIE()._real_extract(url_test)


# Generated at 2022-06-14 16:37:24.409795
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.download_webpage = lambda url: ''
    ie.extract('')

# Generated at 2022-06-14 16:37:26.065677
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	try:
		test_case1 = KonserthusetPlayIE(InfoExtractor)
	except:
		test_case1 = None	
	assert(test_case1 is not None)
	

# Generated at 2022-06-14 16:37:29.213041
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    extractor = KonserthusetPlayIE()
    assert extractor.suitable(url)
    assert extractor.IE_NAME == 'KonserthusetPlay'

# Generated at 2022-06-14 16:37:38.155023
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """

    :return:
    """
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    # url = 'https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    # url = 'http://rspoplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    konserthuset_play = KonserthusetPlayIE()
    konserthuset_play.extract(url)

    return

# Generated at 2022-06-14 16:37:47.929705
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('KonserthusetPlay', 'http://www.konserthusetplay.se', {'id': 1234567})
    assert ie.name == 'KonserthusetPlay'
    assert ie.url == 'http://www.konserthusetplay.se'
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:48.977121
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE

# Generated at 2022-06-14 16:37:57.890152
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    str1 = KonserthusetPlayIE._match_id("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    str2 = KonserthusetPlayIE._match_id("http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw")
    assert str1 == "CKDDnlCY-dhWAAqiMERd-A" and str2 == "elWuEH34SMKvaO4wO_cHBw"

# Generated at 2022-06-14 16:38:31.823737
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	test = KonserthusetPlayIE()
	assert test.IE_NAME == 'konserthusetplay:play'

# Generated at 2022-06-14 16:38:33.073367
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:36.828631
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    info_extractor = KonserthusetPlayIE()
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    info = info_extractor.extract(url)
    assert(info['id'] == 'CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:38:38.257045
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie

# Generated at 2022-06-14 16:38:46.634675
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'KonserthusetPlay'
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie.host() == 'www.konserthusetplay.se'

# Generated at 2022-06-14 16:38:56.964369
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    expected = 'e3fd47bf44e864bd23c08e487abe1967'

    ie = KonserthusetPlayIE()
    assert ie.suitable(url)
    assert ie.IE_NAME == "konserthusetplay:play"
    assert ie._VALID_URL == url

# Generated at 2022-06-14 16:38:58.018262
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE();

# Generated at 2022-06-14 16:39:04.869882
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert not ie.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')

# Generated at 2022-06-14 16:39:08.343637
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE()
    assert isinstance(instance, KonserthusetPlayIE)
    assert hasattr(instance, '_VALID_URL')
    assert hasattr(instance, '_TESTS')

# Generated at 2022-06-14 16:39:09.300795
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert(KonserthusetPlayIE)

# Generated at 2022-06-14 16:39:41.062277
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:43.969524
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'KonserthusetPlay'
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:39:48.143243
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')['id'] == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:39:52.309862
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:53.637130
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except:
        assert False

# Generated at 2022-06-14 16:39:54.900237
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None

# Generated at 2022-06-14 16:40:03.511360
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    cls = KonserthusetPlayIE
    cls.suitable(url)
    assert cls._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:40:08.644363
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Unit test for constructor of class KonserthusetPlayIE
    """
    # URL from the test dictionary
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    # Instanciate the class
    KonserthusetPlayIE(url)

    # URL from the test dictionary
    url = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    # Instanciate the class
    KonserthusetPlayIE(url)

# Generated at 2022-06-14 16:40:09.519969
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE

# Generated at 2022-06-14 16:40:10.307882
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()


# Generated at 2022-06-14 16:41:37.674979
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    test_url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    ie = KonserthusetPlayIE()
    result_video_id = "CKDDnlCY-dhWAAqiMERd-A"
    assert ie._match_id(test_url) == result_video_id

    test_url_2 = "http://rspoplay.se/2.0/?m=G6U1pN_uV7NzZa8uVwL5Yg&width=640&height=360"
    result_video_id_2 = "G6U1pN_uV7NzZa8uVwL5Yg"
    assert ie._match_id(test_url_2) == result

# Generated at 2022-06-14 16:41:39.184359
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Attempt to initialise without url
    url = False
    KonserthusetPlayIE(url)

# Generated at 2022-06-14 16:41:43.091813
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    v = ie.get_media_info('https://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert v['url'] == 'https://vod-as.realnetworks.com/cel-live-live/_definst_/live-live/_definst_/live_kkv_b_500.stream/playlist.m3u8'

# Generated at 2022-06-14 16:41:48.939901
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    info = ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert info['title'] == 'Orkesterns instrument: Valthornen'

# Generated at 2022-06-14 16:41:50.428220
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:01.413269
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthuset_play_ie = KonserthusetPlayIE()
    assert konserthuset_play_ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:42:03.085258
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE._VALID_URL == KonserthusetPlayIE(None)._VALID_URL

# Generated at 2022-06-14 16:42:08.944907
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Unit test for KonserthusetPlayIE
    """
    ie = KonserthusetPlayIE()
    assert ie.suitable('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A&a=3')



# Generated at 2022-06-14 16:42:10.121596
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE is not None

# Generated at 2022-06-14 16:42:10.970268
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()