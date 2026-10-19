

# Generated at 2022-06-14 16:03:12.971969
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Invalid URL
    invalid_url = "http://www.eitb.tv/"
    # Valid URL
    valid_url = "http://www.eitb.tv/eu/bideoa/135578/"

    # Load if invalid URL
    try:
        EitbIE(valid_url)
    except AssertionError:
        # Assertion error if invalid URL
        assert True
    # Load if valid URL
    try:
        EitbIE(valid_url)
        assert True
    except AssertionError:
        assert False

# Generated at 2022-06-14 16:03:14.914236
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print( EitbIE(url="http://www.eitb.tv/es/video/") )

# Generated at 2022-06-14 16:03:18.914943
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/', None) != None


# Generated at 2022-06-14 16:03:20.250029
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE()

# Generated at 2022-06-14 16:03:23.226087
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie.IE_DESC == 'eitb.tv videos'

# Generated at 2022-06-14 16:03:27.957677
# Unit test for constructor of class EitbIE
def test_EitbIE():
	eitb_ie = EitbIE()
	assert eitb_ie.IE_NAME == 'eitb.tv'
	assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:29.126095
# Unit test for constructor of class EitbIE
def test_EitbIE():
    info_extractor = EitbIE()

# Generated at 2022-06-14 16:03:35.124968
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Instantiation of class EitbIE
    eitbIE = EitbIE()
    # Instantiation of class InfoExtractor
    infoExtractor = InfoExtractor()
    # Asserts if the type the name attribute of EitbIE class is equal to unicode
    assert type(eitbIE.IE_NAME) == infoExtractor.type_unicode

