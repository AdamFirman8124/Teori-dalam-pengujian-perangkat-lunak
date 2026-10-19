

# Generated at 2022-06-14 17:27:20.209545
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    info_extractor = TVPlayHomeIE()

# Generated at 2022-06-14 17:27:24.756506
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    ie = ViafreeIE()
    assert ie.suitable(url) is True


# Generated at 2022-06-14 17:27:31.133749
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    constructor_test(
        ViafreeIE,
        [
            {
                'url': 'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869',
            },
            {
                'url': 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2',
            },
        ]
    )


# Generated at 2022-06-14 17:27:34.742115
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    class TestTVPlayIE(TVPlayIE):
        _VALID_URL = TVPlayIE._VALID_URL
        IE_NAME = 'mtg'
        IE_DESC = 'MTG services'
    ie = TestTVPlayIE()
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'


# Generated at 2022-06-14 17:27:46.346815
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    title = 'Kādi ir īri? - Viņas melo labāk'
    video_id = '418113'
    url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    tvplay = ie._real_initialize(url)
    assert tvplay.SUFFIX == ('?autostart=true',)

# Generated at 2022-06-14 17:27:56.658013
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE("http://www.tv3play.tv3.lt/aferistai-10047125")
    assert ie.__name__ == 'TV3 Play: Aferistai'
    assert ie.IE_NAME == 'tv3play:home'
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    assert ie._TESTS[0]['info_dict']['id'] == '366367'

# Generated at 2022-06-14 17:28:10.447585
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert issubclass(ie.__class__, InfoExtractor)
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\\d+)'

