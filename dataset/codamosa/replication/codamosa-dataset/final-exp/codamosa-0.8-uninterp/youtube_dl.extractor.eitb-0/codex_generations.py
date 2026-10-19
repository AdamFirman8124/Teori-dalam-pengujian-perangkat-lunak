

# Generated at 2022-06-14 16:03:13.517096
# Unit test for constructor of class EitbIE
def test_EitbIE():
  url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
  eitb = EitbIE()
  assert eitb != None
  assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:15.363468
# Unit test for constructor of class EitbIE
def test_EitbIE():
    info_extractor_test = EitbIE()
    info_extractor_test.suite()

# Generated at 2022-06-14 16:03:16.303133
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE() != None

# Generated at 2022-06-14 16:03:16.883622
# Unit test for constructor of class EitbIE
def test_EitbIE():
    pass

# Generated at 2022-06-14 16:03:17.789187
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE  # make sure it is imported

# Generated at 2022-06-14 16:03:28.118112
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eie = EitbIE()
    eie._download_json = lambda url: url.split('/')[-1]
    assert eie._real_extract_ex({'id': '4104995148001'}) == {
        'id': '4104995148001',
        'title': '4104995148001',
        'formats': [
            {
                'format_id': 'http-1000',
                'url': '4104995148001',
            },
            {
                'format_id': 'http-400',
                'url': '4104995148001',
            },
            {
                'format_id': 'http-200',
                'url': '4104995148001',
            },
        ],
    }

# Generated at 2022-06-14 16:03:28.791500
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE

# Generated at 2022-06-14 16:03:29.899276
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE()

# Generated at 2022-06-14 16:03:31.611604
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE_TEST = EitbIE()
    assert IE_TEST

# Generated at 2022-06-14 16:03:36.517679
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Load url from file and print formatted url
    from os.path import join
    from pycaption import datauploader
    data, url = datauploader.geUrlFromFile(join('test_data','url.txt'))
    ie = EitbIE(url)

# Generated at 2022-06-14 16:03:53.233400
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        # test valid
        EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")

        # test invalid
        EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/asasd")
        assert False
    except AssertionError:
        # Test invalid url
        print("test_EitbIE Passed!")
test_EitbIE()

# Generated at 2022-06-14 16:03:54.251578
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()  # To test its creation.

# Generated at 2022-06-14 16:03:59.806918
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:00.760153
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE()

# Generated at 2022-06-14 16:04:05.067993
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie_instance = EitbIE()
    assert eitbie_instance.IE_NAME == "eitb.tv"
    assert eitbie_instance._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:07.246542
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE()
    assert type(instance) is EitbIE

# Generated at 2022-06-14 16:04:10.041613
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert repr(ie) == "<EitbIE 'eitb.tv'>"


# Generated at 2022-06-14 16:04:11.048363
# Unit test for constructor of class EitbIE
def test_EitbIE():
	EitbIE(InfoExtractor)



