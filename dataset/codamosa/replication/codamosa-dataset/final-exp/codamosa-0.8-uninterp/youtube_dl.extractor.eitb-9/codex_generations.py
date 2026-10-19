

# Generated at 2022-06-14 16:03:11.203840
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test case:
    #  http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    instance = EitbIE()

    # The unit test asserts the object was created properly
    assert instance.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:03:21.609519
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb.IE_DESC == 'eitb.tv'
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    # Test for instantiation of EitbIE
    video = eitb.ie_key()(EitbIE._TEST.get('url'))
    assert video.display_id() == '4090227752001'
    assert video.title() == '60 minutos (Lasa y Zabala, 30 años)'

# Generated at 2022-06-14 16:03:30.595410
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:03:39.655522
# Unit test for constructor of class EitbIE
def test_EitbIE():
    info_extractor = EitbIE()
    assert info_extractor.IE_NAME == 'eitb.tv'
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:40.931800
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE()
    IE.IE_NAME
    IE.IE_VERSION
    IE.IE_DESC
    IE._VALID_URL

# Generated at 2022-06-14 16:03:42.848618
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE()
    assert instance.name == 'eitb.tv'
    assert instance.ie_key() == 'Eitb'

# Generated at 2022-06-14 16:03:44.585652
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj = EitbIE()
    assert obj is not None

# Generated at 2022-06-14 16:03:48.707578
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE();
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:50.519321
# Unit test for constructor of class EitbIE
def test_EitbIE():
    classe = EitbIE()
    assert(classe is not None)

# Generated at 2022-06-14 16:04:01.171625
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert(repr(ie) == 'EitbIE()')


# test case for EitbIE

# Generated at 2022-06-14 16:04:17.186318
# Unit test for constructor of class EitbIE
def test_EitbIE():
    bet = True
    try: EitbIE()
    except: bet = False
    assert bet

# Generated at 2022-06-14 16:04:22.128517
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert EitbIE._SINGLE_PAGE_RESULTS == False
    assert EitbIE._download_playlist == False
    assert EitbIE._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert EitbIE._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert E

# Generated at 2022-06-14 16:04:27.153696
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE()
    assert instance._VALID_URL == 'https?://(?:www\\.)?eitb\\.tv/(?:eu/bideoa|es/video)/[^/]+/\\d+/(?P<id>\\d+)'
    assert instance.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:32.091760
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert isinstance(e, EitbIE)

# Generated at 2022-06-14 16:04:35.354502
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:35.893304
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:04:45.975610
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from . import EitbIE

    # Test for generation of correct Pafy object
    result = EitbIE()._real_extract(EitbIE._TEST['url'])
    assert result['id'] == '4090227752001'

# Generated at 2022-06-14 16:04:52.144874
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    video_id = '4090227752001'
    title = '60 minutos (Lasa y Zabala, 30 años)'
    description = 'Programa de reportajes de actualidad.'
    timestamp = 1381789200
    ie = EitbIE()
    ie.IE_NAME = 'eitb.tv'
    ie._VALID_URL = r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:04:53.041139
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE()

# Generated at 2022-06-14 16:04:53.534237
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:05:09.635326
# Unit test for constructor of class EitbIE
def test_EitbIE():
    class_ = EitbIE
    # Instantiate the class
    d = class_()
    # test type
    assert isinstance(d, InfoExtractor)
    # test inheritance
    assert issubclass(class_, InfoExtractor)


# Generated at 2022-06-14 16:05:15.585678
# Unit test for constructor of class EitbIE
def test_EitbIE():

	# !!! NEED TO BE CHANGED !!!
	urlTest = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"

	EitbIE._real_extract(EitbIE(), urlTest)


__all__ = ['EitbIE', 'test_EitbIE']

# Generated at 2022-06-14 16:05:19.202530
# Unit test for constructor of class EitbIE
def test_EitbIE():
	EitbIE('http://www.eitb.tv/eu/bideoa/bideoak/partidua-agarik-ez-da-mahairik/4090227725001/4090227747001/?p=4090227752001')

# Generated at 2022-06-14 16:05:30.591163
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .common import InfoExtractor
    from .eitb import EitbIE
    from .youtube import YoutubeIE
    from .youtube import YoutubeIE as YoutubeIE_new
    import re

    ie_lr_eitb = InfoExtractor.list_class(EitbIE)
    assert len(ie_lr_eitb) == 1
    assert ie_lr_eitb [0] == (EitbIE.IE_NAME, EitbIE.IE_DESC, EitbIE._VALID_URL)
    assert re.search(EitbIE._VALID_URL, 'http://www.eitb.tv/eu/bideoa/gaztetxe/20137976/20127092/') != None

# Generated at 2022-06-14 16:05:39.619421
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    ie = EitbIE(url)
    info = ie._real_extract(url)
#     print 'Info:', info
    assert(len(info) == 8)
    assert(info['id'] == '4090227752001')
    assert(info['ext'] == 'mp4')
    assert(info['title'] == '60 minutos (Lasa y Zabala, 30 años)')
    assert(info['description'] == 'Programa de reportajes de actualidad.')

# Generated at 2022-06-14 16:05:40.138298
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:05:45.328144
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    info = ie.extract('http://www.eitb.tv/eu/bideoa/todos-nuestros-avances-en-un-solo-video')
    assert(info['title'] == 'Todos nuestros avances en un solo video')

# Generated at 2022-06-14 16:05:46.337886
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE(object)



