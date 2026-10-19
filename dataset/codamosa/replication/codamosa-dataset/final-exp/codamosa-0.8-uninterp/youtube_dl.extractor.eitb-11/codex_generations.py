

# Generated at 2022-06-14 16:03:15.811345
# Unit test for constructor of class EitbIE
def test_EitbIE():
    class_ = globals()['EitbIE']
    ie = class_()
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:16.743269
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE()

# Generated at 2022-06-14 16:03:27.474610
# Unit test for constructor of class EitbIE
def test_EitbIE():
    import copy
    import os
    from .common import EitbIE

    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    dirname = os.path.dirname(__file__)
    result_JSON_path = os.path.join(dirname, 'tests', 'data', 'eitb.tv', '4090227752001.json')
    result_JSON = open(result_JSON_path).read()
    # Tests constructor
    eitbIE = EitbIE(url)
    assert isinstance(eitbIE, EitbIE)

# Generated at 2022-06-14 16:03:30.884941
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        EitbIE()
    except Exception as e:
        print(e)
        assert False, "Fail to instantiate class"


# Generated at 2022-06-14 16:03:38.966140
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    eitb_ie_obj = EitbIE()
    ret = eitb_ie_obj._real_extract(url)
    assert(ret['id'] == '4090227752001')
    assert(ret['title'] == '60 minutos (Lasa y Zabala, 30 años)')
    assert(ret['duration'] == 3996.76)
    assert(ret['tags'] == None)

# Generated at 2022-06-14 16:03:40.060975
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from EitbIE import EitbIE
    i = EitbIE()
    assert i is not None


# Generated at 2022-06-14 16:03:41.306130
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE(EitbIE.IE_NAME)

# Generated at 2022-06-14 16:03:44.723501
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie == 1


# Generated at 2022-06-14 16:03:45.551495
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE({})

# Generated at 2022-06-14 16:03:50.654628
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj = EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4126686130001/los-desguaces-de-la-banca/')
    print (obj.extract())

# Generated at 2022-06-14 16:04:05.569866
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE is not None

# Generated at 2022-06-14 16:04:15.990236
# Unit test for constructor of class EitbIE
def test_EitbIE():
	eitb = EitbIE()
	eitb_url = "http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
	eitb_extract = eitb._real_extract(eitb_url)
	assert eitb_extract["id"] == "4090227752001"
	assert eitb_extract["ext"] == "mp4"
	assert eitb_extract["description"] == u"Programa de reportajes de actualidad."


# Generated at 2022-06-14 16:04:27.368995
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # This unit test checks if the constructor of class EitbIE works properly
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
   

# Generated at 2022-06-14 16:04:28.448651
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert isinstance(EitbIE(), InfoExtractor)

# Generated at 2022-06-14 16:04:32.883561
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:04:37.017319
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert (eitb_ie.IE_NAME == 'eitb.tv')
    assert (eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')


# Generated at 2022-06-14 16:04:39.056790
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME in InfoExtractor._ALL_CLASSES, "EitbIE class not found in InfoExtractor._ALL_CLASSES"


# Generated at 2022-06-14 16:04:40.266046
# Unit test for constructor of class EitbIE
def test_EitbIE():
	ie = EitbIE()

# Generated at 2022-06-14 16:04:42.360548
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from . import tests_EitbIE as tEitb
    tEitb.test_EitbIE()

# Generated at 2022-06-14 16:04:45.322320
# Unit test for constructor of class EitbIE
def test_EitbIE():
    #Expected value:
    #Type: bool
    assert bool(EitbIE('http://www.eitb.tv/eu/bideoa/'))


# Generated at 2022-06-14 16:05:10.078924
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    class_EitbIE = EitbIE(url)
    assert class_EitbIE.IE_NAME == 'eitb.tv'
    assert class_EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:10.908295
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:05:19.201909
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    url = 'http://www.eitb.tv/eu/bideoa/60-minutos/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    extractor = EitbIE._get_video_extractor(url)
    assert EitbIE == extractor.__class__
    assert extractor._real_extract == EitbIE._real_extract


# Generated at 2022-06-14 16:05:29.116662
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/parade/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    url2 = 'http://www.eitb.tv/eu/bideoa/614/4090227752001/'
    # Test case 1: url not well-formed
    if (EitbIE._VALID_URL == url):
        raise ExtractorError('URL mal formada.')

    # Test case 2: url is well-formed
    if (EitbIE._VALID_URL == url2):
        print('URL bien formada.')
# Testing the class EitbIE
test_EitbIE()



# Generated at 2022-06-14 16:05:33.879166
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie = EitbIE("EitbIE", "http://www.eitb.tv/eu/bideoa/60-minut/4104995148001/4090227752001/lasa-y-zabala-30-urte/", {}, True)


# Generated at 2022-06-14 16:05:37.867479
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)', "Valid URL is assumed to be %s" % e._VALID_URL

