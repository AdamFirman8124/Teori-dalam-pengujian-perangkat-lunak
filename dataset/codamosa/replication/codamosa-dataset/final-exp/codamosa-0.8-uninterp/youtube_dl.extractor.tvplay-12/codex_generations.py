

# Generated at 2022-06-14 17:27:18.091197
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:27:19.170279
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

# Generated at 2022-06-14 17:27:29.927543
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Arrange
    args = ['test', 'abc123']
    kwargs = {'ie': 'tvplay'}

    # Act
    tvplayIE = TVPlayIE(*args, **kwargs)

    # Assert

# Generated at 2022-06-14 17:27:43.119164
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    test_video_file = 'u_m3u8.txt'
    video_url = 'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    url = urljoin(url, video_url)
    video_id = int(video_url.split('/')[-1])
    match = re.match(ViafreeIE.V_URL, url)
    assert match, 'URL must match ViafreeIE.V_URL'
    country = match.group('country')
    path = match.group('id')

# Generated at 2022-06-14 17:27:47.842061
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay_ie = TVPlayIE("http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true")
    assert("mtg" == tvplay_ie.IE_NAME)
    assert("mtg" == tvplay_ie._VALID_URL)
# Unit test ends


# Generated at 2022-06-14 17:27:51.449371
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance = TVPlayHomeIE(None)
    assert isinstance(instance, TVPlayHomeIE)
    assert not isinstance(instance, InfoExtractor)



# Generated at 2022-06-14 17:28:02.483533
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE().IE_NAME == 'mtg'
    assert TVPlayIE().IE_DESC == 'MTG services'
    assert re.match(TVPlayIE._VALID_URL, TVPlayIE._TESTS[0]['url'])
    assert TVPlayIE._TESTS[0]['md5'] == 'a1612fe0849455423ad8718fe049be21'
    assert TVPlayIE._TESTS[0]['info_dict']['id'] == '418113'
    assert TVPlayIE._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert TVPlayIE._TESTS[0]['info_dict']['title'] == 'Kādi ir īri? - Viņas melo labāk'
    assert TV

# Generated at 2022-06-14 17:28:03.765385
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE(None)



# Generated at 2022-06-14 17:28:15.538507
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    obj = TVPlayIE()
    assert obj._VALID_URL == r'(?x)(?:mtg:|https?://(?:www\.)?(?:tvplay(?:\.skaties)?\.lv(?:/parraides)?|(?:tv3play|play\.tv3)\.lt(?:/programos)?|tv3play(?:\.tv3)?\.ee/sisu|(?:tv(?:3|6|8|10)play|viafree)\.se/program|(?:(?:tv3play|viasat4play|tv6play|viafree)\.no|(?:tv3play|viafree)\.dk)/programmer|play\.nova(?:tv)?\.bg/programi)/(?:[^/]+/)+)(?P<id>\d+)'

# Generated at 2022-06-14 17:28:17.698732
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE._build_javascript_result(
        TVPlayHomeIE._VALID_URL, TVPlayHomeIE._TESTS)

# Generated at 2022-06-14 17:28:54.918170
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Test video not available in my country
    ViafreeIE('http://www.viafree.no/programmer/underholdning/hver-gang-vi-motes/sesong-1/episode-1').raise_geo_restricted.assert_called_once_with(countries=['NO'])


