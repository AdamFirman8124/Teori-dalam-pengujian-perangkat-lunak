

# Generated at 2026-11-01 21:05:44.149583
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Constructor should create a valid instance without a downloader
    ie = ViafreeIE()
    assert ie is not None
    assert isinstance(ie, ViafreeIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes
    assert ViafreeIE._GEO_BYPASS is False
    assert ViafreeIE._ENABLED is True
    assert 'viafree' in ViafreeIE._VALID_URL

    # _VALID_URL should match viafree URLs and capture country/path groups
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    match = re.match(ViafreeIE._VALID_URL, url)
    assert match is not None
    assert match.group('country') == 'no'
    assert match.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    match_se = re.match(ViafreeIE._VALID_URL, 'https://viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    assert match_se is not None
    assert match_se.group('country') == 'se'

    # suitable() should accept viafree URLs for all supported countries
    assert ViafreeIE.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1') is True
    assert ViafreeIE.suitable('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1') is True
    assert ViafreeIE.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5') is True

    # suitable() should reject URLs that are handled by TVPlayIE
    assert ViafreeIE.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true') is False
    assert ViafreeIE.suitable('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true') is False
    assert ViafreeIE.suitable('mtg:418113') is False

    # suitable() should reject non-viafree, non-tvplay URLs
    assert ViafreeIE.suitable('http://www.example.com/program/some-show') is False
    assert ViafreeIE.suitable('not a url at all') is False

# Generated at 2026-11-01 21:06:24.486478
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    '''
    Test the constructor of class ViafreeIE.
    '''
    # Constructor should create a usable instance without arguments
    ie = ViafreeIE()
    assert ie is not None

    # Class-level attributes defined on ViafreeIE should be present
    assert ie._GEO_BYPASS is False
    assert ie._VALID_URL is not None

    # The instance should expose inherited InfoExtractor functionality
    assert hasattr(ie, '_download_json')
    assert hasattr(ie, '_extract_m3u8_formats')
    assert callable(ie.geo_verification_headers)

    # The suitable() classmethod must accept viafree URLs
    # but reject URLs already handled by TVPlayIE
    viafree_url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    tvplay_url = 'http://www.tv3play.se/program/husraddarna/395385?autostart=true'

    assert ViafreeIE.suitable(viafree_url) is True
    assert ViafreeIE.suitable(tvplay_url) is False

# Generated at 2026-11-01 21:06:54.088479
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Constructor should work without any arguments and produce a usable instance
    ie = TVPlayHomeIE()

    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)
    assert ie.IE_NAME == 'TVPlayHomeIE'
    assert ie._downloader is None

    # Class-level attributes should be present after construction
    assert hasattr(TVPlayHomeIE, '_VALID_URL')
    assert isinstance(TVPlayHomeIE._VALID_URL, str)

    # All documented URL variants should be recognized by suitable()
    urls = [
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/',
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/',
        'https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/',
        'https://play.tv3.lt/aferistai-10047125',
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317',
        'https://play.tv3.ee/cool-d-ga-mehhikosse-10044354',
    ]
    for url in urls:
        assert TVPlayHomeIE.suitable(url), 'suitable() failed for %s' % url

    # _match_id should extract the trailing numeric id from each variant
    expected_ids = [
        ('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/', '10047125'),
        ('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/', '10280317'),
        ('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/', '10044354'),
        ('https://play.tv3.lt/aferistai-10047125', '10047125'),
        ('https://tv3play.skaties.lv/vinas-melo-labak-10280317', '10280317'),
        ('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354', '10044354'),
    ]
    for url, expected_id in expected_ids:
        assert ie._match_id(url) == expected_id

# Generated at 2026-11-01 21:08:11.596735
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Constructor should create an instance without errors
    extractor = ViafreeIE()
    assert extractor is not None
    assert extractor._VALID_URL is not None
    assert extractor.GEO_BYPASS is False

    # _VALID_URL should match viafree URLs
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    assert ViafreeIE.suitable(url)
    m = re.match(ViafreeIE._VALID_URL, url)
    assert m is not None
    country, path = m.groups()
    assert country == 'no'
    assert path == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')
    assert ViafreeIE.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # suitable() must defer to TVPlayIE for tvplay-like URLs
    assert not ViafreeIE.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert not ViafreeIE.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true')

    # Non-matching URLs should not be suitable
    assert not ViafreeIE.suitable('https://example.com/video')

# Generated at 2026-11-01 21:09:17.847928
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert isinstance(ie._VALID_URL, str)
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) > 0
    # Constructor initializes working URL matcher
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'
    assert ie.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert not ie.suitable('https://example.com/watch/12345')

