

# Generated at 2022-06-14 16:34:47.004474
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj.name == 'konserthusetplay'
    assert obj._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert obj.IE_NAME == 'konserthusetplay'

# Generated at 2022-06-14 16:34:48.613708
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE(None)


# Generated at 2022-06-14 16:34:49.702825
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE

# Generated at 2022-06-14 16:34:50.753064
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:34:53.645987
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	# Tests, if the constructor of class KonserthusetPlayIE is working properly.
	obj = KonserthusetPlayIE()
	assert obj.codec

# Generated at 2022-06-14 16:35:00.585779
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthusetplay_ie = KonserthusetPlayIE()

    assert konserthusetplay_ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:12.777201
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kp = KonserthusetPlayIE()
    params = {
        'media': {
            'playerconfig': {
                'title': 'title',
                'duration': 30,
                'mediaInfo': {
                    'description': 'description'
                },
                'playlist': [
                    {
                        'url': 'url',
                        'bitrates': [
                            {
                                'url': 'bitrate_url',
                                'width': 1280,
                                'height': 720,
                                'bitrate': 1500000,
                            }
                        ],
                        'captionsAvailableLanguages': {
                            'eng': 'url_eng'
                        }
                    }
                ]
            },
            'title': 'title',
            'image': 'image'
        }
    }

    info = kp._

# Generated at 2022-06-14 16:35:14.249361
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(KonserthusetPlayIE._VALID_URL)

    assert ie is not None

# Generated at 2022-06-14 16:35:18.981104
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    test_result = KonserthusetPlayIE()

    assert test_result._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:27.525620
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    '''
    This function tests the constructor of class KonserthusetPlayIE.
    The parameter of constructor is a URL,
    and the return value is a KonserthusetPlayIE class.
    '''
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    obj = KonserthusetPlayIE().ie_key()
    assert obj == 'KonserthusetPlay', 'The return value should be "KonserthusetPlay"'


# Generated at 2022-06-14 16:35:45.542997
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    print("test_KonserthusetPlayIE")
    input_url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    ie = KonserthusetPlayIE()
    ie._VALID_URL = r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?' +\
        r'.*\bm=(?P<id>[^&]+)'
    ie.extract(input_url)
# test_KonserthusetPlayIE()


# Generated at 2022-06-14 16:35:46.356397
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:54.892712
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie.IE_NAME == 'konserthusetplay:play'
    test_inst = ie.suitable(ie._VALID_URL)
    assert test_inst is True
    
if __name__ == '__main__':
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:56.169399
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test direct creation of the object
    KonserthusetPlayIE('')

# Generated at 2022-06-14 16:36:06.490367
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:07.180565
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()


# Generated at 2022-06-14 16:36:08.082453
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE != None

# Generated at 2022-06-14 16:36:12.362136
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    print('Testing constructor')
    ie = KonserthusetPlayIE()
    print('Testing _check_valid_url')
    assert ie._check_valid_url({'url': ie._VALID_URL})
    print('Done!')


# Generated at 2022-06-14 16:36:13.489042
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:24.906599
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:53.323358
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_key() in ie.get_info_extractors()
    assert ie.get_info_extractors()[ie.ie_key()] == ie
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A') == True
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw') == True