# Generated at 2022-06-14 16:05:39.647872
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test EitbIE
    eitbIE = EitbIE()

# Generated at 2022-06-14 16:05:51.442398
# Unit test for constructor of class EitbIE
def test_EitbIE():

    assert(EitbIE("https://www.eitb.tv/eu/bideoa/euskalherria-7-etorria/4104995332001/")
           == "4104995332001")
    assert(EitbIE("http://www.eitb.tv/eu/bideoa/60-minutos/4104995218001/")
           == "4104995218001")
    assert(EitbIE("http://www.eitb.tv/eu/bideoa/jarraibideak/4104995244001/")
           == "4104995244001")

# Generated at 2022-06-14 16:06:01.373426
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie.url == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie.video_id == '4090227752001'
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:04.469249
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie.IE_NAME == "eitb.tv"
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:44.778605
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:55.823860
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:57.906838
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from ..utils import ExtractorError

    try:
        EitbIE()
    except ExtractorError:
        assert False, 'should not raise'

# Generated at 2022-06-14 16:07:00.804013
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:07:10.861034
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:07:14.203560
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:07:15.025833
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(None)

# Generated at 2022-06-14 16:07:21.398210
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE(None)
    assert ie.ie_key() == 'eitb.tv'
    assert ie.ie_name() == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:07:22.858632
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbi = EitbIE()
    print(eitbi)

# Generated at 2022-06-14 16:07:32.533438
# Unit test for constructor of class EitbIE
def test_EitbIE():
    import os
    import unittest
    from test.test_utils import pprint, stringify_dict
    EitbIE.description = 'test'
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    ref_md5 = "edf4436247185adee3ea18ce64c47998"
    # Load EitbIE class and test
    test = unittest.TestLoader().loadTestsFromTestCase(EitbIE)
    outfile = open(os.devnull, "w")
    # Run the EitbIE test

# Generated at 2022-06-14 16:08:50.773855
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:09:01.586356
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Testing construction
    eitb = EitbIE
    assert(eitb._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')
    assert(eitb._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert(eitb._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998')

# Generated at 2022-06-14 16:09:05.337237
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:09:08.651636
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:09:12.482587
# Unit test for constructor of class EitbIE
def test_EitbIE():
    n = EitbIE()
    assert n.IE_NAME == 'eitb.tv'
    assert n._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:09:16.889330
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test for url for the test case
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    ie = EitbIE()
    result = ie.extract(url)
    assert result['id'] == '4090227752001'

# Generated at 2022-06-14 16:09:21.222806
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Simple test to check if constructor is ok or not
    _ = EitbIE('https://www.eitb.eus/es/video/TV/detalle/4113028315001/60-minutos-60-minutos-2013-2014/')

# Generated at 2022-06-14 16:09:31.158579
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test case 1
    eitbIE = EitbIE()
    assert eitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

    # Test case 2

# Generated at 2022-06-14 16:09:37.595512
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.IE_NAME == 'eitb.tv'

# Downloading video JSON and asserting the title (unit test)

# Generated at 2022-06-14 16:09:39.563433
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie is not None

# Generated at 2022-06-14 16:12:39.458621
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:42.797569
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # These tests should pass
    assert EitbIE()
    assert EitbIE(IE_NAME)
    assert EitbIE(IE_NAME, _VALID_URL)
    ie = EitbIE(IE_NAME, _VALID_URL)
    assert ie.extract(url)

# Generated at 2022-06-14 16:12:44.213833
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:12:48.308536
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:12:50.382796
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # If a test fails, this will raise an exception and give a stack trace
    ie = EitbIE()

# Generated at 2022-06-14 16:12:51.514398
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Test constructor of EitbIE
    """
    EitbIE()

# Generated at 2022-06-14 16:12:53.205667
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test that the constructor of EitbIE does not crash
    eitbie = EitbIE(None)
    assert eitbie

# Generated at 2022-06-14 16:12:54.237978
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:13:03.615868
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'