# Generated at 2022-06-14 16:05:49.045580
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:05:50.007223
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._TEST

# Generated at 2022-06-14 16:06:21.362952
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(None)

# Generated at 2022-06-14 16:06:29.113014
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .common import InfoExtractor

    assert EitbIE.IE_NAME == 'eitb.tv'
    assert EitbIE.VALID_URL == EitbIE._VALID_URL
    assert EitbIE.TEST == EitbIE._TEST
    assert EitbIE.__name__ == 'EitbIE'
    assert EitbIE.__doc__ == InfoExtractor.__doc__
    assert EitbIE.__module__ == InfoExtractor.__module__
    assert EitbIE.__class__ == InfoExtractor

# Generated at 2022-06-14 16:06:34.173608
# Unit test for constructor of class EitbIE
def test_EitbIE():

    ie = EitbIE()
    assert ie.IE_NAME == "eitb.tv"
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:40.493724
# Unit test for constructor of class EitbIE
def test_EitbIE():
    class_ = EitbIE
    ie = class_()
    assert ie.ie_key() == 'Eitb'
    assert ie.ie_key() in class_.ie_keys()
    assert ie.extract('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:06:43.694134
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:06:52.245687
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .common import InfoExtractor
    from ..utils import (
        float_or_none,
        int_or_none,
        parse_iso8601,
        sanitized_Request,
    )
    url = "http://www.eitb.tv/eu/bideoa/60-minutos/60-minutos-2014-2015/4153931493001/4090227752001/lasa-y-zabala-30-urte/"
    ie = InfoExtractor()
    ie.add_info_extractor(EitbIE)
    ie.extract(url)

# Generated at 2022-06-14 16:06:53.219557
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(None, None)

# Generated at 2022-06-14 16:06:57.576447
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert_true(ie._VALID_URL)
    assert_true(ie._TEST)
    assert_false(ie._GEO_COUNTRIES)
    assert_false(ie._GEO_BYPASS)
    assert_true(ie._downloader)
    assert_true(ie._WORKING)

# Generated at 2022-06-14 16:06:58.118855
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE

# Generated at 2022-06-14 16:07:01.937709
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test = EitbIE()
    assert test.IE_NAME == 'eitb.tv'
    assert test._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:08:19.974585
# Unit test for constructor of class EitbIE
def test_EitbIE():
	EitbIE('www.eitb.tv/eu/bideoa/', 'www.eitb.tv/eu/bideoa/', r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')


# Generated at 2022-06-14 16:08:21.171307
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert(EitbIE.IE_NAME == 'eitb.tv')

# Generated at 2022-06-14 16:08:22.560946
# Unit test for constructor of class EitbIE
def test_EitbIE():
    raise Exception("Unit test for class EitbIE not implemented")

# Generated at 2022-06-14 16:08:26.926479
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Testing URLs
    EitbIE_url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    EitbIE_url2 = 'http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/berriak-eta-natura/'
    EitbIE_url3 = 'http://www.eitb.tv/eu/bideoa/gaur-egun/4117449610001/4204337792001/gaur-egun/'
    # Creation of a new instance

# Generated at 2022-06-14 16:08:27.733959
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()

# Generated at 2022-06-14 16:08:34.008612
# Unit test for constructor of class EitbIE
def test_EitbIE():
	e = EitbIE()
	assert e.IE_NAME == 'eitb.tv'
	assert e._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:45.056391
# Unit test for constructor of class EitbIE
def test_EitbIE():

    info_extractor = EitbIE()

    # Test 1

# Generated at 2022-06-14 16:08:51.312393
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == '^https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)$'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

# Generated at 2022-06-14 16:08:56.088221
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # This unit test is intended to check the existence of constructor of class EitbIE
    eitb_ie = EitbIE("")
    eitb_ie.IE_NAME


if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:08:57.492926
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE(EitbIE.IE_NAME)

# Generated at 2022-06-14 16:11:47.283596
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        EitbIE()
    except Exception as e:
        assert False, "Construction of erEitbIEd class failed with message: "+str(e)


# Generated at 2022-06-14 16:11:48.703239
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Test class constructor
    """
    ie = EitbIE()
    assert ie.ie_key() == 'eitb.tv'

# Generated at 2022-06-14 16:11:54.520710
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert EitbIE._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert EitbIE._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert EitbIE._TEST['info_dict']['id'] == '4090227752001'
    assert EitbIE._T

# Generated at 2022-06-14 16:12:00.013146
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:12:09.427455
# Unit test for constructor of class EitbIE
def test_EitbIE():
    
    eitbIE = EitbIE(EitbIE.IE_NAME, EitbIE._VALID_URL)

    assert eitbIE.ie_key() == EitbIE.IE_NAME
    assert eitbIE.suitable(EitbIE._VALID_URL)
    assert eitbIE.IE_NAME == 'eitb.tv'
    assert eitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    
    

# Generated at 2022-06-14 16:12:11.735939
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(InfoExtractor)


# Generated at 2022-06-14 16:12:15.056293
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Create instance of the EitbIE class
    instance = EitbIE()
    # Test for the name of the class
    assert instance.IE_NAME == 'eitb.tv'
    # Test for the subclass
    assert issubclass(EitbIE, InfoExtractor)

# Generated at 2022-06-14 16:12:17.989171
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    EitbIE(url)

# Generated at 2022-06-14 16:12:28.526996
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e.IE_NAME == 'eitb.tv'
    assert e._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:36.138229
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)', "Base URL of EitbIE is not correct"