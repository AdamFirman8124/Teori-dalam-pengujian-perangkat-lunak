

# Generated at 2022-06-14 16:03:06.620202
# Unit test for constructor of class EitbIE
def test_EitbIE():

    try:
        # Call the main entry point function
        EitbIE
    except:
        raise AssertionError('Function  failed to instantiate class EitbIE')

# Generated at 2022-06-14 16:03:09.485195
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        EitbIE()
    except Exception as e:
        assert(e.message == 'Can\'t create instance of abstract class EitbIE with abstract methods _real_extract')

# Generated at 2022-06-14 16:03:13.644675
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Testing only constructor without any argument
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:16.214484
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:03:17.134982
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test = EitbIE()
    assert test

# Generated at 2022-06-14 16:03:18.572593
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    query = ie._VALID_URL

# Generated at 2022-06-14 16:03:22.985136
# Unit test for constructor of class EitbIE
def test_EitbIE():
  eitbIE = EitbIE()
  assert eitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:23.627876
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:03:24.240792
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:03:36.103770
# Unit test for constructor of class EitbIE
def test_EitbIE():
    x = EitbIE()
    assert x._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert x.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:03:58.428217
# Unit test for constructor of class EitbIE
def test_EitbIE():
	class EitbTest:
		def __init__(self, param):
			print("Testing EitbIE with {0}".format(param))

			eitb_ie = EitbIE(EitbTest)
			eitb_ie.extract("http://www.eitb.tv/eu/bideoa/2013/11/26/valladolid-la-a-o-0-baskonia-zorte-gabean-/3817633/")
	# Mandatory last line
	if __name__ == "__main__":
		test_EitbIE()

# Generated at 2022-06-14 16:04:07.892824
# Unit test for constructor of class EitbIE
def test_EitbIE():
    '''
    A unit test for EitbIE class
    '''
    # Test for positive case
    print('Positive Case')
    url = 'http://www.eitb.tv/eu/bideoa/60-minutos/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    print('Input: %s' % url)
    eitb = EitbIE()
    info_dict = eitb._real_extract(url)
    print('Output: %s' % info_dict)

    # Test for negative case
    print('Negative Case')
    url = 'http://www.eitb.tv/eu/bideoa/blah'
    print('Input: %s' % url)
    eitb = E

# Generated at 2022-06-14 16:04:08.469753
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:04:13.586803
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:15.989190
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME in [x.IE_NAME for x in EitbIE.ieClassList]

# Generated at 2022-06-14 16:04:22.531377
# Unit test for constructor of class EitbIE
def test_EitbIE():
	"""
	Tests the constructor of class EitbIE
	"""
	test = EitbIE()
	assert test.IE_NAME == 'eitb.tv'
	assert test._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:04:24.323118
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE("eitb", "eitb.tv")

# Generated at 2022-06-14 16:04:26.603234
# Unit test for constructor of class EitbIE
def test_EitbIE():
	eitb_ie = EitbIE()
	assert eitb_ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:28.211216
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert not EitbIE()._LOGGER_ERRORS.errors

# Generated at 2022-06-14 16:04:34.150309
# Unit test for constructor of class EitbIE
def test_EitbIE():
	print("Testing constructor for class EitbIE")
	downloader = EitbIE()
	assert downloader.IE_NAME == 'eitb.tv'
	assert downloader._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:04:55.497985
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE()
    assert IE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:58.832582
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print("Initializing unit test for constructor of class EitbIE")
    assert EitbIE({})
    print("Successfully completed unit test for constructor of class EitbIE")


# Generated at 2022-06-14 16:05:04.862833
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Constructor test
    ie = EitbIE()
    assert ie.ie_key() == 'Eitb'
    assert ie.ie_name() == 'eitb.tv'
    assert ie.thumbnail() == 're:^https?:\/\/.*\.eitb\.eus\/.*'


# Generated at 2022-06-14 16:05:08.167367
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/eu/bideoa/by/60-60-2013-2014/4104995148001/lasa-y-zabala-30-anos/4090227752001/')

