

# Generated at 2022-06-14 17:27:21.460980
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true'
    ie = TVPlayIE()
    result = ie.extract(url)
    assert result["id"] == "238551"


# Generated at 2022-06-14 17:27:23.721569
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie.__init__()


# Generated at 2022-06-14 17:27:33.098593
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    tvph = TVPlayHomeIE()
    assert tvph._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert tvph._TESTS[0]['url'] == 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    assert tvph._TESTS[0]['info_dict']['id'] == '366367'
    assert tvph._TESTS[0]['info_dict']['title'] == 'Aferistai'

# Generated at 2022-06-14 17:27:40.940165
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    for url in ('https://tvplay.tv3.lt/aferistai/aferistai-10047125', 'https://tv3play.tv3.lv/aferistai-10047125', 'https://tvplay.tv3.ee/aferistai-10047125', 'https://play.tv3.lt/aferistai-10047125', 'https://tv3play.tv3.lv/aferistai-10047125'):
        assert TVPlayHomeIE.suitable(url)

# Generated at 2022-06-14 17:27:43.098034
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert str(ViafreeIE) == '<class \'__main__.ViafreeIE\'>'

# Generated at 2022-06-14 17:27:54.719814
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """Test class TVPlayHomeIE"""
    url = 'https://play.tv3.ee/cool-d-ga-mehhikosse-10044354'
    test_video_id = '10044354'
    test_url = 'https://play.tv3.ee/cool-d-ga-mehhikosse-10044354/'
    tvplay_test = TVPlayHomeIE(TVPlayHomeIE._create_get_url_regex(url))
    assert tvplay_test._VALID_URL == TVPlayHomeIE._VALID_URL
    assert tvplay_test._match_id(url) == test_video_id
    assert tvplay_test._match_id(test_url) == test_video_id
    assert tvplay_test._match_id(test_video_id) == test_video

# Generated at 2022-06-14 17:27:56.157091
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert(TVPlayHomeIE()._VALID_URL == TVPlayHomeIE._VALID_URL)


# Generated at 2022-06-14 17:28:00.735756
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, ViafreeBaseIE)



# Generated at 2022-06-14 17:28:12.463639
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from io import BytesIO
    from .nogenie import NoGenericIE
    from .common import InfoExtractor
    from .nogenie import update_url_query
    from .common import ExtractorError
    from .nogenie import try_get
    from .nogenie import qualities
    from .nogenie import determine_ext
    from .nogenie import compat_urlparse
    from .nogenie import compat_HTTPError
    from .common import parse_iso8601
    from .common import int_or_none
    from .common import url_or_none

    def test_init(self):
        try:
            from .common import InfoExtractor
        except:
            self.fail("Failed to import InfoExtractor")

# Generated at 2022-06-14 17:28:17.353526
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE(None)
    assert ie.suitable('http://tv3play.skaties.lv/vinas-melo-labak-10280317') is True
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317') is True
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak-10280317') is True
    assert ie.suitable('https://play.tv3play.skaties.lv/vinas-melo-labak-10280317') is True
    assert ie.suitable('https://play.tv3.lv/vinas-melo-labak-10280317') is True

# Generated at 2022-06-14 17:28:39.383305
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Test if the length of class variables is same
    assert len(ViafreeIE._TESTS) == len(TVPlayIE._TESTS)

# Generated at 2022-06-14 17:28:42.494636
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    mtg = ViafreeIE()
    assert isinstance(mtg, InfoExtractor)
    assert mtg.ie_key() == 'mtg'

