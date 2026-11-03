

# Generated at 2026-11-02 13:45:23.884357
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie is not None
    assert isinstance(ie, InfoExtractor)

    # _VALID_URL should be defined and match viafree URLs
    assert hasattr(ViafreeIE, '_VALID_URL')
    assert re.match(ViafreeIE._VALID_URL, 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1') is not None
    assert re.match(ViafreeIE._VALID_URL, 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1') is not None
    assert re.match(ViafreeIE._VALID_URL, 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5') is not None

    # suitable() must delegate to TVPlayIE for mtg/tvplay URLs and reject them
    assert not ViafreeIE.suitable('mtg:418113')
    assert not ViafreeIE.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert not ViafreeIE.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')

    # suitable() should accept genuine viafree URLs
    assert ViafreeIE.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ViafreeIE.suitable('https://viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # geo bypass flag should be configured to False
    assert ViafreeIE._GEO_BYPASS is False

    # instance-level suitable() should behave the same as the classmethod
    assert not ie.suitable('mtg:418113')
    assert ie.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')

# Generated at 2026-11-02 13:45:54.120989
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # nonce:376734e2
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert ie.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert not ie.suitable('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883')
    assert not ie.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert not ie.suitable('mtg:418113')
    assert ie._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert ie._match_id('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/') == '10280317'
    assert ie._match_id('https://play.tv3.lt/aferistai-10047125') == '10047125'
    assert ie._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'
    assert ie.geo_verification_headers() == {}
    assert ie._GEO_BYPASS is True

# Generated at 2026-11-02 13:46:42.699325
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    assert ie.suitable('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert ie.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert ie.suitable('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true')
    assert ie.suitable('http://www.tv8play.se/program/antikjakten/282756?autostart=true')
    assert ie.suitable('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true')
    assert ie.suitable('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true')
    assert ie.suitable('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true')
    assert ie.suitable('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true')
    assert ie.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert ie.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ie.suitable('mtg:418113')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869') == '676869'

# Generated at 2026-11-02 13:48:00.284989
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Instantiate the extractor via its constructor
    ie = ViafreeIE()
    assert isinstance(ie, ViafreeIE)
    assert isinstance(ie, InfoExtractor)

    # Check basic class-level behavior after construction
    assert ie.ie_key() == 'Viafree'
    assert ie._VALID_URL is not None

    # ViafreeIE must not handle URLs claimed by TVPlayIE
    assert not ViafreeIE.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')

    # ViafreeIE handles viafree URLs
    assert ViafreeIE.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')
    assert ViafreeIE.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # Non-matching URLs are rejected
    assert not ViafreeIE.suitable('http://www.example.com/program/episode-1')

# Generated at 2026-11-02 13:49:28.614143
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    '''
    Unit test for constructor of class ViafreeIE
    '''
    # Instantiation should succeed and produce a ViafreeIE instance
    ie = ViafreeIE()
    assert ie is not None
    assert isinstance(ie, ViafreeIE)

    # GEO bypass is explicitly disabled for this extractor
    assert ie._GEO_BYPASS is False

    # Valid viafree URLs should be deemed suitable
    assert ViafreeIE.suitable(
        'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ViafreeIE.suitable(
        'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    assert ViafreeIE.suitable(
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # URLs already handled by TVPlayIE must not be handled by ViafreeIE
    assert not ViafreeIE.suitable(
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert not ViafreeIE.suitable('mtg:418113')

    # Unrelated URLs should not match
    assert not ViafreeIE.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')

# Generated at 2026-11-02 13:52:00.310492
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """
    Test that ViafreeIE can be constructed and that its class-level
    configuration (suitable(), _VALID_URL, _GEO_BYPASS) behaves correctly.
    """
    # The constructor should work with a default (None) downloader
    ie = ViafreeIE()
    assert ie is not None
    assert ie._downloader is None
    assert ie._GEO_BYPASS is False

    # Also construct with a dummy downloader
    class _FakeDownloader(object):
        params = {}
    ie2 = ViafreeIE(_FakeDownloader())
    assert ie2 is not None
    assert ie2._downloader is not None

    # URLs that ViafreeIE should handle
    handled_urls = [
        'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1',
        'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1',
        'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2',
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5',
    ]
    for url in handled_urls:
        assert ViafreeIE.suitable(url), 'ViafreeIE should handle: %s' % url
        m = re.match(ViafreeIE._VALID_URL, url)
        assert m is not None
        assert m.group('country') in ('dk', 'no', 'se'), url

    # URLs that ViafreeIE must NOT handle:
    # - non-viafree hosts
    # - numeric-id viafree URLs already claimed by TVPlayIE (suitable() returns False)
    # - mtg: scheme URLs handled by TVPlayIE
    unhandled_urls = [
        'https://www.youtube.com/watch?v=BaW_jenozKc',
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true',
        'http://www.viafake.se/program/reality/some-show/sasong-1/avsnitt-1',
        'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869',
        'mtg:418113',
    ]
    for url in unhandled_urls:
        assert not ViafreeIE.suitable(url), 'ViafreeIE should NOT handle: %s' % url

# nonce:bdd4aabf

# Generated at 2026-11-02 13:54:05.683460
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Constructing the extractor without a downloader should succeed
    ie = TVPlayHomeIE()

    # It must be an InfoExtractor instance
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes should be correctly initialized
    assert TVPlayHomeIE._VALID_URL == (
        r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)'
        r'/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    )

    # IE name / key derived from the class name
    assert ie.ie_key() == 'TVPlayHome'
    assert ie.IE_NAME == 'tvplayhome'

    # suitable() should accept matching URLs and reject others
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125')
    assert TVPlayHomeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert TVPlayHomeIE.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert not TVPlayHomeIE.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert not TVPlayHomeIE.suitable('mtg:418113')

    # _match_id should extract the numeric id from matching URLs
    assert ie._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert ie._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'

    # Constructing with an explicit downloader argument should also succeed
    ie2 = TVPlayHomeIE(downloader=None)
    assert isinstance(ie2, InfoExtractor)