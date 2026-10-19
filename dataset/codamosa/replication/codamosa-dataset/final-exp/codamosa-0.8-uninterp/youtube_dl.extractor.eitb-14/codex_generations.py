

# Generated at 2022-06-14 16:03:06.703422
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()


# Generated at 2022-06-14 16:03:11.514333
# Unit test for constructor of class EitbIE
def test_EitbIE(): 
    class_ = EitbIE
    class_(None)._real_extract('https://www.eitb.tv/eu/bideoa/2018/06/07/bideoak-aparteko-kontzertua-olatu-peio-karen-bideoak-aparteko-kontzertua-/4104995148001/4104995610001/')

# Generated at 2022-06-14 16:03:16.659351
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert(eitb.IE_NAME == 'eitb.tv')
    assert(eitb.VALID_URL == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:03:17.917789
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()

# Generated at 2022-06-14 16:03:23.373219
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e.IE_NAME == 'eitb.tv'
    assert e._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:25.220446
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE_Test = EitbIE('test')
    assert(IE_Test.name == 'EitbTV')

# Generated at 2022-06-14 16:03:32.606114
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Class EitbIE
    """
    #Init
    Eitb = EitbIE()

# Generated at 2022-06-14 16:03:35.273825
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Create an EitbIE object
    from .eitb import EitbIE
    eitbIE = EitbIE()
    assert eitbIE != None

# Generated at 2022-06-14 16:03:41.052195
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")

# Generated at 2022-06-14 16:03:43.606311
# Unit test for constructor of class EitbIE
def test_EitbIE():
    class_ = EitbIE
    assert hasattr(class_, 'IE_NAME')
    assert hasattr(class_, '_VALID_URL')
    assert hasattr(class_, '_TEST')

# Generated at 2022-06-14 16:03:59.543089
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test for constructor of class EitbIE
    #
    # Test for constructor of class EitbIE with invalid url
    #     # Arrange
    #
    #     # Act
    #
    #     # Assert
    # TODO
    # Test for constructor of class EitbIE with valid url
    #     # Arrange
    #     # Act
    #     # Assert
    # TODO
    return

# Generated at 2022-06-14 16:04:05.778143
# Unit test for constructor of class EitbIE
def test_EitbIE():
    v = EitbIE()
    print(v.__module__)
    assert v.IE_NAME == 'eitb.tv'

    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/' 
    m = v._match_id(url)
    assert m == '4090227752001'

# Generated at 2022-06-14 16:04:09.907422
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos/4104995148001/4090227752001/lasa-y-zabala-30-urte/')

# Generated at 2022-06-14 16:04:21.898611
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == url
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'
    assert ie._TEST

# Generated at 2022-06-14 16:04:33.303740
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos/2/3698722/')
    assert ie.IE_NAME == 'eitb.tv'
    assert ie.IE_DESC == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:37.968799
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE("").name == 'eitb.tv'
    assert EitbIE("")._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert EitbIE("").IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:39.422920
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert(EitbIE()._VALID_URL == EitbIE._VALID_URL)

# Generated at 2022-06-14 16:04:41.053351
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert isinstance(EitbIE, InfoExtractor)

# Generated at 2022-06-14 16:04:42.084435
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()

# Generated at 2022-06-14 16:04:46.858257
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:01.665445
# Unit test for constructor of class EitbIE
def test_EitbIE():
    tester = EitbIE()
    assert tester

# Generated at 2022-06-14 16:05:11.500175
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:15.783927
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:05:26.303319
# Unit test for constructor of class EitbIE
def test_EitbIE():
    class_ = EitbIE
    instance = class_()
    assert instance.IE_NAME == 'eitb.tv'
    assert instance._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert instance._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert instance._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2022-06-14 16:05:31.228715
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # First test the class EitbIE constructor
    eitbIE = EitbIE("www.eitb.tv")
    # This test asserts that name of the class is equal to "eitb.tv"
    assert eitbIE.IE_NAME == "eitb.tv"

# Generated at 2022-06-14 16:05:31.798788
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:05:33.164073
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    return eitb_ie

# Generated at 2022-06-14 16:05:34.525959
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert isinstance(EitbIE(), EitbIE)


# Generated at 2022-06-14 16:05:42.146026
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE(None)
    ie.IE_NAME = 'eitb.tv'
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    video_id = '4090227752001'

# Generated at 2022-06-14 16:05:46.541656
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:06:21.004968
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie.IE_NAME == "eitb.tv"
    assert eitb_ie.VALID_URL == "https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)"
    assert eitb_ie.IE_DESC == "eitb.tv with video and other formats support"



# Generated at 2022-06-14 16:06:31.935444
# Unit test for constructor of class EitbIE
def test_EitbIE():
  url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
  eitb_ie = EitbIE()
  # Download webpage
  webpage = eitb_ie._download_webpage(url)

  # Extract video id
  video_id = EitbIE._match_id(url)

  # Get JSON
  video = eitb_ie._download_json('http://mam.eitb.eus/mam/REST/ServiceMultiweb/Video/MULTIWEBTV/%s/' % video_id, video_id)
  assert type(video) is dict

  # Get media

# Generated at 2022-06-14 16:06:33.755572
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    print('EitbIE: ', eitb_ie)

# Generated at 2022-06-14 16:06:40.780244
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Create an instance of class EitbIE
    eitb = EitbIE()

    # Call _real_extract method with a valid url
    result = eitb._real_extract(EitbIE._TEST['url'])

    # Assert that id is correctly obtained
    assert(EitbIE._TEST['info_dict']['id'] == result['id'])

    # Assert that timestamp is correctly obtained
    assert(EitbIE._TEST['info_dict']['timestamp'] == result['timestamp'])

# Generated at 2022-06-14 16:06:41.872587
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()


# Generated at 2022-06-14 16:06:42.727635
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(InfoExtractor({}))

# Generated at 2022-06-14 16:06:53.985502
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:07:02.793541
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:07:06.139248
# Unit test for constructor of class EitbIE
def test_EitbIE():

    assert(EitbIE._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')

# Generated at 2022-06-14 16:07:07.880139
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_obj = EitbIE()
    assert test_obj.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:08:27.215215
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:30.285044
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:36.226067
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_test = EitbIE()
    assert(eitb_test.IE_NAME == 'eitb.tv')
    assert(eitb_test._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')

# Generated at 2022-06-14 16:08:39.746206
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj=EitbIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:08:42.416698
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE({})
    assert isinstance(eitb, EitbIE)


# Generated at 2022-06-14 16:08:48.025535
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/eu/bideoa/news/detail/3238994/oposizioa-euskaltzaindia-kapitalista-eta-rentista-delako-txostena/'
    assert EitbIE._get_video_id(url) == '3238994'
    assert EitbIE._valid_url(EitbIE._match_id(url), 'Eitb')

# Generated at 2022-06-14 16:08:51.984120
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
# Test function test_EitbIE()
test_EitbIE()

# Generated at 2022-06-14 16:08:56.999673
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    ie.extract("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")

# Generated at 2022-06-14 16:09:00.814605
# Unit test for constructor of class EitbIE
def test_EitbIE():
    pass
    #ie = EitbIE(EitbIE._TEST['url'], EitbIE._TEST['md5'], EitbIE._TEST['info_dict'])
    #ie._real_extract(EitbIE._TEST['url'])

# Generated at 2022-06-14 16:09:07.321577
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .constructor import Constructor
    from .common import InfoExtractor

    # Initialization of EitbIE class
    eitbIE = EitbIE("test_case")

    # Test if eitbIE is instance of InfoExtractor
    assert isinstance(eitbIE, InfoExtractor)

    # Test test_constructor_of_EitbIE
    constructor = Constructor("test_constructor_of_EitbIE", eitbIE)
    constructor.test()



# Generated at 2022-06-14 16:11:58.120718
# Unit test for constructor of class EitbIE
def test_EitbIE():
    _eitbIE = EitbIE();


if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:12:09.178102
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie.ie_key() == 'Eitb'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:10.497341
# Unit test for constructor of class EitbIE
def test_EitbIE():
	EitbIE()

# Generated at 2022-06-14 16:12:14.188950
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/') == EitbIE

# Generated at 2022-06-14 16:12:14.696846
# Unit test for constructor of class EitbIE
def test_EitbIE(): return EitbIE({})

# Generated at 2022-06-14 16:12:16.489677
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == "eitb.tv"

# Generated at 2022-06-14 16:12:26.566488
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._build_url(id=4104995148001) == "http://www.eitb.tv/video/60-minutos-60-minutos-2013-2014/4104995148001/"
    assert EitbIE._build_url(id=4104995148001, lang="es") == "http://www.eitb.tv/video/60-minutos-60-minutos-2013-2014/4104995148001/"
    assert EitbIE._build_url(id=4104995148001, lang="eu") == "http://www.eitb.eus/video/60-minutos-60-minutos-2013-2014/4104995148001/"

# Generated at 2022-06-14 16:12:28.756154
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test for the constructor of class EitbIE"""
 
    assert EitbIE('EitbIE').ie == 'EitbIE'

# Generated at 2022-06-14 16:12:29.577252
# Unit test for constructor of class EitbIE
def test_EitbIE():
	e = EitbIE()


# Generated at 2022-06-14 16:12:30.268889
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()