# Generated at 2022-06-14 16:05:12.329409
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()

    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:05:12.891478
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:05:15.557986
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert hasattr(EitbIE, 'IE_NAME')
    assert hasattr(EitbIE, '_VALID_URL')
    assert hasattr(EitbIE, '_TEST')
    assert hasattr(EitbIE, '_real_extract')

# Generated at 2022-06-14 16:05:17.758521
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")

# Generated at 2022-06-14 16:05:28.307854
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:05:29.250209
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()


# Generated at 2022-06-14 16:06:00.497550
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url_test = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    EitbIE()._real_extract(url_test)

# Generated at 2022-06-14 16:06:06.159840
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert(repr(EitbIE(url)) == '<EitbIE http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/>')

# Unit test case to run the test download of '60 minutos (Lasa y Zabala, 30 años)'
if __name__ == '__main__':
    print(EitbIE._TEST)

# Generated at 2022-06-14 16:06:07.999313
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:06:12.195826
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    result = EitbIE.suitable(url)
    assert(result == True)

# Generated at 2022-06-14 16:06:13.683396
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE()
    assert instance.IE_NAME == EitbIE.IE_NAME

# Generated at 2022-06-14 16:06:14.798381
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:16.382422
# Unit test for constructor of class EitbIE
def test_EitbIE():
    global ie
    from . import test_utils
    ie = EitbIE()
    test_utils.print_ie_params(ie)


# Generated at 2022-06-14 16:06:18.117948
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test that an object of class EitbIE can be created
    eitbie = EitbIE()
    assert eitbie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:18.617435
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:06:21.636318
# Unit test for constructor of class EitbIE
def test_EitbIE():
  return EitbIE('EitbIE', 'http://www.eitb.tv/eu/bideoa/64-minutos/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:07:18.407080
# Unit test for constructor of class EitbIE
def test_EitbIE():
	EitbIE()

# Generated at 2022-06-14 16:07:19.468802
# Unit test for constructor of class EitbIE
def test_EitbIE():
    pass

# Generated at 2022-06-14 16:07:22.985935
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:07:27.201116
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:07:27.707395
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:07:28.618663
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(None)

# Generated at 2022-06-14 16:07:31.335879
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_instance = EitbIE()

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:07:34.882449
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://mam.eitb.eus/mam/REST/ServiceMultiweb/Video/MULTIWEBTV/4090227752001/')

# Generated at 2022-06-14 16:07:40.171143
# Unit test for constructor of class EitbIE
def test_EitbIE():
	url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
	eitb_IE = EitbIE(url);
	assert eitb_IE.get_match_id() == '4090227752001'

# Generated at 2022-06-14 16:07:42.194188
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE()
    assert (instance.IE_NAME == 'eitb.tv')

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:10:24.001941
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(None, 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:10:27.824180
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
        assert True
    except:
        assert False


# Generated at 2022-06-14 16:10:36.245310
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert eitb_ie.IE_NAME == 'eitb.tv'
    assert eitb_ie.VALID_URL == 'http://(?:www\.)?eitb\.tv/(?:eu|es)/video/'

# Generated at 2022-06-14 16:10:37.042743
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE(InfoExtractor)

# Generated at 2022-06-14 16:10:41.136632
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """ Test case for constructor of class EitbIE """

    video_url = "http://www.eitb.tv/eu/bideoa/desfile-moda-ibiltaria/5151076342001/"
    eitbie = EitbIE()
    assert eitbie.suitable(video_url) is True


# Generated at 2022-06-14 16:10:46.716796
# Unit test for constructor of class EitbIE
def test_EitbIE():
    testClass = EitbIE()
    testClass._real_extract('http://www.eitb.tv/eu/bideoa/ikusi/erakusleak/ernest-etxebarne/2015/06/01/video-ernest-etxebarne-2015-06-01/')
    testClass._real_extract('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:10:49.373465
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert str(ie) == ie.IE_NAME
    assert ie.IE_NAME == 'EitbTV'

# Generated at 2022-06-14 16:10:49.920553
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:10:51.601795
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie is not None

# Generated at 2022-06-14 16:10:53.248044
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE()
    IE.IE_NAME
    IE._VALID_URL