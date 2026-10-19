

# Generated at 2022-06-14 16:03:14.284338
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    eitbie = EitbIE()
    v1 = EitbIE._VALID_URL # global variable
    v2 = eitbie._VALID_URL # class variable
    v3 = EitbIE._TEST # global variable
    v4 = eitbie._TEST # class variable
    # check valid urls
    assert v1 == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:20.305864
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()

    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    eid = "4090227752001"
    info = ie._real_extract(url)
    assert(info['id'] == eid)

# Generated at 2022-06-14 16:03:21.975147
# Unit test for constructor of class EitbIE
def test_EitbIE():
	eitbIE = EitbIE()

# Generated at 2022-06-14 16:03:26.662371
# Unit test for constructor of class EitbIE
def test_EitbIE():
	test = EitbIE()
	assert test._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
	assert test.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:03:29.899902
# Unit test for constructor of class EitbIE
def test_EitbIE():
    '''
    Constructor test
    '''
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:03:39.368991
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    expected = {'id': '4090227752001',
                'ext': 'mp4',
                'title': '60 minutos (Lasa y Zabala, 30 años)',
                'description': 'Programa de reportajes de actualidad.',
                'duration': 3996.76,
                'timestamp': 1381789200,
                'upload_date': '20131014',
                'tags': list,
                'thumbnail': 'http://media.eitb.eus/multimedia/2013/10/01/60_minutos_1310_3_20131010140858_640x360.jpg',
                }

