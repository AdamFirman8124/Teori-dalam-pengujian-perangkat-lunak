

# Generated at 2022-06-14 16:03:06.066031
# Unit test for constructor of class EitbIE
def test_EitbIE():
    result = EitbIE().result
    assert result.get('_type') == 'playlist'

# Generated at 2022-06-14 16:03:07.853522
# Unit test for constructor of class EitbIE
def test_EitbIE():
  ie = EitbIE()
  assert ie.IE_NAME is "eitb.tv"



# Generated at 2022-06-14 16:03:09.172503
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE()

# Generated at 2022-06-14 16:03:19.257733
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.__name__ == 'EitbIE'
    assert EitbIE.__doc__ == 'eitb.tv downloader pattern'
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:23.829560
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE(EitbIE._VALID_URL)
    assert ie.name == EitbIE.IE_NAME
    assert ie.url_re == EitbIE._VALID_URL
    assert ie.ie_key() == EitbIE.IE_NAME

# Generated at 2022-06-14 16:03:35.722913
# Unit test for constructor of class EitbIE
def test_EitbIE():
	from tests.test_utils import TestInputFile

	class TestEitbIE(object):
	    def __init__(self, *args, **kwargs):
	        pass

	class TestProvider(object):
	    def __init__(self):
	        self.video_id = '4090227752001'
	        self.episode = '4104995148001'
	        self.url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

# Generated at 2022-06-14 16:03:45.977938
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
    assert ie._VALID_URL == 'https?://(?:www\\.)?eitb\\.tv/(?:eu/bideoa|es/video)/[^/]+/\\d+/(?P<id>\\d+)'

# Generated at 2022-06-14 16:03:48.407759
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test EitbIE class constructor with some sample urls"""
    EitbIE(None)._real_initialize()

# Generated at 2022-06-14 16:03:49.361696
# Unit test for constructor of class EitbIE
def test_EitbIE():
    InfoExtractor.test_IE(EitbIE)

# Generated at 2022-06-14 16:03:50.321922
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:04:02.300199
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE('http://www.eitb.tv/eu/bideoa/elhuyar-euskara-elhuyar-hizkuntza/4104995148001/4063790619001/la-batalla-del-euskara/').ie_name == 'eitb.tv'


# Generated at 2022-06-14 16:04:04.033847
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:05.350020
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert isinstance(ie, EitbIE)

# Generated at 2022-06-14 16:04:11.247994
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE('www.eitb.tv')
    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:23.204810
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:27.061336
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_class = EitbIE('http://www.eitb.tv/eu/bideoa/deportes/futbol/deportes-futbol/4365523/')
    assert test_class, 'Can not instantiate class'

# Generated at 2022-06-14 16:04:28.306571
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert hasattr(EitbIE, "constructor")

# Generated at 2022-06-14 16:04:29.375039
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()

# Generated at 2022-06-14 16:04:30.751016
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE


# Generated at 2022-06-14 16:04:39.581107
# Unit test for constructor of class EitbIE
def test_EitbIE():
    response = urllib2.urlopen(urllib2.Request("http://www.eitb.tv/es/video/zirimiri/4104995022001/4090071031001/los-mejores-momentos-de-zirimiri/")).read()
    for _ in re.findall(r'<a href="(?P<url>http://www\.eitb\.tv/es/video/[^"]+)"', response):
        video_url = _
    test_EitbIE.test.assertTrue(len(video_url) > 0)
    # Testing constructor of class EitbIE
    # The constructor will take a string (url) as argument
    eitb = EitbIE(video_url)
    # Calling function _real_extract
    eit

# Generated at 2022-06-14 16:04:54.595926
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Object creation test
    """
    obj = EitbIE()
    assert obj.IE_NAME == 'eitb.tv'



# Generated at 2022-06-14 16:04:58.390159
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Check if can instance properly
    try:
        EitbIE()
    except Exception as err:
        assert False, 'Could not instance EitbIE class properly: %s' % str(err)
    # end check
# end test

# Generated at 2022-06-14 16:05:03.226654
# Unit test for constructor of class EitbIE
def test_EitbIE():
	ie = EitbIE()
	assert ie.IE_NAME == 'eitb.tv'
	assert ie._VALID_URL == '(?:/bideoa/|/video/)(?:[^/]+/)+(?P<id>\\d+)'

# Generated at 2022-06-14 16:05:07.772447
# Unit test for constructor of class EitbIE
def test_EitbIE():
    r = EitbIE()
    assert EitbIE.IE_NAME == 'eitb.tv'
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:15.711447
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert EitbIE.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:05:16.854047
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:05:21.372974
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:22.811231
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert(EitbIE().IE_NAME == 'eitb.tv')

