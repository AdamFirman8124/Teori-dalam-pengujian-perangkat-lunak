

# Generated at 2022-06-14 17:27:26.325440
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    lv = TVPlayHomeIE({})
    assert lv.IE_NAME == 'TVPlayHome'
    assert lv.IE_DESC == 'TVPlayHome'
    assert lv._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'


# Generated at 2022-06-14 17:27:29.012117
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE(None)._VALID_URL == TVPlayIE._VALID_URL



# Generated at 2022-06-14 17:27:36.446416
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert ViafreeIE("http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1", None)._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?
                        viafree\.(?P<country>dk|no|se)
                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
                    '''

# Generated at 2022-06-14 17:27:41.633429
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE('www.viafree.no')
    assert viafree.country == 'no'
    viafree = ViafreeIE('www.viafree.se')
    assert viafree.country == 'se'
    viafree = ViafreeIE('www.viafree.dk')
    assert viafree.country == 'dk'

# Generated at 2022-06-14 17:27:53.150709
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree_se = ViafreeIE(
        downloader=None,
        download_webpage_handle=None,
        _GEO_COUNTRIES=None,
        _GEO_BYPASS=None,
        _GEO_BYPASS_RULES=None,
        _GEO_BYPASS_COUNTRIES=None,
        _GEO_COUNTRY=None,
        url='http://www.viafree.se/programmer/dokumentar/all-inclusive/sasong-1/avsnitt-1'
    )
    assert viafree_se._GEO_BYPASS is False
    assert viafree_se._GEO_COUNTRY == 'se'


# Generated at 2022-06-14 17:28:02.283355
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE._ALLOW_WEBVTT = True
    url_parts = urlparse(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    ie = TVPlayHomeIE(url_parts)
    assert ie.country == 'lt'
    assert ie.format_id == '10047125'
    assert ie.view_count() is None
    ie = TVPlayHomeIE(url_parts, view_count=100)
    assert ie.view_count() == 100
    assert str(ie) == '<TVPlayHomeIE: view_count=100>'
    ie = TVPlayHomeIE(url_parts, view_count=None)
    assert ie.view_count() is None

# Generated at 2022-06-14 17:28:03.975526
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    IE = TVPlayIE()
    assert isinstance(IE, TVPlayIE)

# Generated at 2022-06-14 17:28:06.576959
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    tvplayhome_ie = TVPlayHomeIE()
    tvplayhome_ie.suitable(TVPlayHomeIE._VALID_URL)

# Generated at 2022-06-14 17:28:15.645523
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')

# Generated at 2022-06-14 17:28:19.039504
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    IE = TVPlayIE('test')
    assert IE.IE_NAME == 'mtg'
    assert IE.IE_DESC == 'MTG services'


# Generated at 2022-06-14 17:29:01.485101
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # first, test some values in _TOKENIZER_MAP_COMMON
    tokenizer_map_common = {
        'rule': r'(?:play\.novatv\.bg|play\.nova\.bg|tvplay\.skaties\.lv)/(?:[^/]+/)+',
        'token': '<k>',
        'replacement': '<k>',
    }

    if tokenizer_map_common['rule'] != TVPlayIE._TOKENIZER_MAP_COMMON[0]['rule']:
        # These should be equal
        raise AssertionError('_TOKENIZER_MAP_COMMON contains wrong rule')
    if tokenizer_map_common['token'] != TVPlayIE._TOKENIZER_MAP_COMMON[0]['token']:
        # These should be equal
        raise Ass

# Generated at 2022-06-14 17:29:15.092355
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Create an instance of TVPlayIE
    tvplay = TVPlayIE()
    # Test if the instance has been created correctly
    assert isinstance(tvplay, TVPlayIE)
    # Test if the _VALID_URL attribute of object tvplay is the same as its expected value

# Generated at 2022-06-14 17:29:17.509092
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    construct1 = TVPlayIE()
    construct2 = TVPlayIE()

    assert construct1 == construct2

# Generated at 2022-06-14 17:29:24.666717
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """
    Test of factory for class TVPlayHomeIE
    """
    assert isinstance(
        TVPlayHomeIE.suitable(
            'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'),
        compat_bool) is True
    assert isinstance(
        TVPlayHomeIE.suitable(
            'https://tv3play.skaties.lv/vinas-melo-labak-10280317'),
        compat_bool) is True
    assert isinstance(
        TVPlayHomeIE.suitable(
            'https://play.tv3.lt/aferistai-10047125'),
        compat_bool) is True

# Generated at 2022-06-14 17:29:32.460298
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME == "mtg"
    assert ie.IE_DESC == "MTG services"

# Generated at 2022-06-14 17:29:42.367862
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    tester = ViafreeIE()

    # set up some dummy values for testing the constructor
    max_width = 1920
    max_height = 1080
    language = 'en'
    country = 'us'

    # invoke the constructor
    video = tester.make_video(max_width=max_width, max_height=max_height, language=language, country=country)

    # make sure all the values returned by the constructor are the same as the values passed
    assert(video.max_width == max_width)
    assert(video.max_height == max_height)
    assert(video.language == language)
    assert(video.country == country)

# Generated at 2022-06-14 17:29:45.890535
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Confirm that TVPlayIE can't handle 'https://tvplay.tv3.lv/vinas-melo-labak-10280317'
    assert not TVPlayIE.suitable('https://tvplay.tv3.lv/vinas-melo-labak-10280317')

# Generated at 2022-06-14 17:29:51.983726
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    test_cases = [
        (TVPlayHomeIE('http://tv3play.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/'), 'tv3play.tv3.ee'),
        (TVPlayHomeIE('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354'), 'tv3play.tv3.ee'),
        (TVPlayHomeIE('https://tv3play.skaties.lv/vinas-melo-labak-10280317'), 'tv3play.skaties.lv'),
    ]

    for (inst, expected_netloc) in test_cases:
        assert inst._NETLOC == expected_netloc

# Generated at 2022-06-14 17:29:52.926313
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # NOTE: Disabled in IeTestProviderTestsMixin
    return []

# Generated at 2022-06-14 17:30:01.778801
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    ie.extract("http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true")
    ie.extract("http://www.tv3play.se/program/husraddarna/395385?autostart=true")
    ie.extract("http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true")
    ie.extract("http://www.tv8play.se/program/antikjakten/282756?autostart=true")
    ie.extract("http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true")
    ie.ext

# Generated at 2022-06-14 17:30:41.400309
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        ViafreeIE('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
        assert True
    except ValueError:
        assert False


# Generated at 2022-06-14 17:30:45.177471
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Type is the first parameter of constructor of class InfoExtractor
    assert ViafreeIE.suitable('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    assert not ViafreeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true')


# Generated at 2022-06-14 17:30:54.493625
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplayIE = TVPlayIE()
    test_url_1 = "http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true"
    video_id = tvplayIE._match_id(test_url_1)
    streams = tvplayIE._download_json(
        "http://playapi.mtgx.tv/v3/videos/stream/%s" % video_id,
        "418113", "Downloading streams JSON")

# Generated at 2022-06-14 17:30:58.164913
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    ie.suitable(url)
    ie._real_extract(url)

# Generated at 2022-06-14 17:31:02.903046
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie.IE_DESC = 'Test'
    ie.IE_NAME = 'Test'
    ie.IE_VERSION = '2017.05.10'
    assert ie.TVPlayIE.__name__ == 'TVPlayIE'


# Generated at 2022-06-14 17:31:05.860936
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    ie.extract('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')


# Generated at 2022-06-14 17:31:07.148131
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()


# Generated at 2022-06-14 17:31:08.307686
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE()



# Generated at 2022-06-14 17:31:14.646133
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    from .test import get_testcases, list_test_cases
    from .common import InfoExtractor
    testcases = list_test_cases(lambda x: x.startswith('mtg:'),
                                get_testcases())
    for (test_id, input_dict, expected_output) in testcases:
        ie = InfoExtractor()
        ie.initialize()
        ie.extract(input_dict['url'])



# Generated at 2022-06-14 17:31:26.509514
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    initial_state = {'geo_countries': [], 'geo_bypass': False}
    ie = ViafreeIE('http://www.viafree.no')
    assert ie.country == 'no'
    assert ie._GEO_COUNTRIES == ['NO']
    assert ie._GEO_BYPASS == False
    ie = ViafreeIE('http://www.viafree.se')
    assert ie.country == 'se'
    assert ie._GEO_COUNTRIES == ['SE']
    assert ie._GEO_BYPASS == False
    ie = ViafreeIE('http://www.viafree.dk')
    assert ie.country == 'dk'
    assert ie._GEO_COUNTRIES == ['DK']
    assert ie._GEO_BYPASS == False


# Generated at 2022-06-14 17:33:00.067515
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:33:01.217488
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Test for TVPlayHomeIE instance
    TVPlayHomeIE(TVPlayHomeIE.ie_key())


# Generated at 2022-06-14 17:33:02.201973
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()


# Generated at 2022-06-14 17:33:06.732486
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE('https://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')



# Generated at 2022-06-14 17:33:08.721385
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert TVPlayHomeIE._VALID_URL == ie._VALID_URL
    assert TVPlayHomeIE._TESTS == ie._TESTS
    assert TVPlayHomeIE.__name__ == ie.__name__


# Generated at 2022-06-14 17:33:09.245926
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE()

# Generated at 2022-06-14 17:33:11.299209
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE.IE_DESC != None
    assert TVPlayIE.IE_NAME != None
    assert TVPlayIE._VALID_URL != None
    assert TVPlayIE._TESTS != None


# Generated at 2022-06-14 17:33:20.074454
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """
    This test calls the constructor of class TVPlayHomeIE with URL:
    https://play.tv3.ee/cool-d-ga-mehhikosse-10044354
    """

    # Get a video ID from the URL
    video_id = TVPlayHomeIE._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')

    # Test results of constructor with URL:
    # https://play.tv3.ee/cool-d-ga-mehhikosse-10044354
    assert video_id == '10044354'

# Generated at 2022-06-14 17:33:23.481186
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    video_id = '123'
    url = 'http://example.com/' + video_id

    assert TVPlayHomeIE(
        'TVPlayHomeIE', url, tv3.TV3IE
    )._VALID_URL == TVPlayHomeIE._VALID_URL

# Generated at 2022-06-14 17:33:35.499389
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from . import TVPlayHomeIE
    from . import TVPlayIE
    from . import ViafreeIE
    from . import ViafreeBaseInfoExtractor
    from . import ViafreeBaseIE
    from . import MYTVIE
    from . import SFTVIE

    tvh = TVPlayHomeIE(TVPlayHomeIE._create_get_info())

    assert tvh.PLAYER_URL == "flash"
    assert tvh.IE_NAME == "tvplayhome"
    assert tvh._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert tvh.GEO_COUNTRIES == ['LV', 'EE']
   

# Generated at 2022-06-14 17:35:32.475206
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    inst = TVPlayHomeIE()
    assert inst._VALID_URL == TVPlayHomeIE._VALID_URL

# Generated at 2022-06-14 17:35:43.437907
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    def check(country, valid):
        viafree = ViafreeIE(country)
        assert viafree._VALID_URL == r'(?x)https?://(?:www\.)?viafree\.%s/(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)' % country
        assert viafree._GEO_COUNTRIES == [country]

# Generated at 2022-06-14 17:35:49.452724
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    _TVPlayIE = TVPlayIE()
    assert _TVPlayIE.IE_NAME == 'mtg'
    assert _TVPlayIE.IE_DESC == 'MTG services'
    assert _TVPlayIE._VALID_URL == r'(?x)m?(?:https?://[^/]+/[^/]+/|mtg:)(?P<id>\d+)'

# Generated at 2022-06-14 17:35:59.465761
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    s = TVPlayHomeIE()
    # Test common cases
    assert s._match_id("https://tvplay.tv3.lt/sounds-like-friday-night-n-7/sounds-like-friday-night-10280318/") == '10280318'
    assert s._match_id("https://play.tv3.lt/vinas-melo-labak-10280317") == '10280317'
    assert s._match_id("https://tvplay.skaties.lv/vinas-melo-labak-10280317") == '10280317'
    assert s._match_id("https://play.tv3.ee/vinas-melo-labak-10280317") == '10280317'

# Generated at 2022-06-14 17:36:02.223339
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.IE_NAME == 'TVPlayHome'
    assert ie.ie_key() == 'TVPlayHome'
    assert ie.GEO_COUNTRIES == ['LV', 'LT', 'EE']
    assert ie.VALID_URL == TVPlayHomeIE._VALID_URL
    assert ie.br.IE_NAME == 'Generic'
    assert callable(ie.extract)

# Generated at 2022-06-14 17:36:05.007287
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """Basic test cases."""
    url = 'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    video_id = '10280317'
    ie = TVPlayHomeIE(url)

    assert ie.video_id == video_id
    assert ie.url == url

# Generated at 2022-06-14 17:36:15.751518
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:36:24.117437
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    raise SkipTest("Test disabled due to https://github.com/rg3/youtube-dl/issues/14403")
    viafree_url = 'https://viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    ydl = YoutubeDL({'nocheckcertificate': True})
    viafree_ie = ydl.extract_info(viafree_url, download=False)
    assert isinstance(viafree_ie, ViafreeIE)

# Generated at 2022-06-14 17:36:27.601931
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.__name__ == 'TVPlayHome'


# Generated at 2022-06-14 17:36:30.097003
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    get_testcases_from_module(TVPlayHomeIE)
