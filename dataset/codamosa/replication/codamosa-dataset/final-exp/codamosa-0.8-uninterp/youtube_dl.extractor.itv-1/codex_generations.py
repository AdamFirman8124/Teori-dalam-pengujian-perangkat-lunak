

# Generated at 2022-06-14 16:34:44.687107
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE()
    for attr in ['BRIGHTCOVE_URL_TEMPLATE']:
        assert getattr(instance, attr) is not None
        assert getattr(ITVBTCCIE, attr) is not None

# Generated at 2022-06-14 16:34:56.236929
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """Test for constructor of ITVBTCCIE"""
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    TEST_CLASS = ITVBTCCIE(url)
    assert TEST_CLASS.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert TEST_CLASS.IE_NAME == 'brightcove:new'
    assert TEST_CLASS.playlist_id == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:35:00.199334
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    a = ITVBTCCIE()
    assert a._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:35:04.126710
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test constructor of class ITVIE is working
    itv_test = ITVIE('itv', ITVIE._VALID_URL, ITVIE._TESTS)
    itv_test.test()


# Generated at 2022-06-14 16:35:04.800550
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE()

# Generated at 2022-06-14 16:35:17.304779
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVE = ITVIE()
    assert ITVE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ITVE._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:35:24.223873
# Unit test for constructor of class ITVIE
def test_ITVIE():
    videoIE = ITVIE()
    video_id = '2a4547a0012'
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    info_dict = {
        'id': '2a4547a0012',
        'title': 'Liar - Series 2 - Episode 6',
        'ext': 'mp4',
        'description': 'md5:d0f91536569dec79ea184f0a44cca089',
        'series': 'Liar',
        'season_number': 2,
        'episode_number': 6,
    }
    assert videoIE._VALID_URL == videoIE._VALID_URL
    assert videoIE._match_id(url) == video_id
    assert videoIE._extract_url(url) == url

# Generated at 2022-06-14 16:35:34.731071
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ITVIE._GEO_COUNTRIES == ['GB']
    assert ITVIE._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ITVIE._TESTS[0]['info_dict']['id'] == '2a4547a0012'
    assert ITVIE._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert ITVIE._TESTS[0]['info_dict']['title'] == 'Liar - Series 2 - Episode 6'
    assert ITV

# Generated at 2022-06-14 16:35:40.626408
# Unit test for constructor of class ITVIE
def test_ITVIE():
    '''
        Test the class ITVIE, which extracts videos from ITV.
    '''

    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    print("Extracting video from: " + url)

    itvie = ITVIE()
    info = itvie._real_extract(url)

    print("Video title: " + info['title'])
    print("Video description: " + info['description'])
    print("Video id: " + info['id'])
    print("Video url: " + info['formats'][0]['url'])

    assert(info['id'] == '2a4547a0012')


# Generated at 2022-06-14 16:35:42.186627
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, ITVIE)

# Generated at 2022-06-14 16:35:58.449123
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()


# Generated at 2022-06-14 16:36:02.670122
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert ie._TEST['url'] == ie.url
    assert ie._TEST['info_dict'] == ie.info_dict

# Generated at 2022-06-14 16:36:06.627187
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url= 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    itvBTCCIE = ITVBTCCIE()
    assert ITVBTCCIE._VALID_URL == itvBTCCIE._VALID_URL
    assert ITVBTCCIE._TEST == itvBTCCIE._TEST
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == itvBTCCIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:36:08.004659
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE is None

# Generated at 2022-06-14 16:36:19.641551
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert itvbtccie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert itvbtccie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:36:21.194071
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE(InfoExtractor()).test_ITVBTCCIE()


# Generated at 2022-06-14 16:36:27.939901
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Check instance is created corectly
    ie = ITVIE()
    assert ie.IE_NAME == 'itv'
    assert ie.IE_DESC == 'ITV'
    assert ie. _VALID_URL == ITVIE._VALID_URL
    assert ie._NETRC_MACHINE == 'itv'
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie._TESTS == ITVIE._TESTS
    assert ie._downloader is None

# Generated at 2022-06-14 16:36:34.602990
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE().get_title() == ""
    assert ITVIE().get_description() == ""
    assert ITVIE().get_duration() == 0
    assert ITVIE().get_thumbnail() == ""
    assert ITVIE().get_upload_date() == ""
    assert ITVIE().get_subtitles() == {}
    assert ITVIE().get_series() == ""
    assert ITVIE().get_season_number() == 0
    assert ITVIE().get_episode_number() == 0
    assert ITVIE().get_formats() == []
    assert ITVIE().get_id() == ""

# Generated at 2022-06-14 16:36:46.805705
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvie = ITVIE()
    assert itvie._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:36:50.197327
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ie = ITVBTCCIE()
    ie.download(url)
    assert len(ie.playlist) == 9

