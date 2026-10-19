

# Generated at 2022-06-14 16:03:10.494990
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    return eitb_ie


# Generated at 2022-06-14 16:03:14.866159
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:03:17.269173
# Unit test for constructor of class EitbIE
def test_EitbIE():
	"""
	Unit test for the constructor of class EitbIE
	"""
	assert EitbIE(InfoExtractor()).IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:03:20.234495
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eie = EitbIE()
    assert_equal(eie.IE_NAME,'eitb.tv')
    assert_equal(eie.VALID_URL,'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')


# Generated at 2022-06-14 16:03:22.742691
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .embed import EmbedIE
    # Assert type of IE
    assert isinstance(EitbIE(), EmbedIE)

# Generated at 2022-06-14 16:03:26.617644
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert(ie.IE_NAME == "eitb.tv")
    assert(ie.IE_DESC == "EiTB")
    assert(ie._VALID_URL != None)
    assert(ie._TEST != None)


# Generated at 2022-06-14 16:03:32.720063
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos-zientzia-bihotzaren-kurutzea/4104995148001/4094166512001/')

# Module functions for get_info_extractor(EitbIE)

# Generated at 2022-06-14 16:03:40.358135
# Unit test for constructor of class EitbIE
def test_EitbIE():
	from youtube_dl.version import __version__
	from youtube_dl.compat import compat_str
	from ..utils import *
	from ..extractor import *
	try:
		from ..compat import (
			compat_urllib_parse_urlparse,
		)
	except ImportError:
		from urllib.parse import urlparse as compat_urllib_parse_urlparse
	print("""Test unit for extractor EitbIE .
	""")
	print("""\tTesting constructor...""")
	eitbie = EitbIE();
	assert(eitbie.ie_key() == 'EitbIE')
	assert(eitbie.ie_desc() == 'Eitb')
	print("""\tConstructor test successfull""")

# Generated at 2022-06-14 16:03:40.894528
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_test = EitbIE()

# Generated at 2022-06-14 16:03:41.717393
# Unit test for constructor of class EitbIE
def test_EitbIE():
   assert(EitbIE.IE_NAME == "EitbIE")

# Generated at 2022-06-14 16:03:51.360253
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 16:04:02.123279
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:04:06.626840
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_case = EitbIE('test_case', None)
    assert test_case.IE_NAME == 'eitb.tv'
    assert test_case._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:18.995159
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """ Unit test for constructor of class EitbIE """
    def test_eitb_ie_constructor(url):
        """ Test constructor """
        print("Testing constructor: %s" % url)
        IE = EitbIE()
        Instance = IE(url)
        IE._request_webpage = None
        IE._download_webpage = None
        IE.report_download_page = None
        IE.report_extraction = None
        IE._download_json = None
        IE.to_screen = None
        IE._search_regex = None
        IE._html_search_regex = None
        IE._get_n_search_results = None
        IE._get_search_query = None
        IE._get_titles = None
        IE._get_video_id = None
        IE._get_video

# Generated at 2022-06-14 16:04:21.451584
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = EitbIE._TEST['url']
    ie = EitbIE()
    assert ie.suitable(url) == True

# Generated at 2022-06-14 16:04:32.882596
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test for class EitbIE constructor."""
    # Create EitbIE instance
    ie = EitbIE()
    # Check if EitbIE instance has been correctly constructed
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:34.546911
# Unit test for constructor of class EitbIE
def test_EitbIE():
    end = EitbIE()
    assert end.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:37.129332
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        EitbIE()
    except NameError:
        assert False, 'Could not create EitbIE class'

# Generated at 2022-06-14 16:04:41.341736
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instanceEitbIE = EitbIE()
    if (instanceEitbIE.IE_NAME == 'eitb.tv'):
        print('Unit test for constructor of EitbIE: OK')
    else:
        print('ERROR. Unit test for constructor of EitbIE')


# Generated at 2022-06-14 16:04:51.870302
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:07.245132
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE


# Generated at 2022-06-14 16:05:16.416571
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print("Test EitbIE")
    test_video = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    test_video_id = '4090227752001'

    # Return a json with metadata of the video
    # The case when the videoUrl is valid

# Generated at 2022-06-14 16:05:17.547405
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE(InfoExtractor)

# Generated at 2022-06-14 16:05:18.508527
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE is not None

# Generated at 2022-06-14 16:05:29.120149
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie.name == 'eitb.tv'
    assert ie.title == '60 minutos (Lasa y Zabala, 30 años)'
    assert ie.description == 'Programa de reportajes de actualidad.'
    assert ie.thumbnail == 'http://media.eitb.eus/multimedia/2013/10/14/image/20131014_4104995148001_4090227752001_860.jpg'
    assert ie.duration == 3996.76
    assert ie.timestamp == 1381789200

# Generated at 2022-06-14 16:05:35.006968
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        assert EitbIE()._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    except Exception as ex:
        assert False, "Constructor of class EitbIE does not pass. " + str(ex)

# Generated at 2022-06-14 16:05:38.882252
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Intentionally passing a bad url to constructor of class EitbIE
    # to make sure it raises exception
    return EitbIE("http://www.eitb.tv/es/video/jakintza-jaitsiera-arroparen-inbentarioa/4104911690001/1316170898001/")


# Generated at 2022-06-14 16:05:40.249559
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert(EitbIE('EitbIE').IE_NAME == 'eitb.tv')

# Generated at 2022-06-14 16:05:52.137612
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

# Generated at 2022-06-14 16:06:01.955556
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:35.067192
# Unit test for constructor of class EitbIE
def test_EitbIE():
	instance = EitbIE()
	assert (instance != None)


# Generated at 2022-06-14 16:06:36.025133
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert(EitbIE)

# Generated at 2022-06-14 16:06:39.120135
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj = EitbIE("")
    map(lambda obj: obj.IE_NAME, [obj])
    assert obj.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:44.726311
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Unit test for constructor of class EitbIE"""
    eitbIE = EitbIE()
    assert (eitbIE._VALID_URL == eitbIE.VALID_URL)
    assert (eitbIE._TEST == eitbIE._downloader.TESTS[0])
    assert (eitbIE.IE_NAME == eitbIE.ie_key())
    assert (eitbIE._real_extract is not None)