# Generated at 2026-11-01 21:09:47.031647
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie is not None
    assert ie._VALID_URL is not None

    # Valid URLs should match and extract the correct video id
    valid_urls = [
        ('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/', '10047125'),
        ('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/', '10280317'),
        ('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/', '10044354'),
        ('https://play.tv3.lt/aferistai-10047125', '10047125'),
        ('https://tv3play.skaties.lv/vinas-melo-labak-10280317', '10280317'),
        ('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354', '10044354'),
    ]
    for url, expected_id in valid_urls:
        assert TVPlayHomeIE.suitable(url)
        m = re.match(ie._VALID_URL, url)
        assert m is not None
        assert m.group('id') == expected_id

    # Invalid URLs should not match
    invalid_urls = [
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'https://tvplay.tv3.lt/',
        'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869',
    ]
    for url in invalid_urls:
        assert not TVPlayHomeIE.suitable(url)

# Generated at 2026-11-01 21:10:25.436877
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, TVPlayIE)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true') == '238551'
    assert ie._match_id('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869') == '676869'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('mtg:418113')
    assert not ie.suitable('http://www.example.com/video/12345')

# Generated at 2026-11-01 21:11:14.379206
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor must yield a fully initialized InfoExtractor instance
    assert isinstance(ie, TVPlayIE)
    assert isinstance(ie, InfoExtractor)

    # Class metadata defined alongside the constructor
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie._VALID_URL

    # Repeated instantiation (with optional downloader arg) should be safe
    other = TVPlayIE(downloader=None)
    assert isinstance(other, TVPlayIE)
    assert other.IE_NAME == ie.IE_NAME

    # Supported URL forms must be recognized and their ids extracted
    cases = [
        ('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true', '418113'),
        ('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true', '418113'),
        ('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true', '418113'),
        ('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true', '409229'),
        ('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true', '238551'),
        ('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true', '238551'),
        ('http://www.tv3play.se/program/husraddarna/395385?autostart=true', '395385'),
        ('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true', '266636'),
        ('http://www.tv8play.se/program/antikjakten/282756?autostart=true', '282756'),
        ('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true', '230898'),
        ('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true', '21873'),
        ('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true', '361883'),
        ('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true', '624952'),
        ('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true', '764300'),
        ('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869', '676869'),
        ('mtg:418113', '418113'),
    ]
    for url, expected_id in cases:
        assert ie.suitable(url), url
        assert ie._match_id(url) == expected_id, url

    # Unsupported URLs must not match
    for bad_url in (
        'https://example.com/video/123',
        'http://www.tvplay.lv/parraides/vinas-melo-labak/',
        'mtg:',
    ):
        assert not ie.suitable(bad_url), bad_url

