

# Generated at 2022-06-14 16:03:10.619984
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:20.692574
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:03:21.468170
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Unit test for constructor of class EitbIE.
    """
    ie = EitbIE()
    assert ie

# Generated at 2022-06-14 16:03:26.203098
# Unit test for constructor of class EitbIE
def test_EitbIE():
    info = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert (isinstance(info, EitbIE))


# Generated at 2022-06-14 16:03:31.925782
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie_obj = EitbIE()
    assert ie_obj.name == 'EitbIE'
    assert ie_obj.extract('http://www.eitb.tv/eu/bideoa/bideoa/langileak-bideoa/5039134/')


# Generated at 2022-06-14 16:03:32.775559
# Unit test for constructor of class EitbIE
def test_EitbIE():
    pass

# Generated at 2022-06-14 16:03:39.219256
# Unit test for constructor of class EitbIE
def test_EitbIE():
  test_url = 'http://www.eitb.tv/eu/bideoa/euskal-kantak-berriak/4104995148001/4090227801001/asier-huneeus-benito-berriozabala-bixente-urkiza-bixente-uriarte-maite-zabaleta/'
  ie = EitbIE()
  ie.ie_key = 'Eitb'
  ie.get_url_desc = lambda x: ''
  ie._real_initialize(ie.get_url_desc(test_url))


# Generated at 2022-06-14 16:03:47.115023
# Unit test for constructor of class EitbIE
def test_EitbIE():
	from unittest import TestCase
	class TestEitbIE(TestCase):
		def setUp(self):
			self.t = EitbIE()

		def test_eitbIE_constructor(self):
			self.assertIsNotNone(self.t, 'Creation of class EitbIE instance failed')
			self.assertEqual(self.t.IE_NAME, 'eitb.tv', 'The value of IE_NAME class attribute should be "eitb.tv".')
			self.assertIsNotNone(self.t._VALID_URL, 'The value of _VALID_URL class attribute must not be None.')

# Generated at 2022-06-14 16:03:48.975155
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:03:49.577605
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:03:58.937259
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE();
    assert eitb.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:05.487196
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/teleberri/4104995148001/4090227752001/', 'test')
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:04:09.769844
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Check EitbIE.__init__()"""
    a = EitbIE('a')
    assert isinstance(a, InfoExtractor), 'EitbIE should be a subclass of the base InfoExtractor class'