# Generated at 2022-06-14 16:37:19.835295
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = ITVBTCCIE._TEST['url']
    playlist_id = ITVBTCCIE._TEST['info_dict']['id']
    playlist_title = ITVBTCCIE._TEST['info_dict']['title']
    ie = ITVBTCCIE()
    ie.extract(ITVBTCCIE._TEST['url'])


# Generated at 2022-06-14 16:37:21.167735
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:22.442927
# Unit test for constructor of class ITVIE
def test_ITVIE():
	itv = ITVIE()
	itv.suite()

# Generated at 2022-06-14 16:37:29.631687
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE()
    assert itv.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:36.260764
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ITVBTCCIE._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:37:41.465009
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    This is a regression test for ITVBTCCIE.
    """
    constructor = ITVBTCCIE

    t = constructor("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert t

# Generated at 2022-06-14 16:37:43.190085
# Unit test for constructor of class ITVIE
def test_ITVIE():
  itvie = ITVIE()
  assert itvie._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:37:44.536024
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE(None).ie_key() == ITVIE.ie_key()

# Generated at 2022-06-14 16:37:45.096729
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:37:46.285861
# Unit test for constructor of class ITVIE
def test_ITVIE():
	itvIE = ITVIE()
	print(itvIE)

# Generated at 2022-06-14 16:38:56.250832
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # This is not the actual JSON data we get anymore, but the results becomes
    # the same
    video_id = '6195337526001'
    video_url = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=' + video_id

# Generated at 2022-06-14 16:38:58.091787
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ITVIE()._match_id(url) == '2a4547a0012'
    assert ITVIE()._real_extract(url)


# Generated at 2022-06-14 16:39:03.310546
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE(ITVEmbedIE()).BTCC_URL_TEMPLATE == ITVBTCCIE.BTCC_URL_TEMPLATE
    assert ITVBTCCIE(ITVEmbedIE()).BRIGHTCOVE_URL_TEMPLATE == ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE


# Generated at 2022-06-14 16:39:10.220451
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    ie.BRIGHTCOVE_URL_TEMPLATE = '%s'
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    r = ie.url_result(url)
    assert r == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5794910623001'

# Generated at 2022-06-14 16:39:11.437885
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE().IE_NAME == "itv:vod"

# Generated at 2022-06-14 16:39:22.946031
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:39:24.292021
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE(None, None)

# Generated at 2022-06-14 16:39:31.645413
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    test_ITVBTCCIE = ITVBTCCIE(url);
    video_url = ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % '5786239696001'
    assert test_ITVBTCCIE._real_extract(url)[0]['url'] == video_url;

# Generated at 2022-06-14 16:39:35.934332
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert ie.BRIGHTCOVE_URL_TEMPLATE == ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:39:39.826249
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE(None)
    expected_value = ITVIE._VALID_URL, ITVIE._TESTS, ITVIE._GEO_COUNTRIES
    real_value = ie._VALID_URL, ie._TESTS, ie._GEO_COUNTRIES
    assert expected_value == real_value


# Generated at 2022-06-14 16:42:01.410449
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('', '')

# Generated at 2022-06-14 16:42:03.382760
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()
    assert itv_ie != None
    assert type(itv_ie) == ITVIE


# Generated at 2022-06-14 16:42:06.202326
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_func = ITVBTCCIE()._real_extract
    test_func('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:42:08.469155
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE('https://www.itv.com/hub/liar/2a4547a0012').extract('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:42:10.290837
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    info = ITVBTCCIE()
    assert info == ITVBTCCIE('ITVBTCC', ITVBTCCIE.ie_key())

# Generated at 2022-06-14 16:42:17.080882
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    import youtube_dl
    ydl = youtube_dl.YoutubeDL({})
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    result = ydl.extract_info(url, download=False)
    assert result['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert result['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert len(result['entries']) == 9

# Generated at 2022-06-14 16:42:24.406811
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    itvbtcc_ie = ITVBTCCIE()
    assert itvbtcc_ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert itvbtcc_ie._TEST['url'] == test_url
    assert itvbtcc_ie._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:42:25.710310
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE.__name__ == "ITVIE"


# Generated at 2022-06-14 16:42:35.912785
# Unit test for constructor of class ITVIE
def test_ITVIE():
    req = ITVIE()
    assert req.geo_verification_headers() == {'X-Forwarded-For': '213.248.126.151'}
    assert req.geo_verification_headers() == {'X-Forwarded-For': '213.248.126.147'}
    assert req.geo_verification_headers() == {'X-Forwarded-For': '213.248.126.149'}
    assert req.geo_verification_headers() == {'X-Forwarded-For': '213.248.126.150'}
    assert req.geo_verification_headers() == {'X-Forwarded-For': '213.248.126.148'}

# Generated at 2022-06-14 16:42:37.841116
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE()
    assert instance._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'