# Generated at 2026-11-01 21:12:09.368453
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    '''
    Test the constructor of class ViafreeIE.
    '''
    # Instantiate the extractor (downloader argument is optional)
    ie = ViafreeIE()

    # Basic identity checks
    assert ie.ie_key() == 'Viafree'
    assert ie._GEO_BYPASS is False

    # _VALID_URL should be defined and correctly parse viafree URLs
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    m = re.match(ViafreeIE._VALID_URL, url)
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    # suitable() should accept viafree URLs ...
    assert ViafreeIE.suitable(url) is True
    assert ViafreeIE.suitable(
        'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2') is True
    assert ViafreeIE.suitable(
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5') is True

    # ... but must defer to TVPlayIE for tvplay/mtg URLs
    assert ViafreeIE.suitable(
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true') is False
    assert ViafreeIE.suitable('mtg:418113') is False

    # Non-matching URLs must be rejected
    assert ViafreeIE.suitable('https://www.youtube.com/watch?v=BaW_jenozKc') is False

    # Test suite must be attached to the class
    assert isinstance(ViafreeIE._TESTS, list)
    assert len(ViafreeIE._TESTS) == 5

# Generated at 2026-11-01 21:12:55.350174
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Instance should be created successfully and inherit from InfoExtractor
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _match_id should extract the numeric id from supported URL forms
    urls_and_ids = [
        ('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true', '418113'),
        ('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true', '409229'),
        ('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true', '238551'),
        ('http://www.tv3play.se/program/husraddarna/395385?autostart=true', '395385'),
        ('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true', '266636'),
        ('http://www.tv8play.se/program/antikjakten/282756?autostart=true', '282756'),
        ('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true', '230898'),
        ('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true', '21873'),
        ('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true', '361883'),
        ('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true', '624952'),
        ('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true', '764300'),
        ('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true', '418113'),
        ('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true', '418113'),
        ('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true', '238551'),
        ('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869', '676869'),
        ('mtg:418113', '418113'),
    ]
    for url, expected_id in urls_and_ids:
        assert ie._match_id(url) == expected_id, \
            '_match_id failed for URL: %s' % url

    # Non-matching URLs should not be suitable
    unsuitable_urls = [
        'https://www.youtube.com/watch?v=BaW_jenozKc',
        'http://example.com/video/12345',
    ]
    for url in unsuitable_urls:
        assert not ie.suitable(url), \
            'suitable() unexpectedly matched URL: %s' % url

# Generated at 2026-11-01 21:13:47.467367
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Constructor can be instantiated without a downloader
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)

    # ViafreeIE claims its own URLs
    assert ViafreeIE.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ViafreeIE.suitable('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    assert ViafreeIE.suitable('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')
    assert ViafreeIE.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # ViafreeIE must NOT claim TVPlayIE URLs (suitable() defers to TVPlayIE)
    assert not ViafreeIE.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert not ViafreeIE.suitable('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true')
    assert not ViafreeIE.suitable('http://www.tv8play.se/program/antikjakten/282756?autostart=true')
    assert not ViafreeIE.suitable('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true')
    assert not ViafreeIE.suitable('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true')
    assert not ViafreeIE.suitable('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true')
    assert not ViafreeIE.suitable('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true')
    assert not ViafreeIE.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true')
    assert not ViafreeIE.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert not ViafreeIE.suitable('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert not ViafreeIE.suitable('mtg:418113')

    # Unrelated URLs are not suitable
    assert not ViafreeIE.suitable('http://www.viafree.com/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert not ViafreeIE.suitable('https://example.com/programmer/reality/paradise-hotel')
    assert not ViafreeIE.suitable('http://www.viafree.se/some/other/path')

# Generated at 2026-11-01 21:14:50.755943
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Constructor takes no arguments and initializes base state
    ie = TVPlayHomeIE()

    # Instance is a proper InfoExtractor
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # Class-level attributes are accessible from the instance
    assert ie.ie_key() == 'TVPlayHome'
    assert ie.ie_id() == 'TVPlayHome'

    expected_valid_url = r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie._VALID_URL == expected_valid_url

    # _TESTS is a non-empty list of test dicts
    assert isinstance(TVPlayHomeIE._TESTS, list)
    assert len(TVPlayHomeIE._TESTS) > 0
    for test in TVPlayHomeIE._TESTS:
        assert 'url' in test

    # suitable() accepts known URL forms
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert TVPlayHomeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125')
    assert TVPlayHomeIE.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert TVPlayHomeIE.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')

    # suitable() rejects URLs from other sites
    assert not TVPlayHomeIE.suitable('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883')
    assert not TVPlayHomeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert not TVPlayHomeIE.suitable('mtg:418113')

    # _match_id extracts the numeric id correctly
    assert ie._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert ie._match_id('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/') == '10280317'
    assert ie._match_id('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/') == '10044354'
    assert ie._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'

    # Each fresh instance gets its own (empty) cache
    ie2 = TVPlayHomeIE()
    assert ie2 is not ie
    assert ie._cache is not ie2._cache