# Generated at 2022-06-14 17:28:50.833681
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    ie.extract('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    ie.extract('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    ie.extract('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2')
    ie.extract('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')

# Generated at 2022-06-14 17:29:02.434641
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    tvplay_home_ie = TVPlayHomeIE('https://play.tv3.lt/aferistai-10047125')
    assert tvplay_home_ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert not tvplay_home_ie.suitable('https://www.tv3play.lt/toks-batai-10222841')
    assert not tvplay_home_ie.suitable('https://www.tv3play.lv/toks-batai-10222841')
    assert not tvplay_home_ie.suitable('https://tv3play.tv3.ee/toks-batai-10222841')

# Generated at 2022-06-14 17:29:15.602758
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    def check(name, url, *args):
        assert name == args[0].ie_key()
        assert url == args[1].url
    tvplay = lambda name, url: check(name, url, *TVPlayIE._extract_url_info(url))
    tvplay(
        'mtg', 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    tvplay(
        'mtg', 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113/')
    tvplay(
        'mtg', 'http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')

# Generated at 2022-06-14 17:29:18.455682
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    constructor_test(ViafreeIE, ['http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'])


# Generated at 2022-06-14 17:29:25.228392
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE()
    assert ViafreeIE.suitable("https://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/avsnitt-1")
    assert ViafreeIE.suitable("http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5")
    assert not ViafreeIE.suitable("http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true")
    assert not ViafreeIE.suitable("http://play.tv3play.ee/programs/animeeritud/heidi/238551?autostart=true")

# Generated at 2022-06-14 17:29:32.828529
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

# Generated at 2022-06-14 17:29:44.523178
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2022-06-14 17:29:54.526516
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

# Generated at 2022-06-14 17:30:32.948934
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    i = TVPlayIE()
    assert i.IE_NAME == 'mtg', 'Invalid IE name'

# Generated at 2022-06-14 17:30:38.709420
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?
                        viafree\.(?P<country>dk|no|se)
                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
                    '''



# Generated at 2022-06-14 17:30:43.051927
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    video = TVPlayHomeIE._build_video(
        TVPlayHomeIE._extract_url(url),
        url,
        'https://tvplay.tv3.lt/static/autoplay.json')
    assert video.id == '366367'



# Generated at 2022-06-14 17:30:47.944995
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie_test = TVPlayIE()
    # Verify that this instance of InfoExtractor implements the list of
    # requested formats of this test case.
    assert ie_test._WORKING_FORMATS == frozenset([
        'hls', 'medium', 'high'
    ])



# Generated at 2022-06-14 17:30:57.939195
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    from .test_utils import expect_extractor


# Generated at 2022-06-14 17:31:10.589698
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    meta = {
        'title': 'test_title',
        'image': 'test_image_url',
        'description': 'test_description'
    }
    program = {
        'guid': 'test_guid',
        '_links': {
            'streamLink': {
                'href': 'test_href'
            }
        },
        'episode': 'test_episode',
        'video': {
            'duration': {
                'milliseconds': 'test_milliseconds'
            }
        },
        'availability': {
            'start': 'test_start'
        }
    }
    viafree_blocks = {
        '_embedded': {
            'program': program
        }
    }

# Generated at 2022-06-14 17:31:24.418784
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    test_url = 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
    assert ViafreeIE.suitable(test_url)
    assert not ViafreeIE.suitable('http://tvplay.skaties.lv/parraides/tv3-zinas/760183')
    assert not ViafreeIE.suitable('http://tv6play.se/program/den-sista-dokusapan/266636')
    assert not ViafreeIE.suitable('http://play.tv3.lt/kodu-keset-linna/238551')
    assert not ViafreeIE.suitable('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898')

# Generated at 2022-06-14 17:31:27.716017
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    TVPlayIE(url)


# Generated at 2022-06-14 17:31:30.861692
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    key = TVPlayIE.IE_NAME
    ie = TVPlayIE()
    assert ie.ie_key() == key



# Generated at 2022-06-14 17:31:32.261882
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert str(ie) == 'TVPlayHome'

# Generated at 2022-06-14 17:33:12.765893
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'


# Generated at 2022-06-14 17:33:23.965307
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    for url in (
            'https://tvplay.tv3.lt/aferistai-10047125/',
            'https://tvplay.skaties.lv/vinas-melo-labak-10280317/',
            'https://tvplay.tv3.ee/cool-d-ga-mehhikosse-10044354/',
            'https://play.tv3.lt/aferistai-10047125',
            'https://tv3play.skaties.lv/vinas-melo-labak-10280317',
            'https://play.tv3.ee/cool-d-ga-mehhikosse-10044354'):
        ie = TVPlayHomeIE(url, {})
        assert ie._VALID_URL == TVPlayHomeIE._VALID_URL
        assert ie._

# Generated at 2022-06-14 17:33:25.821862
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from .common import test_urls
    for url, ie in test_urls(TVPlayHomeIE):
        pass

# Generated at 2022-06-14 17:33:36.886484
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('http://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert ie.get_url() == 'https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/'
    assert ie.get_id() == '10044354'
    assert ie.get_country() == 'ee'
    assert ie.get_domain() == 'tv3'
    assert ie.get_partner() == 'tv3'
    assert ie.get_query() == 'telecastId=10044354'

# Generated at 2022-06-14 17:33:38.654670
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie.extract("mtg:418113")


# Generated at 2022-06-14 17:33:48.586184
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ConstructorTest(ViafreeIE, [{
        'url': 'http://www.viafree.se/program/underhallning/det-beste-vorspielet/sesong-2/episode-1',
        'only_matching': True,
    }])
    ConstructorTest(ViafreeIE, [{
        'url': 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1',
        'only_matching': True,
    }])
    ConstructorTest(ViafreeIE, [{
        'url': 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5',
        'only_matching': True,
    }])



# Generated at 2022-06-14 17:33:54.898035
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:34:00.007410
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE(None)
    assert ie.REAL_URL is False
    assert ie.tvplayer_id is None
    with pytest.raises(RegexNotFoundError):
        ie.country
    assert ie.url is None
    assert ie.path is None



# Generated at 2022-06-14 17:34:02.662395
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert TVPlayHomeIE._VALID_URL == ie._VALID_URL
    assert TVPlayHomeIE._TESTS == ie._TESTS

# Generated at 2022-06-14 17:34:09.349228
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    vplay_ie = TVPlayHomeIE()
    assert vplay_ie.suitable('https://tvplay.tv3.lt/aferistai-10047125/')
    assert vplay_ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert vplay_ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert vplay_ie.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