# Generated at 2022-06-14 16:36:54.151830
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:58.210981
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # define variables
    konserthuset_play_ie_instance = KonserthusetPlayIE()
    konserthuset_play_ie_instance.suitable('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    konserthuset_play_ie_instance._match_id('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:37:04.587572
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Unit test for constructor of class KonserthusetPlayIE
    """
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    # Create a instance of KonserthusetPlayIE class
    test_ie = KonserthusetPlayIE(url)
    assert test_ie.url == url

# Generated at 2022-06-14 16:37:09.210208
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    test_url = KonserthusetPlayIE._TESTS[0]['url']
    test_webpage = KonserthusetPlayIE._TESTS[0]['info_dict']['id']
    ie._real_extract(test_url + test_webpage)

# Generated at 2022-06-14 16:37:10.993347
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    pass


# Generated at 2022-06-14 16:37:14.823765
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Constructor test
    """
    ie = KonserthusetPlayIE('foo')
    assert ie.name == 'KonserthusetPlay', 'name should be KonserthusetPlay'



# Generated at 2022-06-14 16:37:16.352135
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert isinstance(KonserthusetPlayIE(), InfoExtractor)



# Generated at 2022-06-14 16:37:19.744460
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Simply instantiate and delete the class to ensure that
    the constructor doesn't throw any exceptions.
    """
    konserthusetplayie = KonserthusetPlayIE()
    del konserthusetplayie

# Generated at 2022-06-14 16:37:22.834988
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE("")
    assert obj.name == "KonserthusetPlay"
    assert obj.info_dict == {'id': 'CKDDnlCY-dhWAAqiMERd-A'}

# Generated at 2022-06-14 16:38:07.801553
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    class_object = KonserthusetPlayIE('')

# Generated at 2022-06-14 16:38:16.057049
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:20.524862
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from .konserthusetplay import KonserthusetPlayIE

    assert KonserthusetPlayIE._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:30.282638
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('m','n','o','p','q')
    assert ie.suitable('m') == True
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A') == True
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A&share=1') == True
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A&share=2') == True

# Generated at 2022-06-14 16:38:38.498640
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:50.895413
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE('7Jvpe1SouV0')._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)', 'KonserthusetPlayIE._VAlID_URL should be OK. Please correct it'
    assert KonserthusetPlayIE('7Jvpe1SouV0')._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A', 'KonserthusetPlayIE._TESTS[0][\'url\'] should be OK. Please correct it'

# Generated at 2022-06-14 16:38:52.780468
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    constructor_test(KonserthusetPlayIE, KonserthusetPlayIE._VALID_URL)

# Generated at 2022-06-14 16:39:00.921172
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    import inspect
    from .common import InfoExtractor, _find_mobj

    class_constructor = inspect.getargspec(KonserthusetPlayIE.__init__)
    assert_equals(len(class_constructor.args), 4)
    assert_equals(class_constructor.args[0], 'self')
    assert_equals(class_constructor.args[1], 'ie_name')
    assert_equals(class_constructor.args[2], 'search_title')
    assert_equals(class_constructor.args[3], 'ie_key')
    assert_equals(class_constructor.defaults, ('KonserthusetPlay', 'search_title', 'ie_key',) )


test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:39:05.851188
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

# Generated at 2022-06-14 16:39:06.998246
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	return KonserthusetPlayIE()

# Generated at 2022-06-14 16:41:13.134103
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    def assert_type_object(value, expected_type):
        # Makes sure that the type of value matches the type
        # of the expected_type variable
        assert (type(value) is expected_type,
            "{0} has type {1} which does not match {2}".format(
                value,
                type(value),
                expected_type))

    ie = KonserthusetPlayIE()

    # Testing regex match

# Generated at 2022-06-14 16:41:17.429180
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    i = KonserthusetPlayIE()
    print(i)
    # Chekas for class
    assert i.__class__.__name__ == 'KonserthusetPlayIE'
    # Chekas for variables
    assert i.ie_key == 'KonserthusetPlay'
    assert i.ie_desc == 'Play for Konserthuset'

# Generated at 2022-06-14 16:41:20.021484
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	print("\nUnit test successfully passed")
	print("---------------------------")
	#print(KonserthusetPlayIE())
	print("---------------------------\n")
	
test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:41:25.385022
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A&customer=orkestern')

# Generated at 2022-06-14 16:41:31.073599
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:41:36.517862
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test a few cases
    assert 'https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A' == KonserthusetPlayIE._VALID_URL

    assert 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A' == \
        KonserthusetPlayIE._VALID_URL

# Generated at 2022-06-14 16:41:37.714256
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE(None) is not None

# Generated at 2022-06-14 16:41:42.066936
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie == KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_key() == KonserthusetPlayIE.ie_key()
    assert ie.get_info(False) == ie.get_info(True)
    assert ie.extract_info(False) == ie.extract_info(True)

# Generated at 2022-06-14 16:41:47.538314
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:41:50.910221
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Module variable KonserthusetPlayIE.test_func is constructed here
    KonserthusetPlayIE.test_func = lambda: 'OK'
    assert KonserthusetPlayIE.test_func() == 'OK'