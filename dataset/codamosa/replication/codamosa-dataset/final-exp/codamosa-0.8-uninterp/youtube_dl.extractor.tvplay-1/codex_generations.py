

# Generated at 2022-06-14 17:27:22.118530
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """ Unit test for constructor of class ViafreeIE """

    ie = ViafreeIE(None)
    url = 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'

    assert ie.suitable(url) == True


# Generated at 2022-06-14 17:27:32.154753
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    if ie.suitable(ie.url) is False:
        raise RuntimeError('TVPlayHomeIE should be suitable with the URL')
    if ie.suitable('https://www.tv3play.no/programmer/underholdning/vinas-melo-labak/418113') is True:
        raise RuntimeError('TVPlayHomeIE should\'t be suitable with TVPlay url')
    if ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300') is True:
        raise RuntimeError('TVPlayHomeIE should\'t be suitable with TVPlay url')

# Generated at 2022-06-14 17:27:32.961313
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()


# Generated at 2022-06-14 17:27:43.921162
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Testing for correct constructor of class TVPlayIE
    tvplay_ie = TVPlayIE("tvplay_video_id")
    # Testing if the object is created properly
    assert(isinstance(tvplay_ie, TVPlayIE))
    # Testing to check if the value of _VALID_URL is same as its default value
    assert(tvplay_ie._VALID_URL == 'https?://(?:www\.)?(?:tvplay(?:\.skaties)?\.lv|(?:tv3play|play\.tv3)\.lt|tv3play\.ee|(?:tv(?:3|6|8|10)play|viafree)\.se).*')
    # Testing to check if the value of _TESTS is same as its default value
    assert(tvplay_ie._TESTS == [])


# Generated at 2022-06-14 17:27:50.889078
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    test_url = 'https://tvplay.skaties.lv/vinas-melo-labak-10280317/'
    tvplay_home_instance = TVPlayHomeIE()
    assert(tvplay_home_instance.suitable(test_url))
    assert(tvplay_home_instance._VALID_URL)
    assert(tvplay_home_instance._TESTS)


# Generated at 2022-06-14 17:27:58.711133
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie.country == 'no'
    assert ie.path == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    assert ie.url == 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    assert ie.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1') == True

# Generated at 2022-06-14 17:28:00.870920
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'TVPlay, TVPlay Premium, TV3 Play and Viasat Play'
    assert ie._VALID_URL == TVPlayHomeIE._VALID_URL

# Generated at 2022-06-14 17:28:04.174078
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():

    url_test = "/program/livsstil/husraddarna/sasong-2/avsnitt-2"
    country_test = 'se'
    path_test = "program/livsstil/husraddarna/sasong-2/avsnitt-2"

    global country
    global path
    country, path = re.match(ViafreeIE._VALID_URL, url_test).groups()
    assert country_test == country
    assert path_test == path



# Generated at 2022-06-14 17:28:07.166624
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    return type(TVPlayHomeIE)(TVPlayHomeIE.ie_key(), TVPlayHomeIE.ie_key(), TVPlayHomeIE.ie_key())



# Generated at 2022-06-14 17:28:07.823308
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    pass

# Generated at 2022-06-14 17:28:31.606459
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services' 

# Generated at 2022-06-14 17:28:33.899813
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE(compat_urllib_request.Request("http://foo.bar"))
    assert isinstance(ie, BaseIE)



# Generated at 2022-06-14 17:28:47.771473
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aseristai-n-7/aseristai-10047125')
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie._download == TVPlayHomeIE._download
    assert ie._NETRC_MACHINE == 'mtg'
    assert ie._real_initialize == TVPlayHomeIE._real_initialize
    assert ie.geo_verification_headers == TVPlayHomeIE.geo_verification_headers
    assert ie.geo_blocked_countries == TVPlayHomeIE.geo_blocked_countries


# Generated at 2022-06-14 17:28:51.296893
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'http://viafree.dk/programmer/underholdning/forsidefruer/s%C3%A6son-4/afsnit-22-8'
    tvplay = TVPlayIE()
    result = tvplay._real_initialize()
    assert(tvplay._VALID_URL == TVPlayIE._VALID_URL)
    assert(tvplay._TESTS == TVPlayIE._TESTS)
    assert(tvplay.IE_NAME == TVPlayIE.IE_NAME)
    assert(tvplay.IE_DESC == TVPlayIE.IE_DESC)

# Generated at 2022-06-14 17:28:53.562686
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    pass

# Generated at 2022-06-14 17:28:54.238540
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    pass