# Generated at 2022-06-14 16:03:44.491540
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
    assert(ie.url == "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
    assert(ie.ie_key() == "eitb.tv")
    assert(ie.video_id == "4090227752001")
    assert(ie.ie_name() == "Eitb")


# Generated at 2022-06-14 16:03:51.567361
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/eu/bideoa/contigo-al-100/4184703010001/')
    assert ie.protocol == 'http:'
    assert ie.host == 'www.eitb.tv'
    assert ie.video_id == '4184703010001'
    assert ie.url == 'http://www.eitb.tv/eu/bideoa/contigo-al-100/4184703010001/'



# Generated at 2022-06-14 16:03:53.150012
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:04:04.080781
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Testing EitbIE
    assert EitbIE._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:21.174465
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert instance.ie_key() == 'Eitb'
    assert instance.ie_name() == 'eitb.tv'
    assert instance._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:25.510051
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:04:27.729879
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()._download_webpage(url="http://www.eitb.tv/", data=None, headers=None, query={})

# Generated at 2022-06-14 16:04:28.844623
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(None)

# Generated at 2022-06-14 16:04:31.060556
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert isinstance(eitb, EitbIE)

# Generated at 2022-06-14 16:04:33.024482
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb.tv=EitbIE()
    print(eitb.tv._VALID_URL)

# Generated at 2022-06-14 16:04:33.971605
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()

# Generated at 2022-06-14 16:04:34.550218
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:04:35.767312
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert str(ie) == 'EitbIE'

# Generated at 2022-06-14 16:04:36.350479
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:04:53.409084
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:04:54.673740
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE()
    assert eitbIE

# Generated at 2022-06-14 16:05:06.607861
# Unit test for constructor of class EitbIE
def test_EitbIE():
	import unittest

# Generated at 2022-06-14 16:05:09.435632
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # EitbIE object instance
    eitbie = EitbIE()

    # The video id is extracted correctly
    assert eitbie._match_id(EitbIE._TEST['url']) == EitbIE._TEST['info_dict']['id']

# Generated at 2022-06-14 16:05:10.713126
# Unit test for constructor of class EitbIE
def test_EitbIE():
	i= EitbIE()

# Generated at 2022-06-14 16:05:11.210422
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:05:20.772664
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:05:32.158684
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.SUBTITLE_FORMATS == ['srt', 'sbv', 'vtt']
    assert ie.IE_NAME == 'eitb.tv'
    assert ie.ITEMS_TO_SKIP == ['_live']

# Generated at 2022-06-14 16:05:32.777370
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:05:35.915263
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/eu/bideoa/goazen/20130815/elizaren-arropak-ondoz-ondoko-kaioak-goazen/'
    EitbIE(url)

# Generated at 2022-06-14 16:06:09.306926
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Sample address
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert EitbIE._match_id(EitbIE._VALID_URL, url) == '4090227752001'

# Generated at 2022-06-14 16:06:15.393211
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # url = 'http://www.eitb.tv/eu/bideoa/60-minutos/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    url = 'http://www.eitb.tv/eu/bideoa/60-minutos/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    eitb = EitbIE()
    assert eitb._match_id(url) == '4090227752001'

# Generated at 2022-06-14 16:06:17.931232
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    EitbIE(url)

# Generated at 2022-06-14 16:06:28.049996
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE()
    assert instance.IE_NAME == 'eitb.tv'
    assert instance._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    # test _real_extract
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    video_id = '4090227752001'

# Generated at 2022-06-14 16:06:38.831631
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Assert that constructor of class EitbIE initializes its internal 
    variables correctly.
    """
    # Dummy url to pass in
    url = 'https://www.eitb.tv/eu/bideoa/frankie-fish-et-les-aventuriers-de-la-mer-xixoa/4520/2557817/'

    # Create an instance of class EitbIE
    e = EitbIE(url)

    # Assert that instance variable _VALID_URL was extracted correctly
    # from given url.
    assert e._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert e.IE_

# Generated at 2022-06-14 16:06:44.240530
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj = EitbIE()
    assert obj.ie_key() == 'eitb.tv'
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert obj.match_url(url) == '4090227752001'
    assert obj.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:06:48.730807
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
# Testing object constructor
test_EitbIE()


# Generated at 2022-06-14 16:06:49.794234
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:06:51.736631
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:06:54.243522
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        dl = EitbIE()
    except Exception as exception:
        if str(exception) != 'Module "ffmpeg" has to be installed':
            raise exception

# Generated at 2022-06-14 16:08:13.973158
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    video_id = ie._match_id(url)
    video = ie._download_json(
        'http://mam.eitb.eus/mam/REST/ServiceMultiweb/Video/MULTIWEBTV/%s/' % video_id,
        video_id, 'Downloading video JSON')

    media = video['web_media'][0]

    formats = []
    for rendition in media['RENDITIONS']:
        video_url = rendition.get('PMD_URL')

# Generated at 2022-06-14 16:08:24.524058
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie = EitbIE()
    assert(eitbie.IE_NAME == 'eitb.tv')
    assert(eitbie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')
    test = eitbie._TEST
    assert(test['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert(test['md5'] == 'edf4436247185adee3ea18ce64c47998')

# Generated at 2022-06-14 16:08:25.343735
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Class EitbIE has no constructor
    return

# Generated at 2022-06-14 16:08:32.484944
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE()
    assert IE.IE_NAME == 'eitb.tv'
    assert IE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert IE._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert IE._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2022-06-14 16:08:36.496617
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = EitbIE._TEST['url']
    ie = EitbIE({})
    extracted = ie.extract({'url': url})
    assert extracted.keys() == EitbIE._TEST['info_dict'].keys()

# Generated at 2022-06-14 16:08:38.131235
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        a = EitbIE()
    except:
        a = None
    assert a is not None

# Generated at 2022-06-14 16:08:43.561923
# Unit test for constructor of class EitbIE
def test_EitbIE():
    extractor = EitbIE()
    assert extractor.IE_NAME == "eitb.tv"
    assert extractor._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:08:45.360815
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:51.237353
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = "http://www.eitb.tv/eu/bideoa/partidu-politikoak/5/471935/"
    ie = EitbIE(url)
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:08:52.107394
# Unit test for constructor of class EitbIE
def test_EitbIE():
    pass

# Generated at 2022-06-14 16:11:47.528860
# Unit test for constructor of class EitbIE
def test_EitbIE():
    with open("tests/testdata/EitbIE1.html") as test:
        data = test.read()
    with open("tests/testdata/EitbIE2.html") as test:
        data2 = test.read()
    with open("tests/testdata/EitbIE3.html") as test:
        data3 = test.read()
    with open("tests/testdata/EitbIE4.html") as test:
        data4 = test.read()
    with open("tests/testdata/EitbIE5.html") as test:
        data5 = test.read()
    with open("tests/testdata/EitbIE6.html") as test:
        data6 = test.read()

# Generated at 2022-06-14 16:11:49.413939
# Unit test for constructor of class EitbIE
def test_EitbIE():
    '''
    This is a test for the class EitbIE.
    '''
    # Test import
    from ..utils import EitbIE

    assert EitbIE



# Generated at 2022-06-14 16:11:51.531612
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE()

    assert( eitbIE.IE_NAME == 'eitb.tv')

# Generated at 2022-06-14 16:11:52.527330
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test constructor of class EitbIE"""
    EitbIE()

# Generated at 2022-06-14 16:11:54.783829
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        EitbIE()
    except:
        return False
    return True

# Generated at 2022-06-14 16:12:04.549258
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = IE_NAME()
    assert ie.IE_NAME == 'EitbIE'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:10.023544
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:14.620058
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_video = EitbIE()
    assert eitb_video.ie_key() == 'eitb.tv'
    assert eitb_video.IE_NAME == 'eitb.tv'
    assert eitb_video.ie_key() in eitb_video.SUITABLE_BROWSER

# Generated at 2022-06-14 16:12:21.168778
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE();
    assert eitb.IE_NAME == 'eitb.tv'
    assert eitb._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:12:23.592872
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == 'eitb.tv'
    #TODO: test get_info_extractor(EitbIE._VALID_URL)