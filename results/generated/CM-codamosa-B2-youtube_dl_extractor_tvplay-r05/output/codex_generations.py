

# Generated at 2026-11-03 02:38:07.571540
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Basic attribute checks
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie._VALID_URL is not None

    # URLs that should match
    suitable_urls = [
        'mtg:418113',
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true',
        'http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true',
        'http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true',
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true',
        'http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true',
        'http://www.tv8play.se/program/antikjakten/282756?autostart=true',
        'http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true',
        'http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true',
        'http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true',
        'http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true',
        'https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true',
        'http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true',
        'https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true',
        'http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true',
        'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869',
        'http://www.viafree.no/programmer/underholdning/i-like-radio-live/sesong-1/676869',
        'http://www.viafree.dk/programmer/underholdning/i-like-radio-live/saeson-1/676869',
    ]
    for url in suitable_urls:
        assert ie.suitable(url), 'URL should match: %s' % url

    # URLs that should NOT match
    unsuitable_urls = [
        'http://www.example.com/video/418113',
        'http://www.tvplay.lv/parraides/vinas-melo-labak/',
        'mtg:',
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'http://www.tv3play.se/program/husraddarna/abc?autostart=true',
    ]
    for url in unsuitable_urls:
        assert not ie.suitable(url), 'URL should not match: %s' % url

    # ID extraction
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'
    assert ie._match_id('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869') == '676869'

# Generated at 2026-11-03 02:38:52.836451
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Constructor should instantiate without arguments
    ie = ViafreeIE()
    assert ie is not None
    assert isinstance(ie, InfoExtractor)

    # classmethod suitable() should be available on the instance's class
    assert not ViafreeIE.suitable(
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true')

    # Suitable for viafree URLs
    assert ViafreeIE.suitable(
        'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ViafreeIE.suitable(
        'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    assert ViafreeIE.suitable(
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # _match_id should extract country and path groups
    country, path = ie._match_id(
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert country == 'dk'
    assert path == 'programmer/reality/paradise-hotel/saeson-7/episode-5'

    country, path = ie._match_id(
        'https://viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')
    assert country == 'se'
    assert path == 'program/livsstil/husraddarna/sasong-2/avsnitt-2'

# Generated at 2026-11-03 02:39:27.803263
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie is not None
    assert isinstance(ie, TVPlayIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie._VALID_URL is not None
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('mtg:418113')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true')
    assert not ie.suitable('http://www.example.com/video/123')
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'
    assert ie._match_id('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869') == '676869'

# Generated at 2026-11-03 02:44:49.592115
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor should succeed and expose basic attributes
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.GEO_IP_COUNTRIES is None or True
    assert ie._VALID_URL is not None

    # _VALID_URL regex should be a valid compiled pattern
    assert ie._match_valid_url('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') is not None
    assert ie._match_valid_url('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') is not None
    assert ie._match_valid_url('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true') is not None
    assert ie._match_valid_url('http://www.tv3play.se/program/husraddarna/395385?autostart=true') is not None
    assert ie._match_valid_url('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true') is not None
    assert ie._match_valid_url('http://www.tv8play.se/program/antikjakten/282756?autostart=true') is not None
    assert ie._match_valid_url('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true') is not None
    assert ie._match_valid_url('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true') is not None
    assert ie._match_valid_url('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true') is not None
    assert ie._match_valid_url('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true') is not None
    assert ie._match_valid_url('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') is not None
    assert ie._match_valid_url('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true') is not None
    assert ie._match_valid_url('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true') is not None
    assert ie._match_valid_url('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true') is not None
    assert ie._match_valid_url('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869') is not None
    assert ie._match_valid_url('mtg:418113') is not None

    # Non-matching URLs should be rejected
    assert ie._match_valid_url('http://www.example.com/video/123') is None
    assert ie._match_valid_url('http://www.tvplay.lv/parraides/') is None

    # _match_id should extract the numeric video id
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869') == '676869'

# Generated at 2026-11-03 02:47:13.468092
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    '''
    Test the constructor of class TVPlayHomeIE and its basic behavior.
    '''
    # Construct an instance of TVPlayHomeIE
    ie = TVPlayHomeIE()

    # The extractor should be an instance of InfoExtractor
    from __init__ import InfoExtractor
    assert isinstance(ie, InfoExtractor)

    # Check the class-level attributes set on the class
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TESTS')
    assert isinstance(ie._TESTS, list)

    # suitable() should accept valid URLs from the test suite
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert ie.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')

    # suitable() should reject URLs not matching _VALID_URL
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('mtg:418113')

    # _match_id should extract the trailing numeric id
    assert ie._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert ie._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'
    assert ie._match_id('https://tv3play.skaties.lv/vinas-melo-labak-10280317') == '10280317'