# Generated at 2022-06-14 17:28:57.283419
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE("https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/")
    assert ie.SUFFIX == "TV3" and ie.COUNTRY == "lt"

# Generated at 2022-06-14 17:28:58.330100
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE("TVPlayIE")
    print("Test of class TVPlayIE is finished")


# Generated at 2022-06-14 17:29:04.305370
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        ViafreeIE('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    except Exception as e:
        print('Caught exception:')
        print(e)
        assert False, 'A valid exception was caught'

# Generated at 2022-06-14 17:29:17.435571
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay_ie = TVPlayIE()
    assert tvplay_ie._VALID_URL == r'(?x)(?:mtg:|https?://(?:www\.)?(?:tvplay(?:\.skaties)?\.lv(?:/parraides)?|(?:tv3play|play\.tv3)\.lt(?:/programos)?|tv3play(?:\.tv3)?\.ee/sisu|(?:tv(?:3|6|8|10)play|viafree)\.se/program|(?:(?:tv3play|viasat4play|tv6play|viafree)\.no|(?:tv3play|viafree)\.dk)/programmer|play\.nova(?:tv)?\.bg/programi)(?:/[^/]+/)+)%s'
    # Negative test: non-matching URL


# Generated at 2022-06-14 17:30:00.260158
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()

    # checks the constructor
    ie = ydl.get_info_extractor(TVPlayIE.ie_key())
    assert(ie.__class__ == TVPlayIE)
    assert(ie._VALID_URL == TVPlayIE._VALID_URL)
    assert(ie._TESTS == TVPlayIE._TESTS)  # checks the tests
    assert(ie._downloader is not None)  # checks that the downloader is set



# Generated at 2022-06-14 17:30:01.295208
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()



# Generated at 2022-06-14 17:30:09.760063
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert(TVPlayIE.IE_NAME == 'mtg')
    assert(TVPlayIE.IE_DESC == 'MTG services')

# Generated at 2022-06-14 17:30:10.965514
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('mtg', 'MTG services')


# Generated at 2022-06-14 17:30:15.946658
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    init_test_class(ViafreeIE(TVPlayIE()))
    assert extract_info('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')


# Generated at 2022-06-14 17:30:16.950806
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME in ie.ie_key

# Generated at 2022-06-14 17:30:19.928557
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    class Test(TVPlayHomeIE):
        def _real_extract(self, url):
            pass
    t = Test({})
    assert isinstance(t, TVPlayHomeIE)

# Generated at 2022-06-14 17:30:23.906145
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """Test creation of ViafreeIE objects."""
    for url in VIAFREE_URLS:
        ViafreeIE.suitable(url)

# Generated at 2022-06-14 17:30:30.505234
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """Test the constructor method of the class ViafreeIE"""
    # url is wrong type
    with pytest.raises(TypeError):
        ViarefreeIE(1)

    # url is not a string
    with pytest.raises(ValueError):
        ViarefreeIE([])

    # url has to be non-empty string
    with pytest.raises(ValueError):
        ViarefreeIE('')

    # url should contain at least http and not ' '
    with pytest.raises(ValueError):
        ViarefreeIE(' ')

# Generated at 2022-06-14 17:30:38.418245
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    url = 'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    expected = TVPlayHomeIE(TVPlayHomeIE._create_ie())
    assert isinstance(expected, TVPlayHomeIE)
    assert expected._VALID_URL == TVPlayHomeIE._VALID_URL
    assert expected._TESTS == TVPlayHomeIE._TESTS
    assert TVPlayHomeIE.suitable(url) == True
    assert expected.suitable(url) == True
    assert expected._real_extract(url) == expected._real_extract(url)



# Generated at 2022-06-14 17:31:51.175604
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    mtg_url = 'http://www.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    video = TVPlayIE()._real_extract(mtg_url)
    assert video['title'] == 'Moterys meluoja geriau'
    assert video['episode_number'] == 47


# Generated at 2022-06-14 17:32:03.890584
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    class TestTVPlayIE(TestCase):
        def test_playlist(self):
            '''test playlist parsing'''
            playlist_id = '961805'
            playlist_url = 'http://playapi.mtgx.tv/v3/playlists/%s/videos' % playlist_id
            ie = TVPlayIE()
            ie._initialize_geo_bypass(None)
            webpage = compat_urllib_request.urlopen(playlist_url).read().decode('utf-8')
            playlist = ie._parse_json(webpage, playlist_id)
            for video in playlist:
                video_id = video['id']
                video_url = 'http://playapi.mtgx.tv/v3/videos/%s/streams' % video_id
                webpage = compat_ur

# Generated at 2022-06-14 17:32:07.324904
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE("http://tvplay.skaties.lv/parraides/tv3-zinas/760183", "418113")
    url = "http://playapi.mtgx.tv/v3/videos/418113"
    assert ie.url == url



# Generated at 2022-06-14 17:32:14.585085
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE(None)
    assert ie.extract('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == {
        'age_limit': 18,
        'description': 'Aferistai. Kalėdinė pasaka.',
        'duration': 464,
        'episode': 'Aferistai',
        'episode_number': 1,
        'id': '366367',
        'series': 'Aferistai [N-7]',
        'season': '1 sezonas',
        'season_number': 1,
        'title': 'Aferistai',
        'timestamp': 1394209658,
        'upload_date': '20140307',
    }

# Generated at 2022-06-14 17:32:17.786996
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    e = TVPlayIE('mtg:418113')
    assert e.IE_NAME == 'mtg'
    assert e.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:32:19.258204
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')

# Generated at 2022-06-14 17:32:22.040493
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie.extract('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2022-06-14 17:32:24.946445
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie.suitable(None) == False
    assert ie.suitable('https://www.tv3play.se/program/husraddarna/395385?autostart=true') == False
    assert ie.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2') == True


# Generated at 2022-06-14 17:32:35.873539
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    test_cases = [
        'https://tv3play.tv3.ee/britains-got-talent-10044343/',
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317/',
        'https://play.tv3.lt/aferistai-10047125/',
        'https://play.tv3.ee/cool-d-ga-mehhikosse-10044354/',
    ]
    ie = TVPlayHomeIE()
    for test_case in test_cases:
        ie.suitable(test_case)
        assert ie.suitable(test_case) is True, test_case



# Generated at 2022-06-14 17:32:36.843819
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE()


# Generated at 2022-06-14 17:35:38.991501
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE("mtg", "sv")
    assert viafree is not None, "Could not create instance of class ViafreeIE"



# Generated at 2022-06-14 17:35:41.015207
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE()._VALID_URL == TVPlayIE._VALID_URL



# Generated at 2022-06-14 17:35:42.526903
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """
    Run unit test for constructor of class ViafreeIE
    """
    viafreeIE = ViafreeIE()
    assert 'ViafreeIE' == viafreeIE.ie_key()



# Generated at 2022-06-14 17:35:47.671735
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from .common import fake_urlopen
    ie = ViafreeIE(fake_urlopen)
    assert ie.geo_verification_headers()
    assert ie._VALID_URL
    assert ie._TESTS
    assert ie._GEO_BYPASS
    assert ie.geo_bypass_region()
    assert ie.suitable(ie.IE_NAME + ':http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')

# Generated at 2022-06-14 17:35:56.655528
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Test with regular url
    url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    tvplay_home = TVPlayHomeIE(url)
    assert tvplay_home.short_name() == 'TVPlayHomeIE'
    assert tvplay_home.extract(url) == '366367'

    # Test with url without url suffix
    url = 'https://tvplay.tv3.lt/aferistai-10047125'
    tvplay_home = TVPlayHomeIE(url)
    assert tvplay_home.short_name() == 'TVPlayHomeIE'
    assert tvplay_home.extract(url) == '366367'

    # Test with short url

# Generated at 2022-06-14 17:35:58.103470
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert isinstance(ViafreeIE(), TVPlayIE)

# Generated at 2022-06-14 17:36:04.711436
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    InfoExtractor(ViafreeIE.ie_key())._downloader.cache.remove('https://viafree-content.mtg-api.com/viafree-content/v1/se/path/programmer/underhallning/det-beste-vorspielet/sesong-2/episode-1')

# Generated at 2022-06-14 17:36:05.798177
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    return TVPlayHomeIE().suitable(TVPlayHomeIE._VALID_URL)

# Generated at 2022-06-14 17:36:13.307280
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    test_func(ViafreeIE)
    # Tests for `_VALID_URL` and `suitable`
    test_urlinfo_common(ViafreeIE, [
        # Invalid URL
        (r'http://www.tv6play.se/program/husraddarna/395385', {
            'invalid_json': True
        }),
        # Invalid URL
        (r'https://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1', {
            'invalid_json': True
        }),
        # Invalid URL
        (r'https://play.tv3play.no/programmer/anna-anka-soker-assistent/230898', {
            'invalid_json': True
        }),
    ])

# Generated at 2022-06-14 17:36:20.807574
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')._real_extract('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie['title'] == 'Det beste vorspielet - Sesong 2 - Episode 1'
    assert ie['id'] == '757786'
    assert ie['duration'] == 1116
