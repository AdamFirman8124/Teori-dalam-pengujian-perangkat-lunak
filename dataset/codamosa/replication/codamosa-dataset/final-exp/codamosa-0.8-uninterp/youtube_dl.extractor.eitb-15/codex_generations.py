

# Generated at 2022-06-14 16:03:05.404310
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE()
    # Assert
    assert eitbIE.IE_NAME in eitbIE.ie_key()
    assert eitbIE.IE_NAME in eitbIE.ie_key_test()

# Generated at 2022-06-14 16:03:09.865888
# Unit test for constructor of class EitbIE
def test_EitbIE():
    infoExtractor = EitbIE()
    assert(infoExtractor._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')
test_EitbIE()


# Generated at 2022-06-14 16:03:11.842217
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie_object = EitbIE()
    assert ie_object.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:03:17.355730
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .test_search import mock_search
    from .test_search import MockSearch
    search = MockSearch(
        u'60 minutos (Lasa y Zabala, 30 años)',
        [u'Euskera', u'Euskelaurak', u'Lasa y Zabala', u'60 minutos'])
    mock_search(EitbIE, search, expected_size=3)

# Generated at 2022-06-14 16:03:17.836003
# Unit test for constructor of class EitbIE
def test_EitbIE():
    pass

# Generated at 2022-06-14 16:03:28.471842
# Unit test for constructor of class EitbIE
def test_EitbIE():
    iE = EitbIE()
    assert(iE.IE_NAME == 'eitb.tv')
    assert(iE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')

# Generated at 2022-06-14 16:03:38.644978
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
    assert ie.IE_NAME == "eitb.tv"
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:38.967059
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:03:40.632468
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:03:48.045195
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_case = {
        'url': 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/',
        'info_dict': {
            'id': '4090227752001',
            'ext': 'mp4',
            'title': '60 minutos (Lasa y Zabala, 30 años)',
            'description': 'Programa de reportajes de actualidad.',
            'duration': 3996.76,
            'timestamp': 1381789200,
            'upload_date': '20131014',
            'tags': list,
        },
    }
    assert test_case['info_dict'] == Eit

# Generated at 2022-06-14 16:03:58.786311
# Unit test for constructor of class EitbIE
def test_EitbIE():
	"""
	Unit test for constructor class EitbIE
	"""
	# Calling constructor
	eitb = EitbIE()
	# Testing constructor
	assert eitb.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:03.546480
# Unit test for constructor of class EitbIE
def test_EitbIE():
	"""
	Test for constructor of class EitbIE
	"""

	EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")

# Generated at 2022-06-14 16:04:11.194792
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == 'eitb.tv'
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:13.430987
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb != None


# Generated at 2022-06-14 16:04:19.149800
# Unit test for constructor of class EitbIE
def test_EitbIE():
    a = EitbIE()
    assert a._match_id('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/') =='4090227752001'

# Generated at 2022-06-14 16:04:21.998125
# Unit test for constructor of class EitbIE
def test_EitbIE():
    f = EitbIE(None)
    assert f.IE_NAME == 'eitb.tv'
    assert f.VALID_URL == EitbIE._VALID_URL

# Generated at 2022-06-14 16:04:28.845634
# Unit test for constructor of class EitbIE
def test_EitbIE():
    
    eitb_ie = EitbIE()
    assert eitb_ie is not None
    assert eitb_ie.IE_NAME == 'eitb.tv'
    assert eitb_ie._VALID_URL ==  r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:04:36.009784
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert hasattr(EitbIE, 'IE_NAME')
    assert hasattr(EitbIE, '_VALID_URL')
    assert hasattr(EitbIE, '_TEST')
    assert isinstance(EitbIE._TEST, dict)
    assert 'url' in EitbIE._TEST
    assert 'md5' in EitbIE._TEST
    assert 'info_dict' in EitbIE._TEST
    assert 'video_id' in EitbIE._TEST['info_dict']
    return

# Generated at 2022-06-14 16:04:37.688136
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE(EitbIE.ie_key())
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:40.131733
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print("Ejecución de la prueba para EitbIE")
    #EitbIE(request)
    print("finalizado")

# Generated at 2022-06-14 16:04:56.075172
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = InfoExtractor()
    ie.add_ie(EitbIE)
    ie_name = ie.IE_NAME
    assert ie_name == IE_NAME

# Generated at 2022-06-14 16:05:07.998091
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test of the constructor of class EitbIE with http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/
    try:
        # Creation of a new instance of EitbIE with the valid url
        instance = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
        print("\nClass EitbIE instanced")
    except Exception:
        print("\nERROR: Class EitbIE can't be instanced")


# Generated at 2022-06-14 16:05:17.221551
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie = EitbIE()
    expected = {'id': '4090227752001', 'ext': 'mp4', 'title': '60 minutos (Lasa y Zabala, 30 años)',
                'description': 'Programa de reportajes de actualidad.', 'duration': 3996.76,
                'timestamp': 1381789200, 'upload_date': '20131014', 'tags': list}
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    actual = eitbie._real_extract(url)
    assert actual == expected


# Generated at 2022-06-14 16:05:18.245811
# Unit test for constructor of class EitbIE
def test_EitbIE():
	f = EitbIE()

# Generated at 2022-06-14 16:05:28.838599
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == 'eitb.tv'
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:34.341764
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:05:42.047083
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .common import InfoExtractor, EitbIE
    # Test info extractor without http:// in URL
    url = "www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    eitb = EitbIE(InfoExtractor())
    assert eitb._match_id(url) is not None
    # Test info extractor with http:// in URL
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"

# Generated at 2022-06-14 16:05:44.533415
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:05:51.193660
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # test _VALID_URL
    assert(EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')
    # test instance of InfoExtractor
    ie = EitbIE(InfoExtractor())
    assert(isinstance(ie, InfoExtractor))

# Generated at 2022-06-14 16:05:53.399771
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_EitbIE = EitbIE(None)
    assert isinstance(test_EitbIE, EitbIE)

# Generated at 2022-06-14 16:06:26.660156
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:06:37.736222
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:06:38.867274
# Unit test for constructor of class EitbIE
def test_EitbIE():
    new_url = 'eitb.tv/777'
    ie = EitbIE(new_url)
    assert ie.url == new_url

# Generated at 2022-06-14 16:06:39.755757
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()

# Generated at 2022-06-14 16:06:40.655896
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert isinstance(EitbIE(), InfoExtractor)

# Generated at 2022-06-14 16:06:41.746976
# Unit test for constructor of class EitbIE
def test_EitbIE():
	return EitbIE('test')

# Generated at 2022-06-14 16:06:48.197178
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.ie_key() == 'eitb.tv'
    assert ie.extractor_key() == 'Eitb'
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:53.443437
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie = EitbIE()

    assert eitbie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert eitbie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:56.253181
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert isinstance(eitb_ie, InfoExtractor)
    assert eitb_ie.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:06:58.654858
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .test_video_google import test_constructor, test_suite
    test_constructor(test_suite(__file__, EitbIE), EitbIE)

# Generated at 2022-06-14 16:08:11.254474
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert isinstance(EitbIE, InfoExtractor)

# Generated at 2022-06-14 16:08:13.737860
# Unit test for constructor of class EitbIE
def test_EitbIE():
	try:
		# Code for instantialting class
		EitbIE()
	except NameError:
		assert NameError
	except:
		assert Exception

# Generated at 2022-06-14 16:08:24.408629
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test = EitbIE()
    assert test.IE_NAME == 'eitb.tv'
    assert test._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:31.798050
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test with a valid URL
    eitb = EitbIE()
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:36.647911
# Unit test for constructor of class EitbIE
def test_EitbIE():
    if __name__ == '__main__':
        # If this class is being run from the command line, then it is probably being used to
        # construct unit tests for class EitbIE.  We need to construct an instance of EitbIE in
        # order to do this.
        test_EitbIE()

# Generated at 2022-06-14 16:08:42.984048
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Initialize a instance of this class. print its type.
    eitbie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:08:44.861661
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'



# Generated at 2022-06-14 16:08:46.580525
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Just for coverage, since it is not used
    EitbIE('http://eitb.tv')

# Generated at 2022-06-14 16:08:47.483685
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()

# Generated at 2022-06-14 16:08:49.235007
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:11:36.595438
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE("url", "info", "download", "hls")
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:11:43.664756
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test constructor without parameters
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb._VALID_URL == EitbIE._VALID_URL
    assert eitb._TEST == EitbIE._TEST
    # Test constructor with parameters
    eitb = EitbIE(InfoExtractor.IE_NAME, InfoExtractor._VALID_URL, InfoExtractor._TEST)
    assert eitb.IE_NAME == 'EitbIE'
    assert eitb._VALID_URL == InfoExtractor._VALID_URL
    assert eitb._TEST == InfoExtractor._TEST

# Generated at 2022-06-14 16:11:49.618497
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    url = "http://www.eitb.tv/eu/bideoa/gure-etxea/4104995148001/4104995148001/?autoplay=true&origin=http%3A%2F%2Fwww.eitb.tv"
    result = "http://www.eitb.tv/eu/bideoa/gure-etxea/4104995148001/4104995148001/"
    assert(ie._real_extract(url) == result)

# Generated at 2022-06-14 16:11:53.861471
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Just simple test of EitbIE constructor."""
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:11:55.883713
# Unit test for constructor of class EitbIE
def test_EitbIE():
    i = EitbIE()
    assert i.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:11:57.408181
# Unit test for constructor of class EitbIE
def test_EitbIE():
	e = EitbIE()
	assert(e.IE_NAME == 'eitb.tv')

# Generated at 2022-06-14 16:12:07.470643
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:11.528088
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print('Test constructor of class EitbIE')
    ie = EitbIE()
    print('Passed')


# Generated at 2022-06-14 16:12:12.493079
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert(EitbIE() != None)

# Generated at 2022-06-14 16:12:13.035557
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()