# Generated at 2022-06-14 16:04:16.741298
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:04:21.947426
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE('http://video.euskadi.eus/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:04:33.348399
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Constructor
    ie = EitbIE()
    # File URL
    file_url = 'http://www.eitb.tv/eu/bideoa/detalle/2108241/Euskadi-irati-segitu-nahi-dute-Matxinada-gure-eskolatik/'
    # Video ID
    video_id = ie._match_id(file_url)
    # Make a dictionary to pass arguments of extract() method. If a key is not included, it's treated as None.
    # If a key is None, extract() ignores it.
    # If a key is None, the class' member variable is taken by default.
    kwargs = {'info_dict':{'id': '2108241'}}
    # Extract video

# Generated at 2022-06-14 16:04:34.484445
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:04:35.021668
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:04:36.529947
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie = EitbIE(None)

    assert eitbie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:37.613153
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE()
    assert isinstance(IE, EitbIE)

# Generated at 2022-06-14 16:04:58.929113
# Unit test for constructor of class EitbIE
def test_EitbIE():
    video_test = EitbIE('http://www.eitb.tv/eu/bideoa/informe-especial-eitb/40406895756001/')
    assert video_test.IE_NAME == 'eitb.tv'
    assert video_test._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:01.755034
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test case for constructor of class EitbIE."""
    eitb_ie = EitbIE()

# Generated at 2022-06-14 16:05:08.926808
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('EitbIE')
    # TODO: either remove this test or ensure not to pass any URL, but an object
    assert ie._match_id('https://www.eitb.tv/eu/bideoa/egunkaria/2030348/2030472/') is None
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:05:09.470200
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE

# Generated at 2022-06-14 16:05:11.013731
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:05:17.045862
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv', 'IE_NAME must be eitb.tv'
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)', \
           'URL must follow the regex ' + r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:05:21.234987
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()._real_extract(r'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:05:29.115529
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    url = ie.extract('http://www.eitb.tv/eu/bideoa/talde-txartelak-talde-saio-komikoen-komedia-hilen-efektuak/3801152081001/')
    assert url['id'] == '3801152081001'
    assert url['title'] == 'Talde txartelak - Talde saioa - Komikoen komedia - Hilen efektuak'
    assert url['description'] == 'Ateak zabalik'

# Generated at 2022-06-14 16:05:34.256349
# Unit test for constructor of class EitbIE
def test_EitbIE():
    Ie = EitbIE()
    assert Ie.IE_NAME == 'eitb.tv'
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:42.021277
# Unit test for constructor of class EitbIE
def test_EitbIE():
    info = EitbIE._TEST
    assert info['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert info['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2022-06-14 16:06:14.231123
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print("First: test an EitbIE with an invalid URL")
    test_EitbIE_invalid_url()
    print("Second: test an EitbIE with a valid URL")
    test_EitbIE_valid_url()
    print("Third: test EitbIE with a valid URL from test")
    test_EitbIE_valid_url_from_test()

# Generated at 2022-06-14 16:06:19.216763
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == "eitb.tv"
    ie_eitb = EitbIE("eitb.tv")

    assert ie_eitb.IE_NAME == "eitb.tv"
    assert ie_eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:24.677948
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # pylint: disable=line-too-long
    eitb_ie = EitbIE('Eitb.tv')
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:06:29.444499
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EITB_TV_URL = "http://www.eitb.tv/eu/bideoa/videoa"
    try:
        EitbIE(EITB_TV_URL)
        print("EitbIE created")
    except Exception as ex:
        print("Error creating EitbIE")
        print(ex)
        raise ex

# Generated at 2022-06-14 16:06:40.167448
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:06:49.669155
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj = EitbIE()
    assert obj.IE_NAME == 'eitb.tv'
    assert obj._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert obj._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert obj._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2022-06-14 16:06:53.878962
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
    assert eitbIE != None

# Generated at 2022-06-14 16:06:58.822894
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Function of the class EitbIE that downloads and processes a video file
    eitb = EitbIE(url='http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    eitb.download()

# Generated at 2022-06-14 16:07:00.717102
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE('www.eitb.tv', {})
    assert e.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:07:10.780720
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:37.916418
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from collections import namedtuple
    
    Testcase = namedtuple('Testcase', ['name', 'result'])

    testcases = [Testcase(name='1', result='1')]


# Generated at 2022-06-14 16:08:46.795264
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    A class EitbIE gets the information from the webpage of the EitbTV
    to extract different attributes from the webpage
    """
    from .eitb import EitbIE
    # Create the object of class EitbIE
    eitb_ie = EitbIE()
    # Assert if any parameters are missing in the class
    assert eitb_ie._VALID_URL is not None
    assert eitb_ie._TEST is not None
    assert eitb_ie.IE_NAME is not None
    assert eitb_ie._real_extract is not None
    assert eitb_ie._match_id is not None

# Generated at 2022-06-14 16:08:50.016262
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb._VALID_URL
    assert eitb._TEST.get('url')
    assert 'mam.eitb.eus' in eitb._TEST.get('url')

# Generated at 2022-06-14 16:08:53.174652
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie = EitbIE()
    assert eitbie.IE_NAME == 'eitb.tv'
    assert eitbie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:09:03.691017
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    video_info = e._real_extract(url)
    assert video_info['title'] == "60 minutos (Lasa y Zabala, 30 años)"
    assert video_info['id'] == "4090227752001"

# Generated at 2022-06-14 16:09:04.693670
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:09:13.162885
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert(EitbIE.suitable('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'))
    assert(EitbIE.suitable('http://www.eitb.tv/eu/bideoa/deportes/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'))

# Generated at 2022-06-14 16:09:22.595161
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert hasattr(EitbIE, "IE_NAME")
    assert hasattr(EitbIE, "IE_DESC")
    assert hasattr(EitbIE, "IE_VERSION")
    assert hasattr(EitbIE, "VALID_URL")
    assert hasattr(EitbIE, "URL_REQUEST_HOOK")
    assert hasattr(EitbIE, "SUCCESSFUL_SEARCH_REGEX")
    assert hasattr(EitbIE, "YOUTUBE_IE")
    assert hasattr(EitbIE, "report_download_webpage")
    assert hasattr(EitbIE, "report_extraction")
    assert hasattr(EitbIE, "report_following_redirect")

# Generated at 2022-06-14 16:09:27.901523
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert(ie._TEST['info_dict'] == ie.extract('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'))



# Generated at 2022-06-14 16:09:29.823226
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:12:38.160240
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Unit test for the 'EitbIE' constructor.
    """
    # Create an 'EitbIE' object
    test_eitbie = EitbIE()

    # Check that the 'EitbIE' object is valid
    assert test_eitbie.IE_NAME == 'Eitb'
    assert test_eitbie.VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:38.981043
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()

# Generated at 2022-06-14 16:12:47.894408
# Unit test for constructor of class EitbIE
def test_EitbIE():
    class_name = 'EitbIE'

# Generated at 2022-06-14 16:12:51.913808
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4139120869001/chaves-el-showman/'
    ie.extract_info(url)

# Generated at 2022-06-14 16:12:53.312658
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert (ie.IE_NAME == 'eitb.tv')

# Generated at 2022-06-14 16:13:02.362739
# Unit test for constructor of class EitbIE
def test_EitbIE():
    '''
    Test of class EitbIE
    '''
    # Test with no parameters
    eitb_ie = EitbIE()
    # Test with a none value for url parameter
    eitb_ie = EitbIE(url=None)
    # Test with empty url parameter
    eitb_ie = EitbIE(url='')
    # Test with a none value for ie_key parameter
    eitb_ie = EitbIE(ie_key=None)
    # Test with empty ie_key parameter
    eitb_ie = EitbIE(ie_key='')
    # Test with a none value for video_id parameter
    eitb_ie = EitbIE(video_id=None)
    # Test with empty video_id parameter
    eitb_ie