# Generated at 2022-06-14 17:29:06.012450
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE('www.viafree.com', {})
    assert viafree._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?
                        viafree\.(?P<country>dk|no|se)
                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
                    '''

# Generated at 2022-06-14 17:29:12.706412
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie._TESTS # ie._TESTS is empty

# Generated at 2022-06-14 17:29:20.584879
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from .common import _PY3
    from .common import warning
    for url in ('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/',
                'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/',
                'https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/'):
        ie = TVPlayHomeIE()
        assert ie.suitable(url) is True

# Generated at 2022-06-14 17:29:29.389437
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    try:
        TVPlayIE('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    except Exception as e:
        assert 'geo_blocked' == e.code
    try:
        TVPlayIE('http://www.tv6play.se/program/husraddarna/395385?autostart=true')
    except Exception as e:
        assert 'no streams found' == e.code
    try:
        TVPlayIE('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')
    except Exception as e:
        assert 'geo_blocked' == e.code



# Generated at 2022-06-14 17:29:35.322484
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    def test_tvplay_yie(self, url, video_id, **kwargs):
        self.assertEqual(TVPlayIE(self)._match_id(url), video_id)

    test_tvplay_yie(None, 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113', '418113')
    test_tvplay_yie(None, 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true', '418113')
    test_tvplay_yie(None, 'http://play.tv3.lt/programos/vinas-melo-geriau/409229', '409229')

# Generated at 2022-06-14 17:29:39.176181
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE()


# Generated at 2022-06-14 17:29:41.002022
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from . import ViafreeIE as Class
    assert isinstance(Class.__doc__, str)



# Generated at 2022-06-14 17:29:43.873121
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    IE = ViafreeIE('https://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5');
    assert isinstance(IE, ViafreeIE);

# Generated at 2022-06-14 17:29:46.859057
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tester = TVPlayIE()
    expected_constructor = '<class \'youtube_dl.extractor.mtg.TVPlayIE\'>'
    assert repr(tester) == expected_constructor


# Generated at 2022-06-14 17:31:05.268264
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    url = 'https://play.tv3.lt/aferistai-10047125'
    tvplay_home_ie = TVPlayHomeIE(url)
    assert tvplay_home_ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert tvplay_home_ie._match_id(url) == '10047125'
    assert tvplay_home_ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert not tvplay_home_ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')


# Generated at 2022-06-14 17:31:15.729899
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from . import ViafreeIE
    assert ViafreeIE.ie_key() == 'Viafree'
    assert ViafreeIE.suitable("http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1")
    assert not ViafreeIE.suitable("http://play.novatv.bg/programi/bolen-plen/sesiqta-na-kotka/424111?autostart=true")
    assert ViafreeIE.suitable("http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5")
    assert ViafreeIE.suitable("http://tvplay.skaties.lv/parraides/tv3-zinas/760183?autostart=true")
   

# Generated at 2022-06-14 17:31:26.600494
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    player = {
        'url': 'http://playapi.mtgx.tv/v3/videos/stream/%s',
        'note': 'Test for constructor of class TVPlayIE',
        'playlist': [
            'http://www.tvplay.lv/parraides/vinas-melo-labak/418113',
            'http://playapi.mtgx.tv/v3/videos/418113',
            'http://playapi.mtgx.tv/v3/videos/stream/418113',
            {
                'url': 'http://playapi.mtgx.tv/v3/videos/stream/418113',
                'only_matching': True
            }
        ]
    }
    return player



# Generated at 2022-06-14 17:31:36.900593
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplayie = TVPlayIE()
    url = 'http://www.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    title = 'Moterys meluoja geriau'
    exp_id = '409229'
    exp_age_limit = 0
    age_limit = tvplayie._parse_episode_info(url, title)['age_limit']
    assert age_limit == exp_age_limit, 'age limit for %s differs from expected %s' % (title, exp_age_limit)
    exp_id_retrieved = tvplayie._parse_episode_info(url, title)['id']

# Generated at 2022-06-14 17:31:41.407129
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():

    # Test videos from mtglatvia.com and mtglithuania.com
    mtglatvia_tvplay = TVPlayHomeIE(None)
    mtglithuania_tvplay = TVPlayHomeIE(None)
    assert mtglatvia_tvplay is not None
    assert mtglatvia_tvplay._VALID_URL == TVPlayHomeIE._VALID_URL
    assert mtglithuania_tvplay is not None
    assert mtglithuania_tvplay._VALID_URL == TVPlayHomeIE._VALID_URL

# Generated at 2022-06-14 17:31:46.822477
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from youtube_dl.extractor import gen_extractors_map

    ViafreeIE.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    ViafreeIE.suitable(gen_extractors_map()['http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true'][0]._VALID_URL)
    ViafreeIE.suitable('http://tv.tv3.ee/sisu/kodu-keset-linna/238551')

# Generated at 2022-06-14 17:31:48.240743
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE().IE_NAME == 'mtg'



# Generated at 2022-06-14 17:32:00.331987
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE('test123', 'http://test.com/test.html')

# Generated at 2022-06-14 17:32:01.459076
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()


# Generated at 2022-06-14 17:32:08.005782
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    m = TVPlayHomeIE()
    assert m.get_video_info(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') is not None



# Generated at 2022-06-14 17:35:03.711349
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()


# Generated at 2022-06-14 17:35:12.959605
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    IE = TVPlayHomeIE()
    assert IE.ie_key() == 'TVPlayHome'
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125')
    assert TVPlayHomeIE.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert TVPlayHomeIE.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')


# Generated at 2022-06-14 17:35:16.493324
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Test 1
    video_url = 'http://www.tv3play.lv/parraides/vinas-melo-labak/418113?autostart=true'
    video_id = r'418113'
    geo_country = 'lv'

    t = TVPlayIE()
    video_id_test = t._match_id(video_url)
    assert video_id_test == video_id



# Generated at 2022-06-14 17:35:19.932338
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('ABC', 'XYZ')
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:35:22.778899
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    video_id = '10044354'
    url = TVPlayHomeIE.suitable('https://tv3play.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-' + video_id + '/')
    if url:
        url = TVPlayHomeIE.ie_key() + ':'
        url += video_id

# Generated at 2022-06-14 17:35:29.888858
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    info_extractor = TVPlayHomeIE()
    assert info_extractor._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:35:31.257918
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Contructor for ViafreeIE should not throw any exception
    ViafreeIE('http://some.url')
    assert True


# Generated at 2022-06-14 17:35:38.231996
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    test_url = 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    instance = ViafreeIE(test_url)
    assert instance.format_id == 'sasong-1'
    assert instance.country == 'se'



# Generated at 2022-06-14 17:35:49.203939
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    test_TVPlayIE = TVPlayIE()

# Generated at 2022-06-14 17:35:59.161483
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak-10280317/')
    assert ie.name == 'TVPlayHome'
    assert ie.country == 'LV'
    assert ie.age_limit == 18
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'