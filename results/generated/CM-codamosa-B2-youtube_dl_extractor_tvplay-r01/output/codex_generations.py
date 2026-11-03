

# Generated at 2026-11-02 12:53:32.463499
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie is not None
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert not ie.suitable('https://tvplay.tv3.lt/')
    assert TVPlayHomeIE._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert TVPlayHomeIE._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'

# Generated at 2026-11-02 12:54:29.860687
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert ie.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert not ie.suitable('https://example.com/video-123')
    assert not ie.suitable('https://play.tv3.lt/aferistai/')
    m = re.match(ie._VALID_URL, 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert m is not None
    assert m.group('id') == '10047125'

# Generated at 2026-11-02 12:55:46.581352
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from yt_dlp.extractor.tvplay import ViafreeIE
    import re

    # Constructor should succeed and set up class attributes
    ie = ViafreeIE()
    assert ie is not None
    assert ie.ie_key() == 'Viafree'
    assert ie.IE_NAME == 'viafree'
    assert ie._VALID_URL is not None
    assert ie._GEO_BYPASS is False

    # _VALID_URL should match viafree URLs across supported countries
    for country, path in [
        ('no', 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'),
        ('se', 'program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'),
        ('dk', 'programmer/reality/paradise-hotel/saeson-7/episode-5'),
    ]:
        url = 'https://www.viafree.%s/%s' % (country, path)
        m = re.match(ViafreeIE._VALID_URL, url)
        assert m is not None, 'VALID_URL failed for %s' % url
        assert m.group('country') == country
        assert m.group('id') == path

    # ViafreeIE should defer to TVPlayIE for tvplay URLs
    from yt_dlp.extractor.tvplay import TVPlayIE
    assert not ViafreeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true')
    assert ViafreeIE.suitable('https://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')

    # A fresh instance must be usable for URL matching
    assert ie.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')
    assert not ie.suitable('http://www.viafree.us/program/some/show')

    # Constructing multiple instances should be independent
    ie2 = ViafreeIE()
    assert ie2 is not ie

# Generated at 2026-11-02 12:56:57.032105
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Instance should be created successfully and be an InfoExtractor
    assert isinstance(ie, TVPlayIE)
    assert isinstance(ie, InfoExtractor)

    # Class/instance metadata
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # URL matching
    assert ie.suitable('mtg:418113')
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    assert ie.suitable('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert ie.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert ie.suitable('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true')
    assert ie.suitable('http://www.tv8play.se/program/antikjakten/282756?autostart=true')
    assert ie.suitable('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true')
    assert ie.suitable('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true')
    assert ie.suitable('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true')
    assert ie.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true')
    assert ie.suitable('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert ie.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')

    # Non-matching URLs
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/')
    assert not ie.suitable('mtg:')

    # ID extraction
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'
    assert ie._match_id('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869') == '676869'

# Generated at 2026-11-02 12:58:04.927028
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Verify instance is created and inherits from InfoExtractor
    assert isinstance(ie, TVPlayIE)
    assert isinstance(ie, InfoExtractor)

    # Verify class attributes set at definition time
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie._VALID_URL is not None

    # Verify _VALID_URL matches all expected URL forms
    valid_urls = [
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
        'http://tvplay.skaties.lv/parraides/tv3-zinas/760183',
        'http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true',
        'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869',
        'mtg:418113',
    ]
    for url in valid_urls:
        m = re.match(ie._VALID_URL, url)
        assert m is not None, 'URL should match _VALID_URL: %s' % url
        assert m.group('id') is not None, 'ID group should be extracted for: %s' % url

    # Verify invalid URLs do not match
    invalid_urls = [
        'http://www.tvplay.lv/',
        'http://play.tv3.lt/programos/moterys-meluoja-geriau/',
        'http://www.example.com/program/foo/12345',
        'mtg:',
        'http://play.novatv.bg/programi/zdravei-bulgariya/notanid',
    ]
    for url in invalid_urls:
        assert re.match(ie._VALID_URL, url) is None, \
            'URL should NOT match _VALID_URL: %s' % url

    # Verify extracted IDs for representative URLs
    m = re.match(ie._VALID_URL, 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert m.group('id') == '418113'
    m = re.match(ie._VALID_URL, 'mtg:418113')
    assert m.group('id') == '418113'

    # Verify _TESTS suite is defined and non-empty
    assert isinstance(ie._TESTS, list)
    assert len(ie._TESTS) > 0
    for test in ie._TESTS:
        assert 'url' in test

    # Verify geo_bypass related state initialized properly
    assert ie._downloader is None or ie._downloader is not None  # attribute exists
    assert ie.GEO_COUNTRIES is None or isinstance(ie.GEO_COUNTRIES, (list, type(None)))

# Generated at 2026-11-02 12:59:32.661714
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Constructor should create a valid instance
    ie = ViafreeIE()
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # suitable() should accept valid viafree URLs
    assert ViafreeIE.suitable(
        'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ViafreeIE.suitable(
        'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    assert ViafreeIE.suitable(
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # suitable() should reject URLs already handled by TVPlayIE
    assert not ViafreeIE.suitable(
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert not ViafreeIE.suitable(
        'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')

    # suitable() should reject non-matching URLs
    assert not ViafreeIE.suitable('http://www.example.com/program/foo')
    assert not ViafreeIE.suitable('https://viafree.us/program/underholdning/show/episode-1')

# Generated at 2026-11-02 13:01:26.695279
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    # Constructor should produce an instance of ViafreeIE / InfoExtractor
    assert ie is not None
    assert isinstance(ie, ViafreeIE)

    # Class-level attributes should be initialized as expected
    assert ViafreeIE._GEO_BYPASS is False
    assert 'viafree' in ViafreeIE._VALID_URL
    assert isinstance(ViafreeIE._TESTS, list) and len(ViafreeIE._TESTS) > 0

    # suitable() should accept viafree URLs
    assert ViafreeIE.suitable(
        'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ViafreeIE.suitable(
        'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')
    assert ViafreeIE.suitable(
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # suitable() should reject URLs already claimed by TVPlayIE
    assert not ViafreeIE.suitable(
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert not ViafreeIE.suitable(
        'http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert not ViafreeIE.suitable('mtg:418113')