# Generated at 2022-06-14 17:28:17.951872
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    r = TVPlayHomeIE._build_br_result('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert r['_type'] == 'url_transparent'
    assert r['ie_key'] == 'TVPlayHome'
    assert r['url'] == 'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/?autostart=true'



# Generated at 2022-06-14 17:28:21.493540
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('dummy')
    # Check if TVPlayHomeIE is instance of class InfoExtractor
    assert isinstance(ie, InfoExtractor)
    # Check if TVPlayHomeIE is instance of class TVPlayHomeIE
    assert isinstance(ie, TVPlayHomeIE)

# Generated at 2022-06-14 17:28:24.042623
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    viafree = ViafreeIE()
    assert viafree.suitable(url) == True



# Generated at 2022-06-14 17:28:42.739400
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Test to make sure that calling the constructor
    # of class TVPlayIE doesn't cause an exception
    TVPlayIE()

# Generated at 2022-06-14 17:28:43.323571
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE()



# Generated at 2022-06-14 17:28:46.572865
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """
    Test class constructor with parameter
    """
    x = ViafreeIE()
    assert x is not None


# Generated at 2022-06-14 17:28:48.124358
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    t = TVPlayIE(url)
    assert t.id == '418113'


# Generated at 2022-06-14 17:28:53.393543
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    tvphie = TVPlayHomeIE('http://tv3play.lt')
    assert tvphie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:28:55.056947
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')


# Generated at 2022-06-14 17:28:55.690059
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

# Generated at 2022-06-14 17:29:06.659474
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from . import TVPlayHomeIE
    seo_url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    nice_url = 'https://play.tv3.lt/aferistai-10047125'
    old_url = 'https://tv3play.tv3.lt/vinas-melo-labak-10280317'
    assert TVPlayHomeIE._is_valid_url_tvplay_home(seo_url, 'TVPlayHome')
    assert TVPlayHomeIE._is_valid_url_tvplay_home(nice_url, 'TVPlayHome')
    assert not TVPlayHomeIE._is_valid_url_tvplay_home(old_url, 'TVPlayHome')

# Generated at 2022-06-14 17:29:11.752714
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assertTVPlayHomeIE = functools.partial(assertExtractor, TVPlayHomeIE)
    assertTVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')


# Generated at 2022-06-14 17:29:18.019369
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE.suitable(
        'https://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    ) == True
    ViafreeIE.suitable(
        'https://play.tv3play.se/program/felix-och-hans-kompisar/42391?autostart=true'
    ) == False


# Generated at 2022-06-14 17:29:58.749635
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2022-06-14 17:29:59.902541
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    a = TVPlayIE()


# Generated at 2022-06-14 17:30:03.453434
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    inst = ViafreeIE(url)
    assert inst is not None


# Generated at 2022-06-14 17:30:08.869564
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert not ie.suitable(mtg.TVPlayIE()._VALID_URL)
    assert not ie.suitable(TVPlayIE._VALID_URL)
    assert ie.suitable(ViafreeIE._VALID_URL)



# Generated at 2022-06-14 17:30:11.612782
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance = TVPlayHomeIE(TVPlayHomeIE.ie_key(), TVPlayHomeIE._VALID_URL)
    instance.ie_key()
    instance._VALID_URL



# Generated at 2022-06-14 17:30:21.224161
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """Test constructor of class TVPlayHomeIE
    """
    url = "https://tv3play.skaties.lv/vinas-melo-labak-10280317"
    ie = TVPlayHomeIE()
    info = ie._call_search_ie(url, ie.ie_key(), search_title='vinas-melo-labak')
    assert ie == info['ie_info']
    assert info['url'] == 'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'

# Generated at 2022-06-14 17:30:30.996073
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    try: # Build this IE only in travis
        cls = TVPlayHomeIE
    except NameError:
        return
    assert cls.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert cls.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert cls.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert cls.suitable('https://play.tv3.lt/aferistai-10047125')

# Generated at 2022-06-14 17:30:31.619496
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE(False)


# Generated at 2022-06-14 17:30:35.718918
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert TVPlayIE.suitable('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true')
    assert not ViafreeIE.suitable('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true')

# Generated at 2022-06-14 17:30:48.313504
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """Constructor for class TVPlayIE"""
    # Note: TVPlayIE.extract() and TVPlayIE._real_extract() need internet connection
    # but we don't need all the complexity of internet connections inside our unit test
    # so we implement a "mock class" MockTVPlayIE to test the constructor
    class MockTVPlayIE:
        def __init__(self):
            self.ie_class = TVPlayIE
            self.tvplay_ie = TVPlayIE(self)
            # print(self.tvplay_ie) # uncomment this line to see the tvplay_ie contents
            self.tvplay_ie.url = 'http://mtgx.tv/v3/videos/745600492332?autostart=true'
            self.tvplay_ie.video_id = '745600492332'


# Generated at 2022-06-14 17:31:33.068357
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE({})
    assert ie.suitable('http://www.viafree.se/program/5')
    assert ie.suitable('http://www.viafree.no/programmer/5')
    assert ie.suitable('http://www.viafree.dk/programmer/5')
    assert not ie.suitable('http://www.tv3play.no/programmer/5')
    assert not ie.suitable('http://www.tv3play.se/program/5')
    assert not ie.suitable('http://www.tv3play.lt/programos/5')
    assert not ie.suitable('http://www.tv3play.lv/programmas/5')
    assert not ie.suitable('http://www.tv3play.ee/sisu/5')

# Generated at 2022-06-14 17:31:35.212961
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        ViafreeIE()
    except ValueError as e:
        assert 'VALUE_ERROR' in str(e)


# Generated at 2022-06-14 17:31:36.401428
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    youku = TVPlayIE()
    assert youku is not None



# Generated at 2022-06-14 17:31:37.550269
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    ie.constructor_test()

# Generated at 2022-06-14 17:31:43.695616
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    th = type('', (TestCase,), {'assertEqual': lambda *args: None})
    th.assertEqual(str(TVPlayHomeIE(th, 'https://tv3play.skaties.lv/vinas-melo-labak-10280317')),
                   'tv3.lv')
    th.assertEqual(str(TVPlayHomeIE(th, 'https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')),
                   'tv3.ee')
    th.assertEqual(str(TVPlayHomeIE(th, 'https://tvplay.tv3.lt/aferistai-10047125')),
                   'tv3.lt')

# Generated at 2022-06-14 17:31:46.132766
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    pass

# Generated at 2022-06-14 17:31:57.911471
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    assert ie._TESTS[1]['url'] == 'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'

# Generated at 2022-06-14 17:32:04.155738
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    viafree_ie = ViafreeIE(url)
    assert viafree_ie.suitable(url), url
    url = 'http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true'
    assert not ViafreeIE.suitable(url), url

# Generated at 2022-06-14 17:32:07.888044
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie.get_id('http://tvplay.skaties.lv/parraides/tv3-zinas/760183', 'http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')



# Generated at 2022-06-14 17:32:13.532608
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.name == 'tvplay-home'
    assert ie.brand == 'tv3-play'
    assert ie.country == 'lt'
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:33:41.931182
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie.country == 'no'
    assert ie.path == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'


# Generated at 2022-06-14 17:33:44.102870
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE(None)
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:33:54.023697
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?viafree\.(dk|no|se)/(program(?:mer)?/(?:[^/]+/)+[^/?#&]+)'
    assert ie._GEO_BYPASS == False
    assert ie.IE_DESC == 'Viafree'
    assert ie.ie_key() == 'Viafree'
    assert ie.server_url() == 'https://viafree-content.mtg-api.com'
    assert ie.ad_free() == False



# Generated at 2022-06-14 17:33:55.976735
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('TVPlay')

# Generated at 2022-06-14 17:33:57.380480
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE(None)


# Generated at 2022-06-14 17:33:59.089458
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert isinstance(ViafreeIE(), ViafreeIE)


# Generated at 2022-06-14 17:34:02.814801
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    ie.suitable('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')


# Generated at 2022-06-14 17:34:03.474086
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:34:12.482940
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    print ('Testing TVPlayIE')
    tv = TVPlayIE()
    # Test name and description
    print ('Testing name and description')
    name = tv.IE_NAME
    desc = tv.IE_DESC
    assert name == 'mtg'
    assert desc == 'MTG services'
    # Test valid url
    print ('Testing valid url')
    url = 'http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true'
    url_match = tv._VALID_URL
    valid_url = re.compile(url_match)
    match = re.match(valid_url, url)
    assert match
    # Test invalid url
    print ('Testing invalid url')

# Generated at 2022-06-14 17:34:17.918196
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    VIAFREE_URL = "https://www.viafree.dk/programmer/underholdning/7-veje-til-paradis/saeson-2/episode-12"
    viafree_ie = ViafreeIE()
    VIAFREE_VID = viafree_ie._match_id(VIAFREE_URL)
    assert VIAFREE_VID == '517045'