# Generated at 2022-06-14 16:05:26.714353
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        testEI = EitbIE()
        print("Testing EitbIE constructor")
        print("\tTest OK")
        return True
    except Exception:
        print("\tTest ERROR")
        return False


# Generated at 2022-06-14 16:05:36.341141
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # It is probably a good idea to ensure that the class can be instantiated
    # without exceptions
    #
    # The arguments to the constructor are an optional name, and the IE class
    # to instantiate (in this case EitbIE)
    #
    # When called with the name argument, EitbIE will be added to the list of
    # extractors that can be searched for.  This can, for example, be used to
    # test whether the extractor will handle a given URL
    #
    # In this case EitbIE is instantiated with name set to None, so will not be
    # added to the extractor list.  This is generally what you'd want for unit
    # tests
    ie = InfoExtractor(None, EitbIE)

# Generated at 2022-06-14 16:06:07.239526
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE(None)
    assert eitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:11.156781
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print ("\nStarting tests for EitbIE\n")
    print ("[test_EitbIE] " + "test_no_video" + ": " + "test_no_video" + " passed!!!")
    assert(True)


# Generated at 2022-06-14 16:06:11.687793
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:06:15.563425
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # For now this test case is not useful because it only tests 
    # that the constructor of the class EitbIE works properly.
    # That is because the extractor needs a url to make the test
    # and there is not a url in the unit test case.
    eitbIE = EitbIE()
    assert(type(eitbIE) == EitbIE)

# Generated at 2022-06-14 16:06:19.723348
# Unit test for constructor of class EitbIE
def test_EitbIE():

    # Initializes unit test
    i = EitbIE()

# Generated at 2022-06-14 16:06:21.779159
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb is not None
    assert eitb.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:24.250495
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('eitb.tv')
    assert ie.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:06:28.295658
# Unit test for constructor of class EitbIE
def test_EitbIE():
    a = EitbIE(InfoExtractor())
    assert a._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:33.230482
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:43.125583
# Unit test for constructor of class EitbIE
def test_EitbIE():
	eitb_ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
	assert eitb_ie.IE_NAME == 'eitb.tv'
	assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
	assert eitb_ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:07:48.929256
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()(EitbIE._TEST['url'])

# Generated at 2022-06-14 16:07:59.594035
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test = EitbIE()
    assert test.IE_NAME == 'eitb.tv'
    assert test._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:03.843296
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Tests for the expected return values of class constructor
    obj_eitb = EitbIE(None)
    assert obj_eitb is not None
    assert obj_eitb.ie_key() == 'Eitb'
    assert obj_eitb.ie_name() == 'eitb.tv'
    assert obj_eitb.ie_description() == 'Euskal Irrati Telebista'

# Generated at 2022-06-14 16:08:09.160240
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE()
    assert IE.IE_NAME == "eitb.tv"
    assert IE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert IE._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert IE._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2022-06-14 16:08:13.738091
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:08:15.635782
# Unit test for constructor of class EitbIE
def test_EitbIE():
    t = EitbIE()

# Generated at 2022-06-14 16:08:19.808401
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE('http://mam.eitb.eus/mam/REST/ServiceMultiweb/Video/MULTIWEBTV/4090227752001/')
    assert eitb_ie

# Generated at 2022-06-14 16:08:20.115660
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE

# Generated at 2022-06-14 16:08:24.465063
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2022-06-14 16:08:26.329925
# Unit test for constructor of class EitbIE
def test_EitbIE():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:11:11.065241
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test EitbIE constructor"""

    eitbIE = EitbIE()
    eitbIE.test_test()


# Generated at 2022-06-14 16:11:11.617738
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:11:12.134886
# Unit test for constructor of class EitbIE
def test_EitbIE():
    pass

# Generated at 2022-06-14 16:11:17.958557
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url_eitb = 'http://www.eitb.tv/es/video/euskal-kartzela/4104995148001/4090227752001/'
    eitb_ie = EitbIE()
    assert eitb_ie.suitable(url_eitb)
    url_youtube = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    assert not eitb_ie.suitable(url_youtube)


# Generated at 2022-06-14 16:11:20.821420
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:11:26.415338
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:11:31.625940
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie.IE_NAME == "Eitb.tv"
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:11:35.177054
# Unit test for constructor of class EitbIE
def test_EitbIE():
    t=EitbIE("http://www.eitb.tv/eu/bideoa/video/4104995148001/4090227752001/lasa-y-zabala-30-urte/")

test_EitbIE()

# Generated at 2022-06-14 16:11:39.807888
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from youtube_dl.extractor.eitb import EitbIE
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    e = EitbIE()
    assert e.suitable(url)

# Generated at 2022-06-14 16:11:42.792894
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')