# Generated at 2022-06-14 16:04:17.532414
# Unit test for constructor of class EitbIE
def test_EitbIE():
    r = sanitized_Request("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
    m = EitbIE()
    test = m.suitable(r)
    assert test

# Generated at 2022-06-14 16:04:22.477251
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(EitbIE.IE_NAME, {'url': 'http://www.eitb.tv/eu/bideoa/60-minutos/4104995148001/4090227752001/lasa-y-zabala-30-anos/'})
# end of test_EitbIE

# Generated at 2022-06-14 16:04:45.797558
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    info_dict = {
        'id': '4090227752001',
        'ext': 'mp4',
        'title': '60 minutos (Lasa y Zabala, 30 años)',
        'description': 'Programa de reportajes de actualidad.',
        'duration': 3996.76,
        'timestamp': 1381789200,
        'upload_date': '20131014',
        'tags': 'list'
    }

    info = EitbIE()._real_extract(url)
    assert info == info_dict

# Generated at 2022-06-14 16:04:51.900769
# Unit test for constructor of class EitbIE
def test_EitbIE():
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	from .common import InfoExtractor
	

# Generated at 2022-06-14 16:04:52.452732
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:04:58.342814
# Unit test for constructor of class EitbIE
def test_EitbIE():
    found = EitbIE()._extract_urls(
                "https://www.eitb.tv/eu/bideoa/bideoa/elkargunea/2017312-elkargunea-vigo-torneo-slalom-sup-ibilbide-komunikabide-interaktiboak-euskaraz-titulazio-libre-hitza/")
    assert 1 == len(found)

# Generated at 2022-06-14 16:05:00.275284
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert(EitbIE() is not None)

# Generated at 2022-06-14 16:05:03.035961
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    EitbIE(url)

# Generated at 2022-06-14 16:05:06.470747
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert isinstance(EitbIE, InfoExtractor)
    assert hasattr(EitbIE, '_VALID_URL')
    assert isinstance(EitbIE._VALID_URL, unicode)


# Generated at 2022-06-14 16:05:10.204017
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL.startswith('https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/')

# Generated at 2022-06-14 16:05:11.377726
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE()
    eitbIE.ie_key

# Generated at 2022-06-14 16:05:12.210481
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE() != None

# Generated at 2022-06-14 16:05:40.409144
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie.IE_DESC == 'eitb.tv online videos'
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:42.187877
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Will create the class
    EitbIE()

# Generated at 2022-06-14 16:05:44.576321
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:05:49.920472
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    

# Generated at 2022-06-14 16:05:51.059198
# Unit test for constructor of class EitbIE
def test_EitbIE():
    info_extractor = EitbIE()

# Generated at 2022-06-14 16:05:52.927804
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # pass
    assert isinstance(EitbIE(), EitbIE)


# Generated at 2022-06-14 16:06:02.424519
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print("\n######################################## test_EitbIE() #######################################")
    # Test with the url of the _TEST dict of the EitbIE class
    testurl = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    print("Testing constructor of class EitbIE\n")
    ie = EitbIE()
    # Testing the pre-defined _VALID_URL format regex of the class
    print("Testing with pre-defined format regex")
    print("URL: %s" % testurl)
    print("Valid URL? : %r" % ie._matches_regex(ie._VALID_URL, testurl))

# Generated at 2022-06-14 16:06:04.485197
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert_true(isinstance(ie, InfoExtractor))

# Generated at 2022-06-14 16:06:11.683381
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    eitb_ie = EitbIE(url)
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:16.018029
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Dummy instance of class EitbIE
    eitb = EitbIE()
    if eitb is None:
        raise Exception('Failed to create EitbIE instance')
    if str(type(eitb)) != "<class 'youtube_dl.extractor.eitb.EitbIE'>":
        raise Exception('Incorrect type of EitbIE instance')
    return True

# Generated at 2022-06-14 16:07:15.990105
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie = EitbIE("http://www.eitb.tv/eu/bideoa/kultura/lagunaren-aurkakoa/5478834765001/")
    eitbie._real_extract("http://www.eitb.tv/eu/bideoa/kultura/lagunaren-aurkakoa/5478834765001/")

# Generated at 2022-06-14 16:07:16.770973
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE == EitbIE

# Generated at 2022-06-14 16:07:27.284775
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'https://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    info = EitbIE._real_extract(EitbIE(), url)
    assert info['id'] == '4090227752001'
    assert info['title'] == '60 minutos (Lasa y Zabala, 30 años)'
    assert info['description'] == 'Programa de reportajes de actualidad.'
    # some values of info:
    # ['id', 'ext', 'title', 'description', 'duration', 'timestamp', 'upload_date', 'tags', 'thumbnail', 'formats']
    # id -> '4090227

# Generated at 2022-06-14 16:07:28.790482
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        e = EitbIE()
        assert True
    except:
        assert False

# Generated at 2022-06-14 16:07:39.924004
# Unit test for constructor of class EitbIE
def test_EitbIE():
    import re
    #import pdb; pdb.set_trace()
    assert re.match(
        EitbIE._VALID_URL,
        'http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/',
    )

    assert EitbIE._TEST.get("url") == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

# Generated at 2022-06-14 16:07:46.353559
# Unit test for constructor of class EitbIE
def test_EitbIE():
    s = EitbIE(None)
    a = s._VALID_URL
    assert len(s._TEST) > 0
    for i in s._TEST:
        assert i in s._TEST[i]
        print("URL: "+s._TEST[i]['url'])
        print("MD5: "+s._TEST[i]['md5'])
        print("ID: "+s._TEST[i]['info_dict']['id'])
        print("Title: "+s._TEST[i]['info_dict']['title'])
        print("Description: "+s._TEST[i]['info_dict']['description'])
        print("Duration: "+str(s._TEST[i]['info_dict']['duration']))

# Generated at 2022-06-14 16:07:54.044449
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Unit test that returns an EitbIE instance"""
    video_url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    video_id = '4090227752001'
    ie_eitb = EitbIE('')
    assert ie_eitb._match_id(video_url) == video_id

# Generated at 2022-06-14 16:07:55.772348
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE()
    assert instance.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:07:58.696007
# Unit test for constructor of class EitbIE
def test_EitbIE():
    extractor = EitbIE()
    assert extractor._VALID_URL == '.*eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/\d+'

# Generated at 2022-06-14 16:07:59.870977
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == EitbIE._VALID_URL

# Generated at 2022-06-14 16:10:43.416509
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:10:46.659904
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        a = EitbIE(None, None)
        assert(False)
    except AssertionError:
        assert(True)

# Generated at 2022-06-14 16:10:50.905163
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:10:52.475995
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Test constructor of class EitbIE
    """
    EitbIE()

# Generated at 2022-06-14 16:10:55.693859
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:10:56.208113
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:10:56.972888
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE != None

# Generated at 2022-06-14 16:10:58.307443
# Unit test for constructor of class EitbIE
def test_EitbIE():
        info_extractor = EitbIE()
        assert 'Eitb' == info_extractor.IE_NAME

# Generated at 2022-06-14 16:11:00.324678
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Given a class EitbIE
    ie = EitbIE()

    # When I instantiate it
    # Then I obtain an object of class EitbIE
    assert isinstance(ie, EitbIE)

# Generated at 2022-06-14 16:11:09.885739
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie is not None
    assert ie.SUBTITLE_LANGS == ['eu', 'es']
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'