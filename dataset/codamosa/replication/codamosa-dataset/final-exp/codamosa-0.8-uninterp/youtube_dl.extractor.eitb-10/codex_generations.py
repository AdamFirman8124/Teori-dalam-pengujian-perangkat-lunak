

# Generated at 2022-06-14 16:03:03.975026
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE(EitbIE._TEST)
    assert ie._TEST == ie.IE_NAME

# Generated at 2022-06-14 16:03:08.488669
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert(eitb._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')

# Unit test

# Generated at 2022-06-14 16:03:17.096046
# Unit test for constructor of class EitbIE
def test_EitbIE():
    info = EitbIE()._real_extract('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert info['id'] == '4090227752001'
    assert info['title'] == '60 minutos (Lasa y Zabala, 30 años)'
    assert info['description'] == 'Programa de reportajes de actualidad.'
    assert info['duration'] == 3996.76
    assert info['timestamp'] == 1381789200

# Generated at 2022-06-14 16:03:18.914803
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Test construction of class EitbIE.
    """
    EitbIE()

# Generated at 2022-06-14 16:03:20.303124
# Unit test for constructor of class EitbIE
def test_EitbIE():
	object = EitbIE()
	assert(object)

# Generated at 2022-06-14 16:03:26.103965
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos/lasa-y-zabala-30-anos/')
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:27.013369
# Unit test for constructor of class EitbIE
def test_EitbIE():
    clsEitbIE = EitbIE()

# Generated at 2022-06-14 16:03:29.323495
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e.get_test() == EitbIE._TEST

# Generated at 2022-06-14 16:03:35.321553
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_urls = ['http://www.eitb.tv/eu/bideoa/euskaltegiakomertziala/20131014/lasa-y-zabala-30-urte/4104995148001/']
    test = EitbIE()
    for url in test_urls:
        result = test.match(url)
        assert result

# Generated at 2022-06-14 16:03:41.729382
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:57.918275
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj = EitbIE()
    assert obj.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:05.984077
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_case = EitbIE("http://www.eitb.tv/eu/bideoa/eibar/bideoa-sailkapen-garaiko-makina/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
    assert test_case.IE_NAME == "eitb.tv"
    assert test_case._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:08.730505
# Unit test for constructor of class EitbIE
def test_EitbIE():
	eitb_ie_test = EitbIE(InfoExtractor())

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:04:12.374689
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.ie_key() == 'eitb.tv'
    assert eitb.ie_name() == 'eitb.tv'

# Generated at 2022-06-14 16:04:22.239701
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('test', 'test', 'test')
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, 'IE_NAME')
    assert hasattr(ie, '_TEST')
    assert hasattr(ie, '_real_extract')
    assert hasattr(ie, '_download_json')
    assert hasattr(ie, '_sort_formats')
    assert hasattr(ie, '_extract_f4m_formats')
    assert hasattr(ie, '_extract_m3u8_formats')
    assert hasattr(ie, '_match_id')

# Generated at 2022-06-14 16:04:32.046038
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    ie = EitbIE()
    assert ie._real_extract('http://www.eitb.tv/eu/bideoa/deportea/zuzenean/2014/12/09/ara-perpignan-baskoen-osteguna-/4106131474001/4106131457001/') is not None

# Generated at 2022-06-14 16:04:34.591382
# Unit test for constructor of class EitbIE
def test_EitbIE():
	# This line test the constructor
	assert EitbIE() is not None

if __name__ == '__main__':
	test_EitbIE()

# Generated at 2022-06-14 16:04:35.147033
# Unit test for constructor of class EitbIE
def test_EitbIE():
	pass

# Generated at 2022-06-14 16:04:39.640040
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie.IE_NAME == "eitb.tv"
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert isinstance (eitb_ie._TEST, dict)

# Generated at 2022-06-14 16:04:42.037439
# Unit test for constructor of class EitbIE
def test_EitbIE():
  instance = EitbIE()
  assert isinstance(instance,EitbIE)
  return instance


# Generated at 2022-06-14 16:04:59.003157
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test instantiation of object
    EitbIE()
    #Test passing in argument
    EitbIE(1)
    EitbIE(None)

# Generated at 2022-06-14 16:05:01.395915
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:05:11.257352
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .common import try_get
    from .eitb import EitbIE
    ie = EitbIE()
    _VALID_URL = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    video_id = '4090227752001'

# Generated at 2022-06-14 16:05:12.067328
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()
    

# Generated at 2022-06-14 16:05:13.808981
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == EitbIE._VALID_URL

# Generated at 2022-06-14 16:05:14.332123
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:05:15.148684
# Unit test for constructor of class EitbIE
def test_EitbIE():
	EitbIE(InfoExtractor())

# Generated at 2022-06-14 16:05:16.367098
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj = EitbIE()

# Generated at 2022-06-14 16:05:17.848311
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test = EitbIE()
    print("Test completed")


# Generated at 2022-06-14 16:05:21.147318
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/eu/bideoa/liga-lions-taberna-bideak/k-bidea/4209021716001/')
    assert ie is not None

# Generated at 2022-06-14 16:05:49.225034
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()


# Generated at 2022-06-14 16:05:51.732821
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_EitbIE.EitbIE = EitbIE
    test_EitbIE.eitb_ie = EitbIE()



# Generated at 2022-06-14 16:05:59.088772
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:06:01.263733
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.ie_key() == 'eitb.tv'

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:06:01.767051
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:06:03.429546
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # To test the constructor of EitbIE class
    EitbIE()

# Generated at 2022-06-14 16:06:13.219672
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/', True)
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:14.858476
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:20.679708
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # parameters for construction
    # these parameters are from the self._TEST
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    ie = EitbIE()
    # this will call the __init__ method of class InfoExtractor
    ie.suitable(url)
    assert ie.IE_NAME == 'eitb.tv'



# Generated at 2022-06-14 16:06:31.543045
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test constructor of class EitbIE"""
    #test discovery
    ie = EitbIE()

# Generated at 2022-06-14 16:07:39.192434
# Unit test for constructor of class EitbIE
def test_EitbIE():
    my_test_object = EitbIE()
    assert my_test_object.IE_NAME == 'eitb.tv'
    assert my_test_object._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:07:42.988277
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
        Test of constructor of EitbIE class
    """
    eitb_ie = EitbIE()
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)', "Test failed"
    assert eitb_ie.IE_NAME == 'eitb.tv', "Test failed"
    assert eitb_ie.test() == False, "Test failed"

# Generated at 2022-06-14 16:07:43.793028
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:07:55.036652
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:03.743535
# Unit test for constructor of class EitbIE
def test_EitbIE():
    video_id = '4090227752001'
    video_title = '60 minutos (Lasa y Zabala, 30 años)'
    video_description = 'Programa de reportajes de actualidad.'
    video_thumbnail = 'http://mam.eitb.eus/mam/multimedia/mam/multimedia/vod/mam/images/2013/10/14/mam_mtv_60minutos__4104995149004_4104995156004_4104995158004_4104995159001_thumb_640x360.jpg'
    video_duration = 3996.76
    video_timestamp = 1381789200
    video_tags = ['60', 'minutos', 'lasa', 'zabala', '', '30', 'anos']

   

# Generated at 2022-06-14 16:08:06.159106
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    if not hasattr(ie, "IE_NAME") or ie.IE_NAME != 'eitb.tv':
        raise AssertionError('Invalid IE_NAME')

if __name__ == "__main__":
    test_EitbIE()

# Generated at 2022-06-14 16:08:14.490224
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Example URL:
    url = 'http://www.eitb.tv/eu/bideoak/detalle/1385752/txus-kiss-esan-dut-zuzenean-berriro-kanta-bat-berria'

    # Create object
    ie = EitbIE()

    # Validate URL
    result = ie._VALID_URL.match(url)
    assert result is not None, \
        'URL "%s" is invalid' % url

    # Extract ID from URL
    video_id = result.group('id')
    assert video_id == '1385752', \
        'Video ID is not "1385752"'

# Generated at 2022-06-14 16:08:19.518149
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE("http://www.eitb.tv/eu/bideoa/60-minutos/4104995172001/4090227934001/la-ruta-del-queso-manchego/")
    assert ie is not None

# Generated at 2022-06-14 16:08:21.090304
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE();
    assert eitb.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:08:28.955709
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from . import assertUrlEqual, assertNotEqual

    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    ie = EitbIE()

    # Test case whose URL does not match a regex URL pattern
    not_matching_url = 'http://www.eitb.tv/eu/bideoa/kultura/4058264364001/'
    assertNotEqual(ie.suitable(not_matching_url), True)

    # Test case whose URL matches a regex URL pattern
    assertUrlEqual(ie.suitable(url), True)

# Generated at 2022-06-14 16:11:16.115323
# Unit test for constructor of class EitbIE
def test_EitbIE():
	e = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
	print(e._real_extract(url))

# Generated at 2022-06-14 16:11:18.825156
# Unit test for constructor of class EitbIE
def test_EitbIE():
	#
	# Test constructor of class EitbIE (without arguments)
	#
	try:
		EitbIE()
	except BaseException as e:
		print ('Exception caught trying to create EitbIE instance without arguments.')
		raise e

# Generated at 2022-06-14 16:11:22.455584
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME=="eitb.tv"
    assert EitbIE()._VALID_URL==r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:11:27.482903
# Unit test for constructor of class EitbIE
def test_EitbIE():
    import warnings
    warnings.filterwarnings("ignore")
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

# Generated at 2022-06-14 16:11:32.321304
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie.IE_NAME == 'eitb.tv'
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:11:33.200848
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert "EitbIE" in globals()

# Generated at 2022-06-14 16:11:34.825314
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL

# Generated at 2022-06-14 16:11:38.233025
# Unit test for constructor of class EitbIE
def test_EitbIE():
    b = EitbIE()
    assert b._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:11:45.865855
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:11:48.489802
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from . import extractor_tests

    instance = EitbIE()
    assert isinstance(instance, EitbIE)
    assert isinstance(instance, InfoExtractor)

    extractor_tests.doTestDownload(instance)