# Generated at 2022-06-14 16:03:44.295357
# Unit test for constructor of class EitbIE
def test_EitbIE():
	url= 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
	eitbIE = EitbIE()
	eitbIE._real_extract('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
	return

# Generated at 2022-06-14 16:03:49.089757
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_object = EitbIE()
    valid_test = test_object._VALID_URL
    assert valid_test == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    return test_object

# Generated at 2022-06-14 16:04:04.121358
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # This is a test for constructor.
    # If it fails, it will show error
    assert EitbIE

# Generated at 2022-06-14 16:04:11.339232
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .common import TestCase
    from .common import ExtractorError
    from .extractors.eitb import EitbIE

    # Test for constructor of class EitbIE
    def test_constructor_class_EitbIE():
        try:
            EitbIE()
        except ExtractorError as exc:
            assert exc.args[0] == 'An URL or video id must be provided.'
        except Exception as exc:
            raise TypeError('Exception raised while testing constructor of class EitbIE:' + exc.args[0])
        else:
            pass
        finally:
            pass
    
    # Test cases for constructor of class EitbIE
    # Pass
    test_constructor_class_EitbIE()

test_EitbIE()

# Generated at 2022-06-14 16:04:13.055503
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.__name__ == 'EitbIE'


# Generated at 2022-06-14 16:04:25.253041
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE('http://www.eitb.tv/eu/bideoak/60-minutos/60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert(instance.IE_NAME == 'eitb.tv')
    assert(instance._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')
    assert('id' in instance._real_extract(instance._TEST['url']))
    assert('title' in instance._real_extract(instance._TEST['url']))

# Generated at 2022-06-14 16:04:30.375850
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:39.346117
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:04:40.224910
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:04:44.734646
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/', {}, {})

# Generated at 2022-06-14 16:04:48.655190
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")


# Generated at 2022-06-14 16:04:51.008983
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.ie_key() == 'eitb.tv'
    assert EitbIE.ie_utils_key() == 'EiTBTVUtils'

# Generated at 2022-06-14 16:05:06.233364
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert isinstance(EitbIE({}), InfoExtractor)

# Generated at 2022-06-14 16:05:12.563381
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE("http://www.eitb.tv/eu/bideoa/60-minutos/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.extract == EitbIE._real_extract


# Generated at 2022-06-14 16:05:21.372634
# Unit test for constructor of class EitbIE
def test_EitbIE():
    import unittest
    eitb = EitbIE()
    class TestEitbIE(unittest.TestCase):
        pass
    attrs = dict((attr, getattr(EitbIE, attr)) for attr in dir(EitbIE) if isinstance(getattr(EitbIE, attr), property))
    for attr, value in attrs.items():
        setattr(TestEitbIE, 'test_%s' % attr, lambda self, attr=attr, value=value: self.assertEqual(value, getattr(eitb, attr)))
    unittest.main(argv=[''], verbosity=2, exit=False)

# Generated at 2022-06-14 16:05:26.443136
# Unit test for constructor of class EitbIE
def test_EitbIE():
    E = EitbIE()
    assert E.IE_NAME == 'eitb.tv'
    assert E._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:05:27.894681
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE(EitbIE.ie_key())

# Generated at 2022-06-14 16:05:31.932977
# Unit test for constructor of class EitbIE
def test_EitbIE():
	IE = EitbIE()
	IE._download_json('...', '...', 'Downloading video JSON')
	IE._match_id(IE._VALID_URL)
	IE._real_extract(IE._TEST['url'])

# Generated at 2022-06-14 16:05:37.825842
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME
    assert EitbIE._VALID_URL
    assert EitbIE._TEST
    ie = EitbIE(EitbIE._TEST)
    assert ie.name == EitbIE.IE_NAME
    assert ie._VALID_URL == EitbIE._VALID_URL
    assert ie._TEST == EitbIE._TEST
    assert ie._downloader.params['outtmpl'] == '%(id)s.%(ext)s'

# Generated at 2022-06-14 16:05:39.930680
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:05:51.732748
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:01.660196
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:06:34.438096
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:39.036042
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    
    EitbIE()._real_extract(url)

# Generated at 2022-06-14 16:06:40.730265
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print("Testing class EitbIE")
    print("=====================")
    print("Done unit testing class")
    print("========================")
    print("")
    print("")
    return


# Generated at 2022-06-14 16:06:47.333350
# Unit test for constructor of class EitbIE
def test_EitbIE():
    class FakeInfoExtractor(InfoExtractor):
        def report_warning(self, message, video_id=None):
            pass

    result = EitbIE()
    assert result.name == 'eitb.tv'
    assert result.IE_NAME == 'eitb.tv'
    assert result._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:50.310922
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Tests that _TEST instance matches against EitbIE._TEST"""
    assert EitbIE._TEST == EitbIE._TEST

# Generated at 2022-06-14 16:06:56.217382
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Download the JSON metadata of a video
    video_id = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    video = EitbIE()._download_json(
        'http://mam.eitb.eus/mam/REST/ServiceMultiweb/Video/MULTIWEBTV/%s/' % video_id,
        video_id, 'Downloading video JSON')

    # Verify that obtained a JSON 
    assert len(video) == 2
    assert 'web_media' in video.keys()
    assert 'web_subtitles' in video.keys()

    # Verify that we obtained a list

# Generated at 2022-06-14 16:06:56.784957
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:06:58.978043
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:07:02.961414
# Unit test for constructor of class EitbIE
def test_EitbIE():
	""" test if constructor creates a valid object EitbIE """
	url = 'http://www.eitb.tv/es/video/makroekonomia/279045/'
	video_id = '279045'
	EitbIE(url)._match_id(url) == video_id

# Generated at 2022-06-14 16:07:03.497351
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:08:22.478908
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    # Test not implemented
    pass

# Generated at 2022-06-14 16:08:24.986924
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie_instance = EitbIE()
    print(eitb_ie_instance)
    #return eitb_ie_instance
    assert 1==1


# Generated at 2022-06-14 16:08:27.660989
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:33.964308
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert eitb.IE_NAME =='eitb.tv'

# Generated at 2022-06-14 16:08:38.889145
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == 'eitb.tv'
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:08:47.438991
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == 'http://www\.eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.site_name == 'eitb.tv'
    assert ie.test_url == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

# Generated at 2022-06-14 16:08:51.542935
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'sample url'
    name = 'sample name'
    ie = EitbIE(url, name)
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:09:02.734846
# Unit test for constructor of class EitbIE
def test_EitbIE():
	obj = EitbIE()
	assert(obj.IE_NAME == 'eitb.tv')
	assert(obj._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')

# Generated at 2022-06-14 16:09:11.946159
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test URL with a valid ID
    # http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    # Check if the URL is valid
    assert EitbIE._VALID_URL.match(url) is not None
    # Get info about the video
    info = EitbIE()._real_extract(url)

# Generated at 2022-06-14 16:09:13.314359
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Unit test for constructor of class EitbIE
    """
    return EitbIE()


# Generated at 2022-06-14 16:12:14.378813
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:12:16.490777
# Unit test for constructor of class EitbIE
def test_EitbIE():
    c = EitbIE()
    assert hasattr(c, '_VALID_URL')
    assert hasattr(c, '_TEST')

# Generated at 2022-06-14 16:12:27.171178
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test for EitbIE
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    # Test for _VALID_URL
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    # Test for IE_NAME
    assert ie.IE_NAME == 'eitb.tv'
    # Test for _TEST

# Generated at 2022-06-14 16:12:35.227207
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie['IE_NAME'] == 'eitb.tv'
    assert ie['IE_VALID_URL'] == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:37.026304
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # This test checks if the given URL can be instantiated as a EitbIE class.
    # More details are given in the class constructor.
    assert True == bool(EitbIE(None))

# Generated at 2022-06-14 16:12:40.679714
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:12:50.501923
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from ..utils import load_resource
    from ..utils import compat_str
    from ..utils import compat_urllib_parse
    from ..utils import compat_urllib_request

    class MockUrlOpen(object):
        def __init__(self, *args, **kwargs):
            pass

        def read(self, *args, **kwargs):
            return load_resource('eitb')
    compat_urllib_request.urlopen = MockUrlOpen

    video_url = 'http://eitb.tv/tv/programas/bideoak_es/detalle/4090227752001-60-minutos-lasa-y-zabala-30-anos/'
    ie = EitbIE()

# Generated at 2022-06-14 16:12:57.899404
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie.IE_NAME == 'eitb.tv' # Test IE_NAME
    assert eitb_ie._VALID_URL == r'^https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)$' # Test _VALID_URL