# Test for method _real_extract()

# Generated at 2022-06-14 16:06:50.309858
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:06:56.988538
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()

    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

# Generated at 2022-06-14 16:06:58.978056
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    ie.extract('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:07:01.072115
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        eitb_ie = EitbIE()
    except:
        assert False, "Error in constructor"


# Generated at 2022-06-14 16:07:05.269365
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert eitbIE._VALID_URL

# Generated at 2022-06-14 16:07:15.025255
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .common import InfoExtractor

    # The URL format is not exactly uniform:
    # it is of the form 'http://www.eitb.tv/(eu/bideoa|es/video)/[^/]+/\d+/\d+'
    # where the second \d+ is prefixed by 60/ for 60 minutos, 6/ for 6 minutos,
    # and generally the first digit of the show name. And the language
    # part is the same as the language of the show, not the current user's.
    # Therefore it is better to provide the ID separately.

# Generated at 2022-06-14 16:08:46.047730
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    url1 = 'http://www.eitb.tv/eu/bideoa/eurosport-eurosport-2015-2016/4104995148001/4104995148001-legendaria/legendaria-lourdes-bernardez-vasco-aitzol-iriondo-mendizaleko-txirrindularia/'
    eitbIE = EitbIE()


# Generated at 2022-06-14 16:08:53.804758
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test for class EitbIE
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    eitb = EitbIE()
    assert eitb._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:59.845422
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print(EitbIE()._extract_urls(
        "Lorem ipsum dolor sit amet http://www.eitb.tv/ es/video/banda-sonora-kale-gorria/4104995148001/4090227752001/ana-danobat-banda-sonora-kale-gorria/ consectetur adipiscing elit."
        ))


# Generated at 2022-06-14 16:09:06.383382
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE("http://www.eitb.tv/eu/bideoa/60-minutos/4104930681001/4090223856001/lasa-y-zabala-30-urte/?tipo=audioa")
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:09:07.743435
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:09:09.161706
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:09:12.447117
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    EitbIE(url)

# Generated at 2022-06-14 16:09:15.538583
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:09:16.275873
# Unit test for constructor of class EitbIE
def test_EitbIE():
    get_testcases_for_extractor(EitbIE)

# Generated at 2022-06-14 16:09:18.761051
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:12:26.029316
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .eitb import EitbIE
    eitbie = EitbIE()
    assert eitbie.IE_NAME == 'eitb.tv'
    assert eitbie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:30.206712
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:12:31.257231
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(InfoExtractor())


# Generated at 2022-06-14 16:12:35.514196
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Should assert the object is an EitbIE of the correct name
    eitbie = EitbIE()
    assert eitbie.IE_NAME == "EitbIE"
    # Should assert the object has the correct name
    assert EitbIE().IE_NAME == 'eitb.tv'

# Unit tests for _real_extract method of class EitbIE
# Should assert the video ID is correctly retrieved form the URL

# Generated at 2022-06-14 16:12:36.631669
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:12:37.363213
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(None)

# Generated at 2022-06-14 16:12:38.511877
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()

# Generated at 2022-06-14 16:12:42.338227
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IEClass = EitbIE
    IEClass._VALID_URL
    IEClass._TEST
    IEClass._extract_m3u8_formats
    IEClass._extract_f4m_formats
    IEClass._real_extract
    IEClass.suitable
    IEClass.ie_key
    IEClass.gen_extractors


# Generated at 2022-06-14 16:12:43.160440
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE()._downloader

# Generated at 2022-06-14 16:12:47.444882
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    hasattr(ie, "extract")